# 引擎读取协议

协议版本：`engine_read_2026-11-06`。

本文件和 `prompts/` 里的四份副本只约束仓库中的文字。它们不会修改已经保存的 ChatGPT Scheduled Task。要让线上任务改口，只能由任务所有者把正文贴进任务配置。线上任务正文不在本仓库里。

六文件归档路径、写入顺序和 direct-to-main 规则不变。

## 每个仓库自己的 cutoff

三个引擎仓库各自解析 cutoff，不能靠一个未分仓库的 SHA。解析记录写在该仓库上：

- `cutoff_at` 与 `cutoff_zone`
- `commit_timestamp` 与 `commit_timestamp_source=committer_date`
- 选出的提交是 committer date 不晚于 cutoff 的那一枚，不用 author date 代替
- `cutoff_sha` 与每条已 pin 路径的 `observed_sha` 都是 40 位小写 hex，并且在同一仓库内相同

`pin_failed` 只表示这枚 SHA 还无法解析。一旦 pin 成功，后面的 `not_found`、`permission_denied`、`read_failed` 仍写这枚 40 位 SHA。

HEAD 若在 pin 之后从 A 变成 B，只在仓库上记 `head_changed_after_pin`。B 不是这棵 pinned tree 的成员，不能写成 post-cutoff 读取。若另做隔离复查，`role=isolated_followup` 且 `used_in_report=false`，不进入报告。

## 读取状态和日历分开

`read_status` 只表示字节结果：`ok`、`valid_zero`、`actual_empty`、`truncated`、`parse_error`、`not_found`、`permission_denied`、`read_failed`、`pin_failed`。

旧名只按这个方向折叠，不再混用：

- `empty` → `actual_empty`。它不是 permission，也不是 read failure。
- `missing` → `not_found`。路径或 ref 404 与 `read_failed` 不是一回事。
- `permission` 与 `permission_error` → `permission_denied`。

`not_started`、`not_due`、`stale`、`last_good` 是日历或数据时点，不是 `read_status`。开盘前可以 `read_status=ok` 且 `calendar=not_started`。

`{}` 与 `[]` 是 `valid_zero`，字节长度大于 0。只有 0 byte 才是 `actual_empty`。截断 JSON 是 `truncated`，坏 JSON 是 `parse_error`。无正文的回执不写 `blob_identity`，也不写 `json_validation`。contents 响应元数据里的 blob sha 可以作为 `blob_identity`，不必先把正文再下一次才知道 blob。

`last_good` 必须同时有 40 位 `last_good_commit_sha`、`trade_date` 和 `reason`。该 SHA 不是本次 research pin。当前新鲜快照就是这次 pin，不能再标成 last_good。

## 路径失败不连坐

普通 contents 不完整时，用同一 SHA 的 blob 或 raw 再读。raw 不可用时，保留 `ordinary_contents`，并把这一条路径的 blob 尝试写成 `read_failed` 且 `scope=per_path`，同时记下 `actual_tools`。同仓库另一条已经成功的路径保持成功，不要把仓库收成一次总失败。

商品大文件至少包括 `data/report_input_latest.json` 和 `data/night_session/latest.json`。夜盘供应商快照是 `vendor_snapshot`，`official_night_close_verified` 必须为 false。晨报对已经结束的夜盘写 `session_timing=completed`。晚报对尚未开始的当夜写 `session_timing=not_due`。

不得因文件过大标 `not_found`，不得假设 1MB。ChatGPT 只用已经连接的 GitHub 工具，不运行本仓库的 Python，也不假定 Grok 的本地 helper 存在。

## 回执放在现有字段里

不扩展 schema。`source_status` 已允许附加属性。没有 `engine_read_protocol` 的旧报告不启用这些检查。

```json
{
  "engine_read_protocol": "engine_read_2026-11-06",
  "repos": {
    "china_options": {
      "read_status": "ok",
      "calendar": "not_started",
      "cutoff_sha": "0123456789abcdef0123456789abcdef01234567",
      "cutoff_at": "2026-11-06T07:30:00",
      "cutoff_zone": "Asia/Shanghai",
      "commit_timestamp": "2026-11-05T16:00:00Z",
      "commit_timestamp_source": "committer_date",
      "head_changed_after_pin": "fedcba9876543210fedcba9876543210fedcba98"
    },
    "china_commodities": {"read_status": "permission_denied", "cutoff_sha": "1111111111111111111111111111111111111111", "cutoff_at": "2026-11-06T07:30:00", "cutoff_zone": "Asia/Shanghai", "commit_timestamp": "2026-11-05T16:00:00Z", "commit_timestamp_source": "committer_date"},
    "china_stock": {"read_status": "pin_failed"}
  },
  "source_receipts": [
    {
      "repo": "china_options",
      "repository": "farfromexact/China-Options-Engine",
      "path": "data/radar_latest.json",
      "role": "research_pin",
      "cutoff_sha": "0123456789abcdef0123456789abcdef01234567",
      "observed_sha": "0123456789abcdef0123456789abcdef01234567",
      "read_status": "ok",
      "calendar": "not_started",
      "transport": "contents",
      "blob_identity_source": "contents_metadata",
      "utf8_byte_length": 128,
      "blob_identity": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "json_validation": "object",
      "session_role": "previous_trade_day",
      "market_trade_date": "2026-11-05"
    }
  ]
}
```

上面的 SHA 只是字段形状，不是受信任的 pin。`head_changed_after_pin` 只是元数据。`calendar=not_started` 与 `read_status=ok` 可以同时成立。

## 归档校验

`scripts/engine_read_receipts.py` 只在 `source_status.engine_read_protocol` 等于本版本时检查回执是否自洽。它不访问 GitHub，也不用日历判断数据是否应该存在。

信任描述符只来自 `config/engine_read_evidence.json`。文件缺失或损坏时，引用它的回执失败，不会改用测试目录或内置替身。这组数字是 2026-11-06 对 `farfromexact/China-Commodities-Engine` 提交 `2dfb15b11da3854605013ce15349a43c783384f3` 的事后只读核对，不是当时报告已经看见这些字节的证据。

| path | UTF-8 bytes | git blob | SHA256 |
| --- | ---: | --- | --- |
| `data/report_input_latest.json` | 2266923 | `4dc792ef93e18f8a98e42af811c8b34d5e195460` | `51d01dbe8fe584dd4c12ae03792d333d38db22591f58dbdbe56fc581272168c7` |
| `data/night_session/latest.json` | 1612360 | `aa0548cb195c4a2ba8ad3c1b43c64abf2b3c5ce9` | `4193dc29e6f2628413d0ee4a7d1b7c6b11d55fd4b063ec3641ae2690dda25c0d` |
