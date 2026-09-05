---
report_date: 2026-09-06
edition: commodities_morning
revision: 1
generated_at_bjt: 2026-09-06T07:00:42+08:00
weekend_mode: true
archive_status: partial_pending_manifest
ci_validation_status: pending_or_unverified
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-06

## 一、今日一句话结论

**今日商品期货期权无合格交易。** 周日休市，且China-Commodities-Engine当前Night Session落在周日并出现802/802合约query error与unresolved，执行数据质量闸门触发；周一仅观察SC2610、SA701、V2701。

当前regime：**周末地缘供给冲击未定价 + 周五国内建材/基础化工挤压待验证 + 贵金属受强就业/美元利率压制 + 中国商品数据源当前降级。** 今天不值得新增风险。

## 二、数据质量与覆盖

本次第一读取层实际读取：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需下钻`data/night_session/latest.json`、`data/latest.json`、`data/market_state_latest.json`。

`report_input_latest.json`为schema v2，`requested_date=2026-09-04`，`generated_at=2026-09-06T06:21:10+08:00`。最近可用中国EOD仍为周五9月4日，802个合约、SHFE/INE/DCE/CZCE/GFEX五所均在历史快照中；但本次重跑状态已经降级：Futures与Market State被标记`data_fresh=false`，根状态`source_date_match_pct=0%`、`critical_module_errors=15`、`full_market_ready=false`。核心原因是iFinD返回HTTP 401 `Device exceed limit`，五所期货与Options本次请求均失败。上一份已验证EOD数据仍保留，可作历史/开盘参考，但按本报告纪律**不计当前fresh evidence**。

Physical：`requested_date=2026-09-04`，18/20序列fresh、2 unavailable，validation/published通过；但多数basis缺交割地/品质/税口径等字段，只作context，不把C/D级basis计入方向层。External：17/22序列fresh、5 unavailable，`generated_at=2026-09-06T06:20:43+08:00`，主要为日频/context-only，不是exact-contract import parity。

Night Session当前状态是本晨最重要的数据异常：`trading_date=2026-09-06`、`night_session_date=2026-09-05`、`generated_at=2026-09-06T06:02:04+08:00`，但周日不是中国商品交易日；同时`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`，802个请求合约中`night_session_contract_count=0`、`query_error_count=802`、`unresolved_contract_count=802`，warning为“802 concrete contracts are unresolved”。更进一步，`data/night_session/latest.json`当前为空。故本报告**不自行把周日标签修正成周一，也不把report_input中残留的上一有效raw night记录当作当前Night Session**；Night price、双收益锚、Night ΔOI与Night curve全部记为N/A、scoring weight=0。

Options：trade_date仍为9月4日，19,394条chain、352个series；341个series surface-ready、74个positioning-ready、0个execution-ready，IV coverage约97.71%、OI coverage约68.21%、bid/ask coverage=0。全局`surface_ready=false / positioning_ready=false / execution_ready=false`，且当前模块`data_fresh=false`，因此只能作T-1背景，不能输出可成交权利金、Greeks或具体执行价。

Contract Metadata仍为partial_error；当前动态保证金、涨跌停和部分具体最后交易日参数未完成一致性确认，交易卡中一律标“参数未确认”，不得硬猜。

## 三、商品仪表盘

> 今日中国与主要海外期货市场均处周末休市窗口。Night栏为**当前有效Night层**，不是上一轮残留raw quote；因此全部为N/A。1D/5D为9月4日同一具体合约的已保留EOD历史指标，属于历史参考而非本晨fresh层。

|板块|品种/具体主力|EOD close/settle|1D / 5D|EOD volume / OI / ΔOI|EOD curve|Basis / Physical|Current Night Close|Night vs Close / Settle|Night ΔOI / quality|07:00 Overseas|Options readiness|信号|
|---|---|---:|---:|---:|---|---|---|---|---|---|---|---|
|黑色建材|SA701|1093 / 1080|+1.79% / +5.16%|2.389m / 1.218m / +21.2k|**Contango -5.17%**|spot fresh；basis不可评分|N/A|N/A|N/A；current Night failed|无exact海外映射|surface背景可研究；execution false|周五强，但curve否定|
|黑色建材|SF611|6624 / 6564|+5.06% / +8.42%|1.335m / 482.9k / +20.8k|**Backwardation +2.74%**|仓单/实体不足|N/A|N/A|N/A|无exact海外映射|execution false|周五最强price+curve一致项|
|能源化工|V2701|5128 / 5040|+3.07% / +11.50%|2.668m / 1.135m / 约+91k|Contango|Physical仅context|N/A|N/A|N/A；上一有效raw不计分|原油不是PVC parity|execution false|日盘挤压，周一防高开低走|
|能源化工|SC2610|685.2 / 683.1|周五settle约-1.1% / 5D约+15%|161.9k / OI下降 / —|Backwardation|Physical unavailable|N/A|N/A|N/A；current Night failed|Brent周五96.28、WTI 91.48；周六冲突升级|execution false|**周末最大未定价gap风险**|
|能源化工|EG2610|5898 / 5844|+0.57% / 高位|1.792m / 392.5k / —|Backwardation|Physical context|N/A|N/A|N/A|油价地缘风险偏上|execution false|趋势仍高，但无本晨确认|
|能源化工|TA701|5922 / 5958|-0.90% / +6.47%|0.961m / 1.064m / +15.1k|Backwardation +2.61%|basis仅context|N/A|N/A|N/A|原油强但非exact映射|execution false|price与curve分歧|
|黑色建材|FG701|978 / 971|+0.62% / 约+5.8%|1.799m / 1.209m / —|Contango|Physical fresh但basis不可评分|N/A|N/A|N/A|无exact海外映射|surface背景；execution false|跟随SA，证据不足|
|新能源|LC2701|141940 / 147040|-4.08% settlement（close约-7.41%） / —|312.4k / 392.6k / —|Backwardation|实体/基差不足|制度无有效本晨Night|N/A|N/A|无可靠exact parity|execution false|最弱之一，但curve与price冲突，不追空|
|能源化工|BZ2610|— / —|+1.27% / +12.49%|活跃 / OI小降 / -91|Backwardation +1.03%|Physical不足|N/A|N/A|N/A|油价尾部利多但非纯苯parity|execution false|趋势强但本晨无确认|
|贵金属|AG2610|16250 / 16318|+2.24% / -2.97%|price↑/OI↓ clue|轻度Contango|无完整Physical层|N/A|N/A|N/A|周五spot gold -1.2%、silver -1.7%|source T-1；execution false|昨日反弹逻辑被海外宏观压制|

07:00海外层必须区分“最新收盘”和“周末新闻”：周五Brent结算约**$96.28/bbl**、WTI约**$91.48/bbl**；但周六美国军方称打击三艘伊朗原油运输船，双方在伊朗附近水域继续攻击船只，属于**价格尚未重新开盘验证的新增供给尾部**。因此不能把周六新闻直接写成“Brent已上涨X%”。

## 四、相比上一交易日/上一revision真正变化

1. **数据质量从“周末日历语义降级”进一步恶化为“当前采集失败”。** 昨晨至少保留了611条raw连续交易记录；今晨Night状态为0条有效记录、802 query error、802 unresolved，且`night_session/latest.json`为空。今天不能再引用raw Night双锚作为新信息。
2. **中国EOD重跑也出现iFinD设备上限错误。** 五所期货与期权当前请求都报`Device exceed limit`，所以周五已保留EOD只作为last-good snapshot，不再计fresh层；这直接把昨日60多分的候选压回60以下。
3. **周末能源尾部显著放大，但尚未形成价格证据。** 9月5日美伊双方针对油轮/舰船的冲突升级，Kharg/Hormuz相关供给风险上升；SC的方向先验变多，但由于Brent/WTI尚未在周末消息后开盘，赔率反而更依赖周一gap大小，而不是新闻强度。
4. **周五国内最强仍是SA/SF/V一组建材—基础化工挤压，但curve并不一致。** SF的price与backwardation同向；SA、V价格暴涨却仍contango，说明不能把板块齐涨直接等同于实体短缺。
5. **贵金属短线宏观层转弱。** 强就业数据后美元/利率预期上移，周五现货黄金约-1.2%、白银约-1.7%。当前无周末新价格可证明反转，因此AG只留反弹失败观察，不做提前空。
6. **OPEC+今天成为能源的第二个二元变量。** 官方已确认七国OPEC+于9月6日再次开会；会议结果与周末地缘升级可能同向，也可能部分抵消。SC在周一前不能用单一叙事定仓。

## 五、产业链地图

**1）SC/FU/LU能源链：方向先验偏多，执行置信度低。** EOD SC curve仍Backwardation；周末油轮冲突强化供给尾部，Hormuz船流此前也显著低于常态。但没有周末后的Brent/WTI成交价、没有有效China Night、Physical又缺失。最大缺口是**价格发现尚未发生**，因此不允许把新闻升级成交易确认。

**2）SF/SA/FG/V建材—基础化工：周五最强，内部curve分裂。** SF得到backwardation确认；SA/V/FG为contango，说明EOD price并未获得统一curve确认。周一要看高开后的15/30分钟接受度与OI，而不是追周五涨幅。

**3）芳烃/聚酯：趋势仍强但弹性不透明。** BZ、EG、TA过去5D偏强，部分curve为Backwardation；但当前Night缺失，External只提供上游油价context，不能把上游地缘冲击直接视为下游利润/供需确认。

**4）贵金属：短线中性偏空。** 周五强就业→美元/收益率预期偏鹰→gold/silver走弱；中国AG没有fresh Night/Options确认。若周一国际金银在地缘冲击下重新走强，这条宏观空头链会迅速失效。

**5）新能源LC：最弱但不追。** 周五大跌与Backwardation冲突，实体/海外映射不足；这是典型需要等待反弹失败或curve转弱的品种，而不是看到-7%就顺势追空。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。** 按“stale不计分”的纪律，本晨没有60分以上候选；更没有达到70分试仓阈值的交易。

最接近触发的三项：

|观察项|观察分|方向先验|尚缺确认|为什么暂时不交易|
|---|---:|---|---|---|
|SC2610 周一供给冲击确认多|59|偏多|Brent/WTI周末消息后的首次价格、周一中国15–30m接受、有效Night/curve更新|当前只有fresh宏观/地缘层，gap可能吃掉全部赔率|
|SA701 周一回撤确认多|56|偏多|fresh EOD/Night恢复、突破1108后回踩、contango不再恶化、Physical改善|周五price强但curve反向，当前数据源又降级|
|V2701 高位失败空|55|偏空战术|周一30m跌回5040以下并反抽失败、OI/curve转弱、有效Night|反向交易仍在周五强趋势内部，不能仅凭上一轮raw夜盘回落做空|

评分上限来自数据层，而不是主观风险偏好：SC仅1个当前fresh独立层，≤59；SA/V当前没有足够fresh层，保持观察分，不列为正式机会。

## 七、前三名观察交易卡（非今日可执行交易）

### 1. SC2610｜周一供给冲击确认多｜观察分59

**事实：** 周五close/settle为685.2/683.1，日内高/低699.0/665.4，EOD curve为Backwardation；本晨没有有效Night OHLC、`return_vs_close_pct`、`return_vs_settlement_pct`或Night ΔOI。周六油轮冲突升级，但海外油价尚未在该消息后重新开盘。

**市场定价：** 周五价格只定价到周五收盘；周六新增地缘消息尚未形成可观察价格。**推断：** 周一高开风险显著，但gap越大，追多赔率越差。**主观判断：** 只有“价格接受”而非“新闻更坏”才能把它从59升到70+。

最佳表达：SC2610单腿期货；期权理论上更适合有限损失地表达周末凸性，但当前execution-ready=0，不能实际推荐具体strike/权利金。两腿配比：N/A。

入场：周一先等15–30分钟；若海外油价重开后仍维持供给冲击方向，且SC回踩685–695区间获得承接、随后有效收复699，再考虑第一笔；突破后回踩成功再加第二笔。止损：30分钟接受跌破676。逻辑失效：跌破665.4且Brent/WTI同步回吐周末风险溢价。TP1 715，TP2 735；1–2个交易日无扩张则时间止损。放弃：若直接巨幅高开而15分钟无法形成可控止损距离，宁可错过。

最大损失预算：触发后0.25%–0.50% NAV；今天为0。合约：1000桶/手，tick 0.1元/桶，tick value 100元/手，按685.2计名义价值约685,200元/手；当前动态margin、price limit、exact last trading day本次未确认。夜盘制度存在，但本晨数据无效。交割风险：INE原油实物交割，进入交割窗口前必须roll/exit。若当日官方涨跌停比例为L，1个涨跌停压力约`685200×L`，2个同向约`685200×[(1+L)^2-1]`，L未确认前不伪造数值。

### 2. SA701｜周一回撤确认多｜观察分56

**事实：** 周五close/settle 1093/1080，settlement 1D +1.79%、5D +5.16%，volume约2.389m、OI约1.218m、ΔOI约+21.2k；near-next curve约-5.17%（Contango）。当前Night无有效报价。

**市场定价：** price/volume/OI很强，但期限结构没有确认。**推断：** 这是“挤压/预期交易”的概率高于“已验证短缺”。**主观判断：** 周一只有在1090附近获得承接并突破周五高点1108后成功回踩，才有资格恢复试仓。

入场：15–30分钟后，1080–1095不破且>1108回踩成功；第二笔仅在>1120再次确认。止损：接受<1060。逻辑失效：价格跌回1060附近且contango继续扩大。TP1 1140，TP2 1180；2个交易日时间止损。放弃：高开>2%却OI不扩张/开盘30分钟跌回1108下方。

最大损失预算：触发后0.25%–0.40% NAV。参数：20吨/手、tick 1元/吨、tick value 20元/手；按1093名义约21,860元/手。动态margin、price limit、exact LTD本次未确认；实物交割，提前roll。1/2涨跌停压力分别用`21860×L`、`21860×[(1+L)^2-1]`。

### 3. V2701｜高位失败反向空｜观察分55

**事实：** 周五close/settle 5128/5040，日内高/低5154/4883，settlement 1D约+3.07%、5D约+11.50%，volume约2.668m、OI约1.135m，EOD为Contango。当前Night无有效报价。上一有效raw记录曾出现5072、即-1.09% vs close但+0.63% vs settlement的双锚分歧，但**今天只作审计context，scoring=0**。

**市场定价：** 周五close远强于settlement，反向交易必须等close强势真正失效。**推断：** 若周一30分钟跌回5040以下并反抽失败，才说明日盘抢跑后的边际弹性衰减正在兑现。**主观判断：** 这是战术fade，不是基本面趋势空。

入场：30分钟收于5040下方，随后反抽5040–5080失败；第二笔仅在跌破5000后失败反抽。止损：>5155。逻辑失效：重新站稳5128并伴随OI扩张。TP1 4920，TP2 4800；1–2日时间止损。放弃：周一直接突破5154并稳定30分钟。

最大损失预算：0.25%–0.35% NAV。参数：PVC 5吨/手、tick 1元/吨、tick value 5元/手，按5128名义约25,640元/手；动态margin、price limit、exact LTD本次未确认，实物交割需提前roll。1/2涨跌停压力分别用`25640×L`、`25640×[(1+L)^2-1]`。

## 八、商品期权专项

当前Options只能做研究背景：19,394条、352个series，IV样本覆盖高，但OI不完整且bid/ask coverage=0；更关键的是当前模块不fresh、execution-ready=0。**因此今天不比较可执行IV-RV、不输出具体Delta、strike、净支出或Greeks。**

从风险表达哲学上，SC这种“周末二元供给冲击”更适合有限损失的call spread/ratio-defined structure，而不是开盘裸追期货；但必须等周一实时surface与bid/ask恢复后重新评估IV是否已经把事件溢价完全抬高。Dealer Gamma方向未知，禁止做dealer positioning推断。

固定执行结论：`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

**今天是周日，没有中国商品9:00日盘。以下严格改为“9月7日周一9:00前待更新地图”，不是今天的开盘预测。**

**Layer 1 — Previous China EOD（9月4日）：** SF/SA/V最强，LC最弱；SF price+backwardation一致，SA/V price与contango冲突；SC维持backwardation但周五价格并未继续突破。

**Layer 2 — Current Trading Day Night Session：** **不可用。** 当前status误落`trading_date=2026-09-06`且802合约全失败，`night_session/latest.json`为空；不允许用上一份raw night替代周一Night，也无法计算Night curve。

**Layer 3 — 07:00 Overseas：** 周日主要期货市场未开，最新可交易价格仍是周五结算；新增信息是周六美伊油轮/舰船冲突升级。该信息对SC属于“未定价headline”，对SA/V/FG没有exact-contract海外映射。

|重点品种|周一gap风险|是否已完成Night定价|内外盘冲突|追价？|应等|开盘后确认|
|---|---|---|---|---|---|---|
|SC2610|**高开风险高，但幅度未知**|否|无周末价格可比较|绝不盲追|15–30m|Brent/WTI重开、699接受、OI与curve|
|SA701|不预判|否|无exact海外映射|否|15–30m|1080/1093承接、1108突破回踩、OI|
|SF611|不预判|否|无exact海外映射|否|15–30m|6624上方接受、backwardation是否维持|
|V2701|不预判|否|上游油价不是PVC parity|否|30m|5040/5128区间、OI、curve|
|AG2610|取决于周日晚金银重开|否|周五海外偏空、周末地缘偏多|否|30m|国际金银、DXY/美债、16318附近接受|
|LC2701|平/低开均不可先验确认|无制度有效Night|无exact parity|不追空|45m|147040附近反抽、curve与OI|

External move与China Night之间的信息弹性**本晨无法计算**，因为China Night无有效当前数据。任何用上一有效raw night做“弹性”结论都属于时段错配。

## 十、未来24h / 7日事件

- **9月6日（今日）OPEC+七国月度会议**：OPEC官方此前确认今天开会，但未在该公告中给出具体时点。对SC/FU/LU是最高级Delta/gap事件；结果公布前不预埋方向仓。
- **9月7日美国Labor Day**：EIA明确因此将当周WPSR延至周四，美国商品市场流动性/交易时段需按交易所当日规则确认；周一中国开盘时外盘价格发现可能不完整。
- **9月10日美国东部12:00/14:00（北京时间9月11日00:00/02:00）EIA WPSR**：库存、炼厂与馏分油数据对SC/FU/LU比单纯headline更重要；能源仓位提前控制gap与裂解价差风险。
- **9月11日10:00巴黎时间（北京时间约16:00）IEA Oil Market Report**：重点看供需、炼厂、OECD库存与中东中断假设。
- **9月11日08:30 ET（北京时间20:30）美国8月CPI**：对实际利率、美元与AU/AG形成Delta/Vega重定价；贵金属若用期权，应优先有限损失结构。
- **9月11日12:00 ET（北京时间9月12日00:00）USDA WASDE**：玉米、大豆、豆粕、豆油、棉花等进入事件凸性窗口；不在数据前用季节性替代供需更新。
- **9月11日15:30 ET（北京时间9月12日03:30）CFTC COT**：只用于拥挤度背景，数据截至此前周二，不能解释发布当日盘中方向。
- 天气/矿山/油田/炼厂/化工装置：本晨未发现足够可靠、可量化且独立于上述地缘事件的新异常，因此不额外加分；若周日后续出现停产/封航官方确认，周一需单独重算。

## 十一、风险预算与归档

今天风险预算为**0新增NAV风险**。周一若触发：单一试仓0.25%–0.50% NAV；只有恢复≥3个fresh独立层后才允许进入70+试仓区间，≥4层且无关键错误才讨论确认加仓。SC及其下游油品按同一地缘/油价因子合并计算；SA/SF/V/FG按国内工业挤压因子合并计算。

压力测试必须覆盖：周末油价反向gap、OPEC+与地缘消息相互抵消、止损穿透、连续1/2涨跌停、保证金上调、Night数据继续缺失、相关性破裂、期权IV开盘跳升以及中国开盘时海外流动性不足。

归档说明：本报告按direct-to-main写入历史MD/JSON、latest MD/JSON与status；`manifests/reports.json`为超长单行minified文件，当前GitHub connector无法安全取得完整未截断内容进行唯一键更新，因此manifest保持不动，本次`archive_status=partial`、`ci_validation_status=pending_or_unverified`，不虚构success。

### 关键公开来源

- China-Commodities-Engine：`farfromexact/China-Commodities-Engine`（本报告首要数据源）
- Reuters，2026-09-05，美伊双方在伊朗附近水域攻击船只：https://www.reuters.com/world/middle-east/explosions-heard-near-irans-kharg-island-gulf-origin-unknown-fars-news-says-2026-09-05/
- Reuters，2026-09-05，美国军方称打击三艘伊朗原油运输船：https://www.reuters.com/world/middle-east/us-military-strikes-three-iranian-crude-oil-carriers-central-command-says-2026-09-05/
- OPEC，2026-08-02，确认下一次七国会议为2026-09-06：https://www.opec.org/pr-detail/611-2-august-2026.html
- EIA WPSR：https://www.eia.gov/petroleum/supply/weekly/index.php
- BLS CPI schedule：https://www.bls.gov/schedule/news_release/cpi.htm
- IEA OMR schedule：https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr
- USDA WASDE schedule：https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report
- CFTC COT schedule：https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无；周日休市，周一条件必须等外盘重开与首15–30分钟确认。  
C. 今天应继续观察的机会：SC2610供给冲击确认多、SA701回撤确认多、V2701高位失败空。  
D. 今天必须避免或退出的交易：任何基于当前失效Night数据的交易、周一无确认追油价gap、用T-1且无bid/ask的商品期权直接执行。