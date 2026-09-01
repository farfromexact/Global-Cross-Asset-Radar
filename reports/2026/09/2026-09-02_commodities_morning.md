---
report_date: 2026-09-02
edition: commodities_morning
revision: 1
generated_at_bjt: 2026-09-02T07:00:24+08:00
commodity_trade_date: 2026-09-01
commodity_data_fresh: true
commodity_history_record_count: 0
archive_status: pending
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-02

> **数据截点：** 中国基线为2026-09-01完整五所EOD；中国夜盘仅使用公开媒体可验证行情，与EOD结算严格分开；海外层使用截至今晨可验证的9月1日美欧收盘。`report_input_latest.json`、`market_state_latest.json`和`options/surface_latest.json`当前为空；按v2优先级下钻module-specific数据，且不把T-1 options当作今日fresh evidence。

## 一、今日一句话结论

**今天有一个80+确认但仍需触发的机会：BU2610回撤承接多；EG2610、SC2610为次级条件多。能源与化工已经连续急涨，9:00严禁追高，优先等30—60分钟回撤与curve确认。**

## 二、数据质量与覆盖说明

第一读取层已读取`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。`report_input_latest.json`当前为空，因此按v2协议下钻。最近完整中国EOD为2026-09-01：SHFE、INE、DCE、CZCE、GFEX五所均fresh，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，unknown/duplicate/invalid OHLC/negative volume-OI均为0；placeholder=3，不进入异常排行。

独立`market_state_latest.json`仍为空，故本期不新生成3D/5D/20D、RV20、volume/OI z-score或ΔOI z-score；上一晚间报告中的多周期指标只作为上一revision比较背景，不冒充当前module-specific产物。near-next curve只是期货期限结构，不等于现货基差；当前没有A/B级闭环basis进入套利或方向评分。

Physical module-specific文件`requested_date=2026-09-01`，20个目标仅4个映射、4个按原生频率fresh、0 stale、0 carried-forward：I港口库存、JM旬度焦煤现货、FG周度企业库存、TA周度加工费。BU/EG/MA没有仓库Physical映射，本期仅使用有日期与口径的公开产业资料，并严格区分仓单、炼厂库存、港口库存与社会库存。

External module 6/22映射，其中Brent、SGX铁矿、USDCNH、DXY fresh，LME铜与BMD棕榈油stale；stale不计分。Brent仓库日频为8月31日90.49美元/桶，只作背景；隔夜9月1日海外价格由Reuters更新。

Options trade_date=2026-09-01：23,200个合约、387个series、64/64产品，quality文件标记`surface_ready=true`，但具体`data/options/surface_latest.json`为空；按module-specific优先级，当前报告把surface视为不可验证。OI coverage 68.09%、bid/ask coverage=0、positioning/execution均not ready、dealer gamma方向未知。并且今天已进入9月2日中国交易日，所以9月1日options只能作T-1背景，不计今日fresh evidence；不输出ATM IV、RR25、BF25、PCR、Dealer Gamma、具体strike、权利金或滑点。

Contract metadata仍partial：DCE contract-info JSON解析失败；SHFE/INE/CZCE核心规则可读。前三名交易卡对无法确认的动态保证金/限幅直接标“参数未确认”，不拿旧参数填补。

## 三、商品市场仪表盘

| 板块 | 合约 | 9/1 EOD close/settle | 1D | Volume | OI | curve/Physical | 可验证夜盘/海外 | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 能源 | **BU2610** | **4934 / 4904** | **+4.18% close** | 438,708 | 238,945 | **Back约4.00%**；54家厂库57万吨、周降5.6%，9月地方炼厂排产同比低43.6% | 21:00开盘约+1.86%；Brent +4.6% | **82：回撤承接多** |
| 化工 | **EG2610** | **5525 / 5481** | **+6.37% close** | 1,598,891 | 334,485 | **Back +3.36%**；华东主港14.2万吨、周降3.6万吨 | 23:00公开夜盘+2.68% | **79：回撤承接多** |
| 原油 | **SC2610** | **637.8 / 637.2** | **+3.15% close** | — | — | 前一晚间审计Back约4.32%，但有roll flag；实际Hormuz航运受扰 | **夜盘687.7，+7.93%；Brent 94.65** | **78：只等深回撤** |
| 化工 | **MA610** | **3069 / 3044** | **+5.43% close** | 2,370,930 | 664,801 | Backwardation；港口库存窄幅累库，MTO偏弱，伊朗进口受扰 | 23:00公开夜盘涨超1% | **77：条件多** |
| 油脂饲料 | M2701 | 3377 / 3357 | settle约+0.12% | 1,830,938 | 2,826,855 | 近端轻Contango；无可验证CBOT exact parity | 夜盘豆粕+1.52% | 68：低噪声趋势观察 |
| 建材 | FG701 | 969 / 953 | settle约+1.38% | — | 1,352,049 | Contango约1.09%；周度企业库存7404.9 | 夜盘玻璃+1.68% | squeeze，不追 |
| PTA | TA701 | 5930 / 5904 | +3.17% close | 1,059,477 | 996,593 | Backwardation；最新周度加工费677.532元/吨 | — | 67：成本/curve观察 |
| 黑色 | I2701 | 726.5 / 722 | +0.14% close | — | 577,319 | Backwardation；港口库存仅周度context | — | 64：curve强、price弱 |
| 贵金属 | **AG2610** | 16245 / 16259 | -2.54% close | 466,603 | 232,963 | 轻Back；实际利率/美元压制 | **夜盘15749，-3.14%；海外银-2.9%** | 68：不追空，只等失败反弹 |
| 新能源 | PS2611 | 38000 / 37595 | +3.22% close | 108,644 | 117,273 | Contango；实体层不足 | — | 高波动观察 |
| 畜牧 | LH2611 | — | -2.67% close | 180,401 | 228,933 | Contango；无fresh实体闭环 | — | 弱势但不列交易 |

## 四、相比上一交易日/上一revision真正变化

**1. BU从昨晚78分升级到今天82分，原因不是“又涨了”，而是第三、第四层证据变得更硬。** 9月1日BU2610 close 4934、settle 4904，期限结构约4% Back；产业数据显示截至8月31日54家炼厂库存57万吨、周降3.4万吨/5.6%，开工回落，9月地方炼厂排产87.9万吨、同比下降43.6%。同时Brent周二结算94.65美元/桶、+4.6%，WTI 90.22、+5.2%，两艘装载沙特原油的VLCC在Hormuz遇袭。Price/curve/Physical/External四层同向，满足80+的证据门槛；反方是需求改善仍有限、昨日已涨、夜盘容易高开过度。

**2. EG仍然强，但从“最干净”降为第二。** 9月1日EG2610 close 5525、settle 5481，近端Back约3.36%，夜盘公开收盘再涨2.68%。华东主港库存14.2万吨、周降3.6万吨支持近端紧张；但国内装置周产量与开工正在回升，且两日累计涨幅已很大。因此不把深Back等同于无条件短缺，评分79。

**3. SC的方向更对、交易却更差。** 周二Brent/WTI大涨，Iran实际装船已从3月约200万桶/日降至8月约22万—25.5万桶/日，Hormuz船运攻击证明供给风险正在从headline转为actual flow。中国SC2610夜盘更直接冲到687.7、+7.93%。这确认了上行逻辑，却显著恶化追涨convexity；SC只能等深回撤，不能因基本面更强而把仓位做得更大。

**4. MA继续受益于伊朗进口风险，但实体层仍混合。** MA610日盘+5.43%、Backwardation，夜盘继续涨超1%；供应端受Hormuz/伊朗扰动，沿海现货和基差走强，但港口库存此前周增1.86万吨、MTO开工偏弱。因此Physical不算完整第三票，只有Price/Curve/External三层明确。

**5. 贵金属出现“地缘不再是避险利多”的重要状态。** 现货黄金周二跌超2%至约4342美元/盎司，白银跌2.9%，DXY升至99.68，美国10Y一度约4.80%；中国夜盘沪金-2.07%、沪银-3.14%。当前边际主导变量是油价→通胀→收益率/美元，而不是传统safe-haven。方向偏空，但第一段已走完，不追低。

**6. 宏观并没有给“中国全面工业牛市”绿灯。** RatingDog中国8月制造业PMI升至51.5，输出、新订单和出口订单改善；美国ISM制造业仍在54.6扩张，但低于7月，JOLTS 727.1万显示招聘仍偏弱。更合理的regime是“供应冲击主导的能化多头”，不是需求全面再加速。

## 五、产业链地图

| 产业链 | 当前方向 | Price/Curve | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| **原油—沥青** | **偏多** | BU强+深Back | 炼厂库存去化、供给低；Brent/WTI与Hormuz同向 | 终端道路需求、动态风控参数 | **高** |
| **EG—聚酯** | 偏多 | EG强+Back | 港库极低；国内增产是反方 | 聚酯订单、A/B basis | 中高 |
| **原油—SC** | 方向强/赔率差 | SC夜盘极强 | Iran出口/船流受阻、油价大涨 | exact parity、gap后的承接 | 中高 |
| **MA—MTO** | 偏多/事件敏感 | MA强+Back | 伊朗供应风险 vs 港口累库/MTO偏弱 | 精确船期与MTO复产 | 中高 |
| **贵金属—利率** | 偏空 | 中国金银弱 | DXY/美债收益率压制 | 当前T日surface、资金流 | 中 |
| **中国工业beta** | 分化 | RatingDog PMI扩张 | 需求改善但非全面强 | 多品种Physical覆盖 | 中 |

当前regime：**Hormuz实际供给/航运冲击进入第二轮，能化从“买headline”转向“买有本地库存/期限结构确认的品种”；同时油价推高通胀与实际利率，压制贵金属。**

## 六、机会排行榜

| 排名 | 机会 | 总分 | 方向 | 持有期 | 阶段 | Fresh层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| **1** | **BU2610 回撤承接多** | **82** | Long | 1–5D | confirmed_wait_trigger | **4** | 已连续大涨；终端需求不强；动态限幅/保证金未确认 |
| **2** | **EG2610 回撤承接多** | **79** | Long | 1–3D | conditional_trial | **4** | DCE metadata错误；国内供应回升；两日涨幅过大 |
| **3** | **SC2610 深回撤承接多** | **78** | Long | Intraday–2D | conditional_trial | **4** | 夜盘+7.93%；roll/OI风险；gap与外交反转风险极高 |
| **4** | **MA610 回撤承接多** | **77** | Long | 1–3D | conditional_trial | **3** | Physical混合；MTO偏弱；港口库存曾累库 |
| 5 | **AG2610 失败反弹空** | **68** | Short | Intraday–2D | watch_only | 2 | 已连续下跌；地缘尾部仍可能触发避险反转 |

80+不是“9:00直接市价买”。BU只是从“试仓候选”升级成“确认逻辑、等待价格触发”；若开盘gap使赔率消失，仍然不做。

## 七、前三名交易卡

### 1. BU2610｜82｜回撤承接多

- **事实：** 9/1 close/settle 4934/4904，EOD约+4.18%/+3.55%，curve约+4.00% Back；炼厂库存周降5.6%，9月地方炼厂排产同比低43.6%；Brent/WTI隔夜+4.6%/+5.2%。
- **市场可能错在哪里：** 市场可能仍把BU当简单crude beta，而低炼厂库存、低开工和旺季施工使本地near-term tightness更强；反面是高油价会抑制终端需求，且地缘降级会瞬间打掉成本溢价。
- **Fresh层：** 1价格/持仓；2期限结构；3实体供需；4海外/宏观。Options为T-1，不计。
- **最佳表达：** BU2610 futures；期权仅研究，不给可执行报价。
- **入场：** 9:00后等30—45分钟。若高开，优先等回撤到**4970—5020**区域或首30分钟VWAP附近出现承接，再重新站回VWAP/首30分钟中枢；若直接>5050且无回撤，不追。
- **分批：** 1/3初始；突破首45分钟高点且Brent仍>93.5、BU curve未明显收窄再加1/3；最后1/3必须等下一EOD仍有curve/库存确认。
- **初始止损：** 30分钟接受在**4900以下**。
- **逻辑失效：** BU跌破**4850**且Brent回到92以下，或BU Back快速压到1%以下/转Contango，或供应/库存明显反转。
- **TP1/TP2：** 5100 / 5250；**时间止损：** 1–5D，不延续则减仓。
- **最大损失：** 0.50%–0.75% NAV；若同时持有EG/SC/MA必须合并能源因子。
- **合约参数：** 10吨/手；tick 1元/吨；tick value 10元/手；按4934名义约49,340元/手。当前临时涨跌停/交易保证金**参数未确认**；broker margin未确认。实物交割；最后交易日规则需按BU合约月份官方日历复核，短线必须在交割风险前退出。
- **1/2涨跌停压力：** 因当前动态limit未确认，不虚构具体金额；开仓前必须用交易所/终端实时参数重算。
- **最坏情景：** 周中外交降级+油价跳空下跌+保证金上调，BU跟随成本端快速反转。

### 2. EG2610｜79｜回撤承接多

- **事实：** 9/1 close/settle 5525/5481，close +6.37%，curve Back +3.36%；华东主港库存14.2万吨、周降3.6万吨；公开夜盘再涨2.68%。
- **市场可能错在哪里：** 低港库/进口约束可能让近月紧平衡持续更久；反面是国内装置复产、产量上升，聚酯需求若出现负反馈，深Back可快速压缩。
- **Fresh层：** 1价格；2curve；3Physical；4External。因DCE contract metadata错误，评分停在79。
- **入场：** 9:00后等30—45分钟；优先等gap回吐，**不跌破9/1 close 5525并重新站回首30分钟VWAP**再1/3。若开盘继续急拉>5700，不追。
- **加仓：** 首小时新高且Back仍>2.5%再加；不因夜盘强自动加仓。
- **止损：** 30分钟接受在5480以下。
- **失效：** 5400以下 + Back<1.5% + 港库/进口开始正常化。
- **TP1/TP2：** 5750 / 5900；时间止损2–3D。
- **最大损失：** 0.35%–0.50% NAV。
- **合约参数：** 静态10吨/手、tick 1元/吨、tick value 10元/手；按5525名义约55,250元/手。DCE动态保证金、price limit、确切交割/最后交易日参数当前**未确认**，开仓前必须终端核验；因此停板压力损失不填假值。

### 3. SC2610｜78｜深回撤承接多

- **事实：** 9/1 EOD close/settle 637.8/637.2；公开夜盘收**687.7，+7.93%**。Brent周二结算94.65、+4.6%，WTI 90.22、+5.2%；Hormuz油轮遇袭，Iran实际出口装船大幅下降。
- **市场可能错在哪里：** 供应冲击持续时间可能仍被低估；但中国夜盘已经把大量右尾一次性买进，若外交降级或通航改善，回吐速度也会最大。
- **Fresh层：** 1价格；2curve背景；3实际供给/航运；4海外原油。Options T-1不计。
- **入场：** **至少等60分钟。** 若9:00仍在680以上，不追；优先等**660—675**深回撤后承接，再重回680/VWAP才1/3。
- **止损：** 30分钟接受在650以下；headline行情使用小仓。
- **逻辑失效：** SC<640且Brent<92，或出现可信的Hormuz快速重开/美伊降级。
- **TP1/TP2：** 705 / 735；时间止损1–2D。
- **最大损失：** 0.25%–0.35% NAV。
- **合约参数：** 1000桶/手；tick 0.1元/桶；tick value 100元/手；按687.7名义约687,700元/手；INE现行可核验SC2610涨跌停±14%、一般持仓保证金16%、套保15%。以687.7仅作压力敏感度，一次14%约96,278元/手；两个连续同向14%复合约206,037元/手。夜盘21:00–02:30；实物交割，临近交割月必须提前退出/移仓。

## 八、商品期权专项

本期**不输出具体商品期权surface指标**。原因是quality层虽标记`surface_ready=true`，但module-specific `surface_latest.json`为空；positioning/execution均not ready、bid/ask=0，而且9月1日options对9月2日晨报属于T-1，只能作为背景。

若盘中重新获取同日surface和人工可执行quotes，研究优先级：**BU bull call spread > EG bull call spread > SC bull call spread > AG failed-rally put spread**。固定执行条件：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、9:00开盘风险地图

| 品种 | 最大风险 | 等多久 | 最重要确认 |
|---|---|---:|---|
| **BU2610** | 油价冲击+夜盘高开，追价赔率差 | **30–45m** | 4970–5020承接、VWAP、Back是否维持 |
| **EG2610** | 两日累计涨幅过大 | **30–45m** | 5525是否守住、Back>2.5%、首小时高点 |
| **SC2610** | 夜盘+7.93%，headline反转巨大 | **60m** | 660–675深回撤承接、Brent>93.5 |
| MA610 | 伊朗供应多 vs 港口/MTO反方 | 45m | 3040附近承接、curve不塌 |
| AG/AU | 已大跌，低位追空convexity差 | 45m | 美元/美债、失败反弹、海外金银 |
| FG/V | squeeze误判短缺 | 45m | curve、库存、OI是否真正跟上 |

## 十、未来24小时 / 7日事件

- **9月2日22:30 BJT：EIA Weekly Petroleum Status Report**（week ending Aug 28）。对SC/BU/LU/FU最重要的是原油、汽柴油与炼厂利用率是否继续支持产品稀缺。
- **9月4日20:30 BJT：美国8月非农**。直接影响美元、实际利率、AU/AG，并通过Fed路径反馈油价估值。
- **9月4日约03:30 BJT：CFTC COT**（美东周五15:30），只作拥挤背景，不把分类持仓当最终客户方向。
- **9月8日04:00 BJT：USDA Crop Progress**，关注棉花、大豆、玉米天气与生长条件。
- **全天候：Hormuz通航、油轮安全、美国/伊朗打击与外交渠道**。这是能源Delta的第一催化剂，任何可信降级都优先于技术位。

## 十一、风险预算

BU虽为82分，**开盘瞬间新增风险预算仍为0**；只有价格触发后才允许0.50%–0.75% NAV。EG 0.35%–0.50%，SC 0.25%–0.35%，MA若重评执行则0.25%–0.35%。

BU/EG/SC/MA/LU/FU属于同一个“中东供应冲击+能化beta”大因子：四者合计初始最大损失建议**≤1.25% NAV**，不因它们是不同品种就重复计算alpha。贵金属美元/实际利率因子≤0.50%；中国工业需求beta≤0.50%。

## 数据与模型说明

事实数据、市场定价、模型推导和主观判断已分开。Price/OI组合只称归因线索；near-next curve不等于现货basis；C/D basis不作为套利；周度/旬度fresh只代表原生频率有效；T-1 Options不计今日fresh evidence。

## 关键来源

- Reuters, Oil prices settle up more than $4 a barrel on renewed US-Iran fighting: https://www.reuters.com/business/energy/oil-prices-rise-latest-fighting-resurrects-middle-east-supply-disruption-risks-2026-09-01/
- Reuters, Two tankers carrying Saudi oil attacked in Strait of Hormuz: https://www.reuters.com/business/energy/two-tankers-carrying-saudi-oil-attacked-strait-hormuz-2026-09-01/
- Reuters, Iran oil exports stall: https://www.reuters.com/business/energy/blockade-succeeds-where-sanctions-failed-iran-oil-exports-stall-2026-09-01/
- Reuters, Gold falls to two-week low: https://www.reuters.com/world/india/gold-muted-traders-await-us-jobs-data-monitor-mideast-tensions-2026-09-01/
- Reuters, China RatingDog PMI 51.5: https://www.reuters.com/world/asia-pacific/chinas-august-factory-activity-picks-up-demand-improves-pmi-shows-2026-09-01/
- 每日经济新闻，9月2日国内商品夜盘收盘：https://www.nbd.com.cn/articles/2026-09-02/4569667.html
- 经济观察网，9月1日夜盘收盘：https://www.eeo.com.cn/2026/0901/1019842.shtml
- 证券时报，乙二醇两日大涨与供应约束：https://www.stcn.com/article/detail/4167949.html
- 同花顺/金投网，沥青库存与排产：https://goodsfu.10jqka.com.cn/20260901/c679484728.shtml
- EIA WPSR schedule: https://www.eia.gov/petroleum/supply/weekly/schedule.php
- BLS Employment Situation schedule: https://www.bls.gov/schedule/news_release/empsit.htm
- CFTC COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：BU2610回撤承接多；EG2610回撤承接多；SC2610仅在深回撤后承接多。**  
**C. 今天应继续观察的机会：MA610回撤多、M2701低噪声趋势、AG2610失败反弹空、TA701成本/curve多。**  
**D. 今天必须避免或退出的交易：9:00追BU/EG/SC高开、低位追空AU/AG、把FG/V squeeze解释为短缺，以及任何基于空surface/零bid-ask的精确商品期权交易。**
