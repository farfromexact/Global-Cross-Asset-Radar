from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MIN_FULL_MARKDOWN_DATE = "2026-08-14"
MIN_MARKDOWN_CHARS = 5_000

REQUIRED_SECTIONS = (
    "今日一句话结论",
    "市场仪表盘",
    "相比昨天真正发生了什么变化",
    "机会排行榜",
    "前三名交易卡",
    "黄金专项",
    "AI股票专项",
    "中国50",
    "事件日历",
    "行动清单",
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


def normalized_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace").strip()


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

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]
    if missing_sections:
        errors.append(
            f"{rel} is missing required report sections: {', '.join(missing_sections)}"
        )

    if report_date not in text:
        errors.append(f"{rel} does not contain report_date {report_date}")

    edition_label = "晨间版" if edition == "morning" else "晚间版"
    if edition_label not in text:
        errors.append(f"{rel} does not contain edition label {edition_label}")

    return errors


def validate_historical_reports() -> list[str]:
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
            or edition not in {"morning", "evening"}
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


def validate_latest_consistency() -> list[str]:
    errors: list[str] = []

    for edition in ("morning", "evening"):
        latest_json = ROOT / "latest" / f"{edition}.json"
        latest_md = ROOT / "latest" / f"{edition}.md"

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
                f"latest/{edition}.md is not identical to "
                f"{historical_md.relative_to(ROOT)}"
            )

    return errors


def main() -> int:
    errors = validate_historical_reports()
    errors.extend(validate_latest_consistency())

    if errors:
        print("Full Markdown archive validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Full Markdown archive validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
