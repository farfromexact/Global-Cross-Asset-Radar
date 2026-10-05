# 全球商品期货期权高风险机会雷达（晨间版）

- 报告日期：2026-10-06
- 生成/信息截点：2026-10-06 07:00 北京时间
- edition：`commodities_morning`
- prompt_version：`radar_2026-09-06_coverage_v1`
- data_protocol_version：`china_commodities_v2`
- 当前中国市场状态：国庆休市；最近完整交易日 2026-09-30；下一实际集合竞价 2026-10-08 08:55—09:00，日盘 09:00；下一夜盘 2026-10-08 21:00（归属 2026-10-09 交易日）
- 免责声明：research only; manual quote and manual confirmation required before execution; no premium quoted

## 一、今日一句话结论

> **截至本报告时点，无可立即执行的合格新交易。橡胶仍最接近节后触发，但原油终盘再度回吐、美元走强且国内休市，所有候选均须等 10 月 8 日重新报价。**

研究机会存在但等待条件/报价：RU2701、OI701、柴油物流溢价篮子。已分析但优势不足：BR2611、SR701、SC2611、贵金属。数据不足、暂时无法判断：国内期权执行价差、DCE 期权定位、精确进口平价及当前 USD/CNH。

## 二、数据质量、时间语义与覆盖

### 2.1 实际读取与状态

| 模块 | 路径/来源 | requested/source | generated | 读取状态 | 本期用途 |
|---|---|---:|---:|---|---|
| 统一输入 | [report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) | 2026-09-30 | 2026-10-05 19:08 BJT | ok，schema v2 | 主输入；假期重建，非实时行情 |
| Futures | 同上 + [latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json) | 2026-09-30 | 2026-10-01 08:02 | last-good verified | 806 合约、五所完整、source_date_match 100%、critical errors 0；6 个占位 OHLC 已排除 |
| 根任务状态 | [last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) | 2026-10-05 | 2026-10-05 19:02 | holiday run failed | 15 个取数错误来自非交易日刷新；不自动否定 9/30 last-good |
| Market State | report_input.products | 2026-09-30 | 2026-10-05 19:02 | last-good usable | 77 个品种已扫描；同合约 1D/3D/5D/20D、OI、curve |
| Physical | report_input.physical | 2026-09-30 | 2026-10-01 08:12 | carried_forward | 20 条目标序列；18 条沿用，SC/LU 缺失；basis 均为 C 或缺失，只作 context |
| External（日频） | report_input.external | 2026-10-05 | 2026-10-05 19:07 | fresh/validated | 17/22 序列；全部为 context_only，不构成可执行进口套利 |
| Night Session | report_input + [night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) | 最近有效 2026-09-30 | 当前假期尝试 2026-10-05 08:04 | stale/holiday-failed | 10/5 记录：trading_date=2026-10-05、night_session_date=2026-10-04、data_fresh=false、validation_passed=false、published=false、coverage_complete=false、night contracts=0、products=0；属于无应有夜盘的假期尝试，不是 10/6 夜盘 |
| Options | [quality_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) + surface | 2026-09-30 | 2026-10-01 00:03 UTC | research-ready, execution-missing | 14,468 合约、196 series；surface 192、positioning 47、execution 0；IV coverage 98.84%、OI coverage 68.88%、bid/ask coverage 0 |
| Contract metadata | report_input + [contract_meta.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json) | 2026-09-30 | 2026-10-01 | partial | contract match 67.49%、effective 73.45%；multiplier/tick/margin/limit 约 30.15%，缺项不推断 |

Night 当前尝试的质量计数：selected 806、outside_night_window 592、no_night_trade 0、missing timestamp/price/quote 0、query_error 214、unresolved_contract 214；上一有效快照保留。由于 10 月 1—7 日中国交易所休市，10 月 5 日并无应有的夜盘，故这次失败不等于最新应得 session 缺失；旧 9 月 29 日夜盘仅用于“9/30 EOD 形成过程”的历史分解，不计本期新增催化。交易日历以[上期所国庆安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)及[上期能源国庆安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833507.html)为准。

五所覆盖：SHFE、INE、DCE、CZCE、GFEX 均在 9/30 last-good；`full_market_ready=true`、`source_date_match_pct=100%`、`critical_errors=0`。当前 10/5 根任务的 `full_market_ready=false` 是假期刷新状态，不能冒充 10/5 EOD，也不推翻 9/30 last-good。

### 2.2 海外 07:00 更新

- 原油：10 月 5 日终盘 Brent 约 **100.32 美元/桶**、WTI 约 **89.43 美元/桶**，均较报告库 19:07 快照（102.44/90.31）继续回落；中东原油出口已一度高于战前水平，但油轮袭击与高运费仍在。[Reuters 油价终盘](https://www.reuters.com/business/energy/oil-climbs-after-yemeni-houthis-attack-saudi-aramco-sites-2026-10-04/)；[Reuters 中东出口与油轮风险](https://www.reuters.com/business/energy/middle-east-crude-oil-exports-exceed-pre-war-levels-tanker-attacks-increase-2026-10-05/)
- 美元/利率：10 月 5 日美元指数约升 0.2%，美国 10 年期收益率在 5.3% 上方，构成贵金属及部分工业品的逆风；当前精确 USD/CNH 未核实，因此不量化人民币贡献。[Reuters 全球市场](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-05/)
- 黄金：COMEX 10 月黄金 10 月 5 日结算约 4,128.40 美元/盎司，连续第二日回落；“黄金信用/货币贬值”方向本期没有新增价格确认。[WSJ 黄金终盘](https://www.wsj.com/finance/commodities-futures/gold-rises-as-softer-than-expected-inflation-data-tempers-rate-hike-bets-adcd6783)
- 橡胶：RTAS 官方页截至本截点最近日价仍为 10 月 2 日，未核实 10 月 5 日 SICOM 精确结算；RU 的外盘确认因此沿用且降级，不能称新增催化。[RTAS 日价](https://www.rtas.sg/rubber-prices/)

## 三、商品仪表盘（展示 12 项；全市场扫描见覆盖核对）

> EOD 均为 2026-09-30。Night 为 2026-09-29 开始、归属 9/30 交易日的旧 session，仅作历史分解；“—”表示缺失或不适用。Basis 的 C 级不进入方向评分。

| 板块 | 品种/合约 | EOD close/settle | 1D / 5D | Volume / OI / ΔOI | EOD curve | Basis/Physical | 旧 Night close | vs close / vs settle | Night ΔOI / quality | 07:00 Overseas | Options readiness | 信号 |
|---|---|---:|---:|---:|---|---|---:|---:|---|---|---|---|
| 橡胶 | RU2701 | 20,095 / 19,710 | +3.52% / +3.96% | 513,683 / 150,478 / +18,323 | RU2610>RU2611 +0.24%，轻 backwardation | basis C；实体仅沿用 | 19,665 | +3.45% / +3.28% | +11,873；historical exact，9/29 23:00 | RTAS 最新仍 10/2，未获 10/5 新价 | IV 27.94、RV20 22.25；Y/Y/N | 最强节后条件候选，不追 gap |
| 油脂 | OI701 | 10,230 / 10,217 | +1.72% / -0.25% | 272,992 / 283,749 / +9,681 | OI611>OI701 +1.82%，backwardation | 仓单 1,463，日减 40；basis C | 10,234 | +1.76% / +1.89% | +6,681；historical exact | BMD 棕榈 4,578、CBOT 豆油 70.19（19:07 repo snapshot） | IV 15.26、RV20 14.24；Y/N/N | 相对强，但仅两层支持 |
| 合成橡胶 | BR2611 | 16,000 / 15,870 | +3.12% / +6.58% | 288,172 / 51,622 / -4,127 | +1.13%，backwardation | 实体缺失 | 16,155 | +4.50% / +4.97% | +8,194；historical exact | 橡胶新价缺失；原油转弱 | IV 37.00、RV20 29.01；Y/N/N | 强势但成本端反对，降级 |
| 原油 | SC2611 | 711.0 / 696.1 | -2.90% / -2.93% | 175,510 / 24,979 / -4,690 | -0.06%，近乎平坦 | Physical missing | 705.2 | -0.94% / -1.63% | -1,162；historical exact | Brent 100.32、WTI 89.43 终盘 | IV 67.18、RV20 60.56；Y/N/N | 海外尾部仍大，但国内多头证据不足 |
| 沥青 | BU2611 | 5,013 / 5,091 | -2.00% / -0.29% | 880,746 / 155,550 / -53,419 | +12.61%，深 backwardation/roll 风险 | 实体缺失 | 5,142 | -1.98% / -1.02% | -24,314；historical exact | 原油终盘继续回吐 | surface N；execution N | 深曲线受合约/交割扭曲，不追套利 |
| 有色 | CU2611 | 109,680 / 109,570 | +0.25% / -1.03% | 69,830 / 185,404 / +183 | +0.73%，backwardation | basis C，1,843（不合格） | 109,420 | -0.14% / +0.11% | historical exact | LME Cu 14,362（19:07），美元走强 | surface Y；execution N | 内外信号冲突，等节后 |
| 贵金属 | AG2612 | 14,980 / 14,928 | +0.15% / -7.41% | 273,904 / 283,220 / +6,039 | -0.22%，轻 contango | 无有效实体层 | 14,958 | +0.74% / +0.35% | historical exact | Gold 4,128.40，美元/收益率上行 | surface Y；execution N | 5D 弱势未反转，不抄底 |
| 黑色 | I2701 | 702.5 / 704.5 | +0.43% / -0.98% | 218,646 / 552,096 / -28,979 | -0.21%，轻 contango | basis C | — | — | DCE unresolved | SGX 铁矿 91.8（19:07） | DCE options 数据不足 | 未获实体与期权确认 |
| 油脂 | P2701 | 9,581 / 9,593 | +0.23% / -2.70% | 373,884 / 546,979 / -5,820 | -0.37%，contango | basis C | — | — | DCE unresolved | BMD 棕榈 4,578（19:07） | DCE options 数据不足 | 弱于 OI，暂不交易 |
| 聚酯 | TA701 | 6,300 / 6,268 | +0.22% / +0.10% | 1,191,682 / 1,016,989 / -69,523 | +5.35%，backwardation | basis C | 6,306 | -0.69% / +0.83% | -30,011；historical exact | 原油下跌但物流风险仍在 | surface Y；execution N | close/settle 锚分歧大，等 45 分钟 |
| 软商品 | SR701 | 5,354 / 5,336 | -0.15% / -0.15% | 302,888 / 564,277 / -12,444 | -2.77%，contango | 仓单 26,313，日减 779；basis C | 5,341 | +0.24% / -0.06% | +744；historical exact | ICE sugar 20.20（19:07） | IV 10.36、RV20 6.97；Y/Y/N | 外强内弱研究问题，非套利 |
| 航运 | EC2611 | 2,794 / 2,823.5 | -1.67% / +7.62% | 13,089 / 22,057 / -2,569 | -26.12%，仅 2 个观测/交割月扭曲 | 无 | 不适用 | 不适用 | 无夜盘 | 中东出口恢复、油轮袭击仍多 | 无执行面 | 曲线不可当套利，避免追逐 |

## 四、相比上一期真正变化与旧建议台账

1. **中国层没有新增 EOD 或夜盘。** 10/5 晚报后的所有国内价量、曲线、仓单均仍是 9/30 last-good；本期新增仅是 10/5 海外终盘与假期日历确认。任何国内方向分数均未因“时间经过”上调。
2. **原油尾部溢价再收缩。** Brent/WTI 终盘降至约 100.32/89.43，低于 19:07 repo 快照；中东出口恢复是最强竞争解释，反对立即做多 SC。油轮袭击、运费与炼化物流约束仍支持柴油相对原油的 RV 研究，但不支持无报价追价。
3. **美元与长端收益率走强，黄金回落。** 黄金信用主题本期未获新增确认；AU/AG 不进入正式榜。
4. **RU 外盘确认未刷新。** RTAS 最新仍停在 10/2，RU2701 排名和触发不变；节后若高开超过 20,500，赔率恶化，放弃追涨。
5. **BR 由 62 降至 60。** 变更原因是价格变化：原油成本端转弱，而外盘橡胶未新增确认；不是方向反转。
6. **柴油物流篮子由 61 升至 62。** 变更原因是新增 Reuters 物流证据，但仍缺同一时点可成交报价、保证金和滑点，执行状态仍为待报价。

| idea_id | 首次提出 | 上次状态 | 当前状态 | 变更原因/旧建议处置 |
|---|---:|---|---|---|
| COM-E-RU2701-RUBBER-TIGHTNESS-20261001 | 2026-10-01 | 75，休市等待 | 75，休市等待 10/8 触发 | 无新橡胶结算；原触发/失效/目标不重置 |
| COM-E-OI701-RELSTRENGTH-20260930 | 2026-09-30 | 65，休市等待 | 65，休市等待 | 无国内新增；维持 |
| COM-E-DIESEL-LOGISTICS-20261005 | 2026-10-05 | 61，待报价 | 62，待报价 | 新增物流/油轮风险证据；原油绝对价格下跌抵消部分逻辑 |
| COM-E-BR2611-RELSTRENGTH-20260930 | 2026-09-30 | 62，休市等待 | 60，休市等待 | 原油成本端弱化；无橡胶新价 |
| COM-SR-DIVERGENCE-20260930 | 2026-09-30 | 59，研究观察 | 59，研究观察 | 无新增 |
| COM-FU-SC-SPREAD-20260930 | 2026-09-30 | 已取消 | 继续取消 | 合约错配与物流因子不足；不得恢复为条件单 |

未收到成交反馈，不假设用户持仓；若此前按条件建立，因中国休市也不能用本报告声称已减仓或退出。

## 五、产业链地图

| 产业链 | 方向/强弱 | EOD 与旧 Night | Curve/实体 | 海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 天然橡胶—合成橡胶 | **最强：RU 条件多；BR 次之** | RU EOD 价涨仓增线索，旧夜盘已完成大部分上行；BR 强但 EOD 减仓 | 两者轻 backwardation；实体为沿用 | 橡胶外盘 10/5 未核实；RU IV>RV | 当前 SICOM 精确价、国内开盘报价 | 中 |
| 原油—炼化—物流 | **绝对油价偏弱，柴油物流 RV 偏强** | SC 9/30 弱、BU 减仓大 | SC 近乎平坦；BU 深 back 受 roll 扭曲 | Brent/WTI 下跌；SC/BR IV 较 RV 偏贵 | 同时点 gasoil/Brent bid-ask、运费曲线 | 中低 |
| 油脂—饲料 | OI 相对最强，P 次弱 | OI 价涨仓增线索；DCE Night 缺失 | OI backwardation + 仓单小降；P contango | BMD/CBOT 仅 repo 19:07 快照 | 节后现货基差 A/B、DCE 期权 | 中低 |
| 有色—贵金属 | 震荡偏弱 | CU 近中性；AG 5D 明显弱 | CU 小幅 back，实体 basis C | 美元/收益率上行、黄金回落 | 当前 USD/CNH、LME 终盘与可比库存 | 低 |
| 黑色—建材—新能源 | **最弱：缺新增实体确认** | I/FG/LC 等 5D 偏弱或去仓 | 多数 basis C；LC 5D -10.77% 但无执行期权 | 海外映射不完整 | 节后需求、库存、DCE 期权、碳酸锂实体 | 低 |

Regime：**中国长假休市 + 海外原油事件溢价回吐 + 物流风险残留 + 美元/收益率偏强 + 国内 last-good 分化。**

固定问题答复：EOD 仅 RU/OI 的价格得到曲线部分确认；旧 Night 强化 RU/BR、仅重复 OI、否定/削弱 SC，但均非本期新证据。Night 相对 close 与 settlement 的显著分歧主要见 TA（-0.69% vs +0.83%）和 SR（+0.24% vs -0.06%），说明结算锚不能替代新增信息。无当前 Night curve，不能判断 10/6 曲线确认。库存/实体只部分确认 OI/SR 仓单变化；境内外目前非同一时点，人民币作用不可量化。期权均无 execution readiness，不优于可核验的线性工具。没有达到 exact-contract/import-parity 标准的跨市场套利；柴油篮子仅是研究 RV。BU/EC 深曲线、OP/AD roll、单日大幅去仓多属交割/换月噪音。节后 RU/BR/TA 等 45 分钟，OI 30 分钟，SC/贵金属至少 30—45 分钟。不值得交易：追高 RU/BR、抄底 AG、把 EC 深 contango 当无风险套利、以 C 级 basis 建仓。

## 六、机会排行榜（研究吸引力；最多 5 项）

> 权重：逻辑 25、赔率凸性 25、催化 20、价格/曲线/波动率 15、拥挤持仓技术 15。分数仅用于排序，不是胜率、收益或仓位指令。

| 排名 | idea_id / 方向 / 周期 | 分项与总分 | 有效独立支持层 | 研究判断 / 证据 / 执行 | 工具与最大损失 | 最强反证/缺失 |
|---:|---|---:|---|---|---|---|
| 1 | COM-E-RU2701-RUBBER-TIGHTNESS-20261001；多；2—10D | 22+16+16+13+8=**75** | 4：价量持仓、curve、实体沿用、外盘沿用 | 存在待验证优势 / 部分 / 休市等待触发 | RU2701；期货损失不由结构限定 | 外盘 10/5 未核实；节后高开已定价；IV 不便宜 |
| 2 | COM-E-OI701-RELSTRENGTH-20260930；多；3—15D | 19+14+11+11+10=**65** | 2：价量持仓、curve/仓单 | 存在待验证优势 / 部分 / 休市等待触发 | OI701；期货损失不由结构限定 | 5D 未转强、外盘映射非 exact、basis C |
| 3 | COM-E-DIESEL-LOGISTICS-20261005；多柴油/空 Brent；1—7D | 20+12+15+9+6=**62** | 2：海外价格、物流/实体 | 存在待验证优势 / 部分 / 待报价与参数 | ICE Gasoil Nov-26 vs Brent Dec-26；损失不限定 | 中东出口恢复；无同刻 bid/ask、保证金、运费曲线 |
| 4 | COM-E-BR2611-RELSTRENGTH-20260930；多；2—8D | 18+13+11+8+10=**60** | 2：价量/曲线、外盘橡胶沿用 | 存在待验证优势 / 部分 / 休市等待 | BR2611；期货损失不限定 | 原油转弱、EOD 减仓、短到期 IV 偏贵 |
| 5 | COM-SR-DIVERGENCE-20260930；观察内外分化；3—10D | 17+12+13+8+9=**59** | 1：外盘/仓单合并后仅一层有效 | 证据不足 / 不足 / 研究观察 | SR701 或期权结构待报价 | 国内 contango、价格不强、非 exact parity |

无 80+ 项；仅 RU 达到 70+ 研究门槛，但休市、实时外盘与国内报价缺失，不能转化为立即新仓。

## 七、前三名交易卡

### 7.1 RU2701：节后回踩确认后做多（排名 1，非当前条件单）

- **事实**：9/30 close/settle=20,095/19,710；1D +3.52%，5D +3.96%；OI +18,323。旧 Night OHLC=19,125/19,730/19,090/19,665，vs close +3.45%、vs settlement +3.28%，Night ΔOI +11,873。旧夜盘已完成大部分信息吸收。
- **市场定价**：RU 轻 backwardation，9/30 期权 ATM IV 27.94% 对 RV20 22.25%（+5.69 vol），上行尾部并不便宜。
- **分歧与错价假设**：市场可能低估供给扰动的持续性，但也可能已经通过 9/30 gap 和 IV 完成定价。新增证据缺失，所以只买“节后回踩仍强”，不买预期。
- **五层**：支持①价量持仓、②曲线、③实体 last-good、④外盘 last-good；反对⑤期权偏贵且无报价。Night 不另算层。
- **最佳表达**：RU2701 单腿多，腿比 1:0；期权备选为 2026-12-25 到期 0.35—0.45 Delta 买 Call / 0.15—0.25 Delta 卖 Call 的 1×1 call spread，但 execution_ready=false，未核价前不得下单。
- **入场/分批**：仅在 10/8 09:45 后，20,000—20,200 回踩持稳且近月结构未明显收窄；40%/30%/30%。高开 >20,500 或 45 分钟内不能收复 20,000 则放弃。
- **止损/失效**：30 分钟收在 19,600 下方，或 SICOM 同步转弱且 RU curve 转 contango。TP1 20,750，TP2 21,400；2 个交易日无扩张则时间止损。
- **好/中/坏成交**：20,020/20,100/20,200；以 19,600 为计划止损，TP1 约 1.74R/1.30R/0.92R，TP2 约 3.29R/2.60R/2.00R；滑点与 gap 可使实际损失超过计划值。
- **合约参数**：常规规格按 10 吨/手、最小跳 5 元/吨、tick value 50 元；9/30 名义约 200,950 元/手。国庆安排确认 9% 涨跌停、11% 一般保证金；夜盘 21:00—23:00，10/8 21:00 恢复。仓库 last trading day=2027-01-15、last delivery=2027-01-19；12 月中下旬前随流动性迁移换月，严禁进入交割月。参数开盘前仍需交易所/经纪商复核。[上期所 RU 合约](https://www.shfe.com.cn/products/futures/ru/standard/)
- **压力损失**：按 19,710 settle、10 吨、9% 限幅，一板约 17,739 元/手；两板复合约 37,070 元/手。期货最大损失不由止损结构限定。
- **风险预算**：仅试仓，计划止损损失≤NAV 0.50%；与 BR/轮胎链同因子合并≤1.0%。最坏情景为假期海外橡胶转弱、国内补跌和流动性跳空。

### 7.2 OI701：节后相对强度确认（排名 2，非当前条件单）

- **事实**：9/30 close/settle=10,230/10,217；1D +1.72%、5D -0.25%；OI +9,681。近月对 701 backwardation 1.82%；仓单 1,463、日减 40。旧 Night close 10,234，vs close +1.76%、vs settle +1.89%，ΔOI +6,681。
- **市场定价/分歧**：市场已计入部分节前补库和近端紧张，但 5D 未转强。分歧是曲线强度能否在节后现货成交中延续；仓单小降不足以单独证明短缺。
- **五层**：支持①价格/OI，②curve/仓单；中性④BMD/CBOT context；缺失③高质量 basis，反对⑤期权执行面缺失。
- **最佳表达**：OI701 单腿多，腿比 1:0；或 12/11 到期 0.35—0.45 Delta / 0.15—0.25 Delta 的 1×1 call spread，仅待报价研究。ATM IV 15.26%、RV20 14.24%，并非明显便宜。
- **入场/分批**：10/8 09:45 后 10,120—10,220 回踩持稳，且 backwardation >1.5%；40%/30%/30%。高开 >10,350 不追。
- **止损/失效**：30 分钟收于 10,020 下方，或 curve <0.8%、仓单/现货反向。TP1 10,480、TP2 10,700；3 个交易日不扩张退出。
- **好/中/坏成交**：10,140/10,180/10,220；止损 10,020，TP1 约 2.83R/1.88R/1.30R，TP2 约 4.67R/3.25R/2.40R。
- **合约参数**：仓库确认 10 吨/手、tick 1 元/吨、tick value 10 元、保证金 9%、涨跌停 8%；名义约 102,300 元/手；夜盘 21:00—23:00；last trading day=2027-01-14、last delivery=2027-01-19。12 月中旬前评估换月，避免交割。[郑商所 OI 合约](https://english.czce.com.cn/en/index.htm)
- **压力损失**：一板约 8,174 元/手；两板复合约 17,000 元/手。最大损失不由结构限定。
- **风险预算**：试仓≤NAV 0.35%；与 P/Y/RM/M 同因子合并≤1.0%。最坏情景为油脂外盘假期回落、国内现货不跟、curve 快速走平。

### 7.3 ICE 柴油物流篮子：多 Gasoil / 空 Brent（排名 3，待报价研究卡）

- **合约与定义**：多 5 手 ICE Low Sulphur Gasoil Nov-2026，空 7 手 ICE Brent Dec-2026。以 gasoil 100 吨/手、Brent 1,000 桶/手的常规规格，篮子美元 P&L=`500×ΔGasoil(美元/吨)−7,000×ΔBrent(美元/桶)`。5:7 旨在接近 10/5 19:07 快照的**美元名义中性**，不是 Beta 中性、裂解收益率中性或质量中性；实时名义须重算。
- **事实/定价**：Reuters 报道中东出口恢复、Brent/WTI 终盘回落，反对绝对油价追多；同时油轮袭击和运费高企支持产品物流溢价。市场隐含供给流量恢复，但未必完全定价运输摩擦。
- **五层**：支持④海外相对价格，③物流实体；缺失①同一时点可成交价，②精确期限/运费曲线，⑤期权面。证据仅部分。
- **入场/分批**：下一流动性充足的欧洲/美洲时段，先取得两腿实时 bid/ask 与保证金；15 分钟后篮子相对同步中价上破 1%，且 Brent 不同步大涨，40%/30%/30%。任何一腿滑点 >0.25% 或无法同步成交即放弃。
- **止损/失效/退出**：篮子中价较成交下跌 0.75%，或确认油轮费率/延误快速正常化；TP1 +1.5%、TP2 +3%，两场交易时段未扩张退出。先平流动性差的一腿，再同步对冲残余 Delta。
- **好/中/坏成交**：总滑点≤0.10% / 0.10—0.25% / >0.25%；坏成交直接放弃。因缺实时两腿报价，不编净 R、胜率或期望收益。
- **参数与交割**：gasoil 常规合约 100 吨、tick 0.25 美元/吨（25 美元/手）；Brent 1,000 桶、tick 0.01 美元/桶（10 美元/手）。保证金、最后交易日和交割安排未在中国引擎确认，必须在 ICE/经纪商端核对；至少在到期前 5 个营业日滚动。无涨跌停，可能出现极端 gap、保证金上调和两腿相关性破裂。
- **最大损失/风险预算**：不是有限风险结构；计划止损≤NAV 0.25%，但断市/错腿可显著超出。最坏情景是 Brent 因供应冲击急涨而 gasoil 因需求/炼厂恢复不跟。

## 八、商品期权专项

期权截面为 **2026-09-30 最新有效 T-1/last-good**，假期无新增；夜盘后 moneyness 已在 9/30 EOD 收敛，但执行仍需重新核验。全局 chain available；surface_ready 192/196、positioning_ready 47/196、execution_ready 0/196，dealer gamma 方向未知，禁止推断做市商净 Gamma。

| underlying / expiry | ATM IV / RV20 / spread | RR25 / BF25 | readiness S/P/E | 研究结论 |
|---|---:|---:|---|---|
| RU2701 / 2026-12-25 | 27.94 / 22.25 / +5.69 vol | +1.91 / +0.24 | Y/Y/N | 上偏度正，call 不便宜；仅限价 call spread 待报价 |
| OI701 / 2026-12-11 | 15.26 / 14.24 / +1.02 | +3.92 / +0.64 | Y/N/N | 小幅 IV 溢价，positioning 不完整 |
| BR2611 / 2026-10-26 | 37.00 / 29.01 / +8.00 | -1.36 / -0.35 | Y/N/N | 短到期且 IV 高，避免追买单腿 gamma |
| SC2611 / 2026-10-14 | 67.18 / 60.56 / +6.61 | -2.58 / +2.53 | Y/N/N | 事件凸性昂贵；只研究定义损失的 put/call spread |
| SR701 / 2026-12-11 | 10.36 / 6.97 / +3.39 | +3.01 / +1.34 | Y/Y/N | 内外分化尚不足以证明 vol 错价 |

IV-RV 为同日模型估计，不代表期权“便宜/贵”的充分证据。没有 bid/ask coverage，禁止写权利金、净成本、滑点或精确 Greeks。回避：BR/SC 短到期追买波动、任何裸卖事件尾部、把 OI/PCR 当机构方向。Vol RV 仅保留 RU/BR、SC/BU 的跨品种研究，因到期、标的和事件暴露不一致，当前不可执行。

## 九、9:00 开盘风险地图

**今天中国休市，没有 9:00 开盘。** 下一实际窗口为 2026-10-08 08:55—09:00 集合竞价、09:00 日盘；下表只是截至 10/6 07:00 的预案，10/8 08:45 必须刷新海外价格、人民币和交易所参数，不得把它当作届时有效条件单。

严格三层：
1. Previous China EOD：2026-09-30；
2. Current Trading Day Night Session：不存在；10/5 假期尝试不合法作行情，9/29 Night 只作历史；
3. 07:00 Overseas：原油终盘下跌、美元/收益率偏强、黄金回落，橡胶精确新价缺失。

| 品种 | 10/8 初步 gap 偏向 | 是否已在旧 Night 定价 | 内外冲突 | 首跳追价 | 等待 | 开盘确认 |
|---|---|---|---|---|---:|---|
| RU2701 | 平/偏高但不确定 | 9/30 上行大部已定价 | 橡胶外盘新价缺失 | 否 | 45m | 20,000、近月结构、SICOM 同步 |
| OI701 | 平开为主 | 旧 Night 部分定价 | 油脂海外仅旧快照 | 否 | 30m | 10,120—10,220、backwardation>1.5% |
| BR2611 | 平/偏低 | 旧 Night 强，EOD 未全跟 | 原油弱、橡胶未知 | 否 | 45m | 15,450/16,050、RU/BR 相对强弱 |
| SC2611 | 偏低 | 旧 Night 曾弱 | 与 9/30 EOD 同向偏弱 | 否 | 30m | Brent 最新、人民币、SC curve |
| BU/TA | 偏低但可能被物流抵消 | 锚点分歧大 | 原油跌 vs 产品物流紧 | 否 | 45m | 裂解/加工差、近远月、成交量 |
| CU/AG | 平/偏低 | 旧 Night 信息过时 | 美元/利率偏空 | 否 | 30—45m | DXY、USD/CNH、LME/COMEX |
| I/P | 平开不确定 | DCE old Night 缺失 | 海外只作 proxy | 否 | 30m | exact contract、现货/基差、OI |
| EC | 不判断 | 无夜盘 | 物流风险双向 | 否 | 45m | 运价指数、舱位与近月成交 |

外盘与旧 China Night 不在同一事件窗口，不能计算当前信息弹性。10/8 若外盘累计变动已被集合竞价一次性反映，应避免首跳；RU/BR/TA 等至少等 45 分钟，SC/CU/OI 30 分钟。

## 十、未来 24h / 7d 事件日历（北京时间）

| 时间 | 事件 | 影响路径 | 处理 |
|---|---|---|---|
| 2026-10-06（官方发布日期，具体时刻待核） | [EIA 10 月 STEO / Winter Fuels Outlook](https://www.eia.gov/outlooks/steo/release_schedule.php) | 原油/成品油平衡、库存与冬季需求 | 海外 Delta 先降；无当前中国盘，不将发布前假设当事实 |
| 2026-10-07 22:30（常规窗口，以官网最终为准） | [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/schedule.php) | SC/BU/TA/柴油裂解 | 节后前一夜；用有限风险或等数据后 15 分钟 |
| 2026-10-08 08:55/09:00 | 中国期货节后集合竞价/日盘重开 | 两日海外累计 gap、保证金与流动性 | 所有国内候选延迟 30—45 分钟；单一试仓≤NAV 0.25%—0.50% |
| 2026-10-08 21:00 | 中国夜盘恢复（归属 10/9） | 第二轮价格发现 | 不把 9/30 Night 当替代；重新核验 exact contract |
| 2026-10-10 00:00 | [USDA WASDE（10/9 12:00 ET）](https://usda.azureedge.us/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report) | 谷物、油脂、棉花、糖的供需预期 | 农产品 Delta 降半；期权只用定义损失结构且须有实时报价 |
| 2026-10-10 03:30（常规时刻） | [CFTC COT 周报](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) | 海外拥挤度，非国内机构方向 | 只作后验定位，不用来解释当日资金身份 |
| 未来 7 日持续 | 中东油轮安全、运费、港口/炼厂运行；东南亚橡胶天气 | 原油绝对价与柴油/橡胶相对价 | 事件跳空优先有限凸性；无报价则等待，不卖裸尾部 |

OPEC+/IEA 在本报告可核实的未来 7 日内没有确认的新增定时会议/报告；若临时事件出现，必须按实际发布日期重新评估，不能预设。天气、矿山、油田、炼厂与交易所参数若无官方时点，不编造催化时间。

## 十一、覆盖核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足 | 未入榜最值得跟踪的异常/无异常依据 |
|---|---:|---:|---|---|
| 黑色建材 | 10：I/JM/J/RB/HC/FG/SA/SF/SM/WR | 10 | DCE Night/Options；basis 多为 C | FG 5D -3.65%、ΔOI -7.12%；SF ΔOI -10.47%，均缺 curve/实体共振 |
| 有色贵金属 | 14：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG/PD/PT | 14 | 当前 LME 终盘、USD/CNH；部分新代码历史短 | AO ΔOI -18.82%、AD roll ΔOI +13.9%；AG 5D -7.41% 但 OI 增，冲突 |
| 能源炼化化工 | 26：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP/EC/BZ/OP/ZC/PL | 26 | SC/LU Physical；精确 gasoil/Brent 同刻报价 | BU ΔOI -25.56%、深 back；OP ΔOI +44% 且 OI z=3.32，明显 roll；PX ΔOI -18.45% |
| 新能源 | 3：LC/SI/PS | 3 | LC 实体与执行期权 | LC 5D -10.77%，但无实体/波动率确认，不抄底 |
| 农产品油脂饲料畜牧 | 14：A/B/M/RM/Y/P/OI/C/CS/LH/JD/LG/RR/RS | 14 | DCE Options；A/B 级 basis 缺失 | LG ΔOI -25.06%、B -8.11%、CS -8.04%，更像去杠杆线索 |
| 航运软商品 | 10：EC/CF/CY/SR/AP/CJ/PK/PM/RI/WH | 10 | EC 运价/舱位实时；多品种无有效期权 | AP 1D -1.75%、5D -3.15%、curve +9.38%；PK ΔOI -14.31%，未获实体确认 |
| **合计** | 原要求 63 个不同代码 + 动态新增；引擎实际 77 | **77/77 futures/market-state 已分析** | Options 成功 42/64 产品、22 缺失/失败；execution 0 | 没有因未入榜而跳过板块 |

策略类别：方向、跨期/curve、基差、跨品种、跨市场、波动率/偏度、事件凸性均完成扫描；可执行 exact RV 为 0。周期：1D/3D/5D/20D 在同合约可得处均检查；短历史品种不编 z-score。数据不足不缩小应覆盖：无当前中国 EOD/Night、DCE 期权安全拒绝、0 bid/ask、basis 质量 C、import parity 口径不全、当前 USD/CNH 与 10/5 橡胶精确结算缺失。无夜盘品种和假期 session 属不适用，不视为错误。

风险预算：单一试仓最大损失 NAV 0.25%—0.75%；确认交易 0.75%—1.50%；单一高确信主题总风险≤2.5%—3.0%，同因子合并。压力测试覆盖一/两板、相关性破裂、流动性消失、gap、保证金上调、IV 跳升/塌陷、交割挤压、人民币急变及中国休市时海外大波动。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：无；RU2701、OI701 的 10 月 8 日方案不是今日有效条件单，须节后重新报价确认。
C. 今天应继续观察的机会：RU2701 回踩强度、OI701 backwardation、柴油物流篮子实时价差、BR2611 与原油成本端背离。
D. 今天必须避免或退出的交易：追高 RU/BR、抄底 AG、裸卖 SC/BR 短到期期权、把 BU/EC 深曲线或 C 级 basis 当可执行套利；若此前误按旧条件建立，待市场重开后优先核验而非假设持有。