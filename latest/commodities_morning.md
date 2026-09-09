# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-10

prompt_version=radar_2026-09-06_coverage_v1  
实际生成：07:17北京时间；信息截点：07:00；最近完整中国EOD：9月9日；今晨Night归属交易日：9月10日；下一交易窗口：今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC、FU、CU有待验证优势，但能源已大幅跳升，09:00首跳不追。**

当前regime：**中东供给冲击二次抬升原油与化工、Night完成主要价格发现、黑色与油脂偏弱、铜维持全球高位共振、美国PPI前实际利率约束贵金属。**

最接近触发的三项是SC2610、FU2611、CU2610；分别缺少开盘回撤接受、产品链持续强于原油、以及LME与国内curve继续共振的确认。

## 二、数据质量与覆盖

本期优先读取[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，再按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[逐合约Night](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json)、[期权曲面](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，requested_date=2026-09-09，2026-09-10 06:00:44生成。
- Futures：实际采用9月9日19:02生成、已验证的last-good EOD；五所802个合约，源日期匹配100%，该快照full_market_ready=true、critical errors=0，7条placeholder排除。
- 06:00再校验因iFinD HTTP 401 “Device exceed limit”失败，根状态显示15个critical errors、当次full_market_ready=false。它是刷新失败，不推翻最新应得且已验证的9月9日EOD；本期据此标为degraded/retained-last-good，而非“实时刷新成功”。
- Market State：77个品种，1D/3D/5D/20D同合约指标可得；历史窗口最早8月13日，截止9月9日。
- Physical：9月9日19:17生成，20项目标中18项按原生频率fresh；SC/LU unavailable。所有basis为C级、仅作context；CZCE仓单为9月9日，GFEX的LC/SI仓单沿用9月1日并标stale，仓单不等于社会库存。
- External：9月10日06:00生成，22项中17项按原生频率fresh，全部context_only，不构成exact import parity。
- Options：最新应得9月9日截面，22,302条chain、375个series、57/64产品；AP/CJ/MA/PF/PL/PR/ZC因源日期仍为9月8日而失败。IV覆盖97.98%、OI覆盖68.77%、bid/ask覆盖0；局部364个series surface-ready、70个positioning-ready、0个execution-ready。今晨再次刷新亦受401影响；有效局部曲面可研究，不可冒充当前报价。
- Metadata：quality=partial；有效合约匹配约73.32%，动态margin/limit覆盖约29.80%，未确认参数不猜。

Night质量闸门：trading_date=2026-09-10，night_session_date=2026-09-09，05:59:18生成；data_fresh=true、validation_passed=true、published=true，但coverage_complete=false。共有588个有效夜盘合约、55个品种，192个合法outside-window、20个no-night-trade；missing timestamp/price/quote均为0。两条未解析记录为远月ZN2707、ZN2708，query_error=2、unresolved=2；前三候选具体合约均为fresh。低于100%的夜盘记录占比不等于全市场采集失败。

## 三、商品仪表盘

1D/5D均为同一具体合约结算收益；Night涨跌以相对9月9日close为主、相对settlement为辅。S/P/E分别表示局部surface/positioning/execution readiness；“未核”不等于ready。

|板块｜品种|具体合约|EOD close/settle；1D/5D|EOD Volume/OI/ΔOI；curve|basis/Physical|Night close；vs close/settle；ΔOI；时间|07:00海外映射｜Options|信号|
|---|---:|---|---|---|---|---|---|
|能源｜原油|SC2610|741.5/722.5；+2.73%/+6.67%|18.21万/3.92万/+476；BWD 5.61%|Physical缺失|773.1；**+4.26%/+7.00%**；-1,081；02:30 fresh|Brent 101.21结算、repo 101.79；Y/N/N|强但不追，等45m|
|能化｜纯苯|BZ2610|8829/8705；+1.93%/+5.20%|6.34万/2.97万/-609；BWD 1.64%|不足|9190；+4.09%/+5.57%；+1,694；23:00 fresh|油价代理；Y/N/N|高弹性、结构未更新|
|能化｜苯乙烯|EB2610|9928/9786；+1.26%/+3.81%|91.38万/29.35万/+1,541；BWD 3.22%|不足|10329；+4.04%/+5.55%；+49,452；23:00 fresh|油价代理；Y/Y/N|等45m，近月curve失真|
|能源｜燃料油|FU2611|3999/3934；+1.05%/-0.93%|83.48万/21.58万/-1,641；BWD 5.97%|C级context|4119；+3.00%/+4.70%；+11,725；23:00 fresh|油/柴油同向；Y/N/N|回撤确认多|
|能化｜乙二醇|EG2610|5849/5804；+0.05%/+1.36%|189.27万/34.02万/-20,714；BWD 6.17%|不足|6020；+2.92%/+3.72%；+22,111；23:00 fresh|油价代理；Y/Y/N|补涨，等45m|
|能化｜甲醇|MA610|3411/3402；+3.75%/+7.76%|316.79万/57.87万/-148,449；curve 6.88%但roll flag|C级context|3494；+2.43%/+2.70%；+55,842；23:00 fresh|油价代理；chain失败|方向强、curve反对|
|能化｜丙烯|PL611|8968/8901；+2.15%/+3.62%|7.57万/2.54万/-1,281；curve 2.84%且roll flag|不足|9261；+3.27%/+4.04%；+1,453；23:00 fresh|油价代理；chain失败|异常强、元数据不足|
|有色｜铜|CU2610|111080/111120；+0.78%/+2.78%|10.63万/22.86万/-1,353；BWD 0.32%|C级context|111910；+0.75%/+0.71%；+3,238；01:00 fresh|LME铜14811.5；Y/Y/N|全球共振，等30m|
|贵金属｜银|AG2610|16224/16141；-0.35%/+2.68%|39.20万/19.74万/-1,932；轻contango|不足|16529；+1.88%/+2.40%；+2,015；02:30 fresh|COMEX银约67.93；Y/N/N|多头观察，期权偏贵|
|黑色｜焦炭|J2701|2160.5/2164；+0.12%/-2.76%|4.14万/6.45万/-2,710；contango 1.14%|不足|2118；-1.97%/-2.13%；-2,238；23:00 fresh|无exact外盘；未核/N|弱但不追空|
|黑色｜焦煤|JM2701|1655/1662；+0.73%/-2.41%|88.23万/53.92万/-21,070；BWD 1.08%|C级context|1630；-1.51%/-1.93%；-14,224；23:00 fresh|无exact外盘；Y/未核/N|curve与价格冲突|
|建材｜玻璃|FG701|969/970；+0.31%/+0.52%|105.13万/121.13万/-5,578；contango 5.18%|C级；仓单+98|956；-1.34%/-1.44%；+4,850；23:00 fresh|无exact外盘；Y/Y/N|failed-squeeze观察|
|油脂｜棕榈油|P2701|10307/10306；-1.10%/+0.43%|67.31万/60.32万/-29,048；BWD 1.25%，z=3.17|C级context|10196；-1.08%/-1.07%；-4,253；23:00 fresh|BMD 4968；Y/未核/N|结构强、价格弱|
|油料｜菜粕|RM611|2364/2344；-0.76%/+0.34%|68.23万/59.76万/-1,760；BWD 2.09%|仓单/需求不足|2326；-1.61%/-0.77%；+6,876；23:00 fresh|CBOT仅context；Y/Y/N|双锚分歧，不追空|
|软商品｜苹果|AP701|7546/7555；+1.22%/+2.33%|13.18万/11.58万/+14,689；BWD 1.14%|实体不足|无制度夜盘|无exact外盘；chain失败|次日日盘突破观察|

海外层：Reuters显示9月9日Brent结算101.21美元/桶、WTI 96.05，分别上涨约3.4%和3.25%；repo在06:00附近记录连续/代理价101.79与96.67。两者时点口径不同但方向一致，均只作为境外定价证据，不能写成中国日盘已经交易。[Reuters油市，2026-09-09](https://www.reuters.com/business/energy/brent-crude-rises-above-100-barrel-middle-east-conflict-escalates-2026-09-09/)

COMEX金约4446.9、银约67.93；美国10年期收益率约4.84%，美元小幅走强。贵金属的避险与通胀交易存在，但实际利率竞争解释仍强。[Reuters全球市场](https://www.reuters.com/world/china/global-markets-global-markets-2026-09-09/)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-climbs-subdued-us-dollar-inflation-data-awaited-amid-oil-rally-2026-09-09/)

## 四、相比上一交易日/今晨真正变化

1. **SC由“日盘预交易、等回撤”升级为Night二次价格发现，但赔率下降。** EOD close已较前结算高5.43%，Night仍相对close再涨4.26%；相对settlement的7.00%不能全部写成隔夜新增。SC2610/2611 back由EOD 5.61%扩大至Night约7.66%，curve确认价格，但Night ΔOI -1,081是反证。
2. **FU、BZ、EB、EG把冲击扩散成板块breadth。** 它们相对close上涨3.00%—4.09%；FU back约5.97%→6.12%。EB2609夜盘仅24手，近月—主力back约3.22%→0.30%的收窄不作为有效curve确认。
3. **前一晚SC/FU/EB条件单均未进入原好成交区。** SC Night low 752.4高于733—740，FU low 4069高于3950—3990，EB low 10010高于9850—9910；不能事后追认成交。
4. **CU恢复三层共振。** EOD价涨但减仓，Night转为价涨仓增线索；CU2609/2610 back由0.32%扩至约0.44%，LME铜约14811.5。仍缺A级/B级Physical与exact进口利润。
5. **黑色与油脂逆向。** J/JM、P/Y/OI在能源通胀冲击中走弱；这是产业分化，不支持“所有商品通胀多头”。其中P的强back与价格下跌冲突。
6. **今晨刷新失败是数据事件，不是市场事件。** 401仅使Futures/Options当次模块状态降级；经验证的9月9日last-good EOD及9月10日具体Night记录仍可使用。

旧建议台账：SC（COM-E-SC2610-GAP-20260905）与FU（COM-E-FU2611-PRODUCT-TIGHT-20260908）延续但上移触发区；EB（COM-E-EB2610-DAY-REVERSAL-20260909）延续、因Night curve不确认降一档；CU（COM-M-CU2610-LME-RECORD-20260909）重新升级；MA（COM-M-MA610-SETTLE-RECLAIM-20260908）因roll标记与curve收窄降至69分观察；AP（COM-E-AP701-MOMENTUM-20260909）维持日盘观察。没有成交反馈，不假设真实持仓。

## 五、产业链地图

- **最强：SC—FU—BZ—EB—EG，偏多但严重延伸，置信度中高。** 价格、FU/SC曲线与海外油三层同向；实体层缺失，中国需求下修是最强反证。中石化研究预计2026年中国石油需求下降8.9%，汽油、柴油及乙烯当量需求均走弱。[Reuters需求反证](https://www.reuters.com/business/energy/china-oil-demand-fall-89-2026-sinopec-research-says-2026-09-09/)
- **有色：CU强于AL/ZN，偏多，置信度中。** 铜获Night价仓、curve与LME确认；ZN远月两条采集错误不影响主力研究，但不扩大为全锌链证据。
- **最弱：J—JM—RB与油脂，偏弱，置信度中低。** 价格弱，curve却不完全同向；缺实体更新，故更像相对弱势而非确认趋势空。
- **化工内部：MA/PL价格强，curve质量混合。** MA610/611 Night back约5.15%，低于EOD 6.88%，且EOD配对有roll flag；PL元数据及期权链不足，不能把高涨幅直接解释为现货短缺。
- **贵金属：AG强于AU，置信度中。** 银Night与外盘同向、call skew高；但高IV和收益率上行反对追逐有限凸性，黄金信用主题仍未形成独立优势。

## 六、机会排行榜

|排名|机会|逻辑/赔率/催化/价曲波/仓技|总分|有效支持层|研究判断｜证据｜执行|
|---|---|---:|---:|---|---|
|1|SC2610回撤接受多|23/14/19/13/10|**79**|1、2、4|存在待验证优势｜部分｜等45m|
|2|FU2611产品链延续多|22/17/18/12/9|**78**|1、2、4|存在待验证优势｜部分｜等30—45m|
|3|CU2610全球共振多|21/18/14/13/10|**76**|1、2、4|存在待验证优势｜部分｜等30m|
|4|EB2610油价扩散多|21/15/17/13/9|**75**|1、4、5|存在待验证优势｜部分｜等45m；Night curve反对|
|5|AG2610银强金弱多|19/17/14/12/10|**72**|1、4、5|存在待验证优势｜部分｜等30m；期权待报价|

分项均已复算。层2、3、4、5分别为期限结构/高质量基差/仓单、实体供需、境外宏观、商品期权；C级basis不计支持。SC/FU/EB属于同一油价—供应冲击因子，不得按三笔独立风险叠加。MA为69分研究观察：价格与外油支持，但EOD减仓、Night curve收窄、期权链失败，只有1/4两层。

## 七、前三名交易卡

### 1. SC2610｜79｜回撤接受多

**事实：** 9月9日EOD 741.5/722.5；Night OHLC 753.5/776.4/752.4/773.1，+4.26% vs close、+7.00% vs settlement，ΔOI -1,081。SC2610/2611 back约5.61%→7.66%。  
**市场定价：** 霍尔木兹与油轮风险已进入右尾，Night已交易大部分新增冲击。  
**分歧/推断：** curve确认近端风险，但中国需求走弱与仓位未扩张意味着追价赔率不高；最强竞争解释是地缘premium而非实体消费牛市。  
**最佳表达：** 仅用SC2610条件期货；SC短到期期权IV显著高于RV且无bid/ask，暂不优于期货。

- 好成交：等45分钟，760—768回撤被接受，重上774/VWAP后1/3多。
- 中成交：突破776.5并成功回踩，仓位减半。
- 坏成交：直接高于790或止损距离超过计划1R，放弃。
- 计划止损：45分钟接受752下方；逻辑失效：跌破741.5、back显著收窄且Brent回到99以下。
- TP1 795或1.5R；TP2 825或3R；1—2D无扩张退出。分批为1/3试仓、确认后最多再加1/3，余仓跟踪curve。
- 风险：试仓最大损失0.30%—0.50% NAV；与FU/EB/EG/MA合并。期货最大损失不由结构限定。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；Night名义约77.31万元。动态margin/limit未确认；Night 21:00—02:30；最后交易日2026-09-30，实物交割。[INE合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- roll/交割：不得把2610拖入交割月末；最迟9月18日前核验流动性并计划移至SC2611，服从券商更早限仓。
- 压力：一板不利损失=773,100×L；两板复合下跌=773,100×[1-(1-L)^2]。gap、涨停和保证金上调时计划止损可能失效。

### 2. FU2611｜78｜产品链延续多

**事实：** EOD 3999/3934；Night 4080/4142/4069/4119，+3.00%/+4.70%，ΔOI +11,725；FU2610/2611 back约5.97%→6.12%。  
**市场定价：** 原油与产品供应风险同步进入价格；FU五日结算收益仍为-0.93%，相对SC并非最拥挤。  
**分歧/推断：** 若产品back与夜盘OI继续扩张，FU可能比SC outright更耐久；反证是EOD曾价涨仓减、国内柴油需求下修。

- 好成交：等30—45分钟，4070—4110承接并重上4120/VWAP，1/3多。
- 中成交：突破4145后回踩，仓位减半。
- 坏成交：直接高于4200无回撤，放弃。
- 止损：30分钟接受4060下方；失效：跌破3999、FU back收窄且Brent跌破99。
- TP1 4250/1.5R；TP2 4400/3R；两日时间止损。
- 风险0.25%—0.45% NAV；与SC等能化合并，不能同时满额。
- 参数：10吨/手，tick 1元/吨，tick value 10元；Night名义约41,190元。动态margin/limit未确认；Night至23:00；最后交易日2026-10-30，实物交割。
- 压力：一板=41,190×L；两板=41,190×[1-(1-L)^2]。滑点预算不超过计划1R的10%，超过20%放弃。

### 3. CU2610｜76｜全球共振多

**事实：** EOD 111080/111120；Night 111150/111950/111080/111910，+0.75%/+0.71%，ΔOI +3,238；CU2609/2610 back约0.32%→0.44%。LME铜repo日频约14,811.5美元/吨。  
**市场定价：** 全球铜价维持纪录区，国内Night重新跟随；EOD OI减少说明并非无争议突破。  
**分歧/推断：** 若09:00后中国价差继续back且LME守住高位，国内跟随仍有空间；反证是实体与exact进口利润缺失、美国PPI前收益率高。

- 好成交：等30分钟，111300—111700承接并重上111950/VWAP。
- 中成交：突破112100、回踩不破，仓位减半。
- 坏成交：直接高于113000，放弃。
- 止损：30分钟接受111050下方；失效：跌破110400、curve转contango且LME铜跌破约14500。
- TP1 113500/1.5R；TP2 116000/3R；1—3D时间止损。
- 风险0.25%—0.45% NAV；与AL/BC合并，能源因子另算但总组合仍受主题上限约束。
- 参数：5吨/手，tick 10元/吨，tick value 50元；Night名义约55.96万元。动态margin/limit未确认；Night至01:00；最后交易日2026-10-15，实物交割。[SHFE铜合约](https://www.shfe.com.cn/eng/Market/Futures/Metal/cu_f/ContractText/)
- 压力：一板=559,550×L；两板=559,550×[1-(1-L)^2]。如LME与中国价差在休市时破裂，期货止损不提供有限最大损失。

## 八、商品期权专项

最新有效截面为9月9日EOD，本期有新增surface，但bid/ask仍为0；今晨标的已跳升，moneyness和Delta必须在09:00后重算。

|Underlying/expiry|ATM IV|RV20|IV-RV|RR25/BF25|S/P/E|结论|
|---|---:|---:|---:|---|---|---|
|SC2610/09-11|55.15%|35.74%|+19.41vol|-1.55/-0.84|Y/N/N|极短期event vol高，不追long gamma|
|FU2611/10-19|54.13%|39.22%|+14.91vol|-4.41/-2.38|Y/N/N|put skew，不据此推Dealer Gamma|
|EB2610/09-16|33.31%|25.35%|+7.96vol|+3.39/+2.12|Y/Y/N|call skew支持方向，但无成交成本|
|CU2610/09-23|17.37%|10.61%|+6.75vol|+4.43/+0.13|Y/Y/N|上行偏度已计价|
|AG2610/09-23|43.26%|30.11%|+13.15vol|+6.41/+2.45|Y/N/N|银call昂贵，期货优先|
|FG701/12-11|20.89%|19.53%|+1.36vol|+7.22/+3.12|Y/Y/N|结构异常仅研究|

HC、SS、LU期权今日09:00挂牌；截至07:00尚无首日有效chain、surface或bid/ask，不能借用历史代理曲面。[SHFE公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html)｜[INE公告](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)

当前期权不优于裸期货：并非证明所有期权昂贵，而是execution-ready=0且标的Night跳升后旧Delta失真。Dealer Gamma方向未知。任何call spread或risk reversal均为research only; manual quote and manual confirmation required before execution; no premium quoted。

## 九、9:00开盘风险地图

严格三层：9月9日中国EOD；归属9月10日、今晨已完成的Night；截至07:00的海外结算/最新代理。Night不是未来行情。

|品种|三层映射/预期开盘|是否已在Night定价|首跳与等待|开盘确认|
|---|---|---|---|---|
|SC|EOD↑；Night再↑4.26%；Brent>101｜明显高开/宽幅|大部分|不追；45m|752/773/776、SC2610-2611 back、Brent|
|FU|EOD↑；Night↑3.00%；油/产品同向｜高开|较多|不追；30—45m|4069/4119/4142、back与OI|
|BZ/EB|EOD↑；Night约↑4%；油价同向｜高开|较多|不追；45m|EB 10010/10329/10346；BZ深度|
|EG/MA/PL|EOD分化；Night↑2.4%—3.3%｜高开|较多|不追；45m|settlement、curve、油化breadth|
|CU|EOD↑；Night↑0.75%；LME高位｜小高|部分|不追；30m|111080/111950、curve、LME|
|AG/AU|EOD混合；Night银强金稳；海外银强｜AG高开/AU小高|部分|不追；30m|AG 16154/16529/16628、10Y收益率|
|J/JM/RB|EOD偏弱；Night继续弱；无exact外盘｜低开|较多|不追空；30—45m|Night low、OI、钢材breadth|
|FG/SA|EOD平；Night弱；深contango｜偏低|较多|不追空；30m|FG 951/956/970、仓单与contango|
|P/Y/OI|EOD弱；Night再弱；BMD/CBOT无强确认｜低开|较多|不追空；45m|P 10127/10196、back是否维持|
|AP/SF/SM/JD/LC/SI/PS|无制度Night｜下一日盘09:00|无|等30—45m|EOD突破/回撤、量仓与实体|

External→China Night的信息弹性在SC/BZ/EB/FU很高；铜温和同向；黑色与油脂逆向。SC相对close与settlement相差2.74个百分点，说明昨日日盘close已先于settlement计入部分风险，但今晨仍有真正新增上涨；不能把7.00%全算作Night新信息。

## 十、未来24小时与7天事件

- **9月10日09:00：** HC、SS、LU期权首日挂牌；只观察chain完整性、surface和bid/ask，不用代理IV。
- **9月10日20:30：** 美国8月PPI。BLS确认8:30 ET发布；能源、有色和贵金属在事件前降低Delta/Vega，避免把油价冲击与核心通胀混为一谈。[BLS日程](https://www.bls.gov/schedule/news_release/ppi.htm)
- **9月11日00:00：** EIA因劳动节顺延至9月10日12:00 ET发布周度石油数据；SC/FU/EB同因子仓在此前合并减仓。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月11日16:00附近：** IEA Oil Market Report；重点检验供应中断与需求下修谁占主导。[IEA](https://www.iea.org/reports/oil-market-report)
- **9月11日20:30：** 美国8月CPI；CU/AU/AG面临美元与实际利率重定价。[BLS CPI](https://www.bls.gov/cpi/)
- **9月12日00:00：** USDA WASDE/Crop Production；M/Y/P/OI/C/CF避免无保护方向重仓。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **9月12日约03:30：** CFTC COT，仅作滞后拥挤背景，不等同当前机构方向。
- 持续监控霍尔木兹航运、油轮损失、停产与替代供应。地缘headline扩大分布尾部，不自动提供入场价。[Reuters冲突进展](https://www.reuters.com/world/middle-east/iran-attacks-us-base-jordan-ships-near-hormuz-after-tankers-sunk-2026-09-09/)

## 十一、覆盖、风险与归档核对

强制63个代码全部使用9月9日last-good EOD完成价格、1D/3D/5D/20D、量仓、curve及方向、基差、跨期、跨品种、跨市场、风格/中性、波动率、偏度、事件凸性扫描；另扫描JR、PL、PM、RI、RS、WH、ZC、BZ、LG、RR、PD、PT、OP、WR等动态品种。

- 实际取数且已分析：63/63强制代码；动态有效PL/BZ/LG/RR/PD/PT/OP/WR，共71个有效品种扫描。
- 黑色建材9/9：J/JM夜盘最弱，FG深contango；无三层确认空头。
- 有色贵金属12/12：CU入榜，AG/AU分化；ZN主力可用，仅ZN2707/2708远月错误隔离。
- 能源炼化化工25/25：SC/FU/EB入榜；MA/PL因roll和链缺失降级。
- 新能源及GFEX新材料全部扫描：LC/SI仓单沿用9月1日，实体确认不足。
- 农产品油脂饲料畜牧22/22：P/Y/OI夜盘弱；强curve未获价格确认。
- 航运与软商品全部扫描：AP无夜盘、EC缺exact外盘映射。
- 数据不足：SC/LU Physical、所有A级/B级exact basis、exact import parity、SHFE/DCE完整仓单、7个期权产品、全部期权执行报价及partial metadata。
- 不适用/流动性不足：JR/PM/RI/RS/WH/ZC及若干远月零价零量记录；不进入排行，但未从覆盖清单删除。
- 未入榜最值得跟踪：能化为MA Night curve收窄；黑色为J/JM弱而curve冲突；农产品为P强back/弱价；新能源为LC实体旧；航运为EC映射缺失。没有定义完善的beta-neutral篮子，本期不发布伪套利。

风险预算：单笔试仓0.25%—0.50% NAV；只有回撤、curve和海外继续确认后才可提高至0.75%—1.0%。SC/FU/BZ/EB/EG/MA/PL合并为一个油价—供应冲击主题，当前总风险建议不超过1.25% NAV，低于绝对2.5%—3.0%上限。压力测试包括一/两板、相关性破裂、流动性消失、保证金上调、地缘缓和、人民币急升、PPI/EIA双事件和交割挤压。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2610等45分钟在760—768承接并重上774；FU2611等30—45分钟守4070—4110并重上4120；CU2610等30分钟守111300—111700并重上111950。  
C. 今天应继续观察的机会：EB2610油价扩散、AG2610银强金弱、MA610 curve收窄、FG701 failed-squeeze、P2701强back与弱价冲突，以及HC/SS/LU期权首日流动性。  
D. 今天必须避免或退出的交易：09:00首跳追SC/FU/BZ/EB/EG/MA/PL；把7.00%相对settlement误写成SC全部隔夜新增；追空J/JM/P；在execution_ready=false时臆测期权成本；把C级basis或连续外盘称套利。