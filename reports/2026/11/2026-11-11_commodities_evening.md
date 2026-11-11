# 商品期货期权晚间雷达｜2026-11-11

> 生成时间：2026-11-11T19:32:42+08:00｜中国EOD：2026-11-11｜下一真实窗口：2026-11-11 21:00 BJT（归属交易日2026-11-12）  
> 研究用途，不下单；无成交回执，所有实际持仓均为未提供/未知。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；豆粕1—5正套仍最值得等21:00回踩，SC只看重夺610后的事件多头。**

截至本报告时点，无可立即执行的合格新交易。区别如下：

- **已研究但优势不足**：AG2702反弹与热CPI/鹰派利率冲突；EC2612单日异常上行却缺曲线和实体运价。
- **研究机会存在、等待条件/报价**：M2701/M2705回踩确认；SC2612重夺610并由Brent与1—2价差共同确认；CU价差等待回落旧价值区。
- **数据不足不能判断**：当前五所Futures主批0记录；新能源与多数化工/农产品只有11/9 last-good，不能用“无交易”掩盖缺数。
- **最有价值的下一观察**：①21:00 M1—5是否先回踩再守300；②SC能否在Brent≥93时15分钟站上610；③EC下一日盘是否获运价/曲线确认。

## 2. 数据质量与覆盖

| 模块 | requested/source/generated | 实际取得与就绪 | 局限 |
|---|---|---|---|
| Futures | 11/11；19:03:55 | 五所目标、0合约；full_market_ready=false；source_date_match=0；critical=15 | iFinD -4318；仅13个重点合约/series用公开源下钻 |
| Market State | source 11/9 | 806合约/77产品last-good可作5D/RV背景 | 非11/11 EOD，不作当前触发 |
| Physical | 11/11；18/20 | fresh18、stale0、carried0；basis C=18，A/B=0 | 地区/品质/税/交割缺失，不计套利层 |
| External | 11/11；19:12:37；17/22 | LME/COMEX/CBOT/BMD等context | DXY、USD/CNH、实际利率缺；跨时点不作套利 |
| Night | 交易日11/11、开始11/10；06:04 | fresh/validated/published=true；417/806夜盘；coverage51.737% | detail空；outside169、no-trade6、query_error/unresolved214；official close=false；calendar_mismatch=false |
| Options | trade date11/10；45/64、1078条/45 series | core_v1/sampled；skew_ready=22 | coreATM/surface/positioning/execution=0；bid/ask=0；非全链 |
| Metadata | source11/9 | 可读last-good | 重点合约最后交易日/当期保证金仍需临近复核 |
| Crosscheck | trade date11/11 | SHFE官方238、INE63、CZCE243、GFEX48，但baseline为空 | matched/comparable/different均0；DCE HTTP412；不是价格差异证据 |
| Stock | trade date11/9；research asof11/10 08:40 | 5579证券、事件34、完整最小财务包2 | 复权/当前价/执行未就绪；只做利润验证 |

全范围后台：63个指定代码与last-good 77产品均初筛；当前批0产品，不宣称缺失品种“没有机会”。动态PD/PT仅在期权目录出现，未满足当前期货/流动性/报价核验，未晋级。

## 3. 市场仪表盘

| 标的 | EOD/快照 | 1D/曲线与量仓 | Physical/Options/海外 | 信号 |
|---|---|---|---|---|
| M2701/M2705 | 3139/2839 close; spread300 | +2.15% M2701 vs prev settle; spread +15 vs 11/10 close；exact-contract public EOD; OI 1,862,901/1,152,000; ΔOI -25,247/-6,295 | 2026-11-11 EOD | 21:00只等回踩确认，不追304以上 |
| SC2612 | 604（另一源606） | -0.84% vs prev settle using604；public EOD conflict; O/H/L590/609.8/585.5 | 2026-11-11 EOD | 旧短计划作废；只有重夺610才研究多头 |
| CU2612/CU2701 | 105820/104600; spread1220 | -0.06%/-0.15% vs prev settle；public exact contracts; volumes 96,974/72,294; OI191,115/165,181 | 2026-11-11 EOD | 曲线韧性但价差仍太贵，不追 |
| AG2702 | 12748 | +0.07% vs prev settle；vendor latest/close; OI264,224; volume760,198 | 2026-11-11 EOD | 晨间短空失效；只观察能否站上12820 |
| EC2612 | 2513.5 | +5.35% vs settle; +4.47% vs close；intraday snapshot, final settle unverified | 2026-11-11 14:06 BJT | 旧空头研究失效；无夜盘，不追涨 |
| C2701 | 2188 | -1.13% vs prev settle；public intraday/EOD-near snapshot | 2026-11-11 14:21 BJT | 与USDA供需利多背离，取消做多优先级 |
| I2701 | 683.5 | 缺；contract value embedded in Physical; current core EOD absent | 2026-11-11 Physical snapshot | 现货664.78；basis C，不作套利 |
| RB2701 | 3045 | 缺；region/grade/tax/delivery incomplete | 2026-11-11 Physical snapshot | 现货3106.5；basis C，只作利润桥背景 |
| P2701 | 8854 | 缺；Physical+External context | 2026-11-11 19:12 BJT | 现货8690；外盘BMD palm4407，时点/单位不支持套利 |
| Brent/WTI | 92.77/86.80 | 约+1.4%/+0.9% at 09:34 GMT；Reuters realtime | 2026-11-11 09:34 GMT | 地缘修复与API累库冲突；等待SC夜盘定价 |
| LME Cu 3m proxy | 13815.5 | 缺；repo context-only continuous proxy | 2026-11-11 19:12 BJT | 高于晨间13750确认线，但时点不可与中国收盘做套利 |

板块未入榜异常：黑色Physical虽有I/JM/J/RB当前值但basis全C；能源化工SC以外当前合约不足；新能源LC/SI/PS无11/11准确合约；农业C2701对USDA利多反应偏弱；航运EC是最大异常但证据仅价格层。

## 4. 相比前序的五项真变化

1. **豆粕1—5价差由11/10收盘285扩大至11/11收盘300（结算306）**：方向层与期限层支持仍在，但晨间顺序触发不可由OHLC证明；将下一窗口改为21:00回踩确认，不追涨。
2. **SC2612从585.5低点修复至约604/606，Brent回升至92.77**：晨间反弹失败空的首日低开放弃条件已满足；旧短计划失效，新研究改为只有重夺610的事件多头。
3. **AG2702收复至12748，外盘银52.87超过晨间短空的52.80外部失效线**：晨间新短候选失效；不推断成交或损益，转为双向观察。
4. **EC2612上行约4.5%（相对前收）**：连续两日反弹构成旧趋势空的关键反证；无实体运价/曲线确认，不反手追多。
5. **CU2612-2701收盘1220、LME铜代理13815.5**：曲线与外盘均改善，但价差仍远高于950—1050旧入场区；研究分数上调，执行仍未触发。

前序处置：不以OHLC穿越认定晨间M或AG已触发；SC晨间空计划因首笔/开盘低于598而失效；CU旧950—1050入场带不变；EC旧空头研究被价格反证击穿。

## 5. 产业链与传播路径

| 链条 | 方向/强弱 | EOD与曲线 | 实体/期权/海外 | 最大缺口与置信度 |
|---|---|---|---|---|
| 美豆→进口大豆→豆粕/豆油 | 豆粕近强远弱；强:M2701；弱:C2701/豆油相对 | M1-5 close300；21:00尚未发生；近月升水扩大 | M现货3208、近月3000、主力3139；basis C不计分；M skew局部可读但ATM/execution不可用；CBOT soy1224.25, meal325.6 | 进口到港、压榨利润与当前港口库存缺失；中高 |
| 地缘/航运→Brent/WTI→SC/燃料 | 修复但双向事件风险；强:Brent；弱:SC仍低于前结算 | SC约604/606；21:00待定；SC2612-2701公开配对约11—13但收盘源冲突 | FU/SC基差仅C级；SC ATM/execution未就绪；Brent92.77/WTI86.80；API据报+9mbbl | EIA正式库存和SC精确同源near-next；中 |
| LME铜→进口精矿/冶炼→沪铜/矿企 | 外盘强、国内近月升水韧性；强:LME copper proxy；弱:股票表达证据陈旧 | CU spread1220；21:00待定；近月升水但高于旧价值区 | 现货108321.67、CU2612 105820；basis C；CU skew局部ready，ATM/execution不可用；LME proxy13815.5 | TC/RC、进口盈亏、库存变动和同刻FX；中 |
| 美通胀/实际利率→金银→AG/AU/紫金 | 反弹与利率反证并存；强:银日内弹性；弱:方向确信 | AG2702 12748；21:00待定；未取得当前同源near-next | 公司半年报仅确认条件暴露；AG局部skew可研究、执行不可用；spot silver52.87/gold4051.31 | 实时DXY/实际利率与期权报价；中低 |
| 运价风险溢价→EC | 异常上行/可能挤空；强:EC2612；弱:实体确认 | 2513.5；无夜盘；当前曲线缺失 | SCFI/航线即期报价未取得；不适用/未取得；红海/霍尔木兹运输风险仅间接 | 周度运价、舱位与近远月；低 |

Stock利润桥：紫金的矿产铜/金售价可能受益，但产量、品位、成本、套保、汇率和少数股东决定净效应；宝钢的钢价/结构对抗矿焦煤/能源/库存结转，半年报不支持“原料跌=利润必升”。11/11限定检索未见两家公司新的经营公告，股票表达不优于直接商品。

## 6. 统一机会榜

| 排名 | idea_id / 方向 / 阶段 | 五层 | 分项（逻辑/赔率/催化/价曲波/拥挤） | 总分 | 三轴状态 |
|---:|---|---|---|---:|---|
| 1 | COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111<br>long near/short deferred；conditional_wait_21h | 支持1,2,3,4；反证:两腿OI均下降，无法判定新多/空回补；basis C；期权ATM/执行缺失；缺5 | 21/19/17/9/7 | 73 | 研究:priority；证据:4层支持但实体主要来自USDA/现货背景；执行:not_ready_sequence_and_live_depth_unverified |
| 2 | COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106<br>long near/short deferred；watch_no_chase | 支持1,2,4；反证:价差1220远高于旧入场区950—1050；basis C；TC/库存缺口；缺3,5 | 20/16/13/11/9 | 69 | 研究:focus；证据:3层但Physical不足；执行:not_ready_price_outside_zone |
| 3 | COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111<br>long；conditional_wait_21h | 支持1,2,4；反证:API据报累库9mbbl；收盘源604/606冲突；OPEC供给与EIA未核；缺3,5 | 18/16/15/11/8 | 68 | 研究:focus；证据:3层但第2层依赖待核pair；执行:not_ready_until_exact_21h_quotes |
| 4 | COM-M-AG2702-TWO-WAY-REPRICING-WATCH-20261111<br>two-way watch；research_watch | 支持1,4；反证:热CPI/鹰派利率；无当前curve与ATM执行报价；缺2,3,5 | 17/13/12/11/10 | 63 | 研究:watch；证据:2层；执行:not_ready_no_directional_trigger |
| 5 | COM-M-EC2612-CONTANGO-TREND-SHORT-20261106<br>neutral/watch；old_short_invalidated | 支持1；反证:实体运价和曲线缺失；无夜盘；缺2,3,4,5 | 17/12/12/10/7 | 58 | 研究:watch；证据:1层，按规则封顶59；执行:not_ready |

评分复核：五项分项分别加总为73/69/68/63/58；EC仅1层，严格≤59。分数是研究优先级，不是胜率或仓位。

## 7. 研究/交易卡

### 卡1｜M2701/M2705 近月多—远月空（rev2）

- **新增事实**：close spread=300、settle spread=306；两腿ΔOI=-25,247/-6,295。**定价**：日盘已把晨间285中心明显抬高。**分歧**：若21:00先回踩再守300，近月紧张可能尚未完全定价。
- **证据**：1价格、2期限、3实体、4海外支持；OI下降、basis C、第五层缺失为反证/缺口。OI不解释为新多或回补。
- **触发（AND且有顺序）**：先回踩292—298；首15分钟低点≥286；21:15收盘≥300；随后5分钟回踩296—300不破；CBOT soy≥1220；两腿深度正常。50%在296—300，第二次守300再50%；>304不追。
- **失效/退出**：新计划止损284，TP1=340、TP2=370，11/18 14:55时间退出。仅适用于未来新候选，不改写晨间计划。
- **参数**：1:1；乘数10吨/手，价差1点=10元；费用/滑点假设80元/组；当前保证金未知。
- **好/中/坏**：296入场风险200元，TP1/TP2净360/660元=1.80R/3.30R；300为240元、320/620=1.33R/2.58R；304为280元、280/580=1.00R/2.07R。
- **压力**：单腿涨跌停、腿差流动性消失、夜盘gap均可令损失超过计划止损；期货不是结构限损。

### 卡2｜SC2612重夺610事件多头（新child，parent=原SC空）

- **新增事实**：日盘低585.5、收604/606；Brent92.77、WTI86.80。**已定价**：地缘修复已部分反映。**分歧**：若Brent≥93且SC站稳610，国内风险溢价仍可继续修复。
- **竞争解释**：API据报原油库存+9百万桶、供给上升可压制油价；SC两点收盘冲突使触发必须用21:00同源精确报价。
- **触发（AND）**：Brent≥93；SC首15分钟收≥610；随后5分钟回踩608—611不破；SC2612-SC2701≥10。50%在610，确认后50%≤612；>614放弃。
- **失效/退出**：计划止损599；Brent<91.80或1—2价差<5为逻辑失效；TP1=630、TP2=648；11/17 22:55时间退出。
- **参数**：1000桶/手，tick0.1=100元；成本假设1500元/手；当前保证金未核，last-good限幅背景18%需再核。
- **好/中/坏**：610风险12,500元，TP净18,500/36,500=1.48R/2.92R；612为14,500、16,500/34,500=1.14R/2.38R；614为16,500、14,500/32,500=0.88R/1.97R，因此614不做。
- **压力**：以604计单个18%逆向限幅约108,720元/手，两个限幅约217,440元，未含滑点/保证金上调；止损不封顶。

少于3张：CU价差仍在旧入场区外，AG/EC没有合格方向与执行报价，不凑卡。

## 8. 商品期权专项

- 样本：11/10，45/64产品、1078条、45 series；collection_scope=core_v1、analytics_scope=sampled_strikes；full_chain_verified=false。
- 局部能力：core_atm_ready=0，skew_ready=22，surface/positioning/execution=0；bid/ask与underlying settlement覆盖均0。
- 因无合格ATM配对，不能计算本期Top标的ATM IV-RV；因只有局部skew，不外推term、wing、tail或dealer gamma。
- M/SC可保留“买入价差待询价”作为结构备选，但必须拿到准确expiry/strike/bid/ask/净支出；最高净支出不得超过对应期货计划风险预算。未询价不称便宜、不称可执行或有限损已确认。
- Vol RV：本期最有价值不是裸买波动，而是等待EIA/IEA或夜盘方向触发后再比较局部IV与同口径RV；当前不可计算，明确为数据不足。

## 9. 21:00夜盘风险地图

| 主题 | Previous China EOD | 已完成历史Night | 19:30海外/事件 | 21:00与15/30/45分钟 |
|---|---|---|---|---|
| M1—5 | 300 close/306 settle spread | 11/10夜归属11/11；明细文件空，不作正式收益 | CBOT soy1224.25/meal325.6 | 若开在296—304，等15/30/45分钟顺序；>304不追；<286取消；风险:两腿流动性不同步/价差跳空 |
| SC | 604与606冲突；高609.8 | 旧会话只知status，明细空 | Brent92.77/WTI86.80；API据报累库 | 高开但<610不追；>=610且回踩守住才条件多；<599继续观察不追空；风险:地缘与库存双向gap |
| CU | CU2612/2701=105820/104600，spread1220 | 旧公开快照不重用为今晚行情 | LME proxy13815.5 | 价差仍>1150不追；15/30/45分钟仅看是否回落至价值区；风险:外盘/汇率/合约时点不齐 |
| AG | 12748 | 晨间短空外部失效线已被silver突破 | silver52.87/gold4051.31；鹰派利率反证 | >12820并守30分钟才重评多；<12580才重评弱，不在区间中部交易；风险:宏观数据/美元利率跳变 |

日历闸门：11/11 21:00属于交易日11/12；历史session_start=11/10、trading_date=11/11，归属合法，无calendar_mismatch。禁止将06:04 status或晨间fallback称作今晚夜盘。

## 10. 未来24h/7d事件与行动前检查

- **2026-11-11晚间｜OPEC月报**：公开检索确认计划窗口但截至截点未取得实际报告原文；油价Delta/Vega双向；未取得不作已发生催化
- **2026-11-12 21:30｜美国PPI与USDA出口销售（市场日历，需临近再核官方）**：金银/美元与谷物；不在发布前用旧期权快照做短Gamma
- **2026-11-13 01:00｜EIA Weekly Petroleum Status Report（Thu 12:00 ET）**：SC/Brent方向与IV；若库存与API大幅背离，撤销单边假设
- **2026-11-13 17:00｜IEA Oil Market Report November launch**：原油供需基线；事件前缩小线性仓，未报价期权只待询价
- **2026-11-14以后｜CFTC持仓周报、天气与中国交易所参数/交割公告**：只在实际发布后更新拥挤/保证金；本期不编仓位方向
- **2026-11-12｜宝钢股份临时股东大会（公开公司日历）**：若无经营/成本新增，仅公司治理事件，不计商品第三层

行动前检查：重新取得SC同源close/settle/near-next、M两腿实时深度、CU当前汇率/进口窗口、AG DXY/实际利率、EC运价/曲线；核Options具体腿；复查交易所当期保证金/限幅/最后交易日。未完成的检查不报通过。

## 事实台账（关键条目）

| fact_id | 标的/值/口径 | 观测/known_at | 支持判断 | 局限 |
|---|---|---|---|---|
| F-EOD-M-001 | M2701/M2705: close 3139/2839; settlement 3137/2831; close spread 300; settle spread 306 (EOD vendor table) | 2026-11-11 China EOD; 2026-11-11T19:15:00+08:00 | 近月相对强，晨间价差由285扩大至300 | OHLC不能证明晨间15分钟/回踩顺序；非官方接口独立核验 |
| F-EOD-SC-002 | SC2612: close/latest 604; alternate source 606; O/H/L 590/609.8/585.5; prev settle 609.1 (EOD public snapshots) | 2026-11-11 14:59:59 BJT; 2026-11-11T19:32:42+08:00 | 低开后修复但未明确站稳610 | 两点收盘源冲突，限制精确触发与PnL |
| F-EOD-CU-003 | CU2612/CU2701: 105820/104600; spread 1220 (EOD public snapshot) | 2026-11-11 China EOD; 2026-11-11T19:32:42+08:00 | 近月升水保持但高于旧入场区 | 当前主批缺失；成交/OI未获官方独立交叉核对 |
| F-EOD-AG-004 | AG2702: 12748; O/H/L 12523/12760/12280; prev settle 12739 (EOD vendor snapshot) | 2026-11-11 China EOD; 2026-11-11T19:32:42+08:00 | 早盘弱势被修复，晨间短空优势消失 | 不是交易所最终结算；路径顺序未知 |
| F-EOD-EC-005 | EC2612: 2513.5; +5.35% vs settle/+4.47% vs previous close (intraday vendor snapshot) | 2026-11-11 14:06 BJT; 2026-11-11T19:32:42+08:00 | 原空头趋势遭强反证 | 无最终官方结算、无当前曲线/运价实体 |
| F-EXT-OIL-006 | Brent/WTI: 92.77/86.80 (realtime) | 2026-11-11 09:34 GMT; 2026-11-11T17:34:00+08:00 | 油价从前日两月低位修复 | API原油库存据报道+9mbbl，官方EIA未发布 |
| F-EXT-PM-007 | spot gold/silver: 4051.31/52.87 (realtime) | 2026-11-11 09:16 GMT; 2026-11-11T17:16:00+08:00 | 贵金属反弹，银弹性更高 | 热CPI与鹰派利率仍为反证 |
| F-OPT-008 | China commodity options core: 45/64 products; coreATM0; skew22; surface/positioning/execution0 (T-1 sampled snapshot) | 2026-11-10; 2026-11-11T06:08:00+08:00 | 仅局部偏度可研究 | 无bid/ask、完整曲面、全链持仓或执行报价 |
| F-STOCK-009 | 601899.SH/600019.SH: stock trade_date 2026-11-09; minimum financial bundle 2 (repository facts) | 2026-11-09; 2026-11-10T08:40:19+08:00 | 铜矿/钢铁利润桥背景 | 陈旧且无当前tradability/quote；不作即时表达 |

## 旧观点修订

| idea_id | 原→现 | 原计划/观测 | 状态与理由 |
|---|---|---|---|
| COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111 | rev1→2；74→73 | 09:00回踩280—286→15m>=288→5m守284—288；止268；TP330/360；EOD spread300/settle306；OHLC不能证明顺序 | morning signal/fill unknown; evening future plan distinct；price repriced center upward; tighter future stop and higher targets apply only to new 21:00 candidate |
| COM-E-SC2612-DEESCALATION-FAILED-REBOUND-SHORT-20261109 | rev4→5；66→58 | 09:00反弹失败空；first print<598 abandon；day open590 and low585.5; abandon condition met | old short plan invalid; no fill/PnL inferred；price-path invalidation |
| COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106 | rev10→11；64→69 | entry only950—1050; no chase；EOD spread1220; LME proxy13815.5 | untriggered; thresholds unchanged; no chase；external support returned but price remains outside value zone |
| COM-M-AG2702-HOT-CPI-FAILED-REBOUND-SHORT-20261111 | rev1→2；64→50 | 09:00 rebound12330—12370, silver<=52, 15m<12330/retest fail; stop12590；AG close12748 and silver52.87 exceed invalidation/stop references | invalid/retired; no fill/PnL inferred；price and external reversal |
| COM-M-EC2612-CONTANGO-TREND-SHORT-20261106 | rev7→8；62→58 | conditional short/watch；EC2612 +4.47% vs previous close | old directional short thesis invalidated; no position assumption；second strong rebound and missing current curve/physical |

## 风险预算与发布校验

试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同主题合计≤2.5%—3.0%；M/CBOT、SC/Brent、CU/AG/紫金分别合并因子风险。无NAV与持仓账本，不编净敞口。规模公式：floor(NAV×预算比例/单手计划损失)。已重算分项、价差、好中坏净R与限幅压力；日历和旧参数语义已核。未解缺口：当前Futures主批0、Night明细空、无A/B basis、Options不可执行、SC收盘源冲突、股票当前交易状态未核。

## 来源

- [China-Commodities-Engine root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)｜观测:2026-11-11T19:03:55+08:00｜支持:current futures batch empty；critical errors and iFinD quota failure
- [Physical latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)｜观测:2026-11-11T19:10:05+08:00｜支持:18/20 series；all usable basis grades C/context only
- [External latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)｜观测:2026-11-11T19:12:37+08:00｜支持:17/22 context series；LME/COMEX/CBOT/BMD snapshots
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)｜观测:2026-11-11T06:04:09+08:00｜支持:historical session attribution；coverage 51.737% and 214 unresolved/query errors
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)｜观测:2026-11-10｜支持:45/64 products；sampled_strikes and zero bid/ask
- [DCE public contract table mirror](https://www.steelhome.com/detailspage.php?nid=4792009&ntype=n)｜观测:2026-11-11 EOD｜支持:M2701/M2705 OHLC/settlement/OI
- [SC2612 public quote](https://www.iweiai.com/hangqing/sc2612)｜观测:2026-11-11 14:59:59+08:00｜支持:SC2612 604 and OHLC
- [CU public exact contract quote](https://www.9qihuo.com/hangqing?productcode=cu)｜观测:2026-11-11 EOD｜支持:CU2612/CU2701 close, volume, OI
- [SHFE precious metals vendor table](https://quote.stockstar.com/gold/SHFE.shtml)｜观测:2026-11-11 EOD｜支持:AG2702 12748 and OHLC/OI/volume
- [EC2612 public quote](https://www.iweiai.com/hangqing/ec2612)｜观测:2026-11-11 14:06+08:00｜支持:EC2612 2513.5 and daily range
- [C2701 public quote](https://www.iweiai.com/hangqing/c2701)｜观测:2026-11-11 14:21+08:00｜支持:C2701 2188 and daily range
- [Reuters oil update](https://www.reuters.com/business/energy/oil-rises-two-month-low-hormuz-shipping-attacks-offset-iran-truce-hopes-2026-11-11/)｜观测:2026-11-11 09:34 GMT｜支持:Brent/WTI current prices；Hormuz risk；API reported stock build
- [Reuters precious metals update](https://www.reuters.com/world/india/gold-edges-higher-after-sharp-selloff-fed-hike-bets-weigh-2026-11-11/)｜观测:2026-11-11 09:16 GMT｜支持:gold/silver prices；hot CPI and hawkish rate counterevidence
- [EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/)｜观测:2026-11-11｜支持:official weekly petroleum report schedule
- [IEA events](https://www.iea.org/events)｜观测:2026-11-11｜支持:November OMR launch date
- [China-Stock-Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_inputs_latest.json)｜观测:2026-11-10T08:40:19+08:00｜支持:company evidence directory and capability counts
- [Zijin 2026 H1 report](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)｜观测:2026-08-22｜支持:mined copper/gold exposure and reported financials
- [Baosteel 2026 H1 report](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)｜观测:2026-08-22｜支持:steel/ore cost channel and reported financials

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：M2701/M2705顺序确认正套；SC2612重夺610且Brent/曲线共同确认。  
C. 今天继续观察：CU价差回落价值区、AG二次定价、EC下一日盘的运价与曲线确认。  
D. 今天必须回避或有条件退出：追M>304、追SC>614、追EC单日大涨、无bid/ask期权；旧SC/AG/EC方向若假设已建仓，严格按原失效处理。
