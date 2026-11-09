# 全球跨资产机会雷达晚间版｜2026-11-09

- 实际生成截点：2026-11-09T20:03:27+08:00
- 版别：evening；prompt=radar_2026-10-12_stock_v1；commodity_consumer=core_2026-10-17_v1；research_quality=2026-10-21_v1
- 市场状态：中国日盘已收；欧洲现金交易中；美国现金盘前；中国商品21:00夜盘尚未开始
- 最近完成会话：中国股票/期指/商品日盘 2026-11-09；美国现金最近完整日 2026-11-06
- 下一合法窗口：中国商品 2026-11-09 21:00；美国现金 22:30；中国股票/股指期货 2026-11-10 09:30
- 实际持仓：未提供/未知；本文仅为研究与条件策略，不代客下单。

## 0. 事实台账与数据边界

|fact_id|标的/事实|数值与口径|观测/known_at|来源|支持判断|局限|
|---|---|---|---|---|---|---|
|F-CALENDAR|global sessions|China EOD complete; Europe open; US premarket; commodity night not started；calendar/status|2026-11-09T20:03:27+08:00；2026-11-09T20:03:27+08:00|CFFEX/SHFE/CME/NYSE calendars|legal windows and no false 20:00 execution|venue/product hours can differ|
|F-UST|UST 2Y/5Y/10Y/30Y|4.51/4.64/4.86/5.26%; 2s10s +35bp; 2s30s +75bp; 5s30s +62bp；official indicative close|2026-11-06 ~15:30 ET；2026-11-06|[直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve)|high-rate and term-premium backdrop|par curve, not executable intraday quotes|
|F-REAL|UST 10Y real / inferred BEI|2.63% / 2.23%；official real close / arithmetic|2026-11-06 ~15:30 ET；2026-11-06|[直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)|gold opportunity-cost counterevidence|BEI is nominal-real approximation|
|F-FX|DXY/EURUSD/USDJPY/USDCNH|102.06 / 1.1165 / 158.22 / 6.6719；Europe-session observations|2026-11-09 17:26-19:10 BJT；2026-11-09|Reuters / Investing currency pages|modestly softer USD supports gold; CNH orderly|non-synchronous; FX skew unavailable|
|F-US-PRE|Dow/S&P/Nasdaq100 futures; NVDA|+0.73/+0.40/+0.21%; NVDA -4.5% premarket；US premarket|2026-11-09 05:10 ET；2026-11-09 18:10 BJT|[直达](https://www.reuters.com/world/china/global-markets-view-europe-2026-11-09/)|fragile risk repair and AI-specific stress|premarket can reverse at cash open|
|F-EUROPE|FTSE100/FTSE250|+0.6% / -0.4% at 10:54 GMT；live cash|2026-11-09T10:54:00Z；2026-11-09|[直达](https://www.reuters.com/world/uk/londons-ftse-100-climbs-as-miners-gain-firmer-gold-prices-2026-11-09/)|large-cap/miner support; breadth mixed|UK is not whole Europe|
|F-US-EQ|QQQ/SOXX/SMH|656.10 / 136.53 / 463.96; +1.40/+3.46/+3.57%；cash close last-good|2026-11-06T16:00:00-05:00；2026-11-06|market closes / Cboe commentary|Friday chip rebound baseline|not Monday cash price|
|F-OIL|Brent/WTI|96.67 / 89.87 USD/bbl; -1.7/-1.0%；Europe-session futures|2026-11-09T08:30:00Z；2026-11-09|[直达](https://www.reuters.com/business/energy/oil-prices-fall-trump-signals-us-iran-de-escalation-2026-11-09/)|SC failed-rebound short external layer|shipping attacks and supply outages remain|
|F-GOLD|spot gold|4123.46 USD/oz; +1.4%；spot|2026-11-09T04:28:00Z；2026-11-09|[直达](https://uk.marketscreener.com/news/gold-rises-over-1-as-softer-oil-prices-ease-inflation-worries-ce785fd3d98dff22)|short-term gold narrative improves|live IV/skew and ETF daily flow unavailable|
|F-RISK|VIX/MOVE/HY OAS|25.64 / 92.77 / 3.48% last-good；close / secondary close / official series|2026-11-05 to 2026-11-06；2026-11-09|Cboe / Investing / FRED|risk elevated before CPI|mixed timestamps; MOVE secondary; HY stale|
|F-CN-CASH|SSE50/CSI300/CSI500/CSI1000|2789.15/4056.11/6586.18/6499.74; +0.06/+0.05/-0.17/-0.09%；secondary EOD close|2026-11-09 15:00 BJT；2026-11-09|Investing historical pages|large caps slightly outperformed small/mid|SSE50/CSI500 mirrors conflict slightly; not execution source|
|F-CN-FUT|IH/IF/IC/IM2612|2765.8/4023.6/6532.8/6448.6; OI63014/173775/173023/279836；secondary EOD quote|2026-11-09 15:00 BJT；2026-11-09|[直达](https://www.9qihuo.com/hangqing?heyue=IF2612)|basis and style comparison|not official connector; official ΔOI unavailable|
|F-CN-OPT|HO/IO/MO2612 last-good|ATM 16.71/21.15/35.64%; RR25 -1.97/-1.86/-4.82 vol；official EOD analytics last-good|2026-11-06；2026-11-07T07:20:53+08:00|China-Options-Engine@471a8ad4 data/radar_latest.json|MO downside protection was richest on last-good date|stale for Nov9; history empty; dealer sign unknown|
|F-COM-SCOPE|China commodities|77 products, 806 contracts, five exchanges；vendor EOD scope|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine@c391cc55 data/radar_latest.json|full-market scan|vendor prices; volume/OI not independently official-checked|
|F-COM-OPT|commodity options core_v1|44/64 products; 1058 sampled quotes; ATM44; skew26; surface/positioning/execution0；sampled EOD analytics|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine@c391cc55 data/options/quality_latest.json|local ATM/skew research only|68.75% product coverage; not full chain; no bid/ask|
|F-NIGHT|historical China commodity night snapshot|assigned trading_date 2026-11-09; coverage52.1092%; not tonight；vendor latest-trade as-of snapshot|2026-11-06 night to 2026-11-07 early；2026-11-07T06:02:34+08:00|China-Commodities-Engine data/night_session/last_run_status.json|last-good context only|official_night_close_verified=false; OHLCV scope unverified|
|F-CROSS|commodity futures official crosscheck|SHFE238/INE63/CZCE243/GFEX48 comparable groups; no credible price difference; DCE HTTP412；partial crosscheck|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine data/crosschecks/futures_latest.json|key vendor price confidence not globally invalidated|partial; volume/OI not official-checked|
|F-AG|AG2702|close12632; settle12610; dOI+8065; 5D+6.95%; RV20 39.87%; silver52.525; ATM IV45.45%；EOD plus external snapshot|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine@c391cc55|three-layer conditional long|external and domestic timestamps differ; skew/execution not ready|
|F-CU|CU2612-CU2701|close spread1150; near dOI-3691 / far+1455; LME copper13853; CU ATM17.20%, RR25 -7.11；EOD plus external snapshot|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine@c391cc55|calendar resilience but wait pullback|no spot basis/warehouse confirmation; no live depth|
|F-SC|SC2612|close631; settle637.6; 5D -14.24%; dOI+1117; spread7; Brent96.42-96.67；EOD plus external snapshot|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine and Reuters oil|failed rebound short setup|geopolitical gap and curve reversal counterevidence|
|F-AP|AP701|close5860; settle5887; dOI-12816; RV20 37.20%; ATM IV35.61%, RR25 -1.82；EOD sampled analytics|2026-11-09；2026-11-09T19:32:06+08:00|China-Commodities-Engine@c391cc55|event convexity research|two layers only; no bid/ask/net debit|
|F-STOCK|China Stock Engine|5579 universe/5573 quotes; candidate_union0; adjusted coverage0; two-company evidence directory；EOD engine data|2026-11-06；2026-11-07T00:32:53Z|China-Stock-Engine@c0b7c872 data/latest|broad scan unavailable for Nov9 execution|no rerun after code fix; tradability/adjustment missing|

仓库读取状态：Global/Options/Commodities/Stock均为`ok`；Options history=`empty`；Commodity `report_input_latest`与`night_session/latest`=`empty`而非截断；没有把旧夜盘、读取时间或旧报告当成当前报价。EOD与20:00海外行情仅在明确的跨时区映射中比较，不作同刻收益归因。

## 1. 100字以内一句话结论

> 全球风险修复仍脆弱：油价回落、金银走强而AI盘前再受冲击，最清晰背离在白银外盘强势尚未被中国AG完全吸收；今晚只挂条件，不追价。

## 2. 全市场仪表盘

|资产|最新值|1日/近期变化|信号|时点与属性|
|---|---:|---|---|---|
|UST 2/5/10/30Y|4.51/4.64/4.86/5.26%|+5/+5/+2/+1bp|2s10s+35bp; 2s30s+75bp; 5s30s+62bp|2026-11-06 official close；Treasury par curve; intraday 10Y around4.87% secondary|
|10Y real / BEI|2.63% / 2.23%|+3/-1bp|high real yield remains gold/long-duration counterweight|2026-11-06 official close；real curve / inferred|
|DXY / EURUSD / USDJPY / USDCNH|102.06 / 1.1165 / 158.22 / 6.6719|USD modestly softer in Europe|CNH orderly; yen still weak|2026-11-09 Europe session；non-synchronous; no skew|
|QQQ / Nasdaq futures|656.10 Friday close / Nasdaq100 fut +0.21%|QQQ +1.40% Friday|risk repair fragile before CPI|11/6 cash; 11/9 05:10 ET premarket；mixed close/premarket clearly separated|
|SOXX / SMH / NVDA|136.53 / 463.96 Friday; NVDA -4.5% premarket|+3.46/+3.57% Friday|sector rebound not equal to issuer risk repair|11/6 close; 11/9 premarket；NVDA premarket can reverse|
|WTI / Brent|89.87 / 96.67|-1.0/-1.7%|de-escalation pressure; shipping risk remains|2026-11-09 08:30 GMT；live futures, not China EOD|
|Spot gold / GLD|4123.46 / 372.52 last-good|spot +1.4%; GLD Friday -0.79%|policy-credit narrative slightly strengthens, but CPI/real-yield risk|11/9 spot; 11/6 GLD；different timestamps; IV unavailable|
|VIX / MOVE / HY OAS|25.64 / 92.77 / 3.48% last-good|not refreshed at cutoff|risk elevated, comparison stale before US open|11/5-11/6；mixed primary/secondary|
|SSE50/CSI300/CSI500/CSI1000|2789.15/4056.11/6586.18/6499.74|+0.06/+0.05/-0.17/-0.09%|large-cap relative defense continued modestly|2026-11-09 EOD；secondary mirrors; small conflicts disclosed|
|IH/IF/IC/IM2612|2765.8/4023.6/6532.8/6448.6|OI63014/173775/173023/279836; official ΔOI unavailable|basis -0.84/-0.80/-0.81/-0.79%; Dec annualized about -7.84/-7.50/-7.59/-7.36%|2026-11-09 EOD；secondary futures quote|
|IH/IF/IC/IM2611|2785.2/4048.4/6569.4/6487.4|volume8089/19755/25384/45043|front basis -0.14/-0.19/-0.25/-0.19%|2026-11-09 EOD；secondary quote; front/deferred not same roll risk|
|HO/IO/MO2612|ATM16.71/21.15/35.64%; RR25 -1.97/-1.86/-4.82|no Nov9 refresh|last-good MO put skew deepest|2026-11-06 EOD；stale; dealer sign unknown; execution blocked|
|AG2702 / external silver|12632 close / 52.525 USD/oz|settle +0.28%; dOI+8065|external strength not fully absorbed; no gap chase|2026-11-09 EOD / 19:10 snapshot；ATM45.45%; skew/surface/execution not ready|
|CU2612/2701|close spread1150; LME copper13853|near OI-3691 / far+1455|backwardation resilient but above entry zone|2026-11-09 EOD；ATM17.20%; RR25 -7.11; no live depth|
|SC2612 / AP701 / LC2701|631 / 5860 / 87480 close|SC -0.91%; AP settle -1.37%; LC close -4.85%|SC failed rebound; AP vol watch; LC pressure not chased|2026-11-09 EOD；sampled options; no execution quotes|
|Stock engine|5579 universe; 5573 quotes; candidate_union0|no Nov9 engine run|Zijin/Baosteel research only; zero new operating fact in bounded official search|trade_date 2026-11-06；not execution-ready|

### 七大全球模块判断

1. **美国利率与债券。** 11月6日官方2/5/10/30Y为4.51/4.64/4.86/5.26%，2s10s、2s30s、5s30s分别+35/+75/+62bp；10Y实际2.63%、推算breakeven 2.23%。增长韧性与拍卖供给仍推高前端/长端，反证是油价回落可能减轻通胀风险。11月9日盘中10Y约4.87%仅为二级观察，未与官方收盘混算。
2. **美元与外汇。** DXY约102.06、EUR/USD 1.1165、USD/JPY 158.22、USD/CNH 6.6719；美元较周五温和回落但日元仍弱。中国银行上调美元存款利率可能放慢结汇与人民币升值，并非美元全面走强的独立证明；FX skew缺失。
3. **Nasdaq/AI。** 周五QQQ/SOXX/SMH反弹1.40%/3.46%/3.57%，但周一Nasdaq100期货仅+0.21%、NVDA盘前-4.5%。这更像从广谱去杠杆转为发行人特异风险，尚不能证明AI盈利与现金流重新主导估值。
4. **原油与能源。** Brent/WTI回落至96.67/89.87，谈判缓和削弱供应溢价；航运袭击与潜在供应中断是最强反证。缺近月曲线、裂解与OVX，故全球油价只作为SC/BU外部映射，不宣称完整现货紧张度。
5. **黄金。** 金价约4123.46、+1.4%，受油价和美元回落支持；但2.63%真实利率与次日CPI仍压制无息资产。央行Q3购金与CFTC净多是背景，ETF日流与当前IV/skew缺失。
6. **中国50/300/500/1000。** SSE50/CSI300略涨、CSI500/1000小跌，大盘防御延续；但当前期指来自二级行情，HO/IO/MO仍停在11月6日。IH↔HO、IF↔IO、IM↔MO可研究，IC没有同标的指数期权，MO/IO仅能作为有beta/basis余险的代理。
7. **风险与流动性。** VIX 25.64、MOVE 92.77、HY OAS 3.48%均为11月5—6日last-good，说明高波动但不能证明11月9日盘前风险已缓和。CPI、拍卖、AI财报与商品夜盘同时集中，相关性断裂和保证金风险高于常态。

### 中国商品全范围扫描与消费协议

- 覆盖：77个产品、806张合约、五所；Top5是展示上限，不是扫描范围。
- **black：** I/JM/J/RB/HC/FG/SA/SF/SM全扫；FG701成交异常与dOI+26716，但close888/settle900冲突，未入榜
- **nonferrous：** CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG全扫；AG最强、CU跨期次之、SN偏度昂贵
- **energy_chemicals：** SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP全扫；SC/BU承压，BR相对强，PP增仓但无独立实体确认
- **new_energy：** LC/SI/PS及GFEX新增全扫；LC2701大跌且IV高，不追空
- **agriculture：** A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK全扫；AP仅波动率观察
- **shipping：** EC全扫；5D -10.37%与contango支持趋势，但现货运价/当晚报价缺失，未入榜
- Options：expected 64、successful 44、product coverage 68.75%、sampled quotes 1058；ATM ready 44、skew ready 26，full_chain_verified=false，surface/positioning/execution=0。
- `quote_coverage_complete`只代表计划内抽样返回，不代表全链；局部ATM/skew可用于研究，不能外推完整期限/wing/PCR/dealer gamma，更不能编bid/ask、净权利金或可成交性。
- Night：历史快照覆盖52.1092%，归属2026-11-09交易日但不是今晚；`official_night_close_verified=false`，供应商OHLCV范围未验证，不能推新多/新空。
- Crosscheck：SHFE238/INE63/CZCE243/GFEX48 price groups without credible differences; DCE official HTTP412; volume/OI not independently official-checked。

## 3. 相较严格前序报告的实质变化

1. **China EOD: precious metals lead, oil/chemicals remain stressed：** AG2702 closes12632 with dOI+8065 and external silver52.525; SC2612 close631 and Brent falls toward96.7. The morning SC long reclaim failed and is closed as research, with no fill assumed.
2. **Cross-asset policy-credit expression improves but remains conditional：** Gold rises 1.4% while oil falls and DXY softens modestly. Gold score rises68→69, but 2.63% last-good real yield and next-day CPI prevent immediate Delta/Vega.
3. **AI repair becomes more issuer-specific：** Nasdaq100 futures +0.21% but NVDA -4.5% premarket; Friday's broad chip rebound is not a sufficient cash-flow confirmation. No AI trade enters Top5.
4. **China large-cap defense persists, but execution data splits：** SSE50/CSI300 slightly positive while CSI500/1000 slip. Nov9 futures are available only from a secondary quote source; HO/IO/MO remain Nov6 last-good, so style work stays observation-only.
5. **Engine freshness diverges：** Commodity engine is current through Nov9 EOD; China Options and China Stock engines remain Nov6. Missing current options/stock data constrains only their dependent conclusions, not the full report.

## 4. 全球统一机会 Top5

|#|idea_id|标的/方向|期限|研究/证据/执行三轴|评分（逻辑/赔率凸性/催化/价格期限波动/拥挤技术）|关键错价与最强风险|
|---:|---|---|---|---|---:|---|
|1|COM-E-AG2702-EXTERNAL-SILVER-GAP-ABSORPTION-LONG-20261109|AG2702 外盘白银强势的缺口吸收多头；conditional long|1-5D|有边际优势；只做吸收后确认；三层支持（价仓/曲线/外盘），期权高IV反证；实体缺；not_ready_wait_2100_gap_absorption_and_live_quote|19/16/16/13/8=72|新idea；外盘银价与国内收盘错时形成定价差，禁止用20:00外盘倒填日盘|
|2|COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106|CU2612/2701 近强远弱跨期；long CU2612 / short CU2701 1:1|1-10D|优势仍在但当前价差高于入场区；三层支持；仓单/实体缺；期权下偏度反证；not_ready_spread_above_entry_zone_and_no_live_depth|20/17/15/12/7=71|revision6→7；分数与参数不变，更新11/9 EOD及夜盘窗口；不把未回撤当触发|
|3|GLD-POLICY-CREDIT-STABILIZATION-20261103|黄金政策信用与通胀风险的有限风险表达；conditional long convexity|3-6M|叙事轻度增强，执行仍待报价；金价/美元/油价三项支持；高真实利率与CPI反对；ETF日流/IV缺；not_ready_no_live_option_debit_or_iv|19/16/15/11/8=69|revision9→10；68→69，因11/9金价+1.4%且油价/美元回落；不追现货|
|4|COM-E-SC2612-DEESCALATION-FAILED-REBOUND-SHORT-20261109|SC2612 去升级后的反弹失败空头；conditional short|1-5D|有方向假设，需曲线与Brent共同确认；两层支持，按规则上限<70；曲线/地缘反证；not_ready_curve_ratio_and_retest_sequence_unmet|19/15/15/10/9=68|新successor；旧SC多头未收复646，关闭且不假定成交；新方向不改写旧idea|
|5|COM-M-AP701-LOCAL-VOL-CONVEXITY-WATCH-20261107|AP701 局部波动率凸性观察；two-sided convexity|1-20D|研究候选，方向与成本待询价；两层且价仓混合；ATM就绪但全曲面/执行未就绪；not_ready_no_bid_ask_cost_or_greeks_for_structure|18/16/13/12/9=68|revision3→4；70→68，dOI-12816且ATM35.61低于RV20 37.20的边际收窄；无报价不构造策略|

- **AG2702。** 新增事实是外盘银52.525与国内AG收盘12632错时背离；市场已定价部分是AG五日+6.95%和ATM IV45.45%，我们的分歧仅在“外盘强势能否被21:00缺口吸收而非一次性跳空”。主要PnL来自确认后的国内补涨；最强竞争解释是高IV/高拥挤已透支，下一项区分观测是缺口、12600回踩和外盘银同步。
- **CU跨期。** 近月与远月OI迁移、价差1150和LME13853支持结构韧性；但当前价差不在950—1000入场区，且缺仓单/现货基差。主要PnL来自近月相对远月的结构扩张，不来自单边铜价；最强反证是回落低于800或LME跌破13750。
- **黄金。** 油价/DXY回落与金价+1.4%使政策信用叙事轻度增强；但高真实利率、次日CPI和缺IV报价意味着错价仍是假设。PnL应来自有限风险凸性而非裸期货追涨；下一项观测是4100、真实利率与美元是否同向确认。
- **SC2612。** 旧多头未收复646而关闭，新successor只研究反弹失败空；油价回落是支持，月差与地缘供应是反证。PnL来自去升级溢价继续压缩，必须先反弹再跌破，不能直接追空。
- **AP701。** ATM IV35.61%与RV20 37.20%保留局部凸性研究，但dOI-12816、价仓混合且无双边报价。没有净借方/Greeks/完整腿时不称便宜、不称有限亏损。

## 5. Top3详细交易研究卡

### 1) AG2702 外盘白银强势的缺口吸收多头

- **结构/快照：** 多1手AG2702；仅在顺序条件全部完成后，期货止损不封顶。2026-11-09 EOD close12632/settle12610；外盘银52.525（19:10 BJT附近）；21:00夜盘未开始；用户持仓/成交未知。
- **入场顺序：** 21:00后：相对12632开盘缺口<=1.5%；随后回踩并连续5分钟守12600；再出现15分钟收盘>=12700，且独立外盘银>=52.30。全部AND；若直接>=12850而未回踩、无双边深度、或美元与真实利率同升则放弃。
- **允许成交情景：** 12700/12720/12750；分批权重 50%/50%/0%。
- **风险与退出：** 计划止损 12480；逻辑失效：外盘银<51.80，或AG 15分钟收盘<12480；TP1 13050、TP2 13400；时间退出 2026-11-13中国日盘收盘前。
- **合约与成本：** multiplier 15，tick 1，tick value 15元；成本为情景假设 450元，不是实报。
|入场|成本后风险|TP1净PnL/R|TP2净PnL/R|
|---:|---:|---:|---:|
|12700|3750|4800 / 1.28R|10050 / 2.68R|
|12720|4050|4500 / 1.11R|9750 / 2.41R|
|12750|4500|4050 / 0.9R|9300 / 2.07R|
- **预算/规模：** 试仓<=0.50% NAV；确认<=0.75%；金银+黄金主题合计<=1.50%；floor(0.005*NAV/4500)手，并受更紧保证金/流动性上限约束。
- **压力：** 22%指示保证金约41613元/手；单个涨跌停静态损失约37725元、两次复合约67905元；流动性消失和保证金上调可使止损失效。
- **执行状态：** not execution-ready；等待真实顺序、双边深度与合法窗口。实际持仓=not_provided_unknown。

### 2) CU2612/2701 近强远弱跨期

- **结构/快照：** 多1手CU2612/空1手CU2701；吨数中性而非Beta或保证金中性。2026-11-09 EOD close spread1150；CU2612 105500、CU2701 104350；LME铜13853；21:00前无当晚行情；用户持仓/成交未知。
- **入场顺序：** 21:15后：价差先回踩950—1000且过程从未低于800；随后15分钟收盘重夺1050；同一时点LME铜>=13750且两腿双边深度合格。全部AND；未回撤或缺深度不交易。
- **允许成交情景：** 950/975/1000；分批权重 50%/50%/0%。
- **风险与退出：** 计划止损 800；逻辑失效：价差<800，或LME铜<13750且期限结构同步转弱；TP1 1400、TP2 1650；时间退出 2026-11-13中国日盘收盘或更早流动性换月。
- **合约与成本：** multiplier 5，tick 10，tick value 50元；成本为情景假设 500元，不是实报。
|入场|成本后风险|TP1净PnL/R|TP2净PnL/R|
|---:|---:|---:|---:|
|950|1250|1750 / 1.4R|3000 / 2.4R|
|975|1375|1625 / 1.18R|2875 / 2.09R|
|1000|1500|1500 / 1R|2750 / 1.83R|
- **预算/规模：** 试仓<=0.35% NAV；确认<=0.75%；铜+紫金主题<=1.25%；floor(0.0035*NAV/1500)对；风险按更紧专属上限。
- **压力：** 两腿各9%静态限幅和11%指示保证金下，毛名义约1049250元、指示保证金约115418元；单边限幅/相关性断裂可使止损与配对失效。
- **执行状态：** not execution-ready；等待真实顺序、双边深度与合法窗口。实际持仓=not_provided_unknown。

### 3) SC2612 去升级后的反弹失败空头

- **结构/快照：** 空1手SC2612；仅做反弹失败，不追空。2026-11-09 EOD close631/settle637.6；SC2612-SC2701 close spread7；Brent约96.4-96.7；21:00前无当晚成交；用户持仓/成交未知。
- **入场顺序：** 21:00后：价格先反弹至632—638；随后15分钟收盘<628；同一时点(SC2612-SC2701)/SC2701<=1.0%且Brent<=96.50；之后第一次回测628失败。全部AND；若直接<=615而未反弹则放弃。
- **允许成交情景：** 628/627/626；分批权重 30%/30%/40%。
- **风险与退出：** 计划止损 638；逻辑失效：15分钟收盘>=638，或曲线比率>1.5%，或Brent>98.50，或新确认供应中断；TP1 610、TP2 595；时间退出 2026-11-10T22:45:00+08:00。
- **合约与成本：** multiplier 1000，tick 0.1，tick value 100元；成本为情景假设 1500元，不是实报。
|入场|成本后风险|TP1净PnL/R|TP2净PnL/R|
|---:|---:|---:|---:|
|628|11500|16500 / 1.43R|31500 / 2.74R|
|627|12500|15500 / 1.24R|30500 / 2.44R|
|626|13500|14500 / 1.07R|29500 / 2.19R|
- **预算/规模：** 试仓<=0.25% NAV；确认<=0.50%；油+航运主题<=1.00%；floor(0.0025*NAV/13500)手，并受更紧保证金/流动性上限约束。
- **压力：** 20%指示保证金约127520元/手；单个18%静态限幅损失约114624元、两次复合约249888元；地缘缺口和保证金追加远大于计划止损。
- **执行状态：** not execution-ready；等待真实顺序、双边深度与合法窗口。实际持仓=not_provided_unknown。

## 6. 黄金特别研究

判断：**中期不变、短期轻度增强但未确认；“政策信用期权”是宏观类比，不代表合同限损**。现货4123.46，10Y真实利率last-good 2.63%，DXY约102.06；CFTC非商业净多179548、周变-6903。央行购金与政策信用是中期背景，不是今天新增催化。
- 3—6个月call spread：只有同到期双边报价与净借方明确后才可比较；净借方上限建议不超过宽度35%，否则不交易。
- 微型黄金期货MGC：流动性通常优于远端期权，但止损不封顶；需4100与美元/实际利率共同确认。
- 黄金多+长债put spread：可能同时受真实利率上行冲击，需先核DV01、相关性与两边成本，不能自动称对冲。
- 反向/不交易：若4000破位且美元、实际利率同升，再评估put spread；CPI前“不交易”当前赔率最好。

## 7. AI特别研究

AI链条继续分成盈利/FCF定价权与远端Capex Beta：芯片、设备、云、网络、数据中心电力和软件不能用一个指数代理。周五芯片强于QQQ说明旧“QQQ多/SMH空”逻辑被价格反证并已退役、未触发且不假定成交；周一NVDA盘前-4.5%又说明发行人治理/政策风险可压过指数修复。
- **多现金流龙头/空Capex Beta：** 仍是研究主题，但缺精确权重、beta、借券与公司级最新现金流，不能称beta-neutral。
- **反向表达：** 若CoreWeave/设备/网络指引验证需求与融资可持续，Capex Beta可能反而跑赢；这是最强竞争解释。
- **ETF/期权：** SOXX/SMH可降低单股风险，但盘前不是执行基准；没有当前IV、bid/ask和腿报价，不构造有限风险价差。
- **下一验证：** 美股开盘后15/30/45分钟宽度、NVDA相对SOXX、CoreWeave/Applied Materials/Cisco的收入、FCF、毛利率和资本开支指引。

## 8. 中国50/300/500/1000与公司专项

|指数/合约|现货|2612|basis|年化basis（约39天）|2611/近月basis|OI与质量|
|---|---:|---:|---:|---:|---|---|
|SSE50/IH|2789.15|2765.8|-23.35|-7.84%|IH2611 2785.2；-3.95 (-0.14%)|2612 OI63014；二级行情，官方ΔOI缺|
|CSI300/IF|4056.11|4023.6|-32.51|-7.50%|IF2611 4048.4；-7.71 (-0.19%)|2612 OI173775；二级行情|
|CSI500/IC|6586.18|6532.8|-53.38|-7.59%|IC2611 6569.4；-16.78 (-0.25%)|2612 OI173023；无同标的指数期权|
|CSI1000/IM|6499.74|6448.6|-51.14|-7.36%|IM2611 6487.4；-12.34 (-0.19%)|2612 OI279836；二级行情|

- 风格：SSE50/CSI300分别+0.06/+0.05%，CSI500/1000分别-0.17/-0.09%，大盘略强；但期现basis四类接近，尚不能把风格收益归因于机构净买或“国家队”。
- 期权last-good（11/6）：HO/IO/MO ATM 16.71/21.15/35.64%，RR25 -1.97/-1.86/-4.82 vol；BF约-0.045/+0.651/+0.563。MO保护最贵仅是旧日观察，history empty、当前PCR/OI/ΔOI/Gamma/IV-RV无法更新，dealer方向未知。
- 策略边界：IH相对IM可继续观察，但无当前期权/官方期指数据，不做dollar-neutral或beta-neutral宣称；calendar/diagonal/butterfly/call-put spread均需11月10日开盘后新forward、IV和成交成本。
- China-Stock-Engine：11月6日5579标的/5573报价，candidate_union=0、复权覆盖0、tradability未就绪。限定官方检索601899与600019，截至11月9日新增经营事实为0；不能由旧价量生成今天信号。
- 紫金利润桥：金银量价、铜价与销量，减成本、库存/套保、汇率、少数股东、Capex；9M矿产金/银量增而铜量降，铜主题并非纯beta。宝钢利润桥：钢价/销量减矿焦成本、库存、产品结构和出口；原料跌而钢价/销量同步弱时并不利好。两者均为研究观察、不可执行。

## 9. 下一24小时/7天风险日历与夜盘地图

|北京时间|事件|风险决策|
|---|---|---|
|11/09 21:00|中国商品夜盘开|AG/CU/SC仅做顺序验证；21:15/21:30/21:45检查，不追开盘缺口|
|11/09 21:40|Fed Bowman讲话|观察美元/真实利率对金银和成长股的冲击|
|11/09 22:30|美股现金开盘|15/30/45分钟核NVDA特异风险、QQQ/SMH宽度、VIX与信用是否同向|
|11/10 02:00|美国3Y国债拍卖|观察前端与2s10s；拍卖尾部不得用盘前曲线替代|
|11/10 09:30|中国股票/股指期货下一合法窗口|重新核IH/IM相对、成交广度、USDCNH；股指无今晚21:00夜盘|
|11/10 21:30|美国10月CPI|发布前避免新增裸Delta/Vega；金银、长债、AI共因子合并预算|
|11/11 01:00|USDA WASDE / EIA STEO|农业与能源候选只在原始表发布后更新实体层|
|11/11 02:00|美国10Y国债拍卖|观察期限溢价与黄金真实利率反证|
|11/13 01:00 / 03:00|EIA周报与表格（延后）|SC/BU/BR重新核库存与裂解；不要沿用旧发布时间|
|11/13 02:00 / 05:30 / 17:00 / 21:30|美国30Y拍卖 / Cisco电话会 / IEA OMR / 美国PPI|长端、AI网络、油品供需和事件Vega分别处理|

今晚21:00三种情景：
- **强势吸收：** AG缺口<=1.5%、守12600并收>=12700，外盘银>=52.30；仅此时考虑分批多。CU若未回撤不追。
- **震荡分化：** AG/CU高开回落但不完成顺序，SC在632—638盘旋；全部观察，21:15/21:30/21:45重核曲线与外盘。
- **风险逆转：** 美元/真实利率上行、银<51.80，或Brent重上98.50/供应中断；取消金银多与SC空，降低Delta/Vega，期货保证金按1—2个限幅压力管理。

发布前实证校验：Top5分项加总与上限通过；AG/CU/SC成本后R已按乘数、tick与情景成本重算；入场→确认→失效顺序可达；美国DST、合法窗口、合约月份与单位已核；MD/JSON同源。未解缺口为当前HO/IO/MO、商品盘口/全链、油曲线/OVX、黄金IV/ETF日流、Stock复权/tradability，以及IH/IF/IC/IM官方ΔOI。CI仅标`pending_or_unverified`。

### 公开与仓库来源

- [U.S. Treasury Daily Par Yield Curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve)（U.S. Treasury，2026-11-06）：2/5/10/30Y yields；curve arithmetic
- [U.S. Treasury Daily Real Yield Curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)（U.S. Treasury，2026-11-06）：10Y real yield；inferred breakeven
- [Fragile calm after AI whiplash](https://www.reuters.com/world/china/global-markets-view-europe-2026-11-09/)（Reuters，2026-11-09）：US premarket；AI risks；Fed pricing
- [Oil falls on Iran de-escalation signal](https://www.reuters.com/business/energy/oil-prices-fall-trump-signals-us-iran-de-escalation-2026-11-09/)（Reuters，2026-11-09）：WTI/Brent；Iran talks；shipping counterrisk
- [FTSE miners gain with gold](https://www.reuters.com/world/uk/londons-ftse-100-climbs-as-miners-gain-firmer-gold-prices-2026-11-09/)（Reuters，2026-11-09）：FTSE100/250；gold-miner breadth
- [Gold rises as oil and dollar soften](https://uk.marketscreener.com/news/gold-rises-over-1-as-softer-oil-prices-ease-inflation-worries-ce785fd3d98dff22)（Reuters via MarketScreener，2026-11-09）：spot gold；policy-rate channel
- [US CPI release calendar](https://www.bls.gov/schedule/2026/11_sched.htm)（BLS，2026-11-09）：CPI and PPI dates
- [Federal Reserve calendar](https://www.federalreserve.gov/newsevents/calendar.htm)（Federal Reserve，2026-11-09）：Fed speaker schedule
- [China index futures quote pages](https://www.9qihuo.com/hangqing?heyue=IF2612)（9Qihuo，2026-11-09）：IH/IF/IC/IM prices, volume and OI
- [CSI300 historical data](https://cn.investing.com/indices/csi300-historical-data)（Investing，2026-11-09）：CSI300 EOD
- [SSE50 historical data](https://au.investing.com/indices/shanghai-se-50-historical-data)（Investing，2026-11-09）：SSE50 EOD
- [CSI500 historical data](https://ph.investing.com/indices/china-securities-500-historical-data)（Investing，2026-11-09）：CSI500 EOD
- [CSI1000 historical data](https://cn.investing.com/indices/csi1000-historical-data)（Investing，2026-11-09）：CSI1000 EOD
- [China Options Engine radar](https://github.com/farfromexact/China-Options-Engine/blob/471a8ad421abf9c01f51e25954230b865e77abc7/data/radar_latest.json)（farfromexact，2026-11-06）：HO/IO/MO last-good analytics；futures EOD through 11/6
- [China Commodities Engine radar](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/radar_latest.json)（farfromexact，2026-11-09）：77-product scan；commodity candidates
- [China Commodities options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/options/quality_latest.json)（farfromexact，2026-11-09）：core sampling coverage；readiness limits
- [China Commodities crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/crosschecks/futures_latest.json)（farfromexact，2026-11-09）：partial official crosscheck
- [China Stock Engine opportunity radar](https://github.com/farfromexact/China-Stock-Engine/blob/c0b7c87287c5562ee4e64d6298b5fa4ffa256d1f/data/latest/opportunity_radar_latest.json)（farfromexact，2026-11-06）：stock engine limitations；candidate union
- [China Stock Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/c0b7c87287c5562ee4e64d6298b5fa4ffa256d1f/data/latest/research_inputs_latest.json)（farfromexact，2026-11-07）：Zijin and Baosteel evidence directory

## 10. 严格四行

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：AG2702缺口吸收后多；CU2612/2701回撤后收复；SC2612反弹失败后空；AP701与黄金期权只待双边报价。
C. 今天继续观察黄金政策信用叙事、IH相对IM防御、AI现金流龙头对Capex Beta、紫金/宝钢利润桥；均不等于可执行。
D. 今天必须回避追21:00金银/铜缺口、直接追空原油/碳酸锂、把11月6日HO/IO/MO当今天报价、无bid/ask期权及未经beta/借券核验的AI相对交易；若此前自有仓位，仅按原失效/时间退出条件处理。