# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-09｜信息截点：2026-10-09 07:00 BJT｜生成时间：2026-10-09T07:08:00+08:00｜prompt_version：radar_2026-09-06_coverage_v1｜data_protocol_version：china_commodities_v2**

> **今天的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。**

昨夜能源链继续分化：MA出现真正的新增强势，FU、I、AG的标题涨跌大多只是结算锚差，SC则在国际油价收高背景下相对国内EOD close明显回撤。09:00只做回踩/反抽确认，不追首跳。

## 一、今日一句话结论

**最强链是甲醇—化工，最弱仍是黑色；但Night exact-contract缺失、所有期权execution-ready为零，今天仅保留MA/TA回踩多与I/AG反抽空条件研究。**

## 二、数据质量与覆盖

- **实际读取路径**：China-Commodities-Engine main同一快照下读取 `data/report_input_latest.json`、Night/root status、`radar_latest.json`；按需读取 `latest.json`、`market_state_latest.json`、Physical、External、Options quality/surface、`contract_meta.json`。Night大文件通过connector返回0字符但blob SHA存在，判定为**truncated**，不是源文件为空。
- **统一输入**：requested_date=2026-10-08，generated_at=2026-10-08 19:12:09 BJT。Futures/Market/Physical/External/Options均为10月8日；五所SHFE/INE/DCE/CZCE/GFEX齐全，806份合约、77品种，`full_market_ready=true`，source-date match=100%，critical errors=0。
- **核心质量**：unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0；8个零价占位全部排除排行。official_complete=false：contract metadata、仓单仅部分；basis不可用于评分；会员排名缺失；carried-forward warehouse=5。
- **Night模块**：module-specific status仍为trading_date=2026-10-08、night_session_date=2026-10-07、generated_at=07:56:58；data_fresh=false、validation=false、published=false、coverage_complete=false、night contracts=0、query/unresolved=214。它属于复市前无合法夜盘的失败采集，**与10月9日当前交易日的实际夜盘无关**。本期因此使用公开fallback的主力涨跌，不能替代exact-contract OHLC/OI/curve；`night_session_fallback=true`。
- **Physical**：18/20 fresh，2 unavailable；仅按原生频率作context。basis统一Spot-Futures，但现有C级，不计方向层；仓单与社会库存未混用。
- **External**：仓库日频17/22 fresh；07:00补充：Brent 104.28、WTI 91.49；COMEX金约4126.78、银58.98；USD/CNH约6.703、美元指数小跌0.08%，10Y名义约5.23%、实际约2.91%。海外收盘是中国09:00映射证据，不是国内已交易事实。
- **Options**：10月8日15260条、204个series；200 surface-ready、49 positioning-ready、0 execution-ready，bid/ask coverage=0；DCE chain受权限限制。T-1可研究IV/skew，但Night标的变化造成moneyness漂移，不能当今晨报价。
- **下一窗口**：2026-10-09 09:00日盘；MA/TA/I等已完成属于10月9日交易日的夜盘，但精确仓库记录缺失。无夜盘LC/SI/PS等直接等待09:00。

## 三、商品仪表盘（展示13项；底层全量扫描77品种）

| 板块 | 品种/合约 | EOD close/settle | 1D close/5D settle | volume/OI/ΔOI | EOD curve | basis/Physical | Current T Night | 07:00 Overseas | Options | 09:00信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| 能源与化工 | FU/FU2611 | 5,179/4,995 | 18.35% / 21.36% | 639,615 / 144,059 / 17,317 | 8.89% (z —) | C/context; fresh series/context only | 主力代理+2.86% vs昨结算；折算约5138，较EOD close 5179约-0.79%（非exact-contract） | Brent 104.28(+4.1%)、WTI 91.49(+3.6%)；但低于19:11仓库值 | surface 4/4; positioning 0; execution 0 | 不追；等45m |
| 能源与化工 | MA/MA701 | 3,200/3,148 | 9.03% / 9.8% | 633,499 / 690,748 / 30,180 | 12.19% (z 1.51) | C/context; fresh series/context only | 主力代理+7.17% vs昨结算；折算约3374，较EOD close 3200约+5.44%（非exact-contract） | 油价强；无exact甲醇外盘 | surface 6/6; positioning 4; execution 0 | 最强续涨；等45m回踩 |
| 能源与化工 | TA/TA701 | 6,830/6,688 | 8.97% / 8.89% | 1,242,221 / 1,178,151 / 161,162 | 3.75% (z 0.47) | C/context; fresh series/context only | exact-contract缺失；同链MA强、油价强，仅作代理 | 油价强，芳烃成本支持 | surface 6/6; positioning 3; execution 0 | 等30–45m精确夜盘确认 |
| 能源与化工 | SC/SC2611 | 758.5/737.4 | 8.96% / 6.09% | 76,496 / 27,069 / 2,090 | 3.15% (z —) | missing; missing/unavailable | 主力代理732.8、-0.62% vs昨结算；较EOD close 758.5约-3.39% | Brent/WTI收高，但国内夜盘相对close回撤，冲突 | surface 3/3; positioning 0; execution 0 | 内外冲突；不做首跳 |
| 黑色与建材 | I/I2701 | 682.5/690.5 | -3.12% / -3.22% | 301,115 / 605,201 / 53,105 | -0.86% (z -2.32) | C/context; fresh series/context only | 主力代理-1.16% vs昨结算；折算约682.5，较EOD close约0% | SGX 19:11为91.25；07:00精确增量未确认 | DCE chain blocked/not available | 弱势未扩张；反抽失败才空 |
| 有色与贵金属 | AG/AG2612 | 14,412/14,589 | -3.46% / -9.86% | 195,993 / 294,766 / 11,546 | -0.21% (z -1.1) | missing; missing/unavailable | 主力代理-1.21% vs昨结算；折算约14412，较EOD close约0% | COMEX银58.98、-1.9%，同向但国内新增弹性低 | surface 4/4; positioning 0; execution 0 | 新增弹性低；反抽失败才空 |
| 能源与化工 | RU/RU2701 | 20,145/20,065 | 2.21% / 4.94% | 276,307 / 157,348 / 6,870 | 0.26% (z 0.97) | missing; missing/unavailable | exact-contract缺失 | SICOM截至07:00精确更新缺失 | surface 3/3; positioning 2; execution 0 | 等精确夜盘与30m |
| 能源与化工 | BR/BR2612 | 16,415/16,260 | 4.35% / 10.8% | 62,426 / 56,812 / 10,167 | 2.43% (z 2.87) | missing; missing/unavailable | exact-contract缺失 | 无直接海外同质合约 | surface 3/3; positioning 0; execution 0 | 等换月/精确夜盘 |
| 有色与贵金属 | CU/CU2611 | 110,260/110,740 | 0.63% / -0.04% | 73,476 / 193,823 / 8,419 | 0.73% (z 1.6) | C/context; fresh series/context only | 当月连续109800、约-1.57%，与CU2611不可直接等同 | LME铜仓库值14423；沪铜夜盘代理回落 | surface 9/9; positioning 3; execution 0 | 等15m；内外冲突 |
| 黑色与建材 | FG/FG701 | 868/880 | -3.23% / -5.17% | 1,284,048 / 1,375,714 / 174,215 | 4.05% (z 0.44) | C/context; fresh series/context only | 主力代理-0.11% vs昨结算 | 无可执行外盘映射 | surface 6/6; positioning 3; execution 0 | backwardation反证追空 |
| 农产品 | OI/OI701 | 10,250/10,277 | 0.32% / 1.3% | 169,337 / 297,160 / 13,411 | 1.77% (z 0.99) | C/context; fresh series/context only | exact-contract缺失 | CBOT豆油68.7，WASDE前 | surface 4/5; positioning 1; execution 0 | WASDE前降低Delta |
| 软商品 | SR/SR701 | 5,475/5,486 | 2.6% / 2.16% | 548,200 / 548,793 / -15,484 | -3.06% (z -1.62) | C/context; fresh series/context only | exact-contract缺失 | ICE糖20.79 | surface 5/6; positioning 4; execution 0 | 价涨仓减，避免追 |
| 新能源与材料 | LC/LC2701 | 117,300/121,540 | -1.28% / -6.99% | 227,730 / 409,678 / -3,025 | -0.23% (z -1.24) | missing; missing/unavailable | 无夜盘 | 无可靠外盘映射 | surface 11/11; positioning 0; execution 0 | 无夜盘；09:00等45m |

> Night代理涨跌均优先与EOD close二次比较。FU +2.86% vs settlement折算后仍低于EOD close；I -1.16%与AG -1.21%折算后约等于EOD close，不能写成新增趋势扩张。

## 四、相比上一期真正变化

1. **MA替代TA成为第一研究候选**：EOD MA701 close 3200、价涨仓增、curve z=1.51；夜盘主力代理+7.17% vs settlement，折算相对EOD close仍约+5.44%，是少数真正新增强势。
2. **FU headline strength被close锚削弱**：夜盘+2.86% vs settlement折算约5138，反而较EOD close 5179低约0.79%；能源逻辑仍在，但边际弹性下降。
3. **SC出现最强内外冲突**：国内主力代理夜收732.8，相对EOD close 758.5约-3.39%，而Brent/WTI最终仍上涨4.1%/3.6%。这更像复市溢价回吐，不能直接做跨市场套利。
4. **I与AG的夜盘跌幅几乎只是结算锚差**：折算价格均约等于EOD close，新增弱势没有扩张，09:00追空赔率变差。
5. **RU/BR降级**：EOD价/OI/curve仍偏强，但exact-contract Night与07:00 SICOM更新均无法核实；昨晚排名不再自动延续。
6. **旧SC空头与新SC多头都不具备当前优势**：旧空头已在昨日被735失效位推翻；昨晚供应冲击多头又遭国内夜盘回撤反证，转为无方向观察。

## 五、产业链地图

| 产业链 | 判断 | EOD→Night | curve/实体 | 海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 甲醇—烯烃 | 最强、但过热 | MA EOD +9.03%，夜盘代理新增约+5.44% | backwardation，Physical仅context | RR25 +8.21 call偏；无bid/ask | exact-contract Night | 中高 |
| 原油—燃料油 | 高波动、弹性回落 | SC相对close -3.39%；FU相对close约-0.79% | SC/FU curve均受roll污染 | 国际油价收高；FU put-skew | 进口平价、精确夜盘 | 中 |
| PX—PTA—聚酯 | 偏强但等待验证 | TA exact Night缺失，MA不能替代 | TA curve正、ΔOI强 | 油价支持、RR中性 | TA夜盘与现货负荷 | 中 |
| 黑色建材 | 最弱但不追空 | I headline跌幅无新增；FG小跌 | I contango/z=-2.32；FG backwardation反证 | SGX新增缺失；DCE期权缺失 | 港存/铁水高质量更新 | 中 |
| 贵金属 | 银弱金稳、弹性耗竭 | AG夜盘相对close近0 | AG轻contango | COMEX银-1.9%，金+0.4%；AG RR略call | exact AG2612 OHLC/OI | 中 |

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

| 排名 | idea_id | 方向 | 总分（逻辑/凸性/催化/价格曲线波动/拥挤技术） | 支持层 | 证据 | 执行 |
|---:|---|---|---|---:|---|---|
| 1 | COM-M-MA701-MOMENTUM-HOLD-20261009 | long conditional | 75 (21/15/18/14/7) | 3 | 部分 | 等待触发/精确夜盘与报价确认 |
| 2 | COM-E-TA701-ENERGY-GAP-HOLD-20261008 | long conditional | 71 (20/14/16/13/8) | 3 | 部分 | 等待触发/待报价 |
| 3 | COM-M-I2701-WEAK-CURVE-20261009 | short conditional | 68 (20/14/12/13/9) | 2 | 部分 | 等待反抽失败/参数确认 |
| 4 | COM-E-AG2612-FAILED-REBOUND-SHORT-20261008 | short conditional | 67 (19/14/13/12/9) | 3 | 部分 | 等待反抽失败 |
| 5 | COM-M-FU2611-ELASTICITY-FADE-20261009 | long conditional | 66 (19/12/17/10/8) | 2 | 部分 | 等待回踩/参数确认 |

- **MA701**：市场隐含能源—化工缺口持续；我们的分歧是方向未必错，但当前价格把大量利好一次性计入。新增证据是夜盘相对close继续扩张；最强反证是过热与实体缺失。
- **TA701**：市场隐含成本传导；分歧是没有TA exact-night不能确认链内同步。最佳工具仍是回踩后的期货，或当前报价核验后的有限支出价差。
- **I2701**：市场隐含黑色弱需求；分歧是夜盘没有新增下跌弹性，只有反抽失败才值得冒风险。
- 分数仅为排序；风险偏好高不加分。MA/TA虽≥70，仍因报价、触发或精确Night缺口不能立即执行。

## 七、前三名交易研究卡

### 1. MA701｜条件多｜COM-M-MA701-MOMENTUM-HOLD-20261009

- **事实**：EOD close/settle=3,200/3,148；Night=fallback broad-main; exact OHLC/OI missing，主力代理折算约3,374，相对close 5.44%。
- **市场定价/分歧**：节后能源—化工缺口继续扩张；我们的分歧是方向可能正确但当前位置已透支，只有回踩承接才有正赔率。
- **最佳表达与配比**：MA701期货小试仓；若实时报价合格再研究3300/3500看涨价差；期货1手；期权1:1，仅研究未报价。期权execution-ready=false，当前不得下结构单。
- **入场/分批**：09:45后：精确合约回踩3260–3300守住并重新突破首45分钟高点；1/3触发、1/3回测、1/3创日内新高且OI不萎缩。
- **止损/失效/退出**：3230计划止损；跌破3200 EOD close逻辑失效；TP1 3450，TP2 3560；2个交易日未扩张即退出；最迟5D。
- **最大损失与风险预算**：期货不有限；单笔计划风险NAV 0.25%–0.50%；期权价差仅在净支出核验后有限。一/两个涨跌停压力损失：3,840 / 7,680元/手（简单压力）。
- **合约参数**：multiplier 10；tick 1；tick value 10；notional 32,000；margin 14%/4,480；limit 12%；最后交易日 2027-01-14；制度上有；本期exact-contract记录缺失；持仓进入交割月前平仓/换月。
- **好/中/坏成交**：3260–3300成交：至TP1约2–4R；3300–3340：约1.3–2.4R；>3375不做。
- **1–20D催化/最坏情景/放弃**：1–5D能源供应、国内甲醇补价、WASDE/宏观交叉影响；高开后流动性塌陷、保证金上调、连续跌停；开盘>3375且无回踩、exact-night否定、油价转跌且化工链同步转弱。

### 2. TA701｜条件多｜COM-E-TA701-ENERGY-GAP-HOLD-20261008

- **事实**：EOD close/settle=6,830/6,688；Night=repo truncated / fallback unavailable; MA chain is not substitute。
- **市场定价/分歧**：原油成本冲击会沿PX/PTA链传导；我们的分歧是TA的价格/OI与curve支持，但夜盘精确确认缺失，追价风险高。
- **最佳表达与配比**：TA701期货；报价合格后研究6800/7200看涨价差；期货1手；期权1:1仅研究。期权execution-ready=false，当前不得下结构单。
- **入场/分批**：09:30–09:45后回踩6760–6820守住并重站6860；1/2触发、1/2回测。
- **止损/失效/退出**：6680计划止损；6620下方逻辑失效；TP1 7000，TP2 7180；3D无跟随退出，最迟5D。
- **最大损失与风险预算**：期货不有限；NAV 0.25%–0.50%；期权须实时净支出。一/两个涨跌停压力损失：2,049 / 4,098元/手（简单压力）。
- **合约参数**：multiplier 5；tick 2；tick value 10；notional 34,150；margin 7%/2,390.5；limit 6%；最后交易日 2027-01-14；制度上有；本期exact-contract记录缺失；进入交割月前换月。
- **好/中/坏成交**：6760–6820：TP1约1.5–3R；6820–6860：约1.1–2R；>6900不做。
- **1–20D催化/最坏情景/放弃**：原油、PX现货、聚酯负荷与库存更新；成本端回落、需求不跟、夜盘高开低走；09:45仍不能确认exact-night或开盘>6900无回踩。

### 3. I2701｜条件空｜COM-M-I2701-WEAK-CURVE-20261009

- **事实**：EOD close/settle=682.5/690.5；Night=broad-main proxy，主力代理折算约682.5，相对close 0%。
- **市场定价/分歧**：黑色需求走弱但夜盘并未继续扩张；我们的分歧是只在反抽失败时做空，不能把结算锚跌幅误读为新增弱势。
- **最佳表达与配比**：I2701期货条件空；DCE期权数据不可用；期货1手。期权execution-ready=false，当前不得下结构单。
- **入场/分批**：09:30后反抽686–692失败并重新跌破682；1/2跌破、1/2回测不破682。
- **止损/失效/退出**：699计划止损；700上方逻辑失效；TP1 670，TP2 655；2D无扩张退出，最迟5D。
- **最大损失与风险预算**：期货不有限；NAV 0.25%–0.50%；合约参数未确认。一/两个涨跌停压力损失：参数不足。
- **合约参数**：multiplier —；tick —；tick value —；notional —；margin —%/—；limit —%；最后交易日 —；制度上有；exact-contract缺失；参数未确认，不进入交割月。
- **好/中/坏成交**：690–692反抽空：TP1约2R；686–690：约1.3–1.8R；<680追空放弃。
- **1–20D催化/最坏情景/放弃**：钢材成交、铁水、港口库存与SGX铁矿；政策刺激或补库导致快速反包；开盘直接<680不追；反抽站稳699；参数未核实。


### 旧建议台账

| idea_id | 首次提出 | 上次状态 | 当前状态 | 变更原因 |
|---|---|---|---|---|
| COM-E-TA701-ENERGY-GAP-HOLD-20261008 | 10/8晚 | 等触发 | 保留，降至第2 | MA夜盘新增更强；TA exact-night缺失 |
| COM-E-RU2701-RUBBER-TIGHTNESS-20261001 | 10/1 | 等确认 | 研究观察 | exact Night与SICOM新增缺失 |
| COM-E-BR2612-RUBBER-CONFIRMATION-20261008 | 10/8晚 | 等参数 | 研究观察 | 换月、参数和Night均未补齐 |
| COM-E-AG2612-FAILED-REBOUND-SHORT-20261008 | 10/8 | 等反抽失败 | 继续等待，不追空 | Night相对close无新增下跌 |
| COM-E-SC2611-CONDITIONAL-SHORT-20261006 | 10/6 | 已失效 | 退出/关闭 | 10/8 EOD突破735失效位 |
| COM-E-SC2611-SUPPLY-SHOCK-HOLD-20261008 | 10/8晚 | 等确认 | 转无方向观察 | 国内Night相对close回撤，与外盘冲突 |
| COM-E-DIESEL-LOGISTICS-20261005 | 10/5 | 待报价 | 继续待报价 | exact篮子与同步bid/ask仍缺 |

没有用户成交反馈，不假设任何真实持仓；“持有/退出”仅在此前已经按条件建立时适用。

## 八、商品期权专项

- **MA701 2026-12-11**：ATM 3150，ATM IV 43.345%，RR25 +8.21，BF25约-0.02；surface/positioning ready，execution not ready。夜盘大涨使旧ATM与Delta失真，09:00后必须重算。
- **TA701 2026-12-11**：ATM 6700，ATM IV 35.285%，RR25 +0.08，BF25 +0.775；surface/positioning ready，execution not ready。
- **AG2612 2026-11-24**：ATM 14600，ATM IV 36.41%，RR25 +0.55，BF25 +2.285；surface ready、positioning/execution not ready。
- **FU2611 2026-10-19**：ATM 5000，ATM IV 72.715%，RR25 -6.00，put skew明显；不能仅凭IV-RV判断期权便宜。
- 建议结构均只是研究方向：MA/TA call spread、AG put spread。没有当前bid/ask、净支出、滑点和Greeks，不可下单；禁止推断dealer net gamma。

## 九、09:00开盘风险地图

| 品种 | Previous China EOD | Current T Night | 07:00 Overseas | 预期/操作 | 等待 |
|---|---|---|---|---|---|
| MA | close 3200，+9.03% | 代理新增强势 | 油价高位间接支持 | 高开概率高；禁止首跳追，回踩承接才多 | 45m |
| TA | close 6830，+8.97% | exact缺失 | 油价支持 | 可能高开；先确认TA而非借MA代替 | 30–45m |
| FU | close 5179，+18.35% | headline +2.86%但相对close约-0.79% | Brent/WTI收高 | 平/低于EOD close并不意外；不追headline | 45m |
| SC | close 758.5，+8.96% | 代理732.8、相对close -3.39% | 国际油价上涨 | 可能低于昨日close；内外冲突，不做首跳 | 45m |
| I | close 682.5，-3.12% | 代理约682.5 | SGX增量未确认 | 近乎平开；反抽失败才空 | 30m |
| AG | close 14412，-3.46% | 代理约14412 | COMEX银-1.9% | 偏低/平开；国内弹性已衰减 | 30m |
| RU/BR | EOD偏强 | exact缺失 | SICOM更新缺失 | 无法判断gap；待核实 | 30–45m |
| LC/SI/PS | EOD分化 | 制度上无夜盘 | 无可靠映射 | 直接进入日盘，观察首45分钟 | 45m |

Night return vs settlement与vs close的分歧是本期开盘地图核心：只有MA显示显著新增强势；FU/I/AG不能用结算锚制造追价信号。

## 十、未来24小时/7天事件日历（北京时间）

- **10月10日00:00**：USDA WASDE（10月9日12:00 ET）。豆粕、豆油、玉米、棉花、糖等降低裸Delta；若做事件凸性，只能用当前报价核验后的有限损失结构。
- **10月10日03:30后**：CFTC COT计划发布。仅作拥挤验证，不把持仓报告当即时资金方向。
- **10月14日**：IEA Oil Market Report；原油、燃料油与化工链需预留Vega/gap预算。
- **10月16日00:00**：EIA假期调整后的WPSR（10月15日12:00 ET），位于7日窗口边界；SC/FU避免临近事件放大同因子仓位。
- 地缘与飓风：霍尔木兹运输安全、伊朗相关制裁、美国海湾关停随时改变油价；能源同因子总风险合并，不超过NAV 2.5%–3.0%。
- 国内：关注节后保证金/限幅恢复与交易所临时通知；SC2611、FU2611等高限幅合约继续按提高后的压力测试处理。

## 覆盖核对

| 板块 | 应覆盖 | 实际取数且分析 | 数据不足/低流动性 | 未入榜最值得跟踪 |
|---|---:|---:|---|---|
| 黑色建材 | 10 | 10 | WR流动性极低但保留 | I弱curve；FG backwardation反证追空 |
| 有色贵金属 | 13 | 13 | exact Night仅部分代理 | CU夜盘回落、AG弹性耗竭、PD大跌 |
| 能源炼化化工 | 26 | 25 | ZC零价零量，流动性不足 | SC内外冲突、FU弹性回落、PX curve反证 |
| 新能源 | 3+GFEX新材料 | 3及动态PT/PD等已扫 | 无夜盘属于制度不适用 | LC close弱于settle、SI/PS等09:00确认 |
| 农产品油脂饲料畜牧 | 15 | 15 | DCE期权链受限 | OI相对强但WASDE前不追；LH弱 |
| 航运软商品 | EC及CF/CY/SR/AP/CJ/PK | 全部 | JR/PM/RI/WH低流动性 | SR价涨仓减、EC高波动但参数/夜盘不足 |

全市场77品种：72项取得有效EOD并分析；JR/PM/RI/WH/ZC五项因零成交/零持仓或占位价排除排行。策略类别已扫描方向、curve/跨期、高质量basis可用性、跨品种/跨市场RV、波动率/偏度、事件凸性；1D/3D/5D/20D均按同合约历史检查。未取得的数据不缩小应覆盖清单。

## 风险预算与来源

单一试仓最大损失NAV 0.25%–0.75%；本期因Night/执行缺口限定在0.25%–0.50%。确认交易0.75%–1.50%；单一高确信主题合计≤2.5%–3.0%。压力测试包括1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变。

关键来源：

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（2026-10-08；中国五所EOD、Market/Physical/External/Options）
- [Night Session模块状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（2026-10-08；旧失败快照，不代表10月9日夜盘）
- [第一财经：10月8日23:01国内夜盘](https://www.yicai.com/brief/103386786.html)（FU/MA/I等主力代理涨跌）
- [汇通网：10月9日02:31国内原油与贵金属夜盘](https://quote.fx678.com/symbol/AG0001)（主力代理；非exact-contract）
- [Reuters：10月8日国际原油结算](https://www.reuters.com/business/energy/oil-rises-middle-east-supply-concerns-persist-amid-shipping-attacks-2026-10-08/)
- [Reuters：10月8日贵金属与美元](https://www.reuters.com/world/india/gold-edges-higher-after-hitting-two-month-low-2026-10-08/)
- [USDA WASDE日程](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- [CFTC COT日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- [IEA 10月OMR](https://www.iea.org/events/oil-market-report-october-2026)
- [EIA WPSR日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：09:45后MA701回踩3260–3300守住并重破首45分钟高点；TA701回踩6760–6820后重站6860；I2701仅反抽686–692失败再空，均须当前参数/报价确认。
C. 今天应继续观察的机会：AG2612反抽失败、FU2611回踩承接、RU/BR精确夜盘、SC内外盘背离、WASDE前油脂饲料波动率。
D. 今天必须避免或退出的交易：避免追MA/FU能源首跳、在682附近追空I、在14412附近追空AG、任何无bid/ask期权；若此前建立SC2611空头应已按735失效退出。