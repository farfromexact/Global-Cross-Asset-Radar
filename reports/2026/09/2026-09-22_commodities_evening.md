# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-22

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：19:48 BJT；信息截点：19:30。今日完整中国EOD为9月22日；今天早前Night Session归属9月22日，今晚21:00尚未开始的连续交易归属9月23日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；BU、EG弱势获外油确认，但深back与超跌令21:00追空赔率差，只等反抽失败。**

当前regime：海湾供应恢复与外交预期继续压缩原油风险溢价；近月产品和化工原料仍呈高back，橡胶、有色和部分内需品种相对强，贵金属受美元及高利率压制。

最接近补证的是BU2611、EG2611反抽失败空和CU2611回撤接受多。BU、EG缺完整执行参数或exact早前Night，CU又处于主力换月期，均不满足立即新仓标准。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻EOD、Market State、Physical、External、Options与合约元数据。

- 统一输入：schema v2，`requested_date=2026-09-22`，19:11:05生成。
- Futures：18:59生成，五所806合约、77产品；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；8条placeholder排除。
- Market State：77产品全部初筛；20个交易日窗口完整，但部分产品存在主力换月或near-next pair变化，相关5D/20D与curve按具体合约使用。
- Physical：19:10生成，18/20序列按原生频率有效，SC/LU不可得；全部basis为C级或缺失，只作context。
- External：19:10生成，17/22有效、5项不可得，全部`context_only`；repo油价连续代理与可核实近月报价冲突，已隔离。
- Options：9月22日尝试采集14,486条原始记录，但module state为`empty`且未发布surface；最新正式研究面仍是9月17日16,016条、216 series、45/64产品，212个surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖为0。
- Metadata：partial；DCE合约元数据获取失败、GFEX source date未验证。整体有效匹配约73%，动态margin/limit覆盖约30%，空参数不推断。

### 今天早前已完成的Night Session

Night原始字段：`trading_date=2026-09-22`、`night_session_date=2026-09-21`，06:01生成，`data_fresh=true`、`validation_passed=true`、`published=true`。取得423个有效合约、37个产品；missing timestamp/price/quote均为0。

但`coverage_complete=false`，存在214个query error和214个unresolved contracts，主要限制DCE及部分非代表月份。该Night只能复盘“昨夜→今日日盘”，**不是今晚21:00行情**。Night大文件经connector只能返回紧凑层，属于读取受限，不是源文件为空；不强拼缺失的exact near-next Night curve。

## 三、商品仪表盘

1D/5D均为同合约结算收益；day follow-through为今日EOD close相对今天早前Night close，仅在exact-contract一致时计算。

| 板块 | 品种/合约；EOD close/settle；1D/5D | Vol/OI/ΔOI；curve | 早前Night close；vs昨收；Day follow-through | Physical/basis | 15:00—19:30海外；Options S/P/E | 21:00信号 |
|---|---|---|---|---|---|---|
| 炼化 | BU2611；5098/5106；-4.24%/-3.28% | 73.61万/26.19万/-23,507；Back 12.89% | BU2610代表价，不可比 | C级/缺仓单 | Brent 98.33；历史Y/Y/N | 反抽失败空，不追低开 |
| 化工 | EG2611；5352/5368；-4.07%/-2.77% | 82.35万/24.74万/+26,808；Back 10.20% | DCE exact缺失 | C级/无仓单 | 外油下跌；当前N/N/N | 等反抽，参数未确认 |
| 原油 | SC2611；724/717.1；-1.87%/-14.24% | 17.69万/4.01万/-842；Back 4.11% | 714.3；-1.13%；Day +1.36% | 实体缺失 | Brent 98.33；历史Y/N/N | 晨空弱化，等新锚 |
| 燃料 | FU2611；4253/4184；-0.99%/-6.65% | 69.43万/19.44万/+7,417；Back 26.48% | 4122；-2.16%；Day +3.18% | C级 | 柴油仍紧；历史Y/N/N | 强反转，禁止追空 |
| 聚酯 | TA701；6274/6262；+0.06%/-2.70% | 112.02万/117.82万/+11,255；Back 3.29% | 6216；-1.05%；Day +0.93% | C级 | 原油弱；历史Y/Y/N | 晨空未延续 |
| 有色 | CU2611；110750/110710；+1.09%/+3.97% | 7.10万/16.01万/+12,859；Back 0.46% | 代表合约CU2610，不可比 | C级；仓单沿用 | LME铜14,793.5，仅context；历史Y/Y/N | 回撤接受多观察 |
| 航运 | EC2610；2265/2199；+1.45%/+6.31% | 1.42万/2.34万/-152；Back 20.35% | 制度上无Night | exact运价缺失 | 航线映射不完整；N/N/N | 明早09:45验证 |
| 橡胶 | BR2611；14900/14890；+0.30%/+1.26% | 18.35万/9.68万/+2,921；Back 0.87% | 14895；+1.29%；Day +0.03% | C级 | 境外映射不足；历史Y/N/N | 夜盘已完成大部分涨幅 |
| 建材 | FG701；932/931；+1.64%/+0.98% | 125.16万/121.39万/-59,006；Back 3.83% | 924；+0.11%；Day +0.87% | C级；仓单当日 | 实体不足；历史Y/Y/N | 反弹减仓，偏噪音 |
| 新能源 | LC2701；134400/133160；+1.59%/+2.72% | 23.87万/42.62万/+84；Back 0.40% | 制度上无Night | C级；仓单stale | 无exact锂映射；当前期权未发布 | 明早验证 |
| 贵金属 | AG2612；15949/16123；-0.76%/+4.29% | 15.87万/23.15万/+6,574；Contango 0.13% | AG2610代表价，不可比 | C级 | 金4327.74、银65.65；历史Y/N/N | 偏低开，不恢复旧多 |
| 油脂 | OI701；10218/10243；+0.56%/+1.41% | 19.97万/28.63万/+1,181；Back 1.49% | 10270；+0.64%；Day -0.51% | C级；仓单1,704、当日0变化 | BMD仅context；N/N/N | 晨多被日盘否定 |

截至约18:27 BJT，Brent 11月合约约98.33美元/桶、跌2%，WTI 10月约93.28、跌2.61%；Saudi East-West Pipeline恢复低速运行并准备恢复Yanbu装船，叠加伊朗可能重开Hormuz的外交预期，继续压缩供应溢价。但Reuters同时指出柴油供应仍紧，限制原油向产品端的一比一传导。[油价与供应](https://www.reuters.com/business/energy/oil-rises-slightly-ahead-potential-us-iran-talks-2026-09-22/)｜[Saudi管道恢复](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)

约18:50 BJT，现货黄金4327.74美元/盎司、白银65.65，分别跌0.4%和0.6%；美元处于七周高位附近、美国10年期收益率约4.969%。这是AG/AU的反对证据，而不是证明期权便宜。[贵金属](https://www.reuters.com/world/india/gold-muted-higher-for-longer-rate-outlook-weighs-2026-09-22/)｜[全球市场与利率](https://www.reuters.com/world/china/global-markets-wrapup-1-2026-09-22/)

## 四、相比今晨及上一晚报真正变化

1. **BU、EG取代SC成为最弱价格异常。** BU结算-4.24%、成交量z=2.57；EG结算-4.07%、成交量z=3.01且价跌仓增。两者分别存在12.89%和10.20%的深back，不能把单日跌幅直接解释成需求崩塌。
2. **SC晨间空头条件被日盘反转削弱。** 早前Night收714.3，今日收724，day follow-through为+1.36%；curve back从昨EOD约1.09%扩至4.11%。晨间入场路径无法由日线验证，状态记“未知且当前锚过期”。
3. **FU、TA同样出现Night弱、日盘回补。** FU day follow-through +3.18%，TA +0.93%；晨间TA空卡的6216锚已失效，不能平移至今晚。
4. **OI晨间多头没有延续。** Night收10270、日盘收10218，day reversal -0.51%，且日低10176穿过原计划止损10180；没有分钟路径，不假设成交，但旧条件明确过期。
5. **EC和LC日盘走强。** EC收盘相对昨结约+4.5%、结算+1.45%，但OI下降；LC结算+1.59%、OI近乎不变。价格层存在，资金身份和实体确认均缺。
6. **期权出现9月22日采集尝试，但没有形成发布面。** 14,486条原始记录不能替代正式surface/readiness；最新可用面仍停留在9月17日。

旧建议台账：`COM-M-SC2611-REVERSAL-20260917`与`COM-E-TA701-COST-UNWIND-20260918`转为“旧锚过期，等待重设”；`COM-M-OI701-TREND-20260922`日盘否定；`COM-M-LUSC-RELATIVE-20260918`夜间比值未强化且日盘两腿均反弹，继续降级。没有成交反馈，不假设真实持仓。

## 五、产业链地图

- **最弱：BU—SC—EG—塑化，偏空但超跌，置信度中。** BU、EG价格层与15:00后外油同向；深back、BU减仓、EG实体和DCE Night缺失构成反证。
- **近月产品仍紧：FU/LU相对原油，置信度中。** FU back升至26.48%、LU约4.79%；FU日盘从Night close反弹3.18%。不再做单向产品空，也不把高back自动解释成无风险多。
- **相对最强：铜—橡胶，置信度中。** CU价涨仓增且轻back；BR/RU/NR早前Night和日盘整体偏强。但CU换月、LME仅context，橡胶实体缺失。
- **航运与新能源事件性偏强，置信度中低。** EC深back和尾盘收盘强于结算，LC价涨；两者无Night，且缺exact运价、库存和可执行期权。
- **农产品、黑色没有三层共振。** OI夜强日弱；M/RM反弹但DCE Night缺失；FG上涨减仓，AP下跌却深back，均不适合趋势追价。

## 六、机会排行榜

| 排名 | 候选/idea_id | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | BU2611反抽失败空 / COM-E-BU2611-FADE-20260922 | 20/13/16/11/9 | **69** | 1、4 | 存在待验证优势｜部分；深back反对｜21:30后待参数 |
| 2 | EG2611反抽失败空 / COM-E-EG2611-FADE-20260922 | 19/14/15/11/9 | **68** | 1、4 | 存在待验证优势｜部分；深back与DCE缺口反对｜待参数 |
| 3 | CU2611回撤接受多 / COM-E-CU2611-PULLBACK-20260922 | 20/14/12/11/10 | **67** | 1、2 | 存在待验证优势｜部分；换月/美元反对｜21:30后 |
| 4 | EC2610深back事件多 / COM-M-EC2610-EVENT-20260920 | 19/14/13/10/9 | **65** | 1、2 | 证据部分、OI反对｜明日09:45 |
| 5 | BR2611相对强势多 / COM-M-BR2611-RELATIVE-STRENGTH-20260922 | 18/13/11/10/10 | **62** | 1、2 | 存在待验证优势｜新增弹性不足｜等回撤 |

分项均已复算并遵守证据层封顶。本期没有70+候选；期货最大损失均不由计划止损限定。

## 七、前三名研究卡

### 1. BU2611｜反抽失败空｜69

事实：今日OHLC 5306/5310/4985/5098，结算5106、1D -4.24%，ΔOI -23,507，成交量z=2.57；curve back 12.89%。BU2610早前Night代表价与BU2611不一致，不能用于overnight/day分解。

市场已计入部分管道恢复和原油下行；我们的分歧是反抽若不能收复5100—5230，炼化成本回落仍可能压制远月。最强反证是深back、柴油紧张和价跌减仓。选择期货方向研究，是因为9月22日期权面未发布、execution-ready=false。

- 好成交：21:30后反抽5150—5230失败并重新跌回5100/VWAP下方；只用1/3风险。
- 中成交：跌破4985后回抽5020—5070失败，半风险。
- 坏成交：直接低于4900、滑点超过计划1R的20%或盘口深度不足，放弃。
- 止损：30分钟接受5310上方。
- 逻辑失效：重上5350、back继续扩大且Brent/柴油同步急升，或管道恢复再次中断。
- TP1 4985或+1.5R；TP2 4800或+3R；1—3D无扩张退出，TP1减半。
- 风险0.15%—0.20% NAV；与SC、EG共享能源因子≤0.50%。
- 参数：repo仅确认最后交易日2026-11-16、最后交割日11月18日；multiplier、tick、margin、limit和夜盘参数未确认。补齐前不可执行，不编造一板/两板金额；压力损失按经纪端当日名义×动态限幅另算。

### 2. EG2611｜反抽失败空｜68

事实：今日OHLC 5539/5539/5275/5352，结算5368、1D -4.07%，ΔOI +26,808，成交量z=3.01、OI z=2.53；curve back 10.20%。DCE早前Night exact缺失。

市场可能正在定价原油和聚酯成本回落；我们的分歧是高成交、价跌仓增可能继续产生趋势，但深back表明近月现货紧张，不能低位追空。

- 好成交：21:30后反抽5400—5480失败并跌回5350/VWAP下方。
- 中成交：跌破5275后回抽5300—5340失败，半风险。
- 坏成交：直接低于5200，或DCE盘口/经纪参数无法确认，放弃。
- 止损：30分钟接受5539上方。
- 失效：重上5580、back升破12%且原油/乙二醇现货同步走强。
- TP1 5275或+1.5R；TP2 5100或+3R；1—3D时间止损。
- 风险0.15% NAV；与BU/SC合并≤0.50%。
- 参数：DCE官方元数据、Night历史和期权均受权限/解析缺口影响；multiplier、tick、margin、limit、last-trading-day均未确认。该卡仅为研究条件，**不是可执行委托**。

### 3. CU2611｜回撤接受多｜67

事实：今日OHLC 110810/111150/110070/110750，结算110710、1D +1.09%、5D +3.97%，ΔOI +12,859，curve back 0.46%。主力由CU2610换至CU2611，早前Night代表合约不可比。

市场可能计入中美事件窗口及有色强势；我们的分歧是价仓与curve若在110200上方保持，趋势仍有延续空间。反证是美元处于七周高位、10年期收益率约4.969%，LME铜19:10附近仅约14,793.5、相对前一结算变化有限。

- 好成交：21:30后回撤110200—110650承接并重上110750/VWAP。
- 中成交：突破111150后回踩110900—111150不破，半风险。
- 坏成交：直接高于112000、跌破109500或换月盘口深度不足，放弃。
- 止损：30分钟接受109500下方。
- 失效：跌破109000、curve转为明显contango且LME同步转弱。
- TP1 112300或+1.5R；TP2 114000或+3R；1—5D无扩张退出。
- 风险0.15%—0.20% NAV；有色共享风险≤0.40%。
- 参数：repo仅确认最后交易日2026-11-16、最后交割日11月18日；其余动态参数未确认。最大损失不由期货结构限定。

## 八、商品期权专项

9月22日原始采集尝试没有形成正式surface；以下仍是9月17日历史截面，底层价格已显著变化，不能用于今晚执行。

| Underlying/expiry | 历史ATM IV；当前RV20 | 历史RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---|---|
| BU2611/10-26 | 44.91% / 33.47% | -2.91/+0.97 | Y/Y/N | 当时underlying settle 5452，已严重失真 |
| SC2611/10-14 | 65.57% / 59.49% | +0.73/+1.41 | Y/N/N | 旧事件vol不可当当前报价 |
| FU2611/10-19 | 60.62% / 44.75% | -0.50/+1.42 | Y/N/N | 深back与产品紧张反对裸空Vega |
| TA701/12-11 | 31.87% / 27.76% | +2.43/+0.72 | Y/Y/N | Delta与净支出须重算 |
| CU2611/10-26 | 14.50% / 15.56% | +3.14/+1.86 | Y/Y/N | IV<RV不单独证明便宜 |
| BR2611/10-26 | 35.44% / 32.38% | +2.09/+1.14 | Y/N/N | positioning不足 |
| AG2612/11-24 | 44.14% / 30.71% | 异常极值 | Y/N/N | skew形状隔离 |

当前没有可证明优于裸期货的期权结构。只有取得实时双边报价后，才比较BU/EG put spread或CU call spread；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点及行权交割全部重算。Dealer Gamma方向未知。

## 九、21:00夜盘风险地图

严格区分：①9月22日完整EOD；②今天早前归属9月22日的Night，仅用于复盘；③15:00—19:30海外新增变化；④今晚21:00尚未发生，归属9月23日。

| 品种 | EOD与早前Night分解 | 15:00后海外 | 21:00倾向 | 首跳 | 等待 | 确认指标 |
|---|---|---|---|---|---:|---|
| BU | 当日-4.24%，exact早前Night不匹配 | Brent跌2%、管道恢复 | 低开风险 | 不追空 | 30—45m | 4985/5100/5230、back |
| EG | 当日-4.07%，DCE Night缺失 | 原油继续弱 | 低开风险 | 不追空 | 30—45m | 5275/5350/5480、OI、curve |
| SC | Night弱、日盘反弹1.36%，back扩大 | Brent 98.33 | 平/低开 | 不追 | 30m | 705/717/724/733、near-next |
| FU/LU | Night弱、日盘明显反转 | 原油弱、柴油紧 | 平开分化 | 不追 | 30m | FU back、LU/SC、成交深度 |
| TA/PX/PF/PR | Night弱、日盘多有回补 | 原油继续跌 | 低/平开 | 不追空 | 30m | TA6180/6262/6346、链内breadth |
| CU/BC | 日盘偏强，CU换月 | LME近乎平、美元强 | 平开分化 | 不追多 | 30m | CU110200/110750、LME、CNH |
| BR/RU/NR | 早前Night上涨，日盘继续偏强或横盘 | 映射不足 | 平/高开 | 不追 | 30m | BR14890/15100、curve |
| AG/AU | 日盘下跌，正式合约Night不可比 | 金银继续跌 | 偏低开 | 不恢复旧多 | 30—45m | AG15888/16123、DXY、10Y |
| M/RM/OI | 日盘偏强，DCE Night缺失/OI日盘反转 | CBOT/BMD仅context | 平开分化 | 不追 | 45m | 量仓、near-next、basis |
| EC/LC | 日盘强、制度无Night | 外盘映射不完整 | 今晚不可交易 | 不适用 | 明日09:45 | EC2199/2265；LC133160 |

不值得交易的噪音：FU以结算计仍跌但从早前Night close反弹3.18%；TA晨弱日强；BR大部分涨幅已在早前Night完成；FG上涨伴大幅减仓。

## 十、未来24小时与7天事件

- 今晚21:00：下一合法连续交易；BU、EG、能源化工均等待30—45分钟，不重复追逐白天跌幅。
- 未来24小时：Saudi East-West Pipeline升负荷、Yanbu恢复装船及Hormuz船流；未经独立确认的停运/重开消息只作gap情景。[Reuters管道](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)
- 9月23日22:30：EIA周报；能源仓提前降低Delta，只在实时双边报价存在时使用有限净支出结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月23—25日：中美领导人会晤窗口；人民币、有色、农产品与战略矿产仅按正式结果调整，不预先赋予方向。[Reuters全球市场](https://www.reuters.com/world/china/global-markets-wrapup-1-2026-09-22/)
- 9月24日前后：USDA出口销售；M、RM、油脂只按实际销售、中国采购和国内basis响应调整。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 9月25日03:30附近：CFTC COT常规窗口，只作滞后拥挤背景。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 未来7日：北美收割天气、马棕出口、交易所动态保证金/限幅，以及SC/LU/FU进入10月移仓风险窗口。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态扩展后77产品；商品期权64产品。
- 实际取数且已分析：五所806合约、77产品全部完成9月22日初筛；20交易日Market State可用；Night取得37产品、423合约。
- 数据不足：214个Night具体合约、DCE Night及元数据、19个期权产品、9月22日正式surface、全部实时bid/ask、SC/LU实体、A/B级basis、exact import parity、加工利润和大部分动态交易参数。
- 不适用/流动性不足：JR、PM、RI、WH、ZC为placeholder；RS历史不足，WR等流动性较低；EC、LC等制度上无Night。
- 黑色建材：FG价涨减仓、AP弱价伴深back，均无三层共振。
- 有色贵金属：CU价仓偏强但换月和美元反对；AG/AU价跌仓增且外盘弱。
- 能源化工：BU、EG入榜；SC/FU/TA晨弱日强，不沿用旧锚；深back普遍限制追空。
- 新能源：LC、PS上涨，但无Night或实体闭环。
- 农产品：M/RM/OI反弹，DCE Night与高质量basis不足。
- 航运软商品：EC深back与收盘强势保留观察，OI下降和exact运价缺失反对立即交易。
- 策略覆盖：方向、curve、跨期、跨品种、跨市场代理、近似中性、波动率/偏度和事件凸性均完成扫描；没有全口径import parity或beta-neutral模型，不伪称套利。
- 风险预算：单笔试仓0.15%—0.25% NAV；得到价格、curve和非价格层确认后才考虑提升至0.75%；能源—化工共享因子≤0.50%，单主题总风险≤2.5%。

固定六路径已提交main并完成回读验证；CI为push后的独立校验，不等待。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：BU2611仅在21:30后反抽5150—5230失败并跌回5100/VWAP下方时研究试空；EG2611仅在反抽5400—5480失败并跌回5350/VWAP下方时研究试空，参数未补齐前均不可执行。  
C. 今晚应继续观察的机会：CU2611回撤接受多、EC2610深back与收盘强势、BR/RU/NR相对强势，以及SC、FU、TA日盘反转能否在新Night延续。  
D. 今晚必须避免或退出的交易：低开追空BU/EG/SC、恢复晨间TA或OI旧条件、追CU/EC第一跳、用BU2610或AG2610代表价替代正式合约、把C级basis或外盘proxy称套利，以及在execution-ready=false时臆测期权成本。