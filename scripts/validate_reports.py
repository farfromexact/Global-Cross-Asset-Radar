from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REPORT_SCHEMA_PATH = ROOT / "schemas" / "report.schema.json"
MANIFEST_SCHEMA_PATH = ROOT / "schemas" / "manifest.schema.json"
MANIFEST_PATH = ROOT / "manifests" / "reports.json"

FORBIDDEN_REFERENCE_PATTERNS = [
    re.compile(r"(?:filecite|cite|memcite)"),
    re.compile(r"\bturn\d+(?:search|file|news|view|fetch|product|finance|sports|forecast)\d+\b"),
    re.compile(r"\bconnector_[A-Za-z0-9_-]+\b"),
]

REPORT_TEST_NAME = re.compile(r"_(morning|evening)\.json$")


class ValidationFailure(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationFailure(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc


def validate_json_schema(data: Any, schema: dict[str, Any], path: Path) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    messages: list[str] = []
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{path.relative_to(ROOT)} [{location}]: {error.message}")
    return messages


def scan_forbidden_tokens(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    messages: list[str] = []
    for pattern in FORBIDDEN_REFERENCE_PATTERNS:
        match = pattern.search(text)
        if match:
            messages.append(
                f"{path.relative_to(ROOT)} contains non-portable/private citation token: {match.group(0)}"
            )
    return messages


def report_paths() -> list[Path]:
    paths = list((ROOT / "latest").glob("*.json"))
    paths.extend((ROOT / "reports").glob("**/*.json"))
    if (ROOT / "tests").exists():
        # The tests tree also contains operational smoke-status JSON files. Only
        # files ending in _morning.json or _evening.json are report fixtures and
        # should be validated against the full report schema.
        paths.extend(
            path
            for path in (ROOT / "tests").glob("**/*.json")
            if REPORT_TEST_NAME.search(path.name)
        )
    return sorted(set(paths))


def _compat_title(data: dict[str, Any]) -> str:
    edition_label = "晨间版" if data.get("edition") == "morning" else "晚间版"
    return f"全球跨资产高风险机会雷达｜{edition_label}｜{data.get('report_date') or 'undated'}"


def _compat_sources(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []

    normalized: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict) and isinstance(item.get("title"), str):
            normalized.append(item)
        elif isinstance(item, str):
            normalized.append({"title": item})
        else:
            normalized.append({"title": str(item)})
    return normalized


def normalize_report_for_schema(data: Any, path: Path) -> Any:
    """Map the compact 1.1 archive dialect onto the canonical 1.0 schema.

    The repository contains reports produced by both archive writers. Validation
    remains strict on filenames, manifest links and portable citations; this
    adapter only reconciles renamed/compacted JSON fields.
    """
    if not isinstance(data, dict) or data.get("schema_version") != "1.1":
        return data

    normalized = dict(data)
    normalized["schema_version"] = "1.0"
    normalized.setdefault("generated_at_bjt", data.get("generated_at"))
    normalized.setdefault("title", _compat_title(data))
    normalized.setdefault("regime", data.get("market_regime"))
    normalized.setdefault(
        "input_snapshots",
        {
            "china_options_repository": "farfromexact/China-Options-Engine",
            "china_options_path": "data/radar_latest.json",
            "china_options_history_path": "data/radar_history.json",
            "china_options_date": data.get("china_options_date"),
            "china_options_fresh": data.get("data_fresh"),
            "actual_read_paths": data.get("china_options_engine_actual_read_paths", []),
        },
    )
    normalized.setdefault(
        "source_status",
        {
            "compatibility_adapter": "schema_version_1.1",
            "errors": data.get("errors", []),
        },
    )
    normalized.setdefault("dashboard", [])
    normalized.setdefault("meaningful_changes", [])
    normalized.setdefault("top_trade_cards", data.get("trade_cards", []))
    normalized.setdefault("gold_tracking", {})
    normalized.setdefault("ai_tracking", {})
    normalized.setdefault("event_calendar", [])
    normalized["sources"] = _compat_sources(data.get("sources"))

    if "reports" in path.parts:
        json_path = path.relative_to(ROOT).as_posix()
        markdown_path = path.with_suffix(".md").relative_to(ROOT).as_posix()
    else:
        json_path = None
        markdown_path = None

    errors = data.get("errors")
    error_text = "; ".join(str(item) for item in errors) if isinstance(errors, list) and errors else None
    normalized.setdefault(
        "archive",
        {
            "markdown_path": markdown_path,
            "json_path": json_path,
            "latest_markdown_path": f"latest/{data.get('edition')}.md",
            "latest_json_path": f"latest/{data.get('edition')}.json",
            "archive_status": data.get("archive_status"),
            "commit_sha": data.get("archive_verification_source_commit_sha"),
            "error": error_text,
        },
    )
    return normalized


def normalize_manifest_for_schema(data: Any) -> Any:
    if not isinstance(data, dict) or data.get("schema_version") != "1.1":
        return data
    normalized = dict(data)
    normalized["schema_version"] = "1.0"
    return normalized


def validate_report_file(path: Path, schema: dict[str, Any]) -> list[str]:
    original_data = load_json(path)
    data = normalize_report_for_schema(original_data, path)
    messages = validate_json_schema(data, schema, path)

    status = data.get("status") if isinstance(data, dict) else None
    edition = data.get("edition") if isinstance(data, dict) else None
    report_date = data.get("report_date") if isinstance(data, dict) else None

    if "reports" in path.parts:
        pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})_(morning|evening)\.json$")
        match = pattern.fullmatch(path.name)
        if not match:
            messages.append(f"Historical report filename is invalid: {path.relative_to(ROOT)}")
        else:
            filename_date, filename_edition = match.groups()
            if report_date != filename_date:
                messages.append(
                    f"{path.relative_to(ROOT)} report_date={report_date!r} does not match filename date {filename_date}"
                )
            if edition != filename_edition:
                messages.append(
                    f"{path.relative_to(ROOT)} edition={edition!r} does not match filename edition {filename_edition}"
                )
        if status not in {"published", "archive_failed"}:
            messages.append(
                f"Historical report must be published or archive_failed: {path.relative_to(ROOT)}"
            )

    markdown_path = path.with_suffix(".md")
    if "reports" in path.parts or "tests" in path.parts:
        if not markdown_path.exists():
            messages.append(
                f"Missing Markdown pair for {path.relative_to(ROOT)}: {markdown_path.relative_to(ROOT)}"
            )

    if status == "published":
        archive = data.get("archive", {})
        expected_json = archive.get("json_path")
        expected_md = archive.get("markdown_path")
        archive_paths = set(archive.get("paths") or [])
        if "reports" in path.parts:
            rel_json = path.relative_to(ROOT).as_posix()
            rel_md = markdown_path.relative_to(ROOT).as_posix()
            if expected_json != rel_json and rel_json not in archive_paths:
                messages.append(
                    f"{path.relative_to(ROOT)} archive.json_path={expected_json!r}; expected {rel_json!r} or inclusion in archive.paths"
                )
            if expected_md != rel_md and rel_md not in archive_paths:
                messages.append(
                    f"{path.relative_to(ROOT)} archive.markdown_path={expected_md!r}; expected {rel_md!r} or inclusion in archive.paths"
                )

    messages.extend(scan_forbidden_tokens(path))
    if markdown_path.exists():
        messages.extend(scan_forbidden_tokens(markdown_path))
    return messages


def validate_manifest(schema: dict[str, Any]) -> list[str]:
    if not MANIFEST_PATH.exists():
        return ["Missing manifests/reports.json"]

    original_data = load_json(MANIFEST_PATH)
    data = normalize_manifest_for_schema(original_data)
    messages = validate_json_schema(data, schema, MANIFEST_PATH)
    keys: set[tuple[str, str]] = set()

    entries = original_data.get("reports", []) if isinstance(original_data, dict) else []
    for index, entry in enumerate(entries):
        key = (entry.get("report_date"), entry.get("edition"))
        if key in keys:
            messages.append(f"Duplicate manifest key at index {index}: {key}")
        keys.add(key)

        for field in ("markdown_path", "json_path"):
            value = entry.get(field)
            if value and not (ROOT / value).exists():
                messages.append(f"Manifest entry {key} references missing {field}: {value}")

    messages.extend(scan_forbidden_tokens(MANIFEST_PATH))
    return messages


def main() -> int:
    report_schema = load_json(REPORT_SCHEMA_PATH)
    manifest_schema = load_json(MANIFEST_SCHEMA_PATH)

    errors: list[str] = []
    for path in report_paths():
        errors.extend(validate_report_file(path, report_schema))
    errors.extend(validate_manifest(manifest_schema))

    for path in sorted((ROOT / "status").glob("*.json")):
        try:
            load_json(path)
        except ValidationFailure as exc:
            errors.append(str(exc))
        errors.extend(scan_forbidden_tokens(path))

    if errors:
        print("Report archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Report archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
