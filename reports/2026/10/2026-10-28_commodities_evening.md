# 全球商品期货期权晚间雷达｜2026-10-28

**一句话结论：** 截至本报告时点，无可立即执行的合格新交易；甲醇、铜、沥青只保留21:15后顺序确认，原油与贵金属等待EIA/FOMC。

生成时间：2026-10-28 19:40 BJT；信息截点：19:39 BJT。研究用途，不下单，不假定持仓或成交。中国最近完整日盘为2026-10-28；今晚21:00开始的夜盘归属2026-10-29交易日，尚未发生。

最有价值的待验证观察：①21:15后MA701能否与PX612、近月曲线同步；②CU2612能否在LME三月铜重新站上14,500美元/吨时扩大近月溢价；③BU2701能否在Brent守住115.5美元/桶且强曲线不松时完成回踩。下一真实窗口为2026-10-28 21:00 BJT，首个判断点21:15，随后21:30/21:45复核。

## 1. 事实台账与数据质量

| fact_id | 标的/口径 | 观测值与时间 | 支持的判断 | 局限 |
|---|---|---|---|---|
| F-EOD-001 | 五所期货EOD | 2026-10-28；806合约、77产品；SHFE/INE/DCE/CZCE/GFEX均同日，source-date-match 100% | 日盘横截面可用 | vendor全市场ready不等于全部字段官方核验 |
| F-XC-002 | 官方价格交叉核对 | SHFE 238、INE 63、CZCE 243、GFEX 48个合约匹配且settle差异0；DCE接口HTTP 412 | 四所close/settle/pre-settle独立核对通过 | DCE未官核；不核volume/OI |
| F-NIGHT-003 | 最近已完成Night | 10/27晚—10/28晨，trading_date=10/28；416/806，214 query_error/unresolved | 仅说明上一合法夜盘流程 | coverage不完整；`data/night_session/latest.json`为0字节；不是今晚夜盘 |
| F-FUT-004 | CU2612 | close/settle 109,200/109,200元/吨；1D +0.52%、5D +0.15%；OI +4,388；CU2611-12 +0.586% | 价格与持仓温和确认，曲线接近旧阈值 | C级basis不计证据；动态限幅/保证金未核 |
| F-FUT-005 | MA701 | close/settle 3,464/3,417元/吨；1D +0.44%、5D +9.87%；OI +9,742；近月曲线 +4.467% | 旧多头论点部分修复，但已计价显著 | Options对应MA612而非MA701；basis C级 |
| F-FUT-006 | BU2701 | close/settle 5,054/4,945元/吨；1D +1.06%、5D +9.67%；OI +26,241；近月曲线 +5.479% | 日盘价、量仓、曲线共振 | close高于settle不等于尾盘路径；海外时点不可比 |
| F-EXT-007 | Brent/WTI | Reuters 10/28 12:35 BJT：115.47/101.33美元/桶，各+1.4%；Brent后续公开快照约115.3—115.9 | 油价重新计入供应风险 | 沙特尚未确认胡塞武装所称炼厂遇袭；实时源时点不一 |
| F-EXT-008 | LME/COMEX | LME 10/28现金14,625、三月14,435美元/吨；COMEX铜约6.6365美元/磅、黄金4,065、白银54.015 | LME三月铜低于14,500确认线；贵金属事件前偏弱 | 非统一结算时点，只作映射 |
| F-OPT-009 | 商品期权Core | 974合约、44/64产品；ATM ready 44，skew ready 24；surface/positioning/execution均0 | 可研究局部ATM/skew与IV-RV | sampled_strikes不是完整链；bid/ask覆盖0，不能写可成交净成本 |
| F-STK-010 | 宝钢股份600019三季报 | 10/28披露：Q3营收849.16亿元、归母净利21.67亿元；1—9月钢铁制造毛利率4.8%，同比-1.4pct | 原料成本传导压缩钢厂利润，为黑色链实体反证 | 未核证券实时价格、停牌和交易成本，不称股票可执行 |

仓库读取状态：`data/report_input_latest.json`与`data/night_session/latest.json`均为empty_0_bytes；其余EOD、Market State、Physical、External、Options、Metadata、crosscheck均可解析。Futures full_market_ready=true、critical errors=0、OHLC占位3；Physical 18/20 fresh、2 unavailable、A/B级basis=0；External 17/22 fresh、5 unavailable且均为context-only；Metadata 806合约，直接匹配67.49%、有效匹配73.45%，动态字段覆盖30.15%；Stock私库最新交易日2026-10-21，故仅用10/28公开披露补证。

## 2. 全范围覆盖与板块结论

后台初筛覆盖63个指定代码及引擎实际77产品；五所均取得10/28 EOD。黑色/建材中JM2701 +2.70%且backwardation，但宝钢利润桥提示需求与原料成本解释竞争，只有价格/曲线层；有色中CU最值得验证，AO2701 +2.43%但实体/期权缺；能源化工中PP2701 +2.77%、EG2701 +5.62%、MA/BU/FU活跃，然而PP/EG只有价格曲线层，不能因涨幅入榜；新能源中LC2701 close相对pre-settle -4.64%、OI上升，GFEX仓单失败且期权曲面不可执行；农产品中JD2612 +2.08%、AP701 +1.86%，basis/实体缺口使优势不足；航运EC2612 1D -3.46%、5D -12.23%、contango -15.39%、OI +18.22%，趋势值得观察但缺海外运价/期权/实体独立确认。

## 3. 12项仪表盘

收益均以同一准确合约结算价为基准；curve为近月减次月期货，不是现货基差。今晚Night尚未发生，Night栏统一为“待21:00”。

| 板块/合约 | EOD close/settle | 1D / 5D | Vol / OI / ΔOI | curve | Physical/Options/海外 | 信号 |
|---|---:|---:|---:|---:|---|---|
| CU2612 | 109200/109200 | +0.52%/+0.15% | 79060/195587/+4388 | +0.586% | basis C；ATM IV12.33%、RR25 -1.27；LME3M 14435 | 条件多，未共振 |
| MA701 | 3464/3417 | +0.44%/+9.87% | 282.1万/913840/+9742 | +4.467% | basis C；MA612 ATM IV50.39%、RR25 +2.42 | 条件多，防追高 |
| BU2701 | 5054/4945 | +1.06%/+9.67% | 397061/206508/+26241 | +5.479% | ATM IV44.13；Brent约115.3—115.9 | 强曲线回踩多候选 |
| SC2612 | 733.4/722.4 | -1.26%/+3.08% | 171388/30025/-608 | +0.706% | ATM IV69.13；Brent上涨 | settle弱、close高，方向冲突 |
| FU2701 | 5405/5305 | +0.19%/+10.61% | 842314/257524/+2744 | +16.328% | ATM IV71.06 | 极强曲线，赔率不足 |
| AG2612 | 13010/13099 | +0.87%/-6.59% | 106.7万/254857/-18173 | -0.221% | ATM IV40.44%；COMEX银-0.91% | FOMC前不追 |
| AU2612 | 867.4/870.06 | +0.74%/-2.25% | 474471/182800/-2884 | -0.278% | ATM IV21.37%、RR25 +0.22；金-0.24% | 事件双向gap |
| SH701 | 1448/1476 | -1.53%/-13.07% | 935272/351629/+33697 | +2.282% | SH612 ATM IV39.5%、RR25 -2.31 | 价弱、曲线反对做空 |
| SA701 | 979/983 | +1.55%/+3.26% | 235.2万/128.3万/-29401 | -2.747% | basis C；ATM IV25.2%、RR25 -0.25 | 反弹但OI减 |
| LC2701 | 93300/96460 | -1.41%/-1.25% | 398175/448923/+9791 | +1.321% | basis C；ATM IV57.03；GFEX仓单失败 | 弱价强曲线冲突 |
| LH2701 | 9840/9885 | +0.82%/-1.89% | 158529/145013/-11511 | -6.070% | 无A/B basis、无局部期权 | 反弹未证趋势反转 |
| EC2612 | 2688/2647.5 | -3.46%/-12.23% | 12835/12818/+1976 | -15.392% | 海外运价/期权缺 | 趋势空观察 |

## 4. 相比上一报告真正变化

1. **MA旧多由失效观察修复为条件多。** 今晨供应商夜盘曾较前收跌约2%，但10/28 EOD结算回升至3417、5D扩大至+9.87%、OI转增；旧触发窗口仍已终止，今晚是新条件，不能追认成交。
2. **CU价格确认增强、曲线和外盘仍差半步。** 结算由108640升至109200，OI增加；CU2611-12仅0.586%，LME3M 14435低于新确认线14500，故不把HVC扰动视为未充分定价。
3. **BU成为更纯粹的油价/强曲线候选。** BU2701日盘close 5054、OI单日增14.56%、近月曲线5.479%；Brent重新升至115美元上方，但供应消息未获沙特确认且EIA临近，禁止第一跳追涨。
4. **SC旧条件空已失去方向优势。** 日结算-1.26%，但close高出settle 11元且曲线仍backwardation，海外油上涨；旧“contango延续空”不满足，降为事件观察，不反手追多。
5. **黑色链新增独立公司利润证据。** 宝钢Q3称钢价回升幅度不及原料涨幅、购销差缩窄；1—9月钢铁制造毛利率4.8%同比降1.4pct。这降低了JM/I/RB单边追涨确信，强化“原料—钢材利润压缩”的研究方向，但尚无精确可交易配比。

## 5. 产业链图与Stock利润桥

- **原油→BU/FU/SC→炼化利润：** Brent供应风险支持BU/FU强势，BU曲线与OI最强；SC日内settle弱却curve为backwardation，内外信息弹性冲突。最大缺口是EIA与今晚准确夜盘。置信度：中。
- **HVC→LME铜→CU2612→矿企：** Teck HVC减负荷提供实体供应层，SHFE价/OI确认但LME3M和近月曲线未越阈值。Teck 10/29业绩及运营更新是区分观测。股权表达含矿山、汇率、资本开支与多金属因素，短窗不如CU直接。置信度：中高研究、低执行。
- **煤焦/铁矿→钢材→宝钢利润：** Q3普氏62%铁矿环比-7.9%，吕梁主焦煤+34.9%；宝钢钢铁制造毛利率收窄，说明“矿跌即利润扩张”被焦煤与钢价传导推翻。若煤焦继续强而RB/HC不跟，钢厂利润继续受压；公司成本改善与高端产品结构是最强竞争解释。商品价差比股票更直接，但需先验证配比与合约beta。置信度：中。
- **油→PX/TA→MA：** MA701强于PX/TA且曲线陡，剩余PnL必须来自同步补涨或甲醇自身供需，而不能仅靠油价标题。最大缺口是A/B basis、库存/开工和MA701同到期期权报价。置信度：中。

Stock决策贡献：仅研究宝钢股份600019。利润桥为“钢材售价/销量－铁矿/煤焦/能源成本＋产品结构/成本改善±库存与套保滞后”；披露证明Q3原料涨幅压过钢价回升，但套保、库存重估和长协细项不足，不能量化吨钢利润弹性。公司股票不是本期更优表达：实时价格、停牌、流动性与交易成本未核，且高端产品、出口和成本改善稀释商品因子。

## 6. 统一机会榜

| 排名 | idea_id / 方向 / 期限 | 五层证据 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 研究/证据/执行 |
|---:|---|---|---|---:|---|
| 1 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024；条件多；1—3D | 支持1/2/4；3缺、5错月 | 20/16/15/12/10 | 73 | 优先/3层/等顺序确认 |
| 2 | COM-M-CU2612-HVC-STRIKE-WATCH-20261025；条件多；3—10D | 支持1/2/3；4中性偏反、5反 | 20/16/16/11/9 | 72 | 优先/3层/等LME与曲线 |
| 3 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026；条件多；1—3D | 支持1/2/4；3缺、5中性 | 19/15/14/14/9 | 71 | 优先/3层/等回踩，事件前降仓 |
| 4 | COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026；暂停方向；日内—2D | 支持2/4；1反，3缺、5中性 | 18/14/14/12/10 | 68 | 观察/2层/旧空失效，不反手 |
| 5 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028；观察空；1—5D | 支持1/2；3/4/5缺 | 18/15/12/12/11 | 68 | 观察/2层/仅次日日盘条件 |

未入榜最重要异常：PP2701、EG2701、JM2701日盘涨幅与曲线突出，但有效支持仅一至两层，评分上限59/69；LC、SH价格与曲线冲突；农产品与软商品未取得足以跨越实体/basis缺口的新增证据。这里是“已研究但优势不足”，不是“没有研究机会”。

## 7. 研究/交易卡

### 卡1｜MA701条件多

- 新事实/定价/分歧：EOD close/settle 3464/3417，5D +9.87%，OI +9742，近月曲线+4.467%；市场已计入强势。只有MA、PX与曲线顺序共振，才认为剩余价差扩张尚未计价。
- 入场：21:15后MA701≥3485持续15分钟 **AND** PX612≥9850 **AND** MA611-12≥4.50%；随后回踩3460—3475且3445不破，40%/60%。首个可成交价>3520、曲线<3.5%或PX<9750放弃。
- 止损/目标/时间：计划止损3400；TP1 3550减半，TP2 3650；10/30 14:45退出。止损不封顶。
- 好/中/坏：3460/3468/3475；每手10吨，至3400风险600/680/750元；TP1毛R 1.50/1.21/1.00，TP2 3.17/2.68/2.33。坏价TP1仅1R，不考虑费用，故不能追。
- 参数：tick 1元/吨=10元/手；保证金9%、限幅8%、最后交易日2027-01-14；夜盘时间按郑商所当日参数下单前复核。按settle3417，单/双跌停静态压力约2734/5249元/手；不含滑点、提保和连续封板。
- 期权：MA612 expiry 11/11、ATM3550、ATM IV50.39%、RR25 +2.42%；与MA701错月且execution=false，仅研究，净支出/最大损失待人工询价。

### 卡2｜CU2612条件多

- 新事实/定价/分歧：EOD 109200/109200，OI +4388，CU2611-12 +0.586%；LME3M 14435。HVC扰动已部分计价，LME与曲线未共振。
- 入场：21:15后CU2612≥109600持续15分钟 **AND** CU2611-12≥0.65% **AND** LME3M≥14500；随后回踩109250—109450并守109100，40%/60%。首价>110300不追。
- 止损/目标/时间：计划止损108300；TP1 111500减半，TP2 113800；11/05 14:45退出。HVC复产、LME<14250或曲线<0.30%持续30分钟为逻辑失效。
- 好/中/坏：109250/109350/109450；5吨/手，风险4750/5250/5750元；TP1毛R 2.37/2.05/1.78，TP2 4.79/4.24/3.78；假设往返各1 tick滑点共100元/手，佣金未知。
- 参数：官方规格5吨/手、tick10元/吨=50元/手，最后交易日2026-12-15，夜盘21:00—01:00；动态保证金/限幅未完整核验，不能给一/二板精确压力。
- 期权：CU2612 expiry 11/24、ATM110000、ATM IV12.33%、RR25 -1.27、BF25 1.07；bid/ask=0、execution=false，仅研究看涨价差，最高净支出待询价。

### 卡3｜BU2701强曲线回踩多

- 新事实/定价/分歧：EOD close/settle 5054/4945，1D +1.06%、5D +9.67%，OI +14.56%，曲线+5.479%；Brent约115.3—115.9。市场已计入部分供应风险，剩余PnL需EIA前曲线保持。
- 入场：21:15后BU2701≥5060持续15分钟 **AND** BU2611-12≥5.50% **AND** Brent同一合约≥115.5；随后回踩5010—5040守4980，40%/60%。若首价>5120或Brent<113.8放弃。
- 止损/目标/时间：计划止损4910；TP1 5160减半、TP2 5300；22:15前减至试仓，10/30 14:45退出，避免带满仓穿越EIA/OPEC+。
- 好/中/坏：5010/5025/5040；10吨/手，风险1000/1150/1300元；TP1毛R 1.50/1.17/0.92，TP2 2.90/2.39/2.00。坏价TP1不足1R，禁止成交。
- 参数：官方规格10吨/手、tick1元/吨=10元/手；最后交易日2027-01-15。10/9交易所通知BU2701限幅12%、一般持仓保证金14%；按settle4945，静态单/双跌停压力约5934/11156元/手，仍非最大损失。
- 期权：BU2701 ATM4950、IV44.13%；完整曲面/执行均未ready，不给权利金、Greeks或限损承诺。

风险预算：试仓NAV 0.25%—0.50%，确认后单idea 0.75%—1.25%；MA/PX/TA合并油化主题≤1.5%，SC/BU/FU及油气股合并油价主题≤2.0%，CU与铜矿股合并≤2.5%；全部高确信商品主题合计≤3.0%。规模公式为允许货币风险÷（每手计划止损损失+滑点费用情景），保证金不是风险预算。

## 8. 商品期权专项

Core样本44/64产品、974合约，analytics_scope=sampled_strikes；44个series局部ATM ready、24个skew ready，完整surface/term/positioning/execution均未ready，dealer gamma方向未知。有效局部观测：CU2612 ATM IV12.33%、RR25 -1.27；SC2612 IV69.13%；MA612 IV50.39%、RR25 +2.42；BU2701 IV44.13；AG2612 IV40.44%；AU2612 IV21.37%。仅SC可见IV显著高于RV20约43.84%，但这不等于可卖波动：EIA/地缘gap、无bid/ask、无全链与保证金信息。MA/SH的期权series与主卡合约月份不一致，不能作为精确执行第五层。所有结构均为研究观察，执行前必须人工询价和确认，不提供未经验证的权利金。

## 9. 21:00夜盘风险地图

| 三层信息 | 已知事实 | 可能开盘 | 处理 |
|---|---|---|---|
| Previous China EOD | MA/CU/BU日盘强，SC settle弱但close高，AG/AU修复 | 油化/有色偏高开，原油分化 | 不把close-settle差当夜盘新增 |
| 已完成历史Night | 10/27晚归属10/28，416/806且214 unresolved | 仅作前序，不是今晚 | 不用旧Night判今晚触发 |
| 19:39海外/事件 | Brent约115.3—115.9；LME3M 14435；COMEX金银偏弱；22:30 EIA、次日02:00 FOMC | BU/FU/SC易高开高波；CU高开幅度受LME限制；贵金属双向 | 21:15查价格，21:30查曲线与海外，21:45查回踩/OI；EIA前降油主题风险 |

潜在高开：BU/FU/SC/MA；平至小高：CU；贵金属方向不确定。追价纪律：第一跳不追；只有卡片AND条件按顺序成立再等回踩。无夜盘或流动性不足品种转至10/29 09:00日盘，按09:15/09:30/09:45验证。

## 10. 未来24h / 7d事件

- 10/28 22:30 BJT：EIA周度石油报告；SC/BU/FU Delta降至试仓，未报价期权不做事件Vega。
- 10/29 02:00 FOMC决议、02:30发布会；AU/AG/CU关注美元与实际利率，禁止以旧IV当实时成交。
- 10/29 20:30：美国PCE、GDP/初请窗口；跨市场映射仅作方向背景。
- 10/29美股盘前/23:00前后：Teck Q3及运营更新，重点是HVC减负荷持续时间与产量指引；CU若已触发仍须按复产/曲线条件退出。
- 10/30：SHFE周度库存、Baker Hughes、CFTC；库存/仓单需原生发布日期，不把周频延续当当天催化。
- 11/01：OPEC+会议，市场预期维持12月目标；油主题在会前不扩至主题上限。
- 未来7日：中国PMI、海外天气/出口销售、矿山/炼厂/航运地缘更新；USDA/WASDE本窗口暂无已核新发布日期，不编造事件。

## 11. 旧观点与发布校验

- MA idea：10/27晚73→10/28晨59→今晚73；变化来自价格修复与曲线/OI，旧窗口仍终止，本晚参数仅适用于新候选。
- CU idea：72→74→72；日盘价格增强，但LME与曲线未越确认线，未追认上午触发。
- BU idea：71→63→71；准确EOD补齐且Brent回升，仍因EIA与追价风险受限。
- SC旧空：66→68→68；价格跌但曲线/海外反对，旧空方向暂停，不重置ID反手。
- 实际持仓状态：未提供/未知；任何OHLC穿越均不代表触发顺序、成交或盈利。

校验结果：五项得分均等于分项和；证据层上限通过；MA/CU/BU收益风险与静态限幅压力已重算；准确合约、EOD close/settle、到期日与可得静态参数已核；今晚Night未发生、DCE官核HTTP412、期权bid/ask=0、Physical A/B basis=0、动态参数覆盖30.15%、Stock私库滞后为未解缺口。Markdown与JSON由同一事实/候选对象渲染；CI状态为pending_or_unverified。

## 来源

- [China-Commodities-Engine EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)、[Official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)
- [Reuters油价与沙特炼厂消息，2026-10-28](https://www.reuters.com/world/asia-pacific/oil-prices-rise-after-attack-saudi-arabian-refinery-reignites-supply-concerns-2026-10-28/)、[EIA发布日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[Fed 2026-10日历](https://www.federalreserve.gov/newsevents/2026-october.htm?view=calendar)
- [Teck新闻发布](https://www.teck.com/news/news-releases)、[SHFE BU限幅/保证金通知](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261009_833649.html)、[INE SC限幅/保证金通知](https://www.ine.cn/eng/circularnews/circular/202610/t20261009_833652.html)
- [宝钢股份2026年三季报公开披露文本](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12665161&stockid=600019)、[宝钢主要经营数据](https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12665159&stockid=600019)

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：MA701、CU2612、BU2701，均须21:15后AND条件与回踩顺序成立。
C. 今天继续观察：SC2612事件方向、EC2612趋势空、AG/AU FOMC波动，以及PP/EG/JM的单层异常。
D. 今天必须回避或有条件退出：第一跳追价、EIA/FOMC前满风险、无bid/ask期权、DCE未官核即时执行；若已自行建仓，按各卡失效和时间退出处理。
