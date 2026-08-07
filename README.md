# Global Cross-Asset Radar

全球跨资产高风险机会雷达的可审计报告归档仓库。

本仓库与 [`farfromexact/China-Options-Engine`](https://github.com/farfromexact/China-Options-Engine) 分工如下：

- **China-Options-Engine**：采集和计算中国股指期货/期权底层数据，包括 IH、IF、IC、IM 与 HO、IO、MO 的价格、成交、持仓、IV、偏度和 Gamma 等指标。
- **Global-Cross-Asset-Radar**：保存每天北京时间 08:00 晨间版和 20:00 晚间版的完整中文研究报告、结构化 JSON、最新版本、状态和历史清单。

## 当前部署状态

- 仓库写权限、目录、schema、模板、latest占位文件、状态文件、Manifest和Markdown/JSON配对测试已经完成。
- GitHub Actions校验工作流已经创建；运行结果以Actions页面为准。
- **08:00和20:00两个现有Scheduled Task尚未完成归档prompt注入。** 在将 `docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md` 加入两个任务prompt之前，任务仍会在对话中生成报告，但不会自动把完整报告写入本仓库。

## 目录

```text
.
├── config/
│   └── archive-policy.json
├── latest/
│   ├── morning.md
│   ├── morning.json
│   ├── evening.md
│   └── evening.json
├── reports/
│   └── YYYY/MM/YYYY-MM-DD_{morning|evening}.{md|json}
├── manifests/
│   └── reports.json
├── status/
│   ├── morning_latest.json
│   ├── evening_latest.json
│   └── setup.json
├── schemas/
│   ├── report.schema.json
│   └── manifest.schema.json
├── templates/
│   ├── report.md
│   └── report.json
├── scripts/
│   └── validate_reports.py
└── .github/workflows/
    └── validate-reports.yml
```

## 每日归档流程

1. 雷达读取 `China-Options-Engine/data/radar_latest.json`；需要逐执行价或逐合约细节时再读取 `data/latest.json`，历史比较时读取 `data/snapshots/YYYY-MM-DD.json`。
2. 联网完成全球资产研究，并在 ChatGPT 对话中发布报告。
3. 将完整报告写入当日历史 Markdown 和 JSON。
4. 覆盖相应的 `latest/morning.*` 或 `latest/evening.*`。
5. 更新 `status/*_latest.json` 和 `manifests/reports.json`。
6. GitHub 归档失败不得阻止对话中的报告发布；失败原因应写入报告和状态文件。

## 命名和覆盖规则

- 正式历史文件：`reports/YYYY/MM/YYYY-MM-DD_morning.*` 或 `..._evening.*`。
- 同一日期、同一版本重复运行时更新同一路径，由 Git 历史保留版本差异，不生成无序副本。
- 手工测试使用 `tests/YYYY-MM-DDTHH-MM-SS_{morning|evening}.*`，不得覆盖正式历史文件。
- `latest/` 只保留各版本最近一次成功发布的报告。

## 来源和引用

GitHub Markdown 不保留 ChatGPT 专用的引用标记。归档报告应把关键来源转换为普通 Markdown 链接或脚注；JSON 中应保存结构化 `sources` 数组。任何无法确认的报价、时点或来源必须明确标记，不得补猜。

## 数据边界

- 交易所价格、成交和持仓属于事实数据。
- IV、RR25、BF25、Greeks、Gamma 和 dealer-GEX 类指标属于模型推导或代理指标，必须显式区分。
- IC 当前没有直接对应的 CFFEX 中证500指数期权；使用 MO、IO 或相关 ETF 期权时只能标记为代理，不得写成一一对应套保。
- 本仓库仅提供研究和交易决策支持，不执行自动下单。

## 校验

每次向报告目录、最新文件、清单或 schema 推送变更时，GitHub Actions 会运行 `scripts/validate_reports.py`，检查 JSON schema、Markdown 配对、文件命名和不可渲染的 ChatGPT 引用标记。
