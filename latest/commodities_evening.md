# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-07

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-07T19:50:17+08:00；信息截点：2026-09-07T19:50:17+08:00；最近完整中国交易时段：2026-09-07日盘；下一可交易窗口：2026-09-07 21:00夜盘，归属2026-09-08交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易。** SC已获价格、曲线和外油三层确认，但首跳赔率不足；今晚优先等SC回撤、AU反抽失败与SC-FU价差确认。

## 二、数据质量与覆盖

本期依次读取了[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[雷达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，再按候选下钻[逐合约行情](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[Options质量](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、surface与[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

统一输入`schema_version=2`，`requested_date=2026-09-07`，生成于19:17；Futures/Market State在18:59生成，五所SHFE/INE/DCE/CZCE/GFEX共802合约，802/802源日期匹配，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0。7条OHLC placeholder已从排行排除；无重复、非法OHLC、负成交量或负OI。核心期货有效，但`official_complete=false`，原因是basis、会员排名缺失，SHFE/DCE/GFEX仓单抓取失败或沿用，以及DCE/GFEX合约参数不完整，并非EOD失效。

Physical于19:16更新：20个目标中18个fresh、2个unavailable、无carried-forward；但全部可计算basis均为C级，缺交割地/品质/含税等对齐，只作context。仓单仅CZCE当日可用，GFEX的LC/PS/SI/PD/PT为9月1日stale carry，SHFE与DCE当日缺失。

Options为9月7日最新截面：22,850张合约、377个series、58/64产品；IV覆盖98.05%、OI覆盖67.58%、bid/ask覆盖0。366个局部series可研究surface，72个可研究positioning，但全局`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`，0个series可直接执行；缺MA/PL/PR/SH/TA/ZC。Dealer Gamma方向未知。

Night Session必须隔离：本次任务的`trading_date=2026-09-07`、`night_session_date=2026-09-06`，0条记录、802条均属合法outside-window；周日没有夜盘，因此不应有行情。状态`coverage_complete=true`但`validation_passed=false/published=false`，并保留了一个标签为9月5日的旧Friday-night快照。该旧标签违反交易日语义，不能冒充属于9月7日的validated Night，也不能冒充今晚21:00未来行情。本期因此不计算`overnight_return`或`day_follow_through`；早盘条件是否真正触发在无分钟路径时记为unknown。

## 三、商品仪表盘

EOD涨跌使用同一具体合约结算收益；curve为近月减次月期货曲线，不是现货基差。Night栏“不可算”代表数据隔离，不代表该品种制度上无夜盘。

| 板块 | 合约 | 9/7 close/settle | 1D/5D | Volume/OI/ΔOI | EOD curve | Basis/Physical | 已完成Night→Day | 15:00—截点海外 | Options S/P/E | 21:00信号 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 原油 | **SC2610** | 699.3/688.5 | +0.79%/+11.35% | 195,677/38,974/+3,181 | +6.17% back | 无A级/B级实体层 | 不可算 | WTI约92.2、Brent约97.3，较周五约+0.8%/+1.1% | Y/N/N | 等30m回撤接受 |
| 合成胶 | **BR2611** | 15,455/15,425 | +3.80%/+5.65% | 180,672/97,144/+14,756 | +1.54% back，z=+3.23 | 缺Physical | 不可算 | 海外胶无同日可靠确认 | Y/N/N | 不追首跳，等30—45m |
| 20号胶 | **NR2611** | 16,345/16,260 | +2.43%/+1.50% | 134,532/78,961/+5,754 | -0.19% contango | 缺完整实体层 | 不可算 | 仅代理背景 | Y/N/N | 等45m与BR/RU联动 |
| 天胶 | **RU2701** | 19,180/19,110 | +1.81%/+1.25% | 492,743/164,125/+11,338 | -1.02% contango，z=-3.15 | 缺完整实体层 | 不可算 | 海外胶未确认 | Y/Y/N | 价强/曲线反证 |
| 黄金 | **AU2610** | 950.78/954.52 | -1.68%/-2.42% | 307,857/154,549/-3,835 | -0.45% contango | 无完整实体层 | 不可算 | 现货金约4,392.9，-0.8% | Y/Y/N | 反抽失败再空 |
| 白银 | **AG2610** | 15,990/16,025 | -1.80%/-3.86% | 513,715/199,514/-8,318 | -0.15% contango | 无完整实体层 | 不可算 | 现货银约65.48，-1.0% | Y/N/N | 不抢高beta反转 |
| 纯碱 | **SA701** | 1,079/1,091 | +1.02%/+3.41% | 2,431,804/1,255,644/+37,247 | -6.16% contango，z=-2.43 | C级；仓单-781至5,210 | 不可算 | 无直接海外锚 | Y/Y/N | curve冲突，等30m |
| PVC | **V2701** | 5,051/5,057 | +0.34%/+7.69% | 2,191,975/1,097,510/-37,484 | -1.19% contango | 无完整实体层 | 不可算 | 无exact映射 | Y/Y/N | 5040附近仍是分水岭 |
| 硅铁 | **SF611** | 6,300/6,388 | -2.68%/+3.73% | 1,008,802/415,462/-67,403 | +0.34% back | C级；仓单+74 | 无夜盘 | 无直接锚 | Y/Y/N | 晨间多头观察失效 |
| 锰硅 | **SM611** | 5,880/5,980 | -3.08%/-1.84% | 590,598/336,377/-64,613 | 0.00% | 仓单-657 | 有夜盘但本期不可算 | 无直接锚 | Y/Y/N | 减仓下跌，不追空 |
| 鸡蛋 | **JD2611** | 3,827/3,791 | +1.58%/+1.77% | 326,207/250,598/+18,540 | +6.12% back | 缺实体方向变化 | 无夜盘 | 无直接锚 | Y/N/N | 等次日日盘确认 |
| 燃料油 | **FU2611** | 3,880/3,799 | -1.89%/+1.63% | 990,485/203,033/-2,910 | +4.58% back | C级context | 不可算 | 海外原油强、FU结算弱 | Y/N/N | 观察SC-FU RV |
| 碳酸锂 | **LC2701** | 142,200/141,580 | -3.71%/-11.79% | 147,974/394,996/+2,366 | -0.26% contango | C级；仓单沿用9/1 | 无夜盘 | 无可靠外盘锚 | Y/N/N | 不接第一刀 |

海外层截至截点：repo准实时显示WTI 92.21、Brent 97.32、LME铜14,439.5、BMD棕榈油4,977；Reuters盘中亦显示油价维持六周高位。美元指数约98.9、日内-0.2%；HKEX九月USD/CNH期货17:05约6.7061，人民币没有额外放大进口通胀。[Reuters油市，2026-09-07](https://www.reuters.com/business/energy/oil-extends-gains-after-us-iran-strike-ships-2026-09-07/) [Reuters汇市，2026-09-07](https://www.reuters.com/world/india/rupee-may-withstand-oil-fed-pressures-with-rbi-support-2026-09-07/) [HKEX USD/CNH](https://www.hkex.com.hk/Products/Listed-Derivatives/Foreign-Exchange/USD-CNH-Futures?sc_lang=en)

## 四、相比上一期真正变化

1. **SC把周末事件从“新闻右尾”变成了三层确认。** 结算+0.79%、收盘699.3高于结算，OI增加8.89%，near-next back升至6.17%，外油仍涨约1%。但日内709高点未守住，市场已经部分预交易21:00 gap；今晚不应把同一新闻再买一遍。
2. **BR是全市场最强动量，但证据仍只有两层。** settle +3.80%、ΔOI +14,756、Volume z=3.33、curve z=3.23；日内高15980、收15455暴露高位供应。海外胶与实体均未确认，按评分上限只能69分。
3. **SF/SM晨间观察被否定。** SF/SM分别settle -2.68%/-3.08%，OI减少6.74万/6.46万。价格与OI只能说明减仓型下跌线索，不能断言多头止损身份；若此前未按条件建立，不存在“持仓退出”假设。
4. **黄金地缘对冲没有压过利率冲击。** AU/AG分别-1.68%/-1.80%，外盘金银再跌约0.8%/1.0%；美元却小幅走弱，说明当前主因更接近利率与加息预期，而非单纯美元方向。[Reuters黄金，2026-09-07](https://www.reuters.com/world/india/gold-eases-robust-us-payrolls-boost-rate-hike-bets-inflation-data-focus-2026-09-07/)
5. **期权研究层显著修复，执行层没有修复。** 产品覆盖由52/64升至58/64，SC/AU/AG/BR均有9月7日surface；bid/ask仍为0，所以“能研究IV/skew”不等于“能成交”。
6. **V/SA不再是同一交易。** V仅小涨且OI下降，SA价涨仓增、仓单下降，但二者仍处contango；价格强不等于现货短缺确认。

## 五、产业链地图

**原油—炼化｜偏多但链内分裂｜置信度中高。** SC价格/OI、back和外油同向；FU结算-1.89%、OI下降，说明上游供应风险没有等比例穿透高硫燃料油。最强反证是SC日内高点回落、期权event IV已很高、无实体层。相对价值优于把整条能化链一起做多。

**合成胶—天然胶｜日内最强｜置信度中。** BR/NR/RU均上涨并增仓，但BR back、RU/NR contango，且海外天然胶没有同日有效确认。竞争解释是国内夜盘遗留挤压与仓位反馈，不是已证实的全球短缺。

**贵金属｜最弱宏观链之一｜偏空，置信度中。** 中国与外盘金银同跌，curve轻度contango；美元小跌却未能托住黄金。反证是地缘突发可随时触发避险跳升，且AU看涨skew仍为正。

**硅铁—锰硅—钢材｜由最强转最弱｜置信度中。** SF/SM高成交下减仓下跌，晨间延续逻辑失效；SF curve仍小幅back，但仓单增加且钢材并未同步崩跌。当前更像挤压退潮而非已确认新空趋势。

**纯碱—PVC—玻璃｜分化/挤压而非供需牛市｜置信度中低。** SA价格、OI和仓单方向偏多，V则仓位回吐；两者contango仍是核心反证。未入榜的FG仅+0.72%、仓单不变，没有足够异常。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | **SC2610回撤接受多** | 22/18/18/12/9 | **79** | 1、2、4 | 存在待验证优势｜部分｜等21:00后30m |
| 2 | **多SC2610/空18手FU2611美元中性RV** | 21/20/14/11/8 | **74** | 1、2、4 | 存在待验证优势｜部分｜等两腿报价与触发 |
| 3 | **AU2610反抽失败空** | 20/17/16/11/8 | **72** | 1、2、4 | 存在待验证优势｜部分｜等15—30m |
| 4 | **BR2611回撤确认多** | 21/15/11/13/9 | **69** | 1、2 | 存在待验证优势｜部分｜等30—45m |
| 5 | **JD2611突破延续观察** | 18/16/9/13/10 | **66** | 1、2 | 存在待验证优势｜部分｜无夜盘，等9/8 09:00 |

分数仅是研究排序，不是胜率或仓位。SC与SC-FU不可同时按两笔独立主题加风险；BR因缺第三层严格封顶69；JD无夜盘且缺实体与海外确认。

## 七、前三名交易卡

### 1. SC2610｜回撤接受多｜79｜`COM-E-SC2610-GAP-20260905`

**事实：** 9月7日OHLC 678.0/709.0/666.7/699.3，settle 688.5；1D +0.79%、5D +11.35%，ΔOI +3,181（+8.89%），near-next back 6.17%。有效T Night缺失，不能给overnight/day精确拆分。外油截至截点仍较周五涨约1%。

**市场定价：** 周末油轮攻击和OPEC+结果已被中国日盘部分吸收，699.3收盘隐含供应风险溢价继续存在。**我们的分歧：** 若21:00只小幅高开且699附近被接受，外油的后续强度可能仍未完全进入SC；若直接跳过709，赔率将比逻辑更快恶化。最强反证是709高点未守住、SC近月期权IV已显著抬升。

**工具：** 首选SC2610期货；期权虽可研究但无bid/ask。今晚有夜盘，21:00—次日02:30。

- 好成交：21:00后等30分钟，694—701回撤被接受，重新站上704/VWAP后1/3多。
- 中成交：702—709横盘后突破709并成功回踩，半仓于好成交情景。
- 坏成交：直接>715或首跳接近涨停，放弃追价。
- 初始止损：30分钟接受688.5下方；逻辑失效：跌破678且Brent回落至约95.8下方。
- 退出：TP1 715，减半；TP2 735，再减；1—3D无扩张即时间止损。
- 风险：试仓最大损失0.35%—0.60% NAV，确认后≤1.0%；期货最大损失不由结构限定。地缘缓和、涨跌停、保证金上调和流动性消失可穿透计划止损。

标准合约1,000桶/手、tick 0.1元/桶、tick value 100元/手；按settle名义约688,500元/手；最后交易日2026-09-30、实物交割，进入最后交易月前必须roll/exit。[INE SC合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/) 动态margin/limit本次元数据未确认；一板/两板压力分别为`688,500×L`、`688,500×[(1+L)^2−1]`，L须下单前查交易所/经纪商。

### 2. 多SC2610/空18手FU2611｜美元中性RV｜74｜`COM-E-SC-FU-RV-20260907`

**定义：** 多1手SC2610、空18手FU2611。按settle，SC名义688,500元，18手FU名义约683,820元；这是近似dollar-neutral，不是beta-neutral、裂解套利或import parity。组合损益近似`1,000×ΔSC - 180×ΔFU`元，未含手续费、滑点和保证金差异。

**逻辑与分歧：** SC获得价格/OI、back和外油确认，FU却settle -1.89%、OI下降；市场可能低估原油供应冲击与高硫燃料油自身供需的分化。竞争解释是FU收盘3880已远高于3799结算，弱势只是结算口径；若21:00 FU补涨，RV会快速回吐。

- 入场：两腿21:00后等30分钟；SC守695以上且FU反抽3900—3920失败时，按1:18同步成交。
- 好/中/坏：总滑点≤计划1R的10%为好；10%—20%减半；>20%或任何一腿涨跌停/无深度则放弃。
- 初始止损：组合亏损达到1R；逻辑失效为SC接受688.5下方，或FU站稳3920且外油不再上行。
- 退出：+1.5R减半，+3R再减；2D时间止损。若两腿相关性破裂或保证金跳升，先降总杠杆。
- 风险：0.25%—0.50% NAV；与SC outright、LU/BU/PG合并计同一因子。两腿均为期货，最大损失不受结构限定。

FU为10吨/手、tick 1元/吨、tick value 10元/手；FU2611最后交易日2026-10-30、实物交割。动态margin/limit均未确认；压力损失按两腿各自名义和官方L逐腿计算，不能把dollar-neutral当作有限损失。

### 3. AU2610｜反抽失败空｜72｜`COM-E-AU2610-RATE-GEO-20260905`

**事实：** 9月7日OHLC 952.00/961.88/944.10/950.78，settle 954.52；1D -1.68%、5D -2.42%，ΔOI -3,835，curve -0.45% contango。现货金约4,392.88、-0.8%，白银约65.48、-1.0%；DXY反而小跌约0.2%。

**市场定价：** 地缘风险未能抵消强非农后的加息/实际利率压力。**我们的分歧：** 若954.5—958反抽失败，黄金信用/避险叙事的边际买盘仍偏弱；但美元下跌和任何Hormuz升级都可迅速否定空头。期权9月23日ATM IV仅高RV约2.9 vol，但没有报价，不能证明put便宜。

- 好成交：等15—30分钟，950—955反抽失败后跌破949，1/3空。
- 中成交：跌破944.1后回抽不回，仓位减半。
- 坏成交：直接<942不追空。
- 初始止损：30分钟接受962上方；逻辑失效：接受966且国际金重回4,445上方。
- 退出：TP1 936、TP2 920；PPI前无扩张即减仓，1—2D时间止损。
- 风险：0.25%—0.45% NAV；AU/AG及美元—利率因子合并。期货最大损失不受结构限定。

AU为1,000克/手、tick 0.02元/克、tick value 20元/手；按settle名义约954,520元/手；最后交易日2026-10-15、实物交割。动态margin/limit未在本次元数据确认；一板/两板压力为`954,520×L`与`954,520×[(1+L)^2−1]`。

## 八、商品期权专项

本期可以研究surface，仍不能执行：

- **SC2610 / 2026-09-11：** ATM 690，IV 58.25%，RV20 36.63%，IV-RV +21.63 vol；RR25 +3.92、BF25 +2.83。事件凸性已很贵，不能因地缘风险大就断言call便宜。
- **AU2610 / 2026-09-23：** ATM 952，IV 24.38%，RV20 21.48%，IV-RV +2.90；RR25 +3.62、BF25 +1.53。若实时报价合理，有限损失put spread可研究，但当前不可报价。
- **BR2611 / 2026-10-26：** ATM 15,400，IV 36.26%，RV20 28.87%，IV-RV +7.39；RR25 -0.56、BF25 +3.86。下行尾略贵且凸度高，不支持无条件追call。
- **V2701 / 2026-12-16：** ATM 5,100，IV 22.78%，RV20 25.34%，IV-RV -2.56；RR25 +3.69。存在长波动研究线索，但没有bid/ask、净成本和滑点，不能发布跨式或call spread成交价。
- MA/PL/PR/SH/TA/ZC为9月7日chain失败；Dealer Gamma未知，OI/PCR不作完整拥挤结论。

结论：期权没有优于裸期货的可执行证据；`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、21:00夜盘开盘风险地图

四层时间边界：①9月7日EOD已完成；②周日晚没有属于9月7日的Night，旧标签异常快照已隔离；③15:00—截点海外只是潜在gap映射；④今晚21:00尚未发生，归属9月8日交易日。

| 品种 | 预期 | 海外/国内冲突 | 首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|---|
| SC | 平/小高，宽幅 | 内外同向，日盘已预交易大部 | 不追 | 30m | 699/709、Brent 97、近月back、OI |
| FU/LU/BU | 分化 | 外油强，FU结算弱 | 不追 | 30—45m | FU 3900—3920、SC-FU价差、裂解端 |
| BR | 平/偏高 | 国内强，海外胶未确认 | 不追 | 30—45m | 15400/15590/15980、RU/NR breadth、curve |
| RU/NR | 偏高 | 价格强、contango反证 | 不追 | 45m | curve是否收窄、BR是否守强 |
| AU/AG | 平/偏低 | 中国和外盘同弱，美元小跌 | 不追 | 15—30m | AU 949/954.5/962、国际金、收益率 |
| SA/V | 平开 | 无海外锚，国内结构冲突 | 不追 | 30m | SA contango/OI；V 5040/5072 |
| EG/MA | 平/小高 | 外油支持但国内趋势弹性下降 | 不追 | 30—45m | 是否收回settle、OI与curve |
| SF/JD/LC | 无夜盘 | 不适用 | 不适用 | 次日09:00 | SF是否止跌、JD是否续增仓、LC实体更新 |

## 十、未来24小时/7天事件日历

- **9月8日04:00 BJT：USDA Crop Progress。** 谷物/油脂以Delta降档处理，报告本身不等同WASDE。[USDA日历](https://www.usda.gov/about-usda/reports-and-data/agency-reports)
- **9月9日09:30 BJT：中国8月CPI/PPI窗口。** 黑色、化工和工业金属先减同因子Delta；以国家统计局正式发布为准。[国家统计局发布日程](https://www.stats.gov.cn/sj/fbrc/)
- **9月10日09:00：热卷、不锈钢、低硫燃料油期权挂牌。** 首日只观察链、surface和bid/ask，不能把挂牌等同执行ready。[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html) [INE](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)
- **9月10日20:30：美国8月PPI。** AU/AG、油价与美元因子仓提前减Delta；若买凸性，仅用最大净支出可接受的结构。[BLS PPI](https://www.bls.gov/schedule/news_release/ppi.htm)
- **9月11日00:00 BJT：劳动节顺延的EIA周报。** 对SC、FU、LU与裂解价差优先级高；EIA官方发布为美东9月10日12:00。[EIA](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月11日20:30：美国8月CPI。** 贵金属和工业金属面临Delta/Vega重置。[BLS CPI](https://www.bls.gov/schedule/news_release/cpi.htm)
- **9月12日00:00：USDA 9月WASDE。** M/Y/P/OI/C/CF避免无保护方向重仓；缺实时surface时不预埋期权成本。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- 地缘方面持续监控Hormuz受限区、船舶通行与美伊相互打击；这类headline只改变分布，不自动提供入场价。Reuters称油轮通行降至5月以来低位附近。[Reuters，2026-09-07](https://www.reuters.com/business/energy/oil-extends-gains-after-us-iran-strike-ships-2026-09-07/)

## 十一、覆盖核对、旧建议台账与归档

**覆盖核对：** 63个强制代码全部取得9月7日有效主力合约并完成1D/3D/5D/20D、量仓、curve和策略类别扫描；另扫描JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR共14个动态品种，其中BZ/LG/OP/PD/PL/PT/RR/RS/WR共9个有效分析，JR/PM/RI/WH/ZC因零价、零量、零OI列为不适用/流动性不足。逐板块未入榜异常：黑色I +1.17%但curve roll警告；有色ZN +0.93%但OI略降；化工EG仍有11.69%五日涨幅但当日减仓回落；农产品JD最突出、油脂仅Y curve z异常但价格近零变化；软商品EC +2.45%但高RV且无夜盘。方向、跨期、基差、跨品种/跨市场、dollar-neutral RV、波动率/偏度/事件凸性与1D—20D周期均已扫描；没有A级/B级basis、exact import parity或可执行期权报价，因此不发布伪套利。

**旧建议台账：**

- `COM-E-SC2610-GAP-20260905`：首次9/5；由周末双向gap升级为回撤接受多。变化原因=9/7价格/OI/curve与外油确认；晨间触发路径因无分钟数据仍unknown，不假设成交。
- `COM-M-BR2611-NIGHT-SQUEEZE-20260907`：继续观察，68→69；变化原因=EOD价量仓和curve确认，但高点回落、实体/海外缺失；不假设晨间已建仓。
- `COM-E-V2701-SQUEEZE-20260904`：仍为failed-squeeze观察，67→64（未入榜）；日内最低4970但收5051，触发路径unknown；contango未消失。
- `COM-E-SF611-PULLBACK-20260904`：研究观点失效并退出观察池；变化原因=价格跌破原结算锚、OI大幅回吐、仓单增加。若此前未按条件建立，不存在真实持仓处置；若确已建立，应按原失效纪律退出。
- `COM-E-AU2610-RATE-GEO-20260905`：65→72并保留空头条件；变化原因=中国与外盘金银共同走弱，但地缘反证仍在。

归档按固定六路径直接写main；完成回读后`archive_status=success`，CI不轮询，`ci_validation_status=pending_or_unverified`。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2610在21:00后30分钟回撤接受699附近再多；或多1手SC2610/空18手FU2611在两腿同步触发后建近似dollar-neutral RV；AU2610仅在反抽954.5失败并跌破949后空。  
C. 今晚应继续观察的机会：BR2611回撤守15400后重夺15590、SA701的contango/OI/仓单吸收、V2701对5040的接受、JD2611次日突破延续。  
D. 今晚必须避免或退出的交易：追SC/BR首跳、继续坚持已被价格与OI否定的SF多头观察、把C级basis或SC-FU称套利、在execution-ready=false时臆测期权成本，以及把计划止损写成有限最大损失。