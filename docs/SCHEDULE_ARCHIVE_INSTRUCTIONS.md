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

写入顺序必须为：

1. `reports/YYYY/MM/YYYY-MM-DD_{edition}.md`
2. `reports/YYYY/MM/YYYY-MM-DD_{edition}.json`
3. `latest/{edition}.md`
4. `latest/{edition}.json`
5. `status/{edition}_latest.json`
6. `manifests/reports.json`

其中 `{edition}` 只能是 `morning` 或 `evening`。

### 写入行为

- 历史路径不存在时创建；已经存在时读取当前文件 SHA 后更新同一路径，不创建无序副本。Git提交历史即修订历史。
- `latest/` 文件只能在完整报告已经生成后覆盖。
- Manifest 以 `report_date + edition` 为唯一键；重复运行时更新该条记录，而不是追加重复项。
- Markdown必须保存完整中文报告；JSON必须符合 `schemas/report.schema.json`。
- JSON中必须记录：报告日期、版本、生成时间、市场状态、机会榜、交易卡、行动清单、风险预算、来源、China-Options-Engine输入数据日期和新鲜度、归档路径及状态。
- 正式历史文件的JSON字段 `archive.markdown_path` 和 `archive.json_path` 必须与实际路径一致。
- GitHub Markdown不得包含ChatGPT专用引用标记、内部turn ID、connector ID或私有file引用；将关键来源转换为普通Markdown链接/脚注，并在JSON `sources` 数组中结构化保存。
- 不得将API key、访问令牌、券商凭证、私人邮件、账户信息或未经批准的非公开公司信息写入仓库。

### GitHub失败处理

- 对话中的正式报告必须先正常发布；GitHub写入失败不能吞掉报告。
- 写入某一步失败后，不得声称完整归档成功。
- 尽量把失败信息写入 `status/{edition}_latest.json`；若状态文件也无法写入，则在对话报告末尾明确写出失败路径和错误。
- JSON `status` 使用 `published`、`archive_failed` 或 `not_published`；`archive.archive_status` 使用 `success`、`partial`、`failed` 或 `pending`。

### 数据来源记录

中国股指衍生品数据优先读取：

```text
farfromexact/China-Options-Engine/data/radar_latest.json
```

需要逐执行价/逐合约细节时读取：

```text
farfromexact/China-Options-Engine/data/latest.json
```

需要历史比较时读取：

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

除非用户明确要求“发布为正式报告”，否则不得覆盖 `reports/`、`latest/` 或正式Manifest记录。
