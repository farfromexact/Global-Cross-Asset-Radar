# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-04

生成时点：2026-09-04 07:03 BJT。中国日盘尚未开盘；中国EOD取2026-09-03，当前交易日Night Session取2026-09-04交易日（实际起始2026-09-03晚）。

## 一、今日一句话结论

**有值得冒险的条件型机会，但没有应在9:00直接追价的新仓位：优先观察EB2610、AG2610、FU2611；能源与贵金属的隔夜强势真实，但部分品种已经在夜盘完成大部分定价。**

## 二、数据质量与覆盖

**事实。** China-Commodities-Engine `data/report_input_latest.json` 为schema v2，`requested_date=2026-09-03`，`generated_at=2026-09-04T06:15:59+08:00`。Futures、Market State、Physical、External、Night Session与Options均为各自声明的fresh输入；EOD=T-1、Night `trading_date=T` 的组合符合晨间日期语义。

- 实际读取：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需读取`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/night_session/latest.json`（连接器因文件过大无法展开逐合约全文件）、`data/contract_meta.json`。
- Futures：2026-09-03，802个合约，SHFE/INE/DCE/CZCE/GFEX五所，`full_market_ready=true`，`source_date_match_pct=100%`，`critical_module_errors=0`。但root状态仍为`official_complete=false`：Futures为verified vendor primary；DCE contract-info、仓单、basis、会员排名存在部分/缺失。
- Market State：1D/3D/5D/20D、RV20、成交/持仓z-score、ΔOI、near-next curve可用；本报告不把跨合约拼接当真实收益。
- Physical：18/20 fresh、2 unavailable；多数是原生频率下fresh的现货/产业序列，但basis映射多为C级，缺地区/品质/交割口径，因此只作context，不作为可执行套利或完整Physical证据层。
- External：17/22 fresh，WTI/Brent/LME/COMEX/CBOT/BMD/ICE日频可用；DXY、USDCNH等5项仓库映射不可用。所有repo External均为`context_only`，不作为import-parity套利。
- Night Session：`trading_date=2026-09-04`，`night_session_date=2026-09-03`，`generated_at=2026-09-04T06:01:55+08:00`；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`；610条合约、55个品种，188条合法outside-window，4条no-night-trade，missing timestamp/price/quote、query_error、unresolved均为0，warnings为空。`night_session_coverage_pct=76.06%`不能解释为数据仅完整76%。
- Options：trade_date=2026-09-03，19,354合约、352 series；IV coverage 97.73%，OI coverage 67.86%，bid/ask coverage 0%。全局`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`；`surface_latest.json`当前无法提供可用曲面。故今天不得使用ATM IV、RR25、BF25、Dealer Gamma或具体成交权利金。
- Contract Metadata：整体`quality_state=partial`，有效匹配约73.3%；SHFE/CZCE/DCE部分字段缺失。交易卡中的静态规格仅在交易所公开规则可确认时使用；动态保证金/涨跌停若无法从当日参数表确认则明确标注。

**数据结论：** 价格层与Night Session质量高；curve可用；Physical和Options执行层不足。今天可以做“条件型期货风险”，不应把缺失的Physical/Options硬凑成第四、第五证据层。

## 三、商品仪表盘

> EOD涨跌采用同一具体合约的settlement return；Night headline以`return_vs_close_pct`为主、`vs settlement`为辅。EOD volume/OI为日盘口径；Night volume/OI单独看，不混算证据层。

|板块|品种/合约|EOD close/settle|1D / 5D|EOD vol / OI / ΔOI|EOD curve|Physical|Night close|Night vs Close / vs Settle|Night ΔOI|07:00 Overseas|Options|信号|
|---|---|---:|---:|---:|---|---|---:|---:|---:|---|---|---|
|贵金属|AG2610|16045 / 15960|+1.53% / -4.37%|492,625 / 216,412 / -7,453|+0.11%，轻backwardation|无完整确认|16419|+2.33% / +2.88%|+1,257|现货金+2.3%、银+2.8%，美元/美债收益率回落|T-1；不可执行|**强反弹，但等NFP前确认**|
|能源|FU2611|3813 / 3864|-2.69% / +4.80%|1,028,671 / 214,125 / -12,246|+8.36%，backwardation；仅3个观察|现货映射C级context|3900|+2.28% / +0.93%|+1,581|Brent 97.29(+1.7%)、WTI 93.04(+2.2%)|不可执行|**EOD弱→Night反转**|
|化工|EB2610|9565 / 9563|+1.44% / +11.48%|1,076,406 / 320,070 / +19,134|+2.36%，backwardation|无完整确认|9770|+2.14% / +2.16%|+23,714|油价及柴油裂解偏强|不可执行|**最强price+OI同步**|
|化工|EG2610|5718 / 5811|+1.48% / +14.46%|约2.73m / 376,244 / -3,502|+7.18%，backwardation，z≈1.81|无完整确认|5801|+1.45% / -0.17%|-11,941|原油偏强|不可执行|**vs-close强、vs-settle不强：弹性下降**|
|化工|MA610|3158 / 3188|+0.98% / +13.98%|约3.19m / 613,187 / -12,291|+3.73%，backwardation，z≈1.90|甲醇现货仅C级context|3204|+1.46% / +0.50%|+24,556|油价正向但非一一映射|不可执行|**夜盘重新增仓，但不追**|
|化工|PP2701|8448 / 8521|-0.65% / +8.41%|839,934 / 604,492 / +10,731|+3.87%，backwardation|无完整确认|8617|+2.00% / +1.13%|+19,089|油价正向|不可执行|**强修复，需日盘确认**|
|化工|TA701|5942 / 6012|-0.46% / +8.76%|1,113,210 / 1,049,177 / +46,361|+3.32%，backwardation，z≈2.62|PTA现货C级context|5996|+0.91% / -0.27%|+310|油价正向|不可执行|**相对close修复，未越settle**|
|化工|SA701|1056 / 1061|-0.56% / +4.43%|1,520,163 / 1,197,191 / +3,842|-4.31%，contango|纯碱现货C级context|1060|+0.38% / -0.09%|+10,967|海外映射弱|不可执行|**夜盘增仓但价格弹性弱**|
|油脂|RM611|2361 / 2355|+0.81% / +0.86%|898,762 / 609,592 / -18,069|+6.07%，backwardation|无高质量basis|2347|-0.59% / -0.34%|+9,020|CBOT仅repo日频背景|不可执行|**EOD上涨被Night否定**|
|能源|SC2610|681.7 / 690.9|+2.01% / +20.43%|约201.6k / 37,059 / -2,368|+6.67%，backwardation；仅3个观察|SC Physical unavailable|678.6|-0.45% / -1.78%|-743|Brent/WTI在中国夜盘后仍偏强|不可执行|**中国夜盘否定EOD；等待外盘传导**|

## 四、相比上一交易日/今晨真正变化

1. **EG/MA的边际弹性明显降温。** 昨晨EG Night相对close约+1.82%、相对settle约+3.30%；今晨虽然相对close仍+1.45%，但相对settle已-0.17%。MA从昨晨约+2.10%/+2.95%降至今晨+1.46%/+0.50%。这不是趋势反转，但说明最容易赚的“新闻→价格”阶段已过去。
2. **AG从“反弹观察”升级成真正的条件型多头候选。** Night +2.33% vs close、+2.88% vs settle，且COMEX/现货贵金属同步大涨；但EOD 5D仍为负、日盘OI仍偏低，今天20:30 NFP会重新定价美元与实际利率。
3. **FU出现最清晰的EOD→Night反转。** EOD settlement -2.69%，夜盘却相对close +2.28%、相对settle +0.93%，再叠加07:00外盘Brent/WTI上涨，说明昨日日盘弱势并未延续。
4. **EB成为能化里最干净的price/OI同向品种。** EOD +1.44%且ΔOI +19,134，Night再+2.14%并ΔOI +23,714；这是归因线索，不称“新多”，但比EG的夜盘减仓强得多。
5. **SC出现最重要的内外盘冲突。** 中国夜盘相对close -0.45%，而之后国际油价仍走强。9:00若SC直接高开，不代表夜盘“错了”，而是海外信息在中国闭市后继续累积；要观察开盘后15–45分钟的信息弹性。

## 五、产业链地图

**能化上游—成品油/芳烃。** 方向偏多。最强是EB/FU，最弱是SC夜盘本身。EOD curve普遍backwardation，但SC/FU曲线样本短；Physical层缺完整库存/仓单确认。海外油价与柴油裂解强，是主要第4层证据。置信度：中高。

**聚酯链EG/TA。** 趋势仍偏多，但新增信息弹性下降。EG Night相对close强、相对settle弱且ΔOI下降；TA也出现类似close/settlement分歧。最大缺失是可验证库存/仓单方向和Night exact near-next curve。置信度：中。

**聚烯烃PP/L/V。** Night普遍强于EOD，PP +2.00%、L +1.75%、V +1.31%相对close，且均伴随正ΔOI线索；但没有高质量Physical与import-parity确认。置信度：中。

**贵金属。** 方向偏多但事件风险极高。AG Night强于AU，海外金银同步，美元偏弱；但NFP在20:30，且AG过去5日仍为负。置信度：中高，适合等日盘确认而非9:00追高。

**农产品油脂。** 偏中性/分化。RM Night否定EOD上涨，P/Y变化小；没有形成三层fresh共振。置信度：低中，今天不值得主动冒险。

## 六、机会排行榜

|排名|机会|分数|方向|持有期|阶段|工具|fresh层|数据惩罚|
|---|---|---:|---|---|---|---|---:|---|
|1|EB2610 回撤确认多|79|多|1–3D|条件试仓|期货|3：价格/OI、curve、海外宏观|DCE metadata partial；无Physical；Options不可执行|
|2|AG2610 15–30min确认多|76|多|Intraday–3D|条件试仓|期货；期权仅研究|3：价格/OI、curve、海外贵金属|NFP事件风险；EOD 5D仍负；Options不可执行|
|3|FU2611 EOD弱势反转多|74|多|Intraday–2D|条件试仓|期货|3：价格/OI、curve、海外油价|curve历史仅3；Physical仅C级context|
|4|BZ2610 顺势多|72|多|1–3D|条件试仓|期货|3：价格/OI、curve、海外油价|DCE contract metadata不完整；无Physical|
|5|MA610 回撤承接|69|多|1–3D|观察|期货|2：价格/OI、curve|海外油价仅间接；Physical C级；Options不可执行|

**评分纪律：** 今天没有80+“确认交易”。EB/AG/FU只能试仓/条件单；任何同因子能化仓位必须合并风险预算。

## 七、前三名交易卡

### 1) EB2610｜条件型多｜79分

**事实：** EOD close/settle=9565/9563；EOD +1.44%，5D +11.48%，EOD ΔOI +19,134；EOD near-next curve +2.36%（backwardation）。Night OHLC 9695/9810/9596/9770；vs close +2.14%，vs settle +2.16%，Night ΔOI +23,714，source 2026-09-03 23:00 BJT，quality=fresh。

**市场定价：** EOD与Night均未出现close/settlement锚冲突；夜盘新增强势真实。**推断：** 原油/柴油链强势对苯乙烯成本端形成外部支持，但缺少苯乙烯库存/现货高质量确认，因此不能打80+。**主观判断：** 最适合“回撤不破+VWAP重夺”而不是9:00追高。

- 最佳表达：EB2610期货多；不使用当前期权链做精确执行。
- 入场：9:00后等15–30分钟；9660–9740回撤稳定，随后重新站上VWAP/9780附近才试仓。若直接高开>9820不追。
- 分批：1/3确认VWAP，1/3突破早盘高点，1/3仅在curve不恶化且油价不回吐时。
- 初始止损：30分钟接受价跌破9580；逻辑失效：<9480且curve明显压缩、国际油价同步回落。
- TP1 9950；TP2 10150；时间止损2个交易日。
- 最大损失：0.35%–0.60% NAV试仓；能化同因子总初始风险≤1.25% NAV。
- 1–20D催化：Hormuz航运/美伊冲突、OPEC+ 9月6日会议、成品油裂解与炼厂扰动。
- 最坏情景：地缘快速降温+原油回吐+化工高位拥挤去杠杆。
- gap/涨停：高开>2%且前15min不能继续放量，不追；若接近涨停只允许减仓，不新开。
- Contract Meta：DCE本轮contract-info模块异常，**multiplier/tick/margin/price limit当日参数未能由repo确认**；公开资料显示EB静态交易单位通常为5吨/手，执行前必须以DCE/券商当日参数复核。交割风险：2610进入9月后已接近交割月前窗口，短线仓必须主动roll/退出，不参与交割。
- Night curve：因`data/night_session/latest.json`过大，GitHub connector无法展开EB2609的exact夜盘记录，本次不能可靠计算Night near-next snapshot；不跨合约拼接，故记为“未确认”，不加分。

### 2) AG2610｜15–30min确认多｜76分

**事实：** EOD close/settle=16045/15960；1D +1.53%，5D -4.37%，EOD ΔOI -7,453；EOD curve +0.11%。Night OHLC 16304/16472/16150/16419；vs close +2.33%，vs settle +2.88%，Night ΔOI +1,257，source 02:30 BJT，fresh。海外现货金约+2.3%至4488.54美元/盎司、银约+2.8%，美债收益率和美元回落。

**市场定价：** Night明显强化EOD，且vs close与vs settlement同向，没有锚误读。**推断：** 国内银的夜盘强势获得海外贵金属确认，但EOD 5D仍负、日盘OI下降，说明尚不是干净中期趋势。**主观判断：** 适合事件前小风险试多，不适合重仓跨20:30 NFP。

- 最佳表达：AG2610期货小仓多；若要有限损失，等实时bid/ask后再人工选择call spread，本报告不报价。
- 入场：16320–16420回踩守住，15–30min重新站上16450；若9:00直接>16500不追。
- 止损：30min接受价<16140；逻辑失效：<15950且COMEX银/金同步回吐。
- TP1 16680；TP2 17100；时间止损：NFP前若没有继续扩张则减仓/清仓。
- 最大损失：0.25%–0.50% NAV；不建议把NFP当纯方向赌博。
- 静态规格：SHFE白银15kg/手，最小变动1元/kg，tick value=15元/手；Night当前交易记录到02:30。按Night close 16419估算名义本金约246,285元/手。交易所2025-10-17通知曾将一般保证金调至16%、涨跌停14%，**2026-09-04开盘前仍需核对最新当日参数**。Repo contract metadata显示AG2610为2026-10合约；最后交易日/交割参数执行前复核。
- 1/2涨跌停压力：若按14%静态限幅，仅价格冲击约34,480元/手；连续两日极端情况下不可线性假设可成交，实际损失还受保证金上调和流动性影响。
- Night curve：AG2609/2610 exact night pair未能从过大的night file安全展开；不伪造Night curve。

### 3) FU2611｜EOD弱势反转多｜74分

**事实：** EOD close/settle=3813/3864；1D -2.69%，5D +4.80%，EOD ΔOI -12,246；EOD curve +8.36%，但历史仅3个观察。Night OHLC 3866/3907/3840/3900；vs close +2.28%，vs settle +0.93%，Night ΔOI +1,581，source 23:00 BJT，fresh。海外Brent 97.29(+1.7%)、WTI 93.04(+2.2%)。

**市场定价：** Night对EOD弱势形成反转，且国际油价继续确认。**推断：** 这是“日盘去风险→夜盘重新定价”的典型候选，但EOD curve统计样本过短，不能过度解读。**主观判断：** 只在高开后不回吐时试多。

- 最佳表达：FU2611期货多；入场3850–3900回撤不破后重夺3905，或早盘30min高点突破；>3940直接高开不追。
- 止损：30min接受价<3820；逻辑失效：<3760且Brent跌回94下方或出现可信地缘降温。
- TP1 3980；TP2 4100；时间止损1–2D。
- 最大损失0.25%–0.50% NAV。
- 静态规格：SHFE燃料油10吨/手，tick 1元/吨，tick value=10元；Night记录至23:00。按3900估算名义本金39,000元/手。SHFE 2026-06-23通知对FU2611及相关合约规定涨跌停14%、一般保证金16%；执行时仍以当日交易所/券商参数为准。
- 1/2涨跌停压力：按14%粗算一日价格冲击约5,460元/手；连续两日需计入不可成交、保证金上调和相关性破裂。
- 交割/roll：FU为实物交割，2611不应让短线投机仓进入交割风险窗口；自然人/一般账户按SHFE规则提前降仓或退出。
- Night curve：FU2610/2611 exact pair未能安全展开，当前EOD curve虽强但不把它冒充Night curve确认。

## 八、商品期权专项

**事实：** 2026-09-03链有19,354合约、352 series；IV coverage 97.73%，但`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`，bid/ask coverage=0%，OI coverage=67.86%，Dealer Gamma方向未知。

因此今天：
- 可以研究AG/EB/FU的有限损失call spread思路，但**不能给具体strike、净权利金、bid/ask、滑点或Greeks数值**。
- 不能把vendor IV直接称为可交易ATM IV，也不能输出RR25/BF25/term结构。
- 对NFP这种event convexity，AG最有理论价值；但若没有实时可成交报价，期货小风险条件单反而更透明。
- 回避：裸买极高IV、把T-1链当今天fresh证据、用残缺OI推PCR/crowding、推断Dealer Gamma。

固定执行免责声明：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、9:00开盘风险地图

|品种|1. Previous China EOD|2. Current Trading Day Night Session|3. 07:00 Overseas|预期开盘|是否已定价|是否追价|等待|开盘确认|
|---|---|---|---|---|---|---|---|---|
|EB|EOD强、OI增、backwardation|+2.14%，ΔOI大增|油/柴油偏强|高开|大部分已在夜盘定价|否|15–30m|VWAP、早盘高点、curve是否恶化|
|AG|EOD反弹但5D仍负|+2.33%，继续强化|金+2.3%、银+2.8%|高开|夜盘已定价大部分海外贵金属涨幅|否|15–30m|16450附近接受度、COMEX是否续强|
|FU|EOD明显弱|+2.28%完成反转|Brent/WTI继续涨|高开|部分已定价，外盘还有新增|否|15–30m|3900附近支撑、SC/FU联动|
|SC|EOD强|夜盘-0.45%，否定EOD|外盘油价后续转强|平高/高开|**未完全定价，内外盘冲突最大**|否|30–45m|外盘传导后能否守690/700|
|EG|EOD强、curve强|+1.45% vs close但-0.17% vs settle，ΔOI降|油价偏强|小幅高开|多数已定价|否|30m|是否重新站上settle/VWAP|
|MA|EOD强、curve强|+1.46% vs close、仅+0.50% vs settle|油价间接支持|高开|大部分已定价|否|30m|3200能否形成接受价、curve是否继续压缩|
|RM|EOD小涨|Night -0.59%|外盘农产品无强fresh冲击|低/平开|已定价|不做|15m|若不能迅速收复2355则弱势|

**信息弹性核心：** SC最值得看“External move > China Night move”后的补涨/失败；EG/MA相反，Night已经把大部分新增信息吃掉，追价赔率下降。

## 十、未来24小时 / 7日事件

- **2026-09-04 20:30 BJT｜美国8月就业报告/NFP。** Reuters调查附近预期约+5.6万，失业率约4.1%附近；对美元、实际利率、贵金属和工业金属是最高Delta/Vega事件。AG若日内已有盈利，建议事件前降杠杆；若要跨事件，优先有限损失结构且必须人工确认实时报价。
- **2026-09-05 03:30 BJT｜CFTC COT。** 周五15:30 ET发布；用于观察能源、贵金属、农产品净头寸，但只能作为滞后的crowding背景。
- **2026-09-06｜OPEC+核心成员会议。** Reuters称大概率维持10月产量政策不变；若“维持”已被充分预期，真正尾部是意外增产/减产或对2027基准的强烈信号。
- **2026-09-10/11｜EIA WPSR因美国Labor Day顺延。** EIA官方日程显示数据周截至9月4日的WPSR将在9月10日周四12:00 ET开始发布，即北京时间约9月11日00:00起；对FU/SC/成品油裂解敏感。
- **持续｜Hormuz、美伊/以伊军事与航运。** 当前Brent/WTI风险溢价仍由真实航运与供应担忧驱动，任何可信停火/航道恢复消息都可能造成能化多头gap-down。
- **略超7日｜USDA WASDE 9月11日12:00 ET。** 北京时间9月12日00:00，距离本报告约7天17小时，严格说超出7日窗口，但RM/M/Y/P需要提前纳入下一版计划。

## 风险预算与压力测试

试仓单笔最大损失0.25%–0.75% NAV；今天无80+确认交易，不使用0.75%–1.50%确认档。EB/FU/BZ/PP/MA等能化同因子合并初始风险≤1.25% NAV，任何单一主题总风险≤2.5%。压力测试必须覆盖：1/2个涨跌停、夜盘gap、保证金上调、相关性破裂、流动性消失、地缘瞬间降温、人民币急变、期权IV跳升/塌陷和交割挤压。

## 十一、行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：EB2610回撤确认多；AG2610 15–30分钟确认多；FU2611高开不回吐后的反转多。  
C. 今天应继续观察的机会：BZ2610、MA610、SC2610外盘补涨/失败、PP2701；重点等15/30/45分钟而不是抢9:00第一笔。  
D. 今天必须避免或退出的交易：追高EG/MA/EB；把vs settlement误当夜盘新增涨幅；基于T-1且execution-not-ready期权做精确成交；在NFP前无风险预算地重仓AG。

## 来源

1. China-Commodities-Engine（EOD/Night/Physical/External/Options统一输入）：https://github.com/farfromexact/China-Commodities-Engine
2. Reuters, 2026-09-03, Oil prices hit fresh 6-week highs on renewed Middle East tensions: https://www.reuters.com/business/energy/oil-edges-down-investors-weigh-uncertainty-over-us-iran-strikes-2026-09-03/
3. Reuters, 2026-09-03, Gold jumps 2% as Fed Governor Waller's comments temper rate hike bets: https://www.reuters.com/world/india/gold-rises-dollar-yields-ease-with-us-nonfarm-payrolls-report-spotlight-2026-09-03/
4. Reuters, 2026-09-03, US labor market remains stable; services input price rises point to elevated inflation: https://www.reuters.com/business/world-at-work/us-weekly-jobless-claims-rise-marginally-amid-stable-labor-market-2026-09-03/
5. Reuters, 2026-09-02, OPEC+ likely to keep oil output policy unchanged on Sunday: https://www.reuters.com/business/energy/opec-likely-to-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-02/
6. CFTC 2026 COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
7. EIA Weekly Petroleum Status Report schedule: https://www.eia.gov/petroleum/supply/weekly/schedule.php
8. USDA WASDE release dates: https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report
9. SHFE fuel-oil margin/limit notice, 2026-06-23: https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html
10. SHFE gold/silver margin/limit notice, 2025-10-17: https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html