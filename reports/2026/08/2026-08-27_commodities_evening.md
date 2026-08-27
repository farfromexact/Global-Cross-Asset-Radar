# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-27

> 数据截点：北京时间2026-08-27 19:32。中国8月27日日盘已经结束，但China-Commodities-Engine当前T日核心Futures未通过质量闸门；以下中国价格/OI/curve只把8月26日最后完整EOD作为**stale background**，不冒充8月27日行情。15:00—19:30海外变化单独使用实时/准实时公开来源；21:00中国夜盘尚未发生。

## 一、今日一句话结论

**今日商品期货期权无合格交易。8/27中国EOD五所取数未通过质量闸门；只观察Hormuz能源、农作物天气与铜库存错位，不预埋21:00订单。**

这不是“市场没有行情”，而是**没有一笔能够同时满足当日中国价格—持仓、结构、赔率和数据质量要求的交易**。昨天RM611/FG701/EG2610的79/77/76分条件单今晚全部机械撤销，直到8月27日T日EOD重新验证。

## 二、数据质量与覆盖说明

本轮首先通过GitHub连接读取`farfromexact/China-Commodities-Engine`的`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；随后按v2协议钻取`data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/options/latest.json`，并检查`data/scoped/*`回退。当前可验证的统一`report_input`没有形成可用于8月27日晚盘决策的T日完整EOD；最后一个可验证完整统一汇总仍是`requested_date=2026-08-26`、`generated_at=2026-08-26T19:05:02.243742+08:00`。

更关键的是当前`data/last_run_status.json`已经明确给出8月27日运行结果：SHFE、INE、DCE、CZCE、GFEX五所Futures全部`state=error`、records=0，统一错误为iFinD历史行情响应缺少`time`列；`source_date_match_pct=0%`、`critical_module_errors=15`、`full_market_ready=false`、`data_fresh=false`。因此今天**不存在可验证的8月27日中国close/settle/volume/OI/ΔOI/curve**，也就不能把8月26日的1D/5D、价仓象限或curve继续计作今晚fresh evidence。

范围化回退也不能救场。当前只有`data/scoped/ex-dce`，其最近可用scope是2026-08-18、且排除DCE，本身`full_market_ready=false`；既不同日，也缺铁矿、焦煤、豆粕、油脂、塑化等关键板块，不能静默拼接到8月27日。

Physical模块反而已经滚到`requested_date=2026-08-27`、07:55生成：20个目标中4个按各自原生频率fresh、0 stale、0 carried-forward。铁矿港口库存最新观察日8月26日、15904吨；焦煤旬度现货8月20日2043.1元/吨且basis质量仅C；FG企业库存8月21日7441.4重量箱；TA周度加工费8月21日586.52元/吨。上述多数只有绝对水平，**没有可验证方向变化，不自动构成完整实体证据层**。

Options今晚仍是**T-1（2026-08-26）**：20,346条合约、344个series、56/64品种；IV coverage 94.46%、OI coverage 67.19%、bid/ask coverage 0，330个series在昨日可做surface研究、62个positioning-ready、0 execution-ready。因为不是8月27日T日数据，今晚全部只能作波动率背景，**不得计入fresh证据层，也不输出可执行权利金、bid/ask、滑点或Dealer Gamma方向**。

Contract metadata同样降级：SHFE/INE部分字段可用，DCE JSON异常、CZCE解析异常、GFEX source-date不匹配。故今日没有正式交易卡需要用旧margin/price-limit去填补当前参数；若21:00后人工交易，必须从交易终端/交易所重新核对动态保证金、涨跌停、夜盘资格和到期交割安排。

**不能闭环的产业链：** 黑色/建材缺T日价格与高质量basis；能源化工缺T日中国curve/OI；农产品缺T日中国价格与进口压榨闭环；有色无法形成当日沪伦比/进口窗口；期权没有T日surface和execution quote。

## 三、商品仪表盘

> 下表中国列均为**2026-08-26最后完整EOD，作为stale background，不代表8月27日涨跌**。8月27日海外overlay只在相关行单独标注。

| 板块 | 合约 | 最近可验证中国价 | 1D / 5D（8/26） | Volume / OI / ΔOI（8/26） | Curve（8/26） | Physical / Options | 8/27晚间信号 |
|---|---|---:|---:|---|---|---|---|
| 油粕 | RM611 | close 2314 / settle 2282 | +2.06% / +1.06% | 989,630 / 671,302 / +5.28% | Back +3.33% | 无RM Physical；Options T-1 | **昨日多头信号撤销，等待T日重建** |
| 建材 | FG701 | 895 / 905 | -1.20% / -0.77% | 1,236,286 / 1,645,325 / +9.08% | Contango -2.91% | 周度库存仅level；Options T-1 | **昨日空头信号撤销** |
| 化工 | EG2610 | 5168 / 5247 | -4.55% / +4.56% | 941,964 / 376,074 / +4.04% | Back +2.88% | Physical缺；Options T-1 | **不追空，不抄底** |
| 能源 | FU2611 | 3622 / 3675 | -6.61% / -3.29% | 1,098,439 / 261,424 / -8.88% | Back +16.04%* | 8/27 Brent/WTI反弹；新加坡燃料库存回升 | **69：双侧事件观察** |
| 能源 | BU2610 | 4212 / 4254 | -4.88% / +3.76% | ΔOI +0.92%；其余本轮未复核 | Back +3.10% | 海外油价反弹但产品库存偏松 | 观察 |
| 贵金属 | AG2610 | settle 16670 | -0.63% / +6.69% | 643,479 / 269,980 / -4.34% | 轻Contango | 8/27黄金近持平、白银小涨；Options T-1 | **Warsh前No-Trade** |
| 有色 | CU2610 | settle 109650 | +1.00% / +2.43% | 本轮未复核 | Back +0.15% | LME铜高位但库存受美关税搬仓扭曲 | **64：沪伦错位观察** |
| 黑色 | RB2610 | settle 3270 | -1.03% / -4.27% | ΔOI -9.37%；其余本轮未复核 | Back +0.62% | T日中国数据缺 | 不更新方向 |
| 有色 | SN2610 | settle 301500 | +3.33% / +4.58% | ΔOI -7.86%；其余本轮未复核 | Back +2.31% | T日中国数据缺 | 不追旧强势 |
| 新能源 | LC2701 | settle 160680 | +3.87% / +5.67% | ΔOI +0.98%；其余本轮未复核 | Back +1.99% | 实体库存/排产闭环缺 | 不更新方向 |
| 新能源 | SI2611 | settle 9330 | -3.47% / -6.84% | ΔOI +2.97%；其余本轮未复核 | Contango -0.64% | 实体闭环缺 | 不追旧弱势 |
| 航运 | EC2610 | 价格本轮未复核 | +5.49% / +4.43% | ΔOI约-6.51% | 曲线约-24%，明显扭曲 | Hormuz流量仍低于常态 | 只看事件，不做旧价交易 |

\* FU近端curve此前受交割月污染，16%不能解释为可持续现货紧张，更不能作为可执行跨期套利。

## 四、相比上一交易日真正变化

**第一，最大的变化是数据regime本身从“可交易”变成“不可验证”。** 8月26日晚报五所齐全、803个合约、source-date 100%、critical errors=0；8月27当前五所T日Futures全部0条并出现15个critical errors。于是昨天RM611 79分、FG701 77分、EG2610 76分都不能自然滚存到今晚。**信号失效的原因不是市场反向，而是证据过期。**

**第二，能源从昨天的风险溢价回吐转成盘中反抽，但物理恢复仍不完整。** Reuters在约18:05 BJT记录Brent 88.35美元/桶、+0.58%，WTI 82.41、+0.22%，均从更低的日内低点回升；与此同时Kpler显示8月26日Hormuz只有10艘商品船通过，高于前日8艘但仍低于10日均值约15艘，一艘油轮还遭未知弹体击中。也就是说，外交改善预期和真实物流约束同时存在，方向是双侧的。  
来源：https://www.reuters.com/business/energy/oil-prices-extend-losses-expectations-talks-ease-middle-east-supply-woes-2026-08-27/  
来源：https://www.reuters.com/world/middle-east/shipping-traffic-through-strait-hormuz-rises-slightly-data-shows-2026-08-27/

**第三，成品油比原油更偏空。** 新加坡截至8月26日当周油品总库存39.18百万桶、周增4.0%、三周高位；残渣燃料油库存19.24百万桶、周增4.4%，中馏分和轻馏分库存也回升。它削弱“Brent反弹=FU必须反弹”的简单映射。  
来源：https://www.reuters.com/business/energy/singapore-oil-product-inventories-rebound-highest-three-weeks-2026-08-27/

**第四，农产品出现新的中国天气供应风险，但暂时只能形成观察，不是期货多单。** Reuters 17:32 BJT附近报道，自7月中旬以来东北、华北和新疆的高温/暴雨影响玉米、大豆和棉花；玉米授粉和新疆棉结铃尤其敏感，可能提高饲料谷物进口需求。但当前缺8月27 C/CF/M/RM的价格—持仓—curve确认，而且USDA周度出口销售将在20:30 BJT发布，所以此时抢跑没有edge。  
来源：https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/

**第五，贵金属进入Jackson Hole前的低信息窗口。** Reuters晚间显示现货黄金约4590美元附近、基本持平，白银约68.34、+0.4%；7月PCE同比3.7%使利率预期仍偏紧，市场等待Fed主席Kevin Warsh周五讲话。AG没有T日中国价和T日IV，裸买Vega或赌方向都不划算。  
来源：https://www.reuters.com/world/india/gold-drifts-higher-eyes-fed-chair-warshs-comments-2026-08-27/

**第六，铜的“紧”越来越像地域库存搬家，而不是干净的全球短缺。** Reuters指出美国2027/28精炼铜关税威胁推动库存向美国集中、抽走LME可用库存；这会造成LME局部紧张和COMEX高库存并存。没有8月27 SHFE价格、人民币、税费、运费和cash-3M同刻数据，今晚不能把它包装成沪伦套利。  
来源：https://www.reuters.com/business/us-tariff-threat-upends-copper-surplus-prices-test-all-time-peak-2026-08-25/

## 五、产业链地图

| 产业链 | 当前方向 | Price / Curve | 实体/海外 | Options | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| **原油—燃料油—沥青** | 双侧、反抽 | 中国T日不可验证 | Brent/WTI反弹；Hormuz流量仍低；新加坡油品库存上升 | T-1，仅背景 | 中国T日price/OI/curve、裂解 | **中** |
| **玉米/饲料谷物—棉花** | 供应风险偏多 | 中国T日不可验证 | 中国高温/洪涝为fresh Physical；20:30 USDA待发布 | T-1/部分品种缺 | 中国T日price/curve、进口压榨 | **中** |
| **铜/有色** | 高位但结构扭曲 | 8/26中国旧强势，不计fresh | 美关税推动库存地域搬迁 | T-1 | 当日沪伦比、FX、cash-3M、进口平价 | 中低 |
| **地产建材/化工** | **无法更新** | 8/26 FG/V/EG旧结构不可滚存 | FG只有周度level；TA加工费仅context | T-1 | **8/27中国价格/OI/curve** | **低** |
| **贵金属** | 事件等待 | AG T日不可验证 | 金银平稳；美元/利率仍偏紧；Warsh待讲话 | T-1 | T日IV/skew、实际利率reaction | 中低 |

今天不存在可定义的“最强可交易产业链”。如果只看fresh海外/实体信息，**最值得盯的是Hormuz能源与中国农作物天气；最不能交易的是依赖中国价仓结构的地产建材/化工，因为T日核心证据缺失。** 当前regime是“海外事件驱动仍强，但中国EOD验证层暂时断裂”的No-Trade regime。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。** 评分严格按fresh独立证据层上限执行；没有70+。

| Rank | 观察项 | Score | 方向 | 持有期 | Fresh层 | 工具 | 数据惩罚 |
|---:|---|---:|---|---|---:|---|---|
| 1 | **FU2611 / SC能源恢复错位** | **69** | 双侧观察 | Intraday–3D | **2** | 先观察期货；期权仅研究 | 中国8/27 price/OI/curve缺；Options T-1；FU旧curve有交割污染 |
| 2 | **C/CF中国天气事件凸性** | **66** | 偏多观察 | 1–10D | **2** | 等T日主力确认后再选期货/有限风险期权 | 当前具体主力、OI、curve不可验证；20:30 USDA尚未发布 |
| 3 | **CU2610 美关税—LME库存错位** | **64** | RV观察 | 1–10D | **2** | 未来可研究沪伦RV | 缺当日SHFE、FX、税费运费和exact-contract parity |

昨天的RM611、FG701、EG2610今天**不进入排行榜**：它们的核心fresh层本应来自8月27中国price/OI/curve，而该层当前不存在。

## 七、前三名观察卡（非正式交易卡）

由于没有70+合格交易，**本节不生成可执行正式交易卡**。以下三张只说明“若数据恢复，什么才值得重新评估”；所有入场字段当前均为“禁止预埋订单”。

### 1. FU2611｜能源恢复错位｜69｜双侧观察

**事实：** 8月27约18:05 BJT Brent 88.35、+0.58%，WTI 82.41、+0.22%；Hormuz通行10艘仍低于约15艘10日均值；新加坡油品总库存周增4.0%、残渣燃料库存周增4.4%。中国FU2611最新可靠EOD仍是8月26 close/settle 3622/3675，不能代表今天。

**市场定价：** 海外正在同时交易“外交重开概率上升”和“真实物流仍受限”。**推断：** 原油与燃料油可能分化，Brent反弹未必能被FU完整复制。**市场可能错在哪里：** 若谈判失败，风险溢价会迅速回归；反之若通航和成品油到货同时正常化，旧Backwardation会快速坍塌。

**新鲜证据层：2**——境外实时价格/宏观映射、境外实体物流/库存。中国price/OI/curve和T日期权都缺，因此最高只能69。

**最佳表达：** 现在不建仓。21:00后只有在人工终端补齐8月27结算、首小时OI/curve并确认外油方向后，才在FU2611或SC选择单一Delta；若用期权，只能在live quote下用有限风险Call/Put Spread比较，当前不报premium。

**入场：** 禁止预埋；至少等30–45分钟。多头需要外油保持反弹、国内价格站上VWAP且curve不松；空头需要外油重新跌破日内低位、国内curve同步走平。**分批：** 触发后最多先1/3风险。**止损/失效：** 外油与国内第一小时方向重新背离，或curve反向扩张。**TP1/TP2：** +1R/+2R。**时间止损：** 两个交易时段无延续即撤。**最大损失：** 若未来触发，仅0.25%–0.35% NAV。

**合约参数：** FU静态交易单位10吨/手、tick 1元/吨、tick value 10元；但今晚当前动态margin、price limit、broker add-on未验证，不计算一板/两板损失。SHFE长期规则显示FU属于21:00连续交易品种，现行动态调整仍需下单前终端复核。实物交割，进入交割月前主动roll。

### 2. CU2610｜关税—库存地域错位｜64｜RV观察

**事实：** 最近可靠中国结算为8月26 CU2610 109650、当日+1.00%；Reuters近期LME铜接近历史高位，但核心驱动之一是美国未来精炼铜关税把库存吸向COMEX、挤薄LME可交割库存。**市场可能错在哪里：** 市场可能把地域性库存错配误读为全球绝对短缺；也可能低估中国需求和印尼供应扰动，使紧张持续更久。

**新鲜证据层：2**——海外价格/宏观、海外库存结构；中国T日price/curve和exact import parity均缺。

**最佳表达：** 不是裸多铜，而是等8月27 SHFE、LME cash/3M、USD/CNH、税费运费同刻对齐后再判断沪伦RV。**两腿配比：** 当前不提供；必须按铜吨数+FX Delta+进口成本闭环计算，而不是1:1手数。

**入场/分批/止损：** 现在全部为空；没有exact parity不下单。**失效：** LME库存回流、cash premium消失，或COMEX-LME套利窗口关闭。**目标：** 仅在可执行价差形成后按z-score/成本带定义。**最大损失：** 未来若进入RV试仓≤0.25% NAV。CU为SHFE连续交易品种，长期时段21:00—次日01:00；当前动态margin/limit需终端复核。

### 3. AG2610｜Jackson Hole事件观察｜59｜No-Trade

**事实：** 8月27海外黄金约4590美元附近基本持平，白银约68.34、+0.4%；7月PCE同比3.7%，市场等待8月28日22:00 BJT Warsh讲话。最新可靠中国AG2610结算仍是8月26的16670。Options也是8月26 T-1，bid/ask coverage=0、execution=false。

**市场定价：** 高利率与政策不确定性压制黄金，但财政/货币信用叙事仍提供尾部需求。**推断：** 目前方向信息密度低，真正edge是保留Vega预算到讲话后，而不是提前猜措辞。

**新鲜证据层：1**——海外宏观/金银实时映射，因此按规则≤59。**最佳表达：** 现在不做。若明晚讲话后金银、美元与实际利率出现同向确认，再等待15–30分钟；期权只在T日surface和真实bid/ask齐备后比较Call/Put Spread。**最大损失：** 无仓即0；未来事件试仓≤0.25%–0.40% NAV。SHFE长期规则显示白银连续交易21:00—02:30；当前动态风控参数需终端复核。

## 八、商品期权专项

今晚Options的核心事实不是“IV高低”，而是**T日缺失**。最新独立链为2026-08-26：20,346条、344 series、56/64产品，IV coverage 94.46%、OI coverage 67.19%、bid/ask coverage 0；昨日330个surface-ready、62个positioning-ready、0 execution-ready。Dealer Gamma方向未知。

因此8月26代表样本只能作为历史背景：RM611 ATM IV约18.18%、FG701约22.80%、EG2610约43.95%。**这些不是8月27当前IV，不参与今晚评分，不称全市场最高/最低，也不用于算今晚净权利金。**

当前最有价值的event convexity是AG/AU的Jackson Hole和能源的Hormuz双侧尾部，但因为T日surface/bid-ask都缺，今晚不把任何Call Spread、Put Spread、Calendar或Butterfly放进正式执行清单。需要回避：裸卖地缘Vega、用T-1 skew判断今日crowding、在OI coverage不足时推Dealer Gamma、以及用理论价冒充可成交价。

## 九、21:00夜盘开盘风险地图

> 因8月27中国结算价无法验证，下面的“高/低/平开”只能描述**海外信息映射方向**，不是相对今天真实settle的确定gap判断；置信度整体降一级。

| 品种 | 最近可靠中国基准 | 15:00—19:30海外映射 | 21:00倾向 | 置信度 | 追价？ | 等待 | 开盘后最重要确认 |
|---|---|---|---|---|---|---|---|
| FU/SC/LU/BU | 8/26 EOD，stale | Brent/WTI反弹；Hormuz仍堵；新加坡油品库存升 | **偏上但双侧** | 低—中 | **否** | **45m** | 外油、VWAP、首小时OI、curve、FU/SC相对强弱 |
| AG/AU | 8/26 EOD，stale | 金近持平、银小涨；利率仍偏紧 | 平/小幅正映射 | 低 | **否** | 15–30m | DXY、实际利率、GC/SI、T日IV是否恢复 |
| CU/AL/SN | 8/26 EOD，stale | 铜高位但库存地域错配、美元偏强 | 混合 | 低 | 否 | 30m | LME cash-3M、USD/CNH、SHFE首小时接受度 |
| RM/M/Y/OI/C | 8/26 EOD，stale | 20:30 USDA Export Sales尚未发布 | **不预判** | 低 | **否** | 数据后30m | USDA surprise、CBOT、人民币、国内price/OI |
| FG/SA | 8/26 EOD，stale | 海外直接映射弱 | 无法判断 | 低 | 否 | 30–45m | 8/27真实结算、首小时OI、curve |
| EG/PP/V/TA | 8/26 EOD，stale | 油价反弹但产品库存偏松 | 分化 | 低 | 否 | 30–45m | 原油Beta vs 自身curve、OI、现货利润 |
| LC/SI/EC | 8/26 EOD，stale | 无可靠同品种实时映射 | 未定 | 低 | — | — | **本轮T日metadata未成功复核夜盘资格；下一确定窗口8/28 09:00** |

SHFE/INE官方长期规则可确认原油21:00—02:30、燃料油21:00—23:00、铜21:00—01:00、黄金/白银21:00—02:30等连续交易框架；DCE公开手册显示夜盘品种Session 1为21:00—23:00。**但具体合约当日是否受临时风控/停牌/节前安排影响，仍以下单终端和当日交易所通知为准。**

## 十、未来24h / 7d事件

**8月27日20:30 BJT：USDA Weekly Export Sales。** 官方日历为8:30 ET。玉米、大豆、豆粕、豆油、棉花等在21:00前会先得到一层新的海外需求信息；因此C/M/RM/Y/OI/CF不应在20:30前预埋夜盘方向。  
来源：https://fas.usda.gov/report-release-announcement/weekly-export-sales-300

**8月28日08:00 BJT：Jackson Hole完整议程公布；8月28日22:00 BJT：Fed主席Kevin Warsh讲话。** 贵金属应减少裸Delta，若要保留事件凸性只考虑有限风险结构，且需T日期权真实quote。  
来源：https://www.kansascityfed.org/newsroom/2026-news-releases/kansas-city-fed-to-host-annual-jackson-hole-economic-policy-symposium-2026/

**8月29日02:00 BJT：USDA Quarterly Agricultural Trade Forecast。** 对美国农产品出口路径和中国进口替代叙事提供中期背景，不应替代国内现货/压榨数据。  
来源：https://fas.usda.gov/

**8月29日03:30 BJT：CFTC COT。** 官方排期8月28日15:30 ET发布，数据反映此前周二，只作为positioning背景，不当实时流量。  
来源：https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm

**9月2日22:30 BJT：下一期EIA Weekly Petroleum Status Report。** 当前官方页面显示下次发布日期9月2日；能源仓若届时已有利润，数据前降低同因子Delta。  
来源：https://www.eia.gov/petroleum/supply/weekly/index.php

**持续事件：Hormuz/Oman-Iran谈判与真实船流。** 只要实际通过量仍显著低于常态，能源下行趋势就不能只靠外交headline确认；反之新加坡/亚洲产品库存持续回升会压制FU/裂解的独立Beta。

风险预算在数据恢复前进一步收紧：**本轮新增风险=0**。T日恢复后，单一试仓仍为0.25%—0.75% NAV，确认交易0.75%—1.50%，同一高确信主题≤2.5%—3.0%。FU/SC/LU/BU与EG/TA/PP的能源地缘Beta需合并；AG/AU按美元—实际利率因子合并；C/M/RM/Y/OI按天气—进口因子合并。

### 关键来源

- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- Reuters Oil 2026-08-27: https://www.reuters.com/business/energy/oil-prices-extend-losses-expectations-talks-ease-middle-east-supply-woes-2026-08-27/
- Reuters Hormuz shipping 2026-08-27: https://www.reuters.com/world/middle-east/shipping-traffic-through-strait-hormuz-rises-slightly-data-shows-2026-08-27/
- Reuters Singapore products 2026-08-27: https://www.reuters.com/business/energy/singapore-oil-product-inventories-rebound-highest-three-weeks-2026-08-27/
- Reuters China crops 2026-08-27: https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/
- Reuters Gold 2026-08-27: https://www.reuters.com/world/india/gold-drifts-higher-eyes-fed-chair-warshs-comments-2026-08-27/
- Reuters Copper 2026-08-25: https://www.reuters.com/business/us-tariff-threat-upends-copper-surplus-prices-test-all-time-peak-2026-08-25/
- USDA FAS: https://fas.usda.gov/report-release-announcement/weekly-export-sales-300
- Kansas City Fed: https://www.kansascityfed.org/newsroom/2026-news-releases/kansas-city-fed-to-host-annual-jackson-hole-economic-policy-symposium-2026/
- CFTC: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- EIA: https://www.eia.gov/petroleum/supply/weekly/index.php

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：**无；8/27中国T日Futures/Market State未通过质量闸门，禁止把8/26条件单滚存到今晚。**
C. 今天应继续观察的机会：FU/SC的Hormuz恢复错位、中国玉米/棉花天气凸性、CU的美国关税—LME库存地域错位；都要等T日中国数据或事件后确认。
D. 今天必须避免或退出的交易：继续执行昨日RM/FG/EG条件单、21:00追首跳、用T-1商品期权IV做今日执行、把海外反弹倒写成中国日盘已上涨、以及在无exact parity时做沪伦/进口套利。
