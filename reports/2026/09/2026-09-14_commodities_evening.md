# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-14

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:38 BJT；信息截点：19:30；最近完整中国交易时段：9月14日日盘。今晚21:00连续交易归属9月15日交易日；EC等无夜盘品种下一窗口为9月15日09:00。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC已获价仓曲线确认，但收在日高、外油再涨，今晚只能等回撤接受，禁止追第一跳。**

当前regime：**中东供给冲击获得中国与海外价格确认，SC近端挤压强于FU和化工扩散；美元、实际利率上行压制贵金属与有色；黑色、玻璃纯碱和橡胶链偏弱。**

最接近触发的是SC2611与FU2611；EC2610需等明日日盘。SC缺回撤后的成交接受，FU缺持仓确认，EC缺航线现货映射且日内冲高回落。

## 二、数据质量与覆盖

优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)；因Top合约与周末前合约发生切换，下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)、[期权曲面](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)和[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-14`，19:13:37生成；Futures/Market State截至9月14日18:59:17。
- Futures：五所802合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchange=0；7条placeholder从异常排序中排除。`official_complete=false`来自辅助官方模块不完整，不推翻核心期货质量闸门。
- Market State：同合约1D/3D/5D/20D历史完整；SC主力由2610切换为2611并标roll，涉及旧卡时不拼接收益。
- Physical：19:13:03生成，20项目标中18项按原生频率fresh，SC/LU unavailable；5条仓单沿用。所有basis为C级，只作context，不能称套利。
- External repo：19:13:07生成，17/22 fresh、5项unavailable，全部`context_only`；另用Reuters/LSEG补充19:30附近准实时报价。
- Options：9月14日19:00 BJT截面，22,758条chain、373个series、59/64产品；CJ/MA/PL/PR/ZC失败。363个series surface-ready、78个positioning-ready、0个execution-ready；IV覆盖98.11%、OI覆盖69.09%、bid/ask覆盖0。`surface_latest.json`本身为空文本，统一输入内嵌series可读，故不是工具截断。
- Metadata：partial；有效合约匹配73.32%，multiplier/tick/margin/limit约29.80%，last-trading-day 67.33%。未确认字段不推断。

Night以module-specific状态为准：`trading_date=2026-09-14`、`night_session_date=2026-09-13`、06:02:03生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=true`。请求802合约，0个有效Night、802个合法`outside_night_window`；missing timestamp/price/quote、query error、unresolved contract均为0。这是周日晚制度性无连续交易，属于今日已完成交易日的“无Night”事实，不是今晚21:00未来行情；`overnight_day_decomposition_used=false`。

## 三、商品仪表盘

1D/5D为9月14日同一具体合约结算收益；早前Night均为N/A。曲线为near-minus-next期货曲线，正负含义仅按具体合约对解释，不等于现货基差。S/P/E为surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Basis/Physical | 早前Night；15:00—19:30海外 | Options；21:00信号 |
|---|---|---|---|---|---|
| 原油SC | SC2611；815.2/776.5；+2.62%/+19.74% | 15.28万/3.86万/+6,460；SC2610-11 back 8.83%、z=2.07 | 缺失 | N/A；Brent约107.3—108.0、WTI约102.4—103.5 | Y/N/N；等30—45m回撤 |
| 燃料油FU | FU2611；4392/4365；+1.70%/+14.90% | 126.39万/21.94万/-1,489；back 12.39%、z=2.13 | C/context | N/A；外油约+3% | Y/N/N；不追第一跳 |
| 集运EC | EC2610；2090.5/2114；+3.42%/+11.15% | 2.32万/2.65万/+524；back 20.13%、z=-1.88 | exact运价缺 | 制度无Night；双航道风险 | N/N/N；明日09:00再验 |
| PTA | TA701；6352/6396；+1.33%/+8.00% | 225.64万/117.75万/+38,898；pair roll、曲线1.46% | C；日频现货6980 | N/A；原油强 | Y/Y/N；等30m breadth |
| 玻璃FG | FG701；927/944；-4.07%/-3.48% | 190.58万/121.82万/+63,156；pair roll、曲线1.65% | C；日频现货992 | N/A；无exact外盘 | Y/Y/N；反抽失败空 |
| 纯碱SA | SA701；1019/1037；-3.89%/-4.95% | 186.91万/129.17万/+21,427；pair roll、曲线-0.40% | C；日频现货1090 | N/A；无exact外盘 | chain局部/N；不追空 |
| 铜CU | CU2610；107840/108190；-0.43%/-0.93% | 11.44万/18.78万/-11,069；back 0.60%、z=1.43 | C；日频现货108948 | N/A；LME铜约14067.5、美元走强 | Y/Y/N；反抽失败才空 |
| 锌ZN | ZN2611；26335/26525；-1.23%/多周期弱 | 9.50万/12.80万/+3,573；曲线-0.42%、z=-1.79 | C/context | N/A；LME锌约3831 | Y/N/N；偏弱但不追 |
| 黄金AU | AU2612；937.6/946.54；+0.21%/多周期弱 | 9.88万/16.51万/+6,710；轻曲线0.06% | C/context | N/A；现货金约4292、-1.3% | Y/N/N；实际利率反证 |
| 白银AG | AG2612；15528/15752；+0.48%/-1.85% | 14.36万/19.97万/+6,322；contango 0.24% | C/context | N/A；银约-2.6% | Y/N/N；两边不追 |
| 玉米C | C2611；2221/2236；-1.06%/-2.32% | 76.30万/114.52万/-16,737；pair roll、曲线-1.06% | C/context | N/A；CBOT约530.25 | Y/Y/N；WASDE多头否定 |
| 豆粕M | M2701；3361/3384；-1.11%/-0.59% | 170.67万/267.79万/-55,842；pair roll、曲线-1.09% | C；现货3378 | N/A；CBOT豆约1294.75 | Y/Y/N；采购未闭环 |
| 苯乙烯EB | EB2610；10094/10138；-1.60%/+5.64% | 111.41万/23.59万/-19,107；曲线0.94%、z=-0.92 | C/context | N/A；成本端强 | Y/Y/N；成本弹性衰减 |
| 碳酸锂LC | LC2701；132340/133560；-0.30%/-5.67% | 12.26万/41.16万/+3,985；pair roll | C；现货134000 | 制度无Night；无exact外盘 | Y/N/N；不接第一刀 |
| 丁二烯橡胶BR | BR2611；14985/14975；-3.42%/-2.92% | 11.84万/8.40万/-5,993；pair roll、曲线1.34% | C/context | N/A；无exact映射 | Y/N/N；减仓跌不追 |

19:30附近LSEG延时报价显示NYMEX原油约102.41、Brent约107.32，较周五分别约+2.36%/+2.59%；Reuters报道盘中一度约103.54/108.04。美元升至两周高位，10年美债约4.96%，现货金约4292、跌1.3%，银跌约2.6%。这是今晚潜在gap的海外映射，不是中国期货已交易的价格。[Reuters油市，2026-09-14](https://www.reuters.com/business/energy/oil-prices-jump-more-than-3-after-new-strikes-saudi-strait-hormuz-2026-09-13/)｜[Reuters美元，2026-09-14](https://www.reuters.com/world/asia-pacific/dollar-steady-yen-near-7-month-high-ahead-fed-boj-meetings-2026-09-14/)｜[Reuters贵金属，2026-09-14](https://www.reuters.com/world/india/gold-slips-oil-rally-fans-rate-hike-bets-ahead-fed-meeting-2026-09-14/)

## 四、相比上一交易日/今晨真正变化

1. **SC从新闻风险变成三层价格确认。** SC2611收815.2、接近日高815.8，结算+2.62%，OI单日+20.08%，SC2610-11 back扩大至8.83%、z=2.07；但close高于settle约4.98%，说明今晚追价风险极高。
2. **主力切换改变旧建议。** 旧`SC2610`卡已过主力窗口，本期不把2610触发、止损或收益拼到2611；原idea续作时改为`SC2611`并记录roll修订。
3. **FU与SC显著分化。** FU结算+1.70%、curve更紧，但OI减少0.67%；价格支持、持仓不支持，产品端强于原油的旧分歧没有兑现。
4. **EC高开后边际弹性衰减。** 日高2179.5、收2090.5，close低于settle；back仍深但由22.36%收窄至20.13%。航运多头保留，降级为明日等待。
5. **WASDE玉米多头被中国价格否定。** C2611结算-1.06%、收近低、OI下降；`COM-M-C2611-WASDE-CORN-20260912`退出正式观察榜，原因是新价格反证而非叙事修订。
6. **宏观反证强化。** 外油上涨同时美元与收益率上行，金银下跌；黄金信用主题本期仍不成立，AU/AG不因地缘风险自动做多。

旧建议台账：

- `COM-E-SC2611-GAP-20260905`：由SC2610滚动修订至SC2611，75→82；首次提出日期保持9月5日。旧2610卡停止新增，若此前确已建立须按实际成交与交割计划处理，本报告不假设持仓。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：78→76；价格与curve确认，但OI反向且相对SC不强。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：78→71；日内冲高回落、back收窄，明日触发重置。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：66→68；中国和LME同弱、美元上行支持，但国内back与减仓反对追空。
- `COM-M-C2611-WASDE-CORN-20260912`：55→退出；中国首日价格否定，催化已过期。

没有分钟路径和成交反馈，FU/EC晨间条件是否曾真实触发均记为未知；不把OHLC触及价位等同用户成交。

## 五、产业链地图

- **最强：SC近端原油链，偏多，置信度高。** T日价仓、8.83% back和外油同向构成1/2/4层支持；缺SC实体、A级basis和exact import parity。close-settle大幅分歧是今晚最强追价反证。
- **能源产品—聚酯：上游强、扩散不齐，置信度中。** FU涨但减仓，TA价涨仓增且高成交，EB/BZ下跌；成本冲击只传到部分品种，不宜做未定义篮子。
- **航运：事件仍强、价格弹性转弱，置信度中。** EC价仓与深back支持，但冲高回落、curve收窄；油轮与集装箱映射不纯，不能称跨市场套利。
- **最弱：FG—SA与部分橡胶/黑色，置信度中。** FG/SA价跌仓增仅是归因线索，BR减仓跌、JM价曲冲突；没有A/B basis或实体方向变化，至多观察空。
- **有色贵金属—农产品：宏观偏空、供需不足，置信度中低。** CU/ZN与美元同向偏弱；AU/AG受实际利率压制；C/M中国价格不确认WASDE/采购逻辑。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2611回撤接受多 | 24/14/20/15/9 | **82** | 1、2、4 | 存在待验证优势｜充分但追价反证强｜今晚等30—45m |
| 2 | FU2611产品链延续多 | 23/13/20/12/8 | **76** | 1、2、4 | 存在待验证优势｜部分｜今晚等30—45m |
| 3 | EC2610航运冲击多 | 22/13/18/10/8 | **71** | 1、2、4 | 存在待验证优势｜部分｜无Night，明日等待 |
| 4 | CU2610关税/美元回吐空 | 19/16/14/9/10 | **68** | 1、4 | 存在待验证优势｜部分｜今晚反抽失败才考虑 |
| 5 | FG701弱势延续空 | 18/14/11/8/8 | **59** | 1 | 证据不足｜不足｜等待实体/curve复核 |

分项均已复算且未超上限。FG只有一个独立支持层，封顶59；CU只有两层，封顶69。SC/FU/EC共享地缘—运输因子，初始风险必须合并。所有期货最大损失均不由计划止损限定。

## 七、前三名交易卡

### 1. SC2611｜条件多｜82

**事实：** T日OHLC 740/815.8/737.9/815.2，结算776.5；1D +2.62%、5D +19.74%，ΔOI +6,460（+20.08%），volume z=2.88、OI z=2.32；SC2610-11 back 8.83%、z=2.07。早前Night不存在，不能分解overnight/day。19:30外油约+2%—3%。

**市场定价：** 近端供应中断和替代管道风险已重价。**分歧：** 趋势可延续，但815.2 close较776.5 settle高约4.98%，今晚第一跳的盈亏比很差。最强反证是管道恢复、Hormuz通行改善或外油跌回104下方。

- 最佳表达：SC2611单腿条件多；不把未报价期权当有限损失替代。今晚21:00有Night，通常连续至次日02:30，归属9月15日；具体时段下单前以INE为准。
- 好成交：21:00后等30—45分钟，795—810获得接受并重上816/VWAP，先1/3仓。
- 中成交：突破816后回踩812—816不破，半于好成交仓位。
- 坏成交：直接高于830或距计划止损超过1R，放弃。
- 止损：30分钟接受788下方；逻辑失效：跌破776.5、back降至6.5%以下且Brent低于104或管道恢复。
- TP1 838或+1.5R；TP2 875或+3R；1—2D无扩张退出。1—7D催化为管道修复、Hormuz/Perim通航、EIA与FOMC。
- 风险：0.20%—0.30% NAV；与FU/EC/LU合并初始≤0.60%。最坏情景是通航突变、外油跳水、中国跌停与流动性消失。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；按结算名义776,500元。repo确认最后交易日10月30日、11月6日最后交割日；实物交割，10月中旬前复核移仓。
- margin动态值未确认；按今晚相关合约16%限幅压力假设，一板约124,240元/手，两板复合约228,602元/手。适用范围必须在下单前按[INE规则](https://www.ine.cn/eng/market/futures/energy/sc/contract/)复核。

### 2. FU2611｜条件多｜76

**事实：** T日OHLC 4230/4523/4203/4392，结算4365；1D +1.70%、5D +14.90%，ΔOI -1,489，back 12.39%、z=2.13。价格与curve支持，持仓反对。早前Night不存在；外油继续高于周五收盘。

- 市场可能错在产品端紧张更持久；竞争解释是FU只是成本跟涨且减仓反弹。今晚21:00有Night，首跳不追。
- 好成交：4310—4380承接并重上4395/VWAP，先1/3仓。
- 中成交：突破4525并回踩成功，仓位减半。
- 坏成交：直接高于4580或滑点超过1R的20%，放弃。
- 止损：30分钟接受4280下方；失效：跌破4200、back低于10%、Brent低于104或产品相对SC继续走弱。
- TP1 4520或+1.5R；TP2 4750或+3R；1—3D无扩张退出。
- 风险0.20%—0.30% NAV，与SC/EC/LU合并。最坏情景为油价反转、产品裂解回落与国内跌停。
- 10吨/手，tick 1元/吨，tick value 10元；按结算名义43,650元。repo确认最后交易日10月30日、11月3日最后交割日；实物交割，10月中旬前移仓。
- margin/limit未确认；一板压力=`43,650×L`，两板=`43,650×[1-(1-L)^2]`，L须下单前核验。

### 3. EC2610｜明日条件多｜71

**事实：** T日OHLC 2084/2179.5/2065/2090.5，结算2114；1D +3.42%、5D +11.15%，ΔOI +524；back 20.13%，较9月11日22.36%收窄。EC制度上无Night，今晚不能执行。

- 市场隐含红海/Hormuz扰动；分歧是现货集运可能仍滞后，竞争解释是油轮风险并不等于EC盈利。
- 下一窗口：9月15日09:00后等30分钟。好成交2050—2090接受并重上2115/VWAP；中成交突破2180并回踩，仓位减半；直接高于2220为坏成交。
- 止损：30分钟接受2035下方；失效：跌破1976、back低于17%且实际通航恢复。
- TP1 2180或+1.5R；TP2 2300或+3R；1—5D时间止损。
- 风险0.20%—0.30% NAV，与能源/航运合并。最坏情景是headline反转、运价不跟、涨跌停与流动性消失。
- repo确认最后交易日及最后交割日为10月26日；multiplier、tick、margin、limit仍未确认，参数补齐前不得下单，也不编压力损失。[INE EC合约页](https://www.ine.cn/eng/market/futures/index/)

## 八、商品期权专项

9月14日T日截面已更新；底层大幅变化已反映到EOD moneyness，但全部series `execution_ready=false`，故不能给权利金、净成本、当前可成交Greeks或滑点。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 71.93%/39.06% | +32.86vol | -2.35/+0.42 | Y/N/N | 事件凸性极贵，不追裸call |
| FU2611/10-19 | 73.71%/43.15% | +30.56vol | +3.12/+0.55 | Y/N/N | IV跳升、OI覆盖略低 |
| TA701/12-11 | 34.27%/26.32% | +7.95vol | +3.95/+0.90 | Y/Y/N | 结构可研究、不可报价执行 |
| FG701/12-11 | 22.73%/24.10% | -1.37vol | +6.12/+1.87 | Y/Y/N | IV-RV略负不等于便宜 |
| CU2610/09-23 | 15.23%/14.23% | +1.00vol | -0.65/+1.46 | Y/Y/N | 近到期、先核报价和交割 |
| AG2612/11-24 | 47.11%/34.60% | +12.51vol | +17.77/+6.28 | Y/N/N | 上行尾极贵、positioning不足 |
| C2611/10-23 | 9.75%/8.91% | +0.84vol | +2.29/+0.39 | Y/Y/N | WASDE催化已过期 |

若21:00后取得人工实时双边报价，只研究SC2611同到期1:1 call spread或FU2611同到期1:1 call spread，Delta区间、两腿执行价、最大净支出与局部Greeks须按实时链重算。`research only; manual quote and manual confirmation required before execution; no premium quoted`。Dealer Gamma方向未知。

## 九、21:00夜盘开盘风险地图

严格四层：①9月14日中国完整EOD；②今日交易日没有合法早前Night；③15:00—19:30外油约+2%—3%、美元两周高、金银下跌；④今晚21:00尚未发生，归属9月15日。

| 品种 | T日EOD→早前Night→海外 | 21:00预期/冲突 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| SC | 强收日高、价仓曲线共振→N/A→外油续涨 | 高开倾向，但大部已预交易 | 不追；30—45m | 795/810/816/830、back、Brent107 |
| FU/LU | FU涨减仓、LU弱→N/A→外油强 | 高开但相对强度不确定 | 不追；30m | FU4395/4525、FU强于SC、OI |
| TA/PX | TA价涨仓增→N/A→原油强 | 偏高，部分已白天预交易 | 30m | TA6400、curve breadth、EB是否跟 |
| EB/BZ/EG | 白天下跌或减仓→N/A→上游强 | 高开后回吐风险 | 45m | settlement、OI、FU/TA breadth |
| CU/ZN/AL | 国内弱→N/A→美元强、LME偏弱 | 低开倾向 | 不追空；30—45m | CU107680/108200、LME、back |
| AU/AG | 中国close弱于settle→N/A→金银下跌 | 低开倾向 | 不追；30m | DXY、10Y 4.96%、AG skew |
| FG/SA | 日盘大跌仓增→N/A→无exact外盘 | 低开或技术反抽 | 不追空；30m | FG925/944/974、SA1019、OI/curve |
| M/C/P/Y/OI | 中国弱→N/A→CBOT/BMD混合 | 平/低开 | 45m | C2220、M3357、进口映射 |
| BR/RU/NR | 国内弱→N/A→无exact同品质映射 | 偏低、易反抽 | 30—45m | BR14950、OI、cross-rubber breadth |
| EC/LC/AP/JD/SF/SM/SI/PS | 无制度Night | 今晚不交易 | 下一日盘等30—45m | 日盘量仓、curve、实体更新 |

单日噪音优先判定：BR减仓下跌、AU/AG结算上涨但收盘走弱、EC日内冲高回落。今晚最不值得交易的是第一跳追SC/FU、低开追空FG/SA/有色，以及任何无实时报价的商品期权。

## 十、未来24小时与7天事件

- 未来24h：East-West管道修复时点、Hormuz与Perim通航、受损船舶及Saudi出口库存；恢复消息会同时压缩SC/FU/EC溢价。[Reuters供应分析，2026-09-14](https://www.reuters.com/business/energy/saudi-pipeline-outage-threatens-loss-4-global-oil-supply-2026-09-13/)
- 9月14日21:00：SC/LU相关风险参数调整进入连续交易窗口；线性仓只允许延迟入场并用更小试仓。
- 9月15日10:00附近：中国工业、投资、消费、房地产与能源生产数据；黑色、有色、化工合并降低Delta。
- 9月16日22:30附近：EIA周度石油数据，重点看成品油库存、炼厂开工与出口；SC/FU在事件前减仓，期权仅在取得报价后用有限净支出。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月17日02:00附近：FOMC/SEP；市场对加息预期显著上升。CU/AU/AG提前降低Delta/Vega。[Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 未来7d：CFTC COT仅作滞后拥挤背景；USDA出口销售、美国收割天气、中国大豆采购兑现用于C/M/Y/P/OI后续验证。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)｜[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月14日EOD、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差/跨期、跨品种/跨市场、加工利润、风格/中性、波动率、偏度和事件凸性扫描；LPG按repo代码PG映射。另纳入动态品种，统一输入共77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为零价/零量/零OI占位，RS/WR流动性不足，列不适用而非漏扫。
- 黑色建材9/9：FG/SA大跌仓增最异常；JM、I、RB方向弱但curve/roll不一致。
- 有色贵金属12/12：CU入榜；ZN价跌仓增，AU/AG受美元和实际利率压制，黄金信用主题未成立。
- 能源炼化化工25/25：SC/FU入榜；TA强于EB/BZ，LU与FU分化，SC/LU Physical缺失。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺A级实体及exact海外确认。
- 农产品油脂饲料畜牧22/22：C的WASDE多头已被价格否定；M/P/Y/OI无三层共振。
- 航运及软商品全部扫描：EC入榜；CJ期权失败，仓单绝对变化不足以形成完整实体层。
- 期权应覆盖64个、实际59个；CJ/MA/PL/PR/ZC数据不足，0个execution-ready。
- A/B级basis、exact import parity、可靠加工利润和已定义beta-neutral篮子均不可得；不发布伪套利。

风险预算：单笔试仓最大损失0.20%—0.30% NAV；新增价格与非价格层确认后才可提高至0.75%—1.0%。SC/FU/LU/EC同因子初始合并≤0.60%，总主题风险不得因多品种重复计数。压力测试包含16%一板/两板复合、管道突然恢复、夜盘gap、流动性消失、保证金上调、相关性破裂、IV跳升/塌陷、交割挤压和人民币急变。

固定六路径完成main回读后，`archive_status=success`；CI不等待，`ci_validation_status=pending_or_unverified`。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2611等30—45分钟在795—810承接并重上816，或FU2611在4310—4380承接并重上4395；两者先1/3仓、合并初始风险≤0.60%。  
C. 今晚应继续观察的机会：EC2610明日回撤接受、CU2610反抽失败空、FG701弱势延续、TA强于EB/BZ，以及SC/FU期权实时重报价。  
D. 今晚必须避免或退出的交易：追SC/FU第一跳、低开追空FG/SA/CU/ZN、沿用SC2610旧卡、把油轮风险当EC exact套利，以及在execution-ready=false时臆测期权成本。
