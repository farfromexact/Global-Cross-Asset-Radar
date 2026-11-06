from __future__ import annotations

import base64
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "tests" / "fixtures" / "engine_read_raw"
PIN_O = "1" * 40
PIN_C = "2" * 40
PIN_S = "3" * 40
HEAD = "4" * 40
LAST = "5" * 40
BLOB = "6" * 40
VERIFIED_COMMIT = "2dfb15b11da3854605013ce15349a43c783384f3"
REPORT_BLOB = "4dc792ef93e18f8a98e42af811c8b34d5e195460"
NIGHT_BLOB = "aa0548cb195c4a2ba8ad3c1b43c64abf2b3c5ce9"
REPORT_SHA256 = "51d01dbe8fe584dd4c12ae03792d333d38db22591f58dbdbe56fc581272168c7"
NIGHT_SHA256 = "4193dc29e6f2628413d0ee4a7d1b7c6b11d55fd4b063ec3641ae2690dda25c0d"


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


RECEIPTS = _load("engine_read_receipts", "scripts/engine_read_receipts.py")
HEALTH = _load("report_health_for_receipts", "scripts/check_report_health.py")


def _resolved(sha, read_status="ok", **extra):
    row = {
        "read_status": read_status,
        "cutoff_sha": sha,
        "cutoff_at": "2026-11-06T07:30:00",
        "cutoff_zone": "Asia/Shanghai",
        "commit_timestamp": "2026-11-05T16:00:00Z",
        "commit_timestamp_source": "committer_date",
    }
    row.update(extra)
    return row


def _repos(**overrides):
    repos = {
        "china_options": _resolved(PIN_O, "permission_denied", calendar="not_started"),
        "china_commodities": _resolved(PIN_C, "ok"),
        "china_stock": _resolved(PIN_S, "permission_denied"),
    }
    repos.update(overrides)
    return repos


def _pin(**overrides):
    receipt = {
        "repo": "china_commodities",
        "repository": "farfromexact/China-Commodities-Engine",
        "path": "data/report_input_latest.json",
        "role": "research_pin",
        "cutoff_sha": PIN_C,
        "observed_sha": PIN_C,
        "read_status": "ok",
        "transport": "blob",
        "utf8_byte_length": 128,
        "blob_identity": BLOB,
        "json_validation": "object",
        "freshness": "carried",
    }
    receipt.update(overrides)
    return receipt


def _night(edition, sha, **overrides):
    receipt = {
        "repo": "china_commodities",
        "repository": "farfromexact/China-Commodities-Engine",
        "path": "data/night_session/latest.json",
        "role": "research_pin",
        "cutoff_sha": sha,
        "observed_sha": sha,
        "read_status": "ok",
        "transport": "contents",
        "blob_identity_source": "contents_metadata",
        "utf8_byte_length": 120,
        "blob_identity": "a" * 40,
        "json_validation": "object",
        "vendor_snapshot": True,
        "official_night_close_verified": False,
        "session_timing": "completed" if edition == "commodities_morning" else "not_due",
        "actual_tools": {"contents": "ok", "blob": "not_called", "raw": "absent"},
    }
    receipt.update(overrides)
    return receipt


def _status(receipts, repos=None, edition="commodities_evening", *, night=True):
    repos = repos if repos is not None else _repos()
    body = list(receipts)
    if edition in RECEIPTS.COMMODITY_EDITIONS and night:
        if not any(isinstance(item, dict) and "night_session/latest.json" in str(item.get("path")) for item in body):
            sha = PIN_C
            commodities = repos.get("china_commodities")
            if isinstance(commodities, dict) and RECEIPTS._sha40(commodities.get("cutoff_sha")):
                sha = commodities["cutoff_sha"]
            body.append(_night(edition, sha))
    return RECEIPTS.protocol_errors(
        {
            "engine_read_protocol": RECEIPTS.PROTOCOL_VERSION,
            "repos": repos,
            "source_receipts": body,
        },
        report_date="2026-11-06",
        edition=edition,
    )


class EngineReadReceiptTests(unittest.TestCase):
    def test_verified_evidence_is_production_config_not_a_test_fallback(self):
        evidence = RECEIPTS.load_verified_evidence()
        self.assertEqual(evidence["commit"], VERIFIED_COMMIT)
        self.assertTrue(evidence["not_original_report_visibility"])
        report = evidence["paths"]["data/report_input_latest.json"]
        night = evidence["paths"]["data/night_session/latest.json"]
        self.assertEqual(report["utf8_byte_length"], 2266923)
        self.assertEqual(report["blob_identity"], REPORT_BLOB)
        self.assertEqual(report["sha256"], REPORT_SHA256)
        self.assertEqual(night["utf8_byte_length"], 1612360)
        self.assertEqual(night["blob_identity"], NIGHT_BLOB)
        self.assertEqual(night["sha256"], NIGHT_SHA256)
        source = (ROOT / "scripts" / "engine_read_receipts.py").read_text(encoding="utf-8")
        self.assertNotIn("tests/fixtures", source)
        self.assertNotIn("canonical-blob", source)
        self.assertNotIn("_FALLBACK", source)
        self.assertFalse((ROOT / "tests" / "fixtures" / "engine_read_canonical.json").exists())

        repos = _repos(china_commodities=_resolved(VERIFIED_COMMIT, "ok"))
        good = [
            _pin(
                cutoff_sha=VERIFIED_COMMIT,
                observed_sha=VERIFIED_COMMIT,
                utf8_byte_length=2266923,
                blob_identity=REPORT_BLOB,
                sha256=REPORT_SHA256,
                verified_commit=VERIFIED_COMMIT,
            ),
            _night(
                "commodities_evening",
                VERIFIED_COMMIT,
                utf8_byte_length=1612360,
                blob_identity=NIGHT_BLOB,
                sha256=NIGHT_SHA256,
                verified_commit=VERIFIED_COMMIT,
                transport="blob",
            ),
        ]
        self.assertEqual(_status(good, repos, night=False), [])
        claimed_visible = dict(good[0], original_report_visibility=True)
        visible_errors = _status([claimed_visible, good[1]], repos, night=False)
        self.assertTrue(any("retrospective_is_not_report_visibility" in item for item in visible_errors))

        capped = _pin(
            cutoff_sha=VERIFIED_COMMIT,
            observed_sha=VERIFIED_COMMIT,
            read_status="missing",
            utf8_byte_length=1048576,
            blob_identity=None,
            json_validation=None,
            sha256=None,
            verified_commit=VERIFIED_COMMIT,
            transport="contents",
            reason="file_too_large",
            assumed_max_bytes=1048576,
        )
        capped_repos = _repos(china_commodities=_resolved(VERIFIED_COMMIT, "missing"))
        errors = _status([capped], capped_repos, edition="morning", night=False)
        self.assertTrue(any("canonical_size_mismatch" in item for item in errors))
        self.assertTrue(any("file_too_large_is_not_missing" in item for item in errors))
        self.assertTrue(any("assumed_1mb_cap" in item for item in errors))
        self.assertFalse(any("read_failed must not claim" in item for item in errors))

    def test_malformed_evidence_file_is_not_replaced(self):
        with tempfile.TemporaryDirectory() as temp:
            bad = Path(temp) / "engine_read_evidence.json"
            bad.write_text("{", encoding="utf-8")
            with self.assertRaises(ValueError) as raised:
                RECEIPTS.load_verified_evidence(bad)
            self.assertIn("evidence_file_unusable", str(raised.exception))
            missing = Path(temp) / "missing.json"
            with self.assertRaises(ValueError) as missing_raised:
                RECEIPTS.load_verified_evidence(missing)
            self.assertIn("evidence_file_unusable", str(missing_raised.exception))
            errors = RECEIPTS.protocol_errors(
                {
                    "engine_read_protocol": RECEIPTS.PROTOCOL_VERSION,
                    "repos": _repos(china_commodities=_resolved(VERIFIED_COMMIT, "ok")),
                    "source_receipts": [_pin(
                        cutoff_sha=VERIFIED_COMMIT,
                        observed_sha=VERIFIED_COMMIT,
                        utf8_byte_length=2266923,
                        blob_identity=REPORT_BLOB,
                        sha256=REPORT_SHA256,
                        verified_commit=VERIFIED_COMMIT,
                    )],
                },
                report_date="2026-11-06",
                edition="morning",
                evidence_path=bad,
            )
        self.assertTrue(any("evidence_file_unusable" in item for item in errors))
        self.assertFalse(any("canonical_size_mismatch" in item for item in errors))

    def test_empty_containers_are_valid_zero_and_zero_bytes_are_actual_empty(self):
        empty_object = (RAW / "empty_object.txt").read_bytes()
        empty_array = (RAW / "empty_array.txt").read_bytes()
        zero = (RAW / "zero_byte.txt").read_bytes()
        self.assertEqual((empty_object, len(empty_object)), (b"{}", 2))
        self.assertEqual((empty_array, len(empty_array)), (b"[]", 2))
        self.assertEqual(len(zero), 0)
        self.assertEqual(RECEIPTS.assess_payload(empty_object)["read_status"], "valid_zero")
        self.assertEqual(RECEIPTS.assess_payload(empty_array)["json_validation"], "valid_zero")
        self.assertEqual(RECEIPTS.assess_payload(zero)["read_status"], "actual_empty")
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "valid_zero", "utf8_byte_length": 2, "json_validation": "valid_zero"},
            empty_object,
        ), [])
        self.assertEqual(RECEIPTS.payload_consistency_errors(
            {"read_status": "empty", "utf8_byte_length": 0, "json_validation": "empty"},
            zero,
        ), [])
        self.assertTrue(RECEIPTS.payload_consistency_errors(
            {"read_status": "empty", "utf8_byte_length": 0, "json_validation": "empty"},
            empty_object,
        ))
        legacy_empty = _pin(
            path="data/last_run_status.json",
            transport="contents",
            read_status="empty",
            utf8_byte_length=0,
            blob_identity=None,
            json_validation="empty",
        )
        self.assertEqual(_status(
            [legacy_empty],
            _repos(china_commodities=_resolved(PIN_C, "empty")),
        ), [])
        confused = dict(legacy_empty, read_status="valid_zero", utf8_byte_length=0, json_validation="empty")
        confused_errors = _status([confused], _repos(china_commodities=_resolved(PIN_C, "valid_zero")))
        self.assertTrue(any("valid_zero_requires_bytes" in item for item in confused_errors))

    def test_contents_envelope_taxonomy_covers_base64_and_malformed_payload(self):
        encoded = base64.b64encode(b"{}").decode()
        parsed = RECEIPTS.parse_contents_envelope({
            "encoding": "base64",
            "content": encoded[:2] + "\n" + encoded[2:],
            "sha": BLOB,
            "size": 2,
        })
        self.assertEqual(parsed["errors"], [])
        self.assertEqual(parsed["read_status"], "valid_zero")
        self.assertEqual(parsed["utf8_byte_length"], 2)
        self.assertEqual(parsed["blob_identity"], BLOB)
        bad = RECEIPTS.parse_contents_envelope({"encoding": "base64", "content": "!!!!", "sha": BLOB})
        self.assertIn("bad_base64", bad["errors"])
        self.assertNotIn("truncated", bad["errors"])
        malformed = RECEIPTS.parse_contents_envelope({
            "encoding": "base64",
            "content": base64.b64encode(b"{nope}").decode(),
            "size": 6,
        })
        self.assertEqual(malformed["read_status"], "parse_error")
        self.assertNotIn("bad_base64", malformed["errors"])
        self.assertEqual(malformed["utf8_byte_length"], 6)
        truncated = RECEIPTS.parse_contents_envelope({
            "encoding": "base64",
            "content": base64.b64encode(b'{"a":').decode(),
            "size": 99,
        })
        self.assertEqual(truncated["read_status"], "truncated")
        self.assertIn("size_mismatch", truncated["errors"])
        self.assertEqual(
            RECEIPTS.parse_contents_envelope({"encoding": "utf-8", "content": "", "size": 0})["read_status"],
            "actual_empty",
        )

    def test_truncated_and_bad_json_are_not_successful_reads(self):
        truncated = (RAW / "truncated_object.txt").read_bytes()
        bad = (RAW / "bad_json.txt").read_bytes()
        self.assertEqual(RECEIPTS.assess_payload(truncated)["read_status"], "truncated")
        self.assertEqual(RECEIPTS.assess_payload(bad)["read_status"], "parse_error")
        self.assertTrue(RECEIPTS.payload_consistency_errors(
            {"read_status": "ok", "utf8_byte_length": len(truncated), "json_validation": "object"},
            truncated,
        ))
        claimed_ok = _pin(
            path="data/radar_latest.json",
            transport="contents",
            read_status="truncated",
            json_validation="object",
            utf8_byte_length=len(truncated),
            blob_identity=None,
        )
        errors = _status([claimed_ok], _repos(china_commodities=_resolved(PIN_C, "truncated")))
        self.assertTrue(any("unparsed_json_cannot_be_ok" in item for item in errors))

    def test_permission_not_found_and_read_failed_do_not_claim_bytes(self):
        permission = {
            "repo": "china_options",
            "repository": "farfromexact/China-Options-Engine",
            "path": "data/radar_latest.json",
            "cutoff_sha": PIN_O,
            "observed_sha": PIN_O,
            "read_status": "permission_error",
        }
        failed = {
            "repo": "china_stock",
            "repository": "farfromexact/China-Stock-Engine",
            "path": "data/latest/manifest.json",
            "cutoff_sha": PIN_S,
            "observed_sha": PIN_S,
            "read_status": "read_failed",
            "scope": "per_path",
            "actual_tools": {"contents": "absent", "blob": "read_failed"},
        }
        missing = {
            "repo": "china_options",
            "path": "data/radar_history.json",
            "cutoff_sha": PIN_O,
            "observed_sha": PIN_O,
            "read_status": "missing",
        }
        repos = _repos(
            china_options=_resolved(PIN_O, "permission"),
            china_stock=_resolved(PIN_S, "read_failed"),
        )
        self.assertEqual(_status([permission, failed, _pin()], repos), [])
        self.assertEqual(RECEIPTS.normalize_status("missing"), "not_found")
        self.assertEqual(RECEIPTS.normalize_status("permission"), "permission_denied")
        self.assertEqual(RECEIPTS.normalize_status("empty"), "actual_empty")
        lying = dict(permission, json_validation="object", utf8_byte_length=10, blob_identity=BLOB)
        errors = _status([lying, failed, _pin()], repos)
        self.assertTrue(any("permission_denied must not claim a parsed payload" in item for item in errors))
        missing_errors = _status([missing, failed, _pin()], _repos(
            china_options=_resolved(PIN_O, "missing"),
            china_stock=_resolved(PIN_S, "read_failed"),
        ))
        self.assertEqual(missing_errors, [])
        self.assertNotEqual(RECEIPTS.normalize_status("missing"), RECEIPTS.normalize_status("read_failed"))

    def test_head_move_is_metadata_and_not_a_pinned_tree_member(self):
        repos = _repos(china_commodities=_resolved(PIN_C, "ok", head_changed_after_pin=HEAD))
        followup = _pin(
            role="isolated_followup",
            used_in_report=False,
            observed_sha=HEAD,
            path="data/radar_latest.json",
            transport="contents",
            utf8_byte_length=None,
            blob_identity=None,
            json_validation=None,
        )
        self.assertEqual(_status([followup, _pin()], repos), [])
        self.assertFalse(any("post_cutoff" in item for item in _status([followup, _pin()], repos)))
        contaminated = _pin(observed_sha=HEAD)
        errors = _status([contaminated], repos)
        self.assertTrue(any("not_in_pinned_tree" in item for item in errors))
        self.assertTrue(any("head_move_used_in_report" in item for item in errors))
        self.assertFalse(any("post_cutoff_pin" in item for item in errors))
        used = dict(followup, used_in_report=True)
        self.assertTrue(any("followup_used_in_report" in item for item in _status([used, _pin()], repos)))

    def test_calendar_not_started_can_follow_a_successful_read(self):
        repos = _repos(china_commodities=_resolved(PIN_C, "ok", calendar="not_started"))
        errors = _status([_pin(calendar="not_started")], repos, edition="morning", night=False)
        self.assertEqual(errors, [])
        self.assertFalse(any("not_started repo has a successful receipt" in item for item in errors))
        denied = _repos(china_commodities=_resolved(PIN_C, "not_started"))
        denied_errors = _status([_pin()], denied, edition="morning", night=False)
        self.assertTrue(any("timing_is_not_read_status:not_started" in item for item in denied_errors))
        self.assertFalse(any("not_started repo has a successful receipt" in item for item in denied_errors))

    def test_last_good_needs_its_own_commit_date_and_reason(self):
        good = _resolved(PIN_C, "ok", last_good={
            "last_good_commit_sha": LAST,
            "trade_date": "2026-11-05",
            "reason": "previous verified session",
        })
        self.assertEqual(_status([_pin()], _repos(china_commodities=good), edition="morning", night=False), [])
        same_pin = _resolved(PIN_C, "ok", last_good={
            "last_good_commit_sha": PIN_C,
            "trade_date": "2026-11-05",
            "reason": "same commit as the research pin",
        })
        self.assertTrue(any(
            "last_good_is_research_pin" in item
            for item in _status([_pin()], _repos(china_commodities=same_pin), edition="morning", night=False)
        ))
        date_only = _resolved(PIN_C, "ok", last_good={"date": "2026-11-05"})
        self.assertTrue(any(
            "last_good_incomplete" in item
            for item in _status([_pin()], _repos(china_commodities=date_only), edition="morning", night=False)
        ))
        fresh = _resolved(PIN_C, "ok", freshness="current", last_good={
            "last_good_commit_sha": LAST,
            "trade_date": "2026-11-06",
            "reason": "called last good while current",
        })
        self.assertTrue(any(
            "current_fresh_is_not_last_good" in item
            for item in _status([_pin()], _repos(china_commodities=fresh), edition="morning", night=False)
        ))

    def test_backfill_and_options_previous_trade_day(self):
        backfill = _pin(
            repo="china_stock",
            repository="farfromexact/China-Stock-Engine",
            path="data/latest/manifest.json",
            role="backfill",
            cutoff_sha=PIN_S,
            observed_sha=PIN_S,
            as_of_date="2026-11-05",
            freshness="current",
            transport="blob",
        )
        options = _pin(
            repo="china_options",
            repository="farfromexact/China-Options-Engine",
            path="data/radar_latest.json",
            cutoff_sha=PIN_O,
            observed_sha=PIN_O,
            transport="contents",
            session_role="previous_trade_day",
            market_trade_date="2026-11-05",
            blob_identity="b" * 40,
        )
        repos = _repos(
            china_options=_resolved(PIN_O, "ok"),
            china_stock=_resolved(PIN_S, "ok"),
            china_commodities=_resolved(PIN_C, "permission_denied"),
        )
        errors = _status([backfill, options], repos, edition="morning", night=False)
        self.assertTrue(any("backfill_called_current" in item and "2026-11-05" in item and "2026-11-06" in item
                            for item in errors))
        honest = dict(backfill, freshness="backfill")
        self.assertEqual(_status([honest, options], repos, edition="morning", night=False), [])
        wrong_day = dict(options, market_trade_date="2026-11-06")
        self.assertTrue(any(
            "previous_trade_day_is_report_date" in item
            for item in _status([honest, wrong_day], repos, edition="morning", night=False)
        ))

    def test_three_cutoff_replay_fixture(self):
        fixture = json.loads((ROOT / "tests" / "fixtures" / "engine_read_replay.json").read_text(encoding="utf-8"))
        self.assertEqual(fixture["live_refetch"], "optional_parent_controlled_not_run_in_ci")
        errors = RECEIPTS.protocol_errors(
            fixture["source_status"],
            report_date=fixture["report_date"],
            edition=fixture["edition"],
        )
        self.assertEqual(errors, [])
        repos = fixture["source_status"]["repos"]
        shas = [repos[name]["cutoff_sha"] for name in ("china_options", "china_commodities", "china_stock")]
        self.assertEqual(len(set(shas)), 3)
        self.assertEqual(repos["china_commodities"]["calendar"], "not_started")
        self.assertEqual(repos["china_commodities"]["read_status"], "ok")
        self.assertNotEqual(repos["china_commodities"]["head_changed_after_pin"], repos["china_commodities"]["cutoff_sha"])
        options = fixture["source_status"]["source_receipts"][0]
        stock = fixture["source_status"]["source_receipts"][2]
        self.assertEqual(options["market_trade_date"], "2026-11-05")
        self.assertEqual(options["session_role"], "previous_trade_day")
        self.assertEqual(stock["role"], "backfill")
        self.assertEqual(stock["freshness"], "backfill")
        self.assertEqual(stock["as_of_date"], "2026-11-05")
        stock["freshness"] = "current"
        mutated = RECEIPTS.protocol_errors(
            fixture["source_status"],
            report_date="2026-11-06",
            edition="morning",
        )
        self.assertTrue(any("backfill_called_current" in item for item in mutated))

    def test_night_session_timing_and_per_path_failure(self):
        morning = _status([_pin()], edition="commodities_morning")
        self.assertEqual(morning, [])
        evening_claims_complete = _night("commodities_evening", PIN_C, session_timing="completed")
        self.assertTrue(any(
            "night_session_timing:not_due" in item
            for item in _status([_pin(), evening_claims_complete], night=False)
        ))
        official = _night("commodities_morning", PIN_C, official_night_close_verified=True)
        self.assertTrue(any(
            "vendor_snapshot_is_not_official_close" in item
            for item in _status([_pin(), official], edition="commodities_morning", night=False)
        ))
        failed_night = _night(
            "commodities_evening",
            PIN_C,
            read_status="read_failed",
            scope="per_path",
            ordinary_contents="incomplete",
            transport="contents",
            utf8_byte_length=None,
            blob_identity=None,
            json_validation=None,
            actual_tools={"contents": "incomplete", "blob": "read_failed", "raw": "absent"},
        )
        self.assertEqual(_status([_pin(), failed_night], night=False), [])
        blanket = _repos(china_commodities=_resolved(PIN_C, "read_failed"))
        self.assertTrue(any(
            "per_path_failure_blankets_repo" in item
            for item in _status([_pin(), failed_night], blanket, night=False)
        ))

    def test_pin_failed_only_before_a_sha_exists(self):
        unresolved = _pin(read_status="pin_failed", cutoff_sha=None, observed_sha=None,
                          utf8_byte_length=None, blob_identity=None, json_validation=None, transport=None)
        repos = _repos(china_commodities={"read_status": "pin_failed"})
        self.assertEqual(_status([unresolved], repos, edition="morning", night=False), [])
        late = dict(unresolved, cutoff_sha=PIN_C, observed_sha=PIN_C)
        self.assertTrue(any(
            "pin_failed_has_sha" in item
            for item in _status([late], repos, edition="morning", night=False)
        ))

    def test_ordinary_incomplete_reread_or_per_path_failure(self):
        incomplete = _pin(ordinary_contents="incomplete", transport="contents")
        self.assertTrue(any(
            "incomplete_needs_same_sha_reread_or_per_path_failure" in item
            for item in _status([incomplete])
        ))
        recovered = _pin(ordinary_contents="incomplete", transport="raw")
        self.assertEqual(_status([recovered]), [])
        compact = _pin(transport="compact")
        self.assertTrue(any("big_contents_required" in item for item in _status([compact])))

    def test_cutoff_resolution_uses_committer_date_per_repo(self):
        late = _resolved(PIN_C, "ok", commit_timestamp="2026-11-06T00:00:00Z")
        self.assertTrue(any(
            "commit_after_cutoff" in item
            for item in _status([_pin()], _repos(china_commodities=late), edition="morning", night=False)
        ))
        author = _resolved(PIN_C, "ok", commit_timestamp_source="author_date")
        self.assertTrue(any(
            "cutoff_must_use_committer_date" in item
            for item in _status([_pin()], _repos(china_commodities=author), edition="morning", night=False)
        ))
        other = _pin(cutoff_sha=HEAD, observed_sha=HEAD)
        self.assertTrue(any(
            "pinned sha differs inside the repo" in item
            for item in _status([_pin(), other], edition="morning", night=False)
        ))
        self.assertIn("repo_not_attempted:china_stock", _status(
            [_pin()],
            {key: value for key, value in _repos().items() if key != "china_stock"},
            edition="evening",
        ))

    def test_legacy_and_unversioned_receipts_are_not_enforced(self):
        self.assertEqual(RECEIPTS.protocol_errors(
            {"source_receipts": [{"read_status": "ok"}], "repos": {}},
            report_date="2026-11-06",
            edition="morning",
        ), [])
        self.assertEqual(RECEIPTS.protocol_errors(
            {"engine_read_protocol": "other", "source_receipts": [{"read_status": "not_started"}]},
            edition="evening",
        ), [])
        self.assertEqual(RECEIPTS.protocol_errors(["ok", "missing"], edition="morning"), [])
        self.assertEqual(RECEIPTS.protocol_errors(None), [])

    def test_validator_source_does_not_fetch_github(self):
        source = (ROOT / "scripts" / "engine_read_receipts.py").read_text(encoding="utf-8")
        for token in ("urllib", "subprocess", "requests", "github.com", "socket"):
            self.assertNotIn(token, source)

    def test_prompt_copies_use_canonical_read_terms(self):
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
            self.assertIn("actual_empty", text, name)
            self.assertIn("permission_denied", text, name)
            self.assertIn("not_found", text, name)
            self.assertIn("not_started", text, name)
            self.assertIn("head_changed_after_pin", text, name)
            self.assertIn("committer date", text, name)
            self.assertIn("Scheduled Task", text, name)
        for name in ("radar_morning.md", "radar_evening.md"):
            for repo in RECEIPTS.REPOS.values():
                self.assertIn(repo, prompts[name], name)
            self.assertIn("三个引擎仓库", prompts[name])
        for name in ("commodities_morning.md", "commodities_evening.md"):
            self.assertIn("data/night_session/latest.json", prompts[name])
            self.assertIn("actual_tools", prompts[name])
            self.assertIn("not_due", prompts[name])
            self.assertIn("vendor_snapshot", prompts[name])
        self.assertNotIn('"read_status": "not_started"', protocol)
        self.assertIn("2266923", protocol)
        self.assertIn("1612360", protocol)
        self.assertIn(VERIFIED_COMMIT, protocol)
        self.assertIn(REPORT_BLOB, protocol)
        self.assertIn(NIGHT_BLOB, protocol)
        self.assertIn("不访问 GitHub", protocol)
        self.assertIn("committer", protocol)
        self.assertNotIn(old, protocol)

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
            source_status = {
                "engine_read_protocol": RECEIPTS.PROTOCOL_VERSION,
                "repos": _repos(),
                "source_receipts": [_pin(blob_identity="nope"), _night(edition, PIN_C)],
            }
            report = {
                "report_date": day,
                "edition": edition,
                "archive": {"archive_status": "success"},
                "source_status": source_status,
            }
            self._write_bundle(root, entry, report, config, stem)
            result = self._health(root)
            self.assertFalse(result["ok"])
            self.assertTrue(any(item["code"] == "source_receipt" for item in result["errors"]))

            report["source_status"]["source_receipts"] = [_pin(), _night(edition, PIN_C)]
            self._write_bundle(root, entry, report, config, stem)
            consistent = self._health(root)
            self.assertTrue(consistent["ok"], consistent["errors"])
            self.assertFalse(any(item["code"] == "source_receipt" for item in consistent["errors"]))

            report["source_status"] = {"source_receipts": [{"read_status": "not_started"}]}
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
