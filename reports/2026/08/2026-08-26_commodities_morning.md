# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-26

> revision: 3  
> generated_at_bjt: 2026-08-26T09:13:00+08:00  
> data_protocol_version: china_commodities_v2_night_session  
> 本次为09:00后修订版：使用正式夜盘snapshot，不使用仓库中不存在的09:00后分钟/逐笔日盘数据；所有盘中触发条件均理解为“若尚未触发”。

## 一、今日一句话结论

**正式夜盘层进一步分化信号：V2701、FG701均价跌仓增，是仅有的70+条件空；EG2610夜盘-3.93%却继续增仓，恢复多头再降级；FU2611-5.01%同时减仓，更像去杠杆，禁止追空。**

与revision 2最大的区别，不是夜盘方向被改写，而是现在有了可审计的夜盘OHLC、volume、OI和时间戳：V/FG的弱势得到夜盘价仓继续确认；EG的大跌不是简单long liquidation，因为OI反而增加；FU则是价格大跌同时OI明显下降，更接近去杠杆线索。价仓归因仍只叫“线索”，不把它写成确定的新空/多头止损事实。

## 二、数据质量与覆盖说明

中国EOD基线仍是2026-08-25完整交易日：五所SHFE/INE/DCE/CZCE/GFEX、803个期货合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0。Market State保留同合约1D/3D/5D/20D、RV20、EOD OI和curve，夜盘层明确`daily_metrics_unchanged=true`，因此没有用夜盘价格污染日线收益。

新增正式夜盘层 `data/night_session/latest.json`：`trading_date=2026-08-26`、`night_session_date=2026-08-25`、生成于08:44:07 BJT，`data_fresh=true`、`validation_passed=true`、`published=true`。803个选定合约中610个得到有效夜盘记录，覆盖率75.9651%；missing price/timestamp/query error均为0。session窗口为8月25日20:00至8月26日03:45，来源为iFinD HTTP real_time_quotation。09:00 bot rebuild后，夜盘摘要已投影进last_run_status/latest/market_state/radar/contract_meta/report_input等下游产物，同时保持与EOD分离。

Physical原生覆盖仍只有4/20。FG使用最新周度企业库存；EG、PVC实体确认来自明确标注的商业产业数据，不冒充交易所仓单。JM basis仍为C级context，不计方向评分、不称套利。

Options流水线也在今早补全：8月25日期权共23,046条，64/64品种成功、386个series，IV coverage约98.63%、OI coverage约68.79%，`full_chain_verified=true`；但bid/ask coverage仍为0，`execution_ready=false`。今天已是8月26日，因此这些Options仍是T-1研究背景，不能计今天fresh evidence，也不能报净权利金、滑点或Dealer Gamma方向。所有结构统一遵守：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

Contract Metadata仍partial，DCE动态字段不足、GFEX部分字段不完整；V/EG等合约的当前动态交易所保证金、broker margin和price limit必须下单前复核。

## 三、商品仪表盘

| 板块 | 合约 | 8/25 EOD Close/Settle | EOD状态 | 正式夜盘Close / OI | 夜盘相对EOD结算 / OI变化 | Curve / Physical | 判断 |
|---|---|---:|---|---:|---:|---|---|
| 塑化 | **V2701** | 4539 / 4576 | 1D -2.08%，5D -3.48%，EOD ΔOI **+18.14%** | **4523 / 1,192,679** | **-1.16% / +1.76%** | 夜盘主次约-0.79% Contango；PVC库存同比+37.49%，下游开工39.18% | **第一优先：反弹失败空** |
| 建材 | **FG701** | 913 / 916 | 1D -0.76%，20D -4.98%，EOD ΔOI +1.90% | **911 / 1,524,683** | **-0.55% / +1.08%** | EOD Contango约-3.34%；厂库同比+17.41% | **第二优先：反弹失败空** |
| 能化 | **EG2610** | 5364 / 5497 | 1D +3.25%，5D +10.69%，EOD ΔOI +5.27% | **5281 / 365,568** | **-3.93% / +1.14%** | EG2611夜盘4996，Back约+5.70%；港库20.6万吨、低位 | **紧结构与最新价仓冲突，降级观察** |
| 能源 | **FU2611** | 3842 / 3935 | 1D +2.96%，5D +6.27% | **3738 / 270,745** | **-5.01% / -5.63%** | FU2612夜盘3552，主次仍Back约+5.24%；Hormuz尾部未消失 | **去杠杆线索，不接刀也不追空** |
| 贵金属 | **AG2610** | 16631 / 16775 | 1D -0.65%，5D +4.22%，EOD ΔOI -5.37% | **16751 / 276,032** | -0.14% / **-2.20%** | PCE前事件Vega；T-1上行vol仍贵 | No-Trade |
| 有色 | **CU2610** | 107980 / 108160 | 1D +0.38%，EOD ΔOI +6.60% | **108700 / 210,379** | **+0.50% / +2.90%** | 价格/OI强，但LME/COMEX区域库存迁移扭曲明显 | 强但不追 |
| 新能源 | LC2701 | 150280 / 153960 | 1D -3.79%，5D -0.89% | **无合格完成夜盘记录** | — | GFEX观测落在正式夜盘窗口外；不据此称夜盘涨跌 | 不称短缺/不追空 |
| 建材 | SA701 | 1045 / 1046 | 1D -1.04% | 有夜盘层但无前三优势 | — | Contango约-3.26% | 弱但edge不足 |
| 农产品 | RM611 | 2243 / 2236 | 1D -0.18% | 有效覆盖按品种 | — | 近期price/curve冲突 | No-Trade |
| 航运 | EC2610 | 1894 / 1946.5 | 1D -1.49%，5D +10.91% | 非普通夜盘curve框架 | — | 地缘运输风险双向 | 不追极端动量 |

## 四、相比上一交易日/上一revision真正变化

**1. V的空头确认质量进一步提高。** 日盘已经是价格下跌、OI单日+18.14%、Contango；正式夜盘又收4523，较EOD结算-1.16%，OI从1,172,046升至1,192,679，即夜盘再增约1.76%。这仍只能叫“价跌仓增线索”，但说明弱势并未在夜盘被明显回补。

**2. FG同样得到夜盘价仓继续确认。** 夜盘911、较结算-0.55%，OI较EOD再增约1.08%。结合EOD Contango和高同比厂库，FG从76分上调到78分；但低绝对价格、亏损和冷修反身性使它仍弱于V。

**3. EG恢复多头再降一级。** 夜盘5281、较EOD结算-3.93%，而OI反而从361,462增至365,568，约+1.14%。这与“单纯多头止损后就容易V形恢复”并不一致；同时2610-2611仍约5.70% Back、商业港库仍低，说明它是**最新price/OI与curve/Physical正面冲突**，不是干净空头，也不是立即可买的低库存多头。

**4. FU与EG不同：FU更像去杠杆线索。** FU2611夜盘3738、较结算-5.01%，OI却较EOD下降约5.63%；2611-2612仍约5.24% Back。价格大跌+OI下降与地缘风险溢价快速回吐一致，所以追空的赔率反而更差：一旦Hormuz headline反转，低仓位后的反抽可能很急。

**5. Options数据质量变好，但交易执行质量没有变好。** 品种覆盖从此前不完整补到64/64，合约23,046条；但今天仍是T-1，且bid/ask=0、execution not ready，所以它提高研究置信度，不提高今天精确下单能力。

## 五、产业链地图

**最值得交易的弱链：PVC—地产建材。** V同时具备EOD价仓、正式夜盘价仓、Contango、高同比库存和低下游开工。最大的反证是库存周环比仍-1.31%、绝对价格很低、产业亏损可能促使供应收缩，因此只做反弹失败，不做低位加速追空。

**次弱：浮法玻璃。** FG价跌仓增在EOD和夜盘都延续，Contango和厂库同比高17.41%支持结构空；但周度库存仅微降0.07%，不是“持续累库”，而且低价冷修风险高于PVC，所以赔率稍差。

**实体最紧但当前最矛盾：乙二醇。** 低港库和5.7%左右Backwardation说明tightness真实；夜盘大跌且OI增加又说明市场愿意在更低价格继续建立风险。当前最有信息量的不是再讲库存故事，而是日盘能否重新接受5350/5400以上。

**能源：去风险，不是安全追空。** 国内FU夜盘与海外原油方向一致向下，但Hormuz通航、制裁和油轮安全仍构成反向跳升尾部。FU价格下跌同时减仓，使“继续追空”缺乏价仓确认。

**有色/贵金属：事件等待。** CU夜盘价涨仓增很强，但LME接近纪录高位且COMEX库存迁移受潜在美国关税驱动，不能简单称全球物理短缺；AG则继续在PCE前降低OI，方向性交易要让位给20:30宏观事件。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段 | Fresh独立层 | 主要惩罚 |
|---:|---|---:|---|---|---:|---|
| 1 | **V2701 反弹失败空** | **79** | 空 / 1–5D | 条件试仓 | **3** | 周度仍小幅去库；Options T-1；DCE动态参数缺 |
| 2 | **FG701 反弹失败空** | **78** | 空 / 1–5D | 条件试仓 | **3** | 低价供应收缩/short squeeze；动态参数需复核 |
| 3 | EG2610 价格恢复多头观察 | 68 | 多观察 / 1–2D | 观察 | 3层可用但方向冲突 | 夜盘价跌仓增与tight curve/physical冲突 |
| 4 | CU2610 高位强势但不追 | 67 | 观察 / 1–3D | 观察 | 2 | 区域库存/关税扭曲；PCE风险 |
| 5 | FU2611 去杠杆后双向观察 | 66 | 观察 / Intraday–2D | 观察 | 2 | 大跌但减仓；地缘上行尾部仍在 |

今天仍没有80+确认加仓交易。夜盘数据让V/FG更接近80，但三层证据并不足以绕过低价供给反身性和动态参数缺失。

## 七、前三名交易卡

### 1. V2701｜79分｜反弹失败空

**事实：** EOD结算4576，1D -2.08%、5D -3.48%，EOD ΔOI +18.14%；正式夜盘close 4523、较结算-1.16%，夜盘OI 1,192,679、较EOD再+1.76%；主次夜盘约-0.79% Contango。PVC华东+华南社会库存117.92万吨，周环比-1.31%、同比+37.49%，下游开工约39.18%。

**市场已经定价：** 弱地产需求和高库存。**可能错在：** 库存压力持续时间和供应恢复仍被低估。**反证：** 行业亏损、成本支撑、库存确实仍在缓慢去化。

**若盘中尚未触发：** 等反弹到4525–4555区域失败，并重新落到4518/VWAP下方，先空1/2；跌破4490且OI没有快速塌缩、Contango未明显收窄，再加1/2。若已经直接跌到4490以下而没有反抽，不追，等30–45分钟反弹。

**止损/失效：** 4625上方形成15分钟接受；稳定站上4660，同时库存去化明显加快、下游开工/订单持续回升、curve收窄，则逻辑失效。**TP1/TP2：4450 / 4320；时间止损3个交易日。** 初始最大损失0.30%–0.45% NAV。

DCE PVC 5吨/手、tick 1元/吨、tick value 5元/手；按夜盘4523，notional约22,615元/手。当前动态exchange margin、broker margin和price limit未确认，交易前复核。若需要有限损失表达，等8月26日fresh quote后再比较Put Spread；不报权利金。

### 2. FG701｜78分｜反弹失败空

**事实：** EOD结算916，1D -0.76%、20D -4.98%，EOD ΔOI +1.90%，curve约-3.34% Contango；正式夜盘close 911、较结算-0.55%，夜盘OI 1,524,683、较EOD再+1.08%。周度样本厂库7441.4万重箱，环比-0.07%、同比+17.41%，库存天数34.1天。

**若盘中尚未触发：** 912–920反弹失败并重新跌回910/VWAP下方先空1/2；跌破900且OI不快速流失再加。若已经直接跌到895以下，不追，等反抽。

**止损/失效：** 934上方15分钟接受；curve持续收窄/翻Back，同时厂库加速去化、深加工订单改善或冷修明显超预期，则退出。**TP1/TP2：895 / 875；时间止损3个交易日。** 初始最大损失0.25%–0.40% NAV。

CZCE玻璃20吨/手、tick 1元/吨、tick value 20元/手；按夜盘911，notional约18,220元/手。当前动态保证金/涨跌停正式下单前复核。fresh quote后Put Spread可作为有限风险替代。

### 3. EG2610｜68分｜只保留恢复多头观察

**事实：** EOD结算5497，1D +3.25%、5D +10.69%，EOD ΔOI +5.27%，EOD主次Back约6.26%；华东主港商业库存20.6万吨。正式夜盘close **5281**、较结算**-3.93%**，夜盘OI **365,568**、较EOD**+1.14%**；EG2611夜盘4996，主次Back仍约**+5.70%**。

这组数据不支持“低库存所以直接抄底”，也不支持“跌4%所以追空”。真正的edge只能来自**价格重新接受紧结构**。

只有在至少45分钟后，5250–5300区域被吸收，价格先收复5350、再站上5400/VWAP，同时Back仍大致≥5%、油价停止下跌，才允许≤0.25% NAV探索多头。若触发后5220下方形成15分钟接受先止；5200进一步失守、Back明显压缩且Physical也转松，逻辑失效。TP1 5500、TP2 5650；1–2D不延续退出。

DCE EG 10吨/手、tick 1元/吨、tick value 10元/手，夜盘5281对应notional约52,810元/手。动态margin/limit未确认。期权只在标的恢复后研究Call Spread。

## 八、商品期权专项

本期Options日期仍是8月25日，因此只能称**T-1研究面**。流水线已改善至23,046合约、64/64品种、386 series、IV coverage约98.63%、OI coverage约68.79%；但bid/ask coverage=0、execution_ready=false。

代表性8/25 surface显示：V2701 ATM IV此前约18.47%而RV20约11.64%，看空若确认应优先比较Put Spread而非裸买昂贵Vega；EG2610 ATM IV约40.30%而RV20约35.20%，当前方向冲突不值得提前付事件Vega；AG在PCE前也不适合裸追高IV Call。

所有结构均为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。禁止虚构bid/ask、净权利金、滑点、精确Greeks和Dealer Gamma方向。

## 九、9:00后风险地图

本报告生成时中国日盘已经开市，但仓库没有09:00后的分钟/逐笔流，因此不把任何未验证盘中走势写入报告；以下全部是**如果条件尚未触发**的处理框架。

- **V2701：** 夜盘4523且继续增仓。最优不是低位追空，而是4525–4555反弹失败后再失守VWAP；直接<4490先等反抽。
- **FG701：** 夜盘911且继续增仓。912–920失败反弹是高信息形态；直接<895不追。
- **EG2610：** 夜盘5281且下跌中增仓，强制按45分钟级别看恢复；5350/5400不能收复则不做多。
- **FU2611：** 夜盘3738且OI明显下降，更像去杠杆线索；既不接第一刀，也不在Backwardation+地缘尾部下追空。
- **AG/CU：** PCE/GDP前降低对昨日趋势的信任，异常波动等30–45分钟；CU不追历史高位beta，AG不裸买事件Call。
- **LC/PS：** 正式night snapshot里的GFEX观测落在完成夜盘窗口外，本期不声称夜盘收盘；只用EOD结构判断。

## 十、未来24小时 / 7日事件

**8月26日20:30 BJT：美国7月PCE/Personal Income and Outlays，以及二季度GDP Second Estimate和Corporate Profits。** 对DXY、实际利率、AU/AG、CU及Vega是一级事件；事件前降低裸Delta/Vega。

**8月26日22:30 BJT：EIA Weekly Petroleum Status Report。** 对SC/FU/LU/BU和化工成本链是一级Delta事件；能源今天已经经历大幅夜盘去风险，更不宜在EIA前放大裸仓。

**8月27–29日：Jackson Hole Economic Policy Symposium。** 美元、利率敏感商品进入高Vega窗口。

**8月29日03:30 BJT：CFTC COT。** 只作滞后拥挤背景，不当实时flow。

持续非定时风险仍是Hormuz临时通航、扫雷、制裁执行和油轮安全。当前能源price trend向下，但上行地缘尾部仍很大，有限风险凸性优于大仓裸Delta。

## 十一、风险预算与行动清单

V初始最大损失0.30%–0.45% NAV；FG 0.25%–0.40%；EG只有价格恢复触发后才允许≤0.25%。V+FG+SA属于同一地产/建材需求因子，初始合并风险建议≤0.75% NAV；EG+FU+SC+LU+BU合并计算能源/地缘因子。今天没有80+确认交易，不启用0.75%–1.50%的确认仓预算。

A. 今天没有应立即追单建立的新仓位。  
B. 若盘中尚未触发，只做V2701反弹失败空、FG701反弹失败空；不在低位直接追。  
C. 继续观察EG2610收复5350/5400的恢复多头、CU2610高位强势、FU2611去杠杆后的承接。  
D. 避免追空FU/EG大gap、追LME铜、裸买PCE前贵金属高Vega、以及任何C/D级basis或context-only跨境套利。

## 主要来源

- China-Commodities-Engine night session: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json
- China-Commodities-Engine night status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json
- China-Commodities-Engine status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json
- China-Commodities-Engine market state: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json
- China-Commodities-Engine options quality: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json
- Reuters，2026-08-25，Oil settles down more than 3%: https://www.reuters.com/business/energy/oil-prices-steady-investors-weigh-impact-expanded-us-sanctions-against-iran-2026-08-25/
- Reuters，2026-08-25，Iran and Oman discuss temporary Hormuz corridor: https://www.reuters.com/world/china/iran-oman-discuss-temporary-hormuz-corridor-impasse-with-us-drags-2026-08-25/
- Reuters，2026-08-25，US tariff threat upends copper surplus: https://www.reuters.com/business/us-tariff-threat-upends-copper-surplus-prices-test-all-time-peak-2026-08-25/
- Reuters，2026-08-26，Gold little changed with US inflation data in spotlight: https://www.reuters.com/world/india/gold-little-changed-with-us-inflation-data-spotlight-2026-08-26/
- 浮法玻璃库存: https://www.mysteel.com/oilchem/a/26082016/2D4AB63D4A779922.html
- PVC库存/需求: https://goodsfu.10jqka.com.cn/20260821/c679170626.shtml
- EG港口库存: https://finance.sina.com.cn/money/future/fmnews/2026-08-24/doc-inipkzxw2942246.shtml
- BEA: https://www.bea.gov/news/schedule/
- EIA: https://www.eia.gov/petroleum/supply/weekly/index.php
- Kansas City Fed Jackson Hole: https://www.kansascityfed.org/research/jackson-hole-economic-symposium/
- CFTC COT schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
