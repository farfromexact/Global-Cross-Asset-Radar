# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-18｜版本：commodities_morning｜prompt_version：radar_2026-10-12_stock_v1｜数据协议：china_commodities_core_2026-10-17_v1**  
**生成时间：2026-10-18 07:05北京时间｜研究截点：07:00北京时间**

## 一、今天一句话结论

**截至本报告时点，无可立即执行的合格新交易；周日休市，周五夜盘已预交易油价风险，周一只等待SC、FU、SA条件确认。**

已研究但优势不足：追涨原油/燃油、追空锂和苹果、贵金属反弹。研究机会存在但等待条件/报价：SC2612、FU2701、SA701。数据不足不能判断：DCE夜盘214合约、当前期权成本与成交性、A级/B级基差套利。下一窗口为**2026-10-19 09:00中国日盘**；最有价值的验证是SC/FU高开后的留存、SA弱趋势中的供应商快照反弹、10:00中国宏观数据后的二次定价。

## 二、时间、数据质量与覆盖

### 2.1 会话与Night语义

- 最近完整中国EOD为**2026-10-16**；2026-10-18为周日，无中国商品日盘。下一实际日盘为**2026-10-19 09:00**。
- Core本次把10月16日晚至17日凌晨会话正确标为 `trading_date=2026-10-19`、`night_session_date/session_start_date=2026-10-16`、`session_end_date=2026-10-17`，与官方“连续交易为下一交易日第一节”的制度一致，**无calendar_mismatch**。
- Night价格语义为 `vendor_latest_trade_asof_snapshot`；`night_last_price`/兼容字段`night_close`是供应商观察时点最新成交，不是交易所核验最终收盘。`official_night_close_verified=false`，`ohlcv_scope=vendor_realtime_unverified_session_scope`。本报告可用准确合约的时点变动衡量信息弹性，但不把OHLC、成交量、OI/ΔOI称为完整纯夜盘统计。
- Night requested=806、取得414合约/44品种，outside-window=171、制度无夜盘/无成交=7、query_error与unresolved各214（DCE），missing timestamp/price/quote=0，coverage=51.36%，`validated/published/fresh=true`、`coverage_complete=false`。

### 2.2 固定仓库版本与模块状态

- 商品引擎：[`China-Commodities-Engine@e597eb2`](https://github.com/farfromexact/China-Commodities-Engine/tree/e597eb2ae162b0e086bafc98c7fca9262f671cb0)。`report_input_latest.json` requested_date=2026-10-16，generated_at=2026-10-18T06:14:21+08:00，schema=2，目标77品种/20 core产品；统一层包含Futures、Market、Physical、External、Night、Options、Metadata和Crosscheck。
- Futures/Market：806合约、77品种、SHFE/INE/DCE/CZCE/GFEX五所，source_date_match=100%、`full_market_ready=true`、unknown/duplicate/invalid OHLC=0、critical=0；8条零量/零仓或占位记录不进入排行。
- 官方独立价格核对：SHFE 238、INE 63、CZCE 243、GFEX 48合约的可比settlement/close/prev-settlement差异均为0；DCE官方接口HTTP 412，故整体`state=partial`、`all_compared_prices_equal=false`。后者是**DCE源错误，不是已发现价格差异**。核对不覆盖成交量、OI或turnover，也不替代full-market验证。
- Physical：目标20、原生频率内有效18，SC/LU unavailable；18条basis均为C级且`eligible_for_physical_score=false`。官方仓单本次只有CZCE 23条当前值；SHFE/DCE/GFEX抓取失败，GFEX另有5条沿用值，仅作背景。
- External：目标22、fresh 17；Dubai/Oman、Singapore HSFO/VLSFO、DXY、USDCNH缺失，现有海外序列均为`context_only`，不称跨市套利。
- Options（2026-10-16）：`core_v1/sampled_strikes`，预期64品种、成功33（51.56%），740合约、33 series；IV覆盖100%、OI 94.59%、bid/ask 0%、model Greeks 0%。`core_atm_ready=32`、`skew_ready=25`，但`surface_ready=0`、`positioning_ready=0`、`execution_ready=0`、dealer Gamma方向未知。quote coverage只指采样计划，不是全链。
- Metadata：partial；有效合约匹配73.45%，乘数/tick/effective覆盖36.10%，动态保证金/限幅30.15%，夜盘制度与交割参数覆盖为0。SC2612、BR2612、AG2612有最后交易/交割日，核心乘数、tick、保证金、限幅仍缺；DCE参数缺失。
- Stock：[`China-Stock-Engine@79c96a9`](https://github.com/farfromexact/China-Stock-Engine/tree/79c96a9d9e73a7c2a13d340229acc7c64f4ec144)。最近有效trade_date=2026-10-15，research_asof=2026-10-16 07:38北京时间；本次回填因SSL失败、`data_fresh=false`。映射目录仅核紫金矿业/宝钢股份，证券执行状态与预测能力不足；本期股票候选为0。

实际读取路径：商品 `data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/night_session/latest.json`、`data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`、`data/crosschecks/futures_latest.json`；股票状态、manifest、data reference、research inputs、exposure mapping和两家公司证据分片。

## 三、商品仪表盘（展示12项；后台扫描77品种）

Night列为同准确合约供应商快照；`vs前收`可衡量截至来源时点的新增变动，但不是交易所核验夜盘收盘收益。curve为近月减次月相对次月；basis C均不可作套利确认。

| 板块/品种 | 准确主力 | 10/16 close/settle | 1D / 5D | 成交量 / OI / ΔOI | curve | Physical | 归属10/19的Night快照 | Options / 海外 | 周一信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|
| 原油SC | SC2612 | 711.8 / 723.0 | -1.85% / +0.64% | 119673 / 32965 / +3173 | +0.84% backwardation | 实体缺 | 739.8，vs前收+3.93%，vs结算+2.32%，ΔOI+763，10/17 02:30 | SC期权失败；油价供应/政策冲突 | gap已预交易，不追首跳 |
| 燃料油FU | FU2701 | 4819 / 4770 | -0.35% / +7.43% | 327042 / 211067 / +8765 | +7.92%（近端pair） | basis C | 4947，+2.66%/+3.71%，ΔOI+23709，10/16 23:00 | FU期权为2611临到期；HSFO偏紧 | 等4900–4950留存 |
| 纯碱SA | SA701 | 939 / 940 | +0.21% / -7.02% | 1039014 / 1365611 / -11911 | +1.98% | basis C | 956，+1.81%/+1.70%，ΔOI-20379，23:00 | ATM IV25.41，RR25 +2.68；不可执行 | 弱趋势中的反弹验证 |
| 丁二烯胶BR | BR2612 | 15915 / 15975 | +1.79% / -2.41% | 105309 / 75757 / +9537 | +1.10% | 缺 | 15935，+0.13%/-0.25%，ΔOI-305，23:00 | 期权为BR2611，不匹配 | EOD强，Night未跟随 |
| 白银AG | AG2612 | 14029 / 13889 | +2.49% / -4.31% | 323505 / 282779 / -10546 | -0.10% | 缺 | 13835，-1.38%/-0.39%，ΔOI+1639，02:30 | AG期权失败；金价周线承压 | EOD反弹被夜盘回吐 |
| 黄金AU | AU2612 | 901.82 / 898.80 | +1.36% / -0.03% | 194252 / 222956 / -620 | -0.13% | 缺 | 898.6，-0.36%/-0.02%，02:30 | AU期权失败 | 内外利率冲突，观察 |
| 铜CU | CU2611 | 109860 / 109450 | +0.10% / -0.15% | 106448 / 176863 / -12136 | +0.63% | basis C | 109420，-0.40%/-0.03%，02:30 | LME铜仅context | 去仓、缺宏观确认 |
| 碳酸锂LC | LC2701 | 96320 / 99080 | -4.20% / -16.56% | 358976 / 425349 / +6802 | +0.92% | spot101000、basis C | 制度无夜盘 | ATM IV50.75，skew未就绪 | 弱价/曲线冲突，禁追空 |
| 苹果AP | AP701 | 5998 / 6096 | -3.32% / -11.68% | 246249 / 169454 / +8417 | +15.11% | 缺 | 制度无夜盘 | ATM IV29.88，RR25 -2.62 | 交割结构优先，禁追空 |
| 豆粕M | M2701 | 3281 / 3299 | -1.77% / -2.66% | 1234349 / 2321910 / -61019 | -1.69% | spot3358、basis C | DCE query_error | CBOT豆粕344.6；期权跳过 | 开盘后补验证 |
| 生猪LH | LH2701 | 10490 / 10475 | +0.24% / -6.89% | 174035 / 182448 / +8124 | -3.72% | 缺 | 制度无夜盘 | DCE期权跳过 | 仅破10450不收回看空 |
| 烧碱SH | SH701 | 1726 / 1735 | -1.82% / -6.06% | 207684 / 207093 / +41022 | +0.29% | 缺 | 1729，+0.17%/-0.35%，ΔOI+24351，23:00 | sampled core；exec否 | 增仓弱势但曲线反对追空 |

## 四、相对前序的真正变化

1. **Night日历语义已被Core修正。** 前序因源标签写成周六而隔离；本次正式标为10月19日交易日。供应商快照可进入第一层价格信息，但仍不能冒充官方最终收盘或完整夜盘量仓。
2. **油链已在Friday Night预交易。** SC2612相对前收+3.93%、FU2701 +2.66%，周一不再是“海外冲击尚未交易”的旧状态；方向支持增加，追价赔率反而下降。
3. **贵金属EOD修复被快照回吐。** AG2612 Night -1.38%、AU2612 -0.36%，与10月16日日盘上涨冲突；AG旧反弹多头继续降级观察。
4. **Options由旧全量面板切换为Core采样。** 成功品种从旧口径41降为33但日期更新至10月16；ATM/局部skew可读，完整surface/positioning/execution仍均为0。不能把口径变化误判成市场流动性突然恶化。
5. **新增官方期货价格交叉核对。** 四所可比价格零差异，DCE为接口错误；这提高SHFE/INE/CZCE/GFEX定价可信度，但不增加证据层，也不核验量仓。
6. **燃料油外部证据增强、原油政策反证也增强。** 公开报道显示HSFO供应流显著收紧；同时美国放松部分俄罗斯能源制裁，原油供给尾部风险下降。油链不是单向无反证交易。

## 五、产业链地图与Stock利润桥

1. **原油—燃料链（偏多，追价风险高）**：SC/FU Night快照和backwardation支持，海外供应扰动/燃料油紧张支持；政策性增供与周一gap反对。SC/LU Physical缺失。Stock目录没有纯油链表达，直接商品更纯。
2. **纯碱—玻璃—建材（反弹观察，置信度中低）**：SA701 5D弱、Night快照+1.81%、减仓，curve backwardation；FG无跨层共振，现货基差仅C级。SA期权局部看涨偏度存在但无执行报价。
3. **贵金属—矿业（中性偏弱）**：AG/AU EOD修复、Night回吐、曲线contango。紫金矿业2026H1合并收入1941.78亿元、归母净利391.70亿元、经营现金流554.72亿元，确认金铜利润暴露，但价格传导受销量、成本、套保、汇率和少数股东影响；股票数据落后且执行状态未知，不列候选。
4. **橡胶链（BR相对强但确认不足）**：BR2612 EOD价量仓和backwardation同向，Night仅+0.13%且ΔOI微降；BR期权underlying为BR2611，不能替代2612，实体和国际精确映射缺失。
5. **油脂油料—养殖 / 新能源（冲突）**：M/LH的DCE Night不可得；LH弱趋势/contango与周五止跌冲突。LC/AP急跌但backwardation明显，局部IV高于RV仅说明定价差异，不足以证明便宜或继续下跌。

宝钢股份仅作为铁矿成本—钢材售价—销量/库存/套保的条件性利润桥；黑色本期无跨层机会，且股票快照停在10月15日，未改变商品排序。Stock决策贡献为**排除股票替代表达**，不是新增支持层。

## 六、统一机会榜（研究吸引力，不是胜率）

| 排名 | idea_id / 方向 / 工具 | 逻辑25 | 赔率25 | 催化20 | 价曲波15 | 拥挤15 | 总分 | 有效支持层 / 主要反证 | 三轴状态 |
|---:|---|---:|---:|---:|---:|---:|---|---|
| 1 | `COM-M-SC2612-EIA-SETTLE-RECLAIM-LONG-20261016` / 条件多SC2612 | 21 | 17 | 16 | 11 | 9 | **74** | 1快照、2曲线、4海外；3/5缺，政策增供反对 | 待验证优势 / 充分到部分 / 休市等触发参数 |
| 2 | `COM-M-FU2701-HSFO-TIGHTNESS-LONG-20261018` / 条件多FU2701 | 20 | 14 | 15 | 12 | 9 | **70** | 1价格、2近端曲线、4燃油紧张；实体/准确跨期不完整 | 待验证优势 / 部分 / 休市等触发参数 |
| 3 | `COM-M-SA701-NIGHT-RECLAIM-LONG-20261018` / 条件多SA701 | 18 | 15 | 10 | 13 | 10 | **66** | 1快照、2曲线、5局部skew；中期跌势/减仓反对 | 待验证优势 / 部分 / 等日盘与报价 |
| 4 | `COM-E-BR2612-CURVE-MOMENTUM-LONG-20261016` / 条件多BR2612 | 18 | 15 | 9 | 12 | 11 | **65** | 1 EOD、2曲线；Night未确认，3/4/5缺 | 待验证优势 / 部分 / 待二次确认 |
| 5 | `COM-E-LH2701-WEAK-CURVE-SHORT-20261013` / 条件空LH2701 | 17 | 14 | 8 | 11 | 11 | **61** | 1中期弱势、2contango；日盘止跌与3/4/5缺 | 待验证优势 / 部分 / 周一日盘确认 |

分项总和已复核，未超权重上限。SC/FU/SA虽达到三层门槛，仍因休市、当前报价/参数和触发缺失而不可立即执行；Night/curve未被另算第六层。

## 七、研究/交易卡（3张；参数未齐，不构成订单）

### 卡1｜SC2612：gap吸收后的条件多

- **事实**：10/16 close/settle=711.8/723.0，ΔOI+3173，近端curve+0.84%；10/19归属的供应商快照739.8，vs前收+3.93%，vs结算+2.32%，来源10/17 02:30，快照ΔOI+763。SC实体缺、期权失败。
- **定价/推断/主观**：供应风险已被Friday Night显著预交易，市场是否低估持续性尚未证实。最强竞争解释是制裁放松和运费回落削弱风险溢价。主观只偏多、不追首跳。
- **表达/入场**：只研究SC2612线性多头。好=09:15–09:30回踩735–742后重夺740，curve仍≥0.8%、Brent不低于106；中=742–750二次确认；坏=>752追入，放弃。当前没有可计算滑点后净R。
- **失效/退出**：计划止损724；30分钟收于723下或Brent<106为逻辑失效。TP1=760、TP2=780；10/19 14:30无跟随时间退出。止损不是最大损失。
- **参数/压力**：last trading=2026-11-30、delivery=12-07；乘数/tick/tick value/保证金/限幅/夜盘参数未知，确认前冻结执行。测试1/2限幅、gap、流动性消失、保证金上调和政策逆转。

### 卡2｜FU2701：紧张燃料油与近端曲线

- **事实**：close/settle=4819/4770，5D+7.43%、ΔOI+8765；供应商快照4947，vs前收+2.66%、vs结算+3.71%、快照ΔOI+23709，23:00。近端pair曲线+7.92%，但不是围绕FU2701的完整准确双腿审计；Physical basis C。
- **定价/推断/主观**：HSFO现货紧张支持方向，但公开流量数据不是FU2701可交割货的精确进口平价。最强反证是油价政策逆转、炼厂/调和替代与高位回撤。
- **表达/入场**：只研究FU2701线性多头。好=09:30回踩4900–4950守住并重夺4950；中=4950–5050且SC不反转；坏=>5050追入，放弃。成本、滑点与净R因参数缺失待评。
- **失效/退出**：计划止损4820；30分钟<4770或近端curve<5%失效。TP1=5100、TP2=5300；2个交易日无跟随退出。
- **参数/压力**：合约乘数/tick/tick value/保证金/限幅/最后交易/交割未核全；期权样本为FU2611且10/19到期，不可给FU2701限损。与SC合并同一能源风险预算。

### 卡3｜SA701：弱趋势中的快照反弹

- **事实**：close/settle=939/940，5D-7.02%、ΔOI-11911、curve+1.98%；快照956，vs前收+1.81%、vs结算+1.70%、快照ΔOI-20379。SA701 sampled core ATM strike=940、ATM IV=25.405%、RR25=+2.68、BF25=-0.105；bid/ask与execution未就绪。
- **定价/推断/主观**：快照反弹和backwardation支持均值修复，减仓与中期跌势反对；正RR表明样本看涨偏度较高，不能据此断言看涨期权便宜。
- **表达/入场**：期货条件多优先。好=09:30守952并重夺960、curve≥1.5%；中=960–968；坏=>980追入，放弃。无可验证期权净支出、最大损失或Greeks，期权只保留研究结构。
- **失效/退出**：计划止损938；30分钟<930或curve转contango失效。TP1=985、TP2=1020；3日未到TP1退出。
- **参数/压力**：乘数/tick/保证金/限幅/交割参数未核全；测试一/二限幅、产业政策、流动性与IV塌陷。试仓只在参数补齐后。

## 八、商品期权专项

- **口径**：2026-10-16、33/64产品、740合约、33 series，属于`core_v1/sampled_strikes`。ATM32、skew25、完整surface0、positioning0、execution0；不能由样本OI推全链PCR、拥挤或dealer Gamma。
- **局部IV-RV**：SA701 ATM IV25.41% vs标的RV20 19.31%；AP701 29.88% vs21.62%、RR25 -2.62；LC2701 50.75% vs43.11%、skew未就绪；RU2701 25.74% vs25.44%、skew未就绪。期限与采样口径不完全相同，仅作相对观察。
- **错配/回避**：BR样本underlying=BR2611而候选为BR2612；FU样本=FU2611且10/19到期；SC/AG/AU/CU失败；M/LH因DCE安全限制跳过。不可将这些旧/错配series用作候选执行。
- **事件凸性**：周一10:00宏观、油链headline和EIA周报有Gamma/Vega需求，但没有双边报价和成本时不编具体腿、权利金、最大净支出或滑点。当前最佳动作是等待实时链；若无法获得，则不用期权叙事替线性仓封顶。

## 九、2026-10-19 09:00开盘风险地图

| 品种 | Previous China EOD | Current T Night（已核归属） | 07:00 Overseas/周末 | 潜在开盘与已定价 | 追价/确认 |
|---|---|---|---|---|---|
| SC2612 | 711.8/723.0、curve+0.84% | vendor snapshot 739.8、+3.93% | 油市周末休市；供应风险与制裁放松并存 | 高开大部已预交易 | 不追；09:15/30/45看740、curve、OI |
| FU2701 | 4819/4770、5D+7.43% | 4947、+2.66% | HSFO供应紧张，无exact parity | 偏高开、已预交易 | 09:30等4900–4950留存 |
| SA701 | 939/940、5D弱 | 956、+1.81% | 国内独立；无新海外价格 | 偏高开但性质未定 | 09:30看952/960及curve |
| AG2612 | 14029/13889、OI降 | 13835、-1.38% | 海外周末休市；利率风险仍高 | 偏低开、夜盘已回吐 | 等15–30分钟，不抄底 |
| CU2611 | 109860/109450、OI降 | 109420、-0.40% | 无周末有效新LME报价 | 平/略低 | 10:00宏观前不扩大风险 |
| M2701 | 3281/3299、减仓 | DCE不可得 | CBOT周末休市 | 无中国预交易确认 | 等30分钟与DCE补数 |
| LH2701 | 10490/10475、contango | 制度无夜盘 | 无直接海外映射 | 平开优先 | 仅破10450且不收回 |

四层判断：10/16 EOD是基线；10/16晚至17日凌晨属于10/19 Night且是供应商快照；周末没有新的可成交海外报价；下一未发生阶段是10/19日盘，之后10/19 21:00夜盘归属10/20。不开盘前制造价格，不把Friday Night写成“今晚将发生”。

## 十、未来24小时 / 7日事件与行动前核对

### 事件（日时均为北京时间）

- **10月19日10:00**：国家统计局国民经济运行发布会及工业、能源、投资、地产、消费数据。黑色、有色、能化和人民币敏感；09:00只试探，10:15/10:30/10:45再确认。
- **10月19日LME Metals Seminar、10月20日LME Dinner**：关注铜铝现货升贴水、库存和贸易流；会议观点不替代官方库存。
- **10月21日22:30（标准周三10:30 ET）**：EIA周度石油状态报告。SC/FU降低线性Delta；只有实时可成交链才做有限Vega/Gamma。
- **10月23日/24日**：CFTC周度持仓计划发布；用于拥挤验证，不推dealer Gamma。
- **7日内持续**：霍尔木兹/俄油制裁、VLCC运费、俄罗斯炼厂与燃料油流、矿山/油田/炼厂/化工开停工、天气与交易所参数公告。没有原始披露不增证据层。
- **USDA/WASDE**：官方下一次WASDE为11月10日，非未来7日催化；OPEC+/IEA若无确定官方日程不编日期。

### 覆盖核对、输入版本与旧观点

- **应覆盖/实际分析**：固定63代码全部保留；引擎实际扫描77品种/806合约，包括动态新增BZ/PL/PD/PT/RS/RR/OP/WR/LG等。黑色10、有色14、能源化工26、农产品14、新能源3、软商品10均完成EOD/Market初筛及可得Physical/External/Options复核。
- **数据不足**：DCE Night 214合约；SC/LU Physical；SHFE/DCE/GFEX当前仓单；A级/B级basis；全部实时期权bid/ask；多项乘数/tick/保证金/限幅/交割；DXY/USDCNH与Dubai/Oman/SG燃料油精确映射。
- **不适用/低流动性**：JR/PM/RI/WH/ZC等代表行出现零量/零仓或占位，不入排行；制度无夜盘不算错误。
- **未入榜板块**：黑色无同向价曲实体共振；有色CU去仓、贵金属Night回吐；农产品M外需与内盘弱势冲突；新能源LC弱价与backwardation冲突；EC曲线可比与交割季节性不足，均不称套利。
- **旧观点**：SC同一idea由“日历异常隔离”升级为“合法T=10/19快照、等gap吸收”，不假定成交；BR保留但Night未确认；LH继续等破位；AG继续watch only；旧SA空头保持取消，新增的是反弹研究，不是反向已成交。
- **Stock**：仅核紫金/宝钢利润桥；价量到10/15、回填失败、预测与证券执行不足。没有Stock候选，也不把公司股价作为商品第五/第六层。

风险预算仅在触发、报价和参数补齐后适用：试仓NAV 0.25%–0.75%，确认0.75%–1.50%，同一能源主题SC+FU合并；单一高确信主题总风险预算不超过2.5%–3.0%。压力测试含一/二限幅、相关性断裂、流动性消失、gap、保证金上调、IV升/塌、交割挤压和人民币急变。

## 来源

- [China-Commodities-Engine unified input](https://github.com/farfromexact/China-Commodities-Engine/blob/e597eb2ae162b0e086bafc98c7fca9262f671cb0/data/report_input_latest.json)（requested 2026-10-16；支持全市场、Night、模块摘要）
- [Night session detail](https://github.com/farfromexact/China-Commodities-Engine/blob/e597eb2ae162b0e086bafc98c7fca9262f671cb0/data/night_session/latest.json)（2026-10-19交易日；支持准确合约供应商快照与语义）
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/e597eb2ae162b0e086bafc98c7fca9262f671cb0/data/options/quality_latest.json)（2026-10-16；支持Core采样覆盖与ready层级）
- [Futures official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/e597eb2ae162b0e086bafc98c7fca9262f671cb0/data/crosschecks/futures_latest.json)（2026-10-16；支持四所零价格差异与DCE源错误）
- [China-Stock-Engine](https://github.com/farfromexact/China-Stock-Engine/tree/79c96a9d9e73a7c2a13d340229acc7c64f4ec144)（交易日2026-10-15；支持公司映射、财务与能力限制）
- [Reuters：全球燃料油市场趋紧，2026-10-16](https://www.reuters.com/business/energy/global-fuel-oil-market-stays-tight-conflicts-hit-mideast-russia-supplies-vitol-2026-10-16/)（支持HSFO流量与现货溢价）
- [Reuters：美国放松部分俄罗斯制裁，2026-10-17](https://www.reuters.com/world/europe/trump-waives-many-russia-related-sanctions-tariffs-before-they-were-take-effect-2026-10-17/)（支持原油供给政策反证）
- [Reuters：VLCC运费自峰值回落，2026-10-16](https://www.reuters.com/business/energy/supertanker-rates-fall-record-highs-2026-10-16/)（支持油运压力仍高但边际缓和）
- [Reuters：黄金周线承压，2026-10-16](https://www.reuters.com/world/india/gold-set-weekly-drop-traders-assess-fed-signals-2026-10-16/)（支持贵金属利率冲突）
- [国家统计局发布日程](https://www.stats.gov.cn/sj/fbrc/)（访问2026-10-18；支持10月19日10:00发布会）
- [LME Week 2026](https://www.lme.com/Events/LME-Week)（支持10月19日Seminar与10月20日Dinner）
- [EIA Weekly Petroleum Status Report schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（支持周度发布时间）
- [CFTC COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（支持周度持仓日程）
- [USDA WASDE schedule](https://www.usda.gov/oce/commodity/wasde)（支持11月10日为下一期、排除7日催化）

**归档状态：success（六路径写后回读确认）｜CI：pending_or_unverified**

## 十一、行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：不挂可成交单；预设周一SC2612回踩735–742重夺740、FU2701守4900–4950、SA701守952重夺960后再评。  
C. 今天继续观察：BR2612 Night未跟随、LH2701破10450条件、AG夜盘回吐、LC/AP弱价与backwardation、周一10:00宏观数据。  
D. 今天必须回避或有条件退出：追SC/FU首跳、追空LC/AP、用FU2611/BR2611期权替代2701/2612、把供应商快照称官方收盘；若此前按条件建立且原逻辑失效，依原计划退出。
