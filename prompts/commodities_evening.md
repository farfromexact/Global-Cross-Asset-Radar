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
每天北京时间19:30运行“全球商品期货期权高风险机会雷达（晚间版）”。

用户风险偏好非常高，具备中国及境外商品期货、商品期权、场外期权、互换、掉期、ETF及其他相关衍生品的投资资格。本任务只提供研究和交易决策支持，不自动下单。

报告首先回答：

> **今晚的商品市场究竟有没有值得冒险的机会？**

不得为了每天给出交易而凑数。没有同时满足数据质量、赔率、可交易时段、有效报价和触发条件的机会时，明确写：

> **截至本报告时点，无可立即执行的合格新交易。**

进一步区分“已分析但优势不足”“研究机会存在、等待条件/报价”和“数据不足、暂时无法判断”，不能把无法判断写成市场没有机会。列出最接近触发或最值得补充证据的1—3个观察项、缺失条件及下一验证窗口；尚无完整证据的异常保留研究观察，不冒充可执行建议。

---

# 【最高优先级】China-Commodities-Engine v2 + Night Session 晚间协议

必须通过已连接的GitHub connector读取：
`github.com/farfromexact/China-Commodities-Engine`
不得用普通网页搜索代替仓库读取。

## A. 第一读取层

第一优先级读取：
1. `data/report_input_latest.json`
2. `data/last_run_status.json`
3. `data/night_session/last_run_status.json`
4. `data/radar_latest.json`

`report_input_latest.json`若`schema_version>=2`，视为统一报告输入层，优先使用其中已合并的：
- Futures；
- Market State；
- Physical；
- External；
- Night Session；
- Options chain / quality / surface；
- Contract Metadata；
- 各模块独立requested_date、source_date、generated_at、freshness。

正常情况下不得立即重新读取所有大文件。只有以下情况才下钻：
- report_input仍是T-1但某个module-specific文件已更新到T；
- Top候选需要具体合约；
- 需要具体期权series/expiry/strike；
- 需要交易参数；
- 需要核实当日EOD与早前Night Session的具体合约关系；
- 模块状态冲突或需要审计异常。

按需读取：
- `data/latest.json`
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/night_session/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`
- `data/options/latest.json`
- `data/options/latest_shards/YYYY-MM-DD/EXCHANGE/PRODUCT.json.gz`
- `data/contract_meta.json`
- `data/radar_history.json`
- `data/snapshots/YYYY-MM-DD.json`

长期历史可参考futures/night_session/options Parquet，但日常晚报不得为了已有1D/3D/5D/20D指标强制下载大文件。

## B. 模块状态优先级

冲突时按：
**module-specific / report_input > root last_run_status > radar_latest evidence**。

具体：
- Futures：`report_input.futures` + root status
- Market State：`report_input.products` + `market_state_latest.json`
- Physical：`report_input.physical` + `physical/latest.json`
- External：`report_input.external` + `external/latest.json`
- Night Session：`report_input.night_session` + `night_session/last_run_status.json`
- Options：`report_input.options` + `options/quality_latest.json` + `surface_latest.json`
- Metadata：`report_input.contract_metadata` + `contract_meta.json`

`radar_latest.evidence_count`不得直接作为最终五层证据数量；每个候选按本次可验证、在其原生频率下有效的数据重新核算，并分别记录各层对该候选的支持、反对、中性或缺失。可用数据层数不等于支持证据层数。

---

# 【核心升级】19:30的Night Session时间语义

## C. 当前交易日与夜盘必须严格区分

先记录实际生成时点、研究截点及中国交易所日历。北京时间19:30若当天为中国交易日，则该交易日记为T；周末/节假日分别使用最近已完成交易日和下一实际开市日期，不把自然日当交易日，也不要求非交易日产生新EOD/夜盘。以下T日EOD/今晚21:00流程适用于交易所实际安排该时段开市的日期。

如果当日中国EOD已完成：
- Futures / Market State / Physical应尽量使用T日完整EOD；
- `report_input.night_session.trading_date == T`时，该Night Session是**今天凌晨/昨晚已经完成的、属于T交易日的连续交易阶段**；
- 它可以用于复盘“隔夜阶段→日盘阶段”的信息吸收、gap follow-through或reversal；
- 它**绝不是今晚21:00即将开始的下一段夜盘**。

交易所日历确认今晚有夜盘时，21:00后开始的连续交易归属交易所定义的下一中国交易日T+1（不是下一自然日）；节前或特殊休市若无夜盘，改列下一实际夜盘或日盘窗口及所属交易日。

因此19:30时：
- 禁止把`night_session.trading_date=T`的数据写成“今晚夜盘已经上涨/下跌”；
- 禁止从repo制造或推断T+1夜盘价格；
- 如果在合法开盘前发现`night_session.trading_date=T+1`且source_timestamp处于未来/非合法session窗口，必须视为异常，不得使用；
- 21:00风险地图必须使用**T日EOD + 15:00—19:30海外最新变化 + 事件信息**，而不是未来夜盘数据。

周一、节后首个交易日及特殊休市，Night Session日期必须按交易所实际交易日历及夜盘安排核验，不得只按自然日推断或假设节前一定有夜盘。若repo日期/session语义异常，隔离受影响记录并标注，禁止自行重标trading_date或改写原始状态使其看似正确；可用来源独立核实的替代数据必须单列。周末采集失败与上一有效快照是否仍为最新应得数据分别报告：run_failure不自动使lastgood失效；快照有真实校验错误或已落后于应得session则不计当前证据。

## D. 已完成Night Session在晚报中的用途

当`night_session.trading_date=T`且为所属session有效/validated记录时，晚报应使用它回答；休市报告可复核最近完整交易日但必须标注实际日期，不冒充当日新行情：
- 今天的主要涨跌有多少在夜盘已经发生？
- 日盘是follow-through、横盘消化还是reversal？
- Night close相对previous close的变化，与T日EOD close/settle之间形成了什么“隔夜→日盘”路径？
- Night ΔOI与T日EOD ΔOI是否同向或反向？只作归因线索，不推断最终资金身份。
- 如果夜盘已经完成大部分价格发现，而日盘没有继续扩张，是否说明边际信息弹性下降？
- 如果夜盘弱但日盘强，是否说明中国日间现货/产业/政策信息重新定价？

晚报可定义两个复盘指标：
1. `overnight_return = night_close / previous_day_close - 1`（优先使用repo `return_vs_close_pct`）
2. `day_follow_through = T_EOD_close / night_close - 1`（仅exact-contract对齐时计算）

不得用`return_vs_settlement_pct`替代overnight新增信息；它仅作结算锚辅助。

如果Night代表合约与晚报正式交易合约不同，必须下钻`data/night_session/latest.json`取得同一具体合约，才能做overnight/day decomposition。

Night price/OI仍属于五层中的第1层，不增加第六证据层。

---

# E. 19:30 EOD流水线时点纪律

18点后国内EOD流水线会更新仓库；19:30任务开始时各模块可能不同步。

执行顺序：
1. 先读`report_input_latest.json`及module_freshness；
2. 检查root status确认T日Futures是否完成、五所是否一致；
3. 若report_input仍T-1，但`latest.json`/`market_state_latest.json`/`physical/latest.json`已有T日fresh数据，则按module-specific文件使用并逐模块披露，不得把旧report_input冒充T日；
4. 若T日Futures/Market/Physical已完成而Options仍T-1：按各序列原生发布时间核验截至截点最新应得数据。若T日期权截面已应发布却缺失，T-1标为落后、仅历史背景；若T日完整截面按原生流程尚未应得且T-1仍有效，可支持存量期权研究并标明日期/无新增，重新评估标的变动后的moneyness/IV可比性，不冒充T日变化或当前成交报价；
5. 不得为了等待Options或某个非关键module而错过21:00决策窗口；
6. 不持续轮询GitHub Action；按当前可验证状态完成报告；
7. 15:00—19:30海外市场必须联网补充最新实时/准实时变化，并与repo External EOD明确分层。

---

# F. Market State

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

不得拼接不同主力合约为真实收益。价涨仓增/减、价跌仓增/减只叫归因线索。

---

# G. Physical

优先读取`report_input.physical`。

`quality_state=fresh`只表示在原生发布频率下仍有效，不等于今天刚发布。检查observation_date、source_date、frequency、carried_forward、is_stale、usage。

周度/旬度/月度写清原生频率。孤立绝对水平只作context；只有方向变化、历史比较、阈值/分位或明确产业意义才计完整Physical层。

Basis=`Spot-Futures`。仅A/B且`eligible_for_physical_score=true`可进方向评分/套利；C/D仅context。仓单、社会库存、港口库存、企业库存严格区分。

---

# H. External与19:30海外实时

repo External是日频层；19:30必须联网补充15:00—19:30的最新海外变化。

重点覆盖WTI/Brent、LME、COMEX、CBOT、ICE、SGX、DXY、USD/CNH、实际利率及关键地缘/政策事件。

不得把海外15:00后上涨写成“中国期货已经上涨”；它只是21:00潜在gap的映射证据。

`usage=context_only`不得称可执行套利；import parity必须exact-contract/币种/单位/品质/运费/税费/时点全部对齐才可作为RV证据。

---

# I. Options四级Readiness

每个`exchange × product × underlying_contract × expiry_date`分别检查chain、surface_ready、positioning_ready、execution_ready、iv_coverage、OI coverage、bid_ask coverage。

surface-ready才使用ATM IV/RR25/BF25/term structure并与RV20比较。

positioning not ready时OI/PCR/crowding只能partial；execution not ready时禁止虚构bid/ask、权利金、净成本、滑点和可成交性。

`dealer_gamma_direction_known=false`禁止推断Dealer Gamma方向。

19:30若T日Options仍未完成，按最新应得截面及原生发布时间判断：最新有效T-1可用于存量期权研究与第五层证据评估，披露日期、无新增及标的变化导致的可比性限制；已落后于应得T日截面者仅作历史背景。执行仍需当前目标结构bid/ask与成本，不能以T-1研究有效替代execution_ready；不为等待Options而错过决策窗口。

---

# J. Contract Metadata

前三名交易卡检查：multiplier、tick size、tick value、margin、price limit、night session、last trading day、delivery risk。

优先`report_input.contract_metadata`与`contract_meta.json`；缺失再查交易所最新官方规则；无法确认写“参数未确认”。

必须核实每个重点品种今晚是否有夜盘及交易时段；无夜盘则按交易所日历写下一实际日盘日期和开盘时点，不能在周末/假期机械写次日9:00。

---

# K. 五层证据与评分纪律

五层：
1. 价格—成交—持仓；
2. 期限结构—高质量基差—仓单；
3. 实体供需；
4. 境内外定价及宏观；
5. 商品期权。

保留以下支持证据上限作为研究评分约束，层数采用候选方向上有效且独立的支持层，不能把“数据存在/模块ready”当成支持，反对/中性/缺失层单列：
- 0个支持层：不得给出具备证据支持的方向分数，可保留未评分研究问题；
- 1个有效独立支持层≤59；
- 2个有效独立支持层≤69；
- 至少3个有效独立支持层才具备评至70分及以上的资格；仍可低于70，不保证高分或可执行；
- ≥4个有效独立支持层且无关键错误仅通过确认交易的证据门槛，仍须独立满足赔率、触发、报价/流动性、工具参数及风险条件，不能凭层数或分数自动试仓/加仓。

有效性按原生发布频率、交易日历及截至研究截点最新应得观测核验。carried_forward不自动失效：最新有效周/月度数据或休市期lastgood可支持存量逻辑，但不得计作本期新增催化；真正过期/损坏/错误或已被新版替代者不计当前支持。原始质量标签保留，冲突披露并另列可验证依据。C/D basis不计；Physical仅context不计完整层；同一仓单事实不能在第2/3层重复增加独立支持；早前Night Session只更新第1层，不新增独立层；最新有效T-1 Options依E/I节条件评估研究用途，不冒充T日新截面。

---

# L. 数据质量闸门

核心期货检查source_date_match_pct、unknown/duplicate/invalid OHLC/placeholder/negative volume or OI、critical errors、full_market_ready、excluded exchanges、carried-forward counts、validation errors、各交易所source-date。

某所source_date与交易日历及截至截点最新应得session不匹配时，不得据该异常记录建立立即交易；非交易日沿用最新有效交易日不属日期错误。零价/零量零仓/-100%占位排除异常排行；历史不足3/5/20日不得输出对应趋势或z-score。

只有根目录核心期货不满足full_market_ready、五所完整、截至截点最新应得/有效及验证一致时才检查`data/scoped/*/`回退；不得仅因周末刷新失败而放弃有效lastgood，不得静默拼接不同交易日/生成时点/scope。真实source-date冲突、损坏或过期记录仍须排除或降级，不可通过改标签绕过质量闸门。

如DCE缺失，明确本期不是完整中国商品市场，并说明黑色、油脂、养殖、塑化等判断受限。

---

# M. 强制覆盖范围

每一期均内部完整扫描所有流动性合格中国商品期货和商品期权，包含以下全部63个不同品种代码及动态新增合格品种；数据输入缺项必须保留覆盖记录，不能默默缩小范围。正式热力图8—15个仅限制展示，不限制扫描，也不能仅复查上一期候选。必须覆盖：
- 黑色建材：I/JM/J/RB/HC/FG/SA/SF/SM；
- 有色贵金属：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG；
- 能源炼化化工：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP；
- 新能源：LC/SI/PS及GFEX新材料；
- 农产品油脂饲料畜牧：A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK；
- 航运软商品：EC及棉花/白糖/苹果/红枣/花生。

分析产业链、加工利润、curve、库存/仓单、境内外映射、成本、政策、季节性与交割风险；季节性只作先验。

---

# N. 晚报必须回答

固定回答：
- 今晚是否值得新增风险；
- 最强/最弱产业链；
- 当前regime；
- 今天涨跌有多少来自早前Night Session、多少来自日盘follow-through/reversal；
- EOD price是否获curve确认；
- 是否获库存/实体确认；
- 15:00—19:30海外变化是否与中国EOD同向；
- 21:00可能gap是否已经被中国白天价格部分预交易；
- 人民币/美元作用；
- 期权是否优于裸期货；
- 是否有跨期/跨品种/跨市场RV；
- 哪些是单日噪音；
- 哪些夜盘应等15/30/45分钟；
- 哪些不值得交易。

---

# O. 输出结构

一、今晚一句话结论≤100字。

二、数据质量与覆盖：实际路径、report_input requested/generated、各模块日期/freshness、五所覆盖、full_market_ready、source_date_match_pct、critical errors、carried/stale、Physical/External、Options T日或T-1及surface/positioning/execution readiness。Night Session必须明确其`trading_date`，并注明“属于今天已完成的连续交易阶段”还是与当前报告无关的旧快照，禁止将其写成今晚未来行情。

三、商品仪表盘8—15个：板块、品种、具体主力、T日EOD close/settle、1D、5D、volume、OI、ΔOI、curve、basis、Physical、早前Night close及`return_vs_close_pct`（若同合约可比）、`day_follow_through`（若可算）、15:00—19:30 Overseas、Options readiness、21:00信号、数据时间。

四、相比上一期真正变化3—6项。优先：
- 今天EOD相对上一完整EOD；
- 早前Night→日盘的follow-through/reversal；
- curve/OI/库存/仓单；
- 15:00后海外新增定价；
- IV-RV和roll异常。

五、产业链地图3—5条：方向、最强/最弱、T日价格、早前Night→Day分解、curve、库存/仓单、期权、海外、最大缺失、置信度。

六、机会排行榜最多5个，研究吸引力0—100：逻辑25、赔率凸性25、催化20、price/curve/vol15、拥挤持仓技术15；分项不得超上限且总分须复算。注明方向、持有期、阶段、工具、最大损失是否由结构限定、有效独立支持层、反证/缺失、数据影响，并分别列证据充分度和执行状态。80+为高研究优先级、70—79为重点候选、60—69为观察优先级，均不自动决定建仓或仓位；<60仍可保留为早期异常/待核实研究观察，不能从全市场扫描及覆盖记录消失，必要时进入前五但明确身份。无70+只说明尚无达到该研究门槛的候选；是否立即交易还须独立判断，并区分优势不足、等待条件/报价和数据不足。禁止默认用户持有观察仓。

七、前三名交易卡：具体合约、方向、逻辑、市场可能错在哪里、事实/市场定价/推断/主观判断、有效独立支持层及反证、最佳表达、两腿配比、入场、分批、止损、逻辑失效、TP1/TP2、时间止损、最大损失、1—20D催化、最坏情景、gap/涨跌停、放弃条件。待报价/未触发/低分候选仍可给研究卡，明确未满足条件，不能冒充正式可执行卡；不足三项不凑数。

期货卡额外：
- T日EOD close/settlement；
- 若可比，今天早前night_close与overnight_return；
- `day_follow_through`或day reversal；
- 今晚21:00是否有night session；
- 15:00—19:30海外映射；
- 21:00首跳是否适合追价；
- multiplier、tick、tick value、notional、margin、price limit、last trading day、delivery risk、roll plan、1/2个涨跌停压力损失。

期权卡额外：underlying、expiry、Delta区间、结构、最大净支出/最大损失、Greeks（仅可靠时）、IV/skew、流动性、行权交割；execution not ready禁止虚构报价。

八、商品期权专项：IV样本、IV-RV、event convexity、skew、结构、回避项、vol RV，明确Options是T日还是T-1并披露readiness。

九、**21:00夜盘开盘风险地图**（休市则注明下一实际夜盘/日盘日期和时点）。必须严格区分：
1. T日中国完整EOD；
2. 今天早前已完成Night Session（只作历史价格发现分解）；
3. 15:00—19:30海外最新变化；
4. 截至研究截点尚未发生的下一实际Night Session（正常19:30报告即当晚21:00开始、归属T+1）。补跑时已经开市的部分必须单列为已发生行情，不能继续称未来。

对实际安排有夜盘的品种给：可能高/低/平开、海外与国内冲突、是否首跳追价、应等15/30/45分钟、开盘后最重要确认指标。无夜盘品种按交易所日历注明下一实际日盘日期和开盘时点。按实际生成时点检查信号有效期：补跑或延迟送达若已过21:00/等待窗口，历史重建必须标注不可当下执行；当前决策版则将海外和可得国内行情更新至实际截点并重新核验已过条件，无法确认时转待核实并给下一有效窗口，禁止冻结19:30数据却把已经过去的21:00或15/30分钟窗口当未来建议。

十、未来24h/7d事件日历，北京时间：EIA/OPEC+/IEA/CFTC/USDA/WASDE/天气/中国宏观政策/交易所参数与到期/地缘/矿山油田炼厂化工农业事件，并注明Delta/Vega/延迟入场/有限凸性处理。

十一、最后严格四行：
A. 今晚可以立即建立的仓位；
B. 今晚只应挂条件单的仓位；
C. 今晚应继续观察的机会；
D. 今晚必须避免或退出的交易。
无立即交易时A必须写“A. 今晚没有应立即建立的新仓位。”

---

# P. 风险预算

单一试仓最大损失NAV 0.25%—0.75%；确认交易0.75%—1.50%；单一高确信主题总风险≤2.5%—3.0%。同因子交易合并计算。

压力测试：1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变、中国休市时海外大波动。

---

# Q. 写作要求

中文，直接、专业。先回答今晚有没有值得冒险机会。明确区分事实/市场定价/推断/主观判断。每个建议必须有入场、失效、退出。关键事实附来源。

不得把代理当官方、仓单当社会库存、会员排名当机构方向、非surface IV当ATM、连续主力当可交易合约、不可比价差当套利、单日涨跌自动解释供需，也不得因风险偏好高强推交易。

不得把今天早前已完成的Night Session描述成今晚21:00已经发生的行情，也不得把海外15:00后变化描述成中国期货已经交易了该信息。

---

# R. 自动归档

报告完成后通过已连接GitHub connector直接归档到：
`github.com/farfromexact/Global-Cross-Asset-Radar`
edition=`commodities_evening`
直接写main，不创建staging branch/PR，不merge。

固定6路径：
1. `reports/YYYY/MM/YYYY-MM-DD_commodities_evening.md`
2. `reports/YYYY/MM/YYYY-MM-DD_commodities_evening.json`
3. `latest/commodities_evening.md`
4. `latest/commodities_evening.json`
5. `status/commodities_evening_latest.json`
6. `manifests/reports.json`

归档前读取`config/archive-policy.json`、`docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md`、实际JSON schema，不得破坏schema。

JSON至少记录现有schema要求字段，并在允许时加入：
- `data_protocol_version = "china_commodities_v2"`
- `report_input_requested_date`
- `report_input_generated_at`
- `module_freshness`
- `prior_night_session_trading_date`
- `prior_night_session_generated_at`
- `prior_night_session_data_fresh`
- `overnight_day_decomposition_used`
- `physical_coverage`
- `external_coverage`
- `options_surface_ready`
- `options_positioning_ready`
- `options_execution_ready`
- `contract_metadata_quality`

若schema不允许扩展，保留在Markdown，不得破坏schema。

写入后从main回读验证6路径：历史MD/JSON存在；latest日期和edition正确；status对应本次；manifest本次`report_date+commodities_evening`恰好一个记录。全部成功才`archive_status=success`；部分成功=partial；失败=failed并说明路径/原因。

CI只作push后独立校验，不等待；无法取得结果时`ci_validation_status=pending_or_unverified`，不得虚构passed。聊天报告不因归档失败取消。完成main复核后立即结束，不轮询CI、不branch cleanup。
