# 商品期货期权晨间雷达｜2026-11-04

> 生成时间：2026-11-04T07:04:45+08:00  
> 信息截点：2026-11-04T07:03:00+08:00  
> edition：commodities_morning｜prompt_version：radar_2026-10-12_stock_v1｜data_protocol：china_commodities_core_2026-10-17_v1

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；最值得验证的是铜三锚再确认、EC实体确认后的反弹空及SC不追空后的反弹失败。**

- **研究机会存在但等待条件/报价**：CU2612、EC2612、SC2612，下一真实窗口均为11月4日09:00；最早在09:15获得第一段确认。
- **已研究但优势不足**：MA701的价格空与backwardation冲突；AG2612旧空触发未满足；SH701只有价格层。
- **数据不足不能判断**：LC/SI/PS的11月3日准确合约、当前全市场1D/5D、当期期权链和多数实体序列。无交易结论不是用来掩盖这些缺口。

## 2. 数据质量、覆盖与事实台账

| 模块 | requested/source/generated | 实际范围与状态 | 对研究/执行的影响 |
|---|---|---|---|
| report_input | 读取`data/report_input_latest.json`，SHA 0afa417 | 0字节，read_state=empty | 不是“市场无数据”；转用模块文件，不自行拼成新批次 |
| Futures | requested 11/3；06:21生成 | 五所均受iFinD 401 device-limit，0条，full_market_ready=false，source_date_match=0，critical=15 | 当前全市场EOD不可执行；沿用合法11/2 last-good（806合约、77品种、五所完整）作初筛 |
| Market State | source 11/2 | 77品种、20会话同合约历史可读 | 只作历史基线；不把1/5日与RV写成11/3新增 |
| Physical | requested 11/3 | 20目标、18原生频率内有效、2不可用；A/B合格基差0，18条均C级 | 可作背景，不能作为方向/套利确认 |
| External | source 11/3；11/4 06:22生成 | 17/22有效，均context_only | 可做海外映射；不可宣称跨境套利 |
| Night | trading_date 11/4；session 11/3→11/4；06:04生成 | 日历标签合法，calendar_mismatch=false；806/806 query_error、0合约、未发布、验证失败 | 仅对重点合约用第三方延迟逐合约回退；不是官方夜盘最终收盘 |
| Options | source 11/2 | 64目标/19成功/430合约；ATM 19、skew 12、surface/positioning/execution均0；bid/ask覆盖0 | 落后11/3应得快照，仅历史背景，不计本期第五层 |
| Metadata | source 11/2 | 806合约；有效匹配73.45%，参数覆盖30.15% | Top3缺失参数由交易所原文补证 |
| Official crosscheck | source 11/3 | 当前vendor基线不可得；DCE HTTP412；未观察到具体价差异；量仓未核 | “未核完”不等于“价格有差异” |
| Stock | last-good 10/30；research_asof 10/31 | 当前刷新失败；仅2个完整公司证据包；限定补证3家公司 | 只做利润桥，证券执行状态未就绪 |

**会话闸门**：2026-11-04是周三，11月3日晚—11月4日凌晨夜盘归属11月4日交易日；标签与[上能中心交易时间](https://www.ine.cn/services/calenderandholidays/tradinghours/)一致。repo Night批次自身不可用，以下“夜盘”均为带具体时间的第三方最新成交快照，`official_night_close_verified=false`，不用于编造完整成交路径。

**覆盖结论**：后台初筛使用11月2日五所77品种，覆盖Prompt 63代码并含BZ/JR/LG/OP/PD/PG/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态品种。11月3日当前全市场批次未取得，因此板块“无异常”只可表述为last-good扫描未见多层共振，不能表述为今天市场不存在机会。

**关键事实台账**：F01—F12见下一表；每个数值均附标的、单位/语义、观测日与来源。读取时间不替代行情观测时间。

## 3. 盘面仪表盘（12项，上限内）

| fact_id | 板块/准确合约 | EOD close/settle | 1D/5D、量仓/RV | 曲线/实体 | Night快照/海外/Options | 信号 |
|---|---|---|---|---|---|---|
| F01 | 能源 SC2612 | 698.2 / 694.9（11/3公开日盘） | 当前全市场1D/5D缺；11/3日盘相对前结算-6.31%；夜盘回退OHLC 686.1/693.8/660/678.8；repo量仓不可用；11/2历史基线；非11/3更新 | SC2701同终点报价未核，正式Night Curve缺失；原油实体未覆盖；无A/B基差 | 678.8；vs close -2.78%，vs settle -2.32%；02:29:59；Brent 103.60、WTI 96.09结算；11/3应得快照缺失 | 只等反弹失败，不追空 |
| F02 | 金属 CU2612 | 106090 / 107230 | 11/3相对前结算-1.39%；1D/5D未刷新；夜盘V 49,909 / OI 190,474；ΔOI不可比；11/2历史基线 | CU2612 106540、CU2701 105850；回退同页价差约0.652%；repo无A/B；紫金Q3经营披露支持铜价利润映射 | 106540；vs close +0.42%，vs settle -0.64%；01:00:06；LME 3M repo连续口径14034；官方口径时点不同；当前快照缺；不可执行 | 三锚未齐，不追 |
| F03 | 贵金属 AG2612 | 11655 / 12013 | 11/3相对前结算-0.84%；1D/5D未刷新；精确ΔOI未核；11/2历史基线 | AG2612 11856、AG2702 11894；约-0.32%轻contango；缺实体 | 11856；vs close +1.73%，vs settle -1.31%；02:30；COMEX silver repo 49.81；旧48.80触发未达；11/3快照缺 | 旧空触发未满足 |
| F04 | 化工 MA701 | 3506 / 3447 | 11/3相对前结算-1.32%；1D/5D未刷新；夜盘V 2,314,024 / OI 891,747；ΔOI不判多空；11/2历史基线 | MA701 3389、MA702 3274；backwardation约3.51%，较日盘3.22%扩大；甲醇实体未形成A/B确认 | 3389；vs close -3.34%，vs settle -1.68%；23:00:07；油价下行；MA last-good series与701不匹配 | 价格空、曲线反对 |
| F05 | 能化 BU2701 | 5044 / 5018 | 11/3相对前结算-4.40%；1D/5D未刷新；夜盘V 239,904 / OI 215,370（22:50快照）；11/2历史基线 | BU2612 5030、BU2701 4916；backwardation约2.32%；无A/B基差 | 4916；vs close -2.54%，vs settle -2.03%；22:50:47；Brent走弱；当期不可用 | 不追空，结构仍紧 |
| F06 | 化工 EB2612 | 10006 / 10024 | 11/3相对前结算-4.53%；1D/5D未刷新；22:11快照V 460,434 / OI 298,399；11/2历史基线 | EB近月backwardation强，终场双腿未核；无A/B确认 | 约9851终场回退；vs close约-1.55%；能源成本下降；当期不可用 | 价格/曲线冲突 |
| F07 | 农产品 OI701 | 10199 / 10181 | 11/3相对前结算-0.36%；1D/5D未刷新；夜盘V 105,306 / OI 339,914；11/2历史基线 | 日盘backwardation约2.74%；夜盘次月未核；基差C级，仅背景 | 10085；vs close -1.12%，vs settle -0.94%；23:00:07；BMD palm 4552背景；11/2 ATM15.54、RR25+1.50，仅旧研究 | 长观察降级 |
| F08 | 航运 EC2612 | 2465 / 结算待回读 | 11/3相对前收约-2.95%；1D/5D未刷新；无夜盘；日盘量仓未获官方交叉核验；11/2历史基线 | EC2701 2684.5；contango 219.5点/约8.9%；SCFIS 11/2周涨4.84%反对，后续报价转弱待确认 | 制度无夜盘；下一窗口09:00；缺同口径实时欧洲运价；不适用 | 只等实体确认后的反弹空 |
| F09 | 氯碱 SH701 | 1491 / 1484 | 11/3日盘+1.08%；1D/5D未刷新；22:03快照V 301,685 / OI 300,909；11/2历史基线 | 远月更强但终场同刻未核；无A/B确认 | 1536；vs close +3.02%，vs settle +3.50%；22:03:11；不适用；当期不可用 | 异常强，但仅1层 |
| F10 | 黑色 I2701 | 日盘精确close/settle当前未取得 | 夜盘约+0.7%（第三方）；量仓当前未核；11/2历史基线 | 未核；港口/仓单当期独立核对不足 | 676.5附近；来源为第三方快照；SGX iron repo 91.15；当期不可用 | 内外轻修复，优势不足 |
| F11 | 油脂 P2701 | 日盘close未回读 / settle 9244 | 夜盘约-1.8%；夜盘V 263,636 / OI 555,369；11/2历史基线 | 未核；BMD palm context_only | 9002；23:00:08；BMD palm 4552；当期不可用 | 油脂偏弱但证据不足 |
| F12 | 新能源 LC/SI/PS | 仅11/2 last-good全市场记录 | 11/3 EOD与夜盘准确合约未取得；未核；LC 11/2基线5D偏弱；非本期新证据 | 未核；仓单/库存当前缺口 | 数据不足，不能判断；映射不完整；当期不可用 | 数据不足，不入榜 |

来源：引擎[last-good futures](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)，以及[SC2612](https://www.iweiai.com/hangqing/sc2612)、[CU2612](https://www.iweiai.com/hangqing/cu2612)、[国内逐合约延迟行情](https://www.9qihuo.com/hangqing)。第三方回退值仅支持“该时点最新成交”，不支持官方结算、最终夜盘OHLC或分钟路径。

**未入榜板块异常/无异常依据**：

- 黑色：I夜盘轻修复，FG/SA偏强；RB/J/JM缺实体和期权确认，没有三层共振。
- 金属：CU的近月结构最有价值；AG相对日收盘反弹，NI/SN偏弱但缺多层。
- 能化：SC/FU/LU/BU/PG/EB/MA普跌，SH逆势强；backwardation使“全链追空”赔率恶化。
- 新能源：LC/SI/PS仅有11月2日基线，11月3日准确合约和仓单不足，明确为数据不足。
- 农产品：油脂偏弱，饲料小跌；C级基差与过期期权不能支持方向。
- 航运：EC期货弱而SCFIS周指数上升，最重要的是内外/期现冲突，不是单边结论。

## 4. 相比前序的真变化

1. 能化从“日盘去溢价”演化为夜盘二次下压：SC2612由日收698.2降至678.8，FU/LU/BU/PG/EB同步走弱；但近月backwardation没有普遍瓦解，故只保留反弹失败空，不做开盘追空。
2. 铜的价格信号由单边弱转为双锚冲突：CU2612较日收+0.42%，但较结算仍-0.64%；2612/2701约0.65%价差支持近月，LME绝对价未回到14200触发。旧CU多头止损107600已在11月3日失效，本期新建子idea，不后移旧止损。
3. AG旧空条件没有满足：夜盘未出现15分钟跌破11620后反抽失败，COMEX也未≤48.80；旧候选由条件空降为观察，不把夜盘OHLC穿越当成交。
4. EC仍是结构性空头候选，但实体反证未消失：期货深contango与弱日盘支持空，最近SCFIS周指数上升反对；必须等09:00后新实体运价确认。
5. Options从“局部研究可用”降为“历史背景”：最新成功批次仍为11月2日，落后于11月3日应得快照，不能作为本期第五层或执行报价。

旧观点处置：SC v2在夜盘曾低于697，但没有发生“反弹699—703失败”的完整顺序，且跌破685禁止追价，故**未触发、未成交、无收益认定**；旧CU多计划的107600止损已被11月3日价格穿越，原方案失效；AG旧空条件不满足；EC稳定idea继续但必须增加实体确认。实际持仓均为未提供/未知。

## 5. 产业链与传播路径（5条）

| 产业链 | 方向/最强最弱 | EOD→Night→海外/实体 | 最大反证或缺失 | 置信度 |
|---|---|---|---|---|
| 原油→燃料油/低硫/沥青/化工 | 空头信息最强但不追 | SC -2.32% vs settle，FU/LU/PG/BU普跌；Brent/WTI收低 | SC/BU/MA近月结构可能或实际backwardation，地缘再升级可瞬间反转 | 中 |
| LME铜→沪铜→铜矿利润 | 修复候选 | CU相对日收盘+0.42%、近月价差约0.65%；紫金Q3铜精矿售价/成本利润桥验证价格敏感性 | 相对结算仍-0.64%，LME repo口径14034未越触发；当期期权缺 | 中低 |
| 白银→沪银 | 旧空降级 | AG仍低于结算、曲线轻contango | 相对日收盘反弹1.73%，COMEX 49.81高于旧空触发48.80 | 低 |
| 欧线运价→EC | 趋势空候选 | EC日盘弱、2612/2701深contango | 最近SCFIS周指数上升，现货与期货背离 | 中低 |
| 棕榈油→国内油脂 | 偏弱观察 | P2701夜盘-1.8%、OI701 -0.94% vs settle | 基差仅C级、跨境品质/汇率/税运费未对齐 | 低 |

**Stock利润桥与表达比较**：

- **紫金矿业（601899.SH）**：公司[2026年三季报](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF)披露1—9月矿产铜81.57万吨；铜精矿销售单价84,545元/吨、单位销售成本25,075元/吨、毛利率70.34%。售价上行可扩大利润，但产量、成本、套保、汇率、少数股东与资本开支决定兑现；这验证铜矿利润暴露，不证明股票会跟随一夜CU。当前证券报价/复权/交易状态陈旧，本期CU期货是更纯表达。
- **中国海油（600938.SH）**：限定检索未取得11月3日经营新增。油价下行通常压低实现价格，但产量、成本、长协、套保和汇率可缓冲；输入不足，不编盈利弹性。若SC条件成立，SC比股票更直接。
- **中远海控（601919.SH）**：11月4日可见证券月报类披露而非经营催化。运价下降向收入传导有滞后，运量、合同价、燃油成本、运力和非欧线业务可抵消；EC更纯，但实体反证使其也尚不可执行。

公司证据只为第三层独立经营验证或表达比较，不增第六层；三家公司均未核当前报价/停牌/流动性，不能称股票即时可执行。

## 6. 统一机会榜（5项，不凑即时交易）

| 排名 | idea_id / 方向 / 期限 | 五层证据（支持｜反对｜缺失） | 逻辑/赔率/催化/市场/技术=总分 | 研究/证据/执行 |
|---|---|---|---|---|
| 1 | COM-M-CU2612-RECLAIM-CURVE-LONG-20261104<br>CU2612三锚再确认多｜多｜1—5D | 2曲线、3实体/公司经营｜1价格双锚冲突、4 LME未重回触发｜5期权当期快照 | 19/17/14/11/8=69 | 重点观察｜2层方向支持｜未就绪 |
| 2 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028<br>EC2612反弹失败空｜空｜3—15D | 1价格、2深contango｜3 SCFIS现货指数周涨｜4海外同口径运价、5期权不适用 | 18/17/14/11/8=68 | 重点观察｜2层方向支持｜未就绪 |
| 3 | COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103<br>SC2612反弹失败空v3｜空｜1—3D | 1价格、4海外原油｜2近月结构未核且可能backwardation、地缘再升级｜3实体库存、5当期期权 | 18/16/14/10/9=67 | 重点观察｜2层方向支持｜未就绪 |
| 4 | COM-M-MA701-ENERGY-DEFLATION-REBOUND-FAILURE-SHORT-20261104<br>MA701油价传导空观察｜空｜1—5D | 1价格、4原油下行｜2近月backwardation扩大｜3实体、5当期期权 | 17/16/13/10/9=65 | 观察｜2层方向支持｜未就绪 |
| 5 | COM-E-AG2612-FAILED-BOUNCE-SHORT-20261103<br>AG2612失败反弹空观察｜空｜1—10D | 2轻contango｜1相对日收盘反弹、4 COMEX高于旧触发｜3实体、5当期期权 | 16/15/12/10/8=61 | 观察｜1层支持｜回避 |

评分是研究优先级，不是胜率。全部候选都低于70，原因是当前全市场EOD、当期期权与部分实体缺失；没有用“0分”掩盖待评分输入，也没有因回退行情而把证据层数抬高。

## 7. 研究/交易卡（3张）

### 7.1 CU2612三锚再确认多｜COM-M-CU2612-RECLAIM-CURVE-LONG-20261104

- **状态修订**：父idea `COM-M-CU2612-INTERNAL-EXTERNAL-CONVERGENCE-LONG-20261103` 的107600止损已被11月3日穿越，原计划失效；本卡是新子idea，不后移旧止损。
- **事实/定价/分歧**：夜盘106540较日收+0.42%，但较结算-0.64%；回退近月价差约0.652%。市场已部分定价近月偏强，但LME repo连续口径14034未越14200。本卡的分歧是：只有内盘价格、近月结构与LME三锚同向，修复才有赔率。
- **触发顺序**：09:15后CU2612连续15分钟≥106600 AND 同时点CU2612-CU2701价差/2701≥0.60% AND LME 3M≥14200；随后回踩106400—106650守住106100才分批30%/30%/40%。
- **入场/退出**：好/中/坏106400/106550/106700；止损105800；TP1 108400，TP2 110000；11月10日14:45时间退出。禁止高于107300追价。
- **成本后净R**：假设每手往返费用+滑点100元（情景、非实报）：good 风险3100元、TP1 3.19R、TP2 5.77R；mid 风险3850元、TP1 2.38R、TP2 4.45R；bad 风险4600元、TP1 1.83R、TP2 3.57R。
- **参数/压力**：[上期所铜规则](https://www.shfe.com.cn/regulation/exchangerules/historicalversion/202508/t20250807_828528.html)：5吨/手，tick 10元/吨=50元/手，12月合约最后交易日11/2元数据为12月15日；当前公告口径限幅9%、一般保证金11%。中性价名义保证金约58,503元/手；1/2个限幅理论压力约47,948/95,895元/手，远大于计划止损风险。
- **风险预算**：试仓0.50% NAV；手数=`floor(0.005×NAV/3,850)`；确认后≤1.0%，铜主题合并≤2.5%。替代表达：紫金矿业利润暴露更慢且公司因子多，本期不优于CU；期权execution_ready=0，不使用。
- **最强竞争解释**：夜盘反弹只是对日盘超跌的技术修复，LME与结算锚仍弱。下一项区分观测就是LME≥14200且回踩不破。

### 7.2 EC2612反弹失败空｜COM-T-EC2612-TREND-CONTANGO-SHORT-20261028

- **新增事实/错价假设**：11月3日EC2612收2465，EC2701收2684.5，contango 219.5点（约8.9%）显示远月溢价；但最近SCFIS周指数上升，说明期货弱势可能提前定价而非实体已转差。
- **触发顺序**：09:00后先反弹2470—2510；随后15分钟收回2460下方 AND 同时点EC2701-EC2612≥150点 AND 最新W46附近40HC报价/权威现货指标不高于前次；再反抽2460失败才分批30%/30%/40%。
- **入场/退出**：好/中/坏2510/2490/2470；止损2565；TP1 2320，TP2 2180；11月20日14:45退出。低于2380禁止追。
- **成本后净R**：假设每手往返费用+滑点250元：good 风险3000元、TP1 3.08R、TP2 5.42R；mid 风险4000元、TP1 2.06R、TP2 3.81R；bad 风险5000元、TP1 1.45R、TP2 2.85R。
- **参数/压力**：[INE EC合约](https://www.ine.cn/products/futures/index_f/)为50元/点，tick 0.5点=25元/手，无夜盘、现金交割、基础限幅10%；当前EC2612公开结算参数约22%保证金须开盘复核。中性价名义保证金约27,390元/手；按入场价估算1/2限幅压力12,450/24,900元/手。
- **风险预算**：试仓0.50% NAV；手数=`floor(0.005×NAV/4,000)`；确认后≤1.0%。替代表达中远海控传导更慢且公司因子更多，当前证券状态未核，不优于EC。
- **最强竞争解释**：高现货指数可能迫使近月修复，深contango未必继续扩大。实体报价不转弱，就不做。

### 7.3 SC2612反弹失败空v3｜COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103

- **状态修订**：11月3日晚v2没有完成“反弹699—703失败”顺序且跌破685进入禁止追价区；v2未触发。本卡只对下一日盘重新定义可达顺序，不回填成交。
- **事实/定价/分歧**：SC2612 678.8，较日收/结算-2.78%/-2.32%；Reuters报道Brent 103.60、WTI 96.09，谈判希望压低风险溢价，但各方仍离协议很远且地缘再升级风险未消失。主要PnL来自反弹失败后的剩余去溢价，而不是从678.8追空。
- **触发顺序**：09:00后先反弹684—690；随后15分钟收于682下方 AND 同时点SC2612-SC2701价差/2701≤1.0% AND Brent≤104.50；再反抽682失败才分批30%/30%/40%。
- **入场/退出**：好/中/坏690/687/684；止损696；TP1 660，TP2 640；11月6日22:45退出；低于670禁止追。
- **成本后净R**：假设每手往返费用+滑点500元：good 风险6500元、TP1 4.54R、TP2 7.62R；mid 风险9500元、TP1 2.79R、TP2 4.89R；bad 风险12500元、TP1 1.88R、TP2 3.48R。
- **参数/压力**：[INE通知](https://www.ine.cn/publicnotice/notice/202610/t20261030_833905.html)自11月3日收盘结算起SC2612限幅18%、一般保证金20%；合约1000桶/手、tick 0.1元/桶=100元/手，夜盘至02:30。中性价名义保证金约137,400元/手；以694.9结算计1/2限幅压力125,082/250,164元/手。
- **风险预算**：试仓0.50% NAV；手数=`floor(0.005×NAV/9,500)`；确认后≤1.0%，SC/BU/LU/FU/化工/中海油同一油价因子合并≤2.5%。期权无当前报价，不能称有限损。
- **最强竞争解释**：地缘消息重新升级会使Brent跳升，且近月backwardation可能吸收抛压。Brent>106.50或曲线>1.5%即放弃。

三张卡的止损均为计划风险，不是合同最大损失；费用/滑点均为压力情景，不是实报。保证金只是资金占用，不是NAV风险预算。

## 8. 商品期权专项

- **样本口径**：11月2日，core_v1 / sampled_strikes，64目标、19成功、430合约；core_atm_ready=19、skew_ready=12、surface=0、positioning=0、execution=0、full_chain_verified=false。
- **局部可读但本期过期**：AP701 ATM IV 34.425 vs RV20 30.657、RR25 -0.17、BF25 0.92；OI701 ATM IV 15.54 vs RV20 11.665、RR25 +1.50、BF25 0.48。它们只说明11月2日局部IV-RV/skew，标的已经历11月3日日盘和夜盘，moneyness/Delta均须重算。
- **不能做的事**：没有两个可比到期，不能外推term；surface_ready=0不能谈完整wing/tail；positioning_ready=0不能谈PCR/拥挤/dealer gamma；bid/ask与execution=0不能给权利金、净成本、Greeks或可成交结构。
- **事件凸性**：EIA、就业/CPI、USDA前可研究有限损结构，但只有取得同一时点bid/ask、IV、到期和行权价后才进入执行候选。当前最优选择是等待报价，不是假定“低IV便宜”。

## 9. 09:00开盘风险地图

| 层 | 已知事实 | 潜在开盘 | 行动 |
|---|---|---|---|
| Previous China EOD | 11/3候选逐合约日盘可读；全市场结构化EOD未刷新 | 能化已在日盘大跌，铜/银弱 | 不把close-settle差写成夜盘新增 |
| Current T Night | 合法归属11/4；repo批次0/806，逐合约回退显示SC/BU/MA/EB弱、CU双锚冲突、SH强 | 能化偏低开，CU平/小高，SH高开风险 | 回退不是官方收盘；首笔不追 |
| 07:00 Overseas | Brent 103.60、WTI 96.09；LME/COMEX仅可比到各自时点 | 原油链低开压力已部分定价；铜/银可能与内盘分化 | 09:15核准确合约与海外锚 |

- **09:00—09:15**：只记录开盘价、准确近远月、量仓是否异常；不执行。
- **09:15**：CU/EC/SC按卡片AND与顺序条件做第一次判定。
- **09:30**：确认回踩/反抽是否发生；OHLC触价不等于顺序完成。
- **09:45**：仍无完整触发则本轮开盘计划过期，转为午后或夜盘重新评估；不能事后把窗口重写成已触发。

## 10. 未来24小时/7日事件与行动前核对

| 北京时间 | 事件 | Delta/Vega与处理 |
|---|---|---|
| 2026-11-04 09:00/09:15/09:30/09:45 | 中国日盘分层确认 | 先核准确合约、近远月和海外锚；15分钟确认前不追首笔跳空。 |
| 2026-11-04 23:30 | EIA周度石油报告 | SC/BU/LU/FU的Delta与Vega风险；数据前总油价主题风险≤1.0% NAV。 |
| 2026-11-06 21:30 | 美国就业报告 | 美元/实际利率影响铜、贵金属；若无可执行期权报价，降低隔夜线性Delta。 |
| 2026-11-07 04:30 | CFTC COT | 仅作下一交易日拥挤度背景，不把持仓变化直接解释为新多新空。 |
| 2026-11-10 21:30 | 美国CPI | 接近7日边界；贵金属/铜事件凸性，报价合格才考虑有限损结构。 |
| 2026-11-10 | USDA作物产量/WASDE；俄乌美阿布扎比会谈开始 | 农产品与能源地缘尾部；分别管理，不能把同一新闻跨层重复计数。 |

**行动前必须再核**：11月3日全市场EOD是否恢复；Top3准确近远月同一时点；SC/CU/EC保证金与限幅；11月3日Options新批次和bid/ask；EC最新实体运价；当前LME/Brent；旧idea状态；Stock证券交易状态。任何一项是关键AND输入而未取得，只隔离对应候选，不删除其余研究。

**发布前实证校验**：五个评分均已按25/25/20/15/15重加总；三张卡好/中/坏边界已按乘数和假设成本重算；触发与失效未同时成立；交易日/夜盘归属已核；MD/JSON使用同一候选对象。未完成的检查包括当前全市场EOD、官方Night最终收盘、当期期权报价和Stock即时交易状态，均未报通过。

## 来源

- [China Commodities Engine root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)｜as of 2026-11-04 06:21 BJT｜支持：11月3日当前刷新五所0条、iFinD 401 device-limit、full_market_ready=false
- [China Commodities Engine last-good futures](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)｜as of 2026-11-02 EOD｜支持：五所806合约、77品种、完整EOD初筛基线
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)｜as of 2026-11-02｜支持：77品种同合约历史、RV和曲线研究基线
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)｜as of requested 2026-11-03｜支持：20目标、18原生频率内有效、2不可用、A/B合格基差0
- [External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)｜as of 2026-11-03 overseas close; generated 2026-11-04 06:22 BJT｜支持：17/22海外序列有效、WTI/Brent/LME/COMEX/农产品背景映射
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)｜as of 2026-11-04 06:04 BJT｜支持：交易日与会话日期合法，但806/806 query_error、0合约、未发布
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)｜as of 2026-11-02｜支持：64目标、19成功、ATM19、skew12、surface/positioning/execution均0
- [Official futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)｜as of 2026-11-03｜支持：当前基线不可得、DCE HTTP412、没有已观察到的具体价差异
- [SC2612 delayed exact-contract snapshot](https://www.iweiai.com/hangqing/sc2612)｜as of 2026-11-04 02:29:59 BJT snapshot｜支持：SC2612 678.8、夜盘OHLC和双锚变化
- [CU2612 delayed exact-contract snapshot](https://www.iweiai.com/hangqing/cu2612)｜as of 2026-11-04 01:00:06 BJT snapshot｜支持：CU2612 106540、夜盘OHLC、量仓
- [Domestic futures delayed quote table](https://www.9qihuo.com/hangqing)｜as of 2026-11-03/04 contract-specific timestamps｜支持：MA701、OI701、P2701及板块夜盘快照
- [INE trading hours](https://www.ine.cn/services/calenderandholidays/tradinghours/)｜as of accessed 2026-11-04｜支持：SC夜盘至02:30、EC无夜盘、日盘09:00开始
- [INE SC margin and limit notice](https://www.ine.cn/publicnotice/notice/202610/t20261030_833905.html)｜as of effective after 2026-11-03 settlement｜支持：SC2612限幅18%、一般保证金20%
- [INE EC contract](https://www.ine.cn/products/futures/index_f/)｜as of contract text published 2026-05-11｜支持：EC乘数50元/点、tick0.5点、限幅10%、最低保证金12%、无夜盘
- [SHFE copper rules](https://www.shfe.com.cn/regulation/exchangerules/historicalversion/202508/t20250807_828528.html)｜as of accessed 2026-11-04｜支持：CU乘数5吨、tick10元/吨、最后交易日规则
- [Reuters oil close and geopolitics](https://www.reuters.com/markets/commodities/oil-rises-after-report-us-strike-irans-qeshm-island-2026-11-03/)｜as of 2026-11-03 US settlement｜支持：Brent 103.60、WTI 96.09、谈判希望与再升级风险并存
- [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)｜as of accessed 2026-11-04｜支持：11月4日23:30 BJT常规周度石油报告窗口
- [CFTC release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)｜as of accessed 2026-11-04｜支持：11月7日04:30 BJT COT发布窗口
- [BLS November 2026 schedule](https://www.bls.gov/schedule/2026/11_sched_list.htm)｜as of accessed 2026-11-04｜支持：11月6日21:30 BJT就业报告、11月10日21:30 CPI
- [USDA release calendar](https://data.nass.usda.gov/Publications/Reports_by_Release_Day/)｜as of accessed 2026-11-04｜支持：11月10日作物产量/WASDE窗口
- [Zijin Mining 2026 Q3 report](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF)｜as of published 2026-10-24｜支持：1—9月矿产铜82万吨、铜矿产品售价/成本/毛利率利润桥
- [China Stock Engine status](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/last_run_status.json)｜as of 2026-11-04 current run / last-good 2026-10-30｜支持：当前刷新失败、last-good 10月30日、执行能力未就绪

## 归档状态

archive_status=success（以本次六路径写后回读为准）；CI validation=pending_or_unverified。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：CU2612三锚再确认多、EC2612实体确认后的反弹空、SC2612反弹失败空；AND/顺序缺一不可。  
C. 今天继续观察：MA701价跌与backwardation冲突、AG2612旧空未触发、SH701逆势强、油脂偏弱及LC/SI/PS数据补齐。  
D. 今天必须回避或有条件退出：禁止追空已大跌能化；旧CU多、SC v2空和AG旧触发不得事后认定成交；无成交回执，不默认持仓。
