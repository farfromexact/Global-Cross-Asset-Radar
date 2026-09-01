# 全球商品期货期权高风险机会雷达（晚间版）｜2026-09-01｜manual rerun r2

> **今天的商品市场究竟有没有值得冒险的机会？**
>
> **今日商品期货期权无合格交易。**

本次于北京时间 **2026-09-01 22:38** 手动补跑。核心结论不变：9月1日中国能化价格非常强、贵金属明显弱，但 China-Commodities-Engine 最新统一可用 EOD 仍停在 **2026-08-31**。22:25 被触发的 `Split EOD China Commodities Data` GitHub Actions 在单元测试阶段失败，后续 iFinD futures/options/physical/external/report-input/commit 全部未执行，因此今天的 current curve、ΔOI、RV20、T日期权 surface 仍不能闭环。按五层证据纪律，最强候选只有两层 fresh evidence，评分上限69。

最接近触发：**AU反弹失败空（69）**、**EG2610回撤承接多（69）**、**SC2610供应冲击延续（68）**。共同缺口：T日 Engine curve/OI/options；共同纪律：不把方向正确等同于交易合格。

## 一、今日一句话结论

**能化强、贵金属弱，但T日中国curve/OI/options仍缺失；今晚没有70+机会，不新增立即风险。**

## 二、数据质量与覆盖说明

第一读取层：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按候选继续参考既有 market-state / physical / external / options / contract metadata 层。

当前 root `last_run_status.json` 仍为 **run_date=2026-08-31**：核心期货 `data_fresh=true`、`full_market_ready=true`、SHFE/INE/DCE/CZCE/GFEX 五所齐全、`source_date_match_pct=100%`、`critical_module_errors=0`；但对本次9月1日晚报而言是 **T-1**。Contract metadata 仍为 partial，DCE metadata 存在 JSON decode error。Options 独立流水线的既有8月31日数据只能作背景；execution-ready 仍不足，禁止虚构bid/ask、净权利金和当前成交成本。

### 本次 China-Commodities-Engine Actions 诊断

- 22:25:46 BJT 左右，workflow **`Split EOD China Commodities Data`**（run `33519424029`）由 `workflow_dispatch` 触发。
- 结论：**failure**。
- Checkout、Python、dependencies、project install 均成功。
- `Run unit tests` 失败；170个测试中1个失败。
- 失败测试：`test_daily_twice_daily_schedule_has_distinct_night_and_daytime_roles`。
- 根因：仓库刚把 `.github/workflows/daily.yml` 的两个 GitHub cron（`3 22 * * *`、`3 10 * * *`）删除，改为由 ChatGPT automation 负责调度、workflow只保留 `workflow_dispatch`；但旧测试仍断言这两个cron必须存在。
- 因为测试位于 collection 前，`Plan idempotent iFinD collection`、token、Futures、Options、Physical、External、report-input rebuild、validate、commit/push 全部 skipped。
- 所以 **本次 Action 被触发了，但没有触发实际商品数据采集，更没有生成9月1日新EOD。**

## 三、商品仪表盘

| 板块 | 品种/合约 | 9/1日盘 | 信号 | 本次可计fresh层 |
|---|---|---:|---|---|
| 能源 | SC2610 | 637.8，+3.15% | 海外油价中国收盘后继续上行；T日curve缺 | ①④ |
| 化工 | EG2610 | 5525，+6.37% | 全市场最强之一，但延伸过大 | ①④ |
| 化工 | MA610 | 3069，+5.43% | OI日减约4.8万；价涨仓减仅归因线索 | ①④ |
| 聚酯 | PX/TA/PR | +4.01%/+3.17%/+4.36% | 系统性能化beta | ①④ |
| 贵金属 | AU | -1.87% | 美元/收益率压制，避险失效 | ①④ |
| 贵金属 | AG | -2.54% | 比黄金更弱、更高beta | ①④ |
| 有色 | ZN | +2.71% | 国内相对强，产业闭环不足 | ① |
| 有色 | CU | +0.50% | 国内强与海外利率/美元逆风冲突 | ①④ |
| 黑色 | I | +0.14% | 中性 | ① |
| 黑色 | RB/HC | -0.38%/-0.47% | 明显弱于能化 | ① |
| 农牧 | LH | -2.67% | 单日弱但fresh供需不足 | ① |
| 航运 | EC | — | 无夜盘；下一窗口次日9:00 | — |

中国9月1日日盘显示化工品延续强势：乙二醇涨超6%、甲醇涨超5%，瓶片/沥青/PVC/PX涨超4%；贵金属与生猪偏弱。来源：新华财经：https://www.cnfin.com/dz-lb/detail/20260901/4463508_1.html

海外新增映射：Reuters 9月1日报道 Brent 约 **92.66美元/桶**、WTI约 **88.24美元/桶**，均涨逾2%，霍尔木兹供应/航运风险仍在升温；这部分是中国日盘后的海外信息，不等于SC日盘已交易这段涨幅。https://www.reuters.com/business/energy/oil-prices-rise-latest-fighting-resurrects-middle-east-supply-disruption-risks-2026-09-01/

黄金则跌至两周低位附近，Reuters 报 spot gold 约 **4360.39美元/盎司**，主要由美债收益率和美元走强压制。https://www.reuters.com/world/india/gold-muted-traders-await-us-jobs-data-monitor-mideast-tensions-2026-09-01/

## 四、相比上一交易日真正变化

1. **数据闸门进一步恶化为“流程失败”而非单纯等待。** 22:25 Action 已尝试启动，但被过时的schedule unit test挡在数据采集之前。
2. **能化价格强势仍是真实T日事实。** EG/MA/PX/TA/PR/BU/V形成系统性强势，不是单一品种噪音。
3. **海外油价继续确认地缘供应溢价。** Brent/WTI在中国日盘后继续上涨，且霍尔木兹船舶通行仍低迷。
4. **贵金属safe-haven failure仍成立。** 地缘紧张却金银下跌，边际定价由美元/收益率主导。
5. **结论没有因为“晚一点再跑”而自动升级。** 缺少T日curve/OI/options就是缺少，不用旧数据冒充fresh。

## 五、产业链地图

| 链条 | 方向 | 最强/最弱 | 最大缺失 | 置信度 |
|---|---|---|---|---|
| 原油→进口化工→EG/MA/PX/TA | 强多但过热 | EG最强 | T日curve/OI/options | 中 |
| 贵金属→美元/收益率 | 偏空 | AG弱于AU | T日options/curve | 中 |
| 有色→中国增长/美元 | 分化 | ZN强、CU冲突 | exact parity/physical | 低中 |
| 煤焦钢→工业需求 | 弱/平 | RB/HC弱 | fresh实体+curve | 低 |
| 农牧 | 分化 | LH弱 | fresh供需 | 低 |

当前 regime：**Hormuz supply-route shock + oil/inflation/rates repricing + China energy-chemicals momentum + precious-metals yield shock + T-day Engine data veto**。

## 六、机会排行榜

| Rank | 机会 | 分数 | 方向 | Fresh证据 | 阶段 |
|---:|---|---:|---|---|---|
| 1 | AU反弹失败空 | 69 | 空 | ①④ | 条件观察 |
| 2 | EG2610回撤承接多 | 69 | 多 | ①④ | 条件观察 |
| 3 | SC2610供应冲击延续 | 68 | 多 | ①④ | 条件观察 |
| 4 | MA610回撤承接多 | 66 | 多 | ①④ | 观察 |
| 5 | CU相对弱化 | 63 | 空观察 | ①④ | 观察 |

**今日商品期货期权无合格交易，保留现金和观察仓。**

## 七、前三名交易卡

### 1. AU反弹失败空｜69
事实：中外金价同弱、美元/收益率上行。市场定价：机会成本通道压过避险。入场只允许在夜盘结构性反弹失败后；本次手动运行已晚于21:00，且Engine不提供中国实时夜盘，所以不伪造当前入场价。失效：海外金价持续反转走强且收益率回落。TP1=1R，TP2=2R，时间止损1—3D，最大损失NAV 0.25%—0.50%。黄金标准乘数1000克/手、tick 0.02元/克、tick value 20元；动态保证金/涨跌停以交易所临盘参数为准。

### 2. EG2610回撤承接多｜69
事实：日盘5525、+6.37%，海外油继续强。推断：延续必须由当前curve和OI确认；缺失时不升级。入场：不追第一跳，只接受回撤后的结构确认；若无法取得current curve/OI则放弃。止损：确认区间结构低点；TP1=1R、TP2=2R；1—5D；最大损失NAV 0.25%—0.50%。乘数10吨/手、tick 1元/吨、tick value 10元；DCE动态保证金/涨跌停/交割日参数本次未确认。

### 3. SC2610供应冲击延续｜68
事实：日盘637.8、+3.15%，Brent/WTI中国收盘后继续涨逾2%，霍尔木兹风险未消退。推断：只有current contango收窄/转强才足以升级。入场：等待结构接受与curve确认；Brent显著回落或地缘缓和则取消。TP1=1R、TP2=2R；1—3D；最大损失NAV 0.25%—0.50%。SC乘数1000桶/手、tick 0.1元/桶、tick value 100元；动态保证金/涨跌停需临盘官方确认。

## 八、商品期权专项

T日期权链没有因本次Action而更新，因此8月31日期权仅作背景。不能把T-1 ATM IV/RR25/BF25算作9月1日fresh evidence；execution readiness不足时不写bid/ask、净权利金或精确可成交strike。AU Put Spread、EG Call Spread、SC有限风险多头结构都仅属研究表达，**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、21:00夜盘风险地图

本次是 **22:38手动补跑**，21:00已经发生，因此不能再把“预期高开/低开”包装成未来事件；同时仓库明确不建设中国实时夜盘产品。本次保留原决策框架作为事后检查：SC/EG/MA不追首跳，AU/AG不追低点，关键确认仍是首30—45分钟接受度、海外同向、current curve/OI。由于T日Engine collection失败，这些确认未被仓库数据闭环，故本报告不把任何条件单升级为立即仓。

## 十、未来24小时 / 7日事件

- 9月2日：EIA Weekly Petroleum Status Report，正常周三10:30 ET发布；EIA当前页面明确下一次发布日期为9月2日。https://www.eia.gov/petroleum/supply/weekly/
- 9月4日附近：美国就业数据继续决定收益率/美元，对AU/AG/CU影响显著。
- 9月6日附近：OPEC+政策及霍尔木兹航运/冲突变化继续影响SC与能化。
- 最大非日历风险：霍尔木兹船舶通行、油轮袭击、美国—伊朗冲突升级/缓和；适合有限损失结构，不适合用高杠杆线性仓位赌headline。

## 十一、风险预算

条件试仓单笔最大损失NAV 0.25%—0.50%；只有恢复≥3层fresh evidence才考虑0.75%—1.50%的确认仓。EG/MA/SC/PX/TA合并为同一油价/Hormuz因子；AU/AG合并为rates-USD-Vega因子。

## 十二、本次运行与归档状态

本报告是9月1日晚间版 **revision 2 manual rerun**。研究流程已完整执行到“数据质量否决→市场扫描→机会评分→交易卡→事件→风险预算”。China-Commodities-Engine相关Action被触发但失败，失败发生在数据采集前，因此本次报告主动降级而不是伪造T日Engine数据。归档按既有规则直接更新main，不修改任何定时设置。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：AU反弹失败空、EG2610回撤承接多、SC2610供应冲击延续；但只有current curve/OI/市场结构确认后才有效。  
C. 今天应继续观察的机会：MA610、CU/ZN内外盘冲突，以及China-Commodities-Engine T日数据恢复。  
D. 今天必须避免或退出的交易：追能化首跳、追金银低点、把T-1 curve/options当fresh evidence、execution-not-ready时期权虚构精确报价。