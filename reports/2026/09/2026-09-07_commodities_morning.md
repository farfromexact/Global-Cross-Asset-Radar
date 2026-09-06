# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-07

`prompt_version=radar_2026-09-06_coverage_v1`  
生成/研究截点：2026-09-07 07:02:39 北京时间；最近完整中国EOD：2026-09-04；下一实际交易窗口：2026-09-07 09:00中国日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC2610、BR2611与V2701存在待验证优势，但周末事件与夜盘语义异常令9:00首跳赔率不合格。**

当前regime是：**地缘供给右尾 + 周一开盘价格发现真空 + 橡胶链夜盘挤压 + 国内材料曲线分化 + 高实际利率压制贵金属**。有研究机会，没有开盘即追价的确认交易。

## 二、数据质量与覆盖

第一读取层均来自 [China-Commodities-Engine main](https://github.com/farfromexact/China-Commodities-Engine)：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`；为核实具体合约与曲线，再下钻 `data/latest.json`、`data/night_session/latest.json`、`data/contract_meta.json`。统一输入 `schema_version=2`、`requested_date=2026-09-04`、`generated_at=2026-09-07T06:12:06+08:00`。[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)

- Futures/Market State：9月4日五所SHFE/INE/DCE/CZCE/GFEX共802合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；6条placeholder已排除。周末没有应得的新EOD，9月4日last-good仍有效。[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- Physical：9月4日，20个目标中18个fresh、SC/LU两项unavailable，validation/published均通过；现货/basis多为C级、缺地区/品质/含税/交割地精确对齐，只作context，不计可执行套利或完整实体层。
- External：repo日频为9月4日17/22个series有效，均为`context_only`；07:00海外另行刷新。LME周末未开，官方最新仍为9月4日；人民币代理接近不变。
- Options：最新有效9月4日截面，19,394个合约、352个series、52/64品种；IV coverage 97.71%、OI coverage 68.21%、bid/ask coverage=0。全局 `surface_ready=false`、`positioning_ready=false`、`execution_ready=false`；341个本地series可研究surface、74个可研究positioning、0个可执行。BC/SC及SHFE的AD/AG/AL/AO/AU/CU/NI/PB/SN/ZN共11个品种失败。Dealer Gamma方向未知。[期权质量](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- Contract metadata：`quality_state=partial`；有效合约匹配73.32%，multiplier/tick/margin/limit覆盖仅29.80%，night-session字段覆盖0。交易卡缺少的动态保证金、限幅不推断，下单前必须查交易所/经纪商。

### Night Session日历审计

本次module-specific状态写的是 `trading_date=2026-09-07`、`night_session_date=2026-09-06`、05:58生成，802条全部`outside_night_window`，0条具体报价，`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=true`；这准确反映**周日没有中国夜盘**，不是行情缺失。[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)

但仓库保留的上一有效逐合约快照将周五21:00—周六凌晨标成 `trading_date=2026-09-05`。按交易所规则，夜盘属于随后实际交易日，且周一9月7日正常开市，因此原标签违反交易日语义。处理方式是：**不改写原数据、不把标签冒充正确；隔离其`trading_date`字段，只把时间戳位于9月4日21:00至9月5日凌晨、且与9月4日EOD exact-contract对齐的记录，作为周一开盘前的`night_session_fallback=true`降级证据。** 上期所明确夜盘属于下一交易日；周一不是假期。[交易时段](https://www.shfe.com.cn/eng/reports/CalendarHolidays/TradingHours/) [节假日日历](https://www.shfe.com.cn/eng/reports/CalendarHolidays/Holiday/)

该快照原始采集611个夜盘合约、55个品种，188个合法outside-window、3个no-trade，missing timestamp/price/quote、query error、unresolved contract均为0。**77.1%的表面覆盖不是缺失率。** 由于日历标签错误，所有依赖该段Night证据的候选最高不超过79分。

## 三、商品仪表盘（展示13项，扫描不限于此）

EOD收益均为同一具体合约的结算收益；Night强弱以`vs previous close`为主、`vs settlement`为辅助。成交/持仓单位均为手；曲线为近月减次月的百分比快照；C级basis不计方向证据。

| 板块 | 合约 | 9/4 close/settle；1D/5D | EOD Vol/OI/ΔOI；Curve | Physical/Basis | 周五Night close；vs close/settle；ΔOI；时间 | 07:00海外/Options | 9:00信号 |
|---|---|---|---|---|---|---|---|
| 原油 | **SC2610** | 685.2/683.1；-1.13%/+15.33% | 161.9k/35.8k/-1,266；BWD 5.40% | SC unavailable | 690.7；+0.80%/+1.11%；+2,486；9/5 02:30 | WTI约92.14、Brent约96.90，均较周五高；SC期权失败 | **30m gap接受/失败** |
| 合成橡胶 | **BR2611** | 14810/14860；-0.13%/+3.81% | 63.8k/82.4k/+2,232；BWD 0.34% | 无完整层 | 15590；**+5.27%/+4.91%**；+10,293；9/4 23:00 | 海外天然胶9/4近乎持平；BR IV36.60%、exec false | **45m验真，不追** |
| 天然橡胶 | RU2701 | 18700/18770；+0.27%/-0.21% | 319.5k/152.8k/-73；近月约平 | 无完整层 | 19155；+2.43%/+2.05%；+11,151；23:00 | JPX最新周报偏多但超买；exec false | 等30–45m |
| 20号胶 | NR2611 | 15845/15875；0.00%/-0.44% | 70.3k/73.2k/+287；Contango -1.44% | 无完整层 | 16340；+3.12%/+2.93%；+7,216；23:00 | SGX最新完整日频无周一新增；exec false | 曲线反证，等45m |
| PVC | **V2701** | 5128/5040；+3.07%/+11.50% | 2.67m/1.13m/+91,245；**Contango -2.03%，z=-3.55** | 无完整层 | 5072；**-1.09%/+0.63%**；-32,897；23:00 | V ATM5000 IV22.24% vs RV25.34%，无报价 | **30–45m failed-squeeze** |
| 硅铁 | SF611 | 6624/6564；+5.06%/+8.42% | 1.34m/482.9k/+20,817；BWD 2.74% | 无高质实体层 | 制度无夜盘，不适用 | IV32.21% vs RV19.54%，exec false | 回撤吸收，不追高 |
| 纯碱 | SA701 | 1093/1080；+1.79%/+5.16% | 2.39m/1.22m/+21,206；Contango -5.17% | C-context | 1110；+1.56%/+2.78%；-6,571；23:00 | 本地surface可研究但标的锚不一致；exec false | 价格强/曲线弱 |
| 黄金 | AU2610 | 965.96/970.82；+1.97%/-2.31% | 274.2k/158.4k/-5,012；近月约平 | 无完整层 | 958；-0.82%/-1.32%；-671；9/5 02:30 | 现货金约4429，周末重开近乎持平；AU期权失败 | 等15–30m |
| 白银 | AG2610 | 16250/16318；+2.24%/-2.97% | 467.0k/207.8k/-8,580；轻Contango | 无完整层 | 16080；-1.05%/-1.46%；-2,052；02:30 | 银价约66附近；AG期权失败 | 不抢反弹 |
| 燃料油 | FU2611 | 3841/3872；+0.21%/+5.50% | 800.0k/205.9k/-8,182；BWD 6.30% | C-context | 3793；-1.25%/-2.04%；-17,407；23:00 | 油涨但FU先弱；IV55.86% vs RV38.81%，exec false | 看SC-FU分化 |
| 乙二醇 | EG2610 | 5898/5844；+0.57%/+16.18% | 1.79m/392.5k/+16,269；BWD 6.84% | 无完整层 | 5866；-0.54%/+0.38%；-29,036；23:00 | IV54.57% vs RV38.14%，exec false | 趋势强、弹性降 |
| 豆粕 | M2701 | 3423/3402；+0.47%/+1.73% | 1.78m/2.90m/+98,877；Contango -0.62% | C-context | 3419；-0.12%/+0.50%；-32,719；23:00 | CBOT周末无新完整时段；IV15.42% vs RV9.67% | 无方向edge |
| 航运 | EC2610 | 1860.5/1856.5；+0.54%/-0.54% | 10.9k/23.9k/-335；远月对比不可当套利 | 不适用 | 制度无夜盘 | 无可靠实时映射/无期权 | 不交易单日噪音 |

07:00海外：Brent Nov约96.90、较周五96.28约+0.64%，WTI约92.14、较周五91.48约+0.72%；不同供应商/合约月份存在小差异，故只作SC开盘gap映射，不称exact parity。[Brent futures](https://oilprice.com/futures/brent) [周五收盘](https://markets.businessinsider.com/commodities/oil-price) 美元兑离岸人民币约6.7076、变动很小，人民币不是今晨主要驱动。[USD/CNH](https://www.investing.com/currencies/usd-cnh) LME最新官方价仍是9月4日：铜14370.5/14371、铝3292/3292.5美元/吨，今晨没有新的LME时段可与中国Night逐笔对齐。[LME官方价格](https://www.lme.com/market-data/reports-and-data/lme-official-prices)

## 四、相比上一期真正变化

1. **SC由“周末新闻观察”升级为78分条件候选，但仍非立即多。** 美国确认打击三艘伊朗油轮、伊朗又宣布霍尔木兹附近排除区，OPEC+决定10月维持9月产量要求；周一重开的Brent/WTI小幅上行。新增的是事件与海外价格，不是中国SC已经交易了周末消息。[OPEC官方](https://www.opec.org/pr-detail/613-6-september-2026.html) [排除区报道](https://apnews.com/article/a52beec77dc90af3d040d0553837ad20)
2. **最强中国Night异常换成橡胶链。** BR2611相对9月4日close跳5.27%、RU +2.43%、NR +3.12%；BR的OI增量和小幅backwardation提供两层支持，但海外天然胶9月4日仅-0.04%、JPX周报提示超买回撤风险，实体层缺失，因此不能把链内共振写成已确认供需短缺。[海外橡胶](https://tradingeconomics.com/commodity/rubber) [JPX周报](https://www.jpx.co.jp/derivatives/products/rubber/RubberFuturesInformation/nlsgeu0000057mti-att/JPX-The_Weekly_Rubber_Futures_Report_EN_31082026.pdf)
3. **V的多头挤压出现可验证的失败迹象。** 9月4日close比settle高很多，Night相对close跌1.09%、ΔOI -32,897，同时EOD曲线深contango；相对settle仍+0.63%，说明它是高位回吐，不是趋势空已经确认。
4. **SA与V进一步分化。** SA Night相对close仍+1.56%，却伴随OI下降、近月contango更深；价格支持延续，结构反对“现货短缺牛市”。
5. **贵金属的黄金信用本期没有成立。** 强非农后的AU/AG Night下跌；周末地缘升级后国际金重开仅近乎持平，说明安全资产买盘尚未压过高利率/美元约束。最强竞争解释是市场已把战争溢价计入，或油价通胀冲击反而抬高实际利率预期。
6. **此前未登记晨报的旧数值被最新统一快照纠正。** 9月4日早期稿里的EB2610 night close=9770不再沿用；当前repo exact-contract是9月4日EOD close/settle=9612/9677，随后Night=9660，仅+0.50% vs close、-0.18% vs settle，芳烃不再居首。此变更属于数据更新/纠错，不是观点无故反转。

## 五、产业链地图

1. **最强事件链：原油—炼化，方向右尾、置信度中高。** SC EOD 5D +15.33%、backwardation 5.40%，Night curve扩大至约5.77%，周一外油小幅上行；但SC实体数据unavailable、SC期权失败，且Reuters的最强反证是替代供应和市场适应令伊朗的霍尔木兹杠杆减弱。交易edge是gap接受/拒绝，不是“新闻大所以追多”。[Reuters反证](https://www.reuters.com/business/energy/irans-hormuz-leverage-wanes-us-economic-squeeze-bites-2026-09-06/)
2. **最强价格异常链：BR—RU—NR，方向偏多、置信度中。** BR价格/OI与夜盘近月back共同支持；NR曲线反而加深contango，海外天然胶并未同步跳升。合成胶受原油/原料成本影响属于映射推断，不是exact parity；先验更像周一待验证的仓位挤压。
3. **最强国内日盘链：SF—SA—V，方向分化、置信度中低。** SF价格、成交、OI、backwardation最一致，但无夜盘与新实体催化；SA价格延续而curve反对；V Night回吐且curve最弱。宽泛“材料整体多”已不成立。
4. **聚酯/燃料链：趋势强、边际弹性弱。** EG/MA/FU相对close均弱于EOD，且backwardation普遍收窄；若9:00原油高开而下游不跟，应把上涨理解为原油地缘premium，而不是全化工供需改善。
5. **最弱/最缺edge：农产品与航运。** M虽EOD增仓，但Night相对close略跌，CBOT/ICE/SGX农品在截点前没有可比的新完整时段；EC缺海外exact映射且无期权。没有方向优势，不等于数据不存在。

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

| 排名 | idea_id / 机会 | 分项：逻辑/赔率/催化/价曲波/持仓技术 | 总分 | 有效支持层；反证/缺失 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | `COM-E-SC2610-GAP-20260905` SC2610 gap接受多/failed-gap空 | 22/18/19/11/8 | **78** | 1价格、2曲线、4海外宏观；缺3实体、5期权；Night标签降级 | 存在待验证优势｜部分｜等待9:00后30m |
| 2 | `COM-M-BR2611-NIGHT-SQUEEZE-20260907` BR2611夜盘挤压验真 | 18/14/12/12/12 | **68** | 1价格仓位、2曲线；海外天然胶反对，实体缺失，T-1期权moneyness过时 | 存在待验证优势｜部分｜等待45m |
| 3 | `COM-E-V2701-SQUEEZE-20260904` V2701 failed-squeeze空 | 19/17/10/11/10 | **67** | 1Night回吐、2深contango；EOD强势反对，期权无报价 | 存在待验证优势｜部分｜等待30–45m |
| 4 | `COM-E-SF611-PULLBACK-20260904` SF611回撤吸收多 | 19/16/8/13/10 | **66** | 1价量仓、2backwardation；缺Night属制度不适用，缺实体/海外 | 存在待验证优势｜部分｜等待日盘回撤 |
| 5 | `COM-E-AU2610-RATE-GEO-20260905` AU2610地缘避险失败空 | 18/17/12/9/9 | **65** | 1Night弱、4宏观弹性弱；地缘右尾反对，期权失败 | 存在待验证优势｜部分｜等待15–30m |

分数已逐项复算；两层候选均≤69。SC虽有三层、达到70+研究门槛，但Night语义异常、缺实体和期权执行层，仍不能在开盘前下条件不明的新仓。

### 旧建议台账

manifest中研究截点前最近**已登记**的同版商品晨报是2026-09-01；9月6日`latest/commodities_morning`仅作未登记/partial修订参照，不冒充已发布前序。最近正式商品晚报为9月6日。SC沿用9月5日首次提出的idea，晚报76→本晨78，原因是OPEC+与周一外油新数据；V沿用9月4日idea，55→67，原因是exact Night回吐与曲线确认；SA仍观察但因OI/curve反证未入榜；BR为本期新异常。没有成交回报，**不假设用户已经持仓或旧条件单已成交**。

## 七、前三名交易卡

### 1. SC2610｜gap接受多 / failed-gap空｜78｜条件候选

**事实：** 9/4 OHLC 695.5/699.0/665.4/685.2，settle 683.1；1D -1.13%、5D +15.33%，ΔOI -1,266。降级Night exact-contract为678.0/696.0/666.7/690.7，+0.80% vs close、+1.11% vs settle，ΔOI +2,486；近次月back从5.40%扩大至约5.77%。07:00 WTI/Brent较周五约+0.6%—0.8%。

**市场隐含：** 周末供应冲击应带来高开，但替代供应和航运适应限制均值上移。**我们的分歧：** 方向本身未必错，错误更可能在高开后的“接受程度”。催化是OPEC+不增产、排除区与油轮打击；最强反证是冲突未进一步减少可交割流量，或外油开盘涨幅快速回吐。

**最佳表达：** SC2610期货，先双向观察；SC期权链失败且无live quote，不声称Call Spread更优。

- 好成交：09:00 gap不超过降级Night close约1.5%（约701）且30分钟守住690.7，突破opening-range high后1/3多；初始止损为30分钟重新接受690.7下方。
- 中成交：701—710只在回踩不破、外油继续走强时参与，仓位减半；TP1 1.5R、TP2 3R。
- 坏成交：直接高于约725或止损距离超过风险预算，放弃追多。若高开后跌破690.7、反抽失败且Brent/WTI同步回吐，可用1/3仓做failed-gap空，止损为重回opening-range high。
- 逻辑失效：多头为跌破665.4并且backwardation收窄；空头为重新接受699且外油扩张。时间止损1—3D；分批在1.5R减半、3R再减，余仓跟随opening-range低/高。
- 风险：试仓最大损失0.25%—0.50% NAV；事件+价格+实体再确认后才可至≤1.0%。期货止损不等于最大损失有限；gap、流动性消失和涨跌停会穿透止损。

合约参数：1000桶/手，tick 0.1元/桶，tick value 100元/手；按683.1结算名义约683,100元/手。标准最后交易日为交割月前一月最后交易日，实物交割；repo显示SC2610预计9月30日进入关键到期窗口，须提前roll/exit。[INE标准合约](https://www.ine.cn/products/) 动态margin/limit本版未确认；一板压力=`683,100×L`，两板同向=`683,100×[(1+L)^2−1]`。

### 2. BR2611｜夜盘挤压验真多｜68｜低分研究卡

**事实：** 9/4 OHLC 14850/15015/14715/14810，settle 14860；EOD ΔOI +2,232、5D +3.81%。降级Night OHLC 14760/15595/14660/15590，+5.27% vs close、+4.91% vs settle，ΔOI +10,293；BR2609/2610的近月back约0.34%→0.38%，只算同产品曲线支持，不冒充BR2611自身月差。海外天然胶9/4仅-0.04%，并未确认这5%跳升。

**市场隐含：** 夜盘把成本/供应或仓位冲击一次性计价。**我们的分歧：** 证据不足以区分产业短缺和挤仓，最强竞争解释是低流动性时段跨品种追价。选择期货只是为了等待价格验真；期权T-1 ATM IV36.60%、RR25 -3.92，但夜盘后moneyness已明显变化、execution=false，不能据此成交。

- 入场：至少等45分钟。好成交为回撤至15250—15450后守住、重上15590/VWAP再1/3多；中成交为15600—15800横盘后上破opening-range high，仓位减半；坏成交为直接>16000，放弃。
- 初始止损：45分钟接受<15150；逻辑失效：跌破14860且RU/NR同步回吐、近月back转为明显contango。TP1 1.5R、TP2 3R；时间止损1—2D。
- 最大风险：跳空后流动性消失、三胶相关性破裂、油价回吐、做多拥挤反身性。试仓最大损失0.25%—0.35% NAV；BR/RU/NR合并为同一因子。

合约参数：5吨/手，最新业务细则tick 5元/吨，tick value 25元/手；按Night close名义约77,950元/手。最后交易日规则为交割月15日（节假日顺延），实物交割，BR2611 exact日期及动态margin/limit须下单前复核。[上期所BR业务细则](https://www.shfe.com.cn/regulation/exchangerules/productrules/202512/t20251231_829967.html) 一板/两板压力分别=`77,950×L`、`77,950×[(1+L)^2−1]`。

### 3. V2701｜failed-squeeze空｜67｜条件候选

**事实：** 9/4 OHLC 4900/5154/4883/5128，settle 5040；EOD settle +3.07%、5D +11.50%、ΔOI +91,245，但near-next contango -2.03%、z=-3.55。降级Night OHLC 5115/5144/5053/5072，-1.09% vs close、+0.63% vs settle，ΔOI -32,897。双锚分歧说明“相对日盘收盘转弱”，不是“相对结算已经转空”。

**市场隐含：** 日盘short squeeze仍有余温。**我们的分歧：** 若9:00不能重夺5072—5128，高位持仓回吐与深contango可能形成二次负反馈；最强反证是5040/5053获得承接、OI重新增加并上破5154。

- 入场：等30—45分钟。好成交为反抽5072—5100失败后跌破5040；中成交为先破5040再回抽不回，仓位减半；坏成交为直接低开<4950，不追空。
- 初始止损：30分钟重新接受5128上方；逻辑失效：上破5154且OI扩张、contango明显收窄。TP1 4920、TP2 4800；1—2D时间止损；1.5R减半、3R再减。
- 风险：空头最大损失不由结构限定；高开、再度挤仓和涨停可穿透止损。试仓最大损失0.25%—0.35% NAV。

合约参数：5吨/手，tick 1元/吨，tick value 5元/手；按Night close名义约25,360元/手。最后交易日为合约月份第10个交易日，实物交割；动态margin/limit与V2701 exact日期未确认。[大商所PVC合约](https://www.dce.com.cn/dce/channel/list/2160.html) 一板/两板压力=`25,360×L`、`25,360×[(1+L)^2−1]`。

## 八、商品期权专项

结论：**期权不优于裸期货，因为执行层不是“价格贵”，而是不存在可验证bid/ask。** 全局surface/positioning/execution均false，bid/ask=0；可研究的本地series不等于全局ready，更不等于当前成交。

- BR2611相关T-1 series：ATM约14800、IV36.60%，相对RV20 27.73%高约8.86 vol；RR25 -3.92、BF25 1.39。本来提示下行skew/有限损失结构价值，但Night后标的+5.3%，ATM与Delta已过时，只作历史背景。
- V2701：ATM5000、IV22.24% vs RV25.34%，IV-RV约-3.10 vol，RR25 +3.71、BF25 1.37；surface/positioning可研究但execution=false，不能据此说Call便宜或Put贵。
- SF611：IV32.21% vs RV19.54%，波动率显著偏贵；如果价格触发，更偏期货小仓而非盲买期权，但仍需当前报价比较。
- SC/AU/AG：品种链失败，event convexity只能定性；不输出expiry/strike/权利金/Greeks。dealer_gamma_direction_known=false，禁止Gamma方向推断。

## 九、9:00开盘风险地图

三层必须分开：**Layer 1是9月4日中国EOD；Layer 2是周五21:00—周六凌晨逐合约快照（原标签错误，按日历降级为周一前夜盘替代证据）；Layer 3是周一07:00海外。** 周末油轮/OPEC+消息发生在Layer 2之后，尚未被中国价格交易。

| 合约 | 预期 | 是否已在Night定价 | 内外盘冲突 | 追价？ | 等待 | 开盘确认 |
|---|---|---|---|---|---|---|
| SC2610 | 高开/宽幅 | **未定价周末新增** | Night仅+0.8%，外油重开再涨 | 否 | 30m | 690.7/699接受、外油、近月back |
| BR2611 | 明显高开 | 大量 | 中国Night强、海外天然胶未确认 | **绝不首跳追** | 45m | 15590/VWAP、OI、RU/NR、curve |
| RU2701 | 高开 | 大量 | JPX先验偏多但超买 | 否 | 30–45m | 19155接受、跨胶breadth |
| NR2611 | 高开 | 大量 | 价格强/contango加深 | 否 | 45m | curve是否修复、SGX |
| V2701 | 平/偏低 | 夜盘否定日盘收盘 | 无可靠海外锚 | 否 | 30–45m | 5040/5072/5128、OI |
| SF611 | 平/高开不确定 | 无夜盘（制度） | 无海外锚 | 否 | 30m | 6564—6624吸收、back |
| SA701 | 高开 | 较多 | 价格强/curve弱 | 否 | 30–45m | 1110接受、contango、OI |
| AU/AG | 平/偏低 | 强非农已部分定价 | 周末地缘未带来明显海外金涨 | 否 | 15–30m | 958/16080、美元、实际利率 |
| FU/EG/MA | 平/分化 | 大量 | 原油涨、下游Night弱 | 否 | 30–45m | 是否跟SC、curve、OI |
| M/油脂 | 平 | Night弹性低 | 海外无新完整时段 | 否 | 30m | CBOT重开、人民币 |
| EC | 平 | 无夜盘 | 无exact海外映射 | 否 | 45m | opening range、成交量 |

## 十、未来24小时 / 7日事件日历（北京时间）

- **9月7日09:00：中国周一日盘。** SC看周末事件gap接受；BR/RU/NR看Night挤压验真。优先延迟入场，不在第一跳承担无限Delta。
- **9月9日：中国8月CPI/PPI窗口。** 市场日历通常指向09:30，但本报告未从NBS核实精确发布时间；黑色、化工、有色仓位当天开盘前再确认。
- **9月10日09:00：上期所HC/SS期权、INE LU期权上市。** 新品种首日surface、skew与流动性需重新建立，不用首日报价做历史IV-RV结论。[SHFE公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html) [INE公告](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)
- **9月10日20:30：美国8月PPI；9月11日20:30：美国8月CPI。** AU/AG与油价的Delta/Vega会重置；数据前若已有盈利，减半并把剩余风险限定在0.25% NAV以内。[BLS日历](https://www.bls.gov/schedule/2026/home.htm)
- **9月11日00:00/02:00：EIA周度石油数据分批发布。** 因美国9月7日政府停闭，EIA官方将报告移至美东9月10日12:00/14:00。SC/FU/LU避免把战术仓无意识持有成库存赌注。[EIA官方](https://www.eia.gov/petroleum/supply/weekly/)
- **9月11日约16:00：IEA Oil Market Report窗口**（精确北京时间执行前复核）；关注替代供应与航运恢复是否验证Reuters的反证。
- **9月12日00:00：USDA WASDE；约03:30：CFTC COT常规窗口。** WASDE前M/Y/P/OI/CBOT相关Delta宜降低；COT只作截至周二的拥挤背景，不解释当日价格。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- 地缘24小时连续：霍尔木兹排除区、油轮/护航、Kharg与航运流量。若新闻被否认或油流恢复，SC/BR的右尾会迅速塌缩；没有可靠live期权报价时，不用期权“有限损失”叙事掩盖昂贵Vega。

## 十一、覆盖核对、风险与归档

### 覆盖核对

- **应覆盖：** 强制63个不同代码全部保留；另扫描动态流动性合格PL/PD/PT/BZ/LG/RR/OP/WR，共71个期货品种。方向、1/3/5/20D、curve、basis/仓单、产业链、跨品种/跨市场、风格/中性篮子、期权vol/skew/event convexity均完成可得数据初筛。
- **实际取数且已分析：** 强制63/63；动态8/8；五所802合约；可用商品期权52/64。逐板块：黑色建材9、贵金属有色12、能化21、新能源3、农品17、航运EC 1，全部有期货层分析。
- **数据不足：** SC/LU实体层unavailable；无A级/B级exact basis/import parity；期权11个品种失败且全市场0个execution-ready；contract metadata仅partial；Night交易日标签异常。缺口限制相应层/工具，不抹去方向异常。
- **不适用/流动性不足：** JR/PM/RI/RS/WH/ZC在动态清单中为零成交、零持仓或制度性非活跃，未用于排行；SF/SM/LC/SI/PS/EC等无Night属制度不适用，不计缺失。

未入榜板块最值得跟踪：黑色看I/JM/J的夜盘温和走强是否扩散到RB/HC；有色看ZN夜盘+0.97%能否获LME现货/库存确认；能化看FU与外油背离；新能源LC仍弱、无实体反转，不接第一刀；农品看M高OI却Night弹性不足；航运EC没有新异常。未发现可定义、可按权重执行的dollar-neutral或beta-neutral篮子；SC-FU只是主题观察，未做单位/久期/裂解beta校准，不能称套利。

风险预算：单一试仓0.25%—0.75% NAV，确认交易0.75%—1.50%；SC相关能化、BR/RU/NR、SF/SA/V分别按同因子合并，单主题总风险≤2.5%—3.0%。压力测试必须覆盖1/2个涨跌停、gap穿透、保证金上调、相关性破裂、流动性消失、人民币急变、IV跳升/塌陷和交割挤压。

归档：历史MD/JSON、latest MD/JSON、status、manifest共6路径已按main回读口径写为`archive_status=success`；CI仅标`pending_or_unverified`，不虚构通过。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：09:30后SC2610守住690.7并突破opening-range high的1/3多；或高开跌破690.7、反抽失败且外油回吐的1/3 failed-gap空。  
C. 今天应继续观察的机会：BR2611等待45分钟验真、V2701跌破5040后的failed-squeeze空、SF611在6564—6624的回撤吸收、AU2610地缘避险弹性是否继续失效。  
D. 今天必须避免或退出的交易：9:00首跳追SC/BR/RU/NR；把Night ΔOI当成已知新多；把C级basis当套利；在execution_ready=false时臆测期权权利金；以及忽略同因子合并风险的多品种叠仓。
