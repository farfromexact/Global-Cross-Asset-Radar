---
report_date: 2026-08-29
edition: commodities_morning
generated_at_bjt: 2026-08-29T07:01:07+08:00
commodity_trade_date: 2026-08-28
commodity_data_fresh: true
commodity_history_record_count: 0
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-29

> **周末模式。** 中国最近完整EOD为2026-08-28；周五夜盘属于下周一交易日，只使用公开可验证行情并与EOD分开。海外层使用8月28日欧美收盘。当前China-Commodities-Engine的`report_input_latest.json`、`market_state_latest.json`、`data/latest.json`、`radar_history.json`和8月28日snapshot均为空，因此本期不输出伪造的3D/5D/20D同合约收益、z-score或ΔOI。

## 一、今日一句话结论

**今日商品期货期权无合格交易。周末休市且周五中国夜盘与海外宏观明显分歧；周一最接近触发的是JM回撤多、AG反弹失败空、SA反弹失败空，全部等待30—60分钟确认。**

## 二、数据质量与覆盖说明

第一读取层已检查`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。`report_input_latest.json`目前为空，因此按v2协议下钻。根状态显示2026-08-28 EOD已成功完成：SHFE、INE、DCE、CZCE、GFEX五所共803个期货合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0、unknown/duplicate/invalid OHLC/negative volume-OI均为0，placeholder=5并排除异常排行。核心期货本身可用。

但聚合发布层存在明显缺口：`market_state_latest.json`、`data/latest.json`、`radar_history.json`和`data/snapshots/2026-08-28.json`均为空。因此本期只使用`radar_latest.json`可验证的8月28日具体合约1D、Volume、OI与near-next curve；不把不同主力拼成历史，也不生成3D/5D/20D或z-score。FU2611的近次月曲线被仓库算成约42% Backwardation，明显属于合约选择/roll异常，本期不用于方向评分。

Physical requested_date=2026-08-28，20个目标仅4个映射、4个按原生频率fresh、0 stale、0 carried-forward。FG最新周度企业库存7404.9，较前周7441.4约-0.49%；TA周度加工费677.532元/吨，较前周586.52约+15.5%；JM仓库内NBS焦煤现货仍是8月20日旬度数据、basis质量C，只能作context。External仓库6/22映射，5 fresh、1 stale，但可用日频主要停在8月27，因此8月28海外收盘用Reuters/官方网页补充。

独立Options pipeline为2026-08-28：21,806个合约、370个series、成功61/64品种，IV coverage 98.59%、OI coverage 68.16%，但`surface_latest.json`为空，global `surface_ready=false`、`positioning_ready=false`、bid/ask coverage=0、`execution_ready=false`、dealer gamma direction unknown。因此不输出ATM IV、RR25、BF25、PCR、Dealer Gamma、具体strike、净权利金或滑点。

Contract metadata仍partial：DCE contract-info采集报错，多个动态margin/limit字段为空。前三张观察卡只引用交易所标准合约/最新找到的风险参数，周一下单前仍必须用交易所/终端重新核验动态保证金和涨跌停。

## 三、商品仪表盘

| 板块 | 合约 | 8/28 EOD | 周五夜盘/海外 | Volume / OI | Curve / Physical | 信号 |
|---|---|---|---|---:|---|---|
| 双焦 | **JM2701** | close/settle **1629/1623**，close +2.32% | 国内夜盘主力**涨超3%** | 1,039,129 / 597,545 | Back约**1.53%**；焦煤综合现货2097.8、日+29.1，但港口/焦企库存增加、钢厂库存下降 | **69：最接近多头触发** |
| 纯碱 | **SA701** | **1047/1027**，close +3.05% | 夜盘主力涨超2% | 1,902,641 / 1,154,367 | Contango约**3.41%**；周度产量、开工与厂家库存仍偏宽松 | **68：基本面空但价格拒绝下跌** |
| 原油 | **SC2610** | **596.5/592.3**，close +3.97% | 夜盘**614，+3.66%**；Brent周五结算**89.31，-0.43%** | 153,166 / 43,480 | Contango约1.37%；Hormuz仍有尾部风险但重开传闻压制外盘 | **59：境内外冲突，不追** |
| 贵金属 | **AG2610** | **17215/16818**，日盘close +3.15% | 沪银夜盘**-3.62%**；现货银约-3.5%至66.81美元/盎司 | 765,356 / 261,945 | 轻微Contango约0.14%；DXY升至99.69 | **69：反弹失败空观察** |
| 玻璃 | **FG701** | **927/918**，+2.32% | 夜盘涨超2% | 1,513,705 / 1,504,372 | Contango约2.67%；周度企业库存-0.49%但同比仍+18.35%，需求弱 | 挤空/预期交易，不追多也不旧逻辑追空 |
| PVC | **V2701** | **4578/4520**，+2.58% | 夜盘涨超3% | 1,061,521 / 1,214,734 | Contango约1.09%；Physical缺 | squeeze观察 |
| 碳酸锂 | **LC2701** | **159600/156000**，+4.77% | — | 239,379 / 391,884 | Contango约1.15%；仓单层有数据但方向闭环不足 | 高波动，不追涨 |
| PTA | **TA701** | **5630/5596**，+1.85% | — | 746,791 / 868,133 | Back约1.57%；周度加工费+15.5%，PTA负荷+4.4pp、社会库存-15.8万吨、聚酯负荷-3.1pp | **66：成本/curve多但供需混合** |
| 棉花 | **CF701** | **17180/17200**，+0.94% | — | 464,467 / 604,731 | Contango约1.64%；新疆高温干旱威胁单产 | **65：天气多观察** |
| 乙二醇 | **EG2610** | **5053/5030**，-0.47% | — | 1,240,902 / 349,408 | Back约4.16%；Physical映射缺 | 弱价格/紧curve冲突 |
| 燃料油 | **FU2611** | **3638/3670**，-1.33% | — | 1,041,002 / 227,418 | 仓库near-next出现异常超大Back，弃用 | 数据异常，不做curve交易 |

> 曲线均为期货近月—次近月结构，不等于现货基差；当前没有可进入评分的A/B级高质量basis。

## 四、相比上一交易日真正变化

**1. 昨晨第一名SA701空头被价格直接否决。** 昨晨评分78的“失败反弹空”建立在宽松供需、Contango和弱价格上，但周五SA701收1047、日内+3.05%，周五夜盘又涨超2%。与此同时，纯碱周度厂家库存仍约187.27万吨、环比+1.51%，产量约76.62万吨、环比+2.72%。这意味着“基本面空”仍在，但**价格拒绝交易这个空头**。因此今天把SA从78降到68，除非周一先出现明确失败反弹，否则不再提前做空。

**2. JM2701延续上涨，但实体确认从“偏多”变成“混合”。** 周五JM2701收1629、+2.32%，近端Back扩大到约1.53%，夜盘主力再涨超3%。焦煤综合现货指数升至2097.8、日+29.1；但16港进口焦煤库存周增46.57万吨、独立焦企炼焦煤库存周增13.87万吨，而钢厂炼焦煤库存下降。价格+curve两层很强，Physical却不能干净计为第三层，所以从昨晨75降到证据上限69，周一只看回撤确认，不追夜盘涨幅。

**3. SC出现最明显的境内外定价冲突。** 周五SC2610日盘已+3.97%，夜盘又+3.66%收614；但Brent周五结算89.31美元/桶、下跌0.43%，WTI 83.40、下跌0.16%。Reuters报道Hormuz重开传闻与Fed偏鹰共同压制油价，但伊朗方面仍强调限制没有解除。SC的境内风险溢价可能有合理原因，也可能在周末消息缓和后被快速压缩；没有exact-contract进口平价就不能把这个价差称为套利。

**4. 贵金属从“事件等待”变成宏观冲击后的两层空头观察。** Warsh在Jackson Hole偏鹰，9月加息定价迅速升至约58%；美元指数升至99.69。现货黄金周五跌约3%至4567.23美元/盎司，白银跌约3.5%至66.81；中国夜盘沪金-2.65%、沪银-3.62%。这是目前最干净的跨市场负面增量，但只有中国价格层+海外宏观/价格层两层，按纪律最多69分，周一不追低开。

**5. FG/V的上涨更像“预期/挤空”而不是实体短缺。** FG周五+2.32%、夜盘又涨超2%，V周五+2.58%、夜盘涨超3%；但FG最新周度库存虽降0.49%，同比仍高18.35%，现货与终端需求偏弱，且FG/V仍是Contango。旧空头应退出/停止加仓，但也不能把涨价自动解释成需求拐点。

**6. 数据仓的核心EOD已恢复，但统一报告层没有恢复。** 8月28五所EOD是完整的；真正的问题转成`report_input`、Market State、history/snapshot发布为空。因此今天不再回退到8月27数据，但必须牺牲3D/5D/20D、z-score和ΔOI等二阶判断。

## 五、产业链地图

| 产业链 | 当前方向 | 最强/最弱 | 价格与curve | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 双焦—钢材 | 盘面偏多、基本面混合 | 强JM/J；RB/HC跟涨较弱 | JM价涨+Back | 现货涨；港口/焦企库存增，钢厂库存降 | 铁水/利润/补库连续性 | 中 |
| 纯碱—玻璃 | 强反弹但供需不确认 | 强FG/SA盘面 | SA/FG均Contango | SA库存/产量高；FG小去库但库存同比高 | 订单、检修兑现、高质量basis | 中低 |
| 原油—燃料油 | 地缘高波动、境内外分化 | 强SC / 弱外盘油价 | SC涨而curve仍Contango | Hormuz双向headline | exact parity、裂解、周末船流 | 中低 |
| 贵金属 | **宏观转空** | 弱AG/AU | 中国夜盘已大跌 | Warsh偏鹰、美元与收益率上行 | 期权surface、周日晚外盘确认 | 中高 |
| 油脂/棉花 | 天气与国内risk-on | CF有天气凸性 | CF/Y仍Contango | 新疆天气风险；BMD棕榈repo stale | ICE/CBOT/BMD新鲜映射 | 中低 |

当前regime：**中国周五工业品risk-on/挤空，与Warsh偏鹰后的全球美元走强和贵金属去风险并存；SC存在显著境内风险溢价；周末headline风险高于趋势信息。**

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

| Rank | 机会 | Score | Fresh层 | 方向 | 阶段 | 工具 | 数据惩罚 |
|---:|---|---:|---:|---|---|---|---|
| **1** | **JM2701 回撤确认多** | **69** | 2 | 多观察 | Watch | JM2701期货 | Physical库存信号混合；周五夜盘已过度延伸 |
| **2** | **AG2610 反弹失败空** | **69** | 2 | 空观察 | Watch | AG2610期货；期权仅研究 | 宏观冲击已在夜盘一次性定价；无surface |
| **3** | **SA701 反弹失败空** | **68** | 2 | 空观察 | Watch | SA701期货 | Price层强烈反向；基本面空不等于马上空 |
| 4 | TA701 成本/curve多 | **66** | 2 | 多观察 | Watch | TA701 | PTA供应回升、聚酯负荷下降，Physical混合 |
| 5 | CF701 天气多 | **65** | 2 | 多观察 | Watch | CF701 | Contango；缺ICE/高质量basis/仓单方向闭环 |

没有任何候选达到≥3个干净fresh独立层，因此没有70+试仓资格，更没有80+确认交易。

## 七、前三名交易卡（均为观察卡，周一需重新评分≥70才允许试仓）

### 1. JM2701｜回撤确认多｜69

- **事实：** 8/28 close/settle 1629/1623，Volume 103.9万手、OI 59.75万手，近端Backwardation约1.53%；周五夜盘主力涨超3%。Mysteel焦煤综合现货2097.8、日+29.1，但港口进口焦煤库存+46.57万吨、独立焦企炼焦煤库存+13.87万吨，钢厂炼焦煤库存下降。
- **市场可能错在哪里：** 若下游利润和补库比港口库存更快改善，市场可能仍低估近端紧张；反之，当前涨幅也可能只是高beta补涨。
- **证据层：** Price/volume + Curve共2层；Physical混合，不计第三层。
- **最佳表达：** 周一仅在回撤后用JM2701期货试探；若期权surface/quote恢复，可研究Call Spread，不给strike/权利金。
- **入场：** 09:45后再评。若周一开盘相对周五结算涨幅≥3%，当日不追；若先回吐夜盘涨幅、仍守住周五收盘1629附近并重新站上首30分钟VWAP，同时OI增加且Back保持>1%，才可重新评分。
- **分批：** 重新评分≥70后1/3起步；突破首小时高点且OI继续增再加1/3；没有Physical改善不加满。
- **初始止损：** 30分钟接受在1600下方。
- **逻辑失效：** 1590下方稳定 + curve压平/转Contango + 现货涨势停止且港口/焦企库存继续累积。
- **TP1 / TP2：** 1700 / 1750；2个交易日不创新高时间止损。
- **风险预算：** 当前0；若周一重评≥70，单笔最大损失0.25%—0.35% NAV。
- **合约参数：** DCE标准交易单位60吨/手，tick 0.5元/吨，tick value 30元/手；按1629计名义约97,740元/手。标准最低保证金5%、标准涨跌停±4%，但**当前动态保证金/限幅未确认**；最后交易日为交割月第10个交易日，实物交割。当前metadata未确认精确夜盘时段。按标准4%仅作压力敏感度：单个不利停板约3,910元/手，两个连续4%复合约7,976元/手；这不是周一实际限幅预测。
- **roll/delivery：** 2701离交割尚远，无立即roll压力；进入12月后再显著提高交割/限仓权重。

### 2. AG2610｜反弹失败空｜69

- **事实：** 8/28日盘close/settle 17215/16818，日盘close +3.15%；随后沪银夜盘-3.62%。Reuters：现货银周五约-3.5%至66.81美元/盎司，黄金约-3%，DXY升至99.69，Fed 9月加息概率约58%。
- **市场可能错在哪里：** 如果Warsh冲击不是一次性repricing，而是利率路径真正上移，贵金属前期拥挤多头可能继续去杠杆；但周一直接低开会使追空赔率恶化。
- **证据层：** 中国夜盘Price + 海外宏观/价格共2层；轻微Contango不足以作为第三个方向层。
- **最佳表达：** 周一只做AG2610失败反弹空；期权只能在人工拿到可执行报价后研究Put Spread。
- **入场：** 先看周日外盘重开。若周一中国开盘低开>2.5%，不追；等45分钟反弹，无法站回首45分钟VWAP且海外银仍弱、DXY维持约99.5以上，才重新评分。
- **分批：** ≥70后1/3；跌破首小时低点再加；美元继续走强才允许第二次加仓。
- **初始止损：** 首45分钟高点上方约0.6%，或30分钟重新站稳周五结算16818上方，取更紧者。
- **逻辑失效：** DXY跌回约99.2以下且海外银强力收复Warsh后跌幅，同时沪银重新接受在周五结算上方。
- **TP1 / TP2：** 从实际触发价-2% / -4%；1—2个交易日时间止损。
- **风险预算：** 当前0；重评≥70后0.25%—0.35% NAV。
- **合约参数：** SHFE白银15千克/手，tick 1元/千克，tick value 15元/手，按结算16818计名义约252,270元/手；实物交割，最后交易日通常为交割月份15日。交易所最新明确检索到的贵金属调整通知为涨跌停14%、一般持仓保证金16%，**周一必须重新核验是否有更新**；夜盘交易至02:30。若仍按14%仅作压力敏感度：一个不利停板约35,318元/手，两个连续14%复合约75,580元/手。

### 3. SA701｜失败反弹空｜68

- **事实：** 8/28 close/settle 1047/1027，日盘close +3.05%，近端Contango约3.41%，周五夜盘主力再涨超2%；最新产业口径仍显示纯碱产量和厂家库存处于高位/上升状态。
- **市场可能错在哪里：** 市场可能在提前交易9月检修、亏损减产和政策beta；若这些预期无法兑现，宽松基本面最终会重新主导。但在价格确认前，逆势空就是和市场争论。
- **证据层：** Curve + Physical共2层；Price层反向，不计入空头确认。
- **最佳表达：** 只在周一squeeze失败后用SA701期货；Put Spread仅研究。
- **入场：** 等45分钟。只有反弹/高开失败、重新跌破1047和首45分钟VWAP，且Contango仍>3%、产业数据没有改善，才重新评分；若持续站稳1060上方，放弃当日做空。
- **分批：** ≥70后1/3；跌破1025且OI重新扩张再加；不在1000附近追空。
- **初始止损：** 首小时高点上方约1%。
- **逻辑失效：** 日盘稳定在1080上方 + Contango收窄至约1.5%以下 + 后续周度库存开始下降/检修兑现。
- **TP1 / TP2：** 1020 / 980；2个交易日不回落则退出。
- **风险预算：** 当前0；重评≥70后0.25%—0.35% NAV。
- **合约参数：** CZCE纯碱20吨/手，tick 1元/吨，tick value 20元/手，按1047计名义约20,940元/手；标准最低保证金5%、标准涨跌停±4%，最后交易日为交割月第10个交易日、实物交割。动态保证金/限幅和精确夜盘时段本次metadata未确认，周一前核验。按标准4%仅作压力敏感度：一个不利停板约838元/手，两个连续4%复合约1,709元/手。

## 八、商品期权专项

Options raw chain本身已更新到8月28，但**surface不是ready**：21,806合约、370 series、61/64产品，IV coverage约98.59%，OI coverage约68.16%，bid/ask coverage=0，positioning/execution均不ready，Dealer Gamma方向未知。`surface_latest.json`为空，因此不能声称“全市场最高/最低IV”，不能比较ATM IV-RV，也不能输出RR25/BF25或具体执行价。

如果周一人工报价和surface恢复，研究优先级依次为：**AG失败反弹后的Put Spread、JM回撤确认后的Call Spread、SA失败反弹后的Put Spread**。所有结构均为research only; manual quote and manual confirmation required before execution; no premium quoted。禁止裸卖事件Vega，禁止根据不完整OI推断dealer positioning。

## 九、周一9:00开盘风险地图

| 品种 | 周末前状态 | 周一最大风险 | 操作 |
|---|---|---|---|
| **JM2701** | 日盘+2.32%，夜盘>3% | 高开后获利回吐；Physical混合 | **等45—60分钟**，高开≥3%直接不追 |
| **SA701** | 日盘+3.05%，夜盘>2% | 基本面空与squeeze冲突 | 等45分钟；只有重新失守1047/VWAP才考虑空 |
| **FG701/V2701** | 日夜盘连续强 | 空头挤压延续，也可能快速回吐 | 不旧逻辑追空，不突破追多；等首小时OI/curve |
| **SC2610** | 夜盘614、+3.66%，Brent周五却-0.43% | 周末Hormuz消息令境内溢价gap fade | **至少等60分钟**；无exact parity不做跨市场套利 |
| **AU/AG** | 中国夜盘已大跌，外盘同步 | 低开追空赔率差 / 周日外盘反抽 | 先看周日重开，等45分钟反弹失败 |
| **CF701** | 日盘偏强、天气风险 | 天气headline与Contango冲突 | 等30—45分钟；只有curve改善才升级 |

周六没有中国9:00交易，本表专门用于8月31日周一开盘。

## 十、未来24小时 / 7日事件

| 北京时间 | 事件 | 主要品种 | 处理 |
|---|---|---|---|
| 周末随时 | Hormuz/Iran制裁、通航与谈判headline | SC/LU/FU/BU/PG | 能源隔夜gap风险最高；不留裸方向过量风险 |
| 8/31 上午 | 中国官方8月制造业PMI；Reuters调查中值约49.6、前值49.2 | 黑色、有色、化工 | 若仍<50，警惕工业品周五risk-on回吐；等数据后再加Delta |
| 9/1 04:00 | USDA Crop Progress（8/31 16:00 ET） | C/CF/豆类 | 天气/优良率事件，用有限风险而非追gap |
| 9/2 22:30 | EIA Weekly Petroleum Status Report | SC/Brent/WTI/FU/BU | 观察原油与成品油库存是否继续分化 |
| 9/4 20:30 | 美国8月非农 | AU/AG/CU/原油/美元 | 降低事件前裸Vega与重复美元因子 |
| 9/5 03:30左右 | CFTC COT常规周五发布（数据通常截至周二） | 金银、原油、农产品 | 只作拥挤背景，不推断最终客户方向 |

## 十一、风险预算与因子合并

今天周末且没有70+，**新增风险预算=0**。周一任何候选只有重新达到≥70后才允许0.25%—0.50% NAV试仓；没有第四个独立fresh层，不允许升级到确认仓。黑色同因子JM/J/RB/HC合计试仓风险≤0.75% NAV；贵金属美元/实际利率因子≤0.50%；能源Hormuz因子≤0.50%；SA/FG/V地产—化工squeeze因子≤0.75%。

压力测试必须覆盖：一个/两个实际涨跌停、周末gap、相关性断裂、保证金上调、人民币急变、海外周日开盘跳空、期权IV跳升/塌陷。当前Options execution false，因此不允许用“有限风险”标签掩盖没有报价的结构。

## 数据与模型说明

事实数据、市场定价、推断和主观判断已分开。8月28 EOD来自China-Commodities-Engine；周五夜盘来自公开行情；8月28海外收盘来自Reuters/官方。Market State和history artifact为空，因此不提供伪历史。Price/OI quadrant只应视为归因线索；本期因ΔOI artifact缺失，甚至不使用该归因。C/D级basis不参与评分，BMD palm stale不参与评分。

## 关键来源

- [China-Commodities-Engine](https://github.com/farfromexact/China-Commodities-Engine)
- [Reuters：Gold drops 3% as Warsh comments lift rate hike bets](https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/)
- [Reuters：Dollar jumps after Warsh comments](https://www.reuters.com/world/asia-pacific/dollar-flat-near-one-week-high-investors-await-warshs-jackson-hole-debut-2026-08-28/)
- [Reuters：Oil settles lower on Fed/Hormuz signals](https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/)
- [Reuters：中国8月制造业PMI调查](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/)
- [Reuters：中国作物高温/洪涝风险](https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/)
- [经济观察网：8月28日国内期货夜盘](https://www.eeo.com.cn/2026/0828/1015243.shtml)
- [财联社：SC2610、沪金沪银8月29日凌晨夜盘收盘](https://m.cls.cn/detail/2468396)
- [Mysteel：8月28日煤焦数据](https://coal.mysteel.com/article/pa5157%2C5153aaaaaa1.html)
- [同花顺期货通：8月28日玻璃收评](https://goodsfu.10jqka.com.cn/20260828/c679388565.shtml)
- [同花顺期货通：8月28日PTA收评](https://goodsfu.10jqka.com.cn/20260828/c679388637.shtml)
- [DCE焦煤/焦炭Factsheet](https://www.dce.com.cn/dce/file/2026-01-15/17684624156122c9a882b9ae6dcbb289019bc092f6fc1681.pdf)
- [SHFE交易时间](https://www.shfe.cn/services/calenderandholidays/tradinghours/)
- [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [BLS August 2026 Employment Situation schedule](https://www.bls.gov/CPS/)
- [USDA Crop Progress](https://esmis.nal.usda.gov/publication/crop-progress)

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：没有；周一JM2701、AG2610、SA701均需先重新评分≥70，当前不预埋。**  
**C. 今天应继续观察的机会：JM回撤多、AG反弹失败空、SA反弹失败空、TA成本/curve多、CF天气多，以及SC境内外溢价是否收敛。**  
**D. 今天必须避免或退出的交易：继续执行旧SA空头、追JM/FG/V周五夜盘强势、追低空AU/AG、追高SC，以及任何基于空surface/零bid-ask的精确商品期权交易。**
