# 全球商品期货期权晚间雷达｜2026-10-31

> **一句话结论：截至本报告时点，无可立即执行的合格新交易；周一只承担SC/BU确认后回踩多与AG反抽失败空的条件风险。**

生成/截点：2026-10-31T19:38:00+08:00（北京时间）。这是周六当前更新，不是历史补跑。最近完整中国EOD为2026-10-30；10月30日晚至31日凌晨的合法Night归属11月2日。**今晚没有21:00夜盘，下一真实窗口是11月2日09:00日盘。** 只研究，不下单；实际持仓与成交状态均为“未提供/未知”。

## 1. 今晚值得承担什么风险

**截至本报告时点，无可立即执行的合格新交易。** 原因不是“没有研究机会”，而是周末无真实窗口，且Options无bid/ask与执行就绪数据。研究机会分三类：

- 等条件/报价：SC2612周末事件后突破回踩多、AG2612反抽失败空、BU2701油价与曲线共振后的回踩多；共同下一窗口为11月2日09:00，首次判断点09:15。
- 优势不足：MA701与AP701仍有价差/动量，但新PMI给出需求反证；不因油价或日盘强势直接追单。
- 数据不足：黑色和多数实体套利缺A/B级Basis；AG精确Night公开报价有冲突；商品期权没有可执行bid/ask、全链持仓或dealer Gamma方向。

本期新增最有价值的三项观察：①周日OPEC+结果能否让Brent在周一仍守115；②SC2612-2701、BU2612-2701是否在09:15保持正向近月结构；③弱PMI下MA/PP/EB/EG的夜盘升水是否被日盘需求证据消化，而非单纯高开回吐。

## 2. 数据质量、覆盖与事实台账

| 模块 | 应覆盖/实际 | 源日与生成 | available / published / analytically ready / execution ready | 关键缺口 |
|---|---|---|---|---|
| Futures | 5所；806合约、77品种；SHFE238/INE63/DCE214/CZCE243/GFEX48 | 源日10-30；10-31 19:01刷新 | 是 / 是 / 是 / 周末否 | 4个OHLC占位异常隔离；刷新不等于新交易日 |
| Market State | 77品种、20会话 | 10-30 | 是 / 是 / 是 / 取决于候选 | 连续主力不可冒充同合约收益 |
| Physical | 20目标，18 fresh；A/B级Basis=0 | requested 10-30；10-31 06:04 | 是 / 是 / 局部背景 / 否 | SHFE/DCE/GFEX仓单失败；低质量基差不能作套利确认 |
| External | 22目标，17 fresh | requested 10-30；10-31 06:04 | 是 / 是 / context only / 否 | 周末海外休市；使用周五结算，不冒充实时 |
| Night | 806请求；Night412，outside168，no-trade12，query/unresolved214；51.1166% | trading_date 11-02；start 10-30；end 10-31；05:58生成 | 是 / 是 / 局部 / 否 | raw latest为空；vendor snapshot非官方最终夜盘close；不是今晚 |
| Options | 64目标/45成功，1000合约、45 series；ATM44、skew24 | 10-30；10-31 06:04 | 是 / 是 / 局部ATM/skew / **0** | surface/positioning/execution均0；bid-ask 0%；full-chain=false |
| Metadata | SHFE/INE/CZCE可用；DCE错误；GFEX源日期未确认 | 10-30/10-31 | 局部 / 是 / 局部 / 重点合约需复核 | DCE合约参数HTTP412；不猜缺失参数 |
| 官方crosscheck | SHFE238、INE63、CZCE243（close可比182）、GFEX48全0差异；DCE失败 | 10-30 | partial / 是 / 四所价格可用 / 不含量仓 | DCE HTTP412；不由partial推导实际价差 |
| Stock | 5577 universe、5571原始价量；事件216；完整财务2 | trade_date10-30；research_asof 10-31 10:40 BJT | 局部 / 是 / 利润桥局部 / **0** | 无复权、行业、预测修订、实时交易状态/成本 |

'report_input_latest.json'为0字节；因此模块状态由同版本module-specific文件与root status核对。Night的'coverage_complete=false'不否定412个已取得合约，但214个未解析不可计证据。Options质量文本误写“vendor_greeks 1.0<0.8 blocked”，结构化字段为'vendor_risk_available=true'；本期披露矛盾，不采用更有利解释。

核心事实台账：

| fact_id | 事实与语义 | 观测/known_at | 支持 | 局限 |
|---|---|---|---|---|
| F-CALENDAR-1031 | 中国商品期货：2026-10-31周六休市；今晚无21:00夜盘；下一窗口2026-11-02 09:00（official calendar and trading-hours rule） | 2026-10-31T19:38:00+08:00 / 2026-10-31T19:38:00+08:00 | 合法交易窗口 | 各品种具体交易时段仍按交易所规则；[源](https://www.shfe.com.cn/services/calenderandholidays/holiday/) |
| F-FUTURES-1030 | 五所期货：806 contracts; SHFE238/INE63/DCE214/CZCE243/GFEX48; source-date match 100%（2026-10-30 complete EOD vendor） | 2026-10-30T15:00:00+08:00 / 2026-10-31T19:01:13+08:00 | 全市场价格初筛 | 4个OHLC占位异常已隔离；不是10月31日新增交易日；[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) |
| F-NIGHT-1102 | 历史Night会话：trading_date 2026-11-02; start 2026-10-30; end 2026-10-31; 412/806 night contracts; query_error/unresolved 214（vendor latest-trade snapshot; raw latest file empty） | 2026-10-30T21:00:00+08:00 to 2026-10-31 / 2026-10-31T05:58:24+08:00 | 周一开盘前历史价格层 | coverage 51.1166%; not official final night close; not tonight；[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) |
| F-PMI-1031 | 中国PMI：制造业49.3；生产49.8；新订单49.4；非制造业49.7；建筑业48.0（official monthly release） | 2026-10 / 2026-10-31T09:30:00+08:00 | 顺周期需求反证与链条分化 | 月度扩散指数，不等于具体商品需求量；[源](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html) |
| F-OIL-1030 | Dec Brent/WTI：117.64/104.12; +2.4%/+2.08% Friday settlement（Friday settlement reported by Reuters） | 2026-10-30 US close / 2026-10-31T19:38:00+08:00 | SC/BU外盘与周末跳空风险 | not live weekend quote; contract month differs from SC；[源](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/) |
| F-OPT-1030 | 中国商品期权核心样本：45/64 products, 1000 contracts, ATM-ready44, skew-ready24, surface/positioning/execution 0（core_v1 sampled_strikes EOD） | 2026-10-30 EOD / 2026-10-31T06:04:26+08:00 | 局部IV与skew研究 | bid/ask 0%; full chain not verified; readiness limitation text has a vendor-greeks inequality typo；[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) |
| F-STOCK-1030 | A股研究输入：trade_date 2026-10-30; 5571 raw quote rows; full financial bundle 2; execution ready 0（EOD raw/unadjusted stock research） | 2026-10-30 EOD / 2026-10-31T10:40:26+08:00 | 公司利润桥背景 | 复权、行业、实时交易状态、执行成本不就绪；[源](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_inputs_latest.json) |

## 3. 12项市场仪表盘

所有中国价格均为10月30日完整EOD；“历史Night”指10月30日晚会话、交易日归属11月2日，不是今晚。volume/OI/ΔOI未注明数值者仅表示仓库有EOD字段但本栏不复写，不能据此推断新多/新空。

| 合约 | close/settle | 1D/5D | vol/OI/ΔOI | 曲线/历史Night与外盘 | Options | 信号 |
|---|---:|---:|---|---|---|---|
| SC2612 | 742.4/727.6 | -1.128%/1.478% | 191821/27364/-262 | SC2612-2701：日盘待核；合法夜盘758.5/750.5，近月+1.066%；历史夜盘快照+2.168% vs close；周五Brent 117.64 | ATM730 IV66.16；skew否；执行否 | 周一突破回踩多，禁追高 |
| MA701 | 3480/3463 | 0.933%/8.32% | 3293327/881205/-40955 | 历史夜盘MA701/612=3613/3697，近月+2.325%；历史夜盘+3.822% vs close；PMI需求反证 | MA612 ATM3550 IV48.60；错月；执行否 | 链内确认后多 |
| BU2701 | 5284/5204 | 1.919%/13.13% | 612330/236079/+13377 | 日盘近远曲线约+1.65%；历史夜盘5304；历史夜盘+0.379% vs close；Brent强、建筑PMI弱 | ATM5200 IV46.31；skew否；执行否 | 回踩多，禁高开追 |
| AG2612 | 12093/12374 | -4.211%/-6.647% | 545345/238317/-21622 | 近远月方向偏弱；精确夜盘源冲突，隔离；COMEX银49.097周五结算，月跌18.31% | ATM12400 IV43.25；skew否；执行否 | 只等反抽失败空 |
| AU2612 | 855.18/861.9 | -0.879%/-0.84% | 见EOD/见EOD/待核 | 曲线不作正式结论；COMEX金3885.70周五结算，日跌3.29% | 局部ATM可读；执行否 | 现金化压力，观察 |
| EB2612 | 10404/10253 | 0%/1.716% | 见EOD/见EOD/待核 | 历史夜盘10675；历史夜盘+2.605% vs close | 局部ATM可读；执行否 | 油化强但不追 |
| PP2701 | 10433/10433 | 1.301%/9.59% | 见EOD/见EOD/待核 | 历史夜盘10815；历史夜盘+3.662% vs close | 局部ATM可读；执行否 | MA确认腿 |
| EG2701 | 5392/5342 | 2.044%/10.304% | 见EOD/见EOD/待核 | 历史夜盘5423；历史夜盘+0.575% vs close | 局部ATM可读；执行否 | 涨幅较大，回避追价 |
| CU2612 | 108050/108190 | -0.77%/0.82% | 见EOD/见EOD/待核 | 历史夜盘107250；历史夜盘-0.740% vs close；PMI有色产需弱 | 局部ATM可读；执行否 | 内外与宏观冲突，观察 |
| SN2612 | 360880/370160 | -3.373%/-1.28% | 见EOD/见EOD/+4771 | 历史夜盘362880；-1.967% vs settle；不据OI判新空 | 局部ATM可读；执行否 | 层数不足，禁追空 |
| AP701 | 5887/5678 | 2.788%/-0.838% | 见EOD/见EOD/+15152 | AP701-703结算曲线+5.401%；无夜盘；下一真实窗口11/2 09:00 | ATM5700 IV32.97；RR25 -3.64；执行否 | 仅周一回踩多 |
| EC2612 | 2625/2648 | -0.675%/-11.036% | 见EOD/见EOD/+288 | 结算近远约-14.218%；无夜盘；水运PMI>55但非运价直接证据 | 不适用/无合格执行数据 | 趋势弱但赔率不足 |

板块未入榜结论：黑色9品种已扫，PMI和建筑负面但实体/Basis不足，未形成合格空头；金属13品种中贵金属与锡最弱，追空赔率不足；能源化工29品种的主要异常仍是外油强、内需弱；新能源LC/SI/PS没有三层同向；农产品25品种仅AP曲线/动量突出，油脂粕类无新增独立催化；EC趋势弱但水运PMI强不是运价直接证据。动态目录77品种含PT/PD/BZ，未因Top5省略扫描。

## 4. 相比前序的真实变化

1. **PMI成为新增反证。** 10月制造业PMI 49.3、生产49.8、新订单49.4；建筑业48.0。来源为[国家统计局原表](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html)。这不是价格已反映的证明，但提高黑色、铜和化工追多的门槛。
2. **外油周五最终结算比晨报早盘更强。** [Reuters](https://www.reuters.com/business/energy/oil-rises-supply-concerns-houthis-attack-saudi-arabia-2026-10-30/)报Brent 117.64、WTI 104.12。SC由“等待确认”维持第一，但不把周末静态结算当周一可成交价。
3. **贵金属最终收盘继续去风险。** COMEX金3885.70、银49.097；AG空头方向得到海外层支持，然而EOD减仓与低开使追空赔率下降。
4. **时点修正。** 前序所有“今晚21:00”计划已过期；历史Night合法归属11月2日但不是本晚。旧计划未成交、未持有、未盈利；参数迁移到周一09:15并保留idea_id。
5. **Stock能力更新但无新公司催化。** 引擎trade_date推进至10月30；宝钢/紫金只有8月22日半年报利润桥，不能把周六入库或旧披露当今日经营新增。

## 5. 产业链与公司利润桥

| 传播路径 | 强弱与分歧 | 证据/最大缺口 | Stock校验 |
|---|---|---|---|
| 中东供给风险→Brent/WTI→SC→FU/BU→炼化 | 外油强，SC/BU只做确认后多；内需PMI弱 | 外油结算+历史Night+近月结构；缺OPEC+结果与周一同窗报价 | 无合格新增公司证据；股票不如期货直接，且公司套保/炼化结构会稀释 |
| PMI/建筑→矿石/煤焦→钢材→加工利润 | 需求反证；不直接做空 | PMI官方；A/B Basis与钢厂即时利润缺 | 宝钢2026H1合并口径：营收1607.31亿元、成本1511.02亿元、归母净利45.71亿元、经营现金流148.15亿元，毛利率约5.99%；若钢价传导不及原料，利润承压。反证是高端产品溢价、降本、库存低价结转。股票实时执行未核，故不入榜。[半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF) |
| 油→MA/PP/EB/EG/PX/TA | 成本强、需求弱；MA历史Night最强但PX分化 | 价格/曲线两层；Physical A/B=0，MA期权错月 | 不扩展到独立化工股扫描；无新原始公告足以改变商品判断 |
| 实际利率/美元/现金化→金银→AU/AG | 银弱于金；反抽空优于追空 | EOD+COMEX+曲线；AG精确Night冲突、skew缺 | 紫金2026H1矿产金/铜暴露真实，但AG空头不是其直接利润映射；营收1941.78亿元、归母净利391.70亿元、经营现金流554.72亿元。产量、实现价、套保、少数股东可推翻简单金价映射，因此股票不作AG替代。[半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF) |
| 苹果现货/库存/天气→AP701-703→期权 | 曲线与动量偏多 | 价量/期限两层；库存天气新增缺 | 无直接高质量公司映射；期货比股票表达更纯，但尚未到执行门槛 |

## 6. 统一机会榜

| 排名/idea_id | 方向/期限/阶段 | 逻辑/赔率/催化/价曲波/拥挤=总分 | 五层支持与反证 | 研究/证据/执行 |
|---|---|---|---|---|
| 1. SC2612周末事件后突破回踩多<br>COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030 | 条件多；1—3D；等待11月2日09:15三重确认 | 21/17/17/11/8=74 | 支持1/2/4；反证：PMI与建筑需求走弱、实体库存层缺、期权执行未就绪 | priority/three_layers/weekend_closed_conditional_not_ready |
| 2. AG2612反弹失败空<br>COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029 | 条件空；1—5D；等待周一反抽与COMEX确认 | 19/17/14/12/9=71 | 支持1/2/4；反证：去杠杆降低追空赔率、实体层缺、skew与可执行报价缺 | priority/three_layers/weekend_closed_conditional_not_ready |
| 3. BU2701强曲线回踩多<br>COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 | 条件多；1—3D；等待周一油价与曲线再确认 | 19/14/14/13/9=69 | 支持1/2/4；反证：建筑PMI48.0、实体层缺、周五涨幅已较大 | priority/three_layers_but_odds_limited/weekend_closed_conditional_not_ready |
| 4. MA701油化缺口保持多<br>COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 | 条件多；1—3D；等待链内一致与回踩 | 18/13/13/14/10=68 | 支持1/2；反证：PMI需求负面、实体仅低质量背景、期权错月 | watch/two_layers_cap_69/weekend_closed_conditional_not_ready |
| 5. AP701动量曲线回踩多<br>COM-A-AP701-MOMENTUM-CURVE-PULLBACK-LONG-20261030 | 周一日盘条件多；1—4D；等待09:15与实体增量 | 19/14/10/13/9=65 | 支持1/2；反证：实体库存与天气增量缺、海外层缺、RR25为负且无执行报价 | watch/two_layers_cap_69/next_day_session_only |

评分是研究优先级，不是胜率。MA/AP只有两层，严格封顶69。SC/AG/BU虽有三层，仍因周末、触发未到与报价缺失而不可执行。

## 7. 三张完整研究/交易卡

### 7.1 SC2612｜COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030

- 新事实→定价→分歧：周五Brent升至117.64且历史Night SC2612为758.5，但国内EOD仍弱、PMI偏弱。市场已计入部分供给升水；我们的分歧只在“周日OPEC+后升水能否通过近月曲线保留”，不是预测油价必涨。
- 表达：期货最直接；SC call spread只有双腿bid/ask、净支出和行权交割核实后才是有限损替代。否则选择不交易。
- 入场：11月2日09:15后：SC≥758连续15分钟 AND SC2612-2701≥1.0% AND 可比Brent≥113；再等750—756回踩守746，40%/60%。首价>770或曲线<0.5%放弃。
- 止损/目标：计划止损742；Brent<111持续30分钟或曲线转负为逻辑失效。止损不封顶跳空损失。 TP1 780；TP2 805；11月4日22:45时间退出。
- 好/中/坏：好/中/坏入场750/753/756；单手计划风险8000/11000/14000元；TP1毛R3.75/2.45/1.71，TP2毛R6.88/4.73/3.50；费用与滑点未知。
- 参数与压力：乘数1000桶、tick0.1元、tick价值100元；保证金18%、限幅16%为仓库值待官方复核；按settle估算一/二个16%下限压力约116,416/214,205元每手；相关断裂与保证金上调另计。
- 催化/最强竞争解释：OPEC+维持产量或地缘缓和可令周末升水回吐；周一首个区分观测是“价格与curve同时守住”，不是单看高开。

### 7.2 AG2612｜COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029

- 新事实→定价→分歧：AG EOD下跌且OI减少，COMEX银周五结算49.097。方向已明显定价，故只博反弹失败后的二次下行；若没有反弹，就没有赔率。
- 表达：期货线性空；put spread仅在可执行净支出、两腿流动性和到期风险核实后成立。ATM IV43.25高于RV20 32.06不能独立证明期权贵或便宜。
- 入场：11月2日09:15后先反弹11780—11920，随后15分钟不能站上11950 AND 可比COMEX银≤49.50 AND AG2612-2701≤0；40%/60%。首价<11400、无反弹或精确报价仍冲突则放弃。
- 止损/目标：计划止损12150；COMEX银>51.0或曲线转正并持续30分钟为逻辑失效。 TP1 11300；TP2 10700；11月4日14:45退出。
- 好/中/坏：好/中/坏空11920/11850/11780；风险3450/4500/5550元；TP1毛R2.70/1.83/1.30；TP2毛R5.30/3.83/2.92；费用未知。
- 参数与压力：乘数15千克、tick1元、tick价值15元；保证金22%、限幅20%；按settle估算空头一/二个涨停压力约37,122/81,668元每手。
- 催化/最强竞争解释：现金化冲击可能迅速均值回归；低开后若COMEX企稳、曲线转正，空头逻辑被推翻。AG公共精确Night报价冲突，故不用于正式收益或曲线计算。

### 7.3 BU2701｜COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026

- 新事实→定价→分歧：BU日盘和曲线强，外油周五再涨；但建筑PMI48.0提示终端需求弱。主要PnL来自供给升水向沥青近月传导，不能把Brent涨幅机械映射。
- 表达：BU期货；call spread只有报价核实后可替代。与SC同属油因子，风险预算合并。
- 入场：11月2日09:15后BU≥5300持续15分钟 AND BU2612-BU2701≥1.50% AND 可比Brent≥115；随后5235—5265回踩守5200，40%/60%。首价>5380放弃。
- 止损/目标：计划止损5170；曲线<1.0%或Brent<112持续30分钟逻辑失效。 TP1 5380；TP2 5520；11月4日14:45退出。
- 好/中/坏：好/中/坏5235/5250/5265；风险650/800/950元；TP1毛R2.23/1.63/1.21；TP2毛R4.38/3.38/2.68；费用未知。
- 参数与压力：乘数10吨、tick2元、tick价值20元；保证金14%、限幅12%待官方复核；按settle估算一/二个下限压力约6,245/11,740元每手。
- 催化/最强竞争解释：成本升但需求弱会压裂解/加工利润，BU可能显著落后原油；下一项区分观测是BU曲线而非单腿价格。

## 8. 商品期权专项

10月30日'core_v1/sampled_strikes'覆盖45/64品种、1000合约、45 series；'core_atm_ready=44'、'skew_ready=24'，但'surface_ready=0'、'positioning_ready=0'、'execution_ready=0'、bid/ask覆盖0、full-chain=false。故：

- 可研究：SC2612 ATM730 IV66.16；AG2612 ATM12400 IV43.25对RV20 32.06；BU2701 ATM5200 IV46.31；AP701 ATM5700 IV32.97、RR25 -3.64、BF25 +1.17。
- 不可声称：完整曲面、跨期限结构、全链PCR、拥挤度、dealer Gamma方向、可成交权利金、净成本或限损可执行。
- MA局部期权是MA612，不是MA701；不能把错月IV当第五层执行证据。周一标的moneyness变化后必须重算Delta/ATM；旧IV仅研究背景。
- 事件处理：OPEC+前不买无报价裸Vega；若询价，净支出上限必须由NAV预算倒推且不高于结构最大可承受损失，未取得报价前保持“待询价”。

## 9. 下一真实窗口风险地图（今晚无21:00）

三层事实：Previous China EOD=10月30日；Current T Night=10月30日晚合法会话、归属11月2日且已完成；Weekend overseas=周五最终结算，周六无连续市场。PMI在周六09:30发布，是新增信息但还没有中国价格反应。

| 11月2日09:00情景 | 可能板块 | 行动与15/30/45分钟确认 |
|---|---|---|
| 高开 | SC/FU/BU、油化 | 不追。09:15看近远月与Brent；09:30等回踩；09:45仅在价格、曲线、链内广度同向时第二段 |
| 低开 | 黑色/CU/AG/SN | PMI弱已知，低开不等新alpha；AG/SN禁追空，等反弹失败；黑色等实体/仓单 |
| 平开 | MA/PP/EB/EG、AP | 15分钟看缺口是否保留，30分钟看成交/OI与curve，45分钟才判断是否有可达入场 |
| 内外冲突 | SC与Brent、CU与LME | 只做映射观察；合约/币种/品质/汇率/时点未对齐时不称套利 |

夜盘品种下一次21:00是11月2日晚、交易日归属11月3日。周一日盘未确认的计划不自动顺延；必须重新核报价、曲线和触发顺序。

## 10. 未来24小时与7日事件

- 24小时：11月1日OPEC+线上会议，具体时点未由官方页面给出；[10月4日OPEC原文](https://opec.org/pr-detail/616-4-october-2026.html)确认11月1日再开会、11月维持9月所需产量。油品Delta只在结果和周一价格共同确认后增加。
- 48小时：11月2日09:00中国商品日盘；09:15/09:30/09:45分层确认。PMI已发布，不把它再次列为未来事件。
- 7日：EIA常规周三10:30 ET；美国11月1日结束夏令时，11月4日对应北京时间23:30。来源：[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)。
- CFTC：10月27日为当前持仓日期，[官方CMX页](https://www.cftc.gov/dea/futures/deacmxlf.htm)；下次发布时间待官方更新，只作滞后背景。
- USDA/WASDE：通常在每月8—12日，但本期未核到精确2026年11月时点，不编具体日期；农产品事件凸性等待正式日历。
- IEA 11月OMR为11月13日，[官方事件页](https://www.iea.org/events/oil-market-report-november-2026)；超出7日，仅作后续供需校验。
- 公司：限定检索仅覆盖宝钢、紫金两家现有公司目录与原始半年报；没有取得周六新增、足以推翻商品论点的经营公告。股票报价/停牌/涨跌停/交易成本未核，不能称即时可执行。

## 11. 旧观点、风险与发布校验

旧观点沿用稳定idea_id；所有参数变化均因“交易窗口过期+PMI/周五最终结算新增”，不是事后移动止损。无成交回执，实际持仓=未提供/未知；任何“退出”仅适用于假设已有仓位且逻辑失效。

风险预算：试仓NAV0.25%—0.75%，确认NAV0.75%—1.50%，同一主题合计≤2.5%—3.0%；SC+BU+油化股票/ETF/期权合并计油因子，AG/AU/矿业股合并计贵金属因子。规模公式为'floor(风险预算金额 / 坏成交计划风险每手)'；保证金不是风险，止损不能限制跳空、限板、流动性枯竭、保证金提高、IV跃变、交割逼仓或相关性断裂的最大亏损。

实际校验：五项评分分项均重算并等于总分；好/中/坏R按允许入场与计划止损重算；周末日历、Night归属、外盘结算、PMI、期权readiness、四所官方价格0差异/DCE失败均核对。未完成：DCE官方价格与合约参数、AG精确Night冲突、A/B级Basis、期权bid/ask与完整链、公司实时交易状态。受影响项已局部隔离，没有把全篇降为“数据清单”。

A. 截至本报告时点，无可立即执行的合格新交易。  
B. 仅挂条件：11月2日SC2612三重确认后回踩多、AG2612反弹失败空、BU2701油价与曲线确认后回踩多。  
C. 继续观察：MA701链内一致、AP701实体增量、CU内外映射、黑色对PMI的真实消化与局部Options IV。  
D. 必须回避：虚构今晚21:00、追油品高开、追贵金属低开、用无bid/ask期权执行、把计划止损当最大亏损；若假设已有仓位且卡片逻辑失效，按条件退出。
