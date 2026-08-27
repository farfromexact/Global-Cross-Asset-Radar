---
report_date: 2026-08-27
edition: commodities_morning
generated_at_bjt: 2026-08-27T08:41:00+08:00
commodity_trade_date: 2026-08-26
commodity_data_fresh: true
commodity_history_record_count: 20
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-27

> **revision: 2**  
> **数据截点：** 2026-08-26完整EOD + 2026-08-26夜盘（对应2026-08-27交易日）正式snapshot。当前China-Commodities-Engine main在07:45错误尝试生成2026-08-27日线EOD并进入degraded状态，因此本版日线/Market State使用最后一个完整EOD commit `077a2dd8efea34e74cd0eece8d89eb96f7f41b57`，夜盘使用当前main正式snapshot。两层不混写。

## 一、今日一句话结论

**正式夜盘补齐后，V2701与FG701重新达到70+“只等反弹失败”的条件空标准；RM611仍只有价格强、curve不确认；EG继续是紧Backwardation中的去杠杆，能源整体不追空。今天没有开盘前立即市价仓。**

## 二、数据质量与覆盖说明

今晨China-Commodities-Engine出现一个必须显式降级的编排问题：当前main的`data/last_run_status.json`在07:45把`requested/trade_date`推进到2026-08-27，五所日线均返回0条，`data_fresh=false`、`full_market_ready=false`、critical errors=15；因此当前main的日线latest不能作为晨报EOD基线。

本版采用可审计的混合截面：**日线、1/3/5/20D、OI与EOD curve取2026-08-26最后完整快照commit `077a2dd...`**。该快照五所齐全、source-date match 100%、`full_market_ready=true`、critical errors=0。**夜盘取当前main的正式`data/night_session/latest.json`**：trading_date=2026-08-27、night_session_date=2026-08-26、607个有效夜盘合约、覆盖75.5915%、missing price/timestamp/query error均为0，validation passed。

这里还有一个重要口径：正式`night_return_pct`以**上一日结算价**为分母。为了判断“夜盘新增信息”，本报同时比较**夜盘收盘 vs 8月26日日盘收盘**；否则在日盘close与settle偏离很大时会夸大夜盘变化。

Physical今晨成功滚到requested_date=2026-08-27，但仍只有4/20映射；FG周度库存值7441.4，source_date=2026-08-21，属于native-frequency fresh绝对水平，不能伪装成昨夜库存变化。JM现货仍只作C级context。Options为2026-08-26 T-1：20,346合约、344 series、56/64产品，bid/ask coverage=0、execution_ready=false；只做IV/skew研究，不报权利金或滑点。

## 三、商品市场仪表盘

| 板块 | 合约 | 8/26 EOD close/settle | 正式夜盘close | 夜盘vs settle | 夜盘vs日盘close | 夜盘结构/线索 | 信号 |
|---|---|---:|---:|---:|---:|---|---|
| PVC | **V2701** | 4466 / 4497 | **4456** | -0.91% | **-0.22%** | 夜盘OI 127.97万，较EOD约+2.81%；V2702 4494，Contango约-0.85% | **72：反弹失败空** |
| 玻璃 | **FG701** | 898 / 905 | **898** | -0.77% | **0.00%** | 夜盘OI 168.50万，较EOD约+2.41%；FG702 940，Contango约-4.47% | **71：反弹失败空** |
| 菜粕 | **RM611** | 2314 / 2282 | **2327** | +1.97% | **+0.56%** | 夜盘OI 67.82万，约+1.03%；RM701 2351，仍Contango约-1.02% | **69：强势观察** |
| 乙二醇 | **EG2610** | 5168 / 5247 | **5136** | -2.12% | **-0.62%** | 夜盘OI 35.26万，较EOD约-6.25%；EG2611 4872，Back约+5.42% | **66：去杠杆/紧结构冲突** |
| 沥青 | **BU2610** | 4487 / 4506 | **4563** | +1.26% | **+1.69%** | BU2611 4335，Back约+5.26% | **68：能源反抽观察** |
| 燃油 | **FU2611** | 3622 / 3675 | **3714** | +1.06% | **+2.54%** | FU2612 3536，Back约+5.03% | **67：反抽，不追空** |
| 贵金属 | AG2610 | 16756 / 16670 | — | — | — | 美元PCE后偏强 | No-Trade |
| 有色 | CU2610 | 108750 / 108800 | — | — | — | 高位、海外库存迁移扭曲 | No-Trade |

## 四、相比原晨报真正发生了什么

**1. V/FG弱势得到正式夜盘价仓结构确认，但没有出现新的大幅价格延伸。** V夜盘相对日盘close只再跌约0.22%；FG夜盘close与日盘close相同。真正新增的信息是OI继续抬升，以及FG701-702 Contango扩大到约4.47%。所以交易升级的是“反弹失败后再空”的可信度，不是“开盘追空”的赔率。

**2. RM的+1.97%不能直接理解为昨夜又涨了2%。** 它是相对2282结算价；相对日盘2314收盘仅约+0.56%。夜盘量价和OI仍强，但RM611-RM701约-1.02% Contango，且repo没有菜粕Physical闭环，因此最高仍69分。

**3. EG这一次更像去杠杆，而不是新增空头趋势。** EG2610夜盘5136、较日盘close再跌约0.62%，OI却由约37.61万降至35.26万，降约6.25%；同时2610-2611仍有约5.42% Backwardation。价格弱、仓位降、curve紧三者冲突，最差的操作是继续追空或第一刀抄底。

**4. 能源夜盘发生反抽。** FU2611从日盘close 3622反弹至3714，BU2610从4487反弹至4563。Brent 8月26日仍收87.84、WTI 82.23，市场继续交易Hormuz谈判和替代物流；但Reuters同时指出航运约束仍在、成品油物流比原油更难恢复。因此能源是“双向尾部+均值回归”，不是干净空头。

**5. 宏观对贵金属仍不友好。** 美国7月PCE同比3.7%，高于预期，美元指数约99.1、接近八日高位；现货黄金8月26日约跌1.3%。Jackson Hole开始前，贵金属不值得用昂贵Vega抢方向。

## 五、产业链地图

| 产业链 | 当前方向 | 最强 | 最弱 | 核心解释 | 证据/置信度 |
|---|---|---|---|---|---|
| 地产建材 | 偏空但成熟 | — | V/FG | 价跌仓增+Contango；但低价与去库提高供给收缩反身性 | 中高 |
| 油料饲料 | 价格偏强 | RM | — | 日盘+夜盘price/OI强，curve仍Contango、Physical缺 | 中 |
| EG/聚酯 | 冲突 | curve/库存紧 | 最新价格 | Back仍深、价格与OI去风险 | 中 |
| 能源炼化 | 反抽/双向 | BU/FU夜盘 | 原油风险溢价 | 原油供应替代增加，产品物流瓶颈仍在 | 中 |
| 贵金属 | 事件等待 | — | AG短期赔率 | 美元/实际利率逆风，Jackson Hole待定 | 中 |

## 六、机会排行榜

| 排名 | 机会 | 总分 | 方向 | 持有期 | 阶段 | 工具 | 最大损失有限 |
|---:|---|---:|---|---|---|---|---|
| 1 | **V2701 反弹失败空** | **72** | 空 | 1–3D | 条件试仓 | 期货；fresh quote后Put Spread | 期货否 |
| 2 | **FG701 反弹失败空** | **71** | 空 | 1–3D | 条件试仓 | 期货；fresh quote后Put Spread | 期货否 |
| 3 | **RM611 强势但curve未确认** | **69** | 观察多 | 1–3D | Watch | 不预埋 | — |
| 4 | BU2610/FU2611能源反抽 | 68 | 观察 | Intraday–2D | Watch | 先看相对强弱 | — |
| 5 | EG2610 去杠杆后的双向观察 | 66 | 观察 | Intraday–2D | Watch | No pre-position | — |

今天仍没有80+确认交易。V/FG重新过70的原因只是正式夜盘让价仓/curve证据更完整；**由于位置已经很低，只有“反弹失败”这个入场形态才拥有足够赔率。**

## 七、前三名交易卡

### 1. V2701｜72分｜反弹失败空

- **核心事实：** 8/26 close/settle 4466/4497；1D约-1.73%、5D约-5.31%，EOD OI约+6.20%。夜盘4456，OI约127.97万、较EOD再+2.81%；V2702夜盘4494，Contango约0.85%。
- **市场可能错在哪里：** 高库存/弱需求仍未完全出清，但当前价格已经进入供给减产反馈区。
- **最合适表达：** 小V2701期货空；期权仅等fresh可执行quotes后研究Put Spread。
- **入场触发：** 09:00后至少30分钟。优先等**4480–4520反弹失败**，重新跌回4470/VWAP下方，先1/2；再破4445且OI不快速流失、Contango未明显收窄，再加1/2。若直接开在4440以下，不追，等45分钟。
- **失效条件：** 15分钟接受在4560上方；稳定站上4600，同时库存去化/下游订单持续改善、curve明显收窄，则逻辑失效。
- **止盈：** TP1 4400，TP2 4300；2–3个交易日不创新低退出。
- **风险：** 初始最大损失0.25%–0.35% NAV。DCE动态margin/price-limit本期metadata不完整，下单前终端复核。

### 2. FG701｜71分｜反弹失败空

- **核心事实：** 8/26 close/settle 898/905；EOD ΔOI约+9.08%。夜盘close仍898，但OI升至约168.50万、较EOD再+2.41%；FG702夜盘940，主次月Contango约4.47%。repo周度厂库7441.4，仍属高绝对水平，但不是昨夜新增库存。
- **市场可能错在哪里：** 需求改善预期仍可能过早，但900附近的冷修/供给收缩会限制追空凸性。
- **入场触发：** 等30分钟；**905–915反弹失败**并重新跌回900/VWAP下方先1/2；再破895且OI稳定、Contango仍深再加。直接低开<890不追。
- **失效条件：** 15分钟接受在922上方；930上方稳定+curve快速收窄/翻Back+库存去化加速则放弃。
- **止盈：** 880 / 850；时间止损3个交易日。
- **风险：** 0.25%–0.35% NAV。FG 20吨/手、tick 1元/吨；动态margin/limit正式下单前复核。

### 3. RM611｜69分｜强势观察，不预埋

- **核心事实：** 8/26 close/settle 2314/2282，EOD OI约+5.28%；夜盘2327、较日盘close仅+0.56%，OI约+1.03%；RM701夜盘2351，curve仍约1.02% Contango。
- **为什么不过70：** Price/OI连续两段偏强，但curve没有给短缺确认，repo又没有菜粕库存/进口Physical闭环。
- **升级条件：** 09:00后45分钟仍能守住2320–2327、突破2334且OI继续增加，同时611-701 Contango明显收窄；满足后再重新评分。
- **失效：** 跌回2300下方并形成接受，或高开后OI快速下降。
- **当前风险预算：** 0。

## 八、商品期权专项

8月26日链条为20,346合约、344 series、56/64产品；IV coverage约94.46%、OI coverage约67.19%，**bid/ask coverage=0、execution_ready=false、dealer gamma direction unknown**。因此今日所有期权结构只研究，不执行报价。

V/FG若标的触发空头，优先比较Put Spread而非裸Put；RM即使突破，也要先检查fresh skew是否已经把上行风险溢价买贵。禁止在零bid/ask情况下写净权利金、slippage或“dealer gamma squeeze”。

## 九、夜盘/开盘风险地图

| 品种 | 场景 | 置信度 | 条件与操作 |
|---|---|---|---|
| V2701 | 弱势延续但位置低 | 高 | 4480–4520失败才空；低开不追 |
| FG701 | 深Contango、价位极低 | 高 | 905–915失败才空；<890等45分钟 |
| RM611 | 高开风险 | 中高 | 45分钟后仍站2320并突破2334、curve收窄才升级 |
| EG2610 | 去杠杆+深Back | 高 | 不接第一刀、不追空；看5000–5150接受与Back变化 |
| FU/BU | 夜盘反抽 | 中高 | 先看Opening Range，不能沿用“能源单边空” |
| AG/CU | 美元事件约束 | 中 | Jackson Hole前降低追价与裸Vega |

## 十、未来24小时与7天事件

| 北京时间 | 事件 | 主要品种 | 处理 |
|---|---|---|---|
| 8/27–8/29 | Jackson Hole Symposium | AU/AG/CU/USD敏感品种 | 降低裸Delta/Vega，讲话后再重估 |
| 8/29 03:30附近 | CFTC COT | 贵金属/能源/农产品 | 只作滞后拥挤背景 |
| 8/31 09:30 | 中国8月官方PMI | 黑色/建材/有色 | V/FG空头事件前不满仓 |
| 9/2 22:30 | EIA Weekly Petroleum Status Report | SC/FU/BU/LU | 能源仓位保持事件余量 |
| 非定时 | Hormuz谈判、通航与替代装运 | 能源/航运 | 保持双向gap预算 |

## 十一、行动清单

**A. 可立即建立：** 无。

**B. 只挂条件单：** V2701反弹失败空；FG701反弹失败空。均禁止低开追价。

**C. 继续观察：** RM611能否在09:45后保持2320上方并让Contango收窄；EG2610的Back是否开始压缩；FU/BU反抽能否转为真正price/OI共振。

**D. 必须避免或退出：** 追空已经大跌的EG/FU；看到RM `night_return_pct +1.97%`就误以为昨夜新增上涨2%；低位追空V/FG；Jackson Hole前裸买高Vega贵金属；任何C/D级basis或context-only跨境价差“套利”。

## 风险预算与因子合并

V与FG同属地产/建材弱需求因子，两个条件仓若同时触发，初始合并最大损失建议≤0.60% NAV；单笔0.25%–0.35%。能源EG/FU/BU/SC/LU合并计算Hormuz/原油beta，不把多个品种当独立风险。今日没有80+确认交易，不使用0.75%–1.50%的确认仓预算。

## 数据与模型说明

事实层：8月26日完整EOD、正式8月26日夜盘OHLC/volume/OI、native-frequency Physical、Reuters/官方宏观。市场定价层：curve、price/OI、IV/skew。模型推导层：评分和条件触发。主观判断层：是否值得在当前价格承担风险。**期货curve不是spot basis；night_return_pct是相对EOD settlement，不等同于夜盘相对日盘close的新增涨跌。**

## 关键来源

- China-Commodities-Engine last good EOD status: https://github.com/farfromexact/China-Commodities-Engine/blob/077a2dd8efea34e74cd0eece8d89eb96f7f41b57/data/last_run_status.json
- Current degraded daily status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json
- Formal night session: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json
- Night-session status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json
- Physical: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json
- Options quality: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json
- Reuters Aug27 dollar/PCE: https://www.reuters.com/world/china/dollar-near-eight-day-high-us-data-lifts-fed-hike-bets-2026-08-27/
- Reuters Aug26 global markets/oil/gold: https://www.reuters.com/world/china/global-markets-wrapup-1-2026-08-26/
- Reuters Aug26 Aramco alternative Hormuz loading: https://www.reuters.com/business/energy/aramco-offers-more-oil-outside-hormuz-with-some-cargoes-heading-china-2026-08-26/
