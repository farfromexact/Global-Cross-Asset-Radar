# 全球商品期货期权高风险机会雷达｜晨间版｜2026-10-22

> 生成：2026-10-22 07:08:03 北京时间；信息截点：07:08。中国最近完整EOD为2026-10-21；昨夜会话归属2026-10-22交易日。下一窗口：商品日盘09:00（EC 09:30），A股09:30。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；铝、镍有条件做多价值，油链旧多失效，纯碱只等两步破位。**

当前regime是“有色选择性补涨、油链EIA后冲高回落、航运/新能源弱势、期权不可执行”。研究机会存在，但均缺少开盘后触发或有效双边报价；不是“没有研究机会”，而是“没有现在可下的新仓”。

最值得验证的三个观察：①AL2612能否在09:15守住23335且跨期反向≥250；②NI2612能否在09:15守住123700并获LME≥16300确认；③SA701是否严格先破926、再反抽不过941。

## 2. 数据质量、覆盖与事实台账

仓库ref：Global Radar `0af1b3368c9232000098da5fb6d291bfe66d0188`；China Commodities `45280dc38664344a99f1f2768771720ef3db20cd`；China Stock `79c96a9d9e73a7c2a13d340229acc7c64f4ec144`。核心输入：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/45280dc38664344a99f1f2768771720ef3db20cd/data/report_input_latest.json)，requested=2026-10-21，generated=2026-10-22 06:06:01 BJT。

| 模块 | 实际覆盖/日期 | 状态与边界 |
|---|---|---|
| Futures/Market | 806合约、77品种、5所；10/21；source-date match 100% | full_market_ready=true；critical=0；OHLC占位5 |
| Official crosscheck | SHFE 238、INE 63、CZCE 243、GFEX 48；可比字段different=0 | DCE接口HTTP 412；不代表成交量/OI经官方核验 |
| Physical | 20目标，18 fresh、2 unavailable | 18条basis均C级；不能作为方向或套利确认 |
| External | 22目标，17 fresh、5 unavailable | context_only；不是可执行跨境套利 |
| Night | trading_date=10/22；409合约/37品种；50.7444% | validated/published，但214 unresolved；vendor latest trade snapshot，official close=false |
| Options | 45/64品种、1034合约、45 series | ATM-ready 44、skew-ready 33；surface/positioning/execution均0；bid/ask=0 |
| Metadata | effective match 73.45%；乘数/tick/margin/limit覆盖30.15% | DCE失败；AL/NI动态保证金与限幅不编值 |
| Stock | last-good 10/15；刷新SSL超时 | earnings bundle仅2/5576；execution not ready；映射4条且无AL/NI直接暴露 |

Night日历闸门通过：session_start_date=2026-10-21、session_end_date=2026-10-22、trading_date=2026-10-22，无calendar_mismatch。所有“night close”均只称供应商快照。

| fact_id | 关键事实 | 观测/可得时间 | 支持判断 | 局限 |
|---|---|---|---|---|
| F01 | China futures：806合约/77品种/5所，10/21 EOD，100%日期匹配，full_market_ready=true；5个OHLC占位 | 2026-10-22 06:04 BJT | 全范围价格扫描 | 不等于五所均完成官方独立核价 |
| F02 | Night：10/22交易日，10/21晚开始；409合约/37品种，50.7444%，214 unresolved | 2026-10-22 05:58 BJT | 夜盘价格层 | vendor快照，非交易所最终收盘 |
| F03 | AL2612：23050/22970；night 23300，+1.0846% vs close，ΔOI +7454 | EOD 10/21；snapshot 10/22 00:59:59 BJT | AL条件多 | 夜盘OHLC范围未官方核验 |
| F04 | AL2611-2612：EOD settlement反向325；night快照价差265 | EOD 10/21；snapshot 00:59:59 BJT | 期限层支持 | night curve仅同合约快照 |
| F05 | NI2612：121300/119800；night 123270，+1.6241% vs close，ΔOI -1506 | EOD 10/21；snapshot 01:00 BJT | NI条件多 | OI下降反对；不作新多/回补归因 |
| F06 | NI options：11/24，ATM120000 IV18.41%，RV20 17.21%，RR25 +0.61 | source date 10/21 | 局部第五层轻度支持 | bid/ask 0，execution_ready=false |
| F07 | SA701：949/952；night941；contango -2.3231%；仓单+250 | EOD 10/21；snapshot 23:00 BJT | SA条件空 | 日盘上涨且call skew反对 |
| F08 | Energy：SC/FU/BU night vs close -3.6567%/-0.8307%/-1.3418% | snapshots 23:00-02:30 BJT | 撤销旧油链多 | 快照非官方收盘 |
| F09 | Oil overseas：Brent 108.82 +0.03%，WTI 97.15 -0.7%；EIA原油-306万桶、馏分油+168万桶 | 2026-10-21 US settle/release | 油链反证 | 地缘风险仍在 |
| F10 | Options scope：45/64品种、45 series；ATM-ready44、skew-ready33；surface/positioning/execution均0 | generated 10/22 06:05 BJT | 限制第五层与执行 | 计划采样完整≠全链 |
| F11 | Stock：last valid 10/15；刷新SSL超时；映射4条，无AL/NI直接利润桥 | read 10/22 07:00 BJT | 不用股票表达 | 限定公开检索未取得截止前新经营证据 |
| F12 | Official crosscheck：SHFE238/INE63/CZCE243/GFEX48可比价差为0；DCE HTTP412 | 10/21 | 核验四所EOD价 | 不核成交量/OI；全所仍partial |

后台覆盖：原要求63个代码全部进入77品种初筛；按引擎板块计软/特色10、黑色建材10、能源化工26、农油料饲料畜牧14、新能源材料3、有色贵金属14。JR/PM/RI/WH/ZC/WR为零波动/低活跃占位，不入排名；DCE期货EOD可用，但官方交叉核对和昨夜快照缺口局部限制其执行结论。

## 3. 市场仪表盘

收益为结算口径1D/5D；Night为准确合约对前日close的供应商快照变动，非官方夜盘终值。

| 品种/主力 | EOD close/settle | 1D/5D | ΔOI | 期限/实体 | Night快照 | 海外/期权与信号 |
|---|---:|---:|---:|---|---|---|
| AL AL2612 | 23050/22970 | -0.13%/-0.63% | +8222 | backwardation +1.415%；LME 3027 | 23300 / +1.085% / +7454 | 条件多，勿追>23420 |
| NI NI2612 | 121300/119800 | +1.84%/+0.99% | -2327 | contango -0.242%；LME 16290 | 123270 / +1.624% / -1506 | 强但OI/曲线反证 |
| SS SS2612 | 13635/13495 | +0.97%/+0.19% | +10661 | contango -0.074%；— | 13780 / +1.063% / +1127 | 价格强，证据层不足 |
| CU CU2612 | 108780/109040 | +0.56%/-1.31% | +6236 | backwardation +0.633%；LME 14362 | 108920 / +0.129% / +2372 | 内外不弱，未达优选 |
| AG AG2612 | 13874/14023 | +1.17%/-2.82% | -1287 | contango -0.193%；COMEX 58.105；spot 57.73 | 14015 / +1.016% / +922 | 多空信号冲突 |
| AU AU2612 | 886.78/890.06 | -0.33%/-1.14% | -1049 | contango -0.220%；COMEX 4159.3 | 892.60 / +0.656% / -1123 | 反弹但非趋势确认 |
| SC SC2612 | 716.5/700.8 | -3.64%/-6.12% | -55 | backwardation +1.213%；Brent 108.82 | 690.3 / -3.657% / -1429 | 旧多未触发；不追空 |
| FU FU2701 | 4815/4796 | -2.68%/+0.61% | -9356 | backwardation +12.131%；WTI 97.15 | 4775 / -0.831% / +3800 | 价格弱、曲线紧 |
| BU BU2701 | 4546/4509 | +0.92%/-1.29% | -11071 | backwardation +7.206%；Brent 108.82 | 4485 / -1.342% / -7657 | 旧多未触发 |
| SA SA701 | 949/952 | +0.63%/-0.21% | -32336 | contango -2.323%；仓单+250 | 941 / -0.843% / +3845 | 两步触发空 |
| SH SH701 | 1682/1698 | -1.45%/-4.71% | +23518 | backwardation +1.700%；仓单-5 | 1658 / -1.427% / +12531 | 价格空、结构反对 |
| RM RM701 | 2266/2268 | -1.35%/-5.22% | -6528 | contango -1.146%；仓单-100 | 2261 / -0.221% / +5508 | 跌破未留存 |
| EC EC2611 | 2442/2487 | -6.26%/-8.48% | -907 | contango -11.701%；— | 无夜盘 | 趋势空但严禁追缺口 |

未入榜板块：黑色I2701结算-0.15%、RB2701 +0.36%，无同向产业/海外确认；农产品P反弹而M/RM弱，方向分裂；AP/CJ虽日涨，但5日仍-7.21%/-1.08%，不把单日反弹包装成趋势。

## 4. 相比上一交易日/今晨真正变化

1. **油链旧多明确未触发。** 前序BU需EIA后15分钟收于4568上、SC需重占722；昨夜各自最高4508、712。两项状态改为“到期未触发”，不认定成交或亏损。
2. **铝从日盘平淡变为夜盘确认候选。** AL2612日盘结算-0.13%，夜盘快照却较close +1.085%；AL2611/2612反向由325缩至265元但未消失，支持层从单纯价格扩到价格+期限+海外。
3. **镍升级但不是追价。** NI夜盘+1.624%，LME镍16290；NI2612局部RR25 +0.61提供轻度第五层，但日/夜OI下降、contango仍在，前序65升至72只意味着研究优先级提高。
4. **白银空头条件也未触发。** 昨夜低点13921，高于13820；海外现货银收57.73偏弱而内盘未破，继续观察，不把冲突强行变成新方向。
5. **航运/新能源弱势扩大但验证不足。** EC日结算-6.26%、LC/PS/SI均跌，然而无夜盘且GFEX仓单仍是9月1日陈旧值，不能追空。

## 5. 产业链地图与公司利润桥

| 链条 | 传播与强弱 | 支持/反证 | 置信度 |
|---|---|---|---|
| LME→AL/NI/SS | AL、NI最强；CU次之 | 夜盘与LME同向；AL有backwardation，NI却contango且OI降 | 中 |
| 原油→FU/BU/SC | 价格下、曲线仍紧 | EIA原油去库利多，但馏分油累库、俄乌和谈预期压回油价；国内三品种夜盘均低 | 中 |
| 纯碱→玻璃/烧碱 | SA偏空，SH结构冲突 | SA contango+仓单增；SH价格跌但backwardation扩、仓单降 | 中低 |
| 菜系/油脂→饲料 | RM/M弱，P反弹 | 菜粕仓单下降反对空；DCE昨夜缺口 | 低 |
| 航运/新能源 | EC/LC/PS/SI最弱 | 只有价格/曲线，实体和夜盘缺失 | 低 |

**Stock联动（0个候选）：** Stock仓10/15后陈旧，映射仅紫金金/铜、宝钢矿石/钢材四条，不覆盖AL/NI。限定检索上交所/巨潮10月21日前后的铝、镍、紫金相关经营公告，未取得能在截点前独立验证本期AL/NI利润传导的新事实。对中国铝业类表达，售价上升是否净受益仍取决于氧化铝/电力成本、自产比例、销量、库存、套保、汇率与资本开支；输入缺失，不能给吨毛利或盈利弹性。结论：本期直接商品期货优于股票，股票不进入统一榜。

## 6. 统一机会榜

| 排名 | idea_id / 方向 | 逻辑/赔率/催化/价曲波/拥挤 | 总分 | 五层支持；反证 | 研究/证据/执行 |
|---:|---|---:|---:|---|---|
| 1 | COM-M-AL2612-CONTINUATION-LONG-20261020<br>conditional_long 1-5D | 20/17/13/13/9 | **72** | 1,2,4；10/21日盘结算仍跌0.13%；夜盘并非交易所核验收盘；Physical仅C级且期权对应AL2611而非AL2612 | advantage_waiting_trigger / sufficient_for_70_plus / not_ready_until_09_15_and_parameters_confirmed |
| 2 | COM-E-NI2612-INNER-OUTER-STRENGTH-LONG-20261021<br>conditional_long 1-5D | 20/16/13/13/10 | **72** | 1,4,5；近月-次近月仍为0.21% contango；日盘及夜盘OI均下降；Physical缺失且期权不可执行 | advantage_waiting_trigger / sufficient_for_70_plus / not_ready_until_09_15 |
| 3 | COM-M-SA701-CONTANGO-WARRANT-SHORT-20261022<br>conditional_short 1-5D | 18/15/10/11/9 | **63** | 1,2；10/21结算上涨0.63%；ATM IV高于RV且25Δ RR偏向call；Physical基差仅C级 | early_signal / partial_two_layers / not_ready_until_two_step_trigger |
| 4 | COM-M-EC2611-DOWNTREND-NOCHASE-SHORT-20261022<br>short_watch_no_chase 1-5D | 17/13/8/13/8 | **59** | 1,2；单日已跌6.26%，追空赔率恶化；无夜盘与实体运价增量；交割与限幅参数未完成本次核验 | observed_momentum_not_alpha / partial / avoid_opening_gap |

分项逐项重算，四项均等于总分；层数上限已遵守。得分是研究优先级，不是胜率。RM701跌破2257曾被触及但昨夜收2261且无分钟顺序/留存，原短空计划保持“未知未成交”，不列新榜。

## 7. 研究/交易卡

### 卡1｜AL2612 条件多｜COM-M-AL2612-CONTINUATION-LONG-20261020

- 新事实：10/21 close/settle 23050/22970；night vendor snapshot 23300，较close +1.0846%、较settle +1.4367%，ΔOI +7454；AL2611/2612结算反向325元，night同合约快照反向265元；LME铝3M收3027美元/吨。
- 已定价与分歧：市场已计入部分外盘强势，但日盘结算仍为-0.13%，真正错价只能由09:00后守住昨夜高点及反向结构未坍塌来验证。
- 推断/PnL：若内外盘强度与反向同时保留，主PnL来自补涨和近月紧张向主力传导；若只剩跳空，信号可能只是隔夜追随。
- 触发：**09:15后15分钟收盘>23335，且AL2611-AL2612可比价差≥250、LME铝参考不低于3020；三项AND。** 09:00首跳不追；高于23420放弃。
- 入场/风控：23335/23352.5/23370好中坏；止损23150；TP1 23650、TP2 24000；2026-10-29收盘前；或3个交易日无跟随先退。
- 计算：乘数5吨、tick 5元/吨、tick value 25元。假设往返2 tick（50元/手）后，好/中/坏到TP1净R=1.56/1.35/1.17，到TP2=3.36/3.00/2.70；每手计划损失975/1062.5/1150元。费用为情景，不是实报。
- 参数/压力：最后交易日2026-12-15；动态保证金/限幅未核实，1/2限幅每手损失公式为5×成交价×L%、其两倍。止损不封顶。
- 逻辑失效：15分钟收回23150下方，或价差<150，或LME铝<2985；期货止损不保证封顶。
- 替代：AL2611/AL2612跨期反向可更纯粹表达紧张，但两腿成交与单位风险尚未核价；股票表达因公司映射/财务陈旧更差。
- 风险规模：手数=floor(NAV×风险比例/每手计划损失)；试仓0.25%-0.75%，未给NAV不报手数。

### 卡2｜NI2612 条件多｜COM-E-NI2612-INNER-OUTER-STRENGTH-LONG-20261021

- 新事实：10/21 close/settle 121300/119800，结算+1.8361%；night vendor snapshot 123270，较close +1.6241%、较settle +2.8965%，ΔOI -1506；LME镍3M 16290美元/吨；NI2612 11/24期权ATM120000 IV18.41%，RV20 17.21%，RR25 +0.61 vol。
- 已定价与分歧：价格已预交易强势，近月-次近月仍contango且OI下降；只有突破昨夜高点并获得外盘与期权局部偏度共同保留，才算未充分定价。
- 推断/PnL：主PnL来自内外盘同步延续；竞争解释是空头回补/低流动性拉升，不能由OI方向识别。
- 触发：**09:15后15分钟收盘>123700，且LME镍参考≥16300，NI2611-NI2612 contango不宽于-0.35%；三项AND。** 高开>124800放弃。
- 入场/风控：123700/123950/124200；止损121900；TP1 126600、TP2 129500；2026-10-29收盘前；2日不创新高退出。
- 计算：乘数1吨、tick 10元/吨、tick value 10元。往返2 tick情景后，好/中/坏到TP1净R=1.58/1.27/1.03，到TP2=3.18/2.67/2.28；每手计划损失1820/2070/2320元。
- 参数/压力：最后交易日2026-12-15；动态保证金/限幅未知，1/2限幅按1×成交价×L%及两倍计算。
- 期权替代：11/24 ATM120000 IV18.41%、RR25 +0.61可研究call spread；但bid/ask=0、execution_ready=false，须人工询价、确认最高净支出与行权交割，**no premium quoted**。
- 逻辑失效：跌回121900下方，或LME镍<16050，或contango<-0.6%；放弃高开>124800。
- 同因子：AL/NI/SS合并风险，不各自用满主题上限。

### 卡3｜SA701 两步触发空｜COM-M-SA701-CONTANGO-WARRANT-SHORT-20261022

- 新事实：10/21 close/settle 949/952，结算+0.6342%；near-next contango -2.3231%，仓单3464、日增250；night snapshot 941，较close -0.8430%，SA611/612仍差-22元；ΔOI +3845。ATM950 IV22.965%，RV20 15.449%，RR25 +2.88。
- 已定价与分歧：隔夜回落只部分推翻日盘上涨，且call skew与高IV反映上行尾部保险；空头错价尚未被证实。
- 触发：**先出现15分钟收盘<926，再在随后45分钟内反抽不越941；严格先后AND。**；未先破926不得入，直接低于918不追。
- 入场/风控：926/924.5/923；止损955；TP1 890、TP2 850；2026-10-29收盘前；触发后2日不延续退出。
- 计算：20吨/手，tick 1元，tick value 20元；8%保证金、7%限幅，最后交易日2027-01-14。含往返2 tick情景，好/中/坏到TP1净R=1.10/1.00/0.91，到TP2=2.39/2.23/2.09；每手计划损失620/650/680元。
- 压力：950附近一次/两次反向涨停约1330/2660元每手，高于计划止损；保证金约1520元只是占用，不是风险。
- 反证：10/21结算上涨；ATM IV22.965%高于RV15.449%，RR25 +2.88偏call。若仓单反向大降或收955上，放弃。
- 期权：12/11 put spread仅研究；缺bid/ask，不判断“便宜”与最大损失。

## 8. 商品期权专项

采样口径：10/21，core_v1 / sampled_strikes；45/64品种、45 series、ATM-ready44、skew-ready33；full_chain=false，surface/positioning/execution均不ready，bid/ask覆盖0。局部可读不等于全链。

- NI2612 11/24：ATM120000，IV18.41% vs RV17.21%，RR25 +0.61、BF25 +0.975；轻度call skew，方向支持弱，不能推出dealer gamma。
- SA701 12/11：ATM950，IV22.965% vs RV15.449%，RR25 +2.88；空头买put并不显得天然便宜，需询价后才能比较线性期货。
- RM701 12/11：ATM2275，IV16.405% vs RV19.336%，RR25 +1.67；“IV低于RV”只生成vol研究，不证明期权便宜。
- AL/AG样本对应AL2611/AG2611且10/26到期，不能拿来给AL2612/AG2612计第五层或报价。
- SH701 IV21.96% vs RV8.58%、RR25 +2.65；波动风险溢价显著但无双边报价，不做short-vol建议。

任何结构均为research only；执行前人工询价与确认，不提供未经验证的权利金、净成本、Greeks单位或滑点。

## 9. 9:00开盘风险地图

三层输入：Previous China EOD=10/21；Current T Night=10/21晚至10/22凌晨、归属10/22且日历有效；Overseas=10/21完整收盘及07:08已知消息。

- AL：潜在高开，昨夜已预交易一部分LME强势；不追首跳。09:15看23335+跨期≥250+LME≥3020，09:30看ΔOI是否继续增，09:45看回踩不破23300。
- NI：潜在高开但回补解释强；高于124800直接放弃。09:15/30/45依次看123700、contango、OI是否停止下降。
- SC/FU/BU：国内夜盘已把EIA利多与外交反证交易为净下跌；低开不追空。Brent<108且backwardation收窄才增加空头确信，重返110则警惕挤压。
- SA/SH：SA需严格两步触发；SH不追空，因为价格跌与backwardation/仓单下降冲突。
- EC/LC/PS/SI：无夜盘，首跳信息最不完整；EC 09:30，其他09:00，至少等30分钟。

## 10. 未来24h / 7d事件、覆盖核对与发布闸门

- 10月22日20:30：USDA周度出口销售；M/RM/C/CF/SR Delta风险。[USDA日程](https://www.fas.usda.gov/report-release-announcement/weekly-export-sales-309)
- 10月24日03:30：CFTC COT（15:30 ET）；用于拥挤验证，不把滞后持仓当实时流。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 10月27-28日FOMC；北京时间10月29日02:00声明、02:30记者会，AU/AG/有色Vega与美元风险。[Fed日程](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 预计10月28日22:30下期EIA WPSR，执行前再核官方排期。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 海湾航运与俄乌谈判为不定时gap源；不赋主观概率。

旧观点处置：BU、SC EIA多单条件未触发并取消；AG晚间空头条件未触发；NI沿用原idea并升分；RM保留未知未成交。输入版本：prompt radar_2026-10-12_stock_v1；consumer core_2026-10-17_v1；research_quality 2026-10-21_v1。

发布检查：四项评分加总通过；三张卡单位、乘数、tick、R和SA限幅压力已重算；AL/NI动态保证金/限幅、所有期权双边报价、DCE官方交叉核对、Stock最新经营/交易状态未解决，因此所有候选均not execution-ready。CI状态为pending_or_unverified。

## 11. 行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：AL2612、NI2612、SA701，必须按各卡AND/先后顺序触发。  
C. 今天继续观察：EC/LC/PS/SI弱势、AG/AU冲突、SC/FU/BU价格弱而曲线紧。  
D. 今天必须回避或有条件退出：回避开盘追AL/NI、追空能源/EC及全部未询价期权；若此前按旧BU/SC/AG条件计划，均未触发，不视为持仓。

## 来源

1. [China Commodities Engine report input](https://github.com/farfromexact/China-Commodities-Engine/blob/45280dc38664344a99f1f2768771720ef3db20cd/data/report_input_latest.json)（2026-10-22；支持：Futures/Market/Physical/External/Night/Options/Metadata unified input；77-product scan）
2. [China Commodities Engine night session](https://github.com/farfromexact/China-Commodities-Engine/blob/45280dc38664344a99f1f2768771720ef3db20cd/data/night_session/latest.json)（2026-10-22；支持：10/22 trading-date vendor night snapshots；coverage and price semantics）
3. [Commodity futures official price crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/45280dc38664344a99f1f2768771720ef3db20cd/data/crosschecks/futures_latest.json)（2026-10-21；支持：SHFE/INE/CZCE/GFEX comparable prices had zero differences；DCE source error）
4. [Commodity options quality and local analytics](https://github.com/farfromexact/China-Commodities-Engine/blob/45280dc38664344a99f1f2768771720ef3db20cd/data/options/quality_latest.json)（2026-10-21；支持：45/64 product coverage；no bid/ask execution readiness）
5. [Prior commodities evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/0af1b3368c9232000098da5fb6d291bfe66d0188/reports/2026/10/2026-10-21_commodities_evening.md)（2026-10-21；支持：Prior BU/SC/AG triggers and idea IDs）
6. [Reuters oil market close](https://www.reuters.com/business/energy/oil-rises-middle-east-supply-worries-2026-10-21/)（2026-10-21；支持：Brent and WTI settlements；EIA inventory changes；Russia-Ukraine talk counterweight）
7. [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)（2026-10-21；支持：October 21 weekly petroleum release）
8. [USDA Weekly Export Sales](https://www.fas.usda.gov/report-release-announcement/weekly-export-sales-309)（2026-10-22；支持：October 22 08:30 ET release）
9. [CFTC COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（2026-10-22；支持：October 23 15:30 ET COT release）
10. [Federal Reserve FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)（2026-10-22；支持：October 27-28 FOMC meeting）
11. [SHFE aluminium contract manual](https://www.shfe.com.cn/products/futures/metal/nonferrousmetal/cu_f/manual/201812/P020240320681343651143.pdf)（2026-10-22；支持：AL tick size and last-trading-day convention）
12. [SHFE nickel contract](https://www.shfe.com.cn/products/futures/metal/nonferrousmetal/ni_f/standard_ni_f/202312/t20231205_313864.html)（2026-10-22；支持：NI multiplier and tick size）
13. [China Stock Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/latest/research_inputs_latest.json)（2026-10-15；支持：Stock data staleness and research capability limitations）
14. [China Stock Engine commodity exposure mapping](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/config/company_commodity_exposures.json)（2026-10-12；支持：Only four mapped exposures; no direct aluminium or nickel mapping）
