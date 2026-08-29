# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-29

> 周末模式：今天是周六，中国商品期货/期权休市，国际主要期货市场也已进入周末休市。中国数据使用最近完整交易日 **2026-08-28 EOD**；不得把周末新闻写成已发生的中国价格变化。  
> 数据协议：`china_commodities_v2`。最新中国可交易窗口为 **2026-08-31 09:00**；今天 **没有中国21:00夜盘**。

## 一、今日一句话结论

**今日商品期货期权无合格交易。周五AG多头逻辑被Warsh后金银急跌破坏；SC空头相对价值仍在，但Hormuz周末尾部风险上升，必须等周一开盘确认。**

当前regime是 **hawkish-rates repricing + weekend geopolitical gap risk + China EOD/overseas close divergence**。今天最大的edge不是押方向，而是撤销已经失效的周五预案、保留周末凸性，并把周一09:30中国PMI纳入开盘交易规则。

## 二、数据质量与覆盖说明

本次通过已连接GitHub读取 `farfromexact/China-Commodities-Engine`。第一读取层实际访问：
- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`

统一汇总层当前仍对应最近完整中国交易日2026-08-28；随后按模块状态钻取：
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`

`report_input_latest.json`沿用8月28日汇总，requested_date=`2026-08-28`，generated_at=`2026-08-28T19:41:26.332469+08:00`。根状态显示核心Futures于19:23:52生成；五所SHFE/INE/DCE/CZCE/GFEX全覆盖，共803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、unknown/duplicate/invalid OHLC/negative volume or OI均为0；5个OHLC placeholder不进入异常排行。DCE contract metadata仍有JSON decode error，GFEX metadata存在partial/stale标记，因此动态合约参数继续按“未确认”处理，不拿旧参数补洞。

Physical仍为部分覆盖：20个目标中4条完成映射，主要是铁矿港口库存、焦煤旬度现货、玻璃周度企业库存、PTA周度加工费。这里的fresh只表示仍处于各自原生发布频率的有效期，不代表8月29日新发布；JM basis为C级，不进入方向评分、不称套利。External仓库层仍是完成交易日EOD背景，不把周末新闻或周五美盘收盘混同于中国EOD。

独立Options pipeline最近完整交易日为2026-08-28：21,806条合约、370个series，IV coverage 98.59%、OI coverage 68.16%、bid/ask coverage 0；上一完整surface统计为363个surface-ready、74个positioning-ready、0个execution-ready。全市场质量对象本身仍标记positioning/execution不完整，所以本报告只使用已验证series的ATM IV/RR25/BF25作为**周五结构背景**。今天没有新的中国期权交易日，故这些数据不能作为“8月29日新鲜方向确认”。Dealer gamma方向仍未知。

数据质量结论：**最近完整中国交易日数据质量足够做周一风险地图，但周末没有新的价格—成交—持仓、curve或期权执行证据，因此任何新增方向仓位都不应达到70分。**

## 三、商品仪表盘（最近完整中国交易日：2026-08-28）

| 板块 | 品种/合约 | 最新有效价 close / settle | 1D / 5D / 20D | Volume / OI / ΔOI | Curve | Basis / Physical | Options背景 | 周末信号 |
|---|---|---:|---|---|---|---|---|---|
| 贵金属 | **AG2610** | 17215 / 16818 | settle +0.77%；5D +1.25%；20D +17.71% | 765,356 / 261,945 / +5.77% | -0.14%，近乎平坦contango | 无完整实体层 | ATM IV48.08 vs RV20 29.71；RR25 +7.21；execution false | **昨日多头预案取消；周一反转空观察** |
| 能源 | **SC2610** | 596.5 / 592.3 | settle +3.24%；5D -0.02% | ΔOI +15.93% | **-1.37% contango** | 无fresh实体闭环 | ATM IV45.71 vs RV20 34.50；RR25 -2.07 | 相对溢价fade仍有逻辑，但周末Hormuz尾部更大 |
| 黑色 | **JM2701** | 1629 / 1623 | +1.95%；5D +3.31%；20D +21.35% | 1,039,129 / 597,545 / +7.93% | **+1.53% backwardation** | 焦煤现货为8/20旬度水平；basis C | ATM IV32.32 vs RV20 20.54 | 趋势最好，实体未闭环 |
| 有色 | CU2610 | 108620 / 108660 | +0.15%；5D +3.01%；20D +8.29% | 154,411 / 198,417 / +1.65% | -0.64% contango | 无A/B basis | 未形成新确认 | 周一09:30 PMI前不追 |
| 建材 | FG701 | 927 / 918 | +1.32%；5D未单独钻取 | 1,513,705 / 1,504,372 / 未钻取 | -2.67% contango | 最新周度企业库存7404.9重量箱，仅level | 未用于方向评分 | 涨价未获curve/physical确认 |
| 化工 | TA701 | 5630 / 5596 | +1.23%；5D未单独钻取 | 746,791 / 868,133 / 未钻取 | +1.57% backwardation | PTA加工费677.532元/吨，周度level | 未用于方向评分 | 结构偏强但实体方向缺 |
| 新能源 | LC2701 | 159600 / 156000 | +2.40%；3D +1.33% | 239,379 / 391,884 / 未钻取 | -1.15% contango | Physical unavailable | T日surface背景；execution false | 价格涨+contango，不能写短缺 |
| 油脂饲料 | M2701 | 3340 / 3344 | +0.60%；5D未单独钻取 | ≈165.7万 / ≈274.5万 / 未钻取 | -0.96% contango | 无进口/压榨闭环 | ATM IV15.34；RR25 +4.26 | 无周末触发 |
| 软商品 | CF701 | 17180 / 17200 | +1.06%；5D +0.76%；20D +6.01% | 464,467 / 604,731 / +7.32% | -1.64% contango | Physical unavailable | ATM IV13.15；RR25 +1.84 | 价仓强但curve不认 |
| 建材化工 | SA701 | 1047 / 1027 | settle +1.08%；5D -0.39% | 1,902,641 / 1,154,367 / -4.50% | -3.41% contango | 无完整实体层 | series surface-ready背景；execution false | 冲高fade观察，不能追涨 |
| 航运 | EC2610 | 1825 / 1866.5 | close -1.83%；settle +0.40% | 未钻取 | +27.53%，明显季节/合约结构 | 无可执行跨市场basis | 无执行层 | INE仅日盘；周一09:00再交易 |

所有1D/5D/20D均为**同一具体合约**口径；价涨仓增/价涨仓减只作为归因线索，不解释为确定的新多、新空、空头回补或多头止损。

## 四、相比上一交易日真正变化

1. **AG是最大的逻辑翻转。** 8月28日中国日盘结束时AG仍是76分条件多；随后Warsh讲话触发美元和短端收益率上行，Reuters报道周五现货黄金跌逾3%至约4,567.23美元/盎司、白银跌3.5%至66.81美元/盎司。中国周五收盘没有交易到这段冲击，因此昨日AG顺势多预案必须取消，而不是机械延续到周一。
2. **贵金属的拥挤度使反转更值得尊重。** CFTC 8月25日COMEX futures-only数据显示，黄金非商业多头277,159手，较前周增加20,257手，占总OI 64.8%；白银非商业多头37,871手、空头12,610手。这里不是“机构必然卖出”的结论，只说明Warsh冲击发生前多头风险暴露已经不低。
3. **SC的相对价值逻辑仍在，但周末尾部风险更高。** Brent周五结算89.31美元/桶，日跌0.43%、周跌逾5%；WTI 83.40美元/桶，周跌逾4%，与中国SC周五+3.24%的幅度仍显著不同步。但Reuters周六报道伊朗海军宣称对Hormuz拥有“full control”，且此前船流仍明显低于正常水平；因此不能把周五油价下跌线性外推成周一必跌。
4. **周末本身构成数据闸门。** 8月29日没有新的中国Futures/Market State/Options数据；五层证据中的1、2、5只能沿用周五最近完整状态，不能包装成今日fresh confirmation。
5. **周一09:30 PMI改变工业品开盘策略。** 国家统计局日程确认8月PMI于8月31日09:30发布，距离09:00日盘开盘仅30分钟。CU、JM、I/J/RB/HC、FG/SA、LC/SI等工业品若首30分钟先走一段，09:30可能直接重置方向，因此不应在09:00首跳追单。

## 五、产业链地图

| 产业链 | 当前方向 | 价格/curve | 实体/仓单 | 海外/宏观 | 期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| 贵金属 | **由多转中性偏空观察** | AG周五价格强、curve弱确认 | 无完整实体层 | Warsh后金银急跌；美元/利率偏鹰 | IV与upside skew偏贵 | 周一亚洲盘是否继续跌、Iran避险对冲 | 中 |
| 原油/炼化 | **中国溢价fade观察** | SC周五+3.24%，仍contango | 无fresh实体闭环 | Brent周跌>5%，但Hormuz周末风险上升 | IV-RV仍正 | 周日全球重开后的第一价格 | 中 |
| 焦煤—钢材 | 偏多观察 | JM多周期上涨+backwardation | basis C；实体只是旬度level | PMI将重置中国增长预期 | IV贵 | 铁水/补库/库存方向 | 中 |
| 有色/新能源 | 不追多 | CU/LC价格强但contango | 覆盖弱 | PMI+美元均是逆风测试 | 无新确认 | 09:30后price/curve/OI共振 | 中低 |
| 纯碱—玻璃 | 偏fade观察 | SA/FG均contango | FG仅周度库存level | 海外映射弱 | execution false | 库存方向+A/B basis | 中低 |

**最强的“可观察结构”是JM趋势；最弱的“可追价逻辑”是价格上涨但curve仍contango的工业/新能源品种。** 当前不是广谱shortage regime。

## 六、机会排行榜

**今日商品期货期权无合格交易。保留现金和观察仓。**

| 排名 | 机会 | 分数 | 逻辑/赔率/催化/结构/技术 | 方向 | 持有期 | 阶段 | 最新独立证据层 | 数据/时点惩罚 |
|---|---|---:|---|---|---|---|---|---|
| 1 | **SC2610 周一溢价回吐观察** | **68** | 20/17/13/10/8 | 条件空 | 1–3D | 观察，未激活 | 1、2、4 | Hormuz周末headline可令Brent gap-up；无周末中国确认 |
| 2 | **AG2610 周一反转空观察** | **67** | 19/16/16/7/9 | 条件空 | 1–5D | 观察，未激活 | 1、4、5 | 中国尚未交易Warsh后跌幅；Iran避险可能抵消 |
| 3 | **JM2701 回踩续涨** | **66** | 19/15/9/11/12 | 条件多 | 2–10D | 观察 | 1、2 | Physical没有方向闭环；basis C；PMI临近 |
| 4 | CU2610 PMI后price/curve重评 | 63 | 17/14/13/8/11 | 双向观察 | 1–5D | 观察 | 1、2 | 美元与PMI双事件；curve不确认 |
| 5 | SA701 冲高fade | 61 | 16/15/8/9/13 | 条件空 | 1–5D | 观察 | 1、2 | 无实体确认；不应只凭contango做空 |

没有任何机会达到70分。风险偏好再高，也不应把“周末无法成交、且第一价格尚未出现”的研究观点当成可执行edge。

## 七、前三名交易卡（均为非活动研究卡）

### 1. SC2610｜68｜周一条件空，周末不挂单

**事实**：8/28 close/settle 596.5/592.3；settle +3.24%；5D -0.02%；ΔOI +15.93%；near-next curve -1.37% contango；周五Brent结算89.31、周跌逾5%，WTI 83.40、周跌逾4%。  
**市场定价**：中国SC周五保留更高地缘溢价；海外收盘在押注Hormuz流量改善/潜在协议与鹰派利率压力。  
**市场可能错在哪里**：周六伊朗“full control”表态及低船流意味着海外周五收盘可能低估周末供应尾部，周一油价可能先gap-up。  
**推断**：只有全球原油重开后仍弱、且SC周一不能维持592.3–596.5区域，国内溢价回吐才重新可交易。  
**主观判断**：仍偏向fade，但不值得跨周末承受不连续风险。

**新鲜/可用证据层**：1价格-OI、2curve、4海外/宏观；没有周末可执行确认。  
**最佳表达**：若触发，`short SC2610 futures + protective Call`；期权`execution_ready=false`，不写strike、bid/ask、净权利金。固定执行条件：**research only; manual quote and manual confirmation required before execution; no premium quoted**。  
**入场**：周一先看全球油价重开；中国09:00后至少等30分钟。若SC跌破592.3，反抽594–596失败，且Brent没有因Hormuz冲击显著高开，再进入0.25%–0.40% NAV最大损失试仓。  
**分批**：50%触发仓；09:30 PMI后若SC仍弱、curve未转backwardation，再加50%。  
**初始止损/逻辑失效**：SC重新站稳603–605；或Brent显著gap-up并维持、Hormuz出现新的实质供应中断。  
**TP1 / TP2**：580–582 / 573–575；**时间止损**1–3D。  
**最坏情景**：周末军事升级导致原油跳空、涨停、保护性Call流动性恶化、保证金上调。  
**放弃条件**：全球原油重开即出现供给冲击；或SC直接低开>2%后迅速修复，不追空首跳。

**合约参数**：multiplier 1,000 barrels；tick 0.1元/桶；tick value 100元；按592.3结算notional约592,300元/手。8/28官方规则背景下exchange margin约16%、price limit ±14%，broker margin未确认；INE标准交易日夜盘21:00–02:30，但**今天周六无夜盘**。last trading day/本次动态交割参数未再次确认，普通方向仓不持入交割月。单个±14%静态limit冲击约82,922元/手；两个连续同向+14%复合冲击约177,453元/手。

### 2. AG2610｜67｜昨日多头取消，周一反转空观察

**事实**：8/28中国close/settle 17215/16818，ΔOI +5.77%，20D +17.71%；AG期权ATM IV48.08 vs RV20 29.71、RR25 +7.21。中国收盘后，现货黄金周五跌逾3%、白银跌3.5%至66.81美元/盎司。  
**市场定价**：周五中国市场仍交易贵金属动量；美盘随后将利率路径重新向更鹰派方向定价。  
**市场可能错在哪里**：周末Iran/Hormuz风险可重新抬升避险需求，令周一金银反弹；所以“周五美盘跌”不等于“周一必空”。  
**推断**：中国周一若在16818下方开出并30–45分钟无法收复，且国际银仍弱、美元/实际利率维持强势，才算真正的regime flip。  
**主观判断**：最重要的动作不是立刻反手空，而是**撤销昨日顺势多**。

**证据层**：1周五中国、4Warsh后海外、5周五vol结构；但跨时段冲突，不能给70。  
**最佳表达**：若触发，AG2610空期货 + protective Call，或有限风险Put Spread；当前execution false，不给权利金。固定执行条件：**research only; manual quote and manual confirmation required before execution; no premium quoted**。  
**入场**：周一09:00不追gap；至少等09:30 PMI与首30–45分钟。若价格持续低于16818、反抽失败，再小仓参与。  
**分批**：50%确认仓；跌破首45分钟低点且国际银未反弹，再补50%。  
**止损/失效**：重新有效站上16818并持续，或国际银快速收复Warsh后跌幅的一半以上。  
**TP1 / TP2**：16550附近 / 16200附近，仅作为结构化退出区，不是静态挂单；时间止损1–5D。  
**最大损失**：试仓0.25%–0.40% NAV；有保护性Call时才严格有限。  
**1–20D催化**：PMI、美元/实际利率、美国就业数据、Iran/Hormuz避险。  
**最坏情景**：周末避险跳空上行，空头开盘即不利；因此禁止跨周末裸空。  
**放弃条件**：国际银周一亚洲时段强力反包；或中国AG低开后30分钟内收回16818并形成持续接受。

**合约参数**：multiplier 15kg；tick 1元/kg；tick value 15元；按16818结算notional约252,270元/手。动态exchange/broker margin、当前price limit、last trading day本次未重新确认；标准连续交易背景为交易日21:00–02:30，今天周六无夜盘。交割风险通过提前roll/退出规避。

### 3. JM2701｜66｜趋势多观察，必须跨过PMI

**事实**：8/28 close/settle 1629/1623；1/3/5/20D均为正，5D +3.31%、20D +21.35%；ΔOI +7.93%；curve +1.53% backwardation。最新实体侧只提供旬度spot level，basis C不计分。  
**市场定价**：价格、OI、期限结构是国内最整齐的趋势组合之一。  
**市场可能错在哪里**：20D涨幅与持仓扩张已经不低，而实体确认薄弱；PMI若弱于预期，黑色链可能先发生拥挤去杠杆。  
**推断**：真正的edge是“PMI后仍能守住backwardation与价格”，不是09:00抢跑。  
**主观判断**：今天只有两层明确方向证据，严格压在69以下。

**证据层**：1价格-OI、2curve；Physical不计、C级basis不计、期权只提供vol背景。  
**最佳表达**：周一PMI后若触发再用JM2701期货；不提前挂静态单。  
**入场**：09:30 PMI后至少等15分钟；1600–1615回踩被吸收并重新站上1629，且curve维持backwardation，再考虑0.25%–0.40% NAV试仓。  
**分批**：50%重回1629；突破首小时高点且OI/curve不恶化再补。  
**止损/失效**：1590以下并伴随curve明显收窄或转contango；OI快速塌陷。  
**TP1 / TP2**：1665 / 1710；时间止损2–10D。  
**最坏情景**：PMI弱、钢材需求预期下修、黑色多腿同步平仓、涨跌停不同步。  
**放弃条件**：开盘直接gap-up>2%或PMI后backwardation明显消失。

**合约参数**：标准multiplier 60t、tick 0.5元/吨、tick value 30元，按1623约97,380元/手。因DCE metadata当前仍有抓取错误，dynamic margin、price limit、last trading day及最新夜盘字段本次不补猜；确认前不升级正式交易。

## 八、商品期权专项

今天没有新的中国期权交易日，所以只把8/28 surface作为**最近完整交易日波动率背景**，不称8/29 fresh signal。代表样本：

| Series | ATM IV | RV20 | IV-RV | RR25 | Readiness | 周末解释 |
|---|---:|---:|---:|---:|---|---|
| AG2610 | 48.08% | 29.71% | +18.37 vol | +7.21 | surface yes / execution no | 上行skew与vol原本都贵；Warsh后方向翻转，不宜直接追买put |
| SC2610 | 45.71% | 34.50% | +11.21 vol | -2.07 | surface yes / execution no | 地缘尾部仍贵；更适合期货+保护腿而非裸买昂贵波动 |
| JM2701 | 32.32% | 20.54% | +11.78 vol | +0.11 | surface+positioning ready / execution no | skew近中性，但vol不便宜 |

不声称这是“全市场最高/最低IV”。`execution_ready=0`、bid/ask coverage=0，因此所有Call Spread、Put Spread、Calendar、Butterfly、Diagonal、期货+保护性期权都只是研究结构；**research only; manual quote and manual confirmation required before execution; no premium quoted**。Dealer gamma方向未知，禁止推断。

跨期限/跨品种vol RV今天也不正式建立：没有周一第一笔价格和实时quote，任何“卖贵买便宜”都缺执行闭环。

## 九、21:00夜盘开盘风险地图（周末模式）

**今天是周六，没有中国21:00夜盘。** 上期所规则明确连续交易为每周一至周五；INE也明确SC夜盘21:00–02:30、EC仅日盘。下一中国可交易窗口统一看 **周一2026-08-31 09:00**。SC等有夜盘品种的下一次夜盘，则是周一日盘之后的21:00，不是今天。

| 品种 | 周五中国EOD | 周末/周五美盘映射 | 周一09:00倾向 | 追首跳？ | 等待 | 开盘后最重要确认 |
|---|---|---|---|---|---|---|
| AG | 17215 / 16818 | 金银Warsh后急跌；Iran避险反向支撑 | **偏低开但不确定** | 否 | 30–45m，跨过09:30 PMI | 16818接受/收复、国际银、DXY/实际利率 |
| SC | 596.5 / 592.3 | Brent周跌>5%，但Hormuz周末风险抬升 | **双向gap风险** | 否 | 30–45m | Brent重开、Hormuz新闻、592.3/596.5、curve |
| JM | 1629 / 1623 | 无高质量海外直接腿 | 不预判 | 否 | 至少45m | PMI、1623/1629、OI、backwardation |
| CU | 108620 / 108660 | Warsh后美元偏强；PMI近在09:30 | 偏谨慎 | 否 | 45m | LME/CNH、PMI、curve |
| SA/FG | 1047/1027；927/918 | 海外映射弱 | 不预判 | 否 | 45m | OI、contango、库存方向 |
| EC | 1825 / 1866.5 | 无周末中国交易 | 不预判 | 否 | 周一日盘 | INE仅日盘，09:00开盘 |

这里的“偏低开/双向gap”是**风险地图，不是中国市场已经发生的价格变化**。

## 十、未来24h / 7d事件

- **8月31日09:30 BJT｜中国8月官方PMI**：国家统计局2026发布日程确认。工业品开盘后只有30分钟缓冲；CU/JM/I/J/RB/HC/FG/SA/LC/SI应把09:00–09:30视作pre-event price discovery，方向仓最好等数据后15–30分钟。
- **9月1日04:00 BJT｜USDA Crop Progress（8月31日16:00 ET）**：对玉米、大豆、棉花等天气/作物状况提供周度更新；只在状态变化超预期且CBOT价格确认时计入实体层。
- **9月1日22:00 BJT｜美国JOLTS（10:00 ET）**：影响美元与实际利率，间接作用金银、有色与原油估值。
- **9月2日22:30 BJT｜EIA Weekly Petroleum Status Report**：EIA官方页确认下一次发布为9月2日；SC/FU/LU应联合读取原油、成品油、炼厂开工、进口出口，不只看headline crude inventory。
- **9月3日20:30 BJT｜美国Q2 Productivity and Costs修订值**：美元/利率二阶催化。
- **9月4日20:30 BJT｜美国8月Employment Situation**：BLS官方日程确认；对AG/AU、工业金属与能源都有高Delta宏观影响。贵金属若届时仍处于Warsh后去杠杆阶段，优先有限风险表达，不裸追Gamma。
- **9月5日03:30 BJT｜CFTC COT**：周度仓位背景，不当实时仓位。下一OPEC+七国月度会议为9月6日，略超出本报告严格7日窗口，但能源仓位需要提前知道这一边界事件。
- **WASDE**：未来7日无WASDE，不为了填表虚构农业大事件。

## 十一、风险预算与每日固定回答

**是否值得新增风险**：不值得，今天没有可成交且证据闭环的70+机会。  
**最强/最弱产业链**：JM黑色趋势结构最整齐；贵金属从昨日最强转为最明显的逻辑破坏；工业品中“价格涨+contango+实体缺”最不值得追。  
**当前regime**：hawkish-rates repricing + weekend geopolitical gap risk + China/overseas timing divergence。  
**price是否获curve确认**：JM是；SC的contango支持fade观察；AG/CU/LC/SA/FG普遍不够。  
**是否获库存/实体确认**：总体没有；周度/旬度level不自动计方向层。  
**境内外是否同向**：AG已经从周五同向转为**中国未交易海外急跌**；SC仍是中国强、海外周线弱，但周末Hormuz风险冲突。  
**人民币/美元作用**：Warsh后美元走强构成贵金属/有色逆风；周一需看CNH与PMI共同作用。  
**期权是否优于裸期货**：方向表达若触发，倾向期货+保护腿；但execution false，今天不能给可成交结构。  
**是否有RV**：SC-Brent只是研究级定价背离，不是exact-contract/FX/tax/freight闭环套利。  
**哪些是单日噪音**：LC/CU/FG/SA中“上涨但contango、实体不确认”的部分最像资金/仓位噪音。  
**哪些应等30–45分钟**：AG、SC、JM、CU全部应等，且工业品要跨过09:30 PMI。  
**哪些不值得交易**：周一09:00第一跳追AG/SC、LC/SA追涨、execution-ready=false时裸卖/精确定价期权，都不值得。

风险预算：若周一触发，单一试仓最大损失NAV **0.25%–0.40%**；确认后最多0.75%–1.00%，只有四层以上真正闭环才考虑更高；单一主题总风险≤2.5%–3.0%。AG/AU合并USD-real-yield因子，SC/FU/LU合并Hormuz-energy因子，JM/J/I/RB/HC合并China-industrial因子。压力测试必须覆盖1/2个涨跌停、周末gap、相关性破裂、保护腿流动性消失、保证金上调、IV跳升/塌陷与人民币急变。

A. 今天没有应立即建立的新仓位。  
B. 今天不应跨周末挂静态条件单；SC2610空、AG2610反转空只能在周一开盘及09:30 PMI后完成价格/海外/curve确认再转条件单。  
C. JM2701续涨、CU2610 PMI后price/curve反应、SC/AG周一gap行为继续观察。  
D. 取消昨日AG2610顺势多预案；避免周一首跳追空AG/SC、裸卖期权、把C级basis或周度Physical包装成今日确认。

---

## 主要来源

- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- Reuters｜Gold drops after Warsh comments: https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/
- Reuters｜Oil settles lower; Hormuz deal rumors: https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/
- Reuters｜Iran navy says it has full control over Hormuz: https://www.reuters.com/world/middle-east/irans-navy-says-it-has-full-control-over-strait-hormuz-2026-08-28/
- CFTC｜COMEX futures-only COT, positions as of 2026-08-25: https://www.cftc.gov/dea/futures/deacmxsf.htm
- 国家统计局｜2026年主要统计信息发布日程: https://www.stats.gov.cn/sj/fbrc/bnxxfb/
- EIA｜Weekly Petroleum Status Report: https://www.eia.gov/petroleum/supply/weekly/
- BLS｜September 2026 release schedule: https://www.bls.gov/schedule/2026/09_sched_list.htm
- USDA NASS｜2026 report release days: https://www.nass.usda.gov/Publications/Reports_by_Release_Day/
- INE｜交易时间: https://www.ine.cn/services/calenderandholidays/tradinghours/
- SHFE｜连续交易规则示例/交易时间: https://www.shfe.com.cn/publicnotice/notice/202505/t20250526_827862.html

归档元数据：edition=`commodities_evening`；revision=1；CI=`pending_or_unverified`。
