# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-30

> **今天的商品市场究竟有没有值得冒险的机会？**

**截至本报告时点，无可立即执行的合格新交易。** 节前最后日盘只保留AG/AO/NR三组有限损失条件价差；必须等PMI后确认、取得实时双边报价，并在14:30前退出。

- prompt_version：`radar_2026-09-06_coverage_v1`
- 生成/信息截点：2026-09-30 07:08 BJT；最近完整中国EOD：2026-09-29；下一日盘：2026-09-30 09:00。
- 9月30日晚无夜盘，10月1—7日休市，10月8日08:55集合竞价、09:00恢复日盘，21:00恢复夜盘（[上期所通知，2026-09-21](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)）。

## 一、今日一句话结论

节前去风险与海外原油供给恢复压制风险偏好，但Night exact-contract和期权成交报价均缺，今天只做触发后有限损失、绝不跨假期。

## 二、数据质量与覆盖

| 模块 | 截止/状态 | 本期新增或沿用 | 结论用途 |
|---|---|---|---|
| Futures | 2026-09-29；五所、806合约、77品种；`full_market_ready=true`；source-date match 100%；critical errors 0 | 本期新增 | 可做EOD价格、量仓、同合约1/3/5/20D与curve分析；4条OHLC placeholder已排除 |
| Market State | 2026-09-29；20D exact-contract历史 | 本期新增 | 可用RV20、z-score、near-next curve；不得跨主力拼接 |
| Physical | 18/20按原生频率有效；5项carried-forward；SC/LU缺 | 主要沿用周/旬/月数据 | 全部basis为C级，仅context；仓单不等于社会库存 |
| External(repo) | 17/22 fresh，`context_only` | 沿用日频 | 不能称可执行套利；07:00另补海外公开市场 |
| Night Session | 应得T=2026-09-30；实际状态仍为trading_date=2026-09-29、night_session_date=09-28、generated=09-29 08:06 | 刷新失败 | `data_fresh/validation/published/coverage_complete=false`；0合约、0品种、806 query errors、806 unresolved；所有Night OHLC、两种收益锚、ΔOI、Night curve均为**missing**，不是零变化 |
| Options | 2026-09-29；13,324 records、184 series | 最新有效T-1 | surface-ready 180、positioning-ready 46、execution-ready 0；IV coverage 98.92%、OI 68.97%、bid/ask 0 |
| Metadata | effective match 73.45%；动态字段约30.15% | 部分 | AG/AO可由交易所核实；NR节前动态参数未确认 |

读取路径：[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Radar摘要](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。report_input requested_date=2026-09-29，generated_at=2026-09-29 19:09:31 BJT。

Options失败/跳过25个产品：CJ/MA/PF/PL/PR/ZC日期不匹配，DCE:A失败；B/BZ/C/CS/EB/EG/I/JD/JM/L/LG/LH/M/P/PG/PP/V/Y因权限拒绝被跳过。此缺口只限制对应期权结论，不取消相关期货方向研究。

## 三、商品仪表盘（展示11项；实际扫描77品种）

|板块|品种/合约|EOD close/settle|1D/5D|Vol/OI/ΔOI|EOD curve|Basis/Physical|Night close；vs close/settle；ΔOI|07:00海外|Options|信号|
|---|---|---:|---:|---:|---|---|---|---|---|---|
|有色贵金属|AG/AG2612|14848/14906|-1.792% / -8.248%|299463/277181/14920|-0.2216% contango扩大|missing; missing|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|COMEX银结算代理+1.40%，与国内EOD下跌冲突|surface_ready; positioning_not_ready; execution_not_ready|等09:45；失败反弹才看空|
|有色贵金属|AO/AO2701|2656/2658|-1.592% / -2.387%|218053/266990/34128|-0.6068% contango|C_context_only; fresh_context_only|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|无精确氧化铝映射|surface_ready; positioning_ready; execution_not_ready|等10:00及2639破位|
|能源化工|NR/NR2612|16410/16420|-3.07% / 2.947%|56274/75544/1475|-0.5749% contango|missing; context_only|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|橡胶代理-1.48%，同向但非可执行映射|surface_ready; positioning_not_ready; execution_not_ready|不追低；等16210确认|
|能源化工|SC/SC2611|711.9/716.9|-2.343% / -1.902%|195579/29669/-2741|1.939% backwardation，反对追空|missing; unavailable|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|WTI -3.50%；Brent -2.43%，同向|surface_ready; positioning_not_ready; execution_not_ready; IV74.695%|等45分钟；不追低|
|能源化工|FU/FU2611|4438/4418|0.638% / 4.543%|641064/150615/-19038|22.974% 强backwardation|C_context_only; fresh_context_only|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|原油大跌，反向|surface_ready; positioning_not_ready; execution_not_ready|多空冲突；不交易|
|能源化工|EB/EB2611|9917/9750|1.594% / 2.61%|1133222/353335/8529|5.231% backwardation|C_context_only; fresh_context_only|missing; missing/missing; missing (DCE_security_denial)|原油大跌，反向竞争解释|DCE skipped; no chain|仅观察回撤接受|
|能源化工|BZ/BZ2611|8763/8616|1.82% / 3.458%|98152/24727/-76|7.66% backwardation|missing; not_covered|missing; missing/missing; missing (DCE_security_denial)|原油大跌，反向|DCE skipped; no chain|强势但证据不足|
|航运软商品|EC/EC2611|2845/2871.5|-1.17% / 10.4%|20962/24626/-840|-26.676% contango/roll flag|missing; missing|not_applicable; not_applicable/not_applicable; not_applicable (no_night_session)|精确运价更新缺失|no execution-ready series|不追涨；roll异常观察|
|黑色建材|I/I2701|699/701.5|-0.426% / -1.957%|202899/581075/8456|-0.425% contango扩大/z=-1.80|C_context_only; fresh_context_only|missing; missing/missing; missing (DCE_security_denial)|铁矿代理-0.20%|DCE skipped; no chain|弱但不交易|
|农产品畜牧|LH/LH2611|10560/10495|0.913% / -4.374%|198447/153919/-35702|-7.37% contango|missing; not_covered|not_applicable; not_applicable/not_applicable; not_applicable (no_night_session)|无精确映射|DCE skipped; no chain|反弹伴减仓；不追|
|农产品软商品|CF/CF701|15780/15840|-1.216% / 0.063%|419259/557108/13979|-1.515% contango|C_context_only; fresh_context_only|missing; missing/missing; missing (stale_invalid_no_current_exact_contract)|ICE棉花代理-4.83%，同向|surface_ready; execution_not_ready|跌幅可能含海外映射；等30分钟|

注：Night缺失项不参与强弱、弹性或追价判断；`return_vs_settlement`不能替代`return_vs_close`。海外为9月29日最新收盘/结算或公开代理，不冒充中国期货已交易该信息。

## 四、相比上一期真正变化

1. **T-1 EOD：**AG2612 5日跌幅扩大至-8.25%，同时OI增加14,920；只说明价格/OI象限，不等于确定新空。
2. **T-1 EOD：**AO2701跌1.59%、OI增加34,128，且近月contango；下行研究仍成立，但实体和海外精确映射缺失。
3. **T-1 EOD：**NR2612跌3.07%，海外橡胶代理约-1.48%同向；RU轻backwardation与NR contango构成链内反证。
4. **海外新增：**WTI约89.38（-3.5%）、Brent约102.76（-2.4%），供应恢复是竞争解释；国内SC已先跌而FU/EB/BZ仍强，内外盘分裂（[WSJ，2026-09-29](https://www.wsj.com/business/energy-oil/oil-prices-rise-as-u-s-iran-talks-remain-uncertain-1a33ff00)）。
5. **Night：**本期没有可验证新增信息。T=9/30 exact-contract Night缺失，不能把旧trading_date=9/29快照写成昨夜行情。
6. **期权：**surface研究可用但execution-ready仍为0；节前长假令任何未核价结构都只能是等待报价的研究卡。

## 五、产业链地图

|产业链|方向|最强/最弱|EOD→Night|Curve|实体/仓单|期权|海外|最大缺失|置信度|
|---|---|---|---|---|---|---|---|---|---|
|贵金属|弱/分歧|无/AG|AG 5D -8.25%；当前交易日exact-contract缺失|AG轻度contango扩大|实体层缺失|AG IV高于RV约4.5点、put skew偏贵|美元+0.2%、美债10Y>5%偏空；COMEX金银当日回升构成反证|Night exact-contract、可执行报价或实体更新|中|
|能源—炼化—芳烃|原油弱、燃料/芳烃相对强|FU/BZ/EB/SC|SC -2.34%，EB +1.59%；缺失|SC/FU/EB/BZ均backwardation|多为context_only；SC/LU缺|SC IV极高，不适合追买波动|WTI -3.50%、Brent -2.43%|Night exact-contract、可执行报价或实体更新|中|
|黑色建材|偏弱|无明显/I曲线异常|I -0.43%；DCE采集权限失败|I contango扩大，z=-1.80|最新有效周度/仓单仅context|DCE链缺|铁矿代理-0.20%|Night exact-contract、可执行报价或实体更新|低—中|
|橡胶—轮胎|偏弱|RU相对抗跌/NR|NR -3.07%，RU -2.13%；缺失|NR contango、RU轻backwardation，内部冲突|context_only|NR IV略低于RV、但无报价|橡胶代理-1.48%|Night exact-contract、可执行报价或实体更新|中低|
|农产品—软商品|分化|LH反弹/CF|CF -1.22%；LH +0.91%但OI大减；多数无夜盘或缺失|LH/CF contango|覆盖不完整|DCE链大面积缺|棉花-4.83%、大豆+0.67%|Night exact-contract、可执行报价或实体更新|低|

**最强链：**燃料/芳烃相对强，但受海外原油大跌反证；**最弱链：**贵金属与NR。当前regime是节前去风险、海外原油供应恢复、国内curve分化。EOD只有AG/AO/部分炼化获curve局部确认；实体确认普遍不足。

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

|#|idea_id|方向/持有期|逻辑/赔率/催化/价曲波/拥挤|总分|支持层；反证/缺失|研究判断；证据；执行|
|---:|---|---|---|---:|---|---|
|1|COM-E-AG2612-DOWNSIDE-20260928|short；0-1D（不跨国庆）|21/14/14/11/9|69|支持1,2,4；反证5；缺失3|存在待验证优势；部分；等待09:45后触发与实时组合报价|
|2|COM-E-AO2701-DOWNSIDE-20260929|short；0-1D（不跨国庆）|19/14/12/10/11|66|支持1,2；反证无；缺失3,4|存在待验证优势；部分；等待10:00触发与实时组合报价|
|3|COM-E-NR2612-DOWNSIDE-20260929|short；0-1D（不跨国庆）|19/13/12/9/11|64|支持1,4；反证2；缺失3|存在待验证优势；部分；等待10:00触发与实时组合报价|
|4|COM-E-EB2611-BACKWARDATION-20260929|long；0-1D（不跨国庆）|18/13/12/10/8|61|支持1,2；反证4；缺失3,5|存在待验证优势；部分；等待10:00后内外盘确认；无合格DCE期权链|
|5|COM-M-SC2611-DOWNSIDE-20260929|short；0-1D（不跨国庆）|18/10/13/10/9|60|支持1,4；反证2,5；缺失3|存在待验证优势；部分；等待45分钟；不追低|

没有70+候选；这表示尚未达到研究门槛，不等于全市场没有异常。最高分AG仅69，因为期权报价缺失、Night缺失和长假退出约束共同压低赔率。

## 七、前三名交易研究卡（均未满足当前执行条件）

### 1. COM-E-AG2612-DOWNSIDE-20260928｜买AG2612P14900、卖AG2612P14000，各1手，到期2026-11-24

- **市场隐含/分歧：**EOD已反映5日-8.25%的去杠杆，近月曲线轻度contango；期权ATM IV 38.625%、25D RR +2.86点，未观察到实时净成本；我们的分歧是若双PMI未带来持续反弹且14920/14745失守，强美元与高实际利率仍可能压制银价；但不认为值得裸空或追价
- **事实：**9/29 close 14848 / settle 14906 / high 15072 / low 14745；volume 299,463；OI 277,181；ΔOI +14,920；1D settle -1.79%；5D -8.25%；RV20 34.17%；ATM IV 38.625%；surface ready；positioning/execution not ready
- **五层证据：**支持1,2,4；反证/缺口：海外现货代理与COMEX结算方向出现差异；无实体层；Night exact-contract缺失
- **入场/分批：**09:45后：反弹14920—15080失败并再次跌破14745；同时组合盘口双边可见；首次只用一半风险预算，触发后回测确认再补足。
- **成本情景：**结构满宽900点×15=13,500元/组。好成交：净支出≤3,780元（≤28%满宽）；中：3,780—4,725元；坏：>5,670元或价差缺腿，放弃。均为风险预算反推上限，不是当前报价
- **止损/逻辑失效：**标的30分钟接受15220上方，或组合价值跌至净支出的50%时退出；两者先到；美元/实际利率回落且AG站稳15220、曲线转强并出现实体确认
- **退出：**TP1 14550减半；TP2 14150退出余仓；14:30时间止损，不跨国庆长假
- **最大损失：**已支付净权利金；结构限定。不得以未报价期权替代裸期货的有限损失说明
- **1—20D催化：**09:30官方PMI、随后私营PMI；22:30 EIA通过通胀/美元间接影响；美国数据和中东消息
- **最坏情景：**PMI超预期、美元回落、银价gap上行；最大结构损失仍为净支出
- **合约参数/压力：**期货乘数15千克/手；tick 1元/千克；tick value 15元；一般保证金22%；涨跌停20%；9/30晚无夜盘；LTD 2026-12-15；临近交割前移仓。线性1/2个停板压力约44,718/89,436元/手（按14906，未计复利）
- **放弃条件：**09:45前首跳；实时bid/ask缺失；净支出>满宽42%；价差任一腿流动性不足

### 2. COM-E-AO2701-DOWNSIDE-20260929｜买AO2701P2650、卖AO2701P2500，各1手，到期2026-12-25

- **市场隐含/分歧：**EOD价跌仓增、近月轻度contango；ATM IV 16.62%、25D RR +3.89点，positioning ready但execution not ready；我们的分歧是若PMI未能令AO重回2680，2639下破可能继续释放节前风险；但实体与海外精确映射不足
- **事实：**9/29 close 2656 / settle 2658 / high 2696 / low 2639；volume 218,053；OI 266,990；ΔOI +34,128；1D -1.59%；5D -2.39%；RV20 14.34%；ATM IV 16.62%；OI coverage 92%；bid/ask coverage 0
- **五层证据：**支持1,2；反证/缺口：缺实体供需与精确海外铝土矿/氧化铝映射；期权RR不确定义方向
- **入场/分批：**10:00后：无法收复2680，跌破2639且15分钟不能收回；组合盘口双边可见；首次只用一半风险预算，触发后回测确认再补足。
- **成本情景：**满宽150点×20=3,000元/组。好成交：净支出≤750元；中：750—1,050元；坏：>1,200元放弃。为风险预算反推，不是当前报价
- **止损/逻辑失效：**标的30分钟接受2720上方或价差价值跌至净支出50%；站稳2720并伴随curve改善/实体数据转强
- **退出：**TP1 2580减半；TP2 2500退出；14:30全部平仓，不跨假期
- **最大损失：**已支付净权利金；结构限定
- **1—20D催化：**中国双PMI、节前资金/保证金调整、铝链政策消息
- **最坏情景：**PMI与政策刺激令有色共振上行；最大损失净支出
- **合约参数/压力：**乘数20吨/手；tick 1元/吨；tick value 20元；节前一般保证金11%；涨跌停9%；9/30晚无夜盘；LTD 2027-01-15；交割单位300吨，交割风险需提前移仓。线性1/2停板压力约4,784/9,569元/手
- **放弃条件：**无实时组合盘口；净支出>满宽40%；2639下破后立即V形收回2680

### 3. COM-E-NR2612-DOWNSIDE-20260929｜买NR2612P16400、卖NR2612P15500，各1手，到期2026-11-24

- **市场隐含/分歧：**EOD -3.07%、价格下跌伴OI增加；海外橡胶代理-1.48%；ATM IV 21.92%，但curve未确认；我们的分歧是若16210破位且内外同向，短线下行仍可能延续；但EOD已大跌，不能追低
- **事实：**9/29 close 16410 / settle 16420 / high 16720 / low 16210；volume 56,274；OI 75,544；ΔOI +1,475；1D -3.07%；5D +2.95%；RV20 24.98%；ATM IV 21.92%；surface ready；positioning/execution not ready
- **五层证据：**支持1,4；反证/缺口：curve轻度contango但无异常确认；缺实体层和Night exact-contract
- **入场/分批：**10:00后：跌破16210，反抽16380失败；组合盘口双边可见；首次只用一半风险预算，触发后回测确认再补足。
- **成本情景：**满宽900点×10=9,000元/组。好成交≤2,520元；中2,520—3,150元；坏>3,600元放弃。为风险预算反推，不是当前报价
- **止损/逻辑失效：**标的30分钟接受16680上方或价差价值跌至净支出50%；海外橡胶转强且NR站稳16680、曲线同步改善
- **退出：**TP1 15850减半；TP2 15500退出；14:30全部平仓
- **最大损失：**已支付净权利金；结构限定
- **1—20D催化：**中国PMI、日内橡胶/轮胎链现货反馈、美元和油价
- **最坏情景：**PMI强、油价反弹、胶价gap上行；最大损失净支出
- **合约参数/压力：**期货乘数10吨/手；tick 5元/吨；tick value 50元；LTD 2026-12-15；9/30晚无夜盘。节前合同保证金/涨跌停参数未能从可访问INE页面独立确认；线性压力损失因此不报精确数
- **放弃条件：**无法核验节前参数；无实时bid/ask；16210破位后迅速收复16450

所有三张卡均为研究候选，不代表真实仓位；没有成交反馈时不假设已持有。Greeks因execution-ready=false且无实时组合报价不计算。

## 八、商品期权专项

- 样本：2026-09-29最新有效T-1截面；184 series中180 surface-ready、46 positioning-ready、0 execution-ready。
- AG2612：ATM IV 38.625% vs RV20 34.17%，RR25 +2.86、BF25 +1.775；下行保护不显便宜，适合价差而非裸买put。
- AO2701：ATM IV 16.62% vs RV20 14.34%，RR25 +3.89、BF25 +1.005；可研究但实时价差成本未知。
- NR2612：ATM IV 21.92% vs RV20 24.98%，波动表面相对不贵，但这**单独**不能证明看跌期权便宜或方向正确。
- SC2611：ATM IV 74.695% vs RV20 59.19%；高事件溢价与backwardation使追买下行波动的赔率较差。
- 回避：DCE缺链产品、任何bid/ask coverage=0结构、卖裸期权、基于OI推导做市商净Gamma。

## 九、09:00开盘风险地图

严格三层：①Previous China EOD=2026-09-29；②Current Trading Day Night Session=应得但缺失；③07:00 Overseas=公开市场最新收盘/结算代理。

|品种|EOD层|Night层|海外层|预期开盘|追价？|等待|开盘确认|
|---|---|---|---|---|---|---|---|
|AG|弱、OI增、contango|缺失|金银回升但美元/实际利率偏空|平至低开，置信低|否|45分钟|14920/14745、curve、组合bid/ask|
|AO|价跌仓增、contango|缺失|无精确映射|平至低开|否|60分钟|2680/2639、成交/OI、现货反馈|
|NR|大跌、NR contango|缺失|橡胶代理-1.48%|低开风险|否|60分钟|16210/16380、RU/NR结构|
|SC|已跌、backwardation|缺失|WTI/Brent大跌|低开但可能过度|绝不追低|45分钟|700.4、backwardation、国内资金弹性|
|EB/FU/BZ|国内相对强、backwardation|缺失|原油大跌|低开或相对补跌|否|45分钟|近月强度、curve是否收窄|
|I/黑色|弱、I contango异常|DCE Night缺|铁矿代理微跌|平至低开|否|30分钟|PMI、基差/curve、OI|
|CF|国内弱|缺失|棉花代理-4.83%|低开风险|否|30分钟|15700、OI和现货反馈|

海外与中国Night的信息弹性无法计算；开盘首跳更可能包含累计海外与节前减仓，任何条件单都不得在09:45前生效。

## 十、未来24h/7d事件日历（北京时间）

|时间|事件|处理|
|---|---|---|
|2026-09-30T09:30:00+08:00|中国官方9月PMI及随后私营PMI窗口|先等15—45分钟；有色/黑色/化工Delta延后|
|2026-09-30T14:30:00+08:00|节前风险退出窗口|本报告条件仓全部退出，不跨国庆|
|2026-09-30T22:30:00+08:00|EIA周度石油报告常规窗口|中国无夜盘；境内能源不得带裸Delta等待|
|2026-10-01T00:00:00+08:00|USDA Grain Stocks / Small Grains|中国休市；境外谷物仅用有限损失结构且独立核价|
|2026-10-03T03:30:00+08:00|CFTC COT常规窗口|滞后持仓仅作背景，不当催化|
|2026-10-08T08:55:00+08:00|中国期货期权节后集合竞价|先做gap压力测试，开盘后等45分钟|
|2026-10-08T21:00:00+08:00|下一实际夜盘恢复|重新核验exact-contract Night与海外累计变化|

来源：[中国PMI预期，Reuters，2026-09-29](https://www.reuters.com/business/china-factories-seen-rebounding-september-beijing-signals-more-aid-2026-09-29/)、[EIA发布日历](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[USDA Grain Stocks](https://esmis.nal.usda.gov/publication/grain-stocks)、[CFTC COT日历](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)。

## 十一、旧建议台账

|idea_id|首次提出|上次状态|当前状态|变更原因|历史触发|
|---|---|---|---|---|---|
|COM-E-AG2612-DOWNSIDE-20260928|2026-09-28|等待09:45后触发|等待09:45后触发与实时组合报价|new_data_and_holiday_constraint|unknown_without_intraday_path|
|COM-E-AO2701-DOWNSIDE-20260929|2026-09-29|等待触发|等待10:00触发与实时组合报价|new_data_no_thesis_reversal|unknown_without_fill_feedback|
|COM-E-NR2612-DOWNSIDE-20260929|2026-09-29|等待触发|等待10:00触发与实时组合报价|new_overseas_proxy_support_but_curve_conflict|unknown_without_fill_feedback|
|COM-E-EB2611-BACKWARDATION-20260929|2026-09-29|研究观察|研究观察|overseas_crude_counterevidence|not_applicable|
|COM-M-SC2611-DOWNSIDE-20260929|2026-09-29|等待确认|等待45分钟且不追低|new_overseas_support_but_payoff_worsened|unknown|

若此前已按条件建立任何线性仓，今天14:30前退出；未获得用户成交反馈，不能声明真实持仓、净敞口或已实现期权收益。

## 十二、覆盖核对

|板块|应覆盖|实际取数且已分析|数据不足|未入榜板块最值得跟踪的异常/无异常依据|
|---|---:|---:|---|---|
|黑色建材|9|9|Night与DCE期权；basis仅C级|I2701 contango z=-1.80；其他未见三层独立同向确认|
|有色贵金属|12|12|Night全缺；部分实体缺|AG/AO价跌仓增；AU/铜等无合格新触发|
|能源炼化化工|22|22|SC/LU实体缺；Night全缺；DCE链缺|SC vs FU/EB/BZ内外分裂最值得跟踪|
|新能源|3+GFEX新材料|LC/SI/PS及动态产品已扫描|实体与Night适用性有限|无三层同向异常；LC弱势未获实体确认|
|农产品油脂饲料畜牧|17|17|DCE期权大面积缺；部分无夜盘|LH反弹伴OI大减、CF海外弱；其余无合格异常|
|航运软商品|EC及CF/SR/AP/CJ/PK|全部扫描|EC无Night；精确运价缺|EC 5D强但当日回落且contango/roll flag|
|合计|63个指定代码|63/63（LPG映射PG）；另扫描14个动态产品|Night exact-contract全缺；Physical 2项缺；Options 25产品失败/跳过|方向、跨期、跨品种/跨市场、风格中性、波动率/偏度/事件凸性均完成可得数据初筛|

读取状态：Futures/Market=`ok`；Physical=`partial/carried_forward`；External repo=`ok_context_only`；Night=`stale+parse/query failure`；Options=`partial`；bid/ask=`missing`。未把工具截断或权限拒绝写成源文件为空。

## 来源

- [China Commodities Engine unified report input](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（source_date: 2026-09-29）：五所806合约、77品种；EOD/market/physical/external/options模块状态；具体合约与期权surface指标
- [China Commodities Engine Night Session status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（source_date: 2026-09-29）：Night快照属于旧交易日且validation失败；806 query errors与unresolved contracts
- [SHFE 2026 National Day holiday arrangements](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)（source_date: 2026-09-21）：9月30日晚无夜盘；10月1日至7日休市、10月8日恢复；AG/AO/FU节前涨跌停与保证金参数
- [SHFE 2026 trading holiday calendar](https://www.shfe.com.cn/publicnotice/notice/202512/t20251217_829805.html)（source_date: 2025-12-17）：国庆交易日历
- [Oil prices fall as Gulf supply recovers](https://www.wsj.com/business/energy-oil/oil-prices-rise-as-u-s-iran-talks-remain-uncertain-1a33ff00)（source_date: 2026-09-29）：WTI 89.38 -3.5%；Brent 102.76 -2.4%；供应恢复为主要解释
- [Global commodities snapshot](https://tradingeconomics.com/commodities)（source_date: 2026-09-29）：金银铜、铁矿、橡胶、棉花、大豆方向代理
- [Dollar near two-month peak](https://www.reuters.com/world/africa/dollar-hold-near-two-month-peak-yields-rise-fed-data-looms-2026-09-29/)（source_date: 2026-09-29）：DXY 101.40约+0.2%；美国10年期收益率高于5%
- [China factories seen rebounding in September](https://www.reuters.com/business/china-factories-seen-rebounding-september-beijing-signals-more-aid-2026-09-29/)（source_date: 2026-09-29）：官方PMI预期50.1；RatingDog PMI预期51.6
- [EIA Weekly Petroleum Status Report schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（source_date: 2026-09-30）：常规周三10:30 ET发布窗口
- [USDA Grain Stocks](https://esmis.nal.usda.gov/publication/grain-stocks)（source_date: 2026-09-30）：9月30日12:00 ET报告窗口
- [CFTC COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（source_date: 2026-09-29）：10月2日15:30 ET发布窗口

A. 今天没有应立即建立的新仓位。
B. 09:45后仅在触发且实时双边报价合格时挂AG2612 14900/14000熊市看跌价差；10:00后同理才考虑AO2701 2650/2500或NR2612 16400/15500，均14:30前退出。
C. 今天应继续观察SC供应恢复下的反弹失败、EB/FU/BZ内外盘背离、I曲线异常、CF海外映射；缺失Night与DCE期权链等待节后修复。
D. 今天必须避免或退出09:00首跳追价、任何跨国庆裸期货Delta、C级basis套利、无bid/ask期权、把旧Night快照或OI象限当确定资金方向。