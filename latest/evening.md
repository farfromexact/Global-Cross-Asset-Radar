# 全球跨资产机会雷达晚间版｜2026-11-03

> 研究截点：2026-11-03T20:00:00+08:00。仅供合格投资者研究，不代客下单；实际持仓均为“未提供/未知”。

## 1. 一句话结论

风险偏好转弱但未成信用危机：小盘与AI估值去杠杆、油价地缘反弹并存；最大背离是AI盘前指数修复而个股继续惩罚现金回报，今晚只等AG/SC顺序触发。

## 2. 全市场仪表盘与事实台账

| 资产 | 最新值 | 时点/市场状态 | 晚间判断 |
|---|---:|---|---|
| UST 2Y/10Y/30Y; 10Y real; 2s30s | 4.596% / ~4.90% / 5.29%; 2.63%; +69.4bp | US EOD / lagged；cash closed at BJT20:00 | steep long-end; fiscal/term premium still constrains duration and AI |
| DXY; EURUSD; USDJPY; USDCNH | 101.816; 1.1185; 158.19; 6.6719 | 18:38-18:59 BJT；FX open; secondary | dollar not collapsing enough to validate gold chase |
| QQQ/Nasdaq; SOXX/SMH | 681.09/25164.32; 453.65/508.31 | 11/2 cash close；premarket; cash opens 22:30 | AI deleveraging; futures bounce is not yet cash confirmation |
| US premarket | Dow -0.42%; S&P +0.02%; NQ +0.46%; AAPL -4.5%; PLTR -6.3% | 18:06 BJT snapshot；premarket | cash-flow quality versus capex-beta dispersion |
| WTI/Brent | 97.88/106.58 USD/bbl | European morning snapshot；open; non-settlement | headline convexity high; SC short needs Brent gate |
| Gold spot/futures | 3926.52/3936.3 USD/oz | 11:53 BJT；open but stale to cutoff | policy-credit narrative stable, execution evidence insufficient |
| VIX/MOVE/HY OAS | ~21.22/~101.13/3.26% | mixed last-good；not synchronous | do not call broad crisis; hedge gap risk into elections/JOLTS |
| CSI50/300/500/1000 | 2768.27/4008.87/6327.05/6221.23 | 11/3 EOD；cash closed | morning small-cap relative-long thesis invalidated |
| IH/IF/IC/IM 2612 | 2736.2/3978.8/6283.8/6173.8 | 15:26 BJT secondary；closed; not official settlement | basis -1.16%/-0.75%/-0.68%/-0.76%; next legal window 11/4 09:30 |
| HO/IO/MO 2612 | ATM 16.21/21.66/35.30%; RR25 -0.67/-1.97/-4.42vol | 11/2；analytics ready, 11/3 execution not ready | MO downside skew steeper; dealer direction unknown |
| SC/AG/CU/EC | 698.2/11655/106090/2465 | 11/3 EOD；full baseline failed; exact subset only | AG/SC conditional shorts; CU old long invalid |
| Commodity options | 11/2: 64 expected, 19 successful; ATM-ready19, skew-ready12; 430 records | 11/2 EOD；full_chain=false; surface/positioning/execution=false | local ATM/skew research only; no premium, PCR crowding or dealer gamma claims |
| Commodity Night/crosscheck | 11/3 prior Night collection failed; current 21:00 not started; official compare 0 | 20:00 BJT；expected trading date 11/4 | 21:15/21:30/21:45 staged verification; no old night snapshot reuse |
| China-Stock-Engine | last valid 10/30; 5571 rows; radar rows0 | 08:34 BJT status；research only, execution not ready | bounded public disclosure search found 0 decision-grade new candidate |

中国现金市场已完成11月3日EOD；欧洲盘在交易，美国仅盘前且现金盘22:30才开。美国利率EOD、黄金早盘、FX 18:38与中国EOD不是同一可比时点，故只作条件校准，不把异步变动拼成同一条“因果”。

### 可追溯事实台账

| fact_id | 标的/值/口径 | 观测与known_at | 来源 | 支持判断与局限 |
|---|---|---|---|---|
| F01 | US Treasury 2Y/10Y/30Y：4.596% / ~4.90% / 5.29%（official/verified EOD） | 观测 2026-11-02 US EOD；known_at 2026-11-02；读取 2026-11-03T20:00:00+08:00 | [直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?data=yield&year=2026) | long-end term/fiscal premium remains elevated; 2s30s +69.4bp；局限：not a 20:00 BJT executable quote; 10Y rounded from verified morning report |
| F02 | US Treasury 10Y real / breakeven proxy：2.63% / ~2.27%（official last-good / derived） | 观测 2026-10-29 EOD；known_at 2026-10-29；读取 2026-11-03T20:00:00+08:00 | [直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/textview?data=realyield&year=2026) | gold is not being driven by falling real yields alone；局限：lagged; breakeven proxy = nominal 10Y minus real 10Y and uses non-identical observation dates |
| F03 | DXY / EURUSD / USDJPY / USDCNH：101.816 / 1.1185 / 158.19 / 6.6719（media/secondary intraday observations） | 观测 2026-11-03 18:38-18:59 BJT；known_at 2026-11-03；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.cnyes.com/forex/reuters) | dollar firmer versus CNH/JPY while broadly range-bound；局限：not broker executable; timestamps differ slightly across pairs |
| F04 | QQQ / Nasdaq / SOXX / SMH：681.09 / 25164.32 / 453.65 / 508.31（2026-11-02 cash close） | 观测 2026-11-02 US cash close；known_at 2026-11-02；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.reuters.com/business/retail-consumer/us-stock-futures-mixed-apple-slides-midterms-loom-2026-11-03/) | AI/semiconductor deleveraging persisted into the latest completed cash session；局限：not 20:00 BJT live; SOXX/SMH returns -3.77%/-2.77% are prior-session moves |
| F05 | US index futures / Apple / Palantir：Dow -0.42%, S&P +0.02%, Nasdaq100 +0.46%; AAPL -4.5%, PLTR -6.3% premarket（premarket snapshot） | 观测 2026-11-03 18:06 BJT；known_at 2026-11-03 18:50 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.reuters.com/business/retail-consumer/us-stock-futures-mixed-apple-slides-midterms-loom-2026-11-03/) | index bounce coexists with company-level rejection of capex/margin narratives；局限：premarket snapshot; can gap at 22:30 cash open |
| F06 | WTI / Brent：97.88 / 106.58 USD/bbl（intraday media snapshot） | 观测 2026-11-03 European morning；known_at 2026-11-03；读取 2026-11-03T20:00:00+08:00 | [直达](https://apnews.com/article/stock-markets-ai-earnings-oil-0d235af127a92c68da0cc2c45c028cef) | oil rebounded ~1.5%-1.7% after US strikes, challenging a simple peace-premium short；局限：not exchange settlement; exact observation minute not supplied |
| F07 | Spot gold / COMEX gold proxy：3926.52 / 3936.3 USD/oz（spot / futures intraday） | 观测 2026-11-03 11:53 BJT；known_at 2026-11-03；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.brecorder.com/news/40447185/gold-eases-ahead-of-us-midterm-elections) | gold gave back part of prior +2% rebound before US election/JOLTS；局限：stale versus 20:00 cutoff; not executable quote |
| F08 | VIX / MOVE / US HY OAS：~21.22 / ~101.13 / 3.26%（latest completed or last-good） | 观测 VIX 2026-11-02 close; MOVE 2026-11-02; HY OAS lagged；known_at through 2026-11-03；读取 2026-11-03T20:00:00+08:00 | [直达](https://fred.stlouisfed.org/series/BAMLH0A0HYM2) | risk is higher but credit has not yet signaled full stress；局限：mixed observation dates; VIX close is secondary; no live term-structure snapshot |
| F09 | CSI 50/300/500/1000：2768.27 / 4008.87 / 6327.05 / 6221.23（2026-11-03 cash close） | 观测 2026-11-03 15:00 BJT；known_at 2026-11-03 15:32 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://stock.cngold.org/c/2026-11-03/c10856041.html) | large-cap defense versus sharp small-cap reversal; broad market 2108 up/3309 down；局限：secondary aggregation, not official index file |
| F10 | IH/IF/IC/IM 2612：2736.2 / 3978.8 / 6283.8 / 6173.8; OI 77186/189840/179377/297750（secondary 15:26 latest, not official settlement） | 观测 2026-11-03 15:26 BJT；known_at 2026-11-03；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.9qihuo.com/hangqing) | IH/IF +0.4% while IC/IM -0.7%/-0.9%; small-cap relative-long morning thesis failed；局限：secondary; volume/OI not independently official-crosschecked; close vs settlement semantics not verified |
| F11 | HO/IO/MO 2612：ATM IV 16.21/21.66/35.30%; RR25 -0.67/-1.97/-4.42 vol; PCR OI 0.633/0.635/0.583（engine EOD analytics） | 观测 2026-11-02 EOD；known_at 2026-11-03 05:31 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json) | small-cap downside skew remained steeper; term structures available across expiries；局限：one day stale for 11/3; dealer direction unknown; not a bid/ask execution source |
| F12 | China commodities full universe：77 products / 806 contracts last-good 2026-11-02; current exact-contract subset only（vendor EOD plus partial exact-contract public checks） | 观测 2026-11-02 full EOD; 2026-11-03 subset；known_at 2026-11-03 19:33 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-03_commodities_evening.json) | full-range screening while isolating failed 11/3 baseline；局限：11/3 full-market collection failed; no claim of full current coverage or official volume/OI verification |
| F13 | SC2612 / AG2612 / CU2612 / EC2612：698.2 / 11655 / 106090 / 2465（2026-11-03 exact-contract subset close/last） | 观测 2026-11-03 China EOD；known_at 2026-11-03 19:33 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-03_commodities_evening.json) | SC/AG failed-bounce research, CU long invalidation, EC weakness；局限：settlement missing for SC/EC; official exchange crosscheck unavailable |
| F14 | China-Stock-Engine：failed_backfill; last valid 2026-10-30; 5571 quote rows; candidate rows 0（repository pipeline state） | 观测 requested 2026-10-31 to 11-02；known_at 2026-11-03 08:34 BJT；读取 2026-11-03T20:00:00+08:00 | [直达](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/last_run_status.json) | no fresh engine-generated A-share signal may be claimed；局限：HTTP 401 device limit; price/financial/tradability readiness are separate and current execution is unavailable |
| F15 | US events：JOLTS 11/3 23:00; ISM Services 11/4 23:00; payrolls 11/6 21:30 BJT（official release schedule） | 观测 2026-11-03 cutoff；known_at 2026 calendar；读取 2026-11-03T20:00:00+08:00 | [直达](https://www.bls.gov/schedule/2026/11_sched_list.htm) | clear event windows for rates, gold and AI risk；局限：event outcomes unknown at cutoff |

### 覆盖说明

- 美国利率、外汇、科技、油、金、波动与信用均已扫描；MOVE/HY、实际利率存在不同程度滞后，未伪装为实时。
- 中国股指现金与二级期指报价已分析；官方11月3日结算/量/OI未独立取得，HO/IO/MO仅到11月2日。
- 中国商品后台覆盖既定63代码并动态扩至77品种/806合约；11月3日全市场基线失败，只把精确合约子集用于当日判断，其余沿用11月2日last-good仅作全范围研究，不当新催化。
- Stock引擎10月30日后失败；对11月3日巨潮最新公告、上交所紫金/中海油及金山办公披露做限域检索，新增决策级候选为0。未取得数据不等于市场无机会。

## 3. 相比今晨真正发生了什么变化

- **C1** 中国小盘修复反转：CSI1000 -1.71% vs CSI50 +0.21%，IM -0.9% vs IF +0.4% 处置：CN-RV-IM-LONG-IF-SHORT-SFISF-20261102原计划未触发/已失效；不反手追空，等11/4官方EOD与期权更新
- **C2** CU2612跌至106090，穿越上午107600计划止损与逻辑区间 处置：COM-M-CU2612-LME-TIGHTNESS-DIVERGENCE-LONG-20261102对新仓失效；无成交回执，不宣称实际亏损
- **C3** 油价从前一日约-7%转为WTI/Brent +1.5%/+1.7%地缘反弹 处置：SC空由76降至67，只保留Brent<=105.30与SC反抽失败双闸门
- **C4** AI盘前指数修复，但AAPL/PLTR分别-4.5%/-6.3%且NDX较高点确认回撤>10% 处置：从单边抄底转向现金流质量相对Capex Beta研究；AMD财报前不执行
- **C5** 商品引擎11/3全市场基线失败，只有精确合约子集可用 处置：保留77品种后台扫描与合法last-good，但所有商品执行结论降级；crosscheck的different=0不解释为一致

## 4. 全球统一机会Top5

评分依次为逻辑/赔率凸性/催化/价格期限波动/拥挤技术；研究分不是胜率。

| 排名 | idea_id与方向 | 三轴判断 | 分项=总分 | 支撑/反证/工具 |
|---:|---|---|---:|---|
| 1 | COM-E-AG2612-FAILED-BOUNCE-SHORT-20261103<br>AG2612失败反弹空；short；1-10D | 研究：有条件优势<br>证据：价格/曲线/海外三层；实体与期权执行缺<br>执行：等21:15后顺序触发 | 19/18/14/12/9=72 | 支撑：AG2612 11655、结算12013，失败反弹形态；2612/2701曲线-0.291%；海外银阈值可作为独立映射<br>反证：现货/实体时点不可比；商品期权无执行盘口；地缘升级可令贵金属跳空<br>工具：AG2612 futures；风险：不追11480以下；期货止损不封顶 |
| 2 | US-AI-CASHFLOW-LONG-CAPEXBETA-SHORT-20261103<br>AI现金流质量多/Capex Beta空主题；relative_long_cashflow_quality；2-20D | 研究：研究优势，尚非可执行组合<br>证据：财报现金流、预市场反应、行业ETF三类独立线索<br>执行：等待22:30现金盘及AMD财报；权重/借券/成本未知 | 21/15/17/9/8=70 | 支撑：SOXX/SMH连续承压；AAPL强结果后因内存成本/毛利指引盘前-4.5%；PLTR高于预期指引仍盘前-6.3%，市场要求现金回报<br>反证：NQ期货+0.46%，NVDA/AMD盘前反弹；主题篮子成分权重、beta与借券成本未核<br>工具：优先观测MSFT/GOOGL质量腿对PLTR/高估值Capex Beta；不称beta-neutral；风险：AMD财报后全链重估、空头挤压、相关性断裂 |
| 3 | COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103<br>SC2612反弹失败空v2；short；1-5D | 研究：有条件优势但海外反证增强<br>证据：价格与曲线压缩两层，上限69<br>执行：Brent与SC双闸门未满足 | 18/17/13/10/9=67 | 支撑：SC2612 698.2，日内仍远低于前结算；曲线压缩支持国内去风险<br>反证：Brent 106.58并受地缘事件反弹；绝对backwardation仍在；实体与期权层缺失<br>工具：SC2612 futures；风险：地缘跳空、涨跌停、保证金上调 |
| 4 | GLD-POLICY-CREDIT-STABILIZATION-20261103<br>黄金政策信用溢价稳定观察；watch_long；3-20D | 研究：叙事稳定但未形成交易优势<br>证据：价格/美元/利率部分；ETF流、CFTC最新、IV/报价不足<br>执行：等JOLTS/选举后实际利率与美元共振 | 18/14/14/10/10=66 | 支撑：前一日黄金约+2%，美元未显著走强；地缘与财政信用风险仍提供尾部需求<br>反证：11/3黄金回吐；10Y实际利率last-good仍2.63%；无3-6月真实权利金、IV/skew和ETF流<br>工具：MGC或3-6月call spread仅待询价；也可不交易；风险：美元/实际利率共振上行与IV回落 |
| 5 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028<br>EC2612趋势空；short；3-20D | 研究：弱研究优势<br>证据：仅价格层；实体运价反对<br>执行：无夜盘；最早11/4 09:15 | 16/14/12/10/7=59 | 支撑：EC2612 2465，日内约-2.95%<br>反证：SCFIS现货+4.84%反对；当前曲线、海外映射与期权均缺<br>工具：EC2612 futures；风险：运价跳升与低开破坏赔率 |

未入榜重大项：CU多、IM多/IF空、MA多均按原规则失效；IWM多/QQQ空旧回踩卡已经越过“不追”区且顺序未核，不重置ID。OI701仅观察，BU/EB曲线与价格冲突，LC/SI/PS等当前全市场数据不足。

## 5. 详细交易研究卡（2张）

### 1) COM-E-AG2612-FAILED-BOUNCE-SHORT-20261103

- 标的/方向/定价：SHFE AG2612，short；11/3 close/last11655，settlement12013；21:00前无今晚夜盘报价。
- 合约：15千克/手；tick 1元/千克=15元/手；实物交割；动态保证金/限幅须券商复核。
- 入场与顺序：21:00取得同步报价；15分钟收于11620下 AND COMEX银<=48.80；随后反抽11620-11680失败。顺序缺一不可；分批 30%/30%/40%；第二、三批仅在回抽失败后。
- 放弃/失效：<=11480不追；COMEX>=49.80取消；两地报价不可比则取消；逻辑失效 COMEX>=49.80或AG曲线转明显正且实体银价不弱。
- 计划止损/目标/时间：11920计划止损；非最大亏损保证；TP1 11250；TP2 10850；2026-11-17退出。
- 好/中/坏报价：good 11680，单手计划风险3600元，TP1/TP2约1.79R/3.46R；mid 11650，单手计划风险4050元，TP1/TP2约1.48R/2.96R；bad 11620，单手计划风险4500元，TP1/TP2约1.23R/2.57R。
- 成本与预算：R未计未知手续费/滑点；入场价区间与止损实际可达，但跳空可能越过止损；试仓损失<=0.50% NAV；确认后<=1.0%；贵金属/USD/实际利率共因子合并<=2.5%。
- 状态：实际持仓未提供/未知；上午AG仅反身性观察；19:30商品报告建立新失败反弹子idea，不回填成交。

### 2) COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103

- 标的/方向/定价：INE SC2612，short；11/3 close/last698.2；settlement未取得；Brent约106.58媒体快照。
- 合约：1000桶/手；tick 0.1元/桶=100元/手；参考涨跌停18%、保证金20%仅来自商品报告，须券商复核；实物交割。
- 入场与顺序：Brent<=105.30 AND SC 15分钟收于697下；随后反抽699-703失败。AND与先后顺序完整闭合后才可研究下单；分批 30%/30%/40%。
- 放弃/失效：>710或<685不追；Brent>108或曲线>1.0%取消；逻辑失效 Brent>108或SC 15分钟站上712，或曲线重新扩至>1.0%。
- 计划止损/目标/时间：712计划止损；非最大亏损保证；TP1 682；TP2 665；2026-11-10退出。
- 好/中/坏报价：good 703，单手计划风险9000元，TP1/TP2约2.33R/4.22R；mid 701，单手计划风险11000元，TP1/TP2约1.73R/3.27R；bad 699，单手计划风险13000元，TP1/TP2约1.31R/2.62R。
- 成本与预算：未取得实时报价/手续费/滑点；商品报告R未扣成本，实际净R更低；试仓<=0.35% NAV；确认<=0.75%；油/化工共因子<=2.5%。
- 状态：实际持仓未提供/未知；上午评分76→晚间67；海外油反弹与两层证据上限降级；原711止损改712仅适用于尚未成交的新v2计划。


压力测试：期货止损不限制最大亏损。一个/两个限幅跳空、保证金追加、夜盘流动性消失或外盘地缘跳空均可能显著超过计划风险；无NAV只保留手数公式，不给虚构仓位。

## 6. 黄金特别研究

判断：**“政策信用期权”叙事不变，但证据不足**。该词是宏观类比，不代表合约有限亏损。10Y实际利率last-good仍2.63%，DXY约101.816，黄金在前一日反弹后回吐；央行购金是结构支撑，但本期无新月度流量，ETF流、同周CFTC和3—6月IV/skew/bid-ask均缺。

- 3—6月Call Spread：只有在人工询价后净权利金不高于价差宽度35%才研究；当前不填strike/保费。
- MGC：JOLTS后实际利率不升且DXY不破102.2才研究；期货止损不封顶。
- 黄金多+长债Put Spread：缺权利金、Greeks与DV01，不执行。
- 反向空黄金：仅DXY>102.5且10Y实际>2.70%持续时研究。**当前最优表达是不交易。**

## 7. AI特别研究

本期新增事实是“强结果不再自动换来正股回报”：Apple营收1145亿美元、毛利率47.9%、EPS 2.10、经营现金流280亿美元，但因内存成本与假日季毛利指引盘前跌4.5%；PLTR上调/超预期仍跌6.3%。这说明市场从收入叙事转向资本强度、毛利与现金回报。[Apple原始披露](https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/)；[盘前反应](https://www.reuters.com/business/retail-consumer/us-stock-futures-mixed-apple-slides-midterms-loom-2026-11-03/)。

MSFT季度OCF 580亿、Capex 452亿、FCF 186亿美元；Alphabet OCF 423亿低于Capex 514亿，Meta季度FCF -21.2亿，Amazon TTM FCF -424亿。SOXX/SMH上一现金日跌3.77%/2.77%。偏好“现金流质量多/Capex Beta空”，但没有精确权重、beta、借券和成本，只能称主题、不能称beta-neutral；AMD在美股盘后发布Q3并于11月4日05:00 BJT开电话会，[官方日历](https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results)。现金盘首30分钟与AMD指引是下一项区分观测。

## 8. 中国50/300/500/1000与公司专项

现金EOD：50 +0.21%、300 -0.20%、500 -1.45%、1000 -1.71%；2108涨/3309跌，成交约1.7837万亿元。二级期指15:26为IH/IF/IC/IM 2736.2/3978.8/6283.8/6173.8，basis约-1.16%/-0.75%/-0.68%/-0.76%；按距12月18日45天粗年化约-9.39%/-6.08%/-5.55%/-6.18%。OI较11月2日引擎值的跨源变化约+6601/+5604/+1000/-5850，只作线索，不能称官方核验。

HO/IO/MO 2612在11月2日的ATM IV为16.21%/21.66%/35.30%，RR25为-0.67/-1.97/-4.42 vol，BF25为0.46/0.04/1.03 vol；MO downside skew更陡，但11月3日数据缺失、dealer净方向未知。IH↔HO、IF↔IO、IM↔MO可研究；IC没有一一对应指数期权，任何代理都保留beta、跟踪和basis余险。

公司通道：Stock引擎backfill因HTTP401失败，最后有效日10月30日；5571行价量不代表全市场基本面、radar 0行不等于无机会。限域检索发现的11月3日金山办公业绩说明会/回购进展、三一重工回购进展等没有新的经营量价或利润桥，故A股重点候选为0。缺当前证券状态、估值、共识、订单经济性与可交易成本，不从商品或公告标题机械推导股价。

## 9. 下一24小时/7天风险日历与21:00地图

| 北京时间 | 事件 | 风险处置 |
|---|---|---|
| 2026-11-03 21:00 | 中国商品夜盘（归属11/4交易日）（尚未发生） | 21:15核首个15分钟与AG/SC顺序；21:30核外盘/曲线；21:45仅在成交量与价差正常时允许第二批 |
| 2026-11-03 22:30 | 美国现金市场开盘（DST已结束，EST） | 核AAPL/PLTR/NVDA/AMD与SOXX/SMH；首30分钟不把盘前价当成交证据 |
| 2026-11-03 23:00 | 美国9月JOLTS（BLS确定日历） | 黄金/久期/AI同时缩小Gamma/Vega和方向风险；数据前不追价 |
| 2026-11-04 05:00 | AMD FY2026 Q3电话会（财报盘后、5pm ET电话会） | 拆分数据中心收入、毛利、FCF、Capex与订单；不以盘后单点替代完整指引 |
| 2026-11-04 09:00-09:30 | 中国商品日盘、A股/股指期货重开（下一合法现金/股指窗口） | EC最早09:15；IH/IF/IC/IM重新取官方价格/OI；不延续11/3小盘多 |
| 2026-11-04 23:00 | 美国10月ISM服务业（ISM官方日历） | 检验增长/通胀、收益率与美元；方向仓位不跨数据满仓 |
| 2026-11-04 23:30 | EIA周度石油报告（EIA标准周三10:30 ET） | SC/BU/化工主题缩仓；无可执行期权链时不卖波动 |
| 2026-11-06 21:30 | 美国10月非农（BLS确定日历） | 黄金、利率、AI和USD共因子合并预算；旧短线idea最迟按原时间退出 |
| 2026-11-07 04:30 | CFTC COT（官方周度背景） | 只作仓位拥挤验证，不倒推11/3盘中成交 |

21:00三情景：

1. 风险反弹：21:15 SC>703、AG>11920且Brent>108，取消两张空头卡。
2. 区间：SC 697—703、AG 11620—11680但无“破位→反抽失败”顺序，不交易；21:30核外盘/曲线，21:45核价差/流动性。
3. 风险延续：AG 15分钟<11620且COMEX<=48.80并反抽失败，先试AG；SC还必须Brent<=105.30。禁止跳空追价。

## 商品消费者协议与完整扫描摘要

Futures requested 11/3、full last-good 11/2，77品种/806合约；Market 11/2；Physical 20模块18 fresh；External 22模块17 fresh；Night当期未开始且前次采集失败；Options 64预期/19成功、430条、ATM-ready19、skew-ready12，full_chain/surface/positioning/execution均false；Contract Metadata可研究但非执行源；futures_crosscheck比较0、difference0，表示“未比”，不是“全一致”。

core_v1局部指标：AP701 ATM34.425%、RR25 -0.17vol、BF250.92vol；OI701 ATM15.54%、RR25 +1.50vol、BF250.48vol；MA样本是MA612、不是MA701。局部ready不等于完整曲面；OI/volume样本不冒充全链PCR、crowding或Dealer Gamma；不提供虚构权利金、bid/ask、滑点或可成交性。

分板块结论：黑色RB无edge；有色/贵金属AG条件空、CU旧多失效；能化SC双闸门、BU/EB曲线价冲突、MA旧计划取消；新能源LC/SI/PS当日全市场数据不足；农产品OI观察、AP弱但实体层不全；航运EC价格弱、SCFIS反对且无夜盘。未入榜不表示未扫描。

## 预发布校验与风险预算

- 五项评分均重新加总通过；basis=(期货-现货)/现货，粗年化再乘365/45。
- AG/SC好中坏R、触发先后和入场/失效可达性已重算；手续费滑点未知，净R必低于表值。
- 交易日、DST与合法窗口已核：20:00尚无当晚商品夜盘；股指/股票今晚无常规交易窗口。
- 未解缺口：实时bid/ask、权利金/Greeks、11月3日官方CFFEX结算量OI、商品完整基线/官方比对、Stock新鲜度、黄金ETF/CFTC/IV、券商保证金限幅费用。
- 预算：试仓NAV 0.25%—0.75%，确认0.75%—1.5%，同一高确信主题合计不超过2.5%—3%；保证金不是风险预算。实际账户敞口未知。

归档：六文件写入后回读决定archive_status；CI为push后独立验证，当前仅可记pending_or_unverified。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：AG2612失败反弹空；SC2612仅在Brent<=105.30且SC反抽失败时空；EC2612最早11月4日09:15。
C. 今天继续观察：AI现金流质量多/Capex Beta空主题、黄金政策信用溢价、OI701、11月4日更新后的IH/IF/IC/IM与HO/IO/MO；实际持仓均未提供/未知。
D. 今天必须回避或若此前已建仓则有条件退出：旧CU多、旧MA多、IM多/IF空新仓计划已失效；回避无bid/ask商品期权、把旧夜盘当今晚、追SC/AG跳空及把评分当胜率。
