# 商品期货期权晨间雷达｜2026-11-12

> 生成：2026-11-12T07:07:30+08:00｜信息截点：2026-11-12T07:07:00+08:00｜下一中国窗口：2026-11-12 09:00 BJT  
> 仅研究与决策支持，不下单，不假定持仓或成交。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；豆粕价差、SC收复与苹果长波动值得等09:00条件或报价。**

- 已研究但优势不足：CU近月升水已扩至约1260，EC反弹缺实体确认，AG内外价格锚分裂。
- 研究机会存在但等待条件/报价：M2701/M2705回撤—收复、SC2612收复610、AP701精确期权询价。
- 数据不足不能判断：当前Night仓库会话缺失；期权无bid/ask；全部Physical基差仅C级。
- 最有价值的下一观察：09:15的M价差收复、SC近月曲线是否守10、AP701可成交跨式/宽跨净支出。

## 2. 数据质量与覆盖

| 模块 | 实际取得 | 可分析/可执行 | 关键局限 |
|---|---|---|---|
| Futures | 11/11五所806合约、77品种；SHFE238/INE63/DCE214/CZCE243/GFEX48；source-date100%，critical0，full_market_ready=true | 全市场初筛可用 / 执行仍需实时盘口 | official_complete=false |
| Market State | 77品种，20个同合约观测 | 1D/3D/20D、RV/OI/曲线可用 | 11/4端点缺失，5D统一不可得 |
| Physical | 20目标、18取得、2不可得；A/B基差0、C级18 | context-only / 否 | SC/LU不可得；无方向得分 |
| External | 22目标、17取得、5不可得，另核07:00海外 | 背景+最新海外 / 否 | repo生成19:12，非07:00 |
| Night | 仓库旧标签11/11、start11/10；514/806、63.77%，错误0；detail空 | 旧会话闭环 / 当前会话不可直接消费 | 预期11/12、start11/11未发布；focus用公开fallback；official close=false |
| Options | 64/64、466条、64系列；coreATM60、skew3 | 局部IV可研究 / execution0 | full-chain/surface/positioning均0；bid/ask0 |
| Metadata | 11/9 last-good | SC交割日局部可用 | DCE M仅observed-contract-only |
| Crosscheck | 11/11 state=unavailable | 不阻断vendor数据 | SHFE/INE/CZCE/GFEX baseline unavailable；DCE HTTP412 |
| Stock | 11/11，5580股；events20；完整最小财务包2 | 利润桥局部可用 / execution unknown | forecast0、复权/实时交易能力未就绪 |

Night日期闸门：旧会话自身标签不构成calendar_mismatch，但**当前应得会话缺失**，不得用于正式11/12 Night→Day收益。公开fallback均注明时点与非官方终盘口径。

覆盖：63个指定代码及动态PD/PT全部纳入77品种初筛。黑色最显著SA活跃但证据薄；有色聚焦CU/AG/AL；能化聚焦SC/RU/PP/EG；新能源LC活跃但实体不足；农产品M最强、P/C/AP有分歧；EC反弹伴减仓但无实体确认。

## 3. 仪表盘

| 品种/合约 | EOD close/settle | 1D / 5D | RV20 / OI变化 | 曲线与实体 | 当前Night/海外/期权 | 信号 |
|---|---:|---|---|---|---|---|
| M M2701 | 3139/3137 | settle +2.08% / N/A | 12.62; 1,862,901; Δ-25,247 | M2701-M2705 close300/settle306; basis C/context | 3149; +0.32% vs close/+0.38% vs settle; spread307 (fallback); M2701 ATM3150 IV13.55; coreATM yes, skew/execution no | 价差强但>304不追 |
| SC SC2612 | 604.0/598.1 | settle -1.81% / N/A | 40.18; 15,004; Δ-1,577 | SC2612-SC2701 close12.1/settle14.0; unavailable | 607.3; +0.55%/+1.54%; curve10.0 (fallback); SC2701 ATM580 IV53.045; execution no | 外盘支持、曲线收窄 |
| CU CU2612 | 105820/105230 | settle -0.61% / N/A | 9.85; 191,115; Δ-960 | CU2612-CU2701 close1220/settle1230; basis C/context | 105430/104170同刻，价差1260 (fallback); ATM106000 IV14.325; skew/execution no | 升水极端，等回落 |
| AG AG2702 | 12748/12487 | settle -1.98% / N/A | 38.93; 264,224; Δ+8,951 | curve z +1.68; context | 12520 at02:11; -1.79% vs close/+0.26% vs settle; ATM12500 IV41.86 | close锚偏弱、settle锚不弱 |
| RU RU2701 | 19475/19195 | settle +2.13% / N/A | 16.85; 133,145; Δ+8,811 | contango -620; basis C/context | current exact fallback未核; ATM19250 IV22.555 | 动量强但曲线反证 |
| EC EC2612 | 2485.5/2469 | settle +3.48% / N/A | 47.98; 15,564; Δ-1,239 | contango约12.23%; 运价实体缺 | 无夜盘; N/A | 反弹伴减仓，观察 |
| AP AP701 | 5981/5939 | settle +0.29% / N/A | 37.26; 145,921; Δ-3,735 | backwardation约9.73%; basis C/context | current exact fallback未核; ATM5900 IV30.725; coreATM yes | 长vol待询价 |
| PP PP2701 | 9220/9077 | settle -0.12% / N/A | 31.16; 564,003; Δ+4,411 | backwardation; basis C/context | 板块公开夜盘偏强但exact未核; ATM9100 IV30.08 | close-settle分歧大 |
| EG EG2701 | 4964/4879 | settle +0.87% / N/A | 29.44; 321,045; Δ+22,494 | backwardation +120; basis C/context | exact未核; core ATM可读 | 价仓同升、只作观察 |
| AL AL2701 | 22105/21940 | settle -2.34% / N/A | 16.16; 247,720; Δ+17,685 | backwardation; roll warning; basis C/context | exact未核; core ATM可读 | 价跌仓增，反向压力 |
| C C2701 | 2192/2192 | -0.95% / N/A | 8.05; 1,247,172; Δ+28,247 | curve z +2.22; basis C/context | exact未核; core ATM可读 | 价格与曲线冲突 |
| P P2701 | 8854/8773 | settle +1.63% / N/A | 17.78; 517,194; Δ+4,403 | contango -64; basis C/context | exact未核; ATM8800 IV17.745 | 价格强、曲线反证 |

## 4. 相比前序的真变化

1. 核心期货从11月11日晚报的0记录失败批次恢复为11月11日五所806合约/77品种、source_date_match100%；这是数据恢复，不是市场催化。
2. M2701/M2705由EOD close300/settle306至公开夜盘307；旧计划>304不追价，因此旧夜盘条件未执行，日盘另立回撤—收复序列。
3. SC2612公开夜盘607.3相对close+0.55%、相对settle+1.54%，但SC2612/2701曲线由close12.1收窄至约10；海外Brent92.76支持与曲线反证并存。
4. CU2612/2701同刻公开价差1260，高于EOD close1220与旧价值区950—1050；继续研究但不追。
5. Options由前日晚报45/64且ATM0恢复至64/64、coreATM60；仍无bid/ask、surface/positioning/execution均0，故只提升研究能力，不提升可执行性。
6. Stock更新至11月11日5580股，但仅2家公司具完整最小财务包；紫金盈利桥维持CU公司映射，未产生新的公司催化。

## 5. 产业链与传播路径

- **大豆—豆粕—饲料**：CBOT soy约1225观察值 → M2701强于M2705 → 饲料成本。最强：M2701/M2705价差307；最弱/反证：C2701结算-0.95%。实体：basis C；实体主要沿用USDA；期权：M2701 ATM IV13.55 vs RV12.62，略贵非方向支持；置信度medium。最大缺口：当前Night仓库缺失、现货A/B基差缺失。
- **原油—燃料—化工**：Brent92.76/WTI86.53 → SC2612 607.3 fallback → FU/PP/EG。最强：SC/FU夜盘弹性；最弱/反证：SC近月曲线由12.1收窄至10。实体：SC/LU实体不可得；期权：SC2701 ATM IV53.05 vs RV40.18，事件溢价明显；无执行报价；置信度medium-low。最大缺口：EIA未发、当前Night官方收盘缺失。
- **铜矿—精炼铜—矿企**：海外铜价偏强 → CU2612/2701升水1260 → 紫金矿产铜售价/销量/套保。最强：CU近月升水；最弱/反证：CU日盘价格与OI均降。实体：basis C，仓单/加工费缺失；期权：CU ATM IV14.33 > RV9.85；置信度medium-low。公司桥：紫金H1营收1941.8亿元、归母391.7亿元、OCF554.7亿元；利润桥受产量、成本、套保和卡莫阿约束，股票不如直接曲线纯粹。最大缺口：无新增独立实体证据。
- **贵金属—宏观**：热CPI/美元强 → gold弱，silver相对强 → AG2702相对close回落。最强：AG night12520 vs close -1.79%；最弱/反证：vs settle仍+0.26%，海外银价上行。实体：缺失；期权：AG ATM IV41.86略高于RV38.93；置信度low。最大缺口：内外盘窗口不完全可比。
- **苹果—波动率**：AP701 RV37.26 → ATM IV30.73 → 询价决定是否长Gamma/Vega。最强：IV-RV -6.53vol；最弱/反证：无事件概率、skew/term/bidask。实体：basis C；期权：coreATM yes; execution no；置信度low。最大缺口：精确腿与净成本。

Stock利润校验：紫金矿业2026H1合并口径营收1,941.8亿元、归母净利391.7亿元、经营现金流554.7亿元；矿产铜利润桥为实现售价×销量，扣除成本、库存损益、套保、汇率与Capex，并受卡莫阿减产/检修约束。11/11股价27.86元、1D -1.14%、5D -4.75%，但证券实时可交易状态未核。结论：CU曲线是更纯表达；紫金只作利润通道验证，不增第六证据层，也不改变排名。[公司证据](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_9_002.json)｜[2026H1原件](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)

## 6. 统一机会榜

| 排名 | idea_id | 方向/工具 | 分项（逻辑/赔率/催化/价曲波/拥挤） | 总分 | 有效层 | 研究/证据/执行 |
|---:|---|---|---|---:|---|---|
| 1 | COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111 r3 | long near/short deferred; M2701+M2705 | 21/17/17/9/7 | 71 | 支持1,2,3,4；缺5 | priority/4层但实体/海外含沿用与公开快照/not_ready; 09:00顺序、深度、回踩未发生 |
| 2 | COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106 r12 | long near/short deferred after pullback; CU2612+CU2701 | 20/15/11/12/10 | 68 | 支持1,2,4；缺3,5 | watch/3层、但实体缺失/not_ready; current exact final/depth not verified |
| 3 | COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111 r2 | long conditional; SC2612 | 20/15/17/9/7 | 68 | 支持2,4；缺3,5 | focus/2层支持、价格层混合，按规则≤69/not_ready; day reclaim/retest not occurred |
| 4 | COM-V-AP701-LONGVOL-20261112 r1 | long volatility research; AP701 options | 18/15/10/7/11 | 61 | 支持1,5；缺2,3,4 | watch/2层、IV-RV不独立证明便宜/not_ready; exact quote and max debit required |
| 5 | COM-M-AG2702-MACRO-REPRICING-WATCH-20261112 r1 | two-way watch; bearish below 12480 only; AG2702 | 18/13/10/10/8 | 59 | 支持1；缺2,3,4,5 | early/仅价格层，按规则≤59/not_ready; 12480确认未发生 |

分数仅为研究优先级，不是胜率或仓位。M虽有4层，当前报价已越过旧不追价区；SC仅2层有效支持，按规则封顶69；AG仅1层，封顶59。

## 7. 研究/交易卡

### 卡1｜M2701/M2705 1:1价差｜COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111 r3

- 事实：EOD close价差300、settle价差306；23:04:58公开快照307。旧r2“>304不追”生效，未假定触发或成交。
- 定价/分歧：WASDE与近月强势已显著定价；只有回撤后重新站稳303、CBOT soy仍≥1220，才说明近月供需节奏未完全释放。
- 入场：09:00后先回落至296—300；首15分钟低点>=290且09:15收盘>=303；其后5分钟回踩300—303不破；CBOT soy重新核验>=1220；两腿深度正常。全部AND满足后50%在301—303，第二次守住303再50%；>306不追。
- 失效/退出：新日盘候选计划止损290；逻辑失效为CBOT soy<1220或M2701/M2705价差15分钟收<296。止损不保证成交。 TP1=340，TP2=370，时间退出2026-11-18 14:55 BJT。
- 参数：公开合约文本10吨/手、1元tick=10元/腿；当前保证金、涨跌停、最后交易日未核，**不把未知写成0**。
- 成本情景：80元/组假设；301/302/303入场的净风险190/200/210元，TP1净R 1.63/1.50/1.38，TP2净R 3.21/3.00/2.81。
- 压力：双腿相关断裂、单腿限板/流动性消失可使损失超过计划止损；1/2限幅仅做压力，不承诺封顶。

### 卡2｜SC2612条件多｜COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111 r2

- 事实：Brent结算92.76；SC2612公开夜盘607.3，较EOD close +0.55%、较settle +1.54%；SC2612-SC2701约10，较EOD close12.1收窄。
- 定价/分歧：霍尔木兹风险有支撑，但API库存大增、EIA待发；607.3未满足610确认线。
- 入场：09:00后首15分钟维持603—607上方；09:15收盘>=610；随后5分钟回踩608—611不破；Brent可验证价格>=92.5；SC2612-SC2701>=10。全部AND满足后50%在610—611，第二次守611后50%且最高612；>614不追。
- 失效/退出：计划止损599；逻辑失效：15分钟收<603 OR Brent<91.5 OR curve<7。止损不保证成交。 TP1=630，TP2=648，时间退出2026-11-17 14:55 BJT; SC2612 last trading day 2026-11-30。
- 参数：1000桶/手、0.1元tick=100元；一般保证金20%、涨跌停18%；日内开仓500手上限；夜盘21:00—02:30；SC2612最后交易日11/30。SC2612期权今日到期，不以旧IV代替实时权利金。
- 成本情景：800元/手假设；610/611/612入场的净风险11,800/12,800/13,800元，TP1净R 1.63/1.42/1.25，TP2净R 3.15/2.83/2.55。
- 压力：EIA跳空、18%限板、保证金上调、交割挤压；期权只有在精确腿与净支出核实时才是结构限损。[交易限额](https://www.shfe.com.cn/publicnotice/notice/202611/t20261109_834009.html)

## 8. 商品期权专项

- 样本：11/11 core_v1/sampled_strikes，64/64产品、466条、64系列；IV覆盖91.63%，bid/ask 0%。
- 局部就绪：coreATM 60；skew 3；surface/positioning/execution均0；full_chain_verified=false，dealer gamma方向未知。
- IV—RV：M 13.55 vs12.62；SC 53.05 vs40.18；CU 14.33 vs9.85；AG 41.86 vs38.93；AP 30.73 vs37.26；RU 22.56 vs16.85。
- AP是唯一显著负差（约-6.53vol），但没有bid/ask、事件概率、标准25Δ偏度或期限结构。只允许“询价—检查理论边界—限定最大净支出”的研究流程，不称便宜、不编Greeks或权利金。
- 回避：SC2612到期期权、任何用采样OI推全链PCR/拥挤度、任何未取得净成本却称有限损的结构。

## 9. 09:00开盘风险地图

| 主题 | Previous China EOD | Current T Night（fallback） | 07:00海外 | 09:00行动 |
|---|---|---|---|---|
| M价差 | close300/settle306 | 307，仓库当前Night缺失 | CBOT soy约1225观察值，非官方settle | >310不追；300—308等回撤；<296放弃；09:15/30/45核顺序与深度 |
| SC | 604/598.1；曲线12.1/14 | 607.3；曲线约10 | Brent92.76、WTI86.53 | >614不追；603—610等收复；<599失效；EIA前不扩大 |
| CU价差 | 1220/1230 | 同刻1260 | 海外铜偏强 | >1250不追；只等显著回落；核同刻双腿 |
| AG | 12748/12487 | 12520 | gold弱、silver强 | 12500—12820不做；15m<12480才是早期确认 |

当前Night公开fallback与EOD/海外时点不完全相同，只作headline elasticity和追价风险，不冒充官方终盘。

## 10. 未来24小时/7日事件

- 11/12中国日盘：SC2612期权最后交易日；Gamma、流动性、行权/交割风险上升。[合约表](https://www.shfe.com.cn/products/option/energyandchemical/sc_o/)
- 11/13 01:00/03:00 BJT：EIA因Veterans Day延后发布；SC/Brent Delta与Vega跳变，报告前不扩大线性风险。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/)
- 11/13 17:00 BJT：IEA 11月OMR；重估供应、需求、库存与炼厂假设。[IEA日程](https://www.iea.org/events/oil-market-report-november-2026)
- 11/13 21:30 BJT：USDA Weekly Export Sales；验证M/CBOT soy需求。[USDA日程](https://fas.usda.gov/report-release-announcement/weekly-export-sales-300)
- 11/17 04:30 BJT（暂定）：Veterans Day延后的CFTC COT；只作拥挤背景，不推dealer gamma。
- 持续：霍尔木兹、伊朗、俄乌港口/炼厂事件；对SC/EC/燃料采用gap、相关断裂、流动性消失压力，不以计划止损代替最大亏损。

发布校验：评分分项均和为总分；MD/JSON同源；当前会话、价格锚、单位、Night fallback、Options readiness、Stock时点与旧idea修订已复核。未解关键缺口为当前Night仓库会话、官方期货交叉核对、A/B基差、期权bid/ask及M当前合约参数。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：M2701/M2705回撤—收复；SC2612守603后收复610并回踩；均须全部AND条件与实时报价。  
C. 今天继续观察：CU2612/2701价差、AP701询价、AG2702的12480/12820、EC2612实体确认。  
D. 今天必须回避或有条件退出：追M>306、追SC>614、追CU价差>1250、无bid/ask期权；假设旧仓按原失效条件处理。
