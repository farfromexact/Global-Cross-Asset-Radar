from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_POLICY_PATH = ROOT / "config" / "archive-policy.json"
MIN_FULL_MARKDOWN_DATE = "2026-08-14"
MIN_MARKDOWN_CHARS = 5_000

GLOBAL_REQUIRED_SECTION_GROUPS = (
    ("今日一句话结论",),
    ("市场仪表盘",),
    (
        "相比昨天真正发生了什么变化",
        "真正发生了什么变化",
    ),
    ("机会排行榜",),
    ("前三名交易卡",),
    ("黄金专项",),
    ("AI股票专项",),
    ("中国50",),
    (
        "事件日历",
        "未来24小时与7日事件",
        "未来24小时与7天事件",
        "未来24小时及7日事件",
        "未来24小时及7天事件",
    ),
    ("行动清单",),
)

COMMODITY_REQUIRED_SECTION_GROUPS = (
    ("今日一句话结论",),
    ("数据质量与覆盖说明", "数据质量与覆盖"),
    ("商品市场仪表盘", "商品仪表盘",),
    # The task prompt uses the canonical wording, while existing reports use
    # edition-specific comparisons such as “相比19:30版本” or “相比上一交易日”.
    (
        "相比市场原有定价真正发生了什么",
        "真正发生了什么",
        "相比上一交易日真正变化",
        "相比上一交易日/今晨真正变化",
        "相比上一交易日/上一revision真正变化",
        "相比上一期真正发生了什么",
        "相比上一期真正变化",
    ),
    ("产业链地图",),
    ("机会排行榜",),
    ("前三名交易卡",),
    ("商品期权专项",),
    (
        "夜盘开盘风险地图",
        "夜盘风险地图",
        "开盘风险地图",
        "21:00夜盘开盘风险地图",
        "9:00开盘跳空风险地图",
        "9:00后风险地图",
        "下一中国交易日09:00开盘风险地图",
    ),
    (
        "未来24小时与7天事件",
        "未来 24 小时与 7 天事件",
        "未来24h / 7d事件日历",
        "未来24h / 7d事件",
        "未来24小时 / 7日事件",
        "事件日历",
        "今日事件日历",
    ),
    ("行动清单", "今日行动清单", "A. "),
)

STUB_PATTERNS = (
    re.compile(r"Markdown\s*配对文件", re.IGNORECASE),
    re.compile(r"完整.{0,80}见同目录.{0,80}\.json", re.IGNORECASE | re.DOTALL),
    re.compile(r"完整结构化研究内容.{0,120}\.json", re.IGNORECASE | re.DOTALL),
)


class ValidationFailure(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationFailure(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc

    if not isinstance(data, dict):
        raise ValidationFailure(f"Expected JSON object: {path.relative_to(ROOT)}")
    return data


def configured_editions() -> dict[str, dict[str, Any]]:
    policy = load_json(ARCHIVE_POLICY_PATH)
    editions = policy.get("editions")
    if not isinstance(editions, dict) or not editions:
        raise ValidationFailure("config/archive-policy.json must define a non-empty editions object")
    if any(not isinstance(edition, str) or not isinstance(value, dict) for edition, value in editions.items()):
        raise ValidationFailure("config/archive-policy.json has an invalid editions object")
    return editions


def normalized_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


def section_groups_for_edition(edition: str) -> tuple[tuple[str, ...], ...]:
    if edition.startswith("commodities_"):
        return COMMODITY_REQUIRED_SECTION_GROUPS
    return GLOBAL_REQUIRED_SECTION_GROUPS


def expected_title_fragment(edition: str) -> str:
    if edition.startswith("commodities_"):
        return "全球商品期货期权高风险机会雷达"
    return "全球跨资产高风险机会雷达"


def edition_label(edition: str) -> str:
    return "晨间版" if edition.endswith("morning") else "晚间版"


def validate_full_markdown(
    markdown_path: Path,
    report_date: str,
    edition: str,
) -> list[str]:
    errors: list[str] = []
    rel = markdown_path.relative_to(ROOT)

    if not markdown_path.exists():
        return [f"Missing full Markdown report: {rel}"]

    text = normalized_markdown(markdown_path)

    if len(text) < MIN_MARKDOWN_CHARS:
        errors.append(
            f"{rel} is too short for a full report: {len(text)} chars; "
            f"minimum is {MIN_MARKDOWN_CHARS}"
        )

    for pattern in STUB_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(
                f"{rel} is an index/pairing stub, not a full report: {match.group(0)!r}"
            )
            break

    missing_groups = [
        " / ".join(group)
        for group in section_groups_for_edition(edition)
        if not any(section in text for section in group)
    ]
    if missing_groups:
        errors.append(
            f"{rel} is missing required report sections: {', '.join(missing_groups)}"
        )

    if expected_title_fragment(edition) not in text:
        errors.append(f"{rel} does not contain title fragment {expected_title_fragment(edition)!r}")
    if report_date not in text:
        errors.append(f"{rel} does not contain report_date {report_date}")
    if edition_label(edition) not in text:
        errors.append(f"{rel} does not contain edition label {edition_label(edition)}")

    return errors


def validate_historical_reports(editions: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []

    for json_path in sorted((ROOT / "reports").glob("**/*_*.json")):
        try:
            data = load_json(json_path)
        except ValidationFailure as exc:
            errors.append(str(exc))
            continue

        if data.get("status") != "published":
            continue

        report_date = data.get("report_date")
        edition = data.get("edition")
        if (
            not isinstance(report_date, str)
            or report_date < MIN_FULL_MARKDOWN_DATE
            or edition not in editions
        ):
            continue

        errors.extend(
            validate_full_markdown(
                json_path.with_suffix(".md"),
                report_date,
                edition,
            )
        )

    return errors


def validate_latest_consistency(editions: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []

    for edition, config in editions.items():
        latest_json_rel = config.get("latest_json")
        latest_md_rel = config.get("latest_markdown")
        if not isinstance(latest_json_rel, str) or not isinstance(latest_md_rel, str):
            errors.append(f"Archive policy is missing latest paths for edition {edition}")
            continue

        latest_json = ROOT / latest_json_rel
        latest_md = ROOT / latest_md_rel
        if not latest_json.exists():
            continue

        try:
            data = load_json(latest_json)
        except ValidationFailure as exc:
            errors.append(str(exc))
            continue

        if data.get("status") != "published":
            continue

        report_date = data.get("report_date")
        if not isinstance(report_date, str) or report_date < MIN_FULL_MARKDOWN_DATE:
            continue

        errors.extend(validate_full_markdown(latest_md, report_date, edition))

        # Formal archive writes are deliberately direct-to-main and happen in
        # the policy-defined order.  During that short transaction, the
        # edition status records ``pending``/``partial`` while the historical
        # Markdown may already contain a newer revision than the latest copy.
        # Validate each present report, but defer the identity comparison until
        # the status says the six-file archive is final.  This prevents a
        # legitimate intermediate write from producing a misleading red run.
        status_rel = config.get("status_path")
        status_path = ROOT / status_rel if isinstance(status_rel, str) else None
        if status_path is not None and status_path.exists():
            try:
                status = load_json(status_path)
            except ValidationFailure as exc:
                errors.append(str(exc))
                status = {}
            if (
                status.get("edition") == edition
                and status.get("report_date") == report_date
                and status.get("archive_status") in {"pending", "partial"}
            ):
                continue

        historical_md = (
            ROOT
            / "reports"
            / report_date[:4]
            / report_date[5:7]
            / f"{report_date}_{edition}.md"
        )

        if not historical_md.exists():
            errors.append(
                f"Latest {edition} report references missing historical Markdown: "
                f"{historical_md.relative_to(ROOT)}"
            )
            continue

        if normalized_markdown(latest_md) != normalized_markdown(historical_md):
            errors.append(
                f"{latest_md.relative_to(ROOT)} is not identical to "
                f"{historical_md.relative_to(ROOT)}"
            )

    return errors


def main() -> int:
    try:
        editions = configured_editions()
    except ValidationFailure as exc:
        print(f"Full Markdown archive validation failed:\n- {exc}")
        return 1

    errors = validate_historical_reports(editions)
    errors.extend(validate_latest_consistency(editions))

    if errors:
        print("Full Markdown archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Full Markdown archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
