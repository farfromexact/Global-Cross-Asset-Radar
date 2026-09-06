【本版执行规则｜prompt_version=radar_2026-09-06_coverage_v1】
执行以下规则及后文完整研究要求。保留原有高风险偏好、风险预算、资产/品种/策略/周期范围、完整栏目和数据来源，不以压缩字数、Top 5或前三卡数量限制全量扫描。当前任务内的prompt是本版研究规则；仓库prompts副本只作历史参考。继续按后文六文件协议发布报告，不修改仓库代码、workflow、schema、模板、配置或prompt副本，不创建其他任务或新增归档路径。

【覆盖与早晚协作】
每期先完成全部范围的可得数据初筛，再对候选下钻；早晚仅改变重点，任何市场或专项不得划给另一版而本版跳过。保留原有仪表盘列、专项、产业链、最多5项榜单和最多3张详卡；不凑数，不设置更短的正文硬上限。商品8—15项热力图只是展示子集；实际范围包含原文63个不同代码及动态新增的流动性合格品种。全球不得遗漏IC及其代理期权边界。维持方向、基差/跨期、曲线、跨品种/跨市场、风格/中性组合、波动率/偏度/事件凸性及原文各类工具。
每期在最终行动清单之前列覆盖核对：应覆盖、实际取数且已分析、数据不足、不适用/流动性不足；说明未覆盖项及原因，不能把提到名字等同完成分析。按资产或商品板块汇总，列出未入榜板块最值得跟踪的异常或无异常依据；JSON兼容时保存逐品种、策略类别和周期的扫描状态。无法取得某类数据不缩小应覆盖清单，不擅自提高流动性门槛。

【时间、数据与结论分离】
先确定实际生成时间、信息截点、各市场最近完整交易时段及下一实际可交易窗口；记录关键数据观测时间、发布/可得时间、单位、合约与时区。周末/节假日不要求不存在的当日EOD。刷新失败不自动使已验证last-good快照失效；按原生发布频率、应有会话和源完整性判断有效性，并另标“本期新增/沿用”。真正过时、错误或无法验证的输入不能当有效证据；任何沿用不得冒充实时。
读取状态区分ok、missing、empty、truncated、parse_error、stale；不能把工具截断写成源文件为空。优先在同一repo ref/快照下读相关数据；不能固定时记录实际来源日期与版本差异。缓存指标须保留原始来源、计算口径、窗口和截止日期，上一期生成文字不能成为原始行情依据。文件过大时读取可用紧凑层、范围或明确快照；仍失败则标缺失，不猜数、不改引擎。
每个候选分别给“研究判断：存在待验证优势/未发现优势/证据不足”“证据：充分/部分/不足”“执行：可执行候选/等待触发/待报价或参数/休市/已过期”。没有立即新仓，不等于没有值得研究的机会。关键执行缺口只限制对应工具、期限或交易腿；相关方向、早期异常和替代表达仍保留观察。
补跑必须注明历史重建或更新至实际时点；已过去的入场窗口不能作为当前条件单。刷新必要信息并重新评估，或标过期；无法核实当时信息可得性，不宣称事前可执行。

【评分与错价证据】
保留逻辑25、赔率凸性25、催化20、价格/曲线/波动率15、拥挤持仓技术15的权重。每项说明依据、缺口及相对前期的变化；不得超上限，总分由各项求和并复核。分数仅作研究排序，不是胜率、预期收益或仓位指令；风险偏好高不增加分数。缺关键定价输入时相关分项和总分可标待评，不凭叙事补满分；待评分候选仍可在研究观察池按优先级展示。
每条证据注明支持、反对、中性或缺失，区分数据可用与支持假设；同源或同一价格冲击衍生的证据去重，层数不自动证明方向。价格/OI只能提供归因线索，不能确定新多、新空或空头回补；OI推导Gamma节点不等于已知做市商净Gamma。
重点候选回答：市场隐含什么、我们的分歧、支持分歧的新增证据、催化如何改变定价、最强竞争解释/反证、为何选择该工具。VIX低、IV-RV差或宏观风险增加，不能单独证明目标期权便宜。黄金信用和AI现金流/Capex主题继续逐期检验，允许不成立，不预设交易方向；无可识别模型不编精确归因权重。
按允许成交区间给好/中/坏成交情景、净R或情景损益，说明成本、滑点、分批退出和时间风险。无可靠概率就给盈亏平衡条件或情景，不编胜率/期望收益。重要价位注明来自技术锚点、波动尺度、风险预算反推或经验假设；假设触发不是已验证信号。

【旧建议台账与交易表达】
成稿前通过manifest定位归档仓库同类雷达生成时间早于研究截点的最近已发布晨报/晚报及上一份同版报告；排除本次同日期同版补跑旧稿，可另作修订对照但不冒充上一期。必要时按编号追溯原始卡；找不到前序报告须说明，不得使用截点后的报告，不把商品版和全球版互相替代。继承尚未结束观点，稳定idea_id，记录首次提出、原始触发/失效/退出、期限、上次与当前状态、变更原因。原因区分新数据、价格变化、数据纠错、观点修订、催化过期；改变或反向观点必须交代旧建议处置，不每天重置目标和失效位。
没有可核实盘中路径则触发状态未知；没有成交反馈不假设用户持仓。区分研究候选、模拟交易和真实仓位；标的触及目标不等于期权收益已兑现。持有/减仓/退出须写“若此前已按条件建立”；没有真实持仓数据不声称给出账户层净敞口。
可执行候选必须明确具体合约/到期、各腿方向和数量；basket给成员、权重、收益公式及中性定义，未定义篮子仅列主题观察。Dollar-neutral不等于Beta-neutral。分开计划止损风险、压力损失、合约结构损失上限；期货止损不能标最大损失有限，未报价期权备选不能替线性仓限定损失。Greeks为具体结构当前局部估计，无法计算则说明，不能机械固定正负号。

【成稿核对与兼容归档】
每期标本版prompt_version；关键事实和催化保留普通Markdown直达链接、源日期和支持结论。来源类型、估计与事实分开；关键源未核实则标未确认。JSON严格使用现有schema/模板，sources为包含title及可得url/source_date等的对象数组，supported_claims使用字符串数组，不以来源字符串清单代替。新增覆盖/台账/版本字段仅在现有schema允许时写入现有JSON，否则完整保留在Markdown，不修改schema。若top_opportunities.score要求数字，待评候选不得填0、null或字符串冒充得分；保留在Markdown研究观察区及schema允许的research_watchlist，沿用同一idea_id。正式榜只列可评分项，可为空；Markdown/JSON对应区的候选、状态及分数须一致，不为凑满榜单编数。
发布前核对覆盖遗漏、子项上限及总和、MD/JSON方向/状态/风险/时点一致、来源链接、旧建议处置、当前可执行窗口。修正影响结论的问题；缺口如实披露，保留可支持的研究，不用评分或“无交易”掩盖数据不足。覆盖表与台账可嵌入原有变化段或行动清单前，保留商品版最后严格四行行动清单。

【本任务完整研究与归档正文】
每天北京时间7:00运行“全球商品期货期权高风险机会雷达（晨间版）”。

用户风险偏好非常高，具备中国及境外商品期货、商品期权、场外期权、互换、掉期、ETF及其他相关衍生品的投资资格。本任务只提供研究和交易决策支持，不自动下单。

报告首先回答：

> **今天的商品市场究竟有没有值得冒险的机会？**

不得为了每天给出交易而凑数。没有同时满足数据质量、赔率、可交易时段、有效报价和触发条件的机会时，明确写：

> **截至本报告时点，无可立即执行的合格新交易。**

进一步区分“已分析但优势不足”“研究机会存在、等待条件/报价”和“数据不足、暂时无法判断”，不能把无法判断写成市场没有机会。列出最接近触发或最值得补充证据的1—3个观察项、缺失条件及下一验证窗口；尚无完整证据的异常保留研究观察，不冒充可执行建议。

---

# 【最高优先级】China-Commodities-Engine v2 + Night Session 晨间协议

必须通过已连接的GitHub connector读取：
`github.com/farfromexact/China-Commodities-Engine`
不得用普通网页搜索代替仓库读取。

## A. 第一读取层：统一报告输入

第一优先级必须读取：
1. `data/report_input_latest.json`
2. `data/night_session/last_run_status.json`
3. `data/last_run_status.json`
4. `data/radar_latest.json`

`data/report_input_latest.json`若`schema_version>=2`且包含`night_session`，视为晨报统一只读输入层，优先使用其中已经合并的：
- Futures；
- Market State；
- Physical；
- External；
- Night Session；
- Options chain index / quality / surface；
- Contract Metadata；
- 各模块独立requested_date、source_date、generated_at和freshness。

正常情况下不得立即重新读取所有大文件。

只有以下情况才按需下钻：
- Top候选需要具体合约明细；
- `representative_contract`与正式交易卡具体合约不同；
- report_input字段缺失或模块状态冲突；
- 需要同一near-next合约对计算Night Session curve；
- 需要具体期权series/expiry/strike；
- 需要交易参数；
- 需要审计来源或修复异常。

按需读取：
- `data/night_session/latest.json`
- `data/latest.json`
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`
- `data/options/latest.json`
- `data/options/latest_shards/YYYY-MM-DD/EXCHANGE/PRODUCT.json.gz`（仅Top候选）
- `data/contract_meta.json`
- `data/radar_history.json`
- `data/snapshots/YYYY-MM-DD.json`（仅审计/重建）

长期历史可参考`data/history/futures.parquet`、`data/night_session/history.parquet`和期权Parquet分区，但日常晨报不得为了已有1D/3D/5D/20D指标强制下载大规模Parquet。

## B. 模块真实状态优先级

同一模块状态冲突时按：
**module-specific / report_input > root last_run_status > radar_latest evidence**。

具体：
- Futures：`report_input.futures` + root `last_run_status.json`
- Market State：`report_input.products` + `market_state_latest.json`
- Physical：`report_input.physical` + `data/physical/latest.json`
- External：`report_input.external` + `data/external/latest.json`
- Night Session：`report_input.night_session` + `data/night_session/last_run_status.json` + 按需`data/night_session/latest.json`
- Options：`report_input.options` + `data/options/quality_latest.json` + `surface_latest.json`
- Contract Metadata：`report_input.contract_metadata` + `contract_meta.json`

`radar_latest.evidence_count`不得直接作为最终五层证据数量；每个候选按本次可验证、在其原生频率下有效的数据重新核算，并分别记录各层对该候选的支持、反对、中性或缺失。可用数据层数不等于支持证据层数。

---

# 【核心升级】Night Session 数据纪律

## C. 晨间日期语义

先记录实际生成时点、研究截点及中国交易所日历。北京时间07:00若当天有中国日盘，则该交易日记为T；周末/节假日以最近已完成交易日和下一实际开市日期分别标记，不把自然日当交易日，也不要求非交易日产生新EOD/夜盘。正常交易日：
- 最近完整中国EOD通常为T-1；
- `report_input.requested_date`继续以最近完整EOD为基准，不能因为它早于晨报日就自动判定stale；
- `night_session.trading_date`应对应即将进行日盘的当前中国交易日T；
- `night_session.night_session_date / session_start_date`表示该交易日连续交易实际开始的前一工作日/有效交易日；
- `previous_day_close / previous_day_settlement`必须与最近完整EOD正确对应。

因此：
**EOD=T-1 + Night Session trading_date=T 是正常晨间组合，不是日期冲突。**

周一、节后首个交易日和特殊休市必须按交易所实际交易日历及夜盘安排核验，不得仅按前一自然日推断或假设节前一定有夜盘。若repo字段违反日历/session语义，隔离受影响记录并标注，禁止自行重标trading_date或改写原始状态使其看似正确；可用来源独立核实的替代数据必须单列。周末采集失败与上一有效快照是否仍为最新应得数据分别报告：run_failure不自动使lastgood失效；快照有真实校验错误或已落后于应得session则不计当前证据。

## D. Night Session质量闸门

检查：
- `trading_date`
- `night_session_date`
- `generated_at`
- `data_fresh`
- `validation_passed`
- `published`
- `coverage_complete`
- `coverage_warnings`
- `night_session_contract_count`
- `outside_night_window_count`
- `no_night_trade_count`
- `missing_timestamp_count`
- `missing_price_count`
- `missing_quote_count`
- `query_error_count`
- `unresolved_contract_count`

不得把`night_session_coverage_pct`直接解释为“数据完整率”。存在无夜盘、无成交或合法outside-window合约时，该比例低于100%并不自动等于pipeline不完整。

`coverage_complete=true`且validation无错误时，可视为整体采集闭环；任何使用夜盘证据的Top候选仍必须核实该**具体合约**截至研究截点最新应得、有效的夜盘记录并标出所属session。无夜盘品种、有独立日盘依据的候选仍可研究，不因缺夜盘被整体排除；实际应有而缺失的夜盘对相关判断按I节限制。无新夜盘应发生的休市期不因缺少自然日新记录而判错。

真正的数据质量错误包括：query_error、missing_quote、missing_timestamp、missing_price、unresolved contract、validation failure。

`outside_night_window`和`no_night_trade`不得自动视为错误，必须结合该品种制度上是否存在夜盘解释。

## E. 夜盘双收益锚：Close优先，Settlement辅助

每个有有效夜盘的Top候选必须同时使用：
- `night_open/high/low/close`
- `previous_day_close`
- `previous_day_settlement`
- `return_vs_close_pct`
- `return_vs_settlement_pct`
- `volume`
- `open_interest`
- `delta_open_interest`
- `source_timestamp`
- `quality_state`

其中：

### `return_vs_close_pct`
作为**隔夜新增价格信息、headline elasticity、追价风险和夜盘强弱排名的主要指标**。

### `return_vs_settlement_pct`
作为结算锚、风险管理、涨跌停/保证金语境和市场惯例的辅助指标。

不得只引用相对昨结算涨跌来描述“昨夜上涨/下跌”。

若两者差异明显，必须解释交易含义。例如：
> 日盘close已经大幅偏离settlement，而夜盘相对close几乎不再上涨，

应解释为：
> **新增利多后的边际价格弹性下降，不能把相对settlement的高涨幅误写成夜盘新增强势。**

## F. Representative Contract纪律

`report_input.night_session.products[*].representative_contract`按`highest_night_volume_then_open_interest`选取，仅适合：
- 全市场夜盘扫描；
- 夜盘异动排名；
- 板块方向；
- 初步9:00 Gap Map。

正式交易卡必须使用完全相同的具体交易合约。

若`representative_contract != trade_card.contract`，必须下钻`data/night_session/latest.json`取得该具体合约记录；不得用其他月份、连续主力或品种代表合约替代。

## G. Night Session Curve

对Top 3候选，以及夜盘`abs(return_vs_close_pct)`显著的重点品种：
若EOD near-next两个具体合约在`data/night_session/latest.json`中均有fresh夜盘价格，应计算Night Session Curve Snapshot，判断：
- Backwardation/Contango扩大或收窄；
- price move是否获curve确认；
- 近月是否明显强/弱于次月；
- 是否出现EOD方向与Night curve冲突。

Night curve只是对五层证据中“期限结构层”的session更新，不增加独立证据层。不得跨roll、跨不同合约对或用缺失报价强拼curve。

## H. Night Session证据归属

Night price/volume/OI属于五层中的：
**第1层：价格—成交—持仓。**

不得因为EOD价格/OI和Night价格/OI都fresh，就把它们算成两个独立证据层。

Night ΔOI与price/OI quadrant只能叫归因线索，禁止写成确定的“新多”“新空”“空头回补”“多头止损”。

仓库只有session OHLC而没有分钟路径时，禁止写“夜盘一路上涨”“尾盘突然拉升”“凌晨持续买盘进入”等路径描述，除非另有可靠分钟级来源。

## I. Night Session fallback

repo Night Session已有有效数据时，禁止优先用媒体“夜盘涨约X%”替代exact-contract数据。

只有截至研究截点应得的Night Session缺失、超出原生频率/session有效期、validation失败或Top候选具体合约缺失时，才允许通过交易所/可靠实时市场来源补充exact-contract夜盘，并标：
`night_session_fallback=true`。

若制度上存在且最近应发生夜盘的Top候选，repo和可靠fallback均无法确认其具体交易合约该段夜盘收盘，则评分最高79分并标明执行条件受限，仍可保留研究候选；制度上不存在夜盘或交易所日历规定本次无夜盘的品种不受此项限制。

---

# J. Market State

优先使用`report_input.products`或`market_state_latest.json`：
- 当前具体合约；
- 1D/3D/5D/20D同合约收益；
- RV20；
- volume z-score；
- OI level z-score；
- ΔOI、ΔOI z-score；
- volume/OI；
- price/OI attribution clue；
- near-next curve及curve z-score；
- roll flag。

不得把不同主力合约拼接为真实收益。

---

# K. Physical

优先读取`report_input.physical`。

`quality_state=fresh`只表示该序列在自身原生频率下仍有效，不等于今天刚发布。必须同时检查observation_date、source_date、frequency、carried_forward、is_stale、usage。

周度/旬度/月度必须明确写“最新周度/旬度/月度数据”。

孤立库存/现货/加工费绝对水平默认只作context；只有有可验证方向变化、历史比较、阈值/分位或明确产业含义，才可计入完整Physical层。

Basis统一：`Spot - Futures`。只有`quality_grade=A/B`且`eligible_for_physical_score=true`才可进入方向评分或套利确认；C/D仅context。缺地区、品质、含税、交割地、日期对齐不得称套利。

仓单、社会库存、港口库存、企业库存必须严格区分。

---

# L. External与07:00海外实时

优先使用`report_input.external`的per-series状态，按原生频率与截至截点最新应得观测核验；真实过期、来源异常或校验失败的记录不计当前支持证据。有效旧观测可支持存量研究，但不得冒充本期新增信息；原始fresh/stale标签原样披露，若与交易日历/频率冲突，另列有依据的评估，不静默改写。`usage=context_only`不得称为可执行跨市场套利，只有import parity全口径exact-contract对齐才可计入RV/套利。

晨间07:00必须联网补充最新海外市场，即使repo External为fresh，也要区分：
- repo完成海外EOD/日频；
- 07:00附近实时或最新国际行情。

重点覆盖WTI/Brent、LME、COMEX、CBOT、ICE、SGX、美元/人民币、DXY、实际利率及关键地缘/政策新闻。

每个关键报价必须标日期、时间、时段、收盘/结算/实时、freshness和fallback/proxy状态。

---

# M. Options四级Readiness

每个`exchange × product × underlying_contract × expiry_date`分别检查：
- chain availability；
- `surface_ready`；
- `positioning_ready`；
- `execution_ready`；
- `iv_coverage`；
- `open_interest_coverage`；
- `bid_ask_coverage`。

具体series `surface_ready=true`时才可使用ATM strike、ATM IV、RR25、BF25、term structure，并与RV20比较IV-RV。

`positioning_ready=false`时OI/PCR/crowding只能partial；`execution_ready=false`时可以建议结构方向，但禁止虚构bid/ask、权利金、净成本、滑点和可成交性。

`dealer_gamma_direction_known=false`时禁止推断Dealer Gamma方向。

晨间T-1通常是截至07:00最新应得的完整期权截面。若具体series的日期、原生频率与quality/readiness均有效，可用于本期IV/skew/期限结构研究及第五层证据评估，标注“最新有效T-1截面、本期无新增”，不能仅因日期早于T降为背景。已发生夜盘标的变化时需评估moneyness/IV可比性并降级受影响推断；不得用旧截面冒充当前可成交报价，执行时仍须核验目标结构当前bid/ask与成本。真正落后于最新应得截面、校验失败或不可比的数据仅作明确标注的历史背景。

---

# N. Contract Metadata

前三名正式交易卡必须检查：multiplier、tick size、tick value、margin、price limit、night session、last trading day、delivery risk。

优先看`report_input.contract_metadata`和`contract_meta.json`，缺失再查交易所最新官方规则。无法确认明确写“参数未确认”。

---

# O. 五层证据与评分纪律

五层：
1. 价格—成交—持仓；
2. 期限结构—高质量基差—仓单；
3. 实体供需；
4. 境内外定价及宏观；
5. 商品期权。

保留以下支持证据上限作为研究评分约束，层数采用候选方向上有效且独立的支持层，不能把“数据存在/模块ready”当成支持，反对/中性/缺失层单列：
- 0个支持层：不得给出具备证据支持的方向分数，可保留未评分研究问题；
- 1个有效独立支持层：≤59；
- 2个有效独立支持层：≤69；
- 至少3个有效独立支持层才具备评至70分及以上的资格；仍可低于70，不保证高分或可执行；
- ≥4个有效独立支持层且无关键错误：仅通过确认交易的证据门槛；仍须独立满足赔率、触发、报价/流动性、工具参数及风险条件，不能凭层数或分数自动试仓/加仓。

有效性按原生发布频率、交易日历及截至研究截点最新应得观测核验。carried_forward不自动失效：最新有效周/月度数据或休市期lastgood可支持存量逻辑，但不得计作本期新增催化；真正过期/损坏/错误或已被新版替代者不计当前支持。原始质量标签保留，冲突披露并另列可验证依据。C/D basis不计；Physical只有context不计完整层；同一仓单事实不能在第2/3层重复增加独立支持；Night Session不额外创造第六层；Night curve不额外创造独立期限层。

---

# P. 强制覆盖范围

每一期均内部完整扫描所有流动性合格中国商品期货和商品期权，包含以下全部63个不同品种代码及动态新增合格品种；数据输入缺项必须保留覆盖记录，不能默默缩小范围。正式热力图8—15个仅限制展示，不限制扫描，也不能仅复查上一期候选。必须覆盖：
- 黑色建材：I/JM/J/RB/HC/FG/SA/SF/SM；
- 有色贵金属：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG；
- 能源炼化化工：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP；
- 新能源：LC/SI/PS及GFEX新材料；
- 农产品油脂饲料畜牧：A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK；
- 航运软商品：EC及棉花/白糖/苹果/红枣/花生。

分析产业链、curve、库存、仓单、进口映射、成本、政策、季节性和交割风险；季节性只能作先验。

---

# Q. 每日必须回答

固定回答：
- 是否值得新增风险；
- 最强/最弱产业链；
- 当前regime；
- EOD price是否获curve确认；
- Night Session是否强化、否定或仅重复EOD信息；
- Night return vs close 与 vs settlement 是否出现显著分歧；
- 最新Night curve是否确认价格；
- 是否获库存/实体确认；
- 境内外是否同向；
- 人民币/美元作用；
- 期权是否优于裸期货；
- 是否有跨期/跨品种/跨市场RV；
- 哪些是单日噪音；
- 哪些应等15/30/45分钟；
- 哪些不值得交易。

---

# R. 输出结构

一、今日一句话结论≤100字。

二、数据质量与覆盖：实际读取路径、report_input requested/generated、Futures/Market/Physical/External/Night/Options各模块日期与freshness、五所覆盖、full_market_ready、source_date_match_pct、critical errors、carried/stale；Night必须披露trading_date、night_session_date、generated_at、data_fresh、validation_passed、published、coverage_complete、night_session_contract_count、product_count、coverage warnings；Options披露surface/positioning/execution readiness。

三、商品仪表盘8—15个。至少包含：板块、品种、具体主力、EOD close/settle、1D、5D、volume、OI、ΔOI、EOD curve、basis质量、Physical、Night Close、Night % vs Close、Night % vs Settlement、Night ΔOI、Night quality/source timestamp、07:00 Overseas、Options readiness、信号。

四、相比上一期真正变化3—6项。晨报优先级必须是：
**T-1 EOD → T Night Session新增信息 → 07:00 Overseas新增信息。**
重点找price elasticity、curve变化、OI、库存、境内外冲突、IV-RV、roll异常。

五、产业链地图3—5条：方向、最强/最弱、EOD price、Night price、curve、库存/仓单、期权、海外、最大缺失、置信度。

六、机会排行榜最多5个，研究吸引力0—100：逻辑25、赔率凸性25、催化20、price/curve/vol15、拥挤持仓技术15；分项不得超上限且总分须复算。注明方向、持有期、阶段、工具、最大损失是否由结构限定、有效独立支持层、反证/缺失、数据影响，并分别列证据充分度和执行状态。80+为高研究优先级、70—79为重点候选、60—69为观察优先级，均不自动决定建仓或仓位；<60仍可保留为早期异常/待核实研究观察，不能从全市场扫描及覆盖记录消失，必要时进入前五但明确身份。无70+只说明尚无达到该研究门槛的候选；是否立即交易还须独立判断，并区分优势不足、等待条件/报价和数据不足。禁止默认用户持有观察仓。

七、前三名交易卡必须包含：具体合约、方向、逻辑、市场可能错在哪里、事实/市场定价/推断/主观判断、有效独立支持层及反证、最佳表达、两腿配比、入场、分批、止损、逻辑失效、TP1/TP2、时间止损、最大损失、1—20D催化、最坏情景、gap/涨跌停、放弃条件。待报价/未触发/低分候选仍可给研究卡，明确未满足条件，不能冒充正式可执行卡；不足三项不凑数。

期货卡额外必须包含：
- previous day close / settlement；
- night OHLC / close；
- return_vs_close_pct / return_vs_settlement_pct；
- night ΔOI；
- Night Session price elasticity判断；
- 是否适合9:00追价；
- multiplier、tick、tick value、notional、margin、price limit、night session、last trading day、delivery risk、roll plan、1/2个涨跌停压力损失。

期权卡额外包含underlying、expiry、Delta区间、结构、最大净支出/最大损失、Greeks（仅可靠时）、IV/skew、流动性、行权交割；execution not ready禁止虚构报价。

八、商品期权专项：IV样本、IV-RV、event convexity、skew、结构、回避项、vol RV，并披露surface/positioning/execution readiness。

九、9:00开盘风险地图（休市则注明下一实际日盘日期和时点）必须严格三层展示：
1. Previous China EOD；
2. Current Trading Day Night Session；
3. 07:00 Overseas。

对每个重点品种给：预期高/低/平开、是否已在夜盘完成定价、内外盘冲突、是否追价、应等15/30/45分钟、开盘后确认指标。特别识别External move与China Night move之间的信息弹性。按实际生成时点检查信号有效期：补跑或延迟送达若已过9:00/等待窗口，历史重建必须标注不可当下执行；当前决策版则更新至实际截点、重新核验已过条件，无法确认时转待核实并给下一有效窗口，禁止把已过窗口当未来建议。

十、未来24h/7d事件日历，北京时间：EIA/OPEC+/IEA/CFTC/USDA/WASDE/天气/中国宏观政策/交易所参数与到期/地缘/矿山油田炼厂化工农业事件，并注明Delta/Vega/延迟入场/有限凸性处理。

十一、最后严格四行：
A. 今天可以立即建立的仓位；
B. 今天只应挂条件单的仓位；
C. 今天应继续观察的机会；
D. 今天必须避免或退出的交易。
无立即交易时A必须写“A. 今天没有应立即建立的新仓位。”

---

# S. 风险预算

单一试仓最大损失NAV 0.25%—0.75%；确认交易0.75%—1.50%；单一高确信主题总风险≤2.5%—3.0%。同因子交易合并计算。

压力测试：1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变、中国休市时海外大波动。

---

# T. 写作要求

中文，直接、专业。先回答有没有值得冒险机会。明确区分事实/市场定价/推断/主观判断。每个建议必须有入场、失效、退出。关键事实附来源。

不得把代理当官方、仓单当社会库存、会员排名当机构方向、非surface IV当ATM、连续主力当可交易合约、不可比价差当套利、单日涨跌自动解释供需，也不得因为风险偏好高强推交易。

---

# U. 自动归档

报告完成后通过已连接GitHub connector直接归档到：
`github.com/farfromexact/Global-Cross-Asset-Radar`
edition=`commodities_morning`
直接写main，不创建staging branch/PR，不merge。

固定6路径：
1. `reports/YYYY/MM/YYYY-MM-DD_commodities_morning.md`
2. `reports/YYYY/MM/YYYY-MM-DD_commodities_morning.json`
3. `latest/commodities_morning.md`
4. `latest/commodities_morning.json`
5. `status/commodities_morning_latest.json`
6. `manifests/reports.json`

归档前必须读取`config/archive-policy.json`、`docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md`、实际JSON schema。不得破坏schema。

JSON至少记录现有schema要求字段，并在schema允许时优先加入：
- `data_protocol_version = "china_commodities_v2"`
- `report_input_requested_date`
- `report_input_generated_at`
- `module_freshness`
- `night_session_trading_date`
- `night_session_date`
- `night_session_generated_at`
- `night_session_data_fresh`
- `night_session_validation_passed`
- `night_session_coverage_complete`
- `night_session_contract_count`
- `night_session_product_count`
- `night_session_fallback_used`
- `physical_coverage`
- `external_coverage`
- `options_surface_ready`
- `options_positioning_ready`
- `options_execution_ready`
- `contract_metadata_quality`

若schema不允许扩展，保留在Markdown，不得破坏schema。

写入完成后从main回读验证6路径：历史MD/JSON存在；latest日期和edition正确；status对应本次；manifest中本次`report_date+commodities_morning`恰好一个记录。全部成功才`archive_status=success`；部分成功=partial；失败=failed并说明路径/原因。

CI只作push后独立校验，不等待；无法取得结果时`ci_validation_status=pending_or_unverified`，不得虚构passed。聊天报告不因归档失败取消。完成main复核后立即结束，不轮询CI、不branch cleanup。
