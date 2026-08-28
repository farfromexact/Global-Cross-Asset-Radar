from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

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
            # Some scheduled reports supply one prose claim as a scalar.
            # The archive schema represents claims consistently as a list, so
            # preserve that claim while normalizing the one-item dialect.
            if isinstance(source.get("supported_claims"), str):
                source["supported_claims"] = [source["supported_claims"]]
            # A scheduled report occasionally used prose such as
            # ``official sources enumerated in Markdown`` in the URL slot.
            # Preserve that explanation without allowing it to masquerade as
            # a portable URI in the archive contract.
            url = source.get("url")
            if url is not None and not _compat_is_uri(url):
                source["url_note"] = str(url)
                source["url"] = None
            normalized.append(source)
        elif isinstance(item, str):
            normalized.append({"title": item})
        else:
            normalized.append({"title": str(item)})
    return normalized


def _compat_is_uri(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _compat_curve_definition(value: Any, data: dict[str, Any] | None = None) -> Any:
    """Map the human wording used by the commodity task to the contract label."""
    canonical = "near_minus_next_futures_curve_not_spot_basis"
    if not isinstance(value, str):
        # The 2026-08-20 evening dialect moved the curve label out of
        # ``commodities_tracking.data_quality`` while still publishing curve
        # values in the dashboard.  Recover the metadata only when the report
        # contains concrete curve evidence; otherwise keep the failure visible.
        if isinstance(data, dict):
            text = json.dumps(data, ensure_ascii=False, sort_keys=True).lower()
            if any(token in text for token in ("curve", "backwardation", "contango", "曲线", "近月", "次近月")):
                return canonical
        return value
    if value == canonical:
        return value
    lowered = value.lower()
    if (
        ("curve" in lowered or "曲线" in lowered)
        and ("spot" in lowered or "现货" in lowered)
        and ("near" in lowered or "next" in lowered or "近月" in lowered or "次近月" in lowered)
    ):
        return canonical
    if ("near" in lowered and "next" in lowered) or ("近月" in lowered and "次近月" in lowered):
        return canonical
    return value


def _compat_contract_root(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    text = value.strip().upper()
    match = re.match(r"^([A-Z]{1,4})(?:[A-Z])?\d{3,6}$", text)
    return match.group(1) if match else None


def _compat_contract_from_text(product: str, text: str) -> str | None:
    product = product.strip().upper()
    if not product:
        return None
    # Chinese reports commonly write FU2611/JM2701/FG701 inline in cards.
    # This is only a best-effort identity recovery; if no symbol is present we
    # retain an explicit N/A sentinel rather than inventing a contract.
    match = re.search(rf"\b{re.escape(product)}[A-Z]?\d{{3,6}}\b", text.upper())
    return match.group(0) if match else None


def _compat_mapping_rows(value: Any) -> list[dict[str, Any]]:
    """Turn a keyed summary map into the canonical row-array dialect.

    Scheduled reports have used both ``[{"asset": ...}]`` and
    ``{"UST2Y": {...}}`` for dashboards.  The latter is lossless to adapt in
    memory: the map key becomes the required ``asset`` identity and the value
    remains untouched.  Scalars are retained under ``value`` rather than
    discarded, so this compatibility layer never invents market fields.
    """
    if not isinstance(value, dict):
        return []

    rows: list[dict[str, Any]] = []
    for key, item in value.items():
        if isinstance(item, dict):
            row = dict(item)
        else:
            row = {"value": item}
        row.setdefault("asset", str(key))
        rows.append(row)
    return rows


def _compat_market_dashboard(value: Any, data: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not value:
        value = value if isinstance(value, dict) else data.get("dashboard")
        if not isinstance(value, list):
            value = _compat_mapping_rows(value)

    text = json.dumps(data, ensure_ascii=False, sort_keys=True)
    normalized: list[dict[str, Any]] = []
    for item in value:
        if not isinstance(item, dict):
            continue
        row = dict(item)
        product = row.get("product") or row.get("asset") or row.get("symbol") or "UNKNOWN"
        contract = row.get("main_contract") or row.get("contract") or row.get("main") or row.get("symbol")
        if not contract and isinstance(row.get("asset"), str):
            contract = row["asset"]
        if not isinstance(contract, str) or not contract.strip():
            contract = _compat_contract_from_text(str(product), json.dumps(row, ensure_ascii=False))
        if not contract:
            contract = _compat_contract_from_text(str(product), text) or "N/A"
        row["main_contract"] = str(contract)
        row["product"] = _compat_contract_root(contract) or str(product)
        normalized.append(row)
    return normalized


def _compat_dashboard(value: Any, market_dashboard: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Build the generic dashboard required by the shared report schema."""
    if isinstance(value, list) and value:
        source = value
    elif isinstance(value, dict):
        source = _compat_mapping_rows(value)
    else:
        source = market_dashboard
    normalized: list[dict[str, Any]] = []
    for item in source:
        if not isinstance(item, dict):
            continue
        row = dict(item)
        row.setdefault("asset", row.get("product") or row.get("symbol") or "UNKNOWN")
        normalized.append(row)
    return normalized


def _compat_meaningful_changes(value: Any) -> list[dict[str, Any]]:
    """Normalize prose change summaries to the schema's object-array form."""
    if not isinstance(value, list):
        return []

    normalized: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            normalized.append(dict(item))
        elif isinstance(item, str) and item.strip():
            normalized.append({"summary": item.strip()})
        elif item is not None:
            normalized.append({"summary": str(item)})
    return normalized


def _compat_event_calendar(value: Any) -> list[dict[str, Any]]:
    """Preserve compact prose events as object rows required by the schema."""
    if not isinstance(value, list):
        return []

    normalized: list[dict[str, Any]] = []
    for item in value:
        if isinstance(item, dict):
            normalized.append(dict(item))
        elif isinstance(item, str) and item.strip():
            normalized.append({"event": item.strip()})
        elif item is not None:
            normalized.append({"event": str(item)})
    return normalized


def _compat_top_opportunities(value: Any) -> Any:
    """Keep ambiguous risk labels from violating the boolean contract.

    Scheduled reports sometimes use prose such as ``designable`` or
    ``with options`` instead of answering whether the opportunity itself has
    a defined maximum loss.  Preserve that wording for auditability, but use
    ``null`` for the canonical field rather than inventing a boolean.
    """
    if not isinstance(value, list):
        return value

    normalized: list[Any] = []
    for item in value:
        if not isinstance(item, dict):
            normalized.append(item)
            continue
        row = dict(item)
        if "max_loss_limited" not in row and isinstance(row.get("max_loss_finite"), bool):
            row["max_loss_limited"] = row["max_loss_finite"]
        if "holding_period" not in row and row.get("horizon") is not None:
            row["holding_period"] = str(row["horizon"])
        if "instruments" not in row and row.get("tool") is not None:
            tool = row["tool"]
            if isinstance(tool, list):
                row["instruments"] = [str(part) for part in tool]
            else:
                row["instruments"] = [str(tool)]
        risk_limit = row.get("max_loss_limited")
        if risk_limit is not None and not isinstance(risk_limit, bool):
            row.setdefault("max_loss_limited_note", str(risk_limit))
            row["max_loss_limited"] = None
        normalized.append(row)
    return normalized


def _compat_coverage_count(value: Any, *keys: str) -> int | float | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value
    if isinstance(value, dict):
        for key in keys:
            candidate = value.get(key)
            if isinstance(candidate, (int, float)) and not isinstance(candidate, bool):
                return candidate
    return None


def _compat_research_surface_declared(data: dict[str, Any]) -> bool:
    assessment = data.get("options_assessment")
    if isinstance(assessment, dict) and assessment.get("surface_ready") is True:
        return True

    values: list[str] = []
    for container_name in ("module_freshness", "module_quality"):
        container = data.get(container_name)
        if not isinstance(container, dict):
            continue
        for key in ("options", "options_surface"):
            value = container.get(key)
            if value is not None:
                values.append(str(value).lower())

    text = " ".join(values)
    return any(
        token in text
        for token in (
            "research-ready",
            "research ready",
            "research_ready",
            "surface-ready",
            "surface ready",
            "surface_ready",
        )
    )


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


def _compat_module_quality(data: dict[str, Any]) -> dict[str, Any]:
    value = data.get("module_quality")
    return dict(value) if isinstance(value, dict) else {}


def _compat_china_commodities_snapshot(data: dict[str, Any]) -> dict[str, Any]:
    """Complete the required input snapshot without fabricating unavailable data."""
    input_snapshots = data.get("input_snapshots")
    input_snapshots = dict(input_snapshots) if isinstance(input_snapshots, dict) else {}
    snapshot = input_snapshots.get("china_commodities")
    snapshot = dict(snapshot) if isinstance(snapshot, dict) else {}
    quality_metrics = data.get("quality_metrics")
    quality_metrics = quality_metrics if isinstance(quality_metrics, dict) else {}
    module_quality = _compat_module_quality(data)
    source_status = data.get("source_status")
    source_status = source_status if isinstance(source_status, dict) else {}
    last_good_eod = source_status.get("last_good_eod")
    last_good_eod = last_good_eod if isinstance(last_good_eod, dict) else {}
    options_status = source_status.get("options")
    options_status = options_status if isinstance(options_status, dict) else {}

    snapshot.setdefault("repository", "farfromexact/China-Commodities-Engine")
    snapshot.setdefault("branch", "main")
    snapshot.setdefault("last_run_status_path", "data/last_run_status.json")
    snapshot.setdefault("radar_latest_path", "data/radar_latest.json")
    snapshot.setdefault("radar_history_path", "data/radar_history.json")
    trade_date = (
        snapshot.get("trade_date")
        or data.get("china_commodities_date")
        or last_good_eod.get("date")
        or options_status.get("trade_date")
    )
    snapshot["trade_date"] = trade_date
    snapshot.setdefault(
        "generated_at",
        data.get("report_input_generated_at") or data.get("generated_at_bjt"),
    )
    snapshot.setdefault("data_fresh", data.get("data_fresh"))
    snapshot.setdefault("official_complete", data.get("official_complete"))
    snapshot.setdefault(
        "source_date_match_pct",
        quality_metrics.get("source_date_match_pct"),
    )
    snapshot.setdefault("full_market_ready", data.get("full_market_ready"))
    snapshot.setdefault(
        "critical_module_errors",
        quality_metrics.get("critical_module_errors"),
    )
    snapshot.setdefault("history_record_count", data.get("history_record_count"))
    snapshot.setdefault("module_quality", module_quality)
    snapshot.setdefault(
        "actual_read_paths",
        data.get("report_input_source_paths") or [],
    )
    input_snapshots["china_commodities"] = snapshot
    return input_snapshots


def _compat_quality_status(data: dict[str, Any], module_quality: dict[str, Any]) -> str:
    quality_metrics = data.get("quality_metrics") if isinstance(data.get("quality_metrics"), dict) else {}
    critical_errors = quality_metrics.get("critical_module_errors", 0)
    source_match = quality_metrics.get("source_date_match_pct")
    if data.get("data_fresh") is False or (isinstance(critical_errors, int) and critical_errors > 0):
        return "stale_or_partial"
    if isinstance(source_match, (int, float)) and source_match < 100:
        return "stale_or_partial"
    quality_text = " ".join(str(item).lower() for item in module_quality.values())
    if any(token in quality_text for token in ("partial", "unavailable", "not_ready", "stale", "error", "missing")):
        return "degraded"
    return "ready"


def _compat_required_string(value: Any, fallback: Any = "unknown") -> str:
    if isinstance(value, str) and value.strip():
        return value
    if isinstance(fallback, str) and fallback.strip():
        return fallback
    return "unknown"


def _compat_available_horizons(data: dict[str, Any]) -> list[str]:
    explicit = data.get("available_horizons")
    if isinstance(explicit, list):
        return [item for item in explicit if item in {"1D", "3D", "5D", "20D"}]

    horizons: set[str] = set()
    dashboard = data.get("dashboard")
    if isinstance(dashboard, list):
        for item in dashboard:
            if not isinstance(item, dict):
                continue
            for key, horizon in (("change_1d", "1D"), ("change_3d", "3D"), ("change_5d", "5D"), ("change_20d", "20D")):
                if isinstance(item.get(key), dict):
                    horizons.add(horizon)
    return [horizon for horizon in ("1D", "3D", "5D", "20D") if horizon in horizons]


def _compat_data_quality(
    value: Any,
    data: dict[str, Any],
    tracking: dict[str, Any],
) -> dict[str, Any]:
    quality = dict(value) if isinstance(value, dict) else {}
    module_quality = _compat_module_quality(data)
    input_snapshots = data.get("input_snapshots") if isinstance(data.get("input_snapshots"), dict) else {}
    commodity_snapshot = input_snapshots.get("china_commodities")
    commodity_snapshot = commodity_snapshot if isinstance(commodity_snapshot, dict) else {}
    options_assessment = data.get("options_assessment")
    options_assessment = options_assessment if isinstance(options_assessment, dict) else {}

    derived_status = _compat_quality_status(data, module_quality)
    quality["status"] = quality.get("status") if quality.get("status") in {"ready", "degraded", "stale_or_partial"} else derived_status
    quality["price_source"] = _compat_required_string(
        quality.get("price_source"),
        f"{commodity_snapshot.get('repository', 'China-Commodities-Engine')} / data/radar_latest.json",
    )
    quality["curve_definition"] = _compat_curve_definition(
        quality.get("curve_definition")
        or data.get("curve_definition")
        or module_quality.get("curve_definition"),
        data,
    )
    quality["basis_status"] = _compat_required_string(quality.get("basis_status"), module_quality.get("basis", "unavailable"))
    quality["warehouse_status"] = _compat_required_string(
        quality.get("warehouse_status"), module_quality.get("warehouse", "unavailable")
    )
    quality["member_rankings_status"] = _compat_required_string(
        quality.get("member_rankings_status"), module_quality.get("member_rankings", "unavailable")
    )
    quality["options_chain_status"] = _compat_required_string(
        quality.get("options_chain_status"),
        module_quality.get("options_chain")
        or module_quality.get("options")
        or ("ready" if options_assessment.get("record_count") and options_assessment.get("product_coverage") == 1 else "partial"),
    )
    surface_count = _compat_coverage_count(
        data.get("options_surface_ready"),
        "series_ready",
        "ready_count",
        "surface_ready_count",
    )
    surface_status = module_quality.get("options_surface")
    if (
        surface_status is None
        and surface_count is not None
        and _compat_research_surface_declared(data)
    ):
        surface_status = "research_ready" if surface_count > 0 else "not_ready"
    quality["options_surface_status"] = _compat_required_string(
        quality.get("options_surface_status"),
        surface_status
        or ("ready" if options_assessment.get("surface_ready") is True else "not_ready"),
    )

    if "history_comparison_status" not in quality:
        horizons = _compat_available_horizons(data)
        quality["history_comparison_status"] = "available" if horizons else "insufficient_history"
    else:
        horizons = _compat_available_horizons(data)
    quality.setdefault("available_horizons", horizons)
    if not isinstance(quality.get("available_horizons"), list):
        quality["available_horizons"] = []
    explicit_metrics = quality.get("comparative_metrics")
    if not isinstance(explicit_metrics, list):
        explicit_metrics = data.get("comparative_metrics")
    if isinstance(explicit_metrics, list):
        # Preserve explicitly supplied metrics so the contract validator can
        # reject them when history is insufficient.  Only compact schedule
        # reports without an explicit metrics field may derive metrics from
        # their meaningful-change narrative.
        quality["comparative_metrics"] = _compat_meaningful_changes(explicit_metrics)
    elif quality.get("history_comparison_status") == "insufficient_history":
        # Weekend/event narratives remain in meaningful_changes, but they are
        # not quantitative comparative metrics without a comparable candle.
        quality["comparative_metrics"] = []
    else:
        quality["comparative_metrics"] = _compat_meaningful_changes(
            data.get("meaningful_changes") if isinstance(data.get("meaningful_changes"), list) else []
        )
    return quality


def _compat_options_surface(value: Any, data: dict[str, Any]) -> dict[str, Any]:
    source = dict(value) if isinstance(value, dict) else {}
    if not source:
        assessment = data.get("options_assessment")
        source = dict(assessment) if isinstance(assessment, dict) else {}

    status = source.get("status")
    surface_count = _compat_coverage_count(
        data.get("options_surface_ready"),
        "series_ready",
        "ready_count",
        "surface_ready_count",
    )
    if isinstance(status, str) and status.strip().lower() in {"research_ready", "surface_ready"}:
        # These labels mean the research surface is usable; execution readiness
        # remains separately represented by the coverage counters.
        status = "ready"
    if status not in {"ready", "not_ready", "not_collected", "unavailable"}:
        status = "ready" if (
            source.get("surface_ready") is True
            or (
                surface_count is not None
                and surface_count > 0
                and _compat_research_surface_declared(data)
            )
        ) else "not_ready"

    # Keep only fields that are safe in the canonical surface contract.  The
    # raw assessment may contain labels such as ``skew`` and ``iv_high_low``;
    # copying those into a closed surface would look like collected metrics.
    normalized: dict[str, Any] = {
        "status": status,
        "available_metrics": list(source.get("available_metrics") or []) if status == "ready" else [],
        "tradeable_structures": list(source.get("tradeable_structures") or []) if status == "ready" else [],
        "research_priority_when_ready": list(
            source.get("research_priority_when_ready")
            or source.get("preferred_structure_directions")
            or source.get("research_priority")
            or []
        ),
    }
    # Coverage counts describe the research/execution split; they are not
    # executable prices or Greeks and are useful when a report has a partial
    # chain but a usable research surface.  Some reports keep the counts in
    # top-level ``options_*_ready`` objects instead of this nested object.
    top_level_coverage = {
        "surface_ready_count": "options_surface_ready",
        "positioning_ready_count": "options_positioning_ready",
        "execution_ready_count": "options_execution_ready",
    }
    for key, top_level_key in top_level_coverage.items():
        coverage = source.get(key)
        if coverage is None:
            coverage = data.get(top_level_key)
            if isinstance(coverage, dict):
                coverage = next(
                    (
                        coverage.get(candidate)
                        for candidate in ("series_ready", "ready_count", key)
                        if coverage.get(candidate) is not None
                    ),
                    None,
                )
        if coverage is not None:
            normalized[key] = coverage
    for key in ("limitations", "mandatory_statement", "must_avoid"):
        if key in source:
            normalized[key] = source[key]
    return normalized


def _compat_gate_ready(value: Any, *, gate: str) -> bool:
    """Accept descriptive split-module states without weakening safety gates."""

    text = str(value or "").strip().lower()
    normalized = text.replace(" ", "_")
    if text == "ready":
        return True
    if gate == "chain":
        return "full_chain" in normalized or "chain_verified" in normalized
    if gate == "surface":
        return "research_ready" in normalized or "surface_ready" in normalized
    return False


def _compat_night_action(item: dict[str, Any]) -> str:
    for key in ("action", "recommended_action", "next_action", "risk_action", "操作", "建议", "执行"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()

    fragments: list[str] = []
    aliases = (
        (("expected_open", "expected", "预期"), "expected"),
        (("chase", "追价", "追价?"), "chase"),
        (("wait_minutes", "wait", "等待"), "wait"),
        (("confirmation", "关键确认", "确认"), "confirm"),
        (("night_session", "夜盘"), "session"),
    )
    for keys, label in aliases:
        for key in keys:
            value = item.get(key)
            if value is not None and str(value).strip():
                fragments.append(f"{label}: {value}")
                break
    return "; ".join(fragments) if fragments else "unknown"


def _compat_night_session_risk_map(value: Any, data: dict[str, Any]) -> list[dict[str, Any]]:
    source = value if isinstance(value, list) and value else data.get("opening_gap_map")
    if not isinstance(source, list):
        return []

    normalized: list[dict[str, Any]] = []
    for item in source:
        if not isinstance(item, dict):
            continue
        row = dict(item)
        product = row.get("product") or row.get("asset") or row.get("symbol") or "UNKNOWN"
        confidence = row.get("confidence") or row.get("confidence_level") or row.get("certainty") or row.get("置信度")
        normalized.append(
            {
                **row,
                "product": str(product),
                "confidence": str(confidence).strip() if confidence is not None and str(confidence).strip() else "unknown",
                "action": _compat_night_action(row),
            }
        )
    return normalized


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
    if data.get("schema_version") == "1.1":
        normalized["schema_version"] = "1.0"
    normalized.setdefault("status", _compat_status(data, path))
    normalized["input_snapshots"] = _compat_china_commodities_snapshot(data)
    normalized.setdefault("generated_at_bjt", data.get("generated_at"))
    normalized.setdefault("title", _compat_title(data))
    normalized.setdefault(
        "one_sentence_conclusion",
        data.get("one_sentence") or data.get("commodity_regime") or data.get("regime"),
    )
    normalized.setdefault(
        "regime",
        data.get("commodity_regime") or data.get("market_regime") or data.get("regime"),
    )
    normalized.setdefault("worth_taking_risk", data.get("worth_taking_risk"))
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
    normalized["event_calendar"] = _compat_event_calendar(data.get("event_calendar"))
    normalized.setdefault("action_list", {"A": "", "B": "", "C": "", "D": ""})
    normalized.setdefault("risk_budget", {})

    tracking = dict(data.get("commodities_tracking")) if isinstance(data.get("commodities_tracking"), dict) else {}
    quality = _compat_data_quality(tracking.get("data_quality"), data, tracking)
    tracking["data_quality"] = quality
    market_dashboard = _compat_market_dashboard(tracking.get("market_dashboard"), data)
    tracking["market_dashboard"] = market_dashboard
    if not isinstance(tracking.get("supply_chain_map"), list):
        tracking["supply_chain_map"] = data.get("sector_map") if isinstance(data.get("sector_map"), list) else []
    tracking["options_surface"] = _compat_options_surface(tracking.get("options_surface"), data)
    tracking["night_session_risk_map"] = _compat_night_session_risk_map(
        tracking.get("night_session_risk_map"), data
    )
    normalized["commodities_tracking"] = tracking
    normalized["dashboard"] = _compat_dashboard(data.get("dashboard"), market_dashboard)
    normalized["meaningful_changes"] = _compat_meaningful_changes(
        data.get("meaningful_changes") or quality.get("comparative_metrics", [])
    )
    normalized["sources"] = _compat_sources(data.get("sources"))
    normalized["archive"] = _compat_archive(data, path)
    return normalized


def _normalize_global_schedule_report(data: dict[str, Any], path: Path) -> dict[str, Any]:
    """Adapt compact global morning/evening task output for validation.

    Scheduled reports have appeared both with schema version 1.1 and without a
    schema marker.  Detect the dialect from the edition and its compact field
    names, then add a canonical in-memory view while preserving every raw key.
    """
    if data.get("edition") not in {"morning", "evening"}:
        return data

    compact_markers = {
        "generated_at",
        "market_regime",
        "one_line_conclusion",
        "trade_cards",
        "global_snapshot",
        "events",
    }
    if not compact_markers.intersection(data):
        return data

    normalized = dict(data)
    if data.get("schema_version") in {None, "1.1"}:
        normalized["schema_version"] = "1.0"
    normalized.setdefault("status", _compat_status(data, path))
    normalized.setdefault("generated_at_bjt", data.get("generated_at"))
    normalized.setdefault("title", _compat_title(data))
    normalized.setdefault(
        "one_sentence_conclusion",
        data.get("one_line_conclusion") or data.get("one_line") or data.get("one_sentence"),
    )
    normalized.setdefault("regime", data.get("market_regime"))
    normalized.setdefault("worth_taking_risk", data.get("worth_taking_risk"))

    if not isinstance(normalized.get("input_snapshots"), dict):
        normalized["input_snapshots"] = {
            "china_options_repository": "farfromexact/China-Options-Engine",
            "china_options_path": "data/radar_latest.json",
            "china_options_history_path": "data/radar_history.json",
            "china_options_date": data.get("china_options_date"),
            "china_options_fresh": data.get("data_fresh"),
            "actual_read_paths": data.get("china_options_engine_actual_read_paths")
            or data.get("china_options_engine_paths")
            or data.get("China-Options-Engine实际读取路径")
            or [],
        }
    if not isinstance(normalized.get("source_status"), dict):
        normalized["source_status"] = {
            "compatibility_adapter": "global_schedule_dialect",
            "data_fresh": data.get("data_fresh"),
            "errors": data.get("errors", []),
        }

    normalized["dashboard"] = _compat_dashboard(
        data.get("dashboard") or data.get("global_snapshot"),
        [],
    )
    normalized["meaningful_changes"] = _compat_meaningful_changes(
        data.get("meaningful_changes")
    )
    normalized["top_opportunities"] = _compat_top_opportunities(
        data.get("top_opportunities", [])
    )
    normalized.setdefault("top_trade_cards", data.get("trade_cards", []))
    normalized.setdefault(
        "gold_tracking",
        data.get("gold") if isinstance(data.get("gold"), dict) else {},
    )
    normalized.setdefault(
        "ai_tracking",
        data.get("ai") if isinstance(data.get("ai"), dict) else {},
    )

    china = dict(data.get("china")) if isinstance(data.get("china"), dict) else {}
    china.setdefault("score", china.get("china_opportunity_score"))
    china.setdefault("preferred_future", china.get("preference"))
    normalized["china_tracking"] = _compat_china_tracking(china)
    normalized["event_calendar"] = _compat_event_calendar(
        data.get("event_calendar") or data.get("events")
    )
    normalized.setdefault("action_list", {"A": "", "B": "", "C": "", "D": ""})
    normalized.setdefault("risk_budget", {})
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
    normalized = _normalize_global_schedule_report(normalized, path)
    if data.get("schema_version") == "1.1":
        normalized["schema_version"] = "1.0"

    # Apply harmless dialect normalization to every schema version.  These are
    # in-memory adapters only; the archived source JSON remains unchanged.
    if "dashboard" in data:
        normalized["dashboard"] = _compat_dashboard(normalized.get("dashboard"), [])
    if "top_opportunities" in data:
        normalized["top_opportunities"] = _compat_top_opportunities(
            normalized.get("top_opportunities")
        )
    if "meaningful_changes" in data:
        normalized["meaningful_changes"] = _compat_meaningful_changes(
            normalized.get("meaningful_changes")
        )
    if isinstance(normalized.get("archive"), dict) or "archive_status" in data:
        normalized["archive"] = _compat_archive(normalized, path)

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


def _compat_research_only_structure(value: Any) -> bool:
    """Return whether a structure is explicitly non-executable research text."""
    text = json.dumps(value, ensure_ascii=False, sort_keys=True).lower()
    return any(
        token in text
        for token in (
            "manual quote",
            "manual confirmation",
            "execution false",
            "execution_ready=false",
            "not executable",
            "research only",
            "仅研究",
            "人工确认",
            "执行前确认",
            "不报权利金",
        )
    )


def _compat_partial_surface_evidence(quality: Any, options_surface: Any) -> bool:
    """Recognize a reported research surface when the full chain is partial."""
    if not isinstance(options_surface, dict):
        return False
    count = options_surface.get("surface_ready_count")
    if isinstance(count, (int, float)) and count > 0:
        return True
    text = " ".join(
        str(value)
        for value in (
            quality.get("options_surface_status") if isinstance(quality, dict) else None,
            quality.get("options_chain_status") if isinstance(quality, dict) else None,
        )
    ).lower()
    return any(
        token in text
        for token in (
            "surface-ready",
            "surface ready",
            "surface_ready",
            "research-ready",
            "research ready",
            "research_ready",
        )
    )


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
    chain_ready = isinstance(quality, dict) and _compat_gate_ready(
        quality.get("options_chain_status"), gate="chain"
    )
    surface_ready = isinstance(options_surface, dict) and (
        options_surface.get("status") == "ready"
        or _compat_gate_ready(options_surface.get("status"), gate="surface")
    )
    # A commodity task can have a useful research surface for most products
    # while the complete chain or execution quote layer is still partial (for
    # example, 360/368 surface-ready and 0/368 execution-ready).  Trust that
    # explicit coverage evidence for research summaries, but keep the strict
    # gate for reports that have neither a ready surface nor coverage evidence.
    research_surface_ready = surface_ready and (
        chain_ready or _compat_partial_surface_evidence(quality, options_fields)
    )
    if not research_surface_ready:
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
    elif not chain_ready and options_fields.get("tradeable_structures"):
        # A partial chain may still describe a conditional structure, but only
        # when it explicitly requires a manual quote/confirmation.  This keeps
        # exact executable structures behind the complete-chain gate.
        structures = options_fields.get("tradeable_structures")
        if isinstance(structures, list) and not all(
            _compat_research_only_structure(item) for item in structures
        ):
            messages.append(
                f"{path.relative_to(ROOT)} exposes commodity option trade structures without an explicit manual-quote/confirmation disclaimer"
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


def collect_full_validation_errors(
    report_schema: dict[str, Any],
    manifest_schema: dict[str, Any],
    archive_policy: dict[str, Any],
    allowed_editions: tuple[str, ...],
) -> list[str]:
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
    return errors


def load_manifest_at_ref(base_ref: str | None) -> dict[str, Any] | None:
    """Read the manifest from a Git ref, returning None for unavailable bases."""
    if not base_ref or re.fullmatch(r"0+", base_ref):
        return None

    try:
        result = subprocess.run(
            ["git", "show", f"{base_ref}:manifests/reports.json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def manifest_entries_by_key(data: Any) -> dict[tuple[str, str], dict[str, Any]]:
    if not isinstance(data, dict) or not isinstance(data.get("reports"), list):
        return {}

    entries: dict[tuple[str, str], dict[str, Any]] = {}
    for item in data["reports"]:
        if not isinstance(item, dict):
            continue
        report_date = item.get("report_date")
        edition = item.get("edition")
        if isinstance(report_date, str) and isinstance(edition, str):
            entries[(report_date, edition)] = item
    return entries


def changed_manifest_entries(base_manifest: Any, current_manifest: Any) -> list[dict[str, Any]]:
    base_entries = manifest_entries_by_key(base_manifest)
    current_entries = manifest_entries_by_key(current_manifest)
    return [
        entry
        for key, entry in current_entries.items()
        if base_entries.get(key) != entry
    ]


def _load_markdown_validator() -> Any:
    path = ROOT / "scripts" / "validate_markdown_reports.py"
    spec = importlib.util.spec_from_file_location("publication_markdown_validator", path)
    if spec is None or spec.loader is None:
        raise ValidationFailure(f"Unable to load Markdown validator: {path.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _publication_identity_errors(
    data: dict[str, Any],
    path: Path,
    *,
    report_date: str,
    edition: str,
    revision: int,
) -> list[str]:
    normalized = normalize_report_for_schema(data, path)
    errors: list[str] = []
    rel = path.relative_to(ROOT)
    expected = {
        "report_date": report_date,
        "edition": edition,
        "revision": revision,
    }
    for field, value in expected.items():
        if normalized.get(field) != value:
            errors.append(
                f"{rel} {field}={normalized.get(field)!r}; expected {value!r} from manifest"
            )
    if normalized.get("status") != "published":
        errors.append(f"{rel} status must be 'published' for a final publication")
    archive = normalized.get("archive")
    archive_status = archive.get("archive_status") if isinstance(archive, dict) else None
    if archive_status != "success":
        errors.append(f"{rel} archive.archive_status={archive_status!r}; expected 'success'")
    return errors


def publication_manifest_state_errors(entry: dict[str, Any]) -> list[str]:
    key = (entry.get("report_date"), entry.get("edition"))
    errors: list[str] = []
    if entry.get("status") != "published":
        errors.append(f"Manifest entry {key} status must be 'published' before CI runs")
    if entry.get("archive_status") != "success":
        errors.append(
            f"Manifest entry {key} archive_status must be 'success'; pending entries must not be committed"
        )
    revision = entry.get("revision")
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        errors.append(f"Manifest entry {key} revision must be an integer >= 1")
    return errors


def publication_status_identity_errors(
    status_data: Any,
    path: Path,
    *,
    report_date: str,
    edition: str,
    revision: int,
) -> list[str]:
    errors: list[str] = []
    for field, value in {
        "report_date": report_date,
        "edition": edition,
        "revision": revision,
        "archive_status": "success",
    }.items():
        if not isinstance(status_data, dict) or status_data.get(field) != value:
            actual = status_data.get(field) if isinstance(status_data, dict) else None
            errors.append(f"{path.relative_to(ROOT)} {field}={actual!r}; expected {value!r}")
    return errors


def publication_json_identity_errors(
    historical_data: Any,
    latest_data: Any,
    historical_path: Path,
    latest_path: Path,
) -> list[str]:
    if historical_data == latest_data:
        return []
    return [
        f"{latest_path.relative_to(ROOT)} is not identical to "
        f"{historical_path.relative_to(ROOT)}"
    ]


def validate_publication_bundle(
    entry: dict[str, Any],
    report_schema: dict[str, Any],
    archive_policy: dict[str, Any],
    allowed_editions: tuple[str, ...],
    markdown_validator: Any,
) -> list[str]:
    errors: list[str] = []
    report_date = entry.get("report_date")
    edition = entry.get("edition")
    revision = entry.get("revision")
    key = (report_date, edition)

    errors.extend(publication_manifest_state_errors(entry))
    if not isinstance(report_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", report_date):
        errors.append(f"Manifest entry {key} has invalid report_date")
        return errors
    if edition not in allowed_editions:
        errors.append(f"Manifest entry {key} has an unconfigured edition")
        return errors
    if not isinstance(revision, int) or isinstance(revision, bool) or revision < 1:
        return errors

    expected_json_rel = f"reports/{report_date[:4]}/{report_date[5:7]}/{report_date}_{edition}.json"
    expected_markdown_rel = f"reports/{report_date[:4]}/{report_date[5:7]}/{report_date}_{edition}.md"
    if entry.get("json_path") != expected_json_rel:
        errors.append(
            f"Manifest entry {key} json_path={entry.get('json_path')!r}; expected {expected_json_rel!r}"
        )
    if entry.get("markdown_path") != expected_markdown_rel:
        errors.append(
            f"Manifest entry {key} markdown_path={entry.get('markdown_path')!r}; expected {expected_markdown_rel!r}"
        )

    config = archive_policy.get("editions", {}).get(edition, {})
    latest_json_rel = config.get("latest_json") if isinstance(config, dict) else None
    latest_markdown_rel = config.get("latest_markdown") if isinstance(config, dict) else None
    status_rel = config.get("status_path") if isinstance(config, dict) else None
    configured_paths = {
        "latest_json": latest_json_rel,
        "latest_markdown": latest_markdown_rel,
        "status": status_rel,
    }
    for label, value in configured_paths.items():
        if not isinstance(value, str):
            errors.append(f"Archive policy is missing {label} for edition {edition}")
    if errors and any(not isinstance(value, str) for value in configured_paths.values()):
        return errors

    historical_json = ROOT / expected_json_rel
    historical_markdown = ROOT / expected_markdown_rel
    latest_json = ROOT / str(latest_json_rel)
    latest_markdown = ROOT / str(latest_markdown_rel)
    status_path = ROOT / str(status_rel)
    for path in (
        historical_json,
        historical_markdown,
        latest_json,
        latest_markdown,
        status_path,
        MANIFEST_PATH,
    ):
        if not path.exists():
            errors.append(f"Publication bundle is missing {path.relative_to(ROOT)}")
    if errors and any(
        not path.exists()
        for path in (historical_json, historical_markdown, latest_json, latest_markdown, status_path)
    ):
        return errors

    errors.extend(validate_report_file(historical_json, report_schema, allowed_editions))
    errors.extend(validate_report_file(latest_json, report_schema, allowed_editions))

    historical_data = load_json(historical_json)
    latest_data = load_json(latest_json)
    errors.extend(
        publication_json_identity_errors(
            historical_data,
            latest_data,
            historical_json,
            latest_json,
        )
    )
    errors.extend(
        _publication_identity_errors(
            historical_data,
            historical_json,
            report_date=report_date,
            edition=edition,
            revision=revision,
        )
    )
    errors.extend(
        _publication_identity_errors(
            latest_data,
            latest_json,
            report_date=report_date,
            edition=edition,
            revision=revision,
        )
    )

    status_data = load_json(status_path)
    errors.extend(
        publication_status_identity_errors(
            status_data,
            status_path,
            report_date=report_date,
            edition=edition,
            revision=revision,
        )
    )
    errors.extend(scan_forbidden_tokens(status_path))

    errors.extend(markdown_validator.validate_full_markdown(historical_markdown, report_date, edition))
    errors.extend(markdown_validator.validate_full_markdown(latest_markdown, report_date, edition))
    if (
        historical_markdown.exists()
        and latest_markdown.exists()
        and markdown_validator.normalized_markdown(historical_markdown)
        != markdown_validator.normalized_markdown(latest_markdown)
    ):
        errors.append(
            f"{latest_markdown.relative_to(ROOT)} is not identical to {historical_markdown.relative_to(ROOT)}"
        )
    return errors


def collect_publication_validation_errors(
    base_manifest: dict[str, Any],
    current_manifest: dict[str, Any],
    report_schema: dict[str, Any],
    manifest_schema: dict[str, Any],
    archive_policy: dict[str, Any],
    allowed_editions: tuple[str, ...],
) -> list[str]:
    errors = validate_manifest(manifest_schema, allowed_editions)
    changed_entries = changed_manifest_entries(base_manifest, current_manifest)
    if not changed_entries:
        errors.append("Manifest changed without adding or revising a report entry")
        return errors

    markdown_validator = _load_markdown_validator()
    for entry in changed_entries:
        errors.extend(
            validate_publication_bundle(
                entry,
                report_schema,
                archive_policy,
                allowed_editions,
                markdown_validator,
            )
        )
    return errors


def _print_result(errors: list[str], *, scope: str) -> int:
    label = "Publication validation" if scope == "publication" else "Report archive validation"

    if errors:
        print(f"{label} failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"{label} passed.")
    return 0


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Validate the Radar report archive")
    parser.add_argument("--scope", choices=("full", "publication"), default="full")
    parser.add_argument("--base-ref", help="Git ref containing the manifest before publication")
    args = parser.parse_args(argv)

    report_schema = load_json(REPORT_SCHEMA_PATH)
    manifest_schema = load_json(MANIFEST_SCHEMA_PATH)
    archive_policy = load_json(ARCHIVE_POLICY_PATH)
    allowed_editions = configured_editions(archive_policy)

    if args.scope == "publication":
        base_manifest = load_manifest_at_ref(args.base_ref)
        if base_manifest is None:
            print("Publication base ref is unavailable; falling back to full archive validation.")
            errors = collect_full_validation_errors(
                report_schema,
                manifest_schema,
                archive_policy,
                allowed_editions,
            )
            return _print_result(errors, scope="full")
        current_manifest = load_json(MANIFEST_PATH)
        errors = collect_publication_validation_errors(
            base_manifest,
            current_manifest,
            report_schema,
            manifest_schema,
            archive_policy,
            allowed_editions,
        )
        return _print_result(errors, scope="publication")

    errors = collect_full_validation_errors(
        report_schema,
        manifest_schema,
        archive_policy,
        allowed_editions,
    )
    return _print_result(errors, scope="full")


if __name__ == "__main__":
    sys.exit(main())
