from __future__ import annotations

import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("report_health", ROOT / "scripts/check_report_health.py")
HEALTH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HEALTH)


class ReportHealthTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.edition = "morning"
        self.day = "2026-10-16"
        self.stem = "reports/2026/10/2026-10-16_morning"
        self.entry = {
            "report_date": self.day, "edition": self.edition, "revision": 1,
            "status": "published", "archive_status": "success",
            "json_path": self.stem + ".json", "markdown_path": self.stem + ".md",
        }
        self.config = {"latest_json": "latest/morning.json",
                       "latest_markdown": "latest/morning.md",
                       "status_path": "status/morning_latest.json"}
        self.policy = {"editions": {"morning": self.config}}
        self.report = {"report_date": self.day, "edition": self.edition,
                       "top_opportunities": [{"strategy": "A research idea"}],
                       "archive": {"archive_status": "success"}}
        self.write_json("config/archive-policy.json", self.policy)
        self.write_json("manifests/reports.json", {"reports": [self.entry]})
        self.write_json(self.stem + ".json", self.report)
        self.write_json("latest/morning.json", self.report)
        self.write_json("status/morning_latest.json", {"report_date": self.day, "edition": self.edition})
        self.write(self.stem + ".md", "# A different editorial heading\nA readable research report.")
        self.write("latest/morning.md", "# A different editorial heading\nA readable research report.")

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")

    def write_json(self, name, value):
        self.write(name, json.dumps(value))

    def check(self, base_ref=None):
        check = HEALTH.HealthCheck(self.root)
        check.current(base_ref)
        return check.result()

    def test_readable_report_passes_without_revision_or_fixed_titles(self):
        result = self.check()
        self.assertTrue(result["ok"])
        self.assertTrue(any(row["code"] == "revision" for row in result["warnings"]))

    def test_pending_and_missing_success_are_advisory(self):
        self.entry["archive_status"] = "pending_verification"
        self.write_json("manifests/reports.json", {"reports": [self.entry]})
        self.assertTrue(self.check()["ok"])

    def test_invalid_current_json_blocks(self):
        self.write(self.stem + ".json", '{"report_date":')
        result = self.check()
        self.assertFalse(result["ok"])
        self.assertTrue(any(row["code"] == "unreadable_json" for row in result["errors"]))

    def test_missing_or_empty_current_markdown_blocks(self):
        for text in ("", "  \n"):
            with self.subTest(text=text):
                self.write(self.stem + ".md", text)
                self.assertFalse(self.check()["ok"])
        (self.root / (self.stem + ".md")).unlink()
        self.assertFalse(self.check()["ok"])

    def test_unreadable_manifest_blocks(self):
        self.write("manifests/reports.json", "broken")
        self.assertFalse(self.check()["ok"])

    def test_non_object_current_json_blocks(self):
        for value in ([], {}, None):
            with self.subTest(value=value):
                self.write_json("latest/morning.json", value)
                self.assertFalse(self.check()["ok"])

    def test_explicit_current_identity_conflict_blocks(self):
        for field, value in (("edition", "evening"), ("report_date", "2026-10-15")):
            with self.subTest(field=field):
                changed = dict(self.report, **{field: value})
                self.write_json(self.stem + ".json", changed)
                self.assertFalse(self.check()["ok"])

    def test_wrong_current_manifest_path_blocks(self):
        self.entry["json_path"] = "reports/2026/10/2026-10-16_evening.json"
        self.write_json("manifests/reports.json", {"reports": [self.entry]})
        self.assertFalse(self.check()["ok"])

    def test_metadata_only_manifest_update_does_not_require_report_revision(self):
        before = {"reports": [dict(self.entry, archive_status="pending_verification")]}
        with patch.object(HEALTH, "read_base_manifest", return_value=before):
            self.assertTrue(self.check("base")["ok"])

    def test_historical_repair_never_requires_latest_to_rewind(self):
        old = dict(self.entry, report_date="2026-08-21",
                   json_path="reports/2026/08/2026-08-21_evening.json",
                   markdown_path="reports/2026/08/2026-08-21_morning.md")
        self.write_json("manifests/reports.json", {"reports": [old, self.entry]})
        self.write("reports/2026/08/2026-08-21_morning.json", "historically malformed")
        before = {"reports": [dict(old, revision=2), self.entry]}
        with patch.object(HEALTH, "read_base_manifest", return_value=before):
            result = self.check("base")
        self.assertTrue(result["ok"])
        self.assertTrue(any(row["code"] == "historical_change" for row in result["warnings"]))
        self.assertTrue(any(row["code"] == "unreadable_json" for row in result["warnings"]))

    def test_missing_base_checks_current_files_instead_of_silently_passing(self):
        self.write("latest/morning.json", "broken")
        with patch.object(HEALTH, "read_base_manifest", return_value=None):
            result = self.check("unavailable")
        self.assertFalse(result["ok"])
        self.assertTrue(any(row["code"] == "base_unavailable" for row in result["warnings"]))

    def test_removed_historical_index_entry_is_visible_advice(self):
        before = {"reports": [self.entry, dict(self.entry, report_date="2026-08-21")]}
        with patch.object(HEALTH, "read_base_manifest", return_value=before):
            result = self.check("base")
        self.assertTrue(result["ok"])
        self.assertTrue(any(row["code"] == "removed_entry" for row in result["warnings"]))

    def test_latest_content_difference_and_status_failure_are_advisory(self):
        self.write("latest/morning.md", "# A revised introduction\nDifferent wording.")
        self.write("status/morning_latest.json", "incomplete metadata")
        result = self.check()
        self.assertTrue(result["ok"])
        self.assertTrue(any(row["code"] == "latest_sync" for row in result["warnings"]))

    def test_unindexed_latest_report_is_still_checked(self):
        older = copy.deepcopy(self.entry)
        older["report_date"] = "2026-10-15"
        older["json_path"] = "reports/2026/10/2026-10-15_morning.json"
        older["markdown_path"] = "reports/2026/10/2026-10-15_morning.md"
        self.write_json(older["json_path"], dict(self.report, report_date="2026-10-15"))
        self.write(older["markdown_path"], "# Previous report")
        self.write_json("manifests/reports.json", {"reports": [older]})
        self.write(self.stem + ".json", "broken new report")
        self.assertFalse(self.check()["ok"])

    def test_escape_path_is_rejected(self):
        self.policy["editions"]["morning"]["latest_json"] = "../outside.json"
        self.write_json("config/archive-policy.json", self.policy)
        self.assertFalse(self.check()["ok"])

    def test_bad_config_path_is_a_reported_error(self):
        self.policy["editions"]["morning"]["latest_json"] = None
        self.write_json("config/archive-policy.json", self.policy)
        self.assertFalse(self.check()["ok"])

    def test_zero_base_still_checks_current_report(self):
        self.assertIsNone(HEALTH.read_base_manifest(self.root, "0" * 40))
        self.write("latest/morning.json", "broken")
        self.assertFalse(self.check("0" * 40)["ok"])

    def test_old_bad_json_and_data_shapes_remain_advisory(self):
        for name in ("scripts/validate_reports.py", "scripts/validate_markdown_reports.py",
                     "schemas/report.schema.json"):
            self.write(name, (ROOT / name).read_text(encoding="utf-8"))
        for day, content in (("01", "broken"), ("02", "[]"),
                             ("03", '{"report_date":"2026-08-03","edition":[]}')):
            self.write(f"reports/2026/08/2026-08-{day}_morning.json", content)
            self.write(f"reports/2026/08/2026-08-{day}_morning.md", "# Old report")
        self.write("reports/2026/08/2026-08-04_morning.md", "# Orphan report")
        check = HEALTH.HealthCheck(self.root)
        check.audit()
        result = check.result()
        self.assertTrue(result["ok"])
        codes = {row["code"] for row in result["warnings"]}
        self.assertTrue({"unreadable_json", "schema_or_content", "missing_json_pair"} <= codes)
        # The advisory scan continues through bad files to current reports.
        self.assertTrue(any(row["path"] == self.stem + ".json" for row in result["warnings"]))

    def test_summary_exposes_advice_instead_of_hiding_it(self):
        result = self.check()
        summary = self.root / "summary.md"
        HEALTH.write_summary(result, "current", summary)
        text = summary.read_text(encoding="utf-8")
        self.assertIn("Blocking errors: 0", text)
        self.assertIn("revision", text)

    def test_cli_exit_and_json_artifact(self):
        output = self.root / "health.json"
        with patch.object(HEALTH, "ROOT", self.root), patch.dict("os.environ", {}, clear=True), \
                patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(HEALTH.main(["--output-json", str(output)]), 0)
            self.assertTrue(json.loads(output.read_text())["ok"])
            self.write("latest/morning.json", "broken")
            self.assertEqual(HEALTH.main(["--output-json", str(output)]), 1)
            self.assertFalse(json.loads(output.read_text())["ok"])


if __name__ == "__main__":
    unittest.main()
