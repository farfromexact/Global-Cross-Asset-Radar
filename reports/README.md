# Historical Reports

正式报告按北京时间报告日期归档：

```text
reports/YYYY/MM/YYYY-MM-DD_morning.md
reports/YYYY/MM/YYYY-MM-DD_morning.json
reports/YYYY/MM/YYYY-MM-DD_evening.md
reports/YYYY/MM/YYYY-MM-DD_evening.json
```

同一日期、同一版本重复运行时更新同一路径，由Git历史保留修订。每个JSON必须与同名Markdown配对，并在 `manifests/reports.json` 中保留唯一记录。
