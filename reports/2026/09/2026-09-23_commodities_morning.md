# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-23

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：07:10 BJT；信息截点：07:00。最近完整中国EOD为9月22日；归属9月23日的Night Session已完成，下一交易窗口为今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC与聚酯链获Night和外油共振确认，但跌幅已大，09:00不追空，只做反抽失败或CU回撤接受。**

当前regime：原油供应风险溢价继续快速压缩，能源—聚酯链偏弱；基本金属相对强，美元偏强压制贵金属，国内实体与高质量basis仍不足。

最接近触发的三项：

1. CU2611回撤接受多：等09:30后110700—111000承接及LME同步。
2. SC2611反抽失败空：等09:30后700—708反抽失败，不追低开。
3. TA701反抽失败空：等09:30后6175—6204反抽失败，且PX链同步。

## 二、数据质量与覆盖

本期读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻EOD、Physical、External、Options和合约元数据。

- 统一输入：schema v2，`requested_date=2026-09-22`，9月23日06:17:35生成。
- Futures：06:06:54生成；五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；8条placeholder排除。
- Market State：77产品完成全量初筛；可比较多周期、量仓和curve的记录按roll flag逐项降级，未拼接不同主力。
- Physical：18/20序列在原生频率下有效，SC/LU不可得；仓单仅CZCE更新，SHFE/DCE/GFEX刷新失败，5项沿用。所有basis均为C级或缺失，只作context。
- External：17/22序列按原生频率有效，均为`context_only`；repo WTI/Brent连续代理与可核实近月报价冲突，已隔离。
- Options：最新可发布截面仍为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖为0。9月22日原始采集未形成可发布曲面，不能冒充T日IV。
- Contract Metadata：partial；有效合约匹配73.45%，multiplier/tick/margin/limit约30.15%，DCE元数据失败、GFEX source date未核实。

Night字段为`trading_date=2026-09-23`、`night_session_date=2026-09-22`，06:02:03生成；`data_fresh=true`、`validation_passed=true`、`published=true`。取得423个有效合约、37产品；missing timestamp/price/quote均为0。由于214个query error及214个unresolved concrete contracts，`coverage_complete=false`，主要限制DCE和部分非代表月份。大文件通过connector紧凑读取受限，属于读取截断，不是源文件为空；未强拼缺腿Night curve。

## 三、商品仪表盘

1D/5D为同合约结算收益；curve正值为backwardation。Night收益以昨收为主、昨结为辅；`S/P/E`分别是surface/positioning/execution readiness。

| 板块 | 品种/合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；curve；实体 | Night O/H/L/C；vs close/vs settle；ΔOI | 07:00海外/期权；信号 |
|---|---|---|---|---|---|
| 能源 | SC2611 | 724/717.1；-1.87%/-14.24% | 17.69万/4.01万/-842；back 4.11%；实体缺 | 700.6/710.6/680/694.8；-4.03%/-3.11%；+167；02:30 fresh | Brent约97.44；Y/N/N；反抽失败空 |
| 燃料 | FU2611 | 4253/4184；-0.99%/-6.65% | 69.43万/19.44万/+7,417；back 26.48%；C级spot | 4120/4185/4057/4162；-2.14%/-0.53%；-11,798；23:00 fresh | 产品紧；Y/N/N；深back不追空 |
| 低硫 | LU2611 | 5450/5391；-1.64%/-4.14% | 10.91万/6.32万/-6,027；back 4.79%；实体缺 | 5301/5449/5242/5427；-0.42%/+0.67%；+1,825；02:30 fresh | 相对SC明显强；N/N/N；等比值回撤 |
| 聚酯 | TA701 | 6274/6262；+0.06%/-2.70% | 112.02万/117.82万/+11,255；back 3.29%；C级basis | 6180/6204/6126/6162；-1.79%/-1.60%；-57,523；23:00 fresh | 外油下跌；Y/Y/N；反抽失败空 |
| 聚酯 | PF611 | 8304/8328；-0.22%/N/A | 22.77万/22.36万/-2,236；back 1.71%；仓单0 | 8154/8188/8064/8108；-2.36%/-2.64%；-8,991；23:00 fresh | 链内共振；Y/N/N；不追低开 |
| 沥青 | BU2611 | 5098/5106；-4.24%/-3.28% | 73.61万/26.19万/-23,507；back 12.89%；实体不足 | 4979/5100/4954/5079；-0.37%/-0.53%；+10,645；01:00 fresh | 对SC跌势弹性弱；Y/Y/N；旧空降级 |
| 有色 | CU2611 | 110750/110710；+1.09%/+3.97% | 7.10万/16.01万/+12,859；back 0.46%；C级basis、roll | 111200/111230/110930/111060；+0.28%/+0.32%；+3,965；01:00 fresh | COMEX铜约+0.5%；Y/Y/N；回撤接受多 |
| 贵金属 | AG2612 | 15949/16123；-0.76%/+4.29% | 15.87万/23.15万/+6,574；contango 0.13% | 代表合约AG2610，不可替代；产品层约+2.29% | 外金小跌、银近持平；Y/N/N；冲突观察 |
| 有色 | NI2611 | 124930/124460；+0.57%/N/A | 9.33万/13.78万/-7,290；contango 0.19% | 125910/126460/125780/126030；+0.88%/+1.26%；-3,302；01:00 fresh | exact海外映射不足；早期异常 |
| 不锈钢 | SS2611 | 13745/13750；+0.33%/N/A | 11.90万/12.86万/-2,718；轻contango | 13805/13920/13800/13880；+0.98%/+0.95%；-7,757；01:00 fresh | 镍共振但减仓；Y/Y/N；不追 |
| 油脂 | OI701 | 10218/10243；+0.56%/N/A | 19.97万/28.63万/+1,181；back 1.49%；仓单持平 | 10194/10199/10156/10174；-0.43%/-0.67%；-5,149；23:00 fresh | 强势未延续；Y/N/N；旧多降级 |
| 航运 | EC2610 | 2265/2199；+1.45%/+6.31% | 1.42万/2.34万/-152；back 20.35%；exact运价缺 | 制度上无Night | 海外船流仅context；无成熟链；09:00首次定价 |

FU的Night相对昨收-2.14%，但相对昨结仅-0.53%：昨收本已高于结算，不能把全部差额称为夜盘新增空头信息。相反，SC相对双锚均显著下跌，价格弹性更可信。BU只跌0.37%，显示沥青未跟随SC的第二轮下杀。

截至07:00可核实的海外近月油价进一步下行：Brent约97.44美元/桶、WTI约90.42美元/桶，约跌3%并创两周低位；Saudi East-West管道以较低流率重启，支持供应溢价压缩，但柴油紧张仍反对把产品端视为全面宽松。[Reuters管道重启](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)｜[油价最新](https://www1.folha.uol.com.br/mercado/2026/09/petroleo-cai-mais-de-3-volta-a-ficar-abaixo-de-us-100-e-tem-menor-valor-em-duas-semanas.shtml)

COMEX 9月黄金结算约4338.90美元/盎司、跌0.16%，白银65.932、涨0.16%，铜上涨约0.5%；DXY约100.5。金银没有形成清晰同向避险，美元偏强是反证。[WSJ金属收盘](https://www.wsj.com/finance/commodities-futures/gold-rises-as-strong-fundamentals-support-9f92da11)｜[Reuters美元](https://www.reuters.com/world/asia-pacific/yen-squeezed-hawkish-turn-grips-central-banks-2026-09-22/)

## 四、相比上一期真正变化

1. SC夜盘相对昨收再跌4.03%，外油同步跌约3%；这是EOD→Night→海外的方向共振，但SC已从9月中旬高位快速回撤，09:00追空赔率恶化。
2. LU/SC比值由EOD 7.5276升至Night 7.8115，约扩张3.77%。相对价值逻辑获确认，却已越过昨晚理想成交区，转为等待回撤。
3. 聚酯链TA/PX/PF/PR/PL Night相对昨收分别约-1.79%/-1.74%/-2.36%/-2.17%/-2.12%，链内breadth强化；大幅减仓和backwardation反对低开追空。
4. BU旧空条件未触发：Night高点5100低于原5150入场区，且相对SC表现更强；`COM-E-BU2611-FADE-20260922`降级并废止旧锚。
5. CU日盘价涨仓增、轻back，Night再涨0.28%且OI增加，外铜约+0.5%；由观察升级为70分候选，但roll flag、实体缺失和交易参数不全阻止立即执行。
6. `COM-E-EG2611-FADE-20260922`的DCE exact Night缺失，触发状态未知；`COM-E-CU2611-PULLBACK-20260922`昨夜未回到旧入场区，旧条件未触发，改用今日新锚。未收到成交反馈，不假设持仓。

## 五、产业链地图

- **绝对最弱：SC—PX—TA—PF—PR—PL，置信度中高。** EOD、Night和海外油价同向；SC与聚酯链获得价格层和外部层确认。反证是FU/BU深back、产品紧张、减仓以及实体缺失。
- **相对最强：LU/FU相对SC，置信度中。** LU/SC比值Night大幅扩张，FU back达26.48%；但比值已过度扩张，缺exact crack、SC/LU实体和可执行期权。
- **基本金属偏强，CU优于NI/SS，置信度中。** CU价仓、curve、Night与外铜同向；NI/SS Night上涨但减仓，实体和进口平价均不足。
- **贵金属冲突，置信度低至中。** AG代表Night偏强但正式AG2612不可比；外金偏弱、外银近持平、DXY偏强，黄金信用主题本期不成立为单向交易。
- **油脂、航运、新能源无三层共振。** OI夜盘反转走弱；EC价涨减仓且无exact运价；LC/PS虽日盘反弹但仓单陈旧、无Night。

## 六、机会排行榜

| 排名 | 候选 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | CU2611回撤接受多 | 21/16/13/11/9 | **70** | 1、2、4 | 存在待验证优势｜部分充分｜等09:30及参数 |
| 2 | SC2611反抽失败空 | 21/13/15/11/9 | **69** | 1、4 | 存在待验证优势｜部分、深back反对｜等09:30 |
| 3 | TA701成本回吐空 | 20/14/15/10/9 | **68** | 1、4 | 存在待验证优势｜部分、减仓/back反对｜等反抽 |
| 4 | 多13手LU2611/空1手SC2611 | 20/13/14/11/9 | **67** | 1、4 | 优势存在但过度扩张｜部分｜等比值回撤 |
| 5 | PF611链内弱势空 | 18/13/14/10/9 | **64** | 1、4 | 存在待验证优势｜部分、实体缺失｜等待触发 |

所有分项已复算并遵守支持层封顶。分数仅为研究排序，不是胜率或仓位指令；所有期货最大损失均不由计划止损限定。

## 七、前三名研究卡

### 1. CU2611回撤接受多｜70

- 事实：昨收/昨结110750/110710；Night O/H/L/C为111200/111230/110930/111060，相对昨收+0.28%、昨结+0.32%，ΔOI +3,965。EOD价涨仓增、back 0.46%，COMEX铜约+0.5%。
- 市场定价：已计入一部分海外铜强势；分歧在于国内价仓与Night持续性可能强于美元逆风。
- 最强反证：主力roll flag、C级basis、实体与exact进口平价不足，DXY约100.5。
- 好成交：09:30后110700—111000承接并重上111060/VWAP，先用1/3风险。
- 中成交：突破111230后回踩111000—111230不破，以半风险表达。
- 坏成交：直接高于112000、跌破110500或盘口深度不足，放弃。
- 止损：30分钟接受110400下方。跌破110070、curve转contango且LME铜同步转弱，逻辑失效。
- TP1 112300或+1.5R；TP2 114000或+3R；1—5D无扩张退出。
- 风险0.15%—0.20% NAV；有色共享风险≤0.40%。最大损失不由结构限定。
- 合约参数：repo未完整确认multiplier、tick、动态margin/limit，**补齐前不可下单**；最后交易日11月16日、最后交割日11月18日，10月下旬开始复核移仓。无法可靠计算一至两个涨跌停压力损失。

### 2. SC2611反抽失败空｜69

- 事实：昨收/昨结724/717.1；Night 700.6/710.6/680/694.8，相对昨收-4.03%、昨结-3.11%，ΔOI +167。海外Brent约97.44。
- 市场定价：供应溢价快速压缩；我们的分歧只在反抽若不能收复700—708，仍可能继续压缩，而不是无条件追空。
- 反证：EOD back仍4.11%、产品端紧张、新增设施损害或外交反复。
- 好成交：09:30后反抽700—708失败并重新跌回694.8/VWAP下方。
- 中成交：先破680，仅在回抽685—692失败时半风险跟随。
- 坏成交：直接低于675、重上710.6或滑点超过计划1R的20%，放弃。
- 止损：30分钟接受710.6上方。重上717.1、back重新扩张且Brent重上100.5，或确认新增供应损害，逻辑失效。
- TP1 680或+1.5R；TP2 660或+3R；1—3D无扩张退出。
- 风险0.15%—0.20% NAV；能源—化工共享风险≤0.50%。若LU/SC相对结构触发，不叠加满额SC空。
- 乘数1,000桶/手、tick 0.1元/桶、tick value 100元，Night名义约694,800元；动态margin/limit未确认。最后交易日10月30日、最后交割日11月6日，10月中旬前移仓或退出。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 涨跌停压力：因当前动态限幅未确认，不编金额；必须按经纪端当日参数单独测试一板、两板和流动性消失。

### 3. TA701成本回吐空｜68

- 事实：昨收/昨结6274/6262；Night 6180/6204/6126/6162，相对昨收-1.79%、昨结-1.60%，ΔOI -57,523。PX、PF、PR、PL同向下跌。
- 市场定价：已计入较多原油成本回落；我们只交易反抽不能收复6175—6204，不把减仓解释为新增空头。
- 反证：EOD back 3.29%、实体缺失、大幅减仓和原油急反弹。
- 好成交：09:30后反抽6175—6204失败并跌回6162/VWAP下方。
- 中成交：跌破6126后回抽6135—6160失败，半风险。
- 坏成交：直接低于6080、PX/TA同步转强或深度不足，放弃。
- 止损：30分钟接受6225上方。重上6262、back扩至4%以上且外油/PX同步上涨，逻辑失效。
- TP1 6100或+1.5R；TP2 6000或+3R；1—3D时间止损。
- 风险0.15%—0.20% NAV；与SC/PF合并≤0.50%。
- 乘数5吨、tick 2元、tick value 10元，Night名义约30,810元；基础margin 7%约2,157元/手、price limit 6%。按Night close估算，一板不利压力约1,849元/手，两板复合约3,808元/手；动态参数须再确认。最后交易日2027年1月14日。

## 八、商品期权专项

以下为9月17日历史研究截面；底层已经大幅移动，旧ATM、Delta和moneyness不可用于今日成交。当前仍是212个surface-ready、54个positioning-ready、0个execution-ready。

| Underlying/expiry | 历史ATM IV；当前RV20 | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---|---|
| SC2611/10-14 | 65.57% / 59.49% | +0.73/+1.41 | Y/N/N | 历史event vol高，当前须重报 |
| TA701/12-11 | 31.87% / 27.76% | +2.43/+0.72 | Y/Y/N | put spread仅作结构候选 |
| PF611/10-13 | 31.24% / 27.48% | +5.10/+1.47 | Y/N/N | 旧skew不可直接执行 |
| BU2611/10-26 | 44.91% / 33.47% | -2.91/+0.97 | Y/Y/N | 底层弹性与SC冲突 |
| CU2611/10-26 | 14.50% / 15.56% | +3.14/+1.86 | Y/Y/N | IV<RV不单独证明便宜 |
| AG2612/11-24 | 44.14% / N/A | 异常极值 | Y/N/N | skew形状隔离 |

没有可证明优于裸期货的当前期权结构。取得目标series实时双边报价后，才比较SC/TA put spread或CU call spread；执行价、Delta、净支出、盈亏平衡、Greeks、滑点和行权交割全部重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、09:00开盘风险地图

严格三层：①9月22日中国EOD；②归属9月23日且已完成的Night；③截至07:00的海外最新收盘/报价。Night已经完成的定价绝不是09:00之后的新信息。

| 品种 | 三层信息与预期 | 是否已被Night定价 | 追价 | 等待 | 开盘确认 |
|---|---|---|---|---:|---|
| SC | EOD弱→Night -4.03%→外油约-3%；偏低开 | 大部分已定价 | 否 | 30—45m | 680/694.8/700/710.6、curve、Brent |
| LU/FU | 绝对弱、相对SC强；FU双锚分歧大 | 大部分 | 否 | 45m | LU/SC 7.81、FU back、两腿深度 |
| PX/TA/PF/PR/PL | EOD分化→Night链内齐跌→油价继续弱 | 大部分 | 否 | 30—45m | TA6126/6162/6204、breadth、OI |
| BU | 日盘暴跌→Night仅-0.37%，相对抗跌 | 是，且弹性下降 | 否 | 30m | 4954/5079/5100、OI、curve |
| CU | EOD、Night、外铜同向温和偏强 | 部分 | 否 | 30m | 110700/111060/111230、LME、DXY |
| NI/SS | Night偏强但减仓，海外不足 | 部分 | 否 | 30—45m | 126030/13880、OI、curve |
| AG/AU | 代表合约不匹配；外金银分化、美元强 | 不可精确判断 | 否 | 45m | exact合约、DXY、外金银 |
| OI/RM/M等DCE | OI夜盘走弱；DCE exact覆盖不足 | 不完整 | 否 | 45m | 首次量仓、near-next、CBOT |
| EC/LC/PS | 制度上无Night，09:00首次定价 | 否 | 否 | 45m | EC2199/2265；LC/PS量仓与现货 |
| FG/SA | Night小幅弱，实体不足 | 基本已定价 | 否 | 30m | FG924/929/932、OI与curve |

单日噪音：AG代表合约上涨不能替代AG2612；BU夜盘低弹性否定简单能源同跌；OI日盘强而Night反转；NI/SS上涨伴减仓。今晚/今日不值得交易的是低开追SC、FU、TA、PF，以及用旧期权曲面买“便宜凸性”。

## 十、未来24小时与7天事件

- 今日09:00：中国日盘；能源—聚酯与基本金属等待30—45分钟，先验证价差、curve和量仓。
- 今日22:30：EIA周度石油数据常规窗口；能源仓提前降低Delta，任何期权表达只用实时可报价、有限净支出结构。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)
- 未来24小时：Saudi East-West管道流率、Yanbu装运及潜在美伊接触；未经独立确认的设施消息只进入gap压力情景。[Reuters油市](https://www.reuters.com/business/energy/oil-rises-slightly-ahead-potential-us-iran-talks-2026-09-22/)
- 9月24日前后：USDA周度出口销售；M/RM/C/油脂只按实际销售、中国采购和国内响应调整。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 9月25日03:30附近：CFTC COT常规窗口，只作滞后拥挤背景。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 未来7日：北美收割天气、马棕出口、SC/LU/FU移仓、交易所动态保证金/限幅，以及美元和实际利率变化。未核实到新的OPEC+/IEA正式决策会议，不虚构事件。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态扩展，共77产品；商品期权64产品。
- 实际取数且分析：五所806合约、77产品全部完成EOD初筛；Night覆盖37产品、423具体合约；期权45产品、216 series进入历史研究层。
- 黑色建材：FG夜盘小弱、日盘减仓；I/JM/J/RB/HC未见三层共振。未入榜最值得跟踪FG 924—932接受区。
- 有色贵金属：CU入榜；NI/SS为早期异常；AG/AU因合约不可比和外盘分化未入榜。
- 能源化工：SC、TA、LU/SC、PF入榜；FU深back、BU低弹性均反对追空；EG因DCE Night缺失不升级。
- 新能源：LC/PS日盘反弹，但仓单陈旧、无Night及实体闭环，不入榜。
- 农产品：OI强势未获Night延续，M/RM exact Night不足；仓单、basis与进口利润不能闭环。
- 航运软商品：EC深back但价涨减仓，exact运价和Night不适用；棉糖果及花生未见多层共振。
- 数据不足：214个Night具体合约、19个期权产品、全部实时期权bid/ask、SC/LU实体、A/B级basis、exact进口平价、加工利润、Top候选Night curve及多数动态交易参数。
- 不适用/流动性不足：JR、PM、RI、WH、ZC为占位；RS/WR历史或流动性不足；EC/LC/PS等制度上无Night。
- 风险预算：试仓0.15%—0.25% NAV；取得价格、curve及非价格层确认后最高0.75%；能源—化工共享因子≤0.50%，有色共享≤0.40%，单主题总风险≤2.5%。压力测试包括两板、相关性破裂、流动性消失、margin上调、人民币急变及交割挤压。

固定六路径已从main回读验证：历史与latest内容一致，status对应本期，manifest中`2026-09-23 + commodities_morning`恰好一条。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-23_commodities_morning.md)。`archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：CU2611仅在09:30后110700—111000承接并重上111060时研究试多；SC2611仅在反抽700—708失败并跌回694.8/VWAP下方时试空；TA701仅在反抽6175—6204失败并跌回6162/VWAP下方时试空。  
C. 今天应继续观察的机会：LU2611/SC2611比值回撤、PF611链内弱势、BU相对SC低弹性、NI/SS早期强势，以及EC/LC/PS的09:00首次有效定价。  
D. 今天必须避免或退出的交易：低开追空SC/FU/TA/PF、追CU第一跳、沿用BU/EG旧条件、把AG2610替代AG2612、把C级basis或连续外盘代理称套利，以及在execution-ready=false时臆测期权成本。