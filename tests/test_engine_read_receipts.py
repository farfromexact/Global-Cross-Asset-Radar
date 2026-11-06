from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "tests" / "fixtures" / "engine_read_raw"


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


RECEIPTS = _load("engine_read_receipts", "scripts/engine_read_receipts.py")
HEALTH = _load("report_health_for_receipts", "scripts/check_report_health.py")


def _repos(**overrides):
    repos = {key: {"read_status": "not_started"} for key in RECEIPTS.REPOS}
    repos.update(overrides)
    return repos


def _status(receipts, repos=None, edition="commodities_evening"):
    return RECEIPTS.protocol_errors(
        {
            "engine_read_protocol": RECEIPTS.PROTOCOL_VERSION,
            "repos": repos if repos is not None else _repos(),
            "source_receipts": receipts,
        },
        report_date="2026-11-06",
        edition=edition,
    )


def _pin(**overrides):
    receipt = {
        "repo": "china_commodities",
        "repository": "farfromexact/China-Commodities-Engine",
        "path": "data/report_input_latest.json",
        "role": "research_pin",
        "cutoff_sha": "pin-a",
        "observed_sha": "pin-a",
        "read_status": "ok",
        "transport": "blob",
        "utf8_byte_length": 2266923,
        "blob_identity": "canonical-blob:2266923",
        "json_validation": "object",
        "canonical_descriptor": "pinned_utf8_2266923",
        "freshness": "carried",
        "calendar": "session_closed",
    }
    receipt.update(overrides)
    return receipt


class EngineReadReceiptTests(unittest.TestCase):
    def test_trusted_pinned_sizes_match_canonical_descriptors(self):
        descriptors = RECEIPTS.trusted_descriptors()
        self.assertEqual(descriptors["pinned_utf8_2266923"]["utf8_byte_length"], 2266923)
        self.assertEqual(descriptors["pinned_utf8_1612360"]["utf8_byte_length"], 1612360)
        self.assertEqual(
            RECEIPTS._FALLBACK_DESCRIPTORS["pinned_utf8_2266923"]["utf8_byte_length"],
            2266923,
        )
        self.assertEqual(
            RECEIPTS._FALLBACK_DESCRIPTORS["pinned_utf8_1612360"]["utf8_byte_length"],
            1612360,
        )
        fixture = json.loads(
            (ROOT / "tests" / "fixtures" / "engine_read_canonical.json").read_text(encoding="utf-8")
        )
        self.assertEqual(fixture["descriptors"]["pinned_utf8_2266923"]["utf8_byte_length"], 2266923)
        self.assertEqual(fixture["descriptors"]["pinned_utf8_1612360"]["utf8_byte_length"], 1612360)

        large = _pin()
        other = _pin(
            path="data/latest.json",
            utf8_byte_length=1612360,
            blob_identity="canonical-blob:1612360",
            canonical_descriptor="pinned_utf8_1612360",
        )
        repos = _repos(china_commodities={"read_status": "ok", "cutoff_sha": "pin-a",
                                          "last_good": {"date": "2026-11-05"}})
        self.assertEqual(_status([large, other], repos), [])

        capped = _pin(utf8_byte_length=1048576, assumed_max_bytes=1048576, reason="file_too_large",
                      read_status="missing", json_validation="empty", blob_identity=None,
                      transport="contents")
        errors = _status([capped], _repos(china_commodities={"read_status": "missing"}))
        self.assertTrue(any("canonical_size_mismatch" in item for item in errors))
        self.assertTrue(any("file_too_large_is_not_missing" in item for item in errors))
        self.assertTrue(any("assumed_1mb_cap" in item for item in errors))

    def test_empty_containers_are_valid_zero_and_zero_bytes_are_empty(self):
        empty_object = (RAW / "empty_object.txt").read_bytes()
        empty_array = (RAW / "empty_array.txt").read_bytes()
        zero = (RAW / "zero_byte.txt").read_bytes()
        self.assertEqual(empty_object, b"{}")
        self.assertEqual(len(empty_object), 2)
        self.assertEqual(empty_array, b"[]")
        self.assertEqual(len(empty_array), 2)
        self.assertEqual(len(zero), 0)

        object_assessed = RECEIPTS.assess_payload(empty_object)
        array_assessed = RECEIPTS.assess_payload(empty_array)
        zero_assessed = RECEIPTS.assess_payload(zero)
        self.assertEqual(object_assessed["read_status"], "valid_zero")
        self.assertEqual(object_assessed["utf8_byte_length"], 2)
        self.assertEqual(array_assessed["read_status"], "valid_zero")
        self.assertEqual(array_assessed["json_validation"], "valid_zero")
        self.assertEqual(zero_assessed, {
            "read_status": "empty",
            "utf8_byte_length": 0,
            "json_validation": "empty",
        })
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "valid_zero", "utf8_byte_length": 2, "json_validation": "valid_zero"},
            empty_object,
        ), [])
        self.assertTrue(RECEIPTS.payload_consistency_errors(
            {"read_status": "empty", "utf8_byte_length": 0, "json_validation": "empty"},
            empty_object,
        ))
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "valid_zero", "utf8_byte_length": 2, "json_validation": "valid_zero"},
            empty_array,
        ), [])
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "empty", "utf8_byte_length": 0, "json_validation": "empty"},
            zero,
        ), [])

        valid = _pin(
            path="data/last_run_status.json",
            transport="contents",
            read_status="valid_zero",
            utf8_byte_length=2,
            blob_identity="blob-empty-object",
            json_validation="valid_zero",
            canonical_descriptor=None,
        )
        repos = _repos(china_commodities={"read_status": "valid_zero", "cutoff_sha": "pin-a",
                                          "last_good": {"date": "2026-11-05"}})
        self.assertEqual(_status([valid], repos), [])
        zero_receipt = dict(valid, read_status="empty", utf8_byte_length=0, json_validation="empty")
        self.assertEqual(_status([zero_receipt], _repos(china_commodities={
            "read_status": "empty", "cutoff_sha": "pin-a"})), [])
        confused = dict(valid, read_status="valid_zero", utf8_byte_length=0, json_validation="empty")
        confused_errors = _status([confused], repos)
        self.assertTrue(any("valid_zero_requires_bytes" in item for item in confused_errors))
        self.assertTrue(any("valid_zero_json_validation" in item for item in confused_errors))

    def test_truncated_and_bad_json_are_not_successful_reads(self):
        truncated = (RAW / "truncated_object.txt").read_bytes()
        bad = (RAW / "bad_json.txt").read_bytes()
        truncated_assessed = RECEIPTS.assess_payload(truncated)
        bad_assessed = RECEIPTS.assess_payload(bad)
        self.assertEqual(truncated_assessed["read_status"], "truncated")
        self.assertEqual(truncated_assessed["utf8_byte_length"], len(truncated))
        self.assertEqual(bad_assessed["read_status"], "parse_error")
        self.assertNotEqual(bad_assessed["json_validation"], "object")
        self.assertTrue(RECEIPTS.payload_consistency_errors(
            {"read_status": "ok", "utf8_byte_length": len(truncated), "json_validation": "object"},
            truncated,
        ))
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {
                "read_status": "truncated",
                "utf8_byte_length": len(truncated),
                "json_validation": "truncated",
            },
            truncated,
        ), [])
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "parse_error", "utf8_byte_length": len(bad), "json_validation": "parse_error"},
            bad,
        ), [])

        claimed_ok = _pin(read_status="truncated", json_validation="object", canonical_descriptor=None,
                          utf8_byte_length=len(truncated), blob_identity="blob-cut")
        errors = _status([claimed_ok], _repos(china_commodities={"read_status": "truncated",
                                                                "cutoff_sha": "pin-a"}))
        self.assertTrue(any("unparsed_json_cannot_be_ok" in item for item in errors))

    def test_permission_and_read_failed_do_not_claim_bytes(self):
        permission = {
            "repo": "china_options",
            "repository": "farfromexact/China-Options-Engine",
            "path": "data/radar_latest.json",
            "cutoff_sha": "pin-b",
            "read_status": "permission_error",
            "freshness": "unknown",
        }
        failed = {
            "repo": "china_stock",
            "repository": "farfromexact/China-Stock-Engine",
            "path": "data/latest/manifest.json",
            "cutoff_sha": "pin-c",
            "read_status": "read_failed",
        }
        repos = _repos(
            china_options={"read_status": "permission_error", "cutoff_sha": "pin-b"},
            china_stock={"read_status": "read_failed", "cutoff_sha": "pin-c"},
            china_commodities={"read_status": "ok", "cutoff_sha": "pin-a",
                               "last_good": {"date": "2026-11-05"}},
        )
        self.assertEqual(_status([permission, failed, _pin()], repos), [])
        lying = dict(permission, json_validation="object", utf8_byte_length=10, blob_identity="nope")
        errors = _status([lying, failed, _pin()], repos)
        self.assertTrue(any("permission must not claim a parsed payload" in item for item in errors))
        self.assertFalse(any("china_commodities" in item and "permission" in item for item in errors))

    def test_post_cutoff_pin_is_isolated_from_the_research_sha(self):
        isolated = _pin(
            role="isolated_post_cutoff",
            isolated=True,
            read_status="isolated",
            observed_sha="later-sha",
            utf8_byte_length=None,
            blob_identity=None,
            json_validation=None,
            canonical_descriptor=None,
            transport=None,
        )
        research = _pin(canonical_descriptor=None, utf8_byte_length=80, blob_identity="blob-same",
                        transport="contents", path="data/radar_latest.json")
        repos = _repos(china_commodities={"read_status": "ok", "cutoff_sha": "pin-a",
                                          "last_good": {"date": "2026-11-05"}})
        self.assertEqual(_status([isolated, research], repos), [])
        contaminated = dict(research, observed_sha="later-sha")
        errors = _status([contaminated], repos)
        self.assertTrue(any("post_cutoff_pin" in item for item in errors))

    def test_backfill_2026_11_05_is_not_current_for_2026_11_06(self):
        backfill = _pin(
            role="backfill",
            path="data/snapshots/2026-11-05.json",
            transport="contents",
            canonical_descriptor=None,
            utf8_byte_length=40,
            blob_identity="blob-backfill",
            as_of_date="2026-11-05",
            freshness="current",
            calendar="backfill",
        )
        research = _pin(canonical_descriptor=None, utf8_byte_length=80, blob_identity="blob-current",
                        transport="contents", path="data/radar_latest.json", freshness="carried",
                        as_of_date="2026-11-05")
        repos = _repos(china_commodities={
            "read_status": "ok",
            "cutoff_sha": "pin-a",
            "last_good": {"date": "2026-11-05"},
            "freshness": "carried",
            "calendar": "session_closed",
        })
        errors = _status([backfill, research], repos)
        self.assertTrue(any("backfill_called_current" in item and "2026-11-05" in item and "2026-11-06" in item
                            for item in errors))
        self.assertEqual(sum("backfill_called_current" in item for item in errors), 1)
        honest = dict(backfill, freshness="backfill")
        self.assertEqual(_status([honest, research], repos), [])
        stale_alias = _repos(china_commodities={
            "read_status": "stale",
            "cutoff_sha": "pin-a",
            "last_good": {"date": "2026-11-05"},
            "calendar": "holiday",
        })
        self.assertEqual(_status([], stale_alias), [])
        stale_alias["china_commodities"]["freshness"] = "current"
        self.assertTrue(any("stale alias conflicts" in item for item in _status([], stale_alias)))

    def test_not_started_is_isolated_and_last_good_is_not_the_pin(self):
        repos = _repos(
            china_commodities={"read_status": "ok", "cutoff_sha": "pin-a",
                               "last_good": {"date": "2026-11-05"}},
            china_options={"read_status": "not_started"},
            china_stock={"read_status": "not_started"},
        )
        self.assertEqual(_status([_pin()], repos, edition="morning"), [])
        self.assertTrue(any("not_started repo has a successful receipt" in item for item in _status(
            [_pin(repo="china_options", repository="farfromexact/China-Options-Engine")],
            repos,
            edition="morning",
        )))
        conflated = _repos(china_commodities={"read_status": "not_started", "cutoff_sha": "pin-a",
                                              "last_good": "pin-a"})
        errors = _status([], conflated)
        self.assertTrue(any("last_good_is_pinned_sha" in item for item in errors))
        self.assertFalse(any("missing" in item for item in errors))
        omitted = dict(repos)
        del omitted["china_stock"]
        self.assertIn("repo_not_attempted:china_stock", _status([_pin()], omitted, edition="evening"))

    def test_legacy_and_unversioned_receipts_are_not_enforced(self):
        junk = {"source_receipts": [{"read_status": "ok"}], "repos": {}}
        self.assertEqual(RECEIPTS.protocol_errors(junk, report_date="2026-11-06", edition="morning"), [])
        self.assertEqual(RECEIPTS.protocol_errors(
            {"engine_read_protocol": "other", "source_receipts": [{"read_status": "ok"}]},
            edition="evening",
        ), [])
        self.assertEqual(RECEIPTS.protocol_errors(["ok", "missing"], edition="morning"), [])
        self.assertEqual(RECEIPTS.protocol_errors(None), [])

    def test_ordinary_incomplete_reread_uses_the_same_sha_blob_or_raw(self):
        incomplete = _pin(ordinary_contents="incomplete", transport="contents")
        repos = _repos(china_commodities={"read_status": "ok", "cutoff_sha": "pin-a",
                                          "last_good": {"date": "2026-11-05"}})
        self.assertTrue(any("incomplete_requires_same_sha_blob_or_raw" in item
                            for item in _status([incomplete], repos)))
        recovered = _pin(ordinary_contents="incomplete", transport="raw")
        self.assertEqual(_status([recovered], repos), [])
        compact = _pin(transport="compact")
        self.assertTrue(any("big_contents_required" in item for item in _status([compact], repos)))

    def test_validator_source_does_not_fetch_github(self):
        source = (ROOT / "scripts" / "engine_read_receipts.py").read_text(encoding="utf-8")
        for token in ("urllib", "subprocess", "requests", "github.com", "socket"):
            self.assertNotIn(token, source)

    def test_prompt_copies_replace_the_file_too_large_rule(self):
        prompts = {
            name: (ROOT / "prompts" / name).read_text(encoding="utf-8")
            for name in (
                "radar_morning.md",
                "radar_evening.md",
                "commodities_morning.md",
                "commodities_evening.md",
            )
        }
        protocol = (ROOT / "docs" / "ENGINE_READ_PROTOCOL.md").read_text(encoding="utf-8")
        old = "文件过大时读取可用紧凑层、范围或明确快照；仍失败则标缺失"
        for name, text in prompts.items():
            self.assertNotIn(old, text, name)
            self.assertIn("docs/ENGINE_READ_PROTOCOL.md", text, name)
            self.assertIn("valid_zero", text, name)
            self.assertIn("not_started", text, name)
            self.assertIn("blob", text, name)
            self.assertIn("Scheduled Task", text, name)
        for name in ("radar_morning.md", "radar_evening.md"):
            for repo in RECEIPTS.REPOS.values():
                self.assertIn(repo, prompts[name], name)
            self.assertIn("三个引擎仓库", prompts[name])
        for name in ("commodities_morning.md", "commodities_evening.md"):
            for repo in RECEIPTS.REPOS.values():
                self.assertIn(repo, prompts[name], name)
            self.assertIn("大文件", prompts[name])
        self.assertIn("2266923", protocol)
        self.assertIn("1612360", protocol)
        self.assertNotIn(old, protocol)
        self.assertIn("不访问 GitHub", protocol)
        self.assertIn("Scheduled Task", protocol)

    def test_health_check_blocks_only_versioned_inconsistent_current_reports(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            day = "2026-11-06"
            edition = "commodities_evening"
            stem = f"reports/2026/11/{day}_{edition}"
            config = {
                "latest_json": f"latest/{edition}.json",
                "latest_markdown": f"latest/{edition}.md",
                "status_path": f"status/{edition}_latest.json",
            }
            entry = {
                "report_date": day, "edition": edition, "revision": 1,
                "status": "published", "archive_status": "success",
                "json_path": stem + ".json", "markdown_path": stem + ".md",
            }
            report = {
                "report_date": day,
                "edition": edition,
                "archive": {"archive_status": "success"},
                "source_status": {
                    "engine_read_protocol": RECEIPTS.PROTOCOL_VERSION,
                    "repos": _repos(china_commodities={
                        "read_status": "ok", "cutoff_sha": "pin-a",
                        "last_good": {"date": "2026-11-05"},
                    }),
                    "source_receipts": [_pin(utf8_byte_length=1048576)],
                },
            }
            self._write_bundle(root, entry, report, config, stem)
            result = self._health(root)
            self.assertFalse(result["ok"])
            self.assertTrue(any(item["code"] == "source_receipt" for item in result["errors"]))

            report["source_status"]["source_receipts"] = [_pin()]
            self._write_bundle(root, entry, report, config, stem)
            consistent = self._health(root)
            self.assertTrue(consistent["ok"])
            self.assertFalse(any(item["code"] == "source_receipt" for item in consistent["errors"]))

            report["source_status"] = {"source_receipts": [{"read_status": "ok"}]}
            self._write_bundle(root, entry, report, config, stem)
            legacy = self._health(root)
            self.assertTrue(legacy["ok"])
            self.assertFalse(any(item["code"] == "source_receipt" for item in legacy["errors"]))

    def _write_bundle(self, root: Path, entry, report, config, stem: str) -> None:
        policy = {"editions": {entry["edition"]: config}}
        for relative, payload in (
            ("config/archive-policy.json", policy),
            ("manifests/reports.json", {"reports": [entry]}),
            (stem + ".json", report),
            (config["latest_json"], report),
            (config["status_path"], {"report_date": entry["report_date"], "edition": entry["edition"],
                                     "archive_status": "success"}),
        ):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload), encoding="utf-8")
        text = "# Readable report\nEnough text to be non-empty.\n"
        for relative in (stem + ".md", config["latest_markdown"]):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")

    def _health(self, root: Path):
        check = HEALTH.HealthCheck(root)
        check.current(None)
        return check.result()


if __name__ == "__main__":
    unittest.main()
