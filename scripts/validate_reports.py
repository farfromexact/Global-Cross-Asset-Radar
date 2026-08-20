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
ARCHIVE_POLICY_PATH = ROOT / "config" / "archive-policy.json"

# Keep these checks strict. ChatGPT/private connector citation tokens are not
# portable Markdown and render as garbage outside the chat UI.
FORBIDDEN_REFERENCE_PATTERNS = [
    re.compile(r"(?:filecite|cite|memcite)"),
    re.compile(r"\bturn\d+(?:search|file|news|view|fetch|product|finance|sports|forecast)\d+\b"),
    re.compile(r"\bconnector_[A-Za-z0-9_-]+\b"),
]

class ValidationFailure(Exception):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationFailure(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc


def configured_editions(policy: Any) -> tuple[str, ...]:
    editions = policy.get("editions") if isinstance(policy, dict) else None
    if not isinstance(editions, dict) or not editions:
        raise ValidationFailure("config/archive-policy.json must define a non-empty editions object")

    invalid = [edition for edition, value in editions.items() if not isinstance(edition, str) or not isinstance(value, dict)]
    if invalid:
        raise ValidationFailure("config/archive-policy.json has an invalid editions object")
    return tuple(editions)


def historical_report_pattern(allowed_editions: tuple[str, ...]) -> re.Pattern[str]:
    choices = "|".join(re.escape(edition) for edition in allowed_editions)
    return re.compile(rf"^(\d{{4}}-\d{{2}}-\d{{2}})_({choices})\.json$")


def is_report_test_name(path: Path, allowed_editions: tuple[str, ...]) -> bool:
    return any(path.name.endswith(f"_{edition}.json") for edition in allowed_editions)


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


def report_paths(allowed_editions: tuple[str, ...]) -> list[Path]:
    paths = list((ROOT / "latest").glob("*.json"))
    paths.extend((ROOT / "reports").glob("**/*.json"))
    if (ROOT / "tests").exists():
        paths.extend(
            path
            for path in (ROOT / "tests").glob("**/*.json")
            if is_report_test_name(path, allowed_editions)
        )
    return sorted(set(paths))


def _compat_title(data: dict[str, Any]) -> str:
    edition = data.get("edition")
    labels = {
        "morning": ("全球跨资产高风险机会雷达", "晨间版"),
        "evening": ("全球跨资产高风险机会雷达", "晚间版"),
        "commodities_morning": ("全球商品期货期权高风险机会雷达", "晨间版"),
        "commodities_evening": ("全球商品期货期权高风险机会雷达", "晚间版"),
    }
    title, edition_label = labels.get(edition, ("全球跨资产高风险机会雷达", "未分类版"))
    return f"{title}｜{edition_label}｜{data.get('report_date') or 'undated'}"


def _compat_sources(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []

    normalized: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            source = dict(item)
            # The commodity Scheduled Tasks historically used ``name`` or
            # ``publisher`` and ``date``.  Keep those fields, but expose the
            # canonical archive keys to the schema validator as well.
            title = source.get("title") or source.get("name") or source.get("publisher") or source.get("url")
            source["title"] = str(title or "unspecified source")
            if "source_date" not in source and "date" in source:
                source["source_date"] = source.get("date")
            normalized.append(source)
        elif isinstance(item, str):
            normalized.append({"title": item})
        else:
            normalized.append({"title": str(item)})
    return normalized


def _compat_curve_definition(value: Any) -> Any:
    """Map the human wording used by the commodity task to the contract label."""
    if not isinstance(value, str):
        return value
    canonical = "near_minus_next_futures_curve_not_spot_basis"
    if value == canonical:
        return value
    lowered = value.lower()
    if "curve" in lowered and "spot" in lowered and ("near" in lowered or "next" in lowered):
        return canonical
    return value


def _compat_contract_from_text(product: str, text: str) -> str | None:
    product = product.strip().upper()
    if not product:
        return None
    # Chinese reports commonly write FU2611/JM2701/FG701 inline in cards.
    # This is only a best-effort identity recovery; if no symbol is present we
    # retain an explicit N/A sentinel rather than inventing a contract.
    match = re.search(rf"\b{re.escape(product)}[A-Z]?\d{{3,6}}\b", text.upper())
    return match.group(0) if match else None


def _compat_market_dashboard(value: Any, data: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []

    text = json.dumps(data, ensure_ascii=False, sort_keys=True)
    normalized: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        row = dict(item)
        product = row.get("product") or row.get("asset") or row.get("symbol") or "UNKNOWN"
        row["product"] = str(product)
        contract = row.get("main_contract") or row.get("contract") or row.get("main") or row.get("symbol")
        if not isinstance(contract, str) or not contract.strip():
            contract = _compat_contract_from_text(str(product), json.dumps(row, ensure_ascii=False))
        if not contract:
            contract = _compat_contract_from_text(str(product), text) or "N/A"
        row["main_contract"] = contract
        normalized.append(row)
    return normalized


def _compat_dashboard(value: Any, market_dashboard: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Build the generic dashboard required by the shared report schema."""
    source = value if isinstance(value, list) and value else market_dashboard
    normalized: list[dict[str, Any]] = []
    for item in source:
        if not isinstance(item, dict):
            continue
        row = dict(item)
        row.setdefault("asset", row.get("product") or row.get("symbol") or "UNKNOWN")
        normalized.append(row)
    return normalized


def _compat_archive(data: dict[str, Any], path: Path) -> dict[str, Any]:
    archive = dict(data.get("archive")) if isinstance(data.get("archive"), dict) else {}
    if "reports" in path.parts:
        json_path = path.relative_to(ROOT).as_posix()
        markdown_path = path.with_suffix(".md").relative_to(ROOT).as_posix()
    else:
        json_path = None
        markdown_path = None
    archive.setdefault("json_path", json_path)
    archive.setdefault("markdown_path", markdown_path)
    archive.setdefault("latest_json_path", f"latest/{data.get('edition')}.json")
    archive.setdefault("latest_markdown_path", f"latest/{data.get('edition')}.md")
    archive_status = archive.get("archive_status", data.get("archive_status"))
    if archive_status == "pending_verification":
        archive_status = "pending"
    archive["archive_status"] = archive_status
    return archive


def _normalize_commodity_schedule_report(data: dict[str, Any], path: Path) -> dict[str, Any]:
    """Adapt the existing commodity task dialect without changing its prompt.

    The external Scheduled Tasks already publish useful commodity content, but
    their JSON uses a compact dialect (``name``/``date`` sources, no generic
    dashboard, and descriptive curve labels).  Keep the raw fields and add a
    canonical in-memory view for validation.  Missing contracts become an
    explicit ``N/A`` rather than a fabricated symbol.
    """
    if data.get("edition") not in {"commodities_morning", "commodities_evening"}:
        return data

    normalized = dict(data)
    normalized.setdefault("generated_at_bjt", data.get("generated_at"))
    normalized.setdefault("title", _compat_title(data))
    normalized.setdefault(
        "one_sentence_conclusion",
        data.get("one_sentence") or data.get("commodity_regime") or data.get("regime"),
    )
    normalized.setdefault("source_status", {
        "compatibility_adapter": "commodity_schedule_dialect",
        "data_fresh": data.get("data_fresh"),
        "errors": data.get("errors", []),
    })
    normalized.setdefault("meaningful_changes", [])
    normalized.setdefault("top_opportunities", [])
    normalized.setdefault("top_trade_cards", data.get("trade_cards", []))
    normalized.setdefault("gold_tracking", {})
    normalized.setdefault("ai_tracking", {})
    normalized.setdefault("china_tracking", {})
    normalized.setdefault("event_calendar", [])
    normalized.setdefault("action_list", {"A": "", "B": "", "C": "", "D": ""})
    normalized.setdefault("risk_budget", {})

    tracking = dict(data.get("commodities_tracking")) if isinstance(data.get("commodities_tracking"), dict) else {}
    quality = dict(tracking.get("data_quality")) if isinstance(tracking.get("data_quality"), dict) else {}
    quality["curve_definition"] = _compat_curve_definition(quality.get("curve_definition"))
    tracking["data_quality"] = quality
    market_dashboard = _compat_market_dashboard(tracking.get("market_dashboard"), data)
    tracking["market_dashboard"] = market_dashboard
    normalized["commodities_tracking"] = tracking
    normalized["dashboard"] = _compat_dashboard(data.get("dashboard"), market_dashboard)
    normalized["meaningful_changes"] = data.get("meaningful_changes") or quality.get("comparative_metrics", [])
    normalized["sources"] = _compat_sources(data.get("sources"))
    normalized["archive"] = _compat_archive(data, path)
    return normalized


def _compat_status(data: dict[str, Any], path: Path) -> str:
    status = data.get("status")
    if status in {"published", "archive_failed", "not_published"}:
        return status

    archive_status = data.get("archive_status")
    if archive_status in {"failed", "archive_failed"}:
        return "archive_failed"

    if "reports" in path.parts or "latest" in path.parts:
        return "published"
    return "not_published"


def _compat_china_tracking(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}

    normalized = dict(value)
    preferred = normalized.get("preferred_future")
    if isinstance(preferred, str):
        upper = preferred.upper().strip()
        match = re.match(r"^(IH|IF|IC|IM)\b", upper)
        if not match:
            match = re.search(r"\b(IH|IF|IC|IM)\b", upper)
        normalized["preferred_future"] = match.group(1) if match else None
    return normalized


def normalize_report_for_schema(data: Any, path: Path) -> Any:
    """Normalize report dialects into the canonical schema for validation.

    Compatibility is intentionally permissive for compact/renamed summary
    fields and descriptive labels, while identity, paired files, manifest links,
    JSON validity and portable citations remain strict.
    """
    if not isinstance(data, dict):
        return data

    normalized = dict(data)

    normalized = _normalize_commodity_schedule_report(normalized, path)

    if data.get("schema_version") == "1.1":
        normalized["schema_version"] = "1.0"
        normalized.setdefault("status", _compat_status(data, path))
        normalized.setdefault("generated_at_bjt", data.get("generated_at"))
        normalized.setdefault("title", _compat_title(data))
        normalized.setdefault(
            "one_sentence_conclusion",
            data.get("one_line_conclusion") or data.get("one_sentence") or None,
        )
        normalized.setdefault("regime", data.get("market_regime"))
        normalized.setdefault("worth_taking_risk", data.get("worth_taking_risk"))
        normalized.setdefault(
            "input_snapshots",
            {
                "china_options_repository": "farfromexact/China-Options-Engine",
                "china_options_path": "data/radar_latest.json",
                "china_options_history_path": "data/radar_history.json",
                "china_options_date": data.get("china_options_date"),
                "china_options_fresh": data.get("data_fresh"),
                "actual_read_paths": data.get("china_options_engine_actual_read_paths")
                or data.get("China-Options-Engine实际读取路径")
                or [],
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
        normalized.setdefault("top_opportunities", [])
        normalized.setdefault("top_trade_cards", data.get("trade_cards", []))
        normalized.setdefault("gold_tracking", {})
        normalized.setdefault("ai_tracking", {})
        normalized.setdefault("event_calendar", [])
        normalized.setdefault("action_list", {"A": "", "B": "", "C": "", "D": ""})
        normalized.setdefault("risk_budget", {})
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
                "commit_sha": data.get("archive_verification_source_commit_sha")
                or data.get("publication_commit_sha"),
                "error": error_text,
            },
        )

    # Apply harmless descriptive-label normalization to every schema version.
    normalized["china_tracking"] = _compat_china_tracking(normalized.get("china_tracking", {}))
    return normalized


def normalize_manifest_for_schema(data: Any) -> Any:
    if not isinstance(data, dict) or data.get("schema_version") != "1.1":
        return data

    normalized = dict(data)
    normalized["schema_version"] = "1.0"

    reports = []
    for item in data.get("reports", []):
        if not isinstance(item, dict):
            reports.append(item)
            continue
        compat_item = dict(item)
        if compat_item.get("status") == "publishing":
            compat_item["status"] = "partial"
        reports.append(compat_item)
    normalized["reports"] = reports
    return normalized


def _contains_unavailable_option_metric(value: Any, path: tuple[str, ...] = ()) -> list[str]:
    """Find machine-readable IV/skew/Gamma/strike fields behind a closed gate.

    Textual research priorities are allowed (they describe future collection),
    but a structured result with one of these field names would be interpreted
    as a collected metric or executable option instruction.
    """
    blocked = re.compile(
        r"(?:^|_)(?:atm_?iv|iv|skew|rr(?:_?25|_?10)?|bf(?:_?25)?|pcr|gamma(?:_.*)?|strike)(?:_|$)",
        re.IGNORECASE,
    )
    allowed_field_names = {
        "options_chain_status",
        "options_surface_status",
        # Coverage metadata is not a tradable IV/skew/Gamma metric.  The
        # commodity task may report how much of the chain had vendor Greeks
        # even while the execution surface remains closed.
        "iv_coverage",
        "vendor_greeks_coverage",
        "expiry_coverage",
        "bid_ask_coverage",
        "open_interest_coverage",
        "available_metrics",
        "tradeable_structures",
        "research_priority_when_ready",
    }
    found: list[str] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            key_text = str(key)
            next_path = (*path, key_text)
            if key_text not in allowed_field_names and blocked.search(key_text):
                found.append(".".join(next_path))
            found.extend(_contains_unavailable_option_metric(nested, next_path))
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            found.extend(_contains_unavailable_option_metric(nested, (*path, str(index))))
    return found


def validate_commodity_contract(
    data: Any,
    path: Path,
    allowed_editions: tuple[str, ...],
) -> list[str]:
    if not isinstance(data, dict):
        return []
    edition = data.get("edition")
    if edition not in allowed_editions or not isinstance(edition, str) or not edition.startswith("commodities_"):
        return []
    if data.get("status") != "published":
        return []

    messages: list[str] = []
    tracking = data.get("commodities_tracking")
    if not isinstance(tracking, dict):
        return messages

    quality = tracking.get("data_quality")
    if isinstance(quality, dict) and quality.get("history_comparison_status") == "insufficient_history":
        if quality.get("available_horizons"):
            messages.append(
                f"{path.relative_to(ROOT)} declares comparison horizons despite insufficient commodity history"
            )
        if quality.get("comparative_metrics"):
            messages.append(
                f"{path.relative_to(ROOT)} declares comparative metrics despite insufficient commodity history"
            )

    options_surface = tracking.get("options_surface")
    options_fields = options_surface if isinstance(options_surface, dict) else {}
    chain_ready = isinstance(quality, dict) and quality.get("options_chain_status") == "ready"
    surface_ready = isinstance(options_surface, dict) and options_surface.get("status") == "ready"
    if not chain_ready or not surface_ready:
        if options_fields.get("available_metrics"):
            messages.append(
                f"{path.relative_to(ROOT)} exposes commodity option metrics while the commodity option gate is not ready"
            )
        if options_fields.get("tradeable_structures"):
            messages.append(
                f"{path.relative_to(ROOT)} exposes commodity option trade structures while the commodity option gate is not ready"
            )
        metric_paths = _contains_unavailable_option_metric(data.get("commodities_tracking"), ("commodities_tracking",))
        if metric_paths:
            messages.append(
                f"{path.relative_to(ROOT)} exposes commodity IV/skew/Gamma/strike fields while the commodity option gate is not ready: "
                + ", ".join(metric_paths)
            )
    return messages


def validate_markdown_pairs(allowed_editions: tuple[str, ...], policy: dict[str, Any]) -> list[str]:
    """Require the Markdown/JSON side of every configured archive pair."""
    messages: list[str] = []
    choices = "|".join(re.escape(edition) for edition in allowed_editions)
    markdown_pattern = re.compile(rf"^\d{{4}}-\d{{2}}-\d{{2}}_(?:{choices})\.md$")

    for markdown_path in sorted((ROOT / "reports").glob("**/*.md")):
        if markdown_pattern.fullmatch(markdown_path.name) and not markdown_path.with_suffix(".json").exists():
            messages.append(
                f"Missing JSON pair for {markdown_path.relative_to(ROOT)}: "
                f"{markdown_path.with_suffix('.json').relative_to(ROOT)}"
            )

    editions = policy.get("editions", {})
    if isinstance(editions, dict):
        for edition in allowed_editions:
            configured = editions.get(edition, {})
            markdown_rel = configured.get("latest_markdown") if isinstance(configured, dict) else None
            json_rel = configured.get("latest_json") if isinstance(configured, dict) else None
            if not isinstance(markdown_rel, str) or not isinstance(json_rel, str):
                continue
            markdown_path = ROOT / markdown_rel
            json_path = ROOT / json_rel
            if markdown_path.exists() != json_path.exists():
                missing = json_path if markdown_path.exists() else markdown_path
                present = markdown_path if markdown_path.exists() else json_path
                messages.append(
                    f"Missing latest pair for edition {edition}: {missing.relative_to(ROOT)} "
                    f"(paired with {present.relative_to(ROOT)})"
                )
    return messages


def validate_report_file(
    path: Path,
    schema: dict[str, Any],
    allowed_editions: tuple[str, ...],
) -> list[str]:
    original_data = load_json(path)
    data = normalize_report_for_schema(original_data, path)
    messages = validate_json_schema(data, schema, path)

    status = data.get("status") if isinstance(data, dict) else None
    edition = data.get("edition") if isinstance(data, dict) else None
    report_date = data.get("report_date") if isinstance(data, dict) else None

    if "reports" in path.parts:
        pattern = historical_report_pattern(allowed_editions)
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
        if edition not in allowed_editions:
            messages.append(
                f"{path.relative_to(ROOT)} edition={edition!r} is not configured in archive-policy.json"
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
    messages.extend(validate_commodity_contract(data, path, allowed_editions))
    return messages


def validate_manifest(schema: dict[str, Any], allowed_editions: tuple[str, ...]) -> list[str]:
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

        if entry.get("edition") not in allowed_editions:
            messages.append(
                f"Manifest entry {key} uses an edition not configured in archive-policy.json"
            )

        for field in ("markdown_path", "json_path"):
            value = entry.get(field)
            if value and not (ROOT / value).exists():
                messages.append(f"Manifest entry {key} references missing {field}: {value}")

    messages.extend(scan_forbidden_tokens(MANIFEST_PATH))
    return messages


def main() -> int:
    report_schema = load_json(REPORT_SCHEMA_PATH)
    manifest_schema = load_json(MANIFEST_SCHEMA_PATH)
    archive_policy = load_json(ARCHIVE_POLICY_PATH)
    allowed_editions = configured_editions(archive_policy)

    errors: list[str] = []
    for path in report_paths(allowed_editions):
        errors.extend(validate_report_file(path, report_schema, allowed_editions))
    errors.extend(validate_markdown_pairs(allowed_editions, archive_policy))
    errors.extend(validate_manifest(manifest_schema, allowed_editions))

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
