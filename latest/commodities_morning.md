# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-11

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-11 07:14 BJT；信息截点：07:00 BJT；最近完整中国EOD：9月10日；今晨已完成Night归属交易日：9月11日；下一实际交易窗口：今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC/FU获三层支持但已大幅跳升，CU/AG旧多头被宏观与政策重定价否定，09:00两边都不追。**

当前regime：**中东供给中断与美国通胀黏性并存，能源进入高波动backwardation，有色/贵金属遭利率与铜关税预期反转，农产品等待WASDE。**

最接近触发的是SC2610、FU2611和CU2610反抽失败空；分别缺少09:00后回撤接受、23:00后外油尾段的国内再确认，以及低开后反抽失败。研究机会存在，但当前报价和触发均未发生。

## 二、数据质量与覆盖

本期优先读取[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、逐合约Night、Options quality/surface及metadata。

- 统一输入：schema v2，`requested_date=2026-09-10`，9月11日06:18:48生成。
- Futures/Market State：9月10日五所802个合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；7条placeholder已排除。20个交易日同合约历史完整；无跨主力拼接。
- Night Session：`trading_date=2026-09-11`、`night_session_date=2026-09-10`，06:00:37生成；fresh、validated、published、`coverage_complete=true`。598个有效合约、55个品种；191个合法outside-window、13个制度性no-night-trade；missing timestamp/price/quote、query error、unresolved contract均为0，coverage warnings为空。74.56%是有有效夜盘记录的合约占比，不是完整率。
- Physical：20项目标中18项按原生频率fresh，SC/LU unavailable；无stale target。所有basis为C级，仅作context；仓单有5条沿用，不能冒充本期新增实体确认。
- External：22项目标中17项按原生频率fresh，5项unavailable；全部`context_only`，不构成exact import parity或可执行跨市场套利。
- Options：9月10日19,238条chain、353个series、52/64产品；12个失败产品为BC/SC及AD/AG/AL/AO/AU/CU/NI/PB/SN/ZN。IV覆盖97.67%、OI覆盖69.73%、bid/ask覆盖0；342个series surface-ready、84个positioning-ready、0个execution-ready。HC/SS/LU上市首日尚未进入当前64品种期权覆盖清单，也没有可验证执行报价，单列为新增覆盖缺口。
- Metadata：partial；有效合约匹配73.32%，multiplier/tick/margin/limit覆盖约29.80%，Night session字段覆盖为0。前三卡静态规格以交易所合约规则补充，动态保证金与涨跌停仍须下单前确认。

## 三、商品仪表盘

1D/5D为9月10日同一合约结算收益；Night为归属9月11日的已完成连续交易，涨跌以相对9月10日close为主、settlement为辅。S/P/E表示surface/positioning/execution readiness。basis均为C级context；Physical栏只列可支持程度，不把仓单当社会库存。

| 板块 | 品种/合约 | EOD close/settle；1D/5D | EOD量/OI/ΔOI；curve | Night close；vs close/settle；ΔOI；时间 | Physical/07:00海外 | S/P/E；09:00信号 |
|---|---|---|---|---|---|---|
| 原油 | SC2610 | 769.0/768.4；+6.35%/+11.22% | 23.19万/3.44万/-4,884；back 6.47% | 816.0；**+6.11%/+6.19%**；+2,022；02:30 fresh | repo实体缺；Brent 107.63 | N/N/N；等45m回撤 |
| 燃料 | FU2611 | 4044/4101；+4.25%/+6.13% | 97.58万/21.59万/+109；back 6.66% | 4248；**+5.04%/+3.58%**；+6,392；23:00 fresh | EIA小幅去库；WTI 102.48 | Y/Y/N；23:00后gap风险 |
| 芳烃 | EB2610 | 10307/10282；+5.07%/+7.52% | 169.64万/32.18万/+28,335；back 0.76% | 10370；+0.61%/+0.86%；-25,520；23:00 fresh | 油涨、国内弹性弱 | Y/Y/N；不追多 |
| 芳烃 | BZ2610 | 9227/9150；+5.11%/+9.36% | 11.33万/3.27万/+3,046；**contango 3.30%** | 9269；+0.46%/+1.30%；-4,433；23:00 fresh | 油涨；curve反对 | Y/N/N；高开放弃 |
| 聚酯 | EG2610 | 5917/5987；+3.15%/+3.03% | 232.73万/33.60万/-4,142；back 3.81% | 5968；+0.86%/**-0.32%**；-14,318；23:00 fresh | 油强、仅修复close | Y/Y/N；等45m |
| 聚酯 | TA701 | 6234/6258；+1.82%/+4.09% | 126.70万/113.12万/+1,310；back 5.86% | 6288；+0.87%/+0.48%；+9,553；23:00 fresh | 油强；surface底价冲突 | Y/Y/N*；等45m |
| PX | PX611 | 9274/9292；+2.67%/+5.74% | 36.12万/17.25万/+6,384；contango 4.61% | 9328；+0.58%/+0.39%；-6,667；23:00 fresh | 油强；curve反对 | Y/N/N*；不追 |
| 有色 | CU2610 | 112200/111730；+0.55%/+2.94% | 11.21万/23.41万/+5,529；back 0.61% | 108360；**-3.42%/-3.02%**；-29,555；01:00 fresh | 铜关税决定推迟 | N/N/N；反抽失败空 |
| 贵金属 | AG2610 | 16418/16425；+1.76%/+2.91% | 63.09万/18.93万/-8,092；近乎平坦 | 15593；**-5.02%/-5.07%**；+4,249；02:30 fresh | COMEX银64.19、-4.6% | N/N/N；低开不追空 |
| 有色 | AL2610 | 24490/24575；+0.06%/+1.24% | 14.44万/23.64万/-10,624；轻contango | 24125；-1.49%/-1.83%；-18,111；01:00 fresh | 美元/收益率上行 | N/N/N；跟随弱 |
| 有色 | ZN2610 | 27475/27650；+0.60%/+3.83% | 17.82万/14.67万/-10,551；轻back | 26760；-2.60%/-3.22%；-13,251；01:00 fresh | 全球金属重定价 | N/N/N；不抄底 |
| 黑色 | J2701 | 2136.5/2128.5；-1.64%/-1.37% | 4.93万/6.34万/-1,092；contango、roll flag | 2125；-0.54%/-0.16%；-1,949；23:00 fresh | 无exact外盘 | Y/P/N；弱但不追空 |
| 建材 | FG701 | 964/962；-0.82%/-0.31% | 138.06万/119.62万/-15,114；contango 5.85% | 982；+1.87%/+2.08%；-31,124；23:00 fresh | 仓单仅部分覆盖 | Y/Y/N*；反转待确认 |
| 油脂 | P2701 | 10165/10177；-1.25%/-0.91% | 82.55万/59.05万/-12,710；微back 0.28% | 10228；+0.62%/+0.50%；-896；23:00 fresh | 外盘仅context | Y/Y/N；区间观察 |
| 饲料 | M2701 | 3402/3399；+0.06%/+0.38% | 148.49万/278.55万/-27,369；近乎平坦 | 3440；+1.12%/+1.21%；+18,959；23:00 fresh | 中国采购美豆约100万吨 | Y/Y/N；WASDE前等30m |

`*`：TA/PX/FG的surface底层underlying settlement与核心期货快照不一致，虽模块标ready，本期不使用其IV数值或作为支持层。

07:00附近海外最新完整时段：Brent 9月10日结算**107.63美元/桶（+6.34%）**、WTI **102.48（+6.69%）**；油轮袭击和航运中断是主催化。EIA原油库存仅下降39.1万桶至4.241亿桶，小于预期，OPEC同时下调2026需求增速，是多头反证。[Reuters油市，2026-09-10](https://www.reuters.com/business/energy/brent-holds-above-100-tanker-attacks-deepen-supply-fear-2026-09-10/)

美国8月PPI环比+0.4%、同比+5.4%，美元与长端收益率上行；黄金约4355.85美元/盎司、白银64.19美元，分别跌约1.0%和4.6%。[Reuters PPI](https://www.reuters.com/business/us-producer-prices-increase-expected-august-2026-09-10/)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-edges-higher-weaker-dollar-us-inflation-data-focus-2026-09-10/)

## 四、相比上一期真正变化

1. **晚报的数据缺口已补齐。** 9月10日EOD现已五所完整、802/802同日验证；这是一项数据状态变化，不是市场涨跌。晚报Revision 2只作修订对照，本期重新使用统一输入而非继承文字。
2. **SC/FU由事件观察升级为三层方向确认，但赔率进一步下降。** 9月10日EOD分别+6.35%/+4.25%，curve均深back；今晨又相对close上涨6.11%/5.04%，海外油结算同向。SC EOD ΔOI显著减少、EIA去库小于预期和OPEC需求下修是反证。
3. **EB/BZ没有复制原油的新增弹性。** 两者EOD约+5%，今晨却只相对close +0.61%/+0.46%，且Night ΔOI下降；BZ仍为深contango。油价上涨不再等于整条化工链可追。
4. **CU旧多头逻辑被政策预期反转否定。** 9月10日EOD尚为价涨仓增与back，但白宫推迟精炼铜关税决定，今晨CU2610相对close -3.42%、ΔOI -29,555。关税预期此前推动囤库，当前最强竞争解释是拥挤溢价回吐，而非中国实体需求突然坍塌。[Reuters铜关税](https://www.reuters.com/world/us/white-house-copper-tariff-plan-stalls-amid-affordability-concerns-sources-say-2026-09-10/)
5. **AG“银强金弱多”完全失效。** AG2610今晨-5.02%，外盘白银-4.6%，PPI、美元和收益率三者同向压制；黄金信用主题本期仍不成立。options链又缺AG，不能用有限损失结构替代执行缺口。
6. **豆粕出现独立观察线索。** M2701 Night +1.12%且OI增加；Reuters称中国本周采购约100万吨美国大豆，USDA确认其中34万吨，但WASDE临近、EOD curve近乎平，仍只有两层支持。[Reuters美豆采购](https://www.reuters.com/world/china/china-buys-1-million-tons-us-soybeans-ahead-xi-visit-sources-say-2026-09-10/)

旧建议处置：

- `COM-E-SC2610-GAP-20260905`：延续为回撤接受多；新数据为9月10日EOD、SC exact Night与外油确认。此前触发路径unknown，不假设已成交。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：延续但触发区上移；此前日盘是否完成“回撤—重上”路径unknown。
- `COM-M-CU2610-LME-RECORD-20260909`：**观点失效**；原因是政策信息与价格变化。若此前确已按条件建立，09:00下一流动窗口按原失效纪律退出，不把旧多头悄悄改名为持有。
- `COM-M-AG2610-SILVER-BREADTH-20260910`：**观点失效**；若此前确已建立，下一流动窗口退出。新空头研究使用新idea_id，不冒充原观点延续。
- `COM-E-EB2610-DAY-REVERSAL-20260909`：降级至观察；Night新增弹性与curve确认不足。
- `COM-M-MA610-SETTLE-RECLAIM-20260908`：主力已转MA701，而Night代表仍为MA610，正式合约不可比，本期停止执行参数更新。

## 五、产业链地图

- **最强：SC—FU供应冲击链，偏多，置信度中高。** 价格/OI、EOD backwardation与海外油形成1/2/4三层支持；SC/FU Night相对close均是真新增，不是相对结算重复计价。最大缺失是SC/LU实体序列、Night near-next第二腿和当前期权报价；OPEC需求下修与EIA小幅去库是竞争解释。
- **最弱新增弹性：BZ—EB—EG—PX，方向混合，置信度中。** EOD补涨强，但Night相对close只有0.46%—0.86%，OI普遍下降；BZ/PX contango反对近端短缺。单日成本推动不能直接解释为实体供需牛市。
- **有色—贵金属：战术偏空，置信度中。** CU/AL/ZN与AG Night同步下跌；CU有政策催化，AG有PPI/美元/收益率与外盘确认。反证是EOD铜back和结构性电气化需求仍在，低开追空赔率差。
- **黑色—建材：相对弱但无趋势空确认。** J/JM延续弱，FG却Night反弹1.87%；curve和OI冲突，更像挤压/回吐而非统一需求信号。
- **农产品：M相对最强，置信度中低。** 采购新闻和Night量仓支持，P/OI仅修复；WASDE、天气与南美供应决定下一步。缺高质量进口利润与实体库存，不能称跨市场套利。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2610回撤接受多 | 23/12/19/13/8 | **75** | 1、2、4 | 存在待验证优势｜部分｜等45m |
| 2 | FU2611产品链延续多 | 22/14/18/12/8 | **74** | 1、2、4 | 存在待验证优势｜部分｜等45m |
| 3 | CU2610关税溢价回吐空 | 20/17/15/8/9 | **69** | 1、4 | 存在待验证优势｜部分｜反抽失败才空 |
| 4 | AG2610通胀重定价空 | 20/16/15/9/9 | **69** | 1、4 | 存在待验证优势｜部分｜低开不追 |
| 5 | M2701采购/WASDE观察多 | 19/16/14/9/10 | **68** | 1、4 | 存在待验证优势｜部分｜等30m/事件前减仓 |

分项总和已复核，且不超过各自上限。分数只是研究排序，不是胜率、预期收益或仓位指令。SC/FU属于同一供应冲击因子；CU/AG同属美元—实际利率与拥挤回吐因子。CU/AG/M只有两个独立支持层，严格封顶69分。没有任何候选满足当前报价、触发与赔率三项，因此没有立即新仓。

## 七、前三名交易卡

### 1. SC2610｜75｜回撤接受多

**事实：** 9月10日EOD 769.0/768.4；前一段Night close 773.1，日盘相对其约-0.53%，说明白天没有继续扩张。今晨exact Night OHLC 815.0/819.4/786.5/816.0，+6.11% vs close、+6.19% vs settlement，ΔOI +2,022。EOD back 6.47%；当前Night第二腿未从紧凑层取得，不伪造Night curve。

**市场定价：** 持续航运中断已经进入双位数两日涨幅。**分歧：** 若09:00能消化gap且守住800上方，现货替代采购与运费压力仍可能使back维持；若直接高开扩张，剩余赔率不足。**最强反证：** EOD减仓、OPEC需求下修、EIA去库不及预期，以及任何停火/航道恢复headline。

- 最佳工具：SC2610期货；SC期权本期失败，不能用无报价结构假装有限损失。
- 好成交：等待45分钟，800—812承接并重新站上816/VWAP，先1/3仓。
- 中成交：突破819.5后成功回踩816，仓位为好成交的一半。
- 坏成交：直接高于835、接近涨停或止损距离超过计划1R，放弃。
- 计划止损：45分钟接受786.5下方；逻辑失效为跌破769、back显著收窄且Brent回落至104以下。
- 退出：TP1 835或+1.5R减半；TP2 865或+3R再减；1个交易日不扩张即退出，20:30美国CPI前降风险。
- 成本/滑点：限价；总滑点超过计划1R的10%减半，超过20%放弃。
- 风险：0.25%—0.40% NAV；与FU/BZ/EB/EG合并。期货最大损失不由计划止损限定。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；按Night close名义约81.60万元/手；21:00—次日02:30有夜盘；最后交易日2026-09-30、实物交割。[INE合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/) 动态margin/limit未确认，最迟9月18日前复核移仓SC2611。
- 压力：一板=`816000×L`，两板=`816000×[1-(1-L)^2]`；相关性破裂、保证金上调和航道headline均可能使实际损失越过止损。

### 2. FU2611｜74｜产品链延续多

**事实：** EOD 4044/4101；前一段Night close 4119，日盘相对其约-1.82%，白天发生reversal。今晨exact Night 4268/4300/4201/4248，+5.04% vs close、+3.58% vs settlement，ΔOI +6,392；EOD back 6.66%。FU在23:00收盘，未覆盖之后外油完整尾段。

**市场定价：** 产品紧张和原油风险已显著抬价。**分歧：** 若09:00没有因23:00后外油而失控高开，且产品仍强于SC，back可能延续；若首跳过度补价，赔率迅速转坏。竞争解释是纯粹油价beta而非独立成品油短缺。

- 最佳工具：FU2611期货；期权surface可研究但bid/ask覆盖为0。
- 好成交：等待45分钟，4210—4240承接并重上4248/VWAP，先1/3仓。
- 中成交：突破4300、回踩不破4280，仓位减半。
- 坏成交：直接高于4350或SC/FU breadth分裂，放弃。
- 止损：45分钟接受4190下方；逻辑失效为跌破4101且FU back明显收窄、Brent跌破104。
- 退出：TP1 4380或+1.5R；TP2 4550或+3R；1—2日时间止损，CPI前减仓。
- 风险：0.25%—0.35% NAV；不得与SC同时满额。滑点超过1R的20%放弃。
- 参数：10吨/手，tick 1元/吨，tick value 10元；名义约4.248万元/手；21:00—23:00有夜盘；最后交易日2026-10-30、实物交割。静态规格参照[SHFE燃料油合约](https://www.shfe.com.cn/eng/Market/Futures/Energy/fu_f/ContractText/)，动态margin/limit未确认。
- 压力：一板=`42480×L`，两板=`42480×[1-(1-L)^2]`；计划止损并不限制极端gap损失。

### 3. CU2610｜69｜关税溢价回吐空

**事实：** EOD 112200/111730，ΔOI +5,529，back 0.61%，仍是旧多头结构；前一段Night close 111910，日盘相对其+0.26%。今晨exact Night 108500/109090/108180/108360，-3.42% vs close、-3.02% vs settlement，ΔOI -29,555。

**市场定价：** 关税囤库溢价被快速回吐。**分歧：** 政策决定推迟可能使拥挤溢价继续压缩，但EOD back说明真实全球紧张尚未被证伪。故这里只研究失败反抽，不做无条件趋势空。

- 最佳工具：CU2610期货；CU期权本期失败，无法核实有限损失call/put spread成本。
- 好成交：等待45分钟，108800—109200反抽失败后再破108300，先1/3空。
- 中成交：跌破108180后回抽不过，仓位减半。
- 坏成交：直接低于107500，放弃追空。
- 止损：45分钟接受109600上方；逻辑失效为重上110400、国内curve继续扩大back且LME铜收复新闻前水平。
- 退出：TP1 106500或+1.5R；TP2 103500或+3R；1—3日时间止损，20:30 CPI前减仓。
- 风险：0.25%—0.40% NAV；与AL/ZN/AG合并。相关性反转和政策headline可令空头越过止损。
- 参数：5吨/手，tick 10元/吨，tick value 50元；名义约54.18万元/手；21:00—次日01:00有夜盘；最后交易日2026-10-15、实物交割。[SHFE铜合约](https://www.shfe.com.cn/eng/Market/Futures/Metal/cu_f/ContractText/) 动态margin/limit未确认。
- 压力：空头一板=`541800×L`，两板=`541800×[(1+L)^2-1]`。证据只有1、4两层，不能提高为确认仓。

## 八、商品期权专项

最新有效截面为9月10日EOD；今晨能源与金属大幅变动，所有moneyness、Delta和当前成本必须在09:00后重算。

| Underlying/expiry | ATM IV / RV20 | IV-RV | RR25/BF25 | S/P/E | 研究结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 58.89% / 41.21% | +17.68vol | -0.39/+0.86 | Y/Y/N | 事件波动已贵，无报价不卖vol |
| EB2610/09-16 | 42.51% / 29.17% | +13.34vol | +4.71/+2.36 | Y/Y/N | 短期限event convexity贵 |
| BZ2610/09-16 | 46.54% / 30.26% | +16.27vol | -3.04/+2.59 | Y/N/N | positioning不足，不执行 |
| M2701/12-16 | 15.49% / 9.70% | +5.80vol | +4.39/+1.12 | Y/Y/N | WASDE前只作曲面观察 |
| P2701/12-16 | 16.77% / 12.81% | +3.95vol | -24.62/+16.53 | Y/Y/N | skew极端，须人工复核 |

SC/CU/AG等12个产品chain失败；TA/PX/FG虽标surface-ready，但underlying settlement与核心期货不一致，本期隔离。HC/SS/LU首日无已验证series。Dealer Gamma方向未知；不得输出Gamma squeeze、权利金、净成本、当前Greeks或胜率。

结论：**期权没有优于裸期货的可执行证据。**若盘中取得人工实时链，可优先比较SC/CU有限损失价差；在报价、Delta、行权交割和最大净支出核实前，全部保持`research only`。

## 九、9:00开盘风险地图

| 品种 | Previous China EOD → Current Night → 07:00 Overseas | 是否已定价/冲突 | 追价与等待 | 开盘确认 |
|---|---|---|---|---|
| SC | EOD +6.35% → Night +6.11% → Brent +6.34% | 大部已定价，三层同向 | 不追；45m | 786.5/800/816/819.4、back、Brent |
| FU | EOD +4.25%但日盘回吐 → Night +5.04%至23:00 → 外油后段仍强 | 可能尚有23:00后gap | 不追；45m | 4201/4248/4300、产品强于SC |
| EB/BZ | EOD约+5% → Night仅+0.5% → 外油强 | 新增弹性低，内外冲突 | 不追；45m | EB 10278/10370；BZ contango |
| EG/TA/PX | EOD涨 → Night仅+0.6%—0.9% → 外油强 | 国内只部分跟随 | 不追；45m | settlement、OI、curve breadth |
| CU | EOD↑/back → Night -3.42% → 铜关税预期反转 | 大部已定价，结构反证仍在 | 不追空；45m | 108180/108360/109090、curve |
| AG/AU | EOD银强 → AG Night -5.02% → 外银-4.6%、金-1% | AG基本完成重定价 | 不追空；30—45m | AG 15566/15593/15878、收益率 |
| AL/ZN | EOD混合 → Night -1.5%/-2.6% → 美元/收益率↑ | 跟随宏观弱势 | 不抄底；30m | Night low、CU breadth |
| J/JM/RB | EOD偏弱 → Night继续弱 → 无exact外盘 | 结构不一致 | 不追空；30—45m | OI、钢材breadth、curve |
| FG/SA/V | EOD弱 → FG反弹 → 无可靠海外 | squeeze与contango冲突 | 两边不追；30m | FG 978/982/1010、OI |
| M/P/OI | EOD平/弱 → M +1.12%、P修复 → 美豆采购/WASDE | 部分定价 | 不追；30m | M 3401/3440/3442、豆油联动 |
| AP/JD/LC/SI/PS/SF/SM | 无制度Night | 未定价 | 等30—45m | EOD区间、量仓与实体更新 |

能源与金属的开盘风险方向相反，但都不适合第一跳：SC/FU的主要风险是高开后流动性消失；CU/AG的主要风险是低开后反抽。CPI在20:30 BJT构成第二次美元、实际利率与商品风险重置。

## 十、未来24小时与7日事件

- **9月11日09:00：** 中国日盘验证能源gap接受和金属低开反抽；所有条件单等30—45分钟。
- **9月11日16:00：** IEA 9月Oil Market Report，官方安排巴黎10:00发布；SC/FU持仓提前降低Delta，关注需求预测与紧急库存安排。[IEA日程](https://www.iea.org/events/oil-market-report-september-2026)
- **9月11日20:30：** 美国8月CPI。能源、有色、贵金属在数据前降低方向和Vega；execution-ready=false时不以未报价期权博事件。[BLS CPI](https://www.bls.gov/cpi/)
- **9月12日00:00附近：** USDA 9月WASDE/Crop Production；M/Y/P/OI/C/CF避免无保护重仓。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **9月12日03:30附近：** CFTC COT，只作滞后拥挤背景，不推断交易者实时身份。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **9月15—16日：** 美联储会议窗口；PPI已将加息概率推高，CPI会决定实际利率方向。AU/AG/CU和油价—通胀主题合并计算风险。
- 持续监控霍尔木兹/曼德海峡航运、油轮损失、沙特设施、停火与替代供应。headline改变分布，不自动提供入场价。[Reuters油市](https://www.reuters.com/business/energy/brent-holds-above-100-tanker-attacks-deepen-supply-fear-2026-09-10/)
- SC2610最后交易日9月30日；最迟9月18日前复核移仓、保证金和交割资格，避免事件仓演化为交割风险。

## 十一、覆盖、风险、台账与归档核对

强制63个代码全部完成9月10日EOD、1D/3D/5D/20D、量仓、curve和方向/跨期/基差/跨品种/跨市场/风格中性/波动率/偏度/事件凸性扫描；动态有效品种PL/BZ/LG/RR/PD/PT/OP/WR另行纳入，共71个实际取数并分析。JR/PM/RI/RS/WH/ZC因零价、零量、零OI或制度性低活跃列为不适用/流动性不足，不从应覆盖清单删除。

- 黑色建材9/9：FG Night反转是未入榜最值得跟踪异常；J/JM弱但curve不统一。
- 有色贵金属12/12：CU/AG进入正式榜；AL/ZN确认宏观弱势，AU因主力与Night代表月份不一致不做具体卡。
- 能源炼化化工25/25：SC/FU入榜；EB/BZ/EG/PX的Night弹性衰减是板块核心反证。
- 新能源及GFEX新材料全部扫描：LC/SI/PS无Night，仓单沿用限制实体结论。
- 农产品油脂饲料畜牧22/22：M为最值得跟踪异常；P/OI只修复，WASDE前无三层共振。
- 航运及软商品全部扫描：无exact跨市场映射或三层方向优势。
- 期权应覆盖64个、实际52个；12个失败、0个执行就绪；新增HC/SS/LU尚未形成可验证readiness。
- 数据不足集中于SC/LU Physical、A级/B级basis、exact import parity、完整仓单、Night near-next第二腿、12个期权产品、全部期权执行报价与partial metadata。

风险预算：单笔试仓0.25%—0.40% NAV；确认交易需额外实体/报价与价格确认后才可提高至0.75%—1.0%。SC/FU/BZ/EB/EG/TA/PX按同一供应冲击合并；CU/AL/ZN/AG按美元—实际利率/拥挤回吐合并。压力测试包含1/2个涨跌停、流动性消失、保证金上调、航运headline反转、人民币急变、CPI和周末停牌期间海外跳变。

本报告按固定六路径发布；`archive_status=success`仅在main回读历史MD/JSON、latest、status及manifest且本期记录恰好一条后成立；CI仅作push后独立校验，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2610等45分钟在800—812承接并重上816，或FU2611在4210—4240承接并重上4248；两者合并风险、均先1/3仓。  
C. 今天应继续观察的机会：CU2610反抽失败空、AG2610通胀重定价空、M2701美豆采购/WASDE、EB/BZ Night弹性衰减及HC/SS/LU新期权流动性。  
D. 今天必须避免或退出的交易：09:00追SC/FU首跳、低开追空CU/AG；若此前确已建立则退出已失效CU/AG旧多头；禁止把相对结算涨跌重复计价或在execution-ready=false时臆测期权成本。
