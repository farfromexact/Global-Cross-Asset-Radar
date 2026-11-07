"""Consistency checks for optional engine-read receipts.

This module does not fetch GitHub and does not decide whether a market is open.
ChatGPT Scheduled Tasks must not run it. Daily CI calls it only when a report
sets ``source_status.engine_read_protocol`` to ``engine_read_2026-11-06``.

Verified pin metadata lives in ``config/engine_read_evidence.json``. That file is
the trust source. A missing or malformed evidence file is an error for receipts
that cite it; nothing is substituted from tests or from an in-code fallback.
"""
from __future__ import annotations

import base64
import binascii
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


PROTOCOL_VERSION = "engine_read_2026-11-06"
REPOS = {
    "china_options": "farfromexact/China-Options-Engine",
    "china_commodities": "farfromexact/China-Commodities-Engine",
    "china_stock": "farfromexact/China-Stock-Engine",
}
EDITIONS = {"morning", "evening", "commodities_morning", "commodities_evening"}
COMMODITY_EDITIONS = {"commodities_morning", "commodities_evening"}
NIGHT_PATH = "data/night_session/latest.json"
EVIDENCE_PATH = Path(__file__).resolve().parents[1] / "config" / "engine_read_evidence.json"
_SHA40 = re.compile(r"^[0-9a-f]{40}$")
_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# Canonical read outcomes. Legacy aliases collapse onto these and nowhere else.
READ_STATUS_ALIASES = {
    "ok": "ok",
    "valid_zero": "valid_zero",
    "actual_empty": "actual_empty",
    "empty": "actual_empty",
    "truncated": "truncated",
    "parse_error": "parse_error",
    "not_found": "not_found",
    "missing": "not_found",
    "permission_denied": "permission_denied",
    "permission_error": "permission_denied",
    "permission": "permission_denied",
    "read_failed": "read_failed",
    "pin_failed": "pin_failed",
}
JSON_VALIDATION_ALIASES = {
    "object": "object",
    "array": "array",
    "scalar": "scalar",
    "valid_zero": "valid_zero",
    "actual_empty": "actual_empty",
    "empty": "actual_empty",
    "truncated": "truncated",
    "parse_error": "parse_error",
}
# Calendar / data-timing words. They are not read_status values.
TIMING_WORDS = {"not_started", "not_due", "stale", "last_good"}
SUCCESS_STATUSES = {"ok", "valid_zero"}
NO_PAYLOAD_STATUSES = {"not_found", "permission_denied", "read_failed", "pin_failed"}
PARSED_JSON = {"object", "array", "valid_zero", "scalar"}
BIG_PATH_MARKERS = (
    "report_input_latest.json",
    "opportunity_inputs_latest.json",
    "data/latest.json",
    NIGHT_PATH,
    "radar_history.json",
    "surface_latest.json",
    "options/latest.json",
)


def normalize_status(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    return READ_STATUS_ALIASES.get(value.strip())


def normalize_json_validation(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    return JSON_VALIDATION_ALIASES.get(value.strip())


def _sha40(value: Any) -> bool:
    return isinstance(value, str) and _SHA40.fullmatch(value) is not None


def _sha256(value: Any) -> bool:
    return isinstance(value, str) and _SHA256.fullmatch(value) is not None


def _byte_length(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    return value


def load_verified_evidence(path: Path | None = None) -> dict[str, Any]:
    """Load production pin evidence. Raises if the file is missing or malformed."""
    target = path or EVIDENCE_PATH
    try:
        data = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"evidence_file_unusable: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("evidence_file_unusable: evidence is not an object")
    commit = data.get("commit")
    paths = data.get("paths")
    if not _sha40(commit) or not isinstance(paths, dict) or not paths:
        raise ValueError("evidence_file_unusable: commit or paths missing")
    if data.get("not_original_report_visibility") is not True:
        raise ValueError("evidence_file_unusable: retrospective visibility flag missing")
    for rel, item in paths.items():
        if not isinstance(rel, str) or not isinstance(item, dict):
            raise ValueError("evidence_file_unusable: path entry is malformed")
        length = item.get("utf8_byte_length")
        if isinstance(length, bool) or not isinstance(length, int) or length < 0:
            raise ValueError(f"evidence_file_unusable: {rel} length")
        if not _sha40(item.get("blob_identity")) or not _sha256(item.get("sha256")):
            raise ValueError(f"evidence_file_unusable: {rel} identity")
    return data


def assess_payload(raw: bytes) -> dict[str, Any]:
    """Classify exact UTF-8 bytes. Length is ``len(raw)``, not a character count."""
    length = len(raw)
    if length == 0:
        return {"read_status": "actual_empty", "utf8_byte_length": 0, "json_validation": "actual_empty"}
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return {"read_status": "parse_error", "utf8_byte_length": length, "json_validation": "parse_error"}
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        stripped = text.strip()
        kind = "truncated" if stripped[:1] in "{[" and stripped[-1:] not in "}]" else "parse_error"
        return {"read_status": kind, "utf8_byte_length": length, "json_validation": kind}
    if value == {} or value == []:
        return {"read_status": "valid_zero", "utf8_byte_length": length, "json_validation": "valid_zero"}
    if isinstance(value, dict):
        kind = "object"
    elif isinstance(value, list):
        kind = "array"
    else:
        kind = "scalar"
    return {"read_status": "ok", "utf8_byte_length": length, "json_validation": kind}


def parse_contents_envelope(envelope: Any) -> dict[str, Any]:
    """Decode a contents-API envelope already in memory. Does not fetch."""
    if not isinstance(envelope, dict):
        return {"errors": ["envelope_not_object"], "read_status": None, "raw": None, "blob_identity": None}
    errors: list[str] = []
    blob = envelope.get("sha")
    if blob is not None and not _sha40(blob):
        errors.append("blob_sha_invalid")
        blob = None
    encoding = envelope.get("encoding") or "utf-8"
    content = envelope.get("content")
    raw: bytes | None = None
    if encoding == "base64":
        if not isinstance(content, str):
            errors.append("bad_base64")
        else:
            try:
                raw = base64.b64decode("".join(content.split()), validate=True)
            except (ValueError, binascii.Error):
                errors.append("bad_base64")
    elif encoding in {"utf-8", "utf8"}:
        if isinstance(content, str):
            raw = content.encode("utf-8")
        elif isinstance(content, bytes):
            raw = content
        else:
            errors.append("malformed_payload")
    else:
        errors.append("unsupported_encoding")
    result: dict[str, Any] = {"errors": errors, "blob_identity": blob, "raw": raw}
    if raw is None:
        result["read_status"] = "parse_error" if errors else None
        return result
    declared = envelope.get("size")
    if isinstance(declared, int) and not isinstance(declared, bool) and declared != len(raw):
        errors.append("size_mismatch")
    result.update(assess_payload(raw))
    return result


def payload_consistency_errors(receipt: dict[str, Any], raw: bytes) -> list[str]:
    """Compare a receipt with bytes already in hand. Does not fetch those bytes."""
    if not isinstance(receipt, dict):
        return ["receipt is not an object"]
    assessed = assess_payload(raw)
    errors: list[str] = []
    actual_status = normalize_status(receipt.get("read_status"))
    if actual_status != assessed["read_status"]:
        errors.append(f"payload_read_status:{actual_status}!={assessed['read_status']}")
    if receipt.get("utf8_byte_length") != assessed["utf8_byte_length"]:
        errors.append(
            f"payload_utf8_byte_length:{receipt.get('utf8_byte_length')}!={assessed['utf8_byte_length']}"
        )
    actual_json = normalize_json_validation(receipt.get("json_validation"))
    if actual_json != assessed["json_validation"]:
        errors.append(f"payload_json_validation:{actual_json}!={assessed['json_validation']}")
    return errors


def protocol_errors(
    source_status: Any,
    *,
    report_date: str | None = None,
    edition: str | None = None,
    evidence_path: Path | None = None,
) -> list[str]:
    """Validate a versioned receipt block. Unversioned legacy values return no errors."""
    if not isinstance(source_status, dict):
        return []
    if source_status.get("engine_read_protocol") != PROTOCOL_VERSION:
        return []

    errors: list[str] = []
    repos = source_status.get("repos")
    if not isinstance(repos, dict):
        errors.append("repos must be an object when engine_read_protocol is set")
        repos = {}
    if edition in EDITIONS:
        for key in REPOS:
            if key not in repos:
                errors.append(f"repo_not_attempted:{key}")

    receipts = source_status.get("source_receipts", [])
    if receipts is None:
        receipts = []
    if not isinstance(receipts, list):
        errors.append("source_receipts must be a list")
        receipts = []

    evidence: dict[str, Any] | None = None
    evidence_error: str | None = None
    if any(isinstance(item, dict) and item.get("verified_commit") for item in receipts):
        try:
            evidence = load_verified_evidence(evidence_path)
        except ValueError as exc:
            evidence_error = str(exc)

    parsed: list[dict[str, Any]] = []
    for index, receipt in enumerate(receipts):
        if not isinstance(receipt, dict):
            errors.append(f"source_receipts[{index}] is not an object")
            continue
        parsed.append(receipt)
        for item in _receipt_errors(
            receipt,
            report_date=report_date,
            edition=edition,
            evidence=evidence,
            evidence_error=evidence_error,
        ):
            errors.append(f"source_receipts[{index}]: {item}")

    for key, repo in repos.items():
        for item in _repo_errors(str(key), repo, parsed, report_date=report_date):
            errors.append(item)
    if edition in COMMODITY_EDITIONS:
        errors.extend(_night_errors(edition, parsed))
    return errors


def _repo_key(receipt: dict[str, Any]) -> str | None:
    repo = receipt.get("repo")
    if repo in REPOS:
        return str(repo)
    repository = receipt.get("repository")
    if isinstance(repository, str):
        for key, full_name in REPOS.items():
            if repository == full_name or repository.endswith("/" + full_name.split("/", 1)[1]):
                return key
    return None


def _text_blob(*values: Any) -> str:
    return " ".join(str(value) for value in values if value is not None).lower()


def _is_big_path(path: Any) -> bool:
    if not isinstance(path, str):
        return False
    return any(marker in path for marker in BIG_PATH_MARKERS)


def _is_night_path(path: Any) -> bool:
    return isinstance(path, str) and (path == NIGHT_PATH or path.endswith("/" + NIGHT_PATH))


def _claims_parsed_payload(receipt: dict[str, Any]) -> bool:
    if normalize_json_validation(receipt.get("json_validation")) in PARSED_JSON:
        return True
    length = _byte_length(receipt.get("utf8_byte_length"))
    return length is not None and length > 0 and _sha40(receipt.get("blob_identity"))


def _unused_followup(receipt: dict[str, Any]) -> bool:
    return receipt.get("role") == "isolated_followup" and receipt.get("used_in_report") is False


def _is_pinned_read(receipt: dict[str, Any]) -> bool:
    """A same-SHA read that may support the repo. Backfill counts; a later HEAD does not."""
    if _unused_followup(receipt):
        return False
    status = normalize_status(receipt.get("read_status"))
    if status not in SUCCESS_STATUSES and status != "actual_empty":
        return False
    if receipt.get("role") not in (None, "research_pin", "backfill"):
        return False
    cutoff = receipt.get("cutoff_sha")
    observed = receipt.get("observed_sha")
    return _sha40(cutoff) and observed == cutoff


def _instant(value: Any, zone: str | None) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is not None:
        return parsed
    if not zone:
        return None
    try:
        return parsed.replace(tzinfo=ZoneInfo(zone))
    except (KeyError, ValueError):
        return None


def _receipt_errors(
    receipt: dict[str, Any],
    *,
    report_date: str | None,
    edition: str | None,
    evidence: dict[str, Any] | None,
    evidence_error: str | None,
) -> list[str]:
    if _unused_followup(receipt):
        return []
    if receipt.get("role") == "isolated_followup":
        return ["followup_used_in_report"]
    raw_status = receipt.get("read_status")
    status = normalize_status(raw_status)
    errors = _sha_errors(receipt, status)
    errors.extend(_common_errors(receipt, status, report_date=report_date, edition=edition))
    errors.extend(_evidence_errors(receipt, evidence, evidence_error))
    if isinstance(raw_status, str) and raw_status.strip() in TIMING_WORDS:
        errors.append(f"timing_is_not_read_status:{raw_status.strip()}")
        return errors
    if status is None:
        errors.append("read_status is missing or unknown")
        return errors
    if status == "pin_failed":
        if receipt.get("cutoff_sha") not in (None, ""):
            errors.append("pin_failed_has_sha")
        if _claims_parsed_payload(receipt):
            errors.append("pin_failed must not claim a parsed payload")
        return errors
    if status in NO_PAYLOAD_STATUSES:
        if _claims_parsed_payload(receipt) or receipt.get("json_validation") not in (None, ""):
            errors.append(f"{status} must not claim a parsed payload")
        if receipt.get("blob_identity") not in (None, ""):
            errors.append(f"{status} must not claim blob_identity")
        if status == "read_failed" and receipt.get("scope") != "per_path":
            errors.append("read_failed_scope_per_path")
        return errors
    if status == "actual_empty":
        length = _byte_length(receipt.get("utf8_byte_length"))
        if length != 0:
            errors.append("actual_empty_is_zero_bytes")
        if normalize_json_validation(receipt.get("json_validation")) != "actual_empty":
            errors.append("actual_empty_json_validation")
        return errors
    if status in {"truncated", "parse_error"}:
        if normalize_json_validation(receipt.get("json_validation")) != status:
            errors.append("unparsed_json_cannot_be_ok")
        return errors
    if status in SUCCESS_STATUSES:
        errors.extend(_success_errors(receipt, status, edition))
    return errors


def _sha_errors(receipt: dict[str, Any], status: str | None) -> list[str]:
    if status == "pin_failed":
        return []
    errors: list[str] = []
    cutoff = receipt.get("cutoff_sha")
    observed = receipt.get("observed_sha")
    if not _sha40(cutoff):
        errors.append("cutoff_sha_not_40_hex")
    if not _sha40(observed):
        errors.append("observed_sha_not_40_hex")
    if _sha40(cutoff) and _sha40(observed) and observed != cutoff:
        errors.append("not_in_pinned_tree")
    return errors


def _common_errors(
    receipt: dict[str, Any],
    status: str | None,
    *,
    report_date: str | None,
    edition: str | None,
) -> list[str]:
    errors: list[str] = []
    reason = _text_blob(receipt.get("reason"), receipt.get("incomplete_reason"))
    if status in {"not_found", "actual_empty"} and any(
        token in reason for token in ("file_too_large", "too large", "too_large", "文件过大", "1mb", "1 mb")
    ):
        errors.append("file_too_large_is_not_missing")
    if receipt.get("assumed_max_bytes") in {1048576, 1_000_000, "1MB", "1mb"}:
        errors.append("assumed_1mb_cap")
    if receipt.get("role") == "backfill" and receipt.get("freshness") == "current":
        errors.append(
            f"backfill_called_current: as_of {receipt.get('as_of_date')} is not current for {report_date}"
        )
    if receipt.get("session_role") == "previous_trade_day":
        market_day = receipt.get("market_trade_date")
        if not isinstance(market_day, str):
            errors.append("previous_trade_day_missing")
        else:
            try:
                datetime.fromisoformat(market_day)
            except ValueError:
                errors.append("previous_trade_day_invalid")
            if report_date and market_day == report_date:
                errors.append("previous_trade_day_is_report_date")
    if receipt.get("ordinary_contents") == "incomplete" and not _recovered_or_failed_attempt(receipt, status):
        errors.append("incomplete_needs_same_sha_reread_or_per_path_failure")
    if (
        edition in COMMODITY_EDITIONS
        and status == "ok"
        and _is_big_path(receipt.get("path"))
        and receipt.get("transport") == "compact"
    ):
        errors.append("big_contents_required")
    if receipt.get("original_report_visibility") is True:
        errors.append("retrospective_is_not_report_visibility")
    return errors


def _recovered_or_failed_attempt(receipt: dict[str, Any], status: str | None) -> bool:
    cutoff = receipt.get("cutoff_sha")
    observed = receipt.get("observed_sha")
    same = _sha40(cutoff) and observed == cutoff
    if status in SUCCESS_STATUSES and receipt.get("transport") in {"blob", "raw"} and same:
        return True
    return status == "read_failed" and receipt.get("scope") == "per_path" and same


def _success_errors(receipt: dict[str, Any], status: str, edition: str | None) -> list[str]:
    errors: list[str] = []
    if not _sha40(receipt.get("blob_identity")):
        errors.append("blob_identity_not_40_hex")
    length = _byte_length(receipt.get("utf8_byte_length"))
    if status == "valid_zero":
        if length is None or length <= 0:
            errors.append("valid_zero_requires_bytes")
        if normalize_json_validation(receipt.get("json_validation")) != "valid_zero":
            errors.append("valid_zero_json_validation")
    elif status == "ok":
        if length is None or length <= 0:
            errors.append("ok_requires_utf8_byte_length")
        if normalize_json_validation(receipt.get("json_validation")) not in {"object", "array", "scalar"}:
            errors.append("ok_json_validation")
    if (
        edition in COMMODITY_EDITIONS
        and _is_big_path(receipt.get("path"))
        and receipt.get("transport") not in {"contents", "blob", "raw"}
    ):
        errors.append("big_contents_required")
    return errors


def _evidence_errors(
    receipt: dict[str, Any],
    evidence: dict[str, Any] | None,
    evidence_error: str | None,
) -> list[str]:
    cited = receipt.get("verified_commit")
    if not cited:
        return []
    if evidence_error or evidence is None:
        return [evidence_error or "evidence_file_unusable"]
    if cited != evidence.get("commit"):
        return ["verified_commit_not_in_evidence"]
    path = receipt.get("path")
    known = evidence.get("paths", {}).get(path)
    if not isinstance(known, dict):
        return []
    errors: list[str] = []
    if receipt.get("utf8_byte_length") != known.get("utf8_byte_length"):
        errors.append("canonical_size_mismatch")
    if receipt.get("blob_identity") != known.get("blob_identity"):
        errors.append("canonical_blob_mismatch")
    if receipt.get("sha256") != known.get("sha256"):
        errors.append("canonical_sha256_mismatch")
    return errors


def _night_errors(edition: str | None, receipts: list[dict[str, Any]]) -> list[str]:
    nights = [receipt for receipt in receipts if _is_night_path(receipt.get("path"))]
    if not nights:
        return ["night_path_required"]
    errors: list[str] = []
    expected_timing = "completed" if edition == "commodities_morning" else "not_due"
    for receipt in nights:
        if receipt.get("vendor_snapshot") is not True:
            errors.append("night_vendor_snapshot_required")
        if receipt.get("official_night_close_verified") is not False:
            errors.append("vendor_snapshot_is_not_official_close")
        if receipt.get("session_timing") != expected_timing:
            errors.append(f"night_session_timing:{expected_timing}")
        tools = receipt.get("actual_tools")
        if not isinstance(tools, (dict, list)) or not tools:
            errors.append("actual_tools_required")
    return errors


def _repo_errors(
    key: str,
    repo: Any,
    receipts: list[dict[str, Any]],
    *,
    report_date: str | None,
) -> list[str]:
    if not isinstance(repo, dict):
        return [f"{key}: repo entry is not an object"]
    raw_status = repo.get("read_status")
    status = normalize_status(raw_status)
    if isinstance(raw_status, str) and raw_status.strip() in TIMING_WORDS:
        return [f"{key}: timing_is_not_read_status:{raw_status.strip()}"]
    if status is None:
        return [f"{key}: read_status is missing or unknown"]
    errors: list[str] = []
    mine = [receipt for receipt in receipts if _repo_key(receipt) == key and not _unused_followup(receipt)]
    pinned = [receipt for receipt in mine if _is_pinned_read(receipt)]
    if status == "pin_failed":
        if repo.get("cutoff_sha") not in (None, ""):
            errors.append(f"{key}: pin_failed_has_sha")
        if pinned:
            errors.append(f"{key}: pin_failed repo has a pinned read")
        return errors
    errors.extend(_cutoff_resolution_errors(key, repo))
    if status in NO_PAYLOAD_STATUSES and pinned:
        errors.append(f"{key}: per_path_failure_blankets_repo")
    if status in SUCCESS_STATUSES | {"actual_empty"} and not pinned:
        errors.append(f"{key}: successful repo has no same-SHA pinned read")
    cutoff = repo.get("cutoff_sha")
    if _sha40(cutoff):
        mismatched = [
            receipt for receipt in mine
            if not _unused_followup(receipt)
            and receipt.get("role") != "isolated_followup"
            and _sha40(receipt.get("cutoff_sha"))
            and receipt.get("cutoff_sha") != cutoff
        ]
        if mismatched:
            errors.append(f"{key}: pinned sha differs inside the repo")
    head = repo.get("head_changed_after_pin")
    if head is not None:
        if not _sha40(head):
            errors.append(f"{key}: head_changed_after_pin_not_40_hex")
        elif head != cutoff:
            used = [
                receipt for receipt in mine
                if receipt.get("observed_sha") == head and receipt.get("used_in_report") is not False
            ]
            if used:
                errors.append(f"{key}: head_move_used_in_report")
    errors.extend(_last_good_errors(key, repo, cutoff, report_date=report_date))
    return errors


def _cutoff_resolution_errors(key: str, repo: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not _sha40(repo.get("cutoff_sha")):
        errors.append(f"{key}: per_repo_cutoff_sha_not_40_hex")
    zone = repo.get("cutoff_zone")
    if not isinstance(zone, str) or not zone.strip():
        errors.append(f"{key}: cutoff_zone_required")
        zone = None
    cutoff_at = _instant(repo.get("cutoff_at"), zone if isinstance(zone, str) else None)
    if cutoff_at is None:
        errors.append(f"{key}: cutoff_at_unresolved")
    source = repo.get("commit_timestamp_source")
    if source != "committer_date":
        errors.append(f"{key}: cutoff_must_use_committer_date")
    commit_at = _instant(repo.get("commit_timestamp"), None)
    if commit_at is None:
        errors.append(f"{key}: commit_timestamp_unresolved")
    elif cutoff_at is not None and commit_at > cutoff_at:
        errors.append(f"{key}: commit_after_cutoff")
    return errors


def _last_good_errors(
    key: str,
    repo: dict[str, Any],
    cutoff: Any,
    *,
    report_date: str | None,
) -> list[str]:
    if "last_good" not in repo or repo.get("last_good") is None:
        return []
    last_good = repo.get("last_good")
    if not isinstance(last_good, dict):
        return [f"{key}: last_good_incomplete"]
    errors: list[str] = []
    sha = last_good.get("last_good_commit_sha")
    trade_date = last_good.get("trade_date") or last_good.get("date")
    reason = last_good.get("reason")
    if not _sha40(sha) or not isinstance(reason, str) or not reason.strip():
        errors.append(f"{key}: last_good_incomplete")
    if not isinstance(trade_date, str):
        errors.append(f"{key}: last_good_incomplete")
    else:
        try:
            datetime.fromisoformat(trade_date)
        except ValueError:
            errors.append(f"{key}: last_good_trade_date_invalid")
    if _sha40(sha) and sha == cutoff:
        errors.append(f"{key}: last_good_is_research_pin")
    if repo.get("freshness") == "current" or last_good.get("freshness") == "current":
        errors.append(f"{key}: current_fresh_is_not_last_good")
    if report_date and trade_date == report_date and repo.get("freshness") == "current":
        errors.append(f"{key}: current_fresh_is_not_last_good")
    return errors
