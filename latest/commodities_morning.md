# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-08

prompt_version=radar_2026-09-06_coverage_v1  
实际生成：2026-09-08 07:11:40 北京时间；研究截点：07:00；最近完整中国EOD：2026-09-07；当前交易日：2026-09-08；下一实际交易窗口：09:00日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；PG2610、MA610存在待验证多头优势，FG701出现失败挤压空头线索，均应等开盘确认。**

当前regime是：**油价地缘溢价已由SC大量预交易、LPG/甲醇出现链内补涨，玻璃/纯碱夜盘反转，橡胶挤压分化，贵金属仍受实际利率约束。**

## 二、数据质量与覆盖

本期依次读取了 [统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) 和 [Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻逐合约Night、Options surface与metadata。

- 统一输入schema_version=2，requested_date=2026-09-07，generated_at=2026-09-08 06:15:25+08:00。
- Futures/Market State：五所SHFE/INE/DCE/CZCE/GFEX共802个合约，full_market_ready=true、source_date_match_pct=100%、critical errors=0；7条OHLC placeholder已排除。official_complete=false来自basis/会员排名缺失、metadata与仓单部分覆盖，不是否定核心EOD。
- Night Session：trading_date=2026-09-08、night_session_date=2026-09-07，06:02:17生成；data_fresh、validation_passed、published、coverage_complete均为true。610个有效夜盘合约、189个合法outside-night-window、3个no-night-trade；missing timestamp/price/quote、query error、unresolved contract均为0。这是**属于今日交易日、今晨已经完成的连续交易阶段**，日期语义正常，不是未来行情。
- Physical：9月7日20个目标中18个按原生频率fresh，SC/LU不可得，无stale/carry；basis全部为C级、缺交割地/品级/地区/含税口径，只作context。仓单仅CZCE为当日fresh，GFEX五项沿用9月1日；仓单不冒充社会库存。
- External：repo日频17/22有效；美国劳动节使CBOT/ICE农业最新完整观测仍为9月4日，并非异常。07:00另补充9月7日国际油、金银、美元、橡胶和棕榈油最新时段。
- Options：9月7日19,560张chain、354个series、52/64产品；IV coverage 93.92%、OI coverage 68.68%、bid/ask coverage 0。全局surface/positioning/execution均false；局部338个series可作曲面研究、76个可作持仓研究、0个可执行series。缺SC、AU、AG及多数SHFE有色贵金属产品，Dealer Gamma方向未知。
- Contract Metadata：effective contract match约73.32%；动态margin/limit等覆盖约29.8%。前三卡中MA610、FG701参数可核实，PG2610仅可从DCE合约规则核实标准乘数、tick与最后交易日规则，动态保证金/限幅未确认。

## 三、商品仪表盘

Night涨跌以相对9月7日EOD close为主、相对settlement仅作辅助。量与OI均为手；价格为各合约报价单位。

| 板块/合约 | 9/7 close/settle；1D/5D | EOD volume/OI/ΔOI；curve | Basis/Physical | Night close；vs close/settle；ΔOI；质量时间 | 07:00海外/Options | 09:00信号 |
|---|---|---|---|---|---|---|
| LPG **PG2610** | 6587/6549；+0.40%/+8.02% | 16.2万/10.5万/-2,999；BWD +3.71% | Physical缺完整独立层 | 6702；**+1.75%/+2.34%**；+4,722；fresh 23:00 | Brent 97.31、WTI 92.65；IV 41.76% vs RV20 30.31%，无报价 | **条件多，等30m** |
| 甲醇 **MA610** | 3212/3168；-1.19%/+8.83% | 248.7万/62.1万/+14,234；BWD +3.82% | C级basis，仅context | 3245；**+1.03%/+2.43%**；+46,551；fresh 23:00 | 油价支持；IV-RV +16.19vol，无报价 | **reclaim多，等30m** |
| 玻璃 **FG701** | 976/978；+0.72%/+4.04% | 161.1万/118.1万/-27,835；Contango -4.75% | spot-futures=-10，仅C级 | 964；**-1.23%/-1.43%**；+20,518；fresh 23:00 | 无exact外盘；IV-RV +1.75vol，无报价 | **failed-squeeze空** |
| 天胶 **RU2701** | 19180/19110；+1.81%/+1.25% | 49.3万/16.4万/+11,338；Contango -1.02% | 实体层不足 | 19390；+1.09%/+1.47%；+6,031；fresh 23:00 | 海外胶价代理+0.73%；IV-RV +10.28vol | 多但不追，等30m |
| 20号胶 **NR2611** | 16345/16260；+2.43%/+1.50% | 13.5万/7.9万/+5,754；近似平/轻contango | 实体层不足 | 16580；+1.44%/+1.97%；+1,609；fresh 23:00 | 海外胶价同向；IV-RV +9.07vol | 等三胶breadth |
| 丁二烯胶 **BR2611** | 15455/15425；+3.80%/+5.65% | 18.1万/9.7万/+14,756；BWD +1.54% | 实体层不足 | 15410；**-0.29%/-0.10%**；-2,683；fresh 23:00 | 海外胶价未同步大涨；无报价 | 上期多头降级 |
| 原油 **SC2610** | 699.3/688.5；+0.79%/+11.35% | 19.6万/3.9万/+3,181；BWD +6.17% | SC Physical不可得 | 700.4；**+0.16%/+1.73%**；-224；fresh 02:30 | Brent/WTI续涨；SC期权缺失 | 新闻强、弹性弱 |
| 燃油 **FU2611** | 3880/3799；-1.89%/+1.63% | 99.0万/20.3万/-2,910；BWD +4.58% | C级basis | 3877；-0.08%/+2.05%；+1,652；fresh 23:00 | 油强但FU未跟；IV-RV +16.80vol | SC-FU仅观察 |
| PVC **V2701** | 5051/5057；+0.34%/+7.69% | 219.2万/109.8万/-37,484；Contango -1.19% | 实体层不足 | 5011；**-0.79%/-0.91%**；-1,808；fresh 23:00 | IV 21.72% < RV20 25.34%，无报价 | failed-squeeze空观察 |
| 纯碱 **SA701** | 1079/1091；+1.02%/+3.41% | 243.2万/125.6万/+37,247；Contango -6.16% | C级basis | 1064；**-1.39%/-2.47%**；+30,192；fresh 23:00 | 无exact外盘；IV-RV +4.19vol | 反转最强，不追首跌 |
| 黄金 **AU2610** | 950.78/954.52；-1.68%/-2.42% | 30.8万/15.5万/-3,835；轻contango | 无完整实体层 | 954.10；+0.35%/**-0.04%**；+1,047；fresh 02:30 | 现货金-0.4%至4410.55；期权缺失 | 仅修复settle |
| 白银 **AG2610** | 15990/16025；-1.80%/-3.86% | 51.4万/20.0万/-8,318；近似平 | 无完整实体层 | 16143；+0.96%/+0.74%；+3,419；fresh 02:30 | 现货银约+0.1%；期权缺失 | 中国beta偏高，等15m |
| 棕榈油 **P2701** | 10354/10264；+0.51%/+0.22% | 75.0万/61.8万/+31,139；曲线近乎平 | C级basis | 10455；+0.98%/+1.86%；+17,407；fresh 23:00 | BMD棕榈油+0.99%；IV-RV +7.72vol | 同向但赔率一般 |
| 铁矿 **I2701** | 734.5/734.5；+1.17%/+1.24% | 30.3万/58.9万/+6,223；Contango -1.61% | C级basis | 741.5；+0.95%/+0.95%；-1,572；fresh 23:00 | SGX铁矿100.8；IV-RV +5.69vol | 等30m，结构未确认 |
| 乙二醇 **EG2610** | 5773/5801；-0.74%/+11.69% | 261.7万/34.9万/-43,080；BWD +7.62% | 实体层不足 | 5740；-0.57%/-1.05%；-6,299；fresh 23:00 | 油强而EG弱；IV-RV +10.67vol | 趋势弹性衰减 |

国际油价9月7日升至约六周高位，Brent 97.31美元/桶、WTI 92.65美元/桶；这是海外支持，不是中国期货已交易该信息的证明。[Reuters油市，2026-09-07](https://www.reuters.com/business/energy/oil-extends-gains-after-us-iran-strike-ships-2026-09-07/) DXY约98.9、日内-0.2%，USD/CNH约6.7096，人民币变化小，不是今晨商品排序的主要驱动。[Reuters外汇](https://www.reuters.com/world/india/rupee-may-withstand-oil-fed-pressures-with-rbi-support-2026-09-07/) [USD/CNH行情](https://www.investing.com/currencies/usd-cnh)

## 四、相比上一交易日/今晨真正变化

1. **SC从“事件多头”降为已预交易观察。** 9月7日日盘close已到699.3；今晨Night只相对close再涨0.16%，但相对settlement仍+1.73%，这正是双锚分歧：新闻溢价很高，新增价格弹性却很低。SC2610/SC2611曲线由EOD约+6.17%收窄到Night约+5.94%，Night ΔOI -224。昨晚“回撤接受多”条件未出现704/709突破，按可核实OHLC未触发。
2. **LPG与甲醇接棒成为能化内部最强。** PG +1.75% vs close且Night ΔOI +4,722、back基本稳定；MA +1.03%且Night ΔOI +46,551，但back由约3.82%压缩到约1.45%。这支持“链内补涨”，不支持“所有能化一起追”。
3. **SA/FG出现失败挤压。** SA Night -1.39%且ΔOI +30,192，FG -1.23%且ΔOI +20,518；两者contango仍深。价格/OI只能叫归因线索，但至少说明周一白天的强势没有在Night延续。
4. **橡胶链由BR单点挤压切换成RU/NR breadth。** BR白天+3.8%，Night却-0.29%、OI下降；RU/NR分别+1.09%/+1.44%，海外胶价代理仅+0.73%。此前BR条件多降级，未获得实体短缺确认。
5. **贵金属没有形成“黄金信用”新多头证据。** AU Night相对close +0.35%但仍略低于settlement，国际金周一收跌0.4%；AG中国夜盘弹性明显大于海外银，可能是beta修复，不足以证明独立趋势。[Reuters贵金属，2026-09-07](https://www.reuters.com/world/india/gold-eases-robust-us-payrolls-boost-rate-hike-bets-inflation-data-focus-2026-09-07/)
6. **期权覆盖反而退步。** 产品成功数从上一晚的58/64回到52/64；这是数据覆盖变化，不是市场波动率信号。V的IV低于RV只是研究线索，无bid/ask时不能称便宜且可执行。

旧建议台账：SC idea COM-E-SC2610-GAP-20260905降为观察；SC-FU idea COM-E-SC-FU-RV-20260907隔夜仅扩约0.24个百分点，保留但不升级；AU idea COM-E-AU2610-RATE-GEO-20260905未触发949下破；BR idea COM-M-BR2611-NIGHT-SQUEEZE-20260907因Night回吐降至58分研究池；V idea COM-E-V2701-SQUEEZE-20260904延续。无成交反馈，不假设用户已持仓。

## 五、产业链地图

- **最强：PG—MA事件补涨链，偏多，置信度中高。** 价格/OI、EOD back与海外油构成1/2/4三层支持；最大缺失是PG实体与高质量basis、MA curve收窄、期权无执行报价。它们不是exact crack/import parity套利。
- **最弱：SA—FG—V材料挤压退潮，偏空，置信度中。** Night否定日盘强势，contango确认供给并未呈典型近端紧张；但没有高质量实体层，且开盘再低开会压缩空头赔率。
- **橡胶：RU/NR强、BR弱，置信度中。** Night breadth从BR转移，RU近端曲线改善但代表合约EOD仍contango；海外橡胶仅温和上涨。最强竞争解释是国内仓位轮动而非全球短缺。
- **原油—燃料：headline强、marginal elasticity弱，置信度中。** SC Night几乎不再涨，FU甚至略跌，SC-FU相对价值只保留观察；若09:00油品仍无breadth，原油事件溢价更接近单品种而非全链供需。
- **油脂与农产品：P/Y获得BMD支持，但CBOT因劳动节没有9月7日完整时段。** P价量仓同向，但curve近乎平、IV不便宜；农产品没有足够独立层进入70分。航运EC和新能源LC/SI/PS也未出现可验证的新异常。

## 六、机会排行榜

| 排名 | 机会/idea_id | 分项：逻辑/赔率/催化/价曲波/技术 | 总分 | 支持层 | 研究判断；证据；执行 |
|---|---|---:|---:|---|---|
| 1 | PG2610回撤确认多 / COM-M-PG2610-OIL-BREADTH-20260908 | 21/18/17/12/8 | **76** | 1、2、4 | 存在待验证优势；部分；等30m |
| 2 | MA610 settlement-reclaim多 / COM-M-MA610-SETTLE-RECLAIM-20260908 | 21/17/14/12/9 | **73** | 1、2、4 | 存在待验证优势；部分；等30m |
| 3 | FG701 failed-squeeze空 / COM-M-FG701-FAILED-SQUEEZE-20260908 | 19/18/10/12/10 | **69** | 1、2 | 存在待验证优势；部分；等30m |
| 4 | RU2701橡胶breadth多 / COM-M-RU2701-RUBBER-BREADTH-20260908 | 20/16/12/11/10 | **69** | 1、4；2层混合 | 存在待验证优势；部分；等30m |
| 5 | V2701 failed-squeeze空 / COM-E-V2701-SQUEEZE-20260904 | 19/18/9/11/11 | **68** | 1、2 | 存在待验证优势；部分；等30—45m |

分数由五项直接相加并已复核；分数仅是研究排序，不是胜率或仓位。PG/MA虽达70+，仍缺当前09:00成交路径；所有期货结构最大损失均不受限定。

## 七、前三名交易卡

### No.1 PG2610｜条件多｜76

**事实：** EOD 6587/6549；Night 6600/6731/6553/6702，+1.75% vs close、+2.34% vs settlement，ΔOI +4,722；EOD back约3.71%，Night同对曲线约3.68%。  
**市场定价：** 原油右尾已很贵，但PG相对SC体现更高Night弹性。  
**推断：** 市场可能在补交易LPG自身进口成本/供应风险，而不是简单追SC。  
**主观判断：** 值得冒险的是回撤后再次接受，不是09:00首跳。

- 最佳表达：1手PG2610期货；两腿配比不适用。期权仅研究，execution=false。
- 好成交：6640—6680承接后重上6705/VWAP，先1/3；净R按实际入场到6550的风险定义。
- 中成交：突破6735后回踩不破，仓位减半；坏成交：直接高于6800且不回撤，放弃。
- 止损：30分钟接受6550下方；逻辑失效：跌破6549、back明显塌陷且Brent跌回约95.5以下。
- 退出：TP1 6820或1.5R，TP2 7050或3R；1—3D时间止损，首个1R减回成本风险。
- 成本/滑点：只允许限价；预算至少2—4 ticks加滑点，开盘流动性断层按更差价格压力测试。
- 风险预算：0.30%—0.50% NAV；与SC/FU/LU/MA合并计算。
- 参数：DCE标准20吨/手、tick 1元/吨、tick value 20元；按6702名义约13.40万元。最后交易日规则为交割月倒数第4个交易日，实物交割；PG2610确切日期、动态margin/limit本版未确认，下单前复核。[DCE LPG合约](https://www.dce.com.cn/dalianshangpin/sspz/yhsyq/hyygz7622/6210766/index.html)
- 压力：一板=134,040×当日官方L；两板=134,040×[1-(1-L)^2]。止损不是最大损失上限；交割月前主动roll。
- 1—20D催化：霍尔木兹航运、OPEC+执行、EIA库存；最坏情景是地缘快速缓和、进口成本回落、开盘流动性消失并穿透止损。

### No.2 MA610｜条件多｜73

**事实：** EOD close/settle 3212/3168；Night 3217/3246/3189/3245，+1.03%/+2.43%，ΔOI +46,551；EOD back约3.82%，Night近端同对压缩到约1.45%。  
**市场定价：** Night价格重新站上日盘close，但曲线没有同幅强化。  
**推断：** 这是较高质量的价格/OI延续，却可能只是原油beta与仓位追随。  
**主观判断：** 只做价格与curve共同稳定后的短持有期多头。

- 最佳表达：1手MA610期货；两腿配比不适用。
- 好成交：3210—3230回撤被吸收后重上3246；中成交：3260上方突破回踩，仓位减半；坏成交：>3300无回撤，放弃。
- 止损：30分钟接受3188下方；逻辑失效：跌破3168且back进一步压至近乎平坦。
- 退出：TP1 3310/1.5R，TP2 3400/3R；1—2D无扩张即离场。
- 风险预算：0.25%—0.45% NAV；与PG/SC能化因子合并。
- 参数：10吨/手、tick 1元/吨、tick value 10元；3245名义约32,450元。repo 9月7日参数为margin 7%、limit 6%，最后交易日2026-10-21、最后交割日10-26，实物交割；夜盘有效至23:00。
- 压力：按3168结算，一板不利约1,901元/手，两板复合下跌约3,688元；计划止损不限制极端损失。进入10月交割风险窗口前roll。
- 最大反证：曲线压缩、现货basis仅C级、期权IV-RV约+16.2vol且无报价；不能把贵期权本身当方向证据。

### No.3 FG701｜条件空｜69

**事实：** EOD 976/978；Night 975/975/959/964，-1.23%/-1.43%，ΔOI +20,518；EOD contango约-4.75%，Night同对约-5.11%。  
**市场定价：** 日盘挤压没有延续，且期限结构进一步反对近端短缺。  
**推断：** 失败挤压比趋势空更可信；但低开过多后赔率会迅速消失。  
**主观判断：** 只卖失败反抽，不追首跌。

- 最佳表达：1手FG701期货空；两腿配比不适用。
- 好成交：反抽968—975失败后再破963；中成交：跌破959后回抽不过，仓位减半；坏成交：直接低于950，放弃。
- 止损：30分钟重新接受980；逻辑失效：突破991、OI回落且contango快速收窄。
- 退出：TP1 940/1.5R，TP2 915/3R；1—2D时间止损。
- 风险预算：0.25%—0.40% NAV；与SA/V同一材料挤压因子合并。
- 参数：20吨/手、tick 1元/吨、tick value 20元；964名义约19,280元。repo参数margin 9%、limit 8%，最后交易日2027-01-14、最后交割日01-19，实物交割；Night记录至23:00。
- 压力：按978结算，空头一板上涨约1,565元/手，两板复合约3,255元。最大风险是政策/产业消息令挤压重启并连续涨停。

## 八、商品期权专项

结论：**期权目前不优于裸期货，不是因为已证明全部昂贵，而是执行报价为零。**

- PG2610 9月16日到期：ATM 6500，ATM IV约41.76%，RV20约30.31%，IV-RV约+11.45vol，RR25 +3.48、BF25 +6.12；surface-ready但positioning/execution均false。
- MA610 9月11日到期：ATM 3200，IV约46.42% vs RV20 30.23%，期限极短、IV溢价高；不适合在无报价时买裸event vol。
- FG701 12月11日到期：ATM 960，IV约21.27% vs RV20 19.51%，RR25 +5.52；可研究下行价差，但无bid/ask不能判断净支出。
- RU2701 IV约22.98% vs RV20 12.70%、RR25 +5.39；P2701 IV约17.53% vs RV20 9.81%、RR25 +7.42，均显示上行偏度/波动溢价，不等于Dealer净Gamma方向。
- V2701 IV约21.72%低于RV20约3.62vol，是长波动线索；但无live moneyness与bid/ask，不输出跨式价格。
- SC/AU/AG缺产品链，无法比较event convexity；新上市HC/SS/LU期权在9月10日首日也没有可比历史surface。

任何结构均为：research only; manual quote and manual confirmation required before execution; no premium quoted。

## 九、9:00开盘风险地图

严格三层：Layer 1是9月7日中国EOD；Layer 2是归属9月8日、今晨已完成的Night；Layer 3是截至07:00可得的海外最新时段。中国09:00日盘尚未发生。

| 合约 | 预期开盘/是否已定价 | 内外冲突 | 追价？/等待 | 最重要确认 |
|---|---|---|---|---|
| PG2610 | 偏高，Night已大量定价 | 油价同向 | 不追；30m | 6702/6731、back、OI |
| MA610 | 偏高，Night已定价 | 油支持但curve压缩 | 不追；30m | 3212/3246、curve |
| FG701 | 偏低，Night否定EOD | 无exact外盘 | 不追空；30m | 959/964/978、OI |
| SA701 | 低开风险高 | 国内结构和价格同向转弱 | 不追；45m | 1059/1079、contango |
| RU/NR | 偏高，已定价较多 | 海外胶仅温和同向 | 不追；30—45m | 三胶breadth、RU curve |
| BR2611 | 平/偏低 | EOD强、Night弱 | 不追；45m | 15375/15455、OI |
| SC2610 | 平/小高，事件大部已交易 | 海外强、国内弹性低 | 不追；45m | 699.3/701.7、back |
| FU2611 | 平 | 海外油强、FU弱 | 不追；30m | 3850/3905、SC-FU同步 |
| V2701 | 低开 | 无可靠外盘 | 不追空；30—45m | 4972/5011/5051 |
| AU2610 | 平 | 国际金弱、Night仅修复 | 不追；15—30m | 950.98/954.52、DXY/收益率 |
| AG2610 | 偏高 | 中国弹性高于海外银 | 不追；15—30m | 16000/16282、AU联动 |
| P/Y | 偏高 | BMD同向、CBOT尚无新完整时段 | 不追；30m | P 10330/10468、curve |
| I2701 | 偏高 | SGX背景支持、contango反对 | 不追；30m | 734.5/745、黑色breadth |
| EG2610 | 偏低 | 油强、EG弱 | 不抄底；45m | 5655/5801、back |

SC的External↑→China Night近乎平，信息弹性低；PG/MA的External↑→China Night↑，弹性更高。AU/AG则发生海外金弱、国内银修复的分歧，不能直接追beta。

## 十、未来24小时 / 7日事件

- **9月8日09:00中国日盘：** 首次检验PG/MA补涨及SA/FG失败挤压；所有候选先缩Delta、延迟15—45分钟。
- **9月9日04:00北京时间：** USDA Crop Progress因劳动节延至美东9月8日16:00；关注玉米/大豆成熟、优良率与棉花结铃，数据前不放大M/Y/P/C/CF无保护Delta。[USDA日程](https://esmis.nal.usda.gov/publication/crop-progress)
- **9月9日09:30：** 中国8月CPI/PPI；黑色、化工、工业金属的价格需求预期重置。[国家统计局发布日程](https://www.stats.gov.cn/sj/fbrc/)
- **9月10日09:00：** HC、SS、LU期权上市；首日只观察chain、surface与bid/ask，不拿旧品种IV做代理。[SHFE公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html) [INE公告](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)
- **9月10日20:30：** 美国8月PPI；**9月11日20:30：** 美国8月CPI。AU/AG、油价及美元因子在数据前降低Delta/Vega；若需凸性，必须等待可执行报价。[BLS日程](https://www.bls.gov/schedule/2026/home.htm)
- **9月11日00:00—02:00附近：** 劳动节顺延的EIA周度石油数据；PG/SC/FU/LU重点看成品库存与炼厂利用率，避免把headline多头带入库存赌局。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月11日16:00：** IEA Oil Market Report；**9月12日00:00：** USDA WASDE。油品和油脂饲料在事件前缩仓；期权只有报价与最大净支出可确认时才做有限凸性。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- CFTC COT通常周五15:30 ET发布，但劳动节可延迟；只作截至前一周二的拥挤背景，不解释今晨Night。[CFTC发布说明](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖核对、风险预算与归档

强制63个代码全部完成期货层1D/3D/5D/20D可得指标、量仓、curve、产业链和策略类别扫描；另纳入PL、PD、PT、BZ、LG、RR、OP、WR八个动态流动性合格品种，共71个实际分析。JR、PM、RI、RS、WH、ZC因零价、零成交/持仓或制度性低活跃列为不适用/流动性不足。

- 黑色建材：应覆盖9、实际9；未入榜最值得跟踪I2701 Night +0.95%，但contango未确认。
- 有色贵金属：应覆盖12、实际12；未入榜AG中国Night beta高于海外，AU只修复settlement。
- 能源炼化化工：应覆盖25、实际25；PG/MA入榜，EG在油强背景下继续走弱是最重要反向异常。
- 新能源：应覆盖LC/SI/PS及新材料，实际3+PD/PT/PL；无70分异常，GFEX仓单为9月1日carry，不能计新增证据。
- 农产品油脂饲料畜牧：应覆盖22、实际22；P/Y Night同向最强，但CBOT无9月7日完整时段，证据不足。
- 航运软商品：EC及CF/CY/SR/AP/CJ/PK均分析；无exact海外映射或三层共振。

数据不足：SC/LU实体、全部A级/B级exact basis、import parity、12个失败期权产品、全部期权执行报价、partial metadata、SHFE/DCE仓单。方向、跨期、基差、跨品种、跨市场、风格/中性篮子、波动率/偏度/事件凸性与1D—20D周期均已扫描；SC-FU仅近似美元中性且未校准裂解beta，不称套利或beta-neutral。

单笔试仓最大损失0.25%—0.50% NAV，确认后0.75%—1.0%；PG+MA+SC/FU/LU合并为油价因子，FG+SA+V合并为材料挤压因子。压力测试一/两板、gap、保证金上调、流动性消失、相关性破裂、人民币急变、IV跳升/塌陷和交割挤压。

归档按六路径direct-to-main执行；历史MD/JSON、latest MD/JSON、status与manifest均以2026-09-08 commodities_morning为唯一键，CI不轮询，记录pending_or_unverified。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：PG2610在6640—6680承接并重上6705，或MA610在3210—3230承接并重上3246；均须等待30分钟、先1/3仓。  
C. 今天应继续观察的机会：FG701反抽失败空、RU/NR橡胶breadth、V2701 failed-squeeze、SC-FU相对价值及P/Y油脂联动。  
D. 今天必须避免或退出的交易：09:00首跳追PG/MA/SC/RU、低开追空SA/FG/V、继续追BR挤压、把C级basis当套利、以及在execution_ready=false时臆测期权成本。