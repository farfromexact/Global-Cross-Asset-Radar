# 全球商品期货期权高风险机会雷达｜晨间版｜2026-10-23

> 生成：2026-10-23 07:09:28 北京时间；信息截点：07:03。研究与决策支持，不构成下单指令，也不假定任何建议已成交或持有。

## 1. 一句话结论

截至本报告时点，无可立即执行的合格新交易；油多、银空有研究赔率，但中国当夜精确行情未发布，苹果仅观察曲线—价格背离。

最有价值的下一步观察：

1. 09:00后核SC2612是否已把Brent 113.17美元/桶充分计价，以及SC2611-SC2612是否升至至少0.70% backwardation。
2. 核AG2612能否在国际现货银54.84美元/盎司背景下完成“反抽失败→再破位”，而非低开追空。
3. 核AP701暴跌与AP611-AP612约10.67% backwardation的背离，09:15/09:30两步修复未出现前不做逆势单。

## 2. 数据质量、覆盖与事实台账

当前中国交易日T=2026-10-23（周五），最近完整EOD=2026-10-22；下一合法中国日盘09:00，EC 09:30。仓库当夜模块仍停留在trading_date=2026-10-22、session_start=2026-10-21，故对本期属于**陈旧会话**，不是calendar_mismatch，但不能冒充10月22日晚至23日凌晨行情。未取得可靠exact-contract fallback，当前Night→Day收益、夜盘曲线和触发状态全部隔离。

| 模块 | 实际取得 | 结论与局限 |
|---|---|---|
| Futures | 806合约、77品种、5所；10/22；source-date match 100%；full_market_ready=true | critical=0、invalid OHLC=0、占位5、仓单carry-forward 5；五所均为10/22 |
| Market State | 77品种，同合约20日窗口 | 1/3/5/20、RV、量仓和近远月可读；不把主力切换拼成收益 |
| Physical | 目标20、fresh 18、unavailable 2 | 全部basis仅C级且eligible=false，不能作方向/套利证据 |
| External | 目标22、fresh 17、unavailable 5 | 仓库只到10/22 19:13，均context-only；本报告另核海外结算 |
| Night | 旧会话409/806、37品种，coverage 50.7444%；query/unresolved 214 | validated/published但不属当前T；price_semantics=vendor snapshot、official close=false；本期current-night unavailable |
| Options | 目标64、成功45（70.31%）；1048样本；ATM ready 44、skew ready 26 | surface/positioning/execution均0；bid/ask coverage=0；full_chain=false；quote complete只指计划样本 |
| Metadata | 合约匹配73.45%；乘数/tick 36.10%；margin/limit 30.15%；night 0% | Top3缺项用官方合约文本补交易单位/tick；当日保证金/限幅仍待核 |
| 官方交叉核对 | SHFE 238、INE 63、CZCE 243、GFEX 48配对，价格差异0 | DCE HTTP 412，故state=partial；未核成交量/OI |
| Stock | 10/21原始EOD 5568/5576可读；复权、行业、tradability、execution未就绪 | 仅局部检索紫金、宝钢、中石化；无可改变本期排序的新经营证据，0个股票候选 |

关键事实台账：

| fact_id | 标的/口径 | 事实与观测时间 | 支持判断 | 局限/来源 |
|---|---|---|---|---|
| F01 | SC2612 EOD | close 713.4、settle 702、1D +0.17%、5D -3.20%、ΔOI -2,073；10/22收盘 | 国内油尚未表现为追涨 | [Futures](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/latest.json) |
| F02 | 国际油结算 | Brent 113.17（+4.0%）、WTI 99.47（+2.4%）；10/22纽约结算 | 油链开盘风险向上 | [Reuters](https://www.reuters.com/business/energy/oil-rises-us-orders-diplomats-leave-saudi-arabia-amid-escalating-tensions-2026-10-22/)；出口仍约17mb/d是反证 |
| F03 | AG2612 EOD | 13,608/13,831、1D -1.37%、ΔOI +4,408、curve -0.224% | 国内银已弱但不知夜盘传导 | [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/market_state_latest.json) |
| F04 | 国际贵金属 | 现货银54.84（-5.4%）、现货金4,041.39（-2.4%）；10/22 18:05 GMT附近 | 银空外部确认 | [Reuters](https://www.reuters.com/world/india/gold-drops-over-1-oil-rally-reinforces-higher-for-longer-rate-outlook-2026-10-22/) |
| F05 | AP701 | close 5,704、settle 5,730、1D -3.91%、5D -7.64%；AP611-AP612 +10.665% | 价格—曲线异常，非已证实反转 | [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/market_state_latest.json) |
| F06 | SC期权 | SC2612 11/12到期，ATM700 IV59.47%、RR25 +5.30；RV20 50.25 | 看涨保护已贵，期货优于无报价期权 | [Options](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/options/surface_latest.json) |
| F07 | AP期权 | AP701 11/26到期，ATM5700 IV30.38%、RR25 -6.38；RV20 25.75 | put偏贵，适合等待修复而非追空 | 同上；无bid/ask，不可执行 |
| F08 | current night | 最新文件trading_date=10/22而非10/23 | 所有旧夜盘触发=unknown | [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/night_session/last_run_status.json) |
| F09 | Options全局 | 45/64、surface/positioning/execution=0 | 只可局部读ATM/skew | [Quality](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/options/quality_latest.json) |
| F10 | 前序台账 | 10/22晚报已有SC多、AG空、FU多、SA空、LH空 | 继承idea_id，不重置失败与成交 | [前序报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/22548d0caeb8420ae6082a61c7a93a8d15ed5405/reports/2026/10/2026-10-22_commodities_evening.json) |

完整初筛覆盖原63代码及引擎实际77品种；新增可见PD、PT。板块结果：黑色以I/JM与FG/SA偏弱，未见三层新方向；有色NI/SS偏强、AG外盘转弱；能源SC/FU受海外油冲击但Night缺失；化工EB/MA上涨、SH/PG下跌但实体证据不足；新能源LC/PS弱；农产品AP异常最显著、M/RM偏弱；EC 5D -11.05%但地缘运输风险反向，禁止追空。未入榜品种不是未扫描，主要受Physical C级、海外不可比或流动性/合约元数据不足限制。

## 3. 市场仪表盘

| 品种/准确合约 | EOD close/settle | 1D / 5D | 量仓/波动 | 曲线、实体、期权 | 07:00海外/信号 |
|---|---:|---:|---|---|---|
| SC2612 | 713.4 / 702 | +0.17% / -3.20% | ΔOI -2,073；RV50.25 | +0.370% back；ATM IV59.47、RR+5.30 | Brent113.17；条件多，Night未知 |
| FU2701 | 4,911 / 4,812 | +0.33% / -0.50% | ΔOI +12,792；RV48.06 | 近远月+12.50%，需roll审计；期权错月 | 油链相对强观察 |
| AG2612 | 13,608 / 13,831 | -1.37% / +1.05% | ΔOI +4,408；RV31.29 | -0.224% contango；期权仅AG2611 | 银54.84；条件空，不追低开 |
| AP701 | 5,704 / 5,730 | -3.91% / -7.64% | vol z2.67；ΔOI +6,519 | AP611-612 +10.665%；ATM IV30.38、RR-6.38 | 反向修复只等双确认 |
| SA701 | 935 / 936 | -1.68% / -0.11% | ΔOI +26,897；RV16.16 | -2.146% contango；ATM IV24.93、RR+2.66 | 空头两层，call skew反证 |
| SH701 | 1,610 / 1,632 | -3.89% / -7.17% | vol z3.25；ΔOI +18,824 | curve +3.121%；Options是SH612错月 | 跌势强，错月限制 |
| LC2701 | 94,180 / 94,500 | -3.26% / -6.01% | ΔOI -2,344；RV41.52 | +0.686%；ATM IV51.70，无skew | 波动贵，优势不足 |
| PS2612 | 36,670 / 36,690 | -1.79% / -2.68% | ΔOI +6,845；RV17.82 | -5.955% contango；ATM IV32.10 | 期权溢价大，暂不追空 |
| NI2612 | 121,650 / 122,330 | +2.11% / +4.13% | ΔOI -7,597；RV17.99 | -0.131% contango；期权NI2611错月 | 价格强、曲线/OI不确认 |
| AL2612 | 23,175 / 23,190 | +0.96% / +1.89% | ΔOI +10,520；RV11.33 | +1.251%；ATM IV11.16、RR-2.17 | 旧多触发未证实，降为观察 |
| LH2701 | 9,860 / 9,940 | -1.34% / -5.02% | ΔOI +1,012；RV17.96 | -6.388% contango；无可用Options | 弱势但实体层缺 |
| EC2611 | 2,455 / 2,451.5 | -1.43% / -11.05% | ΔOI -1,163；RV44.64 | -10.035% contango | 海运地缘尾部与价格冲突，回避 |

## 4. 相比前序的真变化

1. 10/22 EOD后，SC2612只+0.17%，而随后Brent结算+4%；信息弹性尚未在可验证的中国当前夜盘中观察，旧SC条件从“21:00触发”迁移为09:00双阶段验证，未认定成交。
2. AG2612 EOD已跌1.37%，海外现货银进一步跌5.4%；方向证据增强，但夜盘传导缺失使“是否仍有剩余赔率”未知，旧idea_id保留、工具仍为期货。
3. AP701跌幅与10.665% backwardation背离扩大；新增为早期观察，不把极端曲线自动解释为供需紧张。
4. NI/AL日盘强，但NI减仓、AL此前严格触发未满足，均未升为新仓；这是价格变化，不是追溯性修改旧计划。
5. Stock输入更新到10/21，限定公开检索未取得新的经营数据来支持油、银、苹果方向；因此股票只作背景，不增第六层证据。

## 5. 产业链与利润传播

- 原油→SC/FU→炼厂：海外风险溢价最强，SC曲线仅小幅back而FU曲线极陡；若SC夜盘已高开，直接商品赔率下降。中石化利润桥同时受原油成本、炼化裂解价差、库存损益、长协和套保影响，不能由油涨推出净受益；股票不如SC表达纯粹。
- 白银→AG→矿企：银价跌可压矿山售价，但紫金利润还受金铜、销量、成本、套保、汇率与少数股东影响。没有新增公司经营披露，AG期货比股票更直接；若银价回到56.5上方，空头逻辑削弱。
- 苹果现货/交割→AP曲线：价格暴跌而近月backwardation极端，可能是等级、仓单、移仓或流动性噪声；缺A/B级现货与库存变化，不能当无风险套利。
- 煤焦钢链：I/JM偏弱、钢材未形成同步三层确认；宝钢利润需看钢价—矿焦成本—销量—库存—套保净桥，本期无新增公告改变判断。
- 航运/油运：EC下跌与中东船运风险相冲突；这不是便宜证明，相关性可能断裂，回避裸追趋势。

## 6. 统一机会榜

| 排名 | idea_id | 方向/阶段/工具 | 五层支持 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 三轴状态 |
|---:|---|---|---|---:|---:|---|
| 1 | COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021 | SC2612条件多；1-5D；期货 | 1/2/4；5反对；3缺 | 21/17/18/11/7 | 74 | 研究优先；证据3层；执行未就绪 |
| 2 | COM-M-AG2612-SILVER-REPAIR-LONG-20261021 | AG2612条件空；1-5D；期货 | 1/2/4；3/5缺 | 20/17/15/13/8 | 73 | 研究优先；证据3层；执行未就绪 |
| 3 | COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022 | FU2701条件多；油链替代 | 1/2/4；3/5缺 | 18/14/17/13/9 | 71 | 研究优先；需roll审计；未就绪 |
| 4 | COM-M-SA701-CONTANGO-WARRANT-SHORT-20261022 | SA701条件空；3-10D | 1/2；5反对；3/4缺 | 19/16/12/12/9 | 68 | 观察；2层；等双确认 |
| 5 | COM-A-AP701-BACKWARDATION-REVERSAL-LONG-20261023 | AP701反向修复多；2-10D | 2；1反对；5中性 | 18/17/10/8/5 | 58 | 早期观察；1层；不追逆势 |

分项已重算且分别不超过25/25/20/15/15；总分依次74、73、71、68、58。分数仅是研究优先级，不是胜率。

## 7. 研究/交易卡

### 卡1｜SC2612条件多

新增事实：Brent结算113.17、WTI99.47；市场已定价部分是SC日盘close较settle高11.4，但当前夜盘未知。分歧是海外风险溢价是否尚未完全传入SC及曲线。主要PnL来自国内开盘后价格与backwardation共振；竞争解释是中东出口仍约17mb/d且Brent技术超买。

- 触发：09:15收盘>=728 **AND** Brent>=112 **AND** SC2611-SC2612同刻backwardation>=0.70%；随后回踩不破722，并于09:30前重收>=728。任一缺失不做，>=732不追。
- 入场/退出：允许728-730；止损714，TP1 748，TP2 770；最迟10月28日或冲突缓和退出。
- 好/中/坏：728入场、0.4元/桶成本情景，TP1 1.36R、TP2 2.89R；730为1.07R/2.41R；732的TP1仅0.85R，放弃。
- 参数/压力：官方1000桶/手、tick0.1元/桶、tick value100元；仓库最后交易日11月30日。当日保证金/实际限幅未核。以settle702的±7%假设，一次冲击约49,140元/手、两次98,280元，止损不保证封顶。
- 风险：试仓NAV0.50%，确认后油主题累计<=1.50%；SC、FU、油相关股合并。

### 卡2｜AG2612条件空

新增事实：现货银54.84、单日-5.4%；国内EOD已跌但current-night未知。主要PnL来自海外跌幅继续传导；反证是地缘与通胀也可能激活实物/避险买盘。

- 触发：09:15反抽13,580-13,620后收<13,600 **AND** 现货银<=55；09:30前再收<13,480。直接低开<13,420不追。
- 入场/退出：13,460-13,480；计划止损13,720；TP1 13,100、TP2 12,600；10月28日或FOMC前降仓。
- 好/中/坏：13,480空、成本6点情景，风险3,690元/手，TP1 5,610元=1.52R、TP2=3.55R；13,460为1.33R/3.21R；13,420的TP1约1.03R，放弃。
- 参数/压力：官方15千克/手、tick1元/千克；仓库最后交易日12月15日。按标准合约基准±3%测，一次约6,224元/手、两次12,448元；当日参数可调整。
- Options：AG2611 10/26到期ATM13800 IV29.53%、RR-2.52，但非AG2612且临近到期，不算第五层，也不能报价执行。

### 卡3｜AP701反向修复多

新增事实：1D -3.91%而AP611-AP612 backwardation约10.665%；市场显然已定价需求/供给弱，但曲线并未同步。主要PnL只能来自超跌修复，最强反证是旧月/等级/移仓噪声。

- 触发：09:15收>5,780 **AND** 可比曲线backwardation仍>=8%；09:30回踩守5,750并重收>=5,780。曲线<5%或close<5,660取消。
- 入场/退出：5,780-5,800；止损5,660；TP1 6,000、TP2 6,200；11月6日或曲线<5%退出。
- 好/中/坏：5,780、5,790、5,800分别对应TP1约1.79R、1.58R、1.39R；高于5,800放弃。成本按2元/吨情景。
- 参数/压力：10吨/手、tick1元/吨、最后交易日2027-01-14；按标准合约±5%基准，一次约2,865元/手、两次5,730元。交割等级与实物风险高，margin未核。
- Options：ATM5700 IV30.38%高于RV20 25.75%，RR25 -6.38显示put更贵；可研究call spread，但bid/ask=0、execution_ready=false，只能待询价。

## 8. 商品期权专项

10/22 EOD为最新应得完整样本：45/64品种、core_v1/sampled_strikes，44个series可读ATM、26个可读局部25Δ skew；没有任何完整surface、positioning或execution-ready series。SC IV-RV约+9.22个百分点且call skew正，方向多宜用期货等待价格触发；AP IV-RV约+4.63、put skew显著，偏向反转观察而非追空；SA IV-RV约+8.77且call skew+2.66，是空头反证；LC IV51.70对RV41.52偏高，且无skew；AG/NI/FU与候选主力错月。不得由样本OI推全链PCR、dealer gamma或拥挤；不得编bid/ask、权利金、净成本、滑点或有限损失。

## 9. 09:00开盘风险地图

- Previous China EOD：SC/FU小涨，AG/AP/SA弱；AP曲线异常、油链海外冲击尚未在可核current-night中体现。
- Current T Night：应属2026-10-23的会话未发布；仓库最新仍是10/22旧会话，故所有“已高开/低开/触发”均为unknown。
- Overseas：Brent113.17、WTI99.47，现货银54.84、金4,041.39；这些是结算/观测价，不是中国开盘价。

情景：

- SC/FU倾向高开，但若SC>732或曲线未扩张，不追；09:15核第一层，09:30核回踩与曲线，09:45才允许加确认仓。
- AG倾向低开；低于13,420不追，等待反抽失败和现货银<=55的AND条件。
- AP只在09:15/09:30两步修复与曲线并存时成立。
- SA需09:15 close<926，随后反抽不能站回936并于09:30/09:45再收<926；旧夜盘未知，不追开盘。
- EC 09:30开盘，海运风险与趋势冲突，至少等待45分钟，不做裸方向。

## 10. 未来24小时/7日事件与行动前缺口

- 10月24日约03:00 BJT：USDA Cattle on Feed（官方周五15:00 ET计划）；影响LH/饲料链，发布前不扩大Delta。
- 10月24日约03:30 BJT：CFTC COT周报；只作仓位背景，不推dealer gamma。
- 10月27-28日美国时间：FOMC会议；贵金属、美元、实际利率Vega/Gap风险上升。
- 10月29日20:30 BJT：美国9月PCE（BEA日历）；接近7日边界，AG/AU与油的通胀交易需降杠杆。
- EIA周度石油、地缘与船运事件需按正式发布时间复核；未取得下一次官方WPSR精确时间，不在本期编造。
- 中国交易所临时保证金/限幅、当前Night exact-contract报价、Top3当日参数、Physical A/B级库存/基差仍是执行前硬缺口。

局部Stock补证：实际检索了紫金矿业、宝钢股份及中国石化近期交易所/IR入口；只找到紫金10月21日业绩说明会通知、中国石化三季报预约10月30日等日程性信息，未取得截至截点的新经营数字，故不改变商品方向或表达。价格、复权、行业与tradability能力未同时就绪，股票不称可执行。

发布闸门检查：评分加总、三张卡的好/中/坏R、乘数与tick、合约月份、日历窗口、AND/顺序触发、旧idea_id与无成交状态已重算；当前Night、当日保证金/限幅、SC近月精确同刻曲线和Physical A/B级证据未解决，相关执行状态保持not execution-ready。CI=pending_or_unverified。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：SC2612条件多、AG2612条件空、AP701反向修复多；全部必须等待09:15/09:30顺序确认，坏成交放弃。
C. 今天继续观察：FU2701油链曲线、SA701破位、NI/AL强弱延续、LH弱势与EC地缘冲突。
D. 今天必须回避或有条件退出：回避旧Night触发回填、低开追空AG、>732追多SC、缺bid/ask的期权净成本叙述；若此前按旧条件建仓，按原止损/时间退出处理，不事后移动参数。
