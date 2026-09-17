# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-17

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:39 BJT；信息截点：19:30；最近可验证完整中国EOD：9月16日。9月17日五所EOD采集全部失败；今晚21:00连续交易归属9月18日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；五所9月17日EOD均未取得，任何基于昨值的21:00条件单均作废，只保留SC、M与FU/LU的待核实研究问题。**

当前regime：**沙特替代装船和管道修复预期压低原油，但Hormuz船舶通行骤降、成品油仍紧；Fed加息后的美元回吐支撑金银。中国当日日盘不可观测，不能把海外变化倒推为国内已成交方向。**

最接近补充证据的是SC2611反转、M2701相对强势和FU/LU产品紧张，但三者都缺9月17日完整EOD、当日curve与21:00实时盘口。本期正式机会榜为空，不以旧锚凑交易。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并下钻[逐合约last-good EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[唯一scoped状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/scoped/ex-dce/last_run_status.json)及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-16`，9月17日19:02:19生成；它保留的是9月16日五所完整last-good，不是9月17日EOD。
- 9月17日核心Futures：五所均因iFinD HTTP 401 `Device exceed limit`返回0条；`full_market_ready=false`、`source_date_match_pct=0%`、critical errors=15、五所均不fresh。不能用该失败运行建立方向或立即交易。
- Scoped回退：仓库唯一`data/scoped/ex-dce/`停留在2026-08-18且排除DCE，属于真实stale，未拼入本期。
- Last-good Futures/Market State：9月16日806合约、77产品、五所完整，历史1D/3D/5D/20D可作背景；7条placeholder排除。它不能冒充9月17日日盘。
- Physical：9月17日刷新恢复，18/20按日频fresh、0 carried/stale，SC/LU仍unavailable；所有basis均C级，仅作context，不能替代当日期货或计入方向层。
- External：9月17日17/22 fresh、5项unavailable，全部`context_only`。repo WTI 96.04与Reuters近月约101.34显著冲突，隔离repo WTI；repo Brent 103.73与Reuters约104.33接近但仍非exact套利腿。
- Options：最新有效为9月16日18,098条、337 series、52/64产品；330个surface-ready、73个positioning-ready、0个execution-ready，IV/OI/bid-ask覆盖97.92%/67.81%/0。晚间T日新截面未得，旧面只作存量研究。
- Metadata：partial；effective match约73.45%，multiplier/tick/margin/limit约30.15%，last-trading-day约67.49%。

Night状态：`trading_date=2026-09-17`、`night_session_date=2026-09-16`，06:01:11生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。806个请求合约中610条有效、55个产品；189条合法outside-window、7条no-night-trade；missing timestamp/price/quote、query error、unresolved均为0，warnings为空。

这批Night属于**今天已完成的连续交易阶段**，绝不是今晚21:00未来行情。因9月17日EOD缺失，`day_follow_through`全部不可计算，`overnight_day_decomposition_used=false`。

## 三、商品仪表盘

下表EOD均为**9月16日last-good**；1D/5D、成交量、持仓、ΔOI和curve也截至9月16日。早前Night属于9月17日交易日。9月17日日盘close/settle、量仓与curve均缺失，故不推断21:00高低开。S/P/E为9月16日期权readiness。

| 板块/品种 | last-good合约；close/settle；1D/5D | Volume/OI/ΔOI；curve | 9月17 Physical/basis | 早前Night close；vs close；ΔOI | 15:00—19:30海外；S/P/E；21:00 |
|---|---|---|---|---|---|
| 原油SC | SC2611；827/838.4；+0.26%/+22.56% | 24.08万/4.15万/+1,704；back6.32% | 缺失 | 804.8；-2.68%；+2,620 | Brent约104.33；N/N/N；**待EOD** |
| 低硫LU | LU2611；5673/5687；+1.12%/+10.06% | 16.35万/6.92万/+625；back2.81% | 缺失 | 5609；-1.13%；+1,154 | 原油回落/柴油仍紧；无series；待EOD |
| 燃料油FU | FU2611；4488/4493；+0.25%/+14.21% | 99.38万/21.41万/+2,116；back18.14%、z2.11 | spot7525，C | 4405；-1.85%；+83 | 产品紧张；Y/N/N；待EOD |
| 豆粕M | M2701；3479/3434；+1.78%/+1.09% | 171.44万/289.00万/+174,015；contango1.10% | spot3486，C | 3463；-0.46%；-6,556 | CBOT豆1327/粕358；Y/Y/N；待EOD |
| 瓶片PR | PR611；8646/8570；+3.18%/+8.34% | 15.81万/6.91万/+4,770；back2.40%、z1.57 | 缺失 | 8584；-0.72%；-3,009 | 油价回落；Y/Y/N；待EOD |
| 乙二醇EG | EG2610；6147/6161；+3.41%/+6.15% | 262.21万/27.68万/-76,758；back4.50% | 缺失 | 6199；+0.85%；-3,331 | 成本/减仓冲突；Y/Y/N；待EOD |
| 玻璃FG | FG701；910/910；-1.30%/-6.19% | 104.96万/130.57万/+68,443；back3.27% | spot1008，C | 905；-0.55%；+40,308 | 无exact外盘；Y/Y/N；待EOD |
| 焦煤JM | JM2701；1616/1606.5；-0.65%/-3.34% | 63.76万/49.63万/+14,335；back2.15% | spot2441.25，C | 1624；+0.50%；+14,121 | 内需与夜弹冲突；Y/Y/N；待EOD |
| 镍NI | NI2611；122240/122060；-1.78%/-4.33% | 11.10万/12.96万/+6,040；roll/轻contango | 缺失 | 代表NI2610=122430；+0.32%；-5,295 | LME约16345；N/N/N；合约错位 |
| 铜CU | CU2610；107740/107430；+0.47%/-3.32% | 7.99万/16.54万/-14,719；roll/轻back | spot108656.67，C | 107960；+0.20%；-2,822 | LME约14382；N/N/N；待EOD |
| 碳酸锂LC | LC2701；125820/126380；-2.51%/-11.03% | 21.31万/41.75万/-1,204；back0.49% | spot131000，C | 制度无Night | 无exact外盘；Y/N/N；明日待EOD |
| 集运EC | EC2610；2080/2050；-0.89%/+6.11% | 0.93万/2.39万/-482；back28.71% | exact运价缺 | 制度无Night | Hormuz通行骤降但映射不纯；N/N/N |

Reuters 9月17日报道，Brent/WTI一度约104.33/101.34美元/桶，均下跌逾1美元，沙特经Sohar增加装船及East-West管道较快修复预期压低原油；与此同时，柴油市场仍紧。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-extend-losses-fears-middle-east-supply-disruptions-ease-2026-09-17/)

Hormuz周三可识别商业船舶通行降至3艘，前一日为12艘、10日均值17艘；AIS关闭可能导致低估。这是供应右尾风险，不能直接换算成SC或EC当日涨幅。[Reuters航运](https://www.reuters.com/world/middle-east/number-ships-transiting-strait-hormuz-falls-three-wednesday-data-shows-2026-09-17/)

Fed加息后美元先创七周高位再回落，现货金反弹逾1%至约4308.57美元/盎司；这说明信用/地缘需求仍在，但并未消除更高利率反证。[Reuters美元](https://www.reuters.com/world/asia-pacific/hawkish-fed-lifts-dollar-seven-week-high-focus-turn-boj-2026-09-17/)｜[Reuters黄金](https://www.reuters.com/world/india/gold-rises-over-1-investors-digest-fed-hike-oil-rally-stalls-2026-09-17/)

## 四、相比上一交易日/今晨真正变化

1. **最大变化是数据闸门失败，而非可验证的市场反转。** 9月17日五所EOD均为0条、critical errors=15；因此今晨09:30—09:45的SC/M/FG条件结果全部记为未知且窗口已过，不能平移到21:00。
2. **Physical恢复，但不能修复价格层。** 9月17日18/20序列fresh；M现货3486、FU现货7525、TA现货7362.2，但basis均C级且映射到9月16日期货，只作context。
3. **外油继续回落，运输右尾却加剧。** Brent/WTI下跌支持SC反转研究，Hormuz仅3艘可识别通行则是最强竞争解释；两条证据不应相互抵消成“确定方向”。
4. **黄金在Fed后反弹。** 美元从七周高点回落、金价逾1%反弹；黄金信用主题由“否定”改为“冲突”，仍不构成中国AU今晚追多证据。
5. **9月17早前Night仍有效，但无法做Night→Day分解。** SC/FU/LU相对9月16前收分别-2.68%/-1.85%/-1.13%；日盘究竟延续还是反转无可验证数据。
6. **期权没有T日新执行面。** 最新仍是9月16 EOD，且全部execution-ready=false；任何权利金、Delta或最大净支出都须重报价。

旧建议台账：

- `COM-M-SC2611-REVERSAL-20260917`：今晨69分条件空的09:45窗口已过；因T日路径缺失，触发状态未知，今晚转为**未评分研究问题**，不沿用812—825旧入场区。
- `COM-M-M2701-SOYMEAL-FOLLOWTHROUGH-20260916`：今晨65分条件多的09:30窗口已过；触发状态未知，今晚不以3463或3475作当前条件单。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`与`COM-M-LU2611-PRODUCT-RELATIVE-20260915`：旧多继续停止新增；没有T日价曲不能判断恢复。
- `COM-E-FG701-WEAK-CONT-20260914`：今晨低分空卡触发未知且过期；当前Physical只有孤立现货，仍不追空。
- `COM-C-PR611-POLYESTER-PASS-20260916`：继续观察；缺T日价格、量仓和加工利润，不恢复条件多。

没有成交反馈，不假设用户持仓；OHLC和旧触发区触及也不等于真实成交。

## 五、产业链地图

- **能源SC—FU—LU：方向冲突，置信度低。** 早前Night与海外油价偏弱，支持反转；9月16深back、柴油紧张和Hormuz通行锐减反对追空。缺9月17中国EOD、SC/LU实体及exact产品映射。
- **农产品M—RM：相对最值得补证，置信度中低。** 9月16M价涨仓增、9月17现货3486及CBOT豆/粕高位提供研究线索；早前Night减仓回吐、contango和T日EOD缺失反对下单。
- **聚酯PR—PX—TA—EG：旧强势能否延续未知。** 9月16PR/PX/TA偏强，早前Night仅EG延续；原油回落可能缓解成本，也可能挤压库存价值。缺T日加工利润、订单与价格路径。
- **最弱背景：FG—SA—LC。** 9月16趋势偏弱，但FG仍back、LC减仓下跌；9月17价格缺失使“继续弱”无法验证，禁止用C级现货代替。
- **贵金属与有色：海外修复、国内未知。** LME和金银反弹、美元回落；中国AU/AG Night代表合约错位且T日EOD缺失，黄金信用主题维持冲突判断。

## 六、机会排行榜

**正式排行榜为空。** 核心9月17价格—成交—持仓与curve缺失，使“价格/曲线/波动率”分项及总分无法可靠评定；不以0、null或旧分数冒充新评分。

研究观察池（不进入正式榜）：

| 优先级 | idea_id / 问题 | 五层状态 | 研究判断｜证据｜执行 |
|---|---|---|---|
| 1 | `COM-M-SC2611-REVERSAL-20260917`：原油反转是否延续 | 1缺T日；2旧back反对；3缺；4外油支持、航运反对；5缺 | 存在待验证优势｜不足｜待T日EOD与实时报价 |
| 2 | `COM-M-M2701-SOYMEAL-FOLLOWTHROUGH-20260916`：豆粕能否恢复强势 | 1缺T日；2旧contango反对；3C级context；4CBOT支持；5研究面可用、执行缺 | 证据不足｜不足｜待T日EOD/量仓 |
| 3 | FU2611/LU2611产品紧张是否重新战胜原油回落 | 1缺T日；2旧back支持；3LU缺；4柴油支持、原油反对；5FU凸性贵且不可执行 | 证据不足｜部分但冲突｜待exact报价与curve |

## 七、研究卡（非正式交易卡）

### 1. SC2611｜反转研究｜待评

**事实：** 最近可验证EOD为9月16日close/settlement=827/838.4；早前Night OHLC=829.9/832.3/788.1/804.8，vs close -2.68%、vs settlement -4.01%、ΔOI +2,620；9月17 EOD缺失。海外Brent约104.33、WTI约101.34，但Hormuz通行锐减。

- 市场隐含：替代装船和管道修复压缩极端短缺溢价。
- 分歧：原油可以继续去溢价，但航道风险和产品紧张使追空赔率不稳。
- 最佳表达：暂不表达；SC2611线性仓最大损失不受止损结构限定，SC期权面缺失。
- 入场：**无有效数值入场**。必须先在经纪端确认9月17 close/settlement、SC2610—2611 curve、21:00实时盘口；21:45后只有反抽失败且跌回当晚VWAP下方才可重新立项。
- 好/中/坏：好=回抽T日settle失败且Brent同步弱；中=窄幅围绕T日settle，继续等；坏=直接跳空或Brent重上108，放弃。
- 失效：Hormuz/Yanbu重新恶化、back重扩且Brent>108；价格阈值待T日EOD补齐。
- 退出：若未来成立，1—2D时间止损，TP按实时1.5R/3R；本期不发布伪精确目标。
- 参数：1,000桶/手、tick 0.1元/桶、tick value 100元；最后交易日10月30日、实物交割。动态margin/limit未确认，不编一板/两板金额。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)

### 2. M2701｜相对强势研究｜待评

**事实：** 最近可验证EOD为9月16日close/settlement=3479/3434、ΔOI +174,015、contango1.10%；早前Night收3463、vs close -0.46%、ΔOI -6,556；9月17日现货3486为C级context，T日EOD缺失。

- 市场隐含：9月16日已重价采购/成本预期；早前Night未延续。
- 分歧：现货与CBOT豆/粕高位可能保留强势，但没有T日量仓无法辨别延续或兑现。
- 最佳表达：暂不表达；不以CBOT代理构造exact进口套利。
- 入场：**无有效数值入场**。先确认9月17 EOD、M2701当日ΔOI、near-next与21:00盘口；21:30后只有回撤被T日settle/VWAP共同接受才重新评分。
- 好/中/坏：好=量仓恢复且守T日settle；中=价格强、OI继续降，继续观察；坏=跌破T日日低或CBOT豆跌破1300，放弃。
- 失效/退出：具体失效价、TP与压力损失待T日数据和DCE参数补齐；研究期限1—3D。
- DCE参数端点仍不完整；multiplier、tick、margin、limit、last-trading-day和交割参数未确认，参数补齐前不得下单。

## 八、商品期权专项

最新有效截面为9月16日EOD；9月17中国日盘未知，moneyness、Delta和当前成本不可比。全体`execution_ready=false`。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 63.56%/42.49% | +21.07vol | -1.22/+5.67 | Y/N/N | event vol仍贵，T日底层未知 |
| PR611/10-13 | 32.97%/27.65% | +5.32vol | +2.12/-1.20 | Y/Y/N | 需重算Delta |
| M2701/12-16 | 15.88%/11.61% | +4.27vol | +4.02/+1.01 | Y/Y/N | call skew偏贵、无报价 |
| FG701/12-11 | 24.40%/25.69% | -1.28vol | +7.39/+1.34 | Y/Y/N | IV<RV不证明put便宜 |
| EG2611/10-23 | 37.25%/40.63% | -3.39vol | -0.19/+5.49 | Y/Y/N | 合约与主力错位、不可执行 |
| SC/LU/AU/AG/CU/NI | 产品失败或无series | N/A | N/A | N/N/N | 不用代理面 |

当前没有可证明优于裸期货的期权结构。只有取得目标底层、到期、两腿方向数量及实时双边报价后，才比较SC put spread或M call spread；本期不发布执行价、权利金、Greeks、净支出或盈亏平衡。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、21:00夜盘开盘风险地图

严格四层：①9月17中国完整EOD：**缺失**；②属于9月17交易日的早前Night：有效；③15:00—19:30海外：外油弱、金银反弹、航运风险上升；④今晚21:00尚未发生，归属9月18日。

| 品种 | 已知信息 / 核心冲突 | 21:00判断 | 追价/等待 | 开盘后必须确认 |
|---|---|---|---|---|
| SC | 早前Night-2.68%；外油续弱；Hormuz通行骤降 | 因T日EOD缺失，不能判高低开 | 不下旧单；45m | T日settle、VWAP、SC2610-11、Brent |
| FU/LU | 早前Night弱；柴油紧、原油弱 | 方向冲突 | 45m | T日close/settle、back、FU/LU/SC相对强度 |
| PR/PX/TA/EG | 9月16旧强；原油回落 | 无法判定是否已预交易 | 45m | T日量仓、加工链breadth、curve |
| M/RM | 旧强；CBOT豆/粕偏高 | 可能强但不可验证 | 30—45m | T日ΔOI、settle、near-next、CBOT |
| JM/J/I/RB | 早前Night小反弹；内需背景弱 | 不判方向 | 45m | 五品种breadth、T日curve、现货仅context |
| CU/AL/ZN/NI | LME偏强、美元从高位回落 | 海外偏多，国内未知 | 45m | T日EOD、LME、CNH、roll |
| AU/AG | 金银反弹；利率仍高 | 双向 | 45m | exact主力、DXY、收益率、T日settle |
| FG/SA | 旧趋势弱但T日未知 | 禁止低开追空 | 45m | T日低点、OI、curve、实体方向 |
| EC/LC/AP/JD/SF/SM/SI/PS | 制度无Night | 今晚不交易 | 9月18日09:00后45m | T日/次日日盘量仓、curve、实体 |

今晚最不值得交易的是：把9月16 EOD当9月17、把早前Night当今晚、用海外油价倒推中国已跌、沿用今晨绝对触发价，以及任何无bid/ask的期权。

## 十、未来24小时与7天事件

- 9月17日21:00：下一合法中国Night，归属9月18日；因T日EOD缺失，所有品种至少等待30—45分钟并先核经纪端结算价。
- 9月17日晚：USDA周度出口销售常规窗口；M/RM/C/Y/P/OI只按实际销售、采购与中国价格响应调整Delta。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 未来24小时：East-West管道修复、Sohar替代装船、Hormuz/Perim通行及俄炼厂扰动；原油与产品端可能继续分化。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-extend-losses-fears-middle-east-supply-disruptions-ease-2026-09-17/)
- 9月18日前后：BOJ政策窗口可能推动美元、日元、贵金属和工业金属二次定价；避免隔夜裸高Delta/Vega。[BOJ日程](https://www.boj.or.jp/en/mopo/mpmsche_minu/index.htm)
- 9月19日03:30附近：CFTC COT常规窗口，只作滞后拥挤背景，不映射为中国会员确定方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月22日前后：联合国大会期间海湾相关会谈与交通安排，关注是否改变Hormuz实际通行；只按可验证船流调整事件风险。
- 9月23日22:30：下一次EIA周报；能源仓在数据前降低Delta，期权只允许有实时报价的有限净支出结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态新增，共77个期货产品；期权应覆盖64产品；方向、基差/跨期、跨品种/跨市场、加工链、风格/中性、波动率、偏度、事件凸性均纳入清单。
- 实际当前取数：9月17 T日Futures **0/77**；Physical 18/20、External 17/22、早前Night 55产品/610合约；Options最新有效9月16为52/64、337 series。
- 实际分析：77产品均用9月16 last-good完成历史初筛，其中70个有有效趋势/量仓/curve；但77个品种的9月17日盘结论全部记为`missing`，没有把last-good冒充T日。
- 数据不足：五所9月17 EOD、T日Market State、当前curve、SC/LU实体、12个期权产品、全部执行报价、A/B级basis、exact import parity、加工利润与beta-neutral篮子。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位；RS/WR流动性极低。唯一scoped回退排除DCE且陈旧至8月18日，未使用。
- 黑色建材9/9：last-good FG最弱、JM早前Night反弹；T日全板块未知。
- 有色贵金属12/12：海外金银/LME修复，国内T日未知；NI/AU/AG存在roll或代表合约错位。
- 能源炼化化工25/25：SC/FU/LU外弱与产品/航道紧张冲突；PR/PX/TA/EG旧强能否延续未知。
- 新能源及GFEX新材料全部扫描：LC旧弱但减仓，PT/PD/PS/SI缺T日价格与高质量实体。
- 农产品油脂饲料畜牧22/22：M最值得补证；其余缺T日量仓，不能由CBOT/BMD代理下结论。
- 航运与软商品全部扫描：Hormuz船流异常值得跟踪，但EC无Night、无exact运价且T日EOD缺失；旧多不恢复。

风险预算：**本期新增风险预算为0。** 核心EOD恢复且经纪端确认具体合约、curve、保证金/限幅后，再按单笔0.25%—0.75% NAV试仓；SC/FU/LU/PR共享能源因子合并计算。压力测试仍包括1/2个涨跌停、Hormuz再封锁、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压与人民币急变。

归档状态见聊天交付与状态文件；CI只作独立事后校验。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；9月17五所EOD缺失，今晨SC/M/FG旧触发价全部过期，禁止平移到21:00。  
C. 今晚应继续观察的机会：SC2611反转能否延续、M2701相对强势、FU/LU产品紧张、Hormuz船流与EC映射，以及金银对美元回吐的持续性。  
D. 今晚必须避免或退出的交易：把9月16当9月17、追SC/FU/LU或FG第一跳、重启能源/EC旧多、用repo冲突WTI或C级basis构造套利，以及在execution-ready=false时臆测期权成本。
