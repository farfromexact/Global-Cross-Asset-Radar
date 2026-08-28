# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-28

> 数据截止：北京时间 2026-08-28 19:30。中国夜盘尚未开始；本报告不使用、也不推断21:00之后的中国价格。  
> 数据协议：`china_commodities_v2`。本次为同日 revision 2；原因是早先19:30:09版本恰逢汇总层未闭环，而核心Futures与独立Options实际分别在19:23:52、19:24:33已生成，`report_input_latest.json`于19:41:26完成重建。本次未持续轮询等待Options。

## 一、今日一句话结论

**有值得冒险的条件机会，但没有应在21:00前预埋的仓位：AG顺势多76分、SC溢价回吐空74分，均须夜盘确认；JM仅69分观察。**

今天的核心不是“找一个最强商品追进去”，而是利用**中国EOD与15:00—19:30海外定价的不同步**。AG是同向确认但已拥挤，SC是最清楚的内外盘确认背离。两者都不适合在夜盘集合竞价或第一跳直接追。

## 二、数据质量与覆盖说明

本次通过已连接GitHub读取 `farfromexact/China-Commodities-Engine`，第一层实际读取：
- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`

按需进一步读取 `data/contract_meta.json`；交易参数缺口再用交易所官网核验。`report_input`：requested_date=`2026-08-28`，generated_at=`2026-08-28T19:41:26.332469+08:00`。核心Futures生成于19:23:52，独立Options生成于19:24:33，因此二者均是夜盘前已经完成的T日数据；19:41只是统一汇总层重建时间。

**核心期货闸门通过**：五所 SHFE/INE/DCE/CZCE/GFEX 全覆盖，803个合约，`full_market_ready=true`，`source_date_match_pct=100%`，unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、critical errors=0；存在5个placeholder，已排除异常排行。`official_complete=false`不改变本次“verified vendor primary”的研究可用状态。

**Physical是部分覆盖，不自动算方向层**：当前映射4条，包括I港口库存、JM旬度NBS现货、FG周度企业库存、TA周度加工费。`fresh`只表示处在各自原生发布频率的有效期，不代表今日变化。JM唯一basis为C级，且期货参考腿是8/27，缺少完整口径对齐，**不计分、不称套利**。

**External按series判断**：repo 22个目标映射6个，5 fresh、1 stale；Brent、LME Cu、SGX铁矿、USDCNH、DXY为日频背景，BMD palm 4月数据剔除。没有可执行import parity。15:00—19:30海外变化单独通过Reuters补充，绝不冒充中国日盘变化。

**Options是T日研究层可用、执行层不可用**：21,806条记录，product coverage 95.31%，370个series中363个`surface_ready=true`、74个`positioning_ready=true`、0个`execution_ready=true`；IV coverage 98.59%，OI coverage 68.16%，bid/ask coverage=0。因此可用ATM IV/RR25/BF25/IV-RV做研究，但**不得声称当前可按某个权利金成交，也不推断dealer gamma方向**。

**Contract metadata仍partial**：engine的DCE contract-info存在JSON decode error，GFEX metadata也有partial/stale标记。SC动态涨跌停、保证金与夜盘已通过INE最新官方页面核实；AG只采用标准合约与连续交易的官方规则背景，动态margin/limit未确认；JM动态margin/limit及当前夜盘时段本次未独立确认，因此明确留空。

数据源入口：
- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- INE交易时间: https://www.ine.cn/services/calenderandholidays/tradinghours/
- INE原油标准合约: https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html
- INE 2026-06-23 SC/LU风控参数调整: https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html

## 三、商品仪表盘

| 板块 | 品种/合约 | 最新有效价 | 1D / 5D | Volume / OI / ΔOI | Curve | Basis / Physical | Options | 信号 |
|---|---|---:|---|---|---|---|---|---|
| 黑色 | JM2701 | close 1629 / settle 1623 | +1.95% / +3.31%；20D +21.35% | 1,039,129 / 597,545 / **+7.93%** | **+1.53% backwardation** | NBS焦煤现货2043.1元/吨为8/20旬度水平；basis C，不计分 | ATM IV32.32 vs RV20 20.54；surface+positioning ready；execution false | 趋势最整齐，但拥挤且实体未闭环 |
| 黑色/建材 | FG701 | 927 / 918 | +1.32% / 5D未单独钻取 | 1,513,705 / 1,504,372 / 未钻取 | **-2.67% contango** | 企业库存7404.9重量箱，8/28周度水平，无方向变化 | 未用于方向评分 | 涨价未获curve/physical确认 |
| 贵金属 | AG2610 | 17215 / 16818 | settle +0.77%；close vs pre +3.15% / 5D +1.25%；20D +17.71% | 765,356 / 261,945 / **+5.77%** | -0.14%，近乎平坦contango | 无完整实体层 | ATM IV48.08 vs RV29.71；RR25 +7.21；execution false | **76分条件多**；不追首跳 |
| 有色 | CU2610 | 108620 / 108660 | +0.15% / +3.01%；20D +8.29% | 154,411 / 198,417 / +1.65% | -0.64% contango；curve z≈-2.87 | 无A/B basis/实体层 | 未用于方向评分 | 价格强而curve弱，不追 |
| 能源 | SC2610 | 596.5 / 592.3 | settle +3.24%；close vs pre +3.97% / 5D -0.02% | 未单独记录 / 未单独记录 / **+15.93%** | **-1.37% contango** | 无完整实体层 | ATM IV45.71 vs RV34.50；RR25 -2.07；execution false | **74分条件fade空** |
| 化工 | TA701 | 5630 / 5596 | +1.23% / 5D未单独钻取 | 746,791 / 868,133 / 未钻取 | **+1.57% backwardation** | PTA加工费677.532元/吨，8/28周度水平 | 未用于方向评分 | price+curve偏强，实体方向缺 |
| 新能源 | LC2701 | 159600 / 156000 | +2.40% / 3D +1.33% | 239,379 / 391,884 / 未钻取 | **-1.15% contango** | physical mapping unavailable | T日series存在；execution false | 价格涨+contango，不能写短缺 |
| 油脂饲料 | M2701 | 3340 / 3344 | +0.60% / 5D未单独钻取 | ≈165.7万 / ≈274.5万 / 未钻取 | -0.96% contango | 无实体/进口压榨闭环 | ATM IV15.34；RR25 +4.26；surface+positioning ready | 不追；call skew偏贵 |
| 软商品 | CF701 | 17180 / 17200 | +1.06% / +0.76%；20D +6.01% | 464,467 / 604,731 / **+7.32%** | -1.64% contango | repo physical unavailable；天气仅先验 | ATM IV13.15；RR25 +1.84 | 价涨仓增但curve不确认 |
| 建材化工 | SA701 | 1047 / 1027 | settle +1.08%；close vs pre +3.05% / 5D -0.39% | 1,902,641 / 1,154,367 / **-4.50%** | **-3.41% contango** | 无完整实体层 | SA多series surface-ready；未提取SA701 exact IV | **price_up_oi_down归因线索**，偏fade观察 |
| 航运 | EC2610 | 1825 / 1866.5 | close -1.83%；settle +0.40% / 未钻取 | 未钻取 | +27.53%，明显合约/季节性结构风险 | 无可执行跨市场basis | 无执行层 | close/settle分裂；INE确认无夜盘 |

注：价涨仓增/价涨仓减只是**归因线索**，不写成“新多”“空头回补”的确定事实。

## 四、相比上一交易日/上一版真正变化

1. **最重要的变化是数据状态，不是价格本身。** 同日revision 1因为恰好在19:30:09看到汇总层尚未闭环而“No Trade”；现在确认T日Futures与Options分别在19:23:52/19:24:33已经完成，五所交易日一致，整个商品雷达可以从T-1降级状态恢复为T日评分。
2. **AG从事件观察升为条件多。** 中国尾盘明显强于结算，OI +5.77%；Reuters在18:32 BJT报道spot silver +1.8%至约70.51美元/盎司，海外与中国方向同向。但20D已+17.7%，且AG ATM IV 48.08%显著高于RV20 29.71%，call skew昂贵，不允许追21:00第一跳。[Reuters](https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/)
3. **SC出现更有交易价值的“确认背离”。** 中国SC settle +3.24%、ΔOI +15.93%，但5D几乎不涨、curve仍contango；Reuters在17:43 BJT附近给出的Brent约89.66美元/桶、当日近持平，且周线约-5.1%。这不是“海外已经跌所以SC必跌”，而是中国日盘涨幅暂未被海外确认。[Reuters](https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/)
4. **JM成为黑色里最干净的趋势组合。** 1D/3D/5D/20D均正、OI +7.93%、backwardation +1.53%。但实体层只有旬度spot水平且basis C，方向证据不够第三层，所以分数压在69。
5. **大量“价格上涨+contango”在LC/CU/FG/SA出现。** 这更像风险偏好、资金/仓位与不同合约结构共同驱动，而不是可以直接写成“现货短缺”。

## 五、产业链地图

| 产业链 | 方向 | 最强/最弱 | 价格与Curve | 实体/仓单 | 期权 | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|
| 贵金属 | 偏多但事件驱动 | AG最强 | price强，curve仅近乎平坦 | 无完整实体层 | IV高、call skew贵 | 银18:32 +1.8% | Warsh之后的美元/实际利率反应 | 中高，条件性 |
| 原油-燃料油 | 中国溢价偏高，倾向fade | SC日盘最强但海外不确认 | +3.24%，仍contango | 无fresh实体闭环 | IV-RV +11.2 vol pts | Brent近持平、周跌约5.1% | Hormuz突发标题 | 中 |
| 焦煤-焦炭-钢材 | JM偏多 | JM | 多周期上涨+backwardation | spot仅水平；basis C | JM surface+positioning ready，IV贵 | SGX铁矿仅repo 8/27 EOD | 铁水/补库/现货方向 | 中 |
| 纯碱-玻璃 | 冲高但供需不确认 | SA价格最猛，FG跟随 | 两者contango | FG只有周度库存水平 | SA surface存在 | 无有效映射 | 库存方向、A/B basis | 中低 |
| 新能源/有色 | 价格强、curve偏弱 | LC/CU | 两者contango | physical覆盖弱 | 未形成方向确认 | LME Cu repo只到8/27 EOD | 19:30 live LME/CNH+physical | 中低 |

**最强产业链：贵金属的跨时区动量。最弱/最不值得追的链：价格涨但curve不确认的新能源/部分工业品。** 当前regime更像“risk-on burst + event volatility”，而不是广谱缺货牛市。

## 六、机会排行榜

评分纪律按本次实际fresh层重算；Physical level、stale series、C级basis不计方向层。

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段 | Fresh层 | 工具 | 关键数据惩罚 |
|---|---|---:|---|---|---|---|---|
| 1 | AG2610 21:00确认后顺势多 | **76** | 多 / 1–5D | 条件试仓 | 1价格-OI；4海外；5期权 | futures + protective Put | 20D拥挤、curve不强、IV/call skew昂贵 |
| 2 | SC2610 中国溢价回吐 | **74** | 空 / 1–3D | 条件试仓 | 1价格-OI；2curve；4海外；5期权 | short futures + protective Call | Hormuz尾部风险巨大、无physical |
| 3 | JM2701 回踩续涨 | **69** | 多 / 2–10D | 观察 | 1、2、5；但仅1/2方向确认 | futures | basis C、实体只有level、20D +21% |
| 4 | SA701 冲高回落fade | **66** | 空 / 1–5D | 观察 | 1、2 | futures | 无physical/external/exact option确认 |
| 5 | CU2610 price/curve背离 | **63** | 不追多/偏空RV | 2–10D | 1、2 | futures/curve | 无19:30 live LME可执行腿 |

**今日有70+机会，但均不是“立即建仓”。** 80分以上的确认交易：无。70–79只允许试仓/条件单。

## 七、前三名交易卡

### #1 AG2610｜76｜21:00确认后顺势多

**事实**：close 17215、settle 16818；ΔOI +14,273（+5.77%）；20D +17.71%。9/23 series ATM 16800，ATM IV 48.08%，RV20 29.71%，RR25 +7.21，BF25 +2.25；surface ready，positioning not ready，execution not ready。Reuters 18:32 BJT：spot silver约70.51美元/盎司，+1.8%。

**市场定价**：国内尾盘和海外银同向，但上行vol已经贵。  
**推断**：若21:00没有形成过度gap，且首15分钟仍能承接，趋势可能继续。  
**主观判断**：最优不是买贵Call，而是用期货拿Delta、用Put封尾。

- 最佳表达：**多1手AG2610 futures + 1手同underlying、9/23到期15–25Δ protective Put**。具体strike、bid/ask、净权利金必须夜盘实时确认；execution_ready=false时不写假报价。
- 入场：21:00后先等15分钟。若相对17215高开≤1.5%，15分钟收盘仍≥17200、不破opening low，同时海外银仍约≥70，可用0.25%–0.40% NAV最大损失试仓。
- 分批：首仓50%；突破首30分钟高点且海外继续确认再补50%。**22:00 Warsh之前不做第二次加仓。**
- 初始止损：opening low / 16980附近；若直接失守16818且不能迅速收回，放弃。
- 逻辑失效：Warsh后银价反转、DXY/实际利率上行、AG跌破opening low；或上涨伴OI明显塌陷、curve继续恶化。
- TP1：17650；TP2：18100或出现冲高+OI转负时退出。
- 时间止损：1–5D；下一完整交易日仍不能站稳17200–17300则撤。
- 最大损失：protective Put成立后理论有限；但因没有执行报价，**精确最大净支出无法确认**。
- Gap规则：若高开>1.5%–2%，至少等30–45分钟，不追第一跳。
- 合约参数：标准单位15kg/手、tick 1元/kg、tick value 15元；按settle名义≈252,270元/手。动态交易所margin、price limit本次未确认；broker margin未确认，因此不伪造1/2板压力损失。SHFE官方连续交易规则显示白银21:00–次日02:30；节假日前例外需核对当日公告。
- 交割/roll：实物交割；标准最后交易日为交割月15日（具体日历核对），普通方向仓进入交割月前按流动性滚动。

### #2 SC2610｜74｜中国溢价回吐空

**事实**：close 596.5、settle 592.3、pre-settle 573.7；settle +3.24%，ΔOI +5,976（+15.93%）；5D -0.02%；near-next -1.37% contango。9/11 options ATM 590、ATM IV45.71%，RV20 34.50%，RR25 -2.07，BF25 +1.86；surface ready、execution not ready。Reuters 17:43 BJT附近Brent约89.66美元/桶，日内近持平、周跌约5.1%。

**市场定价**：中国日盘风险溢价明显高于晚间海外即时确认。  
**推断**：若21:00后SC守不住596.5并进一步失守592.3，溢价有回吐空间。  
**主观判断**：这是fade，不是“看空原油基本面”；必须给Hormuz尾部风险买保险。

- 最佳表达：**短1手SC2610 futures + 1手同underlying 9/11到期15–25Δ OTM protective Call**。RR25为负，call wing相对put wing没那么贵，但只有实时quote后才能正式执行。
- 入场：等15–30分钟。若不能守596.5、跌破592.3后反抽不过594–595，同时Brent仍<约90.5且没有新供应中断标题，才试空。
- 分批：首仓50%；跌破588且Brent仍不跟涨再补50%。
- 初始止损：603–605或opening high上方；Brent若>约91.5且SC重新站稳600，撤。
- 逻辑失效：Brent/WTI显著上行、Hormuz恶化、SC从contango快速转为强backwardation并持续增仓。
- TP1：580–582；TP2：573–575。
- 时间止损：1–3D；下一完整交易日仍守592上方则退出。
- Gap规则：若Brent在21:00前突升>1.5%–2%或SC高开>2%，**取消fade**，不要逆第一跳。
- 合约参数（已核INE）：1000桶/手，tick 0.1元/桶，tick value 100元；按592.3名义=592,300元/手。2026-06-25起SC2610一般持仓交易所保证金16%，约94,768元/手；broker margin未确认。涨跌停±14%（特殊风控情形可再调整）。21:00–02:30夜盘。
- 压力：1个14%限制机械损失≈82,922元/手；连续两次同向14%复合≈177,453元/手。**这是压力测试，不是止损承诺，未计滑点、保证金追加和protective Call。**
- 最后交易/交割：标准规则为交割月前一月最后一个交易日；SC2610即2026年9月最后一个交易日，具体交易日历核对。实物/保税交割，若持仓延长应在9月中下旬前主动评估转SC2611。

### #3 JM2701｜69｜回踩续涨观察卡

**事实**：settle 1623，1D +1.95%、3D +2.85%、5D +3.31%、20D +21.35%；OI +7.93%；near-next +1.53% backwardation。JM options ATM IV32.32% vs RV20 20.54%，RR25 +0.11；surface+positioning ready，execution false。NBS焦煤spot 2043.1元/吨是8/20旬度最新水平；repo basis为C级且期货参考腿是8/27，不能使用。

**为什么只有69**：价格—持仓与curve是两层方向确认；Options只说明vol贵、影响表达，不给多头方向增加确认；Physical没有可验证的方向变化。按证据纪律不升70。

- 当前：**不下单。**
- 未来触发：只有先确认当前DCE交易时段安排，随后若回踩1600–1615、重新站上1629，backwardation仍在且OI不明显下降，才重新评分。
- 若升级：优先小仓JM2701期货；IV-RV过高，不优先买vol。
- 未来止损：1590下方且curve转contango；或OI快速回落。
- TP1/TP2（仅未来触发后）：1665 / 1710；时间2–10D。
- 动态保证金、涨跌停、broker margin、夜盘时段本次**未确认**，不填旧值。DCE 2026 factsheet索引显示标准单位60吨/手、tick 0.5元/吨，名义约97,380元/手；但该PDF直接抓取超时，本次只把静态标准参数作为参考，动态风险参数仍留空。
- 放弃：价格回落同时OI增加、curve转contango；或后续钢材需求/铁水/现货方向显著转弱。

## 八、商品期权专项

本次不能宣称“全市场最高/最低IV”，因为没有把全部363个surface-ready series做统一可比排序；以下只是**代表样本**：

| Series | ATM IV | RV20 | IV-RV | RR25 | BF25 | Readiness | 交易含义 |
|---|---:|---:|---:|---:|---:|---|---|
| AG2610 9/23 | 48.08% | 29.71% | **+18.37 vol** | **+7.21** | +2.25 | surface yes / positioning no / execution no | vol与upside skew都贵；不优先买Call，偏futures+Put保护 |
| SC2610 9/11 | 45.71% | 34.50% | **+11.21 vol** | **-2.07** | +1.86 | surface yes / positioning no / execution no | vol贵；bearish表达更适合short futures + Call tail cap，而非盲买Put |
| JM2701 12/16 | 32.32% | 20.54% | **+11.78 vol** | +0.11 | +1.11 | surface yes / positioning yes / execution no | skew近中性但vol贵；方向若升级，期货优于买vol |

Event convexity：今晚22:00 Warsh最直接作用于AG/AU与美元/实际利率。由于AG implied已经很高，**“有事件”不等于“买波动率有正EV”**；更合理的是控制Delta，并用有限量保护性期权封住gap尾部。

必须回避：
- 任何需要精确bid/ask、净权利金或slippage才能成立的期权结构，因为`execution_ready=false`；
- 把OI不完整的series写成crowding结论；
- dealer gamma方向推断；
- 裸卖SC/AG event vol——当前地缘/央行事件的gap分布太厚尾。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国最近EOD | 15:00–19:30海外映射 | 预期开盘 | 置信度 | 追价？ | 等多久 | 开盘后最重要确认 |
|---|---|---|---|---|---|---|---|
| AG | 17215 / 16818 | silver 18:32 +1.8% | **偏高** | 中高 | 否 | gap≤1.5%等15m；大gap等30–45m | opening low、海外银、DXY/实际利率；22:00 Warsh |
| SC | 596.5 / 592.3 | Brent 17:43近持平、周跌约5.1% | 平/相对偏弱于中国日盘强度 | 中 | 否 | 15–30m | 596.5/592.3、Brent 90.5/91.5、Hormuz标题、curve |
| JM | 1629 / 1623 | 无可执行实时海外映射 | 不判断 | 低 | 否 | **先确认交易时段**，再等30m | OI是否继续增、backwardation是否守住 |
| SA | 1047 / 1027 | 无 | 不判断 | 低 | 否 | 30–45m | OI是否继续下降、contango是否收窄 |
| EC | 1825 / 1866.5 | 不作映射 | 今晚无开盘 | 高 | n/a | **次日09:00** | INE当前交易时间页明确EC仅日盘 |

SC夜盘21:00–02:30由INE当前交易时间页确认。AG白银连续交易规则为21:00–次日02:30；节假日前是否停夜盘需核当日公告。JM/SA本次没能从最新可访问官方页面独立确认夜盘安排，因此**不猜**。

## 十、未来24h / 7d事件日历（北京时间）

- **8/28 22:00 — Fed Chair Kevin Warsh Jackson Hole remarks。** AG/AU、USD、实际利率是第一敏感组。处理：讲话前不二次加贵金属；讲话后至少等15–30分钟确认跨资产同向。[Reuters](https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/)
- **8/29 03:30 — CFTC COT常规发布时间。** 仅作positioning背景，因为报告反映此前周二持仓，不是周五实时流量。https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- **8/31 上午 — 中国官方8月制造业PMI。** Reuters调查中值49.6、前值49.2，仍指向收缩；具体官方发布时间在交易前核对NBS日程。对JM/I/J/RB/HC、CU/AL、化工与CNH敏感。[Reuters](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/)
- **8/31–9/1 — G20财长/央行相关会议，Asheville。** 对USD、利率与贵金属为二阶标题催化；不做标题第一跳。
- **9/2 22:30 — EIA Weekly Petroleum Status Report。** 对WTI/Brent/SC/FU/LU。必须联合看crude、gasoline/distillates与refinery runs，不用单一库存headline做方向。https://www.eia.gov/petroleum/supply/weekly/index.php

7日内没有本次可以可靠核实、且必须预先交易的USDA/WASDE硬节点；不要把9/11 WASDE塞进7日窗口。OPEC+如有临时/特别会议或产量政策标题，作为SC条件单的实时取消条件处理，不预设不存在的会议。

## 十一、风险预算与最终动作

- AG/SC单一**条件试仓**最大损失NAV 0.25%–0.40%；只有触发后再获新一层确认、且事件风险下降，才考虑提高到0.75%–1.00%。
- 当前没有达到“≥4 fresh独立层且无关键错误”的**确认加仓**机会。
- 同因子合并：AG/AU视作同一USD/real-yield factor；SC/FU/LU视作同一Hormuz-energy factor；JM/J/I/RB/HC视作同一China-industrial factor。
- 单一高确信主题总风险仍≤2.5%–3.0% NAV。
- 压测至少覆盖：夜盘gap、1/2个涨跌停（仅参数已确认品种）、流动性消失、margin hike、IV跳升/塌陷、相关性破裂、CNH急变与中国休市时海外大波动。

A. 今天没有应立即建立的新仓位。  
B. AG2610顺势多与SC2610溢价回吐空只应在21:00后满足确认条件时建立；前者等15分钟，后者等15–30分钟。  
C. JM2701回踩续涨、SA701冲高fade、CU2610价格/curve背离继续观察；JM仅69分，不挂静态单。  
D. 必须避免追AG/SC首跳、在execution_ready=false时虚构权利金、把C级basis当套利、把价格涨+contango解释成短缺，以及在Hormuz标题风险下裸放大SC空头。

---
归档元数据：edition=`commodities_evening`；revision=2；CI=`pending_or_unverified`。
