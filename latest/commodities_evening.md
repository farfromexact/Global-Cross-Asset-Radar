# 全球商品期货期权高风险机会雷达（晚间版）｜2026-09-01｜远端更新后重跑 r2

> **一句话：能化供给冲击已经得到 T 日价格、曲线、海外油价与期权波动率四层确认，但日盘涨幅过大且 OI 普遍回落；今晚有条件做多 SC/BU/EG，不宜直接追价。**

本次为北京时间 **2026-09-01 23:20** 的手动重跑。China-Commodities-Engine 远端在原晚报之后完成了 9 月 1 日核心 Futures、Market State、Physical、External 与独立 Options pipeline 更新，因此旧版“统一 EOD 停在 8 月 31 日、评分封顶 69”的结论不再成立。本报告只使用仓库 EOD 和可核验的海外实时信息；**不把 21:00 之后中国夜盘价格写成事实，因为 Engine 不采集分钟/夜盘数据。**

## I. 今日一句话结论

**今晚值得承担“有条件的小仓位风险”，首选 SC/BU、其次 EG；全部要求实时中国报价确认，不允许在日盘大涨后的夜盘开盘直接追。**

## II. 数据质量与覆盖

- 核心 Futures：`data/last_run_status.json` 显示 run_date=2026-09-01，SHFE/INE/DCE/CZCE/GFEX 五所齐全，`source_date_match_pct=100%`，`critical_module_errors=0`，`full_market_ready=true`。
- Market State：`data/market_state_latest.json` 已生成 T 日 exact-contract 1/3/5/20D、RV20、Volume/OI、ΔOI、OI z-score 与近月—次月曲线。
- `data/report_input_latest.json` 已在远端更新，但本次连接器对约 1.2MB 正文直接展开受限；按 v2 优先级，改用 module-specific 最新状态覆盖 root legacy 状态，不把读取限制误判为数据缺失。
- Physical：`data/physical/latest.json` 23:05 BJT 更新，20 个 target 中 4 个可用，且均按原生频率 fresh、无 stale/carried-forward；I 为周度港口库存、JM 为旬度价格且 basis quality=C、FG 为周度库存、TA 为周度加工利润。它们对 SC/BU/EG 不构成 T 日方向性第三层证据。
- External：`data/external/latest.json` 23:05 BJT 更新；6/22 target 可验证，4 fresh、2 stale。仓库 Brent continuous 仅到 8/31，故 9/1 收盘后的油价变化单独用 Reuters 实时覆盖，不与中国 EOD 混写。
- Options：独立 pipeline 为 **2026-09-01 T 日**，23,200 个唯一合约、64/64 品种、387 个 series；IV 覆盖 98.16%，376/387 surface-ready、73 positioning-ready、0 execution-ready；全市场 bid/ask coverage=0，dealer gamma direction unknown。可用 ATM IV、RR25、BF25 做研究评分，**不能虚构可成交权利金、买卖价差、滑点或 dealer gamma 方向**。
- Contract metadata：root 仍为 partial，DCE contract_info 有 JSON decode error；因此 EG 的交易乘数/保证金/涨跌停/最后交易日不从旧数据填充，标记“参数未确认”。SC/BU 使用交易所公开规则，但当前临时风控参数仍需下单前核对。
- 数据异常：JR/PM/RI/WH/ZC 等出现 0/−100% placeholder，全部剔除，不进入机会排名。

## III. 商品仪表盘

| 板块 | 品种/主力 | T日结算/收盘 | 1D | 5D | 成交/持仓与ΔOI | 曲线 | 现货/仓单/Physical | 期权 | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 原油 | SC2610 | 637.2 / 637.8 | +3.06% | +7.67% | Vol 12.93万；OI 4.00万；ΔOI -6.32% | +4.32% backwardation；pair roll flag | 无可计 T 日 physical | ATM IV 53.06%，RR25 -1.04，surface ready / execution false | **强多但不追；首选** |
| 沥青 | BU2610 | 4904 / 4934 | +3.55% | +6.42% | Vol 43.87万；OI 23.89万；ΔOI -3.42% | +4.00% backwardation，z=+1.93 | 缺独立 asphalt physical | ATM IV 39.60%，RR25 -4.84，surface ready / execution false | **曲线最干净的能化多头** |
| 乙二醇 | EG2610 | 5481 / 5525 | +5.53% | -0.29% | OI 33.45万；ΔOI -2.45%；活动 z=+1.70 | +3.36% backwardation，但 curve z=-1.09 | 无可计 T 日 physical | ATM IV 47.29%，RR25 +1.13，positioning ready / execution false | **只做回撤承接** |
| 甲醇 | MA610 | 3044 / 3069 | +4.57% | +3.33% | Vol 237万；OI 66.48万；ΔOI -6.74% | +2.89% backwardation，z=+1.79 | 无可计 T 日 physical | surface 显示 underlier settle 3095，与 market-state 3044 不一致 | **数据错配+价涨仓减，降级** |
| PTA | TA701 | 5904 / 5930 | +2.71% settle | — | Vol 105.95万；OI 99.66万 | +1.51% backwardation | 周度加工利润 fresh，仅背景 | 全市场期权链 T 日；未做候选级 surface 抽取 | 能化 beta，次于 SC/BU |
| 玻璃 | FG701 | 953 / 969 | +1.38% settle | — | Vol 181万；OI 135.20万 | -1.09% contango | 周度库存 7404.9 重量箱；仓单 1268，日变0 | 未做候选级 surface | 价格强但库存方向证据不足 |
| 铁矿 | I2701 | 722 / 726.5 | -0.48% settle | — | Vol 25.53万；OI 57.73万 | +1.62% backwardation | 港口库存 15904（周度、原单位保留） | 未做候选级 surface | 中性，不追黑色 |
| 豆粕 | M2701 | 3357 / 3377 | +0.12% settle | — | Vol 183.09万；OI 282.69万 | -0.30% contango | 本次无新增可计 physical | 未做候选级 surface | 无优势 |
| 生猪 | LH2611 | 11775 / 11685 | -1.92% settle | — | Vol 18.04万；OI 22.89万 | -5.86% contango | 本次无新增可计 physical | 未做候选级 surface | 弱，但缺第二/三层确认 |
| 白银 | AG2610 | 16259 / 16245 | -2.46% settle | — | Vol 46.66万；OI 23.30万 | 近乎平坦 +0.01% | 无新增 physical | 未做候选级 surface | 宏观压制，非今晚首选 |
| 锂碳酸 | LC2701 | 159960 / 157860 | -0.34% settle | — | Vol 21.27万；OI 40.49万 | -0.29% contango | GFEX 仓单 fresh，但绝对量不等于方向 | 未做候选级 surface | 暂无 edge |
| 集运欧线 | EC2610 | 1831 / 1896 | -3.55% settle | — | Vol 2.41万；OI 2.48万 | 近月曲线极端且临近到期语义复杂 | 不作现货基差 | 无夜盘 | **不把极端曲线当套利信号** |

注：“—”表示本次未对非候选品种做候选级 5D 抽取，不用连续主力拼接替代。

## IV. 相比上一交易日/上一版真正变化

1. **数据门槛解除。** 旧版的核心问题是 9/1 T 日 Engine 未闭环；现在五所 Futures 与 Market State 已 T 日 ready，Options 也从 T-1 变成 T 日完整链。
2. **SC 的近端曲线现在显示 +4.32% backwardation。** 但 pair_roll_flag=true，所以这不是一个可无条件外推的“曲线历史突破”；更适合作为当前短缺方向确认，不能拿它做干净的 z-score 趋势。
3. **BU 是更干净的曲线确认：+4.00% backwardation，curve z=+1.93，pair_roll=false。** 这使 BU 从“油价 beta”升级成中国近端供需定价也在收紧的候选。
4. **EG 日内爆发并没有形成干净的 5D 趋势。** T 日 +5.53%，但 exact-contract 5D 仍 -0.29%；OI -2.45%，且 backwardation 的 z-score 反而为 -1.09。结论从“强势追多”改成“只等回撤承接”。
5. **MA 的涨势质量弱于表面。** ΔOI -6.74%，且期权 surface 的 underlying settle=3095 与 Market State settle=3044 不一致，故商品期权层不计分。
6. **海外油价在中国收盘后继续强化。** Reuters 约 21:02 BJT 报 Brent 92.66、WTI 88.24，均涨逾2%；这是海外新增信息，不写成中国夜盘已上涨。

## V. 产业链地图

### 1) 原油—成品/沥青链：最强
- **方向：多。**
- 价格：SC 1D +3.06%、5D +7.67%；BU 1D +3.55%、5D +6.42%。
- 曲线：SC +4.32% backwardation（roll warning）；BU +4.00%、z=+1.93（更干净）。
- 海外：Brent 92.66、WTI 88.24；Hormuz 船舶通行仍显著偏低，两艘载有沙特原油的 VLCC 遭袭，供给路线风险仍在。
- 期权：SC IV 53.06 vs RV20 37.05，BU IV 39.60 vs RV20 24.64，均明显“贵”；方向看多不等于应该追买裸 Call。
- 最大缺口：没有对应 T 日中国现货/炼厂/港口 physical closure；SC 还有 roll flag。
- 信心：SC 78/100；BU 76/100。

### 2) 乙二醇—聚酯链：强，但更像高波动反抽/再定价
- **方向：多，仅回撤。**
- EG 日涨 5.53%，但 5D -0.29%；OI -2.45%，price-up/OI-down 只能作为归因线索。
- 曲线仍 backwardation +3.36%，但 curve z=-1.09，意味着“绝对紧”不等于“边际继续收紧”。
- EG ATM IV 47.29% vs RV20 44.44%，波动率溢价不算夸张；RR25 +1.13 说明 upside call 比 put 更贵。
- 最大缺口：T 日港口库存/进口利润/装置开工并未形成可计的第三层 physical。
- 信心：72/100。

### 3) 甲醇链：价格强、质量弱
- **方向：观察多。**
- 1D +4.57%，但 ΔOI -6.74%；曲线 +2.89% backwardation、z=+1.79。
- Options surface 与 futures underlier settle 出现 51 点错配，因此不计期权层。
- 最大缺口：现货/港口/进口利润与 surface underlier 一致性。
- 信心：68/100。

### 4) 黑色—建材：分化、无统一趋势
- I 基本平，FG 偏强；weekly physical 只能当原生频率背景。
- 没有足够证据证明黑色整体进入新趋势。
- 信心：低。

### 5) 贵金属：弱，但不是今晚最优做空
- AG 日盘明显下跌；全球利率上行对贵金属不利。
- 但地缘风险具有突然反向拉升贵金属的尾部，且本次未完成候选级 AG options/curve 多层闭环。
- 结论：不把“弱”自动等同于“应空”。

## VI. 机会排名

| 排名 | 机会 | 分数 | 方向/周期 | 阶段 | 工具 | Fresh层 | 评分拆分 |
|---|---|---:|---|---|---|---|---|
| 1 | SC2610 供给冲击延续 | **78** | 多，1–3D | 条件试仓 | 期货优先；Call Spread仅研究 | ①②④⑤ | 逻辑22/25；凸性18/25；催化19/20；价格曲线波动11/15；拥挤技术8/15 |
| 2 | BU2610 原油冲击向近端沥青传导 | **76** | 多，1–5D | 条件试仓 | 期货优先；Call Spread仅研究 | ①②④⑤ | 21；17；18；12；8 |
| 3 | EG2610 回撤承接 | **72** | 多，1–5D | 条件试仓 | 期货；期权仅研究 | ①②④⑤ | 19；16；17；11；9 |
| 4 | MA610 回撤承接观察 | **68** | 多，1–3D | 观察 | 期货 only after confirmation | ①②④ | 18；15；16；10；9 |

**关键纪律：70+ 代表可以准备承担风险，不代表此刻应市价追单。今晚三个 70+ 候选全部属于 conditional probe，不属于 confirmed add-on。**

## VII. Top 3 交易卡

### #1 SC2610｜条件做多｜78

**事实**
- T 日 settle 637.2，1D +3.06%，3D +11.07%，5D +7.67%，RV20 37.05%。
- OI 40,001，单日 -6.32%，OI-change z=-1.94；price-up/OI-down 只说明上涨没有得到增仓确认。
- SC2610–SC2611 当前曲线 +4.32% backwardation，但 `pair_roll_flag=true`。
- 9/11 到期的 SC2610 options：ATM 640，ATM IV 53.06%，RR25 -1.04，BF25 +1.27；surface ready，positioning/execution not ready。
- Reuters 21:02 左右：Brent 92.66、WTI 88.24；Hormuz 通行仍低，供给路线风险没有解除。

**市场可能错在哪里**
市场可能低估“运输受阻持续时间”而不是单纯低估一次军事冲突。如果通行持续受限，近端 crude scarcity 可以在高油价下继续维持 backwardation；但若外交快速降温，当前溢价也会快速回吐。

**最优表达**
- 首选：SC2610 futures 的小仓位条件单。
- 期权：ATM附近 25–40Δ bull call spread 仅作研究；SC IV 比 RV 高约16 vol，裸买 Call 的波动率成本太高。
- 固定免责声明：research only; manual quote and manual confirmation required before execution; no premium quoted

**入场**
- 必须先取得真实夜盘报价；Engine 不提供当前 23:20 中国价格。
- 若实时 SC 在日盘 settle 637.2 上方完成 15–30 分钟接受，且 Brent 仍 >92，可开 1/3 probe。
- 若实时 SC 已高于日盘 settle **2%以上（约650）且没有回撤**，不追。
- 第二笔只在 Brent 继续上破/SC 回踩不破且国内近端结构仍紧时加；第三笔留给下一次 OI 不再明显收缩的确认。

**止损/失效**
- 初始止损：实时结构低点；若缺乏结构参考，用 **SC <625 且 Brent <90.5** 作为硬失效组合。
- 地缘快速停火、Hormuz 通行显著恢复、SC 曲线重新转 contango，任一出现都取消多头。
- TP1=1R，TP2=2R；时间止损 1–3D。

**风险**
- 单笔最大 NAV 损失：0.50%，上限0.75%。
- 最坏情景：停火/通航消息造成夜盘跳空，止损无法按计划成交。
- 标准合约：1000桶/手，tick 0.1元/桶，tick value 100元；按637.2计名义约63.72万元/手。
- 标准最低保证金5%、标准涨跌停不超过前结算±4%；**当前临时风控参数未确认，不能把标准值当今天实际券商参数**。
- 夜盘：21:00–02:30。
- 最后交易日规则：交割月前一月最后一个交易日；SC2610 已进入临近交割月阶段，1–3D交易可以，但必须提前滚动/退出，不承担交割风险。
- 按标准±4%仅作压力基线，一板约2.55万元/手；若交易所临时扩大幅度，真实压力更高。

### #2 BU2610｜条件做多｜76

**事实**
- settle 4904，1D +3.55%，5D +6.42%，20D +22.66%，RV20 24.64%。
- ΔOI -3.42%，不是增仓趋势。
- BU2609–BU2610 +4.00% backwardation，curve z=+1.93，pair_roll=false，曲线证据比 SC 更干净。
- BU2610 9/23 options：ATM 4900，IV 39.60%，RR25 -4.84，BF25 +0.80；surface ready，execution=false。
- IV 比 RV 高约15 vol；负 RR 表示 put 明显更贵，bull call spread 在 skew 上相对比 put-funded 结构更干净，但仍需实时报价。

**市场可能错在哪里**
市场可能仍按“原油涨、沥青跟涨”的简单 beta 理解，而当前中国近端 BU backwardation 已经显示更紧的本地时间结构；反面是终端道路需求/炼厂库存没有 T 日 physical 闭环，不能把曲线直接解释成消费旺盛。

**入场/管理**
- 真实夜盘 BU 报价重新确认；若 4900 一带回踩后站稳，且 Brent >92，开 1/3。
- 若 >5000（约日结算+2%）无回踩，不追。
- 加仓要求：BU 近端 backwardation 不显著收窄 + Brent 不回落。
- 初始止损：实时结构低点；硬失效参考 **BU <4825 且 Brent <90.5**。
- TP1=1R，TP2=2R；时间止损 1–5D。
- 单笔 NAV 风险 0.40%–0.60%。

**合约参数**
- 交易单位 10吨/手；tick 1元/吨；tick value 10元；4904 对应名义约4.904万元/手。
- SHFE 规则显示交割月前第一个月起保证金阶段基准提高；BU2610 当前已处于交割月前月，**实际交易所/券商保证金与临时风控参数下单前确认**。
- 标准规则涨跌停/保证金可能被风险通知动态调整，不把历史标准当实时值。
- 规则上的最后交易日为交割月份15日（遇休市顺延/调整）；BU2610 确切日历需下单端确认。
- 夜盘通常为21:00–23:00；以交易所当日安排为准。
- 交割风险：中等；本策略只做1–5D，不进入交割月中后段。

### #3 EG2610｜回撤承接多｜72

**事实**
- settle 5481，T日 +5.53%，但 5D **-0.29%**，20D +15.83%，RV20 44.44%。
- ΔOI -2.45%；不是增仓突破。
- EG2609–EG2610 +3.36% backwardation，但 curve z=-1.09，说明绝对结构仍紧、边际却没有更紧。
- EG2610 9/16 options：ATM 5500，IV 47.29%，RR25 +1.13，BF25 +2.135；OI coverage 94.3%，positioning ready，execution=false。
- IV 仅比 RV 高约2.85 vol，远没有 SC/BU 那么贵；但正 RR 表示 upside call 已经更贵。

**市场可能错在哪里**
油品/进口扰动可能继续向乙二醇成本与进口物流传导；但 T 日暴涨中 OI 回落、5D仍近零，使“趋势延续”不如“高波动回撤后再做多”有赔率。

**入场/管理**
- 不允许在 5525 日收盘价上方直接追。
- 等实时价格回撤后重新站回 5480–5520 区间，并维持至少15–30分钟；若同时 SC/Brent 仍强，再做 1/3。
- 若开盘/夜盘直接 >5590 附近且无回撤，放弃。
- 初始止损：回撤结构低点；硬失效为 **<5400** 且原油链同步转弱。
- TP1=1R，TP2=2R；时间止损 1–5D；NAV 风险 0.35%–0.50%。
- 期权仅考虑 25–40Δ bull call spread 研究结构；execution=false，不能给权利金或具体成交腿。
- 固定免责声明：research only; manual quote and manual confirmation required before execution; no premium quoted

**参数**
- DCE contract metadata 本次仍有 JSON decode error；乘数、tick、当前保证金、涨跌停、夜盘与 EG2610 确切最后交易日均标记 **参数未确认**。不得拿其他月份或旧规则补齐。

## VIII. 商品期权特别部分

本次不宣称“全市场最高/最低 IV”，因为没有对 376 个 surface-ready series 做统一期限归一化排名；只给候选代表样本：

| 品种/到期 | ATM IV | RV20 | IV−RV | RR25 | Readiness | 结论 |
|---|---:|---:|---:|---:|---|---|
| SC2610 / 9-11 | 53.06% | 37.05% | +16.01 vol | -1.04 | surface yes / positioning no / execution no | vol贵，期货优于裸Call |
| BU2610 / 9-23 | 39.60% | 24.64% | +14.96 | -4.84 | surface yes / positioning no / execution no | put skew很贵；看多可研究call spread |
| EG2610 / 9-16 | 47.29% | 44.44% | +2.85 | +1.13 | surface yes / positioning yes / execution no | vol较合理，但upside已偏贵 |
| MA610 / 9-11 | 43.36% | 32.76% | +10.60 | +0.76 | surface/positioning yes / execution no | underlier settle错配，**不用于交易评分** |

- 所有具体结构都需要实时 bid/ask、成交量与流动性确认。
- 不推断 dealer gamma 方向。
- 不给“可成交权利金”、精确滑点或净成本。
- 事件凸性上，SC 的方向性催化最强，但其 IV 也最贵；因此“事件强”不等于“买波动最划算”。

## IX. 21:00 风险地图（23:20重跑补充）

本版重跑发生在夜盘已开始后，但 Engine 没有夜盘分钟数据，因此以下仍以 **中国日盘 settlement + 海外 21:02 Reuters** 构建，不假装知道当前中国夜盘价格。

| 品种 | 中国日盘锚 | 海外新增信息 | 预期方向 | 置信度 | 追价？ | 实际动作 |
|---|---:|---|---|---|---|---|
| SC | 637.2 | Brent 92.66 / WTI 88.24，供给路线风险上升 | 正 gap/强势概率高 | 高 | **否** | 先看真实夜盘15–30分钟接受；>+2%无回撤不追 |
| BU | 4904 | 原油上行 + 本地 backwardation z高 | 偏正 | 中高 | 否 | 回踩4900附近承接优于开盘追 |
| EG | 5481 | 原油链强，但自身5D/ΔOI较弱 | 偏正但易冲高回落 | 中 | 否 | 只做回撤确认 |
| MA | 3044 | 能化 beta 正；自身 OI弱、surface错配 | 双向高波动 | 中低 | 否 | 观察 |
| EC | 1831 | 无对应夜盘 | 不适用 | — | — | 下一交易窗口 9:00 |

SC 官方连续交易为 21:00–02:30。EC 无夜盘。BU/EG/MA 以交易所当日交易时间与下单端为准；本报告不因常见时段记忆而伪造“当前可交易”状态。

## X. 未来24h / 7d事件

1. **9月2日 22:30 BJT：EIA Weekly Petroleum Status Report。** 对 SC/BU/FU/LU/LPG 是 24h 内最直接的库存与供需催化。若持多，事件前不把 probe 加到 confirmed-size；可用减仓或定义损失的期权结构控制 gap。
2. **9月4日 20:30 BJT：美国8月 Employment Situation / NFP。** 影响美元、实际利率、原油需求预期和贵金属；贵金属/有色仓位需降低单因子暴露。
3. **Hormuz/美伊冲突：持续事件，不存在可安全预测的时间点。** 船舶通行恢复速度比政治表态更重要；SC 多头的核心失效变量是“实际通行恢复 + 油价回落”，不是某一句新闻标题。
4. **OPEC+：本次没有从可靠官方/Reuters结果确认未来7日内一个应作为主交易锚的具体决策时点。** 不沿用未经复核的“9月6日必有会议”假设。
5. **CFTC/USDA/WASDE/IEA：** 本次未发现24h内会直接改变前三候选的已确认发布；WASDE不在未来7日核心窗口内。若后续日历确认新增事件，再调整 Vega/Delta，而不是提前编造催化。
6. **中国交易所参数：** 当前地缘油价高波动环境下，保证金和涨跌停临时调整本身就是风险事件；下单前读取交易所/券商实时参数。SC/BU 任何临时提保都应降低手数，而不是增加现金保证金后维持原杠杆。
7. **天气：** 本次没有验证到一个足以对前三候选独立计分的热带天气事件，故不计证据层。

### 风险预算与压力测试

- Probe：每个主题最大 NAV 0.25%–0.75% 亏损；本次建议 SC 0.50%、BU 0.40%–0.60%、EG 0.35%–0.50%。
- Confirmed：只有在下一次价格、曲线、OI/physical继续确认后才允许单主题提升到 0.75%–1.50%。
- SC+BU+EG 同属“中东供给/能化”因子，**组合总损失预算不超过 NAV 1.25%–1.50%，绝不能按三个独立主题各自满配**。
- 极端压力：停火消息导致夜盘跳空；1–2个涨跌停；相关性崩溃；交易所提保；流动性消失；人民币突变；海外油价在中国闭市时急转；IV在事件后瞬间塌陷。
- 期权执行未 ready，因此任何 options idea 都只作为“定义损失的候选表达”，不直接下单。

## XI. 来源与数据路径

China-Commodities-Engine 实际读取/核验：
- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`
- `data/latest.json`
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`
- `data/options/latest.json`
- `data/contract_meta.json`

公开来源：
1. Reuters, Oil up more than 2% as renewed US-Iran strikes stoke supply fears: https://www.reuters.com/business/energy/oil-prices-rise-latest-fighting-resurrects-middle-east-supply-disruption-risks-2026-09-01/
2. Reuters, Strait of Hormuz commodity vessel transits stay in single digits: https://www.reuters.com/world/middle-east/strait-hormuz-commodity-vessel-transits-stay-single-digits-data-shows-2026-09-01/
3. Reuters, Russia cuts expected 2026 oil output to 17-year low: https://www.reuters.com/business/energy/russia-cuts-expected-2026-oil-output-17-year-low-war-fallout-draft-forecasts-2026-09-01/
4. EIA Weekly Petroleum Status Report schedule: https://www.eia.gov/petroleum/supply/weekly/
5. BLS Employment Situation release schedule: https://www.bls.gov/schedule/news_release/empsit.htm
6. INE crude oil contract: https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html
7. INE trading hours: https://www.ine.cn/services/calenderandholidays/tradinghours/
8. SHFE operational rules: https://www.shfe.com.cn/eng/services/Rules/SHFERules/202512/t20251231_829981.html

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：SC2610回撤/接受后做多、BU2610回踩确认做多、EG2610回撤承接多；均先验证真实夜盘报价与交易参数。
C. 今天应继续观察的机会：MA610、TA701、AG2610，以及SC2610→SC2611的移仓与曲线稳定性。
D. 今天必须避免或退出的交易：日盘大涨后无回撤追多能化、在execution_ready=false时按EOD settlement臆测期权成交成本、把同一能化因子拆成三笔独立满风险仓位。
