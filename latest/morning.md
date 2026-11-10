# 全球跨资产高风险机会雷达｜2026-11-10晨间版

生成：2026-11-10T08:13:30+08:00；信息截止：2026-11-10T08:13:30+08:00。仅作研究与交易决策支持，不自动下单；账户权限、合约流动性、报价、保证金和执行资格须另核。

## 1. 一句话风险状态

风险偏好转为事件驱动修复：美股与波动率显著改善，但英伟达逆势、油价急跌及高实际利率揭示结构分化；中国首选白银吸收与铜曲线，仅限日内条件单。

## 2. 全球仪表盘与事实台账

| 资产 | 最新 | 1D | 周变化 | 信号 | 时间 | 缺口 |
| --- | --- | --- | --- | --- | --- | --- |
| UST 2/5/10/30Y | 4.56/4.67/4.88/5.26% | +5/+3/+2/0bp | 未独立重算 | 2s10s 32bp; 2s30s 70bp; 5s30s 59bp | 2026-11-09 official close | term premium and exact Fed path unavailable |
| 10Y real / inferred BEI | 2.66% / 2.22% | +3/-1bp | 未独立重算 | gold与真实利率正相关背离 | 2026-11-09 official close | BEI arithmetic |
| DXY / EURUSD / USDJPY / USDCNY proxy | 101.68 / ~1.1225 / ~157.92 / 6.6709 | DXY -0.60 | 未同源重算 | 美元回落、日元仍弱 | 2026-11-09 non-synchronous | USDCNH exact close unavailable; not executable |
| Nasdaq / QQQ | 25253.14 / 679.35 | +2.74% / +3.45% | 未同源重算 | 广泛risk-on修复 | 2026-11-09 cash | QQQ is delayed feed snapshot |
| SOXX / SMH / NVDA | 146.76 / 487.41 / 178.67 | +7.51% / +5.00% / -4.30% | 未独立重算 | 等权更高的SOXX显著跑赢重NVDA的SMH | 2026-11-09 cash | borrow/beta/options surface not checked |
| WTI / Brent | 86.38 / 92.57 | -4.90% / -5.8% | 未同源重算 | 地缘溢价急退；不等同中期供需转空 | 2026-11-09 settlement/close | curve/cracks/OVX/skew unavailable |
| COMEX gold / GLD | 4149.50 / 379.53 | +1.83% / +1.89% | 未同源重算 | 高真实利率下仍上涨，政策信用/避险假设未失效 | 2026-11-09 | current ETF flow and IV/skew unavailable |
| VIX / MOVE / HY OAS | 19.92 / 86.0 / 3.48% | -22.31% / 约-7.3% / last-good | 未同源重算 | 波动与利率压力回落；信用数据滞后 | VIX/MOVE 11/09; HY 11/05 | mixed frequency |
| SSE50 / CSI300 / CSI500 / CSI1000 | 2789.15 / 4056.11 / 6586.18 / 6499.74 | +0.06/+0.05/-0.17/-0.09% | history empty | 大盘相对小盘占优 | 2026-11-09 EOD | breadth/industry contribution unavailable |
| IH/IF/IC/IM2612 | 2765.8/4023.6/6532.8/6448.6 | +0.41/-0.02/-0.37/-0.26% | history empty | basis -0.84/-0.80/-0.81/-0.79%; OI全降 | 2026-11-09 EOD | cannot infer new long/short |
| HO/IO/MO2611 | ATM 15.13/20.90/35.63%; RR25 -0.90/-1.34/-3.44 | ATM -0.17/-1.04/-1.97 vol | history empty | MO protection仍最贵；IV随修复回落 | 2026-11-09 EOD | dealer direction unknown |
| AG2702 / CU2612-CU2701 / SC2612 | 12610 settle / 1150 spread / 637.6 settle | AG +0.45%; curve unchanged; SC +1.05% vs prior settle | engine horizons vary | AG外盘映射、CU曲线、SC油价去溢价 | 2026-11-09 EOD | night exact prices empty; no live depth |

利率：2s10s/2s30s/5s30s为32/70/59bp；10Y实际2.66%、推算BEI 2.22%。股市上涨与真实利率上行并存，更像油价去溢价和空头回补驱动的风险修复，不是单一宽松叙事。FX报价非同步，USDCNY仅为CNH缺失时的代理，不用于执行。

商品协议：Futures 77品种/806合约、full_market_ready=true；Physical 18/20、External 17/22。Options为core_v1抽样：45/64产品，ATM-ready 44、skew-ready 26、surface/positioning/execution均0，full_chain_verified=false，dealer方向未知。Night状态标签为11/10交易日、11/09夜盘、calendar_mismatch=false、覆盖51.861%，但明细文件为空，不能称官方夜盘收盘。官方价格核对SHFE/INE/CZCE/GFEX全部可比项匹配；DCE HTTP412，且未核量仓。实际影响：期货研究可用；期权仅局部研究；所有执行必须重取实时双边与深度。

覆盖结论：美债、FX、AI、油、金、中国四指数/期权、风险、77商品和5579只A股能力均扫描。全球油品曲线/裂解/OVX、黄金ETF流/IV、Fed精确路径、Stock 11/09刷新缺失，只降级相应结论，不外溢否定其他模块。

## 3. 较前序真正变化

1. **美股风险偏好从压力转为广泛修复**：S&P/Nasdaq分别+2.35%/+2.74%，VIX跌至19.92；但今晚CPI前不能把单日修复外推为新趋势。
2. **AI内部结构比指数方向更重要**：SOXX +7.51%、SMH +5.00%，而NVDA -4.30%；重NVDA权重差解释了部分相对收益，形成可检验但非立即可执行的ETF相对候选。
3. **油价地缘溢价快速回吐**：WTI/Brent约-4.9%/-5.8%；SC前序多头逻辑失效，继承父idea并翻为反弹失败做空，不回填历史盈利。
4. **贵金属与铜对美元走弱反应更强**：COMEX金+1.83%、外盘银与铜上行；AG2702由观察升为第一候选，但引擎夜盘明细为空，必须等09:00日盘确认。
5. **中国通胀结构呈上游挤压**：CPI +0.7%而PPI +5.7%，采掘+27.9%；利好上游并非自动等于矿业股可执行，合同、库存、套保、Capex和少数股东仍是利润桥缺口。
6. **A股公司数据陈旧**：Stock Engine仍停在11/06；对紫金、宝钢及11/09公告做限定检索，未见新增经营披露，因此本期A股重点候选为0。

状态修订：CU沿用稳定idea、revision 7；黄金revision 10。SC原多头先判失效，再以parent_idea_id建立反弹失败空头；未假设历史成交或盈利。

## 4. 全球统一Top5

| 排名 | 机会 | 方向/期限 | 分数 | 三轴 | 证据/执行 |
| --- | --- | --- | --- | --- | --- |
| 1 | AG2702外盘确认后的吸收型日内多头 | 条件做多 | 73 | 待验证优势 | not_ready_wait_0915_sequence_and_live_external |
| 2 | CU2612/2701近强远弱跨期 | 多CU2612/空CU2701 1:1 | 71 | 待验证优势 | not_ready_wait_pullback_reclaim_and_live_LME |
| 3 | SC2612油价去溢价后的反弹失败空头 | 条件做空 | 69 | 待验证优势 | not_ready_wait_failed_rebound_curve_Brent |
| 4 | 多SOXX/空SMH的NVDA集中度相对价值 | 美元中性偏多广义半导体、空高NVDA权重 | 69 | 待验证优势 | not_ready_beta_borrow_and_cash_open_confirmation |
| 5 | 黄金政策信用凸性 | 中期偏多、短线等CPI | 68 | 中期不变、短期证据增强但仍不可执行 | not_ready_wait_CPI_and_options_quotes |

分项：1.AG2702外盘确认后的吸收型日内多头=21+17+15+11+9=73；2.CU2612/2701近强远弱跨期=20+17+15+12+7=71；3.SC2612油价去溢价后的反弹失败空头=20+16+15+10+8=69；4.多SOXX/空SMH的NVDA集中度相对价值=19+15+13+12+10=69；5.黄金政策信用凸性=19+15+15+10+9=68。分数仅为研究优先级，不是胜率、回报或仓位。AP、EC、IH/IM、紫金未入榜不等于未研究。

## 5. Top3交易详卡

共同约束：北京时间21:30美国CPI前不留新增无保护隔夜Delta/Vega；三卡均为研究计划而非订单。

### 1. COM-M-AG2702-ABSORPTION-LONG-20261110

- 合同/方向：AG2702；long；15 kg/point；1 CNY/kg = 15 CNY/lot。
- 窗口与顺序：2026-11-10 09:00—14:45 BJT。open<=12820 AND first 15m low>=12680 AND 09:15 close>=12780 AND live external silver>=53 AND depth normal。
- 分批：50% after complete trigger; 50% only after first pullback holds 12780。
- 失效/止损：30m close<12580 OR external silver<52.30 OR USD and real yields jump together；计划止损 12580，但止损不保证成交或封顶。
- 目标/退出：TP1 13200；TP2 13600；2026-11-10 14:45 BJT; no unbuffered CPI overnight exposure。
- 放弃：open>12820 OR direct print>=12900 before sequence OR live external/depth unavailable。
- 成本与情景：450 CNY/lot round-trip scenario, not a quote。入场12720: 风险2550、TP1净6750(2.65R)、TP2净12750(5R)；入场12760: 风险3150、TP1净6150(1.95R)、TP2净12150(3.86R)；入场12820: 风险4050、TP1净5250(1.3R)、TP2净11250(2.78R)。
- 风险预算：trial 0.35% NAV; confirmed disabled before CPI; size=floor(0.0035*NAV/4050)。压力：one 20% limit ≈37,830 CNY/lot from reference notional; two compounded ≈83,226; margin is not loss cap。实际持仓：unknown/not provided。

### 2. COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106

- 合同/方向：long CU2612 / short CU2701 1:1；long near-minus-deferred；5 t/leg；10 CNY/t = 50 CNY/leg。
- 窗口与顺序：2026-11-10 09:00—14:45 BJT。spread tests 950—1000 without trading below 800; then 15m close>=1050; next 5m pullback to 1020—1050 holds; LME copper>=13750 and both legs show normal depth。
- 分批：50% after reclaim; 50% after pullback hold, integer pairs only。
- 失效/止损：spread<800 OR LME<13750 OR depth/liquidity disappears；计划止损 800，但止损不保证成交或封顶。
- 目标/退出：TP1 1500；TP2 1750；2026-11-10 14:45 BJT; multi-day thesis must be revalidated after CPI。
- 放弃：no pullback, sequence reversed, or worst allowed entry leaves <=1R to TP1。
- 成本与情景：500 CNY/pair round-trip scenario, not a quote。入场1020: 风险1600、TP1净1900(1.19R)、TP2净3150(1.97R)；入场1035: 风险1675、TP1净1825(1.09R)、TP2净3075(1.84R)；入场1050: 风险1750、TP1净1750(1R)、TP2净3000(1.71R)。
- 风险预算：trial 0.50% NAV but cap at formula floor(0.005*NAV/1750); copper+Zijin theme<=1.25%。压力：two-leg gap, exchange limits and margin increase; stop does not cap maximum loss。实际持仓：unknown/not provided。

### 3. COM-M-SC2612-FAILED-REBOUND-SHORT-20261110

- 合同/方向：SC2612；short；1000 bbl/point；0.1 CNY/bbl = 100 CNY/lot。
- 窗口与顺序：2026-11-10 09:00—14:45 BJT。if open<=615 abandon; otherwise rebound to 620—626 then 15m close<618 AND near curve ratio<=0.5% AND Brent<=93.5; enter only after retest of 618 fails。
- 分批：30%/30%/40% at approximately 617/616/615 after full sequence。
- 失效/止损：15m close>=629 OR curve ratio>1% OR Brent>96.5 OR verified supply outage；计划止损 629，但止损不保证成交或封顶。
- 目标/退出：TP1 590；TP2 575；2026-11-10 14:45 BJT。
- 放弃：open<=615 OR no rebound/failure sequence OR live Brent/curve/depth unavailable。
- 成本与情景：1500 CNY/lot round-trip scenario, not a quote。入场617: 风险13500、TP1净25500(1.89R)、TP2净40500(3R)；入场616: 风险14500、TP1净24500(1.69R)、TP2净39500(2.72R)；入场615: 风险15500、TP1净23500(1.52R)、TP2净38500(2.48R)。
- 风险预算：trial 0.25% NAV; size=floor(0.0025*NAV/15500); oil+shipping theme<=1.0%。压力：gap/limit/margin/liquidity risk; stop is not maximum loss。实际持仓：unknown/not provided。

## 6. 黄金专题

结论：中期政策信用期权比喻不变，短期价格证据增强但执行仍待CPI与报价。证据：gold +1.83% while 10Y real +3bp and DXY fell; CFTC Nov3 non-commercial net long 179,548。最强竞争解释：美元下跌可以解释大部分反弹；2.66%真实利率仍高；当前ETF流、IV/skew缺失。

工具比较：3—6M call spread only after live strikes/IV/debit; MGC only after CPI confirmation; gold long plus long-bond put spread remains two separate legs, not contract-limited portfolio loss。替代/不交易：GLD cash, MGC confirmation, reduce/no trade, or dollar/real-yield hedge; no old strike reused。证伪：post-CPI DXY and real yields rise together while gold closes below pre-rally anchor; ETF holdings and CFTC both deteriorate when available。“政策信用期权”只是经济比喻，不代表合同限损。

## 7. AI专题

现金流定价权龙头与Capex Beta继续分化；本期新变量是NVDA idiosyncratic drag and SOXX/SMH weighting difference。覆盖：Nasdaq/QQQ, SOXX/SMH, chips, equipment, networking, cloud, software and power checked; no complete member-level basket or valuation update。候选公式：Dollar-neutral not beta-neutral: long SOXX notional = short SMH notional; at 146.76/487.41, share ratio is 3.321 SOXX per 1 SMH before integer rounding。

最强反证：NVDA issue may reverse quickly; SOXX one-day +7.5% can mean crowded rebound; Cisco earnings and CPI can dominate。执行：not ready until borrow, beta, current prices, weights, fees and 30—45m cash confirmation are checked。催化：Cisco Q1 FY27 results/call Nov13 05:30 BJT。现金流定价权（云/软件/网络龙头）与远期Capex Beta（设备/电力/二线芯片）不能因一天反弹混为一类；缺完整成员与权重的组合只称主题。

## 8. 中国50/300/500/1000及公司专题

- 风格：IH relative to IM strengthened, but without beta estimates it is only a directional style observation, not beta-neutral trade。
- 期货：Dec basis: IH -23.35 (-0.84%, annualized -7.84%), IF -32.51 (-0.80%, -7.50%), IC -53.38 (-0.81%, -7.59%), IM -51.14 (-0.79%, -7.36%); Mar-Dec spreads -37/-61.6/-131.6/-140.2。
- 期权：front ATM 15.13/20.90/35.63 and RR25 -0.90/-1.34/-3.44 for HO/IO/MO; Dec ATM 15.68/19.98/33.30 and RR25 -1.77/-1.15/-4.08; no full history or dealer gamma direction。Gamma峰值仅为绝对OI节点（HO 2800；IO 4100；MO 6600/6800/7000），不推dealer净方向。
- ETF：ETF share-change×close estimates: 50ETF +919m, 300ETF +115m, 500ETF -764m, 1000ETF -238m CNY; estimates are not order-flow proof。IC没有HO/IO/MO同标的一一对应；用MO/IO/ETF代理均留下指数、beta、basis与跟踪误差。
- 公司：Stock Engine源日2026-11-06；限定检索范围为11/09 disclosures for Zijin, Baosteel and a broad CNInfo list，新增经营事实0。Q3 last-good: revenue RMB283.5bn +12%, attributable profit RMB57.5bn +52%, operating cash flow RMB84.3bn +62%, mined gold 70t +8%; not new Nov9 catalyst。利润桥：metal prices×volume minus unit cost, inventory/hedges, FX, capex and minority interests。执行：no Nov9 price/status/fees/current quote; no A-share Top5 candidate。
- 重点非入榜：AP局部波动有研究价值但无双边；EC下行缺现货运价；LC/EB/P/JM异常已查，证据或赔率不足；不以局部期权缺口降低全商品或全球资产评分。

## 9. 未来24小时/7天、风险预算与发布闸门

| 北京时间 | 事件 | 影响 | 计划 |
| --- | --- | --- | --- |
| 11/10 09:00 | 中国商品日盘 | AG/CU/SC及全商品 | 只执行顺序触发；夜盘明细为空，09:00后重建事实 |
| 11/10 09:30 | A股/股指期货现金窗口 | IH/IM、公司股、CNH | 30—45分钟后核宽度、basis与ETF；不把昨日EOD称今日反应 |
| 11/10 21:30 | 美国10月CPI | 全资产 | 此前不留无保护新增Delta/Vega；CPI后重核美元、真实利率、金、油、AI |
| 11/11 01:00 | USDA WASDE（官方页面待当日发布确认） | 农产品 | 商品期权执行未就绪，保持研究观察 |
| 11/11 02:00 | 美国10Y国债拍卖（金额/结果待官方当日确认） | 期限溢价、美元、黄金、成长股 | 看尾部、投标倍数和间接比例，不预判结果 |
| 11/13 01:00 | EIA周度石油报告（假期延后） | WTI/Brent/裂解/SC | 核库存、炼厂、出口；不能以地缘替代供需 |
| 11/13 05:30 | Cisco Q1 FY27业绩电话会 | 网络设备/AI资本开支 | 更新订单、AI收入、毛利、FCF与Capex兑现 |
| 未来7天，具体时点待官方确认 | 中国社融信贷/PBOC操作及A/H股披露 | 中国股指、CNY、地产信用 | 仅以实际发布时间为known_at；不提前编数值 |

风险预算：试仓NAV 0.25%—0.75%；确认0.75%—1.50%，但CPI前禁用新增确认仓；同一高确信主题总上限2.5%—3.0%。专属上限：AG 0.35%，CU 0.50%，SC 0.25%；相关主题上限见JSON。没有账户持仓输入，净敞口未知。压力覆盖CPI跳空、连续涨跌停、保证金、隐波重定价、流动性消失、相关性断裂和假期错位。

发布校验：评分和情景损益已重算；合约乘数/单位、先后顺序、CPI与美股DST换算已核；MD/JSON来自同一对象。未完成项包括实时bid/ask/深度、账户权限、全球油曲线/裂解、黄金流量/IV、Fed精确路径及Stock 11/09刷新。CI为pending_or_unverified，不冒称通过。

来源：

1. [U.S. Treasury nominal curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202611&type=daily_treasury_yield_curve)（U.S. Treasury，2026-11-09；支持：2/5/10/30Y yields、curve spreads）
2. [U.S. Treasury real curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=202611&type=daily_treasury_real_yield_curve)（U.S. Treasury，2026-11-09；支持：10Y real yield、inferred BEI）
3. [US market close recap](https://apnews.com/article/stock-markets-nvidia-ai-oil-iran-f3adb77b72d636c77098ca9ee8dc5b3b)（Associated Press，2026-11-09；支持：S&P/Nasdaq/Russell closes、NVDA divergence、Brent decline）
4. [VIX historical data](https://www.cboe.com/tradable_products/vix/vix_historical_data/)（Cboe，2026-11-09；支持：VIX close and daily change）
5. [CPI release schedule](https://www.bls.gov/schedule/news_release/cpi.htm)（BLS，accessed 2026-11-10；支持：October CPI release Nov10 08:30 ET）
6. [CFTC COMEX futures-only report](https://www.cftc.gov/dea/futures/deacmxsf.htm)（CFTC，positions 2026-11-03；支持：gold positioning）
7. [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（EIA，accessed 2026-11-10；支持：Nov12 12:00 ET holiday-delayed petroleum release）
8. [China October CPI](https://www.stats.gov.cn/sj/zxfb/202611/t20261109_1962034.html)（NBS，2026-11-09；支持：CPI and PPI headline）
9. [China October PPI interpretation](https://www.stats.gov.cn/sj/sjjd/202611/t20261109_1962035.html)（NBS，2026-11-09；支持：industry PPI and purchase prices）
10. [Cisco Q1 FY27 call notice](https://investor.cisco.com/news/news-details/2026/Cisco-Schedules-Conference-Call-for-Q1-Fiscal-Year-2027-Financial-Results/default.aspx)（Cisco IR，2026-11-03；支持：earnings call timing）
11. [China options radar](https://github.com/farfromexact/China-Options-Engine/blob/790037a4b3efe5023df7b491f60918c67dd17874/data/radar_latest.json)（GitHub，2026-11-09；支持：indices/futures/basis/options metrics）
12. [China options history](https://github.com/farfromexact/China-Options-Engine/blob/790037a4b3efe5023df7b491f60918c67dd17874/data/radar_history.json)（GitHub，read 2026-11-10；支持：empty history limitation）
13. [China commodities engine data](https://github.com/farfromexact/China-Commodities-Engine/tree/0a3cfe8edb69df6f5f49ae3c38c3089c412a88b8/data)（GitHub，2026-11-09 / generated 2026-11-10；支持：77-product scan、module quality、AG/CU/SC facts）
14. [China stock engine latest](https://github.com/farfromexact/China-Stock-Engine/tree/c0b7c87287c5562ee4e64d6298b5fa4ffa256d1f/data/latest)（GitHub，2026-11-06；支持：stale capability and company evidence）
15. [Zijin official disclosures](https://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=601899)（SSE，accessed 2026-11-10；支持：bounded disclosure search）
16. [Baosteel official disclosures](https://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=600019)（SSE，accessed 2026-11-10；支持：bounded disclosure search）
17. [Strict prior global report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/97d525275b2f77a58f7e1bc854ed589b2a72435d/reports/2026/11/2026-11-09_evening.json)（GitHub，2026-11-09 evening；支持：stable idea inheritance and revisions）
18. [Same-edition prior report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/97d525275b2f77a58f7e1bc854ed589b2a72435d/reports/2026/11/2026-11-09_morning.json)（GitHub，2026-11-09 morning；支持：same-edition baseline）
19. [2026-11-10 commodity auxiliary report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/97d525275b2f77a58f7e1bc854ed589b2a72435d/reports/2026/11/2026-11-10_commodities_morning.json)（GitHub，2026-11-10 07:07 BJT；支持：commodity scan and conditional cards; market facts traced to engine）

## 10. 今日行动清单

A. 今天可立即建立的新仓：没有；08:08仍在中国开盘前，且今晚美国CPI使隔夜裸方向不满足门槛。
B. 今天仅应挂条件的候选：AG2702吸收多、CU2612/2701回撤重夺、SC2612反弹失败空；均须完整顺序、实时外盘与深度，14:45前退出。
C. 今天继续观察的机会：多SOXX/空SMH美元中性主题、黄金政策信用凸性、IH相对IM、AP局部波动、紫金利润桥；均非执行就绪。
D. 今天必须回避或有条件退出的交易：追高AG/CU、油价急跌后追空SC、无bid/ask商品期权、未经beta/借券核验的AI篮子、把ETF份额变化当机构净买卖；不假定用户持仓。
