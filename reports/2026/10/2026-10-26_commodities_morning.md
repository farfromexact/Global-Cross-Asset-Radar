# 商品期货期权晨间雷达｜2026-10-26

> 信息截点：2026-10-26 06:51:10（北京时间）；生成时间：07:08:36。最新完整中国日盘为10月23日；周五夜盘合法归属10月26日。下一窗口09:00，EC为09:30。仅研究，不下单，不假定成交或持仓。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；油价周日晚回吐、铜对罢工反应平淡，SC/FU只保留严格回踩候选，AG等反抽失败。**

- 优势不足：AL、Y、AP、LC、EC没有跨层闭环。
- 等待条件/报价：SC2612、FU2701、AG2612；MA701仍是研究闸门。
- 数据不足：聚合输入与Night raw均为0字节；DCE官方核验HTTP 412；214个Night合约query_error/unresolved；期权bid/ask=0；全部18条可读basis仅C级。
- 最有价值的三项验证：09:15油链是否在Brent重回114时保留近月升水；CU是否出现价格—曲线共振；AG是否先反抽再失败。

## 2. 数据质量、覆盖与事实台账

| 模块 | 实际取得 | 能力与限制 |
|---|---|---|
| 聚合输入 | report_input_latest.json 0字节；night_session/latest.json 0字节 | 聚合层故障；不等于底层全无，但限制本期同源重建与Night准确合约复核 |
| Futures | 10/23五所806合约、77产品；核心63/63；日期匹配100% | full_market_ready=true、critical=0；5个placeholder隔离；非五所官方全认证 |
| Market State | 77产品、20交易日、exact-contract | 不拼接不同主力 |
| Physical | 20目标、18有效、SC/LU不可用 | 18条basis均C级、0项eligible；不能计方向或套利 |
| External | 22目标、17有效、5不可用 | repo仅context；07:00另用公共延迟报价 |
| Night | T=10/26；416/806、37产品；51.61% | fresh/validated/published但不完整；214错误/未解析；vendor snapshot、非官方收盘；raw当前为空 |
| Options | 64目标、46尝试、45成功；1050合约 | ATM 44、skew 26；surface/positioning/execution=0；bid/ask=0 |
| Crosscheck | SHFE238、INE63、CZCE243、GFEX48；价格different=0 | DCE HTTP412；volume/OI未核 |
| Metadata | effective match 73.45%；静态参数30.15% | partial；动态保证金/限幅待开盘核 |
| Stock | 10/21报价、10/22研究；5576/5568 | 复权/行业/执行未就绪；限定补证0条决策级新增 |

完整初筛覆盖黑色、金属、能源化工、新能源、农产品和EC，并含实际动态新增。黑色无三层共振；油化工Night广泛计价但周日晚外盘回吐；铜有罢工无价格确认；Y价仓偏强但DCE核验缺失；LC/EC高波动且缺实体与同窗外部证据。

| fact_id | 关键事实 | 时间/口径 | 直达源 | 局限 |
|---|---|---|---|---|
| F-001 | China-Commodities-Engine 的 report_input_latest.json 与 night_session/latest.json 本次读取均为0字节；模块状态、EOD、Market State、Options、Physical、External、Crosscheck仍可独立读取。 | 2026-10-26T07:08:36+08:00 | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) | 聚合层故障不等于底层数据全无；但限制同源重建与Night准确合约复核。 |
| F-002 | 10月23日EOD覆盖五所806合约、77产品，source_date_match 100%，full_market_ready=true，critical=0；5个placeholder隔离。 | 2026-10-23 EOD; generated 2026-10-26 05:58:46 BJT | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) | vendor全市场就绪不等于五所官方认证。 |
| F-003 | 周五夜盘合法归属10月26日：416/806合约、37产品；fresh/validated/published但coverage_complete=false，214个query_error/unresolved。 | 2026-10-23 21:00—2026-10-24 02:30 BJT | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) | vendor快照，非官方夜盘最终收盘；raw latest当前为空。 |
| F-004 | SC2612 EOD 724.9/717，1D +2.14%、5D -0.83%、RV20 49.45%；前序归档Night快照744.4、较close +2.69%。 | EOD 2026-10-23; archived snapshot 2026-10-24 02:30 BJT | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json) | Night准确值为前序归档事实，未由当前空raw文件重读。 |
| F-005 | WTI Dec 2026延迟报价102.05美元/桶，较结算103.27下跌1.18%。 | 2026-10-26 06:50:02 BJT | [源](https://www.google.com/finance/quote/CLZ26:NYMEX) | 公共延迟报价，不是可执行或交易所认证实时报价。 |
| F-006 | COMEX铜Dec 2026为6.51美元/磅、近乎持平；COMEX银Dec 2026为54.26美元/盎司、上涨0.59%。 | 2026-10-26 06:50—06:51 BJT | [源](https://www.google.com/finance/quote/HGZ26:COMEX) | 延迟公共报价；不同品种时间戳略有差异。 |
| F-007 | Teck确认Highland Valley Copper罢工开始并降负荷运行，产量影响取决于持续时间，尚无可用损失吨数。 | 2026-10-25 | [源](https://www.teck.com/news/news-releases/2026/strike-commences-at-highland-valley-copper) | 公司未量化损失，铜价又未显著响应。 |
| F-008 | Options 64目标、45成功；ATM ready 44、skew ready 26，surface/positioning/execution均为0，bid/ask覆盖为0。 | 2026-10-23 | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) | 计划采样完成不等于完整期权链。 |
| F-009 | Physical 20目标中18项原生频率有效，但全部basis仅C级、0项eligible；SC/LU不可用。 | 截至2026-10-23 | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json) | 不能作为方向或套利确认。 |
| F-010 | Stock引擎停留10月21日报价/10月22研究；限定检查油企与紫金矿业未发现截点前新的决策级经营披露。 | 2026-10-26T07:08:36+08:00 | [源](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json) | 映射目录不完整、执行能力未就绪。 |

## 3. 市场仪表盘

| 合约 | EOD close/settle | 1D/5D；RV20；ΔOI | Night/曲线 | 07:00海外/Options | 信号 |
|---|---:|---|---|---|---|
| SC2612 | 724.9/717 元/桶 | +2.14%/-0.83%；49.45%；ΔOI +611 | 744.4；+2.69% vs close；前序归档snapshot；EOD 2611-2612 +1.02%；前序归档2612-2701 Night 1.38% | WTI102.05，-1.18%；Brent约115.55，-1.00%指示；ATM IV64.89%，IV-RV +15.44pct；不可执行 | 旧多头门槛失效：Brent<114，不追 |
| FU2701 | 5139/5028 元/吨 | +4.49%/+5.41%；48.81%；ΔOI +20124 | 5349；+4.09%；前序归档snapshot；EOD 2611-2612 +12.70%；旧卡2701-2702 Night 4.74%待重核 | 油价周日晚回吐；ATM IV64.36%，IV-RV +15.55pct；不可执行 | 只观察回踩；同月曲线未重核 |
| MA701 | 3219/3197 元/吨 | +1.43%/+0.31%；37.95%；ΔOI -45882 | 3389；+5.28%；前序归档snapshot；模块可读MA611-612 +6.29%；非701-702 | 原油仅间接代理；MA612错月ATM IV42.82% | 研究闸门，不执行 |
| PX612 | 9576/9462 元/吨 | +1.52%/+0.40%；33.70%；ΔOI +4655 | 9974；+4.16%；前序归档snapshot；同月pair未本次重核 | 油价成本冲击回吐；10/28到期，ATM IV28.42%<RV；旧moneyness失真 | 不追近到期gamma |
| TA701 | 6542/6502 元/吨 | +1.25%/+0.25%；30.62%；ΔOI -12387 | 6762；+3.36%；前序归档snapshot；同月pair未本次重核 | 成本端回吐；同月执行报价缺失 | 待需求确认 |
| BU2701 | 4650/4600 元/吨 | +2.27%/+2.91%；33.85%；ΔOI +7607 | 4766；+2.49%；前序归档snapshot；模块近远月待同窗重核 | WTI回落；ATM IV37.28%；不可执行 | 验证油链广度 |
| AL2612 | 23350/23200 元/吨 | +0.04%/+1.33%；11.20%；ΔOI +1695 | 23575；+0.96%；前序归档snapshot；EOD 2612-2701 +1.27% | 07:00无独立LME实时核；ATM IV10.53%，RR25 -2.40pct | 结构尚可，催化不足 |
| CU2612 | 107900/107310 元/吨 | -0.71%/-1.34%；12.01%；ΔOI +2167 | 108370；+0.44%；前序归档snapshot；EOD近远月 +0.76% | COMEX铜6.51，近乎持平；HVC罢工；CU2611今到期，错月 | 新闻未获价格确认 |
| AG2612 | 13108/13255 元/千克 | -4.16%/-4.56%；33.61%；ΔOI +44 | 13116；+0.06%；前序归档snapshot；EOD轻贴水 -0.19% | COMEX银54.26，+0.59%；ATM IV40.65%，IV-RV +7.03pct | 反抽失败空头等待，外盘反弹为反证 |
| Y2701 | 9125/9080 元/吨 | +1.53%/+2.78%；11.45%；ΔOI +49944 | DCE未核；EOD -0.88% | 油脂仅context；局部研究，执行0 | 价仓偏强但官方核验缺口 |
| AP701 | 5725/5726 元/吨 | -0.07%/-6.07%；25.42%；ΔOI -16109 | 无可用当前raw复核；AP611-612 +9.13%；仅4观测 | 不适用；ATM IV31.64%，RR25 -6.72pct | 等级/移仓噪声风险 |
| LC2701 | 97280/93800 元/吨 | -0.74%/-5.33%；38.31%；ΔOI -10445 | 制度无夜盘；未形成有效同窗曲线 | 锂价外部映射不足；ATM IV52.68%，skew不可用 | 高波动、期权偏贵 |
| EC2611 | 2443/2432 | -0.80%/-11.69%；42.53%；ΔOI -2434 | 制度无夜盘；EOD -8.98% contango | 黑海与中东航运风险；无 | 趋势与地缘尾部冲突，回避 |

公共延迟报价显示：[WTI Dec 2026](https://www.google.com/finance/quote/CLZ26:NYMEX) 06:50为102.05美元、较结算跌1.18%；[COMEX铜](https://www.google.com/finance/quote/HGZ26:COMEX)近乎持平；[COMEX银](https://www.google.com/finance/quote/SIZ26:COMEX)升0.59%。这些不是可执行盘口。

## 4. 相比前序的真变化

1. 油价没有延续周末风险溢价：WTI回到102.05，SC/FU原Brent≥114门槛当前不满足，评分各降2分。
2. [Teck确认HVC罢工](https://www.teck.com/news/news-releases/2026/strike-commences-at-highland-valley-copper)，但没有损失吨数，COMEX铜近乎持平；CU维持58分观察。
3. Night日历合法，但本次raw文件为空；已归档744.4/5349/3389等只能标“前序归档快照”，不能冒充本次重读或官方收盘。
4. AG旧idea_id名称与实际空头正文冲突；本期保留父ID并新建子ID COM-M-AG2612-FAILED-REBOUND-SHORT-20261026，避免重置历史。
5. 油企和紫金矿业限定补证没有新增产量、库存、裂解、套保或量化停产事实，Stock不改变方向或排名。

## 5. 产业链传播与公司利润桥

| 链条 | 方向与强弱 | 最大反证/缺失 | 置信度 |
|---|---|---|---|
| 中东供应/运输→Brent/WTI→SC→FU/BU→PX/TA/MA | 周五Night油化工最强；周日晚海外回吐 | SC/LU实体不可用、全部basis仅C级 | 中 |
| HVC罢工→LME/COMEX铜→CU/BC→冶炼/矿股 | 新闻支持上游紧张 | 铜价未确认、无损失吨数 | 中低 |
| 美元/实际利率→AU/AG | 国内AG趋势弱 | COMEX银反弹、FOMC尾部 | 中 |
| 油脂→Y/P→养殖 | Y价仓偏强 | DCE Night和官方核验缺口 | 低 |
| 黑海/中东航运→运费→EC | 地缘尾部上升 | EC趋势弱、运价不同窗 | 低 |

股票利润桥：上游油企受油价、产量、长协、汇率、税费和套保共同影响；炼化企业还受裂解价差、库存损益和传导滞后影响；紫金矿业混合铜、金、销量、汇率和资本开支。没有新经营数字时，直接商品表达更纯，但当前同样未满足执行门槛。

## 6. 统一机会榜

| 排名 | idea_id | 方向/期限 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 支持/反对层 | 三轴状态 |
|---:|---|---|---:|---:|---|---|
| 1 | COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021 | 多；1—5D | 22/15/18/15/4 | 74 | 1/2/4/5 | priority / three_layers_but_report_input_and_raw_night_empty / not_ready_Brent_below_114_and_sequence_unmet |
| 2 | COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022 | 多；1—5D | 21/14/17/15/5 | 72 | 1/2/4/5 | priority / three_layers_but_exact_2701_2702_curve_not_revalidated / not_ready_Brent_below_114 |
| 3 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 | 多；1—3D | 18/15/14/13/5 | 65 | 1/2/3/5 | watch / two_layers / not_ready_wrong_month_options_and_no_eligible_physical |
| 4 | COM-M-AG2612-FAILED-REBOUND-SHORT-20261026 | 空；1—5D | 19/16/14/12/3 | 64 | 1/2/4/5 | watch / two_layers; COMEX silver rebound is counterevidence / not_ready_wait_rebound_failure |
| 5 | COM-M-AL2612-CURVE-LONG-WATCH-20261024 | 多；3—10D | 18/14/12/12/5 | 61 | 1/2/5/3/4 | watch / three_layers_but_weak_catalyst / not_ready |

分数均已重新加总且不超25/25/20/15/15；它是研究优先级，不是胜率。没有80分以上候选。

## 7. 三张条件研究卡

### SC2612｜74分

- 新事实：WTI已回落，旧Brent≥114门槛当前不满足；Night raw为空。
- 触发：仅10月26日，09:15价格≥742、Brent≥114、2612-2701升水≥1.20%；之后必须先回踩738—744，再出现5分钟收盘≥746。
- 入场744—748，30%/70%；开盘≥760或无回踩直接上冲放弃。止损732；Brent<110或升水<0.70%持续15分钟失效。
- TP1 766、TP2 788；10月30日14:45退出。744/746/748入场到TP1毛R约1.83/1.43/1.13；费用/滑点未知，不按0处理。
- [INE规格](https://www.ine.cn/eng/products/sc/contract/)：1000桶/手、tick0.1元=100元/手。动态保证金/限幅、到期与roll开盘前重核。
- SC2612 11/12 ATM720 IV64.89%，高RV15.44pct；无bid/ask，不称期权便宜或结构可执行。

### FU2701｜72分

- 触发：先回踩5300—5350，再5分钟收盘≥5360，同时2701-2702升水≥4.50%、Brent≥114。
- 入场5350—5380，40%/60%；首个可成交≥5420或价差<4%放弃。止损5190；价差<3.5%持续15分钟或Brent<110失效。
- TP1 5600、TP2 5850；10月29日14:45退出。5350/5365/5380入场到TP1毛R约1.56/1.34/1.16。
- [SHFE规格](https://www.shfe.com.cn/eng/Market/Futures/FuelOil/Contract/)：10吨/手、tick1元=10元/手。当前2701-2702同窗曲线尚未从raw重核，因此执行未就绪。
- FU2701 12/18 ATM5000 IV64.36%，高RV15.55pct；无bid/ask。

### AG2612｜64分｜父idea方向修订

- 父ID COM-M-AG2612-SILVER-REPAIR-LONG-20261021保留；新子ID只表达“反抽失败后空”。
- 触发：09:15反抽13580—13620后收于13600下方，同时银≤55；09:30前再次收于13480下方。
- 入场13460—13480；直接低开<13420不追。止损13720；TP1 13100、TP2 12600；10月30日退出。
- 13480空、成本6点：计划风险约3690元/手，TP1约1.52R、TP2约3.55R。
- [SHFE规格](https://www.shfe.com.cn/eng/Market/Futures/Silver/Contract/)：15千克/手、tick1元=15元/手。COMEX银+0.59%是反证，不满足即时空头。
- AG2612 11/24 ATM13300 IV40.65%，高RV7.03pct；无执行报价。

## 8. 商品期权专项

10月23日core_v1 sampled_strikes覆盖45/64产品、1050合约；ATM ready44、skew ready26；完整曲面、positioning、execution均为0，dealer gamma方向未知。

- SC IV64.89% vs RV49.45%（+15.44pct）；FU IV64.36% vs RV48.81%（+15.55pct）。
- AG IV40.65% vs RV33.61%（+7.03pct）；AL IV10.53% vs RV11.20%（-0.67pct）、RR25 -2.40pct。
- PX IV28.42% vs RV33.70%（-5.28pct）、RR25 -2.54pct，但10月28日临近到期且旧moneyness已变。
- AP IV31.64% vs RV25.42%（+6.22pct）、RR25 -6.72pct，只能说明put相对更贵。
- MA期权对应MA612、CU期权对应CU2611，不得替代MA701/CU2612。没有bid/ask不得编权利金、净成本、滑点、PCR、拥挤度或dealer gamma。

## 9. 09:00开盘风险地图

| 层次 | 已知 | 动作 |
|---|---|---|
| Previous China EOD | FU/BU强，AG/LC/EC弱 | 不用10/23结算价追单 |
| Current T Night | 周五Night合法归属10/26，但raw本次为空 | 仅将前序归档快照作价格层观察，不声称官方收盘 |
| 07:00 Overseas | 油回吐、铜平、银反弹 | 削弱油/铜追涨与银追空 |

09:00—09:15只核准确合约与海外；09:15核触发；09:30等回踩/反抽；09:45只有“回踩或反抽→重新收复/失败→曲线保持”顺序完整才保留。SC≥760、FU≥5420直接放弃；AG<13420不追空。EC 09:30开盘，至少等待45分钟。

## 10. 未来24小时/7日事件与行动前缺口

- 10月27日04:00北京时间：[USDA Crop Progress](https://www.nass.usda.gov/Publications/Todays_Reports/reports/prog4226.pdf)。
- 10月28日22:30：[EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/schedule.php)。
- 10月29日02:00/02:30：[FOMC声明与记者会](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)。
- 未来7日继续核Teck罢工损失吨数、中东/黑海运输、油企三季报及CFTC；新闻转述不重复计层。
- 行动前硬缺口：聚合输入修复、Night准确raw、DCE交叉核对、SC/FU/MA动态保证金和限幅、期权bid/ask及新ATM/Delta、SC/LU实体、用户NAV与成交/持仓回执。

归档状态写入后需以六路径回读为准；CI保持pending_or_unverified。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：SC2612、FU2701须Brent重回114且回踩—收复—曲线保持；AG2612只在反抽失败后条件空。  
C. 今天继续观察：MA701油化工留存、CU2612罢工弹性、AL曲线、Y价仓、AP等级/移仓噪声。  
D. 今天必须回避或有条件退出：回避油链高开追涨、低位追空AG、把前序Night快照当本次官方收盘、零bid/ask期权和错月/错pair；若旧计划曾成交，仅按原止损与时间退出管理。