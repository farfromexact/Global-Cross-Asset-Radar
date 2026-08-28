# Scheduled Task GitHub Archive Instructions

把本文件中的通用规则和对应版本规则加入已配置的 Scheduled Task prompt。当前版本包括 08:00 全球晨间版、20:00 全球晚间版，以及以 07:00 / 19:30 为**最佳努力开始窗口**的商品晨间/晚间版。商品版的实际完成时间由输入数据就绪情况决定，不是硬性 SLA。

## 通用归档规则

报告在对话中生成完成后，使用已连接的 GitHub connector 直接写入：

```text
farfromexact/Global-Cross-Asset-Radar
```

先读取：

1. `config/archive-policy.json`
2. `schemas/report.schema.json`
3. `templates/report.json`
4. `manifests/reports.json`
5. 对应版本的 `status/*_latest.json`
6. 对应版本的 `latest/*.json` 和 `latest/*.md`

正式归档固定更新6个路径：

1. `reports/YYYY/MM/YYYY-MM-DD_{edition}.md`
2. `reports/YYYY/MM/YYYY-MM-DD_{edition}.json`
3. `latest/{edition}.md`
4. `latest/{edition}.json`
5. `status/{edition}_latest.json`
6. `manifests/reports.json`

其中 `{edition}` 必须是 `config/archive-policy.json` 中已配置的版本之一：`morning`、`evening`、`commodities_morning` 或 `commodities_evening`。

### Manifest 只能作为最终一次提交

同一个 `report_date + edition` 的正式归档中，`manifests/reports.json` **只能在其余五个目标文件已经完整写入并复核后更新一次**。不得用 manifest 记录“开始归档”“pending”“revision N”或“成功确认”等中间状态；这会让 GitHub Actions 对同一份尚未完成的报告重复运行全库校验。

若需要修订报告，先完成历史 Markdown/JSON、`latest` Markdown/JSON 与状态文件的替换和复核，再以一次最终 manifest 更新收尾。这样每份正式归档只会触发一次 `Validate Radar Reports` 工作流。

## 正式归档模式：Direct-to-Main

正式晨间版和晚间版归档必须**直接写入 `main` 分支**。

禁止把下列流程作为正式归档的一部分：

- 创建 staging branch
- `Compare & pull request`
- 创建 Pull Request
- 等待或执行 merge
- 等待 branch cleanup

即使仓库中存在旧 branch、旧 PR、历史 staging 说明，也不得因此创建新的 staging branch。

### 写入步骤

1. 在任何GitHub写入发生前，先在本次任务上下文中生成并检查6个目标文件的最终完整内容。
2. 对不存在的历史路径，直接在 `main` 创建。
3. 对已存在路径，直接在 `main` 更新。
4. `latest/{edition}.*` 只能在完整报告生成成功后覆盖。
5. `manifests/reports.json` 以 `report_date + edition` 为唯一键；重复运行更新现有记录，不追加重复项。
6. `status/{edition}_latest.json` 必须记录本次归档状态、报告日期、生成时间、CI状态和错误。
7. 六个路径全部写入后，必须重新通过 GitHub connector 从 `main` 读取并验证：
   - 历史Markdown存在；
   - 历史JSON存在；
   - latest Markdown/JSON对应本次报告；
   - status对应本次运行；
   - manifest中本次 `report_date + edition` 仅有一个记录。
8. 只有第7步全部成功后，才能设置或声称 `archive_status=success`。
9. main验证完成后立即结束本次 Scheduled Task；不要继续轮询、不要等待CI、不要创建或清理branch。

如果 GitHub Git-data 原子操作可以安全直接更新 `main`，可以使用；如果不能，允许通过 contents API 顺序创建/更新6个路径。**不得因为原子提交不可用而退回 staging/PR/merge。**

## Archive状态与CI状态分离

- `archive_status=success`：6个必需路径已经在 `main` 上重新读取并验证成功。
- `archive_status=partial`：部分 main 写入或复核失败。
- `archive_status=failed`：无法完成正式 main 归档。
- GitHub Actions `Validate Radar Reports` 仅作为**push后的独立事后校验**，不得阻塞 Scheduled Task。
- 最终 Manifest 写入触发一次 Actions run：`Validate current publication` 只校验本次变更条目的六文件包，`Validate full archive` 同时扫描完整历史、Markdown 和单元测试。
- 如果任务结束时无法取得 Actions 最终结果，记录：

```text
ci_validation_status = pending_or_unverified
```

不得虚构 `passed`。

如果之后 Actions 红叉，含义是“报告已写入 main，但CI校验失败”，不是归档未发生。

## 写入内容规则

- Markdown必须保存完整中文报告。
- JSON必须以 `templates/report.json` 为字段骨架并符合 `schemas/report.schema.json`；必须写入 `schema_version=1.0` 和 `status=published`，精简字段可作为附加字段保留，不得取代标准字段。
- JSON中至少记录：报告日期、edition、生成时间、市场状态、机会榜、交易卡、行动清单、风险预算、来源、China-Commodities-Engine与China-Options-Engine实际输入路径、各模块数据日期/生成时间/新鲜度、previous_date、errors、archive_status、ci_validation_status。
- `input_snapshots.china_commodities.trade_date` 必须是实际使用的商品 EOD 日期：优先已写快照值，其次顶层 `china_commodities_date`，再其次 `source_status.last_good_eod.date`；不得用报告日期猜测。
- 正式历史JSON的 `archive.markdown_path` 和 `archive.json_path` 应与实际历史路径一致，或在 `archive.paths` 中完整列出实际路径。
- GitHub Markdown不得包含ChatGPT专用引用标记、内部turn ID、connector ID或私有file引用；关键来源转换为普通Markdown链接/脚注，并在JSON `sources` 数组结构化保存。
- 每个 JSON `sources` 对象的 `supported_claims` 必须是字符串数组；即使只有一条，也写成 `["claim"]`，不能写成裸字符串。
- 不得将API key、访问令牌、券商凭证、私人邮件、账户信息或未经批准的非公开公司信息写入仓库。

## GitHub失败处理

- 对话中的正式报告必须正常发布；GitHub归档失败不能吞掉研究报告。
- 任一目标路径写入失败时，继续尽可能完成可安全完成的其他目标路径，并记录失败路径。
- main复核若发现任一必需路径缺失或日期/edition不正确，不得声称成功。
- 若状态文件可以写入，记录 `archive_status=partial` 或 `failed`；若状态文件也无法写入，则在对话中明确说明错误。

## 数据来源记录

中国商品期货/期权晨报主输入优先读取：

```text
farfromexact/China-Commodities-Engine/data/report_input_latest.json
```

该汇总层只包含 EOD 数据和明确的质量状态；`surface_ready`、`positioning_ready`、`execution_ready` 必须按字段/到期日分别读取，不能把全局曲面状态写成全链路执行就绪。

中国股指衍生品数据优先读取：

```text
farfromexact/China-Options-Engine/data/radar_latest.json
```

历史多周期比较优先读取：

```text
farfromexact/China-Options-Engine/data/radar_history.json
```

需要逐执行价/逐合约细节时读取：

```text
farfromexact/China-Options-Engine/data/latest.json
```

需要审计或历史重建时读取：

```text
farfromexact/China-Options-Engine/data/snapshots/YYYY-MM-DD.json
```

归档JSON必须记录实际读取的路径、`date`、`generated_at`、`data_fresh`、官方EOD覆盖率、`previous_date`和错误状态。

## 中国商品期货/期权数据来源记录

商品版本优先读取：

```text
farfromexact/China-Commodities-Engine/data/report_input_latest.json
```

需要审计或逐合约细节时，再读取 `data/last_run_status.json`、`data/radar_latest.json`、`data/market_state_latest.json`、`data/options/surface_latest.json`、`data/physical/latest.json` 和 `data/external/latest.json`。

归档 JSON 必须在 `input_snapshots.china_commodities` 中记录实际读取路径、交易日、生成时间、`data_fresh`、`official_complete`、五所覆盖、`source_date_match_pct`、`full_market_ready`、`critical_module_errors`、模块质量和历史记录数。

商品报告必须明确：近月—次近月曲线不等于现货基差；未采集仓单/基差/会员排名时不得推断；`options_surface != ready` 时不得输出商品 ATM IV、偏度、PCR、Gamma 或具体期权执行价；历史不足时不得生成伪造的 1/3/5/20 日变化。

### 商品期权研究结构的固定免责声明（必填）

当商品期权链不完整、`options_execution_ready=0`、`execution_ready=false` 或 bid/ask 覆盖不足时，`commodities_tracking.options_surface.tradeable_structures` 里的每个结构只能作为研究观察；每个对象的 `condition` 或 `execution_condition` 必须包含下列固定英文句，以便通过归档校验：

```text
research only; manual quote and manual confirmation required before execution; no premium quoted
```

不得只写“fresh quotes required”或“only after live quotes”来替代该句；这些可以保留为补充条件。若无法提供上述明确免责声明，则省略 `tradeable_structures`，不得把结构呈现为可直接执行的交易建议。该固定文本也记录在 `config/archive-policy.json` 的 `commodity_input_data.partial_option_trade_structure_disclaimer` 中。

完整商品 Markdown 的变化段落标题建议固定为 `相比上一交易日真正变化`；若需标注时段，可使用 `相比上一交易日/今晨真正变化`，两者均为当前校验器认可的标题。
全球版完整 Markdown 的变化段落标题也必须包含 `真正发生了什么变化`；可按需要前置“相比昨天”或“相比 HH:MM revision N”等比较对象。
完整商品 Markdown 的事件段落标题建议固定为 `未来24h / 7d事件` 或 `未来24小时与7天事件`；两者均为当前校验器认可的标题。
商品晨间版如沿用既有版式，`相比上一交易日/上一revision真正变化`、`9:00后风险地图` 与 `未来24小时 / 7日事件` 也均为当前校验器认可的标题；新报告仍优先采用上面的规范标题。
## 晨间版专用规则

- `edition = morning`
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_morning.md/json`
- Latest路径：`latest/morning.md/json`
- 状态路径：`status/morning_latest.json`
- Commit message可使用：`radar: publish YYYY-MM-DD morning report`
- 周末或中国节假日可使用最近一个经过验证的中国交易日数据，JSON中设置 `weekend_mode=true` 或写明节假日模式。

## 晚间版专用规则

- `edition = evening`
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_evening.md/json`
- Latest路径：`latest/evening.md/json`
- 状态路径：`status/evening_latest.json`
- Commit message可使用：`radar: publish YYYY-MM-DD evening report`
- 正常中国交易日晚间版应验证 China-Options-Engine `date` 为当日交易日且 `data_fresh=true`；否则必须标明数据降级或滞后。
- 如北京时间20:30有美国关键宏观数据，先完成数据公布后的市场反应更新，再形成最终报告和GitHub归档。

## 商品晨间版专用规则

- `edition = commodities_morning`
- 目标开始窗口：北京时间 07:00 左右；不要求在 07:00 整点产出。前一交易日数据、隔夜外盘或关键事件尚未就绪时，等待并记录实际生成时间；仍应尽量在中国现金市场开盘前完成。
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_commodities_morning.md/json`
- Latest 路径：`latest/commodities_morning.md/json`
- 状态路径：`status/commodities_morning_latest.json`
- 使用最近完整中国交易日数据与隔夜外盘；必须标明开盘前属性，不得把尚未发生的中国日盘写成事实。

## 商品晚间版专用规则

- `edition = commodities_evening`
- 目标开始窗口：北京时间 19:30 左右；不要求在 19:30 整点产出。当日日盘或所需外盘/事件信息尚未就绪时，等待并记录实际生成时间；应在相关夜盘决策窗口前完成，而不是为赶时点降低数据质量。
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_commodities_evening.md/json`
- Latest 路径：`latest/commodities_evening.md/json`
- 状态路径：`status/commodities_evening_latest.json`
- 正常交易日应验证商品引擎交易日与报告日期相符；若不满足当日完整覆盖条件，仍可归档研究报告，但必须在 `commodities_tracking.data_quality` 标明 `degraded` 或 `stale_or_partial`，不得将数据降级误写为 GitHub 归档失败。
- 夜盘前报告必须把 21:00 风险地图与当日中国日盘事实分开描述。

## 手工测试规则

Scheduled Task正式运行以外的手工测试，默认只写：

```text
tests/YYYY-MM-DDTHH-MM-SS_{edition}.md
tests/YYYY-MM-DDTHH-MM-SS_{edition}.json
```

操作性 smoke-status 文件可以使用其他后缀，但不得冒充完整 report JSON，也不应被完整报告schema校验。

除非用户明确要求“发布为正式报告”，否则不得覆盖 `reports/`、`latest/` 或正式Manifest记录。
