# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-15

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:36 BJT；信息截点：19:30；最近完整中国交易时段：9月15日日盘。今晚21:00连续交易归属9月16日交易日；EC、LC等无夜盘品种下一窗口为9月16日09:00。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC日盘接棒夜盘并获价仓确认，FU/LU却回吐夜盘强势，今晚只等SC回撤接受，不追能源首跳。**

当前regime：中东供应冲击继续抬升原油，但产品链由“共振”转为“SC独强”；美元及美债实际利率压力压制金属，国内投资和地产弱势限制黑色、新能源需求。

最接近触发的是SC2611；FU2611和LU2611退回观察。SC缺21:30—21:45的回撤接受，FU/LU缺日盘持仓与相对强度确认，EC多头已被日盘价格否定。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并因前三候选逐合约复盘下钻[9月15日EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、Physical、External、Options与Contract Metadata。

- 统一输入：schema v2，`requested_date=2026-09-15`，19:16:45生成。
- Futures：19:00生成；五所801合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；9条placeholder排除，负量仓/重复/非法OHLC均0。
- Market State：同一具体合约1D/3D/5D/20D完整；EB主力切换至EB2611，不拼接旧合约。
- Physical：19:16生成，18/20按原生频率fresh，SC/LU unavailable；五条仓单沿用。所有basis为C级，仅作context，不进入方向或套利评分。
- External：19:16日频层17/22 fresh、5项unavailable，全部`context_only`；另联网补充19:30附近油价、贵金属、美元与美债。
- Options：9月15日22,680条、370个series、58/64产品；360个surface-ready、80个positioning-ready、0个execution-ready；IV覆盖98.10%、OI覆盖69.30%、bid/ask与模型Greeks覆盖均0。
- Metadata：partial；合约匹配约73.3%，multiplier/tick/margin/limit覆盖约29.8%，last-trading-day约67.3%。

Night状态：`trading_date=2026-09-15`、`night_session_date=2026-09-14`，06:01:19生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。请求802个合约，579条有效Night、55个产品；216条合法outside-window、7条no-night-trade；missing timestamp/price/quote、query error、unresolved contract均0，warnings为空。

这批Night属于今天已完成的连续交易阶段，不是今晚21:00未来行情。72.19%是有效Night记录占请求合约比例，不是“完整率”；整体采集闭环。

## 三、商品仪表盘

1D/5D为9月15日同合约结算收益；“日盘续涨”=`EOD close / Night close - 1`，仅exact-contract计算。曲线为near-minus-next期货结构，不是现货基差；S/P/E为surface/positioning/execution readiness。

|板块/品种|合约；EOD close/settle；1D/5D|Volume/OI/ΔOI；EOD curve|Basis/Physical|早前Night close；vs close/vs settle；Night ΔOI；日盘续涨|19:30海外；Options；21:00信号|
|---|---|---|---|---|---|
|原油|SC2611；838.6/836.2；+7.69%/+25.74%|21.47万/3.98万/+1,174；back 7.71%、z1.10|Physical缺失|821.5；+0.77%/+5.80%；-998；**+2.08%**|Brent约107.35；Y/N/N；回撤接受才多|
|燃料油|FU2611；4476/4482；+2.68%/+15.13%|94.57万/21.19万/-7,446；back 15.84%、z2.27|C/context|4541；+3.39%/+4.03%；+11,454；**-1.43%**|油价+约1%；Y/N/N；不追、降级|
|低硫燃油|LU2611；5639/5624；+2.18%/+9.89%|14.13万/6.86万/-2,904；back 2.84%|缺失|5701；+3.37%/+3.58%；+2,463；**-1.09%**|Brent强；无成熟chain；相对SC偏弱|
|集运|EC2610；2034/2068.5；-2.15%/+8.36%|1.19万/2.44万/-2,046；back 27.31%|exact运价缺|制度无Night|航道风险仍在；N/N/N；今晚不交易|
|PTA|TA701；6460/6436；+0.63%/+6.38%|173.74万/116.93万/-8,222；near curve +2.16%|C；现货7045.25|6516；+2.58%/+1.88%；+16,071；-0.86%|成本支撑；Y/Y/N；不追|
|PX|PX611；9518/9490；+0.89%/+7.04%|40.96万/16.51万/+2,953；near curve +0.57%|C；现货9600|9632；+2.84%/+2.40%；+10,592；-1.18%|原油强；局部surface/N；等30m|
|苯乙烯|EB2611；9901/9874；+0.28%/+4.80%|41.65万/23.38万/+12,931；主力roll|C/context|代表合约为EB2610，不作分解|成本强；Y/Y/N；换月后观望|
|铜|CU2610；107030/106930；-1.16%/-3.02%|10.80万/18.01万/-7,753；back0.65%、z1.53|C；现货107675|106920；-0.85%/-1.17%；-3,283；+0.10%|LME日频14029.5；Y/Y/N；弱但不追空|
|黄金|AU2612；932.3/931.22；-1.62%/-2.84%|8.19万/16.92万/+4,086；轻contango|C/context|代表合约AU2610，不作分解|现货金约4266.5；Y/Y/N；实际利率压制|
|白银|AG2612；15452/15460；-1.85%/-4.80%|10.75万/20.27万/+3,017；轻contango|C/context|代表合约AG2610，不作分解|银约62.80；Y/N/N；不追空|
|玻璃|FG701；909/922；-2.33%/-4.65%|121.22万/123.73万/+19,098；near curve +1.67%|C；现货1008|926；-0.11%/-1.91%；+13,229；-1.84%|无exact外盘；Y/Y/N；弱势延续观察|
|纯碱|SA701；1009/1018；-1.83%/-4.95%|121.62万/128.16万/-9,665；near curve -0.81%|C；现货1090|1021；+0.20%/-1.54%；+8,204；-1.18%|无exact外盘；局部/N；不追空|
|碳酸锂|LC2701；129120/129640；-2.94%/-9.33%|18.72万/41.87万/+7,123；curve +1.15%|C；现货131000|制度无Night|无exact外盘；Y/N/N；不接第一刀|
|玉米|C2611；2208/2212；-1.07%/-3.41%|66.24万/113.54万/-9,817；contango1.12%|C/context|2213；-0.36%/-1.03%；-7,735；-0.23%|CBOT 532.5；Y/Y/N；WASDE多头继续否定|
|豆粕|M2701；3385/3374；-0.30%/-1.20%|118.40万/271.59万/+38,013；contango1.06%|C；现货3382|3381；+0.60%/-0.09%；-8,428；+0.12%|CBOT豆1299.75；Y/Y/N；价仓冲突|

19:30附近Reuters报价：Brent约107.35美元/桶、较前收约+1%，供应扰动仍支撑；美国10年期收益率约5.03%，美元继续走强，现货金约4266.49、银约62.80。[油价，2026-09-15](https://www.reuters.com/business/energy/oil-prices-rise-saudi-pipeline-outage-fresh-attacks-raise-supply-concerns-2026-09-15/)｜[美元与收益率](https://www.reuters.com/world/africa/dollar-near-two-week-high-oil-surge-lifts-yields-fed-hike-bets-2026-09-15/)｜[贵金属](https://www.reuters.com/world/india/gold-holds-ground-investors-await-fed-policy-cues-2026-09-15/)

## 四、相比今晨/上一晚报真正变化

1. **SC成为唯一获得日盘follow-through的核心能源品。** 早前Night相对close仅+0.77%，日盘再+2.08%；全日价涨仓增，说明新增定价发生在中国日间，但OI仅为归因线索。
2. **FU/LU夜强日弱。** 两者早前Night均约+3.4%，日盘分别回吐1.43%和1.09%；全日OI由夜盘增加转为收盘净下降，边际价格弹性明显低于晨间。
3. **SC双收益锚分歧仍大。** Night相对close仅+0.77%，相对settle却+5.80%；日盘close本已大幅偏离前结算，不能把+5.80%写成昨夜新增强势。
4. **EC多头触发被价格否定。** EOD close=2034、等于日低并低于晨间2035止损锚，OI下降7.73%；即使back升至27.31%，也不延续旧多卡。
5. **中国宏观是“生产强、需求弱”。** 8月工业产出同比+5.2%好于预期，零售仅+0.4%，1—8月固定资产投资-7.2%、地产投资同比-19.9%；这支持产业链分化，不支持广谱工业品多头。[Reuters，2026-09-15](https://www.reuters.com/world/china/chinas-factory-output-growth-quickens-in-august-retail-sales-slow-2026-09-15/)
6. **期权IV维持事件溢价。** SC/FU ATM IV约73.60%/72.29%，IV-RV约+29.38/+29.43vol；没有bid/ask，不能把“高IV”直接变成卖波动交易。

旧建议台账：

- `COM-E-SC2610-GAP-20260905`：77→81；继续以SC2611表达。新增原因是日盘follow-through与全日价涨仓增；原始失效框架不变，入场锚上移。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：84→73；Night后日盘回吐、全日减仓，原“产品强于原油”分歧未兑现；仅保留条件观察。
- `COM-M-LU2611-PRODUCT-RELATIVE-20260915`：78→69；日盘回吐与全日减仓使其仅剩两层有效支持。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：71→退出正式榜；价格变化触及旧止损锚，若此前已按条件建立，应按计划退出，不因事件叙事延期。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：68→69；Night跌后日盘横盘、全日减仓，趋势空仍受国内back反证。
- 没有成交反馈，不假设用户持仓；仅凭OHLC无法核实晨间条件是否实际成交。

## 五、产业链地图

- **最强：SC近端原油链，偏多，置信度高。** 第1层由Night弱增量转日盘强follow-through，第2层back仍7.71%，第4层Brent维持107上方；反证是curve较昨收窄、Physical缺失、第一跳拥挤。
- **FU—LU产品链：方向偏多但弹性衰减，置信度中。** Night先完成大部分涨幅，日盘回吐且全日减仓；FU back扩大支持，第3层实体与exact新加坡产品价缺失。
- **PX—TA—EB化工链：成本传导不均，置信度中。** PX价仓支持、TA/EB的全日结构混合，不能把原油上涨等同下游利润改善，也不构造未定义篮子。
- **最弱：FG—SA与LC，置信度中。** FG/LC价跌仓增，SA价跌仓减；C级现货基差只能提供context，缺库存变化与稳定curve历史，暂不建立确认空。
- **有色贵金属—农产品：宏观偏空但追价差。** CU/AU/AG受美元和5%美债收益率压制；C仍未确认WASDE，M/P价仓与海外映射冲突。

## 六、机会排行榜

|排名|机会|逻辑/赔率/催化/价曲波/仓技|总分|支持层|研究判断｜证据｜执行|
|---|---|---:|---:|---|---|
|1|SC2611回撤接受多|24/13/20/15/9|**81**|1、2、4|存在待验证优势｜充分但拥挤｜等待21:30—21:45|
|2|FU2611产品链恢复多|22/12/19/12/8|**73**|1、2、4|存在待验证优势｜部分、日盘反证｜等待30—45m|
|3|CU2610美元/关税回吐空|19/16/15/9/10|**69**|1、4|存在待验证优势｜部分｜等待反抽失败|
|4|LU2611产品相对强恢复|20/12/18/11/8|**69**|2、4|存在待验证优势｜部分、价仓反对｜等待30—45m|
|5|FG701弱势延续空|18/14/11/8/8|**59**|1|证据不足｜不足｜等实体/curve复核|

分项均已复算。SC/FU/LU共享供应因子，合并风险；CU/LU仅两层，封顶69；FG仅一层，封顶59。分数是研究排序，不是胜率或仓位。全部期货最大损失都不由计划止损限定。

## 七、前三名交易卡

### 1. SC2611｜条件多｜81

**事实：** T日OHLC=830/865.5/810.5/838.6，结算836.2；1D +7.69%、5D +25.74%，ΔOI +1,174，volume z=3.05；back7.71%。早前Night OHLC=830/865.5/817.7/821.5，vs close +0.77%、vs settle +5.80%、Night ΔOI -998；日盘follow-through +2.08%。

**市场定价：** 近端供应中断已高度计价。**分歧：** SC日盘重新获得定价权，强于FU/LU；竞争解释是人民币和结算机制放大涨幅、且管道恢复会迅速压缩溢价。

- 最佳表达：SC2611单腿条件多；今晚21:00有Night，归属9月16日。
- 好成交：21:30—21:45在825—836承接并重上840/VWAP，先1/3仓。
- 中成交：突破866后回踩858—866不破，仓位减半。
- 坏成交：直接高于875、止损距离超过1R或滑点超过1R的20%，放弃。
- 止损：30分钟接受818下方；逻辑失效：跌破810.5、back低于6.5%、Brent低于103，或East-West管道确认恢复。
- 退出：TP1 866或+1.5R；TP2 900或+3R；1—2D不扩张退出。
- 风险：0.20%—0.30% NAV；SC/FU/LU合并初始≤0.50%。
- 参数：1,000桶/手，tick0.1元/桶，tick value100元；按结算名义836,200元。最后交易日10月30日，实物交割；10月中旬前复核移仓。
- margin动态值未确认；按16%压力假设，一板约133,792元/手，两板复合约246,177元/手。下单前按[INE合约规则](https://www.ine.cn/eng/market/futures/energy/sc/contract/)核验。

### 2. FU2611｜恢复型条件多｜73

**事实：** T日OHLC=4450/4549/4403/4476，结算4482；1D +2.68%、5D +15.13%，ΔOI -7,446；back15.84%、z2.27。Night close4541、vs close +3.39%、vs settle +4.03%、Night ΔOI +11,454；日盘-1.43%，说明Night强势未获日盘延续。

- 市场可能错在产品短缺比原油更持久；最强竞争解释是高back来自近端挤压，价格反弹伴随全日减仓。
- 好成交：21:30后4420—4470承接并重上4485/VWAP，且相对SC不再走弱，先1/3仓。
- 中成交：突破4550并回踩成功，仓位减半；直接高于4620为坏成交。
- 止损：30分钟接受4395下方；失效：跌破4392、back低于12%、Brent低于103或FU/SC继续走弱。
- TP1 4550或+1.5R；TP2 4700或+3R；1—3D无扩张退出。
- 风险0.15%—0.25% NAV，与SC/LU合并；若SC卡触发，FU不再独立叠加满额。
- 10吨/手，tick1元/吨，tick value10元；结算名义44,820元。margin/limit未确认；最后交易日10月30日，实物交割。
- 一板压力=`44,820×L`；两板=`44,820×[1-(1-L)^2]`，L下单前核验。

### 3. CU2610｜反抽失败条件空｜69

**事实：** T日OHLC=106900/107410/106650/107030，结算106930；1D -1.16%、5D -3.02%，ΔOI -7,753；back0.65%、z1.53。Night close106920、vs close -0.85%、vs settle -1.17%、Night ΔOI -3,283；日盘+0.10%，下跌主要在早前Night完成。

- 市场隐含：美元与高收益率压制、美国关税溢价回吐。分歧是反抽若不能重上108000，仍有下探空间；反证是国内back和减仓下跌、工业产出好于预期。
- 好成交：21:30—21:45反抽107300—107800失败并重新跌破107000，先1/3仓。
- 中成交：跌破106650后回抽不过，仓位减半；直接低于106000为坏成交，放弃追空。
- 止损：30分钟接受108050上方；失效：重上108190、back扩大至1%以上且LME同步转强。
- TP1 106000或+1.5R；TP2 104500或+3R；1—3D时间止损。
- 风险0.20%—0.25% NAV。具体multiplier/tick/margin/limit虽常规可查，但repo动态参数不全，本期不编精确一板/两板金额；临近2610交割，最迟9月下旬复核移仓。

## 八、商品期权专项

9月15日T日截面已更新，但全部series `execution_ready=false`。

|Underlying/expiry|ATM IV/RV20|IV-RV|RR25/BF25|S/P/E|结论|
|---|---:|---:|---:|---|---|
|SC2611/10-14|73.60%/44.23%|+29.38vol|-2.59/+1.64|Y/N/N|事件凸性很贵，不裸追call|
|FU2611/10-19|72.29%/42.86%|+29.43vol|-3.63/+2.14|Y/N/N|Night后日盘回吐，先重报价|
|TA701/12-11|34.97%/26.15%|+8.82vol|+3.49/+1.27|Y/Y/N|可研究，不可执行报价|
|FG701/12-11|22.42%/25.35%|-2.93vol|+5.66/+1.87|Y/Y/N|IV-RV负不单独证明便宜|
|CU2610/09-23|15.93%/14.48%|+1.44vol|-3.91/+1.02|Y/Y/N|近到期、交割风险优先|
|AU2612/11-24|25.73%/21.95%|+3.78vol|+2.75/+1.07|Y/Y/N|信用主题仍未闭环|
|AG2612/11-24|46.45%/35.08%|+11.37vol|+5.80/+1.37|Y/N/N|上行尾仍贵|
|LC2701/12-07|45.61%/38.99%|+6.61vol|+1.84/+0.88|Y/N/N|跌势中不裸卖put|

只有取得人工实时双边报价后，才比较SC/FU同到期1:1 call spread与线性期货；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点和行权交割参数均待报价。Dealer Gamma方向未知。Vol RV仅可研究FG相对SC/FU的表面价差，未完成相关性与成交成本对齐，不是可执行跨品种波动套利。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、21:00夜盘开盘风险地图

严格四层：①9月15日中国EOD；②9月14日晚至15日凌晨、属于9月15交易日的已完成Night；③15:00—19:30外油续涨、美元与美债收益率高位、金银偏弱；④今晚21:00尚未发生，归属9月16日。

|品种|EOD→早前Night→日盘→海外|21:00预期/冲突|追价/等待|开盘确认|
|---|---|---|---|---|
|SC|Night+0.77%→日盘+2.08%→Brent+约1%|偏高；中国日盘已预交易较多|不追；30—45m|825/836/840/866、back、Brent|
|FU|Night+3.39%→日盘-1.43%→油价续涨|平/小高开；内弱外强|不追；30m|4420/4485/4550、FU/SC|
|LU|Night+3.37%→日盘-1.09%→油价续涨|偏高但弹性下降|30—45m|5600/5700、OI、相对SC|
|TA/PX|Night+2.58/+2.84%→日盘回吐→油强|小高开，成本已部分交易|30m|TA6460/6532、PX9630、EB breadth|
|EB/BZ/EG|换月/价仓混合→上游强|高开后回吐风险|45m|结算、OI、主力切换|
|CU/ZN/AL|Night弱→日盘未扩张→美元强|低/平开|不追空；30—45m|CU106650/107800、LME、back|
|AU/AG|代表Night合约不同→T日大跌→海外仍弱|偏低|不追；30m|DXY、10Y、实际利率、skew|
|FG/SA|Night近零→日盘显著下跌|低开或技术反抽|不追空；30m|FG908/922/932、SA1009、OI|
|C/M/P/Y/OI|Night与日盘混合→CBOT/BMD偏强|平/分化|45m|C2204、M3390、进口映射|
|EC/LC/AP/JD/SF/SM/SI/PS|制度无Night|今晚不交易|9月16日09:00后30—45m|量仓、curve、实体更新|

单日噪音优先：JM结算+1.89%但收盘仅+0.06%、M结算跌而收盘近持平、P夜盘涨而日盘回吐。最不值得交易：追SC/FU首跳、低开追空FG/LC/AU/AG、继续做EC事件多、以及无bid/ask的期权。

## 十、未来24小时与7日事件

- 9月15日21:00：下一合法Night；能源先等30—45分钟，SC/LU/FU相关保证金与限幅必须下单前核验。
- 未来24h：East-West管道修复、Hormuz/Perim通航与Saudi出口库存；恢复会同时压缩SC/FU/LU/EC风险溢价。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-rise-saudi-pipeline-outage-fresh-attacks-raise-supply-concerns-2026-09-15/)
- 9月16日22:30附近：EIA周报；SC/FU提前减仓，期权仅在取得报价后使用有限净支出。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月17日02:00附近：FOMC/SEP；市场高度押注加息，CU/AU/AG降低Delta/Vega，禁止跨事件裸卖波动。[Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 未来7日：关注中国地产与投资政策、交易所风控、SC/FU/EC到期滚动；CFTC COT只作滞后拥挤背景。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 农产品：USDA出口销售、北美收割天气和中国采购兑现；高燃料运输成本可能改变basis，但不直接等于期货方向。[Reuters铁路燃油成本](https://www.reuters.com/business/retail-consumer/us-rail-fuel-surcharges-grain-hit-record-highs-squeezing-farmers-harvest-season-2026-09-14/)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月15日EOD、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差/跨期、跨品种/跨市场、加工利润、风格/中性、波动率、偏度和事件凸性扫描；另纳入动态品种，共77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为占位，RS/WR流动性不足，均保留覆盖记录。
- 黑色建材9/9：FG价跌仓增最异常；JM结算与收盘分歧，I/RB曲线或roll不稳定。
- 有色贵金属12/12：CU入榜；AU/AG在高收益率下弱，黄金信用主题不成立。
- 能源炼化化工25/25：SC/FU/LU入榜；SC强于产品，PX强于TA/EB但日盘弹性衰减。
- 新能源及GFEX新材料全部扫描：LC价跌仓增，但缺A级实体和exact海外确认。
- 农产品油脂饲料畜牧22/22：C继续否定WASDE多头；M/P/Y/OI无三层共振。
- 航运及软商品全部扫描：EC旧多退出；CJ期权链仍不足。
- Night应覆盖802个合约、实际579条有效、55产品；216 outside-window和7 no-trade均非错误。
- 期权应覆盖64产品、实际58；6个产品不足，0个execution-ready。
- A/B级basis、exact import parity、可靠加工利润、完整beta-neutral篮子和可执行期权报价均不可得；不发布伪套利。

风险预算：单笔试仓最大损失0.15%—0.30% NAV；只有新一段Night价格、curve与非价格层确认后才提高至0.75%—1.0%。SC/FU/LU初始合并≤0.50%，中东供应主题总风险仍≤2.5%。压力测试包含16%一板/两板复合、管道突然恢复、夜盘gap、流动性消失、保证金上调、相关性破裂、IV跳升/塌陷、交割挤压与人民币急变。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2611在21:30—21:45于825—836承接并重上840；FU2611仅4420—4470承接、重上4485且不再弱于SC时试仓，主题合并风险≤0.50%。  
C. 今晚应继续观察的机会：LU2611恢复强度、CU2610反抽失败空、FG701弱势延续、PX强于TA/EB，以及SC/FU期权实时重报价。  
D. 今晚必须避免或退出的交易：追SC/FU/LU第一跳、继续执行EC2610旧多卡、低开追空FG/LC/AU/AG、把C级basis称套利，以及在execution-ready=false时臆测期权成本。

