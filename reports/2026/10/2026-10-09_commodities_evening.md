# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-09｜信息截点：2026-10-09 19:30 BJT｜生成时间：2026-10-09T19:34:00+08:00｜prompt_version：radar_2026-09-06_coverage_v1｜data_protocol_version：china_commodities_v2**

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；AG出现“夜盘无新增下跌—日盘反转—海外金银续涨”的新多头线索，MA趋势仍强但弹性下降，均只等21:30—21:45确认。**

最强产业链为甲醇—煤化工与部分塑化，最弱为锡、乙二醇、碳酸锂及集运。当前regime是“复市第二日高波动分化：国内化工/煤系强、油价风险溢价回落、贵金属日间反转、WASDE前农产品事件压缩”。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心期货状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)及[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[Contract Metadata](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)、[Options Quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)与模块专用文件。

- report_input：requested_date=2026-10-09，generated_at=19:12:02 BJT，schema_version=2。
- Futures/Market State：10月9日五所、806份合约、77个产品；`full_market_ready=true`、source-date match 100%、critical errors=0、五所均为10月9日。5条OHLC占位记录已排除异常排行；20个交易日同合约窗口可用。
- Contract Metadata：effective match 73.45%，multiplier/tick/margin/limit覆盖30.15%，night-session字段覆盖0；DCE、GFEX参数模块失败，不能凭常识补齐。carried-forward metadata 48份。
- Physical：10月9日19:11生成，18/20条按原生日频fresh；SC/LU不可用。现货绝对水平可作context，但所有basis均为C级，不能用于方向评分或套利确认。
- 仓单：CZCE 10月9日fresh；SHFE、DCE当期采集失败；GFEX五条仅为9月1日stale carry，不计当前证据。
- External repo：10月9日19:11生成，17/22 fresh，但全部为`context_only`；本报告另补19:30公开海外快照。
- Options：10月9日19:01 BJT，14,074条、185个series；39/64产品成功，181个surface-ready、41个positioning-ready、0个execution-ready；IV coverage 98.78%、OI coverage 69.36%、bid/ask coverage 0。DCE全所期权因security denial缺失；TA当日期权源日期不匹配；`surface_latest.json`连接器返回0字符但blob存在，状态记为`truncated`，不是源文件为空。逐series指标只来自统一输入。
- Night Session：module status仍是`trading_date=2026-10-08`、`night_session_date=2026-10-07`、generated_at=10月8日07:56，`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`，night contracts=0、query/unresolved=214；它与今天完成的10月9日连续交易阶段无关。`night_session/latest.json`同样在连接器端返回0字符但有blob SHA，记为`truncated`。因此仅对公开来源能够核实的AG/SC主力使用`night_session_fallback=true`，其余exact-contract夜盘字段缺失，不伪造。
- 今晚21:00开始的连续交易尚未发生，归属下一实际中国交易日**10月12日**；不得把10月9日凌晨行情写成今晚行情。

## 三、商品仪表盘（展示12项；全量扫描77项）

|板块|合约|EOD close/settle|1D close / 5D settle|Volume / OI / ΔOI|Curve|Basis/Physical|早前Night与日盘|15:00后海外|Options S/P/E|21:00信号|
|---|---|---:|---:|---:|---|---|---|---|---|---|
|煤化工|MA701|3338/3321|+6.04% / +14.83%|149.31万/76.12万/+70,427|Back 16.08%|C级；仅context|公开主力涨超7%，exact缺；日盘边际回吐|油价转跌，反对追价|Y/Y/N；IV45.66、RR+2.02|偏低/平开，等45m|
|贵金属|AG2612|14717/14515|+0.88% / -7.99%|30.36万/29.04万/-4,332|Back 0.54%|缺|Night 14413；vs前收约0%；日盘+2.11%|银约+1.7%、金约+1.4%|Y/N/N；IV36.39、RR+1.75|偏高，等30m|
|有色|SN2611|391410/391170|-4.23% / -5.05%|13.50万/3.50万/+3,724|近乎平坦Back|当日SHFE仓单缺；周度社会库存下降反对追空|公开Night为SN2610，合约不匹配|LME锡早前约-5.22%|Y/N/N；IV24.35、RR-2.89|低/平开，等30m|
|黑色|JM2701|1539.5/1517.5|+4.30% / +1.57%|75.59万/42.54万/+10,394|Back 3.48%|C级；仅context|exact缺|无可靠exact映射|DCE缺|偏高但不追|
|塑化|L2701|8860/8781|+3.41% / +8.01%|68.23万/43.71万/+30,068|Back 3.16%|缺|exact缺|油价回落构成反证|DCE缺|平/小低，等30m|
|塑化|PP2701|9395/9284|+3.54% / +9.31%|90.75万/69.85万/+51,612|Back 3.07%|缺|exact缺|油价回落构成反证|DCE缺|平/小低，等30m|
|油品|SC2611|734.1/741.3|-0.45% / +2.28%|13.20万/2.37万/-3,400|Back 3.19%|Physical缺|Night 732.8；vs前收-3.39%；日盘+0.18%|Brent/WTI降至约102.6/90.18|Y/N/N；IV60.91≈RV59.93|偏低，等45m|
|油品|FU2701|4409/4440|+1.47% / +14.32%|24.71万/14.32万/+564|Back 8.70%；主力roll|C级；仅context|公开Night主力月份不一致|油价回落、成品油出口恢复|Y/N/N；IV61.80高于RV|偏低，等45m|
|橡胶|BR2612|16710/16370|+2.77% / +8.23%|8.14万/6.07万/+3,839|Back 2.27%|缺|exact缺|橡胶外盘精确增量缺|Y/N/N；IV49.82、RR+1.02|平开，等30m|
|新能源|LC2701|117000/118740|-3.74% / -5.93%|26.05万/42.16万/+11,960|Back 1.22%|C级；GFEX仓单stale|无制度夜盘|无可靠exact映射|Y/N/N；IV45.13、RR-2.69|下周一09:00|
|化纤|EG2611|5185/5254|-4.16% / -0.68%|161.19万/28.46万/-3,654|Back 9.92%|缺|exact缺|油价回落同向|DCE缺|偏低，等30m|
|航运|EC2611|2700/2749|-5.05% / +0.05%|1.39万/2.13万/-1,776|Contango 22.48%|即期/合约口径未对齐|无制度夜盘|美国—亚洲运费仍高，构成反证|不适用|下周一09:00|

注：AG/SC的早前Night来自10月9日02:32公开主力收盘；AG按10月8日EOD close 14412计算，SC按758.5计算。相对结算涨跌只作风险锚；新增信息以相对close为主。MA只有品种主力摘要，没有仓库exact-contract记录，故不计算正式day_follow_through。

## 四、相比上一期真正变化

1. **AG旧空逻辑失效并转为多头研究。** 早前Night 14413相对10月8日前收几乎没有新增下跌，但日盘收14717、较Night反转约+2.11%；19:30海外金银继续上涨。若此前按14550—14650反抽失败条件建立空单，应以今日收复14700和海外同向反弹作为退出/失效依据；没有成交反馈，不假设用户持仓。
2. **MA从“夜盘动量”转为“趋势强、弹性下降”。** EOD close 3338、价涨仓增、深back仍支持，但公开Night已完成大部分涨幅，日盘未继续扩张；油价在15:00后回落，旧晨报多头条件触发状态未知，今晚不得按已成交管理。
3. **TA旧多条件过期。** close 6668低于上一版6720—6780承接区且ΔOI -19,561；原触发路径无法核实，当前不得继续挂原6800突破条件。若此前已建立，仍按原6610止损管理，不因本报告假设持仓。
4. **SC从供应冲击多头降为反弹失败空观察。** Night相对前收-3.39%，日盘只修复0.18%，当前海外油价因伊朗谈判评论和中国恢复成品油出口而回落；但3.19% backwardation反对追空。
5. **SN弱势获外盘确认，但实体层不一致。** 国内价跌仓增、LME锡夜间下挫；然而最近可核实的社会库存下降，且正式合约Night缺失，必须等反抽失败。
6. **RU价格创新高但curve转为明显contango。** close 20645、ΔOI +17,339，却由上一版轻back转为-3.86% contango；旧多不再是三层同向，若此前建立可向20750旧TP1减风险，新仓不追。

## 五、产业链地图

- **甲醇—煤化工（最强，偏多但不追）：** MA价涨仓增、16.08% backwardation、call skew同向；Physical只有C级，油价回落和日盘未延伸是最大反证。置信度中高。
- **黑色—煤焦（偏强分化）：** JM/J上涨且OI增加，I收682.5、价跌仓增；焦煤curve确认、铁矿curve仅0.29%。缺DCE期权、仓单和合格basis，置信度中。
- **贵金属（由弱转反弹）：** AG早前Night未新增下跌，日盘反转并获海外金银确认；OI下降与call已偏贵限制追价。置信度中高。
- **原油—燃料—聚酯（风险溢价回落）：** SC/FU的高位弹性下降，油价15:00后走弱；SC/FU仍backwardation，说明不能把宏观消息直接转成趋势空。置信度中。
- **有色—新能源（锡/锂最弱）：** SN、LC价跌仓增，SN获LME确认；LC的GFEX仓单停在9月1日不可用，SN社会库存下降构成反证。置信度中。

## 六、机会排行榜

|排名|候选|逻辑/赔率/催化/价曲波/仓技|总分|有效支持层|研究判断｜证据｜执行|
|---:|---|---:|---:|---|---|
|1|AG2612回踩确认多（COM-E-AG2612-DAY-REVERSAL-LONG-20261009）|21/16/15/13/9|**74**|1、4、5|存在待验证优势｜部分｜等21:30|
|2|MA701趋势回踩多（COM-M-MA701-MOMENTUM-HOLD-20261009）|21/14/14/13/10|**72**|1、2、5|存在待验证优势｜部分｜等21:45|
|3|SN2611反抽失败空（COM-E-SN2611-LME-CONFIRMED-SHORT-20261009）|20/14/14/13/9|**70**|1、4、5|存在待验证优势｜部分｜等30分钟/参数已核|
|4|SC2611反弹失败空（COM-E-SC2611-ELASTICITY-FADE-20261009）|19/14/16/10/9|**68**|1、4|存在待验证优势｜部分｜等45分钟|
|5|BR2612回踩多（COM-E-BR2612-RUBBER-CONFIRMATION-20261008）|19/13/12/13/10|**67**|1、2|存在待验证优势｜部分｜等30分钟/参数缺|

评分只用于研究排序，不代表胜率、预期收益或仓位。MA/AG/SN达到70分仅因至少三个独立支持层；期权无bid/ask、Night不完整、动态参数缺失仍可阻止执行。

## 七、前三名交易卡

### 1. AG2612｜回踩确认多｜74

- **事实：** EOD 14717/14515，close 1D +0.88%、settle 1D -0.51%，volume 303,600、OI 290,434、ΔOI -4,332；早前Night 14413，相对前收约0%、相对结算-1.21%，日盘follow-through约+2.11%。海外19:30附近金约+1.4%、银约+1.7%。
- **市场定价：** 国内日盘已撤销“夜盘续跌”定价，海外进一步计入弱美元/油价回落。
- **分歧：** 若市场仍按前一日贵金属弱势交易，日盘反转可能继续；最强竞争解释是OI下降表明反弹主要为减仓，且call skew已计入乐观。
- **证据：** 支持=价格反转、海外同向、期权call skew；中性=轻back；反对=OI下降、IV高于RV约4.95vol、无bid/ask。
- **最佳表达：** AG2612期货条件多。AG2612 2026-11-24到期14500/15500 call spread仅研究；ATM IV36.39%、RV20 31.44%、RR25 +1.75，positioning/execution均false，不报价权利金、Greeks或净成本。
- **入场：** 好成交=21:30后14650—14800承接并重上14850，先1/2；海外银仍>60且回踩14800不破再加1/2。中成交=突破14920后回踩14850不破，只用半风险。坏成交=首跳>15100、跌破14450或海外银跌回59下，放弃。
- **退出：** 30分钟接受14380下方止损；TP1 15200出1/3，TP2 15800再出1/3，其余跟踪；3个交易日不达TP1退出。逻辑失效=国内重新跌破Night锚且海外银同步转弱。
- **情景R：** 14700成交约1.40R/3.14R；14800成交约0.95R/2.38R；未含手续费、gap与滑点。
- **参数：** 官方标准乘数15千克、tick 1元/千克、tick value 15元；close名义约220,755元。10月9日后AG2610—AG2704动态限幅20%、一般保证金22%；按settle保证金约47,900元。last trading day=2026-12-15；11月底前退出/换月，避免实物交割。
- **压力：** 一/两个不利跌停约43,545/78,381元/手；期货止损不等于最大损失有限。试仓风险≤NAV 0.50%，贵金属同因子合并。
- **催化/最坏情景：** 1—3D美元、收益率、地缘谈判；最坏为美元急升、金银同步反转、夜盘gap和20%限板。

### 2. MA701｜趋势回踩多｜72

- **事实：** EOD 3338/3321，close 1D +6.04%、5D +14.83%，volume 1,493,099、OI 761,175、ΔOI +70,427；near-next backwardation 16.08%。公开Night只确认主力涨超7%，仓库exact-contract缺失。
- **市场定价：** 供给/运输风险和近端紧张已被大幅计价。
- **分歧：** price/OI/curve仍支持趋势，但日盘没有继续扩张且下午油价回落，边际买盘可能已拥挤。
- **证据：** 支持=价格/OI、深back、MA701 call skew；反对=Physical仅C级、海外油价回落、两日涨幅过大；缺失=exact Night与实时期权成本。
- **最佳表达：** MA701期货条件多；12月11日到期3300/3500 call spread仅研究。ATM IV45.66%、RV20 35.68%、IV-RV +9.98vol、RR25 +2.02；positioning-ready但execution-ready=false，裸买Vega不优。
- **入场：** 好成交=21:45后3260—3310承接并重上3340，先1/2；重破3375且OI继续增加再加。中成交=3375突破后回踩3340不破，半风险。坏成交=>3420首跳、跌破3220或油价继续快速下挫，放弃。
- **退出：** 30分钟接受3200下方止损；TP1 3460、TP2 3650，分别出1/3；3日不达TP1退出。逻辑失效=backwardation显著收窄且OI转降。
- **情景R：** 3300成交约1.60R/3.50R；3340成交约0.86R/2.21R；>3420不做。
- **参数：** multiplier 10吨、tick 1元、tick value 10元；名义约33,380元，margin 7%（按settle约2,325元），limit 6%，last trading day=2027-01-14。12月中旬前退出/移仓。
- **压力：** 一/两个不利跌停约1,993/3,866元/手；最大损失不由止损限定。试仓风险≤NAV 0.50%。
- **催化/最坏情景：** 1—5D国内装置、进口与运费；最坏为地缘缓和、油价下挫和高位多杀多。

### 3. SN2611｜反抽失败空｜70

- **事实：** EOD 391410/391170，close -4.23%、settle -4.29%，volume 134,989、OI 34,969、ΔOI +3,724；curve近乎平坦。LME锡早前下跌约5.22%至51,447美元/吨。
- **时间纪律：** 公开Night记录为SN2610，而正式交易卡是SN2611，不能跨月做overnight/day decomposition；仓库与fallback均缺SN2611精确Night，故执行受限。
- **证据：** 支持=价跌仓增、LME同向、SN2611 put skew；反对=国内curve不弱、最近周度社会库存下降982吨、当前SHFE仓单采集失败。
- **最佳表达：** SN2611期货反抽失败空；10月26日到期390000/360000 bear put spread仅研究。ATM IV24.35%、RV20 23.65%、RR25 -2.89；execution-ready=false，不编净支出。
- **入场：** 好成交=反抽397000—401000失败并重新跌破395000；中成交=跌破389000后反抽不过389000，只用半风险；坏成交=直接<382000、重新站稳405000或LME锡重上53,500，放弃。
- **退出：** 30分钟接受405000上方止损；TP1 380000、TP2 370000；2日不达TP1减半，5日退出。逻辑失效=国内重新站稳405000且LME同步反弹。
- **情景R：** 398000成交约2.57R/4.00R；400000约1.67R/3.00R；直接下杀不追。
- **参数：** multiplier 1吨、tick 10元、tick value 10元；名义约391,410元。节后动态limit 12%、一般margin 14%，按settle保证金约54,764元；last trading day=2026-11-16。10月底前退出，避免交割月流动性和保证金上调。
- **压力：** 一/两个不利涨停约46,940/99,514元/手；期货最大损失不有限。试仓风险≤NAV 0.35%。
- **催化/最坏情景：** 1—5D LME库存、AI/电子需求叙事和美元；最坏为供应扰动、LME短挤和国内高开涨停。

## 八、商品期权专项

|Underlying|Expiry|ATM IV / RV20|IV-RV|RR25|S/P/E|判断|
|---|---|---:|---:|---:|---|---|
|AG2612|2026-11-24|36.39% / 31.44%|+4.95vol|+1.75|Y/N/N|call偏贵；只研究价差|
|MA701|2026-12-11|45.66% / 35.68%|+9.98vol|+2.02|Y/Y/N|事件Vega昂贵|
|SN2611|2026-10-26|24.35% / 23.65%|+0.70vol|-2.89|Y/N/N|put skew已计价部分下行|
|SC2611|2026-10-14|60.91% / 59.93%|+0.98vol|+1.12|Y/N/N|临近到期，gamma/流动性风险高|
|RU2701|2026-12-25|27.00% / 21.93%|+5.07vol|+3.22|Y/Y/N|call需求明显，追多成本高|
|LC2701|2026-12-07|45.13% / 38.18%|+6.95vol|-2.69|Y/N/N|put侧偏贵|
|FU2701|2026-12-18|61.80% / 45.19%|+16.61vol|+1.04|Y/N/N|裸买Vega不优|
|UR701|2026-12-11|13.11% / 12.42%|+0.68vol|+2.92|Y/Y/N|低IV不等于便宜|

全局positioning不足、bid/ask为0、Dealer Gamma方向未知。当前不存在可验证的vol RV或可成交期权优于期货的结论。固定声明：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、21:00夜盘开盘风险地图

严格区分：①10月9日中国完整EOD；②属于10月9日、今天凌晨已完成的Night，仅AG/SC有可核实主力fallback；③15:00—19:30海外新增定价；④今晚21:00尚未发生的Night，归属10月12日交易日。

|品种组|EOD/早前Night|15:00后海外|今晚预期|是否追首跳|等待|首要确认|
|---|---|---|---|---|---|---|
|AG/AU|AG日盘较Night反转+2.11%|金银上涨、美元偏弱|AG高开、AU小高|否|30m/15m|AG是否守14700、银是否守60|
|MA/PP/L/JM|国内显著上涨|油价回落，缺exact外盘|平/小低|否|45m/30m|MA 3260—3340、OI与curve|
|SC/FU/LU/BU/PG|SC弹性弱、FU/PG仍强|Brent/WTI回落；中国恢复成品油出口|偏低|否|45m|SC 728—735、backwardation是否收窄|
|SN/CU/ZN|SN大跌；CU/ZN偏弱|锡弱、金属外盘相对国内略强|SN低/平，CU平|否|30m|SN反抽395000、LME锡|
|RU/BR/NR|RU/BR价格强，RU curve转contango|精确橡胶增量缺|平开|否|30m|RU contango、BR OI与16600支撑|
|I/JM/J/RB|煤焦强、铁矿弱|SGX铁矿仅context|分化|否|30m|I 680、JM 1500与curve|
|M/Y/P/OI/RM|国内温和分化|WASDE前仓位调整|平开|否|45m|00:00 WASDE；夜盘不留裸事件Delta|
|EC/LC/SI/PS|EC、LC大跌|代理不足|**无制度夜盘**|不适用|10月12日09:45|EC contango、LC OI/现货|

今晚若开盘后已经越过上述等待窗口，条件必须用当时海外和国内实际成交重新核验；本报告的19:30映射不能冻结为未来指令。

## 十、未来24小时与7天事件日历（北京时间）

- **10月10日00:00：USDA 10月WASDE。** 豆粕、油脂、玉米、棉花和糖避免裸Delta；有真实报价时才考虑有限净支出凸性。
- **10月10日03:30：CFTC COT。** 仅用于验证海外拥挤，不反推中国会员方向。
- **周末：伊朗谈判、霍尔木兹/红海物流、飓风停产与中国成品油出口执行。** 能源仓位必须按周末gap和相关性破裂压力；没有持续交易窗口时不放大线性风险。
- **10月12日09:00：EC、LC、SI、PS等无夜盘品种下一实际日盘。** 至少等到09:45。
- **10月13日：MA611期权到期附近流动性/行权风险；** 本报告研究结构使用MA701，仍须核实行权交割。
- **10月14日16:00：IEA 10月Oil Market Report。** SC/FU/PG事件前缩Delta或采用已报价有限损失结构。
- **10月16日00:00：EIA截至10月9日当周石油周报。** 能源链关注原油、成品油库存和炼厂开工。

## 十一、旧建议台账

|idea_id|首次提出|上次状态|当前状态|变更原因|
|---|---|---|---|---|
|COM-E-AG2612-FAILED-REBOUND-SHORT-20261008|10月8日晚|等待反抽失败空|**失效/替换为新多头研究**|日盘反转、海外金银同向；价格变化|
|COM-M-MA701-MOMENTUM-HOLD-20261009|10月9日晨|等待回踩多|继续等待，75→72|日盘弹性下降、油价回落；新数据|
|COM-E-TA701-ENERGY-GAP-HOLD-20261008|10月8日晚|等待回踩多|原条件过期|close跌至6668、OI下降；价格变化|
|COM-E-RU2701-RUBBER-TIGHTNESS-20261001|10月1日|等待确认多|降级观察|curve转contango；新数据|
|COM-E-BR2612-RUBBER-CONFIRMATION-20261008|10月8日晚|等待回踩多|67分继续观察|price/OI/curve支持，但海外/参数缺失|
|COM-E-SC2611-SUPPLY-SHOCK-HOLD-20261008|10月8日晚|等待多|降为反弹空观察|Night弱、海外油价回落；观点修订|

任何“持有/退出”仅适用于若此前已按条件建立；无成交反馈，不声称用户持仓或账户净敞口。

## 十二、来源

- [China-Commodities-Engine unified report input](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（2026-10-09；支持EOD、Market State、Physical、External、Options）
- [China-Commodities-Engine root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（2026-10-09；支持五所覆盖与质量闸门）
- [财联社：10月9日凌晨SC/AG主力夜盘收盘](https://m.cls.cn/detail/2499946)（2026-10-09；支持SC 732.8、AG 14413）
- [证券时报：国内期货夜盘甲醇涨超7%](https://www.stcn.com/article/detail/4209631.html)（2026-10-09；支持MA主力Night方向，但非exact-contract）
- [Reuters：油价因伊朗谈判评论与中国成品油出口恢复而回落](https://www.reuters.com/business/energy/oil-falls-trump-comments-iran-talks-ease-supply-concerns-2026-10-09/)（2026-10-09）
- [Reuters：金银受弱美元和油价回落支持](https://www.reuters.com/world/india/gold-rises-softer-dollar-easing-yields-fed-outlook-focus-2026-10-09/)（2026-10-09）
- [Reuters：中国10月恢复成品油出口](https://www.reuters.com/business/energy/china-resume-october-fuel-exports-after-brief-halt-four-trade-sources-say-2026-10-09/)（2026-10-09）
- [SMM：LME锡与国内Night锡下跌、库存信息](https://news.metal.com/newscontent/104146823-lme-tin-plunged-522-to-51447mt-while-the-most-traded-shfe-tin-sn2610-contract-fell-450-in-the-night-session-breaking-below-the-390000-yuan-mark-smm-tin-morning-meeting-summary)（2026-10-09）
- [USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)（2026-10-09）
- [CFTC COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（访问于2026-10-09）
- [IEA October OMR](https://www.iea.org/events/oil-market-report-october-2026)（2026-10-14）
- [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（访问于2026-10-09）
- [SHFE 2026国庆后动态限幅与保证金通知](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)（2026-09-21）
- [SHFE Silver Futures Rules](https://www.shfe.com.cn/eng/services/Rules/SHFERules/202512/t20251231_829993.html)（访问于2026-10-09）
- [SHFE Tin Futures Rules](https://www.shfe.com.cn/eng/services/Rules/SHFERules/202512/t20251231_829998.html)（访问于2026-10-09）

## 十三、覆盖核对与未入榜异常

|板块|应覆盖|实际取数且已分析|数据不足/低流动性|未入榜最值得跟踪|
|---|---:|---:|---|---|
|软商品与特色农产品|10|6|JR/PM/RI/WH低流动性|EC -5.05%且深contango；CF仓单-73|
|黑色与建材|10|10|期权/高质basis普遍不足|JM +4.30%、I价跌仓增|
|能源与化工|26|25|ZC低流动性；多品种期权/参数缺|EG -4.16%、L/PP价涨仓增、UR价跌仓增|
|农产品油脂饲料畜牧|14|14|DCE期权缺；WASDE前事件风险|P +0.83%且OI增；OI/RM仓单下降|
|新能源与材料|3|3|GFEX仓单stale、无夜盘|LC -3.74%且OI增|
|有色与贵金属|14|14|SHFE仓单缺；多品种参数partial|SN -4.23%、AG日盘反转|
|**合计**|**77**|**72**|**5个低流动性；其余缺口按模块披露**|—|

策略类别扫描：方向、期限结构、基差、跨品种、跨市场、风格/中性、波动率/偏度/事件凸性均已检查；可执行RV仍因合约、币种、品质、运费税费或同步报价不完整而未成立。周期覆盖1D/3D/5D/20D；历史不足或roll污染项不输出伪趋势。商品期权目标64个产品，39个当日成功、25个缺失或失败；这不缩小应覆盖清单。

固定六路径完成后已从main回读验证：[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/10/2026-10-09_commodities_evening.md)。archive_status=success；ci_validation_status=pending_or_unverified。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：AG2612仅21:30后14650—14800承接并重上14850；MA701仅21:45后3260—3310承接并重上3340；SN2611仅397000—401000反抽失败后空，均须临盘核验海外、参数和流动性。  
C. 今晚应继续观察的机会：SC2611反弹失败、BR2612回踩、JM2701强势持续、RU2701 contango、EC/LC下周一重新定价及00:00 WASDE后的油脂饲料波动率。  
D. 今晚必须避免或退出的交易：避免追MA/AG第一跳、在390000附近追空SN、恢复旧TA多或AG空、无bid/ask期权及未定义配比的跨市场套利；若此前已建AG空应按14700收复失效退出。