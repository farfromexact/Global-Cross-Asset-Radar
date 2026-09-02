# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-02

## 一、今日一句话结论

**今天有高波动，但没有满足数据质量与五层证据纪律的可执行新增风险：今日商品期货期权无合格交易。**

最重要的不是“没机会”，而是**中国仓库截至19:30仍未发布9月2日日盘EOD**。当前统一层 `report_input_latest.json` 的 `requested_date=2026-09-01`，核心期货、Market State、Physical、Options也仍是9月1日；只有上一夜盘快照的 `trading_date=2026-09-02`。因此，15:00—19:30外盘虽然出现了非常清晰的“油强、金银弱、美元/美债收益率强”变化，但在21:00前缺少中国9月2日真实结算价、曲线和OI作为锚，按v2五层规则最多只能形成一层当日fresh海外证据，不能把事件波动升级成合格交易。

**今日商品期货期权无合格交易。**

最接近触发的三项：① SC/BU能源多头——需要9月2日国内结算/curve/OI或21:00开盘后30—45分钟接受度确认；② AU/AG失败反弹空——需要国内日盘锚与开盘后美元/实际利率继续同向；③ JM/黑色高位反转——需要9月2日价格-OI和实体/库存方向确认。三者目前都不应追首跳。

---

## 二、数据质量与覆盖说明

### 1. China-Commodities-Engine v2 实际读取

第一层已读取：

- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`

按需进一步读取：

- `data/latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_last_run_status.json`
- `data/night_session/latest.json`

统一报告层在本次19:30决策窗口的状态：

- `report_input requested_date = 2026-09-01`
- `report_input generated_at = 2026-09-02T06:07:06+08:00`
- Futures：2026-09-01，engine-native `data_fresh=true`
- Market State：2026-09-01，exact-contract 1D/3D/5D/20D、RV20、Volume/OI、ΔOI、curve可用
- Physical：requested 2026-09-01，4/20映射可用，均按各自周/旬频率fresh；**但没有9月2日方向变化**
- External：requested 2026-09-01，6/22映射，4条fresh、2条stale；仅作EOD/context，**不冒充19:30实时**
- Options：2026-09-01，共23,200条、387个series；376 `surface_ready`，73 `positioning_ready`，0 `execution_ready`
- Night Session：`trading_date=2026-09-02`、`night_session_date=2026-09-01`，是上一夜盘完成快照，不是9月2日日盘
- Contract metadata：partial；DCE contract-info存在JSON decode error

核心期货质量：五所 SHFE/INE/DCE/CZCE/GFEX 全覆盖，`source_date_match_pct=100%`，`critical_module_errors=0`，`full_market_ready=true`，无excluded exchange，duplicate/invalid OHLC/negative volume-OI均为0；但有3个OHLC placeholder。**这些质量指标证明9月1日快照本身可靠，不代表它可被静默升级成9月2日数据。**

因此，本晚报的数据状态定为 **stale_or_partial for 2026-09-02 decision**：不是仓库“坏了”，而是截至决策窗口，**T日日盘层尚未发布**。不等待到21:00以后，不轮询。

Physical当前可验证映射仅包括：铁矿港口库存（最新周度2026-08-26）、焦煤国家统计局主焦煤现货（最新旬度2026-08-20，basis quality C）、玻璃企业库存（最新周度2026-08-28）、PTA加工费（最新周度2026-08-28）。这些孤立水平只作为physical context，不自动计完整方向证据层。

Options 9月1日链质量较好：IV coverage约98.2%，OI coverage约68.1%，但bid/ask coverage为0，`execution_ready=0/387`，且本报告日为T-1背景，所以**不计9月2日fresh evidence，不提供净权利金、bid/ask、精确交易成本或可成交执行价**。Dealer Gamma方向未知，禁止推断。

来源：
- [China-Commodities-Engine / report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [China-Commodities-Engine / last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- [China-Commodities-Engine / radar_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)

---

## 三、商品仪表盘（国内为最新可用9月1日EOD，不冒充9月2日）

| 板块 | 品种/具体主力 | 最新有效价 | 1D | 5D | OI/ΔOI | Curve | Physical/Basis | Options背景 | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能源 | BU2610 | settle 4904 / close 4934 | +3.55% | +6.42% | OI 238,945；ΔOI -3.42% | +4.00%，z +1.93 | 无T日实体闭环 | ATM IV约39.6%，T-1；执行未就绪 | 昨日条件多逻辑仍在，但今日不可评分 |
| 能源 | SC2610 | settle 637.2 / close 637.8 | +3.06% | +7.67% | OI 40,001；ΔOI -6.32% | pair-roll，z不可用 | 无T日实体闭环 | ATM IV约53.1%，T-1；执行未就绪 | 事件最强、数据锚最弱，禁追首跳 |
| 化工 | EG2610 | settle 5481 / close 5525 | +5.53% | -0.29% | OI 334,485；ΔOI -2.45% | +3.36%，样本仅8 | 无方向physical | ATM IV约47.3%，T-1 | 高波动回撤观察 |
| 化工 | MA610 | settle 3044 / close 3069 | +4.57% | +3.33% | OI 664,801；ΔOI -6.74% | +2.89%，z +1.79 | 无方向physical | series需重新核对underlier/expiry | 涨价减仓，不能叫新多 |
| 黑色建材 | FG701 | settle 953 / close 969 | +1.38% | +4.04% | OI 1,352,049；ΔOI -3.05% | -1.09%，z +2.39 | 最新周度企业库存仅context | T-1 | 反弹但非完整短缺确认 |
| 黑色 | I2701 | settle 722 / close 726.5 | -0.48% | +0.77% | OI 577,319；ΔOI +1.44% | +1.62%，z +2.72 | 港口库存为最新周度level | T-1 | curve强、价格未确认 |
| 农产品 | M2701 | settle 3357 / close 3377 | +0.12% | +4.00% | OI 2,826,855；ΔOI +56,036 | -0.30%，z +2.54 | 缺压榨/进口方向闭环 | ATM IV约14.4%，T-1 | 昨日低噪声趋势候选，今日降级 |
| 贵金属 | AU2610 | settle 961.04 | -1.76% | -4.75% | OI 172,261；ΔOI -3.85% | +0.10% | 宏观主导 | ATM IV约23.4%，T-1 | 失败反弹空观察，不追低 |
| 贵金属 | AG2610 | settle 16259 / close 16245 | -2.46% | -3.08% | OI 232,963；昨日减仓 | backwardation | 宏观主导 | T-1 | 当前外盘继续弱，但地缘反转风险大 |
| 新能源 | LC2701 | settle 159960 / close 157860 | -0.34% | +3.90% | OI 404,917；ΔOI +0.47% | -0.29% | warehouse变化需口径核对 | T-1 | 无9月2日日盘，不做 |
| 航运 | EC2610 | settle 1831 / close 1896 | -3.56% | -5.93% | OI下降约10.6% | 近月曲线约+33%，仅1 obs且roll | 运价/保险需实时闭环 | 无执行层 | 极端curve不称套利 |

说明：表中所有国内价格、收益、OI和curve均为**2026-09-01 EOD**。它们用于说明“进入今天之前市场在哪里”，不计作9月2日fresh层。

---

## 四、相比上一交易日真正变化

1. **油的地缘溢价进一步抬升，但日内已从高点回吐。** 9月2日17:49北京时附近，Reuters报Brent约94.76美元/桶、WTI约90.26；日内高点一度97.04/92.29。相对上一版19:30截点的Brent 92.21，约高2.8%。这不是中国SC已经上涨2.8%，而是今晚开盘的海外映射风险。
2. **Hormuz供给尾部仍在，但“全堵塞”并未发生。** Reuters报道周一仍有约1700万桶原油通过霍尔木兹海峡，同时两艘油轮被水雷致损。对油价而言是典型binary regime：边际升级可冲100美元，缓和则会迅速挤掉战争溢价。
3. **黄金出现“地缘不涨、利率压制”的异常弱势。** 18:07北京时附近，现货金约4302.20美元/盎司，较上一版截点4369.24低约1.5%；12月COMEX金期货约4349.8，白银约63.59、当日约-1%。这说明当前边际定价不是传统safe-haven，而是油价→通胀→更高利率/更强美元。
4. **美元与长端利率成为商品共同宏观因子。** Reuters称DXY触及8月17日以来高位，美国10Y收益率约4.81%，市场对9月Fed加息定价约七成。它同时压贵金属、提高非美元买家的商品成本，并放大油价冲击的二阶通胀交易。
5. **最大的“变化”其实是数据闸门本身：9月2日中国EOD没有进入仓库。** 昨日重跑版曾有五所T日+T日期权，可给BU/SC/M 70+条件分；今天19:30只有海外层是当日fresh，因此同样逻辑必须降级，不能沿用昨天78/76/75的分数。

实时海外来源：
- [Reuters：Oil prices steady as traders weigh supply risks，2026-09-02](https://www.reuters.com/business/energy/oil-up-nearly-1-us-iran-trade-fresh-strikes-2026-09-02/)
- [Reuters：Gold falls to lowest in more than three weeks，2026-09-02](https://www.reuters.com/world/india/gold-hits-over-3-week-low-mideast-tensions-fan-rate-hike-fears-2026-09-02/)
- [Reuters：Dollar hits two-week high，2026-09-02](https://www.reuters.com/world/china/dollar-holds-firm-middle-east-hostilities-lift-oil-2026-09-02/)

---

## 五、产业链地图

| 产业链 | 当前方向 | 价格/curve | 实体/库存 | 海外/宏观 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 原油→燃料油/沥青/芳烃 | 偏多但binary | 9/1 SC/BU强，SC roll使curve降级 | 无9/2实体闭环 | Brent维持约95、Hormuz冲突 | 9/2中国结算、curve、OI | 中低 |
| PX→PTA→聚酯/EG | 偏强但追涨差 | 9/1 PX/TA/EG普遍强，部分涨价减仓 | PTA加工费仅最新周度level | 油价正向映射 | 9/2国内链条与库存方向 | 低 |
| 焦煤/焦炭→钢材 | 高位分歧 | 9/1 JM 20D强但OI明显下降，RB/HC价格弱而OI增 | 焦煤现货旬度、I库存周度，仅context | 无可靠19:30 exact-contract外盘闭环 | 9/2 price-OI、铁水/补库/钢厂利润 | 低 |
| 金银 | 偏空但凸性反转风险高 | 9/1 AU/AG已跌；今日外盘继续弱 | 宏观主导 | 美元、10Y和加息概率上升；地缘本应利多却未抵消 | 9/2国内结算与开盘后实际利率确认 | 中低 |
| 油脂/饲料 | 中性等待 | 9/1 M趋势最好但仅旧锚 | 缺压榨/进口/库存方向 | 当前无足够新鲜CBOT/南美exact-contract映射 | 9/2国内+海外农产品实时 | 低 |

**最强产业链：能源供给冲击链。最弱相对链：贵金属（在地缘升级背景下仍被美元/真实利率压制）。**

但这不是“多油空金”的正式RV交易：油与金在冲突升级/降级时的相关性会非线性翻转，且国内T日锚缺失。

人民币/美元作用：美元偏强是今天非常明确的共同宏观压力；对AU/AG是直接利空，对进口型能源/金属则同时存在“美元计价上涨+人民币换算”的潜在抬升。但没有19:30同频USDCNH与中国T日结算对齐，本报告不把汇率换算当作可执行套利证据。

---

## 六、机会排行榜

**无项目达到60分，因此不进入正式机会榜。**

按v2规则，9月2日当日可确认的独立fresh层只有“15:00—19:30海外/宏观实时映射”这一层；国内价格-OI、curve、Physical、Options均仍是T-1或更低频。**1个fresh独立层的评分硬上限≤59。**

**今日商品期货期权无合格交易，保留现金和观察仓。**

最接近触发但仍不入榜的观察项：

- **SC/BU能源多头：59/100（观察）**。缺：9月2日中国日盘结算、curve/OI；或21:00后30—45分钟价格接受度。为什么不做：Brent日内从97回到94—95，战争溢价二向性极高，直接追gap的赔率差。
- **AU/AG失败反弹空：58/100（观察）**。缺：9月2日国内锚、21:00后美元/美债实际利率继续上行、黄金无法收复日内关键反弹区。为什么不做：地缘消息一条即可使黄金“safe-haven属性”瞬间恢复。
- **JM2701高位衰竭空：54/100（观察）**。缺：9月2日价格-OI继续出现弱价/减仓或弱价/增仓的可验证结构，并需铁水、补库、库存至少一项方向闭环。为什么不做：9月1日只是“价涨仓减/高位去仓”的归因线索，不等于新空建立。

---

## 七、交易卡

**本期没有正式交易卡。** 原因不是缺少交易想法，而是没有任何机会达到60分入榜，更没有70分试仓门槛。为避免把“观察”包装成“交易”，不生成正式入场、止损、TP和保证金参数。

### 非交易观察卡1：SC/BU能源链

- 事实：9/1 SC2610 settle 637.2，BU2610 settle 4904；今日17:49附近Brent 94.76，较上一版截点高约2.8%。
- 市场定价：油价仍含显著Hormuz战争溢价，但从日内97高点回吐。
- 推断：今晚能源链偏高开/强开风险仍在。
- 主观判断：**首跳不值得追。**
- 触发升级：21:00后等30—45分钟；价格站稳开盘区间上沿，且Brent重回/站稳96附近，同时SC/BU不是冲高回落结构。
- 放弃：Brent跌回92附近、冲突缓和、SC/BU开盘高开低走。
- 风险预算：即使触发，初始风险不超过NAV 0.25%—0.50%；待次日T日curve/OI确认才允许加风险。
- 合约multiplier/tick/margin/limit/last trading day：**本期不形成正式交易，因此不引用旧参数；若升级为交易卡必须重新核对交易所当日参数。**

### 非交易观察卡2：AU/AG失败反弹空

- 事实：9/1 AU/AG已经下跌；今日18:07附近现货金4302.2，白银63.59；美元和10Y收益率偏强。
- 市场定价：市场在交易“油价通胀冲击→Fed更鹰”，而不是单纯地缘避险。
- 推断：若21:00后金银反弹失败，趋势延续概率上升。
- 触发升级：等待15—30分钟；反弹不能收复开盘区间上沿，同时DXY/10Y不回落。
- 放弃：黄金快速收复日内跌幅、冲突显著升级、美元/收益率转跌。
- 最佳表达若升级：优先有限风险Put Spread；当前Options为T-1且execution_ready=false，**不得报价或指定可成交权利金**。

### 非交易观察卡3：JM高位衰竭

- 事实：9/1 JM2701 3D约+6.6%、20D约+26.5%，但ΔOI约-9%，属于价涨仓减线索。
- 推断：若今天/今晚价格不能再创新高且OI继续弱，可能从趋势变成拥挤去杠杆。
- 触发升级：必须看到9/2新数据或夜盘30—45分钟失败突破；最好再有铁水/补库/钢厂利润的方向闭环。
- 放弃：价格创新高并伴随OI重新增长、实体需求同步改善。
- 当前不做：没有T日国内层，也没有够新鲜的physical方向层。

---

## 八、商品期权专项

Options正式数据日为**2026-09-01（T-1）**：

- 23,200条唯一合约记录，64/64产品覆盖；
- 387个series；
- `surface_ready=376/387`；
- `positioning_ready=73/387`；
- `execution_ready=0/387`；
- IV coverage约98.2%；
- OI coverage约68.1%；
- bid/ask coverage=0；
- dealer gamma direction unknown。

因此，本期只能把曲面作为**昨日波动率背景**。代表样本而非全市场极值：昨日SC ATM IV约53.1%、EG约47.3%、BU约39.6%、AU约23.4%、M约14.4%。不能称SC为“全市场最高IV”或M为“全市场最低IV”。

研究优先级：

1. **能源event convexity**：若今晚冲突继续升级，SC/BU方向上更适合有限风险Call Spread而不是裸追期货；但需要实时逐strike报价和流动性确认。
2. **贵金属Put Spread**：只有在反弹失败且美元/收益率同向时才研究，避免裸买深虚Put在高波动率中承受vol crush。
3. **M低IV背景**：昨日M样本IV明显低于能源，如果国内趋势重新确认，可研究低成本方向凸性；今天缺T日标的确认，不执行。
4. **必须回避**：任何依赖bid/ask、精确净权利金、Gamma dealer方向或OI crowding结论的结构。

固定执行免责声明：**research only; manual quote and manual confirmation required before execution; no premium quoted**

---

## 九、21:00夜盘开盘风险地图

由于9月2日中国日盘结算缺失，以下是“海外映射方向”，**不是对实际9月2日settle的精确gap预测**。

| 品种 | 海外15:00—19:30映射 | 预期开盘风险 | 置信度 | 是否追价 | 等待 | 开盘后最重要确认 |
|---|---|---|---|---|---|---|
| SC / BU / FU / LU | Brent约94.8，仍高于昨日截点，但从97回落 | 偏高/高波动 | 中 | **不追首跳** | 30—45m | 是否高开低走；Brent是否重回96；开盘区间接受度 |
| PX / TA / EG / MA | 原油正向成本映射，但本地链条9/2未知 | 偏强但分化 | 低 | 不追 | 30—45m | 上游强是否能传导到各自curve/成交 |
| AU / AG | 外盘金银走弱、美元与收益率走高 | 偏低 | 中 | 不追低 | 15—30m | 反弹能否收复开盘区间；DXY/10Y是否继续强 |
| I / JM / J / RB / HC | 缺可靠19:30 exact-contract外盘映射 | 不确定 | 低 | 不做首跳 | 30—45m | price-OI、黑色链联动、成交量是否放大 |
| M / Y / P | 海外农产品实时闭环不足 | 不确定 | 低 | 不做首跳 | 30—45m | CBOT/油脂同向与国内价差结构 |
| LC / SI / PS | 夜盘资格/时段未在本次metadata中完成可靠确认 | **夜盘安排未确认** | 低 | 不交易 | — | 若无夜盘，下一窗口次日9:00 |
| EC | 本身事件/运价驱动且curve受roll影响 | 不确定 | 低 | 不追 | 30m | 现货运价/保险/地缘运输是否同向 |

仓库上一夜盘快照覆盖802个所选合约，其中612个被识别为night-session contract；但本报告不把上一夜盘的品种状态机械外推为今晚规则。无法在metadata中确认的品种明确标为“夜盘安排未确认”。

---

## 十、未来24h / 7d事件

北京时间：

- **9月2日20:15｜ADP美国私营就业**：距本报告仅45分钟。对黄金、白银、美元、美债和铜/油的宏观折现率通道最直接。处理：在数据前不新开宏观方向裸仓；若用期权只保留有限损失凸性。
- **9月2日22:30｜EIA Weekly Petroleum Status Report**：标准周三10:30 ET发布时间。对SC/BU/FU/LU及裂解链是今晚最直接的第二催化。处理：若21:00能源高开，不要在EIA前把首跳当趋势确认。
- **9月4日20:30｜美国8月非农就业报告**：BLS已确认9月4日8:30 ET发布。对美元、真实利率、金银以及所有美元计价商品的beta显著。
- **9月5日03:30｜CFTC COT**：CFTC 2026日历列明9月4日15:30 ET发布，数据通常截至周二。只能解释报告交易者分类仓位，不推断具体机构客户动机。
- **9月7日｜美国Labor Day / CME特殊结算安排**：CME公告9月7日不发布CME/CBOT/NYMEX/COMEX结算价，假日前后流动性和跨市场价格发现质量下降。降低隔夜杠杆，避免把carry-forward settlement当新价格。
- **WASDE**：USDA 2026年9月WASDE定于9月11日12:00 ET，**不在本报告7日窗口内**，仅提前标记，不作为本周立即催化。

官方来源：
- [EIA Weekly Petroleum Status Report schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [BLS Employment Situation](https://www.bls.gov/ces/)
- [CFTC COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- [USDA WASDE report calendar](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- [CME 2026 Labor Day settlement notice](https://www.cmegroup.com/tools-information/holiday-calendar/files/2026/labor-day-holiday-settlement-times-2026.pdf)

---

## 十一、风险预算与今日固定回答

是否值得新增风险：**否，现阶段不值得。**  
当前regime：**地缘能源供给冲击 + 通胀/利率再定价 + 美元偏强 + 中国T日数据真空。**  
Price是否获curve确认：仅能回答9/1，部分能源/化工获确认；9/2不能回答。  
是否获库存/实体确认：**没有。** Physical多为周/旬level，缺方向闭环。  
境内外是否同向：无法对9/2完整判断；外盘油强、金银弱与9/1国内方向大体延续，但不能冒充同日验证。  
人民币/美元作用：美元偏强压贵金属并抬高非美元进口成本；缺同频USDCNH对齐，不计套利证据。  
期权是否优于裸期货：事件性能源/金银若触发，**有限风险期权结构在尾部控制上优于裸期货**，但当前execution_ready=false，只能研究。  
是否有跨期/跨品种/跨市场RV：有“能源强/贵金属弱”的相对观察，但不满足可执行RV口径。  
哪些是单日噪音：SC/油价从97回到94—95的日内波动、贵金属对单条地缘新闻的瞬时反应。  
哪些应等30—45分钟：SC/BU、化工链、黑色、油脂；AU/AG至少等15—30分钟。  
哪些不值得交易：任何基于9/1国内数据直接复制昨天交易卡的订单；任何依赖T-1期权bid/ask或Dealer Gamma的策略。

风险预算：在本报告“无合格交易”状态下，新增风险预算=0。若条件升级，单一试仓最大损失NAV 0.25%—0.50%，只有次日T日国内price/OI/curve重新确认才可提升；同一“油价/通胀/美元”因子必须合并计算。重点压力情景：Hormuz突然缓和导致油价跳跌；冲突升级导致油价跳涨/涨跌停；ADP/EIA造成双向gap；保证金上调；期权IV先升后塌；人民币急变；夜盘流动性消失。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无正式条件单；SC/BU、AU/AG只做触发观察，不在T日锚缺失时预挂追价单。  
C. 今天应继续观察的机会：SC/BU能源多头、AU/AG失败反弹空、JM高位衰竭；分别等待30—45分钟、15—30分钟、30—45分钟。  
D. 今天必须避免或退出的交易：追能源首跳、追空金银首跳、复制9月1日BU/SC/M旧评分、任何依赖未就绪bid/ask或Dealer Gamma的商品期权交易。

---

## 来源与审计备注

中国数据全部来自已连接GitHub仓库 `farfromexact/China-Commodities-Engine`；实时海外层使用Reuters与官方日历。报告严格区分2026-09-01中国EOD、2026-09-01晚间至9月2凌晨的上一夜盘快照、以及2026-09-02 15:00—19:30海外实时映射。未使用或推断21:00之后的中国价格。

本报告只提供研究与交易决策支持，不自动下单。
