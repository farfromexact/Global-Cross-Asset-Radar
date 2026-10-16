# Global Cross-Asset Radar

全球跨资产高风险机会雷达的可审计报告归档仓库。

本仓库与两个底层数据引擎分工如下：

- **China-Options-Engine**：采集和计算中国股指期货/期权底层数据，包括 IH、IF、IC、IM 与 HO、IO、MO 的价格、成交、持仓、IV、偏度和 Gamma 等指标。
- **Global-Cross-Asset-Radar**：保存全球晨报/晚报以及中国商品晨报/晚报的完整中文研究报告、结构化 JSON、最新版本、状态和历史清单。
- **China-Commodities-Engine**：采集中国五所商品期货 EOD、Physical、海外日频序列和商品期权曲面；晨报优先读取其 `data/report_input_latest.json`，而不是自行拼接模块文件。仓单、基差、会员排名和商品期权曲面是否可用必须以当次状态为准。

## 当前部署状态

- 仓库写权限、目录、schema、模板、latest占位文件、状态文件、Manifest和Markdown/JSON配对测试已经完成。
- GitHub Actions校验工作流已经创建；运行结果以Actions页面为准。
- Prompt 源文件保存在 `prompts/`；实际 ChatGPT Scheduled Task 应读取或追加对应 prompt 和 `docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md`。仓库本身是归档与校验层，不替代任务平台的研究/联网能力。

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
│   ├── commodities_morning.md/json
│   └── commodities_evening.md/json
├── reports/
│   └── YYYY/MM/YYYY-MM-DD_{morning|evening|commodities_morning|commodities_evening}.{md|json}
├── manifests/
│   └── reports.json
├── status/
│   ├── morning_latest.json
│   ├── evening_latest.json
│   ├── commodities_morning_latest.json
│   ├── commodities_evening_latest.json
│   └── setup.json
├── schemas/
│   ├── report.schema.json
│   └── manifest.schema.json
├── templates/
│   ├── report.md
│   └── report.json
│   ├── commodities_report.md
│   └── commodities_report.json
├── prompts/
│   ├── radar_morning.md
│   ├── radar_evening.md
│   ├── commodities_morning.md
│   └── commodities_evening.md
├── scripts/
│   ├── check_report_health.py
│   ├── validate_reports.py
│   └── validate_markdown_reports.py
└── .github/workflows/
    └── validate-reports.yml
```

## 每日归档流程

1. 全球版读取 `China-Options-Engine/data/radar_latest.json`；商品版先读取 `China-Commodities-Engine/data/report_input_latest.json`，需要逐执行价或逐合约细节时再读取对应仓库的原始 `data/latest.json`，历史比较时读取对应的 `radar_history.json` 或 snapshots。
2. 联网完成研究，并在 ChatGPT 对话中发布报告。
3. 将完整报告写入当日历史 Markdown 和 JSON。
4. 覆盖相应 edition 的 `latest/*` 文件。
5. 更新对应状态文件和 `manifests/reports.json`。
6. GitHub 归档失败不得阻止对话中的报告发布；失败原因应写入报告和状态文件。

## 命名和覆盖规则

- 正式历史文件：`reports/YYYY/MM/YYYY-MM-DD_{edition}.*`；`edition` 必须在 `config/archive-policy.json` 中配置。
- 同一日期、同一版本重复运行时更新同一路径，由 Git 历史保留版本差异，不生成无序副本。
- 手工测试使用 `tests/YYYY-MM-DDTHH-MM-SS_{edition}.*`，其中 `edition` 必须在归档 policy 中配置；不得覆盖正式历史文件。
- `latest/` 只保留各版本最近一次成功发布的报告。

## 来源和引用

GitHub Markdown 不保留 ChatGPT 专用的引用标记。归档报告应把关键来源转换为普通 Markdown 链接或脚注；JSON 中应保存结构化 `sources` 数组。任何无法确认的报价、时点或来源必须明确标记，不得补猜。

## 数据边界

- 交易所价格、成交和持仓属于事实数据。
- IV、RR25、BF25、Greeks、Gamma 和 dealer-GEX 类指标属于模型推导或代理指标，必须显式区分。
- IC 当前没有直接对应的 CFFEX 中证500指数期权；使用 MO、IO 或相关 ETF 期权时只能标记为代理，不得写成一一对应套保。
- 商品近月—次近月期货曲线不等于现货基差；仓单、基差、会员排名及商品期权曲面未就绪时必须明确标注，不能推导或补猜。
- 本仓库仅提供研究和交易决策支持，不执行自动下单。

## 校验

正式报告的前五个路径先完成写入，最后一次 Manifest 更新才触发 GitHub Actions；不要为了确认成功再写一次 Manifest。代码和测试变更也会触发检查。

日常 CI 采用实用的可读性门槛，不把报告版式当成发布故障：

- **阻断**：当前报告 JSON 缺失、损坏、为空或不是对象；当前 Markdown 缺失或为空；Manifest 无法读取/没有可用条目；当前历史文件日期、edition 或 Manifest 路径明确指错；校验代码及其回归测试出错。
- **提醒**：缺少 revision/schema 字段、字段别名、标题和字数差异、引用格式、状态元数据、latest 内容同步差异，以及旧归档问题。摘要与 JSON artifact 保留具体问题，不再让同一个历史问题每天阻断新报告。
- 每次检查四个 edition 的最新 Manifest 记录和实际 latest 报告；历史 Manifest 修订不要求 latest 回退。拿不到 base ref 时仍检查全部当前报告。

默认两个 job：`Current report readability` 检查当前可读性；`Archive advice and validator tests` 输出完整历史建议并运行回归测试。绿色只代表归档可读及校验代码通过，**不代表数据新鲜、研究结论正确或交易可执行**。

日常验收：

```sh
python scripts/check_report_health.py --output-json current-health.json
python scripts/check_report_health.py --scope audit --output-json archive-advice.json
python -m unittest discover -s tests -p "test_*.py"
```

原严格规则没有删除。需要专项治理时，在 Actions 手动运行勾选 `strict_audit`，或执行下列命令；历史存量问题可能使其失败，这是严格审计结果，不是默认日常门槛：

```sh
python scripts/validate_reports.py --scope full
python scripts/validate_markdown_reports.py
```
