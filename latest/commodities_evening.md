# 商品期货期权晚间雷达｜2026-10-21

> **一句话结论（信息截点 2026-10-21 19:30 北京时间）：截至本报告时点，无可立即执行的合格新交易；油链只在 EIA 后确认做多，白银与新能源弱势只等破位，不追首跳。**

本报告仅作研究和决策支持，不构成下单指令，也不假定此前建议已成交或仍持有。今晚 21:00 夜盘归属 2026-10-22 交易日；本文没有使用任何尚未发生的夜盘行情。

## 1. 结论与最有价值的验证

- **研究机会存在、等待条件**：BU2701、SC2612 的外盘油价与国内日盘相对强弱出现可研究分歧，但 22:30 EIA 周报在前，适合等待 22:45 后价格、曲线和外盘三重确认，不在 21:00 首跳追价。
- **已研究但优势不足**：AG2612 的隔夜涨幅被日盘完全回吐，海外白银走弱；方向偏空，但精确到期的期权不可执行，且原油—利率冲击会放大双向波动，只保留破位条件。
- **数据不足不能判断**：期权仅为 sampled-strikes 核心样本，0 个 series 达 execution-ready；Physical 的 20 个目标中 18 个有效，但基差均为 C 级、无 A/B 级。不能把“无即时交易”解释成全市场没有机会。
- **下一窗口**：21:15/21:30 只确认开盘吸收，能源方向的决定性窗口是 EIA 之后 22:45；无夜盘的 GFEX 品种（LC/SI/PS）下一窗口为 10 月 22 日 09:00。

## 2. 数据质量与覆盖

固定读取 ref：Global-Cross-Asset-Radar `23acf93663595c97ac484620fe20a1a0cfe57486`、China-Commodities-Engine `13ed0b5a19422f57bbebaf053dab1a2c8a4be452`、China-Stock-Engine `79c96a9d9e73a7c2a13d340229acc7c64f4ec144`。核心入口为 [report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/13ed0b5a19422f57bbebaf053dab1a2c8a4be452/data/report_input_latest.json)。

| 模块 | 源日/生成 | 实际范围与状态 | 关键限制 |
|---|---|---|---|
| Futures | 10-21 / 19:07 | 806 合约、77 品种、五所、source-date match 100%、full-market-ready；critical/unknown/duplicate/invalid/negative=0 | 5 个 OHLC 占位已隔离 |
| Market State | 截至 10-21 | 20 个可用交易日；准确合约 1/3/5/20D、RV20、量仓、近远月 | roll 标记品种不把拼接收益当真实收益 |
| Physical | 10-21 / 19:14 | 20 目标、18 fresh、2 unavailable | Basis 全为 C 级，0 个可计分；SHFE/DCE/GFEX 仓单本次失败，GFEX carried 数据已 stale |
| External | 10-21 / 19:14 | 22 目标、17 fresh、5 unavailable | 连续/3M 代理且 context-only，不能称跨市套利 |
| Prior Night | trading-date 10-21，session 10-20→10-21 / 06:01 | 414/806 合约、43 产品；validated/published/fresh=true，coverage=51.36% | 214 query-error/unresolved；vendor latest-trade snapshot，非官方夜盘收盘；official-night-close-verified=false |
| Options | 10-21 / 19:07 | core-v1 sampled-strikes；44/64 品种、1014 合约、44 series；ATM-ready 44、skew-ready 33 | surface/positioning/execution-ready 均 0；bid/ask 覆盖 0；full-chain=false；结构化字段与 limitations 文本一处矛盾，以逐 series 字段为准 |
| Metadata | 10-21 | 有效产品匹配 73.45% | multiplier/tick/tick-value/margin/limit 覆盖均约 30.15%；DCE 失败、GFEX 源日未独立验证 |

日历闸门：上一个 Night 的 trading-date=2026-10-21、session-start=2026-10-20，归属合法，`calendar_mismatch=false`；但其 `price_semantics=vendor_latest_trade_asof_snapshot`、`ohlcv_scope=vendor_realtime_unverified_session_scope`，只按时点快照使用，volume/OI/ΔOI 不声称纯夜盘最终值。

官方价格交叉核对 [futures_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/13ed0b5a19422f57bbebaf053dab1a2c8a4be452/data/crosschecks/futures_latest.json)：SHFE 238、INE 63、CZCE 243（close 可比 188）、GFEX 48 个合约，settlement/close/prev-settlement 的真实 difference 均为 0；DCE 官方接口 HTTP 412，故整体 state=partial。该核对不覆盖成交量/OI。

Stock 联动：最新采集因 SSL 握手超时失败，last-valid trade-date=2026-10-15、data-fresh=false、execution-ready=false。现有商品—公司目录只含紫金矿业（金/铜）和宝钢股份（铁矿/钢材）等 4 条映射，无法为当前油链/白银主题提供及时、精确的利润桥，因此本期公司候选为 0；直接商品工具优于陈旧的股票代理。

## 3. 全范围初筛与仪表盘

全量初筛覆盖要求中的 63 个去重代码及引擎实际 77 个品种。实际取得并分析：黑色 9/9、金属 12/12、能源化工 28/28、新能源 3/3、农产品 25/25、航运 1/1（分类有交叉时按交易所产品去重）；期货 EOD 无板块缺失。数据不足集中于 DCE 官方独立核验、2 个 Physical 目标、20 个未成功 Options 产品以及合约参数；不把缺数据品种判为无机会。

| 板块/合约 | T日 close / settle | 1D close / 5D | vol / OI / ΔOI | curve / Physical | 已完成 T 夜快照→日盘 | 外盘/Options/信号 |
|---|---:|---:|---:|---|---|---|
| SC2612 | 716.5 / 700.8 | -1.49% / -6.12% | 271,772 / 35,694 / -55 | +1.21%；实体不足 | 694.8（-4.46% vs prev close）→+3.12% | Brent 110.85；ATM700 IV55.87>RV50.54、RR+4.29；等 EIA |
| BU2701 | 4546 / 4509 | +1.75% / -1.29% | 194,502 / 108,967 / -11,071 | +7.21%；实体不足 | 无可比 exact-contract night 分解 | ATM4500 IV38.77>RV33.33；油链最强 |
| FU2701 | 4815 / 4796 | -2.29% / +0.61% | 933,226 / 227,788 / -9,356 | +12.13% | 4658（-6.39%）→+3.37% | ATM4800 IV58.95>RV48.03；高波动不追 |
| RM701 | 2266 / 2268 | -1.44% / -5.22% | 638,624 / 698,183 / -6,528 | -1.15%；CZCE仓单 6,170、日减100 | 2264（-0.44%）→+0.09% | ATM2275 IV16.41<RV19.34；2258触及但未留在其下 |
| LH2701 | 10145 / 10075 | +0.35% / -4.64% | 227,171 / 199,502 / -7,550 | -5.41%；实体不足 | 无夜盘 | 跌破9950未发生；空头不追 |
| MA701 | 3130 / 3110 | -0.22% / -5.04% | 3,149,160 / 876,148 / +15,374 | +5.86% | 3049（-3.42%）→+2.66% | 期权 underlying=MA612 非同月；前空头条件失效 |
| SA701 | 949 / 952 | +0.32% / -0.21% | 2,295,564 / 1,252,007 / -32,336 | -2.32%；仓单3,464、日增250 | 954（+1.71%）→-0.52% | ATM950 IV22.97>RV15.45；无执行报价 |
| AG2612 | 13874 / 14023 | +0.09% / -2.82% | 596,900 / 182,722 / -1,287 | -0.19% | 14075（+0.77%）→-1.43% | 现货银57.6、-0.7%；AG2611局部IV28.08<RV31.81、非同月 |
| AU2612 | 886.78 / 890.06 | -0.70% / -1.14% | 247,779 / 85,989 / -1,049 | -0.22% | 890.24（-0.20%）→-0.39% | 现货金4127.53，近一周低位；等待 |
| CU2612 | 108780 / 109040 | +0.32% / -1.31% | 169,381 / 135,347 / +6,236 | +0.63% | 109090（+0.24%）→-0.28% | LME铜14304，约较晨值-1.0%；内外冲突 |
| NI2612 | 121300 / 119800 | +3.11% / +0.99% | 372,333 / 182,252 / -2,327 | -0.24% | 上夜 exact 快照缺失 | LME镍15985、约+1.2%；ATM IV18.41≈RV17.21 |
| SI2612 | 8590 / 8650 | -2.05% / -3.62% | 988,061 / 869,154 / +32,260 | -2.66%；GFEX仓单 stale | 无夜盘 | ATM8600 IV14.41>RV12.47；次日09:00看8580 |

未入榜板块：黑色没有三层同向异常，玻璃日盘下跌但纯碱夜→日回吐，产业链分歧；农产品中 RM 弱势但触发后未留存，油脂外盘代理混杂；航运 EC2611 -7.95%、5D -8.48%，curve -11.70%，但缺少可验证运价/事件层与期权保护，不追空；新能源 LC/PS 单日分别 -4.71%/-4.79%，且 LC pair-roll、GFEX实体数据 stale，只作风险提示。

## 4. 相比前序的真变化

1. **SC旧多头已正式失效，转为新条件研究**：昨晚“地缘回踩做多”在晨报已因供应商快照 694.8 跌破失效位取消；今日 SC2612 从该快照回升至716.5，但相对前日 close 仍跌1.49%。这是日盘修复，不是旧观点自动复活。
2. **油链从一致风险溢价变为国内分化**：BU2701 收涨1.75%，SC/FU分别收跌1.49%/2.29%；与此同时 Brent 18:48 BJT 报110.85、日涨1.9%。外强内分化提升相对价值研究价值，也提高 EIA 后跳空风险。
3. **RM空头触发质量下降**：RM701 日内低点2257触及晨报2258条件，但收于2266且夜→日几乎持平；缺分钟成交路径，不认定成交，条件从“可触发”降为“需重新破位并留存”。
4. **MA晨间弱势被日盘吸收**：MA701 从夜快照3049回升至3130（+2.66%），晨间空头逻辑失效；不能把夜间相对结算的大跌继续当新增弱势。
5. **贵金属修复未成立**：AG2612 夜快照14075后日盘收13874，海外银下跌0.7%，晨间白银修复多头撤销；AU也继续偏弱。
6. **Options局部能力改善但仍不可执行**：skew-ready 从前序30升至33个 series；execution-ready 仍为0，不能编权利金、净支出或当前 Greeks。

## 5. 产业链传播图

| 链条 | 强弱与传播 | 曲线/实体/期权 | 最大缺失与置信度 |
|---|---|---|---|
| 原油→SC/FU/BU | Brent/WTI约+1.9%/+2.2%；中国 BU 最强、SC/FU落后 | BU/SC/FU curve +7.21/+1.21/+12.13%；IV均高于RV | EIA尚未发布、Physical不足；中等 |
| 贵金属→AU/AG | 海外金横盘偏弱、银-0.7%；AG夜涨日跌 | AG曲线近乎平；AG期权非同月且不可执行 | 利率/美元实时序列缺、精确腿报价缺；中低 |
| 黑色→玻璃/纯碱 | FG日盘-1.29%，SA+0.32%；上夜方向相反后均回吐 | FG/SA curve均偏反向；CZCE仓单变化分化 | 需求/产销与高质量basis缺；低 |
| 油脂→RM/豆粕/油脂 | RM五日弱，触发未留存；CBOT/SX代理方向混合 | RM IV<RV但不等于便宜；仓单小降 | DCE官方crosscheck失败、压榨利润缺；中低 |
| 新能源→LC/SI/PS | LC/PS大跌、SI弱，OI增加仅为归因线索 | LC pair-roll；GFEX实体stale；期权不可执行 | 无夜盘、仓单和成本核验不足；低 |

公司利润桥未增加证据层：股票引擎停留在10月15日，且目录无油链精确映射；不以“相关概念股”替代商品供需事实，也不把股票价格反应当第六层。

## 6. 统一机会榜（不代表已持有）

| 排名 / idea_id | 方向、期限、工具 | 逻辑/赔率/催化/价曲波/拥挤（总分） | 五层支持；反证/缺失 | 三轴 |
|---|---|---|---|---|
| 1 `COM-E-BU2701-EIA-CONFIRM-LONG-20261021` | 条件多，1–5D；BU2701期货 | 20/17/16/12/9 = **74** | 支持1价格、2曲线、4海外；反证OI下降、IV>RV；实体和执行期权缺 | 判断：待验证优势；证据：充分；执行：等EIA触发 |
| 2 `COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021` | 条件多，1–3D；SC2612期货 | 19/16/15/11/8 = **69** | 支持2曲线、4海外；层1内部修复但close-to-close仍负；实体缺、IV贵 | 判断：待验证；证据：部分；执行：等触发 |
| 3 `COM-M-AG2612-SILVER-REPAIR-LONG-20261021` | **撤销旧多，改为破位空观察**，1–3D | 18/16/14/11/9 = **68** | 支持1夜→日反转、4海外；层5非同月且不可执行；油价/利率可令波动反转 | 判断：方向修订；证据：部分；执行：等破位 |
| 4 `COM-E-SI2612-WEAKNESS-CONTINUATION-SHORT-20261021` | 条件空，1–5D；SI2612期货 | 18/16/14/10/9 = **67** | 支持1价格、2曲线；实体stale、无夜盘、期权不可执行 | 判断：待验证；证据：部分；执行：次日09:00 |
| 5 `COM-E-NI2612-INNER-OUTER-STRENGTH-LONG-20261021` | 条件多，1–5D；NI2612期货 | 17/15/14/10/9 = **65** | 支持1内盘、4LME；OI下降和近月结构反对，实体缺 | 判断：早期线索；证据：部分；执行：等21:30留存 |

风险预算仅为上限：单项试仓 NAV 0.25%–0.75%，确认后0.75%–1.50%；油链同因子总预算不超过2.5%–3.0%，BU与SC不能各自当作独立分散。期货止损是计划风险，不是最大亏损。

## 7. 研究/交易卡

### 卡1｜BU2701 EIA后确认多（74）

- **事实**：T日 close/settle 4546/4509，日涨1.75%，日高4568；curve +7.21%，OI日减11,071。Brent 18:48 BJT 报110.85、涨1.9%。官方合约10吨/手、1元/吨一跳，tick-value 10元；BU2701当前涨跌停12%、一般保证金14%，以4546估算名义45,460元/手、交易所一般保证金约6,364元/手（经纪商可上浮）。
- **定价与推断**：国内沥青相对SC/FU强，可能在预交易成本与供给风险；但OI下降不能解释为“新多”，也可能是回补。错价只在EIA后外盘强势继续、BU守住日高时成立。
- **入场**：22:45后，15分钟收在4568之上且 Brent≥110、curve仍≥6.5%；好成交4568–4590，中4590–4620，坏>4650放弃。分两笔50%/50%。
- **风控**：计划止损4490；TP1 4680、TP2 4800；3个交易日未到TP1退出。每手从4568至4490计划风险约780元，不含跳空/滑点。1个12%限幅约5,455元/手，2个约10,910元/手的线性压力量级。
- **失效/放弃**：EIA后Brent跌破108，BU跌破4490，或curve收窄至<4%；首跳直接>4650不追。最坏情景为EIA反向、夜盘流动性抽离和保证金再上调。

### 卡2｜SC2612 EIA后修复多（69）

- **事实**：前close/settle为727.2/719.7附近，上夜供应商快照694.8（-4.46% vs close，非官方最终夜收）；T日 close/settle 716.5/700.8，故夜快照→日close +3.12%，但T日close-to-close仍-1.49%。curve +1.21%。SC为1000桶/手、0.1元/桶一跳，tick-value 100元；自10月12日SC2612涨跌停16%、一般保证金18%，以716.5估算名义716,500元/手、交易所一般保证金约128,970元/手。
- **定价与推断**：日盘修复说明694.8极端抛压被吸收，但没有证明趋势反转；真正优势要靠EIA后再站回日盘中枢。期权ATM700 IV55.87%高于RV50.54%、RR+4.29，说明上行保护已有溢价，且execution=false，因此期货仅作条件方案。
- **入场**：22:45后先收复722并在15分钟内守住718，且Brent≥110；好718–723，中723–730，坏>735放弃。单手名义大，风险预算反推仓数，不把保证金当最大亏损。
- **风控**：计划止损704；TP1 740、TP2 760；2个交易日未确认退出。以722至704每手计划风险约18,000元；单个16%限幅压力约114,640元/手，两个约229,280元/手。
- **失效/放弃**：跌回700以下、curve转负、Brent<108或EIA显示库存/产品库存明显反向。若今晚直接高开越过735不追。

### 卡3｜AG2612撤销旧多、仅保留破位空（68）

- **事实**：上夜快照14075（+0.77% vs 前close）后，T日close/settle 13874/14023，夜→日-1.43%，日内高14234；COMEX现货银约57.6美元/盎司、日跌0.7%，黄金近一周低位。AG局部期权是AG2611而非AG2612，ATM IV28.08%<RV31.81%、RR-2.98，但10月26日到期且execution=false，不能作当前腿。
- **定价与推断**：隔夜修复被日盘否决、外盘银也偏弱，故晨间修复多头撤销；但油价推升通胀、贵金属避险和利率冲击可相互抵消，只有价格破位才值得做空。
- **入场**：21:30以后仅当AG2612 15分钟收于13820下方且海外银≤57.5；好13800–13820，中13750–13800，坏<13680放弃。分两笔。
- **风控**：计划止损14080；TP1 13550、TP2 13200；3日时间退出。标准合约15千克/手，若按1元/千克一跳则tick-value 15元；动态保证金/限幅在本次元数据中未确认，执行前必须向交易所/经纪商复核。期货止损不封顶跳空损失。
- **失效/放弃**：重新站上14080、海外银重回58.3或美元/实际利率出现反向冲击。EIA前后第一跳不追。

## 8. 商品期权专项

10月21日样本为 `core_v1 / sampled_strikes`，44/64产品、44个ATM-ready、33个skew-ready；完整曲面、全链持仓和执行均未就绪。局部可读不等于可成交：

- 能源：SC2612 ATM700 IV55.87% vs RV50.54%，RR25 +4.29；FU2701 ATM4800 IV58.95% vs RV48.03；BU2701 ATM4500 IV38.77% vs RV33.33。事件前IV均高于RV，只能说保险价格偏高，不能据此单独做空波动。
- 贵金属：AG仅AG2611可比，ATM14000 IV28.08% vs RV31.81%、RR25 -2.98；与AG2612期货不同月且临近到期，不能用于精确对冲/执行。
- 新能源：LC2701 ATM98000 IV51.96% vs RV41.16、PS2612 ATM37500 IV30.99% vs RV17.44；高IV叠加无夜盘与实体缺口，避免裸买追跌或裸卖波动。SI2612 IV14.41% vs RV12.47%，仍无bid/ask。
- 所有结构只允许作为待询价方案；不得编净权利金、最大损失、滑点、dealer gamma或全链PCR。EIA事件如需有限凸性，应另行获得精确expiry/strike双边报价后再评估。

## 9. 21:00夜盘风险地图

| 层次 | 已知事实 | 21:00含义与确认 |
|---|---|---|
| T日EOD | BU强、SC/FU弱；AG夜涨日跌；NI强；RM触发未留存 | 不把相同地缘信息重复计层；国内油链首跳可能补外盘，也可能反映结构差异 |
| 已完成T Night | 合法归属10-21，但为vendor snapshot；SC/FU极弱后日盘修复 | 只作历史弹性，不称今晚已涨跌 |
| 19:30海外 | Brent110.85 +1.9%、WTI99.95 +2.2%；银-0.7%、金近周低位 | BU/SC潜在高开，AG偏低；外盘连续合约只作映射 |
| 未发生的10-22 Night | 21:00开始；22:30 EIA | 21:15看首跳、21:30看量价留存、21:45看曲线；能源最终确认延后至22:45 |

- **潜在高开**：BU/SC/FU，但BU已部分定价且EIA未出，首跳不追。
- **潜在低开**：AG/AU；AG只有跌破13820且外盘银≤57.5才考虑。
- **内外冲突**：CU内盘小涨、LME铜较晨值约-1%；NI内外同强但OI下降，不对资金身份下结论。
- **无夜盘**：LC/SI/PS只在10月22日09:00后按15/30/45分钟确认；EC也不以笼统海外新闻替代精确航运报价。

## 10. 未来24小时/7日事件与行动前检查

- **10月21日22:30 BJT**：EIA Weekly Petroleum Status Report；API线索为原油库存下降490万桶，但EIA才是决定性验证。油链Delta仓延后至22:45；没有execution-ready期权，不虚构Vega结构。
- **10月22日20:30 BJT**：USDA周度出口销售；影响豆类、玉米、小麦与油脂映射，但DCE官方价格交叉核验仍缺。
- **10月24日约03:30 BJT**：CFTC COT；只作持仓背景，不推断国内交易者身份。
- **10月27–28日**：FOMC会议；油价引发通胀预期与实际利率变化，对金银和工业金属的方向可能相反。贵金属仓位在会前缩短持有期。
- **持续7日**：中东船舶/装运风险、炼厂增产响应、俄乌供给；若地缘缓和或运输恢复，油链风险溢价可快速回吐。

行动前必须重新核：精确合约实时双边报价、BU/SC曲线、Brent同窗价格、EIA结果、经纪商保证金/限幅与夜盘时间；期权还需具体expiry/strike双边报价和行权交割规则。Stock当前不执行。输入版本为 `china_commodities_core_2026-10-17_v1`；旧观点处置：SC旧多取消、MA空取消、AG旧多取消，RM/LH均未认定成交。

## 11. 来源

- [China Commodities Engine report input](https://github.com/farfromexact/China-Commodities-Engine/blob/13ed0b5a19422f57bbebaf053dab1a2c8a4be452/data/report_input_latest.json)：10月21日Futures/Market/Physical/External/Night/Options/Metadata。
- [Commodity official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/13ed0b5a19422f57bbebaf053dab1a2c8a4be452/data/crosschecks/futures_latest.json)：SHFE/INE/CZCE/GFEX比较及DCE HTTP 412。
- [Reuters｜Oil prices jump $2](https://www.reuters.com/business/energy/oil-rises-middle-east-supply-worries-2026-10-21/)：10月21日18:48 BJT Brent/WTI与中东供给风险。
- [Reuters｜Gold near one-week low](https://www.reuters.com/world/india/gold-dips-fourth-session-oil-rally-fans-inflation-concerns-2026-10-21/)：10月21日金银、油价与利率背景。
- [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)：10:30 ET发布窗口与周报表。
- [INE｜SC/LU合约限幅与保证金调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833670.html)：10月12日起SC2612/LU2612参数。
- [SHFE｜FU/BU合约限幅与保证金调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833667.html)：10月12日起FU2701/BU2701参数。
- [China Stock Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/latest/research_inputs_latest.json)：Stock能力与时效限制。
- [前序晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/23acf93663595c97ac484620fe20a1a0cfe57486/reports/2026/10/2026-10-21_commodities_morning.md) 与 [前序晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/23acf93663595c97ac484620fe20a1a0cfe57486/reports/2026/10/2026-10-20_commodities_evening.md)：稳定idea_id与旧建议处置。

A. 今晚没有应立即建立的新仓位。  
B. 今晚仅应挂条件的候选：BU2701、SC2612须待22:45 EIA后确认；AG2612仅破13820且海外银≤57.5。  
C. 今晚继续观察：NI2612内外强弱、RM701重新跌破2257的留存、SI2612次日09:00对8580的反应。  
D. 今晚必须回避或有条件退出：回避LC/PS/EC追跌及所有未报价期权；若先前按条件建立MA或AG多头，旧逻辑已失效。
