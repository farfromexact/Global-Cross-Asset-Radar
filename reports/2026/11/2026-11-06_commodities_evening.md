# 2026-11-06 商品期货期权晚间雷达

> 版本：radar_2026-10-12_stock_v1｜commodity_consumer=core_2026-10-17_v1｜research_quality=2026-10-21_v1  
> 生成：2026-11-06 19:40:09 北京时间｜信息截点：19:40 北京时间｜中国最新完整日盘：2026-11-06｜下一夜盘归属：2026-11-09  
> 仅作研究与决策支持；不下单，不假定任何建议已成交或已持有。

## 1. 一句话结论

截至本报告时点，无可立即执行的合格新交易；今晚只承担非农后经顺序确认的锡空、原油多与铜跨期风险，不追日盘极值。

**今晚值得承担的风险只有“等待后再承担”：** 21:00先看开盘，21:30美国非农后，只有SN反弹失败、SC回踩企稳且布伦特同步、CU跨期价差回撤再确认三类条件候选。**截至本报告时点，无可立即执行的合格新交易。**

- 已研究但优势不足：AP强势但OI下降；PP/L/PG/PL暴跌伴OI下降且曲线仍倒挂；EC缺当周现货；均不追。
- 研究机会存在但条件/报价未到：SN、SC、CU跨期、MA跨期。
- 数据不足不能判断：当前21:00夜盘尚未发生；night明细文件为空；期权无bid/ask；DCE官方交叉核对HTTP 412；动态保证金/涨跌停未核。
- 最有价值的下一窗口：21:00开盘观察；21:30非农；21:45/22:00顺序确认。EC、LC等无夜盘品种下一窗口为11月9日09:00。

## 2. 数据质量、覆盖与事实台账

### 2.1 覆盖数表

| 模块 | 目标 / 实得 | 日期与生成 | 状态 | 局部影响 |
|---|---:|---|---|---|
| Futures | 806合约 / 77品种 / 五所 | 11-06；19:04 | vendor full_market_ready=true；source-date=100%；critical=0；OHLC占位4 | 五所EOD可用于研究；并非全部官方认证 |
| 五所 | SHFE 238、INE 63、DCE 214、CZCE 243、GFEX 48 | 均为11-06 | full_market_ready=true | 全范围初筛完成 |
| Market State | 77品种 | 11-06 | 1/3/5/20D、RV、OI、curve可读；部分roll提示 | 同合约历史，不把roll拼接当收益 |
| Physical | 20目标，18 fresh，2 unavailable | 19:14 | A/B basis=0；现货均C级 | 只作背景，不计方向层或套利 |
| External | 22目标，17 fresh，5 unavailable | 19:15 | context_only | 需和公开盘中来源分层 |
| Night | 上一合法会话420/806=52.11%；outside 166；no-trade 6；query/unresolved 214 | 11-05夜→11-06交易日；05:59发布 | validated/published=true；complete=false；明细latest为空 | 不复用旧夜盘价；当前11-06 21:00尚未发生 |
| Options | 64目标，46尝试，44成功，2失败，18跳过；1048条 | 11-06 | ATM 44、skew 29、surface/positioning/execution 0；bid/ask=0；full_chain=false | 可研究局部IV/skew，不可声称可成交 |
| Metadata | contract match 67.49%；multiplier/tick 30.15%；LTD 67.49% | 11-06 | partial；DCE 412、GFEX日期缺 | Top3乘数/tick另以交易所规则核；动态参数仍阻断 |
| Official crosscheck | SHFE 238、INE 63、CZCE 243、GFEX 48；DCE失败 | 19:15 | 四所可比settle/close/pre-settle差异均0；DCE 412 | 不代表volume/OI官方核验 |
| Stock | 5571只EOD，2个最小财务包 | 股价11-05；research_asof 11-06 08:32 BJT | 复权、行业、实时可交易性不足 | 仅利润桥；不宣称即时股票交易 |

[data/report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) 本次读取为empty，不是missing或truncated；因此按协议使用模块文件与root status。核心路径：[last_run_status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[market_state](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[external](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)、[options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)。

### 2.2 Night与日历闸门

11月6日是周五且不在2026休市清单；按[上期所交易时间](https://www.shfe.com.cn/services/calenderandholidays/tradinghours/)，“某交易日夜盘从上个工作日21:00开始”，因此今晚21:00会话归属11月9日周一。上一状态文件的trading_date=11-06、session_start_date=11-05合法，calendar_mismatch=false；它不是“今晚夜盘”。当前会话未开始，不因未来数据缺失扣分。night明细文件empty，故没有重点合约上一会话的可复核snapshot、双锚或纯夜盘OI；不以旧报告替代。

### 2.3 可追溯事实台账

| fact_id | 标的 / 单位 / 口径 | 观测、known_at、读取 | 来源 | 支持判断 | 局限 |
|---|---|---|---|---|---|
| F-EOD-001 | 五所806合约，CNY各合约单位，EOD close/settle | 11-06 EOD；generated 19:04；read 19:40 | Engine latest/status | 全市场EOD扫描 | vendor全市场≠全部官方 |
| F-SN-002 | SN2612 343340/346310 CNY/t close/settle | 11-06 EOD；read 19:40 | Engine latest | 日跌、5D弱势 | OHLC不证明触发顺序 |
| F-CU-003 | CU2612-2701 close spread 1180、settle 1080 CNY/t | 11-06 EOD；read 19:40 | Engine latest | 近月相对韧性 | 不是可成交实时价差 |
| F-NGT-004 | 420/806，prior night status | 11-05 21:00至11-06；generated 05:59 | Night status | 覆盖局部 | 明细empty，不用于价差/收益 |
| F-OPT-005 | 44/64，ATM44，skew29，bid/ask 0 | 11-06 EOD；generated约19:05；read19:40 | Options quality/surface | 局部IV、skew | 无执行性/全链/positioning |
| F-OIL-006 | Brent Jan 97.55 USD/bbl，08:26 GMT | 16:26 BJT；Reuters 11-06；read19:40 | [Reuters](https://www.reuters.com/business/energy/oil-set-sharp-weekly-drop-middle-east-supply-concerns-provide-floor-2026-11-06/) | 油价外部压力 | repo 19:15 context=98.38，时点冲突 |
| F-LME-007 | LME closing page，USD/t | 11-06页面最新显示；read19:40 | [LME](https://www.lme.com/market-data/reports-and-data/lme-closing-prices) | 锡约45.5k、铜海外弱 | 非21:00同步成交报价 |
| F-EVT-008 | 美国10月非农 | 11-06 08:30 ET=21:30 BJT | [BLS](https://www.bls.gov/ces/) | 今晚主催化 | 结果尚未发布 |
| F-PHY-009 | 18个日频现货，C级 | 11-06；generated19:14 | Engine physical | 产业背景 | 0个A/B，不能算方向层 |
| F-XCK-010 | 四所价格零差，DCE 412 | 11-06；generated19:15 | Engine crosscheck | 四所价格复核 | 不核volume/OI |
| F-STK-011 | 紫金、宝钢2026H1 YTD合并财务 | 报告期6/30；公告8/22；engine known_at 11-06 08:29 | [紫金中报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)、[宝钢中报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF) | 利润传导验证 | 不是今晚新催化 |

### 2.4 全范围后台扫描

| 板块 | 实得与已分析代码 | 未入榜最重要异常 / 无异常依据 |
|---|---|---|
| 黑色与建材（10） | FG/SA/SF/SM/I/J/JM/HC/RB/WR | JM +1.40%但OI -3.43%；RB仅+0.36%，未形成同向板块确认 |
| 金属（14） | PD/PT/BC/AD/AG/AL/AO/AU/CU/NI/PB/SN/SS/ZN | SN -2.04%且量能z=2.56；CU曲线z=2.48；NI +2.14%但OI下降 |
| 能源化工航运（26） | MA/PF/PL/PR/PX/SH/TA/UR/ZC/BZ/EB/EG/L/PG/PP/V/EC/LU/NR/SC/BR/BU/FU/OP/RU/SP | SC/LU反弹与PP/L/PG/PL下跌分裂；EC contango |
| 新能源（3） | LC/PS/SI | LC +1.26%但OI -6.00%，未确认趋势 |
| 农产品（14） | OI/RM/RS/A/B/C/CS/JD/LG/LH/M/P/RR/Y | JD -2.84%；M -0.48%；DCE交叉核对缺口限制精确执行 |
| 软商品与特色（10） | AP/CF/CJ/CY/JR/PK/PM/RI/SR/WH | AP +4.92%最突出但OI下降；不追 |

## 3. 市场仪表盘（12项）

| 品种 / 准确合约 | EOD close / settle | 1D / 5D / RV20 | 量仓与曲线 | Physical / Night / 外盘 / Options | 信号 |
|---|---:|---|---|---|---|
| SC2612 / SC2701 | 644/636.8；639.8/631.8 | SC2701 +0.19% / -3.47% / 44.64% | OI +1.25%；settle spread +5.0=0.79% | SC现货缺；当前Night未开始；Brent 97.55与repo98.38冲突；SC IV63.86>RV | 非农后回踩确认多，非立即 |
| SN2612 | 343340 / 346310 | -2.04% / -7.13% / 28.52% | vol z2.56；OI +2235/+5.59%；backwardation | 无A/B实体；当前Night未开始；LME锡约45.5k；IV43.96、RR25 -8.78 | 反弹失败空，禁止低开追 |
| CU2612 / 2701 | 104260/105110；103080/104030 | -1.14% / -2.52% / 11.64% | OI +5.04%；spread close1180、settle1080 | 现货C级；LME铜弱；IV19.27、RR25 -9.28 | 价差过了旧追价线，等回撤 |
| PP2701 | 9585 / 9496 | -3.51% / -2.98% / 33.95% | OI -9.49%；近月曲线仍backwardation | DCE官方核对失败；期权跳过 | 去杠杆，不追空 |
| L2701 | 8792 / 8762 | -3.78% / -2.49% / 31.51% | OI -9.64% | 同上 | 不追空 |
| AP701 | 6004 / 5969 | +4.92% / +9.81% / 37.20% | OI -3.40%；backwardation | ATM IV33.55<RV但无bid/ask | 只观察失败形态 |
| MA701 / 702 | 3263/3211；3139/3102 | MA -0.71% / -1.86% / 44.06% | close spread124、settle109 | MA现货C级；MA612期权不是同腿 | 研究升水压缩 |
| EC2612 | 2326 / 2351 | -1.59% / -5.63% / 45.22% | OI +1.34%；contango -7.83% | 无当前现货/期权；无夜盘 | 11/9日盘条件空 |
| AG2612 / 2702 | 12367/12539；12402/12575 | -0.43% / -6.14% / 39.95% | 主力已roll至2702 | IV47.17，skew不ready | 旧多失效，不重置 |
| LC2701 | 92860 / 91940 | +1.26% / -2.38% / 44.22% | OI -6.00% | 现货C级；ATM IV52.15，无skew；无夜盘 | 反弹缺仓量确认 |
| JM2701 | 1414 / 1414.5 | +1.40% / +2.02% / 29.93% | OI -3.43%；backwardation | 现货C级；DCE核对失败 | 观察 |
| AU2612 | 869.86 / 879.22 | -0.00% / -0.56% / 19.25% | OI -1.62%；contango | 非农前；ATM IV23.92 | 事件敏感，回避裸Vega |

Night列统一说明：上一合法明细文件empty，本表不编night snapshot/%vsClose/%vsSettle/ΔOI；当前21:00尚未发生。

## 4. 相比前序的五项真变化与旧观点处置

1. **SC从晨间观察到日盘收644。** 日内low 628.2、high 652.5跨越多个旧阈值，但OHLC不能证明“先回撤—守位—再收复”的顺序，更不能证明成交。晨报多头idea保留同一ID，revision 1→2；原止损632、触发642改为只适用于今晚新候选的止损636、非农后收复646。假设已有仓不适用新参数。
2. **SN弱势得到海外锡低位背景，但曲线反证增强。** 分数70→72，原因是11-06日盘和LME页面；backwardation仍反对空头，不追低开。
3. **CU价差已超过晨报“direct spread≥1050放弃”。** 晨报执行计划判为abandoned-for-immediate，不回填盈利；同ID revision 2只等待950—1000回撤后的新顺序。
4. **能源化工从同向下跌变成上下游分裂。** SC/LU反弹，PP/L/PG/PL继续跌且PP/L OI减少近一成；这降低“追空全链”的确信。
5. **AG多头旧观点继续失效。** 当前主力roll至AG2702，AG 5D仍-6.14%；不因换月重置idea_id或移动旧止损。

前序基准：[2026-11-06晨报MD](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-06_commodities_morning.md) / [JSON](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-06_commodities_morning.json)；最近同版：[2026-11-05晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-05_commodities_evening.md)。

## 5. 产业链与Stock利润桥

### 5.1 原油—燃料—化工

SC/LU强而PP/L/PG/PL弱，最自然解释是原油地缘溢价与下游去杠杆同时发生，不是单一需求信号。Reuters 16:26 BJT布伦特97.55、WTI89.79，且中东船舶袭击提供下方风险；repo 19:15 context为Brent98.38，两时点不一致，必须等同时报价。

中国海油只做表达比较：上游股利润桥是“实现油气价×销量－桶油成本±套保/汇率/税/资本开支”，其产量与成本缓冲会弱化今晚SC的纯事件Delta。Stock证据目录没有其完整财务包、当前报价或可交易状态，因此不纳入Top5，不是即时替代。

### 5.2 锡/铜—矿山—冶炼—股权

SN日盘跌、LME锡约45.5k，空头价格层与海外层一致；但近月backwardation反对空。CU outright弱、CU2612/2701价差强，说明库存/近月约束可能仍在。Reuters转引的交易所库存下降只作实体背景，不替代A/B基差。

紫金矿业601899.SH：11月5日未复权EOD 29.48元，1D +0.79%、5D +5.14%，不是今晚报价。2026H1合并YTD营收1941.78亿元、归母391.70亿元、经营现金流554.72亿元，归母同比+68.17%。利润桥是铜金实现价与矿产量减现金成本，再经冶炼、库存、套保、汇率、少数股东与资本开支；Kamoa减产/检修是最强竞争解释。**对CU跨期价差，股票比直接1:1期货差**：多金属与经营因子太多，且股价近5日已涨、实时可交易状态未核。只作背景，不加第六层。

### 5.3 煤—甲醇—聚烯烃—钢铁

JM上涨、MA小跌、PP/L大跌，传播不连续。MA701/702价差压缩具有研究价值，但Physical为C级、MA期权标的是MA612而不是同腿，不能包装成可执行套利。

宝钢股份600019.SH：11月5日未复权EOD 6.08元，1D -1.62%、5D +1.33%。2026H1合并YTD营收1607.31亿元、归母45.71亿元、营业成本1511.02亿元；营收同比+6.18%而归母同比-6.30%。利润桥是钢价/销量减矿煤能源成本，再经品种结构、库存、长协、套保传导。最强反解释是下游需求与产品结构抵消原料变化。**它不比直接JM/钢材价差更纯**，并降低“原料变化必然改善钢企利润”的确信。

### 5.4 苹果

AP日盘强、OI下降、ATM IV局部低于RV。可能是现货/天气或空头回补，也可能是波动采样差异；没有决策级Physical与bid/ask，下一项区分观测是11月9日开盘是否在6000上方稳定30分钟且OI回升。

### 5.5 航运

EC2612 5D -5.63%且contango，但当前周度现货/运价映射缺失。没有夜盘；下一真实窗口11月9日09:00。只研究反弹失败空，不在缺现货时扩大确信。

## 6. 统一机会榜（上限5，不是配额）

| 排名 | idea_id / 方向 / 期限 | 五层证据（支持；反证/缺失） | 25/25/20/15/15 | 总分 | 研究 / 证据 / 执行 |
|---:|---|---|---:|---:|---|
| 1 | SN2612反弹失败空 rev2；1—5D | 1价格、4海外、5skew；2倒挂反对；3缺 | 20/17/15/12/8 | **72** | focus / 3层有冲突 / 等21:45 |
| 2 | SC2612非农后确认多 rev2；1—3D | 1价格、2曲线；4时点冲突、5高IV反对；3缺 | 19/15/15/12/8 | **69** | focus / 2层封顶 / 等Brent同报 |
| 3 | CU2612/2701价差多 rev2；3—10D | 1相对价、2曲线；4外铜弱、5偏度反对；3 A/B缺 | 19/16/14/11/9 | **69** | watch / 2层封顶 / 旧追价线已过 |
| 4 | MA701/702升水压缩 rev2；3—15D | 1相对价、2曲线；3/4/5缺 | 18/15/13/11/9 | **66** | watch / 2层 / 等同步腿价 |
| 5 | EC2612反弹失败空 rev3；5—20D | 1价格、2曲线；3/4/5缺 | 17/15/13/11/8 | **64** | watch / 2层 / 11-09日盘 |

评分只表研究优先级，不是胜率。支持层不足时严格执行≤69上限。

## 7. 三张完整研究/交易卡

### 卡1｜SN2612反弹失败空｜idea rev2

- **事实：** close 343340、settle 346310、pre-settle 353520；1D -2.04%、5D -7.13%；volume 342256、OI 42233、ΔOI +2235；SN2612/2701 settle spread +3180。上一合法Night明细不可用；当前Night未开始。
- **定价与分歧：** 市场已定价一段下跌；我们的分歧只在“非农后反弹仍失败且LME锡不回到45800上方”。backwardation与丰富的put skew是最强反证。
- **触发：** 21:45后，先反弹344000—346000，随后15分钟收在343000下，且同一时点LME 3M锡≤45800，才按343000/342000/341000分30/30/40；不得倒置顺序。
- **止损/失效/退出：** 351000计划止损；15分钟收上351000或LME锡>47800逻辑失效；TP1 330000、TP2 318000；11月12日14:45时间退出。直接≤340000低开、无LME同报、动态参数未确认则放弃。
- **合约：** 1吨/手，最小10元/吨，tick value 10元；21:00—01:00；最后交易12月15日、交割末12月17日。动态保证金与涨跌停未知，执行不ready。
- **好/中/坏成交：** 假设每手费用+滑点200元：343000风险8200元，TP净12800/24800，1.56R/3.02R；342000为9200、11800/23800，1.28R/2.59R；341000为10200、10800/22800，1.06R/2.24R。
- **压力：** 一涨停损失=1×入场价×当日核实L；连续两涨停=1×入场价×[(1+L1)(1+L2)-1]，再加滑点；未核L不编金额。止损不封顶。
- **表达比较：** 直接期货优于昂贵put；期权仅可在取得bid/ask、净支出≤本卡风险预算后重评。试仓≤NAV0.35%，确认≤0.75%，锡主题≤1.25%。

### 卡2｜SC2612非农后回踩确认多｜idea rev2

- **事实：** close644、settle636.8、pre-settle638.4，日内628.2—652.5；SC2701 close639.8、settle631.8；settle spread +5.0（0.79%）。日内穿价不证明晨间触发。
- **定价与分歧：** 曲线与收盘弹性支持近月韧性；但Reuters布伦特97.55与repo context98.38冲突，SC ATM IV 63.86显著高于RV20 44.64。错价仍是假设。
- **触发：** 21:45后先回踩640—642，15分钟不收破638，SC2612/2701同口径价差≥4.5且同时报价Brent≥98.50，再15分钟收复646；按646/647/648分30/30/40。
- **止损/失效/退出：** 636计划止损；15分钟收破636、Brent<97或价差<3失效；TP1 660、TP2 680；11月10日22:45退出。直接≥650无回踩、外盘冲突不解则放弃。
- **合约：** 1000桶/手，最小0.1元/桶，tick value 100元；21:00—02:30；最后交易11月30日、交割末12月7日。动态保证金/限幅未核。
- **好/中/坏成交：** 假设费用+滑点1500元：646风险11500元，TP净12500/32500，1.09R/2.83R；647为12500、11500/31500，0.92R/2.52R；648为13500、10500/30500，0.78R/2.26R。坏成交仅TP2赔率尚可，因此648上方不追。
- **压力：** 一跌停损失=1000×入场价×L；两跌停=1000×入场价×[1-(1-L1)(1-L2)]，再加gap/滑点。期货最大损失不由计划止损限定。
- **表达比较：** SC期权ATM IV高且无bid/ask；不称call spread便宜。试仓≤0.35%，确认≤0.75%，油主题≤1.25%，与FU/LU及中国海油因子合并。

### 卡3｜CU2612/2701近月价差多｜idea rev2

- **事实：** CU2612 close/settle 104260/105110，CU2701 103080/104030；close spread1180、settle1080。CU2612 1D -1.14%、5D -2.52%、ΔOI +9880/+5.04%，curve z=2.48。
- **旧计划处置：** 晨报“direct spread≥1050放弃”，当前close已经1180；原计划不得回填为成交/盈利。revision 2仅适用下一次回撤。
- **触发：** 价差先回撤950—1000、15分钟不收破800，再收复1050，且LME铜≥13750、两腿同步深度合格；按950/975/1000分30/30/40。
- **止损/失效/退出：** 800计划止损；15分钟价差<800或LME铜<13550失效；TP1 1400、TP2 1650；11月20日14:45退出。无回撤、不同步腿价或深度不足放弃。
- **合约：** 各5吨/手，tick 10元/吨、每腿tick value 50元；1:1等吨，不是beta-neutral或margin-neutral。两腿夜盘21:00—01:00；LTD分别12月15日、1月15日。
- **好/中/坏成交：** 假设每对费用+滑点500元：950风险1250元，TP净1750/3000，1.40R/2.40R；975为1375、1625/2875，1.18R/2.09R；1000为1500、1500/2750，1.00R/1.83R。
- **压力：** 相关性断裂时一限幅近腿下跌且远腿上涨的毛损失公式为5×(P近×L近+P远×L远)+费用；两限幅复合计算。限幅未核，不编金额。
- **表达比较：** 直接跨期优于紫金股权与CU put；后两者加入多金属/方向/IV污染。试仓≤0.35%，确认≤0.75%，铜主题≤1.25%。

## 8. 商品期权专项

- 样本是core_v1 / sampled_strikes，不是全链：64目标、44成功；quote_coverage_complete只表示1048个已选合约完成。
- **SC2612 11/12：** ATM640，IV63.86%，RR25 -0.09，BF25 1.66；RV20 44.64%，IV-RV +19.22点。非农/地缘凸性已贵，不裸买。
- **SN2612 11/24：** ATM345000，IV43.96%，RR25 -8.78，BF25 0.10；RV20 28.52%，下偏度贵，不追put。
- **CU2612 11/24：** ATM106000，IV19.27%，RR25 -9.28，BF25 3.61；RV20 11.64%，用跨期代替方向put。
- **AP701 11/26：** ATM6000，IV33.55%，RR25 -2.48；RV20 37.20%，IV-RV -3.66点只是假设便宜，因无bid/ask、模型与事件概率。
- **LC2701 12/07：** ATM92000，IV52.15%，skew不ready。
- 全部surface_ready=false、positioning_ready=false、execution_ready=false；不推全链PCR、dealer Gamma、wing/tail或期限结构，不编权利金、净成本与Greeks组合。

## 9. 21:00夜盘风险地图

| 层 | 已知信息 | 风险判断 | 21:00 / 21:15 / 21:30 / 21:45 |
|---|---|---|---|
| Previous China EOD | SN、CU弱；SC/LU强；PP/L/PG/PL弱；AP强 | 开盘可能分化，不把日盘close-settle差写成夜盘涨跌 | 21:00只记录exact-contract价、成交时点与两锚 |
| Completed historical night | 状态属于11-06交易日，明细empty | 不能用于今晚高低开或Night→Day分解 | 不引用旧夜盘价 |
| 19:40 Overseas/events | Brent时点冲突；LME锡/铜偏弱；21:30非农 | 21:30前信号易反转 | 21:15看价差/深度；21:30禁止新增；21:45首次允许确认 |

- **潜在高开：** SC若Brent同时报价≥98.50且SC近月价差≥4.5；高开≥650无回踩不追。
- **潜在低开：** SN若LME锡≤45800；低开≤340000不追，必须先反弹再失败。
- **内外冲突：** CU价差强而LME铜弱；只做价差，不做裸多。
- **无夜盘：** EC、LC等下一真实窗口为11月9日09:00，等09:15/09:30/09:45确认。
- 15/30/45分钟是从各自合法开盘计时；本报告不宣称未来行情已经发生。

## 10. 未来24小时 / 7日事件与行动前检查

| 北京时间 | 事件 | 处理 |
|---|---|---|
| 11-06 21:30 | [美国10月非农](https://www.bls.gov/ces/) | 21:30前不确认；之后重算美元、油、金属、IV |
| 11-07 04:30（需官网逐项复核） | [CFTC COT日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) | 只作拥挤背景 |
| 11-09 09:30 | [中国CPI/PPI](https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html) | 化工/金属利润与需求验证 |
| 11-10 21:30 | [美国CPI](https://www.bls.gov/schedule/news_release/cpi.htm) | AU/AG/CU的Delta/Vega控制 |
| 11-11 01:00 | [EIA STEO](https://www.eia.gov/outlooks/steo/release_schedule.php) | SC期限与供需再评 |
| 11-13 01:00 | [EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/schedule.php) | 退伍军人节延后；库存/炼厂冲击 |
| 7日内，精确日时待核 | USDA/WASDE、OPEC/IEA | 未核原始日程前不作为触发 |

行动前必须重取：当前exact-contract bid/ask、两腿同时报价、LME/Brent同时时点、动态保证金/涨跌停、SC/SN/CU交割参数、期权净支出；重审旧计划是否已过放弃线。无账户持仓回执，实际持仓状态一律“未提供/未知”。

## 11. 最终行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：21:45后SN2612反弹失败空、SC2612回踩确认多、CU2612/2701价差回撤确认多；均须满足顺序、同时报价与参数复核。  
C. 今天继续观察：EC2612、MA701/702、AP701，以及SC/LU与PP/L/PG/PL的产业链分化。  
D. 今天必须回避或有条件退出：回避21:30非农前追单、无bid/ask期权、DCE参数未核的精确执行、日盘极值追涨杀跌；若存在未披露旧仓，仅按原止损/时间退出处理。

---

归档状态：pending；CI：pending_or_unverified。发布前复核已完成评分加总、PnL公式、日历归属、合约月份与输出语义；未解缺口已列，核验不等于全面行情或成交认证。
