---
report_date: 2026-11-06
edition: evening
generated_at_bjt: 2026-11-06T20:14:30.101+08:00
weekend_mode: false
china_options_date: 2026-11-05
china_options_fresh: false
archive_status: success
---

# 全球跨资产高风险机会雷达｜晚间版

> **实际截点：** 2026-11-06T20:14:30.101+08:00。中国现金市场与商品日盘已收；欧洲伦敦盘进行中；美国仅有11/5收盘和11/6盘前，10月就业报告尚未发布，美国现金市场22:30才开。今晚中国商品夜盘21:00开始，预期归属交易日2026-11-09；股指期货与股票今晚不开盘。本文为投资研究与备选策略，不代客下单；账户实际持仓未提供/未知。

## 一、今日一句话结论

全球仍处去杠杆后的高波动再定价：中美科技同步承压、美元与美债并未失控，锡的三层空头证据最完整，但非农前没有应立即建立的新仓。

## 二、事实台账与全市场仪表盘

### 事实台账（关键项）

| fact_id | 标的/事实 | 数值与口径 | 观测/known_at | 来源 | 支持判断与局限 |
|---|---|---|---|---|---|
| F01 | 报告截点 | 2026-11-06T20:14:30.101+08:00 BJT；实际生成/读取时间 | 2026-11-06T20:14:30.101+08:00 / 2026-11-06T20:14:30.101+08:00 | system clock | 界定可用信息与合法窗口；局限：不是行情时间 |
| F02 | SSE50/CSI300/CSI500/CSI1000 | 2787.41 / 4054.28 / 6597.35 / 6505.35；1D -0.84%/-1.44%/-2.13%/-2.18% index points；close | 2026-11-06 15:00 BJT / 2026-11-06 EOD | [直达](https://www.reuters.com/world/asia-pacific/asian-stocks-tumble-ai-led-wall-street-selloff-2026-11-06/) | 中国风格从11/5的小盘相对强转为小盘更弱；局限：CSI1000精确收盘来自公开市场页；非同一供应商 |
| F03 | A股广度/成交额 | >4700家下跌；约CNY1.67tn，较前日少约CNY0.46tn stocks/CNY；EOD breadth/turnover | 2026-11-06 15:00 BJT / 2026-11-06 EOD | [直达](https://www.chinaday.news/) | 回撤伴随缩量，不能把小盘晨间相对强延续到收盘；局限：媒体汇总；未取得逐股可复核清单 |
| F04 | IH/IF/IC/IM2612 | 2756.4/4018.6/6543.2/6460.8；volume 32755/73157/123957/297482；OI 66170/179235/180259/227187 points/contracts；EOD close/volume/OI | 2026-11-06 15:15 BJT / 2026-11-06 EOD | [直达](https://quote.stockstar.com/futures/ff.htm) | 计算主力合约基差与风格相对变化；局限：公开行情页；并非今日CFFEX官方CSV直读 |
| F05 | IH/IF/IC/IM2612 close basis | -31.01/-35.68/-54.15/-44.55；年化约-9.66%/-7.65%/-7.13%/-5.95% points / annualized %；derived from same-day closes, 42 calendar days | 2026-11-06 EOD / 2026-11-06T20:14:30.101+08:00 | calculation from F02/F04 | 期货仍贴水，IM贴水相对较浅；局限：未扣分红；收盘非结算；并非融资套利报价 |
| F06 | HO/IO/MO2612 | ATM 14.55/18.88/32.54 vol；RR25 -0.69/-1.37/-3.83；BF25 +0.80/+0.91/+0.88；PCR_OI 0.665/0.654/0.616 IV percentage points/ratio；official EOD-derived option metrics | 2026-11-05 EOD / 2026-11-06 07:17 BJT | [直达](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json) | MO左尾保护仍最贵；局限：滞后一个交易日；绝对Gamma峰不等于dealer方向；无11/6实时可执行价差 |
| F07 | China-Commodities futures universe | 806 contracts / 77 products / SHFE+INE+DCE+CZCE+GFEX contracts/products；vendor EOD full-market scan | 2026-11-06 EOD / 2026-11-06 19:04 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) | 原63代码与新增挂牌品种的全范围筛查；局限：full_market_ready是供应商范围，不等于所有附加模块就绪 |
| F08 | Commodity futures crosscheck | SHFE238/INE63/CZCE243/GFEX48匹配且比较价格无差异；DCE HTTP412 source_error contracts；official-vendor EOD advisory comparison | 2026-11-06 EOD / 2026-11-06 19:15 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json) | 四所关键价格可用；DCE仅降级官方核对；局限：成交量/OI/turnover未比；不能说DCE价格不一致 |
| F09 | Commodity options core | 1048 quotes；44/64 products；44 ATM-ready、29 skew-ready；surface/positioning/execution all false contracts/products；core_v1 sampled_strikes | 2026-11-06 EOD / 2026-11-06 19:05 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) | 局部ATM/RR可研究、不能外推全链或执行；局限：bid/ask coverage 0；quote_coverage_complete只指计划样本 |
| F10 | SN2612 | close343340 settle346310；settle -2.04%；5D -7.13%；OI +2235(+5.59%); RV20 28.52%; ATM345000 IV43.96 RR25 -8.78 CNY/t, %, contracts, vol points；EOD/derived local option | 2026-11-06 EOD / 2026-11-06 19:40 BJT | [直达](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-06_commodities_evening.json) | 反弹失败空的三层证据；局限：backwardation反对；实体供需缺失；期权不可执行 |
| F11 | SC2612/SC2701 | close644.0/636.8；settle639.8/631.8；直接相减的 settle spread +8.0（辅助商品报告另有 +5.0 口径，未静默择优）; SC 5D -3.47%; ATM640 IV63.86 CNY/bbl, %, vol points；EOD/curve/local option | 2026-11-06 EOD / 2026-11-06 19:40 BJT | [直达](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-06_commodities_evening.json) | 非农后回踩确认多只可条件化；局限：报告卡使用同口径spread>=4.5；辅助报告字段口径冲突未消除；交易卡只保留来源原规则 spread>=4.5；高IV、实体缺失、外盘冲突；不把不同字段混算 |
| F12 | External WTI/Brent/LME Cu/LME Sn | 90.82/98.38/13719/约45500 USD/bbl or USD/t；context-only public continuous/3M | 2026-11-06 London/Asian snapshot / 2026-11-06 19:15 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json) | SC/SN/CU跨境过滤器；局限：非同刻、非可成交合约对；外部数据usage=context_only |
| F13 | UST 2Y/5Y/10Y/30Y; 10Y real | 4.46/4.59/4.84/5.25%; 2s10s +38bp, 2s30s +79bp,5s30s +66bp; real10Y2.60% yield/bp；official close | 2026-11-05 US close / 2026-11-05 | [直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve) | 股灾下前端领涨的牛陡峭和黄金反常强势；局限：当前盘中10Y约4.855%仅媒体快照；term premium未取得 |
| F14 | DXY/EURUSD/USDJPY/USDCNH | 101.59/1.1216/157.9/6.6665 index/FX；London snapshot | 2026-11-06 ~17:00 BJT / 2026-11-06 | [直达](https://www.reuters.com/world/asia-pacific/dollar-holds-yen-gains-equity-rout-saps-risk-appetite-ahead-payrolls-2026-11-06/) | 就业前美元温和走强而非失控；局限：近似、非同刻；期权skew缺 |
| F15 | Nasdaq/QQQ/SOXX/SMH/VIX | 24315/647.05/131.90/447.73/28.18；1D -5.52/-6.33/-12.75/-11.46/+69.66% index/USD/%；2026-11-05 US close | 2026-11-05 close / 2026-11-05 | [直达](https://www.reuters.com/business/nasdaq-futures-rise-after-steep-ai-selloff-chip-stocks-stabilize-2026-11-06/) | AI链去杠杆与半导体相对弱势；局限：前收不是11/6现金实时 |
| F16 | Nasdaq futures/NVDA premarket | NQ futures约+1.5%~+1.7%；NVDA约+3.6% %；premarket/derivative snapshot | 2026-11-06 pre-open / 2026-11-06 | [直达](https://www.reuters.com/business/nasdaq-futures-rise-after-steep-ai-selloff-chip-stocks-stabilize-2026-11-06/) | 存在技术性稳定但未被现金盘确认；局限：盘前流动性与现金盘不可比 |
| F17 | Gold/GLD/GVZ | spot约4072-4074；GLD前收375.49；GVZ前收25.83 USD/oz, USD, vol index；London snapshot / prior close | 2026-11-06 15:51-17:00 BJT / 11/5 close / 2026-11-06 | [直达](https://www.gold.org/news-and-events/press-releases/central-bank-buying-and-etf-inflows-support-gold-demand-q3) | 黄金从高位回撤但政策信用叙事未失效；局限：三者非同步；没有实时期权链 |
| F18 | China-Stock-Engine | trade_date 2026-11-05；5571 raw quotes/5578 universe；adjustment/RV/tradability not ready；candidate_union empty securities；engine snapshot | 2026-11-05 EOD / 2026-11-06 08:32 BJT | [直达](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/opportunity_radar_latest.json) | 公司研究可继续但今日执行不可用；局限：今日11/6行情未入引擎；Top100/目录不等于全公司基本面 |
| F19 | 限定A股公告检索 | 601899员工持股会议；688281/688012回购报告；600186首次回购；未发现可形成完整利润桥的新经营事实 announcements；official exchange disclosure discovery | 2026-11-06 08:00-20:00 BJT / 2026-11-06T20:14:30.101+08:00 | [直达](https://www.sse.com.cn/disclosure/listedinfo/announcement/) | 本期A股公司Top5为0；局限：限定范围；不代表全市场无公司机会 |
| F20 | Calendar | 21:00 China commodity night; 21:30 US payroll; 22:30 US cash open BJT；legal windows/events | 2026-11-06 / 2026-11-06T20:14:30.101+08:00 | [直达](https://www.bls.gov/schedule/2026/11_sched.htm) | 前30分钟夜盘仅观察，21:45后才可验证；局限：发布延迟/行情延迟仍可能发生 |
| F21 | Tonight China night trade date | session starts Fri 2026-11-06 21:00, expected trading_date Mon 2026-11-09 calendar；exchange session attribution | 2026-11-06 / 2026-11-06T20:14:30.101+08:00 | [直达](https://www.shfe.com.cn/eng/reports/CalendarHoliday/) | 避免把周六自然日写成交易日；局限：各品种夜盘结束时点不同；EC无夜盘 |

### 仪表盘

| 资产 | 最新值 | 变化 | 当前信号 | 数据时间 | 缺口 |
|---|---:|---|---|---|---|
| UST 2Y/10Y/30Y；10Y real | 4.46%/4.84%/5.25%；2.60% | 11/5: -12/-6/-3bp；real -4bp | 牛陡峭；2s30s +79bp，增长/政策路径重定价强于通胀失控 | 11/5 official close；10Y盘中约4.855% | term premium、同日MOVE/HY缺 |
| DXY / EURUSD | 101.59 / 1.1216 | 就业前美元温和偏强 | 未到美元流动性挤兑 | 11/6 London snapshot | 非同刻；FX skew缺 |
| USDJPY / USDCNH | 157.9 / 6.6665 | 日内小幅变化 | CNH稳定，暂未放大中国资产压力 | 11/6 London snapshot | 期权与carry拆解缺 |
| Nasdaq / QQQ | 24,315 / 647.05 | 11/5 -5.52%/-6.33% | 现金盘去杠杆；盘前反弹未确认 | 11/5 close；11/6 NQ盘前约+1.5%~+1.7% | 现金盘22:30才开 |
| SOXX / SMH | 131.90 / 447.73 | 11/5 -12.75%/-11.46% | 半导体Beta显著弱于QQQ | 11/5 close | 盘前/借券/beta未核 |
| WTI / Brent | 90.82 / 98.38 | 11/5 settlement +2.72%/+3.88%；11/6小幅续升 | 地缘风险溢价与现货紧张尚未分离 | 11/6 context snapshot | crack/OVX skew/同步curve缺 |
| Gold / GLD | spot约4,073 / GLD 375.49 | spot自11/5高位回撤；GLD前日+0.83% | 高实际利率下仍强，但就业前不追 | spot 11/6 London；GLD 11/5 close | 非同步；期权链缺 |
| VIX / MOVE / HY OAS | 28.18 / 97.92 / 3.40% | VIX +69.66%；MOVE +4.3%；OAS last-good 11/3 | 权益波动确认，信用未同步失控 | 11/5 / 11/5 / 11/3 | OAS陈旧 |
| SSE50/CSI300/CSI500/CSI1000 | 2787.41/4054.28/6597.35/6505.35 | -0.84/-1.44/-2.13/-2.18% | >4700家下跌、成交缩量；小盘相对回吐 | 11/6 China EOD | 行业逐股贡献未完整取得 |
| IH/IF/IC/IM2612 | 2756.4/4018.6/6543.2/6460.8 | -0.79/-1.51/-2.03/约-2.18%；OI -950/-3348/-3739/-67488 | 全线贴水；IM/IH晨间强化未延续 | 11/6 EOD public quote | 今日官方CSV未直读；curve次合约缺 |
| HO/IO/MO2612 | ATM 14.55/18.88/32.54；RR25 -0.69/-1.37/-3.83 | ATM 1D -0.97/-0.63/-1.57 vol（截至11/5） | MO左尾最贵，但数据滞后一天 | 11/5 official EOD-derived | 11/6链、dealer sign、live bid/ask缺 |
| SN2612 | close343340/settle346310 | settle -2.04%；5D -7.13%；OI +5.59% | 价跌增仓+LME弱+RR25 -8.78，候选空；backwardation反对 | 11/6 EOD | 物理与执行报价缺 |
| SC2612/2701 | close644.0/636.8；settle639.8/631.8 | SC 5D -3.47% | 曲线仍近强远弱，但高IV和外盘冲突 | 11/6 EOD | physical/bid-ask缺 |
| CU2612/2701 | close spread +1180；settle +1080 | CU settle -1.14%；5D -2.52% | 曲线韧性但已高于旧不追价阈值 | 11/6 EOD | 实体A/B缺；需同刻LME |
| Commodity Options / Stock capability | 44/64 products；ATM44/skew29；Stock trade_date11/5 | surface/positioning/execution false；Stock今日未刷新 | 局部研究可用、执行不可用；A股公司Top5=0 | 11/6 commodity EOD / 11/5 Stock | bid/ask=0；adjustment/RV/tradability缺 |

### 覆盖与可得性

- **美国利率/外汇/权益/波动：** 应覆盖项均扫描；2/5/10/30Y、10Y real、DXY、EURUSD、USDJPY、USDCNH、QQQ/SOXX/SMH、油金与VIX可得；term premium、同步FX skew、当日HY OAS不足，分别留缺。
- **中国股指/期权：** 今日现货与IH/IF/IC/IM主力公开EOD可得；HO/IO/MO只取得11/5合法last-good，较今日EOD滞后一个交易日；ETF期权精确指标未出现在本次引擎入口，不能替代。
- **中国商品：** 77品种、806合约、五所完成供应商EOD扫描；DCE官方交叉核对HTTP412只限制“已官方核对”表述，不连带否定供应商价格；basis、会员持仓、部分仓单和完整期权链不足。
- **A股公司：** China-Stock-Engine仅至11/5且复权、RV、tradability未就绪；今日限定检索上交所回购/员工持股/经营披露，获得0个可进入统一Top5的新公司候选。数据不足不是“市场无机会”。

## 三、相比严格前序真正发生了什么

- **中国风格反转：** 11/5 IM相对IH强势在11/6收盘被逆转：CSI1000 -2.18%而SSE50 -0.84%，IM/IH主力比率约2.371→2.344；晨间触发未确认，idea移出Top5。
- **A股广度恶化但成交缩量：** >4700家下跌、两市约1.67万亿元且较前日少约0.46万亿元；这是去风险，不足以单独证明系统性信用事件。
- **锡空头证据强化：** SN2612结算-2.04%、OI +5.59%，LME弱且RR25 -8.78；但backwardation与实体缺失反对追空，分数维持72而执行延后至21:45。
- **AI从现金崩盘假说退回相对稳定性测试：** 亚洲科技续跌支持风险溢价，但NQ与NVDA盘前反弹；只有22:30后现金盘顺序条件才能区分技术反抽与持续修复。
- **黄金出现期望中的回撤但事件窗太近：** spot从11/5高位回到约4073，美元略强；政策信用叙事仍有实体需求支撑，但非农前不能把回撤直接当入场。
- **商品全市场口径升级但执行边界不变：** 806合约/77品种扫描完成；Options 44/64、ATM44、skew29，但全曲面/持仓/执行均false；四所官方价格匹配、DCE仅source_error。

## 四、七大全球模块与统一机会Top5

### 1. 美国利率与债券

11/5官方曲线2Y/5Y/10Y/30Y为4.46%/4.59%/4.84%/5.25%，2s10s、2s30s、5s30s分别+38/+79/+66bp；10Y real 2.60%，简化10Y breakeven约2.24%。前端在股灾中领涨，更像增长/政策路径下修而非通胀尾部消失；反证是10Y在就业前回到约4.855%、油价仍在90美元以上，若就业/薪资偏强，曲线可迅速熊平。财政供给方面，3Y/10Y/30Y拍卖在下周；term premium未取得，不把长端韧性单因子化。

### 2. 美元与外汇

DXY约101.59、EURUSD 1.1216、USDJPY 157.9、USDCNH 6.6665。美元仅温和走强、CNH相对稳定，尚不支持“美元挤兑导致全部风险资产下跌”的单因子叙事。就业报告是关键分叉：热数据会抬升2Y/DXY并压制金属与成长；弱数据若同时令油价走强，则可能出现增长与通胀信号冲突。外汇期权skew未取得，不据动量推断仓位。

### 3. Nasdaq / AI

11/5 Nasdaq -5.52%、QQQ -6.33%，SOXX/SMH约-12.75%/-11.46%；11/6盘前NQ约反弹1.5%—1.7%、NVDA约+3.6%。这更像现金流平台与Capex/半导体Beta的相对分化加上拥挤去杠杆，而非已证实的产业需求坍塌。公司经营证据仍是最强反证。首选仅是就业后、现金盘确认后的QQQ多/SMH空主题；没有精确beta与成份权重，只称Dollar-near-neutral代理。

### 4. 原油与能源

WTI/Brent约90.82/98.38，较11/5结算小幅续升；SC日盘修复但局部ATM IV高达63.86%。地缘运费、炼厂裂解、实物库存与金融流动性没有被同一时点拆开，故不能把油价反弹直接映射成中国化工全面多头。EIA周报因假日顺延至11/13，超过SC卡的时间退出，不能事后延长计划。OVX前收约60，实时skew缺。

### 5. 黄金

10Y real仍在2.60%，黄金却维持4,000上方；WGC Q3央行与ETF需求支持“政策信用/分散化”叙事，但spot从高位回至约4,073、DXY略强。结论是**叙事增强后短线回撤，不等于立即买点**。CFTC最新可用持仓仍旧，期权链未同刻核；MGC不是限损工具，Call Spread只有取得同到期bid/ask与净权利金才具有限损属性。

### 6. 中国50/300/500/1000与期权

今日小盘更弱，IM/IH主力比率约由2.371降至2.344；晨间“多IM/空IH”没有得到EOD确认，不能重置触发或假设成交。四主力均贴水，IM贴水相对浅但OI大降；收盘basis年化仅为比较，不是套利可得回报。11/5期权显示MO2612 ATM32.54、RR25 -3.83，左尾保护最贵，但今日链缺失，绝对Gamma峰也不能推出dealer净方向。结论：今天无合格中国股指交易；下一窗口11/9 09:30。

### 7. 风险与流动性

VIX 28.18、VXN/VVIX高位，MOVE 97.92；HY OAS只有11/3 last-good约3.40%，HYG前日跌幅有限。因此“权益恐慌”已确认，“信用衰退”未确认。最危险的共因子是就业数据令美元、实际利率、科技与金属同时跳变；任何商品夜盘方向单都必须把21:30前后的相关性断裂纳入。

### 统一Top5

| 排名 | idea_id / 机会 | 方向/期限 | 三轴判断 | 分项=总分 | 最关键定价差与风险 |
|---:|---|---|---|---|---|
| 1 | COM-M-SN2612-LME-DIVERGENCE-FAILED-BOUNCE-SHORT-20261106<br>SN2612反弹失败空 | short / 1-5D | 研究：有边际优势<br>证据：三层支持、一层反对、一层缺失<br>执行：21:45后顺序触发；not execution-ready | 20+17+15+12+8=72 | 内盘此前相对LME的溢价仍可能回吐；不能把汇率/税费当零；反证：backwardation反对、实体供需缺失、跳空追空赔率差 |
| 2 | US-AI-QQQ-SMH-RELATIVE-STABILIZATION-20261106<br>多QQQ、空SMH的现金流/Capex Beta相对价值 | relative long/short / 3-10D | 研究：待验证优势<br>证据：经营分化+价格分化；现金盘确认缺<br>执行：就业后现金盘前30分钟观察；待借券/实时成本/beta | 20+16+15+10+9=70 | 市场或过度把监管/Capex冲击等同于全部AI现金流；反证：AMD/Arm/NVIDIA经营证据反对基本面坍塌叙事、QQQ含半导体且非beta-neutral、盘前可完全反转 |
| 3 | GLD-POLICY-CREDIT-STABILIZATION-20261103<br>黄金政策信用凸性：只等数据后回撤确认 | long bias / optionality research / 5-20D | 研究：有边际优势<br>证据：宏观与实体需求支持；期权执行证据缺<br>执行：待21:30后实率/美元确认和期权链询价 | 20+15+14+10+9=68 | 政策信用与分散化需求可能没有被高实率模型充分解释；反证：美元与实际利率上行可压制、CFTC拥挤且最新持仓发布时间尚未到、现货自高位回撤 |
| 4 | COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106<br>CU2612/2701近强远弱价差多 | long near / short far 1:1 / 3-10D | 研究：待验证优势<br>证据：两层支持，按商品规则上限<=69<br>执行：当前spread已越旧不追价位；只等950-1000回撤 | 19+15+13+11+9=67 | 近端紧张若持续可能令曲线重新扩张；当前绝对水平已定价不少；反证：LME铜弱、RR25 -9.28显示左尾保护贵、A/B物理缺 |
| 5 | COM-M-SC2612-OVERNIGHT-REBOUND-CURVE-HOLD-LONG-20261106<br>SC2612非农后回踩确认多 | long / 1-3D | 研究：待验证优势<br>证据：价格/曲线两层支持；实体缺<br>执行：21:45后；current exact quote required | 18+14+14+11+9=66 | 事件溢价可能未完全反映近月供需；也可能只是地缘噪声；反证：ATM IV63.86高、外盘/实体冲突、TP1坏报价净R<1 |

> 研究分只是优先级，不是胜率。商品机会：SN有三层有效证据可超过70；CU/SC只有两层，分别限制在67/66。Top5为展示上限，不代表未扫描其他品种。

## 五、Top3详细交易研究卡

### 卡1｜SN2612反弹失败空（COM-M-SN2612-LME-DIVERGENCE-FAILED-BOUNCE-SHORT-20261106）

- **新增事实→已定价→分歧：** SN结算-2.04%、OI +5.59%，5日-7.13%；市场已定价一部分内外溢价回吐。分歧是若反弹仍无法让LME与内盘同步修复，剩余溢价可继续收敛；backwardation与实体缺失是最强竞争解释。
- **工具/窗口：** SHFE SN2612，1手=1吨，tick 10元/吨、10元/手；21:00开盘但预期交易日11/9，最早21:45。
- **完整入场顺序：** rebound to 344000-346000 THEN 15m close below 343000 AND same-time LME 3M tin <=45800; only then entries 343000/342000/341000 at 30/30/40。
- **分批：** 343000/342000/341000，30%/30%/40%，加权341900。直接低开至≤340000不反弹，放弃。
- **止损与逻辑失效：** 计划止损351000；15分钟收于351000上或LME锡>47800为逻辑失效。期货止损不封顶。
- **TP/退出：** TP1 330000；TP2 318000；2026-11-12 14:45时间退出。
- **成本后赔率（每手，成本假设200元）：** 好/中/坏入场343000/342000/341000，风险8200/9200/10200；TP1净R 1.56/1.28/1.06，TP2净R 3.02/2.59/2.24。动态保证金、限幅与滑点仍须询价。
- **预算/压力：** 试仓≤0.35% NAV、确认≤0.75%、锡主题≤1.25%；一至两个限幅、保证金上调、LME/SHFE错时假日、CNY跳变必须可承受。
- **状态：** research edge=有；evidence=部分充分；execution=not ready；signal=未满足；position=未提供/未知。

### 卡2｜多QQQ、空SMH相对价值（US-AI-QQQ-SMH-RELATIVE-STABILIZATION-20261106）

- **新增事实→已定价→分歧：** 半导体比QQQ多跌约5个百分点以上，盘前反弹说明最悲观叙事正在被测试。分歧是云平台现金流相对Capex Beta仍可能被低估；最强反证是芯片经营数据仍强，短端反弹可演变成轧空。
- **工具/窗口：** QQQ现金ETF多、SMH现金ETF空；22:30—23:30 BJT。非beta-neutral；先核借券。
- **完整入场顺序：** wait first 30m; require 30m QQQ/SMH close >=1.45 AND VIX <=28.36 AND QQQ >=638.94; THEN ratio pullback holds 1.44, enter 30/30/40。
- **规模：** 每边约USD100k：N_QQQ=floor(100000/实时QQQ)，N_SMH=floor(100000/实时SMH)。11/5的154/223只是旧时点，不复用。
- **止损/TP：** 30分钟比率<1.40或QQQ<638.94且广度恶化；TP1 1.52、TP2 1.58；11/12美股收盘退出。
- **成本后赔率：** 实时佣金、SMH borrow、滑点、beta均未知，故好/中/坏净R待评分，不编数字；公式=股数×逐腿价格变化−费用−借券费。
- **放弃：** 比率开盘≥1.52、VIX>32、HYG日跌>1%、无法locate或价差异常。
- **预算/压力：** 试仓≤0.50%、确认≤1.00%、AI相对主题≤1.50%；借券召回、芯片轧空、相关性反转和现金开盘跳空。
- **状态：** research=待验证；evidence=部分；execution=not ready；signal=未满足；position=未提供/未知。

### 卡3｜SC2612非农后回踩确认多（COM-M-SC2612-OVERNIGHT-REBOUND-CURVE-HOLD-LONG-20261106）

- **新增事实→已定价→分歧：** 日盘close644、settle639.8，近远月仍偏强；市场已计入部分地缘溢价。分歧是近端结构能否在就业/美元冲击后继续支撑；最强反证是ATM IV63.86、高波动与实体缺证。
- **工具/窗口：** INE SC2612，1手=1000桶，tick0.1元/桶、100元/手；21:45后。
- **完整入场顺序：** pullback 640-642 AND 15m close not below 638 AND settlement-comparable SC2612-SC2701 spread >=4.5 AND same-time Brent>=98.50 THEN 15m reclaim 646; entries 646/647/648 at 30/30/40。
- **分批/放弃：** 646/647/648，30/30/40，加权647.1；直接≥650无回踩、精确合约报价缺失或源冲突则放弃。
- **止损/失效：** 止损636；15分钟<636、Brent<97或价差<3.0任一失效。
- **TP/退出：** TP1 660、TP2 680；11/10 22:45退出。
- **成本后赔率（每手，成本假设1500元）：** 好/中/坏风险11500/12500/13500；TP1净R 1.09/0.92/0.78，TP2净R 2.83/2.52/2.26。坏报价对TP1无优势，不能为凑单追价。
- **预算/压力：** 试仓≤0.35%、确认≤0.75%、油主题≤1.25%；保证金不是最大亏损。
- **状态：** research=待验证；evidence=两层；execution=not ready；signal=未满足；position=未提供/未知。

## 六、黄金特别研究

**判断：增强后回撤，未失效，执行证据不足。** 10Y real 2.60%、DXY约101.6与黄金约4073形成高实率下的相对韧性；WGC的央行与ETF需求是独立于价格的实体证据。竞争解释是实际利率再上行、美元反弹和流动性抛售。

- **3—6个月Call Spread：** 理论上最能限定损失，但必须先取得同到期链、bid/ask、IV、Delta与净借记；不沿用旧strike，不称“已便宜”。
- **MGC微型黄金：** 可在就业后用于方向确认，但保证金与计划止损都不封顶。
- **黄金多＋长债Put Spread：** 可隔离名义利率上行，需两腿真实IV/成本并压力测相关性反转。
- **反向或不交易：** DXY>102.2 AND 10Y real>2.70% AND gold<4000时优先不交易/条件退出；单一指标不触发反向。
- **预算：** 没有期权净借记，不给手数；黄金、美元和久期风险合并计入同一宏观主题。

## 七、AI特别研究

盈利兑现与长期变现必须分开。微软经营现金流仍强，Meta/Alphabet的高Capex压低自由现金流；AMD/Arm/NVIDIA经营增长反对“需求坍塌”。当前价格冲击更接近监管/Capex担忧与拥挤去杠杆。QQQ/SMH是主题代理，不是精确成份或beta中性；SOXX/SMH本身也含不同权重与设备链。

最自然表达是就业后现金盘确认的QQQ多/SMH空；实质不同的替代是只做QQQ有限风险Call Spread（待报价）或完全不交易。若SMH相对QQQ站回、VIX回落且信用稳定，则相对空芯片失效；若平台公司下一轮现金流指引同步恶化，则“现金流龙头”多头也失效。

## 八、中国50/300/500/1000与公司专项

| 品种 | 11/6现货 | 2612收盘 | volume / OI / ΔOI | close basis | 42天简单年化basis |
|---|---:|---:|---:|---:|---:|
| IH / SSE50 | 2787.41 | 2756.4 | 32,755 / 66,170 / -950 | -31.01 | -9.66% |
| IF / CSI300 | 4054.28 | 4018.6 | 73,157 / 179,235 / -3,348 | -35.68 | -7.65% |
| IC / CSI500 | 6597.35 | 6543.2 | 123,957 / 180,259 / -3,739 | -54.15 | -7.13% |
| IM / CSI1000 | 6505.35 | 6460.8 | 297,482 / 227,187 / -67,488 | -44.55 | -5.95% |

basis是收盘对收盘、未扣分红的研究量，不是可实现套利。今日次合约曲线未取得；11/5的3/5/20日向量只保留为last-good，不与今日窗口拼接。HO/IO/MO2612分别映射IH/IF/IM；IC没有默认一一对应CFFEX指数期权。11/5 MO左尾最贵，但11/6链缺，不能把PCR或Gamma峰写成dealer净头寸。

公司研究双通道结论：价量入口扫描到11/5但adjustment/RV/tradability缺；独立公司目录仅两家满足最小包、无共识预期。11/6限定公告检索得到紫金员工持股会议与若干回购进展，均不足以建立售价—销量—成本—库存—套保—Capex—少数股东的完整利润桥。个股不如指数/商品表达，统一Top5中A股公司为0。

## 九、下一24小时/7天风险日历与今晚夜盘地图

| 北京时间 | 事件 | 资产 | Delta/Vega/执行 |
|---|---|---|---|
| 2026-11-06 21:00 | 中国商品夜盘开盘（预期交易日11/9） | SN/SC/CU/AU/AG/能化 | 0-15m只记录开盘缺口、深度与同刻外盘；不下方向单 |
| 2026-11-06 21:15 | 夜盘15分钟验证 | 商品 | 若价差/外盘不同步则全部候选冻结 |
| 2026-11-06 21:30 | 美国10月就业报告 | rates/USD/gold/AI/oil/metals | 数据前不加Delta/Vega；21:30-21:45等待第一轮跨资产重定价 |
| 2026-11-06 21:45 | 夜盘30/45分钟后首个可行动检查 | SN/SC/CU | 只按完整AND/THEN顺序触发；坏报价或跳空直接放弃 |
| 2026-11-06 22:30 | 美国现金市场开盘 | QQQ/SMH/GLD/HYG/VIX | 前30m观察；23:00后才评估AI相对价值 |
| 2026-11-07 01:15 | Fed Bowman讲话 | 2Y/USD/growth/gold | 若2Y/DXY再鹰，削减成长Delta与黄金Vega |
| 2026-11-07 04:30 | CFTC持仓（截至11/3，发布时间待最终页面确认） | gold/oil/metals | 只更新拥挤，不回填为当前已知 |
| 2026-11-09 09:00/09:30 | 中国商品/股票股指开盘；中国CPI/PPI 09:30 | China index/commodities/CNY | 周末跳空压力；已触发主题名义减30%-50%或保持可承受整数手 |
| 2026-11-10 21:30 | 美国CPI | rates/USD/gold/AI | 长Vega须有真实净成本；无报价不建 |
| 2026-11-10/11/13 02:00 | 美国3Y/10Y/30Y拍卖 | curve/gold/growth | 预留尾部供给风险；DV01而非名义配平 |
| 2026-11-13 01:00 | EIA WPSR（假日顺延） | WTI/Brent/SC | 超过SC时间退出，不得借此延长旧计划 |
| 2026-11-13 21:30 | 美国PPI | rates/USD/equities | 报告7天边界外临近项；下一版核准 |
| 2026-11-09至11-13（未定） | 中国社融/信贷可能窗口；CoreWeave/Cisco/AMAT等财报周 | CNY/China index/AI | 确切发布时间未由原始页面逐项核定，只列条件风险，不作为精准催化 |

### 今晚三种情景与15/30/45分钟验证

1. **就业偏弱、收益率和DXY下行：** 黄金与成长可能先涨；SN空单仍须LME≤45800且反弹失败，不能因美元弱而自动取消；SC需Brent和曲线共同确认。
2. **就业/薪资偏强、2Y和DXY上冲：** 金属下压最明显，但SN若直接≤340000仍禁止追空；黄金长Vega推迟；AI相对价值等待现金盘而非用期货替代。
3. **就业混合、收益率/油价背离：** 全部条件单降为观察；相关性断裂时不以单一美元或油价解释。

21:15只看开盘缺口与深度；21:30数据发布；21:45才是首个合法后数据检查。EC无夜盘，下一真实窗口11/9 09:00；股指/股票下一窗口11/9 09:30。

## 风险预算、状态修订与发布校验

- 试仓0.25%—0.75% NAV，确认0.75%—1.50%，同一高确信主题合计不超过2.5%—3.0%；更紧的专属上限优先。
- 任何手数公式均以**最坏计划损失**而非保证金为分母；期权只有取得真实净借记才可计算数量。
- SN、CU、A股矿业与CNY为同一金属/中国因子；QQQ、SMH、A股算力为同一AI因子；黄金、美元、长债合并压力测。
- 旧idea：AI父idea保留；SC旧空方向失效后用parent/child保留历史；IM/IH未触发、不得重置ID或冒称亏盈；实际持仓均未提供/未知。
- **预发布校验：** 分数加总与上限通过；四组basis、曲线bp、SN/SC逐腿情景重算通过；DST与合法窗口通过；MD/JSON同源；未解缺口为11/6股指期权链、live bid/ask/borrow、SN/SC实体、beta与同日信用。

## 关键来源

- [U.S. Treasury daily par yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve)（2026-11-05；支持：2Y/5Y/10Y/30Y closes、curve spreads）
- [U.S. Treasury real yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)（2026-11-05；支持：10Y real yield）
- [BLS November 2026 release calendar](https://www.bls.gov/schedule/2026/11_sched.htm)（2026-11-06；支持：payroll/CPI/PPI timing）
- [Nasdaq futures rise after steep AI selloff](https://www.reuters.com/business/nasdaq-futures-rise-after-steep-ai-selloff-chip-stocks-stabilize-2026-11-06/)（2026-11-06；支持：US cash selloff、premarket stabilization、NVDA premarket）
- [Dollar gains ahead of payrolls](https://www.reuters.com/world/asia-pacific/dollar-holds-yen-gains-equity-rout-saps-risk-appetite-ahead-payrolls-2026-11-06/)（2026-11-06；支持：FX snapshot、Treasury move、Fed pricing）
- [China shares close lower after AI-led global selloff](https://www.reuters.com/world/asia-pacific/asian-stocks-tumble-ai-led-wall-street-selloff-2026-11-06/)（2026-11-06；支持：China EOD direction、Asia tech selloff）
- [World Gold Council Q3 2026 trends](https://www.gold.org/news-and-events/press-releases/central-bank-buying-and-etf-inflows-support-gold-demand-q3)（2026-10-29；支持：central bank purchases、ETF flows）
- [CFTC futures-only COT](https://www.cftc.gov/dea/futures/other_sf.htm)（2026-10-27 last-good；支持：gold positioning staleness）
- [EIA weekly petroleum schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（2026-11；支持：WPSR delay to 2026-11-13 01:00 BJT）
- [China-Options-Engine radar_latest](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)（2026-11-05；支持：HO/IO/MO metrics、option data quality）
- [China-Commodities-Engine run status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（2026-11-06；支持：806 contracts/77 products、module quality）
- [China-Commodities-Engine option quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)（2026-11-06；支持：44/64 coverage、execution/positioning limits）
- [China-Commodities-Engine option local surfaces](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)（2026-11-06；支持：SN/SC/CU/AU/AP local ATM/RR25/BF25）
- [China-Commodities-Engine official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)（2026-11-06；支持：four exchanges matched、DCE source_error）
- [China-Stock-Engine opportunity radar](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/opportunity_radar_latest.json)（2026-11-05；支持：price scan capability、execution gaps、empty candidate union）
- [SSE listed-company announcements](https://www.sse.com.cn/disclosure/listedinfo/announcement/)（2026-11-06；支持：bounded A-share disclosure discovery）
- [Strict prior global morning report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-06_morning.json)（2026-11-06；支持：stable idea IDs、prior parameters; not current prices）
- [Strict prior same-edition evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-05_evening.json)（2026-11-05；支持：stable ledger and revision history; not current evidence）

## 十、今日行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：SN2612反弹失败空、SC2612非农后回踩多、QQQ多/SMH空相对价值、CU2612/2701回撤后近多远空。  
C. 今天继续观察：黄金数据后回撤、IM/IH是否在11/9重新修复、AP事件凸性、EC反弹失败、A股公司公告经营兑现。  
D. 今天必须回避或若此前已建仓则有条件退出：回避21:30前抢跑、SN低开追空、SC≥650追多、CU价差1180追价、把11/5期权当11/6报价；只有自有仓位触及原失效条件时才按原计划条件退出。
