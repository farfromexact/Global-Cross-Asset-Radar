# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-30

`prompt_version=radar_2026-09-06_coverage_v1`　`data_protocol_version=china_commodities_v2`

生成时间：2026-09-30 19:50 北京时间｜信息截点：19:42｜中国最近可验证完整EOD：2026-09-29｜今日交易日：2026-09-30（但EOD尚未入库）

> **今晚的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。** 9月30日日盘EOD缺失、今晚全市场无夜盘；BR/OI/能源链只保留节后重新报价后的研究机会，不能把晨间条件延长使用。

## 一、今晚一句话结论

截至本报告时点，无可立即执行的合格新交易；9月30日EOD未入库且今晚休市，BR、菜油和能源链仅保留节后重报价观察。

研究判断分三类：已分析但优势不足（AG/AO/EC）；研究机会存在、等待新价格（BR/OI/SC-FU）；数据不足、暂时无法判断（全部品种的9月30日日盘变化、日盘路径及当日EOD曲线）。最接近验证的窗口不是今晚21:00，而是**10月8日08:55集合竞价、09:00日盘**。

## 二、数据质量与覆盖

| 模块 | 实际读取 | 日期/生成时间 | 状态 | 本期用途 |
|---|---|---|---|---|
| 统一输入 | `data/report_input_latest.json` | requested 2026-09-29；generated 2026-09-30 08:20:58 | ok，但非9月30日EOD | 统一质量状态和嵌入式Night摘要 |
| Futures | `data/latest.json`、`data/last_run_status.json` | EOD 2026-09-29；08:07:26 | last-good、verified vendor-primary | 仅作最近完整EOD背景 |
| Market State | `data/market_state_latest.json` | 2026-09-29；77品种 | ok/last-good | 1/3/5/20D、RV20、OI、curve |
| Physical | `data/physical/latest.json` | requested 2026-09-29；09-30 08:20 | 18/20按原生频率fresh；SC/LU unavailable | 仅原生频率背景；basis全为C级，不入方向评分 |
| External repo | `data/external/latest.json` | 2026-09-29 | 17/22 fresh；context_only | 日频背景，不当可执行套利 |
| 早前Night | `report_input.night_session` + `data/night_session/last_run_status.json` | trading_date=2026-09-30；session 09-29晚至09-30凌晨；08:01:30 | data_fresh=true、validation=true、published=true；coverage_complete=false | 属于今天已完成的连续交易阶段；不是今晚未来行情 |
| Night明细 | `data/night_session/latest.json` | 0字节 | empty | 不能下钻；仅使用统一输入内嵌代表合约，禁止跨月替代 |
| Options | `data/options/quality_latest.json`、`data/options/latest.json` | 2026-09-29；13,324条、184 series | 180 surface-ready、46 positioning-ready、0 execution-ready；`surface_latest.json` empty | T-1研究截面；无当前报价执行权 |
| Metadata | `data/contract_meta.json` | 2026-09-29 | partial_error；有效匹配约73.45%，动态参数约30.15% | 缺失参数一律标“未确认” |

核心期货质量闸门：五所（SHFE/INE/DCE/CZCE/GFEX）均覆盖，806合约、77品种，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0；4条OHLC占位记录已排除，5条仓单序列沿用。`official_complete=false`，故事实表述为“经验证的供应商主源EOD”，不是五所官方全量完成。

Night质量闸门：423个有效夜盘合约、37品种；outside-window 165、no-night-trade 4、missing timestamp/price/quote均0；query error与unresolved各214。`coverage_complete=false`的原因是真实未解析合约，不把合法无夜盘或outside-window误报为错误。Top候选BR2611、OI701在内嵌摘要中有exact-contract记录；DCE候选EB没有有效Night记录。

时间纪律：9月30日早前Night归属交易日9月30日，只能解释隔夜价格发现。仓库截至19:42没有9月30日日盘EOD，也没有可核验盘中路径，因此**不能计算早前Night→日盘follow-through/reversal、不能判断今日收盘曲线确认、不能判断晨间条件是否触发**。这是一项数据不足，不是“9月30日市场无异常”。

根据[上期所国庆/中秋安排（2026-09-21）](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)，9月30日晚无夜盘，10月1日至7日休市，10月8日08:55集合竞价，10月8日晚恢复夜盘。故21:00不存在可交易窗口。

## 三、商品仪表盘（12项展示；不限制全市场扫描）

> 下表EOD均为**9月29日last-good**，不是9月30日收盘；Night为归属9月30日交易日、已经完成的连续交易阶段。`1D/5D`按同一具体主力结算序列；curve为近月减次近月百分比，不能当现货基差。

| 板块 | 品种/合约 | 9/29 close/settle | 1D / 5D | Vol / OI / ΔOI | EOD curve | Physical/basis | 9/30早前Night close；vs close/vs settle；ΔOI | 15:00–19:42海外 | Options readiness | 当前信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| 橡胶 | BR2611 | 15460 / 15390 | -0.87% / +3.67% | 141383 / 55749 / -13960 | +1.10% backwardation | 缺失/C级 | 16155；+4.50%/+4.97%；+8194，fresh 23:00 | 合成橡胶代理+2.10%，天然橡胶代理-0.95%，冲突 | 无执行报价 | 节后30分钟确认，不追gap |
| 橡胶 | NR2611* | 16490 / 16525 | NR主力序列-3.07% / +2.95% | 78941 / 42104；主力ΔOI+1475 | NR curve -0.57% contango | 缺失/C级 | 17070；+3.52%/+3.30%；-1158，fresh 23:00 | 天然橡胶代理-0.95%，反向 | series surface可用；execution否 | 竞争解释强，等待45分钟 |
| 橡胶 | RU2701 | 19010 / 19040 | -2.13% / +1.14% | 254432 / 132155 / -14021 | +0.22% backwardation | context/C级 | 19665；+3.45%/+3.28%；+11873，fresh 23:00 | 天然橡胶代理-0.95%，反向 | surface可用；execution否 | 不把夜盘反弹直接外推 |
| 油脂 | OI701 | 10057 / 10044 | -0.89% / -1.39% | 216312 / 274068 / -6074 | +1.74% backwardation，z=+1.11 | context/C级 | 10234；+1.76%/+1.89%；+6681，fresh 23:00 | 棕榈油代理-0.67%，反向 | surface可用；execution否 | 节后重新检验相对强势 |
| 贵金属 | AG2612 | 14848 / 14906 | -1.79% / -8.25% | 299463 / 277181 / +14920 | -0.22% contango，z=-1.67 | 仓单/现货仅context | 14958；+0.74%/+0.35%；+7768，fresh 02:30 | 白银约-0.8%至-1.25%，反向 | ATM IV 38.63%，surface是；position/execution否 | 原空头条件过期，未获新确认 |
| 贵金属 | AU2612 | 898.78 / 897.86 | -1.56% / -5.06% | 237449 / 225820 / -677 | -0.15% contango | 仓单/现货仅context | 905.02；+0.69%/+0.80%；+1932，fresh 02:30 | 金价约持平；DXY略强、实际利率代理高位 | surface是；execution否 | 黄金信用叙事未形成方向证据 |
| 有色 | AO2701 | 2656 / 2658 | -1.59% / -2.39% | 218053 / 266990 / +34128 | -0.61% contango | context/C级 | 2662；+0.23%/+0.15%；-278，fresh 01:00 | 工业金属代理小涨 | IV 16.62%，surface/position是；execution否 | 原空头条件过期 |
| 原油 | SC2611 | 711.9 / 716.9 | -2.34% / -1.90% | 195579 / 29669 / -2741 | +1.94% backwardation | SC实体unavailable | 705.2；-0.94%/-1.63%；-1162，fresh 02:30 | WTI/Brent约+1.45%/+1.63%，但不同源合约报价分散 | IV 74.70%，surface是；execution否 | 等EIA；长假gap风险高 |
| 燃料 | FU2611 | 4438 / 4418 | +0.64% / +4.54% | 641064 / 150615 / -19038 | +22.97% backwardation，z=+1.38 | context/C级 | 4373；-1.46%/-1.02%；-5144，fresh 23:00 | 原油代理转强 | surface是；execution否 | 内外盘冲突，节后再定价 |
| 芳烃 | PX611 | 9388 / 9226 | -0.56% / +0.13% | 319210 / 124540 / -14699 | +0.15% | context/C级 | 9228；-1.70%/+0.02%；-9277，fresh 23:00 | 原油上涨 | surface/position是；execution否 | vs close弱、vs settle平：弹性下降 |
| 沥青 | BU2611 | 5246 / 5195 | +0.83% / -2.57% | 1007133 / 208969 / -15138 | +11.76% backwardation | context/C级 | 5142；-1.98%/-1.02%；-24314，fresh 23:00 | 沥青代理-2.51%，同向 | surface/position是；execution否 | 弱势但不可追，等45分钟 |
| 苯乙烯/航运 | EB2611 / EC2611 | 9917/9750；2845/2871.5 | EB +1.59/+2.61；EC -1.17/+10.40 | EB ΔOI+8529；EC -840 | EB +5.23%；EC -26.68%且roll flag | context/C级 | DCE Night缺失；EC无夜盘 | 苯乙烯代理+2.02%；集运指数-0.66% | execution均否 | EB旧多头窗口过期；EC曲线不可套利化 |

\* NR的Night代表合约是NR2611，而Market State主力是NR2612；因此不把NR2611的夜盘涨幅替代NR2612正式交易卡，也不计算NR2612的隔夜—日盘分解。

## 四、相比上一交易日/今晨真正变化

1. **数据层面变化最大**：统一输入在08:20加入了有效的9月30日交易日Night摘要，但19:42仍没有9月30日日盘EOD。相较今晨，我们能确认BR/RU/NR/OI等早前夜盘价格，却仍不能确认白天是否延续或反转。
2. **橡胶链成为最强早前Night链**：BR2611 +4.50%、NR2611 +3.52%、RU2701 +3.45%（均vs previous close）。BR同时增仓；NR减仓。它们同属价格—成交—持仓第1层，不能拆成多层证据。
3. **菜油早前Night相对强**：OI701 +1.76%，且9月29日曲线backwardation +1.74%；但19:30附近棕榈代理偏弱，境内外不一致，不能直接推广为油脂链共振。
4. **PX/TA/PR等close锚与settlement锚明显分歧**：PX夜盘vs close -1.70%，vs settlement约0；说明9月29日close已偏离settlement，不能把相对昨结算的平盘误写成没有隔夜新增压力。
5. **海外油价在中国收市后偏强但报价离散**：Trading Economics快照显示WTI/Brent约+1.45%/+1.63%；Reuters较早时段也偏强，但其他来源的不同合约出现回落。能源映射只列为21:00/节后gap证据，不能写成中国期货已交易。
6. **晨间交易窗口全部过期**：AG/AO/NR条件价差和EB/SC观察只适用于9月30日日盘且要求14:30前退出。没有成交反馈，触发状态记为unknown；不得假定用户持仓，也不得将这些条件移到10月8日。

## 五、产业链地图

| 产业链 | 方向/强弱 | 价格与Night | Curve | 库存/实体 | 期权 | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|
| 橡胶（BR/RU/NR） | 早前Night最强；节后偏多问题 | BR/RU/NR均大涨；BR增仓，NR减仓 | BR/RU backwardation；NR contango | 实体层缺可评分数据 | surface部分可研究，execution=0 | 合成/天然橡胶代理分化 | 9/30 EOD与社会库存 | 中低 |
| 油脂（OI/P/Y/RM） | OI相对强，板块未共振 | OI夜盘+1.76% | OI backwardation z+1.11 | 现货仅C级context | 无执行报价 | 棕榈代理-0.67% | 9/30日盘与高质量基差 | 中低 |
| 原油—燃料—沥青（SC/FU/LU/BU） | 高波动冲突 | SC/FU/BU早前Night弱，海外午后油价强 | SC/FU/BU均backwardation | SC/LU实体unavailable | SC IV高；execution=0 | 海外油价分歧，EIA未发布 | 9/30 EOD、EIA结果、进口全口径 | 低 |
| 贵金属（AU/AG） | 弱趋势但反弹/宏观冲突 | 9/29弱，早前Night小幅反弹 | AG/AU轻度contango | 仓单不等于社会库存 | AG surface可用，执行不可用 | 银弱、金平，DXY略强而美债收益率回落 | 9/30 EOD与实时组合报价 | 中低 |
| 芳烃—聚酯（PX/TA/EB） | 9/29强弱分化，新增弹性下降 | PX对close走弱；DCE EB Night缺失 | EB backwardation但样本仅4；PX近乎平 | context-only | surface可研究、不可执行 | 原油转强、苯乙烯代理强 | 9/30 EOD与DCE Night | 低 |

当前regime：**节前数据断层 + 长假gap累积 + 早前Night橡胶强势 + 海外能源再定价 + 全期权执行未就绪**。最强链为早前Night的橡胶；最弱可验证链为沥青/部分芳烃的close锚压力，但缺9月30日日盘确认。

## 六、机会排行榜（研究排序，不是胜率或仓位指令）

| 排名 | idea_id | 方向/周期/工具 | 分项（逻辑/赔率/催化/价曲波/拥挤） | 总分 | 支持层；反证/缺失 | 研究判断｜证据｜执行 |
|---:|---|---|---|---:|---|---|
| 1 | `COM-E-BR2611-RELSTRENGTH-20260930` | 偏多；10月8日后1–5D；BR2611期货（仅研究） | 19/15/12/10/11 | **67** | 支持1、2；反对4；缺3、5 | 存在待验证优势｜部分｜休市，等待10/8重报价与参数 |
| 2 | `COM-E-OI701-RELSTRENGTH-20260930` | 偏多；1–5D；OI701期货 | 18/14/11/10/10 | **63** | 支持1、2；反对4；缺3、5 | 存在待验证优势｜部分｜休市，等待10/8触发 |
| 3 | `COM-E-ENERGY-POSTEIA-20260930` | 事件后择向；1–3D；SC2611/FU2611研究篮子 | 17/12/13/8/8 | **58** | 支持2、4；反对1；缺3、5 | 证据不足｜不足｜休市，待EIA和9/30EOD |
| 4 | `COM-E-AG2612-DOWNSIDE-20260928` | 原偏空；已过期；AG熊市看跌价差 | 17/12/8/9/9 | **55** | 支持2；反对1、4；中性5；缺3 | 未发现当前优势｜部分｜已过期，节后重新立项 |
| 5 | `COM-E-EC2611-ROLL-20260924` | 曲线观察；1–10D；EC2611/远月仅观察 | 14/10/10/7/7 | **48** | 支持1；曲线pair roll反证；缺2–5 | 证据不足｜不足｜休市/不可执行 |

总分已逐项复核，均未超过分项上限；只有两个有效独立支持层的候选不超过69分。评分不代表胜率、期望收益或仓位。没有70+候选，不等于没有研究价值。

### 重点候选的定价分歧

- **BR**：市场早前Night已把强势定价到+4.50%。我们的分歧不是“还会马上上涨”，而是若10月8日大gap没有回吐且BR/RU/NR重新同向，9月29日低OI状态后的补库/资金回流可能延续；最强反证是天然橡胶海外代理走弱、9月30日EOD缺失及长假消息累积。
- **OI**：市场隐含菜油相对强于9月29日弱势收盘。我们的分歧仅是相对强势可能延续，非油脂普涨；反证是棕榈代理走弱、实体和高质量basis缺失。
- **能源**：海外在中国收市后重新抬价，但早前SC/FU/BU均弱。真正催化是22:30 EIA及长假期间地缘/出口恢复，竞争解释是不同月份合约与供应恢复导致报价分歧；缺进口平价全口径，不能称跨市场套利。

## 七、交易研究卡（仅2张，不凑数）

### 研究卡1：BR2611节后相对强势确认（非当前可执行卡）

- 事实：9/29 close/settle 15460/15390；9/30早前Night OHLC 15260/16210/15230/16155，vs close +4.50%、vs settle +4.97%，Night ΔOI +8194。9/29曲线+1.10% backwardation。
- 定价/推断：市场已大幅预交易橡胶利多；只有节后gap不回吐并获RU/NR同向与曲线维持确认，才存在延续优势。Night ΔOI只作归因线索，不等于已知新多。
- 最佳表达：BR2611单腿多，仅在参数核验后；不使用未定义的跨品种“中性”篮子。今晚无交易。
- 入场：10月8日09:30后，首30分钟低点不破且价格重新站上当日VWAP；分两批50%/50%。若集合竞价较16155高开>3%，等45分钟，不追首跳。
- 好/中/坏成交：好=VWAP下0–0.3%回踩成交；中=VWAP附近；坏=高于首30分钟高点追入，放弃。按计划风险R：初始止损为加权入场价下1.0%，TP1 +1.2R、TP2 +2.0R；滑点和涨停使实际损失可大于计划R。
- 失效/退出：跌破首30分钟低点且30分钟不收复，或BR强而RU/NR与curve反向；TP1减半、TP2或第5交易日退出。节后首日14:30仍未确认则取消。
- 风险：期货最大损失不由结构限定；单一试仓计划止损≤NAV 0.50%，压力损失按1/2个涨跌停另算。metadata仅确认last trading day=2026-11-16；multiplier/tick/margin/limit/night-session字段在仓库未确认，未补齐前不执行。交割风险高，最迟进入交割月前滚动。

### 研究卡2：OI701节后相对强势（非当前可执行卡）

- 事实：9/29 close/settle 10057/10044；早前Night OHLC 10057/10256/10051/10234，vs close +1.76%、vs settle +1.89%，Night ΔOI +6681；EOD curve +1.74% backwardation。
- 定价/推断：市场对菜油做了相对强势定价，但海外棕榈偏弱。若10月8日菜油强、棕榈/豆油不跟，可能是品种特异性；若三油同跌则Night信号失效。
- 最佳表达：OI701单腿多，非dollar-neutral、非beta-neutral。今晚无交易。
- 入场：10月8日10:00后，仅当OI701站上首小时VWAP且OI/P、OI/Y价差相对开盘扩大；50%试仓，价差维持至10:30再加50%。不使用9月30旧价挂单。
- 好/中/坏成交：好=VWAP±0.2%；中=VWAP上0.2%–0.5%；坏=超过首小时高点0.5%追入，放弃。止损为加权入场下1.2%或相对价差回到开盘值；TP1 +1R、TP2 +1.8R；第5交易日退出。
- 参数：multiplier=10吨/手，tick=1元/吨，tick value=10元；以早前Night close估算名义本金约102,340元/手。仓库margin=9%、price limit=8%、last trading day=2027-01-14。1/2个涨跌停压力约8,187/16,374元每手（以10234静态估算，不含保证金上调、滑点）。
- 失效/退出：OI高开后30分钟内回补全部gap、OI/P与OI/Y不扩、或新高质量basis/库存反向。交割月前滚动；单一试仓计划损失≤NAV 0.50%。

研究卡不足三张：能源篮子缺9月30EOD、EIA结果、精确跨品种配比与完整参数，不定义伪中性篮子。

## 八、商品期权专项

最新有效截面是2026-09-29（T-1相对9月30日），本期无新增成交报价。全样本13,324条、184 series；统一输入中180个series `surface_ready=true`、46个`positioning_ready=true`、**0个`execution_ready=true`**，bid/ask coverage=0，dealer gamma方向未知。全局quality/surface文件分别为not-ready与empty，与嵌入式per-series可研究状态并存；因此只能逐series做研究，不能宣称全市场曲面就绪。

- AG2612 2026-11-24：ATM 14900，ATM IV 38.63%，RR25 +2.86，BF25 +1.78；9/30早前标的反弹改变moneyness，9/29截面不代表当前报价。
- AO2701 2026-12-25：ATM 2650，ATM IV 16.62%，RR25 +3.89，BF25 +1.01；surface/positioning可研究，execution否。
- NR2612 2026-11-24：ATM 16400，ATM IV 21.92%，RR25 +2.48，BF25 +1.08；代表Night为NR2611，不能直接重估NR2612 Greeks。
- SC2611：ATM IV约74.70% vs RV20约59.19%；高IV不自动等于贵，也不证明卖波动，EIA/长假跳空使尾部风险更大。

event convexity结论：长假前后事件密集，但没有当前权利金和双边报价，有限损失结构优于裸期货仅是工具偏好，不是当前可执行建议。任何结构均为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。回避裸卖跨假期Gamma、用旧ATM冒充当前ATM、从OI节点推断做市商净Gamma。

## 九、21:00夜盘开盘风险地图

严格四层：

1. **9月30日中国完整EOD**：仓库缺失，不能作为事实。
2. **今天早前已完成Night**：归属trading_date=2026-09-30；BR/RU/NR/OI强，SC/FU/BU弱；只是历史价格发现。
3. **15:00–19:42海外**：原油偏强但不同源合约报价分散；银弱、金近平；DXY约101.43略强、USD/CNH约6.7065略升值；均未被中国收盘后的市场交易。
4. **下一实际Night**：今晚无夜盘。10月8日21:00恢复夜盘；更早的中国可交易窗口是10月8日08:55集合竞价/09:00日盘。

| 品种群 | 今晚21:00 | 下一窗口gap判断 | 是否追价 | 等待 | 首要确认 |
|---|---|---|---|---|---|
| BR/RU/NR | 休市 | 8天信息累积，方向不可估 | 否 | 45分钟 | 三品种同向、BR曲线、gap回补比例 |
| SC/FU/LU/BU | 休市 | EIA与地缘使gap双向高 | 否 | 45分钟 | 海外近月、成品油裂解、SC/FU曲线 |
| AU/AG | 休市 | 金/银分化，方向不可估 | 否 | 30分钟 | DXY、实际利率、金银比、IV新截面 |
| OI/P/Y/RM | 休市 | OI相对强需重证 | 否 | 30分钟 | 三油价差、仓单/现货、OI变化 |
| EC/LH/JD/LC等无常规夜盘品种 | 休市 | 10月8日09:00日盘定价 | 否 | 45分钟 | 集合竞价量、主力切换、涨跌停参数 |

不值得交易：今晚所有中国商品；10月8日首跳追价；任何以9月29日EOD或9月30日早前Night为当前挂单价格的策略；C级basis套利；无bid/ask的期权；EC roll-flag曲线“套利”。

## 十、未来24h / 7d事件

| 北京时间 | 事件 | 受影响 | 处理 |
|---|---|---|---|
| 9月30日22:30 | 美国EIA周度石油状态报告（发布前，结果未确认） | SC/FU/LU/BU、化工、航运 | 中国休市；不做过期条件单，记录为10/8 gap输入 |
| 10月1–7日 | 中国国庆/中秋休市；海外能源、金属、农产品持续交易 | 全品种 | Delta降至零或预先有限化；本报告不假设真实持仓 |
| 10月1–7日 | 地缘冲突、海峡/红海航运、矿山/油田/炼厂突发 | 油、运价、金属、橡胶 | 只能用有限损失工具；等待中国重开45分钟 |
| 未来7日 | OPEC+/IEA/CFTC/USDA/天气与交易所临时参数 | 能源、农产品、全市场保证金 | 截点前未核实具体日程者不编时间；以官方日历复核后再纳入 |
| 10月8日08:55/09:00 | 中国集合竞价/日盘重开 | 全部中国商品 | 所有旧触发作废；先核验涨跌停、保证金、主力合约和实时报价 |
| 10月8日21:00 | 节后首个夜盘恢复 | 有夜盘品种 | 首跳不追；15/30/45分钟按品种等待 |

人民币/美元：DXY略强与USD/CNH小幅下降（人民币略强）方向相互抵消，对人民币计价商品不是单一方向信号。黄金信用主题与AI现金流/Capex主题本期均未形成可识别、可归因的商品错价；PMI改善只作宏观背景，不预设金属多头。

## 十一、旧建议台账

| idea_id | 首次提出 | 原始期限/触发 | 上次状态 | 当前状态 | 变更原因与处置 |
|---|---|---|---|---|---|
| COM-E-AG2612-DOWNSIDE-20260928 | 09-28 | 9/30日盘失败反弹；14:30前退出 | 晨间69，等待触发 | 已过期/触发未知 | 时间窗口结束；早前Night反弹、海外银弱，证据冲突。若此前按条件建立，按原计划9/30 14:30前退出；不假设持仓 |
| COM-E-AO2701-DOWNSIDE-20260929 | 09-29 | 跌破2639；日内 | 晨间66 | 已过期/触发未知 | 无9/30盘中路径或EOD，不能核验；不得顺延 |
| COM-E-NR2612-DOWNSIDE-20260929 | 09-29 | 跌破16210；日内 | 晨间64 | 已过期且受挑战 | 代表合约NR2611早前Night +3.52%，但不同月份；旧条件仍因时间到期 |
| COM-E-EB2611-BACKWARDATION-20260929 | 09-29 | 日内回撤多 | 晨间61 | 已过期/数据不足 | DCE Night缺失、9/30EOD缺失；不假设成交 |
| COM-M-SC2611-DOWNSIDE-20260929 | 09-30 | 日内反弹失败空 | 晨间60 | 已过期；方向转待评而非反向 | 海外午后油价转强且EIA未发布；需要新数据重新立项 |
| COM-E-BR2611-RELSTRENGTH-20260930 | 09-30 | 10/8后1–5D | 新增研究 | 休市/等待重报价 | 新数据：有效exact-contract Night与curve |
| COM-E-OI701-RELSTRENGTH-20260930 | 09-30 | 10/8后1–5D | 新增研究 | 休市/等待重报价 | 新数据：Night相对强与backwardation；海外反证保留 |

## 十二、覆盖核对

| 板块 | 应覆盖 | 实际取数且已分析 | 9/30当日数据不足 | 不适用/流动性不足 | 未入榜最值得跟踪异常/无异常依据 |
|---|---|---|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/29 EOD与curve全部9个 | 9/30 EOD、当日curve、日盘路径 | 部分无夜盘/期权执行0 | I curve z约-1.8仍异常；其余无独立三层共振 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 全部12个 | 同上；部分Night unresolved | 期权执行0 | AG/AO旧弱势被早前Night小反弹削弱；NI夜盘偏弱 |
| 能源炼化化工 | SC/FU/LU/BU/PG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 全部21个（LPG按PG映射） | 同上；DCE Night大量缺失；SC/LU实体缺 | basis C、import parity不完整 | BR/RU/NR强；PX/TA锚分歧；EB无当日确认 |
| 新能源 | LC/SI/PS及GFEX新增材料 | LC/SI/PS + PD/PT | 9/30 EOD | 夜盘不适用、执行0 | LC 5D弱但无新增证据，不入榜 |
| 农产品油脂饲料畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 全部18个 | 9/30 EOD；实体覆盖仅子集 | 多个无夜盘；执行0 | OI夜盘相对强；CF小幅弱，无实体共振 |
| 航运软商品 | EC及CF/SR/AP/CJ/PK | 已纳入相应主表；EC单独扫描 | 9/30 EOD | EC无夜盘；curve roll flag | EC 5D强但9/29反转、曲线不可比 |
| 动态新增 | JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR | 14个均有9/29 EOD扫描 | 9/30 EOD；多品种流动性/历史不足 | 不满足正式卡参数或流动性要求 | BZ/苯乙烯代理仍强但DCE Night缺失 |

覆盖结论：强制63个代码全部在9月29日last-good层完成扫描，另含14个动态产品，共77个；37品种有归属9月30日的有效代表Night。**9月30日日盘EOD对全部63个均不足**，不能把“提到名字”当作完成当日分析，亦未因此缩小应覆盖清单。策略类别已扫方向、curve、基差/跨期、跨品种/跨市场、波动率/偏度/事件凸性和风格/中性表达；只有方向/curve研究具备部分证据，基差/RV/期权执行均因口径或报价缺口降级。周期覆盖：1D受9/30缺失限制，3/5/20D为截至9/29同合约指标。

## 风险预算

单一试仓计划损失NAV 0.25%–0.75%；确认交易0.75%–1.50%；同因子主题合并≤2.5%–3.0%。当前建议风险为0。压力测试必须另算1/2个涨跌停、长假gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压及人民币急变；期货止损不是最大损失保证。

## 来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（生成于2026-09-30 08:20:58，北京时间；支持质量状态、Night摘要、Options readiness）
- [China-Commodities-Engine期货EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)（交易日2026-09-29；支持合约OHLC/成交/OI）
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)（交易日2026-09-29；支持同合约收益、RV、OI和curve）
- [上期所2026年中秋/国庆安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)（2026-09-21；支持9/30无夜盘、10/1–7休市、10/8复市）
- [Trading Economics商品快照](https://tradingeconomics.com/commodities)（访问于2026-09-30约19:30；支持海外实时/准实时报价代理）
- [Reuters：油价与供给恢复、地缘及EIA预告](https://www.reuters.com/business/energy/oil-climbs-after-trump-denies-he-is-willing-ease-sanctions-iran-2026-09-30/)（2026-09-30；支持能源事件背景）
- [Reuters：中国9月制造业PMI](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-returns-growth-september-amid-ai-boom-2026-09-30/)（2026-09-30；支持宏观背景）
- [Reuters：金银与利率背景](https://www.reuters.com/world/india/gold-track-monthly-decline-investors-brace-us-inflation-data-2026-09-30/)（2026-09-30；支持贵金属外盘背景）
- [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)（官方发布页；结果在本截点尚未发布）

A. 今晚没有应立即建立的新仓位。
B. 今晚没有可挂的中国商品条件单；10月8日所有品种须以新集合竞价、EOD缺口修复和实时参数重建条件。
C. 今晚应继续观察BR2611/OI701节后相对强势、EIA后的SC/FU曲线、AG/AO新期权曲面与全部9月30日EOD补发。
D. 今晚必须避免任何中国商品交易、跨长假裸Delta、旧日盘条件顺延、C级basis套利、无bid/ask期权及把早前Night当今晚行情。
