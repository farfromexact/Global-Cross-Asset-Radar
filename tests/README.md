# Manual Test Reports

手工试跑默认写入本目录，不得覆盖正式报告：

```text
tests/YYYY-MM-DDTHH-MM-SS_morning.md/json
tests/YYYY-MM-DDTHH-MM-SS_evening.md/json
```

只有用户明确要求“发布为正式报告”时，才同步到 `reports/`、`latest/` 和Manifest。
