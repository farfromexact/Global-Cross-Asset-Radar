# 全球跨资产机会雷达晚间版｜2026-11-10

- 生成时点：2026-11-10T20:09:58+08:00
- 版别：evening
- Prompt：radar_2026-10-12_stock_v1
- Commodity consumer：core_2026-10-17_v1
- Research quality：2026-10-21_v1
- 免责声明：仅为投资研究与备选策略，不代客下单；未知实际持仓，不推定任何历史建议已成交。

## 1. 一句话结论

全球风险处于CPI前的脆弱修复：油价与中国油化工共振下跌，小盘A股跑赢但期指仍贴水；最清晰背离是黄金守4100与高实际利率并存，今晚只做条件，不追价。

## 事实台账与截点

中国11月10日日盘已收，欧洲盘交易中，美国现金盘前；中国商品下一合法窗口为21:00，CPI为21:30，美股现金盘22:30。美国已结束夏令时。11月11日NYSE股票正常，但SIFMA建议美元固定收益市场全日休市，不能把所有美国资产当作同步开闭。

| fact_id | 标的/数值 | 币种/单位 | 报价属性与观测时点 | known_at / 实际读取 | 来源 | 支持与局限 |
|---|---|---|---|---|---|---|
| F-US-RATES-1109 | UST 2Y/5Y/10Y/30Y | 4.56/4.67/4.88/5.26 percent yield | official par yield close；2026-11-09 US EOD | 2026-11-09 / 2026-11-10T20:09:58+08:00 | [直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve) | 长端期限溢价压力仍高；2s30s=+70bp；限：非11月10日盘中；CPI前last-good |
| F-US-REAL-1109 | UST 10Y real / breakeven | 2.66 / 2.22 percent | official real par yield; breakeven=4.88-2.66；2026-11-09 US EOD | 2026-11-09 / 2026-11-10T20:09:58+08:00 | [直达](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve) | 高实际利率构成黄金与成长股反证；限：breakeven为算术代理，非通胀互换报价 |
| F-FX-1110 | DXY/EURUSD/USDJPY/USDCNH | 101.70/1.1240-42/158.01-02/约6.67 index or spot | Europe/Asia live indicative；2026-11-10 17:00 JST to 19:30 BJT | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.boj.or.jp/statistics/market/forex/fxdaily/fxlist/fx261110.pdf) | 美元在CPI前稳定，JPY仍弱；限：DXY/CNH为二手快照；四者不同分钟 |
| F-US-PREMARKET-1110 | Nasdaq100/S&P500/Dow futures | -0.35%/近持平/+0.3% percent vs prior settlement | premarket futures snapshot；2026-11-10 approx 05:30 ET | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.reuters.com/business/sp-500-dow-futures-climb-oil-slide-lifts-sentiment-2026-11-10/) | AI与价值风格分化；CPI前不追指数；限：现金盘未开；盘前可变 |
| F-OIL-1110 | Brent/WTI | Brent<90; WTI 84.74 at 09:30 GMT per barrel | live futures observations；2026-11-10 Europe morning | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.reuters.com/business/sp-500-dow-futures-climb-oil-slide-lifts-sentiment-2026-11-10/) | 油价冲击与中国油化工下跌同向；限：两个合约观测分钟不同；WTI来自报告内二手快照 |
| F-GOLD-1110 | XAUUSD spot | 4115.12 per troy ounce | spot live；2026-11-10T02:38:00Z | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://ca.marketscreener.com/news/gold-edges-lower-as-focus-shifts-us-inflation-data-ce785fd3d080fe24) | CPI前金价仍守4100但短线受鹰派言论压制；限：非20:00同秒报价；权利金/IV未核 |
| F-VOL-CREDIT | VIX/MOVE/HY OAS | 19.92/85.98/3.48 index/index/percentage points | last-good closes；2026-11-05 to 2026-11-09 | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://portfolio-terminal.com/markets/vix) | 波动回落但信用未给出强风险清除信号；限：不同日期，不可作同刻横截面 |
| F-CN-SPOT-1110 | SSE50/CSI300/CSI500/CSI1000 | 2784.21/4059.11/6645.89/6579.36 index points | cash EOD；2026-11-10 15:00 BJT | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.google.com/finance/quote/000852:SHA?hl=en) | 小盘显著跑赢大盘；限：来源为公开行情聚合，非引擎今日快照 |
| F-CN-FUT-1110 | IH/IF/IC/IM2612 | 2751.2/4024.6/6576.2/6516.6 index points | vendor EOD observation；2026-11-10 15:27:59 BJT vendor timestamp | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.9qihuo.com/hangqing?shichang=CFFEX) | 小盘期指相对强，但四者仍对现货贴水；限：非CFFEX今日官方文件独立核验 |
| F-CN-OPT-1109 | HO/IO/MO2612 | ATM IV 15.68/19.98/33.30; RR25 -1.77/-1.15/-4.08 vol annualized vol points | official EOD last-good；2026-11-09 EOD | 2026-11-10T07:18:06+08:00 / 2026-11-10T20:09:58+08:00 | [直达](https://github.com/farfromexact/China-Options-Engine/blob/790037a4b3efe5023df7b491f60918c67dd17874/data/radar_latest.json) | MO下行偏斜最陡；仅作昨日结构参照；限：不是11月10日报价；dealer方向未知；不可执行 |
| F-COM-EOD-1110 | SC2612/CU2612/AG2702 | 597.2/105460/12723 contract price units | public EOD vendor observation；2026-11-10 China EOD | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.9qihuo.com/hangqing) | 油化工去风险；铜曲线韧性；白银晨间触发失效；限：成交量/OI未获官方独立交叉核；SC不追跌 |
| F-COM-CORE-1110 | China-Commodities core futures | 5 exchanges 0 fresh normalized contracts; 15 critical errors collection status | engine status；requested 2026-11-10 | 2026-11-10T18:59:49+08:00 / 2026-11-10T20:09:58+08:00 | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/0fe8b5ab37f5db4f06aac266b6ef9ed1defe1ae8/data/last_run_status.json) | 今日全市场供应商核心期货不可作为执行基线；限：失败源于iFinD月度额度；不等于市场无数据/无机会 |
| F-COM-OPT-1110 | China commodity options core_v1 | 44/64 products; 1058/1058 planned quotes; 22 skew-ready; 0 ATM-ready; execution false coverage/status | sampled-strikes EOD；2026-11-10 EOD | 2026-11-10T19:00:15+08:00 / 2026-11-10T20:09:58+08:00 | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/0fe8b5ab37f5db4f06aac266b6ef9ed1defe1ae8/data/options/quality_latest.json) | 局部RR可研究，完整曲面/持仓/执行不可用；限：quote coverage仅计划样本；非全链；bid/ask=0 |
| F-STOCK-1109 | China A-share engine | 5579 universe; 5573 quotes; candidate_union=0 securities | engine EOD last-good；2026-11-09 EOD | 2026-11-10T08:36:41+08:00 / 2026-11-10T20:09:58+08:00 | [直达](https://github.com/farfromexact/China-Stock-Engine/blob/35894a846deeef63b0b7501aeb98a9b184b01923/data/latest/opportunity_radar_latest.json) | 没有合格A股Top5候选；仍完成全市场价量扫描；限：缺复权、行业、指数成份和tradability；今日11/10未入库 |
| F-CALENDAR-1110 | US CPI / CN night / US cash | 21:30/21:00/22:30 BJT time | calendar；2026-11-10 | 2026-11-10 / 2026-11-10T20:09:58+08:00 | [直达](https://www.bls.gov/schedule/news_release/cpi.htm) | 真实下一窗口与触发排序；限：夜盘品种交易时段仍以交易所合约规则为准 |

EOD可比性：A股/中国期货为11月10日收盘；美国利率、VIX/MOVE为最近完整11月9日；欧洲/美盘前是11月10日盘中。跨列只做状态判断，不直接计算同刻相关性。未知项留缺。

## 2. 全市场仪表盘

| 资产 | 最新 | 变化 | 研究信号 | 时点/属性 |
|---|---:|---:|---|---|
| UST 2Y/10Y/30Y | 4.56% / 4.88% / 5.26% | 10Y +2bp vs 11/6 | 2s30s +70bp、5s30s +59bp；长端供给/期限溢价压力未消 | 2026-11-09 US EOD；official last-good; CPI前非实时 |
| UST 10Y real / breakeven | 2.66% / 2.22% | +3bp real vs 11/6 | 高实际利率是黄金与成长股反证 | 2026-11-09 US EOD；official real yield; breakeven arithmetic proxy |
| DXY / EURUSD / USDJPY / USDCNH | 101.70 / 1.1240-42 / 158.01-02 / ~6.67 | mixed | CPI前美元稳定，日元弱；CNH未发出中国流动性冲击 | 2026-11-10 Asia-Europe；mixed timestamps; DXY/CNH secondary |
| QQQ / Nasdaq100 futures | QQQ last trade 679.35; NQ futures -0.35% | cash prior rally; premarket softer | 现金盘未开；CPI与AI公司事件优先于盘前动量 | 2026-11-10 19:44 BJT / Reuters premarket；QQQ feed benchmark incompatible; no return used |
| SOXX / SMH | 146.76 / 487.41 last trade snapshots | return benchmark not accepted | 保留SOXX多/SMH空相对价值研究；非beta-neutral | 2026-11-10 19:44 BJT；premarket/last-trade; execution unverified |
| WTI / Brent | 84.74 at 17:30 BJT / later below 90 | about -2.4% / -3.6% by separate snapshots | 油价冲击传导中国油化工；近月强结构反对追空 | 2026-11-10 Europe morning；non-synchronous live observations |
| Gold spot | USD 4,115.12/oz | -0.6% at 02:38 GMT; later >4100 | 政策信用叙事中期不变，短期被实际利率与鹰派Fed压制 | 2026-11-10 02:38 GMT；spot live snapshot; options IV/debit unavailable |
| VIX / MOVE / HY OAS | 19.92 / 85.98 / 3.48pp | VIX -22.3%; MOVE -7.3% | 波动回落但日期错位；不可宣称信用风险全面解除 | VIX/MOVE 11/9; HY OAS 11/5；last-good, not synchronized |
| SSE50 / CSI300 / CSI500 / CSI1000 | 2784.21 / 4059.11 / 6645.89 / 6579.36 | -0.18% / +0.07% / +0.91% / +1.22% | 小盘强于大盘；不是机构行为证明 | 2026-11-10 15:00 BJT；cash EOD public quotes |
| IH2612 / IH2703 | 2751.2 / 2713.8 | main -0.53% vs prior close | basis -33.01 (-1.19%, simple annualized -11.39%); Mar-Dec -37.4 | 2026-11-10 15:27:59 BJT；vendor EOD observation; vol 22,756, OI 61,472, ΔOI -1,542 |
| IF2612 / IF2703 | 4024.6 / 3964.4 | main +0.02% vs prior close | basis -34.51 (-0.85%, annualized -8.17%); Mar-Dec -60.2 | 2026-11-10 15:27:59 BJT；vendor EOD; vol 51,996, OI 173,620, ΔOI -155 |
| IC2612 / IC2703 | 6576.2 / 6442.2 | main +0.66% vs prior close | basis -69.69 (-1.05%, annualized -10.07%); Mar-Dec -134.0 | 2026-11-10 15:27:59 BJT；vendor EOD; vol 90,676, OI 169,210, ΔOI -3,813; no 1:1 index option |
| IM2612 / IM2703 | 6516.6 / 6373.2 | main +1.05% vs prior close | basis -62.76 (-0.95%, annualized -9.16%); Mar-Dec -143.4 | 2026-11-10 15:27:59 BJT；vendor EOD; vol 165,326, OI 280,266, ΔOI +430 |
| HO/IO/MO2612 options | ATM 15.68/19.98/33.30%; RR25 -1.77/-1.15/-4.08vol | ATM -1.03/-1.16/-2.34vol | MO downside skew deepest; IC has no direct index option | 2026-11-09 EOD；independent options engine last-good; not 11/10 executable; dealer direction unknown |
| China commodities representatives | SC597.2, CU105460, AG12723, FU3985, MA3064, EB8654, AP5901, EC2406 | vs prior settle -6.34%, +0.10%, +0.90%, -6.70%, -5.64%, -4.64%, +0.24%, +3.82% | 油化工系统性去风险；铜曲线韧性；银需CPI后重夺 | 2026-11-10 China EOD；public per-contract checks; core full-market collection failed |
| Commodity options / Night / crosscheck | 44/64 products; 22 skew-ready; ATM/surface/positioning/execution=0; historical night detail empty | — | 局部skew可研究，不推全曲面/PCR/dealer gamma；20:00当晚夜盘未开 | options 2026-11-10; historical night trading_date 2026-11-10；quote_coverage_complete only planned sample; crosscheck baseline unavailable; DCE HTTP412; no calendar mismatch |
| China-Stock-Engine | universe 5,579; quotes 5,573; candidate_union 0 | 11/9 breadth 2242 up / 3148 down; EW +0.11%, median -0.31% | 研究覆盖完成但执行不就绪；11/10限定公司检索新增有效线索0 | engine trade_date 2026-11-09；adjustment/industry/index/tradability missing; company bundle narrow |

### 商品全覆盖与模块边界

- 全范围：以引擎11月9日last-good覆盖77个品种/806合约，含用户列示63个去重代码及新增挂牌品种；11月10日公开精确复核9个关键合约。黑色、有色、能化、新能源、农产品、航运均完成扫描；最终榜单不等于后台范围。
- Futures：11月10日五所核心采集为0、15个critical errors，原因是供应商月度额度；不能把workflow成功等同published/ready。逐合约公开EOD仍可研究，但成交/OI未称官方独立核验。
- Market/Physical/External：Market与多数实体数据停在11月9日，Physical basis多为C级、18个有值但不进入关键候选计分；External由仓库last-good加当前公开油/铜/银补证。
- Night：历史快照trading_date=2026-11-10、session_start=11月9日，日历无错配，但418合约中214 query errors且detail为空；20:00当晚21:00尚未开始，旧夜盘不算今晚行情。
- Options：trade_date=11月10日，core_v1/sampled_strikes，44/64产品、1058/1058计划样本返回、22个skew-ready；core_atm=0、surface/positioning/execution=0。quote_coverage_complete只指计划样本，不是全链；不编ATM/BF/term/PCR/dealer Gamma/权利金/bid-ask。
- Crosscheck：官方合约列表可见，但当前vendor baseline缺；DCE HTTP412，其余baseline unavailable，可信具体价差异=0。这不是“所有价相同”，也不牵连已逐项核验的公开合约。

板块结论：油化工系统性下跌但近月强结构与极端波动反对追空；CU价差韧性而外铜偏弱；AG晨间条件失效，CPI后重夺才重建；P/AP反弹层数不足；EC无夜盘，等次日日盘；黑色与新能源没有达到三层证据的候选。

## 3. 相较严格前序的实质变化

1. 相较今晨，最实质变化是中国能源化工系统性去风险：SC2612较前结算-6.34%、FU2701-6.70%、MA701-5.64%、EB2612-4.64%，欧洲时段Brent进一步跌破90美元；方向偏空但已大幅入价。
2. 中国风格从昨日偏弱转为小盘领跑：CSI1000 +1.22%、CSI500 +0.91%，SSE50 -0.18%；IM2612较昨收+1.05%且ΔOI+430，但期现仍贴水0.95%，不能直接叫趋势反转。
3. AG2702盘中低12609，破坏晨报要求低点不低于12680的条件；旧日盘计划失效，不推断成交。CPI后需重新夺回12820并回踩确认。
4. 美国利率last-good较前日更紧：10Y名义4.88%、10Y实际2.66%；Waller讲话强化加息风险，黄金政策信用叙事的短线证据减弱，但央行购金与月度ETF需求使中期叙事未失效。
5. 数据能力发生实质变化：商品今日核心期货全市场采集因供应商月度额度失败，不能用workflow成功替代数据就绪；当日期权44/64产品局部skew可用，但ATM、完整曲面、持仓与执行均未就绪。

前序身份：最近全球报告为reports/2026/11/2026-11-10_morning.json；最近同edition为reports/2026/11/2026-11-09_evening.json；11月10日商品晚报只作辅助，不替代全球前序。

## 4. 全球统一机会Top 5以内

| 排名 | 机会 | 方向 | 期限 | 三轴：研究/证据/执行 | 逻辑/赔率/催化/价格波动/拥挤=总分 | 已定价 | 最强反证 |
|---:|---|---|---|---|---|---|---|
| 1 | AI现金流定价权相对Capex Beta | 条件性多SOXX/空SMH等名义；非beta-neutral | 3-10交易日 | 中等偏强：Broadcom现金流与AI收入提供基本面锚，而NVDA权重/个体事件使SMH更集中 / 中等：IR与盘前分化有效；组合beta、借券与当日现金盘尚缺 / not_ready | 22/17/15/7/8=69 | 周一反弹已吸收部分超跌，纳指100盘前转弱 | NVDA事件可能快速反转；CoreWeave强指引可抬升高Capex链 |
| 2 | 黄金政策信用对冲（CPI后确认） | 条件性多；不在CPI前追价 | 1-12周 | 中等：央行购金与ETF月度需求对冲高实际利率 / 中等：价格、央行、CFTC有效；今日ETF流和期权IV缺失 / not_ready | 21/17/15/8/7=68 | 金价守4100已计入部分避险与油价回落 | 10Y实际2.66%且Fed更鹰，CPI热可同时推升美元与真实利率 |
| 3 | SC2612去风险后的失败反弹空 | 条件性做空 | 1-3交易日 | 中等：内外油价与宏观两层同向 / 2层；按商品上限低于70 / not_ready until live depth and post-CPI sequence | 18/16/16/9/8=67 | SC已较前结算跌6.34%，大部分冲击已入价 | 旧近月升水、潜在供给中断与低开跳空使追空赔率恶化 |
| 4 | CU2612-CU2701近月曲线韧性 | 条件性做多价差 | 1-3交易日 | 中等：收盘价差1200较前结口径1150扩大 / 2层；实体与完整期权层缺失 / not_ready | 19/15/13/12/7=66 | 近月韧性已部分反映在1200价差 | 海外铜约-0.6%、CPI热与美元走强可打破价差 |

Top5只有4项，不凑配额。得分是研究优先级，不是胜率。商品SC/CU仅两层证据，严格低于70；黄金/AI不机械套用商品层数规则。

## 5. 详细交易研究卡（2张）

### 1. SC2612｜COM-E-SC2612-DEESCALATION-FAILED-REBOUND-SHORT-20261109 r3

- 定价与窗口：2026-11-10 EOD close 597.2; prior settlement 637.6。2026-11-10 21:00夜盘；最早21:45 BJT，归属2026-11-11交易日。实际持仓=not_provided_unknown。
- 合约：1000 barrels/point；tick 0.1 CNY；保证金 20% public reference, broker may differ；限幅 18%; recheck exchange/broker before order；physical futures; user must satisfy eligibility。
- 触发：AND: 21:00后首次反弹进入599-603；AND 等待CPI后至至少21:45；AND Brent<90.50；AND SC 15分钟收盘<600；AND 随后首次回测600失败；AND 精确盘口深度正常。顺序不可交换。
- 入场：603/601/599分30%/30%/40%；若直接跌破597或未反弹，不追；若首段已触612则计划作废
- 风控：计划止损612；期货最大亏损不封顶，跳空可越过。逻辑失效：SC 15分钟收>=612 OR Brent>93.50 OR 可信供给中断。
- 目标/时间：TP1 580；TP2 565；到2026-11-13日盘收盘时间退出
- 成本后情景：入场599，风险14500元，TP1 1.21R，TP2 2.24R；入场601，风险12500元，TP1 1.56R，TP2 2.76R；入场603，风险10500元，TP1 2.05R，TP2 3.48R。
- 成本与规模：每手往返手续费+滑点情景1500 CNY；非实报，未知不按0。试仓手数=floor(0.25%×NAV/14500)；若<1手则不做。确认后单idea总风险不超过1.0% NAV，油/化工主题合并不超过2.5%
- 共振压力：1个18%限幅与保证金追加远超计划止损；两限幅、流动性消失、Brent反向跳涨须按可用现金与极端损失测算
- 相较前序：较晨报从泛SC短升级为日盘大跌后的失败反弹；分数69→67，原因是价格已大幅入价及仅两层证据
- 发布闸门：机器表示不能无损承载全部AND顺序与两腿同步条件，故not execution-ready；以本段为准。

### 2. long CU2612 / short CU2701 1:1 lots｜COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106 r9

- 定价与窗口：2026-11-10 EOD spread 1200; previous-settlement spread 1150。2026-11-10 21:00夜盘；CPI后最早21:45 BJT。实际持仓=not_provided_unknown。
- 合约：5 tonnes/point each leg；tick 10 CNY/tonne；保证金 11% public reference per leg, spread margin broker-specific；限幅 9%; recheck；physical futures; two-leg execution/legging risk。
- 触发：AND: 价差先回测950-1000且不低于800；AND 随后15分钟收>=1050；AND 下一5分钟回踩1020-1050守住；AND LME铜>=13750；AND 两腿盘口可同刻执行。
- 入场：价差1020/1035/1050分30%/30%/40%；直接上冲>1200不追；任一腿无法同步报价则放弃
- 风控：价差800计划止损；非最大亏损保证。逻辑失效：价差<800 OR LME铜<13750且曲线同步转弱。
- 目标/时间：TP1 1500；TP2 1750；2026-11-13收盘时间退出
- 成本后情景：入场1020，风险1600元，TP1 1.19R，TP2 1.97R；入场1035，风险1675元，TP1 1.09R，TP2 1.84R；入场1050，风险1750元，TP1 1R，TP2 1.71R。
- 成本与规模：两腿往返手续费+滑点情景500 CNY/组；非实报。试仓组数=floor(0.25%×NAV/1750)，但还须受两腿保证金与1个限幅名义压力约94,374 CNY/组约束；铜/金/中国资源股共因子合并上限2.5%
- 共振压力：单边跳空、两腿相关性断裂、跨境铜与CNY同时冲击；一限幅约94,374 CNY/组，两限幅约188,748 CNY/组的名义压力代理
- 相较前序：评分71→66；价差扩大支持逻辑，但海外铜走弱、核心期货采集失败且实体/期权层未补强
- 发布闸门：机器表示不能无损承载全部AND顺序与两腿同步条件，故not execution-ready；以本段为准。


## 6. 黄金特别研究

- 判断：政策信用期权叙事“中期不变、短期减弱”。9月央行净购金61吨、10月ETF月度数据与11月3日CFTC last-good支撑；但10Y实际利率2.66%、Waller更鹰、现货金CPI前回落是强反证。
- 市场已定价：守住4100已吸收部分避险与油价回落；我们分歧不在“永远涨”，而在结构性官方需求能否抵消高真实利率。
- 3—6个月Call Spread：只在取得同到期准确strike、bid/ask、IV和净debit后比较；不复用旧strike。最大损失只有在实际成交结构和权利金确认后才可称有限。
- MGC：方向纯、流动性通常更好，但止损不封顶；CPI后金价、DXY与利率代理共同确认才考虑。
- 黄金多+长债Put Spread：是两套腿，不能称组合最大损失已封顶；11月11日债券现金市场休市导致错时与basis风险。
- 反向/不交易：若CPI后美元和真实利率代理同升、黄金失守4100及周五锚点，可研究反向；当前基准仍是不交易。
- 下一项区分观测：21:30后30分钟DXY、名义收益率/TIPS代理、黄金与GVZ是否形成一致方向；今日ETF流与期权skew仍缺。

## 7. AI特别研究

- 盈利/FCF定价权：Broadcom Q3收入295.91亿美元、经营现金流141.97亿、FCF136.65亿、AI半导体收入167亿；这是已实现现金流，不等于所有AI Capex都兑现。
- Capex Beta：CoreWeave今晚美东17:00电话会，关键不是收入headline，而是容量交付、积压质量、融资成本、毛利、Capex与FCF转换。NVDA于11月17日盘后发布Q3 FY2027。
- 当下市场：纳指100期货约-0.35%，NVDA盘前约+0.3%，INTC/MRVL约-2%；个体事件与估值竞争使权重ETF分化。
- 表达比较：等名义多SOXX/空SMH只是在降低共同半导体beta，不是beta-neutral。用19:44快照，股数比约3.321:1；缺真实权重、beta、borrow、费用与现金盘价，故不执行。单买SOXX承担行业beta；单空SMH承担NVDA反转；不交易保留事件选择权。
- 最强竞争解释：NVDA个体争议快速消退、CoreWeave指引强，SMH可能反而胜出。下一观测是CPI后30—45分钟SOXX/SMH比值、上涨家数、NVDA相对收益和VIX。

## 8. 中国50/300/500/1000与公司专项

### 指数、期货、风格

| 产品 | 现货EOD | 主力/次季 | 主力日变动 vs昨收 | 成交量 / OI / ΔOI | basis及曲线 |
|---|---:|---:|---:|---:|---|
| IH | 2784.21 (-0.18%) | 2751.2 / 2713.8 | -0.53% | 22,756 / 61,472 / -1,542 | -33.01点，-1.19%，简年化-11.39%；Mar-Dec -37.4 |
| IF | 4059.11 (+0.07%) | 4024.6 / 3964.4 | +0.02% | 51,996 / 173,620 / -155 | -34.51点，-0.85%，简年化-8.17%；Mar-Dec -60.2 |
| IC | 6645.89 (+0.91%) | 6576.2 / 6442.2 | +0.66% | 90,676 / 169,210 / -3,813 | -69.69点，-1.05%，简年化-10.07%；Mar-Dec -134.0 |
| IM | 6579.36 (+1.22%) | 6516.6 / 6373.2 | +1.05% | 165,326 / 280,266 / +430 | -62.76点，-0.95%，简年化-9.16%；Mar-Dec -143.4 |

basis=主力收盘−现货收盘；年化用38个日历日简单年化，未做股息/融资carry调整。小盘强而贴水仍深，说明“价格相对强”与“远期风险折价”并存；没有beta估计，IF-IH、IM-IF、IM-IH、IC-IF、IM-IC均不能称beta-neutral。

### 股指/ETF期权

HO/IO/MO只能用11月9日独立引擎last-good：Dec ATM 15.68/19.98/33.30%，RR25 -1.77/-1.15/-4.08vol，BF25 0.34/0.47/1.40vol，PCR(OI) 0.643/0.630/0.606，gamma峰2800/4000/7000。上述不是11月10日可执行报价；全链OI不能推出dealer净头寸。IC无一一对应指数期权；MO/IO或ETF期权只能作代理，承担beta、跟踪误差和basis余险。

### China-Stock-Engine与主动发现

- 私库统一ref=35894a846deeef63b0b7501aeb98a9b184b01923，trade_date=11月9日；全市场5579、报价5573。1/3/5/20日原始价量可用，但复权覆盖0、行业/指数成份/tradability为missing，所有技术候选被严格门槛排除，candidate_union=0。
- 公司事实目录34个事件、最低完整财务包2家、forecast revisions=0；这不是全市场基本面覆盖。
- 11月10日限定检索：上交所紫金矿业601899、中国海油600938、宝钢股份600019，以及巨潮最新披露页。新增可改变本期利润桥的经营事实=0。
- 紫金利润桥：金属实现价×矿产销量−单位成本±库存/套保/汇率−Capex及少数股东；CU近远月价差不是公司利润的直接代理。中国海油：实现油价×销量−成本/税费±套保/汇率；油跌未必按一比一压净利。
- 结论：A股重点候选0；不是“全市场无机会”，而是今日价量未入库、财务目录窄、执行参数未核。直接商品表达更纯，但也只能挂条件。

## 9. 下一24小时/7天风险日历

| 北京时间 | 事件 | 风险与动作 |
|---|---|---|
| 2026-11-10 21:00 | 中国商品夜盘开始，归属2026-11-11交易日 | 油化工跳空、金属CPI前抢跑；21:15核开盘缺口/报价连续性；21:30冻结；21:45重核触发 |
| 2026-11-10 21:30 | 美国10月CPI与实际收入 | DXY、利率、黄金、AI、油与CNH共振；热：美元/利率上、金属下；中性：回到油/曲线；冷：金银反弹、SC空头挤压 |
| 2026-11-10 22:30 | 美国现金股市开盘 | AI相对价值与指数波动；23:00-23:15核SOXX/SMH、NVDA、市场宽度和VIX；不把盘前当成交 |
| 2026-11-11 01:00 | EIA STEO与USDA WASDE常规窗口 | 油与农产品Vega/跳空；以实际官方发布时间为known_at；未发布不补写 |
| 2026-11-11 02:00 | 美国10Y国债拍卖预期窗口 | 尾部、投标倍数、间接比例与期限溢价；金额/结果须官方落地；不预判 |
| 2026-11-11 06:00 | CoreWeave Q3电话会 | AI需求、产能、债务与现金转换；订单/积压、Capex、融资成本、毛利、FCF逐项拆分 |
| 2026-11-11 | Veterans Day | NYSE股票正常；美元固定收益市场SIFMA建议全日休市；CME按品种假日安排；跨市场相关性和流动性不可按正常日外推 |
| 2026-11-13 01:00 | EIA WPSR假期延后窗口 | 原油库存、炼厂、出口；SC/Brent计划到期前重估 |
| 2026-11-13 | IEA 11月油市报告；美国10月PPI 21:30 BJT | 油供需与通胀再定价；油价与真实供需方向是否一致 |
| 2026-11-17 approx 05:20-06:00 | NVIDIA Q3 FY2027结果与电话会 | AI现金流定价权与行业权重；收入、毛利、现金流、供应/中国风险；不只看headline |

### 今晚21:00夜盘三情景

1. CPI偏热：DXY与利率上、金银铜承压；SC若Brent仍弱也不追空，等反弹失败。AG/CU多头条件大概率失效。
2. CPI大致符合：宏观冲击衰减，回到油价、SC反弹和CU曲线；只执行写明的AND顺序。
3. CPI偏冷：金银铜可能急升、美元回落；AG需15分钟重夺12820并5分钟回踩12780—12820，SC空头警惕挤压。

验证钟：21:15看开盘缺口与盘口连续性；21:30事件时不新增方向；21:45看第一根事件后15分钟收盘、外盘与回踩；任一报价/深度未知则继续观察。股指期货和A股今晚无常规21:00交易窗口，下一合法窗口为11月11日09:30。

## 风险预算与发布校验

试仓0.25%—0.75% NAV，确认0.75%—1.5%，同主题不超过2.5%—3%。SC专属上限1.0% NAV且油/化工合并≤2.5%；无NAV只给公式，不把保证金当风险预算。实际持仓未提供。

校验：关键事实已打开原文或直达数据页；时间、DST、合法窗口已核；basis、曲线、分项加总和成本后R已重算；SC/CU证据层上限已执行；MD/JSON由同一对象生成。未解：商品当前官方vendor baseline、当日CFFEX官方文件、期权真实bid/ask/debit、AI beta/borrow、今日A股复权与tradability。CI仅标pending_or_unverified。

## 来源

1. [Daily Treasury Par Yield Curve Rates, November 2026](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve)｜2026-11-09｜支持：11月9日2Y/5Y/10Y/30Y为4.56%/4.67%/4.88%/5.26%
2. [Daily Treasury Par Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)｜2026-11-09｜支持：11月9日10Y实际利率2.66%
3. [Schedule of Releases for CPI](https://www.bls.gov/schedule/news_release/cpi.htm)｜2026-11-10｜支持：10月CPI定于11月10日08:30 ET发布
4. [Federal Reserve calendar](https://www.federalreserve.gov/newsevents/calendar.htm)｜2026-11-10｜支持：Waller与Bowman讲话日程；11月11日统计发布假日安排
5. [Foreign Exchange Rates, November 10, 2026](https://www.boj.or.jp/statistics/market/forex/fxdaily/fxlist/fx261110.pdf)｜2026-11-10｜支持：17:00 JST USD/JPY 158.01-02、EUR/USD 1.1240-42
6. [Dollar steadies as Waller argues for more rate hikes](https://www.reuters.com/world/asia-pacific/dollar-sellers-hit-pause-us-inflation-data-2026-11-10/)｜2026-11-10｜支持：市场完全计入12月加息；Waller称若通胀恶化可考虑更大加息
7. [Nasdaq futures slip with Nvidia woes](https://www.reuters.com/business/sp-500-dow-futures-climb-oil-slide-lifts-sentiment-2026-11-10/)｜2026-11-10｜支持：纳指100期货约-0.35%、道指期货约+0.3%、Brent跌破90美元、CoreWeave盘后财报
8. [Gold drops on hawkish Fed comments ahead of CPI](https://www.reuters.com/world/india/gold-edges-lower-focus-shifts-us-inflation-data-2026-11-10/)｜2026-11-10｜支持：金价在CPI前受鹰派Fed言论压制
9. [Gold prices slip ahead of U.S. CPI](https://ca.marketscreener.com/news/gold-edges-lower-as-focus-shifts-us-inflation-data-ce785fd3d080fe24)｜2026-11-10｜支持：02:38 GMT现货金4115.12美元/盎司、较前时段跌0.6%
10. [Commitments of Traders, COMEX futures](https://www.cftc.gov/dea/futures/deacmxsf.htm)｜2026-11-03｜支持：COMEX黄金持仓报告截至11月3日
11. [Central Bank Gold Statistics: September 2026](https://www.gold.org/goldhub/gold-focus/2026/11/central-bank-gold-statistics-september-2026)｜2026-11-04｜支持：9月央行净购金61吨，为2026年以来最高月度
12. [Gold ETF flows: October 2026](https://www.gold.org/goldhub/data/global-gold-backed-etf-holdings-and-flows)｜2026-11-05｜支持：10月全球黄金ETF月度流向已有更新；不是今日盘中流
13. [CFFEX futures quotes](https://www.9qihuo.com/hangqing?shichang=CFFEX)｜2026-11-10｜支持：IH/IF/IC/IM 2612与2703在15:27:59的供应商EOD观察价、成交量与持仓
14. [CSI 1000 Index](https://www.google.com/finance/quote/000852:SHA?hl=en)｜2026-11-10｜支持：中证1000收6579.36、涨1.22%
15. [Global commodities main-contract quotes](https://www.9qihuo.com/hangqing)｜2026-11-10｜支持：中国商品公开EOD逐项核验，包括SC/CU/AG/FU/MA/EB/AP/EC
16. [Short-Term Energy Outlook release schedule](https://www.eia.gov/outlooks/steo/release_schedule.php)｜2026-11-10｜支持：11月STEO计划11月10日发布
17. [Oil Market Report – November 2026](https://www.iea.org/events/oil-market-report-november-2026)｜2026-11-13｜支持：11月OMR于11月13日发布
18. [NVIDIA Q3 FY2027 conference call](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx)｜2026-10-28｜支持：NVDA将于11月17日美东收盘后发布Q3 FY2027结果
19. [CoreWeave Q3 2026 results call](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Date-of-Third-Quarter-2026-Financial-Results-and-Conference-Call/)｜2026-10-27｜支持：CoreWeave电话会11月10日17:00 ET
20. [Broadcom Q3 FY2026 results](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial)｜2026-09-02｜支持：Q3收入295.91亿美元、FCF136.65亿美元、AI半导体收入167亿美元
21. [NYSE holidays and trading hours](https://www.nyse.com/trade/hours-calendars)｜2026｜支持：Veterans Day不在NYSE 2026休市清单
22. [Veterans Day fixed-income close recommendation](https://www.sifma.org/news/press-releases/sifma-fixed-income-market-close-recommendation-in-the-u-s-the-u-k-and-japan-for-the-u-s-veterans-day-holiday-2026)｜2026-10-28｜支持：11月11日美元固定收益市场建议全日休市
23. [Zijin Mining SSE company page](https://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=601899)｜2026-11-10｜支持：限定检索未见11月10日新增紫金经营公告
24. [CNOOC SSE company page](https://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=600938)｜2026-11-10｜支持：限定检索未见11月10日新增中国海油经营公告

A. 今天没有应立即建立的新仓位。
B. 仅挂条件：SC2612失败反弹空（CPI后且五项AND）；CU2612-CU2701价差多（深回踩后重夺且LME确认）；AI相对价值与黄金只进入询价/观察，不下无报价订单。
C. 继续观察：黄金政策信用对冲、SOXX/SMH相对收益、AG2702 CPI后重夺、EC2612次日日盘、IH/IF/IC/IM贴水与MO下行偏斜、紫金矿业/中国海油经营传导。
D. 必须回避或若此前已建仓则有条件退出：追空已跌6%以上油化工；CPI前新增无保护Delta/Vega；把11月9日期权或历史夜盘当今晚可执行报价；缺盘口时卖波动；任何触及原失效条件的旧计划。
