# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-10｜Revision 2

`prompt_version=radar_2026-09-06_coverage_v1`  
补跑/当前决策版。实际生成：2026-09-10 23:40 BJT；研究截点：23:40 BJT。China-Commodities-Engine 数据截点约23:18 BJT。9月10日完整中国EOD已补齐；今晚21:00开始、归属9月11日交易日的Night Session已经发生，但repo尚未发布该session的完整快照，因此不把21:00/15/30/45分钟窗口继续写成未来条件。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易。** 9月10日EOD确认能化维持高位，但SC/FU/EB的大部分新增价格发现已在早前Night完成，日盘没有继续加速；当前Night实时路径又不完整，且EIA在00:00/02:00 BJT临近。研究上仍偏多SC，执行上不追。

当前regime：**Middle-East supply shock / high-level China acceptance but fading marginal elasticity / post-PPI stagflation repricing / energy breadth / metals macro conflict / options surface-ready but execution veto**。

最值得继续验证的三项：SC2610、EB2610、FU2611。共同缺口不是EOD，而是**当前已开Night的完整价格/OI路径、EIA后的再定价和可执行盘口**。FU/EB等23:00收盘品种的当晚窗口已过，下一有效窗口是9月11日09:00；SC仍在交易，但当前quote未能可靠刷新且EIA临近，因此不建立新仓。

## 二、数据质量与覆盖

本次重新读取[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[night_session/last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[radar_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并下钻latest、market_state、physical、external、Night、Options和contract metadata。

- **统一输入已恢复到T日。** `schema_version=2`，`requested_date=2026-09-10`，23:18生成；Futures/Market State于22:57生成。
- **核心期货完整。** 五所共802合约，802/802源日期匹配，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；7条placeholder剔除，无重复、非法OHLC、负量仓。
- `official_complete=false`来自辅助层：basis/member rankings不可用、仓单部分carry-forward、metadata部分失败，不等于核心EOD失效。
- **早前Night**：`trading_date=2026-09-10`、`night_session_date=2026-09-09`，05:59生成，fresh/validated/published；588有效合约、55产品，192 outside-window、20 no-night-trade、2 query error、2 unresolved，`coverage_complete=false`。这是今天已完成连续交易，不是当前Night。
- **当前Night**：21:00后归属9月11日交易日，已经开始；repo尚无完整快照。公开页只可靠取得SC2610 21:10早期点，不足以验证23:40路径，故记`truncated/current_path_unverified`，不假设先前条件触发。
- **Physical**：23:18生成，20目标中18 fresh，SC/LU unavailable；无carried/stale target。basis多为C级，不能进方向评分/套利；孤立现货绝对值不自动构成完整实体层。
- **External**：23:18生成，17/22 fresh；Dubai/Oman、Singapore HSFO/VLSFO、exact USD/CNH、DXY unavailable；全部`context_only`。repo值WTI约100.17、Brent约105.61、LME 3M铜约14235。
- **Options**：9月10日24,154合约、403 series、64/64产品；IV coverage 98.15%、OI coverage 69.65%、bid/ask 0；`surface_ready=true`、`positioning_ready=false`、`execution_ready=false`，Dealer Gamma未知。独立`data/options/surface_latest.json`为空，与report_input内嵌403个series及quality状态存在一致性异常；本期只把内嵌series用于研究。
- **Metadata**仍partial；动态margin/limit未确认不猜。

因此本次与19:48 revision的区别是：**T日EOD和T日期权已补齐，旧版“EOD missing”理由取消；当前执行限制转为“当前Night路径未完整验证 + 已过23:00窗口 + EIA临近”。**

## 三、商品仪表盘

1D/5D采用同一当前合约结算收益；Night为归属9月10日交易日的早前已完成阶段；Day仅在exact-contract对齐时按`EOD close / Night close - 1`。

| 板块 | 合约 | EOD close/settle | 1D/5D | Volume / OI / ΔOI | Curve | 早前Night；overnight；Day | 当前结论 |
|---|---|---:|---:|---|---|---|---|
| 原油 | **SC2610** | 769.0/768.4 | +6.35%/+11.22% | 231,915/34,350/**-4,884** | **+6.47% back** | 773.1；+4.26%；**-0.53%** | 高位接受、边际弹性降；当前quote缺，EIA前不追 |
| 燃料 | **FU2611** | 4044/4101 | +4.25%/+6.13% | 975,788/215,949/**+109** | **+6.66% back** | 4119；+3.00%；**-1.82%** | 23:00已过，次日日盘重评 |
| 苯乙烯 | **EB2610** | 10307/10282 | +5.07%/约+7% | 1,696,448/321,827/**+28,335** | +0.76% back | 10329；+4.04%；**-0.21%** | 量价仓强，但日盘未加速 |
| 乙二醇 | **EG2610** | 5917/5987 | +3.15%/+3.03% | 2,327,269/336,016/**-4,142** | +3.81% back | 6020；+2.92%；**-1.71%** | 高位接受/日盘回吐 |
| PP | **PP2701** | 8939/8953 | +2.45% | 923,723/652,822 | +1.90% back | 8960；+1.83%；**-0.23%** | 能化breadth，窗口已过 |
| PTA | **TA701** | 6234/6258 | +1.82% | 1,267,006/1,131,197 | +5.86% back | 6238；+0.81%；**-0.06%** | 横盘消化 |
| PX | **PX611** | 9274/9292 | +2.67% | 361,157/172,503 | **-4.61% contango** | — | 价格强、curve反对，不追 |
| 沥青 | **BU2611** | 5084/5089 | +2.87% | 231,323/259,832 | +3.08% back | — | 只作breadth |
| 纯苯 | **BZ2610** | 9227/9150 | +5.11% | 113,291/32,727 | **-3.30% contango** | — | spike不追 |
| 铜 | **CU2610** | 结算约111730 | +0.55%/+2.31%(3D) | 价涨仓增线索 | +0.61% back | Night 111910 | 结构尚强，关税催化反证 |
| 白银 | **AG2610** | 约16418/16425 | +1.76% | 630,856/189,315 | 小幅back | — | PPI后海外弱，白天EOD不再代表当前宏观 |
| 玻璃 | **FG701** | 964/962 | -0.82% | 1,380,559/1,196,197 | **-5.85% contango** | — | 偏弱但不追空 |
| 红枣 | **CJ701** | 7720/7820 | settle -1.08%；close -2.34% | 166,313/221,250 | **-16.74% contango** | 无夜盘 | 次日日盘偏空观察 |
| 生猪 | **LH2611** | 11570/11630 | -1.15% | 148,502/238,918 | **-7.05% contango** | 无夜盘 | 弱势观察 |
| 锂 | **LC2701** | — | 弱势历史未扭转 | — | — | 无夜盘 | 无高于能化的edge |

**路径分解是本次最重要信息：** SC、FU、EB、EG、PP、TA的大部分新增定价发生在早前Night，日盘高位接受或小幅回吐，而非继续加速。SC +4.26% overnight / -0.53% Day；FU +3.00%/-1.82%；EB +4.04%/-0.21%；EG +2.92%/-1.71%。

## 四、相比上一交易日/19:48 revision真正变化

1. **9月10日EOD缺失问题消失。** 核心期货恢复802/802同日、full-market-ready，不能再用“数据不足所以不交易”。
2. **SC确认高位但没有确认日盘加速。** settle +6.35%、5D +11.22%、back升至6.47%，但OI下降12.45%、Day约-0.53%；更像高位接受而非第二段加速。
3. **FU/EB/EG/PP/TA形成breadth，但多数日盘回吐Night扩张。** 最佳表达从追能化改为下一窗口的回撤接受/相对强弱。
4. **美国PPI已落地。** 8月PPI同比5.4%，略高于预期；10Y收益率升至约4.92%，加息定价升温，贵金属和工业金属承压，而油价因供给风险独立走强。[Reuters PPI](https://www.reuters.com/business/sp-500-dow-futures-attempt-recovery-ahead-inflation-report-2026-09-10/)
5. **外油比19:30更强。** repo 23:18 context为WTI约100.17、Brent约105.61；Reuters同日盘中亦报道WTI重新越100、Brent约105。[Reuters Oil](https://www.reuters.com/business/energy/brent-holds-above-100-tanker-attacks-deepen-supply-fear-2026-09-10/)
6. **期权从T-1恢复到T日研究曲面，但仍不可执行。** 64/64产品、surface-ready；bid/ask=0、positioning不足、execution-ready=0。

## 五、产业链地图

**SC—FU—LU—BU：最强但不追。** 价格、backwardation、外油与地缘供给风险支持；SC OI下降、FU日盘回吐Night及供应链适应是反证。方向仍偏多，执行赔率下降。

**EB—BZ—PX—TA—EG：能化扩散明确，但结构不统一。** EB价涨仓增最强，EG/TA/PP有back；PX/BZ处contango。最强竞争解释是原油成本冲击beta，而不是所有化工品同步短缺。

**贵金属：PPI后的宏观冲击覆盖中国白天信号。** AG白天上涨，但PPI发生在中国收盘后；下一完整中国价格窗口才重新评价。

**铜—有色：结构尚强，催化转弱。** CU轻back、LME高位；白宫对精炼铜关税决定延后削弱此前溢价。[Reuters Copper](https://www.reuters.com/world/us/white-house-copper-tariff-plan-stalls-amid-affordability-concerns-sources-say-2026-09-10/) 不自动反手空。

**农产品/建材：无更优立即赔率。** 中国新增采购美国大豆是催化，但国内油粕需价格响应；FG/CJ/LH结构弱却缺第三层确认。[Reuters Soybeans](https://www.reuters.com/world/china/china-buys-1-million-tons-us-soybeans-ahead-xi-visit-sources-say-2026-09-10/)

## 六、机会排行榜

| 排名 | idea_id / 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | `COM-E-SC2610-GAP-20260905` / SC2610高位接受后续多 | 22/10/19/13/8 | **72** | 1、2、4 | 待验证优势｜部分｜当前quote/path缺，EIA前不执行 |
| 2 | `COM-E-FU2611-PRODUCT-TIGHT-20260908` / FU2611次日日盘回撤多 | 20/12/16/12/9 | **69** | 1、2、4 | 待验证优势｜部分｜今晚窗口已过，9/11 09:00 |
| 3 | `COM-E-EB2610-DAY-REVERSAL-20260909` / EB2610扩散延续 | 20/11/16/12/10 | **69** | 1、2、4 | 待验证优势｜部分｜当前夜盘已收，次日日盘 |
| 4 | 新观察 / CJ701顺结构弱势 | 18/16/8/13/11 | **66** | 1、2 | 待验证优势｜部分｜无夜盘，9/11 09:00 |
| 5 | `COM-E-MA701-ROLL-RESET-20260910` / MA701 rollover重估 | 19/13/14/10/9 | **65** | 1、4；第2层降级 | 证据不足｜部分｜roll/curve pair不一致，重建锚点 |

SC达到70+只代表研究优先级。**当前仍无立即执行合格新交易。**

## 七、前三名研究/交易卡

### 1. SC2610｜偏多研究，当前不执行｜72

9/10 EOD 769.0/768.4；1D +6.35%、3D +11.60%、5D +11.22%、RV20约39.56%；ΔOI=-4,884；curve +6.47% back。Night 773.1，overnight +4.26%，Day -0.53%。市场已显著计入Hormuz/供给风险；分歧在于**方向未必错，但追价赔率差**。

21:00后的当前Night已经发生，但repo未给完整路径。公开二级页在21:10记录SC2610约806.8、开盘约815、早段802.9—815.1；这是过时的早期点，只能证明曾大幅gap，不能作为23:40成交依据。[secondary quote](https://www.iweiai.com/hangqing/sc2610)

**执行：今晚不新增。** 原19:48“21:45回撤接受”窗口作废。EIA两批数据后优先在9/11 09:00重建锚点：仅当隔夜仍高位、日盘回撤守住前夜价值区且curve不明显收窄时1/3试多；跌回768—776下并伴curve收窄则取消。新仓TP1=1.5R、TP2=3R，1—2D时间止损，最大计划损失0.25%—0.40% NAV。SC 1000桶/手、tick 0.1、tick value 100元；按768.4名义约76.84万元；LTD 9/30，实物交割。动态margin/limit下单前官方复核。

### 2. FU2611｜次日日盘回撤多研究｜69

EOD 4044/4101；1D +4.25%、5D +6.13%、RV20约41.21%；OI较前日仅+109；curve +6.66% back。Night 4119，overnight +3.00%，Day -1.82%。反证是日盘未延续Night，且产品供应链有适应空间。

FU夜盘23:00已结束，本补跑不能再下当晚条件单。9/11 09:00若4040—4100回撤后重回4100/4119，且外油保持强势、curve不明显收窄，可1/3试多；接受4035以下取消。TP1 1.5R、TP2 3R，1—2D；风险0.25%—0.35% NAV，与SC/EB合并因子。FU 10吨/手、tick1、tick value10元；动态margin/limit官方复核。

### 3. EB2610｜能化扩散延续研究｜69

EOD 10307/10282，settle +5.07%；Volume 169.6万、OI 321,827，较前日+28,335；curve仍back约0.76%但z偏弱。Night 10329，overnight +4.04%，Day -0.21%。价格和OI支持，但大部分上涨已在Night完成，curve确认弱于SC/FU。

今晚23:00窗口已结束。9/11 09:00只有10280—10330再次被接受、随后重夺10346且OI不明显回吐才1/3试多；接受10010以下失效。TP1 1.5R、TP2 3R，1—2D；风险0.25%—0.35% NAV。动态margin/limit/LTD下单前官方复核。

## 八、商品期权专项

9月10日期权研究层恢复，执行层仍为零：64/64产品、24,154合约、403 series；IV 98.15%，OI 69.65%，bid/ask 0，`surface_ready=true`、`positioning_ready=false`、`execution_ready=false`。

SC2610 9/11到期：underlying settle 768.4、ATM 770、ATM IV约**73.83%**，RR25约+0.17、BF25约-2.73，OI coverage 88.4%，execution=false；对比RV20约39.56%，IV-RV约+34.3 vol。极短到期+EIA/地缘风险意味着不能仅凭IV-RV正差判断“昂贵”并卖波。SC2611 10/14到期ATM IV约57.66%，同样无execution。

Dealer Gamma方向未知；无bid/ask，不输出净支出、成交价、滑点或可执行结构。独立`surface_latest.json`为空的模块异常使研究层也需额外降一级信任。

## 九、当前Night / 下一开盘风险地图

21:00已经过去，不能继续把开盘或15/30/45分钟窗口当未来。

| 品种 | 当前状态 | 过去窗口处置 | 下一有效窗口 |
|---|---|---|---|
| SC | 当前Night仍在交易，但repo路径未更新 | 原21:45条件作废；EIA前不新增 | EIA后或9/11 09:00 |
| FU/EB/EG/PP/TA/PX/MA | 23:00夜盘已结束，当前close未被repo验证 | 当晚条件全部过期 | 9/11 09:00 |
| AU/AG/CU/AL | 部分仍有夜盘，当前国内路径未验证 | 不用19:30锚直接下单 | PPI后完整Night/次日EOD |
| FG/SA/V/J/JM | 结构冲突/方向不足 | 不追首跳/首跌 | 9/11 09:00 |
| CJ/LH/LC/SI/PS/SF/SM/JD | 无对应当前夜盘 | 不适用 | 9/11 09:00 |

当前最重要时间风险是**EIA**：9月10日12:00和14:00 ET分批发布，即北京时间9月11日00:00和02:00。[EIA schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php) SC在02:30前仍面临第二次事件跳跃。

## 十、未来24h / 7d

- **9/11 00:00、02:00 BJT：EIA WPSR分批发布。** 能源不在数据前追加Delta。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **9/11 20:30 BJT：美国8月CPI。** 贵金属、有色和油价面临美元/实际利率二次重置。[BLS CPI](https://www.bls.gov/schedule/news_release/cpi.htm)
- **9/11：SC2610期权最后交易日。** 极短到期gamma/expiry风险上升；无实时quote不卖波。[交易日历](https://www.shcifco.com/Index/calendar)
- **9/12 00:00 BJT：USDA WASDE。** M/Y/P/OI/C等农业敞口避免事件前无保护加码。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- 持续监控Hormuz、油轮/炼厂、OPEC供给和中国替代采购；这些改变收益分布，不自动提供入场价。

## 十一、覆盖核对、台账与风险

**覆盖核对：** mandatory 63个代码全部在full-market初筛中完成价格/量仓/curve及1D/3D/5D/20D可得指标扫描；动态品种也由802合约全市场输入筛选。黑色建材最值得看FG弱结构但无实体确认；有色为CU结构强/关税反证、金银PPI后宏观覆盖；能化最强SC/FU/EB/EG/PP/TA，PX/BZ contango为反证；新能源无独立高分；农产品CJ/LH偏弱且美豆采购待国内响应；软商品CJ最异常。64个期权产品全部取数。方向、curve/calendar、basis、跨品种/跨市场、相对价值、中性、vol/skew/event convexity均扫描；C级basis、无exact parity和无bid/ask使套利/期权执行不成立。

**旧建议台账：** `COM-E-SC2610-GAP-20260905` 75→72：新EOD确认高位，但Day -0.53%、OI显著下降，且21:00大gap使原窗口作废；不假设成交。`COM-E-FU2611-PRODUCT-TIGHT-20260908` 73→69：Day -1.82%、OI近乎不变，窗口已过。`COM-E-EB2610-DAY-REVERSAL-20260909` 71→69：价涨仓增支持，但Night已完成大部分上涨、curve确认变弱。旧`COM-M-MA610-SETTLE-RECLAIM-20260908`不静默迁移：当前main切换MA701且curve pair roll flag，建立新研究ID `COM-E-MA701-ROLL-RESET-20260910`。`COM-M-CU2610-LME-RECORD-20260909`继续降级，不反手追空。

若下一窗口重启，新试仓最大损失0.25%—0.40% NAV；确认交易0.75%以内起步。SC/FU/EB/MA/EG/TA/PX/BU同属油价—地缘—输入通胀因子，合并主题风险暂不超过1.0% NAV，直到EIA/CPI释放。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；21:00初始窗口已经过去，SC当前实时路径未可靠核验且00:00/02:00 EIA临近，原19:48条件单全部作废而不是顺延。  
C. 今晚应继续观察的机会：SC2610 EIA后/9月11日09:00高位接受，FU2611与EB2610次日日盘回撤确认，CJ701结构弱势，以及PPI后AU/AG/CU的下一完整中国价格响应。  
D. 今晚必须避免或退出的交易：追SC大gap、把9月10日早前Night当当前Night、把FU/EB已关闭的23:00窗口继续写成可挂单、用C级basis做套利、在execution_ready=false时臆测期权成本，以及把油价同因子多头拆成多笔独立风险。