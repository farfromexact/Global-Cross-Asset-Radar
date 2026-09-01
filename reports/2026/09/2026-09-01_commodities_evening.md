# 全球商品期货期权高风险机会雷达（晚间版）｜2026-09-01｜远端更新后重跑 r3

> **一句话：T日五所与期权已补齐，晚间从“无交易”升级为条件风险：BU/SC回撤多、M2701趋势多最优，但没有应立即追价建立的新仓位。**

本次于北京时间 **2026-09-01 23:39** 手动修订。China-Commodities-Engine 在原 19:30 晚报窗口之后补齐了 9 月 1 日 EOD Futures、Market State、Physical、External 与独立 Options pipeline。本修订版允许使用这些后来补齐、但对应 **9 月 1 日日盘 EOD** 的数据纠正数据门槛；为避免 hindsight，正式机会评分与 21:00 风险地图的海外价格截面仍严格截止 **19:30 BJT**，不使用 19:30 之后外盘变化，也不使用任何中国夜盘价格。Engine 本身没有分钟/夜盘行情。

## I. 今日一句话结论

**有70+条件交易，但没有应立即建立的新仓位：BU2610、SC2610与M2701最值得等确认，核心纪律是不追日盘大涨。**

## II. 数据质量与覆盖

- 第一读取层：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；候选继续读取 `data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/options/latest.json`、`data/contract_meta.json`。
- 核心 Futures：`run_date=2026-09-01`，SHFE/INE/DCE/CZCE/GFEX 五所齐全；`source_date_match_pct=100%`、`critical_module_errors=0`、`full_market_ready=true`。但 `official_complete=false`，因此“全市场可研究”不等于“所有辅助模块官方完备”。
- Market State：T 日 exact-contract 1/3/5/20D、RV20、成交、持仓、ΔOI、OI/成交 z-score 与近月—次近月曲线已生成；不拼接变化的主力合约。
- 数据异常：`ohlc_placeholder_count=3`；JR/PM/RI/WH/ZC 等 0 / -100% placeholder 全部剔除，不进入排名。
- Physical：23:05 BJT 重建；20 个 target 中仅 4 个 verified mapping，4 个均按原生频率 fresh、无 stale/carried-forward。I 为周度港口库存、JM 为旬度价格且 basis quality=C、FG 为周度企业库存、TA 为周度加工费。孤立绝对值只作背景，不自动构成方向性 physical layer。
- External：23:05 BJT 重建；22 个 target 中 6 个 verified，4 fresh、2 stale。仓库 Brent continuous 仅为 8/31 EOD 背景；正式 19:30 layer 4 单独使用 15:00–19:30 海外实时截面，不与中国价格混写。
- Options：独立 T 日 pipeline 为 23,200 个唯一合约、64/64 品种、387 个 series；IV coverage 98.16%，376/387 `surface_ready`、73/387 `positioning_ready`、0 `execution_ready`；全市场 bid/ask coverage=0，dealer gamma direction unknown。可以研究 ATM IV / RR25 / BF25，但不能写成可直接成交的权利金、价差、滑点或 dealer Gamma 方向。
- Contract metadata：root 为 `partial_error`，DCE contract_info 存在 JSON decode error。BU/SC 仅使用已核验的交易所标准合约规则作压力基线；**当前临时保证金、涨跌停、券商加收与夜盘当日安排仍需下单前确认**。M 因 DCE metadata 失败，关键参数一律写“参数未确认”。

## III. 商品仪表盘

| 板块 | 品种/主力 | T日结算/收盘 | 1D | 5D | 成交/OI/ΔOI | 曲线 | Physical/仓单 | ATM IV / readiness | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能源化工 | **BU2610** | 4904 / 4934 | +3.55% | +6.42% | 43.87万 / 23.89万 / **-3.42%** | **+4.00% backwardation，z=+1.93，无roll** | 无T日方向性physical闭环 | 39.60%，surface yes / exec no | **最干净的能化条件多** |
| 原油 | **SC2610** | 637.2 / 637.8 | +3.06% | +7.67% | 12.93万 / 4.00万 / **-6.32%** | +4.32% backwardation；**pair roll flag** | 无T日方向性physical | 53.06%，surface yes / exec no | **催化最强，但结构比BU脏** |
| 油脂油料 | **M2701** | 3357 / 3377 | +0.12% | **+4.00%** | 183.09万 / 282.69万 / **+5.60万手（+2.02%）** | -0.30% contango，但**曲线收紧z=+2.54** | 本次无新增physical | 14.43%，OI coverage 97.6%，surface yes / exec no | **低噪声趋势候选** |
| 贵金属 | **AU2610** | 961.04 / — | -1.76% | **-4.75%** | 22.40万 / 17.23万 / -3.85% | +0.10%近乎平坦 | 无新增physical | 23.44%，surface/positioning yes / exec no | 反弹失败空，不追低 |
| 能源化工 | EG2610 | 5481 / 5525 | +5.53% | **-0.29%** | 159.89万 / 33.45万 / -2.45% | +3.36% backwardation，z=-1.09 | 无T日physical | 47.29%，surface/positioning yes / exec no | 只做回撤承接 |
| 能源化工 | MA610 | 3044 / 3069 | +4.57% | +3.33% | 237.09万 / 66.48万 / **-6.74%** | +2.89% backwardation，z=+1.79 | 无T日physical | surface underlier settle=3095 与 market-state 3044 错配 | **降级观察** |
| 聚酯 | TA701 | 5904 / 5930 | +2.71% | 未候选级抽取 | 105.95万 / 99.66万 | +1.51% backwardation | 周度加工费677.532元/吨，仅背景 | 未候选级抽取 | 能化beta，次于BU/SC |
| 建材 | FG701 | 953 / 969 | +1.38% | +4.04% | 181.02万 / 135.20万 / -3.05% | -1.09% contango，收紧z=+2.39 | 周度库存7404.9重量箱；仓单1268、日变0 | 未候选级抽取 | 反弹，尚非完整多头 |
| 黑色 | I2701 | 722 / 726.5 | -0.48% | +0.77% | 25.53万 / 57.73万 / +1.44% | +1.62% backwardation，z=+2.72 | 周度港存15904（原单位保留），绝对值背景 | 未候选级抽取 | 曲线偏强、价格未确认 |
| 新能源 | LC2701 | 159960 / 157860 | -0.34% | +3.90% | 21.27万 / 40.49万 / +0.47% | -0.29% contango | GFEX仓单45839，日增1209 | 未候选级抽取 | 多头质量下降 |
| 贵金属 | AG2610 | 16259 / 16245 | -2.46% | 未候选级抽取 | 46.66万 / 23.30万 | +0.01%近乎平坦 | 无新增physical | T日期权存在，未候选级抽取 | 宏观压制但尾部反转风险大 |
| 航运 | EC2610 | 1831 / 1896 | -3.55% | 未候选级抽取 | 2.41万 / 2.48万 | 极端近端结构 | 不作现货基差 | — | 不把极端曲线当套利 |

## IV. 相比上一交易日 / 上一 revision 真正变化

1. **旧版的数据门槛已经解除。** 五所 Futures、exact-contract Market State 和独立 Options 都是 9/1 T 日；旧版因 T-1 只能封顶69分的约束不再成立。
2. **BU 上调为第一。** BU 5D +6.42%，近端 backwardation +4.00%、curve z +1.93 且无 roll warning；SC 虽催化更强，但 OI -6.32% 且 pair-roll 使曲线历史可比性更差。
3. **M2701 从“无优势”上调为真正候选。** 5D +4.00%、OI 单日 +5.60万手、曲线相对历史收紧至 +2.54σ，期权 ATM IV 14.43% 对 RV20 10.19%；它是今晚最不依赖地缘 headlines 的趋势候选。
4. **SC/BU/EG 的日盘强势仍有共同瑕疵：价涨仓减。** 这只能解释为持仓未同步确认，不能直接叫“空头回补”或“新多入场”。
5. **期权层从缺失变成可研究，但仍不可直接执行。** 376/387 surface-ready，execution-ready=0；SC/BU IV 显著高于 RV，裸买 Call 的波动率成本偏高。
6. **正式19:30截面剔除所有21:00后信息。** 原 r2 使用了更晚的海外油价；r3 只保留 18:46 BJT 的 Brent 92.21 / WTI 87.88 与 18:03 BJT 的黄金截面，避免用后见之明重写晚间决策。

## V. 产业链地图

### 1) 原油—沥青链：最强，但“BU结构 > SC催化”
- **方向：条件多。** BU 与 SC 同时具备日盘趋势、backwardation、海外油价确认和 T 日期权层。
- **BU 更干净：** 5D +6.42%，curve +4.00%、z +1.93、无 roll；缺点是 OI -3.42%、没有 T 日沥青 physical closure。
- **SC 催化更强：** 5D +7.67%，19:30前 Brent/WTI 仍明显上涨；但 OI -6.32%、curve pair-roll，使“短缺持续”需要更严格的价格确认。
- **期权：** BU IV 39.60 vs RV20 24.64；SC IV 53.06 vs RV20 37.05。两者 vol 都贵，方向观点优先用期货小仓位，期权只研究 bull call spread。
- **最大缺口：** T日炼厂/库存/现货利润等 physical 第三层没有闭环。
- **信心：BU 78/100；SC 76/100。**

### 2) 豆粕链：低噪声的独立多头候选
- **方向：条件多 M2701。** 5D +4.00%、OI +2.02%，price-up/OI-up 只是归因线索，但比能化的“价涨仓减”更健康。
- 近端仍是 -0.30% contango，不能说已进入绝对短缺；真正重要的是 curve z=+2.54，说明 contango 相对历史显著收紧。
- ATM IV 14.43% vs RV20 10.19%，vol 有溢价；RR25 +5.27 表明 call skew 已贵，因此如果用期权，更适合用上方卖腿对冲一部分波动率成本。
- **最大缺口：** 本次没有可计的豆粕 physical / CBOT exact-contract / import parity layer，因此只给 75 分，不做 confirmed add-on。
- **信心：75/100。**

### 3) 贵金属：方向偏空，但更像多头撤退而非新空趋势
- AU exact-contract 5D -4.75%，当日 -1.76%，但 OI 同时 -3.85%，属于 `price_down_oi_down` 归因线索，不能写成“空头主动增仓”。
- 18:03 BJT Reuters 截面：spot gold 4369.24，日跌1.8%；美国长端收益率上升，方向上支持贵金属承压。
- AU ATM IV 23.44 vs RV20 21.29，vol 不算极端贵；RR25 +3.37 表明 calls 更贵，若做空可研究 put spread，但仍无 bid/ask 执行层。
- **结论：只空失败反弹，不追开盘低点。**

### 4) 乙二醇—聚酯链：日涨最猛，不等于趋势最强
- EG T日 +5.53%，但 exact-contract 5D **-0.29%**；OI -2.45%，curve z=-1.09。
- 绝对 backwardation +3.36% 仍显示近端紧，但“边际继续收紧”并未得到历史 z-score 支持。
- **结论：只做回撤承接，排名低于 BU/SC/M。**

### 5) 黑色/建材：曲线有信息，价格没有统一确认
- I 的 curve z +2.72，但 1D 价格仍 -0.48%；FG 5D +4.04% 但 OI -3.05%、仍 contango。
- Weekly physical 是原生频率 fresh 背景，但没有方向变化序列，不计独立第三层。
- **结论：不把局部曲线收紧扩展成“黑色新趋势”。**

## VI. 机会排名

| 排名 | 机会 | 分数 | 方向/周期 | 阶段 | 工具 | Fresh evidence层 | 评分拆分 |
|---|---|---:|---|---|---|---|---|
| 1 | **BU2610 回撤确认多** | **78** | 多，1–5D | conditional probe | 期货优先；Call Spread仅研究 | ①价格量仓 ②曲线 ④海外 ⑤期权 | 逻辑22/25；凸性17/25；催化18/20；价格曲线波动12/15；拥挤技术9/15 |
| 2 | **SC2610 供给冲击延续** | **76** | 多，1–3D | conditional probe | 期货优先；Call Spread仅研究 | ①②④⑤ | 22；17；20；10；7 |
| 3 | **M2701 低噪声趋势多** | **75** | 多，2–10D | conditional probe | 期货优先；Call Spread仅研究 | ①②⑤ | 21；16；11；14；13 |
| 4 | **AU2610 反弹失败空** | **73** | 空，1–3D | conditional probe | 期货；Put Spread仅研究 | ①④⑤ | 20；17；15；12；9 |
| 5 | **EG2610 回撤承接多** | **71** | 多，1–5D | conditional probe | 期货；Call Spread仅研究 | ①②④⑤ | 19；15；17；11；9 |

**70+ 代表“值得准备承担小仓位风险”，不代表“现在就市价下单”。当前没有任何一个候选达到 confirmed add-on：能化缺 physical、SC/BU/EG 又普遍价涨仓减；M 缺 external/physical；AU 缺增仓确认且存在地缘反向跳空风险。**

## VII. Top 3 交易卡

### #1 BU2610｜回撤确认多｜78

**事实**
- settle 4904，1D +3.55%，3D +7.64%，5D +6.42%，20D +22.66%，RV20 24.64%。
- OI 238,945，ΔOI -8,451（-3.42%），OI-change z -0.75；上涨未获增仓确认。
- BU2609–BU2610 近端 +4.00% backwardation，curve z +1.93，pair_roll=false。
- 9/23 到期 BU2610 options：ATM 4900，ATM IV 39.60%，RR25 -4.84，BF25 +0.80；surface-ready，positioning-ready=false，execution-ready=false。
- 18:46 BJT 海外截面：Brent 92.21、WTI 87.88，分别约 +1.9% / +2.47%；这是海外市场新增信息，不是中国夜盘涨幅。

**市场可能错在哪里**
- 市场也许仍把 BU 视为简单 crude beta；当前中国近端 time-spread 已明显收紧，可能意味着供给冲击在本地近端结构中的传导比简单方向 beta 更强。
- 反面：没有 T 日沥青现货/炼厂/库存 physical closure，不能把 backwardation 直接解释成终端需求旺盛。

**最优表达与入场**
- 首选：BU2610 futures，小仓位条件单；不追日盘涨幅。
- 任何实际下单前先取得真实盘中报价。若从下一决策窗口计，先等 **30–45分钟**；要求 4900 一带/首30分钟低点守住，且下单时海外原油未明显跌破正式19:30逻辑锚。
- 若实时价格已高于日结算约 **2%（约5002）且无回撤**，放弃追多。
- 分批：1/3 结构确认；第二笔要求油价与国内价格继续共振；第三笔只留给下一次 EOD OI/curve 继续确认。

**止损 / 失效 / 退出**
- 初始止损：实时结构低点；若缺少结构，用 **BU <4825 且 Brent <90.5** 作为硬逻辑失效组合，而非机械盘中止损。
- 失效：原油快速去风险、BU time-spread 明显收窄/转 contango、或地缘供应路线实质恢复。
- TP1=1R，TP2=2R；时间止损 1–5D。
- Probe 最大损失建议 NAV **0.40%–0.60%**。

**合约与压力基线**
- 交易单位：10吨/手；最小变动：1元/吨；tick value=10元/手；按4904名义约49,040元/手。
- SHFE 标准规则：交割月前第一月起最低保证金基准10%；**当前交易所临时参数与券商加收未确认**。
- 标准涨跌停基线 ±3%；**当前临时涨跌停未确认**。按标准3%做纯压力基线：一板约1,471元/手，两板线性粗算约2,942元/手；不代表当前实际限幅。
- 最后交易日规则：交割月份15日（遇休市/交易所调整按规则）；BU2610 对应具体日历仍应在下单端确认。
- 夜盘安排：**未确认，以交易所当日安排为准**。
- 交割：实物；本策略只做1–5D，进入交割月前主动滚动/退出。

**期权**
- IV-RV≈+14.96 vol，裸买 Call 成本偏高；可研究 25–40Δ bull call spread。
- `research only; manual quote and manual confirmation required before execution; no premium quoted`

### #2 SC2610｜供给冲击延续｜76

**事实**
- settle 637.2，1D +3.06%，3D +11.07%，5D +7.67%，20D +20.98%，RV20 37.05%。
- OI 40,001，ΔOI -2,698（-6.32%），OI-change z -1.94；price-up/OI-down 只作归因线索。
- SC2610–SC2611 +4.32% backwardation，但 pair_roll_flag=true，仅1个可比观测，不能宣称“曲线历史突破”。
- 9/11 到期 options：ATM 640，IV 53.06%，RR25 -1.04，BF25 +1.27；surface-ready，positioning/execution not ready。
- 18:46 BJT Brent/WTI 仍明显上涨，支持供给路线风险继续被定价。

**市场可能错在哪里**
- 真正的误价可能不是“有没有冲突”，而是 **Hormuz/运输受阻持续多久**。如果实际通行持续受限，近端 scarcity 可以继续维持高油价与 backwardation；若通航快速恢复，溢价会迅速回吐。

**入场 / 管理**
- 不使用 21:00 后中国价格作为本修订版事实。实际下单时必须先看真实盘中价。
- 从下一决策窗口等待 30–45 分钟；若价格继续接受在 637.2 上方、且外盘原油仍保持强势，可开 1/3 probe。
- 若实时价格已比637.2高 **2%以上（约650）且无回撤**，不追。
- 初始止损：实时结构低点；硬逻辑失效参考 **SC <625 且 Brent <90.5**。
- TP1=1R，TP2=2R；时间止损1–3D；单笔 NAV 风险 **0.40%–0.60%**。

**合约与压力基线**
- INE 标准合约：1000桶/手；tick 0.1元/桶；tick value=100元；按637.2名义约637,200元/手。
- 标准最低保证金5%、标准涨跌停基线 ±4%；**当前临时保证金/限幅与券商加收未确认**。
- 按标准4%压力基线：一板约25,488元/手，两板线性粗算约50,976元/手；不代表当前实际限幅。
- 最后交易日规则：交割月前一月最后一个交易日；SC2610 规则上指向9月底，**具体合约日历仍以INE公告/交易端为准**。
- 夜盘安排：**未确认，以交易所当日安排为准**。
- 交割：实物；只做1–3D，不持有进入交割流程。

**期权**
- IV-RV≈+16.01 vol，事件溢价很贵；方向看多优先期货，期权只研究 bull call spread。
- `research only; manual quote and manual confirmation required before execution; no premium quoted`

### #3 M2701｜低噪声趋势多｜75

**事实**
- settle 3357，1D +0.12%，3D +0.99%，5D +4.00%，20D +7.22%，RV20 10.19%。
- OI 2,826,855，单日 +56,036（+2.02%）；volume z +1.66，OI level z +1.52。
- M2609–M2611 仍为 -0.30% contango，但 curve z **+2.54**，说明 contango 相对历史显著收紧；绝不能写成“已经 backwardation”。
- M2701 options：underlying 3357，ATM 3350，ATM IV 14.43%，RR25 +5.27，BF25 +1.485，OI coverage 97.6%，surface-ready；execution-ready=false。

**市场可能错在哪里**
- 市场可能低估的是“缓慢、低噪声的趋势与曲线收紧”，而不是一次 headline squeeze。和能化相比，它对同一地缘因子的依赖更小，适合做组合层面的因子分散。
- 反面：本次没有豆粕 physical、CBOT exact-contract 或完整进口平价闭环，所以只能是 probe，不能上升为 confirmed add-on。

**入场 / 管理**
- 首选 M2701 futures。下一可交易窗口先看真实报价与前30分钟结构。
- 参考触发：3350–3370 区间守住后再上，或有效突破3380且不是 >1% gap 后直线追价；若无回撤直接高于约3391，放弃追。
- 初始止损：首30分钟结构低点；硬失效参考 **跌破3330且下一次曲线重新显著走阔、OI转弱**。
- TP1=1R，TP2=2R；时间止损2–10D；NAV 风险 **0.35%–0.50%**。

**合约参数**
- DCE contract metadata 本次解析失败；乘数、tick、tick value、名义金额、当前保证金、涨跌停、夜盘安排、最后交易日：**参数未确认**。
- 交割与持仓规则：下单前必须按 DCE / 券商实时合约页确认；本报告不拿其他月份或旧规则补齐。
- 因参数未确认，不给一板/两板金额压力值。

**期权**
- IV-RV≈+4.24 vol，RR25 +5.27 表明上行 skew 已贵；若手工报价确认，可研究 bull call spread，用上方卖腿对冲部分 IV / skew 成本。
- `research only; manual quote and manual confirmation required before execution; no premium quoted`

## VIII. 商品期权特别部分

本次**不宣称全市场最高/最低 IV**，因为没有对 376 个 surface-ready series 做统一期限归一化排名；以下只列代表样本：

| 品种/到期 | ATM IV | RV20 | IV−RV | RR25 | Readiness | 研究结论 |
|---|---:|---:|---:|---:|---|---|
| SC2610 / 9-11 | 53.06% | 37.05% | +16.01 vol | -1.04 | surface yes / positioning no / execution no | vol很贵，期货优于裸Call |
| BU2610 / 9-23 | 39.60% | 24.64% | +14.96 | -4.84 | surface yes / positioning no / execution no | put skew贵，看多研究call spread |
| M2701 | 14.43% | 10.19% | +4.24 | +5.27 | surface yes / OI coverage97.6% / execution no | call skew贵，研究bull call spread |
| AU2610 / 9-23 | 23.44% | 21.29% | +2.14 | +3.37 | surface/positioning yes / execution no | 看空可研究put spread，避免追低 |
| EG2610 / 9-16 | 47.29% | 44.44% | +2.85 | +1.13 | surface/positioning yes / execution no | vol接近RV，但upside已偏贵 |

共同限制：bid/ask coverage=0，不能给可成交净权利金、slippage 或精确交易成本；dealer gamma direction unknown，不做 dealer Gamma 方向推断。

## IX. 21:00 风险地图（正式信息截止19:30）

> 本表只用中国 15:00 EOD + 15:00–19:30 海外信息。**不使用任何21:00后中国夜盘或海外价格。** 夜盘实际交易资格/时段若未从当日官方安排确认，则写“夜盘安排未确认”。

| 品种 | 中国EOD锚 | 19:30前海外新增 | 预期gap/方向 | 置信度 | 追价？ | 开盘后确认 |
|---|---:|---|---|---|---|---|
| **BU2610** | 4904 settle | Brent 92.21 / WTI 87.88 @18:46 | 偏正 | 中高 | **否** | 等30–45m；回踩/接受4900附近；>+2%无回撤不追 |
| **SC2610** | 637.2 | 同上，供应路线风险继续计价 | 偏正 | 高 | **否** | 等30–45m；确认接受 + 外盘不反转；roll/OI是减分项 |
| **M2701** | 3357 | 无可计独立海外豆粕 exact-contract 层 | 温和偏多 | 中 | 否 | 等15–30m；3350–3370守住或有效突破3380；关注OI/曲线延续 |
| **AU2610** | 961.04 | spot gold 4369.24、-1.8% @18:03；收益率上行 | 偏负 | 中 | **不追低** | 等30m反弹失败；若黄金/收益率反向则取消 |
| **EG2610** | 5481 | 原油偏强 | 偏正但易冲高回落 | 中 | 否 | 等45m；只做回撤再接受，不追日盘+5.5% |
| EC2610 | 1831 | — | 不推断 | 低 | — | **夜盘安排未确认；若无夜盘，下一窗口为9:00** |

BU/SC/M/AU/EG 的夜盘当日安排在本次 metadata 中未完整确认；任何条件单首先要求券商/交易所实时确认“当前可交易”。

## X. 未来24h / 7d事件

1. **9月1日 22:00 BJT JOLTS（正式19:30视角仍属未来事件）。** 本次23:39重跑不回填结果到19:30评分，避免 hindsight。对美元/收益率/贵金属和需求预期有即时冲击。
2. **9月2日 22:30 BJT：EIA Weekly Petroleum Status Report。** 对 SC/BU/FU/LU/LPG 是24h内最直接库存催化。SC/BU probe 不在数据前加到 confirmed-size；若已有盈利，优先缩敞口而不是赌单点数据。
3. **9月4日 20:30 BJT：美国8月 Employment Situation / NFP。** 影响美元、实际利率、原油需求预期、贵金属与有色；AU空头尤其需防宏观反向跳空。
4. **Hormuz / 美伊冲突与实际船舶通行：持续事件。** 对SC/BU而言，真正失效变量是“通行恢复 + 海外油价回落”，不是单一句政治表态。
5. **OPEC+：** 本次没有从可靠官方/Reuters结果确认未来7日内一个可作为主交易锚的具体决策时点，因此不沿用未经复核的“某日必有会议”假设。
6. **交易所临时提保 / 扩限：** 高波动能化环境下本身就是风险事件。下单前重读交易所和券商实时参数；提保时应降低手数，不是简单追加现金维持原杠杆。
7. **天气 / USDA / WASDE / IEA：** 本次未验证到未来24h内足以对前三候选独立计分的事件；不为凑催化而虚构事件层。

### 风险预算与压力测试

- Probe：单一候选最大 NAV 损失 **0.25%–0.75%**；本版 BU 0.40%–0.60%、SC 0.40%–0.60%、M 0.35%–0.50%、AU 0.35%–0.50%、EG 0.30%–0.45%。
- Confirmed：只有下一次价格 + 曲线 + OI/physical 继续确认，才允许单主题提升到0.75%–1.50%。
- BU+SC+EG 属同一“中东供给/能化”因子，**组合损失预算建议≤1.25%–1.50% NAV**；不能当三笔独立 alpha 各自满配。
- M 是更独立的农业趋势因子，但缺 fundamental closure，仍只给 probe。
- 极端压力：1–2个涨跌停、相关性崩溃、流动性消失、夜盘跳空、提保、IV急升/塌陷、交割挤压、人民币突变、海外在中国闭市时急转。
- execution-ready=false 时，期权只作为“定义损失的候选表达”，不直接下单。

## XI. 来源与实际数据路径

China-Commodities-Engine：
- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`
- `data/options/latest.json`
- `data/contract_meta.json`

公开来源：
1. Reuters syndication via Euronext，18:46 BJT 油价截面：https://live.euronext.com/en/financial-news/oil-around-2-renewed-us-iran-strikes-stoke-supply-fears
2. Reuters syndication via Kitco，18:03 BJT 黄金/收益率截面：https://www.kitco.com/news/off-the-wire/2026-09-01/gold-drops-over-1-treasury-yields-rise-investors-eye-us-jobs-data
3. EIA Weekly Petroleum Status Report：https://www.eia.gov/petroleum/supply/weekly/schedule.php
4. U.S. BLS September 2026 release schedule：https://www.bls.gov/schedule/2026/09_sched.htm
5. INE crude oil standard contract：https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html
6. SHFE operational rules：https://www.shfe.com.cn/eng/services/Rules/SHFERules/202512/t20251231_829981.html

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：BU2610回撤确认多、SC2610接受后做多、M2701趋势确认多、AU2610反弹失败空；全部先验证实时价格与交易参数。
C. 今天应继续观察的机会：EG2610回撤承接、MA610、I2701曲线收紧、FG701反弹，以及下一次EOD的OI/physical是否补确认。
D. 今天必须避免或退出的交易：无回撤追多日盘暴涨能化、把价涨仓减写成新增多头、在execution_ready=false时臆测期权成交成本、把SC/BU/EG当三个独立因子同时满风险。