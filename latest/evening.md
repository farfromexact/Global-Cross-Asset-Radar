# 全球跨资产机会雷达晚间版｜2026-11-11

- 生成/事实截点：2026-11-11T20:04:40+08:00 / 2026-11-11T20:04:00+08:00
- 版别：evening；Prompt：radar_2026-10-12_stock_v1；Commodity consumer：core_2026-10-17_v1；Research quality：2026-10-21_v1
- 仓库ref：Global `108d026a0187c4f81eaed78e61d5a36bb0883bda`；Options `a0e62a62c78b3fc3432303153408bfe4e818d69a`；Commodities `61c89422880c91041c2c368c44036e0a989da28c`；Stock `8e61b672d10566406a25bb437a2f46f01d36e2c8`
- 严格前序：`reports/2026/11/2026-11-11_morning.json`；同版前序：`reports/2026/11/2026-11-10_evening.json`
- 免责声明：仅为投资研究与备选策略，不代客下单；未获成交回执，所有实际持仓均为“未提供/未知”。

## 1. 100字内结论

热CPI后的美元与实际利率压力未消退，但AI盘前和中国小盘反弹；最大背离是风险资产回暖而利率波动仍高，今晚只做条件单。

## 2. 全市场仪表盘、事实台账与覆盖

### 2.1 全市场仪表盘

| 资产/指标 | 最新值 | 变化 | 时点 | 口径、信号与局限 |
|---|---:|---:|---|---|
| US Treasury 2/5/10/30Y; 10Y real; 2s30s | 4.73/4.81/4.98/5.35%; 2.78%; +62bp | 11/10 EOD; 2s30s -8bp d/d | 2026-11-10 EOD | official close; 11/11 cash market closed；hot CPI bear-flattening; no holiday execution |
| DXY; EUR/USD; USD/JPY; USD/CNH | 102.49; 1.1137; 158.96; 6.6728 | DXY about +0.27% intraday; CNH -0.06% d/d | 11/11 Europe/US premarket | realtime/vendor snapshots, not synchronized close；USD firm; CNH not disorderly |
| Nasdaq Composite / QQQ | 25,065.87 / 674.76 | -0.74% / -0.65% on 11/10; NQ futures about +1.6% | 11/10 close; 11/11 premarket | close plus futures；AI rebound unconfirmed before cash open |
| SOXX / SMH | 146.59 / 483.63; ratio 0.30310 | -0.21% / -0.76% on 11/10 | 2026-11-10 close | ETF close；trigger 0.3040 not met on last close |
| WTI Dec / Brent Jan | 86.80 / 92.77 USD/bbl | about +0.9% / +1.4% | 2026-11-11 09:34 GMT | Reuters realtime；shipping risk versus reported API build |
| Spot gold / GLD | about 4,054 USD/oz / 369.36 | spot about +0.4%; GLD -2.67% on 11/10 | 11/11 spot; 11/10 GLD close | mixed realtime/close；technical stabilization, macro headwind |
| VIX / MOVE / US HY OAS | 19.46 / 92.43 / 331bp | VIX -2.31%; MOVE +6.45; HY -3bp | latest completed 2026-11-10 | last-good completed day；equity calm versus rates vol |
| SSE50 / IH2612 (IH2611) | 2765.54 / 2742.2 (2761.8) | cash -0.27%; OI63,192 Δ+1,720; vol25,950 | 2026-11-11 EOD | cash recap + public futures；basis -23.34 (-0.84%), ann -8.33% |
| CSI300 / IF2612 (IF2611) | 4075.71 / 4043.4 (4067.2) | cash +0.41%; OI173,783 Δ+163; vol56,405 | 2026-11-11 EOD | cash recap + public futures；basis -32.31 (-0.79%), ann -7.82% |
| CSI500 / IC2612 (IC2611) | 6627.91 / 6664.0 (6701.8) | cash -0.27%; OI173,915 Δ+4,705; vol102,586 | 2026-11-11 EOD | nonofficial cash + public futures；basis +36.09 (+0.54%), ann +5.37% |
| CSI1000 / IM2612 (IM2611) | 6669.55 / 6623.0 (6662.0) | cash +1.37%; OI290,211 Δ+9,945; vol196,766 | 2026-11-11 EOD | public cash/futures；basis -46.55 (-0.70%), ann -6.89% |
| HO/IO/MO 2612 options | ATM 14.90/18.10/29.51%; RR25 -1.27/-0.92/-3.05pp | 11/10 ATM -0.77/-1.88/-3.79pp d/d | 2026-11-10 official EOD | one session stale; history empty；MO protection richest, not executable tonight |
| M1-5 / CU1-2 / SC2612 | 300 / 1220 / 604 (alternate606) | M +15 vs prior close; CU expensive; SC conflict | 2026-11-11 EOD | public exact contracts；M pullback; CU no chase; SC reclaim610 |
| China-Stock-Engine | 5579 universe; 5573 quotes; trade date11/9 | 11/11 backfill failed | known_at 11/11 08:32 BJT | stale; public sector scan supplemental；no executable A-share candidate |
| Commodity capability | 63 target; 77 last-good; current core0; options45/64 | night417/806 51.737%, detail empty | 19:03-19:32 BJT | partial/public EOD；ATM0, skew22; surface/position/execution0 |

EOD可比性：美国利率、ETF收盘为11/10，中国为11/11 EOD，海外实时为11/11欧洲盘/美股盘前，**不可作同一时点价差**。美股现金22:30 BJT开盘；美债11/11休市。今晚21:00只有相关商品夜盘，股指与股票下一合法窗口为11/12 09:30 BJT。

### 2.2 关键事实台账

| fact_id | 标的/单位/口径 | 观测、发布时间/known_at | 实际读取 | 直达来源 | 支持判断与局限 |
|---|---|---|---|---|---|
| F-US-CPI-1110 | US Oct CPI headline +0.4%m/m, core +0.3%; food +0.5, energy +0.7, shelter +0.3 | released 2026-11-10 08:30 ET；known_at 2026-11-10 | 11/11 19:57 BJT | [直达来源](https://www.bls.gov/news.release/archives/cpi_11102026.htm) | hot-inflation repricing；局限：not an execution quote |
| F-UST-1110 | 2/5/10/30Y=4.73/4.81/4.98/5.35%; 10Y real=2.78% | 2026-11-10 EOD；known_at 2026-11-10 | 11/11 19:58 BJT | [直达来源](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve) | 2s30s=62bp and gold headwind；局限：11/11 bond holiday; term premium missing |
| F-US-PRE-1111 | S&P futures +0.7%, Nasdaq100 futures about +1.6%; NVDA +4%, CRWV about +16% premarket | 2026-11-11 10:43 UTC；known_at 2026-11-11 | 11/11 19:58 BJT | [直达来源](https://www.reuters.com/business/sp-500-nasdaq-futures-rise-after-coreweave-soothes-ai-spending-fears-2026-11-11/) | AI rebound；局限：premarket only |
| F-CRWV-Q3 | CRWV Q3 revenue $3.661bn, op margin6%, net loss$709m, backlog$132.5bn; FY revenue$13.0-13.3bn; capex$37-39bn | Q3; released 2026-11-10；known_at 2026-11-10 | 11/11 19:59 BJT | [直达来源](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx) | AI demand/Capex split；局限：company-adjusted metrics; debt/interest countercase |
| F-CN-EOD | SSE50 2765.54 -0.27%; CSI300 4075.71 +0.41%; Shanghai +0.46%; ChiNext +3.11% | 2026-11-11 15:00 BJT；known_at 15:30 BJT | 11/11 19:56 BJT | [直达来源](https://news.10jqka.com.cn/20261111/c681700951.shtml) | growth/small-cap leadership；局限：media recap |
| F-CFFEX-PUB | IH/IF/IC/IM2612 2742.2/4043.4/6664.0/6623.0; volume/OI as dashboard | 2026-11-11 15:28 BJT；known_at 2026-11-11 | 11/11 19:56 BJT | [直达来源](https://www.9qihuo.com/hangqing?shichang=CFFEX) | current futures/basis；局限：public vendor; not official engine CSV |
| F-CN-OPT-1110 | HO/IO/MO2612 ATM14.90/18.10/29.51%; RR25 -1.27/-0.92/-3.05pp | 2026-11-10 official EOD；known_at 11/11 07:21 BJT | 11/11 19:56 BJT | [直达来源](https://github.com/farfromexact/China-Options-Engine/blob/a0e62a62c78b3fc3432303153408bfe4e818d69a/data/radar_latest.json) | option richness；局限：not 11/11 quote; history empty |
| F-COM-STATUS | current futures0 records; last-good806 contracts/77 products; Physical18/20, External17/22 | requested 11/11, generated19:03-19:12；known_at 2026-11-11 | 11/11 19:54 BJT | [直达来源](https://github.com/farfromexact/China-Commodities-Engine/tree/61c89422880c91041c2c368c44036e0a989da28c/data) | coverage limits；局限：core absent; selective public EOD |
| F-COM-OPT | commodity options45/64 products,1078 sampled contracts,22 skew-ready,0 core-ATM/surface/position/execution-ready | source date 2026-11-10；known_at 11/10 22:08 UTC | 11/11 19:54 BJT | [直达来源](https://github.com/farfromexact/China-Commodities-Engine/blob/61c89422880c91041c2c368c44036e0a989da28c/data/options/quality_latest.json) | local skew boundary；局限：sample not full chain; no bid/ask |
| F-OIL-1111 | Brent92.77, WTI86.80; shipping risk versus reported API +9mbbl build | 2026-11-11 09:34 GMT；known_at 2026-11-11 | 11/11 19:32 BJT | [直达来源](https://www.reuters.com/business/energy/oil-rises-two-month-low-hormuz-shipping-attacks-offset-iran-truce-hopes-2026-11-11/) | SC conditional reclaim；局限：EIA delayed; OPEC text missing |
| F-CFTC-GOLD | Gold non-commercial long220,530, short40,982; OI399,169 | positions 2026-11-03；known_at published 11/06 | 11/11 20:00 BJT | [直达来源](https://www.cftc.gov/dea/futures/deacmxsf.htm) | gold positioning net long；局限：weekly lag; not options skew |
| F-STOCK-CAP | Stock engine trade date11/9; universe5579, quotes5573, candidate_union empty; refresh failed | last valid 2026-11-09；known_at 11/11 08:32 BJT | 11/11 19:55 BJT | [直达来源](https://github.com/farfromexact/China-Stock-Engine/tree/8e61b672d10566406a25bb437a2f46f01d36e2c8/data/latest) | broad prior scan；局限：no current tradability/adjusted prices |

仓库读取状态：Global、Options、Commodities、Stock主入口均为ok；商品`report_input_latest.json`、night detail与Options history为empty；当批商品Futures为失败且0记录；Stock为stale/failed_backfill。工具截断未当成empty。

### 2.3 完整后台覆盖与展示上限分离

| 类别 | 应覆盖 | 实际可得且分析 | 数据不足/不可比 | 处置 |
|---|---|---|---|---|
| 美国利率/债券 | 2/5/10/30Y、实际利率、曲线、Fed/供给 | 11/10官方EOD | 11/11休市；term premium/swap/DV01缺 | 2s30s条件池 |
| 美元/外汇 | DXY、EUR/USD、USD/JPY、USD/CNH | 欧洲盘/盘前快照 | FX skew与同点carry缺 | 无直接交易 |
| Nasdaq/AI | QQQ、SOXX、SMH与公司IR链 | 前收+盘前催化 | 权重/Beta/borrow/期权链缺 | 相对价值条件池 |
| 油/能源 | WTI、Brent、SC与官方日历 | 实时油价+中国EOD | 裂解/OVX/OPEC原文缺 | SC条件池 |
| 黄金 | 现货、GLD、实际利率、CFTC | 可用并分析 | 央行/ETF日流/IV缺 | 观察 |
| 中国股指/期权 | 50/300/500/1000、期指期权 | 股指11/11；期权11/10 | 当前期权/Beta/官方当日CSV缺 | 次日观察 |
| 中国商品 | 63码+77 last-good | 13合约/上下文+Physical/External | core0；surface/position/execution0 | M/SC条件池 |
| A股公司 | 5579旧扫描+4公司补查 | 价量旧；公告补查 | 调整价/可交易/利润桥输入缺 | 0可执行个股 |
| 风险/流动性 | VIX/MOVE/HY | 11/10 last-good | CTA/dealer gamma缺 | 小仓/不追 |

## 3. 相较严格前序的实质变化

1. 中国EOD推进到11/11：创业板+3.11%、CSI1000约+1.37%而SSE50-0.27%，小盘/成长相对强度扩大；但HO/IO/MO仍停在11/10。
2. 美国从热CPI后的11/10收跌转为11/11盘前修复：纳指期货约+1.6%、CRWV约+16%、NVDA约+4%；削弱裸空AI，却未满足现金盘顺序触发。
3. 美债曲线无新价格发现：Veterans Day休市，2s30s仍以11/10的62bp为最近完整值；观点保留但不可宣称成交。
4. 商品新事实：M1-5收300、CU1-2达1220、SC至604/606、EC异常上行；旧SC空和EC空研究失效，M条件区上移，SC改为父idea下重夺610多头。
5. 黄金由急跌转约+0.4%技术修复，但DXY约102.49、10Y实际2.78%，政策信用叙事仍弱化。

## 4. 全球统一机会Top5

评分次序为逻辑/赔率凸性/催化/价格期限波动/拥挤技术；得分是研究优先级，不是胜率或风险预算。

| 排名 | idea_id/机会 | 方向/期限 | 分项=总分 | 研究｜证据｜执行 | 最关键错价与反证 | 工具 |
|---:|---|---|---:|---|---|---|
| 1 | `COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111` r2；M2701-M2705近多远空 | long near/short deferred；1-7 trading days | 21/19/17/9/7=73 | 有待验证优势｜4层但basis/option execution不足｜wait 21:00 ordered trigger | near-month tightness may persist only if pullback holds；反证：both legs OI fell；basis only C；no current bid/ask or margin | long 1 M2701 / short 1 M2705 |
| 2 | `AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106` r4；SOXX/SMH现金流—Capex Beta相对价值 | long SOXX short SMH；5-20 trading days | 22/17/15/8/8=70 | 有待验证优势｜部分｜wait US cash open and borrow | cash-flow breadth versus concentrated Capex financing risk；反证：AI premarket gap rebound；CRWV debt/interest expense；basket weights/beta incomplete | long 33 SOXX / short 10 SMH, dollar-neutral proxy not beta-neutral |
| 3 | `UST-2S30S-HOT-CPI-FLATTENER-20261111` r2；US 2s30s flattener | flattener；5-15 trading days | 22/17/16/8/7=70 | 有待验证优势｜部分｜closed; wait DV01/reopen | front-end policy tail may dominate only after retracement；反证：30Y supply/term premium；auction tail；no holiday price discovery | pay 2Y fixed / receive 30Y fixed or DV01-neutral futures |
| 4 | `COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111` r1；SC2612重夺610事件多头 | long；1-5 trading days | 18/16/15/11/8=68 | 有待验证优势｜3层但curve待核｜wait 21:00 exact quote | domestic acceptance of overseas risk premium above610；反证：reported API build；SC close conflict；EIA/OPEC missing | SC2612 after ordered trigger |
| 5 | `CN-IM-IH-SMALLCAP-BREADTH-RV-20261111` r1；IM-IH小盘相对强度延续 | long small-cap / short large-cap, beta pending；3-10 trading days | 19/14/12/11/10=66 | 方向假设待验证｜2层｜not ready until beta/current options/next breadth | growth breadth may persist if not one-day AI beta；反证：CSI500 lagged；options stale；dollar-neutral not beta-neutral | next-day beta-calibrated IM/IH or limited-risk MO/HO after quote |

## 5. Top3详细交易研究卡

### 卡1｜COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111 r2

- 定价与差异：11/11 EOD close3139/2839, spread300。r1的280-286/288触发改为当前292-298/300；不追溯修改假设旧仓
- 新事实→已定价→分歧/PnL：近月紧张只有在21:00回踩守住且CBOT豆类不弱时才延续；主要PnL由`risk=(entry-284)*10+80; target_net=(target-entry)*10-80`决定。最强竞争解释：两腿OI下降，basis/期权执行弱
- 催化/窗口：21:00重定价和1-7日USDA消化；下一合法窗口：21:00-23:00 BJT
- 工具：long1 M2701 / short1 M2705；乘数/最小变动：1点价差=CNY10；每腿tick价值CNY10；保证金：当前未知
- 顺序入场：先回踩292-298；首15m低点>=286；21:15收盘>=300；随后5m回踩296-300不破；CBOT soy>=1220；深度正常。全部AND。50%在296-300，第二次守300再50%；>304不追。
- 放弃/失效：CBOT<1220 OR first15m low<286 OR jump>304 no pullback OR depth abnormal；计划止损：284；期货损失不封顶
- 目标/退出：TP1 340；TP2 370；时间退出 2026-11-18 14:55 BJT
- 成本与好/中/坏：情景往返成本CNY80/组。entry=296, risk_cny=200, tp1_net_cny=360, tp1_R=1.8, tp2_net_cny=660, tp2_R=3.3；entry=300, risk_cny=240, tp1_net_cny=320, tp1_R=1.33, tp2_net_cny=620, tp2_R=2.58；entry=304, risk_cny=280, tp1_net_cny=280, tp1_R=1, tp2_net_cny=580, tp2_R=2.07
- 预算/压力：planned stop<=0.25% NAV; size=min(floor(0.0025*NAV/280),floor(0.0025*NAV/3531));后项为旧计划一限幅压力代理，须复核
- 待核：margin、two-leg slippage、limit、last trading day。实际持仓=未提供/未知；OHLC穿越不证明触发顺序或成交。

### 卡2｜AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106 r4

- 定价与差异：11/10 close 146.59/483.63; ratio0.30310; 11/11 only premarket rally。score72→70, r3→r4 because premarket gap raises chase risk; trigger retained
- 新事实→已定价→分歧/PnL：分散现金流相对集中Capex/融资beta仅在开盘后回踩确认时有价值；主要PnL由`ratio proxy only; actual basket needs same-time quotes, borrow, beta, fees and FX`决定。最强竞争解释：CRWV需求与NVDA反弹可令SMH重新领涨；债务/利息仍高
- 催化/窗口：22:30 cash open and AI financing updates；下一合法窗口：after22:30 BJT
- 工具：long33 SOXX / short10 SMH；乘数/最小变动：PnL=33*ΔSOXX-10*ΔSMH；保证金：short borrow/margin unknown
- 顺序入场：开盘后30-45m，ratio先15m收>0.3040，再回踩守0.3035；QQQ守首30m低；borrow/fee核实。50/50；>0.3070无回踩不追。
- 放弃/失效：borrow unavailable OR gap>0.3070 no pullback；计划止损：daily ratio close<0.3000 OR NVDA relative rebound>6% with ratio<0.3010
- 目标/退出：TP1 0.309；TP2 0.315；时间退出 20 trading days
- 成本与好/中/坏：unknown, not zero。entry=0.304, stop_risk_pct=1.32, tp1_gross_R=1.25, tp2_gross_R=2.75；entry=0.3045, stop_risk_pct=1.48, tp1_gross_R=1, tp2_gross_R=2.33；entry=0.3055, stop_risk_pct=1.8, tp1_gross_R=0.64, tp2_gross_R=1.73
- 预算/压力：zero until borrow/beta/quotes; then <=0.25% NAV trial
- 待核：borrow fee、beta、same-time quotes、cost。实际持仓=未提供/未知；OHLC穿越不证明触发顺序或成交。

### 卡3｜COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111 r1

- 定价与差异：11/11 EOD604, alternate606; Brent92.77。旧空因价格变化失效；新方向仅在reclaim触发，并保留父idea
- 新事实→已定价→分歧/PnL：只有610重夺且Brent/curve同向才证明国内接受风险溢价；主要PnL由`risk=(entry-599)*1000+1500; target_net=(target-entry)*1000-1500`决定。最强竞争解释：API据报+9mbbl、EIA延后、OPEC原文缺、收盘冲突
- 催化/窗口：21:00, EIA11/13 01:00, IEA11/13；下一合法窗口：21:00-02:30 BJT
- 工具：long SC2612；乘数/最小变动：1000 bbl/contract；CNY100 per0.1；保证金：unknown; last-good limit18% reverify
- 顺序入场：Brent>=93 AND SC first15m close>=610 AND next5m pullback608-611 holds AND SC1-2>=10。50%在610，第二50%<=612；>614放弃。
- 放弃/失效：SC>614 before pullback OR Brent<91.80 OR conflict persists OR official data bearish；计划止损：599；逻辑失效Brent<91.80或spread<5
- 目标/退出：TP1 630；TP2 648；时间退出 2026-11-17 22:55 BJT
- 成本与好/中/坏：CNY1500/contract。entry=610, risk_cny=12500, tp1_net_cny=18500, tp1_R=1.48, tp2_net_cny=36500, tp2_R=2.92；entry=612, risk_cny=14500, tp1_net_cny=16500, tp1_R=1.14, tp2_net_cny=34500, tp2_R=2.38；entry=614, risk_cny=16500, tp1_net_cny=14500, tp1_R=0.88, tp2_net_cny=32500, tp2_R=1.97
- 预算/压力：trial<=0.25% NAV; 18% move around604≈CNY108,720 before fees
- 待核：exact close、spread、margin/limit、OPEC。实际持仓=未提供/未知；OHLC穿越不证明触发顺序或成交。

## 6. 黄金特别研究

`GLD-POLICY-CREDIT-STABILIZATION-20261103` r12：政策信用叙事判断为**减弱但未失效**。11/11现货反弹是技术稳定，最近完整10Y实际2.78%与DXY坚挺仍是直接逆风。CFTC非商业净多较大且周频滞后；新鲜央行月度购金、GLD日流和可执行IV/skew未取得。

- CFTC截至2026-11-03：非商业多/空220,530/40,982，OI 399,169；周频滞后，不能代替当日期权拥挤。
- 3-6个月Call Spread：仅在实时链询价后，选流动期限，长25-40Δ/短10-20Δ；核净权利金与盈亏平衡，不复用旧strike。
- 微型黄金期货：10盎司线性、非限损；只有金价重夺并守住4080且DXY不扩张才研究。
- 黄金多+长债Put Spread：缓冲部分实际利率冲击，但增加曲线、波动率、相关性风险，须两条链都实报。
- 反向/不交易：实际利率继续上行且DXY>102.7时，失败反弹空优于硬做政策信用多；当前首选不交易。
- 执行状态：not_ready_no_option_quotes；实际持仓未提供/未知。

## 7. AI特别研究

CoreWeave Q3收入36.61亿美元、backlog 1325亿美元及上调全年收入/调整后营业利润指引支持需求；净亏7.09亿美元、利息8.46亿美元、Capex指引370-390亿美元及Reuters债务469亿美元保留融资风险反证。

覆盖与边界：已看大盘/QQQ、NVDA与芯片ETF、设备、网络/光通信、云/neocloud、软件和数据中心电力；完整成份权重、统一估值和当日期权Greeks缺失。

- 可选工具：SOXX/SMH相对篮子（非beta-neutral）；实时链后才用ETF期权；现金盘宽度确认后才研究QQQ方向；不交易。
- 下一项区分观测：22:30-23:15 BJT现金宽度、ratio回踩、NVDA贡献及CRWV股债分化。
- 结论：长期变现与当期盈利必须分开；需求验证不能抹去融资/利息/Capex风险，盘前上涨也不等于现金盘确认。

## 8. 中国50/300/500/1000、商品与公司专项

### 8.1 股指期货与期权

| 映射 | 现货 | 12月主力 / 11月次合约 | 主力量/OI/ΔOI | basis；年化 |
|---|---:|---|---:|---:|
| IH↔HO | 2765.54 | IH2612 2742.2 / IH2611 2761.8 | 25,950 / 63,192 / +1,720 | -23.34 (-0.844%)；年化-8.33% |
| IF↔IO | 4075.71 | IF2612 4043.4 / IF2611 4067.2 | 56,405 / 173,783 / +163 | -32.31 (-0.793%)；年化-7.82% |
| IC | 6627.91 | IC2612 6664.0 / IC2611 6701.8 | 102,586 / 173,915 / +4,705 | 36.09 (0.545%)；年化5.37% |
| IM↔MO | 6669.55 | IM2612 6623.0 / IM2611 6662.0 | 196,766 / 290,211 / +9,945 | -46.55 (-0.698%)；年化-6.89% |

basis按12月主力收盘减现货、37日历日简单年化，未调股息/融资；CSI500现货源置信度较低。相对收益：IM-IH +1.64pp，IF-IH +0.68pp，IM-IF +0.96pp，IC-IF -0.68pp，IM-IC +1.64pp；dollar-neutral≠beta-neutral。

期权：HO/IO/MO官方EOD晚一日。ATM14.90/18.10/29.51%，RR25 -1.27/-0.92/-3.05pp，BF25 0.61/0.63/1.26pp，PCR(OI)0.629/0.626/0.628；10Δ put IV18.04/20.97/37.67%。Gamma峰仅是模型绝对Gamma集中，不是dealer方向。 IC没有默认同标的一一对应CFFEX指数期权。11/10期权只能作研究基线；PCR/OI不推dealer净Gamma。

### 8.2 中国商品全扫描与消费者口径

- 覆盖：63个目标代码、77个last-good产品、当前13个准确合约/上下文；新增PD/PT仅列动态发现。未取数不等于无机会。
- 黑色：I/JM/J/RB Physical可得但basis全为C级；无当前完整core curve，仅背景。
- 有色/贵金属：CU、AG准确合约核过；CU价差1220远离旧入场，AG双向观察；其余多为External/旧状态。
- 能源化工：SC/FU/MA上下文及海外油核过；core为空限制排序，不代表无机会。
- 新能源：LC/SI/PS仅last-good；当前准确合约缺失。
- 农产品：M/C/Y/P当前上下文已查；M领先，C与USDA逻辑背离，其余证据不足。
- 集运：EC2612较结算约+5.35%但只是14:06快照；旧空失效，无夜盘且实体运价/曲线缺。
- Options：45/64抽样产品；quote_coverage_complete只代表计划样本。22个skew-ready可做局部研究，但core-ATM=0、surface/positioning/execution=0；不得写完整PCR、拥挤、dealer Gamma、权利金或可成交限损。
- Night：此前夜盘归属交易日11/11且无calendar_mismatch，但detail为空、official close未核。今晚21:00归属11/12，截点尚未开始。
- Crosscheck：SHFE/INE/CZCE/GFEX有官方合约计数，DCE HTTP412；vendor baseline缺，matched/comparable/different均0。这是不可比，不是价差冲突。

### 8.3 China-Stock-Engine与公司证据

引擎当前刷新失败、candidate_union为空。限定补查中微公司、沪电股份、紫金矿业、宝钢股份截至截点公告，未确认除既有回购/季报外的新经营事实。A股11/11公开扫描为90行业中72上涨，元件、通信设备、自动化、半导体居前；这是价格宽度，不是公司基本面核验。

简化利润桥：
- 紫金：金铜售价×销量减采选成本、权益金、汇率、Capex与少数股东；金属涨不证明当期已兑现利润。
- 宝钢：钢价/销量减矿焦能源成本、库存与长协滞后；I/RB基差仅C级，不能报精确吨毛利。
- 中微/沪电：订单转收入和毛利率减Capex、营运资金及估值；回购改善资本配置但不是新增经营利润。

没有新增可执行个股候选。最优表达优先可验证指数/期货/ETF相对结构；下一窗口2026-11-12 09:30 BJT；无21:00股指期货夜盘。

## 9. 七大全球模块、风险日历与夜盘地图

- 美国利率：11/10官方2/5/10/30Y=4.73/4.81/4.98/5.35%，2s10s25bp、2s30s62bp、5s30s54bp；10Y实际2.78%，同日差推BEI约2.20%。热CPI重定价前端，但11/11休市。反证是30Y供给/期限溢价可令曲线重新变陡；term premium和实时swap未取。
- 外汇：DXY约102.49，EUR/USD1.1137、USD/JPY158.96、USD/CNH6.6728。组合压制黄金与长久期，但CNH未现失序。FX skew与同点carry缺，故无期权结构或单因子归因。
- 油/能源：Brent/WTI反弹至92.77/86.80，运输风险与据报API累库对冲。裂解、OVX/skew、完整官方曲线缺。中国化工利润传导仍取决于长协、库存、汇率与滞后。
- 风险/流动性：VIX19.46、MOVE92.43、HY OAS331bp均为最近完整日。股波/信用未失序而利率波动上升，支持相对交易与减杠杆。CTA与dealer gamma方向未核。

### 9.1 下一24小时/7天北京时间风险日历

| 北京时间 | 事件 | 状态 | 风险应对 |
|---|---|---|---|
| 2026-11-11 21:00 | 中国商品夜盘开盘（11/12交易日） | 合法窗口 | M/SC/CU/AG；15/30/45分钟顺序验证 |
| 2026-11-11 22:30 | 美股现金开盘 | 股票开、Treasury现金休 | AI盘前反弹确认；债券不可执行 |
| 2026-11-12 09:30 | A股和股指期货开盘 | 计划窗口 | 重核IM/IH宽度、basis及当日期权链 |
| 2026-11-12 23:00 | Fed Barr演讲：AI与不平等 | 官方Fed日历10:00 ET | AI政策标题风险 |
| 2026-11-13 01:00 | EIA周度石油状态报告 | 官方节假日延后Thu12:00 ET | SC/Brent与IV；API背离可翻转 |
| 2026-11-13 02:00 | 美国30Y再开标预期 | 第二周常规日历；精确条款待核 | 2s30s变陡尾部 |
| 2026-11-13 21:30 | 美国10月PPI | BLS Fri08:30 ET | USD/利率/黄金/AI；避免无报价短Gamma |
| 2026-11-13（官方时刻未取） | IEA Oil Market Report | 日期已确认 | 油供需基线 |
| 2026-11-16 10:00 | 中国10月活动、工业、消费、投资、地产 | NBS官方日历 | 风格、金属、CNH |
| 2026-11-17 21:30 | 美国进出口价格 | BLS官方日历 | 商品通胀/FX |

OPEC月报市场日历指向11/11，但截至截点未取得官方原文，不计已发生催化。社融/MLF若无官方明确时刻，只列条件事件。

### 9.2 今晚21:00商品夜盘风险地图

- 21:15：M首15m低>=286且收>=300；SC仅在Brent>=93时收>=610
- 21:30：M回踩296-300守住；SC回踩608-611守住且1-2>=10
- 21:45：深度正常、无单腿限幅/报价冲突、海外映射仍同向

- **风险延续**：若M守300、SC>610、Brent>=93、USD稳定；仅顺序条件单；商品主题初始planned-loss<=0.75% NAV
- **假突破**：若M<286或SC<599；取消新多；无新完整setup不反手
- **流动性冲击**：若深度消失、来源冲突、DXY/JPY跳变；不新建期货价差；重算保证金/限幅

### 9.3 组合预算与压力

- 试仓NAV0.25%-0.75% planned-loss；卡片专属更紧上限优先；确认NAV0.75%-1.5%且须新鲜报价/完整触发；主题合计同一高确信主题2.5%-3%。
- 规模：contracts=floor(card cap*NAV/stressed loss per unit)，再受margin/liquidity约束；margin不是风险预算
- 压力：1/2个限幅跳空与价差腿错位；中美错时假日与21:00/22:30跳空；追加保证金/流动性消失/FX换算/相关性断裂；IV崩飙、信用与地缘极端。
- 实际持仓：未提供/未知；不编净敞口。

### 9.4 发布校验与未解缺口

已重算Top5分项、M/SC情景PnL、AI比率R、IH/IF/IC/IM basis与年化；日历/DST/合法窗口、合约月份/乘数/单位、父idea与参数变更、同源MD/JSON表达已核。未解：CSI500 cash source nonofficial；SC close604/606 conflict；commodity core batch absent；11/11 China options absent；stock engine stale；option premiums/margins absent。缺口只限制依赖候选。

### 9.5 公开来源

1. [US October 2026 CPI](https://www.bls.gov/news.release/archives/cpi_11102026.htm)（BLS，2026-11-10；读取 2026-11-11 19:57）：headline/core CPI、components
2. [US Treasury nominal yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve)（US Treasury，2026-11-10；读取 2026-11-11 19:58）：2/5/10/30Y、curve
3. [US Treasury real yield curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)（US Treasury，2026-11-10；读取 2026-11-11 19:58）：10Y real、breakeven inference
4. [BLS 2026 release calendar](https://www.bls.gov/schedule/2026/)（BLS，accessed 2026-11-11；读取 2026-11-11 20:01）：Nov13 PPI、Nov17 import/export
5. [Federal Reserve calendar](https://www.federalreserve.gov/newsevents/calendar.htm)（Federal Reserve，2026-11-11；读取 2026-11-11 20:01）：Veterans Day、Barr speech
6. [CoreWeave Q3 2026 results](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx)（CoreWeave IR，2026-11-10；读取 2026-11-11 19:59）：results、guidance、capex/interest
7. [US premarket AI rebound](https://www.reuters.com/business/sp-500-nasdaq-futures-rise-after-coreweave-soothes-ai-spending-fears-2026-11-11/)（Reuters，2026-11-11；读取 2026-11-11 19:58）：futures、NVDA/CRWV
8. [Reuters oil update](https://www.reuters.com/business/energy/oil-rises-two-month-low-hormuz-shipping-attacks-offset-iran-truce-hopes-2026-11-11/)（Reuters，2026-11-11；读取 2026-11-11 19:32）：Brent/WTI、shipping/API
9. [CFTC CMX futures only](https://www.cftc.gov/dea/futures/deacmxsf.htm)（CFTC，2026-11-03 positions；读取 2026-11-11 20:00）：gold positions、OI
10. [China 11/11 market recap](https://news.10jqka.com.cn/20261111/c681700951.shtml)（10jqka，2026-11-11；读取 2026-11-11 19:56）：indices、sector breadth
11. [CFFEX public quote table](https://www.9qihuo.com/hangqing?shichang=CFFEX)（9qihuo，2026-11-11；读取 2026-11-11 19:56）：IH/IF/IC/IM quote volume OI
12. [China options radar](https://github.com/farfromexact/China-Options-Engine/blob/a0e62a62c78b3fc3432303153408bfe4e818d69a/data/radar_latest.json)（GitHub，2026-11-10；读取 2026-11-11 19:56）：option metrics、prior basis
13. [China commodities engine data](https://github.com/farfromexact/China-Commodities-Engine/tree/61c89422880c91041c2c368c44036e0a989da28c/data)（GitHub，2026-11-09 to 2026-11-11；读取 2026-11-11 19:54）：readiness、coverage、commodity facts
14. [2026-11-11 commodities evening auxiliary report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/108d026a0187c4f81eaed78e61d5a36bb0883bda/reports/2026/11/2026-11-11_commodities_evening.json)（GitHub，2026-11-11；读取 2026-11-11 19:54）：commodity candidates、calculations
15. [China stock engine latest](https://github.com/farfromexact/China-Stock-Engine/tree/8e61b672d10566406a25bb437a2f46f01d36e2c8/data/latest)（GitHub，2026-11-09；读取 2026-11-11 19:55）：universe、gaps、stale
16. [NBS 2026 release calendar](https://www.stats.gov.cn/xw/tjxw/tzgg/202512/t20251224_1962137.html)（NBS，published 2025-12-25；读取 2026-11-11 20:01）：Nov16 activity
17. [Strict prior global report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/108d026a0187c4f81eaed78e61d5a36bb0883bda/reports/2026/11/2026-11-11_morning.json)（GitHub，2026-11-11 morning；读取 2026-11-11 19:53）：lineage、prior scores/triggers
18. [Same-edition prior global report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/108d026a0187c4f81eaed78e61d5a36bb0883bda/reports/2026/11/2026-11-10_evening.json)（GitHub，2026-11-10 evening；读取 2026-11-11 19:53）：lineage、prior states

## 10. 严格四行行动清单

A. 今天没有应立即建立的新仓位。
B. 仅挂条件：M2701-M2705正套；22:30后SOXX/SMH相对价值；SC2612重夺610；美债重开后的2s30s趋平。
C. 继续观察：IM-IH小盘相对强度、黄金稳定化、CU2612-2701、AG2702与A股公司证据更新。
D. 必须回避：追涨M>304、SC>614、盘前直接追AI；若此前按旧研究自有仓位，则旧SC空头与EC空头仅按原失效规则有条件退出，不能据此认定已持仓。
