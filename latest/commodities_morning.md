---
report_date: 2026-09-01
edition: commodities_morning
revision: 2
generated_at_bjt: 2026-09-01T07:30:24+08:00
commodity_trade_date: 2026-08-31
commodity_data_fresh: true
commodity_history_record_count: 0
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-01

> **数据截点：** 中国基线为2026-08-31完整EOD；8月31日晚中国夜盘只使用公开可验证行情并与EOD分开；海外层使用截至北京时间约07:30可验证的8月31美欧收盘与今晨事件。**Revision 2仅修正审计字段：module-specific `data/physical/latest.json` 的 `requested_date` 实际为2026-08-31，不是09-01；交易排序与触发条件不变。** China-Commodities-Engine核心五所EOD健康，但`report_input_latest.json`与`market_state_latest.json`仍为空，`options/surface_latest.json`也为空，因此不伪造3D/5D/20D、RV20、z-score或商品期权surface指标。

## 一、今日一句话结论

**今天有两项值得冒险的条件机会：EG2610与MA610回撤承接多；SC2610降级为次选。昨日能化大涨已高度计价地缘冲击，9:00后不追高，等待30—60分钟。**

## 二、数据质量与覆盖说明

第一读取层已读取`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。`report_input_latest.json`当前为空，因此按v2协议下钻。最近完整中国EOD为2026-08-31：SHFE、INE、DCE、CZCE、GFEX五所共803个期货合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，unknown/duplicate/invalid OHLC/negative volume-OI均为0；placeholder=2，不进入异常排行。

统一Market State产物仍为空。因此当前可靠使用的是2026-08-31具体合约1D、Volume、OI和near-next期货曲线；3D/5D/20D、RV20、volume/OI z-score、ΔOI z-score与完整price/OI quadrant均不可用。为了比较最近两个完整交易日，仅对上一期报告中同一具体合约做close/OI点对点比较，并明确只叫归因线索。near-next curve只是期货期限结构，不等于现货基差；当前没有A/B级闭环basis进入方向评分。

**Physical module-specific文件的`requested_date=2026-08-31`，generated_at=2026-08-31T20:51:05+08:00；20个目标仍仅4个映射，I/JM/FG/TA按原生频率fresh，周度/旬度fresh不等于今晨发布。** 对Top候选EG/MA，仓库没有独立Physical映射，因此使用8月31日有明确日期和口径的产业资料补充并折扣计分。

独立Options pipeline trade_date=2026-08-31：22,674个合约、383个series、64/64产品，但IV coverage仅76.06%、OI coverage67.70%、bid/ask coverage=0；`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`、dealer gamma direction unknown，且`surface_latest.json`为空。因此本期不输出ATM IV、RR25、BF25、PCR、Dealer Gamma、具体strike、净权利金或滑点。

Contract metadata仍partial：DCE contract-info采集失败，EG动态保证金/限幅无法由仓库确认；MA静态合约规则可核验，但当前动态风控参数必须另行确认；SC2610使用INE当前可核验动态参数。

## 三、商品市场仪表盘

| 板块 | 合约 | 8/31 EOD close/settle | 1D | Volume | OI | near-next curve | 夜盘/海外 | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 能化 | **EG2610** | **5331 / 5194** | **+5.98%** | 1,072,606 | 342,882 | **Back +5.33%** | 夜盘公开口径涨近3%，为结算参考 | **77：回撤承接多** |
| 能化 | **MA610** | **2983 / 2911** | **+6.01%** | 1,540,188 | 712,865 | **Back +3.88%** | 夜盘主力涨超3%，为结算参考 | **76：回撤承接多** |
| 原油 | **SC2610** | **635.1 / 618.3** | **+7.23%** | 189,512 | 42,699 | **Contango -2.05%** | 夜盘637.2；Brent 90.49、WTI 85.76 | **71：深回撤承接多** |
| 塑化 | **V2701** | **4791 / 4696** | **+6.00%** | 1,718,450 | 1,109,193 | Contango -1.00% | 夜盘涨超3% | squeeze，不追 |
| 塑化 | **PP2701** | **8366 / 8210** | **+5.44%** | 923,568 | 599,187 | Back +3.05% | — | 69：强势观察 |
| 双焦 | **JM2701** | **1729 / 1696** | **+6.53%** | 1,544,767 | 636,470 | **微Contango -0.17%** | 夜盘焦煤/焦炭跌超1% | 63：日盘强、curve/夜盘不确认 |
| 纯碱 | **SA701** | **1061 / 1055** | **+3.31%** | 1,870,144 | 1,172,774 | Contango -4.22% | — | squeeze/curve冲突 |
| 玻璃 | **FG701** | **941 / 940** | **+2.51%** | 2,081,063 | 1,394,560 | Contango -3.07% | — | 价格强、OI下降线索；不追 |
| PTA | **TA701** | **5836 / 5748** | **+4.29%** | 1,152,329 | 940,161 | Back +1.53% | — | 成本/curve偏多 |
| 贵金属 | **AU2610** | **961.92 / 978.24** | **-3.20%** | 604,495 | 179,157 | Back +0.46% | 夜盘-1.88%；海外黄金继续承压 | 不低位追空 |
| 贵金属 | **AG2610** | **16293 / 16669** | **-3.12%** | 1,214,308 | 239,957 | Back +0.10% | 夜盘-2.74% | 68：失败反弹空观察 |
| 新能源 | **LC2701** | **161000 / 160500** | **+3.21%** | 166,812 | 403,032 | Contango -0.47% | — | 高波动，不追涨 |

FU2611的radar near-next约46% Back属于明显异常，继续从curve交易中剔除。

## 四、相比上一交易日真正变化

**1. 最强机会从SC转向EG/MA。** SC2610日盘已从596.5大涨到635.1，同一合约close-to-close约+6.47%，OI约-1.80%；夜盘637.2只比日盘close再高约0.33%。这只能叫价涨仓减归因线索，不能断言空头回补。Brent/WTI最终收90.49/85.76、分别涨约2.7%/2.8%，方向确认但追涨赔率下降。

**2. EG出现目前最干净的Price + Curve + Physical组合。** EG2610日盘+5.98%，near-next Back约5.33%。8月31华东主港库存14.2万吨，较上周四下降3.6万吨，9月进口预计仍偏低；反方是国内周产量35.76万吨、环比+4.5%，产能利用率55.19%、环比+2.37个百分点。因此这是“低港库/进口约束 vs 国内增产”的紧平衡，不是无条件短缺。

**3. MA也补齐三层，但Physical更混合。** MA610日盘+6.01%、Back约3.88%。产业资料显示伊朗7套甲醇装置停车、合计约1090万吨/年，8月到港卸货较上月缩减约40%，8月底至9月中旬进口船货约24万吨；但国内产量可能回升且MTO需求偏弱。因此只给76，不给80+。

**4. JM的日盘大涨没有得到curve与夜盘确认。** JM2701 close 1729、较8月28 close约+6.14%，OI约+6.51%，只能称价涨仓增线索；near-next已转约0.17%微Contango，夜盘焦煤/焦炭跌超1%。官方制造业PMI虽升至49.8但仍低于50，今天09:45还需看RatingDog制造业PMI后的价格弹性。

**5. V/FG更像高beta squeeze而不是已确认短缺。** 两者价格上涨但同合约OI较上一EOD下降、curve仍Contango，因此不把上涨解释成短缺，也不追。

**6. 贵金属继续弱，但地缘与利率相互拉扯。** Reuters称周一现货黄金约跌0.4%，美债10Y处在约4.7%上方，偏鹰利率路径压制贵金属；美伊冲突又提供避险反向力量。AU/AG只等失败反弹，不追低。

## 五、产业链地图

| 产业链 | 当前方向 | Price/Curve | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| **乙二醇—聚酯** | **偏多** | EG强 + 深Back | 港口库存14.2万吨、周降3.6；进口受限，但国内增产 | 聚酯终端订单与A/B basis | **中高** |
| **甲醇—MTO** | **偏多但高事件风险** | MA强 + Back | 伊朗装置停车/到港低；国内产量恢复、需求偏弱 | 精确船期、MTO复产 | 中高 |
| **原油—成品油** | 右尾仍高、但已计价较多 | SC强但Contango | Brent/WTI同步涨；霍尔木兹仍受扰 | actual flow、exact parity | 中 |
| **双焦—钢材** | 日盘强、夜盘降温 | JM大涨但curve近中性 | 官方PMI仍<50 | 铁水、利润、补库 | 中低 |
| **贵金属—美元—利率** | 偏空但不追 | 中国金银弱 | 偏鹰利率与地缘避险冲突 | 当前surface、实时资金 | 中 |
| **纯碱—玻璃—PVC** | squeeze / 不确认短缺 | SA/FG/V仍Contango | Physical覆盖不足 | A/B basis、库存/检修闭环 | 中低 |

当前regime：**美伊冲突驱动的中国能化高beta行情进入第二阶段，alpha从“买原油headline”转向受进口/库存真正约束且curve已确认的EG/MA；高实际利率压制贵金属，中国需求数据仍不支持全面工业多头。**

## 六、机会排行榜

| 排名 | 机会 | 总分 | 方向 | 持有期 | 阶段 | Fresh层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| **1** | **EG2610 回撤承接多** | **77** | Long | 1–3D | conditional_trial | **3** | OI下降线索；国内供应回升；DCE动态风控参数缺失 |
| **2** | **MA610 回撤承接多** | **76** | Long | 1–3D | conditional_trial | **3** | 需求偏弱、国内产量或回升；夜盘百分比为结算参考 |
| **3** | **SC2610 深回撤承接多** | **71** | Long | Intraday–2D | conditional_trial | **3** | EOD已+7.23%；夜盘相对日盘仅小幅续涨；Contango |
| 4 | **Long MA / Short V RV观察** | **69** | RV | 2–5D | watch_only | 2 | V Physical缺失；无beta/vol历史 |
| 5 | **AG2610 失败反弹空** | **68** | Short | Intraday–2D | watch_only | 2 | 已先跌；地缘避险反向；surface不可用 |

没有80+确认交易；前三项都必须等开盘后触发。

## 七、前三名交易卡

### 1. EG2610｜回撤承接多｜77

- **事实：** 5331/5194，1D +5.98%，Volume 1,072,606，OI 342,882，near-next Back +5.33%。
- **Physical：** 华东主港库存14.2万吨、周降3.6万吨；9月进口仍偏受限；国内周产量+4.5%、利用率+2.37pct是反方。
- **市场可能错在哪里：** 资金可能把能化全当原油beta；EG更关键的是低港库和进口约束，深Back显示近端紧张。
- **最佳表达：** EG2610期货条件试仓；期权只有surface/报价恢复后研究Call Spread。
- **入场：** 等30–45分钟。5270–5320回撤守住并重新站上5330/VWAP时先1/3；若开盘>5400，等60分钟，不追。
- **分批：** 首45分钟高点突破且Back仍>4%再加1/3；最后1/3只在实体紧张继续验证时考虑。
- **初始止损：** 30分钟接受在5190以下。
- **逻辑失效：** 稳定跌破5100，同时Back压到2%以内并出现进口/港库正常化。
- **TP1/TP2：** 5450 / 5650；2个交易日不延续则时间止损。
- **最大损失：** 0.35%–0.50% NAV。
- **合约参数：** 静态10吨/手，tick 1元/吨，tick value 10元/手，按5331名义约53,310元/手；实物交割。DCE本期动态保证金、限幅与部分metadata未确认，必须下单前重查；不把标准参数冒充今日参数。

### 2. MA610｜回撤承接多｜76

- **事实：** 2983/2911，1D +6.01%，Volume 1,540,188，OI 712,865，Back +3.88%；夜盘主力涨超3%为结算参考口径。
- **Physical：** 伊朗7套装置停车约1090万吨/年；8月到港卸货约环比-40%，8月底至9月中旬进口船货约24万吨；国内产量回升和MTO弱是反方。
- **入场：** 等45分钟。2920–2960承接并重新站2980/VWAP，先1/3；直接>3050不追。
- **分批：** 突破首45分钟高点且Back>3%再加；第三档只在船期/伊朗装置继续恶化时。
- **初始止损：** 30分钟接受在2890以下。
- **逻辑失效：** 跌破2840并维持、Back<1%，同时伊朗装置/进口到港正常化。
- **TP1/TP2：** 3070 / 3200；2–3日时间止损。
- **最大损失：** 0.35%–0.50% NAV。
- **合约参数：** 10吨/手，tick 1元/吨，tick value 10元/手，按2983名义29,830元/手；最后交易日交割月第10个交易日、实物交割。当前动态保证金/限幅未确认，必须下单前核验。

### 3. SC2610｜深回撤承接多｜71

- **事实：** 635.1/618.3，1D +7.23%，Volume 189,512，OI 42,699，near-next Contango -2.05%；夜盘收637.2，相对日盘close仅约+0.33%。Brent/WTI收90.49/85.76。
- **市场可能错在哪里：** 风险仍可能升级，但SC已计入大量headline，赔率来自深回撤而非突破追多。
- **入场：** 等45–60分钟；625–632承接并重站635/VWAP才1/3。直接>645不追。
- **初始止损：** 30分钟接受在618以下。
- **逻辑失效：** 跌破610，同时Brent回到88.5以下或出现可信快速降级/通航恢复。
- **TP1/TP2：** 650 / 675；1–2日时间止损。
- **最大损失：** 0.25%–0.35% NAV。
- **合约参数：** 1000桶/手，tick 0.1元/桶，tick value 100元/手，按637.2名义637,200元/手；夜盘21:00–02:30、实物交割。当前动态涨跌停/保证金按INE最新公告与终端核验，券商保证金未确认。

## 八、商品期权专项

**raw chain完整度提高，但surface/positioning/execution仍不ready。** 22,674个合约、383个series、64/64产品；IV coverage 76.06%、OI coverage 67.70%、bid/ask 0。不能称任何品种“全市场IV最高/最低”，也不输出可信IV-RV、RR25/BF25、具体strike、权利金或slippage。

盘中若surface与人工可执行quotes恢复，研究优先级：**EG Call Spread > MA Call Spread > SC Call Spread**。执行固定约束：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、9:00开盘风险地图

| 品种 | 主要风险 | 等待 | 关键确认 |
|---|---|---:|---|
| **EG2610** | 昨日涨停附近+夜盘再强 | **30–45m；>5400等60m** | 5270–5320承接、Back>4%、进口/港库无改善 |
| **MA610** | 地缘双向headline强 | **45m；>3050不追** | 2920–2960承接、Back>3%、船期/伊朗装置 |
| **SC2610** | 已高度price-in | **45–60m** | 625–632承接、Brent不破、635/VWAP |
| JM2701 | 日盘+6.5%但夜盘转弱、curve转微Contango | **至少等09:45 PMI** | PMI后能否守1700附近及curve是否收紧 |
| AU/AG | 偏鹰利率与地缘避险冲突 | **45m** | 10Y、美元、海外金银 |
| V/FG/SA | squeeze与Contango冲突 | **45m** | OI、curve、Physical是否跟上 |

## 十、未来24小时 / 7日事件

- **09:45 北京时间：** 中国8月RatingDog制造业PMI；工业品重点看数据后的价格弹性。
- **21:45 / 22:00：** 美国S&P Global制造业PMI终值 / ISM制造业PMI；高油价背景下重点看ISM Prices。
- **9月2日22:30：** EIA Weekly Petroleum Status Report。
- **9月4日20:30：** 美国8月就业报告。
- **持续：** 霍尔木兹船流、油轮安全事件、美伊互袭、伊朗MA/EG装置与中国进口船期。任何快速降级都可能令EG/MA/SC高beta多头出现大gap反转。

## 十一、风险预算

即时新增风险仍为0；只有触发后建立。EG与MA共享“霍尔木兹/进口中断”因子，二者合计初始风险≤0.70% NAV；SC与EG/MA三者同因子总风险≤0.85% NAV。单一EG或MA试仓0.35%–0.50%，SC 0.25%–0.35%。没有第四个独立fresh层，不升级确认仓。

Long MA / Short V的notional近似中性可参考4手MA对5手V，但不是beta-neutral：V Physical缺失、跨交易所保证金/限幅不同、相关性可能失效，因此只作RV观察。

## 关键来源

- [China-Commodities-Engine](https://github.com/farfromexact/China-Commodities-Engine)
- [Reuters：China factory activity improves but remains contractionary](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-improves-stays-contraction-august-2026-08-31/)
- [Reuters：Gold slips to near two-week low on Fed rate hike bets](https://www.reuters.com/world/india/gold-hits-near-two-week-low-fed-chiefs-hawkish-stance-2026-08-31/)
- [新浪财经：乙二醇华东主港库存14.2万吨](https://finance.sina.com.cn/money/future/fmnews/2026-08-31/doc-iniqexup7847472.shtml)
- [光大期货/新浪财经：美伊战火重燃，甲醇涨停](https://finance.sina.com.cn/money/future/2026-08-31/doc-iniqetnx9076819.shtml)
- [财联社：8月31日晚中国商品夜盘](https://www.cls.cn/subject/1501)
- [INE：原油期货标准合约](https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html)
- [EIA：Weekly Petroleum Status Report Schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：EG2610回撤承接多、MA610回撤承接多、SC2610深回撤承接多；都必须等开盘后触发。**  
**C. 今天应继续观察的机会：Long MA/Short V RV、AG2610失败反弹空、PP2701强势延续、09:45 PMI后的JM再定价。**  
**D. 今天必须避免或退出的交易：开盘追EG/MA/SC高开、把夜盘涨幅误当日盘close后的增量、追低空AU/AG、机械追V/FG/SA squeeze，以及任何基于空surface/零bid-ask的精确商品期权交易。**