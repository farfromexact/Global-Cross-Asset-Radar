# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-11｜生成：19:43 BJT｜信息截点：19:35 BJT｜prompt_version：`radar_2026-09-06_coverage_v1`**

## 一、今晚一句话结论

> **今晚休市，无可立即执行的新仓；周一优先等AG、MA、RU触发，油品因地缘升级与保证金/限额上调只观察、不追价。**

**截至本报告时点，无可立即执行的合格新交易。** 今天是周日，中国商品期货没有日盘，也没有21:00夜盘。最近完整中国交易日是2026-10-09；下一实际日盘为2026-10-12 09:00，下一实际夜盘为2026-10-12 21:00，归属2026-10-13交易日。

最接近触发的三个研究项是AG2612反转延续、MA701强势回踩、RU2701供给驱动延续；它们分别缺少周一开盘后承接、过热消化、以及contango收窄和境外橡胶确认。风险偏好很高不改变评分，也不把休市期研究候选写成可执行新仓。

## 二、数据质量、时间与覆盖

### 2.1 实际读取与时点

- 统一输入：`China-Commodities-Engine/data/report_input_latest.json`，`requested_date=2026-10-09`，`generated_at=2026-10-11T19:06:57.429064+08:00`，schema v2。周日没有应产生的中国EOD，10月9日last-good仍是最新应得数据；19:06只是容器刷新，不是行情更新时间。
- 核心期货：`data/last_run_status.json`；交易日2026-10-09，806个合约，SHFE/DCE/CZCE/INE/GFEX五所齐全，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0，无需scoped回退。
- Market State：统一输入内77个产品；72个具有足够流动性并完成1D/3D/5D/20D、OI和near-next初筛；JR/PM/RI/WH/ZC为不适用/流动性不足。
- Physical：18/20个配置序列可用；SC、LU实体序列不可用；5项为按原生频率有效的carried-forward。basis均为C级/context-only，不进入方向评分，也不称可执行套利。
- External：仓库17/22条日频序列可用，底层源日期仍是2026-10-09；周末没有15:00—19:30可比期货连续交易，新增信息来自事件与沙特周日现货股市代理，不能写成中国或全球期货已完成定价。
- Options：交易日2026-10-09；185个series、181个surface-ready、41个positioning-ready、0个execution-ready。DCE因权限失败；另有7个产品失败；全局bid/ask coverage为0。所有期权结构均为研究表达，禁止填权利金、净成本、滑点或当前Greeks。
- Contract Metadata：统一输入仅部分覆盖。AG2612、RU2701关键乘数/跳动/保证金/涨跌停未完整确认；MA701元数据较完整。参数缺失只限制对应执行，不抹掉方向性研究。

### 2.2 Night Session语义与隔离

`data/night_session/last_run_status.json`显示`trading_date=2026-10-11`、`night_session_date=2026-10-10`、`generated_at=2026-10-11T08:01:14.462305+08:00`，但`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`。周六晚制度上没有属于周日的中国夜盘，因此该记录是**周末失败/无会话状态，不是今晚行情，也不是2026-10-12日盘前夜盘**；整段隔离，不计任何候选证据，`overnight_day_decomposition_used=false`。

### 2.3 数据状态

| 模块 | 状态 | 最新有效观测 | 本期用途 |
|---|---|---|---|
| Futures | ok / latest-expected | 2026-10-09 EOD | 全市场价格、量仓、主力合约 |
| Market State | ok / latest-expected | 2026-10-09 | 同合约多周期、curve、OI线索 |
| Physical | partial / carried | 各序列原生频率；SC/LU missing | 仅方向变化或阈值明确者计层 |
| External | partial / weekend | 2026-10-09收盘 + 10月11事件 | 事件映射，不是可执行价差 |
| Night | parse/status ok，session invalid | 周末无合法新session | 隔离；不做夜盘分解 |
| Options | surface mostly ok；execution missing | 2026-10-09 | IV/skew研究；不可报价执行 |
| Metadata | partial | 2026-10-09 | MA可核；AG/RU参数待核 |

### 2.4 周末新增事实

- 沙特周日TASI下跌约1%，Aramco跌约0.6%，说明地缘风险已影响当地风险资产；但该报道没有给出油田、管线或出口装船受损证据。因此它提高SC/LU/FU/BU周一gap尾部风险，却不能单独证明应该追多原油。[Reuters，2026-10-11](https://www.reuters.com/world/middle-east/saudi-stocks-slide-after-attack-riyadh-airport-2026-10-11/)
- 上期能源宣布，自2026-10-12收盘结算起，SC2612、SC2701、LU2612、LU2701涨跌停板调至16%，一般持仓保证金18%、套保持仓17%。这在周一09:00尚未生效，但会抬高周一收盘后的持仓资金与压力预算。[上期能源，2026-10-09](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833670.html)
- 上期所宣布，自2026-10-12收盘结算起，FU2612/FU2701涨跌停16%、一般保证金18%，BU相关合约涨跌停12%、一般保证金14%；并自2026-10-12夜盘（归属10月13交易日）起，对指定FU/BU合约日内开仓限额1500手。[上期所保证金通知](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833667.html)｜[上期所限额通知](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833668.html)

## 三、商品仪表盘（展示12项；全量扫描不止于此）

“Night”栏为周末无合法新session；不以相对结算价代替相对收盘价，也不把失败状态冒充零涨跌。Physical中的仓单不等同社会库存。

| 板块 | 品种/合约 | 10/9 EOD close/settle | 1D / 5D | Volume / OI / ΔOI | EOD curve | Basis / Physical | 早前Night | 15:00—19:30海外/周末事件 | Options S/P/E | 周一信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| 贵金属 | AG2612 | 14717 / 14515 | +0.88% / -7.99% | 303600 / 290434 / -4332 | +0.54% backwardation | C/context；实体无独立确认 | 无合法周末session | 沙特风险升级，未有新期货价 | Y/N/N | 09:30后14650守稳才多 |
| 化工 | MA701 | 3338 / 3321 | +6.04% / +14.83% | 1493099 / 761175 / +70427 | +16.08% backwardation | C/context | 无 | 无新增海外定价 | Y/Y/N | 等45分钟，严禁追高 |
| 橡胶 | RU2701 | 20645 / 20220 | +2.89% / n/a | n/a / n/a / +17339 | -3.86% contango | C/context | 无 | SICOM周末无新价 | Y/Y/N | 20500守稳且contango收窄 |
| 橡胶 | NR2612 | n/a | +0.09% / +3.16% | n/a / n/a / +7200 | -2.16% contango | C/context | 无 | 无新价 | partial | 仅作RU交叉验证 |
| 黑色 | JM2701 | 1539.5 / 1517.5 | +4.30% / n/a | n/a / 415009 / +10394 | +3.48% backwardation | C/context | 无 | 无新增外盘锚 | N/N/N | 等30分钟；不追首跳 |
| 有色 | SN2611 | 391410 / 391170 | -4.23% / n/a | 134989 / 34969 / +3724 | +0.50% | C/context | 无 | LME周末无新价 | partial | 观察，不接飞刀 |
| 原油 | SC2611 | 734.1 / 741.3 | -0.45% / n/a | n/a / n/a / -3400 | +3.19% backwardation | Physical missing | 无 | 沙特风险升；无设施受损确认 | Y/N/N | 等45分钟；不追gap |
| 合成胶 | BR2612 | 16710 / 16370 | +2.77% / n/a | n/a / n/a / +3839 | +2.27% | C/context | 无 | 油品两端尾部上升 | partial | 只观察 |
| 谷物 | C2611 | n/a | -0.42% / n/a | n/a / n/a / -48586 | -1.38% contango | C/context | 无 | WASDE后周末无CBOT新价 | DCE缺失 | 等45分钟 |
| 饲料 | M2701 | n/a | +0.03% / n/a | n/a / n/a / +49030 | -1.00% contango | C/context | 无 | 无CBOT新价 | DCE缺失 | 等45分钟 |
| 新能源 | LC2701 | 117000 / 118740 | -3.74% / n/a | n/a / n/a / +11960 | +1.22% | C/context | 制度上无夜盘 | 无直接海外锚 | partial | 周一09:00等45分钟 |
| 航运 | EC2611 | 2700 / 2749 | -5.05% / n/a | n/a / n/a / -1776 | -22.48% | 实体/运价口径未对齐 | 制度上无夜盘 | 地缘升温但非exact运价映射 | N/N/N | 不抄底 |

当前regime是：**周末无价格发现、周一gap尾部扩大、贵金属反转与甲醇/橡胶动量并存、能源事件风险与交易制度收紧同时上升**。最强链仍是甲醇/部分橡胶的动量，最弱是EC与锂链；能源的事件重要性最高，但方向证据最不干净。

## 四、相比上一期真正变化

1. **沙特风险资产出现可观察反应**：TASI约-1%、Aramco约-0.6%；这是地缘风险扩散的新证据，但不是原油供应中断证据。能源gap风险上升，追涨胜率没有因此提高。
2. **SC/LU/FU/BU资金与涨跌停制度将在周一收盘后收紧**：周一09:00前仍按旧参数交易，但若持仓过结算，必须按新保证金和更宽涨跌停压力重新预算。
3. **FU/BU日内开仓限额从周一夜盘起生效**：事件行情中流动性和冲击成本可能非线性上升，旧的线性止损假设更不可靠。
4. **仓库19:06重生成但没有新行情**：Futures仍是10月9日last-good；不得把generated_at写成10月11日收盘。
5. **Night状态出现周末无效日期组合**：`trading_date=10-11`且validation/published/coverage均false，已隔离；这不是“夜盘跌涨为0”。
6. **AG、MA、RU没有新增价量/curve/期权截面**：评分保持71/70/69；新增周末消息只改变周一gap与执行风险，不为这些方向加分。

## 五、产业链地图

| 产业链 | 方向/强弱 | EOD与curve | 实体/仓单 | 期权 | 海外/事件 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| 贵金属 | AG反转偏强 | AG +0.88%，近强远弱 | 无独立实体确认 | AG IV36.39% vs RV31.44%，右偏；不可执行 | 地缘风险支持尾部，不等于银价已涨 | 周一COMEX/人民币联动与AG实时报价 | 中 |
| 甲醇—化工 | 最强但过热 | MA +6.04%，curve +16.08%，价仓同升仅作线索 | basis C，不计层 | IV45.66% > RV35.68%，右偏；不可报价 | 无新增海外锚 | 回踩质量与backwardation延续 | 中 |
| 橡胶 | 次强 | RU +2.89%但contango -3.86%反对追涨 | 实体只作context | IV27.00% > RV21.93%，右偏 | 周末SICOM无新价 | curve收窄与exact外盘 | 中低 |
| 油品 | 方向冲突、事件最敏感 | SC -0.45%，curve +3.19% | SC/LU physical missing | SC近月IV60.91%≈RV59.93%，exec N | 沙特升级；同时无设施受损确认，且美国海湾复产/SPR形成反向解释 | 周一Brent/WTI、装船/设施事实、保证金后资金行为 | 低 |
| 黑色—新能源—航运 | 相对弱/分化 | JM强，LC/EC弱；EC陡峭contango | 多为C/context | DCE或执行层缺失 | 缺exact海外映射 | 需求、库存与期权完整性 | 低 |

## 六、机会排行榜（研究排序，不是胜率或仓位指令）

| 排名 | idea_id / 方向 / 周期 | 分项（逻辑/凸性/催化/价曲波/拥挤） | 总分 | 有效支持层 | 研究判断 / 证据 / 执行 | 反证与数据影响 |
|---|---|---:|---:|---:|---|---|
| 1 | `COM-E-AG2612-DAY-REVERSAL-LONG-20261009` 条件多 1—5D | 18/18/14/11/10 | **71** | 3：价格、curve、海外 | 存在待验证优势 / 部分 / 休市，等待触发 | 5D仍-7.99%、OI下降；无周末新价，参数不全 |
| 2 | `COM-M-MA701-MOMENTUM-HOLD-20261009` 条件多 1—5D | 19/17/14/11/9 | **70** | 3：价格、curve、期权 | 存在待验证优势 / 部分 / 休市，等待回踩 | 5D+14.83%过热、IV显著高于RV；无新价不加分 |
| 3 | `COM-M-RU2701-SUPPLY-LONG-20261002` 条件多 3—10D | 18/16/13/12/10 | **69** | 2：价格、期权 | 存在待验证优势 / 部分 / 待curve与外盘 | contango反对追涨；参数不全，按上限≤69 |
| 4 | `COM-M-JM2701-MOMENTUM-CONTINUATION-20261010` 条件多 1—5D | 17/15/13/11/10 | **66** | 2：价格、curve | 存在待验证优势 / 部分 / 等30分钟 | DCE期权缺失，实体确认不足 |
| 5 | `COM-M-C2611-WASDE-GAP-WATCH-20261010` 条件空 1—5D | 16/14/15/8/6 | **59** | 1：海外事件 | 证据不足 / 不足 / 仅观察 | 国内EOD未确认WASDE，DCE期权缺失；按1层上限≤59 |

分数复核无超项、总和一致。0—100分是研究吸引力，不是胜率、预期收益或仓位指令。油品没有进入前五：周末新增地缘信息与复产/SPR、无设施损坏确认以及周一收盘后风控参数调整互相冲突，缺乏可识别错价。

### 旧建议台账

- AG、MA、RU、JM、C延续10月10日晚报与10月11晨报的稳定idea_id；状态从“休市等待”保持不变，原因是**无新价格**，但周一gap风险因新地缘/制度信息上升。
- 原SC空头研究继续降级；若此前按旧条件建立，只有在复产快于预期、周一SC跌破日盘锚且curve同步走弱时才重新评估，不能因周末消息反向追多或机械持有。
- SN短线观点仍为已取消；没有成交反馈，不假定用户持仓，也不声称账户净敞口。

## 七、前三名交易卡（均非今晚可执行）

### 1. AG2612 条件多｜`COM-E-AG2612-DAY-REVERSAL-LONG-20261009`

- **事实**：10/9 close/settle=14717/14515，1D +0.88%，5D -7.99%，volume 303600，OI 290434，ΔOI -4332，near-next +0.54%。周末无合法night OHLC/close，因此overnight return、return_vs_settlement、night ΔOI均为missing，而不是0。
- **市场隐含/分歧**：市场仍隐含急跌后的脆弱反弹；我们的分歧是若周一14650之上出现承接，海外贵金属尾部风险与近端curve可使反转延续，但OI下降和5D跌幅是最强反证。
- **工具**：首选AG2612期货；期权仅研究2026-11-24、30—45Δ call spread，ATM14500、IV36.385%、RV20 31.436%、RR25 +1.75%，surface Y / positioning N / execution N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/成交情景**：周一09:30后；好=14650—14720承接，0.25% NAV试仓；中=14720—14800回踩守稳，最多0.25%；坏=>14850无回踩或>15200，放弃。首跳不追。
- **风险与退出**：计划止损14380，日收低于14250逻辑失效；TP1 15150减半，TP2 15700；2日不扩张时间止损，最多5日。期货最大损失不由结构限定，gap/涨跌停/流动性消失可超过计划损失。
- **参数**：LTD 2026-12-15；multiplier/tick/tick value/margin/price limit/night session均未确认；notional、1/2涨跌停压力损失无法可靠计算。交割风险随12月临近上升，10月底前重新滚动评估。
- **催化/放弃**：1—5D海外贵金属与地缘风险；若白银代理跌破58.5、开盘>15200或关键参数/实时报价仍不可得则放弃。

### 2. MA701 条件多｜`COM-M-MA701-MOMENTUM-HOLD-20261009`

- **事实**：10/9 close/settle=3338/3321，1D +6.04%，5D +14.83%，volume 1493099，OI 761175，ΔOI +70427，curve +16.08%。价涨仓增只作归因线索，不能断言“新多”。周末无合法night OHLC。
- **市场隐含/分歧**：市场已计入强短缺/挤仓；我们只在回踩不破且backwardation不塌时接受延续，不能把过热本身写成优势。
- **工具**：MA701期货；2026-12-11 call spread只研究，ATM3300、IV45.655%、RV35.677%、RR25 +2.02%、BF25 1.445%，S/P/E=Y/Y/N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/成交情景**：周一09:45；好=3330—3350回踩后收复前15分钟VWAP；中=3350—3380缩量回踩；坏=>3480或无回踩，放弃。两腿配比不适用于期货单腿；期权若未来执行仅1×1价差。
- **风险与退出**：计划止损3270，日收低于3250失效；TP1 3460减半，TP2 3580；2日不扩张退出、最多5日。NAV试仓0.25%—0.50%，不因高风险偏好增加。
- **参数/压力**：multiplier 10吨/手，tick 1元/吨，tick value 10元；EOD名义33380元，保证金率7%约2336.6元；涨跌停6%，1个板约2002.8元/手，2个板简单压力约4005.6元/手；LTD 2027-01-14；night session参数未确认，交割风险当前低但需滚动。
- **催化/放弃**：1—5D库存/开工与curve持续性；若curve收窄伴价格下跌、OI继续激增但承接失败，或无法获得实时报价，放弃。

### 3. RU2701 条件多｜`COM-M-RU2701-SUPPLY-LONG-20261002`

- **事实**：10/9 close/settle=20645/20220，1D +2.89%，ΔOI +17339，curve -3.86%（contango）。周末无SICOM新价与合法中国night；这使第4层缺失，不能把媒体宽口径涨幅当exact contract。
- **市场隐含/分歧**：市场定价供给扰动与需求改善，但contango说明现货紧张未充分确认；只有周一20500守稳且contango收窄，才表明价格获得curve补证。
- **工具**：RU2701期货；2026-12-25 call spread仅研究，ATM20250、IV27.00%、RV21.927%、RR25 +3.22%、BF25 0.68%，S/P/E=Y/Y/N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/成交情景**：周一09:30；好=20500附近守稳且contango收窄；中=20600—20800确认；坏=>21200或contango扩大，放弃。不追首跳。
- **风险与退出**：计划止损20150，日收低于19900失效；TP1 21200减半，TP2 21800；3日不扩张退出，最多10日；试仓最大损失NAV 0.25%。
- **参数**：LTD 2027-01-15；multiplier/tick/tick value/margin/price limit/night session未确认，notional和1/2板压力损失待参数；期货最大损失不有限。交割风险当前低，但必须在移仓窗口前滚动。
- **催化/放弃**：1—10D东南亚天气/供给、SICOM与curve；若SICOM弱、contango扩大或参数/报价不可得则放弃。

## 八、商品期权专项

- **样本日期**：2026-10-09，是截至周日晚最新有效截面；本期无新增。AG、MA、RU的surface可用，但标的周末无新价；moneyness待周一开盘重置。
- **IV-RV**：AG +4.95 vol，MA +9.98 vol，RU +5.07 vol，SC约+0.98 vol。高IV-RV只说明隐含波动高于历史实现，不证明期权贵/便宜，也不自动支持卖波。
- **偏度/凸性**：AG、MA、RU均有正RR25，右尾需求已部分计价；若要表达方向，价差优于裸买，但execution readiness=0，不能给净支出、盈亏平衡或Greeks。
- **Event convexity**：油品面临中东、海湾复产与周一参数调整三重事件；SC近月expiry 2026-10-14时间价值与跳空风险极端，不做未报价裸卖波。
- **Vol RV**：可研究AG相对MA/RU的风险预算效率，但没有跨品种同到期、同Delta、bid/ask与保证金口径，不称套利。
- **回避**：DCE期权、任何dealer gamma方向、PCR/OI推断新多新空、无bid/ask的权利金和净成本。

## 九、周一09:00与下一夜盘风险地图

今晚（周日）没有21:00中国夜盘。四层时间顺序是：①中国最近完整EOD=10月9日；②本周末没有合法已完成Night Session；③周末新增只有事件与交易所通知，没有可比15:00—19:30期货价格；④下一日盘=10月12日09:00，下一夜盘=10月12日21:00、归属10月13交易日。

| 品种 | 周一可能开盘 | 是否已定价 | 内外/事件冲突 | 首跳 | 等待 | 开盘确认 |
|---|---|---|---|---|---|---|
| SC/LU/FU/BU | 高开或高波动 | 未完成 | 沙特升级支持风险溢价；无设施受损、美国海湾复产/SPR反对追多 | 不追 | 45分钟 | Brent/WTI、人民币、curve、OI、现货/装船；收盘后新保证金 |
| AG | 偏高/高波动 | 未完成 | 地缘支持；5D跌幅与OI下降反对 | 不追 | 30分钟 | 14650、COMEX银/金、USD/CNH、curve |
| MA | 高开风险 | 10/9已大幅预交易 | 国内动量强；无海外新增锚、IV高 | 不追 | 45分钟 | VWAP、3330—3380、curve、ΔOI |
| RU/NR | 偏高但易冲高回落 | 未完成 | 供给叙事与contango冲突 | 不追 | 30分钟 | RU20500、近远月、SICOM |
| JM | 平高开 | 部分 | 国内动量强；实体与期权缺失 | 不追 | 30分钟 | 1539.5、curve、成交/OI |
| C/M | 平开/事件gap | 未完成 | WASDE外盘与国内旧EOD未对齐 | 不追 | 45分钟 | CBOT映射、人民币、基差口径 |
| LC | 平/低开 | 无夜盘 | 周五弱势、缺海外exact锚 | 不追 | 45分钟 | 117000、curve、成交/OI |
| EC | 高波动但方向不确定 | 无夜盘 | 地缘可能抬升运价；周五价格/curve仍弱 | 不追 | 45分钟 | 运价事实、2700、curve；不抄底 |

若周一09:00发生超过1个当日波动尺度的gap，所有静态入场价自动转为“待重新报价”，不能把本报告条件单机械送入市场。周一15:00结算后，SC/LU/FU/BU相关风险预算必须按新保证金/涨跌停重新计算；FU/BU在21:00还要检查1500手限额对冲击成本的影响。

## 十、未来24小时 / 7日事件日历（北京时间）

| 窗口 | 事件 | 影响与处理 |
|---|---|---|
| 10/12 09:00 | 中国商品周一日盘重开 | 所有候选先等15/30/45分钟；gap大则取消旧条件 |
| 10/12 收盘结算 | SC/LU/FU/BU新涨跌停与保证金生效 | 降低杠杆，合并油品同因子风险；1/2板压力重算 |
| 10/12 21:00 | 下一实际中国夜盘，归属10/13 | FU/BU指定合约1500手日内开仓限额开始；不追首跳 |
| 10/12—10/14 | Riyadh世界石油大会、沙特安全局势 | 油品Delta与IV跳升风险；只用有限凸性或延迟入场 |
| 未来24—72h | 美国海湾平台复产/损坏评估、SPR执行 | 复产快则压油价溢价；损坏/延迟则相反，需事实确认 |
| 下周常规窗口 | EIA周报、CFTC持仓、USDA后续、天气 | 发布时点待官方日历核验；不预填未经确认的精确小时 |
| 未来7日 | 中国交易所临时参数、到期/移仓 | 每日核查SC/LU/FU/BU与近月期权；避免交割与流动性挤压 |

风险处理：单一试仓最大损失NAV 0.25%—0.75%，确认交易0.75%—1.50%，单一高确信主题合并风险≤2.5%—3.0%；油品、化工、橡胶的能源/通胀共因子合并计算。压力测试必须包含1/2个涨跌停、相关性破裂、保证金上调、流动性消失、周一gap、人民币急变和IV跳升/塌陷。

## 十一、覆盖核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足 | 不适用/流动性不足 | 未入榜最值得跟踪的异常/无异常依据 |
|---|---|---|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/9 EOD与curve初筛 | DCE期权缺失，实体多为context | 0 | JM价曲强但仅2层；其余未出现跨层独立异常 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | 部分参数/实体；positioning不齐 | 0 | SN单日-4.23%且OI增，仅早期异常；AU/AG外盘需周一重定价 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 22/22 | SC/LU physical missing；部分exact海外与期权执行缺失 | 0 | 油品新增制度风险最高；BR强但不具跨层确认 |
| 新能源 | LC/SI/PS及GFEX新材料 | LC/SI/PS与动态品种均初筛 | 海外exact映射/期权执行部分不足 | 0 | LC价跌仓增与curve正斜率冲突，等待周一而非追空 |
| 农产品油脂饲料畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 18/18 | DCE options缺失，WASDE国内映射待周一 | 0 | C/M的OI异动只作归因线索；未发现可执行RV |
| 航运软商品 | EC及棉花/白糖/苹果/红枣/花生 | EC/CF/SR/AP/CJ/PK均初筛 | EC外部运价口径未exact对齐 | 0 | EC跌5.05%且深contango，是异常但不是抄底信号 |
| 动态新增/低流动 | 引擎77品种 | 共72个完成量价/curve扫描 | JR/PM/RI/WH/ZC | 5 | 缺失不等于无机会；仅因流动性和历史不足不入榜 |

策略类别：方向、基差/跨期、curve、跨品种/跨市场、风格/中性、波动率/偏度、事件凸性全部扫描。跨市场与基差因口径非exact仅作context；未定义篮子不写成dollar-neutral或beta-neutral。周期覆盖1D/3D/5D/20D；缺历史处不输出伪趋势。

## 来源

1. [China-Commodities-Engine（统一输入与模块状态）](https://github.com/farfromexact/China-Commodities-Engine) — 2026-10-11访问；支持EOD、curve、Physical、External、Night、Options、Metadata状态。
2. [Reuters：Saudi stocks slide after Riyadh airport attack](https://www.reuters.com/world/middle-east/saudi-stocks-slide-after-attack-riyadh-airport-2026-10-11/) — 2026-10-11；支持TASI/Aramco下跌与地缘升级，不支持油田受损推断。
3. [上期能源：SC/LU涨跌停与保证金调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833670.html) — 2026-10-09；支持10月12日收盘结算后参数。
4. [上期所：FU/BU涨跌停与保证金调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833667.html) — 2026-10-09；支持10月12日收盘结算后参数。
5. [上期所：FU/BU日内开仓限额](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833668.html) — 2026-10-09；支持10月12日夜盘起1500手限额。

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：无；休市，AG2612、MA701、RU2701条件仅用于周一开盘后人工重验，不预挂隔夜单。
C. 今晚应继续观察的机会：AG反转、MA回踩延续、RU的contango收窄、JM动量，以及SC/LU/FU/BU地缘与新参数共同作用。
D. 今晚必须避免或退出的交易：避免追逐任何周末油品/贵金属headline，避免无bid/ask期权、DCE缺失链、EC抄底及未按新保证金重算的油品隔夜敞口。
