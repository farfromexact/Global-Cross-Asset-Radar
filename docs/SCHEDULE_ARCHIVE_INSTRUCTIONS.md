# Scheduled Task GitHub Archive Instructions

把本文件中的通用规则和对应版本规则加入08:00晨间版、20:00晚间版的 Scheduled Task prompt。

## 通用归档规则

报告在对话中生成完成后，使用已连接的 GitHub 写入仓库：

```text
farfromexact/Global-Cross-Asset-Radar
```

先读取：

1. `config/archive-policy.json`
2. `schemas/report.schema.json`
3. `manifests/reports.json`
4. 对应版本的 `status/*_latest.json`
5. 对应版本的 `latest/*.json` 和 `latest/*.md`

逻辑更新集合固定为：

1. `reports/YYYY/MM/YYYY-MM-DD_{edition}.md`
2. `reports/YYYY/MM/YYYY-MM-DD_{edition}.json`
3. `latest/{edition}.md`
4. `latest/{edition}.json`
5. `status/{edition}_latest.json`
6. `manifests/reports.json`

其中 `{edition}` 只能是 `morning` 或 `evening`。

### 正式归档必须使用单次原子提交

上述6个路径是**一个归档事务**，不是6次独立Git提交。正式晨间版/晚间版归档必须优先使用 GitHub Git-data 操作一次完成：

1. 读取当前 `main` HEAD，并以其为唯一 parent/base。
2. 在任何写入发生前，先在内存中生成并校验上述6个文件的最终完整内容。
3. 对已存在路径使用替换后的完整内容；对新历史路径使用新内容。
4. 基于当前 HEAD 创建一个包含全部6个路径变更的 Git tree。
5. 只创建**一个** commit，commit message 使用对应版本规则。
6. 只将 `main` ref 前移**一次**到该 commit。
7. 最终6个文件应来自同一个 commit；一次正式归档正常情况下只触发一次 `Validate Radar Reports` workflow。

不得把正式归档实现为6次连续 `create_file` / `update_file` contents-API commit。只有在当前连接明确不提供 Git tree/commit/ref 原子操作时才允许降级。

### 原子写入不可用时：staging branch 必须完成PR合并

如果无法安全取得当前 base tree SHA，允许采用 staging branch 作为降级方案，但**staging branch不是最终归档结果**。必须连续完成：

1. 从当前 `main` 创建 `radar-archive-YYYY-MM-DD-{edition}-staging`。
2. 在该分支写齐上述6个最终路径；缺少任何一个都不得进入下一步。
3. 用 `compare main...staging` 确认分支不落后于main，且变更集合包含全部6个路径。
4. 创建指向 `main` 的 Pull Request。
5. 等待 `Validate Radar Reports`。若失败，读取日志并在同一 staging branch 修复；不得把已知失败的报告自动合并。
6. 校验通过后，使用 squash 或 merge 将PR合入 `main`。
7. 再次读取 `main` 中的历史Markdown、历史JSON和状态文件，确认正式报告已存在。
8. 只有完成第7步，才可写或声称 `archive_status=success`。仅产生 staging branch、未创建PR或未合并时，只能记为 `pending` 或 `partial`。
9. 合并完成后可删除 staging branch；不允许把黄色 “Compare & pull request” 横幅当作归档完成。

发生任何降级时，必须在 `status/{edition}_latest.json` 和对话中明确写 `atomic_commit=false`、实际commit模式及降级原因。

### 写入行为

- 历史路径不存在时创建；已经存在时更新同一路径，不创建无序副本。Git提交历史即修订历史。
- `latest/` 文件只能在完整报告已经生成后更新。
- Manifest 以 `report_date + edition` 为唯一键；重复运行时更新该条记录，而不是追加重复项。
- Markdown必须保存完整中文报告；JSON必须符合 `schemas/report.schema.json`。
- JSON中必须记录：报告日期、版本、生成时间、市场状态、机会榜、交易卡、行动清单、风险预算、来源、China-Options-Engine输入数据日期和新鲜度、归档路径及状态。
- 正式历史文件的JSON字段 `archive.markdown_path` 和 `archive.json_path` 必须与实际路径一致；或在 `archive.paths` 中完整列出实际历史Markdown与JSON路径。
- GitHub Markdown不得包含ChatGPT专用引用标记、内部turn ID、connector ID或私有file引用；将关键来源转换为普通Markdown链接/脚注，并在JSON `sources` 数组中结构化保存。
- 不得将API key、访问令牌、券商凭证、私人邮件、账户信息或未经批准的非公开公司信息写入仓库。

### Archive状态与CI状态必须区分

- `archive.archive_status=success` / `status/*_latest.json` 中的 `archive_status=success` 表示本次要求的仓库文件已经出现在 `main`。
- staging branch写齐但尚未合并时，状态只能是 `pending` 或 `partial`。
- GitHub Actions 的 `Validate Radar Reports` 是提交后的独立校验。只有该workflow通过时，自动化才可以合并staging PR。
- 如果无法在当前执行上下文读取Actions最终结果，不得把 staging PR 自动标记为成功；应保留 `ci_validation_status="pending_or_unverified"` 并明确说明尚未合并。

### GitHub失败处理

- 对话中的正式报告必须先正常发布；GitHub写入失败不能吞掉报告。
- 原子提交、staging写入、PR创建、校验或合并任一步失败时，不得声称完整归档成功。
- 尽量把失败信息写入 `status/{edition}_latest.json`；若状态文件也无法写入，则在对话报告末尾明确写出失败路径和错误。
- JSON `status` 使用 `published`、`archive_failed` 或 `not_published`；`archive.archive_status` 使用 `success`、`partial`、`failed` 或 `pending`。

### 数据来源记录

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

## 晨间版专用规则

- `edition = morning`
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_morning.md/json`
- Latest路径：`latest/morning.md/json`
- 状态路径：`status/morning_latest.json`
- Commit message：`radar: publish YYYY-MM-DD morning report`
- 周末或中国节假日可使用最近一个经过验证的中国交易日数据，JSON中设置 `weekend_mode=true` 或写明节假日模式。

## 晚间版专用规则

- `edition = evening`
- 历史路径：`reports/YYYY/MM/YYYY-MM-DD_evening.md/json`
- Latest路径：`latest/evening.md/json`
- 状态路径：`status/evening_latest.json`
- Commit message：`radar: publish YYYY-MM-DD evening report`
- 正常中国交易日晚间版应验证China-Options-Engine `date`为当日交易日且 `data_fresh=true`；否则必须标明数据降级或滞后。
- 如北京时间20:30有美国关键宏观数据，先完成数据公布后的市场反应更新，再形成最终报告和GitHub归档。

## 手工测试规则

Scheduled Task正式运行以外的手工测试，默认写入：

```text
tests/YYYY-MM-DDTHH-MM-SS_{edition}.md
tests/YYYY-MM-DDTHH-MM-SS_{edition}.json
```

操作性 smoke-status 文件可以使用其他后缀，但不得冒充完整 report JSON，也不应被完整报告schema校验。

除非用户明确要求“发布为正式报告”，否则不得覆盖 `reports/`、`latest/` 或正式Manifest记录。
