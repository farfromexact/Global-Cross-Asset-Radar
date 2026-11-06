"""Consistency checks for optional engine-read receipts.

This module does not fetch GitHub, clone engine repositories, or decide whether
a market snapshot is fresh. ChatGPT Scheduled Tasks must not be required to run
it. Daily CI calls it only when a report explicitly sets
``source_status.engine_read_protocol`` to ``engine_read_2026-11-06``.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROTOCOL_VERSION = "engine_read_2026-11-06"
REPOS = {
    "china_options": "farfromexact/China-Options-Engine",
    "china_commodities": "farfromexact/China-Commodities-Engine",
    "china_stock": "farfromexact/China-Stock-Engine",
}
EDITIONS = {"morning", "evening", "commodities_morning", "commodities_evening"}
COMMODITY_EDITIONS = {"commodities_morning", "commodities_evening"}
STATUS_ALIASES = {
    "ok": "ok",
    "missing": "missing",
    "empty": "empty",
    "truncated": "truncated",
    "parse_error": "parse_error",
    "stale": "stale",
    "permission_error": "permission",
    "permission": "permission",
    "read_failed": "read_failed",
    "not_started": "not_started",
    "valid_zero": "valid_zero",
    "isolated": "isolated",
}
SUCCESS_STATUSES = {"ok", "valid_zero"}
NO_PAYLOAD_STATUSES = {"missing", "permission", "read_failed", "not_started", "isolated"}
BIG_PATH_MARKERS = (
    "report_input_latest.json",
    "opportunity_inputs_latest.json",
    "data/latest.json",
    "radar_history.json",
    "surface_latest.json",
    "night_session/latest.json",
    "options/latest.json",
)
_FALLBACK_DESCRIPTORS = {
    "pinned_utf8_2266923": {
        "utf8_byte_length": 2266923,
        "blob_identity": "canonical-blob:2266923",
        "json_validation": "object",
    },
    "pinned_utf8_1612360": {
        "utf8_byte_length": 1612360,
        "blob_identity": "canonical-blob:1612360",
        "json_validation": "object",
    },
}
_DESCRIPTOR_CACHE: dict[str, dict[str, Any]] | None = None


def trusted_descriptors() -> dict[str, dict[str, Any]]:
    """Return pinned size descriptors. Never contacts GitHub."""
    global _DESCRIPTOR_CACHE
    if _DESCRIPTOR_CACHE is not None:
        return _DESCRIPTOR_CACHE
    path = Path(__file__).resolve().parents[1] / "tests" / "fixtures" / "engine_read_canonical.json"
    loaded: Any
    try:
        loaded = json.loads(path.read_text(encoding="utf-8")).get("descriptors")
    except (OSError, UnicodeError, json.JSONDecodeError, AttributeError):
        loaded = None
    if not isinstance(loaded, dict) or not loaded:
        _DESCRIPTOR_CACHE = dict(_FALLBACK_DESCRIPTORS)
        return _DESCRIPTOR_CACHE
    _DESCRIPTOR_CACHE = loaded
    return _DESCRIPTOR_CACHE


def normalize_status(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    return STATUS_ALIASES.get(value.strip())


def assess_payload(raw: bytes) -> dict[str, Any]:
    """Classify exact UTF-8 bytes. Length is ``len(raw)``, not a character count."""
    length = len(raw)
    if length == 0:
        return {"read_status": "empty", "utf8_byte_length": 0, "json_validation": "empty"}
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
    if receipt.get("json_validation") != assessed["json_validation"]:
        errors.append(
            f"payload_json_validation:{receipt.get('json_validation')}!={assessed['json_validation']}"
        )
    return errors


def protocol_errors(
    source_status: Any,
    *,
    report_date: str | None = None,
    edition: str | None = None,
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

    parsed: list[dict[str, Any]] = []
    for index, receipt in enumerate(receipts):
        if not isinstance(receipt, dict):
            errors.append(f"source_receipts[{index}] is not an object")
            continue
        parsed.append(receipt)
        for item in _receipt_errors(receipt, report_date=report_date, edition=edition):
            errors.append(f"source_receipts[{index}]: {item}")

    for key, repo in repos.items():
        for item in _repo_errors(str(key), repo, parsed):
            errors.append(item)
    return errors


def _byte_length(value: Any) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        return None
    return value


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


def _claims_payload(receipt: dict[str, Any]) -> bool:
    if receipt.get("json_validation") in {"object", "array", "valid_zero", "scalar"}:
        return True
    length = _byte_length(receipt.get("utf8_byte_length"))
    identity = receipt.get("blob_identity")
    return length is not None and length > 0 and isinstance(identity, str) and bool(identity)


def _is_research_pin(receipt: dict[str, Any]) -> bool:
    status = normalize_status(receipt.get("read_status"))
    if status not in SUCCESS_STATUSES:
        return False
    if receipt.get("isolated") is True or receipt.get("role") in {"isolated_post_cutoff", "backfill"}:
        return False
    cutoff = receipt.get("cutoff_sha")
    observed = receipt.get("observed_sha")
    if not isinstance(cutoff, str) or not cutoff:
        return False
    if observed not in (None, cutoff):
        return False
    return receipt.get("role") in (None, "research_pin")


def _receipt_errors(
    receipt: dict[str, Any],
    *,
    report_date: str | None,
    edition: str | None,
) -> list[str]:
    status = normalize_status(receipt.get("read_status"))
    errors = _common_errors(receipt, status, report_date=report_date, edition=edition)
    if status is None:
        errors.append("read_status is missing or unknown")
        return errors
    if status in NO_PAYLOAD_STATUSES:
        if _claims_payload(receipt):
            errors.append(f"{status} must not claim a parsed payload")
        return errors
    if status == "stale":
        if receipt.get("freshness") == "current":
            errors.append("stale alias conflicts with freshness current")
        if _claims_payload(receipt):
            errors.extend(_success_errors(receipt, "ok", edition))
        return errors
    if status == "empty":
        length = _byte_length(receipt.get("utf8_byte_length"))
        if length != 0:
            errors.append("empty_is_zero_bytes")
        if receipt.get("json_validation") != "empty":
            errors.append("empty_is_not_valid_zero")
        return errors
    if status in {"truncated", "parse_error"}:
        if receipt.get("json_validation") != status:
            errors.append("unparsed_json_cannot_be_ok")
        return errors
    if status in SUCCESS_STATUSES:
        errors.extend(_success_errors(receipt, status, edition))
    return errors


def _common_errors(
    receipt: dict[str, Any],
    status: str | None,
    *,
    report_date: str | None,
    edition: str | None,
) -> list[str]:
    errors: list[str] = []
    cutoff = receipt.get("cutoff_sha")
    observed = receipt.get("observed_sha")
    if (
        isinstance(cutoff, str)
        and isinstance(observed, str)
        and cutoff
        and observed
        and observed != cutoff
    ):
        isolated = (
            receipt.get("isolated") is True
            and receipt.get("role") == "isolated_post_cutoff"
            and status == "isolated"
        )
        if not isolated:
            errors.append("post_cutoff_pin")

    reason = _text_blob(receipt.get("reason"), receipt.get("incomplete_reason"))
    if status in {"missing", "empty"} and any(
        token in reason for token in ("file_too_large", "too large", "too_large", "文件过大", "1mb", "1 mb")
    ):
        errors.append("file_too_large_is_not_missing")
    if receipt.get("assumed_max_bytes") in {1048576, 1_000_000, "1MB", "1mb"}:
        errors.append("assumed_1mb_cap")

    descriptor_id = receipt.get("canonical_descriptor")
    if descriptor_id is not None:
        known = trusted_descriptors().get(descriptor_id)
        if not isinstance(known, dict):
            errors.append("unknown_canonical_descriptor")
        else:
            if receipt.get("utf8_byte_length") != known.get("utf8_byte_length"):
                errors.append("canonical_size_mismatch")
            if receipt.get("blob_identity") != known.get("blob_identity"):
                errors.append("canonical_blob_mismatch")
            if status in SUCCESS_STATUSES and receipt.get("json_validation") != known.get("json_validation"):
                errors.append("canonical_json_mismatch")

    if receipt.get("role") == "backfill" and receipt.get("freshness") == "current":
        errors.append(
            f"backfill_called_current: as_of {receipt.get('as_of_date')} is not current for {report_date}"
        )

    if receipt.get("ordinary_contents") == "incomplete":
        same_sha = isinstance(cutoff, str) and observed == cutoff
        if receipt.get("transport") not in {"blob", "raw"} or not same_sha:
            errors.append("incomplete_requires_same_sha_blob_or_raw")

    if (
        edition in COMMODITY_EDITIONS
        and status == "ok"
        and _is_big_path(receipt.get("path"))
        and receipt.get("transport") == "compact"
    ):
        errors.append("big_contents_required")
    return errors


def _success_errors(receipt: dict[str, Any], status: str, edition: str | None) -> list[str]:
    errors: list[str] = []
    cutoff = receipt.get("cutoff_sha")
    if not isinstance(cutoff, str) or not cutoff:
        errors.append("cutoff_sha is required")
    length = _byte_length(receipt.get("utf8_byte_length"))
    identity = receipt.get("blob_identity")
    if not isinstance(identity, str) or not identity.strip():
        errors.append("blob_identity is required")
    if status == "valid_zero":
        if length is None or length <= 0:
            errors.append("valid_zero_requires_bytes")
        if receipt.get("json_validation") != "valid_zero":
            errors.append("valid_zero_json_validation")
    elif status == "ok":
        if length is None or length <= 0:
            errors.append("ok_requires_utf8_byte_length")
        if receipt.get("json_validation") not in {"object", "array", "scalar"}:
            errors.append("ok_json_validation")
    if (
        edition in COMMODITY_EDITIONS
        and _is_big_path(receipt.get("path"))
        and receipt.get("transport") not in {"contents", "blob", "raw"}
    ):
        errors.append("big_contents_required")
    return errors


def _repo_errors(key: str, repo: Any, receipts: list[dict[str, Any]]) -> list[str]:
    if not isinstance(repo, dict):
        return [f"{key}: repo entry is not an object"]
    status = normalize_status(repo.get("read_status"))
    if status is None:
        return [f"{key}: read_status is missing or unknown"]
    errors: list[str] = []
    mine = [receipt for receipt in receipts if _repo_key(receipt) == key]
    if status == "not_started" and any(_is_research_pin(receipt) for receipt in mine):
        errors.append(f"{key}: not_started repo has a successful receipt")
    if status in {"permission", "read_failed", "missing"} and any(
        _is_research_pin(receipt) for receipt in mine
    ):
        errors.append(f"{key}: {status} repo also claims a successful read")
    if status in SUCCESS_STATUSES and not any(_is_research_pin(receipt) for receipt in mine):
        errors.append(f"{key}: successful repo has no same-SHA research receipt")
    if status in SUCCESS_STATUSES:
        cutoff = repo.get("cutoff_sha")
        if isinstance(cutoff, str) and cutoff:
            mismatched = [
                receipt for receipt in mine
                if _is_research_pin(receipt) and receipt.get("cutoff_sha") != cutoff
            ]
            if mismatched:
                errors.append(f"{key}: research receipt cutoff_sha does not match the repo pin")
    cutoff = repo.get("cutoff_sha")
    last_good = repo.get("last_good")
    if isinstance(last_good, str) and isinstance(cutoff, str) and last_good == cutoff:
        errors.append(f"{key}: last_good_is_pinned_sha")
    if isinstance(last_good, dict) and isinstance(cutoff, str):
        sha = last_good.get("sha") or last_good.get("cutoff_sha")
        has_date = bool(last_good.get("date") or last_good.get("market_date"))
        if sha == cutoff and not has_date:
            errors.append(f"{key}: last_good_is_pinned_sha")
    if status == "stale" and repo.get("freshness") == "current":
        errors.append(f"{key}: stale alias conflicts with freshness current")
    return errors
