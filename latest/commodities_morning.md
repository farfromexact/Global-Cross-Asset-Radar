# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-25

> 数据截点：北京时间 2026-08-25 07:13 左右。仅用于研究和交易决策支持，不自动下单。中国国内基线为最近完整交易日 2026-08-24 EOD；China-Commodities-Engine 不生产中国分钟、逐笔、夜盘/session 产品，因此本报告不从仓库推断 8 月 24 日中国夜盘。仓库 `report_input_latest.json` 已于 2026-08-25 06:28 BJT 重建，但其 External 子模块仍停在 2026-08-24 06:24 BJT，本期海外层用 8 月 24 日欧美收盘和 8 月 25 日早间公开实时/延时网页补充，严格与中国 EOD 分开。

## 一、今日一句话结论

**今天有值得冒险的机会，但没有开盘前应立即建立的新仓：EG2610 的库存挤压/主次月 Backwardation 是第一优先级；FG701 只做反弹失败空；昨日 FU/AG 多头明显降级。**

## 二、数据质量与覆盖

第一读取层已从 `farfromexact/China-Commodities-Engine` main 读取 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需进一步读取 `data/latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/contract_meta.json`。协议版本 `china_commodities_v2`。

统一输入 `requested_date=2026-08-24`，`generated_at=2026-08-25T06:28:45.894489+08:00`。Futures 为 8/24 完整 EOD：SHFE/INE/DCE/CZCE/GFEX 五所齐全，`full_market_ready=true`，`source_date_match_pct=100%`，803 个合约，critical errors=0，unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、核心 carried-forward=0；placeholder=4，排除异常排名。

Market State 有 20 个有效交易日，可使用同合约 1D/3D/5D/20D、RV20、成交/OI z-score、ΔOI 以及期限结构。Physical 为 4/20 映射、4 fresh-by-native-frequency、0 stale、0 carried-forward：I 港口库存最新周度 8/19，JM NBS 主焦煤现货最新旬度 8/20，FG 企业库存最新周度 8/21，TA 加工费最新周度 8/21。JM basis 为 C 级，不能计分或称套利。

External 子模块仍是 `requested_date=2026-08-24`、`generated_at=2026-08-24T06:24:19.226673+08:00`，即今晨没有完成新一轮海外日频刷新；22 个目标仅 6 个映射，5 fresh-by-own-lag、1 stale，且全部只允许 context、没有 executable import parity。故本期海外结论主要用 Reuters、EIA、BEA、CFTC 等公开最新来源补充。

独立 Options pipeline 的 8/24 数据为 21,726 个合约、58/64 品种成功、364 个 series；356 surface-ready、72 positioning-ready、0 execution-ready，bid/ask coverage=0。由于报告日已进入 8/25 中国交易日，8/24 Options 按 v2 规则仅作 T-1 背景，不计今日 fresh evidence。Dealer gamma direction unknown，禁止推断。

Contract Metadata 为 partial：SHFE 合约可取得 official_partial 的到期信息；DCE contract-info 当次抓取报 JSONDecodeError，GFEX contract-info 日期字段不完整。EG 的交易单位/最小变动价位可由大商所业务细则确认，但 EG2610 当日动态保证金/涨跌停未获得同等级官方确认，因此正式下单前必须由交易所/终端复核，且本报告不伪造一板/两板精确损失。

## 三、商品仪表盘

| 板块 | 合约 | 8/24 close / settle | 1D结算 | 5D | 成交 / OI / ΔOI | 有效期限结构 | Physical / basis | Options T-1背景 | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能化 | **EG2610** | 5404 / 5324 | **+3.20%** | **+9.95%** | 1,267,017 / 343,368 / **+70,384（+25.78%）** | **主2610-次2611结算 Back约+5.24%**；仓库近月曲线+10.20%含临交割扭曲，不直接用于普通curve评分 | 隆众/市场报道：8/24华东主港库存20.6万吨，较8/20的26.8万吨再降6.2万吨；repo本品种实体层缺 | ATM IV43.345% vs RV20 35.05%，RR25 +0.29；surface✓/positioning✓/execution× | **第一优先：回撤确认多** |
| 建材 | **FG701** | 922 / 923 | +1.88% | -0.43% | 2,043,327 / 1,480,236 / **-121,002（-7.56%）** | Contango | 最新周度厂库7441.4万重箱，WoW -0.07%、YoY +17.41%；高库存但本周非累库 | ATM IV23.735% vs RV20 17.95%，RR25 +6.15；surface✓/positioning✓/execution× | **只做反弹失败空** |
| 能源 | **FU2611** | 3829 / 3822 | -0.73% | +6.49% | 890,787 / 约284,651 / -963（-0.34%） | **主2611-次2612结算 Back约+4.97%**；近月FU2609临近最后交易日，+12.71%近月Back不作普通主逻辑 | repo Physical 缺失 | ATM IV45.08% vs RV20 34.42%，RR25 -0.53；surface✓/positioning×/execution× | 昨日多头降级；只等低开后重新承接 |
| 贵金属 | **AG2610** | 16843 / 16885 | +1.65% | +5.51% | 757,231 / 298,270 / **-8,552（-2.79%）** | 轻Contango约-0.26% | 实体层缺 | ATM IV48.93% vs RV20 30.60%，RR25 +8.12；surface✓/positioning×/execution× | 趋势仍强但赔率差；不追多 |
| 建材 | SA701 | 1054 / 1057 | +2.52% | +2.52% | 2,217,259 / 1,078,686 / +34,263（+3.28%） | Contango约-3.52% | 实体层缺 | ATM IV26.585% vs RV20 22.36%，RR25 +2.81；surface✓/positioning✓/execution× | 价仓强但curve反向，观察 |
| 新能源 | LC2701 | 158860 / 160020 | +2.34%结算 | — | 219,750 / 359,138 / 数据可用 | Contango | repo锂库存缺失 | surface可研究，execution× | 反弹≠短缺，不追 |
| 有色 | CU2610 | 107910 / 107750 | +0.69%结算 | — | 77,057 / 数据可用 | 近端结构无足够强信号 | 无A/B基差 | T-1 surface | 美元走强背景下不追 |
| 黑色 | I2701 | 716 / 715.5 | +1.20%结算 | — | 300,058 / 数据可用 | 无异常普通curve | repo港口库存15964原单位，最新周度8/19，仅绝对水平 | T-1 | 中性偏强，缺实体方向变化 |
| 农产品 | RM611 | — | 数据可用 | — | 数据可用 | 近期Back背景 | 实体闭环缺 | T-1 | 不做价格/curve冲突仓 |
| 航运 | EC2610 | — | 高波动 | 近期高动量 | 数据可用 | 不作普通curve套利 | 地缘运输驱动 | 无执行级vol | 45分钟内不追 |

**海外锚：** 8 月 24 日 Reuters 报 Brent 结算 **92.17美元/桶（-2.35%）**、WTI **85.01美元/桶（-2.35%）**，市场对新一轮伊朗制裁的边际反应弱于此前预期；但 Hormuz 航运约束和伊朗对部分油轮的黑名单仍保留上行尾部。黄金周一走强，现货收于约4639美元/盎司、12月期金4697.8；白银反而下跌约0.4%。美元指数约99.01、日涨约0.2%。这意味着国内 FU/AG 的外盘确认比昨日显著变差。[Reuters Oil](https://www.reuters.com/world/asia-pacific/oil-falls-1-ahead-us-announcement-impose-further-sanctions-iran-2026-08-23/) [Reuters Gold](https://www.reuters.com/world/india/gold-hits-over-3-month-high-ahead-us-inflation-data-fed-chair-speech-2026-08-24/)

## 四、相比上一交易日真正变化

1. **最大新增信号从FU切换到EG。** EG2610 8/24收5404、结算5324，结算+3.20%，5D+9.95%，单日OI+25.78%、成交z约3.63；主2610相对2611结算价差约+5.24%，不是靠临交割EG2608/2609曲线才成立。
2. **EG实体层出现方向性确认。** 8/24隆众口径华东主港库存据市场报道降至20.6万吨，较8/20的26.8万吨再去化6.2万吨，且处于近五年同期低位；8/24仓单报道为3666手。该数据来自商业/市场来源，不是交易所库存代理，口径需与期货仓单严格区分。[EG库存来源](https://finance.sina.com.cn/money/future/fmnews/2026-08-24/doc-inipkzxw2942246.shtml)
3. **FU多头被外盘和国内价仓共同降级。** FU2611 8/24结算-0.73%、OI微降；虽然2611-2612仍有约4.97% Back，但隔夜Brent/WTI均跌2.35%，说明地缘风险溢价没有继续扩张。
4. **FG空头逻辑从“顺势跌”变成“等反弹失败”。** FG701 8/24反弹，结算+1.88%，但OI骤降7.56%，5D仍略负且curve仍Contango；周度库存仅微降0.07%，同比却高17.41%。不能把价格反弹自动解释成需求修复。[玻璃库存](https://www.mysteel.com/oilchem/a/26082016/2D4AB63D4A779922.html)
5. **AG方向和期权赔率进一步分化。** 国内银价继续上涨，但OI下降、curve轻Contango；海外黄金走强而白银下跌。T-1 ATM IV升至48.93%，比RV20高约18.33 vol，RR25 +8.12，裸追Call的赔率更差。
6. **Options已刷新到8/24，但今天仍是T-1。** 356/364 series surface-ready、72 positioning-ready、0 execution-ready；可以研究IV/skew，不能把它算成8/25 fresh evidence，也不能报可成交权利金。

## 五、产业链地图

**最强：乙二醇/聚酯上游的短缺挤压。** Price/OI、有效主次月Backwardation、库存快速去化三层共振，置信度高；最大缺失是仓库自身EG Physical映射和今天9:00后真实流动性。当前regime更像“库存稀缺+资金拥挤”，不是低波动趋势行情，追价风险很高。

**最弱：玻璃/地产建材。** FG最新周度库存并未重新累积，但同比仍高17.41%，5D价格仍弱，Contango未逆转；周一反弹伴OI大幅下降只是一条价仓归因线索，不能直接称空头回补。置信度中高，最大风险是低价亏损触发供应收缩与政策beta挤压。

**能源：结构仍紧，价格确认转弱。** FU2611-2612 Back约4.97%仍强，但Brent/WTI隔夜下跌2.35%。Hormuz风险没有消失，伊朗又将45艘油轮列入黑名单，但新制裁短期未触发新一轮追价。[Hormuz](https://www.reuters.com/world/middle-east/iran-warns-vessels-violating-hormuz-transit-rules-fines-detention-2026-08-24/)

**贵金属：黄金强、白银相对弱。** 这不再是简单的“金银同涨”环境；AG已有高IV、高call skew、OI下降和轻Contango，短期更适合等回撤或做相对价值观察，不适合裸追上行Vega。

**新能源：价格反弹但短缺证据仍缺。** LC仍缺repo实体库存映射，curve没有给出短缺式Backwardation；因此价格上涨不升级为供给短缺叙事。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段/工具 | fresh证据层 | 数据惩罚 |
|---:|---|---:|---|---|---:|---|
| 1 | **EG2610 回撤确认多** | **79** | 多 / 1–5D | 条件试仓；期货优先 | **3：价仓、有效主次月curve、实体库存** | Options T-1；DCE动态margin/limit未官方确认；13连阳拥挤 |
| 2 | **FG701 失败反弹空** | **73** | 空 / 1–5D | 条件试仓 | **3：价仓线索、curve、周度库存/历史比较** | 周度库存轻微去化；参数需终端复核；低价供应收缩风险 |
| 3 | **FU2611 低开后重新承接多** | **69** | 多 / 1–3D | 观察；仅触发后小试 | 3层可观察但方向冲突 | 外油-2.35%；Price/OI转弱；Physical缺；Options T-1 |

**没有80+确认加仓交易。** 今天值得冒险，但只值得在EG/FG满足开盘触发后使用试仓风险预算。

## 七、前三名交易卡

### 1. EG2610｜79分｜回撤确认多

**事实：** 8/24 close/settle 5404/5324；1D结算+3.20%、5D+9.95%、20D+13.01%；成交z约3.63、OI水平z约2.98、ΔOI +70,384（+25.78%）。EG2611结算5059，因此2610-2611主次月Back约265元/吨、约5.24%。隆众口径市场报道8/24华东主港库存20.6万吨，较8/20再降6.2万吨。

**市场定价：** 低库存、进口/供应扰动和近端资源紧张已被快速资本化，13连阳意味着拥挤也在上升。**推断：** edge在第一次有序回撤被吸收，而不是第14根阳线开盘追涨。**主观判断：** 当前是全市场最值得承担风险的单品种，但赔率只在回撤/再确认时合格。

**最佳表达：** 小仓EG2610期货；8/24期权ATM IV43.345% vs RV20 35.05%、RR25近乎平，若8/25 fresh quote出现且bid/ask恢复，可研究35–45Δ长Call / 15–25Δ短Call的1:1 Call Spread。当前execution=false，不给净权利金。

**入场与分批：** 09:00后至少等30分钟；若高开>1.5%则等45分钟。优先等5300–5360区域被接受并重新站回5400/VWAP，先1/3；突破开盘区间高点加1/3；只有OI继续增加但不出现失控式放量、且2610-2611 Back不快速收窄时加最后1/3。直接高开并冲过5500不追。

**初始止损：** 5220下方15分钟接受先减半。**逻辑失效：** 跌破8/24低点5166并且主次月Back明显收窄、最新港口库存不再去化/进口到港显著恢复。**TP1/TP2：** 5600 / 5800。**时间止损：** 2–3个交易日不能创有效新高则退出至少一半。

**最大损失：** 初始0.35%–0.50% NAV；确认后最多0.75%。最坏情景是库存挤压迅速缓和、临近合约移仓导致结构坍塌、保证金临时上调和夜盘流动性消失。

**合约参数：** 大商所业务细则确认10吨/手、tick 1元/吨、tick value 10元；按5324结算名义约53,240元/手；标准夜盘通常21:00–23:00。repo DCE contract metadata本次错误，EG2610当日动态交易所margin/price-limit以及精确最后交易日未取得同等级官方确认；按规则最后交易日为合约月份倒数第4个交易日，规则推算约2026-10-27但下单前必须核验交易日历。因为动态limit未确认，**一板/两板压力损失不硬算**。[大商所乙二醇业务细则摘录来源](https://www.xzcs2022.com/kjfgk/17281.html)

### 2. FG701｜73分｜失败反弹空

**事实：** 8/24 close/settle 922/923，1D结算+1.88%、5D-0.43%、20D-6.01%；ΔOI -121,002（-7.56%），成交z约2.28，curve仍Contango。最新周度样本企业库存7441.4万重箱，WoW -0.07%、YoY +17.41%、库存天数34.1天不变。

**市场定价：** 深度悲观已经反映在低绝对价格中，周一出现明显反弹。**推断：** 只有反弹无法改变Contango且价格再次失守，空头赔率才恢复。**主观判断：** 不做“低价追空”，只做失败反弹。

**入场：** 等30分钟；930–945区域冲高失败并重新跌回922/VWAP下方，先1/2；跌破905且OI不出现异常流失再加1/2。若直接低开<900，不追，等反抽。

**初始止损：** 952上方15分钟接受。**逻辑失效：** curve显著收窄/转Back，且后续周度库存加速去化、产销连续改善。**TP1/TP2：** 900 / 875。**时间止损：** 3个交易日不能有效跌破900退出。

**最大损失：** 0.25%–0.40% NAV。最坏情景是政策/地产headline与行业冷修共振导致涨停式short squeeze。

**合约参数：** 20吨/手、tick 1元/吨、tick value 20元；按923结算名义约18,460元/手。repo对CZCE metadata仍partial，本期未取得同等级当日官方动态margin/price-limit确认，broker margin也未知；一板/两板压力损失不伪造，正式下单前复核交易所/终端。

### 3. FU2611｜69分｜观察卡，不是合格挂单

**事实：** 8/24 close/settle 3829/3822，1D结算-0.73%、5D+6.49%，ΔOI -963（-0.34%）。主2611与2612结算3822/3641，对应有效主次月Back约4.97%；仓库自动近月FU2609/FU2610 Back约12.71%，但FU2609已临近最后交易日，本报告不把这段近月挤压当普通curve主证据。Brent/WTI隔夜均跌2.35%。

**触发前不交易。** 若09:00明显低开，至少等30–45分钟；只有价格重新站回3820并突破Opening Range High、外油停止下跌、2611-2612 Back不收窄，才允许0.25% NAV以内小试。初始止损3760；**逻辑失效**为跌破8/24低点3725并形成接受，同时外油继续弱。TP1 3905，TP2 4000；两天不延续退出。

**合约参数：** 上期所官方合约确认10吨/手、tick 1元/吨、tick value 10元；按3822结算名义约38,220元/手。上期所2026-06-23通知明确FU2611涨跌停14%、套保保证金15%、一般持仓16%；repo official_partial显示最后交易日2026-10-30。按14%静态压力，一板约5,351元/手，两板复合约9,953元/手。券商加收保证金未确认。[SHFE风控](https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html) [FU合约](https://www.shfe.com.cn/products/futures/energyandchemical/fu_f/standard_fu/202312/t20231205_327331.html)

## 八、商品期权专项

本期只能称 **8/24代表性样本**，不能称8/25全市场最高/最低IV：21,726合约、58/64品种成功、364 series，356 surface-ready、72 positioning-ready、0 execution-ready，bid/ask coverage=0。

- EG2610：ATM IV43.345% vs RV20 35.05%，IV-RV约+8.30 vol；RR25 +0.29，skew接近平。若fresh quotes恢复，Call Spread比裸Call更容易控制Vega成本。
- AG2610：ATM IV48.93% vs RV20 30.60%，IV-RV约+18.33 vol；RR25 +8.12，call wing非常贵。方向看多也不等于应买Call。
- FG701：ATM IV23.735% vs RV20 17.95%，IV-RV约+5.79 vol；RR25 +6.15。如果该skew在8/25真实quote中延续，Put Spread相对裸Put更值得比较。
- FU2611：ATM IV45.08% vs RV20 34.42%，IV-RV约+10.66 vol；RR25 -0.53，方向skew较均衡。
- SA701：ATM IV26.585% vs RV20 22.36%，IV-RV约+4.23 vol；但价格上行与Contango冲突，不优先做方向结构。

所有结构仅研究观察：**research only; manual quote and manual confirmation required before execution; no premium quoted**。Dealer gamma方向未知；不得推断。

## 九、9:00开盘风险地图

**EG：** 最可能高开/高波动，但隔夜原油下跌会压制化工beta。gap≤1.5%等30分钟；gap>1.5%等45分钟。最重要确认：5300–5360接受度、VWAP/Opening Range、ΔOI、EG2610-2611 Back、最新港口库存/到港消息。

**FG：** 周一反弹后容易继续挤空。30分钟内不卖第一波；只有930–945失败后重新跌回922下方才做空。若高开并在950上方形成接受，取消空头计划。

**FU：** 隔夜外油明显走弱，偏低开风险。不得用“地缘仍紧张”去接第一刀。至少30分钟，异常gap等45分钟；确认外油、3820回收、2611-2612 Back和OI。

**AG：** 黄金强、白银弱，内外盘分化。若AG高开而COMEX银不跟，视为过冲；等30–45分钟。当前上行IV/skew太贵，不裸追Call。

**LC/SA/EC：** 资金动量品种统一等45分钟；LC必须先看curve是否由Contango收窄，SA要看上行是否能克服Contango，EC要看Opening Range与流动性而不是headline追价。

## 十、未来24小时 / 7日事件

- **8月26日20:30 BJT：美国7月Personal Income and Outlays / PCE。** BEA明确8/26 08:30 ET发布。对美元、实际利率、金银Vega影响高；贵金属仓位进入事件前应降低裸Vega。[BEA](https://www.bea.gov/sites/default/files/2026-02/pi1225.pdf)
- **8月26日22:30 BJT：EIA Weekly Petroleum Status Report。** EIA页面确认下一次8/26、10:30 ET。对SC/FU/LU/BU和裂解链Delta高；能源新仓不宜在数据前放大。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **8月27–29日：Jackson Hole Symposium。** 重点是Fed主席Kevin Warsh讲话及利率路径预期，对DXY、黄金、白银和有色估值影响高。
- **8月29日03:30 BJT：CFTC COT。** CFTC 2026日历确认8/28 15:30 ET发布，仅作为滞后拥挤背景，不作实时flow。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **持续非定时：Hormuz通航、伊朗制裁/反制、Black Sea港口和能源设施。** 伊朗8/24将45艘油轮列入黑名单；这些事件对能源、航运与粮运均可能造成夜盘gap。

## 十一、风险预算

试仓单笔最大损失0.25%–0.75% NAV；今天没有80+确认加仓交易。EG初始0.35%–0.50%、满足第二次确认后最多0.75%；FG初始0.25%–0.40%；FU若触发也只允许≤0.25%，因为目前仅69分观察。

EG/FU/SC/LU/BU并非完全独立：都受中东供应、原油/成品油成本和化工beta影响，合并初始主题风险建议≤1.25% NAV。AG/AU合并美元—实际利率—贵金属Vega风险。压力测试必须覆盖夜盘gap、1/2个涨跌停、保证金上调、相关性断裂、curve快速塌陷、交割挤压和人民币急变。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：EG2610回撤确认多；FG701反弹失败空。  
C. 今天应继续观察的机会：FU2611低开后重新承接、SA701价仓强但Contango、AG2610高IV下的回撤/波动率相对价值。  
D. 今天必须避免或退出的交易：追EG高开、裸买AG高IV Call、在FG低开时追空、把LC上涨解释成短缺、把临交割近月curve或C/D级basis写成套利。

## 主要来源

- China-Commodities-Engine（main）：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`、`data/latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/contract_meta.json`。
- Reuters：8/24原油收盘、新制裁与Hormuz；8/24贵金属收盘。
- 隆众资讯/市场转载：8/24乙二醇华东主港库存；8/20浮法玻璃样本厂库。
- SHFE：FU合约文本及2026-06-23动态风控通知。
- EIA、BEA、CFTC：本周事件日历。
