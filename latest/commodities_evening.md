# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-12｜生成：19:42 BJT｜信息截点：19:38 BJT｜prompt_version：`radar_2026-10-12_stock_v1`**

## 一、今晚一句话结论

> **今晚没有满足报价与触发的即时新仓；铜是唯一70+研究候选，贵金属与化工须先验证海外回落是否压过中国日盘强势。**

**截至本报告时点，无可立即执行的合格新交易。** 当前regime是“国内高波动分化、铜内外同强、贵金属与能源在中国收盘后转弱、期权和Night执行层缺失”。最接近验证的是CU2611突破回踩、AG2612海外回落反转、MA701冲高后延续下破；下一验证窗口分别为今晚21:30、21:30、21:45。LC2701的暴跌是重大异常，但无夜盘、曲线与价格相反，不能当作即时抄底或追空。

## 二、数据质量、时点与覆盖

### 2.1 实际读取与版本

- **中国商品仓库**：`farfromexact/China-Commodities-Engine@2b08a42cfe8285fa943c4827a6456127a42b0c77`。第一层读取`data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`；因重点合约、状态冲突和参数审计，下钻`data/latest.json`、`data/contract_meta.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`。
- 统一输入`requested_date=2026-10-12`，`generated_at=2026-10-12T19:11:00.250240+08:00`，schema v2。Futures/Market State/Physical/External均更新到10月12日；核心期货18:58生成，Physical/External约19:10生成。
- **核心价格**：806合约、77品种，SHFE/INE/DCE/CZCE/GFEX五所齐全，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0。5条OHLC占位记录已从异动排序排除；无负volume/OI、无重复合约、无非法OHLC。
- **模块缺口**：DCE contract-info失败、GFEX contract-info source-date未验证；SHFE/DCE/GFEX仓单抓取失败，保留5条旧仓单但不把它们当本期新增；basis主模块与会员排名不可用。Contract Metadata总体`partial`，动态保证金/限幅和夜盘字段覆盖不足。
- **Physical**：18/20条当日可用，SC/LU unavailable，0 carried-forward。当前basis均为C级且缺地区/品质/含税/交割地，对方向评分和可执行套利均不合格；孤立现货绝对值只作context。
- **External仓库层**：17/22条10月12日日频/准实时序列可用，5条unavailable，usage均为`context_only`；19:10值包括LME铜14666.5美元/吨、Brent 105.67美元/桶、WTI 92.68美元/桶、COMEX金4195.6美元/盎司、银60.94美元/盎司。它们不是全口径进口平价。
- **Options**：根状态显示10月12日抓到13604条但模块状态为`empty`、未发布；统一层只能提供10月9日14074条/185 series的旧截面（181 surface-ready、41 positioning-ready、0 execution-ready，bid/ask coverage=0）。因10月12日完整截面此时应已产生却失败，10月9日仅作历史背景，不计本期第五层；`data/options/surface_latest.json`本次读取为空，不能当作曲面已就绪。dealer Gamma方向未知。
- **Stock仓库**：`farfromexact/China-Stock-Engine@5f80b92eb79694253cfc276b59a3e1688f171f79`。按manifest和company directory仅读取紫金矿业`data/latest/research_9_002.json`、宝钢股份`data/latest/research_d_002.json`及映射配置；不是全A股扫描。research_asof=2026-10-12 09:38 BJT，但价量trade_date仍为10月9日，tradability/ADT20/市场规则未验证，故公司经营证据可用于当前研究，股票报价与今晚执行均不可用。

### 2.2 已完成Night Session的语义与质量闸门

模块专用状态是`trading_date=2026-10-11`、`night_session_date=2026-10-10`、`generated_at=2026-10-11T08:01:14.462305+08:00`、`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`；night contract=0、product_count未发布、outside-window=592、query_error=214、unresolved=214，missing timestamp/price/quote=0。统一层更旧至9月30日。

这不是属于10月12日交易日的有效Night快照，也不是今晚21:00未来行情，已整段隔离。只有晨报公开回退核实了RU2701周五夜收20980；用相同合约可得今日收20640相对夜收的`day_follow_through=-1.62%`，说明早前+1.62%隔夜涨幅被日盘完全反转。该回退没有OHLC/量仓/时间戳，不能推广到其他合约，也不把Night拆成第六证据层。

### 2.3 收盘后海外新增定价（15:00—19:38 BJT）

- 约17:11 BJT，现货金4176.86美元/盎司、-0.4%，现货银60.6219美元/盎司、-0.3%；强美元压制贵金属。[Reuters，2026-10-12](https://www.reuters.com/world/india/gold-gains-weaker-oil-dollar-us-inflation-data-focus-2026-10-12/)
- 约16:47 BJT，Brent约104.90美元/桶、-0.6%，WTI约91.10、-0.8%；俄油/柴油供给预期压价，但中东冲突仍保留上行尾部。[Barron's，2026-10-12](https://www.barrons.com/livecoverage/stock-market-news-today-101226/card/oil-falls-after-trump-strikes-deal-with-russia-on-diesel-supply-IdkRG1cjCDnZ4wdRovtc)
- 约16:31 BJT，LME铜站上14600美元/吨，受中国刺激预期与智利矿山劳资风险支撑；19:10仓库值14666.5，方向与中国铜收盘同向。[WSJ，2026-10-12](https://www.wsj.com/finance/commodities-futures/gold-rises-as-markets-weigh-oil-pullback-2c0301c2)
- DXY约102.38、+0.2%；USD/CNH约6.6944，前收6.6927，人民币小幅偏弱。美元强势对金银构成反向力量；人民币变化幅度不足以单独解释境内商品。[Investing USD/CNH，2026-10-12](https://www.investing.com/currencies/usd-cnh)

## 三、商品仪表盘（展示12项；全市场扫描见覆盖核对）

1D/5D为同一当前合约结算收益；“close change”另用close相对pre-settle，避免把结算锚当隔夜新增信息。Night除RU外均为missing，不是0。

| 板块 | 品种/精确合约 | 10/12 close/settle | close change；1D/5D | Volume/OI/ΔOI | EOD curve | Basis/Physical | 已完成Night→Day | 收盘后海外 | Options | 21:00/下一窗口 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 新能源 | LC2701 | 104740/108880 | -11.79%；-8.30%/-9.88% | 405572/429039/+7401 | +4.07% backwardation，z=+2.82 | 现货114000；C级basis +5120，仅context | 无夜盘；不适用 | 无exact海外锚 | 10/9历史S=Y/P=N/E=N | 10/13 09:00等45分钟；不接飞刀 |
| 橡胶 | RU2701 | 20640/20780 | +2.08%；+2.77%/+6.81% | 563573/177637/+2950 | -0.95% contango，roll flag | 缺合格实体 | 20980→20640，日盘-1.62%；夜量仓缺 | SICOM新价缺 | 10/9历史Y/Y/N | 今晚平开偏弱；等30分钟 |
| 橡胶 | NR2612 | 17620/17870 | +1.76%；+3.21%/+5.49% | 153854/85370/-3526 | -3.10% contango，z=-2.57 | 缺 | exact missing | 无新exact锚 | 10/9历史Y/N/N | 不追；看RU/NR价差与curve |
| 贵金属 | AG2612 | 14816/14854 | +2.07%；+2.34%/-2.13% | 248317/288058/-2376 | -0.90% contango，z=-2.47 | 缺独立实体 | exact missing | 银-0.3%、金-0.4%、DXY强 | 10/9历史Y/N/N | 偏低开；21:30前不反手 |
| 贵金属 | AU2612 | 905.52/907.78 | +0.71%；+0.97%/-0.47% | 170015/228793/+334 | +0.02%，近乎平 | 缺 | exact missing | 金-0.4%、美元强 | 10/9历史Y/partial/N | 偏低开；等30分钟 |
| 有色 | CU2611 | 110630/110770 | +0.93%；+1.06%/+1.22% | 72159/195149/+3109 | +0.81% backwardation，z=+1.21 | 现货112028；C级basis，仅context | exact missing | LME铜>14600，方向同向 | 10/9历史Y/partial/N | 偏高开；突破回踩才多 |
| 化工 | MA701 | 3229/3257 | -2.77%；-1.93%/+11.01% | 1740113/773423/+12248 | +13.88% backwardation | 现货4050；C级basis +793 | exact missing | 原油回落，间接偏空 | 10/9历史Y/partial/N | 高波动；等45分钟确认3176 |
| 能源 | SC2612 | 719.3/709.5 | +0.13%；-1.24%/+3.61% | 58665/24990/+2282 | +2.95% backwardation；仅3观测 | Physical unavailable | exact missing | WTI/Brent收盘后下行 | 10/9历史Y/N/N | 偏低开但事件尾部大；等45分钟 |
| 油品 | BU2611 | 5111/5160 | -3.91%；-2.99%/+0.16% | 642358/151851/-9394 | +12.00% backwardation | 缺合格实体 | exact missing | Brent/WTI下行 | 10/9历史Y/partial/N | 低开概率高；不追空首跳 |
| 黑色 | JM2701 | 1546/1550 | +1.88%；+2.14%/+6.75% | 619932/413832/-11571 | +4.23% backwardation | 现货2206；C级basis | exact missing | 无exact外盘锚 | DCE当前不可用 | 可能平高；等30分钟 |
| 豆类 | A2701 | 5510/5498 | +1.92%；+1.70%/+6.45% | 216796/258595/+20901 | -0.78% contango | 缺 | 无夜盘 | CBOT豆1282.75，仅当前值无可比变化 | DCE当前不可用 | 10/13 09:00等45分钟 |
| 谷物 | C2701 | 2204/2201 | +1.05%；+0.92%/-0.36% | 375020/864547/+40438 | -1.36% contango | 缺 | 无夜盘 | CBOT玉米512，仅context | DCE当前不可用 | 10/13 09:00；不追单日量仓 |

**强弱判断**：最强产业链是铜；最弱是锂链。中国日盘的贵金属和橡胶强势没有获得收盘后海外/同合约Night确认；MA、SC、BU则处在“国内高波动与油价回落、近端backwardation”冲突中。LC暴跌伴OI增加只是归因线索，正curve反对无条件追空。

## 四、相比上一交易日/今晨真正变化

1. **LC成为全市场最大异常**：LC2701 close相对pre-settle -11.79%，结算-8.30%，量/OI均高；但near-next backwardation升至+4.07%、z=+2.82，与价格下跌相反。它是“需要产业解释”的异常，不是证据完整的空头。
2. **RU晨间强势被日盘完全反转**：公开回退夜收20980、今收20640，日盘-1.62%；相比周五close 20645几乎不变。相对昨结算仍显得上涨，是结算锚差异，不应写成今天新增强势。晨间RU追多条件降级。
3. **MA晨间多头逻辑失效**：开3327、高3384、低3176、收3229；收盘低于晨报3270计划止损及3250逻辑失效位。无分钟路径不能认定用户成交，但若此前按条件建立，应视为退出条件触发。
4. **铜出现三层同向**：CU2611价格/OI、near-next backwardation、收盘后LME铜强势同向；这是本期唯一具备70+评分资格的候选。现货basis仍是C级，不能把现货绝对值再加一层。
5. **贵金属从中国反弹转为内外冲突**：AG中国收盘+2.07%，但curve转contango、OI下降，之后国际金银分别约-0.4%/-0.3%，DXY强。晨间AG多头不再适合加仓，新空也必须等21:30确认。
6. **Stock新增但不产生可执行股票表达**：紫金的金铜矿业务和2026H1利润/现金流增长确认商品→利润通道；宝钢的铁矿成本/钢材价差确认利润受双边影响。两者当日股价、交易状态和ADT缺失，因此只改变表达比较，不新增证据层、不进Top5。

## 五、产业链地图

| 产业链 | 方向/强弱 | EOD与Night→Day | curve/实体 | 期权 | 海外 | 公司利润传导与决策贡献 | 最大缺失/置信度 |
|---|---|---|---|---|---|---|---|
| 铜—矿山—冶炼 | **最强，条件多** | CU close +0.93%；exact Night缺 | backwardation +0.81%；basis C不计 | T日失败、10/9历史不可执行 | LME>14600同向；DXY反向 | 紫金矿产铜售价渠道成立，但产量、成本、套保/汇率与Kamoa减产约束；股票今晚休市且报价滞后，直接CU优于股票 | 缺精确进口平价/当前期权/动态参数；中高 |
| 贵金属 | **日内强、收盘后转弱** | AG/AU上涨；Night缺 | AG contango反对，AU近乎平；实体缺 | 旧截面且exec N | 金银回落、美元强 | 紫金矿产金为条件性正暴露；2026H1归母利润391.7亿元、同比+68.2%，但旧经营事实不是今晚催化 | 缺当前银价与期权报价/夜盘；中低 |
| 甲醇—烯烃—芳烃 | **由过热转反转观察** | MA收跌，早夜缺 | backwardation仍+13.88%强烈反对追空；basis C | 旧截面 | 油价回落仅间接 | 无高质量公司映射加入；不以概念股替代 | 缺库存变化、MTO利润、night exact；中低 |
| 锂—新能源材料 | **最弱但曲线冲突** | LC close -11.79%；无夜盘 | backwardation +4.07%反对追空；现货/basis C | 旧截面、OI覆盖0、exec N | 无exact海外 | 未建立合格公司暴露与当前证券报价；不以“锂概念”推利润 | 缺高质量库存/成本/交割仓单；低 |
| 油品—航运 | **价格偏弱、事件尾部双向** | SC close近平、BU大跌；Night缺 | SC/BU backwardation反对无条件空；实体SC/LU缺 | 旧截面 | 油价收盘后跌，俄供给预期利空；中东风险反向 | 不引入炼化股：裂解价差、库存和套保未对齐 | 缺设施/出口事实、当前期权和精确时差映射；低 |

### Stock公司证据核验

- **紫金矿业601899.SH**：官方2026半年报（合并、2026H1 YTD）收入1941.78亿元、同比+15.78%；归母净利润391.70亿元、+68.17%；经营现金流554.72亿元、+92.41%。矿产铜/金产品售价通道被原件确认，但实现售价、销量、单位成本、长协、套保、汇率、少数股东与检修都会改变传导。[紫金2026半年报，2026-08-22](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)
- **宝钢股份600019.SH**：官方2026半年报收入1607.31亿元、+6.18%，归母净利润45.71亿元、-6.30%，H1毛利率约5.99%；报告支持“铁矿成本—钢材售价—产品结构”的双边传导，不支持固定利润敏感系数。[宝钢2026半年报，2026-08-22](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)
- 两家公司仓库tape只到10月9日，security state均unknown、execution not verified。紫金10月9日收30.8、单日+4.87%，宝钢收5.87、-1.68%，不能替代10月12日收盘，也不能以触及日线价认定成交。**本期Stock贡献：铜优先直接商品，黄金不通过紫金追价，黑色不通过宝钢表达；公司证据未改变五层计数。**

## 六、机会排行榜（研究吸引力，不是胜率/仓位）

| 排名 | idea_id / 方向 / 周期 | 分项：逻辑/凸性/催化/价曲波/拥挤 | 总分 | 有效支持层 | 三轴状态 | 反证、缺失与前期变化 |
|---|---|---:|---:|---:|---|---|
| 1 | `COM-E-CU2611-LME-BREAKOUT-LONG-20261012` 条件多 1—5D | 19/17/14/13/10 | **73** | 3：价格量仓、curve、外盘 | 待验证优势 / 部分 / 等21:30触发与参数 | DXY强、basis C、当前期权与动态保证金缺；本期新入池 |
| 2 | `COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012` 条件空 1—3D | 17/16/13/11/10 | **67** | 2：curve、外盘宏观 | 待验证优势 / 部分 / 等21:30 | 中国EOD上涨反对；地缘尾部、期权缺；晨间多头因新海外/curve证据注销 |
| 3 | `COM-E-MA701-POSTSPIKE-REVERSAL-SHORT-20261012` 条件空 1—3D | 17/15/13/10/9 | **64** | 2：价格量仓、外盘映射 | 待验证优势 / 部分 / 等21:45 | +13.88% backwardation和5D+11%反对；原多头失效后新建反转研究 |
| 4 | `COM-E-LC2701-OVERSHOOT-REBOUND-WATCH-20261012` 条件多 1—5D | 15/15/12/8/6 | **56** | 1：curve | 证据不足 / 不足 / 无夜盘，等10/13 09:45 | 价格/OI反对，basis C，实体与期权执行缺；仅早期异常 |

分数复核无超项。CU有三层才可超过70；AG/MA按两层上限≤69；LC按一层上限≤59。没有任何分数自动生成仓位。SC/BU油品未入榜：外盘下跌支持空，但近端backwardation、地缘尾部、实体缺失和新保证金/限额使赔率不可识别。

### 旧建议台账

- `COM-M-RU2701-SUPPLY-LONG-20261002`：首次10月2日。晨间高点21005可能短暂碰到条件区，但无分钟路径和成交反馈，触发仍**未知**；收盘20640使新增追多条件失效。观点由“等待回踩多”降为观察，原因是价格变化与日盘反转，不假定持仓。
- `COM-M-MA701-MOMENTUM-HOLD-20261009`：今日close 3229低于3270计划止损、3250逻辑失效。旧多头研究**注销**；若此前已按条件建立，应按原计划退出。新空是不同的post-spike反转假设，不继承旧目标。
- `COM-E-AG2612-DAY-REVERSAL-LONG-20261009`：早间入场区被当日OHLC覆盖，但路径/成交未知。收盘后海外转弱且curve为contango，旧多头不再允许加仓；若此前建立，14700下破作为收紧退出条件。新空仅在21:30确认后成立。
- JM、C旧观察保留但不入榜；SC旧空头仍不恢复为即时交易。无用户持仓或账户信息，不声称净敞口。

## 七、前三名交易卡（均等待触发，不是当前立即单）

### 1. CU2611条件多｜`COM-E-CU2611-LME-BREAKOUT-LONG-20261012`

- **事实**：close/settle=110630/110770；open/high/low=110300/111100/110190；close相对pre-settle +0.93%，5D +1.22%；OI195149、ΔOI+3109；near-next +0.81% backwardation。LME铜在中国收盘后仍高于14600。
- **定价/分歧/反证**：市场已预交易中国刺激与矿端扰动；分歧是若今晚站稳111100，内外同向与近端结构仍有延续空间。最强反证是DXY强、进口平价未对齐、事件已充分定价。
- **支持层**：①价格量仓支持；②curve支持；③Physical中性/缺失（C级basis不计）；④LME支持；⑤Options缺失。三层有效。
- **最佳表达**：CU2611期货条件单研究；股票紫金不是今晚表达，CU期权因T日截面和bid/ask缺失只可研究有限支出call spread，固定免责声明：`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/成交情景**：21:30后。好=110800—111100回踩守稳且LME≥14600，先半；中=111100突破后回踩不破，再半；坏=>112500无回踩，放弃。不得21:00首跳追价。
- **风险/退出**：计划止损109950；日收<109600或LME<14400且curve转contango为逻辑失效。TP1=112800，TP2=115500；2日不扩张退出，最长5日。试仓计划风险NAV 0.25%—0.50%；期货最大损失不由结构限定。
- **参数/交割**：LTD=2026-11-16，需在10月底前评估滚至CU2612，禁止进入交割月被动持有。当前仓库未验证multiplier/tick/tick value/margin/price-limit/night-session字段，名义、1/2板压力损失与保证金不填；参数未确认前执行状态保持“待参数”。
- **最坏/放弃**：LME反转、人民币急变、夜盘低流动gap、交易所临时提保；若无法核参数或当前价差报价，放弃。

### 2. AG2612条件空｜`COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012`

- **事实**：close/settle=14816/14854；高低14995/14679；中国close +2.07%，但ΔOI=-2376、near-next -0.90% contango；之后金银下跌、DXY上升。
- **定价/分歧/反证**：市场白天定价反转修复；分歧是海外回落若在21:00传入，contango可放大中国日盘涨幅的回吐。最强反证是中国价格层仍强、地缘风险和银的工业属性可能快速反转。
- **支持层**：①价格层反对；②curve支持空；③Physical缺；④外盘/美元支持空；⑤Options缺。两层有效。
- **表达**：首选AG2612期货小规模条件空；put spread只研究，不给strike/权利金/Greeks，固定免责声明：`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/情景**：21:30后同时满足AG<14700、COMEX银≤60.5且反抽14700—14800失败。好=14700附近失败；中=14650下破回抽；坏=<14400首跳，放弃追空。
- **止损/失效/退出**：止损15020；AG重回14995上且银>61.3为逻辑失效。TP1=14400、TP2=13950；1日不扩张退出，最长3日。试仓风险NAV 0.25%，与AU/美元同因子合并。
- **参数/压力**：稳定合约规格参考15千克/手，按14816名义约222240元/手；LTD=2026-12-15。当前仓库未返回tick、动态保证金和限幅，tick value及1/2板压力不可靠；11月底前滚动，实物交割风险不可忽略。期货最大损失不有限。
- **旧观点处置**：旧AG多头不再加仓；若此前按条件建立，14700下破应优先退出而非直接反手。没有成交反馈，不声称已有多头。

### 3. MA701条件空｜`COM-E-MA701-POSTSPIKE-REVERSAL-SHORT-20261012`

- **事实**：open/high/low/close=3327/3384/3176/3229，close相对pre-settle -2.77%，5D仍+11.01%；OI773423、ΔOI+12248，价跌仓增仅作归因线索；curve仍+13.88% backwardation。
- **定价/分歧/反证**：市场从短缺/挤仓转向高波动消化；分歧是若3176失守且backwardation明显收窄，post-spike unwind可能延续。最强反证就是当前近端结构仍极强，低位追空可能遭逼仓。
- **支持层**：①价格量仓支持空；②curve反对；③Physical仅C级context；④油价下跌间接支持；⑤Options缺。两层有效。
- **入场/成交情景**：21:45后，MA<3176并回抽不越3200，且near-next由+13.88%收窄至<+10%。好=3160—3180失败；中=3150下破回抽；坏=<3050首跳，放弃。
- **风险/退出**：止损3255；价格重回3320或backwardation恢复>+15%为逻辑失效。TP1=3050、TP2=2920；1日不扩张退出，最长3日。试仓风险NAV 0.25%；与油品/化工空头合并计算。
- **参数/压力**：10吨/手、tick 1元/吨、tick value 10元；按close名义32390元/手，仓库保证金率7%约2267元/手，限幅6%。按close简单估算1板约1943元/手、2板约3887元/手，不含扩板、滑点或提保；LTD=2027-01-14，夜盘有交易，当前交割风险低但需滚动。期货止损不是最大损失。
- **旧观点/放弃**：晨间多头止损与失效均被收盘验证；若curve不收窄、油价反弹或无法取得实时near-next，放弃新空，不机械反手。

## 八、商品期权专项

- **样本状态**：10月12日根模块有13604条但状态empty；统一层仅10月9日185 series，181 surface-ready、41 positioning-ready、0 execution-ready。由于T日应有截面缺失，10月9日只作历史背景；LC、MA、AG标的已大幅移动，旧ATM/Delta不可比。
- **IV-RV**：本期不输出新的ATM IV、RR25、BF25、term或IV-RV结论；旧截面不能冒充T日曲面。RV20仍可用于期货波动尺度，但不与落后IV建立错价。
- **event convexity**：美国CPI、IEA与油品地缘风险提高有限凸性的研究价值；没有当前bid/ask与净支出，就不能证明期权优于期货，也不能给盈亏平衡或净R。
- **定位/拥挤**：positioning仅历史局部且OI coverage不足；不使用PCR/OI推断机构方向，不推dealer Gamma。
- **回避项**：所有裸卖波、近到期SC/CF等旧series、无当前报价的跨品种vol RV；若需结构，先重新取得目标underlying×expiry×strike双边报价、成交量/OI、行权交割与当前Greeks。

## 九、21:00夜盘开盘风险地图

四层严格分开：①10月12日中国EOD；②属于10月12日的早前Night只有RU exact-close回退，其余缺失；③15:00后海外新增；④今晚21:00尚未发生、归属10月13日交易日。LC/A/C/EC等无夜盘品种，下一实际窗口为10月13日09:00。

| 品种 | T日EOD | 早前Night历史分解 | 15:00后海外 | 下一夜盘预期 | 首跳/等待 | 核心确认 |
|---|---|---|---|---|---|---|
| CU | +0.93%，curve正 | missing | LME铜强、美元强形成次级冲突 | 偏高开，部分已被日盘预交易 | 不追；30分钟 | 111100、LME14600、near-next |
| AG/AU | 日盘反弹；AG contango | missing | 金银回落、DXY强 | 偏低/平低 | 不反手；30分钟 | AG14700/14995、银60.5、USD/CNH |
| SC/BU | SC近平、BU大跌；均backwardation | missing | 油价约-0.6%至-0.8%，但地缘尾部在 | 偏低开、高波动 | 不追空；45分钟 | WTI91、SC695.3、curve、裂解/装船事实 |
| MA/PX/TA/EB | MA日盘大幅反转 | missing | 油价偏空但非exact成本映射 | 偏低/高波动 | 45分钟 | MA3176与curve<+10%、化工链共振 |
| RU/NR | 日盘强但RU相对夜收-1.62% | RU仅close可比 | 无新SICOM exact | 平开偏弱 | 30分钟 | RU20525/21005、contango、NR联动 |
| JM | 日盘+1.88%、backwardation | missing | 无exact锚 | 平高开/震荡 | 30分钟 | 1533/1572、curve、ΔOI |
| LC | close -11.79%，curve强 | 制度上无夜盘 | 无exact锚 | 不适用 | 10/13 09:00等45分钟 | 104680、curve、库存/仓单 |
| A/C/EC | A/C上涨、EC未入热图 | 制度上无夜盘 | CBOT仅当前值，运价未对齐 | 不适用 | 10/13 09:00等45分钟 | exact外盘变化、基差、curve |

若21:00 gap超过当日RV尺度或一档有效限幅，所有静态价位自动失效；重新报价后再按15/30/45分钟规则判断。

## 十、未来24h / 7d事件

| 北京时间 | 事件 | 处理 |
|---|---|---|
| 10/12 21:00 | 下一中国夜盘，归属10/13；FU/BU指定合约日内开仓限额生效 | 不追首跳；油品流动性/滑点按非线性压力处理 |
| 10/12收盘后起 | SC/LU/FU/BU新保证金与涨跌停参数生效 | 已过结算；今晚持仓按新参数重算，不能沿用日盘前风险预算 |
| 10/14 16:00—17:00 | IEA Oil Market Report October 2026发布活动 | 油品减Delta，未报价期权不卖Vega；以有限凸性或延迟入场应对。[IEA](https://www.iea.org/) |
| 10/14 20:30 | 美国CPI（Reuters日历） | 金银、铜、美元高跳空风险；数据前缩仓或结构限损 |
| 10/14 22:30附近 | EIA周度石油状态报告，常规周三10:30 ET，假日可能调整 | SC/BU/FU/LU不在发布前追单；先核官方时间。[EIA release](https://ir.eia.gov/) |
| 10/15 20:30 | 美国PPI与零售销售（Reuters日历） | 再评实际利率/DXY与贵金属；等待首轮波动 |
| 未来1—7日 | 智利Centinela/Escondida劳资进展、中国刺激落地 | CU多头看供应事实与中国需求，不以标题替代库存/订单 |
| 未来7日 | CFTC、USDA/天气、交易所临时参数、矿山/炼厂/化工装置 | 发布前后减仓；无精确官方时点者标“待核”，不编日历 |
| 公司层 | 紫金/宝钢下一正式披露或交易状态核验 | 股票只在A股开市且当前quote/ADT/状态可验证后比较，不把旧半年报当新催化 |

风险预算：试仓计划最大损失NAV 0.25%—0.75%，确认交易0.75%—1.50%，单一高确信主题总风险预算≤2.5%—3.0%；这不是保证最大亏损。CU/AG与美元/中国刺激同因子、MA/SC/BU与能源同因子须合并。压力测试1/2涨跌停、相关性破裂、流动性消失、夜盘gap、提保、IV升/塌、交割挤压、人民币急变及中国休市时海外大动。

## 十一、覆盖核对、输入版本与缺口

| 板块 | 应覆盖 | 实际取得且已分析 | 数据不足 | 不适用/流动性不足 | 未入榜异常/无异常依据 |
|---|---|---|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/9价格/量仓/curve | DCE参数/期权；实体多为C级 | 0 | JM价曲强但OI下降；FG/SA量仓异常未获实体/期权确认 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | T日期权、部分动态参数/实体 | 0 | CU入榜；SN +1.74%但5D弱，AG内外冲突 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 22/22 | SC/LU Physical；多数exact Night；部分期权/参数 | 0 | RU/NR强但日内回吐；BU/PX/EB跌幅大，curve反对追空 |
| 新能源/动态GFEX | LC/SI/PS及PT/PL/BZ等动态品种 | 引擎可用品种全扫 | GFEX参数源日未验证、仓单/期权执行 | 0 | LC为最大异常；PL 5D+12.19%但roll/历史可比性限制 |
| 农产品/油脂/饲料/畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 18/18 | DCE期权、部分physical、exact海外变化 | 0 | A/C价仓同升但curve/海外不确认；LH/JD跌价增仓仅线索 |
| 航运软商品 | EC及相关CF/SR/AP/CJ/PK | 6/6 | EC运价口径和期权不足 | 0 | EC 5D-4.46%、deep contango，未见足够反转证据 |
| 动态/低流动 | 引擎77品种 | 72个具备完整可比状态 | JR/PM/RI/WH/ZC历史/流动性不足 | 5 | 缺失保留在覆盖记录，不解释为无机会 |

固定清单与动态上市品种均完成可得数据初筛；仪表盘只展示12项。策略类别已扫描方向、基差/跨期、curve、跨品种/跨市场、产业链RV、中性组合、IV/skew/term/event convexity；因basis C、import parity不完整与期权执行缺失，本期没有可执行套利或定义完整的中性basket。周期1D/3D/5D/20D均扫描，历史不足者不输出伪指标。

关键输入版本：
- [China-Commodities-Engine@2b08a42](https://github.com/farfromexact/China-Commodities-Engine/tree/2b08a42cfe8285fa943c4827a6456127a42b0c77)
- [China-Stock-Engine@5f80b92](https://github.com/farfromexact/China-Stock-Engine/tree/5f80b92eb79694253cfc276b59a3e1688f171f79)
- 前序：[2026-10-12晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/4732637b52a5a93c737ce63f305052e459e3cfdc/reports/2026/10/2026-10-12_commodities_morning.md)；最近同版：[2026-10-11晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/4732637b52a5a93c737ce63f305052e459e3cfdc/reports/2026/10/2026-10-11_commodities_evening.md)。

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：CU2611待21:30突破回踩111100且LME≥14600；AG2612与MA701只在21:30/21:45满足双重确认后人工下单，不预挂首跳单。
C. 今晚应继续观察的机会：LC价跌—backwardation冲突、RU夜涨日间全回吐、油品海外下行与地缘/近端结构冲突，以及紫金/宝钢利润通道能否由后续公司数据量化。
D. 今晚必须避免或退出的交易：避免LC抄底/追空、能源首跳、所有无T日bid/ask期权；若此前按条件建立MA多头应按原失效位退出，AG多头跌破14700则退出而非机械反手。