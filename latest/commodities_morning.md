# 全球商品期货期权高风险机会雷达｜晨间版｜2026-10-01

`prompt_version=radar_2026-09-06_coverage_v1` · `data_protocol_version=china_commodities_v2`

## 一、今日一句话结论

> **今天的商品市场究竟有没有值得冒险的机会？截至本报告时点，无可立即执行的合格新交易；中国休市且9月30日EOD缺失，只保留橡胶、菜油及能源链的节后重报价观察。**

信息截点：2026-10-01 07:04（北京时间）。中国最近已验证完整EOD为2026-09-29；9月30日日盘本应存在但未入库。9月30日晚无夜盘，10月1日至7日休市；下一实际中国交易窗口为10月8日08:55集合竞价/09:00日盘，下一夜盘为10月8日21:00。所有下列中国价格均是历史锚，不是当前可成交报价。

最接近触发的观察项：①BR2611节后相对强势；②OI701节后相对强势；③能源链“美国燃料去库、原油累库、海湾出口恢复”分化。三者都必须在10月8日重新报价并观察30—45分钟，当前执行状态均为**休市/等待触发**。

## 二、数据质量与覆盖

实际读取：[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。四者同属main当前快照。

| 模块 | 实际观测/生成 | 读取状态 | 本期用途 |
|---|---|---|---|
| Futures | EOD 2026-09-29；生成9/30 08:07 | `ok_last_good`但落后于最新应得9/30 EOD | 仅历史锚；五所、806合约、77品种，source-date match 100%，critical errors 0，full_market_ready=true |
| Market State | 9/29，20日同合约指标 | `ok_last_good`；9/30缺失 | 1/3/5/20D、RV20、OI和curve均不冒充9/30变化 |
| Physical | requested 9/29；18/20 fresh，SC/LU unavailable | `ok_native_frequency` | 周/月度及仓单仅按原生频率沿用；5条GFEX仓单沿用且stale；basis均C级，只作context |
| External(repo) | 9/29；17/22 fresh | `ok_context_only` | 不作可执行进口套利；与07:00公开市场分层 |
| Night Session | trading_date=9/30，session_start=9/29；生成9/30 08:01 | `partial_last_legal_session` | 属于9/30已完成连续交易阶段，不是10/1夜盘；fresh/validated/published=true，coverage_complete=false |
| Options | 9/29；13,324 records、184 series | `research_only` | 180 series surface-ready、46 positioning-ready、0 execution-ready；bid/ask coverage=0 |
| Contract metadata | 9/29 | `partial` | effective match 73.45%；multiplier/tick/margin/limit覆盖约30.15%，缺失参数不推断 |

Night质量：`trading_date=2026-09-30`，`night_session_date=2026-09-29`，`generated_at=2026-09-30T08:01:30+08:00`，`data_fresh=true`，`validation_passed=true`，`published=true`，`coverage_complete=false`，423合约/37品种；outside-window 165、no-night-trade 4不自动视为错误；query/unresolved各214，是具体合约级缺口。整体可复盘，但Top卡只使用代表合约完全一致的记录。

关键限制：①9月30日日盘价格、OI、curve、仓单与完整期权截面缺失；②中国休市，无当前bid/ask；③Night detail文件此前为空，不能拼近次月Night curve；④dealer gamma方向未知；⑤价格/OI仅是归因线索。

## 三、商品仪表盘（展示11项；全范围扫描见覆盖核对）

EOD均为9月29日last-good；Night均为归属9月30交易日的已完成阶段。海外为截至10月1日07:04附近的最新结算/公开代理。

| 板块/品种 | 具体合约 | EOD close/settle；1D/5D | volume/OI/ΔOI | EOD curve；basis/实体 | Night close；vs close/vs settle；Night ΔOI | 07:00海外/期权 | 信号 |
|---|---|---|---|---|---|---|---|
| 合成胶BR | BR2611 | 15460/15390；-0.87%/+3.67% | 141,383/55,749/-13,960 | +1.10% backwardation；实体context | 16155；+4.50%/+4.97%；+8,194 | 无精确境外映射；期权research-only | 节后等45分钟，禁止追gap |
| 菜油OI | OI701 | 10057/10044；-0.89%/-1.39% | 216,312/274,068/-6,074 | +1.74% backwardation；C级basis | 10234；+1.76%/+1.89%；+6,681 | 外盘油脂未形成可执行映射；exec=0 | 等三油相对价差确认 |
| 原油SC | SC2611 | 711.9/716.9；-2.34%/-1.90% | 195,579/29,669/-2,741 | +1.94% backwardation；实体缺 | 705.2；-0.94%/-1.63%；-1,162 | WTI 90.42 +1.2%，Brent Dec 98.03 +1.9%；IV约74.7%，exec=0 | EIA后方向冲突，不追 |
| 燃油FU | FU2611 | 4438/4418；+0.64%/+4.54% | 641,064/150,615/-19,038 | +22.97% backwardation；C级basis | 4373；-1.46%/-1.02%；-5,144 | 燃料油代理不足；surface yes/exec no | 结构强、价格弱，等待重估 |
| 沥青BU | BU2611 | 5246/5195；+0.83%/-2.57% | 1,007,133/208,969/-15,138 | +11.76% backwardation；C级basis | 5142；-1.98%/-1.02%；-24,314 | 原油反弹但国内旧Night弱；exec no | 内外冲突，不交易 |
| 白银AG | AG2612 | 14848/14906；-1.79%/-8.25% | 299,463/277,181/+14,920 | -0.22% contango；实体缺 | 14958；+0.74%/+0.35%；+7,768 | COMEX银约60.59，日内约-0.9%；surface yes/exec no | 旧空单已过期，节后重建 |
| 黄金AU | AU2612 | 898.78/897.86；-1.56%/-5.06% | 237,449/225,820/-677 | -0.15%轻contango；实体缺 | 905.02；+0.69%/+0.80%；+1,932 | COMEX金约4155.6；DXY约101.17—101.47；exec no | 信用主题未获新方向确认 |
| 氧化铝AO | AO2701 | 2656/2658；-1.59%/-2.39% | 218,053/266,990/+34,128 | -0.61% contango；C级basis | 2662；+0.23%/+0.15%；-278 | 无精确外盘映射；surface/position yes，exec no | 旧空触发窗已过期 |
| 20号胶NR | NR2612 | 16410/16420；-3.07%/+2.95% | 56,274/75,544/+1,475 | -0.57% contango；实体context | 代表Night为NR2611=17070；不可直接分解NR2612 | 海外橡胶代理不足；surface yes/exec no | 合约不匹配，不作正式卡 |
| 天胶RU | RU2701 | 19010/19040；-2.13%/+1.14% | 254,432/132,155/-14,021 | +0.22% backwardation；实体context | 19665；+3.45%/+3.28%；+11,873 | 海外橡胶无精确映射；exec no | 与BR同向但curve分化 |
| 集运EC | EC2611 | 2845/2871.5；-1.17%/+10.40% | 20,962/24,626/-840 | -26.68% contango/roll flag | 无制度Night | 精确运价更新缺；无exec series | roll噪音高，不追 |

双收益锚的含义：BR/RU/OI相对close和settlement同向，早前Night确有新增强势；PX、TA等品种两锚曾明显分歧，说明close与settlement偏离，不把相对settlement涨跌误写成新增信息。因9月30日EOD缺失，无法计算Night→日盘follow-through，也无法确认Night curve。

## 四、相比上一交易日/今晨真正变化

1. **中国输入未更新**：四个第一层文件仍停在9月29日EOD/9月30日早前Night。9月30日日盘是应得而缺失，故所有基于日盘follow-through、最新OI、curve和仓单的结论降级；这不同于10月1日休市下无需新EOD。
2. **EIA形成“原油累库、燃料去库”分化**：截至9月25日当周美国商业原油+92.2万桶至4.273亿桶，汽油-170万桶、馏分油-230万桶。原油端是反对追多的证据，产品端是支持裂解/燃料紧张的证据。[EIA](https://www.eia.gov/petroleum/supply/weekly/)（发布9/30）。
3. **油价仍上涨**：WTI结算90.42美元/桶、+1.2%；Brent 11月103.50、+0.9%，更活跃12月98.03、+1.9%。市场把美伊谈判停滞、成品油紧张放在原油累库和海湾出口恢复之前；这增加节后gap风险，但不等于SC已经交易该信息。[Reuters](https://www.reuters.com/business/energy/oil-climbs-after-trump-denies-he-is-willing-ease-sanctions-iran-2026-09-30/)（9/30）。
4. **美元/贵金属未给清晰方向**：DXY在101.17—101.47附近、10年美债收益率约5.24%；COMEX金收约4155.6，银约60.59且弱于金。黄金信用与避险主题继续保留，但高实际/名义利率是强反证；不预设方向。
5. **农产品出现中国需求反证**：中国压榨利润弱、油厂大豆库存处高位，且美国大豆仍面临额外关税，削弱M/RM/Y链进口需求叙事。[Reuters](https://www.reuters.com/world/china/chinas-weak-soybean-demand-dims-prospects-us-cargoes-after-tariff-snub-2026-09-30/)（9/30）。

## 五、产业链地图

| 产业链 | 方向/最强最弱 | EOD→Night | curve/实体 | 期权/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 橡胶—轮胎 | 最强BR，RU次之；NR合约错配 | 9/29弱、9/30早前Night强，BR vs close +4.50% | BR/RU backwardation而NR contango，链内冲突；实体仅context | exec=0；无精确海外映射 | 9/30日盘、Night曲线、节后报价 | 中低 |
| 油脂—油料 | OI相对强；豆系需求偏弱 | OI Night +1.76%，但无9/30日盘确认 | OI backwardation；basis C级 | 中国大豆需求反证；三油外盘口径不完整 | OI/P/Y精确相对价差与9/30EOD | 中低 |
| 原油—炼化—芳烃 | 外盘原油与成品油强，国内旧Night SC/FU/BU弱 | 只能确认早前Night弱，不能确认日盘吸收 | SC/FU/BU均backwardation；SC/LU实体缺 | EIA燃料去库支持产品、原油累库反对；期权exec=0 | 9/30中国EOD、进口平价全口径 | 中 |
| 贵金属 | 金强于银；国内旧EOD均弱 | 早前Night小幅修复 | AU/AG轻contango；实体缺 | 美元回落有限、高收益率压制；AG surface可研究 | 9/30中国EOD与10/8新IV | 中低 |
| 黑色—建材 | 整体无高质量方向；I曲线最弱 | DCE具体Night覆盖受限 | I contango扩大；实体/basis只作context | 无执行就绪期权、海外铁矿仅代理 | 9/30EOD、DCE chain、现货口径 | 低 |

## 六、机会排行榜（研究吸引力；不是胜率或仓位）

| 排名/idea_id | 方向/期限/工具 | 评分（逻辑/赔率/催化/价曲波/拥挤） | 有效支持层 | 研究判断；证据；执行 | 反证与缺口 |
|---|---|---|---|---|---|
| 1 `COM-E-BR2611-RELSTRENGTH-20260930` | 节后偏多；1—5D；BR2611期货 | **67**=18/17/13/11/8 | 2：价格持仓、curve | 存在待验证优势；部分；休市/等待10/8触发 | 9/30 EOD缺失、实体/海外/期权不足，Night已先涨4.5% |
| 2 `COM-E-OI701-RELSTRENGTH-20260930` | 节后偏多；1—5D；OI701期货 | **63**=17/16/12/10/8 | 2：价格持仓、curve | 存在待验证优势；部分；休市/等待10/8触发 | 大豆需求弱、外盘油脂未确认、basis C级 |
| 3 `COM-E-ENERGY-POSTEIA-20260930` | 裂解/产品相对强研究；1—10D；暂不定义篮子 | **61**=17/14/14/9/7 | 2：实体EIA、境外定价 | 存在待验证优势；部分；待合约/配比/报价 | 原油累库、海湾出口恢复；中国9/30EOD与进口平价缺失 |
| 4 `COM-M-AUAG-MACRO-DIVERGENCE-20261001` | 金强银弱观察；1—7D；待报价价差 | **56**=15/13/11/10/7 | 1：境外定价 | 证据不足；不足；休市/待报价 | 高收益率压制、国内最新日盘缺失、非中性篮子 |
| 5 `COM-A-SOY-DEMAND-WEAK-20261001` | 豆系偏弱观察；5—20D；M/RM/Y链 | **54**=17/12/10/8/7 | 1：实体供需 | 存在待验证优势；部分；休市/等待节后 | harvest与生物燃料可能反向，DCE期权/9/30EOD缺 |

没有70+候选，表示尚无达到研究门槛的方向，并不表示数据充分地证明“市场没有机会”。

## 七、交易研究卡（2张，不凑数）

### 卡1：BR2611节后相对强势确认（非当前可执行卡）

- 市场隐含：早前Night已把橡胶利多计入BR2611约4.50%；我们的分歧是仅当节后gap不回吐、RU/NR同向且BR曲线维持，延续才有优势。
- 事实：9/29 close/settle 15460/15390；9/30早前Night OHLC 15260/16210/15230/16155，vs close +4.50%、vs settle +4.97%，Night ΔOI +8194；EOD curve +1.10% backwardation。OI只能作归因线索。
- 工具：BR2611单腿多，1手；不把BR/RU/NR未定义组合称中性。multiplier/tick/tick value/margin/price limit/night-session参数未由仓库确认；last trading day=2026-11-16。参数未补齐前不执行。
- 入场：10月8日09:30后，首30分钟低点不破且重新站上VWAP；50%+50%。高开超过16155的3%则等45分钟，不追首跳。
- 好/中/坏：VWAP下0—0.3%回踩/靠近VWAP/VWAP上方追首30分钟高点；坏成交直接放弃。由于当前休市，不给虚构成交价和滑点。
- 止损/失效/退出：加权价下1.0%或跌破首30分钟低点且30分钟不收复；BR强而RU/NR、curve反向也失效。TP1=+1.2R减半，TP2=+2.0R；第5交易日时间止损。
- 风险：期货最大损失不由结构限定；计划损失≤NAV 0.50%，1/2个涨跌停压力损失待参数核验。交割月前滚动，流动性消失/保证金上调/gap均可使实际损失大于计划R。

### 卡2：OI701节后相对强势（非当前可执行卡）

- 市场隐含：早前Night已将菜油相对利多计入1.76%；我们的分歧是只有OI/P、OI/Y在节后继续扩张，才说明不是油脂共振噪音。
- 事实：9/29 close/settle 10057/10044；早前Night OHLC 10057/10256/10051/10234，vs close +1.76%、vs settle +1.89%，Night ΔOI +6681；curve +1.74% backwardation。中国豆粕需求偏弱是竞争解释。
- 工具：OI701单腿多，1手；非dollar-neutral、非beta-neutral。multiplier=10吨/手，tick=1元/吨，tick value=10元；静态名义本金约102,340元/手（以旧Night close估算）。仓库margin=9%、price limit=8%、last trading day=2027-01-14；节后须复核交易所临时参数。
- 入场：10月8日10:00后，OI站上首小时VWAP且OI/P、OI/Y较开盘扩大；50%试仓，10:30仍维持再加50%。
- 好/中/坏：VWAP±0.2%/VWAP上0.2—0.5%/超过首小时高点0.5%追入；坏成交放弃。无实时概率，不编胜率。
- 止损/失效/退出：加权价下1.2%或相对价差回到开盘值；TP1=+1R、TP2=+1.8R；第5交易日退出。OI高开后30分钟内回补gap或三油同跌，取消。
- 风险：计划损失≤NAV 0.50%；以10234静态估算，1/2个8%涨跌停约8,187/16,374元每手，不含滑点、保证金上调。交割月前滚动。

能源研究卡不足以成立：缺中国9月30EOD、精确跨品种配比、进口平价和可成交报价；不定义伪中性篮子。

## 八、商品期权专项

最新可用截面仍是2026-09-29：13,324条、184 series；180 surface-ready、46 positioning-ready、0 execution-ready，IV coverage约98.92%，OI coverage约68.97%，bid/ask coverage=0，dealer gamma方向未知。统一层中的逐series研究状态与全局surface文件空/quality not-ready并存，故只能逐series研究。

- AG2612（11/24）：ATM 14900，ATM IV 38.63%，RR25 +2.86，BF25 +1.78；银价变化已改变moneyness。
- AO2701（12/25）：ATM 2650，ATM IV 16.62%，RR25 +3.89，BF25 +1.01；positioning可研究但不可执行。
- NR2612（11/24）：ATM 16400，ATM IV 21.92%，RR25 +2.48，BF25 +1.08；代表Night是NR2611，不能机械给NR2612 Greeks。
- SC2611：ATM IV约74.70% vs RV20约59.19%；EIA、OPEC+与地缘跳空使“高IV=该卖”不成立。

结构偏好：节后若报价完整，方向候选优先用有限损失价差；跨假期事件凸性已在境外持续释放，中国旧截面不能证明便宜。所有结构均为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。回避裸卖Gamma、旧ATM、用OI节点推断dealer gamma，以及无bid/ask的“净成本”。

## 九、9:00开盘风险地图

今天无9:00日盘。严格三层：①Previous China EOD=9月29日last-good，9月30日EOD缺失；②Current Trading Day Night=不存在，最近合法Night归属9月30且仅作历史锚；③07:00 Overseas=9月30欧美结算与10月1亚洲盘前公开信息。下一有效窗口是10月8日09:00。

| 重点 | 节后可能gap | 是否已在Night定价 | 是否追价/等待 | 开盘后确认 |
|---|---|---|---|---|
| BR/RU/NR | 8日信息累积，方向不可预估 | 仅9/30早前已部分定价 | 否；45分钟 | 三品种同向、BR curve、gap回补率、参数 |
| SC/FU/LU/BU | EIA/OPEC+/地缘双向高gap | 没有定价9/30 EIA及长假信息 | 否；45分钟 | 外盘近月、成品油裂解、SC/FU curve、人民币 |
| OI/P/Y/RM | OI旧强、豆系需求弱，分化 | 仅OI早前Night | 否；30分钟 | 三油相对价差、压榨利润、仓单/现货 |
| AU/AG | 金强银弱；美元与收益率拉扯 | 仅早前小幅修复 | 否；30分钟 | DXY、实际利率、金银比、新IV/skew |
| EC/LH/JD/LC等无常规Night品种 | 首个日盘一次性重估 | 否 | 否；45分钟 | 集合竞价量、主力切换、涨跌停/保证金 |

不值得交易：今天所有中国商品；10月8日首跳追价；任何以9月29日EOD或9月30日早前Night为当前挂单价格的策略；C级basis套利；无bid/ask期权；不同月份/单位强拼跨市场套利。

## 十、未来24h / 7d事件

| 北京时间 | 事件 | 处理 |
|---|---|---|
| 10月1日全天 | 中国国庆休市，境内无日盘/夜盘 | 境内策略保持零新增Delta；只更新海外累计gap |
| 10月1日夜间 | 美国ISM制造业/就业与利率敏感数据窗口 | 金属、原油先观察美元和美债；不以单一数据点追价 |
| 10月3日03:30附近 | CFTC COT常规窗口 | 滞后持仓只作拥挤背景，不当成即时催化 |
| 10月4日 | OPEC+核心成员与JMMC线上会议，市场预期11月目标大致不变 | 能源Delta限额；优先有限损失，不裸卖Vega/Gamma；[Reuters](https://www.reuters.com/business/energy/opec-oil-producers-set-keep-output-targets-steady-sunday-meeting-sources-say-2026-09-30/) |
| 10月7日22:30 | 下一份EIA周报常规窗口 | 与长假累计海外价格合并，不能单独映射SC |
| 10月8日08:55/09:00 | 中国节后集合竞价/日盘恢复 | 先做1/2个涨跌停、流动性消失和保证金上调压力测试；等30—45分钟 |
| 10月8日21:00 | 下一实际中国夜盘 | 重新核验exact-contract Night、curve与双收益锚 |

## 覆盖核对与旧建议台账

**覆盖统计**：应覆盖提示定义的63个代码及动态新增合格品种；引擎映射并扫描77个产品（63个强制+14个动态：JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR）。实际取数且已分析：77个产品的9/29 EOD/Market State；Night 37个产品代表记录；Physical 18/20；External repo 17/22加公开海外；Options 184 series逐series质量。数据不足：全部77个产品的9/30 EOD、9/30最新curve/OI；214个Night具体合约；SC/LU实体；DCE部分期权链；全市场执行报价。流动性不足/不适用：无Night制度品种、JR等零量/占位记录及动态冷门品种不进入排名；仍保留扫描状态。

| 板块 | 强制代码 | 实际状态 | 未入榜最值得跟踪的异常/无异常依据 |
|---|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/29全取；9/30缺 | I contango扩大但只有2层以内证据；其余无跨层共振 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 9/29全取；期权逐series不一 | AG弱于AU；AO价跌仓增仅作线索；铜外盘小涨未形成国内确认 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 9/29全取；Night部分 | 产品裂解/原油分化最重要；PX close-settle分歧不当新增强势 |
| 新能源 | LC/SI/PS及GFEX新材料 | 9/29价格取；仓单沿用/stale | 仓单9/1沿用，不能作当前支持；无高质量共振 |
| 农产品油脂饲料畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 9/29全取；DCE options受限 | OI旧Night强；中国大豆需求弱是M/RM/Y反证；LH反弹伴减仓不追 |
| 航运软商品 | EC及CF/SR/AP/CJ/PK | 9/29全取 | EC curve/roll flag最异常但无精确运价和9/30 EOD，不作套利 |

策略类别：方向、基差/跨期、curve、跨品种、跨市场、波动率/偏度/event convexity均已扫描；基差因C级不可评分，跨市场因口径不完整不可执行，期权因execution-ready=0只保留研究。周期覆盖：盘中15/30/45分钟、1—5D、7D长假、20D状态；当前所有盘中窗口均顺延至10月8日。

旧建议：`COM-E-BR2611-RELSTRENGTH-20260930`与`COM-E-OI701-RELSTRENGTH-20260930`从9月30日晚报继承，状态由“等待节后”改为“休市/等待10月8日重报价”，原因=新EIA/海外价格与中国数据缺口；没有成交反馈，不假设持仓。`COM-E-ENERGY-POSTEIA-20260930`由待EIA升级为“EIA已发布、分化逻辑存在但缺中国映射”；AG/AO/NR节前空头条件窗已过期，不复活。EC仍是roll观察。

归档状态：六路径写入并回读后更新；CI仅作独立事后校验，当前记为`pending_or_unverified`。

A. 今天没有应立即建立的新仓位。
B. 今天没有有效中国挂单窗口；10月8日仅在重报价、参数核验及30—45分钟确认后，才考虑BR2611或OI701条件单。
C. 今天应继续观察BR/RU/NR相对强度、OI/P/Y价差、EIA后的产品裂解、AU/AG分化及中国豆系需求；每日更新长假累计海外gap。
D. 今天必须避免或退出所有中国商品新增Delta、以9月29日/早前Night旧价挂单、C级basis套利、无bid/ask期权和未定义中性篮子。
