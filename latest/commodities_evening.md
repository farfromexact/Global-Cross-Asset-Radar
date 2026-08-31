# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-31｜Revision 4

## 一、今日一句话结论

**今天有值得冒险的条件机会：EG2610 77分、MA610 75分；均只做21:00后30—45分钟确认，不追首跳。SC2610虽日盘涨7.23%，但curve仍为contango，仅68分观察。**

当前 regime：**Hormuz supply shock / energy-to-chemicals beta expansion / curve bifurcation / China PMI less-bad / options research-ready but execution-not-ready**。

本次Revision 4是对20:25 Revision 3的实质修订：远端 China-Commodities-Engine 后续成功恢复8/31五所EOD，之前因`Device exceed limit`形成的数据质量否决已经失效。本报告生成时已过21:00，但为了保持“晚间版/夜盘前”语义，**中国价格证据冻结在8/31日盘EOD，海外评分证据冻结在19:30前；不使用21:00后中国夜盘价格倒推结论。**

## 二、数据质量与覆盖说明

本次优先读取 `data/report_input_latest.json`，并按v2协议复核 `data/last_run_status.json`、`data/radar_latest.json`；因Top候选与模块状态需要，下钻 `data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_last_run_status.json` 与 `data/options/latest.json`。

核心Futures已恢复到 **2026-08-31**：五所SHFE/INE/DCE/CZCE/GFEX均为当日source date，`data_fresh=true`、`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0、excluded exchanges=0；unknown/duplicate/invalid OHLC/negative volume或OI均为0。根状态仍有2个OHLC placeholder，异常排行继续剔除。`official_complete=false`主要来自非核心模块/元数据不完整，不覆盖核心Futures的五所fresh事实。

Contract metadata仍是partial：SHFE、INE、CZCE可用；DCE contract-info继续JSON decode error；GFEX元数据存在source-date问题。因此EG等DCE品种的动态保证金/涨跌停不拿旧值补齐，执行前必须再以交易所终端核验。

Physical请求日已推进到8/31，但20个目标仍只有4个verified mapping：铁矿港口库存（8/26周度）、焦煤主焦煤现货（8/20旬度）、浮法玻璃企业库存（8/28周度）、PTA加工费（8/28周度）。这些`fresh`只表示仍处于原生发布频率有效期，**不是8/31当日变化**。JM basis质量仍为C，不计方向证据；SC、MA、EG均无可用Physical mapping。

External请求日8/31，22个目标映射6个，5 fresh / 1 stale；其中Brent、LME铜、SGX铁矿、USDCNH、DXY属于EOD/context-only，不包装成19:30实时。19:20 BJT附近Reuters实时层显示Brent约90.97美元/桶、+3.26%，WTI约86.31、+3.49%，背景为美伊重新互袭及Hormuz航运风险；该层可作为第4层海外/宏观证据，但不是可执行进口套利。

独立Options pipeline也恢复到 **2026-08-31**：22,674个合约，64/64产品成功，source-date match 100%，IV coverage 76.06%，OI coverage 67.70%，bid/ask coverage 0。383个series中274个surface-ready、31个positioning-ready、0个execution-ready。全局surface由于IV coverage低于80%而不ready；不能把全局状态套给每个series。本次未安全提取EG/MA/SC具体series的readiness，因此**三者均不把Options计作第5层fresh证据**，也不输出ATM IV、RR25、BF25、strike、权利金或dealer-gamma方向。

### 五层证据总览

| 层 | 当前质量 | 规则 |
|---|---|---|
| 1. 价格—成交—持仓 | 高 | 五所8/31 fresh；ΔOI未从本次安全读取结果中完整提取，不做“新多/新空”归因 |
| 2. Curve—高质量basis—仓单 | 中高 | curve可用；basis多数缺失；FU近月结构受交割扭曲，不计普通curve确认 |
| 3. 实体供需 | 低 | 4/20 mapping；MA/EG/SC无方向性Physical |
| 4. 海外/宏观 | 高（方向映射） | Reuters油价+Hormuz、NBS PMI；不称跨市场套利 |
| 5. 商品期权 | 研究中等/执行低 | T日链完整，但全局surface partial，0 execution-ready；候选series本次不计分 |

## 三、商品仪表盘

| 板块 | 品种/合约 | 8/31 close / settle | 1D vs pre-settle | Volume / OI | Curve | Physical / Options | 信号 |
|---|---|---:|---:|---:|---|---|---|
| 能源 | **SC2610** | 635.1 / 632.2 | **+7.23%** | 189,512 / 42,699 | **约-2.05% contango** | Physical缺；T日期权不计候选series层 | 强price、弱curve，观察不追 |
| 能化 | **EG2610** | 5331 / 5172 | **+5.98%** | 1,072,606 / 405,205 | **约+5.33% backwardation** | Physical缺；Options不计 | **price+curve+海外共振** |
| 能化 | **MA610** | 2983 / 2912 | **+6.01%** | 1,540,188 / 987,929 | **约+3.88% backwardation** | Physical缺；Options不计 | **price+curve+海外共振** |
| 燃料 | FU2611 | 3845 / 3771 | +4.77% | 1,159,968 / 192,370 | 表面约+46%，**近月/交割扭曲，剔除** | Physical缺 | 不用curve加分 |
| 黑色 | **JM2701** | 1696 / 1666.5 | **+6.53%** | 1,544,767 / 611,796 | **约-0.17% contango** | 8/20旬度spot 2043.1；basis C | price强、curve不确认 |
| 有色 | **CU2610** | 106970 / 107060 | **-2.06%** | 236,875 / 246,422 | **约-0.75% contango** | 无Physical；LME EOD仅context | PMI改善下仍弱，观察空头相对强弱 |
| 有色 | NI2610 | — | 约-2.24% | 当前合约状态fresh | 未形成可计分curve | LME_NI无映射 | 弱，但证据不足 |
| 贵金属 | AG2612 | — | 约+1.7% | 当前合约状态fresh | 未形成正式curve确认 | 海外金弱银强；Options候选series未核 | 双向，不追 |
| 建材 | FG701 | — | 当日fresh | — | 结构不进入Top | 8/28周度企业库存7404.9重量箱 | 周度level不是今日确认 |
| 新能源 | LC2701 | — | 当日fresh | — | 结构未进入Top | Physical缺 | 不把上涨/波动包装成短缺 |
| 航运 | EC2610 | 1791.5 / 1817.8 | **-1.63%** | 97,696 / 144,883 | deferred premium大，季节/合约效应强 | 无闭环 | 无夜盘；次日9:00再看 |

Market State中存在1/3/5/20D历史层，但本次connector对超大文件未稳定暴露全部Top候选的同合约历史字段；因此表格只报告已安全读取的8/31值，不用连续主力或旧合约拼接伪造5D。

## 四、相比上一交易日真正变化

1. **数据闸门翻转。** 20:25时五所曾因iFinD device-limit失败；20:37后重新采集成功，8/31五所Futures source-date全部匹配，full-market-ready恢复。Revision 3的“No-Trade because data failure”因此不再成立。
2. **能源冲击已经真实进入中国EOD。** SC2610日盘close/pre-settle +7.23%，MA610 +6.01%，EG2610 +5.98%，FU2611 +4.77%。这不是仅靠海外映射猜测的gap，而是中国日盘已经发生的大幅重定价。
3. **curve发生明显分化。** EG约+5.33%、MA约+3.88% backwardation，说明两者的近端定价同步强化；SC反而仍约2.05% contango，所以“原油涨得最多”并不等于“原油是最优追多表达”。
4. **JM是典型反例。** 焦煤日盘约+6.53%，但curve由上周的backwardation转为轻微contango；PMI改善与price大涨没有得到期限结构确认，不能直接解释成现货短缺或补库。
5. **宏观是less-bad，不是全面工业牛市。** NBS 8月制造业PMI 49.8，生产50.4、新订单50.6；总指数仍低于50。与此同时CU2610跌约2.06%且contango，说明工业品内部仍高度分化。
6. **期权研究层恢复，但执行层没有恢复。** T日64/64产品链完整，但全局IV/OI覆盖不足且bid/ask=0；因此今晚最优表达仍以期货条件单为主，不用虚构期权成本。

## 五、产业链地图

| 产业链 | 当前方向 | price | curve | 实体 | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| **原油—进口化工—EG/MA** | **偏多但极度延伸** | 强 | **EG/MA强确认；SC不确认** | 缺 | **Hormuz强确认** | MA/EG实体与候选series期权 | 中高 |
| 原油本体 | 偏多但不追 | **SC极强** | **contango** | 缺 | Brent/WTI强 | curve/Physical | 中 |
| 双焦—钢材 | beta冲高 | JM强 | **JM不确认** | 旬度context | PMI略正 | 铁水/补库/A-B basis | 中低 |
| 有色—中国增长 | 偏弱分化 | CU弱 | contango | 缺 | LME EOD仅context | 19:30实时LME exact mapping | 中低 |
| 贵金属 | 双向 | AG偏强 | 未确认 | — | 金银/利率冲突 | candidate surface | 低中 |

最强产业链不是“原油本身”，而是**能源冲击向EG/MA近端结构传导**；最弱的交易方式是追所有涨停/大涨品种做同一个Hormuz beta。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 逻辑/赔率/催化/结构/技术 | Fresh层 | 阶段 |
|---|---|---:|---|---|---|
| 1 | **EG2610 回撤承接多** | **77** | 21 / 18 / 18 / 14 / 6 | **1、2、4** | 条件试仓 |
| 2 | **MA610 回撤承接多** | **75** | 20 / 18 / 18 / 13 / 6 | **1、2、4** | 条件试仓 |
| 3 | SC2610 supply-shock continuation | **68** | 20 / 16 / 18 / 7 / 7 | 1、4；curve逆风 | 观察 |
| 4 | JM2701 PMI后趋势延续 | **66** | 18 / 15 / 13 / 9 / 11 | 1、4；curve不确认 | 观察 |
| 5 | CU2610 弱势/curve背离空头观察 | **64** | 17 / 16 / 10 / 11 / 10 | 1、2 | 观察 |

**今天值得新增的是条件风险，不是立即风险。** EG/MA达到3层fresh证据，因此可以合法超过70；但两者日盘已经接近+6%，赔率惩罚与拥挤惩罚明显，不允许追21:00第一跳。

## 七、前三名交易卡

### #1 EG2610｜77｜回撤承接多

**事实**：close 5331、settle 5172、pre-settle 5030，日盘close/pre约+5.98%；volume约107.3万手、OI约40.5万手；near-next约+5.33% backwardation。海外19:20附近Brent/WTI上涨约3%+，Hormuz供应与航运风险升高。

**市场定价**：日盘已经计入明显供应冲击，但EG的backwardation说明近端结构比SC更愿意为短期紧张付费。

**市场可能错在哪里**：中东headline缓和、航运恢复、油价回吐；或者EG上涨只是高beta跟随而非真实进口/现货收紧。

**推断**：如果21:00后的第一轮获利回吐不能破坏5172—5200区域，且重新接受5280以上，趋势延续的赔率仍优于追SC。

**主观判断**：EG是今晚最佳“能源冲击二阶表达”，但不是开盘市价单。

- 最佳表达：EG2610 futures；期权仅研究，不给报价。
- 入场A：21:00后等30—45分钟，回撤至5200—5250区域得到承接并重新站上5280。
- 入场B：若不回撤，等待首30—45分钟高点被二次突破；若相对5331高开>约2%，放弃追价。
- 分批：50%触发仓；确认后再50%。
- 初始止损：5140附近或首45分钟结构低点二者更严格者。
- 逻辑失效：Brent快速回落、Hormuz出现可信缓和；EG curve明显由backwardation收窄至平/contango。
- TP1：5450；TP2：5600；时间止损1—5D。
- 最大损失：试仓NAV 0.25%—0.50%；确认后总风险不超过0.75%。
- multiplier：10吨/手；tick：1元/吨；tick value：10元；按close notional约 **53,310元/手**。
- night session：21:00—23:00（固定合约背景）；LTD：交割月份倒数第4个交易日。
- 当前动态exchange margin / price limit：**未确认**；DCE contract metadata本次失败，broker margin亦未确认。标准合约旧基准不得替代当前风控参数。
- 1/2涨跌停压力损失：**当前动态limit未确认，禁止伪算**。
- delivery/roll：不承担交割；最迟在交割月前显著降仓，避免最后交易日前流动性与限仓风险。

### #2 MA610｜75｜回撤承接多

**事实**：close 2983、settle 2912、pre-settle 2814，close/pre约+6.01%；volume约154万手、OI约98.8万手；near-next约+3.88% backwardation。Hormuz风险对中东能源/化工物流和成本端构成方向性映射，但本报告不把它称为可执行进口套利。

**市场定价**：MA不仅price强，近端结构也同步变强；比单纯“油涨带化工”多一层curve确认。

**市场可能错在哪里**：国内甲醇煤制属性较强，油价冲击并不等于国内成本曲线一比一上移；伊朗/中东物流若未实质中断，风险溢价可能快速回落。

**推断**：若2912附近的结算区域不被夜盘持续跌破，日盘结构更像有carry-through，而非一次性headline spike。

- 最佳表达：MA610 futures；期权只作研究观察。
- 入场：等30—45分钟；2925—2960回撤承接后重回2960以上，或首45分钟高点二次突破。若高开到3040以上，不追。
- 分批：50% + 50%。
- 初始止损：2880附近或首45分钟结构低点。
- 失效：跌破2912且不能收回；backwardation显著收窄；油价/地缘headline反转。
- TP1：3060；TP2：3160；时间止损1—5D。
- 最大损失：NAV 0.25%—0.50%，确认后≤0.75%。
- multiplier：10吨/手；tick：1元/吨；tick value：10元；notional约 **29,830元/手**。
- night session：21:00—23:00；LTD：交割月份第10个交易日；实物交割。
- 标准合约基准为5%最低保证金、±4%基础涨跌停，但**今天+6%日盘本身表明动态风控参数不能用基础值代替**；当前exchange/broker margin和实际price limit未确认。
- 1/2板压力：当前动态limit未确认，不输出伪精确金额。
- roll：不进交割月，优先在9月下旬前评估移仓。

### #3 SC2610｜68｜只观察，不进入条件单

**事实**：close 635.1、settle 632.2、pre-settle 592.3，close/pre约+7.23%；volume 189,512、OI 42,699；但near-next约 **-2.05% contango**。海外Brent/WTI同向上涨约3%+。

**为什么只有68**：第1层和第4层支持多头，但第2层没有确认；Physical缺、candidate options layer未安全确认。按两层fresh证据上限必须≤69。

**升级条件**：夜盘至少观察45分钟，632附近得到接受；SC curve contango明显收窄；Brent维持90美元附近或以上且没有可信缓和headline。满足后才重新打分。

**观察型触发区**：重新站稳640以上才考虑升级；620以下视为shock明显回吐。若未来升级，可参考TP1 655、TP2 675，试仓风险0.25%—0.50% NAV。

合约固定参数：1000桶/手；tick 0.1元/桶，tick value 100元；按close notional约 **635,100元/手**；夜盘21:00—02:30；LTD为交割月份前一月最后一个交易日，SC2610原则上为2026-09-30，交易所调整优先。INE 6月23日公告对SC2610规定涨跌停14%、一般持仓保证金16%、套保持仓15%；按settle 632.2静态计算，一板14%约 **88,508元/手**，连续两板复合约 **189,407元/手**。broker margin未确认。

## 八、商品期权专项

T日Options已经恢复，但不能把“链完整”写成“执行ready”：22,674 contracts、64/64 products、IV coverage 76.06%、OI coverage 67.70%、bid/ask coverage 0；383 series中274 surface-ready、31 positioning-ready、0 execution-ready。

因此本期：

- 不声称“全市场最高/最低IV”；
- 不输出EG/MA/SC ATM IV、RR25、BF25，因为具体候选series readiness未安全核实；
- 不输出PCR/OI crowding作为完整结论；
- 不给Call Spread/Put Spread的strike、premium、滑点；
- dealer gamma direction保持unknown。

后续研究优先级：**EG/MA事件后IV-RV是否过度抬升、SC供给shock skew、AG/AU利率—地缘双向vol**。

固定免责声明：**research only; manual quote and manual confirmation required before execution; no premium quoted.**

## 九、21:00夜盘开盘风险地图

本Revision 4在数据真正ready后完成时间已晚于21:00；为了不产生事后偏差，以下仍按“8/31中国EOD + 19:30前海外”形成，不引用21:00后中国价格。

| 品种 | 夜盘资格 | 夜盘前映射 | 预期 | 追首跳？ | 等待 | 最重要确认 |
|---|---|---|---|---|---|---|
| **EG** | 21:00—23:00 | 油价/地缘偏多 + backwardation | 偏高开风险 | **否** | 30—45m | 5172/5200承接、curve是否维持 |
| **MA** | 21:00—23:00 | 地缘/化工物流偏多 + backwardation | 偏高开风险 | **否** | 30—45m | 2912承接、curve、油价 |
| **SC** | 21:00—02:30 | Brent/WTI偏强 | 高开风险高 | **否** | 45m | 632接受度、contango是否收窄、Hormuz |
| JM | 夜盘安排执行前以DCE终端确认 | PMI略正但curve不确认 | 不预测 | 否 | 30—45m | 1666/1696、curve |
| CU | 有夜盘 | 中国日盘弱、美元/利率偏鹰 | 双向 | 否 | 30m | LME/CNH实时与106970附近接受度 |
| EC | **无夜盘** | — | — | — | — | 下一窗口9月1日09:00 |

## 十、未来24h / 7d事件

- **9月1日04:00 BJT｜USDA Crop Progress**：农产品只在报告变化与CBOT价格同步时升级Physical层。
- **9月1日22:00 BJT｜美国JOLTS**：美元/前端利率→金银、有色；不在数据前裸放大Vega。
- **9月2日22:30 BJT｜EIA WPSR**：SC/FU/LU同时看crude、gasoline、distillate、refinery runs、imports/exports。
- **9月3日20:30 BJT｜美国Q2 Productivity and Costs修订**：主要看rates传导。
- **9月4日20:30 BJT｜美国8月Employment Situation**：贵金属与美元高vol窗口；优先有限风险表达。
- **9月6日｜OPEC+七国会议**：必须区分Hormuz战争shock与OPEC供给政策。

## 十一、风险预算与最终判断

今天**值得新增条件风险**，但只能集中在EG/MA；二者共同暴露于同一个“Middle East energy/chemical supply”因子，不能各自按独立主题满配。建议EG+MA合计初始最大损失不超过 **NAV 0.75%—1.0%**；任一单腿0.25%—0.50%。SC若后续升级，与EG/MA合并后整个能源/Hormuz主题总风险仍≤2.5%，在目前延伸行情下更建议≤1.5%—2.0%。

压力测试重点：地缘headline突然缓和；夜盘gap后流动性消失；交易所提高保证金；EG/MA curve由backwardation快速转平；SC一个/两个14%涨跌停；多品种同因子相关性在压力时趋近1。

归档说明：本Revision 4已按direct-to-main模式准备更新同一历史路径与latest/status；由于`manifests/reports.json`为超大单行JSON，而当前GitHub connector写接口只支持完整文件替换，本次无法在不冒险破坏历史manifest的前提下安全重建整文件。因此manifest保留Revision 3条目，归档状态记为`partial`，不虚构`success`；聊天报告不受影响。

### 来源

- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- 国家统计局，2026年8月PMI：https://www.stats.gov.cn/sj/zxfbhjd/202608/t20260831_1965154.html
- Reuters，8月31日油价与美伊/Hormuz：https://www.reuters.com/business/energy/oil-jumps-more-than-2-after-us-attack-irans-larak-island-2026-08-30/
- INE原油交易时间：https://www.ine.cn/services/calenderandholidays/tradinghours/
- INE原油风险参数公告：https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html
- CZCE甲醇业务细则/合约：https://www.czce.com.cn/cn/uploadfile/2024/02/07/20240207154824122.pdf

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：EG2610回撤承接多（77）与MA610回撤承接多（75），均须21:00后等待30—45分钟并满足价格/curve确认。
C. 今天应继续观察的机会：SC2610供应冲击延续（68）、JM2701趋势延续（66）、CU2610弱势/curve背离（64）。
D. 今天必须避免或退出的交易：追EG/MA/SC首跳、把JM暴涨解释成现货短缺、使用FU畸形近月curve加分、把0 execution-ready的期权结构包装成可成交交易。