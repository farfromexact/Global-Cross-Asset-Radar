# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-29

`prompt_version=radar_2026-09-06_coverage_v1` · `data_protocol_version=china_commodities_v2`

**实际生成：2026-09-29 19:46 BJT；研究截点：19:40 BJT。** 最近完整中国时段为9月29日日盘（T）；今晚21:00开始的连续交易归属9月30日交易日（T+1），尚未发生。仓库Night快照停在9月24日且验证失败，不能冒充9月29日早前已完成的Night，也不能据此计算今日隔夜—日盘分解。

## 一、今晚一句话结论

> **截至本报告时点，无可立即执行的合格新交易；AG、AO偏空和EB回撤多存在待验证优势，但须等夜盘报价、触发与节前参数确认。**

最强产业链是纯苯—苯乙烯及部分能化裂解品，最弱是橡胶、贵金属与新能源材料；regime是“节前保证金上调、国内强弱分化、海外油价回落与美元偏强”。价格与曲线对AG/AO下行、EB上行各有两层支持，但实体证据不足，期权全部缺bid/ask，不能把研究分数当成胜率或仓位指令。

## 二、数据质量与覆盖

本期首先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[雷达摘要](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，随后为具体合约下钻[data/latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[market_state_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、Physical、External、Options quality/surface和contract_meta；所有仓库输入取自同一main快照语义，未拼接scoped回退。

| 模块 | 日期/生成时间 | 状态 | 本期用途与限制 |
|---|---|---|---|
| Futures | 2026-09-29 / 18:57 BJT | ok；五所；`full_market_ready=true`；source-date match 100% | 806个具体合约；unknown/duplicate/invalid OHLC/negative volume-OI均0；4个placeholder已排除排行；critical errors 0 |
| Market State | 2026-09-29 / 18:57 | ok；77品种 | 同合约1/3/5/20D、RV20、量仓z、near-next curve；个别新品历史不足时不输出z |
| Physical | 2026-09-29 / 19:09 | ok，18/20 fresh，2 unavailable | 仅绝对现货水平；没有可验证变化序列，不能单独计完整实体层；Basis均C级、只作context |
| External（日频） | 2026-09-29 / 19:09 | ok，17/22 fresh，5 unavailable | 全部`context_only`，不是exact-contract进口套利 |
| Night Session | 快照trading_date=2026-09-24；状态任务trading_date=2026-09-29 / 08:06 | **stale/validation failed/unpublished** | 状态任务0条Night合约、806 query errors/806 unresolved；统一输入旧快照423条但同样invalid。今日早前Night close、return-vs-close、day-follow-through、Night curve均缺失 |
| Options | 2026-09-29 / 18:58 | 13,324合约、184 series；39/64产品 | 180/184 series surface-ready；positioning-ready 46；execution-ready 0；IV 98.92%、OI 68.97%、bid/ask 0%；全局surface文件为empty，但统一输入逐series紧凑层可用 |
| Contract Metadata | 2026-09-29 / 18:57 | partial_error | DCE contract-info失败、GFEX source-date未验证；动态margin/limit覆盖不足。前三卡缺口逐卡披露，不能据静态值直接下单 |

Night质量字段：`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`；状态任务`night_session_contract_count=0`、`missing_timestamp/price/quote=0`、`query_error=806`、`unresolved_contract=806`。旧统一快照的`coverage_pct=52.48%`不解释为本期完整率。由于本期真正缺失的是应得的9月29日具体Night数据，所有涉及昨夜路径的结论降级为“证据不足”；本期不启用媒体Night fallback去伪造exact-contract OHLC。

五所核心期货均完整，DCE只缺**合约参数**而非行情，因此中国市场价格扫描仍完整；仓单方面SHFE/DCE刷新失败，5条last-good沿用只作背景。原始读取状态：report_input/期货/市场状态/Physical/External/Options=ok；surface_latest=empty（不是截断）；Night=stale+validation failure；basis/member rankings=missing；contract metadata=partial_error。

## 三、商品仪表盘（展示12项；全量扫描见覆盖核对）

`1D/5D`为同一具体主力结算收益；curve为近月减次月，正=backwardation。早前Night列统一为缺失，因为仓库没有9月29日有效快照；这不是“昨夜无波动”。

| 板块/品种 | 合约 | EOD close/settle | 1D / 5D | volume / OI / ΔOI | curve | Basis/Physical | 早前Night / day follow | 15:00后海外 | Options readiness | 21:00信号 |
|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| 芳烃 BZ | BZ2611 | 8763 / 8616 | +1.82% / +3.46% | 98,152 / 24,727 / -76 | +7.66% back | 无高质basis/实体变化 | 缺失/不可算 | Brent、WTI约-0.9%/-1.0% | 无可执行series | 高开追价差；等45分钟 |
| 芳烃 EB | EB2611 | 9917 / 9750 | +1.59% / +2.61% | 1,133,222 / 353,335 / +8,529 | +5.23% back | 无高质basis | 缺失/不可算 | 原油回落，反对追多 | chain未覆盖 | 回撤确认后才研究 |
| 贵金属 AG | AG2612 | 14848 / 14906 | -1.79% / -8.25% | 299,463 / 277,181 / +14,920 | -0.22% contango；z=-1.67 | 仓单刷新失败 | 缺失/不可算 | 银约60.98、日内转正约0.6%，与国内弱势冲突 | S/P/E=是/否/否；ATM14900 IV38.63% | 不追空，等30分钟反抽 |
| 铝链 AO | AO2701 | 2656 / 2658 | -1.59% / -2.39% | 218,053 / 266,990 / +34,128 | -0.61% contango | 无高质basis | 缺失/不可算 | LME铝代理不精确 | 是/是/否；ATM2650 IV16.62% | 反抽失败才偏空 |
| 橡胶 NR | NR2612 | 16410 / 16420 | -3.07% / +2.95% | 56,274 / 75,544 / +1,475 | -0.57% contango | 无高质basis | 缺失/不可算 | SGX/日胶精确映射缺失 | 是/否/否；ATM16400 IV21.92% | 等30分钟，不追首跳 |
| 原油 SC | SC2611 | 711.9 / 716.9 | -2.34% / -1.90% | 195,579 / 29,669 / -2,741 | +1.94% back；z=-1.24 | 无高质basis | 缺失/不可算 | WTI91.64、Brent104.32，均约-1% | 是/否/否；ATM720 IV74.70% | 偏低开；等45分钟 |
| 燃料油 FU | FU2611 | 4438 / 4418 | +0.64% / +4.54% | 641,064 / 150,615 / -19,038 | +22.97% back | 现货7637.5，但C级basis | 缺失/不可算 | 原油回落，反对追多 | 是/否/否；ATM4400 IV71.20% | 内外冲突，等45分钟 |
| 沥青 BU | BU2611 | 5246 / 5195 | +0.83% / -2.57% | 1,007,133 / 208,969 / -15,138 | +11.76% back | 无高质basis | 缺失/不可算 | 原油回落 | 是/是/否；ATM5200 IV48.82% | 高位不追；等45分钟 |
| 聚酯 TA | TA701 | 6350 / 6254 | +0.06% / -0.06% | 1,108,743 / 1,086,512 / +16,220 | +4.85% back；z=1.93 | 现货7328.75，C级basis | 缺失/不可算 | 原油回落 | 是/是/否；ATM6300 IV32.96% | 平低开风险；等30分钟 |
| 航运 EC | EC2611 | 2845 / 2871.5 | -1.17% / +10.40% | 20,962 / 24,626 / -840 | -26.68% contango；roll flag | 无最新运价确认 | 制度无Night/不适用 | 无15:00后同口径指数 | 无期权 | 下一窗口9/30 09:00 |
| 畜牧 JD | JD2611 | 3698 / 3717 | -2.31% / -3.10% | 325,331 / 208,218 / -45,089 | +3.17% back | 无可验证库存变化 | 无制度Night/不适用 | 不适用 | 无可执行series | 下一窗口9/30 09:00 |
| 新能源 LC | LC2701 | 118780 / 119540 | -1.06% / -8.80% | 255,636 / 415,687 / -8,400 | +0.13% back | 现货122000，C级basis | 无制度Night/不适用 | 锂代理约-2.3% | 是/否/否；ATM120000 IV44.28% | 下一窗口9/30 09:00 |

海外观测约19:30 BJT：WTI 91.64（-1.04%）、Brent 104.32（-0.91%）、金4160.67（+1.11%）、银60.98（+0.59%）、DXY约101.33（+0.13%）、USD/CNH约6.71且较前收走低。它们是海外实时/准实时代理，不表示中国期货已交易这些变化。油价日内来源间点位有小差异，方向均为自欧洲早段高位回落；人民币偏强部分抵消美元走强对进口成本的抬升。[海外报价](https://tradingeconomics.com/commodities)；[美元](https://tradingeconomics.com/united-states/currency)；[USD/CNH](https://ca.investing.com/currencies/usd-cnh-historical-data)。

## 四、相比上一期真正变化

1. **AG弱势延续但赔率下降。** 9月29日AG2612再跌2.17%（close口径），5D结算回报-8.25%，同时ΔOI +14,920、量能z=3.08；这只说明价仓归因线索，不等于已知“新空”。日内低点14745后收14848，首跳追空的坏成交风险上升。
2. **纯苯—苯乙烯成为最强链。** BZ2611/EB2611收盘分别+3.56%/+3.33%，两者backwardation为7.66%/5.23%；EB量能z=1.97且ΔOI +8,529。但15:00后海外油价约跌1%，新增外盘信息反对21:00直接追多。
3. **EC从昨日极强转为日内回撤。** EC2611高3020、低2781.5、收2845，收盘-2.08%，ΔOI -840；昨日“回撤接受多”上午条件是否触发无法由EOD路径核实，且今日curve为-26.68%并带roll flag，旧多头候选降级。
4. **AO/NR出现价跌仓增线索。** AO收盘-1.67%、ΔOI +34,128；NR收盘-3.13%、ΔOI +1,475，且二者contango。方向层支持下行，但实体和境外橡胶/氧化铝映射缺失。
5. **FU/BU继续强，但更像曲线与风险溢价而非全面量仓确认。** FU/BU收盘分别+1.09%/+1.82%，backwardation很深，但ΔOI分别-19,038/-15,138；海外原油随后回落，前期多头只保留条件观察。

## 五、产业链地图

| 链条 | 方向/强弱 | 价格—曲线—实体—海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|
| 纯苯→苯乙烯→聚酯 | **最强，但不追** | BZ/EB大涨且强back；TA收盘强于结算但1D结算近零；海外油价回落 | 苯乙烯/纯苯实体库存、利润与Night路径 | 中 |
| 贵金属 | 弱，AG优于AU作为下行观察 | AG/AU 5D -8.25%/-5.06%；AG价跌仓增、contango加深；海外金银在欧洲时段反弹、形成冲突 | 当日Night、当前期权bid/ask、白银库存 | 中 |
| 橡胶 | 弱 | NR/RU收盘-3.13%/-2.29%；NR价跌仓增、contango，RU价跌仓减 | 日胶/新胶精确盘后映射、库存变化 | 中低 |
| 原油—燃料 | 内部分化 | SC跌、FU/BU涨；三者backwardation仍在，15:00后Brent/WTI回落 | exact-contract裂解利润、仓单/库存方向 | 中低 |
| 航运 | 高波动回撤 | EC 5D仍+10.40%，但今日收盘-2.08%、OI下降、curve极端contango且roll flag | 同口径运价、盘中触发路径、期权工具 | 低至中 |

## 六、机会排行榜（研究吸引力，不是胜率）

| 排名 | idea_id / 方向 / 工具 | 逻辑/赔率/催化/价曲波/拥挤技术 | 总分 | 五层证据 | 判断 / 证据 / 执行 |
|---:|---|---:|---:|---|---|
| 1 | `COM-E-AG2612-DOWNSIDE-20260928` 偏空；AG2612或11/24熊市put spread | 21/17/14/9/8 | **69** | 支持1价仓、2contango；4海外反弹反对；3缺失；5可研究但不可执行 | 存在待验证优势 / 部分 / 等触发及报价 |
| 2 | `COM-E-AO2701-DOWNSIDE-20260929` 偏空；AO 12/25熊市put spread | 19/16/11/10/10 | **66** | 支持1价仓、2contango；5中性；3/4缺失 | 存在待验证优势 / 部分 / 待报价 |
| 3 | `COM-E-EB2611-BACKWARDATION-20260929` 回撤多；EB2611 | 18/14/12/12/9 | **65** | 支持1价量仓、2back；4油价回落反对；3/5缺失 | 存在待验证优势 / 部分 / 等触发与参数 |
| 4 | `COM-E-NR2612-DOWNSIDE-20260929` 偏空；NR2612/put spread | 18/14/10/11/10 | **63** | 支持1、2；5中性；3/4缺失 | 存在待验证优势 / 部分 / 等30分钟与报价 |
| 5 | `COM-E-EC2611-ROLL-20260924` 回撤接受多，研究观察 | 17/11/10/8/8 | **54** | 1仅弱支持；2极端contango反对；3/4/5缺失 | 证据不足 / 不足 / 9月30日盘重新验证 |

没有70+候选。两层有效独立支持的项目最高69，未用叙事补足实体或境外层；Options ready只表示可研究surface，不等于支持方向或可成交。

## 七、前三名研究卡

### 1. AG2612下行延续（条件卡，非当前委托）

- **市场隐含与分歧：** 市场已计入连续两日大跌和节前降风险；我们的分歧仅是“反抽若无法收复14980—15080，弱势可能再扩张”，不是认为任何价格都应追空。新增支持是9月29日价跌、OI与量能同步扩张及contango加深；竞争解释是节前移仓/对冲造成OI变化，且海外银已反弹。
- **最佳表达：** 优先AG2612对应2026-11-24到期1×1熊市put spread（买14900P、卖14000P）；只在21:30后取得双边报价、净支出≤价差宽度35%且盘口容量合格时研究。否则只观察线性期货，不用未报价期权假装限定风险。
- **入场/分批：** 好成交：反抽14980—15080失败后，15分钟收回14920下，1/2风险；中成交：跌破14745后反抽不越14820，1/3风险；坏成交：首跳直接低于14550，放弃。TP1 14550，TP2 14150；时间止损1—3D无扩张。逻辑失效：30分钟接受15220上方；彻底失效：15450上方且海外银转强。
- **风险与参数：** option最大损失=实际净支出，未报价不可计算；Greeks、滑点、净R待当前报价。AG乘数15kg、tick 1元/kg、tick value 15元；EOD名义价值约222,720元/手；静态last trading day 2026-12-15。9月29日结算后交易所通知AG2612涨跌停20%、套保保证金21%、一般保证金22%；线性期货1个涨停压力约44,720元/手、连续2个约98,384元/手，最大损失并非有限。夜盘通常21:00—02:30；本卡要求在2026-10-8恢复交易前清掉无法承受长假gap的Delta。来源：[上期/节日参数通知](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)。

### 2. AO2701下行（待报价卡）

- **事实/推断：** EOD 2656/2658，日内低2639；ΔOI +34,128、价跌仓增只是归因线索；near-next contango -0.61%。推断是弱势可能延续；反证是5D仅-2.39%、没有实体库存变化和精确LME氧化铝映射。
- **表达：** AO2701对应2026-12-25到期买2650P/卖2500P 1×1；surface-ready、positioning-ready，但bid/ask=0，execution-ready=false。最大净支出/最大损失、Greeks、滑点一律待报价。
- **入场/退出：** 21:30后反抽2680—2700失败且重新跌破2640，先1/2；跌破2639后回抽不过2650再加1/4。TP1 2580，TP2 2500；30分钟接受2720上方止损，2740上方逻辑失效；3D不扩张退出。首跳低于2580不追。
- **参数/压力：** 仓库仅确认last trading day 2027-01-15，乘数、tick、margin、limit、夜盘参数在本期metadata中缺失，故线性期货不可列为可执行替代，也不编1/2涨跌停金额。

### 3. EB2611 backwardation回撤多（参数待确认卡）

- **事实/错价：** close 9917、settle 9750、日内9555—9996；1D结算+1.59%、5D +2.61%、ΔOI +8,529、near-next back 5.23%。市场计入芳烃偏紧；我们的分歧是回撤若守9750可能仍有正carry。但海外原油收盘后约跌1%，最强反证是成本端风险溢价回吐。
- **表达与入场：** 仅EB2611线性期货；DCE期权series未覆盖。21:45后9750—9820获得30分钟接受并重新站上9920，1/3试仓；不在9996上方首跳追价。止损9650；逻辑失效9555下方接受或backwardation收窄至2%以下。TP1 10150、TP2 10400；时间止损2D。
- **风险：** 最大损失不有限。DCE合约元数据本期为`observed_contract_only`，乘数、tick、margin、limit、last trading day均未确认，故本卡只是研究触发器；参数确认前不得下单。最坏情景为海外油价继续下挫、节前流动性消失及假期地缘gap。

所有卡风险预算：单一试仓最大损失NAV 0.25%—0.50%；因贵金属/能化同因子合并计算；长假前不得把条件触发自动升级为确认仓位。若使用期货，止损只是计划风险，不是结构性最大损失。

## 八、商品期权专项

- 截面为**T日2026-09-29 EOD，本期新增**：13,324合约、184 series、180 surface-ready、46 positioning-ready、0 execution-ready；全局surface文件empty，但统一输入含逐series计算结果，读取状态不是truncated。
- AG2612 11/24：ATM 14900、ATM IV 38.63%、RR25 +2.86 vol、BF25 +1.78；AO2701 12/25：ATM2650、IV16.62%、RR25 +3.89、BF25 +1.00；NR2612 11/24：ATM16400、IV21.92%；FU2611 10/19：ATM4400、IV71.20%；SC2611 10/14：ATM720、IV74.70%。RR符号口径未用于推断dealer方向。
- IV-RV：AG IV约38.6%略高于RV20 34.2%；AO IV16.6%略高于RV14.3%；NR IV21.9%低于RV25.0%；FU/SC IV显著高于RV39.1%/59.2%。这些差值不单独证明便宜/昂贵；节前跳空与期限错配会改变可比性。
- `positioning_ready=false`时不使用PCR/OI拥挤；`dealer_gamma_direction_known=false`，禁止推断做市商净Gamma。所有series bid/ask coverage=0，因此不报权利金、净成本、滑点、Greeks或期望收益。event convexity只保留有限损失结构方向，执行前必须重新取价。

## 九、21:00夜盘开盘风险地图

严格四层：①9月29日中国EOD如上；②今天早前Night应得但仓库缺失，不能分解；③15:00—19:40海外新增：油价下、金银反弹、美元偏强/离岸人民币偏强；④今晚21:00尚未发生，归属9月30日交易日。

| 品种 | 预期开盘/冲突 | 追价？ | 等待 | 最重要确认 |
|---|---|---|---:|---|
| AG/AU | 平至小高；海外反弹与国内弱势冲突 | 否 | 30分钟 | AG能否收复14980；COMEX银是否守60.7 |
| SC/FU/BU | 偏低；国内燃料强而海外油价回落 | 否 | 45分钟 | Brent/WTI方向、SC 700/720、FU 4350/4450 |
| EB/BZ/TA/PX | 平低；国内最强链面对成本端回落 | 否 | 45分钟 | EB9750、BZ8500附近接受；back是否维持 |
| AO/NR/RU | 偏低或平；境外精确代理不足 | 否 | 30分钟 | AO2639、NR16210是否被有效跌破；OI只作线索 |
| CF/RM/OI/P | 平低；美元偏强但CNH偏强、外盘农产品偏弱 | 否 | 30分钟 | 中国自身成交与curve，不用代理硬套 |
| EC/LC/JD/LH | 无制度夜盘 | 不适用 | 下一日盘15—45分钟 | 9月30日09:00—09:45价量与curve |

**特殊日历：** 今晚21:00仍有夜盘；9月30日日盘后，当晚无Night。10月1—7日休市，10月8日08:55集合竞价、09:00复市，10月8日晚恢复Night。节前保证金和涨跌停扩大，意味着好方向也可能是坏交易。官方安排见[上期所通知](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)与[能源中心通知](https://www.ine.com.cn/publicnotice/notice/202609/t20260921_833506.html)。

## 十、未来24小时/7日事件日历（北京时间）

| 时间 | 事件 | 影响与处理 |
|---|---|---|
| 9月30日09:30 | 中国官方制造业PMI；市场预期约50.1、前值49.8 | 黑色、有色、能化Delta；不在9:00预埋大仓，等数据后15—30分钟。来源：[Reuters 2026-09-29](https://www.reuters.com/business/china-factories-seen-rebounding-september-beijing-signals-more-aid-2026-09-29/) |
| 9月30日约09:45 | RatingDog制造业PMI | 与官方PMI冲突时延迟入场，不用单一数据追价 |
| 9月30日20:30—22:00 | 美国ADP/PCE与劳动力数据窗口（具体时点以官方日历为准） | 美元、实际利率、贵金属Vega；AG只用有限损失结构 |
| 9月30日22:30 | EIA周度石油状态报告（常规周三10:30 ET） | SC/FU/BU/EB gap；中国当晚无Night，若无法海外对冲，日盘前主动降Delta。来源：[EIA schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 10月1日00:00 | USDA季度Grain Stocks（12:00 ET） | 豆、粕、油、玉米；中国休市，优先境外有限凸性或不持仓。来源：[USDA/NAL](https://esmis.nal.usda.gov/publication/grain-stocks) |
| 10月1—7日 | 中国期货休市 | 地缘、油田/炼厂、天气累积gap；无跨市场对冲能力则9月30日收盘前减仓 |
| 10月4日 | OPEC+七国会议 | 原油与能化Vega/Delta；目标为11月政策，避免假期裸空Gamma。来源：[Reuters 2026-09-06](https://www.reuters.com/business/energy/opec-set-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-06/) |

## 十一、旧建议台账与覆盖核对

### 旧建议处置

| idea_id | 首次提出 | 上次状态 | 当前状态/变更原因 |
|---|---|---|---|
| `COM-E-AG2612-DOWNSIDE-20260928` | 9月28日晚 | 9月29晨72分、等待09:30 | EOD继续下跌但盘中路径不足，晨间触发未知；不假设持仓。当前降至69，原因=价格变化与海外反弹。若此前按条件建立，仅在原止损未触发且能承受长假gap时管理，禁止追增 |
| `COM-E-EC2611-ROLL-20260924` | 9月24 | 69分、等待09:45 | 日内低2781.5低于旧参考2794，但是否形成45分钟接受未知；降至54并取消旧条件单。若此前建立，须核对成交与止损记录，不能因收盘2845自动声称持有/退出 |
| `COM-E-FU2611-ENERGY-20260928` | 9月28 | 65分、等待09:30 | 收盘续涨但OI显著下降、海外油价转弱；移出前五正式新卡，保留观察。若此前建立，9月30收盘前评估长假敞口，不加仓 |

### 覆盖核对

- **应覆盖：** 用户基线63个不同代码及动态新增；统一输入实际77个产品。强制清单全部有价格/曲线扫描，LPG以DCE代码`PG`对齐；动态新增BZ、LG、OP、PD、PL、PT等一并扫描。
- **实际取数且已分析：** 黑色建材9/9；有色贵金属12/12；能源炼化化工21/21（含PG别名）；新能源3/3及GFEX新增PT/PD；农产品油脂饲料畜牧17/17；航运EC 1/1。策略类别覆盖方向、curve、跨期、跨品种、跨市场代理、期权vol/skew/event convexity；周期覆盖1D/3D/5D/20D（足够历史者）。
- **数据不足：** 今日Night全模块；高质量basis；SHFE/DCE当日仓单；多数产品实体变化；5个External目标；25个期权产品；全部期权bid/ask；DCE合约参数、GFEX source-date验证。缺口限制对应工具，不删除品种。
- **不适用/流动性不足：** EC/LC/JD/LH等无Night；小品种/近月若量仓不足不入榜，但仍完成扫描。placeholder记录4条已排除异常排行。
- **未入榜板块异常：** 黑色无一致强趋势，FG价跌但back、仅噪音候选；农产品JD/LH价跌仓减更像去风险线索；软商品CF价跌仓增且contango，值得跟踪但缺Physical变化；新能源LC 5D -8.80%但价跌仓减、曲线近乎平，未发现三层优势；航运EC为最值得继续验证的roll异常。

压力测试必须合并考虑1/2个涨跌停、相关性破裂、流动性消失、保证金上调、9月30无Night后的长假gap、IV跳升/塌陷、交割挤压及人民币急变。研究分数不是胜率、期望收益或仓位建议。

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：无；AG/AO期权缺bid/ask、EB合约参数未确认，全部先观察而不提交委托。
C. 今晚应继续观察的机会：21:30后AG反抽失败、AO跌破回抽、21:45后EB守9750的触发；9月30日盘复核EC与FU旧观点。
D. 今晚必须避免或退出的交易：避免首跳追空AG/NR、追多EB/FU、C级basis套利和无bid/ask期权；无法对冲国庆长假gap的仓位须在9月30收盘前降至可承受水平。
