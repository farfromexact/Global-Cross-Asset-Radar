# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-28

## 一、今日一句话结论

**今日商品期货期权无合格交易。** 19:30当日五所EOD流水线仍在运行，昨天RM/CF/M等高分信号全部降为观察；今晚最值得等的是Warsh后的贵金属反应，以及RM/M/CF能否在21:00后重新获得T日价仓与curve确认。

这不是“今天市场没有波动”，而是**当前可验证证据不足以承担新增风险**。上一完整中国交易日（2026-08-27）的农产品方向仍有逻辑，海外能源和贵金属今晚也有事件，但在2026-08-28中国Futures/Market State未完成、Options仍为T-1的情况下，任何70+交易评分都会违反五层证据上限。

## 二、数据质量与覆盖说明

本次按China-Commodities-Engine v2执行。第一读取层实际读取了`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`，并按模块异常继续读取`data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`、`data/radar_history.json`以及`data/scoped/ex-dce/last_run_status.json`。

**核心结论：19:30时2026-08-28完整中国EOD尚未形成。** `report_input_latest.json`为空；`data/latest.json`、`market_state_latest.json`和`radar_history.json`也为空。根目录`last_run_status.json`虽然requested/run date是2026-08-28，但它生成于04:30左右，五所期货模块均报`iFinD history response missing columns: time`，source-date match=0%、critical module errors=15、full_market_ready=false。与此同时，GitHub Actions显示当日`Split EOD China Commodities Data`于19:23 BJT启动、19:30仍为`in_progress`。因此本报告**不能把04:30错误解释成全天最终失败，也不能把2026-08-27冒充为2026-08-28日盘EOD**。

最近一个可验证完整五所价格层是**2026-08-27**：五所均覆盖、source-date match=100%、full_market_ready=true、critical errors=0。这些数据在本报告只作为T-1背景和上一交易日比较基准，不计入2026-08-28 fresh price/OI/curve证据。

Physical模块已经有2026-08-28独立更新：20个目标中4个映射在各自原生频率下fresh，包括铁矿港口库存（observation 8/26，周度，15904，仓库原单位“吨”）、焦煤NBS现货（observation 8/20，旬度，2043.1元/吨，basis quality C）、浮法玻璃企业库存（observation 8/28，周度，7404.9重量箱）和PTA周度加工费（observation 8/28，677.532元/吨）。这些都是**最新周度/旬度水平**；由于当前文件没有可靠的方向变化/历史分位，默认只做Physical context，不自动计入完整方向性证据层。

External仓库层requested date仍为2026-08-27，6个已验证映射中5条fresh、1条stale；Brent、LME铜、SGX铁矿、USDCNH、DXY均是EOD context，不冒充19:30实时。15:00—19:30增量使用独立公开实时/准实时来源补充。

Options是**T-1（2026-08-27）**：22,348条记录、64/64品种范围，IV coverage约98.33%，OI coverage约67.87%，但bid/ask coverage=0；全局`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`，dealer gamma direction unknown。`surface_latest.json`当前为空。因此今晚不输出ATM IV、RR25/BF25、IV-RV、PCR、Gamma方向、具体strike、净权利金、bid/ask或滑点。

Contract Metadata同样停在2026-08-27且多数为`official_partial`，multiplier/tick/margin/price-limit/night-session等动态执行参数并非全品种完整。本报告没有70+正式交易，因此不以旧参数补齐“交易卡”。

Scope fallback仅有`data/scoped/ex-dce`，其run date为2026-08-18且排除DCE，明显过旧，**拒绝使用**。如果误用，该scope会丢失铁矿、焦煤、焦炭、豆粕、豆油、棕榈油、生猪、玉米、聚烯烃等关键DCE品种，破坏黑色、油脂、养殖和塑化链判断。

## 三、商品仪表盘（8—15个重点品种）

> 表中中国价格全部明确标注为最近可验证的2026-08-27 EOD；它们不是2026-08-28当前价格。无法从当前可读汇总恢复的字段直接写“缺失”，不做推算。

| 板块 | 品种/主力 | 最新有效价 | 1D / 5D | Volume / OI / ΔOI | Curve | Basis / Physical | Options | 当前信号 |
|---|---|---|---|---|---|---|---|---|
| 油粕/饲料 | RM611 | 8/27 close 2348 / settle 2335 | +2.32% / +2.55% | 888,871 / 672,634 / +0.20% | Back ~3.08% | basis无；天气context | T-1 chain only | 昨日多头逻辑保留，但**今天只观察** |
| 软商品 | CF701 | 17030 / 17020 | +0.65% / 约0% | 264,840 / 563,478 / +4.21% | Contango ~1.63% | 新疆天气风险；无当前高质basis | T-1 chain only | 天气观察，不是当前交易 |
| 豆粕 | M2701 | 3355 / 3324 | +1.78% / +1.84% | 1,893,769 / 2,786,805 / +3.88% | Contango ~1.17% | 进口/压榨未闭环 | T-1 chain only | 观察；不要与RM叠加风险 |
| 纯碱 | SA701 | 1011 / 1016 | -2.21% / -1.65% | 1,674,745 / 1,208,732 / +10.66% | Contango ~3.23% | 当前Physical缺失 | T-1 chain only | 昨日空头结构不能机械滚动 |
| 乙二醇 | EG2610 | 5028 / 5077 | -3.24% / 缺失 | 1,333,883 / 347,889 / -7.49% | Back ~4.22% | 港库/进口/聚酯负荷缺 | T-1 chain only | price/curve冲突，**不追空** |
| 玻璃 | FG701 | 909 / 906 | +0.11% / -1.09% | 1,570,837 / 1,605,428 / -2.42% | Contango ~2.02% | 8/28周度企业库存7404.9重量箱，仅level context | T-1 chain only | 等库存变化，不交易 |
| 焦煤 | JM2701 | 当前可读聚合未恢复精确价 | radar T-1 close return +1.93% / 缺失 | 1,040,547 / 553,648 / 缺失 | T-1 Back | NBS旬度现货2043.1元/吨，basis C | T-1 chain only | context only |
| 工业硅 | SI2611 | 当前可读聚合未恢复精确价 | radar T-1 +0.34% / 缺失 | 145,679 / 316,410 / 缺失 | T-1 Contango | SI Physical mapping unavailable | T-1 chain only | 无交易 |
| 白银 | AG2610 | 8/27 close 16728 / settle 16690 | +0.12% / +3.60% | 672,442 / OI当前字段缺 / ΔOI -3.50% | 近端大致平 | 当前Physical缺 | T-1 chain only | 22:00 Warsh事件观察 |
| 燃料油 | FU2611 | 3675 / 3687 | +0.33% / -2.20% | 1,036,758 / 245,737 / -6.00% | 近端Back ~27.39%，交割窗污染 | 当前产品库存/裂解缺 | T-1 chain only | Hormuz双侧，**不追首跳** |

因此“今天最强/最弱产业链”无法用T日中国数据正式排名。**上一完整EOD最强是油粕/饲料与棉花天气交易，最弱更偏EG/SA；今天是否延续尚未验证。**

## 四、相比上一交易日真正变化

**1. 最大变化不是价格，而是可交易性下降。** 昨日晚间RM611、CF701、M2701分别是78/76/74分条件机会；今天第一层price-volume-OI和第二层current curve都未完成，按五层证据规则不能继续保持70+。逻辑没有被证伪，但交易资格被撤销。

**2. 当日Physical有增量，但仍不足以“救回”方向评分。** FG企业库存与TA周度加工费的observation date已到8/28；I是8/26周度，JM是8/20旬度。没有变化率、分位或阈值意义时，它们只能说明产业状态，而不能证明今日价格方向。

**3. 原油从“单边地缘多”转成更明显的双侧博弈。** Reuters在17:43 BJT附近给出的Brent约89.66美元/桶、WTI约83.21美元/桶；Brent本周约跌5.1%、WTI约跌4.5%。与此同时Hormuz周四只有7艘商品船通过，低于10日均值15。价格风险溢价回吐与物理物流尾部仍存同时发生，SC/FU更容易首跳后反向。

**4. 贵金属进入真正的事件窗。** 18:32 BJT附近现货黄金约+0.1%、白银约+1.8%，但Fed主席Kevin Warsh的Jackson Hole讲话安排在22:00 BJT。当前最重要的信息不是18:30前的涨幅，而是讲话后美元/美债实际利率与金银是否同向确认。

**5. 中国作物天气催化没有消失。** 8/27 Reuters继续报道东北、华北玉米/大豆高温洪涝风险和新疆棉花高温干旱风险。它仍然给RM/M/CF一个正向prior，但天气新闻不是今天的price/OI/curve确认。

**6. 19:23启动的EOD流水线本身是一个数据流程事件。** 这意味着今晚不能重复昨天“太早把当日取数判死”的错误；但v2也明确要求19:30不持续轮询等Options，因此本版直接以当前可验证模块出报告，宁可No-Trade，也不延误21:00风险准备。

## 五、产业链地图

| 链条 | 方向 | Price / Curve | 库存/仓单/实体 | 海外/宏观 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 油粕/饲料+棉花 | 催化偏多、执行未确认 | 8/27 RM强+Back；M/CF强但Contango | 天气风险fresh；品种Physical未闭环 | 无可执行CBOT/ICE parity | **8/28价仓与curve** | 低—中 |
| 原油—燃料油 | **双侧** | Brent日内近横盘、周线明显回落；中国current curve缺 | Hormuz物流仍受阻；产品库存缺 | 地缘尾部仍大 | SC/FU当日结算、裂解、产品库存 | 中（regime）/低（方向） |
| 贵金属 | **事件波动** | 海外白银强于黄金；中国T日价缺 | 非主导 | 22:00 Warsh、美元/利率 | T日中国价+可执行surface | 中（事件）/低（方向） |
| 纯碱—玻璃 | 上一日偏弱、今天未知 | T-1 SA/FG Contango | FG周度库存有level、无方向历史 | 海外映射弱 | T日价仓+库存变化 | 低 |
| MEG/聚酯/新能源 | 证据不足 | EG T-1 price弱但Back；SI T-1 Contango | TA加工费level；SI映射缺 | 不完整 | T日price/curve+需求/库存 | 低 |

当前regime最准确的描述是：**data-degraded + event-risk + no-trade**。price是否获curve确认、库存是否确认、境内外是否同向，今天都无法对中国T日完成闭环。人民币/美元作用今晚主要通过22:00后美元与实际利率映射贵金属，以及CNH对进口商品的二阶影响；不应在缺少当前中国结算时硬算“内外套利”。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

本期没有任何候选满足≥60分的可列榜标准：当前T日中国price/OI/curve缺失，能获得的fresh独立层最多是事件/Physical/海外中的零散一两层，严格受≤59/≤69证据上限约束。为避免“给分即暗示可交易”，本期`top_opportunities`留空。

最接近触发的3个观察项：

1. **RM611 / M2701天气延续多。** 尚缺：8/28当前价、OI变化、curve，以及进口/压榨或更直接实体确认。为什么不交易：昨天强势不等于今天fresh证据；RM与M还是高度相关同因子。
2. **CF701天气凸性多。** 尚缺：8/28当前价/OI、curve不能继续走弱、仓单/高质量basis或更明确减产量级。为什么不交易：新疆天气是催化，不是执行确认。
3. **AG/AU Warsh后事件交易。** 尚缺：22:00后DXY/美债收益率/金银反应、当前中国价格接受度、若用期权则还缺T日surface和bid/ask。为什么不交易：事件尚未发生，且Options为T-1、execution not ready。

## 七、前三名交易卡

**本期没有正式交易卡。** 原因不是缺少想法，而是没有任何机会达到70分。以下只保留“观察卡”，不得按静态价格直接下单，也不补造multiplier、tick、margin、price-limit、last trading day或night-session参数。

### 观察卡1｜RM611 / M2701｜条件多

**事实：** 8/27 RM和M价格都强，但这是T-1；8/28 China EOD当前不可用。  
**市场定价：** 今天是否继续交易天气风险未知。  
**推断：** 如果21:00后30—45分钟价格持续站在当前session VWAP/Opening Range上方、OI同步增加且curve不恶化，天气逻辑才重新获得第一、二层确认。  
**主观判断：** RM/M只选一条腿，不能因为两个都强就重复下注同一个feed/crop factor。  
**入场：** 现在无入场；等待实时确认。  
**止损/失效：** 必须用当晚真实Opening Range和current curve定义；不能机械沿用8/27止损。  
**退出：** 45分钟未确认则放弃；没有T日数据不设TP1/TP2。  
**未来风险预算：** 若确认，试仓最大损失NAV 0.25%—0.40%。

### 观察卡2｜CF701｜条件多

**事实：** 新疆天气直接映射棉花，但8/27仍有Contango。  
**市场定价：** 8/28日盘是否已提前计价未知。  
**推断：** 21:00后需要价格接受+OI增加+curve不继续走弱三者一起出现。  
**主观判断：** 这比“天气利多所以直接买”严格得多，也更符合当前信息边界。  
**入场：** 现在无入场；30—45分钟后再评估。  
**失效：** 天气影响被证伪，或价格失败同时Contango扩大。  
**退出：** 第一小时无确认则跳过。  
**未来风险预算：** 0.25%—0.35% NAV。

### 观察卡3｜AG2610 / AU｜Warsh后事件

**事实：** 18:32 BJT海外白银+1.8%、黄金+0.1%；Warsh 22:00 BJT讲话。  
**市场定价：** 事件前金属偏强，但中国8/28 settle未知。  
**推断：** 讲话后美元/实际利率与金银价格同向，才有信息价值。  
**主观判断：** 事件后15—30分钟的第二次接受，比事件前猜方向更有edge。  
**入场：** 22:00前没有新仓；22:15—22:30后再看。  
**失效：** USD/real yields与金属方向冲突、第一次冲击无法维持。  
**退出：** 两向whipsaw持续30分钟则放弃。  
**未来风险预算：** 0.25%—0.35% NAV。若改用Options，必须先确认T日surface、bid/ask和最大净支出。

## 八、商品期权专项

本期不能做“全市场最高/最低IV”排名，也不能做ATM IV-RV、RR25/BF25、term structure、PCR、Gamma或crowding结论。原因很清楚：Options仅有2026-08-27 T-1 chain，`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`，bid/ask coverage=0，dealer gamma direction unknown。

当前唯一可说的是**事件凸性需求存在，但可执行性不存在**：Warsh讲话对AU/AG是明显波动率事件；作物天气对CF/M/RM是路径依赖事件。然而在没有T日surface和报价的情况下，Call Spread、Put Spread、Calendar、Butterfly等结构都只能是研究方向，不能给具体strike、净权利金、成交成本或希腊值。

必须回避：1）Warsh前裸卖金银波动率；2）把T-1 vendor IV当成今晚ATM IV；3）用缺失OI覆盖形成PCR/crowding结论；4）任何dealer gamma方向推断。

## 九、21:00夜盘开盘风险地图

> 这里是“风险映射”，不是对中国期货已经发生的价格描述。由于8/28日盘settle缺失，本期不能定量计算真实gap。

| 品种 | 最近中国参考 | 15:00—19:30海外/事件映射 | 预期 | 置信度 | 追价？ | 等多久 | 开盘后最重要确认 |
|---|---|---|---|---|---|---|---|
| AG | AG2610 8/27 settle 16690（T-1） | 18:32 BJT银+1.8%、金+0.1%；22:00 Warsh | 若日盘未充分计价则有高开风险，**不可量化** | 低—中 | **不追** | 30—45分钟；更优是22:15后 | COMEX银/金、DXY、美债收益率、当前OI/接受度 |
| CF | CF701 8/27 settle 17020 | 新疆天气偏多，但无当前ICE棉实时映射 | 小幅偏高风险，仅是prior | 低 | 不追 | 30分钟 | 当前价/OI、curve、首小时高低 |
| RM/M | RM611 2335 / M2701 3324（8/27） | 天气催化；无可验证15:00—19:30 CBOT/菜籽精确parity | **方向无法确认** | 低 | 不追 | 30—45分钟 | price/OI/curve；只选一腿 |
| SC/FU | FU2611 8/27 settle 3687；SC当日参考缺 | Brent约89.66，周跌5.1%；Hormuz流量低于10日均值 | 平/混合映射，双侧gap tail | 低—中 | 不追 | 30分钟 | Brent/WTI、Hormuz headlines、SC/FU OI、裂解/产品相对强弱 |
| SA/FG | 8/27 SA 1016 / FG 906 | 无强海外映射 | 无法确认 | 低 | 不追 | 15—30分钟 | 当前价仓+curve；FG再加库存方向 |

Night-session字段在当前contract metadata中不完整。本报告不猜具体结束时点。AG/能源等连续交易品种有夜盘历史/交易所制度基础，但**当晚具体品种结束时间仍以交易所/终端为准**；未能确认夜盘的品种不得假设21:00可交易。若实际无夜盘，由于8/29—8/30为周末，下一可交易窗口应是**2026-08-31 09:00 BJT**。

## 十、未来24h / 7d事件

| 北京时间 | 事件 | 主要资产 | 处理 |
|---|---|---|---|
| **8/28 22:00** | Fed主席Kevin Warsh Jackson Hole讲话 | AU/AG、USD、rates、广义商品 | 事件前不新增方向；讲话后等15—30分钟 |
| **8/29 03:30** | CFTC COT计划发布 | 油、贵金属、谷物、棉花 | 作为下周仓位背景；注意数据是前一周二持仓，不是实时flow |
| **8/31 09:30** | 中国官方8月制造业PMI | 黑色、有色、工业品、CNH | 大幅surprise后先等15—30分钟；避免工业beta叠加 |
| **9/1 时间待确认** | RatingDog中国制造业PMI | 工业品/CNH | 与官方PMI交叉验证；不编造具体时点 |
| **9/2 22:30** | EIA Weekly Petroleum Status Report | WTI/Brent、SC/FU/LU、裂解 | 看原油+成品油+开工率组合，不用单一库存标题交易 |
| **7日外：9/6** | OPEC+七国月度审视 | 原油 | 已宣布9月从此前自愿减产中调整+188kb/d；会议不在严格7日窗口 |
| **7日外：9/11** | USDA WASDE / Crop Production | 豆、玉米、棉花 | 当前天气逻辑的重要下一批硬数据 |

## 十一、风险预算与最终行动

今晚的最优风险预算是**0新增风险**。若21:00/22:00后数据重新闭环，单一试仓最大损失NAV 0.25%—0.40%，低于常规0.25%—0.75%区间上沿；没有≥3 fresh layers不升级确认仓。RM/M/CF按同一crop-weather/feed因子合并，AG/AU按USD-real-yield因子合并，SC/FU/LU按Hormuz-energy因子合并。任何后续试仓都要压力测试1/2个涨跌停、周末gap、流动性消失、保证金上调、IV跳升/塌陷、CNH急变和相关性破裂。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：原则上不挂静态价单；仅保留RM/M、CF与Warsh后AG/AU的实时确认条件，触发后仍需人工核对当前价、OI、curve与保证金参数。  
C. 今天应继续观察的机会：RM/M天气延续、CF天气凸性、AG/AU 22:00后事件反应、SC/FU Hormuz双侧尾部。  
D. 今天必须避免或退出的交易：把8/27阈值机械滚到8/28、追21:00首跳、用T-1 options做精确IV/strike/权利金交易、同时叠加RM+M+CF同因子满仓。

---

## Sources

- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- Reuters, Oil holds steady, on track for weekly fall on US-Iran talks stalemate (2026-08-28): https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/
- Reuters, Shipping traffic via Strait of Hormuz slips below 10-day average (2026-08-28): https://www.reuters.com/business/energy/shipping-traffic-via-strait-hormuz-slips-below-10-day-average-data-shows-2026-08-28/
- Reuters, Gold inches up ahead of Fed Chair Warsh's Jackson Hole remarks (2026-08-28): https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/
- Reuters, Heat, floods threaten China crops as U.S. farm purchases loom (2026-08-27): https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/
- Reuters, China's factory activity seen contracting again in August (2026-08-28): https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/
- NBS 2026 release calendar: https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html
- CFTC COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- EIA Weekly Petroleum Status Report: https://www.eia.gov/petroleum/supply/weekly/index.php
- OPEC+ 2 August 2026 press release: https://www.opec.org/pr-detail/611-2-august-2026.html
