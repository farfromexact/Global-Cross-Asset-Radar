# 商品期货期权晚间雷达｜2026-11-07

> 生成时间/信息截点：2026-11-07T19:42:36+08:00；研究用途，不下单，不假定持仓或成交。

## 1. 一句话结论

截至本报告时点，无可立即执行的合格新交易；周六无21:00夜盘，周一仅等CU跨期、SC重夺与AP有效报价，锡空因实体紧张降级。

今晚值得承担的不是周末方向仓，而是把风险预算留给周一可验证的三个条件：CU跨期回踩重夺、SC守位后重夺646、AP期权取得真实双边报价。**截至本报告时点，无可立即执行的合格新交易。** 已研究但优势不足：EC、SN；研究机会存在但等待条件/报价：CU、SC、AP；数据不足不能判断：EC现货运价、A/B基差、期权执行报价、动态保证金/限幅。最有价值的验证顺序是11月9日09:15的CU价差、SC价与Brent同向确认，以及AP701期权双边报价。

## 2. 数据质量、覆盖与事实台账

当前ref：Global-Cross-Asset-Radar `7c224833…`；China-Commodities-Engine `a7586fbc…`；China-Stock-Engine `80485af9…`。`report_input_latest.json`为空，故以模块文件为准；没有把空合并层冒充缺失全市场。

| 模块 | 目标/实际 | 日期/生成 | 状态与局限 |
|---|---:|---|---|
| Futures | 5所、806合约、77品种 | 源11/6；19:02重读 | full_market_ready=true，日期匹配100%，critical=0，placeholder=4 |
| Market State | 77/77 | 11/6 | 准确合约1/5D、RV/OI/曲线；部分历史缺交易日 |
| Physical | 20/18 | 11/6；06:09 | 2项不可用；A/B基差0，全部C级不计方向 |
| External | 22/17 | 11/6；19:04 | context_only；连续合约close与结算/官方收盘不混用 |
| Night | 806选、420夜盘、166窗外、6无成交、214 unresolved | 11/6晚—11/7凌晨，归属11/9 | validated/published；coverage 52.1092%、complete=false；detail空；exact-contract公共快照fallback，不认证官方夜收 |
| Options | 64目标、46尝试、45成功、1失败、18跳过；1068合约/45 series | 11/6；19:03再发布 | core ATM 44、skew 29；surface/positioning/execution均0，bid/ask=0，full-chain=false |
| Metadata | 806 | 11/6 | match 67.49%、effective 73.45%；乘数/tick effective 36.10%；night 0%；margin/limit 30.15% |
| Official crosscheck | SHFE238/INE63/CZCE243/GFEX48 | 11/6 | 比较字段无可信差异；DCE HTTP412；不含量仓核验 |
| Stock | 5579证券、5573报价、2个完整最小财务包 | trade_date 11/6；research_asof 11/7 08:32 BJT | 财务partial、复权missing、execution not_ready |

日历闸门：11月7日是周六，官方休市；周五夜盘属于11月9日交易日，`calendar_mismatch=false`。今晚不存在21:00会话，下一中国期货窗口是11月9日09:00。

| fact_id | 标的 | 值/口径 | 观测/known_at | 支持判断 | 局限 |
|---|---|---|---|---|---|
| F01 | 五所期货全集 | 806合约/77品种 | 源交易日2026-11-06；19:02重读 | 全市场扫描 | 无新交易日 |
| F02 | 夜盘状态 | trading_date=2026-11-09；420/806 | 生成2026-11-07 06:02 | 周五晚归属周一 | 214 unresolved、非完整覆盖 |
| F03 | CU2612/2701 | EOD收盘价差1180；夜快照1230 | 11/6收盘；11/7 01:00 | 近月韧性 | 快照非官方夜收 |
| F04 | SC2612/2701 | EOD收盘价差4.2；夜快照5.2 | 11/6；11/7 02:30 | 期限层未崩 | 实体SC/LU缺失 |
| F05 | SN2612 | 夜快照349830，较收盘+1.89% | 11/7 01:00 | 旧空触发未满足 | 供应商范围未认证 |
| F06 | 锡库存/曲线 | LME 3885t、SHFE 4004t；两地贴水 | Reuters 11/6 | 反对追空 | 周度/交易所库存仍需持续跟踪 |
| F07 | Brent/WTI | 98.32/90.83美元/桶结算 | 11/6纽约结算 | SC周一外部锚 | 周末无实时盘 |
| F08 | Options | 45/64成功；44 core ATM、29 skew | 11/6快照 | 局部IV可研究 | bid/ask=0，执行不ready |
| F09 | Physical | 18/20；A/B basis=0 | 11/6 | 实体层局部 | C级基差不计方向 |
| F10 | Crosscheck | SHFE/INE/CZCE/GFEX零价格差异 | 11/6 | 四所价格核对 | DCE 412未核 |
| F11 | CFTC铜 | 非商业净多37710，周减10607 | 持仓11/3，周五发布 | 铜外部层混合 | 并非实时仓位 |
| F12 | 紫金矿业601899.SH | 11/6收28.28，-4.07%；H1归母391.70亿元 | 价11/6；报表H1 | 公司表达校验 | 周六非实时、交易性未核 |
| F13 | 宝钢股份600019.SH | 11/6收6.11，+0.49%；H1归母45.71亿元 | 价11/6；报表H1 | 钢铁利润桥 | 采购/售价/套保未量化 |
| F14 | 交易日历 | 周六无21:00；下窗11/9 09:00 | 11/7核验 | 窗口闸门 | 周末突发只改变缺口风险 |

完整扫描分板块：黑色10、金属14、能源化工航运26、新能源3、农产品14、软商品10，合计77个实际产品；未入榜最重要异常分别为FG/SA旧夜盘快照本次未重验、锡实体紧张反驳追空、PP去杠杆但非新空信号、LC价升仓降、油脂谷物等待WASDE、AP价升仓减。覆盖不等于每个模块都具备执行数据。

## 3. 市场仪表盘

收益为结算基准；Night为供应商最新成交快照，非交易所核定最终夜盘收盘。OI/量如列为Night仅是供应商会话范围观察。

| 合约 | EOD收/结 | 1D/5D | 量/OI/ΔOI | 曲线 | Night快照 | 信号 |
|---|---:|---:|---:|---:|---|---|
| CU2612 | 104260/105110 | -1.1381%/-2.8468% | 193345/205726/9880 | 1.722% | 105060；2026-11-07 01:00 BJT；vsC 0.7673% / vsS -0.0476% | calendar-spread pullback only |
| SC2612 | 644/636.8 | 0.1903%/-12.7107% | 127996/18762/— | —% | 639.1；2026-11-07 02:30 BJT；vsC -0.7609% / vsS 0.3612% | reclaim 646 not satisfied |
| SN2612 | 343340/346310 | -2.0395%/-6.4432% | 342256/42233/2235 | 1.2214% | 349830；2026-11-07 01:00 BJT；vsC 1.89% / vsS 1.0164% | short trigger not satisfied; physical tightness opposes |
| AP701 | 6004/5969 | 4.9218%/5.125% | 546544/161014/-5668 | 6.8539% | —；—；vsC —% / vsS —% | local-vol watch; bid/ask absent |
| EC2612 | 2326/2351 | -1.5906%/-11.216% | 11797/17790/235 | -7.8265% | —；—；vsC —% / vsS —% | trend short watch; spot/freight missing |
| SA701 | 961/974 | -0.8147%/-0.2049% | 1641105/1209679/61934 | -2.4717% | —；—；vsC —% / vsS —% | previous fallback not revalidated; wait Monday |
| FG701 | 882/892 | 0.6772%/3.1214% | 1454240/1142845/-20658 | -0.7735% | —；—；vsC —% / vsS —% | previous fallback not revalidated; no chase |
| PP2701 | 9585/9496 | -3.5057%/-8.9811% | 1506943/538712/-56453 | 7.5276% | 9518；2026-11-06 23:00 BJT；vsC -0.699% / vsS 0.2317% | liquidation not a fresh short signal |
| AG2702 | 12402/12575 | -0.4276%/1.3704% | 611260/235765/2546 | -0.7975% | 12523；2026-11-07 02:30 BJT；vsC 0.9756% / vsS -0.4135% | option sample underlying mismatch |
| LC2701 | 92860/91940 | 1.2555%/2.0875% | 387415/391338/-24978 | 0.4081% | —；—；vsC —% / vsS —% | price up/OI down; no night session |

外盘完整会话锚：Brent 98.32、WTI 90.83美元/桶；repo连续合约口径分别97.92/90.34，仅作context。CFTC铜非商业多85660、空47950，净多37710，周减10607。周六19:30没有欧洲/美国实时窗口。

## 4. 相比前序的真变化

1. **仓库Futures于19:03重读11月6日全市场，值与晨报一致；没有新交易日** 合法last-good，不算新催化；全部触发移到周一真实窗口
2. **Stock引擎从11月5日推进到11月6日：紫金28.28/-4.07%，宝钢6.11/+0.49%** 只更新表达比较；同一商品冲击的股价不增加证据层
3. **新增独立锡实体证据：LME+SHFE库存合计约7889吨、四年低位且两地贴水** SN空头由64降59；旧触发仍未满足，不事后移动
4. **纳入CFTC 11月3日铜持仓：非商业净多37710、周减10607** CU外部层改为混合，72降71；仍须LME>=13750和价差回踩
5. **周六欧洲/美国与中国均休市；没有19:30实时海外增量或21:00夜盘** 风险只表现为周一缺口，不可写成已发生价格路径

旧观点处置：CU、AP、SC、EC的idea_id和触发不变；SN不重置ID、不移动343000/351000/330000/318000参数，只因新增反证降级。无成交回执，实际持仓一律为“未提供/未知”。

## 5. 产业链与公司利润桥

1. **铜矿—LME/SHFE—冶炼—电网/制造—紫金**：方向=CU跨期韧性强于单边；最强=CU2612-CU2701夜快照1230；最弱/反证=CFTC非商业净多周减10607；实体=CU现货109720但基差C级，不计方向层；期权=CU ATM IV19.265% vs RV11.636%，RR25=-9.28；无bid/ask；Stock=紫金11/6跌4.07%；H1利润强但产量、套保、金业务混合，股权表达不优于价差；置信度=中。
2. **原油—SC/LU/FU—炼化—PP/L/BU**：方向=短线地缘上行风险与供给宽松冲突；最强=SC近月价差夜快照5.2、Brent98.32；最弱/反证=FU/LU五日大跌、PP五日-8.98%；实体=SC/LU实体映射缺失；期权=SC ATM IV63.86%显著高于RV44.64%，不支持盲买波动；Stock=无新增合格公司披露；置信度=中低。
3. **锡矿—冶炼—焊料/光伏—电子**：方向=价格弱但实体紧，方向冲突；最强=LME/SHFE库存低位与贴水；最弱/反证=SN五日-6.44%、AI股风险偏好冲击；实体=独立实体证据反对追空；期权=ATM IV43.96%>RV28.52%、RR25=-8.78，保护需求已贵；Stock=未扩展为云锡独立股票推荐；公司原件未在本预算内核完；置信度=中。
4. **铁矿—焦煤焦炭—钢材—宝钢**：方向=原料与成材均缺高质量基差，利润桥待验；最强=I/RB/HC现货有值；最弱/反证=全部basis为C级；实体=宝钢H1收入+6.18%而归母-6.30%、成本+7.20%，说明传导不完全；期权=未形成可执行结构；Stock=宝钢11/6 +0.49%，但采购/库存/售价时滞未量化；置信度=低。
5. **鲜果—AP现货/期货—冷库/消费—期权**：方向=价格急升而OI下降，适合研究波动而非追多；最强=AP +4.92%、backwardation 6.85%；最弱/反证=OI -5668且实体层缺失；实体=无可计分A/B基差；期权=ATM IV33.545%低于RV37.203%，RR25=-2.48；但bid/ask=0；Stock=无自然优于期权的公司表达；置信度=中低。

限定公开补证覆盖紫金、宝钢及11月7日CNINFO检索；未取得足以改变商品论点的新经营公告。11月6日股票EOD是新增输入，但股价是同一风险冲击的映射，不增加第六层。

## 6. 统一机会榜

评分=逻辑25/赔率凸性25/催化20/价格曲线波动15/拥挤技术15；评分是研究优先级，不是胜率。

| 排名 | idea_id | 方向 | 分项=总分 | 五层证据 | 研究/证据/执行 |
|---:|---|---|---:|---|---|
| 1 | COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106 | 多近月/空远月 | 20/17/15/12/7=71 | 支持1,2,4；反对5；缺3 | priority/three_layers_external_mixed/not_ready_wait_pullback_depth_live_quotes |
| 2 | COM-M-AP701-LOCAL-VOL-CONVEXITY-WATCH-20261107 | 双向波动研究 | 18/16/15/12/9=70 | 支持1,2,5；反对1；缺3,4 | priority/three_layers_with_internal_counterevidence/not_ready_no_bid_ask |
| 3 | COM-M-SC2612-OVERNIGHT-REBOUND-CURVE-HOLD-LONG-20261106 | 多 | 19/17/14/10/9=69 | 支持2,4；反对—；缺3 | priority/two_layers_mixed_price/not_ready_wait_reclaim_646_monday |
| 4 | COM-M-EC2612-CONTANGO-TREND-SHORT-20261106 | 空 | 16/15/11/10/12=64 | 支持1,2；反对—；缺3,4,5 | observe/two_layers/not_ready_no_night_no_spot_freight |
| 5 | COM-M-SN2612-LME-DIVERGENCE-FAILED-BOUNCE-SHORT-20261106 | 空 | 14/12/11/10/12=59 | 支持4,5；反对1,2,3；缺— | early_watch/two_layers_with_three_opposing_layers/not_ready_old_trigger_not_satisfied |

## 7. 研究/交易卡

### 卡1：CU2612/CU2701跨期韧性多

- 新事实→定价→分歧：夜快照价差1230已反映近月韧性，不能追；分歧只在回踩后能否重新站上1050。CFTC净多下降使确信降低，但LME锚仍在阈值附近。
- 表达：多1手CU2612、空1手CU2701；吨数中性，不是Beta/保证金中性。股票替代紫金劣于跨期，因为混合金铜暴露、产量和套保噪声更大。
- 入场：11/9 09:15后价差先回踩950—1000、从未低于800，随后15分钟收盘重夺1050，且LME铜>=13750、两腿深度合格；全部AND。无回踩不追。
- 风险/退出：计划止损800；逻辑失效=价差<800或LME铜<13750且曲线同步转弱；TP1=1400、TP2=1650；11/13日盘收盘时间退出。
- 好/中/坏：950/975/1000，含每对500元成本后风险1250/1375/1500；TP1净利1750/1625/1500，R=1.40/1.18/1.00；TP2净利3000/2875/2750，R=2.40/2.09/1.83。
- 参数：每腿5吨、tick10元/吨、tick价值50元；最后交易日12/15与1/15。试仓<=0.35% NAV，手数=`floor(0.0035*NAV/1500)`。动态保证金/限幅未核；一腿失去流动性时止损不保证成交。

### 卡2：SC2612回踩后重夺多

- 新事实→定价→分歧：EOD收644、夜快照639.1，价差由4.2收盘口径到5.2快照口径；Brent98.32。市场已部分定价周五地缘反弹，分歧是宽松平衡表能否压过周末油轮风险。
- 表达：自然工具是SC2612期货；SC期权ATM IV63.86%高于RV44.64%，又无bid/ask，不是更好表达；不交易仍优于盲买高IV。
- 入场：11/9 09:15后守636—640、15分钟收>=640、SC2612-SC2701>=5、Brent>=98，之后重夺646；全部AND。开盘>=650且无回踩则放弃。
- 风险/退出：计划止损636；逻辑失效=Brent<96.5且价差<3；TP1=660、TP2=680；11/10中国日盘收盘退出。
- 好/中/坏：646/647/648，含1500元成本后风险11500/12500/13500；TP1 R=1.09/0.92/0.78；TP2 R=2.83/2.52/2.26。
- 参数：1000桶/手，tick0.1元/桶，tick价值100元；夜盘21:00—02:30，最后交易日11/30、交割开始12/7。试仓<=0.35% NAV，手数=`floor(0.0035*NAV/13500)`。1/2涨跌停和周末gap均可突破计划止损。

SN旧空头卡不升级：原条件“反弹344000—346000后15分钟跌破343000，且LME锡<=45800”未按顺序满足；夜快照反而349830。新增库存/贴水反证后，必须等实体紧张缓和才恢复为条件候选。

## 8. 商品期权专项

| 品种/series | ATM IV / RV20 | 25Δ skew | 局部结论 | 执行 |
|---|---:|---:|---|---|
| AP701 11/26 | 33.545% / 37.203% | RR -2.48、BF 2.225 | IV低于历史RV只构成研究线索；价格急升仓减，待双边询价 | not_ready |
| CU2612 11/24 | 19.265% / 11.636% | RR -9.28、BF 3.605 | 下行保护偏贵；不替代跨期 | not_ready |
| SC2612 11/12 | 63.86% / 44.645% | RR -0.09、BF 1.655 | 短到期事件波动已贵 | not_ready |
| SN2612 11/24 | 43.96% / 28.517% | RR -8.78、BF 0.10 | 下行skew贵且实体反证 | not_ready |
| LC2701 12/07 | 52.145% / 44.218% | skew not_ready | 仅ATM | not_ready |
| AG2612 11/24 | 47.165% / — | skew not_ready | 与主力AG2702月份不一致 | 不可用于主力执行 |

没有完整曲面、期限结构、全链持仓或dealer净Gamma结论；`quote_coverage_complete`只表示计划采样完成。缺bid/ask时只能倒推可接受成本，不能称期权已便宜或结构已限损。

## 9. 21:00夜盘风险地图

今晚无21:00夜盘。三层状态：Previous China EOD=11/6完整；Completed Night=11/6晚至11/7凌晨、归属11/9且局部；19:30 Overseas=周末休市，无实时新增。

- CU：周一可能偏高，但1230价差已定价韧性；09:15不追，等回踩；09:30中国CPI/PPI前控制试仓。
- SC：地缘新闻支持高开、供给宽松支持低开/冲高回落；只有守636—640再重夺646才行动。
- SN：夜盘反弹已反驳旧追空；先看343000是否按顺序失守，且实体贴水/库存紧张是否缓和。
- AP/EC/LC：制度无夜盘；09:15看价格、09:30看量仓、09:45看曲线与宏观冲击。不把周五OHLC穿越当成周一成交。

## 10. 未来24小时/7日事件与行动前清单

| 北京时间 | 事件 | 影响 | 处理 |
|---|---|---|---|
| 未来24小时 | 无预定一级宏观/交易所窗口；仅周末地缘、油轮与矿山/装置突发 | SC/有色周一缺口风险 | 不提前认定方向；周一用首15/30/45分钟确认 |
| 2026-11-09 09:30 | 中国10月CPI/PPI | 黑色、化工、有色需求与名义价格预期 | 开盘30分钟内不追宏观第一跳 |
| 2026-11-10 21:30 | 美国10月CPI | 美元/实际利率、贵金属和工业金属 | 线性仓降Delta；期权仅在双边报价可核后使用 |
| 2026-11-11 01:00左右 | USDA Crop Production/WASDE；EIA STEO | 谷物油脂与原油平衡表 | AP非直接替代；油品控制隔夜Delta/Vega |
| 2026-11-13 01:00 | EIA WPSR（Veterans Day顺延） | SC/LU/FU/BU | SC时间退出不晚于数据前再审 |
| 2026-11-13 17:00左右 | IEA 11月OMR | 全球油需/库存 | 若供给宽松证据强化，取消SC多头 |
| 2026-11-13 21:30 | 美国10月PPI | 美元利率/金属 | 避免事件前裸Vega和追价 |

行动前必须重新取得：周一准确合约双边报价/深度、动态保证金与限幅、CU/SC同步外盘、AP期权bid/ask；复核DCE官方交叉核对、A/B基差、EC现货运价。旧观点参数沿用上表，不因周末延后期限；输入版本为商品`a7586fbc…`、Stock`80485af9…`、Global prior`7c224833…`。发布前已重算5项评分和两张卡全部净R；未做完整曲面、实时保证金/限幅与实盘成交校验，故不能报通过。

## 资料来源

- [China-Commodities-Engine root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 五所806合约、77品种、full_market_ready=true；Futures 19:02重读但源交易日未变
- [China commodity exact-contract futures snapshot](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 仪表盘EOD收盘、结算、成交与持仓；近远月价差
- [China commodity market state](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 1/5日收益、RV20、OI变化、曲线
- [Night session status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（观测/报告日：2026-11-06/07；读取：2026-11-07T19:42:36+08:00）— trading_date=2026-11-09；420夜盘合约、214 unresolved、coverage incomplete
- [Sina exact-contract weekend quote fallback](https://hq.sinajs.cn/list=nf_CU2612,nf_CU2701,nf_SC2612,nf_SC2701,nf_SN2612,nf_PP2701,nf_AG2702)（观测/报告日：2026-11-06/07；读取：2026-11-07T19:42:00+08:00）— CU/SC/SN/PP/AG供应商最后成交快照；仅快照，不认证交易所最终夜盘收盘或纯夜盘OHLC/OI
- [Core option local surfaces](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— AP/CU/SC/SN局部ATM与25Δ偏度；surface/positioning/execution均未ready
- [Physical indicators](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 18/20可用；所有basis均C级且0项A/B可计分
- [External context snapshot](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 17/22 context-only；repo连续合约口径与结算/官方收盘不完全相同
- [Official futures price crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— SHFE/INE/CZCE/GFEX已比价格无差异；DCE HTTP412未核完
- [Reuters: tin rout versus physical tightness](https://www.reuters.com/commentary/reuters-open-interest/tin-hit-by-ai-stock-rout-despite-physical-market-tightness-2026-11-06/)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— LME库存3885吨、SHFE库存4004吨、合计约四年低位；两地贴水结构与印尼出口下降、个旧检修反驳追空
- [Reuters: oil settles amid Iran/tanker risk](https://www.reuters.com/business/energy/oil-set-sharp-weekly-drop-middle-east-supply-concerns-provide-floor-2026-11-06/)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— Brent 98.32、WTI 90.83结算；供给宽松与油轮袭击风险并存
- [CFTC COMEX copper futures-only COT](https://www.cftc.gov/dea/futures/deacmxsf.htm)（观测/报告日：2026-11-03；读取：2026-11-07T19:42:36+08:00）— 非商业多85660、空47950，净多37710；周净多减少10607，周末才纳入研究但不是新市场时点
- [SHFE 2026 holiday calendar](https://www.shfe.com.cn/services/calenderandholidays/holiday/)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— 11月7日周六休市；11月9日周一为下一实际日盘
- [NBS release calendar](https://www.stats.gov.cn/sj/fbrc/)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— 10月CPI/PPI于11月9日09:30发布
- [BLS November 2026 release calendar](https://www.bls.gov/schedule/2026/11_sched_list.htm)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— 美国CPI 11月10日08:30 ET；美国PPI 11月13日08:30 ET
- [USDA November 2026 crop report calendar](https://data.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=11&view=l&year=2026)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— 11月10日12:00 ET Crop Production；WASDE通常同日中午
- [EIA release schedules](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— WPSR因Veterans Day延至11月12日12:00 ET
- [IEA November Oil Market Report event](https://www.iea.org/events/oil-market-report-november-2026)（观测/报告日：2026-11-07；读取：2026-11-07T19:42:36+08:00）— OMR 2026-11-13发布
- [China-Stock-Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_inputs_latest.json)（观测/报告日：2026-11-06；读取：2026-11-07T19:42:36+08:00）— 5579证券、公司证据目录2家公司；执行检查not_ready
- [Zijin 2026H1 filing](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)（观测/报告日：2026-06-30；读取：2026-11-07T19:42:36+08:00）— 收入1941.78亿元、归母391.70亿元、经营现金流554.72亿元；铜/金利润传导取决于产量、成本、套保与时滞
- [Baosteel 2026H1 filing](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)（观测/报告日：2026-06-30；读取：2026-11-07T19:42:36+08:00）— 收入1607.31亿元、归母45.71亿元、毛利率约5.99%；原料上涨与钢材售价传导不完全

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：11月9日09:15后CU2612/2701回踩再重夺1050；SC2612守636—640后重夺646；AP701仅待双边期权报价。
C. 今天继续观察：EC2612趋势空、SN2612反弹失败空（已因实体紧张降级）、SA/FG周一量仓确认，以及紫金/宝钢利润桥。
D. 今天必须回避或有条件退出：回避周末虚构21:00行情、以旧快照代替周一报价、无bid/ask期权、C级基差套利和锡价下跌追空；未提供成交回执，不假定任何持仓。
