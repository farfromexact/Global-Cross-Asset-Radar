# 商品期货期权晨间雷达｜2026-10-28

> 生成时间：2026-10-28 07:02:36 BJT  
> 信息截点：2026-10-28 07:02 BJT  
> 研究范围：全球商品期货、商品期权、产业链与限定Stock利润验证；只研究，不下单，不假定持仓或成交。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；铜与原油仅有条件机会，须等待09:15后价格、曲线与外盘共同确认。**

今天并非“没有研究机会”，而是三类机会尚未合并为可执行交易：

- **研究机会存在但等待条件：** CU2612夜盘价格偏强，但近远月斜率收窄且LME阈值未到；SC2612绝对价格偏弱，但主—次月backwardation反而扩大。
- **已研究但优势不足：** MA701旧多逻辑被夜盘回撤和海外油跌破坏；BU/FU虽有强曲线，缺准确夜盘合约核验。
- **数据不足不能判断：** 214个夜盘合约未解析、期权bid/ask覆盖为0、Physical无A/B级basis；这些缺口只限制依赖项，不代表市场无机会。

最有价值的三个待验证观察：① 09:15后CU价格、CU2611-12与LME是否重新同向；② SC跌破是否伴随SC2612-2701价差收窄；③ FOMC前AU/AG反弹能否脱离单纯事件前空头回补。下一实际窗口为2026-10-28 09:00 BJT，EC为09:30；不在开盘第一分钟追价。

## 2. 数据质量、范围与事实台账

| 模块 | 最新应得/实际日期 | 实际取得 | 可分析 | 可执行 | 关键缺口 |
|---|---|---:|---|---|---|
| Futures | 2026-10-27 EOD | 806合约、77产品、五所同日；source-date match 100% | 是 | 否 | 5个OHLC占位；动态参数仅30.15% |
| Market State | 2026-10-27 | 77产品、20日同合约历史 | 是 | 否 | 连续主力不当真实单合约收益 |
| Physical | requested 2026-10-27 | 18/20 fresh；0 stale；0 carried | 局部 | 否 | SC/LU不可用；18条basis均C级、A/B=0 |
| External | requested 2026-10-27 | 17/22 fresh | 仅context | 否 | 无intraday；不能据此做跨市套利 |
| Night | trading_date 2026-10-28；start 10-27 | 416/806；51.6129% | 重点合约需fallback | 否 | 214 query_error/unresolved；raw latest=0 bytes |
| Options | 2026-10-27 | 45/64产品、988记录；ATM ready44、skew ready25 | 局部 | 否 | surface/positioning/execution均0；bid/ask=0 |
| Metadata | 2026-10-27 | contract match67.49%；effective73.45% | 局部 | 否 | multiplier/tick/margin/limit动态覆盖30.15% |
| Stock | tape 2026-10-21 | 5576 universe、5568 quotes；最小财务包2公司 | 背景 | 否 | 价量陈旧，交易状态/行业/执行未ready |

数据入口与状态：[Futures EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)。report_input_latest.json与night_session/latest.json本次均为空文件；未把“空”误写成“无市场机会”。

**交易日历闸门。** 2026-10-27晚至10-28凌晨的夜盘归属2026-10-28交易日，EOD=10-27、Night trading_date=10-28是合法组合；calendar_mismatch=false。仓库流程validation/published为真只证明流程闭环，不证明每个合约有执行级报价。公开补证的CU/SC/MA/AU均标记为供应商快照，official_night_close_verified=false，不称交易所最终夜盘收盘。

**官方独立交叉核对。** SHFE 238、INE 63、CZCE 243、GFEX 48个合约匹配，settle/close/pre-settle实际差异均为0；DCE官方接口HTTP 412，故state=partial。partial来自独立源缺口，并非已观察到价格差异；该交叉核对不覆盖成交量和持仓量。详见[futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)。

**全范围覆盖。** 指定63代码及动态新增均进入77产品横截面初筛；LPG按交易所产品代码PG映射。黑色、金属、能源化工、新能源、农产品、航运均检查方向、近远月、basis/仓单可得性、实体、海外和期权局部面板。未入榜不等于未扫描：

- 黑色：I2701、RB2701偏弱但无三层共振；JM/J/HC/FG/SF/SM无达到70分的独立优势。
- 金属：CU有条件多；AU/AG仅FOMC事件观察；AL/ZN/PB/NI/SN/SS/BC/AO/AD未出现更高质量共振。
- 能源化工：SC价格与曲线冲突；BU/FU曲线强但外油回落；PX/TA/EG/EB/PP/L/V/RU/NR/BR/SH/UR/SP多数为板块映射或局部异常，未构成可执行优势。
- 新能源：LC反弹伴减仓；SI/PS及GFEX新增品种未获三层独立支持。
- 农产品：LH弱趋势、M/Y偏弱；A/B/RM/P/OI/C/CS/JD/CF/CY/SR/AP/CJ/PK无足够跨层共振。
- 航运：EC2612 1D -6.26%、5D -15.86%，增仓但没有夜盘和可靠现货套利口径，保留弱势观察。

## 3. 12项市场仪表盘

| 标的 | EOD close/settle | 1D / 5D | OI变化 | 曲线/Physical | 夜盘或海外 | Options/信号 |
|---|---:|---:|---:|---|---|---|
| CU2612 | 108390 / 108640 | +0.43% / +0.19% | +524 | EOD CU2611-12 +0.644%；basis C | 109420；+0.95% vs close；night curve +0.512% | ATM IV12.49% vs RV11.40%；价格强、曲线未共振 |
| SC2612 | 733.7 / 731.6 | -1.10% / +0.59% | -1528 | EOD主-次月+8.2/+1.134%；无A/B basis | 712.9；-2.84% vs close；night spread+9.4/+1.336% | ATM IV68.28% vs RV44.44%；不追空 |
| MA701 | 3448 / 3402 | +1.67% / +8.45% | -48484 | MA611-12 +5.584%，非701精确pair | 3378；-2.03% vs close、-0.71% vs settle | MA612 ATM IV49.66%；旧多失败 |
| BU2701 | 4965 / 4893 | +3.27% / +9.51% | +17992 | near-next +7.268% | 海外油结算回落；准确夜盘未补 | IV46.61% vs RV30.91%；待消化 |
| FU2701 | 5386 / 5295 | +1.09% / +7.45% | +2123 | near-next +12.696% | 准确夜盘未补 | IV71.85% vs RV46.34%；高事件溢价 |
| AG2612 | 12763 / 12986 | -0.49% / -6.31% | -1182 | near-next -0.223% | 夜盘品种汇总约+0.93%，非精确卡片报价 | IV42.00% vs RV30.11%；FOMC前不追 |
| AU2612 | 861.16 / 863.68 | +0.21% / -3.29% | -3102 | near-next -0.201% | vendor 873.18，观察时点00:08:48 | IV21.20%、RR25 -0.76；上涨已部分计价 |
| SH701 | 1486 / 1499 | -3.54% / -13.00% | +1691 | near-next +1.170% | 夜盘精确报价未核 | IV38.89%、RR25 -3.75；价曲冲突 |
| SA701 | 981 / 968 | +0.62% / +2.33% | -44376 | near-next -2.277% | 精确夜盘未核 | IV26.38%、RR25近0；反弹减仓 |
| LC2701 | 98500 / 97840 | +3.08% / -1.91% | -4815 | near-next +1.122% | 精确夜盘未核 | IV54.01% vs RV40.93%；不判新多 |
| LH2701 | 9975 / 9805 | +0.77% / -3.02% | -18181 | near-next -4.895% | 无夜盘 | 20D -16.62%；趋势弱但减仓 |
| EC2612 | 2687 / 2742.5 | -6.26% / -15.86% | +1969（+22.18%） | near-next -16.171% | 无夜盘；09:30开 | 无合格执行结构；弱势观察 |

注：CU/SC精确夜盘来自[CU供应商页](https://www.9qihuo.com/hangqing?productcode=cu)与[SC供应商页](https://www.9qihuo.com/hangqing?productcode=sc)；其OHLC、成交和OI只作供应商观察，不声明纯夜盘最终持仓或精确盘中路径。

## 4. 相比前序报告的真变化

1. **铜：价格强化、曲线弱化。** CU2612从EOD 108390至夜盘109420，但CU2611-12由0.644%收窄到0.512%。这不是完整的“突破确认”，旧触发的曲线部分仍未满足；评分72→74仅反映夜盘价格与供应事件延续，不等于仓位升级。
2. **原油：单边下跌、月差走强。** SC2612夜盘712.9较EOD跌2.84%，同时SC2612-2701从+8.2扩大到+9.4。若近端紧张仍被价差保留，追空的竞争解释更强；旧短线的curve条件失败。
3. **甲醇：旧多计划终止。** EOD 3448后夜盘3378，较close -2.03%，且日盘OI减少48484；前序“价格、PX、backwardation同步”未发生。评分73→59，旧21:15/21:30窗口不延长。
4. **海外油：结算继续回撤。** 10月27日Brent 113.88（-1.67%）、WTI 99.90（-1.83%）；外交缓和压价，但航运与供应中断风险仍在，故油链不是单向无条件空。来源：[Reuters](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)。
5. **期权：局部研究不等于执行。** ATM ready44、skew ready25，但surface/positioning/execution均0；任何“IV高于RV”的结论只说明观察差，不证明期权昂贵或可做空Vega。

## 5. 产业链传播与Stock利润桥

| 产业链 | 传播路径 | 最强/最弱 | 最大缺失 | 置信度 |
|---|---|---|---|---|
| 铜矿→冶炼→CU/BC→线缆新能源 | HVC停产风险→LME/COMEX→沪铜 | 夜盘价格最强；曲线共振最弱 | LME现货升贴水与日盘再确认 | 中 |
| Brent/WTI→SC→FU/BU→化工 | 外交缓和→海外油跌→SC gap；近端紧张仍在月差 | BU/FU EOD曲线强；SC绝对价弱 | 准确BU/FU夜盘、EIA结果 | 中 |
| 煤/气→MA→MTO/PX | MA日盘强→夜盘回撤→PX验证 | EOD backwardation强；night价格弱 | MA701精确夜盘curve | 中低 |
| 美元/实际利率→AU/AG | FOMC事件→双向Delta/Vega | 夜盘反弹；5D趋势仍弱 | 当前期权bid/ask、实时实际利率 | 低 |
| 铁矿/煤焦→钢材→航运 | 原料与终端需求→吨钢利润→EC需求 | EC弱势最显著 | 高质量现货/运价与交割口径 | 中低 |

Stock限定补证没有产生新的商品方向证据：

- **紫金矿业601899：** 简化利润桥为铜价×销量，扣矿山成本、冶炼费、套保、汇率、少数股东与扩产Capex。HVC不是紫金资产，因此HVC罢工只通过铜价间接影响紫金，不能把事件当公司独立催化。Stock tape截至10月21日且交易状态未核，**直接CU表达更纯**。
- **宝钢股份600019：** 利润桥为钢价/销量，扣铁矿煤焦成本、库存损益、出口汇率、套保与Capex。原料跌既可能扩吨钢利润，也可能反映需求弱并压售价；等待10月28日三季报再区分。当前不形成股票候选。
- 限定检索截至07:02没有取得新的经营公告；旧财务资料入库不算今天催化。公司模块只影响表达选择，未新增第六证据层。

## 6. 统一机会榜

| 排名 | idea_id / 方向 | 期限/阶段 | 五层支持与反证 | 分项（逻辑/赔率/催化/价曲波/技术） | 总分 | 研究/证据/执行 |
|---:|---|---|---|---:|---:|---|
| 1 | COM-M-CU2612-HVC-STRIKE-WATCH-20261025 / 条件多 | 1—10D；等09:15—09:45 | 支持1/2/3/4；反对：curve收窄、LME阈值未到、期权不可执行 | 20/17/16/11/10 | 74 | 有效 / 4层冲突 / 仅条件 |
| 2 | COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026 / 条件空 | 日内—2D；等曲线侵蚀 | 支持1/4；反对：backwardation扩大、EIA、IV结构不可执行 | 18/16/15/10/9 | 68 | 有效 / 2层上限69 / 仅条件 |
| 3 | COM-M-AG2612-FOMC-REBOUND-WATCH-20261028 / 观察偏多 | 1—3D；事件前不追 | 支持1/4；反对：5D弱、FOMC gap、bid/ask=0 | 17/16/15/10/8 | 66 | 研究 / 2层 / 数据不足 |
| 4 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 / 观察偏多 | 1—5D；等回撤 | 支持1/2；反对：外油跌、夜盘缺、EIA | 17/14/12/11/9 | 63 | 观察 / 2层 / 受限 |
| 5 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 / 中性偏空观察 | 日内—3D；旧多失败 | 仅支持2；反对：night跌、日盘减仓、外油跌、精确curve缺 | 16/12/12/10/9 | 59 | 优势不足 / 1层 / 旧窗口终止 |

分数只代表研究优先级，不代表胜率或仓位。得分与分项均已重算；五层上限规则满足。

## 7. 研究/交易卡

### 卡1｜CU2612条件多

- **新增事实：** CU2612供应商夜盘快照109420，较EOD close108390 +0.950%、较settle108640 +0.718%；CU2611=109980，night near-next +560/+0.512%，低于EOD +0.644%。
- **市场已计价：** 夜盘上涨已计入部分HVC供应扰动；曲线没有同步强化。
- **分歧与PnL：** 只有价格、curve、LME三者同向，才说明停产时长尚未充分计价；PnL来自CU2612方向，不是跨市套利。
- **触发顺序：** 09:15后CU2612≥109500持续15分钟 **AND** CU2611-12≥0.60% **AND** LME三月铜≥14450；其后09:30/09:45回踩109150—109350且不破109000。先突破、再回踩，不能用触发前价格入场。
- **入场与退出：** 条件成立后40%/60%；首个可成交价>110200放弃。计划止损108300；TP1 111500减半，TP2 113800；11月5日14:45时间退出。HVC复工、LME<14250或curve<0.30%持续15分钟为逻辑失效。
- **好/中/坏成交：** 109150/109250/109350；每手5吨。至止损计划风险4250/4750/5250元；TP1毛利11750/11250/10750元，毛R 2.76/2.37/2.05；TP2毛利23250/22750/22250元，毛R 5.47/4.79/4.24。往返各1 tick的情景滑点=100元/手，佣金未知，净R待询价。
- **合约/期权：** 5吨/手、tick10元=50元，最后交易日2026-12-15。动态保证金、当日限幅和交割参数覆盖不完整。EOD ATM108000 IV12.49% vs RV11.40%，skew=false、bid/ask=0；看涨价差仅待询价，不称可执行限损。
- **风险：** 试仓NAV0.50%，确认后单idea≤1.25%；与铜股合并主题≤2.5%。计划止损不封顶；动态限幅未核，不编精确一/二板损失。

### 卡2｜SC2612反抽失败条件空

- **新增事实：** SC2612供应商夜盘快照712.9，较EOD close733.7 -2.835%、较settle731.6 -2.556%；SC2701=703.5，主—次月+9.4/+1.336%，较EOD +8.2/+1.134%更强。
- **市场已计价：** 外交缓和与海外油跌已被绝对价格快速计入，追空赔率下降；月差仍保留近端紧张。
- **分歧与PnL：** 只有主—次月价差降至6元以内且Brent≤113，期限层才开始确认单边下跌。PnL来自SC2612方向，不是月差套利。
- **触发顺序：** 09:15 SC2612≤710持续15分钟 **AND** SC2612-SC2701≤6.0元 **AND** Brent≤113；随后反抽712—716失败。若09:00直接低于705，不追。
- **入场与退出：** 条件成立后50%/50%；计划止损722；TP1 699减半，TP2 690；10月28日14:45未达目标即退出，不跨22:30 EIA。Brent>116或价差≥10元持续15分钟为逻辑失效。
- **好/中/坏成交：** 对空头而言715/713.5/712；每手1000桶。至722计划风险7000/8500/10000元；TP1毛利16000/14500/13000元，毛R2.29/1.71/1.30；TP2毛利25000/23500/22000元，毛R3.57/2.76/2.20。费用、滑点未知，净R待询价。
- **合约/期权：** 1000桶/手、tick0.1元=100元；动态保证金/限幅未完整确认。EOD ATM740 IV68.28% vs RV44.44%，skew不可用、bid/ask=0，不能据此做空波动。
- **风险：** 仅试仓NAV0.25%—0.50%，EIA前不扩仓；与BU/FU/油气股合并主题≤2.0%。供应/航运新闻可造成反向gap，止损不限制最大损失。

仅两张卡；其余候选缺准确报价、证据层或可执行参数，不凑数。

## 8. 商品期权专项

样本口径为core_v1 / sampled_strikes，45/64产品、988条记录。core_atm_ready=44、skew_ready=25，但surface_ready=0、positioning_ready=0、execution_ready=0、full_chain_verified=false。

- 可使用的只是同series同到期的局部ATM/局部25Δ：SC ATM IV68.28% vs RV44.44%；FU71.85% vs46.34%；BU46.61% vs30.91%；AU21.20% vs14.35%；AG42.00% vs30.11%；MA ATM49.66%、RR25 +1.05；SH ATM38.89%、RR25 -3.75。
- 不可用：完整wing/tail、跨期term（没有两个准确可比到期便不外推）、全链PCR、拥挤、dealer gamma方向、执行净权利金和滑点。
- “IV高于RV”不是独立便宜/昂贵证明；FOMC/EIA前高IV可能是事件补偿。没有bid/ask时，最多从风险预算倒推可接受净支出上限，不能称期权已便宜。
- PX期权样本到期日为10月28日且无bid/ask，回避临到期执行/行权风险。夜盘标的已变后，10月27日moneyness和Delta必须在日盘重算。

## 9. 09:00开盘风险地图

| 层次 | 已知事实 | 开盘倾向 | 15/30/45分钟检查 |
|---|---|---|---|
| Previous China EOD | CU强、油化EOD偏强，EC/LH弱；多品种曲线极端 | 仅作锚，不等于今日方向 | 先核准确合约、close/settle基准与roll |
| Current T Night | CU109420但curve收窄；SC712.9但主次月价差扩大；MA3378 | CU可能高开、SC/MA低开；均不追 | 09:15价格+curve；09:30跨品种；09:45五分钟收盘/OI |
| 07:00 Overseas | Brent113.88、WTI99.90结算下跌；FOMC与EIA待发 | 油链压力、贵金属事件gap、铜外盘支持不完整 | 海外报价必须与中国开盘时间对齐，错时只作映射 |

- **潜在高开：** CU、AU/AG；若开盘直接透支且curve/外盘未确认，放弃追价。
- **潜在低开：** SC、MA、BU/FU；SC低开若月差继续强，不做单边追空。
- **平开/分化：** 黑色、农产品、新能源；只在自身价曲/实体证据形成时升级。
- **无夜盘：** LH等在09:00，EC在09:30用日盘确认；不存在的夜盘不构成扣分。
- 09:15/09:30/09:45是未来合法窗口；若补跑已越过，应改用实际行情重审，不回填触发和成交。

## 10. 未来24小时/7日事件与风险处理

| 北京时间 | 事件 | 影响 | 处理 |
|---|---|---|---|
| 10/28 09:00—09:45 | 中国日盘三段确认 | 全市场 | 禁止首分钟追价；价、curve、跨品种、OI依次核 |
| 10/28 22:30 | [EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/) | SC/BU/FU/Brent/WTI | 14:45前退出或降至事件预算；无报价不做短Vega |
| 10/29 02:00/02:30 | [FOMC声明/发布会](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) | AU/AG/CU、DXY/CNH | 警惕双向gap与IV塌陷；线性止损不封顶 |
| 10/29 19:00前后/23:00 | [Teck Q3结果/电话会](https://www.teck.com/news/news-releases/2026/teck-to-release-third-quarter-2026-results-on-october-29%2C-2026) | HVC、铜 | 核产量、罢工时长、指引；复工直接失效铜多 |
| 10/28 | 宝钢股份三季报预约 | 钢铁利润桥 | 核售价、销量、原料、库存、套保；不预判股票 |
| 10/30 | [EIA Petroleum Supply Monthly](https://www.eia.gov/petroleum/supply/monthly/) | 油链中频供需 | 不当盘中触发 |
| 未来7日 | 中东外交/航运、CFTC周报、USDA天气/作物进度 | 油、贵金属、农产品 | 精确发布时间未完全确认；只计原始新事实 |

没有独立确认未来7日内OPEC+/IEA正式发布时点，因此不编日期；地缘与矿山新闻只有在原始声明、交易所或权威报道出现新事实后才增证据层。

## 11. 旧观点、行动前清单与发布校验

旧观点状态：

- CU稳定idea_id保留；夜盘价格达标但curve/LME未达，**信号未满足**，实际持仓=未提供/未知。
- SC旧短idea保留；价格穿越不等于原curve条件满足，**不得追认触发或成交**。原SC多idea继续invalidated。
- MA评分73→59，原因是价格变化与海外油回落；旧多窗口终止，不移止损、不延长期限。
- BU评分71→63，原因是海外油回落与准确夜盘缺失；继续观察。
- 新AG观察idea不设执行腿；缺bid/ask、Delta和执行状态时不写结构限损。

行动前覆盖清单：

- 应覆盖：63代码+动态新增；实际取得77产品、806合约，五所同日。
- 实际下钻：CU、SC、MA、BU、FU、AU、AG、SH、SA、LC、LH、EC；其余按板块异常/无异常扫描。
- 数据不足：Night raw空、214 unresolved、DCE官方crosscheck失败、A/B basis=0、Options bid/ask=0、Stock截至10/21。
- 不适用：无夜盘品种不因缺night受罚；EC等无合格期权结构不硬填。
- 风险预算：试仓NAV0.25%—0.75%，确认0.75%—1.50%，同因子主题合并≤2.5%—3.0%；油链本期专属上限≤2.0%。
- 压力：1/2涨跌停、夜盘gap、保证金上调、流动性消失、相关性断裂、IV跳升/塌陷、交割挤压、汇率急变、中国休市海外大波动。保证金不是风险预算，期货止损不封顶。

发布校验：分项加总74/68/66/63/59均通过；五层分数上限通过；夜盘日历通过；CU/SC关键计算与两张卡R值重算；MD/JSON由同一事实对象生成。未解决项如实保留，不能宣称全市场执行报价得到认证。CI状态为 **pending_or_unverified**。归档目标为六路径同一报告，archive_status在写后回读六路径全部一致后确认。

主要来源：[China Commodities Engine - futures EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)；[China Commodities Engine - market state](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)；[China Commodities Engine - night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)；[China Commodities Engine - physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)；[China Commodities Engine - options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)；[China Commodities Engine - official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)；[CU exact-contract vendor snapshot](https://www.9qihuo.com/hangqing?productcode=cu)；[SC exact-contract vendor snapshot](https://www.9qihuo.com/hangqing?productcode=sc)；[Oil settles lower on diplomacy hopes](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)；[Federal Reserve 2026 FOMC calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)；[EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)；[Teck Q3 2026 release schedule](https://www.teck.com/news/news-releases/2026/teck-to-release-third-quarter-2026-results-on-october-29%2C-2026)；[China Stock Engine manifest](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json)。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：CU2612三重确认后的回踩多；SC2612价格、月差与Brent共同确认后的反抽失败空。  
C. 今天继续观察：AG/AU事件修复、BU/FU强曲线、MA旧多失效后的新结构、LH/EC弱势及其余无精确夜盘品种。  
D. 今天必须回避或有条件退出：回避09:00追价、无bid/ask期权执行、供应商快照冒充官方收盘；若已自行建仓，按卡片逻辑失效与时间退出独立处理。
