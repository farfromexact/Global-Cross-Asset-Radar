---
report_date: 2026-09-04
edition: commodities_morning
revision: 2
generated_at_bjt: 2026-09-04T07:25:33+08:00
status: published
archive_status: partial
---
# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-04｜Revision 2

生成时点：2026-09-04 07:25 BJT。中国日盘尚未开盘；中国EOD使用2026-09-03，当前交易日Night Session为2026-09-04交易日、实际起始于2026-09-03晚间。

## 一、今日一句话结论

**有值得冒险的条件型机会，但没有9:00应直接追价的新仓位：优先EB2610、AG2610、BZ2610；夜盘已完成大量重定价，先等15—30分钟。**

核心判断：今天不是“全商品Risk-on”，而是**地缘供给冲击下的强分化行情**。最强是芳烃链与贵金属；最值得警惕的是“新闻很强、价格新增弹性却下降”的原油SC和前一日领涨的EG/MA。所有70分以上机会均为条件单/试仓，没有80分以上确认交易。

## 二、数据质量与覆盖

### 2.1 实际读取路径

第一读取层：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`。

按需下钻：`data/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`、`data/night_session/latest.json`。其中Night Session全量文件通过GitHub connector可确认schema/覆盖，但因文件超大无法安全定位Top候选near-next两个具体合约的完整记录，因此本版**不虚构Night curve**，只使用report_input中可验证的具体交易合约Night记录；Night curve不加分。

### 2.2 统一输入与模块状态

- `report_input_latest.json`：schema v2；`requested_date=2026-09-03`；`generated_at=2026-09-04T06:15:59.429799+08:00`。EOD=T-1、Night trading_date=T完全符合晨报协议，不判stale。
- Futures：2026-09-03，802个合约；SHFE、INE、DCE、CZCE、GFEX五所；`full_market_ready=true`、`source_date_match_pct=100%`、`critical_module_errors=0`。但`official_complete=false`，Futures为verified vendor primary；contract metadata/仓单/basis/会员排名仍有局部缺口。
- Market State：fresh；同一具体合约1D/3D/5D/20D、RV20、成交/OI z-score、ΔOI、near-next curve可用，不使用跨roll拼接收益。
- Physical：18/20 fresh、2 unavailable。多数spot/basis缺地区、品质、交割地、税口径，映射basis多为C级，故仅作context；不计完整Physical层，不称套利。
- External：17/22 fresh，但repo用途均为`context_only`；DXY、USDCNH等部分序列不可用，无exact-contract import parity，因此不做可执行跨市场套利。
- Night Session：`trading_date=2026-09-04`、`night_session_date=2026-09-03`、`generated_at=2026-09-04T06:01:55.452677+08:00`；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。802个请求合约中610个有效夜盘记录、188个合法outside-night-window、4个no-night-trade；missing timestamp/price/quote、query error、unresolved均为0，warnings为空。`night_session_coverage_pct=76.06%`不是“完整率只有76%”。
- Options：T-1（2026-09-03）背景；19,354条、352个series；IV coverage 97.73%、OI coverage 67.86%、bid/ask coverage 0；全局`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`，dealer gamma方向未知。单series若`surface_ready=true`可用于T-1背景，但**不计2026-09-04 fresh证据**，也不能虚构成交成本。
- Contract Metadata：整体partial。SHFE部分合约最后交易日可确认；DCE静态/动态字段存在缺失。无法确认的保证金、涨跌停、最后交易日必须写“未确认”，不使用猜测值。

数据结论：**价格—成交—持仓层和正式Night Session质量高；EOD curve可用；Physical与Options执行层不足；Top3 Night curve未独立验证。**

## 三、商品仪表盘（重点10个）

说明：EOD涨跌采用同具体合约settlement return；Night强弱以`return_vs_close_pct`为headline，`return_vs_settlement_pct`为风险锚。Night数据仍属于第1层，不重复计层。

|板块|品种/合约|EOD close/settle|1D / 5D|EOD volume / OI / ΔOI|EOD curve|Basis/Physical|Night close|Night % vs Close / vs Settle|Night ΔOI|Night质量/时间|07:00 Overseas|Options|信号|
|---|---|---:|---:|---:|---|---|---:|---:|---:|---|---|---|---|
|贵金属|AG2610|16045 / 15960|+1.53% / -4.37%|492,625 / 216,412 / -7,453|+0.11%，near>next，z≈1.38；近月临交割需折价看|无完整Physical确认|16419|+2.33% / +2.88%|+1,257|fresh；02:30|黄金现货+2.3%、白银+2.8%；美元与美债收益率回落|AG链本轮未形成可执行surface|**条件多，15—30m确认**|
|芳烃|EB2610|9565 / 9563|+1.44% / +11.48%|1,076,406 / 320,070 / +19,134|+2.36%，near>next，z≈0.71|无高质量Physical|9770|+2.14% / +2.16%|+23,714|fresh；23:00|原油盘中冲高但最终Brent 95.52(-0.12%)、WTI 91.30(+0.32%)；供应风险仍高|EB2610 Sep16：T-1 surface/positioning ready，execution false|**最干净的price+OI延续**|
|芳烃|BZ2610|8351 / 8367|+1.11% / +12.29%|74,162 / 29,433 / +1,387|+3.26%，near>next，z≈0.90|无高质量Physical|8557|+2.47% / +2.27%|+2,034|fresh；23:00|同受油价/芳烃供给预期支撑，但外盘原油尾盘回吐|T-1；execution false|**强，但流动性低于EB**|
|能源|FU2611|3813 / 3864|-2.69% / +4.80%|1,028,671 / 214,125 / -12,246|+8.36%，near>next；仅3个观察|映射basis仅context|3900|+2.28% / +0.93%|+1,581|fresh；23:00|柴油/馏分油供应偏紧；原油最终仅小幅变动|T-1；execution false|**EOD弱→Night反转，vs-settle明显较弱**|
|LPG|PG2610|6332 / 6326|-0.66% / +9.60%|— / 104,165 / +1,409|-3.26%，near<next，curve不确认|无完整Physical|6568|+3.73% / +3.83%|+9,298|fresh；23:00|油价供应风险正向，但尾盘回吐|T-1；execution false|**夜盘很强但期限结构否定，先观察**|
|乙二醇|EG2610|5718 / 5811|+1.48% / +14.46%|2,727,968 / 376,244 / -3,502|+7.18%，near>next，z≈1.81|无完整Physical|5801|+1.45% / -0.17%|-11,941|fresh；23:00|原油风险溢价正向但非exact parity|T-1；execution false|**关键降级：相对close涨、相对settle反而跌**|
|甲醇|MA610|3158 / 3188|+0.98% / +13.98%|约3.19m / 613,187 / -12,291|+3.73%，near>next，z≈1.90|现货仅C级context|3204|+1.46% / +0.50%|+24,556|fresh；23:00|油价/化工情绪正向但非直接映射|T-1；execution false|**增仓修复，但边际弹性弱于headline**|
|PTA|TA701|5942 / 6012|-0.46% / +8.76%|1,113,210 / 1,049,177 / +46,361|+3.32%，near>next，z≈2.62|PTA现货C级context|5996|+0.91% / -0.27%|+310|fresh；23:00|油价正向|T-1；execution false|**只修复close，仍低于settle**|
|原油|SC2610|681.7 / 690.9|+2.01% / +20.43%|约201.6k / 37,059 / -2,368|+6.67%，near>next；仅3个观察|Physical unavailable|678.6|-0.45% / -1.78%|-743|fresh；02:30|Brent/WTI盘中创六周高位后回吐，最终95.52/91.30|T-1；execution false|**新闻强、价格弹性弱：不追多**|
|有色|CU2610|108410 / 108540|+0.40% / +0.14%|— / 206,566 / -643|+0.49%，near>next，z≈1.65|现货仅context|109110|+0.65% / +0.53%|+743|fresh；01:00|LME EOD fresh、美元走弱；无exact import parity|T-1；execution false|**温和条件多，非第一选择**|

## 四、相比上一期真正变化

1. **EG从昨日第一梯队降级。** EOD趋势仍强、curve仍陡，但夜盘`+1.45% vs close`同时`-0.17% vs settlement`，且Night ΔOI=-11,941。含义不是“重新加速”，而是把偏弱的日盘close修回settlement附近；新增利多弹性下降。
2. **MA也从确认交易降为观察。** Night `+1.46% vs close`但仅`+0.50% vs settlement`；尽管Night ΔOI+24,556，Physical仍只有C级context，严格证据纪律下只有两层可靠确认，不能维持上一期80+评分。
3. **SC出现最重要的反身性警告。** EOD已极度强势，但Night相对close -0.45%、相对settle -1.78%，同时海外原油盘中因中东冲突大涨、最终却大幅回吐。强新闻没有换来中国原油新增价格弹性，追价赔率变差。
4. **芳烃链BZ→EB接棒成为最强中国链。** EB、BZ均表现为EOD上涨+OI增加，Night继续上涨且OI继续增加；其价格/OI一致性优于EG/MA/SC。
5. **AG成为新的宏观凸性候选。** EOD反弹后Night再涨2.33%（vs close），同时国际金银、美元、收益率方向共振；但20:30 NFP会直接重定价美元/实际利率，必须把事件风险写进入场条件。
6. **外盘原油的“盘中高点”不能继续当07:00价格。** Sep3盘中Brent/WTI一度约97.29/93.04，但最终Reuters收盘口径为Brent 95.52(-0.12%)、WTI 91.30(+0.32%)。这强化了“不把Headline当最终定价”的纪律。

## 五、产业链地图

### 1）芳烃：BZ → EB｜最强｜偏多｜置信度中高
EOD price：两者均上涨且OI增加。Night：BZ +2.47%、EB +2.14% vs close，Night OI分别+2,034/+23,714。EOD curve：两者near>next。库存/仓单：无足够高质量fresh层。Options：EB特定series可研究IV/skew，但T-1且execution false。海外：上游原油有供给风险，但尾盘回吐。最大缺失：Physical与Night near-next curve。结论：**最强，但9:00高开不追。**

### 2）贵金属：AG｜偏多｜置信度中高
EOD：+1.53%，但EOD OI下降；Night +2.33%并有小幅OI回升。EOD curve轻度near>next，但near leg接近交割、样本需折价。海外：黄金+2.3%、白银+2.8%，美元/收益率回落。Options：当前不能执行。最大缺失：高质量Physical与可执行期权。结论：**等15分钟确认后才允许试仓，并控制NFP Vega/Gap风险。**

### 3）原油/燃料：SC → FU｜方向分裂｜置信度中
SC Night下跌而FU Night强反转；`FU +2.28% vs close`只有`+0.93% vs settlement`。海外原油盘中冲高、最终基本持平。柴油/馏分油供应偏紧对FU比对SC更友好。结论：**FU可条件多，SC不追；这不是一条统一的能源多头。**

### 4）聚酯/甲醇：EG / TA / MA｜趋势仍强、弹性下降｜置信度中低
EG、TA都出现“vs close为正、vs settlement为负/接近零”；MA也有明显双锚差。EOD curve仍支持，但Night没有独立curve验证。结论：**昨日赢家今天不是最佳新增风险。**

### 5）农产品/油脂｜混合｜置信度低
P/Y夜盘接近持平，RM夜盘对EOD上涨形成否定；CBOT/BMD只有repo EOD背景，没有形成三层fresh共振。结论：**没有值得为高风险偏好硬做的农产品交易。**

## 六、机会排行榜（严格五层证据）

|排名|机会|分数|方向/持有期|阶段/工具|fresh层|最大损失有限？|主要数据惩罚|
|---|---|---:|---|---|---:|---|---|
|1|EB2610 回撤确认多|78|Long / 1—3D|条件试仓 / futures|3：价格OI、EOD curve、海外宏观|否|无高质量Physical；Options T-1不可执行；Night curve未验证；DCE metadata partial|
|2|AG2610 15—30m确认多|76|Long / intraday—3D|条件试仓 / futures|3：价格OI、EOD curve、海外宏观|否|近月curve可能受交割扰动；Options不可执行；NFP事件风险|
|3|BZ2610 回撤确认多|74|Long / 1—3D|条件试仓 / futures|3：价格OI、EOD curve、海外宏观|否|新上市品种相对流动性较低；Physical缺；DCE metadata partial|
|4|FU2611 反转确认多|71|Long / intraday—2D|条件试仓 / futures|3：价格OI、EOD curve、海外宏观|否|curve仅3个观察；vs-settle强度明显弱；海外原油尾盘回吐|
|5|CU2610 温和突破多|70|Long / 1—3D|条件试仓 / futures|3：价格OI、EOD curve、海外宏观|否|趋势强度低；无exact import parity；Physical仅context|

评分拆分：EB 23/18/17/12/8；AG 21/19/18/10/8；BZ 21/17/16/11/9；FU 20/16/18/10/7；CU 19/17/15/11/8（依次为逻辑25、赔率凸性25、催化20、price/curve/vol15、拥挤持仓技术15）。

**没有80+确认交易；因此没有应立即建立的新仓位。** 70—79只允许试仓/条件单。EG、MA、PG虽接近触发，但在严格证据上分别受双锚冲突、层数不足、curve不确认限制。

## 七、前三名交易卡

### #1 EB2610｜条件多｜78

**事实：** previous close 9565；settlement 9563。Night O/H/L/C=9695/9810/9596/9770；`+2.143% vs close`、`+2.165% vs settlement`；Night volume 488,764；Night OI 343,784；ΔOI +23,714；source 23:00，fresh。EOD 1D +1.44%、5D +11.48%，EOD ΔOI +19,134；EOD near-next curve +2.36%、z≈0.71。

**市场定价：** close与settlement双锚一致，说明Night不是单纯修复日盘弱close；价格与OI连续两段同向，是今天中国能化里最干净的延续信号。

**推断：** 上游供给风险和芳烃链情绪仍能给EB溢价，但Reuters最终油价远弱于盘中高点，说明日盘若继续高开、上游不跟，EB可能出现“下游先透支”的回吐。

**主观判断：** 9:00不追。第一路径：9680—9740回撤守住，15—30分钟重新站上9780/VWAP才买；第二路径：15分钟收盘>9820后，必须等9780—9820回踩不破再买。若直接开>9900且不给回踩，放弃。

- 最佳表达：EB2610单腿期货；两腿配比=N/A。
- 分批：触发后50%，突破/回踩确认再50%。
- 初始止损：30分钟有效跌破9580；逻辑失效：<9480，同时EOD curve明显压平且原油/纯苯链风险溢价退潮。
- TP1=9950；TP2=10250；时间止损=2个交易日内未扩张则减/平。
- 计划风险：0.35%—0.60% NAV；同BZ属于同一芳烃因子，EB+BZ初始风险合计不超过0.75%—1.00% NAV。
- 最坏情景：地缘缓和+原油急跌+高开后流动性消失；期货止损不保证最大损失有限。
- Gap/涨跌停：若高开>9900不追；若流动性跳空直接穿9580，按风险预算减仓而不是扩大止损。
- 1—20D催化：Hormuz/中东供应、OPEC+、上游纯苯/原油传导、化工库存与开工。
- 合约参数：交易单位5吨/手、tick 1元/吨、tick value 5元/手（公开静态规格）；Night close名义价值约48,850元/手。repo当前保证金、涨跌停、EB2610精确最后交易日未确认，故不写伪精确值。1个涨跌停压力损失=48,850×当日官方L；2个连续停板约=48,850×[(1+L)^2-1]（仅价格压力公式，实际保证金/强平需另算）。实物交割品种；短线策略应在交割风险窗口前退出/roll。
- Night curve：未独立验证exact near-next pair，**不计fresh curve确认**。

### #2 AG2610｜条件多｜76

**事实：** previous close 16045；settlement 15960。Night O/H/L/C=16304/16472/16150/16419；`+2.331% vs close`、`+2.876% vs settlement`；Night volume 306,311；Night OI 217,669；ΔOI +1,257；source 02:30，fresh。EOD 1D +1.53%、5D -4.37%、EOD ΔOI -7,453；EOD near-next curve +0.1065%、z≈1.38。

**市场定价：** Night相对两个锚都明显上涨，国际金银同向、美元和美债收益率回落，属于直接跨市场共振；但5D仍负、EOD OI先降后Night仅小幅恢复，不能写成“新多大举进场”。

**推断：** 如果NFP前美元弱势延续，AG有补涨空间；若开盘直接把国际金银涨幅一次性映射完，9:00追多的赔率反而下降。

**主观判断：** 第一路径：16280—16360回撤守住并重新站上16420；第二路径：15分钟收盘>16480后回踩16420—16480不破。若开>16600且没有回踩，放弃。

- 最佳表达：AG2610期货；两腿配比=N/A。当前期权执行层不可用，不用期权报价。
- 分批：50%触发、50%二次确认。
- 初始止损：30分钟有效跌破16140；逻辑失效：<15950且国际金银反转、美元/收益率重新上行。
- TP1=16850；TP2=17300；时间止损=2个交易日；若NFP前仍无扩张，主动降风险。
- 计划风险：0.25%—0.50% NAV；NFP前实际风险倾向下沿。
- 最坏情景：20:30美国就业大超预期引发美元/实际利率跳升、贵金属夜盘gap。
- 合约参数：上期所公开规格15千克/手，tick 1元/千克，tick value 15元/手；Night close名义价值约246,285元/手。repo确认AG2610 last trading day=2026-10-15、last delivery day=2026-10-19；当前动态保证金/涨跌停未可靠确认。1个停板压力=246,285×L；2个连续停板约=246,285×[(1+L)^2-1]。Night交易已由02:30 fresh记录证实。实物交割，进入10月后必须主动roll/退出，不持有投机仓进入交割风险窗口。
- Night curve：未独立验证exact AG2609/AG2610 Night pair；且AG2609临近最后交易日，EOD curve本身也需交割折价。

### #3 BZ2610｜条件多｜74

**事实：** previous close 8351；settlement 8367。Night O/H/L/C=8433/8584/8388/8557；`+2.467% vs close`、`+2.271% vs settlement`；Night volume 32,584；Night OI 31,467；ΔOI +2,034；source 23:00，fresh。EOD 1D +1.11%、5D +12.29%、20D +24.86%；EOD ΔOI +1,387（+4.95%），EOD curve +3.26%、z≈0.90。

**市场定价：** EOD与Night均表现为价格上行、OI增加的归因线索；但这只能叫“增仓伴随上涨”，不能确定为新多。流动性显著弱于EB，且两者是同因子。

**推断：** 若纯苯供给风险继续向下游传导，BZ可能比原油本身更有弹性；反过来，若EB在9:00率先失守，BZ高beta会放大回撤。

**主观判断：** 至少等30分钟。8460—8520守住后重回8560才买；或15分钟>8600后回踩不破。若开>8700无回踩，放弃。

- 最佳表达：BZ2610单腿期货；两腿配比=N/A。
- 初始止损：30分钟有效跌破8375；逻辑失效：<8300且EB同步转弱/curve压平。
- TP1=8750；TP2=9050；时间止损=2个交易日。
- 计划风险：0.25%—0.40% NAV；与EB合并计芳烃因子风险。
- 合约参数：公开最终上市资料确认30吨/手、tick 1元/吨、tick value 30元/手；Night close名义价值约256,710元/手。公开合约规则显示最后交易日为合约月份倒数第4个交易日，但repo未给出BZ2610精确2026年10月日历日期；动态保证金/涨跌停也未确认。1个停板压力=256,710×L；2个连续停板约=256,710×[(1+L)^2-1]。实物交割，必须在交割月前按流动性和OI迁移主动roll。
- 放弃条件：EB弱于Night low、原油风险溢价快速消失、BZ开盘量价背离、买卖盘明显恶化。
- Night curve：未独立验证exact near-next Night pair，不加分。

## 八、商品期权专项

全市场T-1 options：19,354条、352 series；IV coverage 97.73%，OI coverage 67.86%，bid/ask=0；aggregate surface/positioning/execution均未ready，dealer gamma方向未知。因此**期权是研究背景，不是今天07:25的fresh执行层**。

唯一值得记录的具体背景是EB2610、expiry 2026-09-16：T-1 `surface_ready=true`、`positioning_ready=true`、`execution_ready=false`；ATM≈9600，ATM IV≈37.85%，RR25≈+3.32 vol、BF25≈+2.28 vol。与EB2610 RV20≈24.82%比较，IV-RV约+13.0 vol，短期限事件溢价已经很贵。含义：

- 不建议在9:00无报价验证地裸买Call；
- 若日盘live chain恢复且bid/ask可用，更适合研究**有限损失Bull Call Spread**，但本报告不提供虚构strike权利金/净成本；
- NFP带来event convexity，但高IV意味着“方向对、波动率仍可能亏”；
- AG本轮没有可靠可执行surface，不用非surface IV冒充ATM；
- dealer gamma方向未知，禁止推断gamma squeeze。

跨期/跨品种/跨市场RV：**今天没有可直接执行的RV。** EB/BZ相对EG强势可以作为观察，但两腿notional/波动率配比尚未在可靠metadata基础上校准；External仅context_only，无import-parity exact contract，禁止称跨市场套利。

## 九、9:00开盘风险地图（三层严格分开）

### Layer 1｜Previous China EOD（2026-09-03）
AG反弹；EB/BZ延续并增仓；EG/MA趋势仍强但已拥挤；SC 20D极度强势；FU日盘明显回撤；CU温和。

### Layer 2｜Current Trading Day Night Session（trading_date=2026-09-04）
AG +2.33%；EB +2.14%；BZ +2.47%；PG +3.73%；FU +2.28%；SC -0.45%；EG +1.45%但vs settlement -0.17%；TA +0.91%但vs settlement -0.27%。最大信息是**芳烃继续扩张，而SC/EG/TA的headline强度被双锚显著削弱。**

### Layer 3｜07:00 Overseas（最新可验证海外收盘/盘后背景）
Sep3原油盘中一度Brent约97.29、WTI约93.04，但最终Brent 95.52(-0.12%)、WTI 91.30(+0.32%)；说明中东风险仍高但边际买盘并未把全天高点保留到收盘。黄金现货+2.3%、白银+2.8%，美元与美债收益率回落；20:30美国NFP是下一次宏观再定价节点。

|品种|预期9:00|夜盘是否已大量定价|内外盘冲突|追价？|应等|开盘后确认|
|---|---|---|---|---|---|---|
|EB2610|高开|是|上游原油尾盘较弱|否|15—30m|9680—9740支撑、9780/9820、OI是否继续扩张|
|AG2610|高开|是|暂无，贵金属同向|否|15m|16420、16480、美元/收益率|
|BZ2610|高开|是|上游尾盘回吐|否|30m|8460—8520、8560/8600、EB同步性|
|FU2611|高开/偏高|部分|vs-close强但vs-settle仅+0.93%，外油最终仅小涨|否|30m|3840 Night low、3905、Brent是否重新上行|
|PG2610|明显高开|是|EOD curve不确认|绝对不追|30—45m|curve/相对强度是否修复、6560附近承接|
|SC2610|低于昨close或平偏弱|否定EOD强势|中国Night弱、海外盘中强但收盘回吐|否|45m|能否重回690附近、OI、内外盘弹性|
|EG2610|高于昨close但接近settle|主要是修复|双锚冲突|否|30m|5811 settle、Night OI是否止降|
|MA610|偏高|较多|无直接海外映射|否|30m|3188 settle、3204、OI持续性|
|TA701|偏高|只是修复close|低于settle|否|30m|6012 settle能否真正站回|
|CU2610|小幅高开|部分|美元弱支持|可条件、不追|15m|109200附近、OI与LME同步|

**开盘原则：** 夜盘已完成>2%重定价的品种默认不追；15/30/45分钟不是机械时间止损，而是让日盘真实成交、OI和跨市场弹性重新出现。

## 十、未来24h / 7d事件日历（北京时间）

|时间(BJT)|事件|影响|处理|
|---|---|---|---|
|2026-09-04 20:30|美国8月Employment Situation / NFP|美元、实际利率、AG/AU高Delta/Vega|NFP前未扩张的贵金属仓减半；新凸性优先有限损失|
|2026-09-05 03:30|CFTC COT（通常使用前一周二数据）|COMEX/能源/农产品拥挤背景|只作滞后positioning，不当即时方向信号|
|2026-09-06（时间待OPEC+公布）|七个OPEC+核心成员月度会议|油价政策与2027基准预期|SC/FU/化工周末gap风险；不在周末前无预算加满|
|持续|美伊/霍尔木兹航运、以伊局势、俄乌外交/供应|原油、燃料、化工双向gap|期货仓位按最坏gap而非普通止损 sizing|
|2026-09-11 00:00|EIA WPSR，劳动节延迟至周四12:00 ET|SC/FU/成品油库存与炼厂|事件前检查Delta；若用期权必须先确认live execution|
|2026-09-10 20:30|美国8月PPI|美元/利率/贵金属/工业品|次级宏观催化|

IEA/WASDE：本次7日窗口内未核实到比上述事件更早、足以改变Top3的官方高优先级发布；不为凑日历虚构时间。交易所临时保证金/涨跌停/到期参数若盘中有公告，以交易所最新通知为准。

## 风险预算与压力测试

- 单一试仓最大计划损失：NAV 0.25%—0.75%；今天没有确认交易，因此不用0.75%—1.50%确认预算。
- 单一高确信主题总风险≤2.5%—3.0%；芳烃EB+BZ视为同一因子，初始合并风险≤0.75%—1.00%，后续只有在四层证据出现后才可扩。
- 压力：1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变、中国休市期间海外大波动。
- 当前动态涨跌停参数缺失的合约不做伪精确压力金额，使用`notional × 当日官方limit%`和连续停板复合公式，开盘前由交易终端复核。

## 来源

- China-Commodities-Engine（GitHub connector，main）：https://github.com/farfromexact/China-Commodities-Engine
- Reuters，2026-09-03，Oil prices mixed as investors weigh Middle East escalation, chance of Russia-Ukraine peace deal：https://www.reuters.com/business/energy/oil-prices-rise-escalation-middle-east-2026-09-03/
- Reuters，2026-09-03，Gold jumps 2% as Fed Governor Waller's comments temper rate hike bets：https://www.reuters.com/world/india/gold-rises-dollar-yields-ease-with-us-nonfarm-payrolls-report-spotlight-2026-09-03/
- Reuters，2026-09-02，OPEC+ likely to keep oil output policy unchanged on Sunday：https://www.reuters.com/business/energy/opec-likely-to-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-02/
- OPEC，2026-08-02：https://www.opec.org/pr-detail/611-2-august-2026.html
- BLS September 2026 release calendar：https://www.bls.gov/schedule/2026/09_sched_list.htm
- CFTC COT release schedule：https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- EIA WPSR schedule：https://www.eia.gov/petroleum/supply/weekly/schedule.php

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：EB2610回撤确认多、AG2610 15—30分钟确认多、BZ2610 30分钟确认多；FU2611/CU2610仅次级条件单。
C. 今天应继续观察的机会：PG2610夜盘强但curve未确认；EG2610/MA610/TA701的双锚弹性是否重新扩张；SC2610能否获得海外原油的日盘重新确认。
D. 今天必须避免或退出的交易：9:00追高EB/BZ/AG/PG；把vs settlement误当夜盘新增涨幅；基于T-1且execution-not-ready期权做精确成交；NFP前无预算重仓贵金属；继续把SC强新闻等同于强价格。