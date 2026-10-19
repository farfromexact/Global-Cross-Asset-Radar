# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-20｜版本：commodities_morning｜信息截点：2026-10-20 07:03 BJT**  
**prompt_version：radar_2026-10-12_stock_v1｜data_protocol_version：china_commodities_core_2026-10-17_v1**

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；昨夜SC急升、FU回落使能源旧观点同时失效，今天只等AL、LH、RM日盘二次确认。**

研究判断分三类：已研究但优势不足——SC/FU追价、AG/AU抄底；机会存在但等条件——AL2612多、LH2701空、RM701空；数据不足不能判断——DCE夜盘与官方交叉核对、实时期权成本、动态保证金/限幅。下一合法窗口为2026-10-20 09:00中国日盘。

## 2. 数据质量与覆盖

本次固定读取Global-Cross-Asset-Radar main ref 7f7488bfe40fcdc0246b870c6a6556c9c78744bc、China-Commodities-Engine main ref c6b740a5eb927588ca4215257eed141abd5fa5c3、China-Stock-Engine main ref 79c96a9d9e73a7c2a13d340229acc7c64f4ec144。统一输入请求日2026-10-19，生成于2026-10-20 06:06:59 BJT。

| 模块 | 日期/范围 | available/published | 分析/执行状态 | 关键缺口 |
|---|---|---|---|---|
| Futures | 2026-10-19；五所806合约、77产品 | 是/核心文件已发布 | 全市场分析就绪；非实时执行 | source-date match 100%，8个零量零仓占位已排除 |
| Market State | 2026-09-14至10-19；77产品 | 是/是 | 分析就绪 | 部分曲线仅1—3个观察或发生pair roll |
| Physical | 目标20、取得18，均标2026-10-19 | 局部可读/否 | 仅逐series背景 | 模块data_fresh=false、validation=false；两项不可得；全为C级spot，无A/B基差 |
| External | 目标22、取得17，2026-10-19 | 是/是 | context-only | DXY、USD/CNH等5项不可得；无独立第二供应商 |
| Night | 交易日2026-10-20；会话2026-10-19晚至20日凌晨 | 是/是 | 供应商快照可分析，不是官方终盘 | 410/806合约、37产品；214 query_error/unresolved，完整率50.87% |
| Options | 2026-10-19；45/64产品、1014合约、45 series | 是/是 | 局部ATM/skew研究可用；执行不可用 | ATM ready 43、skew 30、surface/position/execution均0，bid/ask 0% |
| Metadata | 2026-10-19 | 局部/是 | 仅已核字段可用 | effective match 73.45%；乘数/tick/保证金/限幅仅约30.15%；night字段0% |
| Stock | 最近有效交易日2026-10-15 | 旧值/是 | 背景，不可当前执行 | 5576证券中日价量5565，company evidence eligible仅2；预测与当前交易状态不足 |

Night日历闸门通过：trading_date=2026-10-20、session_start_date=2026-10-19、session_end_date=2026-10-20，calendar_mismatch=false。价格语义为vendor_latest_trade_asof_snapshot；official_night_close_verified=false；OHLC范围为vendor_realtime_unverified_session_scope。因此下文“昨夜快照”均指源时点最新成交，不宣称交易所核验终盘或完整夜盘路径。

官方EOD交叉核对：SHFE 238、INE 63、CZCE 243、GFEX 48个合约配对，settle/close/pre-settle实际差异均为0；DCE官方接口HTTP 412，故总体state=partial。该交叉核对不含volume/OI/turnover，不能替代vendor full_market_ready。

覆盖清单：要求的63代码及LPG引擎别名PG均进入初筛；引擎另含BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态代码。黑色、金属、能源化工、新能源、农产品、软商品和EC均检查EOD/状态；低流动占位JR/PM/RI/WH/ZC不入榜。DCE夜盘缺口限制黑色、油脂、养殖和部分塑化夜间确认，但不抹去其合法日盘研究。

仓库源：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/report_input_latest.json)、[night_session/latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/night_session/latest.json)、[futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/crosschecks/futures_latest.json)。

## 3. 市场仪表盘

EOD为2026-10-19中国日盘；1D close按准确合约，5D为同合约结算收益；Night为上述供应商快照。

| 板块/准确合约 | EOD close / settle | 1D close / 5D settle | Volume / OI / ΔOI | 曲线 | Night latest vs close（源时点） | Options/判断 |
|---|---:|---:|---:|---:|---:|---|
| FU2701 | 4917 / 4957 | +3.08% / +10.85% | 430,966 / 230,998 / +19,931 | 产品curve +8.75%，但pair FU2611-2612 | 4852，-1.32%，ΔOI -6,540（23:00） | FU期权对应FU2612，不可替代；旧多失效 |
| SC2612 | 713.6 / 718.8 | -1.30% / +1.31% | 171,358 / 33,280 / +315 | SC2611-2612 +0.64% | 735.6，+3.08%，ΔOI +2,177（02:30） | ATM720 IV55.10%，无skew/报价；旧空失效 |
| LH2701 | 10215 / 10320 | -2.48% / -5.93% | 143,278 / 191,578 / +9,130 | LH2611-2701 -3.10% | 制度无夜盘 | DCE期权/官方核对缺；空头条件保留 |
| AL2612 | 22970 / 23015 | +0.33% / -1.96% | 151,705 / 221,389 / +9,041 | AL2611-2612 +1.33% | 23105，+0.59%，ΔOI +2,998（00:59:58） | ATM23000 IV11.62%，RR25 -2.07；候选多 |
| RM701 | 2345 / 2350 | 0.00% / -0.76% | 624,165 / 685,370 / -24,893 | RM611-701 -1.45% | 2306，-1.66%，ΔOI -687（23:00） | ATM2350 IV17.11%，RR25 +3.09；候选空但不追 |
| AG2612 | 13999 / 13956 | +0.79% / -6.05% | 318,750 / 279,508 / -3,271 | -0.14%，样本仅2 | 13917，-0.59%，ΔOI +4,442（02:30） | ATM14000 IV35.58%，skew未就绪；多头降级 |
| AU2612 | 902.42 / 901.48 | +0.40% / -0.69% | 222,179 / 222,071 / -885 | -0.15%，样本仅2 | 895.3，-0.79%，ΔOI +3,091（02:30） | ATM904 IV20.23%，RR25 +0.15；不抄底 |
| SA701 | 951 / 953 | +1.17% / -4.22% | 1,047,616 / 1,307,802 / -57,809 | SA610-611 -0.43% | 953，+0.21%，ΔOI +10,056（22:59:59） | ATM950 IV23.99%，RR25 +4.12；方向冲突 |
| SH701 | 1737 / 1722 | +0.12% / -6.51% | 415,124 / 249,927 / +42,834 | SH611-612 +1.47% | 1729，-0.46%，ΔOI +8,389（23:00） | 价仓仅归因线索，未下方向结论 |
| AP701 | 5881 / 5928 | -3.53% / -13.45% | 278,360 / 171,173 / +1,719 | +13.22%，发生pair roll | 无夜盘 | 超跌但曲线不可比，不接刀 |
| I2701 | 682.5 / 682.5 | +1.26% / -0.29% | 344,720 / 606,526 / -33,472 | -0.43%，pair roll | DCE夜盘缺 | 反弹伴OI降，仅观察 |
| LC2701 | 100560 / 99380 | +1.49% / -8.73% | 369,575 / 418,791 / -6,558 | +0.81% | 无夜盘 | RV20 41.16%，超跌波动高，不追 |

## 4. 相比前序的真变化与旧观点处置

1. **能源双向打脸而非新趋势确认。** 昨晚FU2701条件多的失效位为4880，昨夜快照4852，故idea COM-M-FU2701-HSFO-TIGHTNESS-LONG-20261018状态改为invalidated_before_new_entry；无成交反馈，不假设建仓。SC2612条件空失效位724，昨夜快照735.6，故COM-M-SC2612-GAP-FAILURE-SHORT-20261019同样invalidated_before_new_entry。
2. **SC/FU相对变化扩大。** 相对10月19日EOD，SC +3.08%、FU -1.32%，方向差约4.40个百分点；但两个品种交割品质、税制与成本不同，且没有完全对齐的可执行跨品种模型，因此仅作产业链分歧，不称套利。
3. **贵金属日盘修复未获夜间确认。** AG由EOD +0.79%转为Night -0.59%，AU由+0.40%转为-0.79%；外部金价周一约跌0.4%，美元与收益率走强，COM-M-AG2612-OVERSEAS-REPAIR-LONG-20261019降为观察。
4. **AL出现相对干净的连续确认。** AL2612日盘close +0.33%、Night +0.59%，EOD与Night OI均增加；期限正向强度+1.33%。但LME铝只有10月19日3033美元/吨静态context，无07:00增量与A/B基差，证据仍只有价格与期限两层。
5. **RM夜间跌破EOD中性。** RM701日盘close持平，Night快照-1.66%；但Night OI略降而非扩张、25Δ call skew更贵，故只保留破位后的二次确认空，不追第一跳。

## 5. 产业链与传播路径

- **原油—燃料油—沥青：** SC最强、BU次强、FU最弱。海外Brent周一约109.55美元/桶、跌0.3%，活跃WTI约98.54、跌0.5%；中国Night的SC上涨与海外小跌冲突，可能含期限/交割/地缘风险差异。最大缺口是Dubai/Oman和新加坡高硫燃料油准确映射、A/B基差；置信度低。
- **有色：** AL、NI强于CU，AL日盘与Night同向且曲线偏强；NI代表Night合约是NI2611而EOD主力为NI2612，不做跨月正式分解。LME铝/铜/镍只有10月19日EOD context。置信度中低。
- **贵金属：** 中国日盘AG/AU小涨，Night转弱，外部金价受美元和收益率压制。期权局部ATM有效但无报价、无完整曲面；置信度中。
- **油脂油料—饲料—养殖：** RM Night走弱；M、P、OI缺DCE夜盘确认；LH日盘价格下行且OI增加、远月贴水。缺库存/压榨利润的有效变化与DCE官方核对，置信度中低。
- **建材/化工：** SA反弹但5D仍弱，SH价格弱而OI增加，FG曲线pair roll；Physical仅C级spot，不能确认套利。置信度低。

Stock利润桥：Stock引擎只到10月15日且目录合格公司仅紫金矿业、宝钢股份；它们不能验证AL、LH、RM的新增利润传导，也不优于直接期货表达。本期股票候选为0，Stock仅背景，未改变方向或评分。

## 6. 统一机会榜

| 排名 | idea_id / 方向 / 工具 | 逻辑/赔率/催化/价曲波/拥挤 = 总分 | 五层 | 三轴状态 |
|---:|---|---:|---|---|
| 1 | COM-M-AL2612-CONTINUATION-LONG-20261020；条件多；AL2612期货 | 19/15/13/12/9 = **68** | 支持1、2；5中性；3、4缺 | 待验证优势 / 部分 / 等09:15与参数 |
| 2 | COM-E-LH2701-WEAK-CURVE-SHORT-20261013；条件空；LH2701期货 | 17/14/11/13/10 = **65** | 支持1、2；3—5缺 | 待验证优势 / 部分 / 等日盘触发与DCE动态参数 |
| 3 | COM-M-RM701-NIGHT-BREAK-SHORT-20261020；条件空；RM701期货 | 17/13/12/11/10 = **63** | 支持1、2；5反对/中性；3、4缺 | 待验证优势 / 部分 / 等09:15二次确认 |
| 4 | COM-E-AG2612-OVERSEAS-REPAIR-LONG-20261019；观察多；期货优先 | 14/12/10/10/9 = **55** | 2弱支持；1、4反对；5中性 | 优势不足 / 不足 / 不执行 |

分数均服从两层最高69；AL虽有局部期权数据，但put skew较贵只改善潜在表达，不是方向支持。无任何候选达到三层独立支持或70分。

## 7. 研究/交易卡

### 卡1｜AL2612条件多

- 事实：EOD 22970/23015，日close +0.33%；Night快照23105（00:59:58），较前收+0.59%，快照区间22990—23120，ΔOI +2,998；产品curve +1.33%。
- 定价/推断：市场给出连续价格确认，但5D仍-1.96%，更像修复而非已确认趋势。最强竞争解释是短期回补或有色共振，缺实体增量。
- 表达：09:15后连续15分钟守23080并突破23120，且CU不同时跌破Night低位，再试AL2612多；23120—23150为好/中成交，>23200为坏成交并放弃追价。计划止损22940；TP1 23350、TP2 23600；5日时间退出。
- 参数：官方合约规则为5吨/手、tick 5元/吨、tick value 25元；仓库last trading day 2026-12-15。当前动态保证金/限幅及Night交易时间在仓库未核，执行前必须查交易所当日参数。
- 风险：一手按23120名义约115,600元；止损距离180点约900元/手，不含gap与滑点。试仓总计划风险0.25%—0.50% NAV；1/2限幅、流动性消失和保证金上调压力不得由止损替代。
- 放弃：09:15前直接高开>23200；15分钟收在23080下；curve转负；LME铝与中国价格反向扩大。

### 卡2｜LH2701条件空

- 事实：EOD 10215/10320，close -2.48%、5D settlement -5.93%，ΔOI +9,130；LH2611-2701曲线-3.10%。生猪无夜盘，下一窗口09:00。
- 定价/推断：价格弱、OI增与远月贴水共同支持空头，但不能把OI直接等同新空。最强反证是超跌、季节性需求和现货/养殖利润缺失。
- 表达：优先等反弹至10320—10420失败；备选是09:30后跌破10180且曲线仍≤-2.5%。好成交10320—10380反弹失败，中成交10170—10180破位，坏成交<10080不追。计划止损10520；TP1 9950、TP2 9600；5日时间退出。
- 参数：官方标准合约16吨/手、tick 5元/吨、tick value 80元；仓库DCE动态保证金、限幅、last trading day均未核，执行状态因此受限。
- 风险：止损不是最大损失；按破位10180到10520约340点，理论约5,440元/手，未含跳空。仅0.25% NAV试仓，确认仓不超过0.75%。
- 放弃：09:30前快速收复10420；曲线收窄至>-2%；现货/政策出现可验证反向冲击。

### 卡3｜RM701条件空

- 事实：EOD 2345/2350，日close持平、5D -0.76%；Night快照2306（23:00）较前收-1.66%，区间2304—2350，ΔOI -687；curve -1.45%。
- 定价/推断：Night首次给出向下弹性，但OI下降不支持“新增空头”断言；局部期权ATM2350 IV17.11%约等于RV20 17.59%，RR25 +3.09点显示calls更贵，对追空构成反证。
- 表达：09:15后仍低于2310并跌破2295才试空；2295—2305为中成交，反抽2310失败为好成交，<2260为坏成交不追。计划止损2355；TP1 2250、TP2 2200；3日时间退出。
- 参数：仓库核得10吨/手、tick 1元/吨、tick value 10元、基准margin 7%、limit 6%、last trading day 2027-01-14；经纪商/交易所当日动态参数仍需盘前复核。
- 风险：按2300至2355约550元/手，gap和流动性可放大。试仓风险0.25% NAV；RM与M/OI/P的共同油脂因子合并。
- 放弃：09:15收复2330；Night跌幅被完全回补；curve转正；DCE/菜系外盘出现反向确认。

## 8. 商品期权专项

样本为2026-10-19 EOD、core_v1 sampled_strikes，不是全链。45/64产品成功，IV覆盖100%、OI覆盖96.25%，但bid/ask 0%、model Greeks 0%；43个series可用局部ATM，30个可用合格25Δ skew，完整surface、positioning、execution均为0，dealer_gamma_direction_known=false。

- AL2612：2026-11-24 expiry，ATM23000 IV11.62%，RV20 10.96%，IV略高约0.66点；RR25 -2.07、BF25 +0.165。只支持“put侧相对更贵、call结构可能相对便宜”的研究，不足以证明方向或成交成本。
- RM701：2026-12-11 expiry，ATM2350 IV17.11%，RV20 17.59%，RR25 +3.09、BF25 +0.745；call侧更贵反对追空，但没有bid/ask不能构造可执行put spread。
- SC2612：ATM720 IV55.10%，而RV20 55.21%，近似相当；skew未就绪，Night后moneyness已明显变化，10月19日面板不能当今日报价。
- AG2612：ATM14000 IV35.58%高于RV20 31.80%，但Night标的回落且无skew/报价，不做事件凸性买入。

结论：只允许盘前询价后的有限损结构比较；在execution_ready=false时，不写权利金、净支出、Greeks或最大损失。当前线性期货止损也不因此获得合同封顶。

## 9. 09:00开盘风险地图

- **Previous China EOD（10月19日）：** 能源日盘FU强、SC弱；AL/NI小涨；LH/AP弱；贵金属修复。
- **Current T Night（10月19日晚至20日凌晨）：** SC +3.08%、FU -1.32%形成最大分歧；RM -1.66%；AL +0.59%；AG/AU转弱。全部为供应商快照，不是官方终盘。
- **07:00 Overseas：** Brent周一约109.55美元/桶、-0.3%；活跃WTI约98.54、-0.5%；金价约4147.87美元/盎司、-0.4%，美元与美债收益率走强。海外油价小跌与SC Night上涨冲突，贵金属则同向偏弱。

开盘情景：SC倾向高开、FU和RM倾向低开、AL温和高开、AG/AU偏低开。**首跳均不追。** 09:15检查Night缺口留存与价差，09:30检查volume/OI和曲线是否同向，09:45才考虑把试仓从0.25%提高至0.50% NAV。SC若高开后回落至724下，视为Night冲击衰减；若稳在735上也不追，等日盘curve和海外原油再确认。FU低开跌破4880后旧多已经失效，不反手追空。

## 10. 未来24小时/7日事件与行动前核对

- 2026-10-20 09:00 BJT：中国日盘；AL/LH/RM只按卡片二次确认。
- 2026-10-20 21:00 BJT：下一中国夜盘（归属10月21日交易日）；能源、金属和贵金属重新核exact-contract报价。
- 2026-10-21 22:30 BJT附近：EIA Weekly Petroleum Status Report常规窗口，实际日程须以EIA页面最后确认；SC/FU线性Delta应降，期权Vega须先有真实报价。
- 2026-10-22：美国周度失业金及领先指标；通过美元、收益率影响贵金属与有色。
- 2026-10-23 15:45 BJT附近：美国/欧洲PMI窗口；关注需求预期对铜铝、原油与黑色映射。
- 2026-10-24 03:30 BJT：CFTC COT预定发布；属于滞后持仓，不能推dealer gamma或即时资金身份。
- 7日内：中东/霍尔木兹与俄罗斯能源制裁豁免仍是油价gap核心；USDA月度WASDE本周未见新一期，农产品以周度出口、天气和现货为主。

行动前必须重核：准确合约实时价、开盘15/30/45分钟路径、动态保证金和限幅、DCE数据、可用A/B基差、期权bid/ask与净成本、海外同向性、经纪商风控与交割资格。风险预算：试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同一主题合并不超过2.5%—3.0%；SC/FU/BU能源为同因子，AL及相关股票不能假装分散。

旧观点台账：FU2701条件多与SC2612条件空均因Night价格越过失效位而失效；AG2612多降为观察；LH2701空延续但仍未触发；新建AL2612和RM701只作为研究候选，无成交/持仓假定。

## 来源

- [China-Commodities-Engine unified input](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/report_input_latest.json)（2026-10-19/20）
- [China-Commodities-Engine EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/latest.json)（2026-10-19）
- [Night session detail](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/night_session/latest.json)（交易日2026-10-20）
- [Official futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/c6b740a5eb927588ca4215257eed141abd5fa5c3/data/crosschecks/futures_latest.json)（2026-10-19）
- [Reuters：10月19日黄金受美元与收益率压制](https://www.reuters.com/world/india/gold-edges-higher-softer-oil-fed-rate-outlook-focus-2026-10-19/)
- [Reuters：10月19日油价与制裁豁免](https://www.reuters.com/business/energy/oil-slips-trumps-sanction-waiver-may-lead-more-russian-fuel-supplies-2026-10-18/)
- [EIA WPSR日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [CFTC 2026 COT日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- [SHFE铝期货合约](https://www.shfe.com.cn/products/futures/metal/nonferrousmetal/al_f/standard_al_f/202312/t20231205_330052.html)
- [DCE生猪业务细则](https://www.dce.com.cn/dalianshangpin/fgfz/6142914/6142926/6262877/index.html)

## 11. 严格行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：AL2612多、LH2701空、RM701空，均等09:15/09:30二次确认与动态参数。  
C. 今天继续观察：SC/FU能源分歧、AG/AU外盘弱化、SA/SH价仓冲突，以及AP/LC超跌但不接刀。  
D. 今天必须回避或有条件退出：追SC高开、追FU低开、无bid/ask期权；若此前已按条件建仓，FU2701旧多与SC2612旧空已触发失效。