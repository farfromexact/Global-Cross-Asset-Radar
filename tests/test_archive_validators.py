from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "archive_validator", REPO_ROOT / "scripts" / "validate_reports.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

MARKDOWN_SPEC = importlib.util.spec_from_file_location(
    "markdown_validator", REPO_ROOT / "scripts" / "validate_markdown_reports.py"
)
assert MARKDOWN_SPEC and MARKDOWN_SPEC.loader
MARKDOWN_VALIDATOR = importlib.util.module_from_spec(MARKDOWN_SPEC)
MARKDOWN_SPEC.loader.exec_module(MARKDOWN_VALIDATOR)


class ArchiveValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.policy = json.loads((REPO_ROOT / "config" / "archive-policy.json").read_text(encoding="utf-8"))
        cls.report_schema = json.loads((REPO_ROOT / "schemas" / "report.schema.json").read_text(encoding="utf-8"))
        cls.manifest_schema = json.loads((REPO_ROOT / "schemas" / "manifest.schema.json").read_text(encoding="utf-8"))
        cls.allowed_editions = VALIDATOR.configured_editions(cls.policy)
        cls.commodity_report = json.loads(
            (REPO_ROOT / "reports" / "2026" / "08" / "2026-08-19_commodities_evening.json").read_text(
                encoding="utf-8"
            )
        )

    def test_policy_is_the_validator_edition_source(self) -> None:
        self.assertEqual(
            self.allowed_editions,
            ("morning", "evening", "commodities_morning", "commodities_evening"),
        )
        pattern = VALIDATOR.historical_report_pattern(self.allowed_editions)
        self.assertIsNotNone(pattern.fullmatch("2026-08-19_commodities_evening.json"))
        self.assertIsNone(pattern.fullmatch("2026-08-19_unknown.json"))

    def test_rejects_bad_edition_and_filename_edition_mismatch(self) -> None:
        path = REPO_ROOT / "reports" / "2026" / "08" / "2026-08-20_commodities_morning.json"
        mismatched = {
            "schema_version": "1.0",
            "status": "archive_failed",
            "report_date": "2026-08-20",
            "edition": "commodities_evening",
        }
        with patch.object(VALIDATOR, "load_json", return_value=mismatched), patch.object(
            VALIDATOR, "scan_forbidden_tokens", return_value=[]
        ):
            errors = VALIDATOR.validate_report_file(path, self.report_schema, self.allowed_editions)
        self.assertTrue(any("does not match filename edition" in error for error in errors))

        invalid = dict(mismatched, edition="unknown")
        with patch.object(VALIDATOR, "load_json", return_value=invalid), patch.object(
            VALIDATOR, "scan_forbidden_tokens", return_value=[]
        ):
            errors = VALIDATOR.validate_report_file(path, self.report_schema, self.allowed_editions)
        self.assertTrue(any("not configured in archive-policy.json" in error for error in errors))

    def test_rejects_missing_markdown_and_json_pairs(self) -> None:
        # Use a date that is not already present in the live archive.  The
        # report validator only needs a path for its filename/pair checks; a
        # fixed existing date would make this test depend on today's archive.
        json_path = REPO_ROOT / "reports" / "2026" / "08" / "2026-08-21_commodities_evening.json"
        report = {
            "schema_version": "1.0",
            "status": "archive_failed",
            "report_date": "2026-08-20",
            "edition": "commodities_evening",
        }
        with patch.object(VALIDATOR, "load_json", return_value=report), patch.object(
            VALIDATOR, "scan_forbidden_tokens", return_value=[]
        ):
            report_errors = VALIDATOR.validate_report_file(
                json_path, self.report_schema, self.allowed_editions
            )
        self.assertTrue(any("Missing Markdown pair" in error for error in report_errors))

        virtual_root = REPO_ROOT / "_validator_virtual_root"
        orphan_markdown = virtual_root / "reports" / "2026" / "08" / "2026-08-21_commodities_evening.md"
        original_glob = Path.glob

        def fake_glob(path: Path, pattern: str):
            if path == virtual_root / "reports" and pattern == "**/*.md":
                return [orphan_markdown]
            return original_glob(path, pattern)

        with patch.object(VALIDATOR, "ROOT", virtual_root), patch.object(Path, "glob", fake_glob):
            pair_errors = VALIDATOR.validate_markdown_pairs(self.allowed_editions, self.policy)
        self.assertTrue(any("Missing JSON pair" in error for error in pair_errors))

    def test_rejects_duplicate_manifest_key(self) -> None:
        manifest_path = REPO_ROOT / "_virtual" / "manifests" / "reports.json"
        entry = {
            "report_date": "2026-08-20",
            "edition": "commodities_evening",
            "markdown_path": "",
            "json_path": "",
            "status": "published",
        }
        manifest = {
            "schema_version": "1.0",
            "updated_at_bjt": "2026-08-20T19:30:00+08:00",
            "reports": [entry, copy.deepcopy(entry)],
        }
        original_exists = Path.exists

        def fake_exists(path: Path) -> bool:
            return path == manifest_path or original_exists(path)

        with patch.object(VALIDATOR, "MANIFEST_PATH", manifest_path), patch.object(
            VALIDATOR, "load_json", return_value=manifest
        ), patch.object(VALIDATOR, "scan_forbidden_tokens", return_value=[]), patch.object(Path, "exists", fake_exists):
            errors = VALIDATOR.validate_manifest(self.manifest_schema, self.allowed_editions)
        self.assertTrue(any("Duplicate manifest key" in error for error in errors))

    def test_published_commodity_requires_input_metadata(self) -> None:
        report = copy.deepcopy(self.commodity_report)
        del report["input_snapshots"]["china_commodities"]
        normalized = VALIDATOR.normalize_report_for_schema(report, REPO_ROOT / "fixture.json")
        errors = VALIDATOR.validate_json_schema(normalized, self.report_schema, REPO_ROOT / "fixture.json")
        self.assertTrue(any("china_commodities" in error for error in errors))

    def test_commodity_schedule_dialect_is_normalized_for_validation(self) -> None:
        for filename in ("latest/commodities_evening.json", "latest/commodities_morning.json"):
            path = REPO_ROOT / filename
            raw = json.loads(path.read_text(encoding="utf-8"))
            normalized = VALIDATOR.normalize_report_for_schema(raw, path)
            errors = VALIDATOR.validate_json_schema(normalized, self.report_schema, path)
            self.assertEqual(errors, [], filename)
            self.assertEqual(
                VALIDATOR.validate_commodity_contract(normalized, path, self.allowed_editions),
                [],
                filename,
            )

        pending = copy.deepcopy(self.commodity_report)
        pending.pop("archive", None)
        pending["archive_status"] = "pending_verification"
        normalized_pending = VALIDATOR.normalize_report_for_schema(
            pending, REPO_ROOT / "latest" / "commodities_evening.json"
        )
        self.assertEqual(normalized_pending["archive"]["archive_status"], "pending")

    def test_current_evening_top_level_dialect_materializes_safe_tracking(self) -> None:
        path = REPO_ROOT / "latest" / "commodities_evening.json"
        raw = json.loads(path.read_text(encoding="utf-8"))
        self.assertNotIn("commodities_tracking", raw)

        normalized = VALIDATOR.normalize_report_for_schema(raw, path)
        tracking = normalized["commodities_tracking"]
        quality = tracking["data_quality"]

        self.assertEqual(
            set(tracking),
            {"data_quality", "market_dashboard", "supply_chain_map", "options_surface", "night_session_risk_map"},
        )
        self.assertEqual(quality["curve_definition"], "near_minus_next_futures_curve_not_spot_basis")
        self.assertIn("1D", quality["available_horizons"])
        self.assertEqual(tracking["options_surface"]["status"], "not_ready")
        self.assertEqual(tracking["options_surface"]["available_metrics"], [])
        self.assertEqual(tracking["options_surface"]["tradeable_structures"], [])
        self.assertTrue(tracking["options_surface"]["research_priority_when_ready"])
        self.assertTrue(tracking["market_dashboard"])
        self.assertTrue(tracking["supply_chain_map"])
        self.assertTrue(tracking["night_session_risk_map"])
        self.assertTrue(all("confidence" in row and "action" in row for row in tracking["night_session_risk_map"]))
        self.assertEqual(
            VALIDATOR.validate_commodity_contract(normalized, path, self.allowed_editions),
            [],
        )

    def test_missing_night_fields_and_non_uri_source_are_explicitly_normalized(self) -> None:
        report = copy.deepcopy(self.commodity_report)
        report["commodities_tracking"]["night_session_risk_map"] = [
            {"product": "FU", "expected_open": "higher", "wait_minutes": 30},
        ]
        report["sources"] = [{"publisher": "official", "url": "official sources enumerated in Markdown"}]
        normalized = VALIDATOR.normalize_report_for_schema(report, REPO_ROOT / "fixture.json")

        night_row = normalized["commodities_tracking"]["night_session_risk_map"][0]
        self.assertEqual(night_row["confidence"], "unknown")
        self.assertIn("expected: higher", night_row["action"])
        self.assertEqual(normalized["sources"][0]["url"], None)
        self.assertEqual(normalized["sources"][0]["url_note"], "official sources enumerated in Markdown")

    def test_global_evening_heading_alias_is_accepted(self) -> None:
        markdown_path = REPO_ROOT / "latest" / "evening.md"
        errors = MARKDOWN_VALIDATOR.validate_full_markdown(markdown_path, "2026-08-20", "evening")
        self.assertEqual(errors, [])

    def test_pending_archive_defers_latest_markdown_identity_check(self) -> None:
        virtual_root = REPO_ROOT / "_pending_archive_virtual_root"
        latest_json = virtual_root / "latest" / "commodities_evening.json"
        latest_md = latest_json.with_suffix(".md")
        status_path = virtual_root / "status" / "commodities_evening_latest.json"
        historical_md = virtual_root / "reports" / "2026" / "08" / "2026-08-20_commodities_evening.md"
        latest_report = {
            "status": "published",
            "report_date": "2026-08-20",
            "edition": "commodities_evening",
        }
        pending_status = {
            "edition": "commodities_evening",
            "report_date": "2026-08-20",
            "archive_status": "pending",
        }
        editions = {
            "commodities_evening": {
                "latest_json": "latest/commodities_evening.json",
                "latest_markdown": "latest/commodities_evening.md",
                "status_path": "status/commodities_evening_latest.json",
            }
        }

        def fake_exists(path: Path) -> bool:
            return path in {latest_json, latest_md, status_path, historical_md}

        def fake_load_json(path: Path) -> dict[str, Any]:
            return pending_status if path == status_path else latest_report

        with patch.object(MARKDOWN_VALIDATOR, "ROOT", virtual_root), patch.object(
            Path, "exists", fake_exists
        ), patch.object(MARKDOWN_VALIDATOR, "load_json", fake_load_json), patch.object(
            MARKDOWN_VALIDATOR, "validate_full_markdown", return_value=[]
        ):
            errors = MARKDOWN_VALIDATOR.validate_latest_consistency(editions)
        self.assertEqual(errors, [])

    def test_commodity_markdown_alias_headings_are_accepted(self) -> None:
        for filename in (
            "reports/2026/08/2026-08-19_commodities_evening.md",
            "reports/2026/08/2026-08-20_commodities_morning.md",
        ):
            markdown_path = REPO_ROOT / filename
            json_path = markdown_path.with_suffix(".json")
            report = json.loads(json_path.read_text(encoding="utf-8"))
            errors = MARKDOWN_VALIDATOR.validate_full_markdown(
                markdown_path,
                report["report_date"],
                report["edition"],
            )
            self.assertEqual(errors, [], filename)

    def test_blocks_history_comparisons_and_option_metrics_behind_gates(self) -> None:
        report = copy.deepcopy(self.commodity_report)
        quality = report["commodities_tracking"]["data_quality"]
        quality["history_comparison_status"] = "insufficient_history"
        quality["available_horizons"] = ["1D"]
        quality["comparative_metrics"] = [{"metric": "return_1d", "value": 1.0}]
        report["commodities_tracking"]["options_surface"]["status"] = "ready"
        report["commodities_tracking"]["market_dashboard"][0]["atm_iv"] = 0.25
        path = REPO_ROOT / "fixture.json"
        errors = VALIDATOR.validate_commodity_contract(report, path, self.allowed_editions)
        self.assertTrue(any("comparison horizons" in error for error in errors))
        self.assertTrue(any("comparative metrics" in error for error in errors))
        self.assertTrue(any("IV/skew/Gamma/strike" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
