# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-30

> **周末模式。** 今天是周日，中国商品期货/期权休市；北京时间19:30时CME/COMEX/NYMEX与ICE Brent周日盘尚未重开。本报告严格使用最近完整中国交易日 **2026-08-28 EOD**、周五国际收盘与周末新闻，绝不把周末新闻包装成已发生的中国价格。  
> 数据协议：`china_commodities_v2`。下一批真正可交易的新信息先来自 **周一约06:00 BJT全球商品重开**，随后是 **09:00中国日盘、09:30中国8月官方PMI**。

## 一、今日一句话结论

**今日商品期货期权无合格交易。SC2610溢价回吐空最接近触发，AG2610失败反弹空次之，JM2701趋势多第三；三者都必须等周一全球重开与09:30 PMI后的真实价格确认。**

当前 regime：**weekend price-discovery vacuum + hawkish-rate repricing + unresolved Hormuz tail + pre-PMI China event risk**。今天最大的 edge 是不把“逻辑成立”误写成“现在可交易”。

## 二、数据质量与覆盖说明

本次第一读取层严格读取 China-Commodities-Engine 的 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`，并为前三名参数补读 `data/contract_meta.json`。统一输入在 **2026-08-30 08:23:40 BJT** 被重新构建，但 `requested_date` 仍是 **2026-08-28**，说明周末没有新的中国交易日。核心期货仍为8月28日五所完整EOD：SHFE/INE/DCE/CZCE/GFEX，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、unknown/duplicate/invalid OHLC/negative volume or OI均为0；5个OHLC placeholder继续排除异常排行。

Market State同样停留在8月28日，但它是最近完整交易日，1/3/5/20D均按**同一具体合约**计算，不拼连续主力。Physical仍是稀疏的native-frequency层：此前映射约4/20个目标；周度/旬度值只作为“最新周度/旬度数据”而不是今日变化。JM现货/basis仍为C级背景，不进入方向评分、不称套利。External仓库层为EOD/mixed per-series；周日19:30没有可用的15:00—19:30海外连续盘价格，因为全球主要商品期货尚未重开。

独立Options最新完整日期为8月28日：此前汇总为21,806条合约、370个series，363个`surface_ready`、74个`positioning_ready`、0个`execution_ready`，bid/ask coverage=0。周日统一输入将Options明确视为非当日fresh，因此本报告只把8月28日ATM IV/RR25/BF25当**最近完整波动率背景**，不把它计成周日新增期权证据，更不会虚构权利金、bid/ask、净成本或Dealer Gamma方向。

Contract metadata仍为partial：DCE contract-info抓取有JSON decode error，GFEX部分字段partial/stale；仓库整体multiplier/tick/margin/limit覆盖不足。SC2610的标准合约和最近可检索的交易所风控参数可由INE官方页面闭环；AG/JM无法独立闭环的动态参数继续标“未确认”。

## 三、商品仪表盘（最近完整中国交易日：2026-08-28）

| 板块 | 合约 | close / settle | 1D / 5D / 20D | Volume / OI / ΔOI | Curve | Physical / Basis | Options背景 | 周一信号 |
|---|---|---:|---|---|---|---|---|---|
| 贵金属 | **AG2610** | 17215 / 16818 | settle +0.77%；5D +1.25%；20D +17.71% | 765,356 / 261,945 / +5.77% | -0.14%，近乎平坦contango | 无方向闭环 | ATM IV 48.08%，RR25 +7.21；exec N | **失败反弹空观察** |
| 能源 | **SC2610** | 596.5 / 592.3 | settle +3.24%；5D -0.02% | ΔOI +15.93% | **-1.37% contango** | 无新实体闭环 | IV45.71 vs RV34.50；exec N | **溢价回吐空观察** |
| 黑色 | **JM2701** | 1629 / 1623 | 1/3/5/20D均正；5D +3.31%；20D +21.35% | 1,039,129 / 597,545 / +7.93% | **+1.53% backwardation** | 旬度现货仅level；basis C | IV32.32 vs RV20.54 | **PMI后趋势多观察** |
| 有色 | CU2610 | 108620 / 108660 | +0.15%；5D +3.01%；20D +8.29% | 154,411 / 198,417 / +1.65% | -0.64% contango | 无A/B basis | 仅研究 | PMI后重评 |
| 建材 | FG701 | 927 / 918 | +1.32% | 1,513,705 / 1,504,372 | -2.67% contango | 最新周度企业库存仅level | — | 不追涨 |
| 化工 | TA701 | 5630 / 5596 | +1.23% | 746,791 / 868,133 | +1.57% backwardation | PTA周度加工费仅level | — | 结构偏强，实体缺 |
| 新能源 | LC2701 | 159600 / 156000 | +2.40%；3D +1.33% | 239,379 / 391,884 | -1.15% contango | Physical unavailable | 研究层 | **涨价+contango≠短缺** |
| 油脂饲料 | M2701 | 3340 / 3344 | +0.60% | ≈165.7万 / ≈274.5万 | -0.96% contango | 缺进口/压榨闭环 | IV15.34；RR25 +4.26 | 等CBOT重开 |
| 软商品 | CF701 | 17180 / 17200 | +1.06%；5D +0.76%；20D +6.01% | 464,467 / 604,731 / +7.32% | -1.64% contango | 无fresh实体闭环 | IV13.15；RR25 +1.84 | 价仓强、curve弱 |
| 纯碱 | SA701 | 1047 / 1027 | settle +1.08%；5D -0.39% | 1,902,641 / 1,154,367 / -4.50% | -3.41% contango | 实体未闭环 | surface背景；exec N | fade观察 |
| 航运 | EC2610 | 1825 / 1866.5 | close -1.83%；settle +0.40% | — | +27.53%，强合约/季节效应 | 无可比海外套利 | — | 周一09:00再看 |

所有“价涨仓增/价涨仓减”等只作为attribution clue，不解释为确定的新多、新空、空头回补或多头止损。

## 四、相比上一交易日/上一期真正变化

**1）最重要的新信息其实是“没有新价格”。** `report_input_latest`周日早晨重新生成，但requested_date仍为8月28日；北京时间19:30时CME能源/金属和ICE Brent都还没有周日重开。CME/COMEX/NYMEX商品通常在周日美东18:00附近恢复，ICE Brent周日伦敦23:00开盘；按当前夏令时都约对应**周一06:00 BJT**。因此今晚不存在可以诚实称为“15:00—19:30海外实时变化”的价格层。

**2）周一交易流程从“一道门”变成“两道门”。** 第一门是约06:00海外重开，先让Brent/WTI/COMEX金银消化整个周末；第二门是09:30中国官方PMI。Reuters调查的8月制造业PMI中值为 **49.6**，较7月官方 **49.2**略改善但仍在50以下。因此49.5—49.7本身不是足够强的工业品bullish surprise；真正值得重新定价的是明显超预期、尤其重新站上50，或者显著弱于预期。

**3）原油和成品油的基本面方向进一步分叉。** 周日委内瑞拉宣布与美国的25年能源协议，目标把原油产量提高到 **150万桶/日**，这是中期增加原油供给的bearish背景；与此同时俄罗斯将柴油出口限制延长至9月30日，给中间馏分油供给带来相反方向的支撑。这个组合提高了“产品强于crude”的RV研究价值，但由于周末没有新spread价格，今天仍不能叫可执行套利。

**4）Hormuz尾部没有被解除。** Reuters最新可验证信息仍是伊朗为重开海峡设置条件、否认无条件恢复通航，且航运流量此前仍低于正常水平。因而SC的“中国溢价偏高”逻辑虽然更有中期供给支持，却不能在全球重开前升级为正式空单。

**5）AG的失败反弹空逻辑仍在，但没有新增确认。** 周五中国收盘后，Warsh的鹰派表态推动美元/利率重定价，现货黄金跌逾3%，白银跌3.5%至约66.81美元/盎司。CFTC 8月25日futures-only数据显示COMEX白银non-commercial多37,871、空12,610；黄金多277,159、空33,825，且黄金多头较前周增加20,257。它说明价格下跌前的多头仓位基础并不轻，但这是周二快照，只能叫positioning context，不能叫周日机构流向。

## 五、产业链地图

| 产业链 | 当前方向 | Price/Curve | 实体/仓单 | 海外/宏观 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 贵金属 | 中性偏空，等失败反弹 | AG周五强，但curve近乎平 | 无方向闭环 | Warsh后金银大跌；周一COMEX重开待确认 | safe-haven vs USD/real yield谁占优 | 中 |
| 原油/炼化/成品油 | **SC premium fade；产品相对强** | SC强涨但contango | 中国实体层不足 | Hormuz bullish tail；Venezuela crude bearish；Russia diesel ban bullish products | 周一Brent/WTI/Gasoil真正价格发现 | 中 |
| 焦煤—钢材 | JM偏多观察 | price/OI/backwardation整齐 | basis C；旬度spot仅level | PMI是第一催化 | 铁水/补库/库存方向 | 中 |
| 有色/新能源 | PMI前不追 | CU/LC价格强、curve弱 | sparse | 鹰派美元/利率 vs 中国需求 | PMI后curve/OI | 中低 |
| 农产品/软商品 | 选择性观察 | CF价仓强但curve弱 | 中国天气有背景，缺价格确认 | CBOT周一重开 | 天气→产量/进口→价格闭环 | 中低 |

当前最强结构仍是JM，但最有“错价味道”的仍是SC；最不值得追的是LC/CU/FG/SA等价格上涨却没有curve/实体共同确认的品种。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

| 排名 | 机会 | 分数 | 逻辑/赔率/催化/结构/技术 | 方向/持有期 | 有效证据层 | 阶段/数据惩罚 |
|---|---|---:|---|---|---|---|
| 1 | **SC2610 周一溢价回吐** | **69** | 20/17/14/10/8 | 条件空，1–3D | 1、2、4；期权仅背景 | 观察；周末无价格+Hormuz gap |
| 2 | **AG2610 失败反弹空** | **68** | 20/16/15/8/9 | 条件空，1–5D | 1、4；期权8/28背景 | 观察；避险反向尾部 |
| 3 | **JM2701 PMI后趋势续涨** | **66** | 19/15/9/11/12 | 条件多，2–10D | 1、2 | 观察；basis C+实体缺 |
| 4 | 中间馏分油相对原油强势RV | **64** | 18/15/15/8/8 | 多产品裂解/空crude beta，3–20D | 4 | 研究；无周末spread/中国不可比 |
| 5 | CU2610 PMI后price/curve重评 | **63** | 16/14/14/9/10 | 双向，1–5D | 1、2 | 观察；contango+PMI事件 |

SC虽然最接近70，但我仍把它压在69：周末没有第一笔全球重开价格，而且Hormuz风险是跳跃过程，不是普通波动。AG同样不因为周五美盘大跌就直接升级空单；中国市场必须自己“接受”低价。

## 七、前三名交易卡

### #1 SC2610｜69｜周一溢价回吐空观察

**事实**：8月28日close/settle 596.5/592.3，settle +3.24%，5D -0.02%，ΔOI +15.93%，near-next -1.37% contango；周五国际原油收跌且周线明显回落。周日委内瑞拉25年协议目标把产量提高到150万桶/日，增加中期原油供给压力；但Hormuz仍未无条件恢复。

**市场定价**：周五中国SC保留的地缘溢价明显高于全球原油周末前的最终定价。  
**市场可能错在哪里**：一条真正改变实物流量的Hormuz攻击/封锁新闻，可让Brent和SC直接跳空到任何静态止损之上。  
**推断**：只有周一全球重开不支持高油价、且SC在PMI后仍守不住592.3—596.5，fade才真正成立。  
**主观判断**：这是今晚最好的“等待交易”，不是周末持空交易。

**最佳表达**：`Short SC2610 futures + protective Call`。保护腿只有周一获得实时quote/Delta后才能确定；`execution_ready=false`，不提供strike、bid/ask、净权利金。

**入场**：今晚不下单。第一闸门：约06:00 BJT看Brent/WTI重开；第二闸门：09:30 PMI。优选 **09:45以后**，SC持续低于592.3，反抽594—596失败，同时海外原油没有持续gap-up。若SC一开盘就低开>2%，不追，至少等45分钟。

**分批**：50%在PMI后失败反抽；另50%只在创当日新低且curve没有明显转强时加。  
**初始止损**：603—605区域；若Hormuz出现已验证的实质供应中断，优先按逻辑止损。  
**失效**：SC接受603—605上方；Brent持续高开；curve显著走强/转backwardation。  
**TP1/TP2**：580—582 / 573—575。**时间止损**：1–3D。  
**最大损失**：试仓NAV 0.25%–0.40%，能源同因子合并计算。

**参数**：INE标准合约交易单位1000桶/手、tick 0.1元/桶、tick value 100元/手；按592.3计notional约592,300元/手。INE 2026-06-23公告对SC2610给出的涨跌停为±14%，一般持仓保证金16%（若触发风险控制规则仍可进一步调整）；broker margin未确认。单个14% limit静态名义PnL约82,922元/手，两个同向14%复合约177,453元/手。标准合约最后交易日规则为“交割月份前一月最后一个交易日”，具体日历日期执行前再核。今天周日没有21:00中国夜盘。

### #2 AG2610｜68｜失败反弹空观察

**事实**：8月28日17215/16818，20D +17.71%，ΔOI +5.77%。8月28日9/23到期series：ATM strike 16800、ATM IV 48.08%、RR25 +7.21、BF25 +2.245，`surface_ready=true / positioning_ready=false / execution_ready=false`。中国收盘后国际白银跌3.5%至约66.81美元/盎司。

**市场定价**：中国周五收盘还没有交易Warsh后更鹰的美元/利率路径。  
**市场可能错在哪里**：Hormuz恶化或美元/实际利率反转，会迅速恢复贵金属避险需求。  
**推断**：真正的bearish regime flip不是“低开”，而是周一中国市场在16818下方持续接受。  
**主观判断**：先确认旧多逻辑死亡，再确认空逻辑出生；两件事不是同一件事。

**最佳表达**：空AG2610期货+protective Call，或确认quote后做有限风险Put Spread。IV与upside skew都很贵，不主张无条件追买Put。

**入场**：约06:00先看COMEX金银；09:30 PMI后至少等至09:45。AG持续低于16818、反抽失败，同时COMEX silver没有明显修复周五跌幅。若低开>2%，不追，等45分钟。  
**分批**：50%失败反抽；50%跌破前45分钟低点。  
**失效**：重新接受16818上方，同时COMEX silver明显反转。  
**TP1/TP2**：16550 / 16200附近。时间止损1–5D。最大损失0.25%–0.40% NAV。

**参数**：上期所资料可确认标准交易单位15千克/手，据此16818结算对应notional约252,270元/手；但本次仓库`contract_meta`对AG仍属official_partial，tick、动态margin、price limit、night-session、LTD未在本次运行中完整闭环，全部执行前复核，不能拿旧参数填补。

### #3 JM2701｜66｜PMI后趋势续涨观察

**事实**：1629/1623；1/3/5/20D同合约收益均正，5D +3.31%、20D +21.35%；ΔOI +7.93%，near-next +1.53% backwardation。实体层只有旬度现货level，basis C，不能计入方向评分。

**市场定价**：国内煤焦趋势结构是目前最整齐的一组。  
**市场可能错在哪里**：20D涨幅已经大、OI扩张，而实体闭环不足；弱PMI可以把“趋势”瞬间改写成拥挤去杠杆。  
**推断**：PMI后backwardation仍在，才比09:00首跳有信息量。  
**主观判断**：只有两层方向证据，严格停在70以下。

**入场**：PMI公布后至少等15分钟；1600—1615回踩被吸收，重新站上1629，backwardation没有明显收窄且OI不塌陷。  
**分批**：50%重回1629；50%突破PMI后首小时高点。  
**止损/失效**：1590下方，同时curve明显收窄/转contango或OI快速下降。  
**TP1/TP2**：1665 / 1710；时间止损2–10D；probe risk 0.25%–0.40% NAV。

**参数**：DCE contract-info本次仍报JSON decode error，因此multiplier、tick、tick value、exchange margin、price limit、night session、LTD全部标记**未确认**。没有这些参数，本卡不能升级成正式执行卡。

## 八、商品期权专项

周日没有新的中国期权交易。以下均为8月28日最近完整surface背景，不计成“周日新鲜期权层”：

| Series | ATM IV | RV20 | IV-RV | RR25 | Positioning | Execution | 结论 |
|---|---:|---:|---:|---:|---|---|---|
| AG2610 | 48.08% | 29.71% | +18.37 vol | +7.21 | N | N | vol/upside skew贵；不盲追Put |
| SC2610 | 45.71% | 34.50% | +11.21 vol | -2.07 | N | N | 地缘tail已收费；用保护腿而非纯买vol |
| JM2701 | 32.32% | 20.54% | +11.78 vol | +0.11 | Y | N | skew近中性，但IV仍贵于RV |

因此今晚没有一个可以称为“全市场买波动率机会”的信号。更合适的框架仍是：**期货拿Delta，期权封尾部**；等周一实时报价恢复后再决定结构。`dealer_gamma_direction_known=false`，不推断dealer gamma。

## 九、21:00夜盘开盘风险地图｜周末模式

**今晚没有中国21:00夜盘。** 这是周日，不得构造不存在的夜盘gap。下一中国可交易窗口为 **2026-08-31 09:00 BJT**；真正更早的价格发现来自约 **06:00 BJT** 的CME能源/金属与ICE Brent重开。

| 品种 | 周末信息映射 | 周一风险 | 是否追首跳 | 等待 | 第一确认 |
|---|---|---|---|---|---|
| **SC** | Hormuz未解 + Venezuela中期增供 + Russia柴油限制 | 双向gap最大 | **否** | 海外重开30–60m；中国等过PMI | Brent/WTI、592.3/596.5、curve、Hormuz |
| **AG** | Warsh后金银跌 vs 地缘避险 | 偏低开但双向 | **否** | COMEX先看；中国30–45m并跨PMI | 16818、silver、USD/real yields |
| **JM** | 海外直连弱 | 不预判 | **否** | PMI后15–30m | 1623/1629、OI、backwardation |
| CU | 鹰派美元/利率 + China PMI | 事件敏感 | 否 | PMI后30–45m | LME/COMEX copper、CNH、curve |
| SA/FG/LC | Friday price强但curve弱 | 高噪音 | **不追** | 45m | curve/OI/实体是否补确认 |
| EC | 无夜盘 | — | — | 周一09:00 | 仅看日盘 |

## 十、未来24h / 7d事件

- **8月31日约06:00 BJT｜CME能源/金属、ICE Brent周日盘重开**：这是周末后第一笔真正价格。SC/AG任何入场都必须先看这三小时海外价格发现；gap本身不是追单理由。
- **8月31日09:00｜中国商品日盘开盘；09:30｜中国8月官方PMI**：Reuters调查制造业PMI中值49.6，7月官方为49.2。黑色、有色、建材、新能源的09:00—09:30应视为pre-event discovery；至少等PMI后15分钟。
- **9月1日04:00｜USDA Crop Progress**：玉米、大豆、棉花等只在作物状况变化与CBOT价格共同确认时计入实体层。
- **9月1日22:00｜美国JOLTS**：通过美元/前端利率影响AG/AU、CU；不在数据前把贵金属Delta加满。
- **9月2日22:30｜EIA Weekly Petroleum Status Report**：SC/FU/LU同时看crude、gasoline、distillate、refinery runs、imports/exports，不能只看headline crude inventory。
- **9月3日20:30｜美国Q2 Productivity and Costs修订；9月4日20:30｜美国8月Employment Situation**：均是美元/实际利率/贵金属的重要催化，事件前优先有限损失结构。
- **9月6日｜OPEC+七国月度会议**：8月会议已决定9月从额外自愿减产中调整 **+188 kb/d**，9月6日再评估市场；能源仓位必须把周末gap纳入持仓成本。

## 十一、风险预算与决策归纳

**是否值得新增风险？** 今天不值得；周一若触发，SC/AG/JM初始probe建议最大损失NAV **0.25%–0.40%**，而不是因为风险偏好高直接打到1%。只有周一真实价格+curve+宏观/实体重新形成≥3层，才考虑把单笔确认风险提高至0.75%–1.50%。

**Price是否获curve确认？** JM是；SC的contango支持“premium fade”而不是追多；AG curve几乎平；CU/LC/FG/SA普遍没有。  
**是否获库存/实体确认？** 大多数没有，这是今晚不出现70+交易的核心原因。  
**境内外是否同向？** 目前不能谈周日“同向”，因为海外尚未重开；周五贵金属与中国收盘明显错位，SC也存在中国/全球错位。  
**人民币/美元作用？** 周一主要通过PMI→CNH和Warsh→USD/real yields传导；没有周日实时价格，不写具体点位。  
**期权是否优于裸期货？** 作为保护腿优于裸风险，但IV普遍不便宜；execution-ready=0，不能给伪精确结构成本。  
**RV？** “中间馏分油强于原油”值得追踪，但Russia diesel ban、Venezuela crude supply是不同期限的基本面冲击，未有周末spread price，因此现在只是研究级RV，不是套利。  
**单日噪音/不值得交易？** LC/CU/FG/SA这类Friday上涨+contango+实体不确认，仍是最需要避免追价的组合。

### 关键公开来源

- [Reuters — Oil settles lower on clues about Fed policy, rumors of Hormuz deal](https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/)
- [Reuters — Iran sets conditions for reopening Strait of Hormuz](https://www.reuters.com/world/middle-east/irans-security-chief-denies-allegations-iranian-plot-assassinate-trumps-son-al-2026-08-27/)
- [Reuters — Venezuela 25-year US energy deal](https://www.reuters.com/business/energy/venezuelas-interim-president-says-us-energy-deal-will-last-25-years-2026-08-30/)
- [Reuters — Russia extends diesel export ban](https://www.reuters.com/business/energy/russia-extends-ban-diesel-exports-until-september-30-2026-08-29/)
- [Reuters — Gold drops 3% after Warsh comments](https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/)
- [Reuters — China August PMI poll](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/)
- [国家统计局 — 2026年7月中国采购经理指数](https://www.stats.gov.cn/sj/zxfbhjd/202607/t20260731_1964253.html)
- [CFTC — COMEX futures-only COT](https://www.cftc.gov/dea/futures/deacmxsf.htm)
- [CME Group — Trading Hours](https://www.cmegroup.com/trading-hours.html)
- [ICE — Brent Crude Futures](https://www.ice.com/products/219/Brent-Crude-Futures)
- [INE — 原油期货标准合约](https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html)
- [INE — 2026-06-23 SC/LU保证金及涨跌停调整](https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html)
- [OPEC — 2 August 2026 production adjustment](https://www.opec.org/pr-detail/611-2-august-2026.html)
- [EIA — Weekly Petroleum Status Report Schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [BLS — September 2026 release schedule](https://www.bls.gov/schedule/2026/09_sched_list.htm)
- [USDA NASS — August 2026 calendar](https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=08)

A. 今天没有应立即建立的新仓位。  
B. 今天不应挂跨周末静态条件单；SC2610空、AG2610失败反弹空、JM2701多只能在周一06:00海外重开和09:30 PMI后的价格/curve确认后转为条件单。  
C. 今天应继续观察SC中国溢价、AG在16818下方的接受度、JM backwardation，以及俄罗斯柴油出口限制与委内瑞拉增产计划造成的成品油/原油相对价值。  
D. 今天必须避免把周五EOD当周日实时、追周一首个gap、在execution_ready=false时虚构期权成本、把JM C级basis当套利或把价格上涨+contango解释为短缺。
