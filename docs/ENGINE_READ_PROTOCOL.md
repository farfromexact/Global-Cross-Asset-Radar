# 引擎读取协议

协议版本：`engine_read_2026-11-06`。

本文件和 `prompts/` 里的四份副本只约束仓库中的文字。它们**不会**修改已经保存的 ChatGPT Scheduled Task。要让线上任务改口，只能由任务所有者把正文贴进任务配置。合并本仓库的变更不等于线上任务已经更新。

六文件归档路径、写入顺序和 direct-to-main 规则不变。本协议只规定研究开始前如何读取三个引擎仓库，以及如何把可选回执放进现有 JSON。

## 固定 cutoff SHA

对每个要读的仓库，在使用其内容做研究之前先固定一个 cutoff SHA。之后该仓库的研究读取都指向这个 SHA。后出现的提交不能混进同一次研究；若工具返回了另一个 SHA，把那次读取标成隔离的 post-cutoff，不要把它当作本次 pin。

不能固定 SHA 时写明限制。不得编造 SHA、字节长度或 blob identity。

## 先读小文件，再读该 SHA 的正文

每个仓库先读小的 status / manifest，再读本次研究真正要用的内容：

- `farfromexact/China-Options-Engine`：`data/last_run_status.json`、`data/radar_latest.json`。历史或逐合约大文件仍按原研究规则，但必须落在同一个 cutoff SHA。
- `farfromexact/China-Commodities-Engine`：`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`，然后才是 `data/report_input_latest.json` 和其他大 JSON。
- `farfromexact/China-Stock-Engine`：`data/last_run_status.json`、`data/latest/manifest.json`。公司明细只在全球研究需要时再读同一 SHA，不猜分片。

路径以该 SHA 上实际存在的文件为准。文件不存在就记 `missing`，不要改读更新的提交来补。

## 普通 contents 不完整时用同一 SHA 的 blob 或 raw

普通文件读取不完整（截断、只有摘要、工具声明过大）时，用**同一个 cutoff SHA** 再取 git blob 或 raw 正文。不要改 pin，也不要改标成 `missing`。

不得假设 1MB 或其他固定上限。文件大于该上限仍然可以是完整、可解析的 JSON。回执里的长度是实际 UTF-8 字节数 `len(utf-8 bytes)`，不是字符数，也不是工具愿意返回的上限。

`{}` 和 `[]` 是合法 JSON，状态为 `valid_zero`，字节长度大于 0。只有 0 byte 才是 `empty`。截断 JSON 是 `truncated`，其余无法解析的正文是 `parse_error`。这两种都不是 `ok`，也不是源文件为空。

## 回执放在现有字段里

不扩展 schema。`source_status` 已经允许附加属性。需要留下机器可读回执时，写在 `source_status` 内，并带上本协议版本。没有这组字段的旧报告仍然有效。

```json
{
  "engine_read_protocol": "engine_read_2026-11-06",
  "repos": {
    "china_options": {
      "read_status": "ok",
      "cutoff_sha": "<sha pinned before research>",
      "last_good": {"date": "2026-11-05"},
      "freshness": "carried",
      "calendar": "session_closed"
    },
    "china_commodities": {"read_status": "permission"},
    "china_stock": {"read_status": "not_started"}
  },
  "source_receipts": [
    {
      "repo": "china_options",
      "repository": "farfromexact/China-Options-Engine",
      "path": "data/radar_latest.json",
      "role": "research_pin",
      "cutoff_sha": "<same sha>",
      "observed_sha": "<same sha>",
      "read_status": "ok",
      "transport": "contents",
      "ordinary_contents": "complete",
      "utf8_byte_length": 128,
      "blob_identity": "<git blob sha of those exact bytes>",
      "json_validation": "object",
      "freshness": "carried",
      "calendar": "session_closed"
    }
  ]
}
```

成功读取至少要有三项：实际 UTF-8 字节长度、blob identity、JSON 校验结果。`transport` 使用实际走通的那一种：`contents`、`blob` 或 `raw`。商品大 JSON 不得用 compact 摘要代替正文。

旧读取状态继续可用：`ok`、`missing`、`empty`、`truncated`、`parse_error`、`stale`、`permission_error`。新增粒度是 `valid_zero`、`permission`（`permission_error` 的同义值）、`read_failed`、`not_started`、`isolated`。

## 状态、新鲜度、日历、last_good 分开

`read_status` 只表示这次字节有没有拿到、是否解析成功。它不表示行情新不新，也不表示今天是否开市。

`freshness` 和 `calendar` 单独写。`stale` 只保留为旧别名，不能再拿来同时表示“读失败”和“数据过期”。沿用已验证的 last-good 市场快照时，`last_good` 记录市场日期或其他市场身份，不能把 cutoff SHA 本身写成 last_good。

补跑或 backfill 必须自标 `role=backfill`。一份 `as_of_date=2026-11-05` 的 backfill 不是 `2026-11-06` 的 current 读取；新鲜度写 `backfill` 或 `carried`，不要写成 `current`。

## 一个仓库失败不影响其他仓库

全球晨报和晚报必须尝试三个仓库。商品晨报和晚报必须检查这三个仓库，并且商品大文件走上面的正文回执。任一仓库可以是 `permission`、`read_failed`、`missing` 或 `not_started`。这个结果只属于该仓库，不能清空其他仓库已经读到的回执，也不能把未开始写成缺失。

## ChatGPT connector 的能力边界

线上 ChatGPT 只用当前任务里已经连接的 GitHub 工具。能用的通常是仓库文件 contents 读取；若同一次连接另外提供了该 SHA 的 git blob 或 raw 读取，普通 contents 不完整时改用其中一种，SHA 保持不变。

本协议不假定每个 ChatGPT 连接器都同时暴露 contents、blob 和 raw，也不假定工具名叫某一个固定函数。记录实际调用到的工具。若 blob/raw 不在本次工具列表里，记 `read_failed`，并写明缺的是哪一种读取；不要编造长度、blob identity 或 SHA，也不要把不完整响应写成 `missing` 或 `empty`。

不要用网页搜索代替私有仓库文件。不要要求 Scheduled Task 运行本仓库的 Python，包括 `scripts/engine_read_receipts.py`。Grok 或其他本地环境可能有 checkout 和 `gh`，线上 ChatGPT 不能假定这些 helper 存在。

## 归档校验做什么

`scripts/engine_read_receipts.py` 只在报告写出 `source_status.engine_read_protocol = engine_read_2026-11-06` 时检查回执是否自洽。它不访问 GitHub，不判断新鲜度，也不用日历决定某天是否应该有数据。

自洽包括：成功回执的三项字段齐全；`valid_zero` 的字节长度大于 0，`empty` 的字节长度为 0；截断或坏 JSON 不能标成 `ok`；普通 contents 不完整时必须是同一 SHA 的 blob 或 raw；商品大文件不能用 compact；cited canonical descriptor 的长度和 blob identity 必须与描述符一致；post-cutoff SHA 必须隔离；backfill 不能标成 current；`last_good` 不能等于 pinned SHA；`not_started` 不能同时带成功回执。

两个受信任的固定描述符只用于这个一致性检查，不是当前 HEAD，也不是 CI 现场测量：

| descriptor | UTF-8 bytes | blob identity | JSON |
| --- | ---: | --- | --- |
| `pinned_utf8_2266923` | 2266923 | `canonical-blob:2266923` | object |
| `pinned_utf8_1612360` | 1612360 | `canonical-blob:1612360` | object |

引用描述符时，长度必须等于上表，即使它大于 1MB。不引用描述符的回执不跟这两行比较。描述符数字来自已确认的 pin，校验器禁止为了“更新”它们去读 GitHub。
