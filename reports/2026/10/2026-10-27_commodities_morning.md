# 商品期货期权晨间雷达｜2026-10-27

> **一句话结论：截至本报告时点，无可立即执行的合格新交易；铜、甲醇与原油反转均只到条件研究，须等09:15后精确曲线和报价确认。**

生成时间/信息截点：2026-10-27 07:09 BJT。最近完整中国EOD为2026-10-26；合法夜盘归属T=2026-10-27，开始日2026-10-26；下一真实窗口为今日09:00。

**截至本报告时点，无可立即执行的合格新交易。** 已研究但优势不足：LH/AP/EC延续空、AG修复。研究机会存在但等待条件/报价：CU、MA、SC。数据不足不能判断：其余未取得精确夜盘合约的品种及全部商品期权执行价格。最有价值的三项待验证观察是：09:15后CU是否突破108800并扩升水、MA是否回踩守3400且PX同步、SC是否跌破731并保持contango；下一检查为09:15/09:30/09:45。

## 1. 数据质量与覆盖

- 全范围：指定63代码全部映射并扫描（LPG→PG），引擎实际77产品、806合约；五所均为2026-10-26，source_date_match=100%，full_market_ready=true，critical errors=0，6个OHLC placeholder。
- 入口：[`report_input_latest.json`](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) 为0 bytes；因此分别读取模块文件。Futures/Market State为10/26；Physical 18/20 fresh；External 17/22 fresh但均context-only。
- Night：[`last_run_status`](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) 对应10/27，validation/published=true；416/806、51.6129%，214 query_error/unresolved；日期合法、calendar_mismatch=false。`night_session/latest.json`为0 bytes。CU/SC/MA启用独立exact-contract fallback；其余夜盘不用于执行判断。fallback不是交易所官方收盘，official_night_close_verified=false。
- Options：64目标、45成功、1052记录；core_atm_ready=44、skew_ready=27、surface/positioning/execution=0；quote coverage只覆盖采样目录，full_chain_verified=false。结构化vendor risk coverage=1与limitations文字矛盾，按保守口径不用模型Greeks。
- Metadata：合约匹配67.49%、有效73.45%，动态参数覆盖30.15%；DCE合约参数HTTP412、GFEX source-date mismatch。重点卡只使用库内或交易所已核参数，未知留缺。
- 官方交叉核对：SHFE 238、INE 63、CZCE 243、GFEX 48全部matched且settle/close/pre-settle差异0；DCE为source_error。未核成交量/OI。
- Stock：tape截至10/21，5568报价、最小财务包2公司；限定检索中国海油/中国石化/紫金矿业，新增经营线索0，股票不执行。
- 读取ref：Global manifest blob `29432f08...`；商品和Stock按main逐文件SHA读取，未声称统一部署commit。

### 事实台账

| Fact ID | 标的 | 值/单位 | 观测时点 | 直达源 | 支持判断 | 局限 |
|---|---|---|---|---|---|---|
| F-EOD-001 | 中国商品期货全市场 | 806合约、77产品、五所，source_date=2026-10-26；63项指定代码全部覆盖（LPG以PG映射） | 2026-10-26 EOD | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json) | 日盘全范围初筛与横截面比较 | 6个OHLC占位；vendor full_market_ready不等于官方全字段认证 |
| F-NIGHT-002 | 2026-10-27归属夜盘 | 416/806合约；214 query_error/unresolved；coverage=51.6129%；validation_passed/published=true；raw latest=0 bytes | 2026-10-26夜至10-27晨 | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) | 会话日历合法但重点合约必须独立补证 | 流程闭环不等于准确合约执行就绪 |
| F-CU-003 | CU2612 | EOD close/settle 108110/108180；1D结算+0.81%，5D-0.90%，ΔOI +6896；夜盘参考108570（+0.43% vs close，+0.36% vs settle） | 2026-10-26 EOD；2026-10-27 01:00 | [源](https://hq.smm.cn/futures/104179481) | 铜仍有供给事件研究价值，但未越过旧108800触发 | 夜盘为行情页独立fallback，非交易所官方收盘核验；Night曲线未得 |
| F-SC-004 | SC2612 | EOD close/settle 728.1/739.7；SC2611-SC2612=-1.6899%；夜盘733.30（+0.71% vs close，-0.87% vs settle） | 2026-10-26 EOD；2026-10-27 02:31 | [源](https://www.cls.cn/detail/2515846) | 旧≤724条件空未触发；contango与海外油回落仍保留反转空研究 | 媒体行情fallback；无同会话精确near-next夜盘曲线 |
| F-MA-005 | MA701 | EOD close/settle 3389/3346，1D结算+4.66%，5D+5.25%，ΔOI +66968；夜盘行情页3401（+0.35% vs close，+1.64% vs settle） | 2026-10-26 EOD；2026-10-27夜盘后页面 | [源](https://quote.stockstar.com/futures/czcema.html) | 强势延续但不证明完整多腿触发 | PX同步与MA701-next精确曲线、分钟顺序未核 |
| F-OIL-006 | Brent/WTI | 10月26日结算115.81/101.76美元/桶，日跌0.8%/1.46% | 2026-10-26 US settlement | [源](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/) | 反对追多国内油链，支持SC反转空的外部层 | 仓库External为110.17/101.25，合约口径冲突；跨市场套利不可用 |
| F-CU-007 | Highland Valley Copper | Teck收到罢工通知，最早可于10月24日08:00 PT启动 | 2026-10-24 | [源](https://www.teck.com/news/news-releases/2026/teck-receives-highland-valley-copper-operations-strike-notice) | 铜供给事件催化 | 未取得本期产量损失、复工时点或新公司公告 |
| F-OPT-008 | 商品期权core_v1 | 45/64产品成功；1052记录；core ATM 44、skew 27；surface/positioning/execution均0 | 2026-10-26 EOD | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) | 局部ATM/skew研究 | 全链未验、bid/ask=0，不能写可成交权利金或持仓结构 |
| F-XCHK-009 | 官方价格交叉核对 | SHFE238、INE63、CZCE243、GFEX48匹配且价格差异0；DCE HTTP412 source_error | 2026-10-26 EOD | [源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json) | 四所close/settle/pre-settle独立核对 | 不核成交量/OI；DCE未核完 |
| F-STOCK-010 | Stock联动 | 私库tape截至2026-10-21，5568报价、最小财务包2公司；限定检索600938/600028/601899未见10月26日新增经营公告 | 截至2026-10-27 07:09 | [源](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json) | 公司表达仅作利润桥背景 | 价格陈旧、映射不全、证券执行状态未核 |

## 2. 市场仪表盘

| 标的 | EOD close/settle | 1D/5D（结算） | Vol/OI/ΔOI | 曲线 | Basis/Physical | Options | Night/信号 |
|---|---:|---:|---:|---|---|---|---|
| MA701 | 3389/3346 | 4.66%/5.25% | 3322801/952582/+66968 | MA611-MA612 +6.50%（非701精确pair） | C，仅context | 主力series未匹配；execution=false | 夜盘参考3401；强但不追 |
| SC2612 | 728.1/739.7 | 3.17%/2.91% | 194360/32161/-2071 | SC2611-SC2612 -1.6899% | 无A/B | ATM740 IV68.31%，skew不可用 | night fallback733.30；旧空触发未到 |
| CU2612 | 108110/108180 | 0.81%/-0.90% | 88952/190675/+6896 | CU2611-CU2612 +0.6471% | C，仅context | ATM108000 IV13.00%，skew不可用 | night fallback108570；旧多触发未到 |
| PX612 | 9782/9820 | 3.78%/4.31% | 349829/112827/+18101 | PX611-PX612 +1.4460% | C，仅context | ATM9800 IV41.88%，10/28到期，execution=false | 强价强仓但近到期不追期权 |
| BU2701 | 4828/4738 | 3.00%/6.47% | 286173/162275/+12310 | BU2611-BU2612 +7.1267%（非2701） | 无A/B | 主力series未匹配 | 国内强、海外油跌；冲突 |
| FU2701 | 5295/5238 | 4.18%/5.67% | 940140/252657/-8047 | FU2611-FU2612 +13.2228%（非2701） | C，仅context | 无合格主力series | 价涨OI降；不追 |
| AG2612 | 13040/13050 | -1.55%/-6.49% | 451246/274179/-9509 | AG2611-AG2612 -0.1609% | 无A/B | ATM13000 IV39.95%，skew不可用 | 沪银夜盘+0.31%；旧空不追 |
| AL2612 | 23450/23475 | 1.19%/2.00% | 220539/255547/-1134 | AL2611-AL2612 +1.1715% | C，仅context | ATM23400 IV11.20%，RR25 -1.15 | IV略低于RV但非便宜证明 |
| LH2701 | 9560/9730 | -1.22%/-5.72% | 181663/192896/+3392 | LH2611-LH2701 -6.1151% | 无A/B | 无当前合格series | 趋势空；无夜盘；DCE官方核对缺 |
| SA701 | 966/962 | 1.48%/0.94% | 1595349/1258150/-23419 | SA611-SA612 -1.9792% | C，仅context | ATM960 IV25.18%，RR25 +1.52 | 正确EOD 966/962；反弹但OI降 |
| AP701 | 5542/5591 | -2.36%/-5.68% | 324958/164267/+4498 | AP611-AP612 +10.6833%（仅5观测） | 无A/B | ATM5600 IV34.30%，RR25 -3.96 | 跌价增仓；曲线样本短 |
| EC2611 | 2403.5/2421.5 | -0.43%/-12.77% | 7640/10222/-2035 | EC2610-EC2611 -8.6723% | 不适用 | 无 | 弱势但OI锐减，非新空确认 |

未入榜板块：黑色无A/B基差和完整仓单，只有现货C级背景；新能源LC/SI/PS无精确Night，不能判断即时机会；油脂谷物受USDA收获（玉米60%、大豆79%）影响但缺中国精确夜盘；EC弱势但量仓收缩，不等于新增空头。

## 3. 相比前序的真变化

1. EOD→Night：CU2612从108110到fallback108570，但仍低于旧108800确认线，前序条件多未触发。
2. EOD→Night：SC2612 fallback733.30相对close+0.71%、相对settle-0.87%；旧≤724条件空未触发，双锚结论冲突。
3. EOD→Night：MA701行情页3401延续强势，但缺精确曲线/PX同会话确认，不能把单点价写成完整信号。
4. 海外新增：Brent/WTI结算115.81/101.76、分别跌0.8%/1.46%；反对追多国内油链，但仓库Brent110.17存在合约口径冲突。
5. Options由前序44成功增至45，core ATM仍44、skew增至27；全链/positioning/execution仍为0，研究能力改善不等于可成交。
6. 旧观点处置：SC早间多头继续invalidated；CU/MA/SC三张前序卡均无成交回执，position_status仍为未提供/未知。

## 4. 产业链传播与公司利润桥

1. **原油→燃料油/沥青→芳烃/甲醇**：中国EOD最强为FU/BU/MA/PX，但Brent/WTI美盘结算下跌。SC contango支持反转风险，MA/PX价仓支持短期强势；最大缺口是统一Brent合约和精确Night曲线，置信度中低。
2. **铜矿→精铜→加工**：HVC罢工是独立实体层；CU EOD价升OI升、近月小升水，但夜盘108570未过触发，LME库存上升为最强反证。中国现货109771.67仅C级context，不称套利。置信度中。
3. **贵金属**：沪金夜盘+0.4%、沪银+0.31%，而AG EOD五日-6.49%；FOMC前方向和Vega都高风险。AG ATM IV39.95%高于RV30.86%但无bid/ask，不证明昂贵可卖。置信度中低。
4. **农产品/畜牧/航运**：LH/AP跌价增仓、EC五日-12.77%但OI大降；USDA收获推进。缺中国现货、养殖利润和DCE官方交叉核对，置信度低。
5. **Stock利润验证**：中国海油的油价售价弹性需扣税费、套保、Capex和时滞；中国石化上游受益可能被炼化成本抵消，10/30三季报再验；紫金矿业不是HVC资产，铜价冲击须扣成本、套保、汇率与少数股东。当前直接商品表达更纯，但均未到执行门槛。

## 5. 统一机会榜

评分顺序为逻辑/赔率凸性/催化/价格期限波动/拥挤技术；证据层为1价格、2期限、3实体、4海外、5期权。

| 排名 | 机会 | 总分（分项） | 有效支持层 | 方向/期限 | 研究/证据/执行 |
|---:|---|---:|---|---|---|
| 1 | CU2612 HVC罢工后的突破确认多 | 70（19/17/15/10/9） | 1,2,3 | 条件多/1—10D | 有效研究/3层但外部冲突/等待精确曲线与日盘确认 |
| 2 | MA701供应缺口强势延续 | 68（18/16/12/12/10） | 1,2 | 条件多/1—3D | 有效研究/2层，上限69/仅条件；不追3420以上 |
| 3 | SC2612 contango反转空 | 67（18/17/13/10/9） | 2,4 | 条件空/1—2D | 有效研究/2层，上限69/等待09:15/09:30且先解海外口径 |
| 4 | LH2701弱势与contango延续 | 64（16/16/10/11/11） | 1,2 | 观察空/3—10D | 有效研究/2层/非即时；等09:30 |

## 6. 研究/交易卡

### 1. CU2612｜条件多｜COM-M-CU2612-HVC-STRIKE-WATCH-20261025

- 新事实：夜盘fallback 108570，仅+0.43% vs EOD close；Teck罢工仍是供给事件。
- 已定价：EOD已涨0.81%，OI增6896；近月升水0.647%，一部分供给风险已计价。
- 分歧与PnL：若09:15后价格与曲线同步强化，市场可能尚未充分计入停产时长；若LME库存压力占优则论点失败。 CU2612突破后的方向收益；非跨市套利。
- 催化/竞争解释：1—10D：HVC停产/谈判更新、FOMC、LME库存与现货升贴水。 最强反解释：库存上升、需求担忧、罢工影响小于预期。
- 触发顺序：09:15 CU≥108800且CU2611-CU2612≥0.8%，09:30或09:45五分钟收于109000上方；二者须同时满足。
- 入场：仅在上述顺序后回踩108800—109100，40%/60%；若首个可成交价>110000放弃。
- 止损/失效：计划止损107600；曲线<0.2%持续15分钟或Teck复工消息为逻辑失效。
- 目标/时间退出：TP1 111500减半；TP2 114000；11月5日14:45时间退出。
- 好/中/坏与R：好/中/坏入场108800/108950/109100；每手5吨、tick10元=50元。至止损计划风险6000/6750/7500元；TP1毛利13500/12750/12000元，毛R 2.25/1.89/1.60；TP2 26000/25250/24500元，毛R4.33/3.74/3.27。假设往返各1 tick滑点=100元/手，佣金未知，净R待佣金后重算。
- 合约参数：SHFE CU2612；EOD 108110/108180；night fallback108570；静态5吨/手、tick10元；最后交易日2026-12-15；最低保证金5%与±3%为合约静态，不等于当日风控参数。
- 期权替代：EOD ATM108000 IV13.00% vs RV20 11.34%；无bid/ask、skew不可用，期权价差仅待询价，不称限损可执行。
- 风险预算/压力：试仓NAV 0.5%，确认后单idea≤1.25%，与紫金等铜股合并主题≤2.5%。 1个静态限幅约16,227元/手，2个约32,454元/手，未含限幅变化、保证金上调与跳空；止损不封顶。

### 2. MA701｜条件多｜COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024

- 新事实：EOD强价强仓，夜盘行情页3401，但未取得精确701-next曲线/PX同步序列。
- 已定价：EOD+4.66%且成交量z=2.10，供应扰动已被高度交易。
- 分歧与PnL：若回踩后仍守3400并由PX确认，缺口交易可延续；直接高开则赔率迅速恶化。 MA701短期趋势延续。
- 催化/竞争解释：1—3D：进口到港、伊朗装置、港口库存与PX/烯烃链同步。 最强反解释：供应故事已充分计价，海外油回落、下游利润受压导致需求破坏。
- 触发顺序：09:15 MA≥3380；随后回踩3390—3410不破，并在09:30/09:45五分钟收≥3400；同时PX612≥9750且准确MA701-next曲线为正。
- 入场：3390—3410，50%/50%；>3420不追，>3430放弃。
- 止损/失效：计划止损3330；精确曲线转负持续15分钟或PX<9600为逻辑失效。
- 目标/时间退出：TP1 3500减半；TP2 3620；10月29日14:45退出。
- 好/中/坏与R：好/中/坏3390/3400/3410；10吨/手、tick1元=10元。计划风险600/700/800元；TP1毛利1100/1000/900元，毛R1.83/1.43/1.13；TP2 2300/2200/2100元，毛R3.83/3.14/2.63。假设往返各1 tick=20元/手，佣金未知，净R待询。
- 合约参数：CZCE MA701；EOD3389/3346；night page3401；10吨/手、tick1元；库内保证金11%、限幅9%、最后交易日2027-01-14。
- 期权替代：无与MA701匹配且execution-ready的当前报价；不使用未报价期权封顶线性风险。
- 风险预算/压力：试仓NAV0.25%—0.5%；确认≤1.0%；油化工共同主题≤2.5%。 按库内9%静态限幅约301点=3010元/手，2限幅约6020元/手；实际风控参数可能调整。

### 3. SC2612｜条件空｜COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026

- 新事实：夜盘733.30相对close反而+0.71%，旧≤724首触发未到；相对settle-0.87%且外油结算回落。
- 已定价：EOD曲线已深contango -1.6899%，反转交易并非冷门。
- 分歧与PnL：若09:15跌破731且反弹失败，国内相对EOD的韧性可能消失；否则空头赔率不足。 SC2612回落的方向收益。
- 催化/竞争解释：1—2D：地缘外交/航运、EIA库存、国内开盘后套保流。 最强反解释：地缘再升级、Brent仍处高位、夜盘相对close为正。
- 触发顺序：先统一Brent合约口径；09:15 SC≤731且SC2611-SC2612≤-1.0%，随后733—737反弹失败，09:30/09:45五分钟收<731。
- 入场：仅在顺序完成后729—732，40%/60%；若首个可成交价<724不追。
- 止损/失效：计划止损741；曲线>-0.5%持续15分钟或Brent同合约>117为逻辑失效。
- 目标/时间退出：TP1 715减半；TP2 704；10月28日14:45退出。
- 好/中/坏与R：好/中/坏729/730.5/732；1000桶/手、tick0.1元=100元。计划风险12000/10500/9000元；TP1毛利14000/15500/17000元，毛R1.17/1.48/1.89；TP2 25000/26500/28000元，毛R2.08/2.52/3.11。假设往返各1 tick=200元/手，佣金未知，净R待询。
- 合约参数：INE SC2612；EOD728.1/739.7；night fallback733.30；1000桶/手、tick0.1元；最后交易日2026-11-30；动态保证金/限幅未取得。
- 期权替代：ATM740 IV68.31% vs RV20 46.69%；skew、bid/ask、execution均不可用，看跌价差仅待询价。
- 风险预算/压力：试仓NAV0.25%—0.5%；确认≤1.0%；与BU/FU/能源股合并≤2.5%。 若按未知动态限幅，1/2限幅损失不能可靠数值化；地缘gap、流动性消失和保证金上调可能超过计划止损。

## 7. 商品期权专项

- 口径：10/26 EOD，core_v1/sample strikes；45/64产品、44 ATM、27 skew。全曲面、期限结构、全链PCR、持仓拥挤与dealer gamma均不可用；dealer_gamma_direction_known=false。
- CU：ATM108000 IV13.00% vs RV20 11.34%，+1.66 vol；夜盘后moneyness需重算，skew不可用。
- SC：ATM740 IV68.31% vs RV46.69%，+21.62 vol；事件溢价显著但无成交价，不能称贵或卖波动。
- AG：ATM13000 IV39.95% vs RV30.86%，+9.09 vol；FOMC前事件凸性高，裸卖Vega回避。
- AL：ATM23400 IV11.20% vs RV11.83%，-0.63 vol，RR25=-1.15；低于RV不等于便宜。
- SA/AP：ATM IV25.18/34.30%，RR25 +1.52/-3.96；只表示局部采样偏度。
- PX：ATM9800 IV41.88%，10/28到期；无bid/ask且临近到期，Gamma/行权交割风险高，回避。
- 结构备选仅限“待询价”：CU看涨价差、SC看跌价差、FOMC前AU/AG有限损结构。取得同系列bid/ask、净成本、成交量和Delta后再验证；当前不得称限损已可执行。

## 8. 09:00开盘风险地图

- **Previous China EOD**：油化工强、SC深contango；CU价升仓增；LH/AP/EC弱。此层已反映10/26。
- **Current T Night**：会话归属合法，但raw明细为空。CU108570、MA3401、SC733.30为fallback；CU/SC均未满足旧触发，MA缺多条件顺序。
- **07:00 Overseas**：Brent/WTI结算回落；LME铜受库存上升压制；HVC罢工仍是供给催化。仓库Brent与Reuters价格冲突，禁止跨市比价。
- **潜在开盘**：CU平至小高、MA/PX小高但易兑现、SC分歧平开、AU/AG小高、LH无夜盘后弱开风险。
- **操作节奏**：09:00不追；09:15核准确价/near-next/成交；09:30核5分钟持续和跨品种；09:45再决定是否从研究转试仓。任何一项报价、曲线或海外合约未统一，继续观察。

## 9. 未来24小时/7日事件

- 今日全天：FOMC会议第一日；贵金属、铜、油和人民币均有Delta/Vega风险。
- 10月28日22:30：EIA周度石油报告；油链若有线性试仓，数据前降风险。
- 10月29日02:00/02:30：FOMC声明/发布会；警惕方向gap与IV塌陷。
- 10月30日：中国石化三季报预约；核分部利润桥，不把旧年报当新催化。
- 未来7日：HVC谈判/停产影响、地缘与航运、USDA下一期Crop Progress。10月26日USDA已发布，不再当未来催化。
- 未解决关键缺口：Night raw空、214 unresolved、Brent口径冲突、DCE官方接口失败、Options无bid/ask、Stock tape陈旧。缺口只限制依赖项，不推导全市场无机会。

## 10. 风险预算与发布校验

试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同一主题合并上限2.5%—3.0%。无NAV时：手数=`floor(NAV×预算比例/(每手计划风险+成本缓冲))`。压力覆盖1/2限幅、夜盘gap、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、汇率和中国休市海外波动；止损不保证最大亏损。

校验：三候选分项加总、证据分层上限、合约乘数/tick、情景R、交易日归属和旧观点状态已重算；MD/JSON来自同一对象。未通过/未做：Night全合约、DCE官方价格、全链期权、股票实时可交易性。CI状态：pending_or_unverified。

## 11. 来源

1. [China Commodities Engine - futures EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)：806合约/77产品/五所同日；EOD close/settlement/volume/OI。
2. [China Commodities Engine - market state](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)：1/3/5/20D、RV20、OI与曲线。
3. [China Commodities Engine - night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)：夜盘归属、覆盖、214 unresolved、发布验证状态。
4. [China Commodities Engine - options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)：45/64、1052记录、非全链、无执行报价。
5. [China Commodities Engine - options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)：44 core ATM、27 skew、局部IV。
6. [China Commodities Engine - physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)：18/20 fresh、A/B basis为0。
7. [China Commodities Engine - external](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)：17/22 context-only、仓库国际收盘。
8. [China Commodities Engine - official futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)：四所价格差异0、DCE HTTP412。
9. [SC2612夜盘快讯](https://www.cls.cn/detail/2515846)：SC2612 733.30、相对结算-0.87%；沪金+0.4%、沪银+0.31%。
10. [沪铜2026-10-27夜盘行情](https://hq.smm.cn/futures/104179481)：CU2612 108570、01:00。
11. [甲醇行情中心](https://quote.stockstar.com/futures/czcema.html)：MA701 3401、昨结3346、区间3379—3444。
12. [Oil settles lower on peace hopes](https://www.reuters.com/business/energy/oil-prices-down-almost-1-early-trading-2026-10-25/)：Brent115.81 -0.8%、WTI101.76 -1.46%。
13. [Teck HVC strike notice](https://www.teck.com/news/news-releases/2026/teck-receives-highland-valley-copper-operations-strike-notice)：HVC罢工通知与最早启动时间。
14. [SHFE copper contract](https://www.shfe.com.cn/products/futures/metal/nonferrousmetal/cu_f/standard_cu_f/202312/t20231205_331277.html)：CU 5吨/手、tick10元、静态最低保证金5%、静态限幅3%。
15. [INE crude oil contract](https://www.ine.cn/products/futures/energyandchemical/)：SC 1000桶/手、tick0.1元。
16. [CZCE methanol contract](https://www.czce.com.cn/cn/sspz/jc/bzhy/qhhy/H077002008001001index_1.htm)：MA 10吨/手、tick1元。
17. [USDA Crop Progress](https://data.nass.usda.gov/Publications/Reports_by_Release_Day/)：本周报告已于10月26日发布。
18. [FOMC calendars](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)：10月27—28日FOMC会议。
19. [EIA weekly petroleum schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)：周度石油状态报告发布时间。
20. [SSE periodic report reservation](https://www.sse.com.cn/disclosure/listedinfo/periodic/)：公司定期报告预约核查入口。
21. [China Stock Engine manifest](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json)：Stock数据日期与研究能力范围。

## 12. 最终行动

A. 今天没有应立即建立的新仓位。
B. 仅挂条件：CU2612突破回踩多、MA701回踩确认多、SC2612跌破反抽失败空；全部须在09:15/09:30重新核精确合约与曲线。
C. 继续观察：LH2701趋势空、AG2612修复、SA701反弹、AP701/EC2611弱势，以及所有未能取得精确夜盘的品种。
D. 必须回避：追高油化工、用旧期权EOD当当前报价、把vendor snapshot称官方夜盘收盘、把DCE或Stock缺数据解释成无机会；若已自行建仓，按各卡逻辑失效与时间退出独立处理。
