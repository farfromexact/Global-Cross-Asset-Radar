# 商品期货期权晚间雷达｜2026-10-26

> 生成时间：2026-10-26T19:26:40+08:00｜信息截点：2026-10-26 19:26 BJT｜中国最近完整EOD：2026-10-26｜今晚21:00夜盘归属交易日：2026-10-27

**截至本报告时点，无可立即执行的合格新交易；SC早间多头失效，今晚只等曲线反转空、铜罢工多与化工相对强势的严格确认。**

机会不是没有，而是条件未到：SC反向研究已有价格、曲线、海外三层支持，但今晚尚未开盘且Brent口径冲突；CU有罢工催化但产量影响未知；MA有强价强仓但精确701跨月与执行期权报价缺失。最有价值的三项验证是：21:15 SC同窗曲线、21:30 CU—LME联动、21:45 MA精确跨月；下一真实窗口为2026-10-26 21:00，LH/AP等无夜盘品种为10月27日09:00。

## 1. 数据质量与覆盖

| 模块 | 实际取得 | 分析/执行状态 | 关键缺口 |
|---|---|---|---|
| 聚合输入 | [report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) 为0字节 | 不可用；转读模块文件 | 聚合层空，不据此宣称模块不存在 |
| Futures | 2026-10-26，806合约/77产品；SHFE/INE/DCE/CZCE/GFEX均同日；full_market_ready=true、source_date_match=100%、critical=0 | 分析就绪；参数未全 | 6个placeholder；成交量/OI未做官方独立核对 |
| Market State | 77产品、20日完整历史 | 分析就绪 | 产品近远月不总与代表合约同月 |
| Physical | 20目标、18 fresh、2 unavailable；18个basis全为C，eligible=0 | 仅背景 | 地区/品质/含税/交割地缺失 |
| External | 22目标、17 fresh、5 unavailable，均context_only | 可作方向映射 | repo Brent 109.74与19:26媒体约114.57冲突 |
| Night | 上一合法会话：trading_date=10/26，start=10/23，end=10/24；416/806，214 unresolved；validation/published=true，complete=false | 仅解释今日EOD前置会话 | [night_session/latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json) 0字节；不是今晚；无official night close |
| Options | 64目标、46尝试、44成功；ATM ready44、skew27、surface/positioning/execution均0；OI覆盖97.97%、bid/ask覆盖0 | 局部ATM/skew可研究，不可执行 | sampled_strikes、非全链；ZC/A失败；结构化ready与limitations文字有冲突 |
| Metadata | contract match67.49%、effective73.45%；乘数/tick/保证金/限幅覆盖约30.15% | 局部可用 | SC/CU动态保证金/限幅缺失；DCE合约信息HTTP412 |
| 官方crosscheck | SHFE238、INE63、CZCE243（close可比187）、GFEX48：三价格字段different=0；DCE HTTP412 | 四所价格独立一致 | all_equal=false来自DCE源错误，不是已观察差异；不含量仓 |
| Stock | trade_date=10/21；5568 quotes；最低财务/商品映射仅2公司 | 当前决策陈旧，不可执行 | 复权、行业、交易能力未ready；映射不含油企 |

五所EOD实际日期均为2026-10-26。今晚21:00正常交易属于10月27日，尚未发生；10月23日晚至24日凌晨的旧Night归属10月26日，日期语义无calendar_mismatch，但覆盖不全，不能当今晚行情。数据入口：[期货](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[实体](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[海外](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)、[期权质量](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[曲面](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)、[官方核对](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)。

## 2. 可追溯事实台账

| fact_id | 标的/口径 | 观测与known_at | 支持判断 | 局限 |
|---|---|---|---|---|
| F-EOD-001 | 中国806合约/77产品EOD | 10/26 EOD；19:06生成 | 日盘是本报告有效基准 | vendor完整不等于全字段官核 |
| F-SC-002 | SC2611-2612 -1.690%；SC2612 728.1/739.7 close/settle | 10/26 EOD | 原多头曲线条件失效 | 今晚未开盘 |
| F-CHEM-003 | MA/FU/BU/PX对pre-settle +6.01%/+5.31%/+4.96%/+3.78% | 10/26 EOD | 国内油化工广泛强势 | 同一冲击只算价格层 |
| F-OIL-004 | Dec Brent 114.57、WTI100.96美元/桶，-1.8%/-2.2% | 10/26欧洲时段；19:26读取 | 反对追多国内油链 | repo Brent口径冲突 |
| F-CU-005 | HVC罢工，矿山降负荷 | 10/24发布 | 铜实体催化 | 影响取决于持续时间，未量化吨数 |
| F-OPT-006 | Options 64/46/44；ATM44、skew27、exec0 | 10/26 EOD；19:14生成 | 局部IV/skew可研究 | 无bid/ask、非全链 |
| F-PHY-007 | Physical 18/20；basis C=18、eligible=0 | 10/26；19:14生成 | 实体现货仅背景 | 不可称可交割套利 |
| F-NIGHT-008 | 旧Night 416/806，214 unresolved | 10/23—24；10/24 05:58生成 | 只解释今日前置夜盘 | raw latest为空、非今晚 |
| F-XCHK-009 | 四所价格0差异、DCE412 | 10/26 EOD | 四所价格字段可信度提高 | DCE与量仓未核 |
| F-STOCK-010 | Stock trade_date10/21、映射2公司 | 10/21；10/22可知 | 仅作旧证据映射 | 不能作今晚股票执行依据 |

海外即时油价来自[WSJ 10月26日](https://www.wsj.com/business/energy-oil/oilspot-oil-prices-fall-as-traders-weigh-u-s-iran-diplomacy-saudi-attacks-a59376cd)并由[Reuters](https://www.reuters.com/world/asia-pacific/global-markets-pix-2026-10-26/)交叉核对；HVC事件来自[Reuters 10月24日](https://www.reuters.com/business/world-at-work/teck-says-strike-begins-highland-valley-copper-mine-british-columbia-2026-10-24/)。这些与仓库缓存不是同一来源，但不同时间/合约口径不做机械套利比较。

## 3. 12项仪表盘

| 标的 | close/settle | 1D / 5D | 量仓 | 曲线 / Physical | Options | 结论 |
|---|---:|---:|---|---|---|---|
| MA701 | 3389 / 3346 | +6.01% / +5.25% | vol 332.3万；OI95.3万；ΔOI+66968 | MA611-612 +6.50%，非701 pair；basis C | MA612错月，ATM IV53.74% | 强但不追 |
| FU2701 | 5295 / 5238 | +5.31% / +5.67% | vol94.0万；ΔOI-8047 | FU2611-12 +13.22%，非2701 pair；C | 错月，IV-RV+25.51pct | 旧多窗口过期 |
| PX612 | 9782 / 9820 | +3.78% / +4.31% | ΔOI+18101 | PX611-12 +1.45%；C | 10/28到期，IV41.88% | 强价强仓，临到期 |
| SC2612 | 728.1 / 739.7 | +1.55% / +2.91% | ΔOI-2071 | SC2611-12 -1.69% contango | ATM740 IV68.31%，高RV21.62pct | 原多失效，等反弹空 |
| BU2701 | 4828 / 4738 | +4.96% / +6.47% | ΔOI+12310 | BU2611-12 +7.13%，非2701 pair | 错月，IV-RV+10.94pct | 内强外弱 |
| SH701 | 1512 / 1554 | -5.44% / -9.76% | vol z2.41；ΔOI-18 | SH611-12 +3.76%反对做空 | 错月，IV-RV+20.92pct | 价格—曲线冲突 |
| AG2612 | 13040 / 13050 | -1.55% / -6.49% | ΔOI-9509 | -0.16% contango | ATM IV39.95% | 低位不追空 |
| CU2612 | 108110 / 108180 | +0.81% / -0.90% | ΔOI+6896 | CU2611-12 +0.65%；basis C | ATM IV13.00%，+1.66pct | 罢工催化，响应温和 |
| AL2612 | 23450 / 23475 | +1.19% / +2.00% | ΔOI-1134 | +1.17%；basis C | IV11.20%，略低RV | 偏多但催化弱 |
| LH2701 | 9560 / 9730 | -2.94% / -5.72% | ΔOI+3392 | -6.12% contango | 无合格core | 次日日盘条件空 |
| AP701 | 5542 / 5591 | -3.21% / -5.69% | ΔOI+4498 | AP611-12 +10.68%，仅5观测 | IV34.30%，RR25 -3.96 | 分歧大，不做方向 |
| EC2611 | 2403.5 / 2421.5 | -1.17% / -12.77% | ΔOI-2035 | -8.67% contango | 无 | 移仓/流动性优先 |

注：1D为close相对pre-settlement；settlement仅用于结算/保证金/限幅基准。旧Night raw为空，本表不伪造Night close、OHLC或ΔOI。repo海外为context-only；其Brent 109.74与19:26媒体约114.57不一致，已隔离。

## 4. 相比前序的真变化与旧观点处置

1. **SC多头被否定。** 早间稳定idea `COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021`要求backwardation和回踩收复；日盘SC2611-12却为-1.690% contango，close低于settle1.57%。原参数不移动，标记invalidated；反向研究用新child ID，不抹去失败。
2. **FU不追认触发。** FU2701日盘虽涨5.31%，但收5295低于早间5360确认价，且无成交回执；原09:15—09:45序列已过，状态为窗口过期/未知，不是“持有”。
3. **化工内强外弱。** MA/PX/BU/聚烯烃普涨，而Brent欧洲时段约跌1.8%；这既可能是中国补库/风险溢价，也可能是挤仓，21:00需验证信息弹性。
4. **铜由事件线索升为三层候选。** HVC罢工正式开始，CU日盘价/OI与backwardation同向，但海外同窗确认和产量损失仍缺。
5. **期权数据更新但执行能力未变。** 44个产品成功、27个skew ready，不等于完整曲面或可成交；0 bid/ask使所有腿只停留在研究。
6. **AG不再允许低位追空。** 晨间反抽失败条件未获顺序证据；现价13040已低于原“不追”阈值，不能事后确认成交。

实际持仓状态一律“未提供/未知”；OHLC穿越不证明条件顺序或成交。

## 5. 产业链与传播路径

- **原油→SC/FU/BU→芳烃/聚酯/甲醇：** 国内日盘最强、海外油价回落。SC精确近月contango支持回吐，BU/FU产品近月升水支持紧张，但非代表合约精确pair。最大缺失是可比Brent合约、合格实体和今晚同窗曲线；置信度中。
- **原油/煤→MA/PP/L/EB：** MA强价强仓、产品近月升水大，PP/L/EB同步上涨；但basis全C、MA期权错月。若21:00守强可确认中国相对强势，否则按挤仓回吐处理；置信度中低。
- **铜矿→冶炼→CU/BC：** HVC罢工是独立供给事实，CU价格/OI与曲线温和确认；最强竞争解释是市场预期罢工短暂。下一观测是LME同窗与曲线≥0.8%；置信度中。
- **铁矿/焦煤→钢材：** I/RB近乎平、JM弱；未出现价差与实体同时改善，宝钢旧映射也不能证明今晚利润扩张。无合格新机会；置信度低。
- **饲料/油脂→LH及软商品：** LH价格与contango同向偏空，但DCE官核缺失、无夜盘；AP价格弱却backwardation强，方向冲突。下一真实窗口10月27日09:00；置信度低至中。

## 6. 统一机会榜

| 排名 | idea_id / 方向 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 五层证据 | 研究 / 证据 / 执行 |
|---:|---|---:|---:|---|---|
| 1 | COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026 空 | 21/17/17/13/4 | 72 | 支持1/2/4；反对/缺失3/5 | priority / 三层 / 等21:15—21:30 |
| 2 | COM-M-CU2612-HVC-STRIKE-WATCH-20261025 多 | 20/15/16/11/8 | 70 | 支持1/2/3；4待核、5中性 | priority / 三层 / 等LME+回踩 |
| 3 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 多 | 20/15/15/14/4 | 68 | 支持1/2；反对4/5，3缺失 | watch / 两层 / 缺精确pair |
| 4 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 多 | 19/14/15/14/5 | 67 | 支持1/2；反对4 | watch / 两层 / 不可执行 |
| 5 | COM-E-LH2701-TREND-CONTANGO-SHORT-20261026 空 | 19/16/12/13/6 | 66 | 支持1/2；3/4/5缺失 | watch / 两层 / 次日日盘 |

分数是研究优先级，不是胜率。所有分项均在25/25/20/15/15上限内并重算为总分；一层/两层候选分别受59/69上限约束。

## 7. 三张研究/交易卡

### 7.1 SC2612曲线反转条件空

- **事实与错价：** close728.1、settle739.7、pre-settle717；日盘结算仍高3.17%，但收盘低结算1.57%，SC2611-12=-1.690% contango。海外Brent约114.57、跌1.8%。市场可能仍给日盘供应风险高溢价，而近月相对次月已转弱。
- **触发顺序：** 21:15 SC≤724 **AND** SC2611-12≤-1.0% **AND**可比Brent≤114.5；随后反弹724—730失败，并在21:30后5分钟收盘<723。721—724分40%/60%；首个可成交<716放弃。
- **风险/退出：** 计划止损735；曲线>-0.5%持续15分钟或Brent>117为逻辑失效；TP1 704、TP2 686；10月28日14:45时间退出。
- **可达性：** 好/中/坏入场724/723/721，毛风险11/12/14点；TP1毛R1.82/1.58/1.21，TP2 3.45/3.08/2.50。费用滑点未知，不得当0。
- **参数：** 1000桶/手、tick0.1元/桶=100元/手为静态规则；仓库last trade 2026-11-30。动态保证金/限幅缺失，必须交易前复核。
- **期权：** 11/12 ATM740 IV68.31%，较RV20高21.62pct；无bid/ask，不称put spread便宜或有限损可执行。
- **预算/压力：** 试仓≤0.35% NAV、确认≤0.75%，油链合并≤1.25%；压力含1/2限幅、夜盘gap、保证金上调、地缘反转。

### 7.2 CU2612罢工弹性条件多

- **新增事实：** CU2612 close108110、settle108180，1D+0.81%、ΔOI+6896，CU2611-12 +0.647%；HVC已罢工并降负荷，影响取决于持续时间。
- **触发顺序：** 21:30前CU≥108800 **AND**曲线≥0.80% **AND**可比LME铜不低于19:26参考；先突破再回踩108800—109200守住，30%/70%。首个成交>110000放弃。
- **风险/退出：** 计划止损107600；曲线<0.20%持续15分钟或罢工结束失效；TP1 111500、TP2 114000；11月5日退出。
- **可达性：** 108800/109000/109200入场，风险1200/1400/1600元/吨；TP1毛R2.25/1.79/1.44，TP2 4.33/3.57/3.00，未扣费。
- **参数：** 5吨/手、tick10元/吨=50元/手；last trade 2026-12-15；动态保证金/限幅缺失。期权ATM108000 IV13.00%、RV11.34%，无bid/ask。
- **最强反证：** 价格响应温和可能已表达“罢工短暂”；美元/实际利率上行会抵消供给利多。试仓≤0.35%、确认≤0.75%，与矿业股合并≤1.25%。

### 7.3 MA701油化工相对强势研究闸门

- **事实：** close3389、settle3346、pre-settle3197，1D+6.01%、5D+5.25%，vol z2.10、OI+66968；MA611-12升水6.50%，但不是701精确pair。
- **条件：** 21:15守3350，随后5分钟收盘≥3400，精确MA701-next curve为正且PX612≥9750；3390—3410分批。**精确pair未取得前不可执行。**
- **风险/退出：** 计划止损3330；曲线转负或PX<9600失效；TP1 3500、TP2 3620；10月29日14:45退出。
- **可达性：** 3390/3400/3410入场，风险60/70/80点；TP1毛R1.83/1.43/1.13，TP2 3.83/3.14/2.63。净R最坏边界不足1则放弃。
- **参数：** 10吨/手、tick1元=10元/手；保证金11%、限幅9%、last trade 2027-01-14；夜盘时段字段缺失需复核。MA612期权错月、无bid/ask。
- **竞争解释：** 广泛化工上涨可能是短期空头回补，basis C不能提供实体确认。预算试仓≤0.25%、确认≤0.50%，并入油链≤1.25%。

## 8. 商品期权专项

样本是`core_v1 / sampled_strikes`，不是完整链。44个series局部ATM ready，27个skew ready；完整曲面、跨期、positioning、dealer gamma方向和execution均不可用。quote_coverage_complete若出现只指计划采样腿，不代表全链。

- **SC2612 11/12：** ATM740 IV68.31%，RV20 46.69%，IV-RV+21.62pct。方向空不等于put便宜；无bid/ask。
- **CU2612：** ATM108000 IV13.00%，RV11.34%，差+1.66pct；局部ATM可用于事件Vega研究，不能给净权利金。
- **AL2612：** ATM23400 IV11.20%，略低RV0.63pct；没有催化和报价，不据此做多波动。
- **AP701：** ATM5600 IV34.30%、RR25 -3.96，负skew与价格弱一致，但backwardation强、仅5个曲线观测，方向冲突。
- **RM701/SA701：** RR25分别约+1.36/+1.52；仅局部偏度，不推全链PCR、拥挤或dealer gamma。
- **错月隔离：** MA/FU/BU/SH/TA期权标的与仪表盘代表合约不同，不纳执行和第五层。PX期权10月28日到期，Gamma/交割风险高。

结构备选只能在21:00后重算moneyness、Delta、到期和真实买卖盘；在此之前最高净支出、最大损失、滑点和盈亏平衡均“待询价”。

## 9. 21:00夜盘风险地图

官方日历入口为[INE Trading Calendar](https://www.ine.cn/eng/reports/calendarholidays/calendar/)。今晚会话属于10月27交易日；19:26没有未来Night数据。三层基准是：10月26日EOD；10月23—24日旧Night只作今日EOD前置；19:26海外油价约跌2%、HVC罢工仍在。

| 开盘情景 | 油链/化工 | 铜/贵金属 | 操作纪律 |
|---|---|---|---|
| 高开 | MA/BU若>日盘高位不追；SC高开先看曲线是否仍contango | CU>110000放弃追多；AG反抽不等于趋势反转 | 21:15核价格+曲线+外盘，先不下结论 |
| 平开 | SC 724—730反弹失败才研究空；MA守3350再核精确pair | CU需≥108800且曲线≥0.8% | 21:30要求第二条件，不能只凭一次触价 |
| 低开 | SC<716不追空；化工低开先排除外油传导 | CU跌破107600取消多头；AG低位不追 | 21:45再核二次收盘、量仓仅作线索 |
| 内外冲突 | 国内化工强而Brent弱时优先减杠杆 | LME不确认则铜降至观察 | 不做跨市场套利，因合约/汇率/税运费未对齐 |

LH、AP等无夜盘品种下一真实窗口为10月27日09:00；不因今晚无报价扣分，也不虚构盘前触发。

## 10. 未来24小时/7日事件与Stock联动

- [USDA NASS日历](https://www.nass.usda.gov/Publications/Calendar/print.html?month=10&view=c&year=2026)：Crop Progress常规窗口约10月27日04:00 BJT；谷物/油籽只在正式发布后重评。
- [Federal Reserve](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)：FOMC 10月27—28日会议；贵金属、铜、原油面临美元/实际利率和Vega跳变，线性仓先减、无报价不买卖Vega。
- [EIA](https://www.eia.gov/petroleum/supply/weekly/schedule.php)：WPSR常规周三10:30 ET，即10月28日22:30 BJT；油链事件前主题风险减半。
- 中东/Hormuz/沙特运输与HVC罢工：只把实际供应、出货或产量变化计入实体层，标题不重复计数。
- [INE 11月2日价差指令扩围](https://www.ine.cn/eng/circularnews/circular/202610/t20261023_833811.html)：是执行制度变化，不是价格催化。
- Stock限定检索：中国石化600028、中国海油600938、紫金矿业601899，使用[上交所最新公告](https://www.sse.com.cn/disclosure/listedinfo/announcement/)与[预约披露](https://www.sse.com.cn/disclosure/listedinfo/periodic/)；截至截点未取得三家公司新的经营披露，新增证据0。Stock engine仍停在10月21日且映射仅紫金/宝钢；油企利润桥只能列待验证假设。
- 利润桥：中国海油是油价→实现售价，受销量/成本/税费/汇率/套保约束；中国石化上游受益与炼化原料、库存损益相反；紫金是铜价→矿产铜售价，受自产/冶炼、产量、成本、套保和少数股东约束。三者均缺当前报价、流动性与证券执行核验，股票不优于直接商品期货表达。

## 发布前校验

覆盖：77产品全范围初筛；五板块+航运均汇报。评分：五项分量与总分重算通过。日历：今晚归属10月27日，无未来行情。合约：MA参数可用，SC/CU动态参数局部缺失。语义：旧触发不移动、不假定持仓、不用OHLC证明成交。未解缺口：聚合与raw Night空、Brent源冲突、DCE官核412、basis全C、options bid/ask为0。CI状态：pending_or_unverified。

A. 今晚没有应立即建立的新仓位。
B. 今晚仅应挂条件的候选：SC2612曲线反转空、CU2612罢工弹性多；MA701须先补精确跨月报价。
C. 今晚继续观察：BU2701内外分歧、LH2701次日日盘空、SH/AP价格—曲线冲突、AG低位去杠杆。
D. 今晚必须回避或有条件退出：追认早间SC/FU多头、把旧Night当今晚、Brent口径冲突下下单、零bid/ask或错月期权、DCE未官核品种即时执行。
