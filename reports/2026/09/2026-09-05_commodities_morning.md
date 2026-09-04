---
report_date: 2026-09-05
edition: commodities_morning
revision: 1
generated_at_bjt: 2026-09-05T07:03:31+08:00
weekend_mode: true
archive_status: partial_pending_manifest
ci_validation_status: pending_or_unverified
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-05

## 一、今日一句话结论

**今日商品期货期权无合格交易。** 今天是周六，中国商品期货无9:00日盘；更重要的是repo把昨晚连续交易标成`trading_date=2026-09-05`，与交易日历语义冲突，因此Night Session整层降级为审计/背景，不计当前交易日fresh evidence。最接近下一有效交易日触发的是SA701、SC2610、V2701。

## 二、数据质量与覆盖

第一读取层实际读取：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需下钻`data/night_session/latest.json`，并读取`data/radar_history.json`用于归档字段。

`report_input_latest.json`：schema v2，`requested_date=2026-09-04`，`generated_at=2026-09-05T06:20:08+08:00`。Futures为9月4日完整EOD，802个合约，SHFE/INE/DCE/CZCE/GFEX五所覆盖，`full_market_ready=true`、`source_date_match_pct=100%`、`critical_module_errors=0`；但`official_complete=false`，contract metadata为partial，仓单存在5项carry-forward，basis和会员排名不可用。

模块：Futures/Market State均fresh；Physical `requested_date=2026-09-04`，18/20 fresh、2 unavailable；External 17/22 fresh、5 unavailable，主要为`context_only`，不是exact-contract import parity；Options trade_date=2026-09-04，19,394条、352个series，341个series surface-ready、74个positioning-ready、0个execution-ready，IV coverage 97.71%、OI coverage 68.21%、bid/ask coverage 0，因此所有期权结构只能研究，不能写可成交净权利金。

Night原始状态：`trading_date=2026-09-05`、`night_session_date=2026-09-04`、`generated_at=2026-09-05T06:02:14+08:00`、`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`；802个请求合约中611个有效记录，188个outside-night-window、3个no-night-trade，missing timestamp/price/quote、query error、unresolved contract均为0，coverage warnings为空。

**但日历语义闸门失败。** 2026-09-05为星期六，不存在中国商品9:00日盘。昨晚原始quote可以保留作审计和“下一有效交易日可能如何定价”的背景，但本报告不把`trading_date=2026-09-05`自行修饰为9月7日，也不把Night price/OI/Night curve计入fresh层。下一有效交易日前必须先看到repo交易日字段纠正，或用交易所一致的exact-contract fallback重新确认。

## 三、商品仪表盘

> Night列均为repo原始记录；因calendar semantic failure，统一标记`context-only / score=0`。

|板块|品种/合约|EOD close/settle|1D/5D|EOD volume/OI/ΔOI|EOD curve|Basis/Physical|Raw Night close|vs Close / vs Settle|Raw Night ΔOI|07:00 Overseas|Options|信号|
|---|---|---:|---:|---|---|---|---:|---:|---:|---|---|---|
|黑色建材|SA701|1093/1080|+1.79%/+5.16%|2.389m/1.218m/+21.2k|Contango，near-next约-5.17%|spot fresh但basis口径不足，不计层|1110|+1.56%/+2.78%|-6.6k|无exact overseas parity|surface可研究，execution false|最强观察；price强但curve冲突|
|能源化工|V2701|5128/5040|+3.07%/+11.50%|2.668m/1.135m/+91.2k|Contango|Physical仅context|5072|-1.09%/+0.63%|-32.9k|原油周线强但非PVC parity|execution false|EOD强、raw night弹性转弱|
|能源化工|SC2610|685.2/683.1|-1.13%/+15.33%|高活跃/OI下降|Backwardation约+5.40%|Physical unavailable|690.7|+0.80%/+1.11%|下降|Brent 92.68、WTI 91.48周五结算，均上涨|execution false|海外确认，但周末headline gap极高|
|贵金属|AG2610|16250/16318|+2.24%/-2.97%|price up/OI down clue|轻度Contango约-0.29%|无完整Physical层|16080|-1.05%/-1.46%|—|spot gold -1.2%，silver -1.7%|AG链存在source-date mismatch；execution false|昨日多头逻辑被海外/Night原始方向否定|
|能源化工|EG2610|5898/5844|+0.57%（5D仍高）|1.792m/392.5k/EOD price↑OI↑|Backwardation约+6.84%|Physical context|5866|-0.54%/+0.38%|-29.0k|油价偏强|execution false|双锚分歧，边际弹性下降|
|能源化工|TA701|5922/5958|-0.90%/+6.47%|0.961m/1.064m/—|Backwardation|basis C/context|5938|+0.27%/-0.34%|—|油价强但聚酯映射非exact|T-1 surface-ready样本，execution false|主要是close→settle修复，不追|
|黑色建材|FG701|978/971|+0.62%/—|1.799m/1.209m/—|Contango|Physical fresh但basis不可评分|988|+1.02%/+1.75%|—|无exact海外映射|surface ready，execution false|跟随建材情绪，证据层不足|
|新能源|LC2701|—/—|-4.08%（close口径约-7.41%）|312k/392.6k/—|Backwardation|Physical/basis不足|无制度夜盘确认|—|—|无可靠exact overseas parity|surface可研究，positioning/execution不足|全市场最弱之一；不因单日暴跌追空|

07:00海外层：Brent周五结算$92.68/bbl、+0.8%，WTI $91.48、+0.2%，周涨幅约7.6%/近10%；美国柴油均价约$5.85/gal。美国8月非农+162k、失业率4.1%，强化加息概率；spot gold在纽约下午约$4,419.09/oz、-1.2%，COMEX Dec gold结算$4,476.60、-1.4%，spot silver约$65.83、-1.7%。DXY/USDCNH没有repo exact series，本版只写“美元就业数据后先跳升、后回吐部分涨幅”，不虚构07:00点位。

## 四、相比上一交易日/今晨真正变化

1. **最强链从昨日芳烃切到国内建材/基础化工挤压。** SA、V、SF在9月4日日盘出现显著价格与活跃度扩张；其中SA EOD ΔOI约+21k、V约+91k，但两者均是Contango，价格强并未获得curve一致确认。
2. **V的headline elasticity明显转负。** EOD close 5128后，raw Night 5072，相对close -1.09%，但相对settlement仍+0.63%；这说明日盘close本身已比结算锚强很多，不能把“vs settlement仍上涨”误写成新增夜盘强势。
3. **SA raw Night继续涨，但OI线索没有确认。** 1110相对close +1.56%、相对settlement +2.78%，raw ΔOI -6.6k。只能称price/OI attribution clue，不能写成确定的“新多/空头回补”。
4. **AG昨日条件多已被否定。** 中国raw Night双锚均下跌，同时美国强就业推高加息预期、黄金白银下跌；下一有效交易日不再把AG列为追多候选。
5. **SC从昨日“headline elasticity failure”转成海外重新确认。** 中国raw Night +0.80% vs close，周五Brent/WTI也收涨；但周末存在OPEC+和中东战事双重gap，最差的做法仍是提前在休市状态把方向当成确定事实。
6. **Night pipeline本身出现比行情更重要的异常：交易日标签错误。** validation虽然pass，但`trading_date=2026-09-05`落在周六，说明现有validation没有挡住calendar-semantic error；因此本晨所有Night排序、curve和ΔOI均降级。

## 五、产业链地图

**1）SA/FG建材链：偏强观察，中等置信度。** EOD price/activity强；SA/F​​G raw Night也偏强，但SA/FG均Contango，basis又没有A/B级可交易口径。最大缺失是高质量库存/现货变化和正确归属交易日的Night curve。

**2）PVC/基础化工：EOD强、边际弹性转弱。** V EOD +4.87% close口径且OI大增，但raw Night相对close回落、OI下降；这是典型的“日盘已抢跑，隔夜新增买盘没有延续”的观察项。下一有效交易日更适合等15–30分钟验证，而不是开盘追多。

**3）SC/FU能源链：海外最强，但周末风险最高。** Brent/WTI周线和周五结算都强，柴油也紧；EOD SC仍处Backwardation。问题在于周日OPEC+会议与持续地缘冲突会先于中国下次开盘重写价格，所以方向正确也可能因gap让赔率变差。

**4）贵金属：短线由多转中性偏空。** 强就业→美元/收益率压力→gold/silver下跌，与AG raw Night同向。这里是宏观层对昨日中国多头价格层的否定，而不是简单“AG跌了所以看空”。

**5）新能源LC：最弱，但暂不追空。** 日盘close口径约-7.4%，EOD curve仍Backwardation，实体与海外映射不足。单日大跌与期限结构冲突时，追空赔率通常差于等待反弹失败确认。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。** 所有候选均低于70分：一方面今天休市，另一方面Night calendar语义异常，不能把它作为当前交易日fresh layer。

|Rank|观察项|分数|方向|持有期|阶段|工具|fresh层|数据惩罚|
|---|---|---:|---|---|---|---|---:|---|
|1|SA701 下一有效日回撤确认多|68|多|1–3D|观察/条件|SA701 futures|2|Contango、Physical/basis不足、Night calendar降级、options不可执行|
|2|SC2610 地缘/供给延续多|67|多|1–3D|观察/条件|SC2610 futures|3|周末gap、OPEC+、Night calendar降级、Physical缺失|
|3|V2701 高位失败反向空|65|空|intraday–2D|观察|V2701 futures|2|EOD强趋势尚未破、Night calendar降级、无高质量Physical|
|4|AG2610 反弹失败空|64|空|intraday–2D|观察|AG2610 futures|3|周末宏观重定价、option quote date mismatch、近月交割因素|
|5|LC2701 弱势延续空|62|空|1–3D|观察|LC2701 futures|2|无夜盘、Backwardation与价格冲突、实体确认不足|

## 七、前三名观察交易卡（今天不可执行）

### 1. SA701｜下一有效交易日回撤确认多｜68

**事实：** EOD close/settle 1093/1080，5D settlement约+5.16%，EOD ΔOI约+21.2k；near-next为明显Contango。raw Night 1095/1112/1093/1110，+1.56% vs close、+2.78% vs settlement，raw ΔOI -6.6k。

**市场定价：** 日盘和原始夜盘价格都强，但curve没有确认；raw Night price↑/OI↓只是一条归因线索。

**推断：** 若下一有效日开盘后仍能守住1090–1100并重新突破1112，才说明国内强势不仅是周五短期挤压。

**主观判断：** 赔率尚不足70分；绝不在周末把raw Night当成Monday已验证价格。

最佳表达：单腿SA701；两腿配比N/A。入场：下一有效日开盘后至少等15分钟，1090–1100承接并站回1112；第二档突破1120后回踩不破。止损：1078下方接受；逻辑失效：跌回1060附近并且Contango继续扩大。TP1 1145，TP2 1180；2个交易日不扩张则时间止损。最大计划损失0.25%–0.40% NAV。

合约参数：20吨/手、tick 1元/吨、tick value 20元/手；按1110参考名义约22,200元/手。当前动态margin、price limit和SA701 exact last trading day未能从partial metadata可靠确认，执行前必须查交易所/经纪商；实物交割，必须在交割风险窗口前roll/exit。一个/两个涨跌停压力分别为`notional × L`与`notional × [(1+L)^2-1]`，L未确认时不伪造数值。

### 2. SC2610｜地缘/供给延续多｜67

**事实：** EOD 685.2/683.1，1D settlement -1.13%、5D +15.33%，near-next Backwardation约+5.40%；raw Night 678.0/696.0/666.7/690.7，+0.80% vs close、+1.11% vs settlement。Brent/WTI周五分别结算92.68/91.48，均上涨。

**市场定价：** 海外重新给供给风险更高价格，但这恰恰把周末OPEC+/地缘消息的gap beta推高。

**推断：** 真正有优势的不是“油一定继续涨”，而是等周日/周一海外先交易后，观察中国是否仍有未定价的正弹性。

**主观判断：** 今天不建仓。下一有效中国日盘若直接gap到高位，不追。

入场：下一有效日先看海外最新价格；若SC 682–690承接且15–30分钟重新站上696，可试；或>700突破后回踩确认。止损：676下方接受；逻辑失效：跌破raw Night low 666.7并伴Brent/WTI同步回吐。TP1 710，TP2 730；1–2D时间止损。最大计划损失0.25%–0.50% NAV。

合约参数：1000桶/手、tick 0.1元/桶、tick value 100元/手；按690.7参考名义约690,700元/手。当前margin/price limit和SC2610 exact last trading day需执行前官方确认；原油实物交割，临近交割月必须roll。夜盘制度存在但本次trading_date标签异常，因此不以该session作正式交易卡fresh证据。

### 3. V2701｜高位失败反向空｜65

**事实：** EOD 5128/5040，1D settlement +3.07%、5D +11.50%，EOD OI +91.2k，curve为Contango；raw Night 5115/5144/5053/5072，-1.09% vs close但+0.63% vs settlement，raw ΔOI -32.9k。

**市场定价：** 这是本晨最典型的双收益锚分歧：相对昨收已经明显回吐，相对结算却仍显得上涨。新增信息应以vs close为主，因此边际弹性已转弱。

**推断：** 如果下一有效日不能收复5128，并在30分钟内跌破5050，周五的price↑/OI↑趋势可能转为高位失败。

**主观判断：** 只做失败确认，不预判顶部。

入场：30分钟无法站回5128且跌破5050后反抽失败；分两档5050下/5020下。止损：重新接受5145上方；逻辑失效：>5180并伴OI重新扩张。TP1 4970，TP2 4880；最多2D。风险预算0.25%–0.40% NAV。

合约参数：5吨/手、tick 1元/吨、tick value 5元/手；按5072参考名义约25,360元/手。动态margin/limit与V2701 exact last trading day未可靠确认；实物交割，进入交割月前主动roll/exit。

## 八、商品期权专项

全局：19,394条、352个series；IV coverage 97.71%，OI coverage 68.21%，bid/ask 0；aggregate `surface_ready=false`、`positioning_ready=false`、`execution_ready=false`。因此**期权今天不优于裸期货，因为连可执行净成本都无法确认。**

可研究的T-1样本：TA701、2026-12-11 expiry，ATM strike约5900、ATM IV约33.29%，RV20约25.41%，即IV-RV约+7.9 vol points；RR25约-1.27 vol、BF25约+15.21 vol。它说明隐波相对实现波动不便宜、翼部形状也极端，研究上更偏有限损失spread而非裸买，但bid/ask coverage=0，不能写权利金、净支出或滑点。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

Dealer Gamma方向未知，禁止推断Gamma squeeze/pin。AG、SC期权还出现了请求9月4日却返回9月5日source date的quote mismatch，进一步降低今晨期权可用性。

## 九、9:00开盘风险地图

今天**没有中国9:00开盘**，因此严格三层改写为“下一有效日开盘前准备”：

1. **Previous China EOD（9/4）：** SA/V/SF最强，LC最弱；SC EOD回落但curve仍Backwardation；AG日盘反弹。
2. **Raw continuous session（9/4晚）：** repo错误标为T=9/5，整层calendar-degraded，不计分。上下文上SA偏强、SC偏强、V/AG/EG相对close转弱。
3. **Friday overseas close（截至9/5早晨可见）：** oil强、gold/silver弱、美元就业后偏强。

下一有效日：SA等15–30分钟看1112能否有效突破；SC至少等15–30分钟且先检查周末后Brent/WTI；V等30分钟看5050/5128；AG等30分钟观察是否继续低于16080/16250；LC没有夜盘，至少等45分钟，避免对周五-7%单日跌幅做情绪追空。

External→China信息弹性：油价层目前对SC为正；强就业/美元层对AG为负；V/SA没有可执行海外parity，因此不能用原油或DXY替代其品种自身确认。

## 十、未来24h / 7d事件

- **9月6日：OPEC+七国产量调整月度会议**，官方已确认日期，具体时点未公布。SC/FU/LU/BU/PG是最高gap/Delta风险；更适合等待会议和周末地缘消息后再定方向。
- **9月7日：美国Labor Day。** 海外交易时段/流动性特殊，跨市场对冲可能不连续；中国若正常开市，需把海外薄流动性当额外风险预算。
- **9月10日20:30 BJT：美国8月PPI**（BLS 08:30 ET）。对贵金属、美元、实际利率以及能源通胀预期是高Delta/Vega事件。
- **9月11日00:00/02:00 BJT：EIA Weekly Petroleum Status Report**，因Labor Day延至周四12:00/14:00 ET。能源链应优先盯原油、汽油、馏分油库存与炼厂利用率，而不是只看headline crude stock。
- **9月11日16:00 BJT：IEA Oil Market Report**（巴黎10:00）。
- **9月11日20:30 BJT：美国8月CPI**（BLS 08:30 ET），本周最重要的贵金属/美元/利率vol reset之一。
- **9月12日00:00 BJT：USDA WASDE**（9月11日12:00 ET），豆粕、油脂、玉米、棉花与天气交易的核心event convexity。
- 农产品天气：FAO称全球食品价格8月升至2022年底以来高位，印度9月降雨预期偏少且El Niño风险增强；这些是未来7日的供给prior，不足以替代中国具体合约price/curve/库存确认。

## 风险预算与归档

今天无可执行新仓，因此风险预算为0；下一有效日若触发，单笔试仓0.25%–0.50% NAV，只有新增第三/第四独立fresh层后才上调。SA/FG同因子合并；SC/FU/LU同能源因子合并。压力测试必须覆盖周末gap、OPEC+意外、地缘升级/缓和、涨跌停、保证金上调、流动性消失、期权IV跳升/塌陷和交割挤压。

归档：历史MD/JSON、latest MD/JSON、status将直接写main并回读；`manifests/reports.json`当前是单行大型文件，connector只能做整文件替换且返回内容被截断。为避免覆盖丢失历史manifest，不安全重建；若无法完成manifest唯一键更新，本次`archive_status=partial`，CI=`pending_or_unverified`。

## 来源

- China-Commodities-Engine：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`、`data/night_session/latest.json`。
- 上海期货交易所交易日历/休市安排：https://www.shfe.com.cn/services/calenderandholidays/holiday/
- Reuters Oil, 2026-09-04：https://www.reuters.com/business/energy/oil-set-steepest-weekly-gain-since-mid-july-over-intensifying-us-iran-tensions-2026-09-04/
- Reuters Gold, 2026-09-04：https://www.reuters.com/world/india/gold-holds-ground-with-us-payrolls-data-radar-2026-09-04/
- Reuters US payrolls, 2026-09-04：https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/
- OPEC：https://www.opec.org/pr-detail/611-2-august-2026.html
- EIA：https://www.eia.gov/petroleum/supply/weekly/schedule.php
- BLS CPI：https://www.bls.gov/schedule/news_release/cpi.htm
- BLS PPI：https://www.bls.gov/schedule/news_release/ppi.htm
- IEA OMR：https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr
- USDA WASDE：https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：无；市场休市，且Night trading_date字段存在日历语义错误。
C. 今天应继续观察的机会：SA701下一有效日回撤确认多、SC2610周末事件后延续多、V2701高位失败空、AG2610反弹失败空。
D. 今天必须避免或退出的交易：把9月4日晚raw Night误当成“9月5日交易日”正式证据；周末预埋SC地缘方向；追多AG；在bid/ask coverage=0时执行商品期权。