# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-24

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：07:12 BJT；信息截点：07:00。最近完整中国EOD为9月23日；归属9月24日的Night Session已完成，下一实际交易窗口为今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；能源—聚酯夜盘强反转获外油确认，但首跳赔率差，只等SC、FU、TA回撤接受。**

当前regime：前一日“原油风险溢价压缩”在夜盘被部分逆转；能源与聚酯由弱转强，橡胶内部出现分化，有色与贵金属受海外走弱压制。

最接近触发的是SC2611、FU2611和TA701的回撤接受多；EC2610仍是无夜盘的09:00事件观察。四者均须等开盘后确认，不能把夜盘涨幅直接当日盘追价信号。

## 二、数据质量与覆盖

本期实际读取：[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻EOD、Physical、External、Options、合约元数据和Night compact层。

- 统一输入：schema v2，`requested_date=2026-09-23`，9月24日06:21:43生成。
- Futures：06:09生成；五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0，3条placeholder排除。
- Market State：77产品完成全范围初筛；同合约1D/3D/5D/20D、RV20、量仓和curve可用时使用，roll标记保留。
- Physical：06:21生成，18/20序列按原生频率有效；SC/LU不可得。Basis均为C级或缺失，只作context；5条仓单记录为carried-forward，不冒充本期新增。
- External：06:21生成，17/22有效、全部`context_only`；连续代理与可核实近月冲突项隔离。
- Options：9月23日未形成新的正式surface；最新发布研究面仍为9月17日，16,016条、216 series、45/64产品；212个series surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖为0。大文件紧凑读取被截断，不能解释为源为空。
- Metadata：partial；有效合约匹配约73.45%，动态margin/price-limit覆盖约30.15%，DCE参数缺口仍在。

Night字段：`trading_date=2026-09-24`、`night_session_date=2026-09-23`，06:03:12生成；`data_fresh=true`、`validation_passed=true`、`published=true`。有效423合约、37产品；outside-window 165、no-night 4，missing timestamp/price/quote均为0。

`coverage_complete=false`，存在214个query error和214个unresolved concrete contracts，主要限制DCE及部分非代表月份。Top候选所用SC、FU、TA均为与交易卡完全一致的exact contract；Night near-next大文件读取受限，因此不强拼Top候选Night curve。

## 三、商品仪表盘

EOD curve为近月—次近月年化百分比口径；正值记back。Basis均为C级或缺失，不能进入套利评分。S/P/E分别为surface/positioning/execution readiness；均为最新正式历史面而非实时报价。

| 板块 | 品种/具体主力 | EOD close/settle；1D/5D | Vol/OI/ΔOI；EOD curve | Physical/Basis | Night close；vs close/vs settle；ΔOI；质量/时间 | 07:00海外；S/P/E | 信号 |
|---|---|---|---|---|---|---|---|
| 原油 | SC2611 | 688.1/695.1；-3.07%/-17.09% | 24.55万/3.96万/-549；Back 7.93% | 缺失/C | 730；+6.09%/+5.02%；+539；fresh/02:30 | Brent proxy 103.10、+3.88%；Y/N/N | 强反转，等回撤 |
| 燃料 | FU2611 | 4117/4116；-1.63%/-8.39% | 76.00万/17.63万/-18,136；Back 22.98% | context/C | 4253；+3.30%/+3.33%；+8,746；fresh/23:00 | EIA馏分油-40万桶；Y/N/N | 产品端强，不追 |
| 低硫 | LU2611 | 5385/5364；-0.50%/-5.68% | 14.35万/6.51万/+1,944；Back 7.70% | 缺失/C | 5533；+2.75%/+3.15%；-457；fresh/23:00 | 外油上涨；N/N/N | 强价但OI线索冲突 |
| 沥青 | BU2611 | 4898/4989；-2.29%/-7.61% | 78.55万/25.25万/-9,324；Back 13.19% | context/C | 4997；+2.02%/+0.16%；-12,354；fresh/23:00 | 外油上涨；Y/Y/N | 主要回到结算锚 |
| 聚酯 | TA701 | 6120/6142；-1.92%/-5.80% | 106.81万/108.42万/-94,032；Back 3.25% | context/C | 6298；+2.91%/+2.54%；+14,498；fresh/23:00 | 原油/石脑油proxy上涨；Y/Y/N | 链内反转确认 |
| 芳烃 | PX611 | 9066/9102；-1.66%/-6.09% | 29.72万/14.15万/-10,538；Back 0.68% | context/C | 9326；+2.87%/+2.46%；+13,223；fresh/23:00 | 石脑油proxy +2.46%；N/N/N | 与TA同向 |
| 短纤 | PF611 | 8022/8078；-3.00%/-6.87% | 25.83万/21.01万/-13,550；Back 1.88% | context/C | 8214；+2.39%/+1.68%；-5,255；fresh/23:00 | 成本反弹；Y/Y/N | 反弹但量仓弱 |
| 瓶片 | PR611 | 7910/7916；-2.68%/-7.63% | 8.25万/5.17万/-4,888；Back 1.82% | context/C | 8118；+2.63%/+2.55%；-157；fresh/23:00 | 成本反弹；Y/N/N | 不追第一跳 |
| 橡胶 | RU2701 | 19455/19120；+0.84%/+1.46% | 41.53万/15.56万/+12,238；Back 0.33% | context/C | 19395；-0.31%/+1.44%；-2,631；fresh/23:00 | rubber proxy +1.55%；Y/Y/N | vs close转弱，旧多未确认 |
| 合成胶 | BR2611 | 15160/14830；-0.40%/-0.40% | 27.02万/10.51万/+8,215；Back 0.88% | context/C | 15380；+1.45%/+3.71%；-13,827；fresh/23:00 | rubber proxy +1.55%；Y/N/N | 价强仓减，不追 |
| 20号胶 | NR2611 | 16725/16380；+1.20%/+2.60% | 9.02万/6.21万/+3,165；轻Contango 0.12% | context/C | 16815；+0.54%/+2.66%；+40；fresh/23:00 | rubber proxy +1.55%；N/N/N | 增量有限 |
| 航运 | EC2610 | 2225.5/2223.5；+1.11%/+8.46% | 1.12万/2.13万/-2,072；Back 18.96% | exact运价缺失/C | 制度上无Night | 船运成本仅context；N/N/N | 09:00首次定价 |
| 有色 | CU2611 | 110330/110780；+0.06%/+3.44% | 6.90万/17.12万/+11,093；Back 0.50% | context/C | 110190；-0.13%/-0.53%；+638；fresh/01:00 | 铜proxy -0.68%；Y/Y/N | Night否定追多 |
| 贵金属 | AU2612 | 939.50/940.18；-0.01%/+0.64% | 12.21万/21.28万/+6,129；轻Contango 0.16% | 不适用/C | 931.02；-0.90%/-0.97%；+6,136；fresh/02:30 | 金proxy -1.70%；N/N/N | 内外同弱 |
| 油脂 | OI701 | 10152/10145；-0.96%/-0.24% | 23.64万/27.67万/-9,585；Back 1.72% | context/C | 10194；+0.41%/+0.48%；+1,910；fresh/23:00 | 棕榈proxy -0.87%；N/N/N | 内外冲突，等待 |

07:00海外为Trading Economics 9月23日美国时段最新可见代理：WTI 92.35（+2.02%）、Brent 103.10（+3.88%）、汽油+3.16%、石脑油+2.46%；黄金-1.70%、白银-3.80%、铜-0.68%，橡胶+1.55%。这些是海外方向代理，不是中国具体合约报价，也不构成全口径跨市场套利。[海外商品行情](https://tradingeconomics.com/commodities)

EIA截至9月18日当周数据显示：美国商业原油库存增加300万桶至4.264亿桶、炼厂加工量下降51.9万桶/日；汽油库存下降170万桶、馏分油下降40万桶，后者仍较五年均值低12%。原油端与产品端信号分化，支持FU相对强而不是无条件追SC。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)｜[EIA摘要](https://ir.eia.gov/wpsr/summary.txt)

## 四、相比上一期真正变化

1. **能源方向发生反转。** SC昨日日盘结算-3.07%，夜盘相对昨收+6.09%；Brent海外代理再涨3.88%。昨日“反抽失败空”与BU/EG空头旧锚均失效，不能继续沿用。
2. **SC的Night涨幅并非结算口径幻觉。** 相对昨收+6.09%、相对昨结+5.02%，两锚均大；BU则相对昨收+2.02%但相对昨结仅+0.16%，更多是恢复日内close—settle偏差，不能把两者视作同等强势。
3. **聚酯链获得链内breadth。** TA、PX、PF、PR夜盘相对昨收分别+2.91%、+2.87%、+2.39%、+2.63%；TA/PX夜盘ΔOI为正，但这仍只是归因线索，不能认定“新多”。
4. **RU旧多未获Night确认。** RU相对昨收-0.31%、相对昨结+1.44%；差异来自日盘close已显著高于settlement。Night边际弹性下降，昨晚条件触及状态因无分钟路径而未知。
5. **BR延续上涨但原入场区未给。** Night低点15220高于旧计划14900—15100，条件未触发；价涨同时OI下降，仅保留观察。
6. **有色、贵金属被海外反对。** CU Night -0.13%、海外铜proxy -0.68%；AU Night -0.90%、海外黄金proxy -1.70%。不恢复CU/AU/AG旧多。

旧建议台账：
- `COM-E-RU2701-PULLBACK-20260923`：触及19350边界但未收复19455收盘锚；无分钟路径，触发未知，当前降级为等待重新接受。
- `COM-E-BR2611-REVERSAL-20260923`：Night未进入14900—15100入场区，明确未触发；不追高。
- `COM-E-TA701-COST-UNWIND-20260918`：夜盘链内反转，空头逻辑失效，转为新的回撤接受多研究。
- `COM-M-EC2610-EVENT-20260920`：仍有效至今日09:45验证，但外油上行提高gap风险，入场锚重设。
- 未收到成交反馈，不假设用户实际持仓；若此前按旧条件建立，只按原失效规则处置。

## 五、产业链地图

- **最强：SC—FU—LU—PX—TA，偏多但已高弹性，置信度中高。** Night和海外同向，EOD back支持近月紧张；EIA原油累库与管道恢复是反证，实体/高质量basis缺失。
- **产品端强于原油，置信度中。** FU deep back 22.98%、EIA汽油/馏分油去库支持；但该curve本身可能已计价紧张，追涨风险高。
- **橡胶内部分化，置信度中。** BR/NR Night续强而RU相对昨收转弱；BR价涨仓减、RU弹性下降，不把板块proxy上涨当全链确认。
- **航运事件性偏强，置信度中。** EC 5D +8.46%、back 18.96%，但OI下降、无Night和exact运价，09:00才首次定价。
- **有色贵金属与农产品无三层共振。** CU/NI/SS Night转弱，AU与外金同跌；OI小幅反弹但棕榈proxy走弱，黑色、新能源亦无可执行共振。

## 六、机会排行榜

| 排名 | 候选/idea_id | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2611回撤接受多 / COM-M-SC2611-GAP-ACCEPT-20260924 | 22/14/17/13/8 | **74** | 1、2、4 | 存在待验证优势｜部分充分；EIA原油累库反对｜等09:45 |
| 2 | FU2611产品紧张回撤多 / COM-M-FU2611-PRODUCT-TIGHTNESS-20260924 | 21/14/15/13/9 | **72** | 1、2、4 | 存在待验证优势｜部分充分；深back/追价风险｜等09:30 |
| 3 | TA701链内反转多 / COM-M-TA701-CHAIN-REVERSAL-20260924 | 20/14/16/12/9 | **71** | 1、2、4 | 存在待验证优势｜部分充分；日盘弱势反对｜等09:30 |
| 4 | EC2610事件回撤多 / COM-M-EC2610-EVENT-20260920 | 20/15/15/11/9 | **70** | 1、2、4 | 存在待验证优势｜部分；OI/exact运价反对｜等09:45 |
| 5 | BR2611相对强势回撤多 / COM-E-BR2611-REVERSAL-20260923 | 18/13/13/10/11 | **65** | 1、2 | 存在待验证优势｜部分；Night减仓｜等回撤 |

分项已逐项复算并遵守证据层封顶。排名按研究优先级综合，不以分数单独决定仓位。全部期货最大损失均不由计划止损结构性限定。

## 七、前三名研究卡

### 1. SC2611｜回撤接受多｜74

事实：昨收/昨结688.1/695.1；Night OHLC 703/734.4/702.8/730，相对昨收+6.09%、昨结+5.02%，ΔOI +539。EOD back 7.93%，海外Brent代理+3.88%。

市场隐含供应风险重新上升；我们的分歧是，只有09:00后能在714—724上方获得接受，才说明Night不是一次性headline squeeze。最强竞争解释是EIA原油累库、炼厂加工下降和Saudi管道恢复意味着供给风险最终继续消退。[Saudi管道恢复](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)

- 最佳表达：SC2611期货小风险试多；期权execution-ready=false，不能虚构call spread净支出。
- 好成交：09:45后回撤714—724承接，并重上730/VWAP；先1/3风险。
- 中成交：突破734.4后回踩728—734不破；半风险。
- 坏成交：直接高于750、跌破710或盘口滑点超过计划1R的20%，放弃。
- 止损：45分钟接受702.8下方；逻辑失效为跌破695.1、back明显收窄且Brent回落至99下方，或确认供应恢复。
- TP1 744或+1.5R；TP2 770或+3R；1—3D无扩张退出，TP1减半。
- 价格锚：702.8/734.4来自Night低高，714—724为Night区间回撤与风险预算假设，不是已验证信号。
- 风险：0.15%—0.25% NAV；与FU/TA共享因子合并≤0.60%。
- 参数：标准乘数1,000桶/手、tick 0.1元/桶、tick value 100元，Night名义约730,000元；有夜盘。最后交易日10月30日、最后交割日11月6日，10月中旬前移仓或退出。动态margin/price limit未确认，不能可靠计算一至两个涨跌停压力金额；最坏情景为headline反转、gap和流动性消失。

### 2. FU2611｜产品紧张回撤多｜72

事实：昨收/昨结4117/4116；Night 4200/4282/4183/4253，相对昨收+3.30%、昨结+3.33%，ΔOI +8,746。EOD back 22.98%；EIA汽油和馏分油库存下降，馏分油仍低于五年均值12%。

市场已计入近月产品紧张；我们的分歧不是继续追涨，而是若回撤仍守住4183—4230，deep back与库存紧张可能延续相对强势。反证是curve极陡、EOD价跌减仓以及原油端累库。

- 最佳表达：FU2611期货回撤多；不与SC满额叠加。
- 好成交：09:30—09:45回撤4190—4230承接并重上4253/VWAP。
- 中成交：突破4282后回踩4240—4282不破；半风险。
- 坏成交：直接高于4400、跌破4160或深度不足，放弃。
- 止损：30分钟接受4150下方；逻辑失效为跌破4116、back快速压至15%以下且外油同步转弱。
- TP1 4350或+1.5R；TP2 4500或+3R；1—3D时间止损。
- 风险0.15%—0.20% NAV；能源共享因子合并≤0.60%。
- 参数：repo确认最后交易日10月30日、最后交割日11月3日；multiplier、tick、动态margin/limit未完整确认。执行前补齐，不编造名义、一板或两板损失。

### 3. TA701｜链内反转多｜71

事实：昨收/昨结6120/6142；Night 6172/6324/6158/6298，相对昨收+2.91%、昨结+2.54%，ΔOI +14,498；PX611同步+2.87%、ΔOI +13,223，PF/PR亦上涨。EOD back 3.25%。

市场可能只把Night当成本反弹；我们的分歧是，若09:30后6220—6270获接受且PX不转弱，链内breadth可能推动进一步修复。最强反证是昨日日盘弱、TA EOD减仓94,032、实体与加工利润缺失。

- 最佳表达：TA701期货条件多；期权历史面不可作为实时执行依据。
- 好成交：09:30后回撤6220—6270承接并重上6298/VWAP。
- 中成交：突破6324后回踩6290—6324不破；半风险。
- 坏成交：直接高于6400、跌破6180或PX同步转弱，放弃。
- 止损：30分钟接受6158下方；逻辑失效为跌破6120、PX Night低点失守且外油回落。
- TP1 6380或+1.5R；TP2 6480或+3R；1—3D无扩张退出。
- 乘数5吨、tick 2元、tick value 10元，Night名义约31,490元；基础margin 7%、price limit 6%，有夜盘，最后交易日2027年1月14日。
- 以6298静态估算，一板不利约1,889元/手、两板复合约3,665元/手；实际限幅、保证金和结算锚需按交易所当日参数复核。风险0.15%—0.20% NAV；与SC/FU合并≤0.60%。

## 八、商品期权专项

最新正式面仍为9月17日，已落后于9月23日EOD和9月24日Night；底层大幅变化使旧ATM、Delta与moneyness失真，只作历史波动背景。

| Underlying/expiry | 历史ATM IV / 当前RV20 | 历史IV-RV | S/P/E | 判断 |
|---|---:|---:|---|---|
| SC2611/10-14 | 65.57% / 57.65% | +7.92vol | Y/N/N | 事件vol历史偏高，不能当当前报价 |
| FU2611/10-19 | 60.62% / 37.37% | +23.25vol | Y/N/N | 裸买Vega历史成本高 |
| TA701/12-11 | 31.87% / 24.74% | +7.13vol | Y/Y/N | Delta与净支出须重算 |
| BR2611/10-26 | 35.44% / 26.73% | +8.71vol | Y/N/N | positioning不足 |
| AG2612/11-24 | 44.14% / 30.75% | +13.39vol | Y/N/N | 历史skew异常，隔离 |
| CU2611/10-26 | 14.50% / 15.45% | -0.95vol | Y/Y/N | IV<RV不单独证明便宜 |

当前没有可证明优于裸期货的期权结构。取得实时双边报价后才比较SC/FU/TA有限净支出call spread；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点和行权交割全部重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、09:00开盘风险地图

严格三层：①9月23日中国完整EOD；②归属9月24日、已经完成的Night；③07:00海外最新代理。Night未覆盖或代表合约不一致时不做替代。

| 品种 | 三层信息与预期开盘 | 是否已由Night定价 | 首跳 | 等待 | 开盘确认 |
|---|---|---|---|---:|---|
| SC | EOD大跌→Night +6.09%→Brent proxy +3.88%；高开 | 大部分已定价 | 不追 | 45m | 702.8/714/730/734.4、curve、Brent |
| FU/LU | EOD弱→Night +3.30%/+2.75%→产品库存紧；高开 | 多数已定价 | 不追 | 30—45m | FU4183/4253、back、LU/SC |
| PX/TA/PF/PR | EOD弱→Night全链+2.4%至2.9%→外油/石脑油强；高开 | 多数已定价 | 不追 | 30m | TA6158/6298/6324、PX breadth |
| BU | EOD收盘显著低于结算→Night vs close +2.02%但vs settle仅+0.16%；平/高开 | 主要是回归结算 | 不追 | 30m | 4883/4997/5028、back |
| RU/BR/NR | RU Night -0.31%，BR +1.45%，海外rubber proxy强；分化 | BR部分、RU否 | 不追 | 30m | RU19350/19455；BR15220/15380 |
| EC | EOD偏强、无Night、运输仅context；可能高开 | 否 | 不追 | 45m | 2194/2225.5/2265、back、OI |
| CU/NI/SS | EOD偏强→Night转弱→海外铜弱；低/平开 | 是 | 不追多 | 30m | CU109930/110190、LME proxy、CNH |
| AU/AG | AU Night与海外金银同跌；偏低开 | AU已定价，AG正式合约缺失 | 不抄底 | 30—45m | AU928.8/931、DXY/收益率 |
| OI/M/RM | OI Night小涨但棕榈/谷物proxy弱，DCE exact缺口；分化 | 部分/不足 | 不追 | 45m | OI10124/10194、DCE量仓、basis |
| FG/黑色 | FG Night -0.43%、减仓；钢/铁矿proxy分化 | 是 | 不追 | 30m | FG918/921、量仓、curve |
| LC/EC等无Night | 9月23日EOD后09:00首次定价 | 否 | 不追 | 45m | LC128900、EC2225.5及实体响应 |

人民币最新同时间报价未独立刷新；9月21日可核实的在岸/离岸约6.6950/6.6946仅作旧背景，不能量化今日贡献。[人民币与美元](https://www.reuters.com/world/asia-pacific/yuan-hits-fresh-multi-year-peak-pboc-eases-curb-ahead-trump-xi-summit-2026-09-21/)

## 十、未来24小时与7天事件

- 9月24日09:00：中国商品日盘；能源—聚酯等待30—45分钟，EC/LC等无Night品种等待45分钟。
- 9月24日晚间：USDA周度出口销售常规发布窗口；M、RM、C和油脂只按实际销售、中国采购与国内响应调整。[USDA出口销售](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 未来24小时：Saudi East-West Pipeline负荷、Yanbu装船及Hormuz/Perim船流；未经独立确认的停运/恢复消息只作gap压力情景，不追headline。[Reuters管道恢复](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)｜[航运成本](https://www.reuters.com/business/energy/saudi-arabia-denies-buying-oil-tankers-after-iraq-blames-it-higher-shipping-2026-09-22/)
- 9月26日约03:30 BJT：CFTC COT常规窗口，只作滞后拥挤背景。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月30日22:30 BJT常规窗口：下一份EIA周度石油数据；能源仓提前降低Delta，若用期权仅限实时可报价的有限净支出结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 未来7日：北美收割天气、马棕出口、交易所动态保证金/限幅、SC/LU/FU进入10月移仓与交割风险窗口。
- 截至截点，未确认未来7日有新的OPEC+/IEA正式决策会议；不凭日历空白预设催化。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态扩展后77产品；商品期权64产品。
- 实际取数且已分析：五所806合约、77产品完成9月23日EOD初筛；Night取得37产品、423合约；方向、curve、跨期、跨品种、跨市场代理、近似中性、波动率/偏度和事件凸性均完成扫描。
- 数据不足：214个Night具体合约、DCE Night及部分元数据、19个期权产品、9月23日正式surface、全部实时bid/ask、SC/LU实体、A/B级basis、exact import parity、加工利润及Top候选Night curve。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为placeholder；RS历史不足，WR等流动性较低；EC、LC等制度上无Night。
- 黑色建材：FG Night弱且减仓，无三层共振；未入榜。
- 有色贵金属：CU/NI/SS被Night和海外反对，AU/AG同步弱；不恢复旧多。
- 能源化工：SC、FU、TA入榜；BU的close/settle分歧显示边际弹性较弱，EG因DCE exact Night缺失而不升级。
- 新能源：LC EOD价跌仓增、5D仍正，实体与Night缺失，等待09:45。
- 农产品：OI Night小幅修复但外盘反对，M/RM DCE Night不足；无可执行共振。
- 航运软商品：EC保留事件多观察；OI下降、无Night与exact运价缺失限制执行。
- 风险预算：单笔试仓0.15%—0.25% NAV；价格、curve和非价格层确认后才考虑提高至0.75%；能源—化工共享因子≤0.60%，单一高确信主题总风险≤2.5%。
- 压力测试：一至两个涨跌停、海外headline反转、相关性破裂、流动性消失、保证金上调、人民币急变、IV跳升/塌陷与移仓交割挤压。
- 固定六路径从main回读验证后方可确认归档；CI不等待，记录`pending_or_unverified`。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-24_commodities_morning.md)

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2611仅在09:45后回撤714—724承接并重上730/VWAP时试多；FU2611仅在4190—4230承接并重上4253时试多；TA701仅在6220—6270承接并重上6298时试多，三者按同因子合并风险。  
C. 今天应继续观察的机会：EC2610在09:45后对2194—2265的接受度、BR/NR强势能否在RU转弱背景下延续、BU是否只是回归结算锚，以及DCE品种首次有效定价。  
D. 今天必须避免或退出的交易：追SC/FU/TA/PX第一跳、恢复昨日能源—聚酯空头旧锚、追BR缺失的入场区、恢复RU/CU/AU旧多、用AG2610替代AG2612、把C级basis或海外proxy称套利，以及在execution-ready=false时臆测期权成本。