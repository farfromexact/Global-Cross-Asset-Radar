# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-22

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:18 BJT；信息截点：07:00。最近完整中国EOD为9月21日；9月22日Night Session已完成，下一实际交易窗口为今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；外油与中国夜盘共同确认能源—聚酯弱势，但低开追空赔率差，只等SC、TA反抽失败。**

当前regime：原油供应风险溢价继续压缩，能源—聚酯链承压；橡胶与油脂相对强，人民币偏强、美元与高利率压制贵金属。最接近触发的是SC2611、TA701反抽失败空，以及OI701回撤接受多；三者均须等09:30后确认。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻EOD、Physical、External、Options quality/surface及合约元数据。

- 统一输入：`requested_date=2026-09-21`，9月22日06:16:52生成。
- Futures：9月21日五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；7条占位记录排除。
- Market State：77产品完成初筛；76个具备有效日收益/量仓，约68个具备可比较多周期与curve；roll或短历史不强行输出不存在的5D/20D。
- Physical：18/20序列按原生频率有效，SC/LU不可得；CZCE仓单为当日数据，GFEX部分为沿用。全部basis为C级或缺失，只作背景，不计方向证据。
- External：17/22序列在自身频率下有效，均为`context_only`；repo原油代理与可核实近月价格冲突，已经隔离。
- Options：最新可用研究截面仍为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖为0。9月21日底层已变化，因此旧Delta、moneyness与skew只作历史背景。
- Metadata：partial；有效合约匹配73.45%，multiplier/tick覆盖36.10%，margin/price-limit约30.15%，last-trading-day覆盖73.45%。

### Night Session质量闸门

Night原始字段为：`trading_date=2026-09-22`、`night_session_date=2026-09-21`、06:01:25生成，`data_fresh=true`、`validation_passed=true`、`published=true`。取得423个有效合约、37个产品；outside-window 165、no-night-trade 4、missing timestamp/price/quote均为0。

但`coverage_complete=false`，有214个query error与214个unresolved concrete contracts；这是真实覆盖缺口，主要限制DCE及部分非代表月份。大文件通过connector返回紧凑层不足，状态为“读取受限/需紧凑输入”，**不是源文件为空**。正式卡使用统一输入中的同一具体合约Night记录；由于near-next两腿明细不可完整回读，本期不强拼Night curve。

## 三、商品仪表盘

Basis均为C级或缺失；Physical栏只有具备方向变化或明确产业意义时才计支持。Night收益以昨收为主、昨结为辅。

| 板块 | 品种/合约；EOD close/settle；1D/5D | Vol/OI/ΔOI；EOD curve | Physical | Night close；vs close/vs settle；ΔOI；时间 | 07:00海外/期权S-P-E | 信号 |
|---|---|---|---|---|---|---|
| 原油 | SC2611；722.5/730.8；-3.13%/-5.89% | 26.17万/4.10万/-1,256；Back 1.09% | 缺失 | 714.3；-1.13%/-2.26%；+858；02:30 fresh | Brent 100.34收盘；Y/N/N | 反抽失败空，不追低开 |
| 燃料 | FU2611；4213/4226；-0.77%/-3.18% | 77.26万/18.70万/-3,940；Back 17.06% | C级现货 | 4122；-2.16%/-2.46%；-3,581；23:00 fresh | 柴油仍紧；Y/N/N | 深back反对追空 |
| 燃料 | LU2611；5429/5481；-0.62%/-0.42% | 15.63万/6.92万/-2,219；Back 5.04% | 缺失 | 5361；-1.25%/-2.19%；-4,882；23:00 fresh | 原油弱；N/N/N | 相对SC未强化 |
| 聚酯 | TA701；6282/6258；-0.86%/-2.16% | 113.79万/116.70万/-4,264；Back 2.52% | C级现货 | 6216；-1.05%/-0.67%；-8,183；23:00 fresh | 油价下行；Y/Y/N | 反抽失败空 |
| 化工 | PL611；9027/9125；-0.44%/N/A | 可用量仓；Back 3.61% | C级/仅背景 | 8817；-2.33%/-3.38%；-377；23:00 fresh | 成本下行；N/N/N | 跌幅已大，不追 |
| 橡胶 | BR2611；14705/14845；+1.06%/N/A | 20.28万/9.39万/+1,962；Back 0.91% | C级/仅背景 | 14895；+1.29%/+0.34%；+4,267；23:00 fresh | 海外映射不完整；N/N/N | 回撤接受多观察 |
| 油脂 | OI701；10205/10186；+0.72%/-0.06% | 22.46万/28.51万/+15,799；Back 1.63% | C级；仓单0变化 | 10270；+0.64%/+0.82%；+7,625；23:00 fresh | 加菜油映射不足；N/N/N | 相对最强，等回撤 |
| 有色 | CU2610；110180/109960；+0.39%/+1.64% | 6.44万/14.79万/-3,953；Back 0.40% | C级现货 | 110700；+0.47%/+0.67%；+340；01:00 fresh | 人民币偏强；N/N/N | 温和确认，不追 |
| 纸浆 | SP2611；4978/4938；+3.05%/+3.05% | 68.06万/20.60万/+5,349；Contango 0.04% | C级现货 | 4978；0.00%/+0.81%；+1,753；23:00 fresh | 缺同口径海外映射；Y/Y/N | Night弹性归零 |
| 建材 | FG701；923/916；+0.44%/-2.97% | 123.30万/127.29万/-22,222；Back 4.43% | C级；仓单-375 | 924；+0.11%/+0.87%；-2,040；23:00 fresh | 实体不足；Y/Y/N | 单日反弹噪音 |
| 菜粕 | RM701；2341/2347；-1.76%/N/A | 40.81万/63.70万/+28,731；Contango 1.53% | C级；仓单-1,728 | 当前合约缺失；RM611代表价不可比 | CBOT仅背景；Y/Y/N | 不用跨月代表价 |
| 贵金属 | AG2612；16140/16246；+0.88%/+3.14% | 14.86万/22.49万/+9,918；Contango 0.15% | C级/仅背景 | 当前合约缺失；AG2610代表价不可比 | 金4349.94、银65.99收盘；Y/N/N | 海外转弱，旧多降级 |
| 航运 | EC2610；2197/2167.5；-0.98%/+2.53% | 1.06万/2.36万/-1,721；Back 23.28% | exact运价缺失 | 制度上无Night | 无可执行映射；N/N/N | 09:00首次定价 |

截至07:00可核实的最新海外层是周一美国时段收盘，而非同分钟实时报价：Brent 100.34美元/桶、WTI 95.78美元/桶，分别下跌约3.4%和4.5%；沙特装运增加和外交预期压低供应风险溢价，但全球柴油价格仍在高位，反对把原油下跌等同于产品端全面宽松。[油价收盘](https://www.wsj.com/world/middle-east/oil-prices-fall-for-fourth-day-as-supply-concerns-ease-f2583983)｜[沙特出口](https://www.reuters.com/business/energy/saudi-arabia-ramps-up-gulf-oil-exports-after-pipeline-attack-shipping-data-shows-2026-09-21/)｜[柴油市场](https://www.reuters.com/business/energy/global-diesel-prices-hit-record-highs-further-rises-possible-2026-09-21/)

黄金现货约4349.94美元/盎司、白银65.99，分别回落约0.6%和0.4%；DXY约100.23，美元偏强与升息预期压制贵金属。人民币在岸/离岸约6.6950/6.6946，人民币偏强对人民币计价进口商品构成温和抑制，但未做精确归因。[贵金属](https://www.reuters.com/world/india/gold-eases-firmer-dollar-profit-taking-mideast-conflict-focus-2026-09-21/)｜[人民币与美元](https://www.reuters.com/world/asia-pacific/yuan-hits-fresh-multi-year-peak-pboc-eases-curb-ahead-trump-xi-summit-2026-09-21/)

## 四、相比上一期真正变化

1. **9月21日EOD确认原油链弱化。** SC结算跌3.13%，curve back压至1.09%；EC事件gap多未触发原条件，日内最高2205未重上2220，旧条件已过期。
2. **9月22日Night继续给出负价格弹性。** SC、FU、TA相对昨收再跌1.13%、2.16%、1.05%；相对昨结跌幅更大主要因为日盘close已低于settlement，不能把两者差额误当夜盘新增跌幅。
3. **产品端并非全面强于原油。** LU/SC由EOD约7.514降至Night约7.505；旧“多LU/空SC”条件是否盘中触发无法由session OHLC验证，状态记为未知，不假设成交。
4. **最强转向OI与BR。** OI价涨仓增、Night再涨且增仓；BR白天与Night同向上行。两者只有价格/curve两层，尚不足70分。
5. **SP的白天动量未获Night确认。** Night close恰等于昨收，说明新增价格弹性归零；不追白天3%涨幅。
6. **海外继续确认原油风险溢价回吐，贵金属转弱。** 这强化SC/TA方向，却也让09:00低开追空的赔率下降；AG旧多由等待触发降为观察。

旧建议台账：`COM-M-SC2611-REVERSAL-20260917`由双向观察恢复为空头研究，但原728—735入场窗已过期并重设；`COM-E-TA701-COST-UNWIND-20260918`延续，Night路径不足使触发未知；`COM-M-LUSC-RELATIVE-20260918`降级；EC与AG旧多条件均未确认触发。没有成交反馈，不假设用户持仓。

## 五、产业链地图

- **最弱：SC—FU—PL—PX—TA—PF—PR，偏空、置信度中高。** EOD、Night及海外原油同向，SC curve同步压缩；反证是FU深back、全球柴油紧张以及实体数据缺失。
- **最强：BR—RU—NR橡胶链，偏强、置信度中。** BR价仓与Night同向，RU/NR亦偏强；curve支持有限，缺库存、轮胎开工与境外exact映射。
- **油脂强于饲料，置信度中。** OI价仓与Night同向，M/RM白天弱；DCE Night缺口、高质量basis与进口利润不足，不能构造跨市场套利。
- **有色温和偏强，置信度中低。** CU/BC Night上涨但幅度有限，人民币偏强构成反向作用；库存和LME—中国全成本平价未闭环。
- **航运/建材/新能源无三层共振。** EC深back但价跌减仓且无Night；FG反弹减仓；LC白天反弹却缺Night和实体确认，均不入正式候选。

## 六、机会排行榜

| 排名 | 候选/idea_id | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 有效支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2611反抽失败空 / COM-M-SC2611-REVERSAL-20260917 | 23/16/17/13/8 | **77** | 1、2、4 | 存在待验证优势｜部分充分；柴油紧与实体缺失反对｜等09:30触发 |
| 2 | TA701成本回吐空 / COM-E-TA701-COST-UNWIND-20260918 | 20/15/14/11/9 | **69** | 1、4 | 存在待验证优势｜部分；back反对｜等反抽失败 |
| 3 | OI701趋势回撤多 / COM-M-OI701-TREND-20260922 | 19/14/12/11/10 | **66** | 1、2 | 存在待验证优势｜部分；实体/海外缺失｜等09:30 |
| 4 | 多LU2611/空SC2611 / COM-M-LUSC-RELATIVE-20260918 | 20/14/12/10/8 | **64** | 2、4 | 优势减弱｜部分；Night比值未强化｜等待重新报价 |
| 5 | BR2611相对强势多 / COM-M-BR2611-RELATIVE-STRENGTH-20260922 | 18/14/11/10/10 | **63** | 1、2 | 存在待验证优势｜部分；实体缺失｜等回撤 |

分项均已复算并遵守证据层封顶。分数仅用于研究排序，不是胜率、预期收益或仓位指令；所有期货结构的最大损失都不由计划止损限定。

## 七、前三名研究卡

### 1. SC2611反抽失败空｜77

事实：昨收/昨结722.5/730.8；Night OHLC 715.1/719.5/705.4/714.3，相对昨收-1.13%、昨结-2.26%，Night ΔOI +858。EOD back 1.09%。海外油价继续下跌。

市场可能隐含供应风险继续消退；我们的分歧不是“油价一定跌”，而是认为反抽若无法收复714—723，风险溢价仍有再压缩空间。最强反证是柴油紧张、FU深back及新的设施损害。最佳表达为条件触发后的SC期货空，而非旧截面期权。

- 好成交：09:30后反抽716—723失败，重新跌回714/VWAP下方，试1/3风险；允许滑点不超过2 ticks。
- 中成交：先破705.4，再反抽708—712失败，半风险。
- 坏成交：直接低于700、滑点超过4 ticks或盘口深度不足，放弃。
- 止损：30分钟接受728上方；逻辑失效为重上730.8且curve back扩张、Brent重上102，或出现新增供应损害。
- TP1 705或+1.5R；TP2 690或+3R；1—3D无扩张退出。分批为1/2在TP1、1/4在+2R、余仓跟踪。
- 风险：0.15%—0.25% NAV；能源—化工同因子合并≤0.50%。期货止损不能防gap。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；按Night close名义约714,300元。动态margin/price limit未由repo确认；若限幅为L，一板空头压力损失约`714,300×L`，两板约`714,300×[(1+L)^2−1]`。最后交易日2026-10-30、交割终止2026-11-06，10月中旬前必须移仓或退出。

### 2. TA701成本回吐空｜69

事实：昨收/昨结6282/6258；Night 6264/6294/6180/6216，相对昨收-1.05%、昨结-0.67%，Night ΔOI -8,183。弱价与减仓只能作为归因线索，不能断言资金身份。EOD back 2.52%反对激进追空。

市场已经计入部分成本下行；我们的分歧是若反抽无法收复6258—6294，聚酯链可能继续向下重估。最强反证是原油反弹或TA back显著扩张。选择期货是因为期权execution-ready=false。

- 好成交：09:30后反抽6225—6260失败并跌回6216/VWAP下方；允许滑点≤2 ticks。
- 中成交：跌破6180后反抽6200—6220失败，半风险。
- 坏成交：直接低于6150、滑点>4 ticks或PX/TA同步转强，放弃。
- 止损：30分钟接受6294上方；失效为重上6332、back扩至4%以上且外油/PX同步上行。
- TP1 6120或+1.5R；TP2 6000或+3R；1—3D时间止损；TP1后回补一半。
- 风险：0.15%—0.20% NAV；与SC、PX、PR合并≤0.50%。
- 参数：5吨/手，tick 2元/吨，tick value 10元；Night名义约31,080元，margin 7%、price limit 6%。空头一板不利上行压力约1,865元/手，两板复合约3,842元/手；最后交易日2027-01-14、交割终止2027-01-19。进入交割月前退出。

### 3. OI701回撤接受多｜66

事实：昨收/昨结10205/10186；Night 10226/10288/10221/10270，相对昨收+0.64%、昨结+0.82%，Night ΔOI +7,625；EOD back 1.63%。价格与持仓同向只说明归因线索，不识别“新多”。

市场可能已计入菜油相对强势；我们的分歧是若10220—10270获得接受，油脂可能继续相对饲料走强。反证是进口利润、库存和DCE Night缺失，不能做跨市场或跨品种确认。

- 好成交：09:30后10220—10260承接并重上10270/VWAP；允许滑点≤2 ticks。
- 中成交：突破10288后回踩10260—10288不破，半风险。
- 坏成交：直接高于10400、跌破10180或盘口深度不足，放弃。
- 止损：30分钟接受10180下方；失效为跌破10117、back显著收窄且EOD ΔOI转负。
- TP1 10380或+1.5R；TP2 10520或+3R；1—5D无扩张退出；TP1减半。
- 风险：0.15%—0.20% NAV；油脂共享风险≤0.40%。
- 参数：10吨/手，tick 1元/吨，tick value 10元；Night名义约102,700元，margin 7%、price limit 6%。多头一板不利下跌压力约6,162元/手，两板复合约11,954元/手；最后交易日2027-01-14、交割终止2027-01-19，进入交割月前退出。

## 八、商品期权专项

最新可用截面是9月17日，已落后于9月21日EOD和9月22日Night；以下仅为历史研究背景，不是当前可成交报价。

| Underlying/expiry | 历史ATM IV / 当前RV20 | 历史IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/58.55% | +7.02vol | +0.73/+1.41 | Y/N/N | 旧事件vol仍高，须重报 |
| FU2611/10-19 | 60.62%/45.38% | +15.24vol | -0.50/+1.42 | Y/N/N | 裸买Vega历史成本高 |
| TA701/12-11 | 31.87%/28.09% | +3.78vol | +2.43/+0.72 | Y/Y/N | 旧Delta不可执行 |
| AG2612/11-24 | 44.14%/30.70% | +13.44vol | 形状异常 | Y/N/N | skew隔离 |
| SP2611/适用series | 15.57%/16.90% | -1.33vol | +2.91/+1.23 | Y/Y/N | IV<RV不单独证明便宜 |

没有可证明优于裸期货的期权结构。取得实时双边报价后才能比较SC put spread、TA put spread或OI call spread，并重算执行价、Delta、净支出、盈亏平衡、Greeks、滑点和行权交割。Dealer Gamma方向未知；event convexity不能由旧IV-RV单独确认。

## 九、09:00开盘风险地图

三层严格区分：①9月21日中国完整EOD；②归属9月22日、已经完成的Night Session；③截至07:00最新可核实海外收盘。Night并不是09:00之后的未来行情。

| 品种 | 三层合成/预期开盘 | Night是否已定价 | 追价 | 等待 | 开盘后确认 |
|---|---|---|---|---:|---|
| SC | EOD弱、Night再跌、外油跌；偏低开 | 大部分已定价 | 否 | 30—45m | 705.4/714/723、curve、Brent |
| FU/LU | Night弱但深back/产品紧；偏低开分化 | 部分 | 否 | 45m | FU back、LU/SC 7.50、成交深度 |
| PX/TA/PF/PR/PL | 成本链同向弱；偏低开 | 多数已定价 | 否 | 30—45m | 6180/6216/6258、链内breadth |
| BR/RU/NR | Night相对强；偏高开 | 部分 | 否 | 30m | BR14895/15090、curve、OI |
| OI | EOD与Night同向强；偏高开 | 较多 | 否 | 30m | 10220/10270/10288、OI |
| CU/BC | 温和高开，人民币偏强反对 | 部分 | 否 | 30m | 110700、LME、USD/CNH |
| AG/AU | 中国具体主力Night缺失、海外金银回落 | 无法判断 | 否 | 45m | exact contract、外金银、DXY |
| SP | 白天大涨、Night零弹性；平开 | 已消化 | 否 | 30m | 4978、量仓、curve |
| M/RM等DCE | EOD偏弱，Night exact缺失 | 否 | 否 | 45m | 首次量仓、near-next、CBOT |
| EC/LC等无Night | 09:00首次有效定价 | 否 | 否 | 45m | EC2167/2197、LC131080、盘口 |

单日噪音：SP白天涨幅未获Night扩张；FG反弹伴减仓；CU温和上涨但EOD减仓。最不值得交易的是09:00追空已连续下跌的FU/PL/TA，以及用不可比RM611或AG2610代表价替代正式合约。

## 十、未来24小时与7天事件

- 9月22日09:00：中国日盘；能源—化工等待30—45分钟，不把Night跌幅重复追价。
- 9月22日：美国汽柴油零售价格周报更新；只把实际发布值作为炼化背景。[EIA汽柴油](https://www.eia.gov/petroleum/gasdiesel/)
- 9月23日22:30：EIA周度石油数据；能源仓在数据前降低Delta，只有取得实时双边报价时才考虑有限净支出Vega。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)
- 9月23—25日：中美领导人会晤窗口及稀土议题，人民币、有色和战略矿产存在政策gap；不开会前方向赌注。[人民币与峰会](https://www.reuters.com/world/asia-pacific/yuan-hits-fresh-multi-year-peak-pboc-eases-curb-ahead-trump-xi-summit-2026-09-21/)｜[稀土议题](https://www.reuters.com/world/china/rare-earths-force-trump-be-less-hostile-before-xi-summit-2026-09-21/)
- 未来一周：USDA出口销售、北美收割天气、中国采购及马棕出口；仅以实际数据和国内响应调整油脂饲料。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- CFTC持仓只作滞后拥挤背景，不用于确认今日日内方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 截至截点未确认未来7天有新的OPEC+/IEA正式决策会议；不把例行预期写成确定催化。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态扩展后77产品；期权64产品。
- 实际取数且已分析：77产品均进入EOD初筛，76个有有效日价仓、约68个具备可比较多周期/curve；Night取得37产品、423具体合约；期权45产品、216 series有历史研究截面。
- 数据不足：DCE及214个Night具体合约、19个期权产品、全部实时期权bid/ask、SC/LU实体、A/B级basis、exact进口平价、可靠加工利润，以及Top候选near-next Night curve。
- 不适用/流动性不足：JR、PM、RI、WH、ZC为占位；RS/WR历史或流动性不足；EC/LC等制度上无Night。均保留扫描状态，未默默删除。
- 未入榜板块：黑色/建材仅FG弱反弹减仓，无三层共振；有色仅温和上行；新能源LC反弹缺实体与Night；农产品中M/RM弱但DCE Night缺；航运EC深back与价跌减仓冲突。
- 策略覆盖：方向、跨期、curve、跨品种、跨市场代理、近似名义中性、波动率/偏度和事件凸性均已扫描；没有全口径import parity或beta-neutral模型，不伪称套利。
- 风险预算：单笔试仓0.15%—0.25% NAV；取得价格、curve及非价格层确认后才可提升至0.75%；SC/TA等能源—化工同因子合并≤0.50%，单一主题总风险≤2.5%。压力测试包含一/两板、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳变、交割挤压和人民币急变。

固定六路径已提交main；回读核对完成后以归档状态为准，CI为push后的独立验证，不等待。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2611仅在09:30后反抽716—723失败并跌回714/VWAP下方时试空；TA701仅在反抽6225—6260失败并跌回6216/VWAP下方时试空，二者按能源—化工同因子合并风险。  
C. 今天应继续观察的机会：OI701回撤接受多、LU2611/SC2611重新确认比值与Night curve、BR2611相对强势，以及EC、LC和DCE品种09:00首次有效定价。  
D. 今天必须避免或退出的交易：低开追空SC/FU/PL/TA、追BR/OI第一跳、恢复AG或SP旧多、把RM611代表价替代RM701、把C级basis或连续外盘代理称套利，以及在execution-ready=false时臆测期权成本。