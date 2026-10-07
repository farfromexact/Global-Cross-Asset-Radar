# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-07｜信息截点：19:30北京时间｜prompt_version：radar_2026-09-06_coverage_v1｜data_protocol_version：china_commodities_v2**

> **今晚的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。**

## 一、今晚一句话结论

截至本报告时点，无可立即执行的合格新交易。TSR20当日回撤否定RU追多，油价与柴油升水并存；明早开市只做确认后的条件表达。

中国交易所仍在国庆休市，今晚没有21:00夜盘；下一可交易窗口是 **10月8日08:55集合竞价/09:00日盘**，下一连续交易是 **10月8日21:00**。[SHFE休市安排（2026-09-21）](https://www.shfe.cn/eng/CircularNews/Circular/202609/t20260921_833508.html)

最接近触发：RU2701条件多头（外盘确认转反对，等45分钟）、柴油物流RV（逻辑增强但缺同步报价/参数）、SC2611条件空头（只在高开衰竭或Brent跌破100时成立）。

## 二、数据质量与覆盖

### 2.1 实际读取路径

- [data/report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（sha `98755c6fea679f2867acf4cccd5e06f02f1deae3`）：requested_date=2026-09-30，generated_at=2026-10-07 19:05:45 BJT。
- [data/last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（sha `d2bfcfec9c11a538e95c2ce76d669095a1445c6a`）。
- [data/night_session/last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（sha `05026f77df407f1779e651e732bc7397b9fd82e6`）。
- [data/radar_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)（sha `d3ec3938b6b29a42f94bc31ae436c13311bea996`）；其evidence_count未直接采用。
- 前序台账：[今晨报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/10/2026-10-07_commodities_morning.md)与[上一晚报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/10/2026-10-06_commodities_evening.md)；本日同版旧稿不存在。

### 2.2 模块真实状态

|模块|观测/生成|状态|结论|
|---|---|---|---|
|Futures last-good|EOD 2026-09-30；806合约、77品种、五所|ok/沿用|原快照full_market_ready=true、source-date match=100%、critical=0；最近应有完整EOD，不冒充10月7日行情|
|10月7日刷新|18:59 BJT|error|五所均0记录；match=0%、full_market_ready=false、critical=15。法定休市不使last-good自动失效，但无“今日中国EOD”|
|Market State|历史9月2–30；18:59重建|ok/沿用|77品种，同合约1/3/5/20D；无新交易日|
|Physical|9月30；10月7日刷新|partial/carried|20目标：18沿用、SC/LU失败；A/B basis=0|
|External|10月7日19:05|ok/fresh|17/22 fresh、validated/published；均context_only，不是精确进口平价|
|Night|trading_date=10月7日、session_start=10月6日|missing/not expected|data_fresh/validation/published/coverage均false；806选择、0有效、outside-window 592、query/unresolved 214；休市无应有夜盘|
|Options|9月30 last-good；10月7日采集0条|stale/current-empty|last-good 14,468合约、196 series、surface 192、positioning 47、execution 0、bid/ask 0|
|Metadata|9月30|partial|contract match 67.49%、effective 73.45%、动态参数约30.15%|

五所last-good包含SHFE/INE/DCE/CZCE/GFEX；**当前**full_market_ready=false，但最近应有last-good完整。读取状态：report_input=ok、current futures=error、Night=missing/not_expected、options current=empty、physical=carried_partial、external=ok。

## 三、商品仪表盘（展示12项；实际扫描77品种）

中国列均为2026-09-30 EOD；“早前Night”是9月29所属9月30交易日历史阶段，不是今晚。

|板块|品种/合约|close/settle|1D/5D|Volume/OI/ΔOI|EOD curve|basis/Physical|早前Night close；vs close/vs settle；ΔOI|10月7日海外|S/P/E|10月8日信号|
|---|---|---:|---:|---:|---|---|---|---|---|---|
|橡胶|RU2701|20095/19710|+3.52/+3.96%|513683/150478/+18323|近月升水0.24%|C级背景|19665；+3.45/+3.28%；+11873|TSR20 Dec-26 247.3，较今晨259.2约-4.59%|Y/Y/N|低开风险；等45m|
|能源|SC2611|711/696.1|-2.90/-2.93%|175510/24979/-4690|轻contango -0.06%|实体缺|705.2；-0.94/-1.63%；-1162|Brent 101.81、WTI 89.91|Y/N/N|高开衰竭才空|
|油脂|OI701|10230/10217|+1.72/-0.25%|272992/283749/+9681|back 1.82%|仓单1463、日减40|10234；+1.76/+1.89%；+6681|BMD棕榈4522|Y/N/N|等30m|
|合成胶|BR2611|16000/15870|+3.12/+6.58%|288172/51622/-4127|back 1.13%|C级背景|16155；+4.50/+4.97%；+8194|油强/TSR20弱，冲突|Y/N/N|等45m|
|白糖|SR701|5354/5336|-0.15/-0.15%|302888/564277/-12444|contango -2.77%|仓单26313、日减779|5341；+0.24/-0.06%；+744|ICE糖20.71|Y/Y/N|外强内弱；等30m|
|贵金属|AG2612|14980/14928|+0.15/-7.41%|273904/283220/+6039|轻contango -0.22%|C级背景|14958；+0.74/+0.35%；—|COMEX银60.33；美元/收益率强|Y/P/N|不抄底|
|有色|CU2611|109680/109570|+0.25/-1.03%|69830/185404/+183|back 0.73%|C级背景|109420；-0.14/+0.11%；—|LME铜14403|Y/P/N|等30m|
|黑色|I2701|702.5/704.5|+0.43/-0.98%|218646/552096/-28979|轻contango -0.21%|C级现货|DCE unresolved|SGX铁矿91.6|不足|无确认|
|能源化工|BU2611|5013/5091|-2.00/-0.29%|880746/155550/-53419|深back 12.61%，roll警报|C级背景|5142；-1.98/-1.02%；-24314|油价偏强|N/N/N|避免假套利|
|芳烃|TA701|6300/6268|+0.22/+0.10%|1191682/1016989/-69523|back 5.35%|C级背景|6306；-0.69/+0.83%；-30011|油强，无精确PX平价|Y/P/N|等45m|
|航运|EC2611|2794/2823.5|-1.67/+7.62%|13089/22057/-2569|contango 26.12%，仅2观测|实体缺|无夜盘|无同步运价验证|N/N/N|不做曲线套利|
|棕榈|P2701|9581/9593|+0.23/-2.70%|373884/546979/-5820|contango -0.37%|C级背景|DCE unresolved|BMD棕榈4522|不足|弱于OI，等30m|

## 四、相比上一期真正变化

1. **中国没有10月7日EOD**：仍休市；18:59失败刷新有15个critical errors，不是价格证据。
2. **repo External刷新到10月7日19:05**：17/22 fresh；WTI 89.91、Brent 101.81、LME铜14403、COMEX金4142.8、银60.33、SGX铁矿91.6、BMD棕榈4522、ICE糖20.71。
3. **RU海外确认反转**：SGX官网TSR20 Dec-26为247.3，较今晨259.2约-4.59%；这不是RU已交易，而是明早回吐风险。RU 77→69。
4. **能源从“原油回落”转成“油涨+产品更紧”**：Brent约101.8；欧洲柴油较Brent升水约77美元。SC空头降级，柴油RV 65→68。[Reuters 2026-10-07](https://www.reuters.com/business/energy/oil-prices-rise-storms-air-strikes-threaten-supply-2026-10-07/)
5. **黄金信用主题仍未通过**：DXY约102.119、美国10Y约5.309%，金价约4135–4143回落；地缘风险没有压过美元/利率。[Reuters全球市场](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-07/)
6. **糖强、油脂分化**：ICE糖高位为SR增加海外支持；BMD棕榈偏弱，OI不升级。

## 五、产业链地图

|产业链|方向/强弱|EOD与早前Night|curve/库存/实体|期权/海外|最大缺失|置信度|
|---|---|---|---|---|---|---|
|天然橡胶|国内旧结构最强、海外转弱|RU旧EOD和Night强|轻back；实体仅C级|call skew偏多；TSR20回撤|开市盘口与同合约curve|中低|
|原油—成品油|柴油物流最强，单边SC混合|SC旧EOD/Night弱|轻contango；SC/LU实体缺|Brent上涨、柴油升水扩大|同步双腿报价/参数|中|
|油脂|OI强于P，外盘偏弱|OI旧价强、P弱|OI back、P contango|BMD偏弱；执行期权缺|MPOB/进口平价|中低|
|糖|海外强、国内旧结构弱|SR旧价平弱|contango、仓单下降|ICE糖20.71；期权无bid/ask|明早弹性与curve|低中|
|有色贵金属|美元/收益率压金银|中国旧EOD混合|CU back、AG contango|LME铜高位；金银回落|USD/CNH与重开基差|低|

Regime：**中国假期最后一晚 + 海外能源供应风险抬价 + 美元/长端收益率偏强 + 橡胶外盘反转 + 农产品分化**。无新EOD curve确认；历史Night不能解释今晚；实体多数无新增。可研究RV只有柴油物流篮子，尚不执行。

## 六、机会排行榜

|#|idea_id|方向/周期|逻辑/凸性/催化/价曲波/拥挤|总分|支持层；反证/缺失|研究判断；证据；执行|Δ今晨|
|---:|---|---|---|---:|---|---|---:|
|1|COM-E-RU2701-RUBBER-TIGHTNESS-20261001|条件多；2–10D|21/14/13/12/9|69|3层支持；TSR20强反对，实体弱|待验证优势；部分；等待触发|-8|
|2|COM-E-DIESEL-LOGISTICS-20261005|多gasoil/空Brent；1–7D|22/14/17/10/5|68|2层支持；同步报价/参数缺|待验证优势；部分；待报价|+3|
|3|COM-E-SC2611-CONDITIONAL-SHORT-20261006|条件空；1–5D|18/15/12/10/8|63|旧价格/curve支持；Brent上涨反对|待验证优势；部分；等待触发|-3|
|4|COM-E-OI701-RELSTRENGTH-20260930|条件多；3–15D|18/14/9/10/10|61|2层支持；BMD弱、实体缺|待验证优势；部分；等待触发|-2|
|5|COM-SR-DIVERGENCE-20260930|多头研究；3–10D|17/12/14/8/8|59|仅海外糖支持；国内价/curve/OI反对|证据不足；不足；观察|0|

总和复核：69、68、63、61、59均等于五分项之和。无70+候选；分数不是胜率、收益或仓位指令。

- **RU隐含**：国内旧价格定价供应偏紧；分歧是海外回撤或令溢价吐回。工具选RU2701而非期权，因bid/ask缺；期货损失不受限。
- **柴油RV隐含**：产品物流压力仍高；分歧是$77升水可能继续扩张。竞争解释是库存释放/炼厂恢复。5:7仅近似美元中性，不是beta-neutral。
- **SC隐含**：重开先补涨合理；只在高开后无弹性时做空。风暴/中东/柴油紧张是反证。

## 七、交易卡

### 卡1：RU2701条件多——降级等待

- 事实：9月30日close/settle=20095/19710；历史Night O/H/L/C=19065/19725/18945/19665，vs close +3.45%、vs settle +3.28%，ΔOI +11873。TSR20 Dec-26现247.3。
- 入场：好=19800–19950企稳并回20000；中=20000–20150且curve不弱；坏=>20350追价或<19600未收复，放弃。10月8日09:45后，40/30/30。
- 止损/失效：30分钟收于19600下；或SICOM续弱且RU转contango。TP1/TP2=20750/21400；2日无扩张退出。
- 参数：10吨/手；tick 5元/吨；tick value 50元；旧close名义200950元；假期margin约11%、limit约9%；夜盘21:00–23:00；LTD 2027-01-15。一/两板压力约17739/37070元；12月中旬前滚动。
- 最大损失：期货不受结构限定；压力含低开跌停、流动性消失。风险≤NAV 0.25%–0.50%。**等待触发。**

### 卡2：多5 ICE Gasoil Nov-26 / 空7 Brent Dec-26

- 事实：Brent约101.8；欧洲柴油较Brent约升水77美元。EIA上调Q4 Brent预测至105并提示柴油紧张。
- 中性与PnL：仅按10月5日快照近似美元名义中性，非beta/crack/yield中性；(500×ΔGasoil_{$/t}-7000×ΔBrent_{$/bbl})。
- 入场：好=同步bid/ask、单腿滑点<0.10%、篮子15m确认+1%；中=0.10%–0.25%滑点，只半风险；坏=>0.25%或不同步，放弃。40/30/30。
- 止损/退出：篮子-0.75%或物流恢复；TP +1.5%/+3%；2个流动时段无扩张退出。
- 参数：multiplier/tick/margin/limit/LTD/交割须从ICE/经纪商当前页确认，本期缺失；禁止执行。期货双腿损失不受限，风险≤NAV 0.25%。**待报价或参数。**

### 卡3：SC2611条件空——只做高开衰竭

- 事实：9月30日close/settle=711/696.1；历史Night O/H/L/C=711.9/716.8/696.3/705.2，vs close -0.94%、vs settle -1.63%，ΔOI -1162。Brent现约101.8。
- 入场：好=720–735高开后45m跌回715下且Brent<101；中=705–715反弹失败且Brent<100；坏=<690追空或Brent>103，放弃。40/30/30。
- 止损/失效：30m站稳736；或Brent>103且SC curve转back。TP=690/665；2日无扩张退出。
- 参数：1000桶/手；tick0.1；tick value100元；旧close名义711000元；假期margin约22%、limit约20%；LTD 2026-10-30。一/两板压力约139220/306500元；临近交割须尽快滚动。
- 最大损失不受限；风险≤NAV0.25%。**等待触发，不是开盘空。**

## 八、商品期权专项

最新有效研究截面仍为9月30日：surface=192、positioning=47、execution=0；10月7日当前链为空，不能编bid/ask、权利金、净成本或Greeks。

|Underlying/Expiry|ATM IV/RV20/差|RR25/BF25|判断|
|---|---|---|---|
|RU2701/12-25|27.94/22.25/+5.69|+1.91/+0.24|call偏贵；外盘变动后moneyness不可沿用|
|SC2611/10-14|67.18/60.56/+6.61|-2.58/+2.53|短到期event vol高，执行缺|
|OI701/12-11|15.26/14.24/+1.02|+3.92/+0.64|call skew含部分强势|
|SR701/12-11|10.36/6.97/+3.39|+3.01/+1.34|外糖利多，国内curve反对|
|BR2611/10-26|37.01/29.01/+8.00|-1.36/-0.35|成本高且外盘冲突，回避|

EIA、FOMC、中国重开可抬升event convexity，但不证明期权便宜。Dealer gamma方向未知。

## 九、21:00风险地图

1. **中国EOD**：最近为9月30日。
2. **今天早前Night**：不存在；10月7日采集0条且休市。9月29历史Night仅作旧路径。
3. **15:00–19:30海外**：Brent/WTI 101.81/89.91；LME铜14403；金/银4142.8/60.33；SGX铁矿91.6；TSR20 247.3；BMD棕榈4522；ICE糖20.71。
4. **下一实际连续交易**：今晚21:00不发生；10月8日09:00先恢复日盘，21:00恢复夜盘。

|品种|明早倾向|冲突|追价？|等候|确认|
|---|---|---|---|---|---|
|RU|低开/高波动|外胶跌、国内旧结构强|否|45m|19600/20000、curve、SICOM|
|SC|高开概率|外油涨、国内旧价弱|否|45m|Brent100/103、SC715/736|
|SR|偏高开|ICE糖强、国内contango|否|30m|curve/OI|
|OI/P|平至低开|BMD弱、OI旧curve强|否|30m|OI/P相对强弱|
|CU|平/小低开|LME高、美元/收益率强|否|30m|USD/CNH、CU back|
|AG|低开风险|金银回落、旧5D弱|否|45m|DXY、10Y、IV|
|I|平开附近|SGX有价、无精确平价|否|30m|curve/现货|
|TA/BU|偏高开但分化|油涨、旧curve/roll异常|否|45m|PX/原油映射与curve|

## 十、未来24h/7d事件

|北京时间|事件|处理|
|---|---|---|
|10月7日22:30|EIA周报|能源Delta减半；公布后等15m；[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)|
|10月8日02:00|FOMC 9月会议纪要|金属Delta/Vega控制；[Fed日历](https://www.federalreserve.gov/newsevents/2026-october.htm)|
|10月8日08:55/09:00|中国集合竞价/日盘恢复|旧触发全部重检；等30–45m|
|10月8日21:00|中国夜盘恢复|只用exact-contract当前数据|
|10月9–10日（待官方最终时点）|USDA/WASDE、CFTC COT|农产品降Delta；COT只作背景|
|未来7日|IEA/G7库存释放讨论、海湾风暴/地缘|RV或有限损失优先|
|未来7日|MPOB、东南亚天气|数据后确认；季节性仅先验|

## 十一、覆盖核对与旧建议台账

- 应覆盖63代码+动态新增；引擎实际77品种，完成9月30日last-good的价格/OI/curve/1–20D初筛。
- 实际分析：黑色10、有色贵金属14、能源化工26、新能源3、农产品14、航运软商品10，共77。
- 数据不足：当前中国EOD、SC/LU Physical、A/B basis、DCE Night/options、执行期权、精确进口平价、gasoil/Brent同步报价。
- 不适用/流动性不足：今晚中国Night；EC无夜盘；部分期权OI/报价不足。
- 策略：方向、curve、basis、跨品种、跨市场、波动/偏度、事件凸性与1/3/5/20D均扫描。黑色无升级异常；有色受美元约束；化工curve受roll污染；新能源缺实体；农产品糖最强；航运缺实体。

|idea_id|上次→当前|原因|
|---|---|---|
|COM-E-RU2701-RUBBER-TIGHTNESS-20261001|77等待→69等待|TSR20外盘证据转反对|
|COM-E-DIESEL-LOGISTICS-20261005|65待报价→68待报价|柴油升水约77美元|
|COM-E-SC2611-CONDITIONAL-SHORT-20261006|66等待→63等待|Brent重回101上方；禁止追空|
|COM-E-OI701-RELSTRENGTH-20260930|63→61等待|BMD弱且无中国新价|
|COM-SR-DIVERGENCE-20260930|59观察→59观察|外糖支持、国内反对|
|COM-AU-AG-CREDIT-20261001|未确认→未确认|美元/收益率反证|
|COM-E-SC2611-SUPPLY-TAIL-20261005|取消→继续取消|不与条件空头混淆|
|COM-FU-SC-SPREAD-20260930|取消→继续取消|工具/证据不匹配|

没有成交反馈，不假设真实持仓。

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：无；RU2701与SC2611须等10月8日09:45后确认，柴油RV仍缺同步报价与合约参数。
C. 今晚应继续观察的机会：TSR20回撤后的RU开市吸收、Brent/柴油升水分化、SR外强内弱、OI/P相对强弱及FOMC纪要前的金银压力。
D. 今晚必须避免或退出的交易：追多RU/BR、开盘即空SC、抄底AG、把BU/EC旧curve当套利、使用C级basis或无bid/ask期权下单。