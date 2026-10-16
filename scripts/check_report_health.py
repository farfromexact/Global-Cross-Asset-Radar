"""Practical daily checks: unreadable current reports block, editorial drift does not.

The original schema/Markdown validators remain available for opt-in strict audits.
This module never rewrites reports or silently upgrades their data readiness.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


class HealthCheck:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.issues: list[dict[str, str]] = []
        self.checked: set[str] = set()
        self._seen: set[tuple[str, str, str, str]] = set()

    def add(self, code: str, path: str, message: str, *, blocking: bool = False) -> None:
        severity = "error" if blocking else "warning"
        key = (severity, code, path, message)
        if key not in self._seen:
            self._seen.add(key)
            self.issues.append(dict(severity=severity, code=code, path=path, message=message))

    def path(self, relative: str, *, blocking: bool) -> Path | None:
        if not isinstance(relative, str) or not relative:
            self.add("unsafe_path", str(relative), "Expected a non-empty repository path", blocking=blocking)
            return None
        target = (self.root / relative).resolve()
        if not target.is_relative_to(self.root):
            self.add("unsafe_path", relative, "Archive path escapes the repository", blocking=blocking)
            return None
        return target

    def read_json(self, relative: str, *, blocking: bool) -> dict[str, Any] | None:
        target = self.path(relative, blocking=blocking)
        if target is None:
            return None
        self.checked.add(relative)
        try:
            value = json.loads(target.read_text(encoding="utf-8-sig"))
            if not isinstance(value, dict) or not value:
                raise ValueError("Expected a non-empty JSON object")
        except (OSError, ValueError) as exc:
            self.add("unreadable_json", relative, str(exc), blocking=blocking)
            return None
        return value

    def read_markdown(self, relative: str, *, blocking: bool) -> str | None:
        target = self.path(relative, blocking=blocking)
        if target is None:
            return None
        self.checked.add(relative)
        try:
            value = target.read_text(encoding="utf-8-sig")
            if not value.strip():
                raise ValueError("Report Markdown is empty")
        except (OSError, ValueError) as exc:
            self.add("unreadable_markdown", relative, str(exc), blocking=blocking)
            return None
        # Titles, section names, length, and citation syntax are editorial advice.
        return value.replace("\r\n", "\n").strip()

    def identity(self, data: dict[str, Any], relative: str, report_date: str,
                 edition: str, *, blocking: bool) -> None:
        for field, expected in (("report_date", report_date), ("edition", edition)):
            actual = data.get(field)
            if actual is None:
                self.add("missing_metadata", relative, f"{field} is omitted; path identifies {expected}")
            elif actual != expected:
                self.add("identity_mismatch", relative,
                         f"{field}={actual!r}; expected {expected!r}", blocking=blocking)

    def bundle(self, entry: dict[str, Any], config: dict[str, Any],
               *, blocking: bool, include_latest: bool) -> None:
        report_date, edition = entry["report_date"], entry["edition"]
        stem = f"reports/{report_date[:4]}/{report_date[5:7]}/{report_date}_{edition}"
        history_path = stem + ".json"
        history = self.read_json(history_path, blocking=blocking)
        markdown = self.read_markdown(stem + ".md", blocking=blocking)
        if history is not None:
            self.identity(history, history_path, report_date, edition, blocking=blocking)

        for field, expected in (("json_path", history_path), ("markdown_path", stem + ".md")):
            reference = entry.get(field)
            if not isinstance(reference, str) or not reference:
                self.add("manifest_metadata", "manifests/reports.json", f"{report_date}/{edition}: {field} omitted")
            elif reference != expected:
                self.add("manifest_path", "manifests/reports.json",
                         f"{report_date}/{edition}: {field}={reference!r}; expected {expected!r}",
                         blocking=blocking)

        if not include_latest:
            return
        latest_path = config.get("latest_json", f"latest/{edition}.json")
        latest_md_path = config.get("latest_markdown", f"latest/{edition}.md")
        latest = self.read_json(latest_path, blocking=blocking)
        latest_md = self.read_markdown(latest_md_path, blocking=blocking)
        status_path = config.get("status_path", f"status/{edition}_latest.json")
        status = self.read_json(status_path, blocking=False)
        if latest is not None:
            # A previous/newer latest pointer can coexist during sequential writes.
            if latest.get("edition") not in (None, edition):
                self.add("identity_mismatch", latest_path, f"Expected edition {edition!r}", blocking=blocking)
            if latest.get("report_date") != report_date:
                self.add("latest_sync", latest_path,
                         f"Latest date {latest.get('report_date')!r}; manifest date {report_date!r}")
            if history is not None and latest != history:
                self.add("latest_sync", latest_path, "Latest and historical JSON differ")
            if markdown is not None and latest_md is not None and markdown != latest_md:
                self.add("latest_sync", latest_md_path, "Latest and historical Markdown differ")
        for relative, data in ((history_path, history), (latest_path, latest),
                               (status_path, status), ("manifests/reports.json", entry)):
            if data is None:
                continue
            revision = data.get("revision")
            if revision is None or revision != entry.get("revision"):
                self.add("revision", relative, f"Optional revision={revision!r}; manifest={entry.get('revision')!r}")
            archive = data.get("archive")
            archive_status = archive.get("archive_status") if isinstance(archive, dict) else data.get("archive_status")
            if archive_status != "success":
                self.add("archive_status", relative, f"Archive state {archive_status!r}; not a readability failure")
        if status is not None and (status.get("report_date"), status.get("edition")) != (report_date, edition):
            self.add("status_sync", status_path, "Status metadata is not synchronized with the manifest")

    def load_index(self, *, blocking: bool) -> tuple[dict[str, Any], dict[tuple[str, str], dict[str, Any]]]:
        policy = self.read_json("config/archive-policy.json", blocking=True)
        editions = policy.get("editions") if policy is not None else None
        if not isinstance(editions, dict) or not editions or not all(isinstance(v, dict) for v in editions.values()):
            self.add("configuration", "config/archive-policy.json", "Expected configured editions", blocking=True)
            return {}, {}
        manifest = self.read_json("manifests/reports.json", blocking=blocking)
        if manifest is None:
            return editions, {}
        records = manifest.get("reports")
        if not isinstance(records, list) or not records:
            self.add("manifest_shape", "manifests/reports.json", "Expected a non-empty reports array", blocking=blocking)
            return editions, {}
        entries: dict[tuple[str, str], dict[str, Any]] = {}
        for index, entry in enumerate(records):
            if not isinstance(entry, dict):
                self.add("manifest_entry", "manifests/reports.json", f"Entry {index} is not an object")
                continue
            report_date, edition = entry.get("report_date"), entry.get("edition")
            try:
                date.fromisoformat(report_date)
                if edition not in editions:
                    raise ValueError("Unknown edition")
            except (TypeError, ValueError):
                self.add("manifest_entry", "manifests/reports.json", f"Entry {index}: invalid date/edition")
                continue
            key = (report_date, edition)
            if key in entries:
                self.add("duplicate_entry", "manifests/reports.json", f"Repeated key {key}")
            entries[key] = entry
        if not entries:
            self.add("manifest_shape", "manifests/reports.json", "No usable report entries", blocking=blocking)
        return editions, entries

    def current(self, base_ref: str | None = None) -> None:
        editions, entries = self.load_index(blocking=True)
        selected: dict[tuple[str, str], dict[str, Any]] = {}
        for edition, config in editions.items():
            candidates = [entry for (day, ed), entry in entries.items() if ed == edition]
            if candidates:
                newest = max(candidates, key=lambda entry: entry["report_date"])
                selected[(newest["report_date"], edition)] = newest
                self.bundle(newest, config, blocking=True, include_latest=True)
            else:
                self.add("unindexed_edition", "manifests/reports.json", f"No entry for {edition}")
            # Also check the actual latest report if it has not yet been indexed.
            latest_path = config.get("latest_json", f"latest/{edition}.json")
            latest = self.read_json(latest_path, blocking=True)
            if latest is None:
                continue
            latest_date = latest.get("report_date")
            if latest_date is None:
                self.add("missing_metadata", latest_path, "report_date omitted")
            else:
                try:
                    date.fromisoformat(latest_date)
                except (ValueError, TypeError):
                    self.add("identity_mismatch", latest_path, "Invalid report_date", blocking=True)
                    continue
                if (latest_date, edition) not in selected:
                    inferred = {"report_date": latest_date, "edition": edition}
                    self.bundle(entries.get((latest_date, edition), inferred), config,
                                blocking=True, include_latest=True)

        if not base_ref:
            return
        base = read_base_manifest(self.root, base_ref)
        if base is None:
            self.add("base_unavailable", "manifests/reports.json",
                     "Base ref unavailable; all current editions were checked")
            return
        old = {(row.get("report_date"), row.get("edition")): row
               for row in base.get("reports", []) if isinstance(row, dict)
               and isinstance(row.get("report_date"), str) and isinstance(row.get("edition"), str)}
        for key, entry in entries.items():
            if entry != old.get(key) and key not in selected:
                self.add("historical_change", "manifests/reports.json",
                         f"Historical entry changed: {key}; latest is not required to rewind")
                self.bundle(entry, editions[key[1]], blocking=False, include_latest=False)
        for key in old.keys() - entries.keys():
            self.add("removed_entry", "manifests/reports.json", f"Index entry removed: {key}")

    def audit(self) -> None:
        editions, entries = self.load_index(blocking=False)
        if not editions:
            return
        for key, entry in entries.items():
            self.bundle(entry, editions[key[1]], blocking=False, include_latest=False)
        # Include files absent from the manifest, not only indexed reports.
        for path in sorted((self.root / "reports").glob("**/*.json")):
            relative = path.relative_to(self.root).as_posix()
            data = self.read_json(relative, blocking=False)
            self.read_markdown(path.with_suffix(".md").relative_to(self.root).as_posix(), blocking=False)
            if data is not None:
                key = (data.get("report_date"), data.get("edition"))
                if all(isinstance(part, str) for part in key) and key not in entries:
                    self.add("unindexed_report", relative, f"Report {key} is not in the manifest")
        # Retain detailed schema/content findings as advice instead of deleting checks.
        validator = load_validator(self.root, "validate_reports")
        markdown = load_validator(self.root, "validate_markdown_reports")
        report_schema = validator.load_json(validator.REPORT_SCHEMA_PATH)
        for path in validator.report_paths(tuple(editions)):
            relative = path.relative_to(self.root).as_posix()
            data = self.read_json(relative, blocking=False)
            if data is None:
                continue
            try:
                messages = validator.validate_report_file(path, report_schema, tuple(editions))
            except (validator.ValidationFailure, ValueError, TypeError, AttributeError, OSError) as exc:
                # Legacy adapters assume particular data shapes. A malformed
                # old record must not abort the advisory scan of other files.
                messages = [f"Strict data check could not interpret this record: {exc}"]
            for message in messages:
                self.add("schema_or_content", relative, message)
            day, edition = data.get("report_date"), data.get("edition")
            if (isinstance(day, str) and day >= markdown.MIN_FULL_MARKDOWN_DATE
                    and isinstance(edition, str) and edition in editions):
                try:
                    messages = markdown.validate_full_markdown(path.with_suffix(".md"), day, edition)
                except OSError as exc:
                    messages = [str(exc)]
                for message in messages:
                    self.add("markdown_style", relative, message)
        for path in sorted((self.root / "reports").glob("**/*.md")):
            if not path.with_suffix(".json").exists():
                self.add("missing_json_pair", path.relative_to(self.root).as_posix(),
                         "Historical Markdown has no JSON pair")

    def result(self) -> dict[str, Any]:
        errors = [item for item in self.issues if item["severity"] == "error"]
        warnings = [item for item in self.issues if item["severity"] == "warning"]
        return {"ok": not errors, "files_checked": len(self.checked),
                "errors": errors, "warnings": warnings}


def read_base_manifest(root: Path, ref: str) -> dict[str, Any] | None:
    if not ref or not ref.strip("0"):
        return None
    try:
        proc = subprocess.run(["git", "show", f"{ref}:manifests/reports.json"],
                              cwd=root, capture_output=True, text=True, encoding="utf-8",
                              check=False)
        value = json.loads(proc.stdout) if proc.returncode == 0 else None
    except (OSError, ValueError):
        return None
    return value if isinstance(value, dict) and isinstance(value.get("reports"), list) else None


def load_validator(root: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, root / "scripts" / f"{name}.py")
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_summary(result: dict[str, Any], scope: str, path: Path) -> None:
    counts = Counter(item["code"] for item in result["warnings"])
    lines = [f"## Radar {scope}: {'passed' if result['ok'] else 'failed'}", "",
             f"Checked {result['files_checked']} files. Blocking errors: {len(result['errors'])}. "
             f"Advisory findings: {len(result['warnings'])}.", "",
             "Daily checks require readable current reports. Editorial/legacy findings below are advisory.",
             "", "| Advisory category | Count |", "| --- | ---: |"]
    lines.extend(f"| {code} | {count} |" for code, count in sorted(counts.items()))
    lines += ["", "Detailed findings are retained in the report-health artifact.", ""]
    if result["errors"]:
        lines += ["### Blocking errors", ""]
        lines += [f"- {item['path']}: {item['message']}" for item in result["errors"]]
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=("current", "audit"), default="current")
    parser.add_argument("--base-ref")
    parser.add_argument("--output-json", type=Path)
    args = parser.parse_args(argv)
    check = HealthCheck(ROOT)
    if args.scope == "current":
        check.current(args.base_ref)
    else:
        check.audit()
    result = check.result()
    print(f"Report health ({args.scope}): {len(result['errors'])} blocking errors, "
          f"{len(result['warnings'])} advisory findings, {result['files_checked']} files checked.")
    for item in result["errors"]:
        print(f"ERROR {item['path']}: {item['message']}")
    for item in result["warnings"][:10]:
        print(f"WARNING [{item['code']}] {item['path']}: {item['message']}")
    if len(result["warnings"]) > 10:
        print("Additional advisory findings are included in the JSON artifact.")
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        write_summary(result, args.scope, Path(os.environ["GITHUB_STEP_SUMMARY"]))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
