# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-29

`prompt_version=radar_2026-09-06_coverage_v1` · `data_protocol_version=china_commodities_v2`

**实际生成/信息截点：2026-09-29 07:08 北京时间。最近完整中国 EOD：2026-09-28；下一实际交易窗口：2026-09-29 09:00 日盘。**

## 一、今日一句话结论

> **截至本报告时点，无可立即执行的合格新交易；贵金属空头逻辑获海外与夜盘主力回退价确认，但边际弹性下降，09:00 不追价。**

最接近触发的是 AG2612 失败反弹空、EC2611 回撤接受多、FU2611 回撤接受多；三者分别缺少当前精确夜盘 OHLC/曲线、最新运价确认、精确夜盘合约报价，因此都只能等待日盘触发。当前 regime 是“节前保证金上调前的高波动分化”：EC 是 9 月 28 日 EOD 最强，贵金属与锂链最弱；昨夜主力回退价显示贵金属、SC 继续走弱，但能源外盘与内盘原油出现冲突。

## 二、数据质量与覆盖

- 仓库统一输入：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)，`requested_date=2026-09-28`，`generated_at=2026-09-28T19:08:35.691959+08:00`，schema v2。Futures/Market State/Physical/External/Options 均更新到 9 月 28 日；五所、806 个合约、77 个品种，`full_market_ready=true`、`source_date_match_pct=100%`、核心 critical errors=0。4 个占位记录已从异常排序剔除。
- Futures：9 月 28 日 18:59 生成，fresh；五所 source date 一致。Market State 同快照；个别历史起点为 8 月 31 日不等于当日记录过时。
- Physical：9 月 28 日 19:08 生成，fresh/validated/published；20 个目标中 18 个可用，SC、LU 无可用现货行。可用现货均为 C 级 basis/context，缺地区、品质、含税和交割地对齐，**不进入方向评分或套利确认**。
- External：9 月 28 日 19:08 生成，fresh/validated/published；17/22 条日频序列可用、全部 `context_only`。缺 Dubai/Oman、Singapore HSFO/VLSFO、DXY、USD/CNH；后两项以公开实时代理单列补充，绝不冒充仓库序列。
- Night Session：统一输入内嵌快照仍是 `requested_date=2026-09-24/source_date=2026-09-23/generated_at=2026-09-24T06:03:12+08:00`；模块状态文件虽较新，却仅记录周日尝试：`trading_date=2026-09-28`、`night_session_date=2026-09-27`、`generated_at=2026-09-28T08:00:49.778056+08:00`，`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`、night contracts/products=0/0，outside-window=592、query_error=214、unresolved=214，warning 为“214 concrete contracts are unresolved”。它与昨晚归属 9 月 29 日的实际连续交易**无关**，本期不得使用。
- Night fallback：截至 02:30 的公开主力合约收盘仅确认沪金 898、沪银 14,930、SC 原油 712；没有精确合约 OHLC、完整 OI、近次月曲线，故 `night_session_fallback_used=true`，只作主力映射和第 1 层方向证据，不据此拼造 Night curve。[来源：格隆汇，2026-09-29 02:30](https://www.gelonghui.com/live/2692613)
- Options：9 月 28 日 14,716 条、206 个 series；202 个 surface-ready、52 个 positioning-ready、0 个 execution-ready，IV coverage 99.02%、OI coverage 69.05%、bid/ask coverage 0。全局 `surface_latest.json` 是 empty（0 bytes），但统一输入内 202 个具体 series 的 IV/skew 字段可作 T-1 研究；任何结构仍须 09:00 后核验 bid/ask、净权利金和滑点。
- Contract metadata：覆盖质量 partial；合约匹配 67.49%、有效匹配 73.45%，multiplier/tick/margin/limit 覆盖 30.15%，Night 参数覆盖 0。AG/FU/EC 的日期由仓库确认，静态规格和节日动态参数另以交易所规则核验；未确认项明确保留缺口。

## 三、商品仪表盘（展示 10 项；实际扫描 77 个品种）

`1D` 为 close/pre-settle；`5D` 为同合约结算收益；曲线为 EOD near-next 百分比，正值=backwardation、负值=contango。`—` 表示缺失而非 0。

| 板块 | 品种/主力 | EOD close/settle | 1D / 5D | Volume / OI / ΔOI | EOD curve | Basis / Physical | Night close；vs close / vs settle；ΔOI | Night quality/time | 07:00 overseas | Options readiness | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|---|
| 贵金属 | AG2612 | 14,985 / 15,178 | -5.01% / -5.75% | 158,226 / 262,261 / +15,563 | -0.185% contango | 无合格 basis；Physical 缺 | 14,930；-0.37% / -1.63%；OI 网页快照 +9,084、未与仓库校验 | 主力回退；02:30 | 银 60.76，-5.44%；DXY 101.14，约持平 | S/P/E=Y/N/N；IV 38.46，IV-RV +4.53 | 空头续行但新增弹性低，等 30 分钟 |
| 贵金属 | AU2612 | 904.66 / 912.06 | -2.86% / -3.61% | 150,703 / 226,497 / +4,291 | -0.035% contango | 无合格 basis | 898；-0.74% / -1.54%；— | 主力回退；02:30 | 金 4,122.96，-3.78% | Y/Y/N；IV 23.10，IV-RV +4.23 | 弱势确认，不追空 |
| 能源 | SC2611 | 727.3 / 734.1 | +0.34% / -2.69% | 102,089 / 32,410 / -3,412 | +0.899% back | Physical unavailable | 712；-2.10% / -3.01%；— | 主力回退；02:30 | WTI 93.29，-0.01%；Brent 105.85，+1.46% | Y/N/N；旧 ATM730 IV 74.90 | 内外冲突；等 30–45 分钟 |
| 能源 | FU2611 | 4,418 / 4,390 | +3.78% / +3.08% | 479,456 / 169,653 / -5,127 | +19.36% back | C级 spot context | — | 当前精确夜盘缺失 | Brent +1.46%，但无 HSFO exact | Y/N/N；IV 69.78，IV-RV +30.50 | 多头赔率被高 IV 和缺价削弱 |
| 航运 | EC2611 | 2,937.5 / 2,905.5 | +6.92% / +12.27% | 23,009 / 25,466 / +6,073 | +23.72% back | 无可用 Physical | 无夜盘制度 | N/A | 最新 exact 运价增量缺失 | 无 execution-ready series | EOD 最强；只买回撤接受，不追 |
| 黑色建材 | FG701 | 893 / 896 | -2.83% / -1.75% | 1,065,406 / 1,246,772 / +89,832 | +3.964% back | C级 spot；仓单175、Δ0 | — | 当前精确夜盘缺失 | 无 exact 海外映射 | Y/Y/N；IV 24.41，IV-RV -1.71 | 价跌仓增，但 back 反证空头 |
| 新能源 | LC2701 | 119,040 / 120,820 | -5.69% / -5.95% | 250,102 / 424,087 / -5,315 | +0.889% back | C级 spot；仓单停在9/1且 stale | 无夜盘制度 | N/A | 无 exact 海外映射 | Y/N/N；IV 46.48，IV-RV +7.27 | 跌势强但仓单过时，拒绝追空 |
| 黑色原料 | JM2701 | 1,457.5 / 1,452 | -2.44% / -4.91% | 460,640 / 416,427 / +5,216 | +0.216% back | C级 spot context | — | 当前 exact 主力夜盘缺失 | 无 exact 海外映射 | DCE 期权本期 skipped | 弱势观察；缺夜盘确认 |
| 有色 | CU2611 | 109,440 / 109,430 | -0.70% / +0.24% | 66,988 / 185,247 / +6,657 | +0.484% back | C级 spot context | — | 当前精确夜盘缺失 | COMEX 铜 6.615，-2.23%；CNH 6.7153、人民币略强 | 具体 series 未入重点 | 低开风险；等 30 分钟 |
| 畜牧 | LH2611 | 10,295 / 10,400 | -4.01% / -6.35% | 181,731 / 189,621 / -14,144 | -8.491% contango | Physical 未覆盖 | 无夜盘制度 | N/A | 无 exact 外盘映射 | DCE 期权本期 skipped | 跌势伴减仓，追空赔率差 |

海外口径：WTI 9 月 28 日结算历史价 93.29、-0.01%（[Investing](https://www.investing.com/commodities/crude-oil-historical-data)）；Brent 105.85、+1.46%（[Trading Economics](https://tradingeconomics.com/commodity/brent-crude-oil)）；黄金 4,122.96、-3.78%（[Trading Economics](https://tradingeconomics.com/commodity/gold)）；白银 60.76、-5.44%（[Trading Economics](https://tradingeconomics.com/commodity/silver)）；铜、谷物等为 9 月 28 日 20:09 海外快照（[COMEX Live](https://comexlive.org/page/12/)）；DXY 与 USD/CNH 为公开代理，分别约 101.14 与 6.7153，人民币较前收 6.7227 略强（[DXY](https://www.investing.com/indices/usdollar-historical-data)、[USD/CNH](https://www.investing.com/currencies/usd-cnh-historical-data)）。

## 四、相比上一期真正变化

1. **T-1 EOD：EC 由观察跃升为全市场最强。** EC2611 close +6.92%、5D +12.27%，OI 单日 +31.3%，backwardation 23.72%；这是价格—持仓与曲线同向，但没有最新运价/船期确认，仍不足以追涨。
2. **T-1 EOD：贵金属与锂链转为最弱。** AG2612 -5.01%、AU2612 -2.86%、LC2701 -5.69%；AG 价跌仓增只能称归因线索，不能断言“新空”。
3. **T Night：公开主力回退价继续压低 AU/AG/SC，但边际弹性不同。** AG 相对 EOD close 仅再跌 0.37%，却相对 settle 跌 1.63%；这说明 headline 看似更弱，新增信息弹性实际有限，09:00 追空赔率下降。SC 相对 close 再跌约 2.10%，夜盘重新定价更充分。
4. **海外冲突扩大。** COMEX 金银与铜显著下跌，支持境内贵金属/铜低开；但 Brent 日频仍 +1.46%，SC 主力回退价却相对 EOD close -2.10%，能源链不能用单一外盘方向解释。
5. **Options 从旧档升级至 9 月 28 日有效 T-1 截面。** 具体 series 的 IV/skew 可研究，但 bid/ask coverage 仍为 0；SC 夜盘标的已离开旧 ATM730，moneyness 可比性显著下降。
6. **风险参数发生实质变化。** AG2612 当前维持 20% 涨跌停、一般保证金 22%；FU2611 9 月 29 日日盘前按 18%/20%，当日结算后上调到 20%/22%。这不是观点变化，而是节前交易所参数变化。[上期所通知，2026-09-21](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)

### 旧建议台账

| idea_id | 首次提出 | 上次状态 | 当前状态 | 变更原因/旧建议处置 |
|---|---|---|---|---|
| COM-E-AG2612-DOWNSIDE-20260928 | 9/28 晚报 | 等 21:30 失败反弹空 | 继续；改为 09:30 后条件单，72分 | 新数据：外盘与主力回退价支持；价格已下移、赔率略降。21:30 是否触发未知；无成交反馈，不假设持仓 |
| COM-E-FU2611-ENERGY-20260928 | 9/28 晚报 | 等 21:30 回撤接受多 | 降为观察，65分 | 夜盘 exact-contract 缺失；Brent 支持但 FU 日盘价涨仓减、高 IV 反对。旧条件窗口已过期，不沿用为当前订单 |
| COM-E-EC2611-ROLL-20260924 | 9/24 | 回撤接受多 | 继续等待 09:45，69分 | 价格/OI/curve 强化，但最新实体运价缺失；不抬高追价位 |
| COM-E-BR2611-REVERSAL-20260923 | 9/23 | 9/28 09:45 回撤多 | 退出正式榜 | 价格虽涨但 OI -19.6%，昨夜 exact-contract 缺失；触发状态未知，证据不足 |
| COM-E-TA701-HOLIDAY-FADE-20260925 | 9/25 | 失败反弹空 | 转一般观察 | 9/28 close 低于6270，但无盘中路径证明触发；OI下降且昨夜缺价，不把事后收盘当事前成交 |
| COM-E-AG2612-REVERSAL-20260925 / COM-E-FU2611-HOLIDAY-FADE-20260925 | 9/25 | 旧 AG 多 / 旧 FU 空 | 已失效，不恢复 | 9/28 价格变化导致方向反转；若此前曾按条件建立，应按原失效规则处置，不以新观点掩盖旧仓风险 |

## 五、产业链地图

1. **贵金属（最弱，高置信）**：EOD AG/AU 下跌并伴 AG OI 增；AG/AU 曲线近乎平坦至轻 contango；夜盘主力回退价继续走低；COMEX 金银分别 -3.78%/-5.44%。反证是 AG 旧截面 call skew 为正且 IV 已高于 RV，说明期权不是明显便宜。实体层缺失。
2. **航运（最强，中等置信）**：EC2611 价格、OI、backwardation 同向，日盘完成主要定价；无夜盘。最大缺失是最新 SCFIS/船期/即期运价，没有实体层就只能买回撤接受，不能把 EOD 爆发直接外推。
3. **能源（方向冲突，中低置信）**：FU 日盘强且深 back，但 OI 下降；SC 日盘近乎平，夜盘主力回退价弱；Brent/WTI 日频并不同步。SC、LU Physical 缺失，Singapore fuel oil 映射缺失，跨市场 RV 不可执行。
4. **黑色建材（偏弱，中低置信）**：FG、JM 下跌且 OI 增；但 FG/JM 仍为 back，C级 spot 不能当 basis，仓单只有 FG 175、日变0。Night exact 缺失，无法判定是否强化。
5. **农产品/畜牧（偏弱但分散，中低置信）**：LH、M、OI 均跌，LH/M/OI 同时减仓，追空含义弱；CBOT 玉米、麦类海外快照下跌，9 月 30 日 USDA Grain Stocks/Small Grains 是主要催化。

## 六、机会排行榜（研究排序，不是胜率或仓位）

| 排名 | idea_id / 方向 / 周期 | 逻辑25 | 赔率25 | 催化20 | price/curve/vol15 | 拥挤技术15 | 总分 | 有效支持层 | 研究判断 / 证据 / 执行 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | COM-E-AG2612-DOWNSIDE-20260928；空；1–5D | 22 | 16 | 16 | 10 | 8 | **72** | 1、2、4 | 存在待验证优势 / 部分 / 等待09:30触发；期货损失不由结构限定 |
| 2 | COM-E-EC2611-ROLL-20260924；多；1–5D | 20 | 14 | 14 | 11 | 10 | **69** | 1、2 | 存在待验证优势 / 部分 / 等待09:45触发及参数；无夜盘 |
| 3 | COM-E-FU2611-ENERGY-20260928；多；1–3D | 19 | 13 | 14 | 12 | 7 | **65** | 2、4 | 存在待验证优势 / 部分 / 等待09:30且待精确报价 |
| 4 | COM-M-FG701-DOWNSIDE-20260929；空；1–3D | 17 | 14 | 11 | 9 | 8 | **59** | 1 | 早期异常 / 不足 / 等待夜盘与curve确认 |
| 5 | COM-M-SC2611-DOWNSIDE-20260929；空；1–3D | 18 | 13 | 14 | 8 | 5 | **58** | 1 | 早期异常 / 不足 / 内外冲突，等待45分钟 |

分数复核：72=22+16+16+10+8；69=20+14+14+11+10；65=19+13+14+12+7；59=17+14+11+9+8；58=18+13+14+8+5。支持层上限已执行：1层≤59、2层≤69、3层才可≥70。AG 的第1层是 EOD+夜盘同一价格/OI层，未重复计数；第2层为 contango/曲线，第4层为 COMEX 贵金属与美元。Physical 缺失、Options 为反证/中性。

## 七、前三名交易卡

### 1) AG2612 失败反弹空｜72分｜等待触发

- **市场隐含/分歧**：市场已计入大幅下跌，但旧 T-1 options 仍显示 ATM IV 38.46%、高于 RV20 33.93%，RR25 +2.28（call 更贵）；我们不认为“put 明显便宜”，分歧只在于海外金银弱势和境内 contango 是否继续压低期货。
- **事实**：EOD close/settle=14,985/15,178，日高/低=15,449/14,975，close -5.01%，OI +15,563；夜盘主力 fallback close=14,930，vs close -0.37%、vs settle -1.63%。精确 AG2612 夜盘 O/H/L 缺失；公开网页给 OI≈271.3k、ΔOI+9,084，但未与仓库校验，仅为低置信归因线索。
- **五层**：①支持（价跌、OI增、夜盘未反转）；②支持（轻 contango）；③缺失；④支持（COMEX 银 -5.44%、金 -3.78%，DXY不弱）；⑤反对/中性（IV不便宜、call skew为正、execution not ready）。最强竞争解释：国内白银已在日盘完成主要去杠杆，夜盘相对 close 仅 -0.37%，09:00 可能均值回归。
- **最佳表达**：AG2612 期货条件空；不使用无 bid/ask 的期权冒充有限损失。若实时 put spread 净支出可核验，才将 11/24 到期、约 35–45Δ put / 15–25Δ put 做 1:1 debit spread 作为替代表达。
- **入场/分批**：09:30 后，反弹到 14,980–15,080 失败且 15 分钟重新收于 14,920 下方，先 1/2；跌破14,880后回抽不过再加1/2。09:00 第一跳不追。
- **止损/失效/退出**：计划止损为30分钟接受在15,220上方；逻辑失效为重新站上15,450且 COMEX 银同步转强。TP1=14,550，TP2=14,150；1–5D 未扩张则退出。若此前已按昨晚条件建立，先按原止损管理，不假设账户持仓。
- **好/中/坏成交**：15,040/14,930/14,880；以15,220止损，TP1约2.7R/1.3R/1.0R，TP2约4.9R/2.7R/2.1R；未含手续费，另留3–8跳滑点。坏成交不建仓。
- **规格与压力**：multiplier 15kg，tick 1元/kg，tick value 15元；按14,930名义约223,950元/手。当前一般保证金22%、涨跌停20%，估算保证金约49,269元/手；空头遭遇1个/2个复合涨停压力约45,534/100,175元/手，期货最大损失不有限。交易时间含21:00–02:30；last trading day 2026-12-15。个人/机构交割资格与交割月规则须向经纪商确认，11月底前滚动，避免进入交割月。[白银业务细则](https://www.shfe.cn/regulation/exchangerules/productrules/202512/t20251231_829961.html)
- **催化/最坏/放弃**：1D催化为日盘对COMEX跌幅的再定价；2–5D为中国PMI、美元和节前降杠杆。最坏是海外贵金属急反弹叠加20%限幅和流动性消失。开盘直接跌破14,700、或实时价差超过可接受的8跳，放弃。

### 2) EC2611 回撤接受多｜69分｜等待触发及参数

- **市场隐含/分歧**：EOD 已隐含运价/流动性利多继续，价格、OI、backwardation三者同向；分歧在于没有最新实体运价确认，强势可能是短期仓位挤压而非持续供需。
- **事实**：EOD O/H/L/C=2,799/2,978/2,794/2,937.5，settle=2,905.5，close +6.92%、5D +12.27%，OI +6,073（+31.3%），backwardation 23.72%。无夜盘制度；没有 overnight return 或 Night curve。
- **五层**：①支持；②支持；③缺失；④中性/缺失（无 exact 外盘映射）；⑤缺失。最强反证：OI 激增也可能代表双向换手，不能识别资金身份；实体层缺口令持续性不足。
- **最佳表达**：EC2611 期货1手条件多；无成熟 options 替代表达。两腿配比不适用。
- **入场/分批**：09:45 后仅在2,880–2,920守住并重新收复2,938/VWAP时，1/2+1/2；高开超过3,020不追。
- **止损/失效/退出**：计划止损45分钟接受低于2,794；逻辑失效为跌破2,747.5且OI/成交同步降温。TP1=3,050，TP2=3,200；1–5D无扩张退出。
- **好/中/坏成交**：2,900/2,938/2,980；以2,794止损，TP1约1.4R/0.8R/0.4R，TP2约2.8R/1.8R/1.2R；只接受好成交，坏成交放弃。
- **规格与压力**：multiplier 50元/点，tick 0.5点，tick value 25元；按2,937.5名义约146,875元/手。无夜盘；last trading day 2026-11-30，现金交割，无实物交割风险但有到期结算跳变。仓库未确认 EC2611 当前动态 margin/limit；标准合约基准为12%/10%，节前实时参数必须由交易所/经纪商二次确认，未确认前不执行，不能把基准参数当当前压力上限。[EC标准合约](https://www.ine.com.cn/products/futures/index_f/ec_f/standard_ec_f/202602/t20260210_830423.html)
- **催化/最坏/放弃**：1–5D催化为运价、船期和持仓延续。最坏是流动性真空、OI挤压反转和现金结算预期重定价。未取得当前保证金/限幅、实体运价或开盘接受度，放弃。

### 3) FU2611 回撤接受多｜65分｜待精确夜盘报价

- **市场隐含/分歧**：日盘已定价重油紧张与深 backwardation；我们的分歧是 Brent 仍强能否抵消 SC 夜盘走弱。EOD price涨但OI减，说明方向证据不干净。
- **事实**：EOD O/H/L/C=4,363/4,463/4,293/4,418，settle=4,390，close +3.78%，5D +3.08%，OI -5,127，EOD backwardation 19.36%。仓库及可靠外部来源均未给出可验证的 FU2611 夜盘 O/H/L/C、双收益锚与ΔOI，因此不声称昨夜涨跌。
- **五层**：①中性（价涨仓减）；②支持（深back）；③中性（C级spot不可评分）；④支持但仅context（Brent +1.46%）；⑤反对（IV69.78、较RV高30.50点且无报价）。
- **最佳表达**：只在精确合约价可核验后用 FU2611 期货；旧期权截面 expiry=2026-10-19、ATM4400、RR25=-1.80，整体vol昂贵，暂不买call。
- **入场/分批**：09:30 后，4,350–4,390守住并重新站上4,420/VWAP，1/2+1/2；若直接高开4,460以上不追。
- **止损/失效/退出**：30分钟接受低于4,293止损；逻辑失效为backwardation显著收窄且SC/Brent同步转弱。TP1=4,550，TP2=4,680；1–3D无扩张退出。
- **好/中/坏成交**：4,380/4,420/4,460；以4,293止损，TP1约2.0R/1.0R/0.5R，TP2约3.4R/2.0R/1.3R；仅好成交具备赔率。
- **规格与压力**：multiplier 10t，tick 1元/t，tick value 10元；按4,418名义44,180元/手。9月29日日盘前限幅18%、一般保证金20%；当日收盘结算后调整至20%/22%。当前1个/2个18%复合涨停压力约7,952/17,337元/手；期货最大损失不有限。交易时间含21:00–23:00；last trading day 2026-10-30，实物交割风险高，自然人应在经纪商截止日前退出，计划10月16日前滚动。[燃料油业务细则](https://www.shfe.cn/regulation/exchangerules/productrules/202512/t20251231_829966.html)
- **催化/最坏/放弃**：1D为SC/Brent冲突收敛，1–3D为EIA与地缘；最坏是原油跳水、保证金上调、夜盘流动性消失。无精确夜盘/开盘价、back收窄或成交落入坏情景即放弃。

## 八、商品期权专项

- **AG2612 / 2026-11-24**：ATM15200，IV38.455%，RV20 33.927%，IV-RV +4.53点，RR25 +2.28，BF25 2.025；S/P/E=Y/N/N。夜盘标的仅小幅低于EOD close，旧ATM仍大体可比；方向性空头优先条件期货，put spread仅在实时净支出可核验时考虑。
- **FU2611 / 2026-10-19**：ATM4400，IV69.78%，IV-RV +30.50点，RR25 -1.80，BF25 0.79；Y/N/N。puts更贵、整体vol昂贵，不以“事件风险大”单独证明call便宜。
- **SC2611 / 2026-10-14**：旧ATM730，IV74.90%，IV-RV +16.48点，RR25 +6.25；Y/N/N。夜盘主力回退价712令旧ATM明显失真，T-1截面只作背景。
- **FG701 / 2026-12-11**：ATM900，IV24.405%，IV-RV -1.71点，RR25 +10.41；Y/Y/N。表面上IV略低于RV，但call skew昂贵且没有bid/ask，不能据此买波动。
- **AU2612 / 2026-11-24**：ATM912，IV23.095%，IV-RV +4.23点，RR25 +0.59；Y/Y/N。标的夜盘898令旧ATM可比性下降。
- **LC2701 / 2026-12-07**：ATM120000，IV46.48%，IV-RV +7.27点，RR25 -1.93；Y/N/N。无夜盘且仓单stale，不把负skew解释为做市商净Gamma。
- **Event convexity / vol RV**：9月30日中国PMI、USDA Grain Stocks、EIA，以及国庆休市gap均支持“有限损失结构优于裸期货”的研究方向；但 execution-ready=0，本期没有可报价的vol RV。任何 Greeks、净权利金、滑点和最大损失都必须在具体series实时报价后重算。

## 九、09:00开盘风险地图

| 品种 | Previous China EOD | Current trading day Night | 07:00 Overseas | 预期开盘/冲突 | 追价与等待 | 开盘后确认 |
|---|---|---|---|---|---|---|
| AG2612 | -5.01%，价跌仓增、轻contango | 主力14,930；vs close仅-0.37%，大部分弱势已在日盘 | 银-5.44%、金-3.78%，同向 | 偏低/但边际弹性低 | 不追；等30分钟 | 14,880回抽、15,000接受、OI与curve |
| AU2612 | -2.86%、轻contango | 主力898；vs close-0.74% | 金-3.78%，同向 | 偏低 | 不追；等30分钟 | 900整数位、COMEX是否止跌 |
| SC2611 | +0.34%、OI减、back0.90% | 主力712；vs close-2.10% | WTI近持平、Brent+1.46%，冲突 | 偏低、可能已完成较多定价 | 不追；等45分钟 | 712/717.5、SC近次月、人民币 |
| FU2611 | +3.78%、OI减、深back | exact缺失 | Brent正向、HSFO缺失 | 不确定 | 等30分钟，未核价不下单 | 4,390/4,420、back与成交量 |
| CU2611 | -0.70%、OI增、back0.48% | exact缺失 | COMEX铜-2.23%，CNH略强均偏空 | 偏低 | 等30分钟 | 109,000、LME/COMEX、OI |
| EC2611 | +6.92%、OI大增、深back | 制度上无夜盘 | exact运价增量缺失 | 高开/平开皆不追 | 等45分钟 | 2,880–2,938接受、OI、运价 |
| FG701/JM2701 | -2.83%/-2.44%，OI增 | exact缺失 | 无exact映射 | 低开风险但证据不全 | 等30–45分钟 | EOD低点、curve、FG仓单 |
| LC2701/LH2611 | -5.69%/-4.01% | 无夜盘 | 无exact映射 | 低开或弱平 | 等45分钟 | 是否减仓延续、现货/仓单 |

海外 move 与 China Night 的信息弹性：AG/AU 同向但国内相对 close 的新增跌幅远小于外盘日跌幅，说明中国 9 月 28 日日盘已经预交易大部分贵金属压力；SC 与 Brent 日频方向冲突，说明单一 headline 不能映射为可追的境内 gap。Night near-next 两腿缺失，**最新 Night curve 无法确认价格**。

## 十、未来24小时 / 7日事件日历（北京时间）

| 时间 | 事件 | 影响与处理 |
|---|---|---|
| 9/29 15:00结算后 | 上期所/上能所节前扩大限幅与保证金；AG维持20%/22%，FU2611升至20%/22%，SC2611升至20%/22% | 压缩裸 Delta；同因子合并风险；不得用旧保证金反推仓位。来源：[SHFE](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)、[INE](https://www.ine.com.cn/publicnotice/notice/202609/t20260921_833506.html) |
| 9/29 21:00 | 当晚连续交易开始，归属9/30交易日 | 先看15/30分钟，不把今晨主力回退价当今晚未来行情 |
| 9/30 09:30 | 中国官方9月PMI（按国家统计局月末惯例；最终公告待发布） | 黑色、有色、化工 Delta 催化；数据前不扩大同向篮子 |
| 9/30 15:00后 | 国庆休市前最后结算；9/30晚无夜盘，10/1–10/7休市 | 任何隔夜仓必须能承受海外7日gap；优先有限凸性，但需实时bid/ask |
| 10/1 00:00 | USDA Grain Stocks + Small Grains Summary（9/30 12:00 ET） | 谷物/粕类 Vega 与gap；无报价则减裸Delta。[USDA日历](https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?js=1&month=09&view=l&year=2026) |
| 9/30 22:30 | EIA Weekly Petroleum Status Report常规窗口 | SC/FU/BU/LU Delta/Vega；事件前不追价。[EIA schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 10/3 03:30左右 | CFTC COT常规周五发布窗口 | 仅作滞后持仓背景，禁止解释为当前机构方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) |
| 10/4 | OPEC+审议11月政策（媒体报道日期） | 原油gap与波动率催化；中国休市，裸Delta需按海外流动性压力管理。[Reuters/WSJ摘要](https://www.wsj.com/business/energy-oil/opec-allies-agree-to-keep-oil-output-steady-in-october-c7fceb83) |
| 10/8 08:55–09:00 | 中国期货/期权集合竞价，夜盘当晚恢复 | 休市gap分两段处理；先看开盘45分钟，不把节前条件单机械沿用 |

## 十一、风险预算、覆盖核对与归档

- 单一试仓最大损失 NAV 0.25%–0.75%；确认交易0.75%–1.50%；单一高确信主题≤2.5%–3.0%。鉴于 Night exact 数据缺口、节前保证金上调和长假gap，本期单一条件单仅用区间下沿0.25%–0.50%；贵金属/美元、能源/地缘分别合并计算。
- 压力测试必须包含：1/2个动态涨跌停、相关性破裂（SC vs Brent 已示范）、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割/到期、人民币急变，以及9月30日晚至10月8日的海外累计波动。

### 覆盖核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足 | 未入榜最值得跟踪的异常/无异常依据 |
|---|---:|---:|---|---|
| 黑色建材 | 9 | 9/9 futures+market state | Night exact全缺；Physical仅C级 | FG价跌仓增且仓单不变；JM弱但back仍在，未达多层证据 |
| 有色贵金属 | 12 | 12/12 | Night仅AU/AG主力回退；CU等exact缺；basis不合格 | AU/AG弱，CU外盘偏空；其余无跨层共振 |
| 能源炼化化工 | 21 | 21/21 | Night仅SC主力回退；SC/LU Physical缺；HSFO/VLSFO缺 | FU深back但OI减；SC内外冲突；BR价涨OI骤减 |
| 新能源/GFEX材料 | 3+动态新品 | LC/SI/PS及仓库动态品种均纳入77品种扫描 | LC仓单stale；无Night | LC跌幅大但实体不新，追空不合格 |
| 农产品油脂饲料畜牧 | 17 | 17/17 | DCE多数期权 skipped；部分Physical未配置 | LH/M/OI价跌仓减；USDA事件临近但无事件前错价证据 |
| 航运软商品 | EC及CF/SR/AP/CJ/PK | 全部纳入 futures/market state | EC实体运价、soft外盘exact映射不全 | EC价格/OI/curve最强；软商品无多层异常 |

- **应覆盖63个指定代码：63/63均在全市场 futures/market-state 初筛中；实际扫描77个品种、806个具体合约。** 热力图只展示10项，不代表其余未分析。
- **策略类别**：方向、基差、跨期、跨品种/跨市场RV、风格/中性、波动率/偏度、事件凸性均扫描。可用结果仅方向/跨期研究；C级basis、缺口径的进口映射、未定义篮子均不得称套利或中性组合。周期覆盖日内确认、1–3D、1–5D及节前7D gap。
- **Options覆盖**：64个目标中45个成功、1个失败（DCE:A）、18个skipped（DCE:B/BZ/C/CS/EB/EG/I/JD/JM/L/LG/LH/M/P/PG/PP/V/Y）；不是“没有机会”，而是对应第五层与执行判断数据不足。
- **不适用/流动性不足**：EC/LC/LH等无夜盘不是错误；所有期权 execution-ready=0，不能虚构报价。Night工具对当前交易日的精确合约与曲线均数据不足。
- 归档路径：`reports/2026/09/2026-09-29_commodities_morning.{md,json}`、`latest/commodities_morning.{md,json}`、`status/commodities_morning_latest.json`、`manifests/reports.json`。`archive_status=success` 仅在 main 六路径回读通过后成立；`ci_validation_status=pending_or_unverified`，不等待CI。

A. 今天没有应立即建立的新仓位。
B. 09:30后仅挂AG2612失败反弹空、FU2611回撤接受多的条件单；EC2611须等09:45并先确认动态参数。
C. 继续观察SC内外盘冲突、FG/JM价跌仓增、LC/LH弱势、9月30日PMI/USDA/EIA与节前保证金变化。
D. 避免09:00追贵金属/原油首跳、无精确Night数据的追价、C级basis套利、无bid/ask期权及国庆长假裸露大Delta。
