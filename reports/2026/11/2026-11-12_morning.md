# 全球跨资产高风险偏好机会雷达｜2026-11-12 晨间版

- **实际生成时间**：2026-11-12T08:05:54+08:00
- **信息截止**：2026-11-12T08:05:00+08:00
- **时段**：美国11月11日现金市场完整收盘；美国固定收益11月11日Veterans Day休市，利率使用11月10日last-good；中国11月12日开盘前。
- **研究边界**：只作研究与交易决策支持，不自动下单；未收到成交回执，所有实际持仓均为“未提供/未知”。
- **固定仓库ref**：Global `464576ecdb9d9277a75489f7bc3b04f752a15f22`；Options `a4c16a18d16d039a30e9c162950096c9333a0a49`；Commodities `7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a`；Stock `8b496efb1a7ac54b901c223cb4a23e843ad37a65`。
- **前序基准**：严格前序 `reports/2026/11/2026-11-11_evening.json`；同版前序 `reports/2026/11/2026-11-11_morning.json`；商品辅助 `reports/2026/11/2026-11-12_commodities_morning.json`。

## 1. 一句话风险状态

**混合Risk-on修复：AI与中国小盘领涨、VIX回落，但美元续强、实际利率高位且油金分化；仅相对价值与回撤确认值得跟踪。**

本期“可研究”不等于“可立即执行”：相对价值的证据优于单边方向，但中国开盘顺序、美股借券/同步报价、美债DV01以及商品期权bid/ask都尚未获得。

## 2. 全球仪表盘与事实台账

### 2.1 全球仪表盘

| 资产 | 最新 | 1D | 1周 | 信号 | 观测时间/口径 |
|:---|:---|:---|:---|:---|:---|
| US Treasury 2Y | 4.73% | 11/10 +14bp；11/11休市 | 未同口径核验 | 前端重新定价加息 | 2026-11-10 cash close ET; UST nominal yield; last-good |
| US Treasury 10Y | 4.98% | 11/10 +12bp；11/11休市 | 未同口径核验 | 接近5%，但无11/11现金发现 | 2026-11-10 cash close ET; UST nominal yield; last-good |
| US Treasury 30Y | 5.35% | 11/10 +6bp；11/11休市 | 未同口径核验 | 供给/期限溢价仍是曲线反证 | 2026-11-10 cash close ET; UST nominal yield; last-good |
| US 10Y real yield | 2.78% | +12bp on 11/10 | 未同口径核验 | 压制黄金与长久期估值 | 2026-11-10; real yield; last-good |
| 2s30s | 62bp | -8bp on 11/10 | 未同口径核验 | 熊平后待重开验证 | 2026-11-10; 30Y-2Y |
| DXY | 102.92 | +0.67% | +1.33% vs 11/4 | 美元强而美股反弹，背离 | 2026-11-11 close; derived index |
| EUR/USD | 1.1127 | -0.78% ECB fixing | 未同口径核验 | 利差压制欧元 | 2026-11-11 ECB reference; reference fixing, not executable |
| USD/JPY | 159.23 | +0.67% derived | 未同口径核验 | 临近160，干预/波动风险 | 2026-11-11 ECB cross; EUR cross-derived |
| USD/CNH | 6.674 | -0.04% | 近乎持平 | 人民币未跟随DXY明显走弱 | 2026-11-11 vendor close; offshore quote; secondary source |
| QQQ | 690.38 | +2.28% | 未同口径核验 | AI修复但利率未确认 | 2026-11-11 US close; ETF close |
| SOXX | 155.4 | +6.02% | 未同口径核验 | 相对SMH领先1.16pp | 2026-11-11 US close; ETF close |
| SMH | 506.96 | +4.87% | 未同口径核验 | 权重集中beta仍强 | 2026-11-11 US close; ETF close |
| WTI front | $86.53/bbl | +0.57% | 未同口径核验 | 两月低位反弹 | 2026-11-11 settlement; front futures settlement |
| Brent front | $92.76/bbl | +1.39% | 未同口径核验 | 地缘/航运溢价仍在 | 2026-11-11 settlement; front futures settlement |
| Gold futures | $3,992/oz | -0.7% | 未同口径核验 | 美元强压过避险 | 2026-11-11 settlement; front futures settlement |
| GLD | 365.17 | -1.14% | 未同口径核验 | 政策信用叙事弱化 | 2026-11-11 US close; ETF close |
| VIX | 17.49 | -10.1% | 未同口径核验 | 风险偏好修复但非低风险证明 | 2026-11-11 close; Cboe index |
| MOVE | 92.43 | delayed/holiday | 未同口径核验 | 11/11债市休市，不作新验证 | last-good observed 2026-11-11; delayed composite |
| US HY OAS | 3.34pp | delayed/holiday | 未同口径核验 | 信用未显示急性压力，但数据延迟 | last-good/delayed; ICE/FRED derived |
| IH2612 / SSE50 | 2742.2 / 2765.54 | -0.45% / -0.27% | 历史不足 | basis -23.34 (-0.844%; annualized -8.33%) | 2026-11-11 official EOD; close; futures basis vs spot |
| IF2612 / CSI300 | 4043.4 / 4075.71 | +0.35% / +0.41% | 历史不足 | basis -32.31 (-0.793%; annualized -7.82%) | 2026-11-11 official EOD; close; futures basis vs spot |
| IC2612 / CSI500 | 6664.0 / 6713.18 | +1.04% / +1.01% | 历史不足 | basis -49.18 (-0.733%; annualized -7.23%) | 2026-11-11 official EOD; close; no direct same-index CFFEX option |
| IM2612 / CSI1000 | 6623.0 / 6669.55 | +1.37% / +1.37% | 历史不足 | basis -46.55 (-0.698%; annualized -6.89%) | 2026-11-11 official EOD; close; futures basis vs spot |
| HO2612 ATM / RR25 / BF25 | 14.65% / -0.982pp / 0.224pp | ATM -0.255pp | history unavailable | put skew modest | 2026-11-11 EOD; model/engine; no dealer gamma direction |
| IO2612 ATM / RR25 / BF25 | 17.79% / -1.276pp / 0.303pp | ATM -0.315pp | history unavailable | 中等put skew | 2026-11-11 EOD; model/engine; no dealer gamma direction |
| MO2612 ATM / RR25 / BF25 | 27.95% / -2.356pp / 0.181pp | ATM -1.561pp | history unavailable | 绝对IV仍高且put skew更陡 | 2026-11-11 EOD; model/engine; no dealer gamma direction |

**利率补充**：11月10日5Y约4.81%，2s10s约25bp、5s30s约54bp、10Y breakeven约2.20%；期限溢价当期精确值未取得。11月11日美元固定收益全日休市，QQQ反弹、VIX回落或TLT ETF成交都不能替代现金国债曲线发现。[SIFMA假日说明](https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026)

**FX补充**：DXY与收益率同向走强，EUR/USD与JPY走弱；USD/CNH收在约6.674、未随DXY明显走弱，支持“亚洲风险偏好尚未被美元完全压制”的条件判断，但离岸报价与ECB fixing口径不同，不能做无成本套利输入。[Reuters美元综述](https://www.reuters.com/world/asia-pacific/dollar-gains-traction-fed-speakers-warn-risks-inflation-2026-11-11/)；[ECB参考汇率](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)

### 2.2 中国商品紧凑附录

| 模块 | 源日/生成 | 实际覆盖 | 分析就绪 | 执行就绪 | 研究影响 |
|:---|:---|:---|:---|:---|:---|
| Futures | 2026-11-11 / 22:07 BJT | 5所、806合约、77品种；source-date match 100% | 是，vendor primary | 否；实时深度/保证金/账户未核 | 全63代码及动态PD/PT完成扫描；不把vendor validated写成交易所独立核验 |
| Market State | 2026-11-11 | 77品种；20日窗口18个实际观测，缺11/3、11/4 | exact-contract 1/3/5/20可按可用端点研究 | 否 | 不拼接不同主力；缺端点留缺 |
| Physical | 2026-11-11 19:12 | 20目标中18 fresh；SC/LU unavailable | C级/context only | 否 | 可作背景，不能代替高质量basis/仓单 |
| External | 2026-11-11 19:12 | 22目标中17 fresh | 部分 | 否 | WTI/Brent/LME/COMEX可辅助；缺Dubai/Oman与成品油映射 |
| Night | status=published；payload为空 | 状态覆盖与明细矛盾 | 否 | 否 | 不称官方夜盘收盘，不做Night→Day、纯夜盘OHLC/OI或价仓归因 |
| Options | 2026-11-11 | 64/64 sampled products；core ATM 60、skew 3、surface 0；bid/ask 0 | 仅逐series局部ATM/skew | 否 | 可研究IV-RV候选；不得编权利金、滑点、PCR/拥挤、dealer gamma |
| Contract metadata | last-good 2026-11-09 | 静态字段可参考；当前Wind批次unavailable | 部分 | 否 | 候选逐合约再核最后交易日、乘数、限幅与交割 |
| futures_crosscheck | 2026-11-11 | DCE HTTP412；其余4所baseline unavailable | 否 | 否 | 不是已比对价格冲突；也未核成交量/OI |

商品异常但未入榜：CU2612/CU2701 close/settle价差1220/1230，已高于旧价值区，研究结论为“有相对强势但赔率不足、等回落”；AP701 ATM样本IV 30.725%低于20日RV 37.26%，但单月、无skew、无bid/ask，不能据此宣称期权便宜；RU、EC、PP、EG、AL、C、P均有价仓或曲线异常，但实体/国际/执行证据不足，未进入统一Top5。

### 2.3 可追溯事实台账

| fact_id | 标的/值 | 口径与时点 | known_at/读取 | 支持判断 | 局限 |
|:---|:---|:---|:---|:---|:---|
| F-US-RATES-001 | UST 2Y/10Y/30Y: 4.73/4.98/5.35% | 11/10 cash close, last-good; 2026-11-10 ET close | 2026-11-10 ET; 2026-11-12T08:05:54+08:00 | curve and real-yield constraints | 11/11 fixed-income holiday |
| F-US-EQ-001 | QQQ/SOXX/SMH: 690.38/155.40/506.96 | 11/11 ETF close; 2026-11-11 16:00 ET | 2026-11-11 close; 2026-11-12T08:05:54+08:00 | AI relief and SOXX relative outperformance | not executable now |
| F-FX-001 | DXY/EURUSD/USDJPY/USDCNH: 102.92/1.1127/159.23/6.6740 | close/reference fixing; 2026-11-11 | 2026-11-11; 2026-11-12T08:05:54+08:00 | strong dollar with CNH resilience | mixed quote semantics |
| F-OIL-001 | Brent/WTI front futures: 92.76/86.53 USD/bbl | settlement; 2026-11-11 | 2026-11-11; 2026-11-12T08:05:54+08:00 | oil rebound and SC external condition | full curve/cracks/skew unavailable |
| F-GOLD-001 | front gold/GLD: 3992 USD/oz / 365.17 | settlement/ETF close; 2026-11-11 | 2026-11-11; 2026-11-12T08:05:54+08:00 | gold thesis weakening | fresh ETF flow/CFTC/IV missing |
| F-CN-IDX-001 | IH/IF/IC/IM2612 and cash indices: official 2026-11-11 EOD | close, settlement, OI, cash close; 2026-11-11 15:00 BJT | 2026-11-12 07:16 BJT; 2026-11-12T08:05:54+08:00 | smallcap relative trade | no intraday path or beta |
| F-COM-001 | China commodity futures universe: 806 contracts / 77 products / 5 exchanges | Wind EOD; 2026-11-11 | 2026-11-11 22:07 BJT; 2026-11-12T08:05:54+08:00 | full-range commodity scan | independent official crosscheck unavailable |
| F-COM-OPT-001 | China commodity options sample: 64/64 products; core ATM ready60; skew ready3; bid/ask0 | core_v1 sampled_strikes; 2026-11-11 | 2026-11-11 22:07 BJT; 2026-11-12T08:05:54+08:00 | bounded local IV research | not full chain, surface, positioning or execution ready |
| F-STOCK-001 | A-share universe: 5580 quotes/status; 5574 traded; 3538 up/1828 down | 11/11 EOD; 2026-11-11 | 2026-11-11 22:19 BJT; 2026-11-12T08:05:54+08:00 | breadth and bounded discovery | industry/index/tradability/forecasts missing |

## 3. 相比前序真正发生了什么变化

1. **AI修复由盘中变为收盘确认：QQQ +2.28%、SOXX +6.02%、SMH +4.87%；SOXX/SMH比率+1.13%，旧相对价值篮子收盘毛PnL约+57.43美元。** 处置：AI idea price validation up; do not chase after large gap。
2. **中国小盘相对强势获得官方11/11 EOD确认：CSI1000较SSE50领先1.64pp，IM OI +9,945且贴水更浅；Stock breadth 3538/1828。** 处置：IM/IH score 69->73; promoted to rank1。
3. **商品核心期货恢复为11/11五所806合约，期权样本64/64且ATM-ready60；这是数据能力恢复，不是催化。** 处置：commodity research confidence up; execution readiness unchanged。
4. **Brent/WTI反弹而SC日盘仍弱；今夜EIA前，供应风险和库存反证并存。** 处置：SC remains conditional, no immediate delta expansion。
5. **黄金期货与GLD再跌，DXY升至102.92；因债市休市，不能把风险资产反弹解释为实际利率回落。** 处置：gold policy-credit thesis weakened, outside Top5。
6. **Stock Engine恢复11/11全市场价量历史，但行业/指数/可交易性仍缺；限定公告检索只找到资本配置事实，未形成A股Top5。** 处置：research coverage improved, no execution candidate。

没有新增证据证明“低VIX=期权便宜”、也没有证据证明中国期指OI增长必然来自新多；这两类推论本期继续拒绝。Stock Engine的数据恢复与商品数据恢复都属于输入能力变化，不计入市场催化。

## 4. 全球统一Top5

| 排名 | 机会/方向 | 期限与阶段 | 工具 | 逻辑/赔率/催化/价曲波/拥挤 | 总分 | 研究/证据/执行 |
|:---|:---|:---|:---|:---|:---|:---|
| 1 | IM2612多 / IH2612空小盘相对强度；long 5 IM2612 / short 8 IH2612; near dollar-neutral, not beta-neutral | 3-10交易日；conditional_next_session | IM2612 + IH2612 | 21/18/15/10/9 | 73 | 待验证优势；部分：官方现金指数、期指价量仓与基差、ETF份额估算；beta与实时深度缺失；等09:30后完整顺序与实时深度 |
| 2 | SOXX多 / SMH空半导体ETF相对价值；long 33 SOXX / short 10 SMH; near dollar-neutral, not beta-neutral | 5-20交易日；validated_price_move_wait_pullback | SOXX + SMH | 22/18/15/9/8 | 72 | 价格验证增强、基本面纯度下降；部分：同日ETF收盘、公司/行业事件、风险指标；borrow/beta/费用缺；等待回撤、同步报价与借券核验 |
| 3 | M2701-M2705近多远空；long 1 M2701 / short 1 M2705 | 1-7交易日；conditional_wait_day_pullback | DCE M2701 + DCE M2705 | 21/17/17/9/7 | 71 | 有待验证优势；价格/OI、期限、实体、海外4层；basis/仓单/执行仍缺；等待09:00后回撤—收复顺序 |
| 4 | SC2612事件型多头，仅收复后；conditional long SC2612 | 1-5交易日；conditional_wait_reclaim | INE SC2612 | 20/15/17/9/7 | 68 | 待验证优势；海外与期限2层，国内价格层混合；EIA待发；等待09:00后收复与回踩 |
| 5 | 美国2s30s曲线趋平；flattener after cash reopen | 5-15交易日；await_cash_reopen_auction_and_dv01 | US Treasury 2s30s + DV01-neutral futures or swaps | 20/16/15/8/8 | 67 | 有待验证优势；CPI/Fed路径与11/10曲线支持；11/11现券休市无新发现；待现金债重开、30Y供给结果、DV01/roll/账户核验 |

分数是研究优先级，不是胜率、预期收益或仓位。五项分数均已重加总；所有候选的实际持仓状态都是未提供/未知。

- **#1 IM/IH**：新增事实是小盘现金指数、期指OI、basis和ETF份额估算同向；市场已定价部分是11月11日相对领先1.64pp。分歧在于贴水改善和广度是否能延续；PnL来自5:8篮子相对表现。最强竞争解释是高beta单日反弹。下一项区分观测是09:30—10:00现金风格差、组合P和basis同步。
- **#2 SOXX/SMH**：新增事实是收盘比率+1.13%；市场已定价了CoreWeave利好与超跌修复。分歧不再包装成纯“现金流对Capex”，而是ETF权重相对价值。最强反证是CoreWeave约+24.7%说明Capex beta可以领涨；AMAT/CSCO指引将区分需求兑现与估值修复。
- **#3 M正套**：新增有效事实是fresh五所EOD与价差300/306；WASDE与近月紧张已明显定价。PnL来自近月相对远月继续扩张，反证是近月OI下降与追价。只接受回撤—收复。
- **#4 SC**：海外油价反弹与国内SC日盘疲弱并存；PnL来自事件溢价回补。库存增加、曲线收窄和EIA是最强竞争解释/反证。
- **#5 2s30s趋平**：热通胀和前端路径支持趋平，但30Y供给可能令长端独立上行。11月11日休市意味着没有新价格验证，故降分。

## 5. Top3详卡

### 卡1｜IM2612多 / IH2612空（5:8）

- **结构与中性**：多5手IM2612、空8手IH2612；按乘数200/300，11月11日收盘名义分别约CNY6.623m/CNY6.581m，净多CNY41,720、净/双边总名义0.316%，近似Dollar-neutral但绝非Beta-neutral。
- **确定性计算**：组合 (P=1000\times IM-2400\times IH)。按11月10日前结算到11月11日收盘，组合毛PnL约CNY119,360，占前日双边名义约0.908%；这只是历史同口径表现，不代表用户成交。
- **入场顺序**：09:30后P先回撤/处于20k—50k；09:45收>=30k；随后15分钟低点>=20k且10:00收>=40k；CSI1000-SSE50同期收益差>=+0.40pp；IM年化basis不比IH差超过0.25pp；深度正常。全部AND。50%在P=40k—50k，二次5分钟守50k再50%；P>80k无回踩不追。
- **止损/失效**：计划P=-60k；逻辑失效为现金风格差30分钟<-0.30pp或IM basis比IH更差>0.25pp。止损不保证成交。
- **目标/时间**：TP1 P=180k；TP2 P=320k；2026-11-25 14:55 BJT。
- **费用与情景**：CNY6,000/个5:8篮子往返情景假设，非实报。

| 允许入场P | 计划风险CNY | TP1净利/R | TP2净利/R |
|:---|:---|:---|:---|
| 30000 | 96000 | 144000 / 1.5 | 284000 / 2.96 |
| 40000 | 106000 | 134000 / 1.26 | 274000 / 2.58 |
| 50000 | 116000 | 124000 / 1.07 | 264000 / 2.28 |

- **最坏压力/放弃**：期指跳空、流动性消失、保证金上调和相关断裂都可能超出计划止损；开盘P>80k无回撤；深度异常；现金风格不确认；beta/保证金/费用无法核验。
- **替代表达**：不交易；或只用IM方向但风险更大且失去相对价值逻辑。MO不能无摩擦替代IM/IH篮子；IH↔HO、IF↔IO、IM↔MO，IC无默认同标的期权。

### 卡2｜SOXX多 / SMH空（33:10）

- **结构与中性**：多33股SOXX、空10股SMH；11月11日收盘净多约USD58.60、净/双边总名义约0.574%，近似Dollar-neutral，未核Beta-neutral。
- **确定性计算**：11月10日收盘SOXX/SMH为146.59/483.63，11月11日155.40/506.96；比率0.30310→0.30653（+1.131%），组合毛PnL USD57.43，约占前日双边名义0.594%。不混用单腿回报替代篮子PnL。
- **入场顺序**：美股开盘30—45分钟后，ratio回撤0.3045—0.3060且15分钟收>=0.3055；随后回踩守0.3045；Q回撤20—40美元；QQQ守首30分钟低点；borrow/fee/分红税与同步报价核验。全部AND。50/50；ratio>0.3080无回踩不追。
- **止损/失效**：Q=-20美元或日线ratio<0.3010；逻辑失效为NVDA相对SOXX反弹>6%且ratio<0.3020。
- **目标/时间**：Q=130美元 / ratio约0.311作代理；Q=220美元 / ratio约0.317作代理；20交易日。
- **费用与情景**：USD15/篮子往返情景假设；borrow/dividend/tax真实值未知。

| 允许入场Q | 计划风险USD | TP1净利/R | TP2净利/R |
|:---|:---|:---|:---|
| 20 | 55 | 95 / 1.73 | 185 / 3.36 |
| 30 | 65 | 85 / 1.31 | 175 / 2.69 |
| 40 | 75 | 75 / 1 | 165 / 2.2 |

- **最坏压力/放弃**：借券召回、分红、税费、ETF成分变化与盘后财报跳空；borrow不可得；ETF成分/公司行动异常；盘中ratio>0.308无回撤；AMAT/CSCO指引使SMH权重beta占优。
- **替代表达**：不交易；或用精确成分篮子做Beta-neutral，但本期未取得完整权重/borrow，故不得称已完成。

### 卡3｜M2701多 / M2705空（1:1）

- **结构**：DCE M2701/M2705各1手，吨数中性；价差定义为近月减远月。期货止损不是合同最大损失。
- **市场隐含/分歧**：close/settle价差300/306已计入大量近月紧张；分歧是回撤后300附近能否再次成为支撑，而非继续追扩张。
- **入场顺序**：09:00后先回落至296—300；首15分钟低点>=290且09:15收>=303；其后5分钟回踩300—303不破；CBOT soy重新核验>=1220；两腿深度正常。全部AND满足后50%在301—303，第二次守303再50%；>306不追。
- **止损/失效**：计划价差290；逻辑失效为CBOT soy<1220或价差15分钟收<296。
- **目标/时间**：TP1 340；TP2 370；2026-11-18 14:55 BJT。
- **费用与情景**：CNY80/组往返情景假设。

| 入场价差 | 计划风险CNY | TP1净利/R | TP2净利/R |
|:---|:---|:---|:---|
| 301 | 190 | 310 / 1.63 | 610 / 3.21 |
| 302 | 200 | 300 / 1.5 | 600 / 3 |
| 303 | 210 | 290 / 1.38 | 590 / 2.81 |

- **最坏压力/放弃**：两腿错配、涨跌停与流动性消失可使损失超过计划；开盘价差>310无回撤；首15分钟低点<290；09:15收<303；CBOT soy<1220；深度异常。
- **替代表达**：豆粕期权只有局部ATM样本、无bid/ask与执行就绪，故本期不构造“有限损”价差，更不能编净权利金。

## 6. 黄金专题

结论：**弱化但未失效；“政策信用期权”只是经济比喻，不是合同限损。**

- 支持：中长期政策信用与央行配置需求仍是结构性背景；地缘和财政供给仍可能提供凸性。
- 反证：前月黄金结算约3,992美元/盎司、-0.7%，GLD -1.14%，DXY +0.67%；10Y实际收益率last-good 2.78%。在现金债休市日，美元走强而黄金继续下跌更符合持有成本/流动性竞争解释。[黄金结算](https://www.marketwatch.com/livecoverage/stock-market-today-dow-s-p-500-nasdaq-nvidia-scandal-hotter-than-expected-cpi-coreweave/card/gold-settles-lower-again-reversing-early-gains-Z4WIH1KzdY1kRB7b1jDc)
- 缺证：同日黄金ETF申赎、最新央行月度购金、fresh CFTC、3—6个月可执行IV/skew/bid-ask均未取得；因此不做强因果归因。
- 工具比较：新报价后的3—6月Call Spread可控制合同最大净成本；MGC只适合在实际利率与美元共同反转后确认；“黄金多头+长债Put Spread”需两边同时报价；若已有仓位则减持/对冲必须条件化；当前最优替代是**不交易**。
- 原稳定idea `GOLD-POLICY-CREDIT-CONVEXITY-20261111` revision 3，评分68→65；不沿用旧strike，不把GLD跌幅当期权组合盈亏。

## 7. AI专题

- **龙头/芯片**：QQQ +2.28%，SOXX +6.02%，SMH +4.87%，NVDA +2.94%；半导体比率修复比大盘更快，但盘中高点回落，仍未证明新趋势。
- **云与Capex beta**：CoreWeave约+24.7%直接反驳“高Capex beta必然继续下跌”。因此多SOXX/空SMH的解释从“多现金流空Capex”修订为更朴素的ETF权重/广度相对价值。
- **设备/网络**：Applied Materials与Cisco于11月12日美股收盘后公布/召开电话会，分别检验晶圆厂设备支出与网络AI订单/毛利。[AMAT通知](https://ir.appliedmaterials.com/node/29796/pdf)；[Cisco通知](https://investor.cisco.com/news/news-details/2026/Cisco-Schedules-Conference-Call-for-Q1-Fiscal-Year-2027-Financial-Results/default.aspx)
- **软件/电力**：本期没有取得足够新的公司级FCF、Capex、估值与订单原件来形成精确篮子；只保留为覆盖结论，不假设成员权重。
- **估值/基本面区分**：11月11日更像去杠杆后的盈利/需求修复，而非已经证明高实际利率不影响估值。下一项区分观测是AMAT/CSCO指引与SOXX/SMH能否在高DXY、现金债重开后继续走强。
- **期权**：未取得可执行财报后IV曲面，不能因VIX下降就称Call Spread便宜；Vega计划为零，直到实际报价。

## 8. 中国50/300/500/1000及公司专题

### 8.1 股指、期货、期权

| 现货/主力 | 现货1D | 期货close/settle | Volume/OI/ΔOI | basis/年化 | 期权截面 |
|:---|:---|:---|:---|:---|:---|
| SSE50 / IH2612 | -0.27% | 2742.2 / 2746.0 | 25,950 / 63,192 / +1,720 | -23.34；-8.33% | HO2612 ATM14.65%；RR25 -0.982pp；BF25 0.224pp；PCR OI0.617 |
| CSI300 / IF2612 | +0.41% | 4043.4 / 4048.6 | 56,405 / 173,783 / +163 | -32.31；-7.82% | IO2612 ATM17.79%；RR25 -1.276pp；BF25 0.303pp；PCR OI0.643 |
| CSI500 / IC2612 | +1.01% | 6664.0 / 6671.8 | 102,586 / 173,915 / +4,705 | -49.18；-7.23% | 无默认同标的CFFEX期权；MO/IO/ETF代理有指数、Beta、basis残差 |
| CSI1000 / IM2612 | +1.37% | 6623.0 / 6628.4 | 196,766 / 290,211 / +9,945 | -46.55；-6.89% | MO2612 ATM27.95%；RR25 -2.356pp；BF25 0.181pp；PCR OI0.650 |

- 同口径历史：引擎history为空，期权与指数的3/5/20日比较不可得；只报告1D，不把Stock Engine的全市场中位数替代指数历史。
- ATM变化：HO/IO/MO分别-0.255/-0.315/-1.561vol点；MO绝对IV和put skew仍高，但不能只凭IV高就卖波动。
- Gamma：引擎可给绝对Gamma节点，但dealer净方向未知，故不写“dealer long/short gamma”。价格/OI象限也不推新多新空。
- 线性优先：IM/IH能用组合P明确计算；MO不能无摩擦替代IM，IC没有上述同标的期权。Long Gamma、Calendar、Butterfly或有限风险Short Gamma均因当前盘口/历史不足只作研究。
- 开盘验证：09:30—10:00是未来计划，不称已经发生。

### 8.2 A股公司研究与主动发现

Stock Engine 11月11日覆盖5,580只、实际成交5,574只；价量历史与复权能力恢复，但行业覆盖0、正式指数成份缺、预期修订0、EOD可交易性未知，完整最小财务包仅2家公司。全市场3538涨/1828跌、等权+1.14%、中位数1/3/5/20日为+0.59%/+2.03%/+2.47%/-4.29%，说明短线修复尚未扭转20日中位回撤。

限定公开检索范围为巨潮/交易所11月11—12日新增经营、订单、资本配置与负面风险：

- 洛阳钼业披露金融机构股票回购专项贷款承诺函；这是资本配置融资支持，不是铜/钴售价、销量或成本的新经营事实。[公告页](https://www.cninfo.com.cn/new/disclosure/stock?orgId=gshk0003993&stockCode=603993)
- 申科股份完成285.2万股、占总股本1.9013%、约3,993.82万元回购并提前届满；回购用于员工持股/股权激励，既不等同注销，也不证明经营改善。[原公告PDF](https://static.cninfo.com.cn/finalpage/2026-11-12/1225667775.PDF)

CMOC若映射铜价，利润桥仍须分别验证售价/销量、矿山成本、库存、套保、汇率、Capex与少数股东；当前缺少新的同口径经营输入，不能由CU价差扩张直接推导公司盈利。申科的回购已完成，边际买盘可能结束是最强竞争解释。两者均为“研究候选/证据不足/执行未就绪”，A股Top5为0，不代表未扫描全市场。

## 9. 未来24小时/7天、覆盖与发布闸门

### 9.1 事件日历（北京时间）

| 时间 | 事件 | 计划 |
|:---|:---|:---|
| 2026-11-12 09:00 | China commodity day session / SC2612 option last trading day | M and SC only after ordered reclaim/retest; no unquoted option execution |
| 2026-11-12 09:30-10:00 | China stock/index open validation | IM/IH require combo P, cash style spread, basis and depth all confirm |
| 2026-11-12 23:00 | Fed Governor Barr speech (10:00 ET) | AI/FX/rates only react after actual statement; no pre-attribution |
| 2026-11-13 01:00 | EIA WPSR (12:00 ET holiday schedule) | before release keep SC linear delta small; after release separate crude stocks, products, refinery and exports |
| 2026-11-13 02:00 around | US 30Y auction / cash-bond supply test | rates candidate needs actual auction and 2s30s reaction; exact award time/size reverify |
| 2026-11-13 05:30 | Cisco and Applied Materials calls after US close | do not add AI Vega before quotes; update networking/equipment guidance and Capex beta thesis |
| 2026-11-13 21:30 | US October PPI | hot surprise: reduce unprotected duration/gold delta; softer: retain convexity only if dollar/real yield confirm |
| next 7 days | China activity/credit/PBOC and A/H disclosures | CPI/PPI already released Nov9; use only actual publication/known_at; no guessed policy timing |
| 2026-11-13 17:00 (auxiliary calendar, reverify) | IEA November OMR | reassess oil balance and event premium |
| ongoing | Hormuz/Iran and Russia-Ukraine shipping/refinery risks | gap, limit and correlation-break stress; avoid naked event risk without budget |

美国初请失业金通常于周四08:30 ET发布，但本期未取得11月12日当周官方具体发布页，故只列为“可能的21:30 BJT风险窗口”，不写成已确认事件。中国10月CPI/PPI已于11月9日发布，未来7天若出现社融/信贷、PBOC或政策披露，只在实际发布known_at后使用；不预判“国家队”或机构净买卖。[国家统计局日程](https://www.stats.gov.cn/sj/fbrc/)

### 9.2 覆盖核对

| 模块 | 应覆盖 | 实际取得并分析 | 缺失/受限 | 对结论影响 |
|:---|:---|:---|:---|:---|
| 美国利率 | 2/5/10/30、曲线、实际、BEI、Fed、供给 | 11/10 last-good及11/12 Fed/30Y事件 | 11/11休市、期限溢价精确值、DV01/roll | 仅限制利率执行；不影响AI/中国EOD事实 |
| FX | DXY、EURUSD、USDJPY、USDCNH、carry/skew | 现货/参考fixing与跨资产传导 | FX期权skew/carry拥挤不足 | 方向研究可用，期权表达不可用 |
| AI | QQQ、芯片、设备、网络、云、软件、电力 | ETF、NVDA、CoreWeave及AMAT/CSCO事件 | 完整估值、成员权重、post-earnings IV | 相对价差可研究，纯因子与期权不可执行 |
| 原油 | WTI/Brent、曲线、库存、裂解、OPEC、OVX/skew | 结算、地缘、EIA日程 | 完整曲线/裂解/OVX/skew | SC保持事件条件，不升为立即交易 |
| 黄金 | 现货/COMEX、实际利率、美元、ETF/CFTC/IV | 期货/GLD、美元、real-yield last-good | ETF flow、央行月度、CFTC、IV | 结论弱化，执行为0 |
| 风险 | VIX、MOVE、HY OAS、广度、拥挤、流动性 | VIX、延迟MOVE/HY、A股广度 | CTA/gamma拥挤精确值 | 不推单因子确定结论 |
| 中国股指/期权 | 50/300/500/1000及HO/IO/MO | 11/11官方EOD、basis、ATM/RR/BF/PCR | 历史为空、dealer方向/盘中路径缺 | IM/IH仅等开盘确认 |
| 中国商品 | 63代码+动态、五层证据 | 77品种/806合约、market/physical/external/options | Night空、crosscheck/warehouse/member缺 | 全范围研究完成；执行限于依赖项 |
| A股公司 | 价量全扫+公司事实发现 | 5580价量与有限公告检索 | industry/index/tradability/forecasts | 无A股Top5，但不停止研究 |

### 9.3 风险预算与压力

- 试仓计划NAV 0.25%—0.75%，确认0.75%—1.50%，同一高确信主题总预算不超过NAV 2.5%—3.0%。
- 专属上限更紧：IM/IH压力预算≤0.50%；AI在borrow/beta/费用未核前为0，核验后≤0.25%；M≤0.25%；SC在EIA前≤0.25%；UST在DV01/roll未核前为0；黄金无报价为0。
- 未取得账户持仓，不编净敞口。AI/中国小盘共享增长beta与流动性；黄金/国债/美元共享实际利率；SC/CU/M共享美元、中国需求与保证金，不能视作天然分散。
- 压力测试：跳空、连续涨跌停、保证金上调、隐波重定价、流动性消失、相关性断裂与假期跨市场冲击。保证金不是风险预算，止损不保证成交或封顶。

### 9.4 状态修订与实际校验

| idea_id | 前序→本期 | 原因 | 参数/状态处理 |
|:---|:---|:---|:---|
| CN-IM-IH-SMALLCAP-BREADTH-RV-20261111 | 69→73；rev2→3 | new evidence and price confirmation | new combo-P entry/stop/targets added for new candidate only; no assumed old fill |
| AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106 | 72→72；rev5→6 | price validation plus thesis revision | entry updated to pullback after 11/11 close; old stop not moved for any hypothetical position |
| COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111 | 73→71；rev3→3 | execution window passed / price change | uses commodity morning day plan; old night plan not backfilled |
| COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111 | 68→68；rev2→2 | oil rebound and inventory counterevidence | unchanged conditional day plan |
| UST-2S30S-HOT-CPI-FLATTENER-20261111 | 68→67；rev3→4 | holiday/no new price discovery | no DV01 or trigger fabrication |
| GOLD-POLICY-CREDIT-CONVEXITY-20261111 | 68→65；rev2→3 | price and dollar evidence weakened | watchlist; no old strike reused |

校验结果：

- 五个Top分项均与总分一致；AI 33/10与IM/IH 5/8组合PnL、净名义、情景R均已重算。
- 交易卡保留AND与先后顺序、确认时长、不追价、独立止损/逻辑失效、TP与时间退出；未取得的费用明确是情景假设。
- 合约、乘数、close/settlement、basis和期限已区分；IC代理残差、Night空文件与商品官方crosscheck缺口已隔离。
- 未做且不声称通过：实时盘口、成交回报、账户权限、保证金、borrow、Beta、DV01/roll、完整油金期权链、A股可交易性。
- CI为 `pending_or_unverified`；GitHub回读成功与否只决定archive_status，不代表行情或成交全面认证。

### 9.5 主要来源

- [Global Cross-Asset Radar prior evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/464576ecdb9d9277a75489f7bc3b04f752a15f22/reports/2026/11/2026-11-11_evening.json)（GitHub/farfromexact；源日 2026-11-11；支持：stable idea_ids, prior scores, prior triggers and revision state）
- [2026-11-12 China commodities morning auxiliary report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/464576ecdb9d9277a75489f7bc3b04f752a15f22/reports/2026/11/2026-11-12_commodities_morning.json)（GitHub/farfromexact；源日 2026-11-12；支持：commodity candidate calculations and day-session conditions; market facts cross-checked to engine/primary sources）
- [China-Options Engine radar_latest](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：IH/IF/IC/IM closes, OI, basis, cash indices and HO/IO/MO metrics）
- [China-Options Engine radar_history](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json)（GitHub/farfromexact；源日 2026-11-11；支持：history empty; no 3/5/20 option comparison）
- [China-Commodities Engine last_run_status](https://github.com/farfromexact/China-Commodities-Engine/blob/7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a/data/last_run_status.json)（GitHub/farfromexact；源日 2026-11-11；支持：five-exchange 806-contract Wind EOD coverage and module states）
- [China-Commodities options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a/data/options/quality_latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：64/64 product sampling, 60 core ATM series, 3 skew-ready series, no bid/ask or execution readiness）
- [China-Commodities market state](https://github.com/farfromexact/China-Commodities-Engine/blob/7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a/data/market_state_latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：77 products and exact-contract historical features with 18 of 20 sessions observed）
- [China-Commodities physical and external modules](https://github.com/farfromexact/China-Commodities-Engine/blob/7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a/data/physical/latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：physical 18/20 fresh targets; SC/LU unavailable）
- [China-Commodities official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/7f596faeaeaba5ae2da6b76e6d5540f1e5a6476a/data/crosschecks/futures_latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：independent official EOD comparison unavailable; no proven price conflict）
- [China-Stock Engine status and research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/8b496efb1a7ac54b901c223cb4a23e843ad37a65/data/latest/research_inputs_latest.json)（GitHub/farfromexact；源日 2026-11-11；支持：5580-stock scan capability, partial company events/financials, no forecasts/industry/index/tradability readiness）
- [US fixed-income Veterans Day full close recommendation](https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026)（SIFMA；源日 2026-10-28；支持：US fixed-income market closed 2026-11-11）
- [Dollar climbs as traders raise December Fed hike bets](https://www.reuters.com/world/asia-pacific/dollar-gains-traction-fed-speakers-warn-risks-inflation-2026-11-11/)（Reuters；源日 2026-11-11；支持：DXY 102.90 area, December 25bp hike odds 87%, EUR and JPY weakness）
- [Oil up 1% as Iran official says country will keep enriched nuclear material](https://www.reuters.com/business/energy/oil-rises-two-month-low-hormuz-shipping-attacks-offset-iran-truce-hopes-2026-11-11/)（Reuters；源日 2026-11-11；支持：Brent 92.76, WTI 86.53 and persistent shipping disruption）
- [EIA Weekly Petroleum Status Report schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（EIA；源日 2026-11-12；支持：holiday-delayed WPSR at 12:00 ET on Nov12）
- [BLS November 2026 release schedule](https://www.bls.gov/schedule/2026/11_sched_list.htm)（BLS；源日 2026-11-03；支持：October PPI release Nov13 08:30 ET）
- [Federal Reserve calendar](https://www.federalreserve.gov/newsevents/calendar.htm)（Federal Reserve Board；源日 2026-11-10；支持：Barr speech and delayed H.15/H.4.1 releases on Nov12）
- [ECB reference exchange rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)（ECB；源日 2026-11-11；支持：EUR/USD 1.1127 and EUR/JPY 177.18 reference fixings）
- [BLS/NBS release calendar](https://www.stats.gov.cn/sj/fbrc/)（National Bureau of Statistics of China；源日 2026；支持：China CPI/PPI already released Nov9; next major release schedule reviewed）
- [申科股份回购提前届满公告](https://static.cninfo.com.cn/finalpage/2026-11-12/1225667775.PDF)（巨潮资讯；源日 2026-11-12；支持：1.9013% repurchase completed; not a new operating catalyst）
- [洛阳钼业公告页](https://www.cninfo.com.cn/new/disclosure/stock?orgId=gshk0003993&stockCode=603993)（巨潮资讯；源日 2026-11-11；支持：buyback special-loan commitment disclosure found in bounded search）
- [Cisco Q1 FY2027 earnings call notice](https://investor.cisco.com/news/news-details/2026/Cisco-Schedules-Conference-Call-for-Q1-Fiscal-Year-2027-Financial-Results/default.aspx)（Cisco Investor Relations；源日 2026-11-03；支持：Cisco reports after Nov12 US close; call 16:30 ET）
- [Applied Materials FY2026 results notice](https://ir.appliedmaterials.com/node/29796/pdf)（Applied Materials Investor Relations；源日 2026-10-22；支持：AMAT call Nov12 16:30 ET）
- [Market closes and ETF quotes](https://finance.yahoo.com/markets/)（Yahoo Finance structured market data；源日 2026-11-11；支持：QQQ, SOXX, SMH, GLD, HYG, IWM and NVDA closes）
- [Gold settles lower again](https://www.marketwatch.com/livecoverage/stock-market-today-dow-s-p-500-nasdaq-nvidia-scandal-hotter-than-expected-cpi-coreweave/card/gold-settles-lower-again-reversing-early-gains-Z4WIH1KzdY1kRB7b1jDc)（MarketWatch/Dow Jones Market Data；源日 2026-11-11；支持：front-month gold settlement near 3992, down 0.7%）

## 10. 今日行动清单

A. 没有；中国开盘前缺实时顺序与深度，美股/美债下一窗口尚未开启。
B. IM2612/IH2612 5:8篮子、M2701/M2705正套、SOXX/SMH 33:10篮子、SC2612收复多、美国2s30s趋平；均按各卡全部AND，未满足即不交易。
C. CU2612/CU2701价差回落、AP701局部长波动、黄金政策信用凸性、AI设备/网络财报、CMOC资本配置但无经营新事实。
D. 追IM/IH组合P>80k、追M价差>306、追SC>614、追CU价差>1250、任何无bid/ask期权、把空Night文件当官方夜盘收盘、未经beta/借券/账户核验的相对价值；不假设用户持仓。