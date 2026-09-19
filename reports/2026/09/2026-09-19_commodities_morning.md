# 全球商品期货期权高风险机会雷达｜晨间补跑版｜2026-09-19

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际补跑生成：2026-09-19 18:44 BJT；最近完整中国EOD：2026-09-18。**这是延迟补跑，不把已经过去的9:00/09:15/09:30/09:45窗口写成当前可执行建议。**

## 一、今日一句话结论

**休市补跑：当前无可立即执行新仓；周五能源化工急跌后夜盘部分修复，LU/SC相对强、FU深back与JM暴跌最值得周一验证。**

当前regime：**周末价格发现真空 + 原油供应溢价压缩 + 成品油相对偏强 + 焦煤去杠杆 + 贵金属反弹。**  
当前`worth_taking_risk=false`的原因不是“没有研究机会”，而是**中国商品市场已休市、周末地缘与LPR存在gap风险，且商品期权执行层仍不可用**。

## 二、数据质量与覆盖

本次优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)与[历史层](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_history.json)，并核对[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)、[Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)和[Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)。最近的同版晨报与昨晚商品晚报亦用于旧建议台账，而非作为原始行情证据：[前晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-18_commodities_morning.md)、[昨晚晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-18_commodities_evening.md)。

- **Futures / Market State：** 9月18日五所全覆盖，806个具体合约，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0；4条placeholder不用于异常排名。同合约1D/3D/5D/20D历史可用。
- **Physical：** 18/20序列在其原生频率下有效；SC、LU unavailable。现货/基差均为C级或缺地区、品级、税费、交割地等信息，只作context，**不计完整实体层**。
- **External：** repo 17/22可用、5项缺失（Dubai/Oman、Singapore HSFO/VLSFO、USD/CNH、DXY），全部`context_only`。周末无新增主流商品交易收盘，本次用Reuters更新9月18日最终结算和9月19日已发布新闻，不把旧价写成实时。
- **Options：** 最新完整截面仍为9月17日，16,016合约、216 series、45/64产品；IV覆盖99.11%、OI覆盖69.50%、bid/ask覆盖0。root quality明确`surface_ready=false / positioning_ready=false / execution_ready=false`；`surface_latest`为空。因此**本期不生成任何可交易期权结构、精确权利金或Greeks**。即使逐series存在研究性ATM IV/RR/BF，仍不能越过report-level readiness。
- **Night Session：** 状态文件显示423条有效具体合约，165条合法outside-window、4条no-night-trade，214条query_error且214个unresolved；missing timestamp/price/quote均为0，`validation_passed=true / published=true / coverage_complete=false`。
- **日期语义异常：** repo把周五晚至周六凌晨这批记录标为`trading_date=2026-09-19`、`night_session_date=2026-09-18`。但9月19日为周六，交易所[2026休市日历](https://www.shfe.com.cn/services/calenderandholidays/holiday/)显示9月20日亦为周末休市，下一实际日盘是**9月21日09:00**。因此本报**保留原始标签、不静默重写**，仅把exact quote视为已观察到的周五连续交易阶段；不称其为“9月19日交易日”。
- **覆盖核对：** 内部扫描范围仍覆盖SHFE/INE/DCE/CZCE/GFEX全部806具体期货合约及77产品，并保留黑色、有色、能源化工、新能源、农产品与航运板块。DCE在Night与期权层存在系统性缺口，故JM/J/M/EB等不能把“缺Night”误写成“无机会”。

### 五层证据可用性

| 证据层 | 当前状态 | 是否可用于方向评分 |
|---|---|---|
| 1. 价格—成交—持仓 | EOD完整；Night部分完整 | 是；Night仅对exact contract |
| 2. Curve/高质量basis/仓单 | EOD curve可用；basis C/缺；仓单模块partial | curve可用；C级basis不计 |
| 3. 实体供需 | Physical有绝对值但缺高质量方向变化 | 本期多数不计完整层 |
| 4. 境内外定价/宏观 | Reuters/官方源可用，但repo外盘为context_only | 可作宏观/方向证据；不得当exact套利 |
| 5. 商品期权 | 9/17 partial；执行层0 | 仅研究背景，不计执行层 |

## 三、商品仪表盘（展示15项；内部扫描不止这些）

Night `% vs close`是隔夜新增价格信息主指标，`% vs settle`用于判断“真实新增强弱”还是仅修复日盘close/settle偏离。EOD curve均为**near-minus-next期货结构，不是现货基差**。

| 板块 | 品种 | 9/18 EOD | 1D/结构 | 周五连续交易阶段 | 关键信号 |
|---|---|---|---|---|---|
| 原油 | SC2611 | close 728 / settle 754.4 | settle -6.29%；back 1.59%，z -2.49；EOD ΔOI -2,115 | O/H/L/C 739.7/757.2/728.6/734.8；**+0.93% vs close / -2.60% vs settle**；ΔOI -1,246 | 反弹不足以逆转弱势，但也不适合追空 |
| 成品油 | LU2611 | 5440 / 5515 | settle -2.09%；back **4.79%**，z 2.30；EOD ΔOI +1,703 | 5537/5629/5520/5589；**+2.74% / +1.34%**；ΔOI +2,847 | 能源链最强相对腿 |
| 成品油 | FU2611 | 4200 / 4259 | settle -3.29%；back **12.80%**；EOD ΔOI -12,686 | 4267/4333/4260/4297；**+2.31% / +0.89%**；ΔOI +1,597 | 深back + 修复，周一验证 |
| 聚酯 | PX611 | 9160 / 9238 | settle -3.47%；back 0.65% | 9216/9312/9186/9258；+1.07% / +0.22%；ΔOI -2,966 | 修复多于新趋势 |
| 聚酯 | TA701 | 6238 / 6312 | settle -2.86%；back 2.14% | 6280/6332/6256/6304；+1.06% / **-0.13%**；ΔOI -25,427 | Night仍低于settle，偏弱 |
| 芳烃 | EB2611 | 9470 / 9477 | settle约-2.99%；back约4.86% | DCE Night unresolved | 无Night确认，不追空 |
| 黑色 | JM2701 | 1487 / 1527 | close -7.78%；settle -5.30%；back 2.81%；EOD ΔOI -42,633 | DCE Night unresolved | 极端去杠杆；方向未定 |
| 黑色 | J2701 | 1952.5 / 1985.5 | settle -3.85%；curve近中性 | DCE Night unresolved | 弱于钢材但未同JM极端 |
| 贵金属 | AG2612 | 16304 / 16104 | 约+2.79%；curve近中性 | Night代表合约AG2610，**不替代正式合约** | 海外金银强，但正式Night确认不足 |
| 贵金属 | AU2612 | 951.38 / 946.18 | 约+0.96% | Night代表AU2610，不替代 | 观察，不追涨 |
| 有色 | CU2610 | 109620 / 109530 | settle +1.31%；back 0.33%但曲线样本短 | 109840/109950/109620/109900；+0.26%/+0.34%；ΔOI -766 | EOD涨幅基本被维持 |
| 有色 | AL2611 | 24400 / 24385 | settle +0.68%；EOD价格涨/OI增 | 24330/24390/24285/24375；-0.10%/-0.04%；ΔOI +5,296 | Night近乎横盘 |
| 饲料 | M2701 | 3397 / 3429 | settle约-1.47%；contango约1.10% | DCE Night unresolved | 无法确认弱势延续 |
| 建材 | FG701 | 907 / 912 | settle +0.55%；5D -7.32% | 不把未核验Night硬填 | 短期稳、趋势仍弱 |
| 航运 | EC2610 | 2172.5 / 2189 | settle约+2.99%；back约21.29% | 制度无Night | 航运事件风险高，但无exact运价确认 |

## 四、相比上一交易日真正变化

1. **LU/SC相对交易继续获确认，但“更正确”同时意味着“更贵”。** 9/18 EOD结算LU -2.09% vs SC -6.29%；随后exact连续交易LU再跑赢SC约**1.80pp**。LU EOD与Night均增仓，SC均减仓；LU curve 4.79%且z=2.30，SC curve缩至1.59%且z=-2.49。研究证据由“产品强于原油”进一步增强，但周一不应追跳空。
2. **夜盘能源反弹不是一致的新多头趋势。** FU +2.31% vs close但仅+0.89% vs settle；TA +1.06% vs close却-0.13% vs settle；PX +1.07% vs close、+0.22% vs settle。**只有LU对close和settle都表现出较强正弹性**；其余多数更像日盘close相对settle过度下探后的修复。
3. **JM是全市场最显著的去杠杆异常之一。** close相对前结算-7.78%、settle -5.30%、OI单日减42,633，仍处backwardation。价格跌/OI降只能说明去杠杆线索，不能确定“多头止损”或“空头主动”；DCE Night缺口让周一开盘成为第一验证窗口。
4. **贵金属反弹有海外确认，但中国正式合约确认仍不闭环。** Reuters 9/18收盘附近现货金报**$4,390.11/oz，+1.2%**，银**$66.70，+2.3%**；AU/AG中国EOD同向。但Night代表合约与正式AU2612/AG2612不一致，不能跨月替代。
5. **外部原油利空与供应尾部同时存在。** Brent周五结算**$104.87**、WTI **$100.30**，均回落；沙特计划9—10月通过Ras Tanura/Sohar路径增加约6000万桶输出，压低供应溢价。与此同时，Hormuz周四仅4艘可识别商品船通过，低于10日均值约16艘，说明尾部风险未消失。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-fall-1-hopes-limited-supply-disruptions-2026-09-18/) [沙特增运](https://www.reuters.com/business/energy/aramco-boost-exports-strait-hormuz-60-million-bbl-september-october-traders-say-2026-09-18/) [Hormuz船流](https://www.reuters.com/world/middle-east/shipping-traffic-via-strait-hormuz-stays-below-10-day-average-data-shows-2026-09-18/)
6. **期权层比期货层更弱。** 最新链仍停在9/17、45/64产品，bid/ask=0，report-level readiness全为false。9/10新上市的LU期权虽然扩大了工具箱，但本期没有可执行报价，不能用“有品种”代替“可交易”。[LU期权上市通知](https://www.shfe.com.cn/publicnotice/notice/202608/t20260831_833173.html)

## 五、产业链地图

| 产业链 | 方向 | Price/Night | Curve | Physical/海外 | 判断 |
|---|---|---|---|---|---|
| 原油→LU/FU | **原油溢价压缩、产品相对强** | SC大跌；LU/FU Night修复更强 | LU 4.79% back、FU 12.80% back、SC仅1.59% | SC/LU physical缺；海外原油回落但运输仍受限 | **最强研究链：做相对，不追单边** |
| PX→TA→聚酯 | EOD去杠杆、Night部分修复 | PX/TA均约+1.06% vs close | 仍back，但Night curve未核 | physical C/context；原油回落降成本 | 修复证据不够强 |
| JM→J→钢材 | **上游煤最弱** | JM极端跌，J次之，RB/HC跌幅温和 | JM仍back | physical C；DCE Night缺 | 更像链内分化/去杠杆，不是统一需求崩塌 |
| 贵金属/有色 | 相对强 | AU/AG/CU Friday强，CU Night持稳 | 多数curve不强 | 海外金银同向；无exact parity | 两层证据，研究优先但不追 |
| 油脂油料/饲料 | 偏弱但低置信 | M下跌且DCE Night缺 | contango | CBOT仅context，非进口平价 | 等周一数据 |

**最强产业链：低硫/燃料油相对原油。最弱产业链：焦煤—焦炭上游端，尤以JM为代表。**

## 六、机会排行榜（研究吸引力，不是胜率）

评分权重固定为逻辑25、赔率/凸性25、催化20、price/curve/vol15、拥挤/技术15。五层证据上限严格执行。

| # | 机会 | 分数 | 支持层 | 证据 | 执行状态 |
|---|---|---:|---|---|---|
| 1 | **多13 LU2611 / 空1 SC2611近似名义中性** | **80** =22+20+17+13+8 | 1/2/4 | 较强但缺实体/期权 | **周一等待确认** |
| 2 | **FU2611洗盘后反弹延续多** | **74** =20+18+16+12+8 | 1/2/4 | 部分 | 周一等待确认 |
| 3 | AG/AU贵金属延续观察 | 68 | 1/4 | 部分 | 正式Night合约不匹配；期权不可执行 |
| 4 | JM2701极端下跌后的方向选择 | 63 | 1/2 | **方向证据不足** | DCE Night缺；只观察 |
| 5 | TA701/PX611夜盘修复 | 62 | 1/2 | 部分 | 修复多于新趋势 |

### 为什么没有更高分
- Physical/basis没有足够质量，不能靠绝对现货价“补满”第3层。
- Options没有可执行bid/ask，第5层不进入执行判定。
- Night curve没有完整near-next exact pair，不从EOD curve重复创造“第六层”。
- 周末本身使执行状态为休市；高研究分不等于当前可开仓。

## 七、前两名交易卡（不足三项不凑数）

### 1）LU2611 / SC2611：相对价值延续，但等回撤

**事实。** LU EOD close/settle=5440/5515，SC=728/754.4；结算1D分别-2.09%和-6.29%。周五连续交易LU O/H/L/C=5537/5629/5520/5589，`+2.74% vs close / +1.34% vs settle`、ΔOI +2,847；SC=739.7/757.2/728.6/734.8，`+0.93% / -2.60%`、ΔOI -1,246。EOD LU back=4.79%(z2.30)，SC back=1.59%(z-2.49)。

**市场定价。** 市场同时在做两件事：压缩原油供应溢价、保留低硫/产品端相对紧张。Reuters显示Brent/WTI周五下跌，而沙特增加经Sohar转运；但Hormuz航运仍受限。因此第4层支持“产品相对原油”，**不支持构造LU-VLSFO或SC-Brent exact套利**。

**我们的分歧/判断。** 相对价值优于直接赌原油方向；但从Friday EOD simple price ratio `LU/SC=7.47`到连续交易close约`7.61`，优势已经被部分交易。最大反证是：这可能只是日盘close/settle错位与headline timing，而非可持续裂解/产品结构。

**最佳表达。** 多13手LU2611 / 空1手SC2611，按连续交易close估算两腿名义约72.66万 vs 73.48万元，约98.9%匹配。不是Beta-neutral，也不是风险中性。

**下一有效窗口。** **9月21日09:15—09:45**。现在不下单。
- 好成交：09:30后比价回撤仍守约7.50，随后重回7.60，先1/3。
- 中性：直接突破7.65但可回踩7.55—7.60，再考虑。
- 坏成交：开盘>7.80或任一腿相对Friday-night close跳空约2%以上，**不追**。
- 逻辑失效：30分钟接受在7.40下方，或有经核实的新原油供应冲击令SC相对LU单独跑赢>3pp。
- TP1：7.75；TP2：8.00；均为技术/风险预算锚，不是市场报价。
- 时间止损：3个交易日内不扩张即重估。

**合约/保证金。** LU=10吨/手；SC=1000桶/手。9月11日交易所通知显示LU2611/SC2611当前涨跌停16%、一般持仓保证金18%；券商可加收。[INE风险参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260911_833373.html) [SC标准合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)  
以Friday-night close粗算，13LU+1SC交易所保证金约**26.3万元**；若两腿发生极端反向8%/8%分化，压力损失约**11.7万元**；16%/16%反向分化约**23.4万元**。这是压力情景，不是最大损失上限；期货gap和追加保证金风险仍然存在。

### 2）FU2611：洗盘后反弹延续多，只做确认

**事实。** EOD close/settle=4200/4259，settle 1D -3.29%，EOD ΔOI -12,686；near-next back高达12.80%。Friday-night O/H/L/C=4267/4333/4260/4297，`+2.31% vs close / +0.89% vs settle`，ΔOI转+1,597。

**解释竞争。** 主解释是“深back结构下日盘去杠杆过度，Friday-night修复”；竞争解释是“只是在close相对settlement过度偏低后机械回归”，且海外Brent/WTI当日仍下跌。因此不把Night一根OHLC写成“买盘一路进入”。

**下一有效窗口。** 9月21日09:15—09:45：
- 入场：先确认4260上方保持15—30分钟，并重新接受4333；首仓1/3。
- 不追：周一直接高开明显超过4333且无回踩。
- 失效：30分钟接受在4200下方，或backwardation快速压缩而价格不能恢复。
- TP1：4404（前结算锚）；TP2：4520（风险/波动锚，不是实时目标价）。
- 时间止损：2个交易日。

FU标准合约10吨/手、最小跳动1元/吨；9月11日通知当前FU2611涨跌停16%、一般保证金18%。[FU标准合约](https://www.shfe.com.cn/products/futures/energyandchemical/fu_f/standard_fu/202312/t20231205_327331.html) [FU风险参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260911_833382.html)  
以4297估算名义约4.30万元/手、交易所保证金约0.77万元/手；8%/16%单向不利压力约0.34万/0.69万元/手。**期货不是有限损失结构。**

## 八、商品期权专项

当前结论：**期权研究层有信息，执行层不可用。**

- 9/17 chain：16,016 contracts、216 series、45/64 products；IV coverage 99.11%。
- OI coverage 69.50%，不足positioning-ready阈值；bid/ask coverage=0，execution-ready必然失败。
- 全局`surface_ready=false`；`surface_latest`为空。逐series计算出的ATM IV/RR25/BF25只能当历史研究输入，不能写成当前surface。
- `dealer_gamma_direction_known=false`，不推断做市商净Gamma。
- **本期tradeable option structures为空。** 对LU、FU、AG/AU可保留“未来优先研究”身份，但任何Call Spread/Put Spread/Calendar必须等当前bid/ask、underlying、expiry、Delta与成本重新核实。
- 低硫燃料油期权已于9月10日上市，但“上市”与“本次数据可执行”是两件事。[交易所通知](https://www.shfe.com.cn/publicnotice/notice/202608/t20260831_833173.html)

所以，“期权是否优于裸期货”的答案是：**理论上在周末/事件风险下有限风险凸性更合适；数据上暂时无法确认可执行，因此不能替代期货卡。**

## 九、开盘风险地图：本日窗口已过，改列下一实际窗口

9月19日为周六，本次补跑时09:00/09:15/09:30/09:45早已过去，且中国日盘本就休市。交易所日历显示**下一实际日盘为9月21日09:00**；9月25—27日中秋休市，9月24日晚不进行夜盘交易。[2026休市安排](https://www.shfe.com.cn/services/calenderandholidays/holiday/)

| 品种 | Friday EOD | 已观察连续交易 | 周一首跳判断 | 应等多久 | 周一最重要确认 |
|---|---|---|---|---|---|
| LU/SC | LU明显强于SC | 相对优势再扩1.80pp | 容易高开/价差扩张，**不追** | 30—45m | 比价是否守7.50、两腿OI与curve是否继续分化 |
| FU | EOD洗盘、深back | +2.31% vs close | 中性偏强 | 15—30m | 4260是否守住、4333能否接受 |
| JM | -7.78% close shock | DCE Night缺 | 高不确定 | **至少30—45m** | 是缩量反弹还是再放量破1480；OI是否重新扩张 |
| AG/AU | Friday强 | formal contract Night不匹配 | 可能跟随海外金银 | 30m | 现货金银周末后方向+正式合约quote |
| TA/PX | EOD弱 | 约+1.06% vs close | 可能只是修复 | 15—30m | 是否能站上Friday settle，而非只站上close |

## 十、未来24h / 7d事件（北京时间）

- **9月20日（周日）中国LPR复核。** Reuters对21名市场参与者调查均预期1Y/5Y维持3.00%/3.50%；这是调查预期，不是已公布结果。周日中国期货不开市，结果应进入周一gap评估。[Reuters](https://www.reuters.com/world/china/china-set-keep-loan-rates-steady-16th-consecutive-month-september-2026-09-18/)
- **9月21日09:00：下一中国商品日盘。** 周一开盘是本报告所有条件单的第一有效窗口。
- **9月23日22:30：EIA Weekly Petroleum Status Report**（10:30 ET常规发布时间）。能源链在发布前不应放大裸Delta；若使用期权，必须先人工验证bid/ask与最大净支出。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月24日：美中高层/领导人会晤相关消息风险。** 只作为CNH、金属、农产品与能源贸易政策事件窗口，不预设政策方向。[Reuters周度前瞻](https://www.reuters.com/business/take-five/global-markets-themes-graphic-2026-09-18/)
- **9月24日晚无夜盘；9月25—27日中秋休市；9月28恢复。** 这意味着9月24日收盘后海外风险会累积到9月28，持仓需要单独计holiday gap预算。[上期所休市安排](https://www.shfe.com.cn/services/calenderandholidays/holiday/)

## 十一、固定问题快速回答

- **是否值得新增风险：** 现在不值得；周一有两项条件型候选。
- **最强/最弱链：** 最强=LU/FU相对SC；最弱=JM/J上游煤焦。
- **当前regime：** 原油溢价压缩、产品相对紧、煤焦去杠杆、贵金属反弹、周末真空。
- **EOD price获curve确认吗：** LU/SC相对分化获得；FU单边下跌不完全获得；JM崩跌被backwardation部分反证。
- **Night强化/否定/重复：** 强化LU/SC；否定追空FU；TA/PX多为重复close-settle修复；AG/AU正式合约未知。
- **Night vs close/settle最大分歧：** SC +0.93% vs close但-2.60% vs settle；TA +1.06%却-0.13%。说明不能把“Night涨”一律解释为新增强势。
- **Night curve：** exact near-next双腿未完整核实，本期不计算，不制造额外证据层。
- **库存/实体确认：** 不足；SC/LU physical缺，其他basis多为C级context。
- **境内外同向吗：** 原油不同向——海外油价周五下跌，LU/FU连续交易反弹；这支持相对研究，不等于跨市场套利。
- **人民币/美元作用：** repo USD/CNH、DXY缺失，本期不作FX归因。
- **期权优于裸期货吗：** 概念上可能，但当前execution-ready=0，无法给可执行判断。
- **RV：** LU/SC是当前最清晰；其他跨期/跨市场缺exact输入。
- **单日噪音：** TA/PX Night修复、AL Night横盘可能更多是close/settle归一化。
- **应等15/30/45分钟：** FU至少15—30m；LU/SC 30—45m；JM至少30—45m。
- **不值得交易：** 追空JM、周一首跳追LU/SC、无bid/ask期权、基于proxy做exact套利。

## 十二、风险预算

- 单一试仓最大损失：NAV **0.25%—0.75%**。
- 单一确认交易：NAV **0.75%—1.50%**。
- 单一高确信主题总风险：NAV **≤2.5%—3.0%**。
- **LU/SC与FU共享“能源/运输/中东供应”因子，必须合并算风险，不能各给一份预算。**
- 压力测试至少包括：半/一个涨跌停、相关性破裂、流动性消失、周末/夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变、中国休市期间海外大波动。

## 十三、今日行动清单

A. **今天没有应立即建立的新仓位。**  
B. **周一仅挂条件单：LU/SC相对价值与FU2611反弹延续，均须09:15—09:45确认且先核实时价/保证金。**  
C. **继续观察AG/AU、JM冲击后的方向选择、TA/PX修复，以及LPR和周末中东/航运消息。**  
D. **避免追空JM、追高贵金属、使用无bid/ask验证的商品期权、以及把repo连续合约/外盘proxy当作exact套利。**

## 关键来源

- [China-Commodities-Engine unified input](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [Night run status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Core run status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- [Radar latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [SHFE 2026休市安排](https://www.shfe.com.cn/services/calenderandholidays/holiday/)
- [Reuters：9月18日油价与中东供给](https://www.reuters.com/business/energy/oil-prices-fall-1-hopes-limited-supply-disruptions-2026-09-18/)
- [Reuters：沙特经Sohar增运](https://www.reuters.com/business/energy/aramco-boost-exports-strait-hormuz-60-million-bbl-september-october-traders-say-2026-09-18/)
- [Reuters：Hormuz船流](https://www.reuters.com/world/middle-east/shipping-traffic-via-strait-hormuz-stays-below-10-day-average-data-shows-2026-09-18/)
- [Reuters：黄金白银](https://www.reuters.com/business/gold-extends-gains-scale-one-week-high-crude-prices-ease-2026-09-18/)
- [Reuters：中国LPR前瞻](https://www.reuters.com/world/china/china-set-keep-loan-rates-steady-16th-consecutive-month-september-2026-09-18/)
- [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [INE：SC/LU风险参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260911_833373.html)
- [SHFE：FU风险参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260911_833382.html)

> 说明：本报告为研究与交易决策支持，不自动下单；所有“周一条件”均需在下一实际交易窗口重新验证，不得把本次补跑中已经过去的时点当作未来建议。
