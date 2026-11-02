# 商品期货期权晚间雷达｜2026-11-02

**一句话结论（信息截点：2026-11-02 19:36 北京时间）**：截至本报告时点，无可立即执行的合格新交易；今晚只值得承担MA、CU确认后的条件风险，EC留待明日日盘，原油与白银旧计划均已被海外门槛否定。

> 研究用途，不下单；不假定持仓、触发、成交或盈亏。最近完整中国日盘为2026-11-02；今晚21:00夜盘属于2026-11-03交易日。报告生成时间2026-11-02 19:36 BJT（11:36 UTC）。

## 1. 今晚风险结论

- **可承担但尚未到执行门槛**：MA701强势后的回踩多、CU2612内外盘分歧收敛多；二者都须21:00后用准确合约重验，不能开盘追价。
- **研究存在、下一窗口不在今晚**：EC2612趋势空。EC无夜盘，下一真实窗口为11月3日09:00；缺少同步、可比的欧洲航线现货/指数更新，当前仅有价格与曲线两层。
- **优势已不足**：AG2612虽日盘下跌且2612/2701为轻微contango，但欧洲时段银价反弹至约50.38美元，否定晨报“COMEX银≤49.5”的必要条件；SC、BU多头条件则被Brent约108.5—110美元显著低于113.5/115美元否定。
- **关键数据不足**：合并输入`report_input_latest.json`为空；本次按协议使用同批模块文件。期权无bid/ask、全链、持仓与执行就绪数据；DCE官方价格交叉核对HTTP 412；今晚未来会话尚未发生，不存在可用的“今晚夜盘价”。

最有价值的三项待验证：①21:15后MA701是否守住3520且MA612/701反向价差仍≥2.5%；②21:30后CU2612能否站上108300并把2612/2701反向价差扩至≥0.6%；③11月3日09:15 EC2612跌破2520时，2611/2612 contango是否仍≤-12%且出现可比运价弱证据。

## 2. 数据质量与覆盖

| 模块 | 实际范围与日期 | 能力状态 | 局限/影响 |
|---|---|---|---|
| 合并输入 | `data/report_input_latest.json`，读取0字节 | empty；不可用 | 不把空文件解释为模块无数据；改读同一批次模块文件 |
| Futures | 11月2日，806合约、77产品；SHFE 238、INE 63、DCE 214、CZCE 243、GFEX 48；日期一致率100% | available/published/analytically ready；`full_market_ready=true` | 5个零价量仓占位（JR/PM/RI/WH/ZC）隔离；`official_complete=false`不等于vendor数据失败 |
| Market State | 77产品，20个同合约交易日，1/3/5/20D、RV20、量仓z、near-next | analytically ready | roll pair不作连续可比；价仓象限只作线索 |
| Physical | 20目标、18 fresh、2 unavailable（SC/LU） | available；方向评分仅局部 | 18条basis均为C级，A/B eligible=0；周/月延续不是今日催化 |
| External | 仓库文件仍是10月30日批次，17/22 context-only | stale for 19:36 | 当前Brent/银/铜/DXY改用独立网页时点；不把不同窗口当跨境套利 |
| 历史Night | 归属11月2日，实际开始10月30日、结束10月31日；412/806合约，214 query/unresolved | validated/published但coverage_complete=false | `data/night_session/latest.json`为空；旧会话不是今晚。无准确原始记录，不计正式收益、曲线或证据层 |
| 今晚Night | 应归属11月3日；11月2日21:00开始 | 尚未发生 | `current_night_session_started=false`；`calendar_mismatch=false`；不能要求未来数据或虚构开盘 |
| Options | 11月2日，992记录；44/64产品（68.75%）；44 ATM ready、29 skew ready | core_v1/sampled_strikes可研究 | surface/positioning/execution均0；bid/ask覆盖0；不是完整链。vendor Greeks可读但单位未统一，不能据此给可成交Greeks |
| Crosscheck | SHFE 238、INE 63、CZCE 243、GFEX 48全部可比价格相等；DCE接口HTTP 412 | partial；观察到的价格差异=0 | `all_compared_prices_equal=false`来自源错误，不是已发现差价；量/OI未被官方核对 |
| Contract metadata | SHFE/INE/CZCE当日部分可用；DCE失败，GFEX源日缺 | partial | 候选未知参数不猜；保证金不是风险预算 |
| Stock | 交易日10月30日，research_asof 10月31日10:40 BJT，5571股价状态 | 映射可研究；execution not ready | 复权、行业、指数成分、tradability均缺；11月2日对紫金/宝钢限定公告检索未取得改变商品判断的新经营披露（0条） |

核心路径：[Futures状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[Options质量](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[Options局部曲面](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)、[官方交叉核对](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)。

## 3. 事实台账与12项仪表盘

关键事实台账（价格均为人民币/各合约报价单位，除非另注；读取于19:20—19:36 BJT）：

| fact_id | 标的/口径/观测时间 | 数值与支持判断 | 限局 |
|---|---|---|---|
| F-EOD-1102 | 五所EOD，11月2日15:00后生成 | 806合约、77产品、源日期一致100% | vendor完整不等于五所官方全部认证 |
| F-MA-1102 | MA701 close/settle | 3557/3553；结算1D +2.60%、5D +6.19%；OI +3.07% | 价格与OI同升不能判定“新多” |
| F-MA-CURVE | MA612/701准确同日 | close价差+3.15%，settle价差+2.79% | Market State展示的MA611/612为+0.96%，不同pair不混称 |
| F-CU-1102 | CU2612 close/settle | 107810/107580；结算1D -0.56%、5D -0.55% | 国内价格层反对立即做多 |
| F-CU-CURVE | CU2612/2701同日 | close +0.57%，settle +0.53% | 未达到新计划≥0.6%的确认线 |
| F-EC-1102 | EC2612 close/settle | 2540/2585.5；1D -2.36%、5D -11.62%、OI +8.55% | EC无夜盘；价仓不证明新空 |
| F-EC-CURVE | EC2611/2612同日 | close -12.44%，settle -13.81% | 强contango，但缺同步运价实体层 |
| F-AG-1102 | AG2612 close/settle | 11885/11754；1D -5.01%、5D -9.93%、OI -6.56% | 下跌伴减仓，追空拥挤与反弹风险高 |
| F-OIL-EXT | Brent 11月2日09:53 UTC附近 | 约108.51美元/桶，较前日显著下跌；稍早FT 06:27 UTC为110.03 | 与中国EOD非同一时点，只作21:00映射，不作套利 |
| F-SILVER-EXT | 现货银11月2日09:30 UTC | 50.38美元/盎司、较周五+2.54% | 非COMEX准确合约成交；足以否定“≤49.5”必要条件但不用于盈亏 |
| F-LME-CU | LME 11月2日官方价 | 现金卖价14449、3月卖价14250美元/吨，现金升水约199 | 官方参考价与SHFE收盘窗口不同，只支持紧张映射 |
| F-OPT-1102 | 期权11月2日EOD样本 | CU ATM IV13.16、RR25 -4.73；AG IV45.955、RR25 -4.89 | 无bid/ask、全链与执行就绪，不可称便宜或可成交 |

| 品种/准确主力 | EOD close/settle | 1D/5D结算；RV20 | 量仓/曲线 | Physical/海外/Options | 晚间信号 |
|---|---:|---:|---|---|---|
| MA701 | 3557/3553 | +2.60%/+6.19%；38.57 | OI +3.07%；MA612/701 settle +2.79% | basis C；期权样本为MA612、不可移植 | 等回踩确认，不追高 |
| CU2612 | 107810/107580 | -0.56%/-0.55%；11.03 | OI -1.70%；2612/2701 +0.53% | LME现金升水；ATM IV13.16、RR25 -4.73 | 内弱外紧，等国内确认 |
| EC2612 | 2540/2585.5 | -2.36%/-11.62%；45.80 | OI +8.55%；2611/12 -13.81% | 实体/Options缺 | 次日日盘条件空 |
| AG2612 | 11885/11754 | -5.01%/-9.93%；33.63 | OI -6.56%；2612/2701 -0.12% | 银50.38反弹；ATM IV45.96、RR25 -4.89 | 不追空，旧条件失败 |
| SC2612 | 729.5/745.2 | +2.42%/+0.74%；40.20 | OI -4.23%；2612/2701 +1.33%但roll警告 | Physical不可用；Brent急跌；ATM IV70.53 | 多头旧条件失败，IV偏高 |
| BU2701 | 5199/5276 | +1.38%/+11.36%；31.27 | OI -4.43%；近月曲线+3.53% | BU期权为BU2612；Brent下跌 | 5D过热且外盘反对 |
| SH701 | 1479/1475 | -1.67%/-5.08%；21.44 | OI -3.99%；curve -1.47% | Physical/执行期权缺 | 趋势空观察，证据薄 |
| JD2612 | 3564/3535 | +3.03%/+6.67%；27.57 | OI +0.55%；curve +7.64% | DCE官方交叉核对失败 | 强势但执行降级 |
| RB2701 | 3007/3019 | -0.66%/-0.72%；7.77 | OI +4.83%；curve -1.19% | basis C | 黑色偏弱，赔率不足 |
| AP701 | 5757/5771 | +1.64%/+3.22%；30.66 | OI -3.70%；curve +6.56%但z -2.26 | ATM IV34.43、RR25 -0.17 | 反弹减仓，暂不追 |
| LC2701 | 90700/90500 | +0.49%/-4.66%；40.78 | OI -0.92%；curve +0.71% | basis C；ATM IV54.95、skew不ready | 波动溢价高、方向弱 |
| OI701 | 10167/10236 | -0.57%/-0.96%；11.66 | OI -7.69%；curve +4.73% | ATM IV15.54、RR25 +1.50 | 价格与曲线冲突 |

全范围初筛实际覆盖77产品。板块未入榜结论：黑色/建材除FG放量外整体趋势不强，J/RB价弱但实体A/B basis缺；有色贵金属的AG/AU/SN跌势显著，海外银反弹使追空赔率下降；能源化工呈“油品冲高回落、煤化工/塑化偏强、烧碱偏弱”，Brent下跌是今晚主要外部冲击；新能源LC/PS/SI均缺高质量实体确认；农产品最强JD但DCE官方核对缺，油脂油料缺USDA当期新催化；EC趋势最弱但只有两层。JR/PM/RI/WH/ZC为零价量仓占位，未进入排序，不代表制度上不存在。

## 4. 相比前序报告的真变化与旧观点处置

前序基准：[11月2日晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-02_commodities_morning.md)及[11月1日晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-01_commodities_evening.md)。

1. **SC多头旧计划失效于新入场**：日盘高763.9、低719.4、收729.5；OHLC不能证明“站稳758→回踩750—756→成交”的先后和持续，且19:36前Brent约108.5—110，低于晨报113.5必要条件。`COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030`由71降为观察，不回填成交或止损。
2. **BU多头旧计划失效于新入场**：BU2701高5416、低5126、收5199；不能用穿越5300证明15分钟确认或成交，Brent亦低于115。`COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026`从69降为观察；原参数不后移。
3. **AG空头的外部AND条件明确未满足**：国内日盘大跌、准确AG2612/2701 settle价差-0.12%符合≤0，但银价欧洲时段约50.38，未满足≤49.5。`COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029`由72降至65，状态从重点条件空降为观察；没有持仓回执，实际持仓仍“未提供/未知”。
4. **MA成为国内最强可验证候选**：MA701结算+2.60%、5D+6.19%、OI+3.07%，且MA612/701 settle反向价差+2.79%；但basis仅C、Options标的是MA612、海外油价下跌提供竞争解释，故分数仅由66升至69、仍受两层上限。
5. **铜出现内外分歧**：CU2612结算-0.56%，但LME官方现金对3月升水约199美元/吨、国内近远月仍backwardation。当前更像待验证收敛而非已证实错价；新建研究ID，不包装成跨境套利。

## 5. 产业链与利润传播

| 链条 | 传播与强弱 | 最大反证/缺口 | 置信度 |
|---|---|---|---|
| 原油→SC→BU/FU/LU→化工 | Brent欧洲时段跌约3%—4%，中国日盘SC结算仍+2.42%、BU +1.38%，21:00存在低开/基差重估风险；FU/LU曲线有roll警告 | 仓库External过期，SC/LU Physical不可用；停火谈判标题冲击可能反复 | 中 |
| 煤/气→MA→烯烃/聚酯 | MA701价格、OI、612/701反向价差同向；PP/L/EG 5D亦强 | MA basis C，现货口径不可套利；原油下跌可能削弱油化成本锚 | 中低 |
| 铜矿→LME/SHFE铜→电力/制造 | LME现金升水、海外铜反弹，SHFE CU日盘偏弱且曲线backwardation，形成收敛观察 | 时点、汇率、税运费不齐，不能称跨境套利；国内价格层反对 | 中低 |
| 贵金属去杠杆→AG/AU→矿企 | AG日盘-5.01%、OI下降；海外银反弹+2.54%，更像高波动去杠杆后的反抽风险 | 同一价格冲击不重复计层；期权put skew偏贵 | 中低 |
| 欧线运价→EC→航运利润 | EC2612 5D -11.62%、2611/12 contango -13.81%，趋势仍弱 | 缺同步SCFIS/订舱价与海外运价证据；EC无夜盘 | 中低 |

**Stock利润校验（0个可执行股票候选）**：Stock引擎仅提供10月30日价格状态，复权、行业、tradability均未就绪。限定检索紫金矿业、宝钢股份在上交所/巨潮11月2日公告，未取得改变商品判断的新增经营披露。既有[商品暴露目录](https://github.com/farfromexact/China-Stock-Engine/blob/main/config/company_commodity_exposures.json)只支持：紫金的矿产铜售价可能受铜价正向影响，但销量、单位成本、套保、汇率、少数股东及卡莫阿约束可抵消；宝钢利润取决于钢价相对铁矿/焦煤的真实采购与库存价差。两只股票均混合多因素、当前可交易性未核，作为CU或钢材表达都弱于直接期货，故不进入统一榜单。

## 6. 统一机会榜（上限5，本期5项）

评分顺序为逻辑25/赔率25/催化20/价格曲线波动15/拥挤技术15；总分仅研究优先级，不是胜率。

| 排名 | idea_id / 方向 / 期限 | 分项=总分 | 五层支持/反证 | 研究/证据/执行 |
|---:|---|---:|---|---|
| 1 | `COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024`；条件多；1—5D | 19/16/13/11/10=**69** | 支持1价格量仓、2期限；反对4油价下跌；3 basis C、5错月 | 重点 / 两层上限 / 等21:15 |
| 2 | `COM-M-CU2612-LME-TIGHTNESS-DIVERGENCE-LONG-20261102`；收敛多；2—10D | 19/16/14/11/9=**69** | 支持2曲线、4 LME；反对1国内价格；3非独立官方、5中性偏贵 | 重点 / 两层上限 / 等21:30 |
| 3 | `COM-T-EC2612-TREND-CONTANGO-SHORT-20261028`；条件空；1—5D | 20/17/12/11/8=**68** | 支持1价格量仓、2期限；3/4/5缺失 | 重点 / 两层上限 / 下一日盘 |
| 4 | `COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029`；观察空；1—5D | 18/13/11/13/10=**65** | 支持1跌势、2远月contango；反对4海外银反弹；5 put skew昂贵，OI下降 | 观察 / 两层 / 不追空 |
| 5 | `COM-C-SH701-DOWNTREND-CONTANGO-SHORT-20261102`；观察空；1—5D | 17/14/10/11/10=**62** | 支持1价格、2 contango；OI下降，3/4/5缺 | 观察 / 两层 / 不执行 |

## 7. 三张研究/交易卡

### 卡1｜MA701条件多（稳定idea_id延续）

- **事实/定价/分歧**：close/settle 3557/3553；5D +6.19%、OI +3.07%；MA612/701 settle反向价差+2.79%。市场已定价了国内强势，我们的分歧只在于强价差能否在油价回落时保留；最大竞争解释是煤化工供给/短期挤仓而非终端需求改善。
- **触发（AND且有顺序）**：21:15后MA701≥3580持续15分钟，且同一窗口MA612/701 settle可比口径价差≥2.5%；随后回踩3540—3565并守住3520，才允许研究性试仓。21:00直接高开≥3620不追；任一条件未知即放弃。
- **表达**：首选MA701期货；替代为不交易。MA612期权虽ATM/skew可读，但错月、无bid/ask与execution readiness，不能当作有限损替代。
- **参数**：乘数10吨/手、tick 1元/吨、tick value 10元；仓库保证金9%、限幅8%、最后交易日2027-01-14，但经纪商实际标准需复核。计划止损3505；逻辑失效=MA612/701价差跌破1.5%或MA701 30分钟收于3520下；TP1 3650、TP2 3760；最迟11月6日22:45退出。
- **好/中/坏成交**（假设往返滑点费用合计20元/手，非实报）：3545/3555/3565；到TP1净R约2.45/1.79/1.34，到TP2约5.07/3.90/3.11。计划风险400/500/600元/手，费用后风险420/520/620；跳空和涨跌停可远超计划止损。
- **规模**：手数≤`floor(NAV×单笔风险预算/(每手计划风险+费用))`；只允许0.25%—0.75%试仓，确认后总主题≤1.5%，与PP/L/EG同因子合并。

### 卡2｜CU2612内外紧张收敛多（新研究ID）

- **事实/定价/分歧**：CU2612 close/settle 107810/107580，日跌0.56%；CU2612/2701 settle +0.53%。LME 11月2日官方现金卖价14449、3月卖价14250，现金升水约199美元/吨。国内弱价已定价部分需求疑虑；我们只研究“国内曲线未松、海外现货紧张”能否带来收敛，不称跨境套利。
- **触发（AND且有顺序）**：21:30后CU2612≥108300持续30分钟，CU2612/2701准确价差≥0.60%，且可验证LME 3月价≥14200美元/吨；随后回踩107900—108200守住107600。任何腿不同时可比、USDCNH/税运费突然恶化或高开>109500即放弃。
- **表达**：首选CU2612期货；替代为小额看涨价差仅在取得具体bid/ask和净支出后。当前CU2612期权11月24到期ATM IV13.16、RR25 -4.73、IV-RV约+2.13 vol，不能证明期权便宜，execution ready=false。
- **参数**：交易所标准乘数5吨、tick 10元/吨、tick value 50元；夜盘21:00—01:00；CU2612最后交易日12月15日。当前合约动态保证金/限幅未在同批元数据确认，故不以最低标准做规模。止损107300；逻辑失效=曲线≤0或LME现金升水快速消失；TP1 110000、TP2 112000；11月6日22:45时间退出。
- **好/中/坏成交**（假设往返成本100元/手）：107900/108050/108200；TP1净R约3.35/2.51/1.93，TP2约6.58/5.10/4.11。计划价差风险3000/3750/4500元/手；止损不封顶，实际limit参数未知时不得宣称最大损失。
- **Stock比较**：紫金矿业暴露更分散且当前tradability未核；直接CU更纯、参数更透明。若矿产量/单位成本/套保披露恶化，股票可与铜价背离。

### 卡3｜EC2612趋势contango空（只研究，下一日盘）

- **事实/定价/分歧**：close/settle 2540/2585.5；1D -2.36%、5D -11.62%、OI +8.55%；EC2611/2612 settle -13.81%。趋势和曲线已定价大量弱势，剩余PnL依赖现货运价继续走弱而非单纯技术延伸。
- **触发（AND且有顺序）**：11月3日09:15后EC2612≤2520持续15分钟，EC2611/2612准确contango仍≤-12%，并取得同窗口SCFIS/订舱价或可靠运价弱证据；随后反抽2520—2550失败。09:00低开≤2450不追；实体证据缺失继续观察。
- **参数**：乘数50元/点；2026年5月11日起tick 0.5点、tick value 25元；无夜盘；最后交易/现金交割日2026-12-28。当前已核参考为EC2612 ±20%、一般保证金22%，下单前仍须复核是否有新通知。止损2615；TP1 2400、TP2 2250；11月6日14:45退出。
- **好/中/坏成交**（做空2550/2535/2520，假设往返100元/手）：TP1净R约2.21/1.62/1.22，TP2约4.45/3.45/2.76。计划风险3250/4000/4750元/手；按20%参考限幅，一次反向限幅压力约25855元/手、线性两次约51710元/手，远高于止损计划。
- **工具比较**：无合格商品期权；航运股含运力、燃油、汇率和公司治理，不是EC纯替代。最自然替代是不交易。

## 8. 商品期权专项

样本为11月2日EOD、`core_v1/sampled_strikes`：44/64产品成功，44个series `core_atm_ready`，29个`skew_ready`，但完整surface、positioning、execution均为0；quote coverage complete仅指采样计划完成，不代表全链。无bid/ask，不能编权利金、净成本、滑点或合同限损；样本OI不能推出全链PCR、dealer gamma或拥挤。

| series | 局部ATM IV / RV20 | 局部skew | 研究含义 |
|---|---|---|---|
| CU2612，11/24 | 13.16 / 11.03（+2.13 vol） | RR25 -4.73、BF25 +2.11 | put较贵；多头看涨价差需询价，不称低IV便宜 |
| AG2612，11/24 | 45.96 / 33.63（+12.32 vol） | RR25 -4.89、BF25 +1.49 | 下行保护昂贵；追买put赔率受损 |
| SC2612，11/12 | 70.53 / 40.20（+30.33 vol） | RR25 +6.20、BF25 +1.49 | 极高事件溢价、calls更贵；不卖裸波动，不把高IV等同必跌 |
| LC2701 | 54.95 / 40.78（+14.17 vol） | skew not ready | 仅ATM可读，不能外推翼部或期限 |
| OI701 | 15.54 / 11.66（+3.88 vol） | RR25 +1.50 | 局部call偏贵；无执行报价 |
| MA612，11/11 | 50.61 / 不可比 | RR25 +1.21、BF25 +3.05 | 标的是MA612，不能移植到MA701交易卡 |

跨期/wing/全链、持仓、dealer gamma均不可用。今晚若标的大幅跳空，历史EOD Delta/moneyness必须重算；所有结构仅作询价模板。

## 9. 21:00夜盘风险地图

今晚会话属于11月3日；[上期所交易时间](https://www.shfe.com.cn/services/calenderandholidays/tradinghours/)明确夜盘从上一个工作日21:00开始。三层顺序是：11月2日中国EOD → 10月30日晚至31日凌晨的历史Night（原始文件空，隔离） → 11月2日欧洲/美国盘前。没有任何“今晚已发生”行情。

| 主题 | 可能开盘/追价 | 15/30/45分钟检查 |
|---|---|---|
| SC/BU/FU/LU | Brent较中国收盘窗口显著下跌，偏低开；不追空SC，油品已有高RV | 21:15看SC是否失守724、BU是否失守5150；21:30核Brent是否仍<110；21:45核SC2612/2701是否仍backwardation。任一反转则不做方向性结论 |
| MA/PP/L/EG | 国内强势但油价下跌，可能分化；MA不追高 | 21:15 MA≥3580且612/701≥2.5%；21:30回踩是否守3520；21:45 OI若无法获得可靠纯夜盘口径，不用来判新多 |
| CU/有色 | LME紧、国内弱，偏平至小高开；等待收敛 | 21:15核108300；21:30核2612/2701≥0.6%与LME≥14200；21:45回踩107600能否守住 |
| AG/AU | 海外银反弹，AG可能高开修复；不追空 | 21:15是否站回11950；21:30银是否仍>50；21:45若AG curve转backwardation，撤销空头研究 |
| 黑色/建材 | 海外映射弱，预计平弱；不因价仓象限追空 | 15/30/45分钟看RB3000、I670与J/JM曲线是否同步；只有价格和曲线共振才升级 |
| 农产品 | 外盘当期精确映射不足，平开概率假设不可验证 | 等45分钟；JD因DCE官方核对缺不做即时执行 |
| EC | **无夜盘** | 下一真实窗口11月3日09:00，按卡3执行确认 |

## 10. 未来24小时/7日事件与风控

- **11月2日21:00 BJT**：中国夜盘（归属11月3日）。先等15/30/45分钟，不把集合竞价跳空当确认。
- **11月3日收盘结算起**：INE调整部分SC/LU合约、SHFE调整FU2612/FU2701及部分BU合约的限幅和保证金；[INE通知](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833903.html)、[SHFE通知](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833901.html)。油品主题规模按更高压力预算，不把保证金当最大损失。
- **11月3日23:00 BJT**：美国9月JOLTS（美国东部10:00，已进入冬令时）；美元/实际利率冲击黄金、白银与铜。
- **11月3日全天至11月4日亚洲早盘**：美国中期选举；[FEC确认11月3日为联邦大选日](https://www.fec.gov/introduction-campaign-finance/election-results-and-voting-information/)。结果可能延迟，避免在贵金属/油品上卖裸Gamma。
- **11月4日23:30 BJT**：EIA周度石油状态报告；[EIA页面确认下次11月4日、常规周三10:30 ET](https://www.eia.gov/petroleum/supply/weekly/schedule.php)。油品期权Delta/Vega在数据前压缩或用有限支出结构；当前无报价则不执行。
- **11月5日21:30 BJT**：美国三季度生产率初值；**11月6日21:30**美国10月就业报告；[BLS日历](https://www.bls.gov/schedule/2026/11_sched_list.htm)。关注美元、实际利率与贵金属反向冲击。
- **11月7日04:30 BJT**：CFTC COT（11月6日15:30 ET，通常反映前周二持仓）；[CFTC日历](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)。只作拥挤背景，不替代实时OI。
- **7日内**：USDA WASDE通常8—12日发布，本报告窗口内未核到具体11月发布日期；不编日期。天气、矿山、油田、炼厂和地缘突发只在原始来源确认后计催化。

压力统一：试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同一商品因子（含股票/期权/期货）总预算≤2.5%—3.0%；本期卡片更紧的单笔限制优先。压力涵盖1/2涨跌停、开盘gap、流动性消失、相关断裂、保证金上调、IV跳升/塌陷、交割逼仓、人民币急变及中国休市期间海外跳空。无账户数据，不编净敞口。

## 11. 发布前校验与来源

已实际重算：五项评分分项之和；MA/CU/EC准确合约曲线；三卡好/中/坏成交的每手货币PnL与净R；EC 20%参考限幅压力；Options IV-RV差。已核：11月2日为最新完整EOD，今晚夜盘归属11月3日；AG/SC/BU旧计划的AND条件；CU/AG/EC乘数、tick或到期信息的交易所来源。未解缺口：合并输入与Night raw为空、DCE官方接口失败、期权无执行报价、Physical无A/B basis、SC/LU实体缺、Stock tradability缺、国际价格与中国EOD非同窗。

主要直接来源：[LME官方价格](https://www.lme.com/en/market-data/reports-and-data/lme-official-prices)、[Brent延时报价](https://markets.ft.markitdigital.com/data/commodities/tearsheet/historical?c=Brent+Crude+Oil)、[11月2日贵金属与油价报道](https://www.reuters.com/world/india/gold-rises-softer-oil-markets-parse-fed-signals-2026-11-02/)、[铜市场报道](https://www.brecorder.com/news/40447031/london-copper-climbs-as-tight-supply-falling-oil-offer-support)、[CU合约规则](https://www.shfe.com.cn/docview/docview_211238434.htm)、[EC标准合约](https://www.shfe.com.cn/products/futures/index_f/ec_f/standard_ec_f/202601/t20260121_830168.html)、[Stock输入](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_inputs_latest.json)、[紫金公告检索](https://www.cninfo.com.cn/new/fulltextSearch?keyWord=601899)、[宝钢公告](https://www.sse.com.cn/assortment/stock/list/info/announcement/index.shtml?productId=600019)。

A. 截至本报告时点，无可立即执行的合格新交易。
B. 仅挂条件：MA701确认回踩多、CU2612内外紧张收敛多；EC2612空单只等11月3日日盘三条件同现。
C. 继续观察：AG2612、SH701、JD2612及油品21:00低开后的曲线；实际持仓均未提供/未知。
D. 必须回避：追空AG、追涨SC/BU、用MA612或BU2612旧期权样本替代新主力、无bid/ask时宣称期权可执行；旧SC/BU/AG计划不再用于新入场。
