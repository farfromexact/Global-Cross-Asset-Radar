# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-20｜版本：commodities_evening｜信息截点：2026-10-20 19:32 BJT**  
**prompt_version：radar_2026-10-12_stock_v1｜data_protocol_version：china_commodities_core_2026-10-17_v1**

## 1. 今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC获四层方向支持但地缘溢价已高，今晚只等开盘留存，RM/LH空头不追跌。**

已研究但优势不足：追跌EC、追高油链、AL续多、贵金属抄底；机会存在但等待条件/报价：SC2612条件多、RM701与LH2701条件空；数据不足不能判断：DCE官方独立核价、全品种A/B级基差、期权可成交成本、SC/RM实时Night Curve。下一窗口：SC/RM及多数夜盘品种为2026-10-20 21:00，LH/EC为2026-10-21 09:00日盘。

## 2. 数据质量、会话与覆盖

本次固定读取Global-Cross-Asset-Radar main ref `07b623a23014618c2208b25ac45291008b6c92ab`、China-Commodities-Engine ref `8f05b14f9699b2f649e409d900593ce1b5e9d4d5`、China-Stock-Engine ref `79c96a9d9e73a7c2a13d340229acc7c64f4ec144`。统一输入requested_date=2026-10-20、generated_at=19:13:35 BJT。

| 模块 | 源日/生成时点 | 目标→实际 | published / analytical / execution | 局部限制 |
|---|---|---|---|---|
| Futures | 2026-10-20 / 19:06 | 5所、77品种、806合约 | yes / yes / conditional | source_date_match 100%，full_market_ready=true；8个OHLC占位、critical=0；零价无成交合约剔除排名 |
| Market State | 2026-09-15—10-20 | 20个交易日 | yes / exact-contract / conditional | 换月与pair-roll逐项标记，不拼连续主力收益 |
| Physical | 2026-10-20 / 19:12 | 20→18 fresh，2 unavailable | yes / context-heavy / no | validation=true；现货均C级、无A/B basis，不计完整第二或第三层 |
| External | 2026-10-20 / 19:12 | 22→17 fresh，5 unavailable | yes / context-only / no | 缺DXY、USD/CNH、Dubai/Oman、HSFO/VLSFO；不同合约时点不称套利 |
| 已完成Night | trading_date=2026-10-20；session=10-19 20:00—10-20 03:45 | 806请求；410 Night、172 outside、10 no-trade、214 query_error | published/partial/no | validation=true、coverage_complete=false；`vendor_latest_trade_asof_snapshot`，official_night_close_verified=false；日历一致，无calendar_mismatch |
| Options Core | 2026-10-20 / 19:07 | 64目标、46尝试、44成功、2失败、18 skipped；1002合约/44 series | core ATM 44、skew 30；surface/positioning/execution均0 | core_v1、sampled_strikes、full_chain_verified=false；IV 100%、OI 98.90%、bid/ask 0%，不编权利金/滑点/dealer gamma |
| Contract Metadata | 2026-10-20 | effective match 73.45% | partial | multiplier/tick/margin/limit仅30.15%；缺字段不猜，SC/RM用交易所原始规则补核 |
| Stock | 最后有效2026-10-15 | 仅紫金、宝钢4条映射；candidate_union=0 | stale / limited / no | 10月16日采集SSL超时；无相关能源、菜粕、生猪公司当前证据，不列股票候选 |

官方独立价格核对：SHFE 238、INE 63、GFEX 48个合约的settle/close/pre-settle全部零差异；CZCE 243个settle/pre-settle及181个可比close零差异；DCE接口HTTP 412，故DCE vendor数据仍可研究，但LH等执行结论受“未独立官方核价”限制。该核对不覆盖成交量和持仓。

## 3. 全范围扫描与12项仪表盘

后台实扫77个引擎品种，覆盖要求的63个代码；LPG按交易所代码PG映射。新增/额外扫描包括BZ、PL、OP、PT、PD、LG、RS、RR、WR等。JR/PM/RI/WH/ZC及部分远月为零成交/零收盘占位，不进入异常榜。表内1D/5D为同准确主力结算收益，curve为仓库near-next百分比；Night为昨晚已经完成且归属10月20日的供应商快照，不是今晚行情。

| 板块/准确合约 | EOD close/settle | 1D/5D | vol/OI/ΔOI；RV20 | curve | 已完成Night→日盘 | Options/外盘 | 结论 |
|---|---:|---:|---|---:|---|---|---|
| 原油 SC2612 | 727.2/727.3 | +1.18%/-0.64% | 146,437/35,749/+2,469；55.07% | +0.55% | 735.6，较前收+3.08%；日盘较快照-1.14% | ATM730 IV56.64%，RR25 +6.22；Brent 111.26 | 四层支持，等21:15，不追首跳 |
| 燃油 FU2701 | 4976/4928 | -0.59%/+6.00% | 493,047/237,144/+6,146；46.13% | +10.33% | 4852，较前收-1.32%；日盘+2.56% | 期权对应FU2612非同合约；缺HSFO | 强结构但尾盘低于日高，条件观察 |
| 菜粕 RM701 | 2274/2299 | -2.17%/-3.32% | 891,955/704,711/+19,341；18.98% | -1.22% | 2306，较前收-1.66%；日盘再-1.39% | ATM2300 IV17.08%，RR25 +0.83 | 晨报价破获收盘确认；不追跌 |
| 生猪 LH2701 | 9995/10110 | -2.03%/-5.38% | 170,782/207,052/+15,474；18.38% | -3.56% | query_error；制度无今晚夜盘 | DCE options skipped；官方核价缺 | 趋势最弱，明早等反抽/二次破位 |
| 铝 AL2612 | 23045/23000 | -0.07%/-0.99% | 145,880/236,244/+14,855；10.79% | +1.35% | 23105，较前收+0.59%；日盘-0.26% | options为AL2611；LME铝2989.5 | 晨报续多未确认，降级 |
| 集运 EC2611 | 2555/2653 | -4.43%/-3.93% | 22,633/16,761/-2,550；40.48% | -16.94% | 无夜盘、旧快照outside-window | 无合格期权面 | -7.96%收盘跌幅后严禁追空 |
| 工业硅 SI2612 | 8710/8770 | -1.52%/-1.90% | 113,220/202,093/+24,662；11.94% | -2.96%* | 无合法Night分解 | ATM8800 IV14.44%，RR25 +0.47 | 价弱仓增；curve pair roll，降级 |
| 玻璃 FG701 | 846/854 | -1.04%/-0.58% | 1,014,567/1,611,348/+92,017；16.66% | 0.00% | 864，较前收+0.58%；日盘-2.08% | ATM850 IV22.25%，RR25 +5.35 | Night反转、仓增；只观察 |
| PVC V2701 | 4994/4975 | +1.04%/+2.24% | 1,873,574/1,121,758/+29,992；19.68% | -0.49% | query_error | DCE options skipped | 化工相对强但缺夜盘与实体确认 |
| 碳酸锂 LC2701 | 100520/99740 | +0.36%/-5.44% | 344,770/430,070/+11,279；41.47% | +1.34% | 无合法Night分解 | ATM100000 IV50.19%，无合格skew | 高波反弹，非趋势反转证据 |
| 黄金 AU2612 | 892.06/893.02 | -0.94%/-1.09% | 188,139/219,729/-2,342；14.96% | -0.14% | 895.3，较前收-0.79%；日盘-0.36% | ATM896 IV19.93%；现货金4120.49 | 海内外同弱，未见反转 |
| 白银 AG2612 | 13967/13861 | -0.68%/-5.63% | 306,494/280,523/+1,015；31.56% | -0.19% | 13917，较前收-0.59%；日盘+0.36% | options为AG2611；现货银57.19 | 修复但证据不足，不追 |

\*SI curve发生pair-roll，不作正式期限支持。

板块未入榜核对：黑色最重要异常为JM2701收盘-2.36%、FG仓增下跌；有色除AL外SN/NI反弹但5日仍弱；能源化工BZ/EB/V领涨而PG下跌，产品分化；新能源LC反弹、SI价弱仓增；农产品RM/LH/JD弱、P反弹，缺实体变化确认；软商品AP 5日-12.16%但继续追空赔率差；航运EC为日盘极端波动且无夜盘。所有板块均实际取得EOD并分析，Physical/External/Options缺口按模块局部限制。

## 4. 相比前序的真变化与旧观点处置

1. **RM晨报条件得到EOD确认，但不能认定成交。** RM701从昨夜2306快照降至2274，日盘再跌1.39%，收盘低于晨报2295触发线且curve仍负；没有09:15后的分钟路径，所以只把研究状态升为“已收盘确认、等今晚重建入场”，不记持仓或收益。
2. **LH方向确认、赔率变差。** LH2701收9995、日内低9985，低于晨报10180触发且curve扩大至-3.56%；但当日已跌3.15%、5日跌5.38%，追空的gap风险上升。今晚无夜盘，改为明早反抽失败或二次破位方案。
3. **AL续多失败而非止损成交。** 日高恰为23120，但收23045、低22860，既不能证明09:15后有效突破，也未守23080；LME铝从晨报约3033降至2989.5美元/吨。`COM-M-AL2612-CONTINUATION-LONG-20261020`降级观察；未确认入场，不记止损。
4. **SC由“反手空”转为新的条件多研究。** 昨夜735.6冲击有部分留存，日盘收727.2、较昨夜快照回吐1.14%，但较前结算+1.18%、OI增2,469；19:12 Brent/WTI约111.26/100.54，较晨报109.55/98.54明显上移。旧短`COM-M-SC2612-GAP-FAILURE-SHORT-20261019`继续失效，新多不是自动反手，必须等待今晚留存。
5. **FU旧多不因日盘反弹自动复活。** 旧Night跌至4852已经使前次4880失效条件成立；今日从Night快照反弹2.56%并把curve推至10.33%，说明相对强度仍在。重建需新触发，不能把旧计划当持仓续拿。

## 5. 产业链与传播路径

1. **地缘→Brent/WTI→SC→FU/LU/BU。** 海外油价维持五个月高位附近，SC日盘保留部分昨夜冲击；FU与LU日盘相对Night修复更强，BU亦上涨。SC的期权ATM IV 56.64%仅较RV20高1.56个百分点，RR25为+6.22点，但无bid/ask；高波并不自动便宜。缺Dubai/Oman与HSFO/VLSFO，无法把FU-SC写成可执行裂解价差。置信度：中。
2. **油籽/粕→饲料→养殖。** RM价跌仓增、负curve；LH价跌仓增且curve更负，方向一致但可能分别反映进口粕预期与养殖去产能/交割压力。CBOT豆粕344.3美元/短吨仅context，国内现货与压榨利润缺失。RM局部IV略低于RV，仍因无报价不能买put执行。置信度：中低。
3. **LME铝→沪铝→加工企业。** AL曲线仍正、OI增加，但日盘没有保住昨夜价格，LME铝约2989.5美元/吨亦较晨报弱。Options采样在AL2611而非AL2612，不能跨月给续多第五层。无相关公司映射；股票表达不优于期货。置信度：低。
4. **光伏材料→工业硅/多晶硅→碳酸锂。** SI价弱仓增且curve pair-roll，LC高波反弹但5日仍跌；两个品种不能因同属新能源就视作同一利润链。SI/LC IV均高于各自RV20约2.50/8.72个百分点，无执行报价。置信度：低。
5. **地产/玻璃→黑色。** FG昨夜快照+0.58%后日盘回吐2.08%，OI大增；JM、RB同步偏弱，显示需求端压力线索，但FG spot 956元/吨为C级、无地区品质税费，不能称可套利基差。置信度：中低。

Stock决策贡献为0个候选：股票引擎仅到10月15日，目录内紫金/宝钢与今晚前三主题不匹配；旧半年报只验证条件暴露，不提供今天催化。商品期货更直接、可审计；不把股票当分散化。

## 6. 统一机会榜（最多5项）

| 排名/idea_id | 方向/期限/工具 | 逻辑/赔率/催化/价曲波/拥挤 | 总分 | 五层支持、反证/缺口 | 研究/证据/执行 |
|---|---|---:|---:|---|---|
| 1 `COM-E-SC2612-GEOPOLITICAL-RECLAIM-LONG-20261020` | 条件多，1—3D，SC2612期货；期权仅研究备选 | 20/16/17/13/10 | **76** | 支持1/2/4/5；缺3；反证为日盘较Night回吐、地缘溢价高 | 待验证优势/充分/等21:15、动态参数与实时海外合约 |
| 2 `COM-M-RM701-NIGHT-BREAK-SHORT-20261020` | 条件空，1—3D，RM701期货 | 18/15/13/13/9 | **68** | 支持1/2；5中性；缺3/4 | 待验证优势/部分/等反抽失败或二次破位，不追跌 |
| 3 `COM-E-LH2701-WEAK-CURVE-SHORT-20261013` | 条件空，3—10D，LH2701期货 | 18/14/12/13/10 | **67** | 支持1/2；缺3/4/5；DCE官方核价缺 | 待验证优势/部分/下一日盘等触发与参数 |
| 4 `COM-M-FU2701-HSFO-TIGHTNESS-LONG-20261018` | 重建条件多，1—5D，FU2701期货 | 17/12/11/13/11 | **64** | 支持1/2；4仅油价映射、缺精确HSFO；缺3/5 | 早期优势/部分/旧计划已失效，等新触发 |
| 5 `COM-M-AL2612-CONTINUATION-LONG-20261020` | 观察多，1—5D，AL2612 | 14/10/8/12/10 | **54** | 支持2；1中性、4反对；缺3/5同合约 | 未发现足够优势/不足/不执行 |

证据上限已复核：RM、LH、FU只有两层，总分均≤69；AL只有一层有效支持，总分≤59；SC虽有四层，仍因赔率、参数和报价不足低于80。分项均未超过25/25/20/15/15。

## 7. 三张研究/交易卡

### 卡1｜SC2612条件多｜`COM-E-SC2612-GEOPOLITICAL-RECLAIM-LONG-20261020`

- **事实：** 10月20日OHLC 720/741.6/711.1/727.2，settle727.3；较前结算+1.18%，volume146,437、OI35,749、ΔOI+2,469，near SC2611—next SC2612 curve +0.55%。昨夜供应商快照735.6，较10月19日close+3.08%，日盘较快照-1.14%；snapshot不是官方Night close。19:12 repo Brent/WTI 111.26/100.54美元/桶；Reuters 09:09 UTC Brent 111.48、五个月高位，现货金同时受油价/利率压力。
- **定价/推断：** 市场已计入明显海湾风险溢价，但SC尚未完全跟随海外再冲高；若今晚开盘后仍能站上730且近月结构不弱，国内可能补计价。最强竞争解释是高溢价已被昨夜和日高741.6充分交易，任何缓和消息都可能让SC回到718附近。
- **触发与成交情景：** 21:00首跳不追。21:15后15分钟守住730、SC2611—2612 curve≥0.5%，并核实活跃Brent仍≥110：好成交729—733；中性733—738仅半风险；>740或直接涨停方向跳空为坏成交，放弃。21:30查量仓和海外同向，21:45仍不跌回724才允许确认。
- **风控：** 15分钟收于718下或Brent<108且curve转负，逻辑失效；TP1 746、TP2 760；最迟3个交易日退出。以731入场、718止损为假设，TP1/TP2约1.15R/2.23R，未扣手续费滑点；期货止损不限定最大亏损。
- **参数与压力：** 官方规格1000桶/手、tick0.1元/桶、tick value 100元；名义约72.72万元/手。INE 10月12日起SC2612涨跌停16%、一般保证金18%（名义保证金约13.09万元/手），日内开仓限800手；last trading day 2026-11-30、last delivery 2026-12-07，需提前roll。按727.3估算单个限幅约11.64万元/手，连续两次限幅损失会超过简单止损并随结算基准变化。
- **期权备选：** SC2612、2026-11-12到期，ATM730 IV56.64%、RR25 +6.22、BF25 +0.76；core ATM/skew ready，但surface/positioning/execution均false。只可询价牛市价差，不编腿代码、权利金、Greeks或最大损失；未询价结构不能替代期货限损。

### 卡2｜RM701条件空｜`COM-M-RM701-NIGHT-BREAK-SHORT-20261020`

- **事实：** OHLC2344/2351/2261/2274，settle2299；结算1D-2.17%、5D-3.32%，volume891,955、OI704,711、ΔOI+19,341，RM611—RM701 curve -1.22%。昨夜快照2306，较前收-1.66%，日盘再-1.39%。晨报2295触发线在收盘层面已破，但无分钟路径，成交未知。
- **定价/推断：** 价格与负曲线支持偏空；市场或在交易进口/饲料需求偏弱，但国内压榨利润、库存和A/B basis缺失，不能把因果坐实。竞争解释是三日快速下跌后空头拥挤，今晚任何油籽反弹会造成回补。
- **触发与成交情景：** 首选2290—2310反抽失败后做空；次选21:15后15分钟收于2258下且curve≤-1.2%。好成交2290—2310；中性2255—2270减半；<2235坏成交不追。止损2355；TP1 2230、TP2 2180；最迟3日退出。以2300入场估算风险55点、TP约70/120点，即1.27R/2.18R，未扣成本。
- **参数与压力：** 10吨/手、tick1元/吨、tick value10元；仓库10月20日动态字段margin7%、limit6%，名义约22,740元/手、保证金约1,592元/手。按settle2299，单限幅压力约1,379元/手；连续两日及夜盘gap可超过计划止损。last trading day 2027-01-14、delivery 2027-01-19；21:00—23:00有夜盘。
- **期权：** RM701、2026-12-11，ATM2300 IV17.08% versus RV20 18.98%，RR25 +0.83、BF25 +0.20。局部ATM/skew ready但bid/ask=0、execution=false；“IV低于RV”不单独证明便宜，bear put spread仅待询价。

### 卡3｜LH2701条件空｜`COM-E-LH2701-WEAK-CURVE-SHORT-20261013`

- **事实：** OHLC10215/10280/9985/9995，settle10110；结算1D-2.03%、5D-5.38%，volume170,782、OI207,052、ΔOI+15,474，LH2611—LH2701 curve -3.56%。DCE Night为query_error但LH制度无今晚夜盘，不构成应得会话失败。
- **定价/推断：** 趋势、持仓变化与负曲线支持弱势；但实体猪价、出栏、冻品与交割数据不在统一层，无法判断是持续供给压力还是交割月结构。竞争解释是连续下跌后边际利空已计价，1万元关口附近易出现政策/产业买盘。
- **下一窗口与触发：** 2026-10-21 09:00日盘。09:15后10120—10220反抽失败为好成交；09:30后跌破9950且curve≤-3.5%为中性追随；<9850开盘为坏成交，放弃。失效10320；TP1 9800、TP2 9500；5个交易日退出。无当前minute路径，不认定晨报已成交。
- **参数与压力：** 官方业务细则确认16吨/手、tick5元/吨、tick value80元，合约月倒数第4个交易日为最后交易日；动态margin/limit及LH2701确切最后交易日未在本批元数据确认，执行前必须查交易所/经纪商。DCE官方EOD核对HTTP412，Options全体skipped；因此只研究、不列即时执行。

共同风险预算：每项试仓NAV 0.25%—0.75%，确认0.75%—1.50%；SC/FU/LU/BU同一能源因子合并，RM/LH共享饲料/养殖因子但并非天然对冲；高确信主题总预算≤2.5%—3.0%。压力覆盖1/2涨跌停、相关性断裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、汇率与中国休市海外跳空。

## 8. 商品期权专项

本期Core为`sampled_strikes`而非全链：44/64品种有局部ATM，30有合格skew，完整surface/positioning/execution均为0。quote_coverage_complete只表示计划样本，不表示所有月份和行权价完整。

| series | ATM IV / RV20 | 局部skew | 可研究 | 禁止推断 |
|---|---:|---:|---|---|
| SC2612 2026-11-12 | 56.64% / 55.07% | RR25 +6.22、BF25 +0.76 | 地缘事件凸性、询价价差 | 无bid/ask，不称便宜/可成交，不推dealer方向 |
| RM701 2026-12-11 | 17.08% / 18.98% | RR25 +0.83、BF25 +0.20 | 下行保护/看跌价差询价 | IV-RV不足以证明错价；无净成本 |
| AU2612 2026-11-24 | 19.93% / 14.96% | RR25 +0.49、BF25 +0.77 | 宏观事件vol观察 | 旧EOD IV非今晚报价 |
| SI2612 2026-11-06 | 14.44% / 11.94% | RR25 +0.47、BF25 +0.76 | 局部vol RV | curve roll，不做期限外推 |
| FG701 2026-12-11 | 22.25% / 16.66% | RR25 +5.35、BF25 +1.35 | 事件凸性观察 | 无全链PCR/拥挤度 |
| LC2701 2026-12-07 | 50.19% / 41.47% | skew not ready | 高波事件观察 | 单月不能外推term/wing |

FU期权对应FU2612、AL对应AL2611、AG对应AG2611，均与榜单期货月份不一致，只作背景；LH及其他DCE品种被计划跳过，不等于市场没有期权机会。今晚要做任何期权结构，必须先取得准确腿、同到期bid/ask、净支出、行权交割与最大损失。

## 9. 21:00风险地图

| 层次 | 已知事实 | 对下一窗口的含义 |
|---|---|---|
| 2026-10-20中国EOD | SC+1.18%且OI增，FU从Night快照反弹2.56%；RM/LH收盘破位；AL突破未留存；EC收盘-7.96% | 油链可能高开、粕偏低开；极端品种首跳不追 |
| 已完成历史Night | trading_date=10-20、session=10-19/20；SC735.6、FU4852、RM2306、AL23105；均为vendor snapshot | 只用于Night→Day分解，绝不写成今晚已涨跌 |
| 15:00—19:32海外/事件 | repo 19:12 Brent111.26、WTI100.54、LME铝2989.5、COMEX金4139；Reuters 09:09 UTC Brent111.48 | SC偏高开但地缘溢价高；AL缺海外确认；贵金属偏弱 |
| 尚未发生的T+1 Night | 21:00后归属2026-10-21；SC至02:30、RM至23:00；LH/EC无夜盘 | 21:15看缺口留存，21:30看量仓和精确curve，21:45才升级触发 |

具体情景：SC若高开并在21:15守730且Brent≥110，才考虑条件多；直接冲过740不追。RM若低开<2235不追，优先等2290—2310反抽失败；跌破2258需curve同步。FU须先收复5050并保持curve≥9%，否则只是日盘反弹；旧多不复活。AL需重新站稳23120并由LME铝止跌配合，当前不挂多。LH/EC下一窗口为10月21日09:00，分别等待15/30/45分钟确认，不能在今晚列即时交易。

## 10. 未来24小时/7日事件与行动前清单

- **10月21日22:30 BJT：EIA Weekly Petroleum Status Report。** 官方日程为周三10:30 ET；同时10月21日起调整第三方价格表发布方式。SC/FU/LU/BU为高Delta，高波下优先减线性风险；只有取得报价后才用有限支出期权管理Vega。
- **10月22日20:30 BJT：USDA FAS Weekly Export Sales。** 官方日历列10月22日08:30 ET；影响大豆、豆粕、玉米、棉花，RM/M/Y/C/CF开盘前需重审海外方向。
- **10月24日03:30 BJT：CFTC COT。** CFTC常规周五15:30 ET，数据截至周二；只用于拥挤背景，不把一周滞后持仓当今晚交易流。
- **10月27—28日：FOMC。** Reuters称市场关注指引，油价推升通胀预期；AU/AG、DXY代理和实际利率缺口需外部补核，不能靠当前局部IV下注精确政策路径。
- **持续事件：** Hormuz航运、Houthi/沙特基础设施与俄油政策仍是SC/FU gap源；任何停火/运输恢复可使风险溢价快速坍缩。中国交易所还需关注SC2612 16%限幅/18%一般保证金与800手日内开仓限制。
- **产业/天气/公司：** 国内压榨、猪价、光伏库存和钢材需求没有本批高质量新发布；Stock无截至10月20日新公司披露能力，不把缺数据写成无影响。

行动前必须重核：实时准确合约、21:15/30/45路径、SC/RM近远月同会话报价、DCE官方EOD、动态保证金/限幅、经纪商风控、A/B级basis、期权各腿bid/ask和净成本、海外活跃合约及USD/CNH。输入版本：Global `07b623a`、Commodity `8f05b14`、Stock `79c96a9`。

## 11. 来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/report_input_latest.json)（2026-10-20 19:13 BJT；支持Futures/Market/Physical/External/Night/Options/Metadata）
- [日盘原始快照](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/latest.json)（2026-10-20；支持806合约EOD）
- [Night原始快照](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/night_session/latest.json)（session 2026-10-19/20；vendor snapshot语义）
- [官方价格交叉核对](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/crosschecks/futures_latest.json)（2026-10-20；四所零差异、DCE源错误）
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/options/quality_latest.json)与[局部surface](https://github.com/farfromexact/China-Commodities-Engine/blob/8f05b14f9699b2f649e409d900593ce1b5e9d4d5/data/options/surface_latest.json)（2026-10-20）
- [Reuters：10月20日油价与贵金属](https://www.reuters.com/world/india/gold-slips-investors-weigh-fed-rate-outlook-2026-10-20/)（09:09 UTC；Brent111.48、金4120.49、银57.1931）
- [INE交易时间](https://www.ine.cn/services/calenderandholidays/tradinghours/)（SC Night 21:00—02:30；EC仅日盘）
- [INE：SC2612限幅与保证金调整](https://www.ine.cn/eng/circularnews/circular/202610/t20261009_833652.html)及[开仓限额](https://www.ine.cn/eng/circularnews/circular/202610/t20261009_833650.html)（2026-10-09）
- [CZCE菜粕业务细则](https://www.czce.com.cn/cn/uploadfile/2023/01/10/20230110103802217.pdf)（交易单位、tick、Night）
- [DCE生猪业务细则](https://www.dce.com.cn/dalianshangpin/fgfz/6142914/6142926/6262877/%E5%A4%A7%E8%BF%9E%E5%95%86%E5%93%81%E4%BA%A4%E6%98%93%E6%89%80%E7%94%9F%E7%8C%AA%E6%9C%9F%E8%B4%A7%E4%B8%9A%E5%8A%A1%E7%BB%86%E5%88%99%EF%BC%88%E6%A0%B9%E6%8D%AE2025%E5%B9%B46%E6%9C%8824%E6%97%A5%E3%80%942025%E3%80%9559%E5%8F%B7%E6%96%87%E4%BB%B6%E4%BF%AE%E6%94%B9%EF%BC%89.pdf)（16吨/手、tick5元、交割期限）
- [EIA WPSR与日程](https://www.eia.gov/petroleum/supply/weekly/)（下一发布2026-10-21）
- [USDA FAS Weekly Export Sales](https://www.fas.usda.gov/report-release-announcement/weekly-export-sales-309)（2026-10-22 08:30 ET）
- [CFTC COT发布日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（周五15:30 ET）
- [Stock映射目录](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/config/company_commodity_exposures.json)与[状态](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/last_run_status.json)（最后有效2026-10-15）

A. 今晚没有应立即建立的新仓位。
B. 今晚仅应挂条件的候选：SC2612在21:15后守730且Brent≥110、curve≥0.5%时条件多；RM701只等2290—2310反抽失败或2258下二次确认。
C. 今晚继续观察：LH2701明早反抽/破9950、FU2701新触发、AL2612能否重夺23120、EC2611极端波动后的流动性。
D. 今晚必须回避或有条件退出：追涨油链、追跌EC/RM/LH、无bid/ask的期权结构；若此前已按条件建仓，按各卡失效位和时间退出执行。
