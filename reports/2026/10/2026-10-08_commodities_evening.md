# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-08｜信息截点：2026-10-08 19:40 BJT｜生成时间：2026-10-08T19:42:00+08:00｜prompt_version：radar_2026-09-06_coverage_v1｜data_protocol_version：china_commodities_v2**

> **今晚的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。**
>
> 复市EOD显示能源化工是真强势，但多数品种接近涨停式扩张；最值得研究的是TA回踩多、RU/BR二次确认与AG反抽空。它们均缺当前可执行报价或触发，不能在21:00首跳追价。

## 一、今晚一句话结论

能源供应冲击获外盘与部分曲线确认，但复市补涨、换月污染和零期权执行就绪令立即追价赔率不合格；今晚只挂条件，不追首跳。

## 二、数据质量与覆盖

- 实际读取：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[night_session/last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[radar_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按需下钻latest、physical、options quality、contract metadata。
- unified input：requested_date=2026-10-08，generated_at=19:12:09 BJT，schema_version=2。
- Futures/Market State：10月8日EOD，五所全覆盖，806合约/77品种，full_market_ready=true，source_date_match_pct=100%，critical errors=0；unknown/duplicate/invalid OHLC/negative volume或OI均为0。8条placeholder已从排行排除，20个交易日同合约历史完整。
- official_complete=false不是核心期货失败：合约参数与仓单模块部分失败。DCE合约参数抓取失败、GFEX source date未核验；合约有效匹配73.45%，动态参数覆盖30.15%。仓单仅CZCE当日可用，SHFE/DCE失败、GFEX沿用5条且stale。Basis主模块不可用，Physical中的C级代理基差只作context。
- Physical：20个目标中18个fresh，SC/LU unavailable，均为日频且未沿用。孤立现货绝对水平和C级基差不计完整实体支持层。
- External：repo日频17/22 fresh，19:11 BJT生成；15:00精确基准快照缺失，因此只报告截至19:11同日方向，不编造“15:00后涨幅”。Reuters显示Brent约105.20、WTI约92.75，[供应与航运风险仍是主因](https://www.reuters.com/business/energy/oil-rises-middle-east-supply-concerns-persist-amid-shipping-attacks-2026-10-08/)。
- Night Session：module-specific状态优先。trading_date=2026-10-08，night_session_date=2026-10-07，generated_at=07:56:58，data_fresh=false，validation_passed=false，published=false，coverage_complete=false；night_session_contract_count=0，outside_window=592，query_error/unresolved=214。10月7日为休市期，没有属于10月8日交易日的有效早前Night，不能做overnight/day decomposition；report_input内9月30日旧Night也不用于本期。
- Options：10月8日15,260条、204个series；200个surface-ready、49个positioning-ready、0个execution-ready，bid/ask覆盖0。DCE期权因权限拒绝未覆盖；全局surface/positioning/execution均false，但可使用具体series的曲面研究。不得据此报权利金、滑点或Dealer Gamma方向。
- 下一窗口：TA/RU/BR/AG/SC等预计21:00进入归属10月9日的连续交易；当前metadata的night_session字段覆盖为0，下单前必须以交易所/券商终端核验。GFEX品种按下一日盘10月9日09:00处理。

## 三、商品仪表盘（展示13项；实际扫描77品种）

1D为close相对前结算，5D为同合约结算收益；curve为near-next near-minus-deferred。带*者pair-roll污染。Night列不是今晚未来行情。

|板块|品种|具体主力|EOD close/settle|1D/5D|volume/OI/ΔOI|curve|basis/Physical/仓单|早前Night/day follow|19:11海外映射|期权S/P/E|21:00信号|
|---|---:|---|---:|---:|---:|---:|---|---|---|---|---|
|能源化工|FU|FU2611|5179/4995|18.35%/21.36%|639,615/144,059/+17,317|8.89%*|spot基差C/2568；仓单缺|N/A（休市）|油价同向↑；19:11 Brent 105.42/WTI 92.76|SY/PN/EN|首跳禁追，等45m|
|能源化工|SC|SC2611|758.5/737.4|8.96%/6.09%|76,496/27,069/+2,090|3.15%*|Physical不可得|N/A（休市）|油价同向↑；19:11 Brent 105.42/WTI 92.76|SY/PN/EN|首跳禁追，等45m|
|能源化工|TA|TA701|6830/6688|8.97%/8.89%|1,242,221/1,178,151/+161,162|3.75%|spot基差C/1168；仓单缺|N/A（休市）|油价同向↑；19:11 Brent 105.42/WTI 92.76|SY/PY/EN|回踩企稳才多，等30–45m|
|能源化工|PX|PX611|10022/9822|9.01%/7.91%|202,566/117,507/+15,951|-6.07%|spot基差C/78；仓单0/+0|N/A（休市）|油价同向↑；19:11 Brent 105.42/WTI 92.76|无同标的series|曲线反证，避免追多|
|能源化工|BR|BR2612|16415/16260|4.35%/10.80%|62,426/56,812/+10,167|2.43%|缺|N/A（休市）|TSR20 10/7 -1.16%，方向冲突|SY/PN/EN|内外冲突，等30m|
|能源化工|RU|RU2701|20145/20065|2.21%/4.94%|276,307/157,348/+6,870|0.26%|缺|N/A（休市）|TSR20 10/7 -1.16%，方向冲突|SY/PY/EN|守19900再评估，等30m|
|有色贵金属|AG|AG2612|14412/14589|-3.46%/-9.86%|195,993/294,766/+11,546|-0.21%|缺|N/A（休市）|COMEX银约-1.87%，同向偏空|SY/PN/EN|反抽失败再空，等30m|
|有色贵金属|CU|CU2611|110260/110740|0.63%/-0.04%|73,476/193,823/+8,419|0.73%|spot基差C/1847；仓单缺|N/A（休市）|COMEX铜约+0.31%，同向|SY/PY/EN|等15m确认外盘|
|黑色建材|I|I2701|682.5/690.5|-3.12%/-3.22%|301,115/605,201/+53,105|-0.86%|spot基差C/-11；仓单缺|N/A（休市）|SGX铁矿91.25；15:00基准缺|无同标的series|反抽失败再空，等30m|
|黑色建材|FG|FG701|868/880|-3.23%/-5.17%|1,284,048/1,375,714/+174,215|4.05%|spot基差C/84；仓单750/+0|N/A（休市）|代理/15:00区间增量缺|SY/PY/EN|backwardation反证，避免追空|
|农产品|OI|OI701|10250/10277|0.32%/1.30%|169,337/297,160/+13,411|1.77%|缺|N/A（休市）|CBOT豆油68.7；区间增量缺|SN/PN/EN|相对强但催化弱，等15m|
|新能源|LC|LC2701|117300/121540|-1.28%/-6.99%|227,730/409,678/-3,025|-0.23%|spot基差C/1460；仓单45839/+1209 stale|N/A（休市）|代理/15:00区间增量缺|SY/PN/EN|无夜盘；10/9 09:00|
|软商品与特色农产品|SR|SR701|5475/5486|2.60%/2.16%|548,200/548,793/-15,484|-3.06%|缺|N/A（休市）|ICE糖20.79；区间增量缺|SN/PN/EN|价涨仓减，避免追涨|

## 四、相比上一交易日/今晨真正变化

1. **能源化工从“假期外盘风险”变成中国EOD事实。** FU +18.35%、SC/TA/PX约+9%，且TA、SC、FU均价涨仓增；TA的ΔOI +161,162最突出。
2. **曲线没有一致确认整个能源链。** TA near-next backwardation +3.75%支持紧张；PX却为-6.07% contango且z=-3.28，反对“全链无差别追多”；SC/FU的curve只有1次观测且pair-roll，不能算独立确认。
3. **RU晨报条件区被日内触及，但触发仍未知。** RU低19815、高20260、收20145；无分钟路径和成交反馈，不假设用户已持仓。价涨仓增与期权call skew支持，但10月7日TSR20 -1.16%构成反证。
4. **晨报SC空头研究被新数据推翻。** SC收758.5，高于晨报735逻辑失效位；若此前按条件建立应已止损。没有成交反馈，不声称真实亏损。新的SC多头是独立、低赔率的等待触发研究。
5. **AG空头方向获EOD与外盘确认，但新仓赔率下降。** AG收14412，接近晨报TP1 14400；日内是否先触发再到目标不可核实，今晚不得在低位追空，只等反抽失败。
6. **人民币不是主驱动。** USD/CNH约6.7026、日内约+0.01%；能源和贵金属的主要新增解释来自油价、美元/利率与地缘。

## 五、产业链地图

|产业链|方向/强弱|EOD与曲线|实体/仓单|期权|海外|最大缺失|置信度|
|---|---|---|---|---|---|---|---|
|原油—燃料—芳烃—聚酯|最强；趋势上但追价差|SC/FU/TA/PX全涨；TA backwardation确认，PX contango反证，SC/FU换月污染|SC/LU Physical缺；TA/FU仅C级基差；仓单大多缺|TA曲面ready、IV35.29%；SC/FU IV>70%；全部execution not ready|Brent/WTI同向大涨|精确15:00基准、仓单/加工利润|中|
|天然/合成橡胶|RU/BR强|RU +2.21%、BR +4.35%；BR曲线z=2.87|无可计分实体/仓单|RU positioning-ready；BR not ready|TSR20下跌，冲突|外盘同时间报价、交易参数|中|
|贵金属|AG最弱、AU偏弱|AG -3.46%且contango；AU -1.32%|实体层缺|AG IV36.41% vs RV32.41%，RR略偏call|银约-1.87%、金约+0.21%|分钟路径/实盘报价|中|
|黑色建材|偏弱|I -3.12%且contango确认；FG -3.23%但backwardation反证|I/FG仅C级基差；FG仓单750、日变0|FG曲面ready；I期权缺|SGX铁矿91.25仅context|DCE仓单与期权|中低|
|油脂/软商品|分化|OI +0.32%且backwardation；P -0.88%；SR +2.60%但价涨仓减、contango|覆盖有限|OI/SR当前series不完整|WASDE临近|事件前可执行报价|中低|

未入榜板块异常：新能源LC日内冲高回落（close -1.28%、settle +2.29%）且5D -6.99%；航运EC +1.93%但curve -24.69%且只有3次观测，不称套利；特色农产品CJ -4.42%且OI上升，是弱势异常但缺独立层。

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

|#|idea_id|方向/周期|逻辑/凸性/催化/价曲波/拥挤|总分|支持层|研究判断|证据|执行|
|---:|---|---|---|---:|---:|---|---|---|
|1|COM-E-TA701-ENERGY-GAP-HOLD-20261008|回踩多，1–5D|21/14/17/13/9|74|3|存在待验证优势|部分|等待30–45分钟触发|
|2|COM-E-RU2701-RUBBER-TIGHTNESS-20261001|条件多，2–10D|22/15/14/13/9|73|3|存在待验证优势|部分|触发未知；待二次确认/参数|
|3|COM-E-BR2612-RUBBER-CONFIRMATION-20261008|条件多，1–7D|20/14/14/14/10|72|3|存在待验证优势|部分|待参数/等待触发|
|4|COM-E-AG2612-FAILED-REBOUND-SHORT-20261008|反抽空，1–5D|20/15/14/12/9|70|3|存在待验证优势|部分|等待反抽失败，禁止追空|
|5|COM-E-SC2611-SUPPLY-SHOCK-HOLD-20261008|条件多，1–5D|20/14/18/10/7|69|2|存在待验证优势|部分|等待45分钟/参数|

各分项均不超上限，总分已复核。TA/RU/BR/AG具3个有效独立支持层；SC只有2层，按纪律封顶69。风险偏好没有增加分数。

研究观察池：I2701条件空（约65，价—仓与contango两层）、FU2611回踩多（约68，price/OI与外盘两层；curve受roll污染）、3×TA701多/2×PX611空的近似美元中性RV（3TA名义102,450元、2PX名义100,220元，差2.2%；不是beta或工艺中性，缺历史分布，暂不下单）。

## 七、前三名交易卡

### 1. TA701能源冲击回踩多

- **事实：** close 6830、settle 6688、1D +8.97%/+6.70%，volume 1,242,221，OI 1,178,151，ΔOI +161,162；无有效早前Night。海外油价同向。
- **市场定价：** 隐含供应冲击继续向聚酯链传导。
- **推断/分歧：** 方向可信度高于全链平均，但首日收近高位已预交易大量消息，21:00首跳赔率差。
- **证据层：** 支持=价格/OI、曲线、海外；反对=Physical只C级、TA仓单缺、期权无bid/ask。
- **最佳表达：** TA701期货条件多。期权备选为TA701 2026-12-11到期买6700C/卖7200C 1:1，仅研究；ATM IV 35.29% vs RV20 31.12%，RR25 +0.08，positioning-ready但execution-ready=false，最大净支出/Greeks/成交成本均待人工报价。
- **入场/退出：** 21:30后6720–6780守住并重站6800；先1/2，Brent仍>104且curve不弱再加1/2。止损6610；TP1 7040出1/3，TP2 7280出1/3，其余跟踪；3日不达TP1退出。直接>6900放弃。
- **好/中/坏成交：** 6750成交，TP1≈2.07R、TP2≈3.79R；6830成交约0.95R/2.05R；>6900不做。未含手续费与跳空滑点。
- **参数：** multiplier 5吨、tick 2元、tick value 10元、close名义34,150元、margin 7%（按settle约2,341元）、limit 6%、last trading day 2027-01-14；night_session字段缺，需临盘确认。12月20日前退出/换月，避免1月交割。
- **最大损失与压力：** 期货不限定最大损失；6800→6610约950元/手计划风险，单笔≤NAV 0.50%。一/两个6%限板约2,049/4,098元/手，未含gap、保证金上调和流动性消失。
- **催化/最坏情景：** 1–3D航运/地缘；10月14日IEA、15日EIA。最坏为消息逆转和跳空低开。

### 2. RU2701橡胶紧张度延续

- **事实：** close 20145、settle 20065，日内19815–20260，ΔOI +6,870，curve +0.26%，RV20 21.88%；无有效早前Night。
- **市场定价：** 国内紧张度与call skew仍需溢价。
- **推断/分歧：** 国内支持，但TSR20 10月7日-1.16%反对；晨报区间已触及而分钟路径缺，触发状态未知。
- **证据层：** 支持=价格/OI、curve、options；反对=外盘、实体层缺。
- **最佳表达：** RU2701条件多；RU2701 2026-12-25到期20000/22000 call spread 1:1仅研究。ATM IV26.67% vs RV21.88%，RR25 +3.06，positioning-ready，execution-ready=false；最大损失仅在取得真实净权利金后才能定义。
- **入场/退出：** 21:30后19900–20100企稳并重站20150；突破20260且OI续增再加。沿用晨报止损19600；TP1 20750、TP2 21400；5日不达TP1减半、10日退出。>20300不追。
- **情景：** 20000成交对应TP约1.88R/3.50R；20150约1.09R/2.27R；参数未确认或>20300为坏成交，放弃。
- **参数/压力：** 当前verified metadata的multiplier、tick、margin、limit、night session均为空；last trading day 2027-01-15。不得用常识值冒充本期参数，人民币notional、1/2限板压力待确认。期货最大损失不有限；试仓≤NAV 0.50%。
- **催化/最坏情景：** 1–5D内外盘重新同步与OI留存。最坏为外盘继续下跌、换月/流动性突变和夜盘gap。

### 3. BR2612强曲线但换月噪音

- **事实：** close 16415、settle16260、1D +4.35%，ΔOI +10,167（+21.8%），near-next +2.43%、z=2.87；main roll flag=true；无有效早前Night。
- **市场定价：** 近端丁二烯橡胶紧张延续。
- **推断/分歧：** price/OI/curve一致，但主力刚换月、外盘天然胶下跌；可能是补涨和换月噪音。
- **证据层：** 支持=价格/OI、curve、options RR；反对=外盘、roll、参数缺失。
- **最佳表达：** BR2612条件多；2026-11-24到期16200/17500 call spread仅研究。ATM IV42.16% vs RV20 30.84%，RR25 +1.14，positioning/execution均false；高IV不等于便宜。
- **入场/退出：** 21:30后16200–16400守住并突破16550；1/2试仓，回踩16500不破且curve维持backwardation再加。止损15950；TP1 16950、TP2 17500；3日不达TP1退出。>16900放弃。
- **情景：** 16350成交约1.50R/2.88R；16550约0.67R/1.58R；>16900或参数缺失为坏成交，不做。
- **参数/压力：** 当前verified metadata缺multiplier/tick/margin/limit/night session；last trading day 2026-12-15。人民币notional和限板压力待确认。期货最大损失不有限；试仓≤NAV 0.35%，11月20日前退出/换月。
- **催化/最坏情景：** 1–3D换月后OI是否留存。最坏为主力换月假信号、外盘拖累和流动性蒸发。

## 八、商品期权专项

- 数据是**10月8日T日EOD**。全局204 series、surface-ready 200、positioning-ready 49、execution-ready 0；DCE期权缺失。options/surface_latest.json当前为空文件，故采用统一输入层的per-series字段，不把全局false误写为每个series均不可研究。
- TA701 12/11：ATM 6700，IV35.29%，RV20 31.12%，IV-RV约+4.16pts，RR25 +0.08，BF25 +0.78；曲面可研究，执行不可。
- RU2701 12/25：ATM20000，IV26.67%，RV20 21.88%，IV-RV约+4.78pts，RR25 +3.06；call skew支持方向但并不证明便宜。
- BR2612 11/24：ATM16200，IV42.16%，RV20 30.84%，IV-RV约+11.32pts，RR25 +1.14；高事件溢价，裸买凸性不优。
- AG2612 11/24：ATM14600，IV36.41%，RV20 32.41%，IV-RV约+4.00pts，RR25 +0.55；skew轻微反对追空。
- SC2611 10/14：ATM740，IV71.13%，RV20 60.04%，RR25 +11.52；临近到期且无bid/ask，不用作立即交易。
- 所有结构固定条件：**research only; manual quote and manual confirmation required before execution; no premium quoted**。禁止推断Dealer Gamma方向；当前没有可执行vol RV。

## 九、21:00夜盘开盘风险地图

严格四层：①10月8日中国EOD；②早前Night不存在/无效；③截至19:11–19:40海外同日快照；④尚未发生的21:00窗口归属10月9日。

|品种组|EOD|早前Night|海外|21:00预期/是否预交易|等待|开盘后确认|
|---|---|---|---|---|---|---|
|SC/FU/LU/BU/TA/PX|大涨，能源链最强|无|油价继续大涨|偏高开，但中国白天已预交易大部分；首跳不追|45m（TA 30–45m）|Brent>104、近月曲线、OI续增、涨停打开质量|
|RU/BR|价涨仓增|无|TSR20下跌|平/小高开但内外冲突|30m|19900/16200支撑、curve与OI|
|AG/AU|国内偏弱|无|银跌、金微涨|AG偏低/平开，AU平开；AG不追空|30m/15m|银价、美元/收益率、AG14600反抽|
|CU|小涨、backwardation|无|COMEX铜约+0.31%|小高/平开，部分预交易|15m|外盘持续性、110000支撑|
|I/FG/SA|国内偏弱|无|铁矿代理缺区间增量|平/低开；FG曲线反证，勿追空|30m|I contango、FG仓单/curve、OI|
|OI/P/SR|分化|无|农产品变化有限|平开为主，WASDE前不追|15–30m|外盘豆油/糖、国内curve|
|LC/SI/PS/PD/PT|LC冲高回落|不适用|外盘代理不足|本报告不确认夜盘；下一窗口10月9日09:00|开盘30m|结算—收盘背离修复|

night session参数覆盖为0，以上安排必须临盘用券商/交易所确认；若品种未开放夜盘，则条件自动顺延至10月9日09:00。

## 十、未来24h / 7d事件

- **未来24h：** [CFTC COT](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)计划10月9日15:30 ET（北京时间10月10日03:30）发布；只作拥挤验证。
- **未来24h：** [USDA 10月WASDE](https://usda.azureedge.us/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)计划10月9日12:00 ET（北京时间10月10日00:00）发布；油脂、谷物、棉糖事件前优先有限损失结构，但本期无执行报价，故延迟入场。
- **未来7d：** [IEA 10月OMR](https://www.iea.org/events/oil-market-report-october-2026)10月14日发布；影响原油/燃料Delta与期限结构。
- **未来7d边界：** [EIA周度石油报告](https://www.eia.gov/petroleum/supply/weekly/schedule.php)因假期调整至10月15日12:00 ET（北京时间10月16日00:00，略超7×24h）；SC/FU/TA需降低隔夜gap暴露。
- OPEC+于10月4日维持11月产量安排，下一次会议11月1日，未来7日无新例会；地缘、油轮/港口、飓风停产消息仍可随时改变Delta/Vega。
- 中国交易所参数：本期未核实到新的正式调整公告；DCE参数抓取失败，所有DCE条件单须人工确认。
- 黄金信用主题：AU -1.32%而COMEX金仅小涨，强美元/高收益率仍压制；没有模型证明信用溢价错价，未发现优势。
- AI现金流/Capex主题：CU +0.63%、外盘铜约+0.31%，无法把单日变动归因于AI Capex；不构成独立支持层。

## 十一、旧建议台账与覆盖核对

|idea_id|首次提出|上次状态|当前状态|处置/变更原因|
|---|---|---|---|---|
|COM-E-RU2701-RUBBER-TIGHTNESS-20261001|2026-10-01|等待09:45触发，75|等待二次确认，73|新EOD价涨仓增/curve/options支持；外盘反证；触发路径未知|
|COM-E-SC2611-CONDITIONAL-SHORT-20261006|2026-10-06|等待失败反抽，68|逻辑失效/停止|SC收758.5高于735失效位；若此前建立应止损；不假设真实持仓|
|COM-E-AG2612-FAILED-REBOUND-SHORT-20261008|2026-10-08晨|等待30m，67|等待反抽失败，70|EOD与外盘确认，但接近旧TP1，禁止低位追空；触发未知|
|COM-E-DIESEL-LOGISTICS-20261005|2026-10-05|待报价，65|继续待报价、未入榜|供应冲击强化但缺exact pair quotes/参数，不称套利|
|COM-E-OI701-RELSTRENGTH-20260930|2026-09-30|等待触发，61|继续观察|收10250、curve支持但催化弱|
|COM-SR-DIVERGENCE-20260930|2026-09-30|研究观察|降级观察|价格上涨但OI下降、contango反证|

**覆盖核对：**

- 应覆盖：强制63个不同代码（LPG以DCE代码PG映射）+引擎动态/其他品种，共77个。
- 实际取数且已分析：72个有量有仓且engine liquidity_eligible品种；强制63清单全部映射，并覆盖PL/BZ/LG/PD/PT/OP/RR/WR等动态品种。逐品种方向、1–20D同合约、curve、OI与可得Physical/Options均完成初筛。
- 不适用/流动性不足：JR/PM/RI/WH/ZC共5个，主力volume=0且OI=0，未用于排行。
- 数据不足但未删范围：DCE期权、SC/LU Physical、SHFE/DCE仓单、GFEX当日仓单、全市场高质量basis/会员排名、所有期权实时bid/ask、早前Night分解。
- 策略覆盖：方向、curve/跨期、basis、跨品种/跨市场、近似美元中性、波动率/偏度/事件凸性均扫描；basis与跨市场套利因口径/时点不齐降级。
- 周期覆盖：1–2D事件/夜盘、3–5D战术、6–20D结构均检查。
- 未入榜板块依据：黑色I/FG弱但曲线分歧；新能源LC日内反转；农产品OI/SR缺独立催化；航运EC曲线样本太短；有色除AG外无≥3层异常。
- IC及代理期权属于非商品股指范围，本商品版标“不适用”，没有用其替代商品证据。

## 十二、最终行动清单

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：TA701回踩6720–6780守住并重站6800；RU2701守19900–20100并重站20150；AG2612仅14550–14650反抽失败后空；均须等待30–45分钟及参数/报价确认。
C. 今晚应继续观察的机会：BR2612换月后OI与backwardation、SC/FU能源高弹性是否降温、I2701弱曲线、3×TA701多/2×PX611空的非beta中性RV。
D. 今晚必须避免或退出的交易：避免追涨SC/FU/PX、避免在14412附近追空AG、避免任何无bid/ask期权；若此前建立SC2611空头应按735失效规则退出。
