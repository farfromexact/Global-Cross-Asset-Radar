# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-12｜生成：07:06 BJT｜信息截点：07:00 BJT｜prompt_version：`radar_2026-09-06_coverage_v1`**

## 一、今日一句话结论

> **RU得到合约级夜盘与SICOM补证，但已接近原目标；今天只等回踩确认，AG、MA降为次级条件单，不追能源headline。**

**截至本报告时点，无可立即执行的合格新交易。** 研究机会存在，最接近触发的是RU2701回踩延续、MA701强势回踩和AG2612反转再确认；三者均需09:00后现价、曲线及成交质量验证，且期权执行报价仍缺失。

最近完整中国EOD是2026-10-09；周五晚属于2026-10-12交易日的夜盘，本仓库未形成有效快照。公开来源仅能合约级确认RU2701夜盘收20980元/吨，故RU使用`night_session_fallback=true`；其余重点合约夜盘精确收盘仍为missing。下一实际交易窗口为今天09:00日盘。

## 二、数据质量、时间与覆盖

### 2.1 实际读取路径与模块状态

- 第一层：`China-Commodities-Engine/data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`。
- 统一输入：`requested_date=2026-10-09`，`generated_at=2026-10-11T19:06:57.429064+08:00`，schema v2。周末无新中国EOD，10月9日仍是周一开盘前最新应得、可验证的last-good；周末重跑失败不使该快照失效。
- Futures：10月9日，806合约、77品种；SHFE/DCE/CZCE/INE/GFEX五所齐全，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0。周末root status的五所抓取失败是“无应有会话的刷新失败”，与last-good有效性分开披露。
- Market State：72个流动性合格品种完成同合约1D/3D/5D/20D、量仓和near-next扫描；JR/PM/RI/WH/ZC因流动性/历史不足不适用。
- Physical：18/20配置序列可用；SC、LU missing；5项carried-forward但仍在其原生频率有效。basis均为C级/context-only，不进入方向评分或套利确认。
- External：仓库17/22条日频序列可用，源日期10月9日；07:00联网层另列Reuters/LSEG市场快照、SICOM结算与USD/CNH，不与仓库日频混写。
- Options：10月9日，14074条、185个series；181 surface-ready、41 positioning-ready、0 execution-ready。39/64产品成功，DCE全链跳过，另有CJ/PF/PL/PR/TA/ZC/DCE:A失败；bid/ask coverage=0，dealer gamma方向未知。
- Contract Metadata：部分覆盖；MA较完整，RU稳定乘数/跳动/LTD可由交易所规格确认，但当前保证金和涨跌停未确认；AG关键执行参数不全。

### 2.2 Night Session质量闸门与日期语义

模块状态为`trading_date=2026-10-11`、`night_session_date=2026-10-10`、`generated_at=2026-10-11T08:01:14.462305+08:00`、`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`。覆盖计数：selected/request=806/806，night contracts=0，outside-window=592，query_error=214，unresolved=214，missing timestamp/price/quote均为0；warning为“214 concrete contracts are unresolved”。这是周末失败/无会话状态，绝不是属于10月12日的周五晚夜盘。

因此：仓库Night整段隔离；公开回退仅用于已核实的**同一具体合约RU2701夜盘收盘**。RU夜盘open/high/low、volume、OI、ΔOI仍为missing，不猜数；AG/MA/JM等宽口径媒体涨幅不替代exact-contract数据。

### 2.3 07:00海外层

- Reuters/LSEG市场屏在约07:00 BJT显示：黄金4191.40（+0.01%）、铜1427.35（+1.41%）、Brent 104.54（-0.17%）、CBOT大豆1292.25（+0.02%）。这是近实时/准实时显示值，单位沿原页面，不作为境内外可执行价差。
- USD/CNH约6.6930，前收6.6927，基本持平；人民币未给商品gap提供明显单向驱动。
- SICOM最新官方结算仍为10月9日：TSR20 Nov/Dec/Jan分别259.0/257.6/256.7美分/公斤，近端backwardation，支持境外橡胶近端偏紧，但不是周一07:00实时成交。
- 周日沙特机场再遭袭，Dammam机场也获官方确认受击；胡塞声称袭击Aramco设施，但沙特政府与Aramco未确认。Brent仅小跌，显示事件风险尚未形成新的单向油价弹性；不能把headline直接写成SC已经上涨。

## 三、商品仪表盘（展示12项；全量扫描见覆盖核对）

1D/5D优先为引擎同合约收益；close/settle与先前已验证10月9日快照一致。Night栏的“missing”是数据缺失，不是零涨跌。

| 板块 | 品种/合约 | 10/9 EOD close/settle | 1D / 5D | Volume / OI / ΔOI | EOD curve | Basis / Physical | 10/9 Night close；vs close / vs settle；ΔOI | Night quality/time | 07:00海外 | Options S/P/E | 09:00信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|---|
| 橡胶 | RU2701 | 20645 / 20220 | +2.89% / +4.09% | n/a / n/a / +17339 | -3.86% contango，roll flag | C/context | **20980；+1.62% / +3.76%；missing** | fallback exact-close-only；10/9夜收 | SICOM近端backwardation | Y/Y/N | 等30分钟回踩；不追>21200 |
| 化工 | MA701 | 3338 / 3321 | +6.04% / +14.83% | 1493099 / 761175 / +70427 | +16.08% backwardation | 港口样本库存10/8环比-22.47%至30.51万吨；basis C | exact missing | repo invalid；未用宽口径替代 | 无直接exact锚 | Y/Y/N | 09:45后3330—3380回踩 |
| 贵金属 | AG2612 | 14717 / 14515 | +0.88% / -7.99% | 303600 / 290434 / -4332 | +0.54% backwardation | C/context | exact missing | repo invalid | 黄金4191.4，较屏显前值近乎持平；银现货最新周五60.77 | Y/N/N | 09:30后14650守稳 |
| 黑色 | JM2701 | 1539.5 / 1517.5 | +4.30% / +1.57% | n/a / 415009 / +10394 | +3.48% backwardation | C/context | exact missing | repo invalid | 无exact外盘锚 | N/N/N | 等30分钟，首跳不追 |
| 原油 | SC2611 | 734.1 / 741.3 | -0.45% / +2.28% | n/a / n/a / -3400 | +3.19% backwardation | Physical missing | exact missing | repo invalid | Brent104.54，-0.17%；沙特事件升温 | Y/N/N | 等45分钟；不追gap |
| 合成胶 | BR2612 | 16710 / 16370 | +2.77% / +8.23% | n/a / n/a / +3839 | +2.27% | C/context | exact missing | repo invalid | 油价平、橡胶外盘近强 | partial | 仅交叉验证RU |
| 20号胶 | NR2612 | n/a | +0.09% / +3.16% | n/a / n/a / +7200 | -2.16% contango | C/context | exact missing | repo invalid | SICOM近端偏强 | partial | 不单独追价 |
| 有色 | SN2611 | 391410 / 391170 | -4.23% / -5.05% | 134989 / 34969 / +3724 | +0.01% | C/context | exact missing | repo invalid | 铜代理+1.41%，非锡exact | partial | 反弹也不接飞刀 |
| 谷物 | C2611 | n/a | -0.42% / -1.19% | n/a / n/a / -48586 | -1.38% contango | C/context | exact missing | repo invalid | CBOT豆+0.02%，非玉米exact | DCE缺失 | 等45分钟 |
| 饲料 | M2701 | n/a | +0.03% / -0.47% | n/a / n/a / +49030 | -1.00% contango | C/context | exact missing | repo invalid | CBOT豆+0.02% | DCE缺失 | 等45分钟 |
| 新能源 | LC2701 | 117000 / 118740 | -3.74% / -5.93% | n/a / n/a / +11960 | +1.22% | C/context | 制度上无夜盘 | n/a | 无exact海外锚 | partial | 09:45后才判断，不追空 |
| 航运 | EC2611 | 2700 / 2749 | -5.05% / +0.05% | n/a / n/a / -1776 | -22.48% contango；仅4观测 | 运价口径未exact对齐 | 制度上无夜盘 | n/a | 中东风险不是exact运价 | N/N/N | 不抄底 |

当前regime：**周一gap与事件风险、橡胶/甲醇动量、贵金属反转观察、能源headline与风控参数收紧并存**。最强链从“甲醇单独领跑”转为“橡胶得到新增夜盘和境外曲线确认”；最弱仍是EC与锂链。能源事件重要性最高，但Brent反应有限、供应损坏未证实，方向错价最不干净。

## 四、相比上一期真正变化

1. **RU出现可核实的新增价格信息**：RU2701周五夜盘收20980；相对日收盘仅+1.62%，相对结算价+3.76%。两锚差异2.14个百分点，说明使用结算锚会明显夸大隔夜新增强势。
2. **RU获境外curve补证但国内curve仍反对**：SICOM TSR20 Nov/Dec/Jan为259.0/257.6/256.7，近端backwardation；国内RU near-next仍为-3.86% contango且roll flag，跨市场方向同强、结构不同，不能称套利。
3. **MA实体层增强但追价赔率恶化**：10月8日港口样本库存环比-22.47%至30.51万吨、续创样本低位，支持供应紧张；但EOD已+6.04%、5D+14.83%，若周一再高开，剩余上行与止损距离不对称。
4. **AG海外没有继续扩张**：周五银涨至60.77、金涨至4194.36后，约07:00黄金屏显4191.40，新增弹性接近零；AG缺exact夜盘，评分由71降至68。
5. **沙特风险进一步升级但油价未同向扩张**：Dammam机场受击获确认，Aramco设施受击仍只是胡塞单方声称；Brent约-0.17%，最强竞争解释是供应链尚未出现可确认损坏。
6. **今天收盘后油品风控参数上调**：SC/LU部分合约涨跌停16%、一般保证金18%；FU涨跌停16%/保证金18%，BU涨跌停12%/保证金14%。今晚21:00起FU/BU指定合约日内开仓上限1500手，隔夜资金与冲击成本需重算。

## 五、产业链地图

| 产业链 | 方向/强弱 | EOD→Night/curve | 实体/仓单 | 期权 | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| 天然橡胶 | **最强，偏多但不追** | RU +2.89%；night +1.62% vs close；国内contango反对 | 实体只作context | IV27.00% > RV21.93%，RR25 +3.22；exec N | SICOM近月backwardation支持 | 夜盘OHLC/量仓与night curve | 中高 |
| 甲醇—化工 | 强但过热 | MA +6.04%，curve +16.08% | 港口样本库存显著下降；basis C | IV45.66% > RV35.68%，右偏；exec N | 无exact海外锚 | MA701 exact夜收与09:00回踩 | 中 |
| 贵金属 | 反转待确认 | AG +0.88%、curve近强；exact night missing | 无独立实体层 | IV36.39% > RV31.44%，RR25 +1.75；exec N | 金近乎平，银仅周五价 | AG exact夜收与COMEX银周一价 | 中低 |
| 油品 | 事件敏感、方向冲突 | SC日盘偏弱但curve正；night missing | SC/LU physical missing | SC IV60.91%≈RV59.93%，exec N | 沙特风险升、Brent微跌；美湾复产/SPR反向 | 设施/出口损坏事实 | 低 |
| 黑色—新能源—航运 | 分化偏弱 | JM强；LC/EC弱，EC深contango | 多为context | DCE或执行层缺失 | exact映射不足 | 需求、库存、期权完整性 | 低 |

## 六、机会排行榜（研究吸引力，不是胜率/仓位）

| 排名 | idea_id / 方向 / 周期 | 分项：逻辑/凸性/催化/价曲波/拥挤 | 总分 | 有效支持层 | 研究判断 / 证据 / 执行 | 反证、缺失与较前期变化 |
|---|---|---:|---:|---:|---|---|
| 1 | `COM-M-RU2701-SUPPLY-LONG-20261002` 条件多 3—10D | 19/17/14/13/10 | **73** | 3：价格、外盘、期权 | 存在待验证优势 / 部分 / 等30分钟回踩 | 国内contango与roll flag反对；夜盘量仓缺失。由69升73，原因是exact夜收+SICOM曲线新数据 |
| 2 | `COM-M-MA701-MOMENTUM-HOLD-20261009` 条件多 1—5D | 19/17/14/11/9 | **70** | 3：价格、curve/实体、期权 | 存在待验证优势 / 部分 / 等45分钟回踩 | 过热、IV高、exact夜收缺失；分数不变，实体补证被赔率恶化抵消 |
| 3 | `COM-E-AG2612-DAY-REVERSAL-LONG-20261009` 条件多 1—5D | 17/17/14/10/10 | **68** | 2：curve、期权 | 存在待验证优势 / 部分 / 等30分钟 | 5D仍弱、OI下降、黄金新增弹性低、exact夜收缺失；由71降68 |
| 4 | `COM-M-JM2701-MOMENTUM-CONTINUATION-20261010` 条件多 1—5D | 17/15/13/11/10 | **66** | 2：价格、curve | 存在待验证优势 / 部分 / 等30分钟 | DCE期权缺失、实体不足；不变 |
| 5 | `COM-M-C2611-WASDE-GAP-WATCH-20261010` 条件空 1—5D | 16/14/15/8/6 | **59** | 1：海外事件 | 证据不足 / 不足 / 仅观察 | 国内EOD未确认、DCE期权缺失；按1层上限≤59 |

分项均未超上限，总分已复核。RU的三层是：第1层价格、第4层SICOM外盘与近端结构、第5层期权右尾；第2层国内curve明确反对，第3层仅context。层数不自动决定下单；执行报价、触发与风险参数仍独立受限。

### 旧建议台账

- RU沿用原`idea_id`，首次提出2026-10-02。周五夜盘可能触及原20500入场区间，但无分钟路径、无成交反馈，故**触发状态未知**；不得假设用户持仓。原TP1 21200已很近，当前新仓不得按旧条件追入。
- MA、AG沿用10月9日idea_id。MA的实体证据增强但价格过热；AG因外盘未扩张和night缺失下调。变化原因分别是新数据/价格变化与证据修订，不是每天重置观点。
- JM、C仍为观察；原SC空头研究继续取消。若此前已按旧条件建立SC空头，只能依据当前账户与新保证金自行评估，本报告不声称持仓或账户净敞口。

## 七、前三名交易卡（当前均等待触发）

### 1. RU2701 条件多｜`COM-M-RU2701-SUPPLY-LONG-20261002`

- **事实**：10/9 EOD close/settle=20645/20220，日盘+2.89%，ΔOI +17339，domestic near-next=-3.86% contango并有roll flag。合约级fallback夜收20980；`return_vs_close=+1.62%`、`return_vs_settlement=+3.76%`。night open/high/low、volume、OI、ΔOI、source timestamp精确分钟均missing。
- **市场隐含与分歧**：市场已计入供给扰动；我们的分歧不是“仍会无条件上涨”，而是外盘近端backwardation与夜盘延续尚未被国内contango确认。只有回踩承接且contango收窄，剩余赔率才成立。
- **工具选择**：首选RU2701期货的条件单研究；RU 2026-12-25期权仅研究1×1、约30—45Δ call spread，ATM20250、IV27.00%、RV20 21.927%、RR25 +3.22%、BF25 0.68%，S/P/E=Y/Y/N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场与成交情景**：09:30后；好=20750—20900回踩、20700守稳且contango收窄，可用NAV 0.25%试仓；中=20900—21050，须突破前30分钟高点后回踩；坏=>21200无回踩或contango扩大，放弃。原20500窗口已经过去，不能作为当前条件单。
- **风险/退出**：当前新仓计划止损20480；原逻辑失效位19900不变。TP1仍21200仅作首次减仓锚，TP2 21800；若入场后3日不扩张退出，最长10日。好/中情景到TP1的剩余R偏低，若净R不足1.5则不做。
- **参数/压力**：交易单位10吨/手，tick 5元/吨，tick value 50元；按20980名义209800元/手；LTD 2027-01-15，实物交割。当前保证金率和涨跌停幅度未确认，故1/2板压力损失不能可靠给数；期货最大损失不由结构限定。12月前评估移仓，禁止接近交割。
- **弹性/催化/放弃**：夜盘相对close为正但显著低于相对settlement，边际弹性仍正、并非+3.76%的全新增信息。1—10D看东南亚供给、SICOM、国内curve；若09:30后跌破20700、SICOM转弱、contango扩大或参数仍不可核，放弃。

### 2. MA701 条件多｜`COM-M-MA701-MOMENTUM-HOLD-20261009`

- **事实**：10/9 close/settle=3338/3321，1D +6.04%，5D +14.83%，volume1493099、OI761175、ΔOI+70427，curve +16.08%。价涨仓增只作归因线索。10/8港口样本库存30.51万吨、环比-22.47%；exact-contract night close missing。
- **市场隐含与分歧**：市场已定价显著短缺甚至挤仓。我们的优势只存在于回踩后的承接，不存在于高开追价；MTO利润负反馈、伊朗浮仓释放是最强竞争解释。
- **工具选择**：MA701期货；2026-12-11、30—45Δ 1×1 call spread仅研究，ATM3300、IV45.655%、RV35.677%、RR25 +2.02%、BF25 1.445%，S/P/E=Y/Y/N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/分批**：09:45后；好=3330—3350回踩并收复前15分钟VWAP，先半；中=3350—3380缩量回踩，再半；坏=>3480或无回踩，放弃。任何周五宽口径夜盘涨幅不作为订单锚。
- **风险/退出**：止损3270，日收<3250逻辑失效；TP1 3460减半，TP2 3580；2日不扩张退出、最多5日。试仓最大损失NAV 0.25%—0.50%。
- **参数/压力**：multiplier10吨/手、tick1元/吨、tick value10元；按3338名义33380元，保证金率7%约2336.6元；涨跌停6%，1板约2002.8元/手、2板简单压力约4005.6元/手；LTD 2027-01-14。夜盘有交易但本次exact记录缺失；交割风险当前低，需滚动。
- **催化/放弃**：1—5D库存、进口到港、MTO利润与curve。若backwardation快速收窄伴价格跌破3330、OI继续增而承接失败，或无法获得实时报价，放弃。

### 3. AG2612 条件多｜`COM-E-AG2612-DAY-REVERSAL-LONG-20261009`

- **事实**：10/9 close/settle=14717/14515，1D +0.88%，5D -7.99%，volume303600、OI290434、ΔOI-4332，curve +0.54%。exact night close missing；07:00黄金4191.40，较周五4194.36近乎无新增扩张。
- **市场隐含与分歧**：市场隐含急跌后的脆弱反弹；我们的分歧是14650若获日盘承接，近端curve和海外贵金属尾部仍可支持反转，但OI下降、5D弱势与黄金弹性低是强反证。
- **工具选择**：AG2612期货；2026-11-24、30—45Δ 1×1 call spread仅研究，ATM14500、IV36.385%、RV31.436%、RR25 +1.75%，S/P/E=Y/N/N。`research only; manual quote and manual confirmation required before execution; no premium quoted`。
- **入场/分批**：09:30后；好=14650—14720守稳，半仓；中=14720—14800回踩承接，再半；坏=>14850无回踩、>15200或开盘后跌破14650，放弃。首跳不追。
- **风险/退出**：计划止损14380，日收<14250逻辑失效；TP1 15150、TP2 15700；2日不扩张退出，最多5日；试仓损失上限NAV 0.25%。
- **参数/压力**：稳定乘数15千克/手，按14717名义约220755元/手；LTD 2026-12-15。当前tick、保证金、涨跌停与夜盘精确参数未完整确认，tick value及1/2板压力损失不填；期货最大损失不有限，11月底前主动滚动。
- **催化/放弃**：1—5D COMEX银/金、USD/CNH与地缘；若银跌破58.5美元、AG跌破14650且curve转弱，或执行参数/报价仍缺，放弃。

## 八、商品期权专项

- **截面日期与readiness**：10月9日是最新有效T-1截面；181/185 surface-ready，41 positioning-ready，0 execution-ready。周五夜盘后RU标的上移1.62%，其moneyness需09:00重置；旧ATM不能冒充当前可成交strike。
- **IV-RV**：AG +4.95 vol、MA +9.98 vol、RU +5.07 vol、SC约+0.98 vol。IV高于RV不是自动卖波证据；地缘/供给事件会使历史RV低估跳空。
- **skew/event convexity**：AG/MA/RU RR25均为正，右尾需求已被部分定价；有限支出价差优于裸买，但没有bid/ask，不能给权利金、盈亏平衡、净R或Greeks。
- **vol RV**：可比较方向性波动预算，不能在缺同到期/同Delta/成交成本时称跨品种套利。SC近月到期10月14日，事件与theta都极端，回避未报价裸卖波。
- **明确回避**：DCE期权；dealer gamma方向推断；以PCR/OI断言机构方向；无execution readiness时虚构净成本和滑点。

## 九、09:00开盘风险地图

三层严格分开：①Previous China EOD=10月9日；②Current Trading Day Night Session=10月9日晚、归属10月12日，但仓库缺失，仅RU2701 exact-close fallback；③07:00 Overseas为Reuters/LSEG、SICOM前收与周末事件。海外变化尚未被周一中国日盘交易。

| 品种 | 可能开盘 | 夜盘是否完成定价 | 内外/事件冲突 | 首跳 | 等待 | 09:00后确认 |
|---|---|---|---|---|---|---|
| RU/NR | 偏高，RU易冲高回落 | RU部分：+1.62% vs close；量仓/curve未确认 | SICOM近强支持；国内contango反对 | 不追 | 30分钟 | RU20700、20980/21200、近远月、SICOM |
| MA | 高开/高波动 | exact未知；日盘已预交易大部分短缺 | 库存低支持；5D过热与MTO负反馈反对 | 不追 | 45分钟 | 3330—3380、VWAP、curve、ΔOI |
| AG | 平高开 | exact未知 | 周五银强但周一金近乎平、人民币平 | 不追 | 30分钟 | 14650、COMEX银、USD/CNH、curve |
| SC/LU/FU/BU | 高波动，方向不确定 | exact未知 | 沙特袭击支持尾部；Brent-0.17%、设施损坏未证实、美湾复产/SPR反对追多 | 不追 | 45分钟 | Brent/WTI、装船/设施事实、人民币、curve；收盘后新保证金 |
| JM | 平高开 | exact未知 | 国内价曲强；实体和期权缺失 | 不追 | 30分钟 | 1539.5、curve、成交/OI |
| C/M | 平开 | exact未知 | CBOT豆近乎平，WASDE国内传导仍待证 | 不追 | 45分钟 | exact CBOT品种、人民币、基差 |
| LC | 平/低开 | 制度上无夜盘 | 周五弱、缺海外exact锚 | 不追 | 45分钟 | 117000、curve、成交/OI |
| EC | 高波动、方向不确定 | 制度上无夜盘 | 地缘可能抬运价；周五价格/curve弱 | 不追 | 45分钟 | 运价事实、2700、curve；不抄底 |

若开盘gap超过1个当日波动尺度，所有静态入场价自动转“待重新报价”。09:15只用于观察首跳；RU/AG最早09:30，MA/能源/农产品最早09:45。今天收盘后油品新保证金与涨跌停生效，今晚21:00 FU/BU限额生效，隔夜仓必须重算。

## 十、未来24小时 / 7日事件日历（北京时间）

| 窗口 | 事件 | 处理 |
|---|---|---|
| 10/12 09:00 | 中国商品周一日盘重开 | 所有候选等15/30/45分钟；gap大则取消旧条件 |
| 10/12 收盘结算 | SC/LU/FU/BU新涨跌停与保证金生效 | 降杠杆，油品同因子合并；按新参数重算1/2板压力 |
| 10/12 21:00 | 下一夜盘，归属10/13；FU/BU指定合约1500手日内开仓限额开始 | 不追首跳，评估流动性与滑点 |
| 10/12—10/14 | Riyadh WPC Energy与沙特安全局势 | 油品Delta/Vega双跳风险；有限凸性或延迟入场 |
| 10/14 | SC2611期权到期与IEA常规事件窗口 | 近月theta/行权交割风险高；不卖未报价波动 |
| 未来24—72h | 美国海湾平台复产/损坏评估、SPR执行 | 复产压风险溢价；损坏/延迟相反，等待事实 |
| 未来7日 | EIA、CFTC、USDA/天气、交易所临时参数 | 精确时点须按官方日历当期核验；发布前后减Delta或限定最大损失 |

风险预算：单一试仓最大损失NAV 0.25%—0.75%；确认交易0.75%—1.50%；单一高确信主题总风险≤2.5%—3.0%。油品、化工、橡胶按能源/通胀共因子合并。压力测试包括1/2涨跌停、相关性破裂、流动性消失、gap、保证金上调、IV跳升/塌陷、交割挤压与人民币急变。

## 十一、覆盖核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足 | 不适用/流动性不足 | 未入榜板块最值得跟踪的异常/依据 |
|---|---|---|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/9 EOD与curve | DCE期权、实体多为context | 0 | JM价曲强但仅2层；其余未见跨层独立异常 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | 部分实体/元数据，AG exact night缺 | 0 | SN跌价增仓是早期异常；CU外盘强需09:00确认 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 22/22 | SC/LU physical；多数exact night；TA/PF/PR期权失败 | 0 | 油品事件/风控异常最高但方向冲突；BR强只作交叉验证 |
| 新能源 | LC/SI/PS及GFEX新材料 | LC/SI/PS与动态品种初筛 | exact海外/执行期权部分不足 | 0 | LC价跌仓增与正curve冲突，不追空 |
| 农产品油脂饲料畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 18/18 | DCE options、CJ期权失败；CBOT exact映射部分不足 | 0 | C/M OI变化仅归因线索；无可执行RV |
| 航运软商品 | EC及CF/SR/AP/CJ/PK | 6/6 | EC运价口径未exact对齐 | 0 | EC深contango且跌幅大，是异常但不是抄底信号 |
| 动态新增/低流动 | 引擎77品种 | 72个完成量价/curve扫描 | JR/PM/RI/WH/ZC | 5 | 缺失不等于无机会；因流动性/历史不足不入榜 |

策略类别已扫描：方向、基差/跨期、curve、跨品种/跨市场、风格/中性、波动率/偏度、事件凸性。跨市场和basis因非exact口径只作context；未定义篮子不写成dollar-neutral或beta-neutral。周期覆盖1D/3D/5D/20D；历史不足不输出伪趋势。

## 来源

1. [China-Commodities-Engine](https://github.com/farfromexact/China-Commodities-Engine) — 统一输入生成于2026-10-11、行情源日2026-10-09；支持EOD、curve、Physical、Night状态、Options与Metadata质量。
2. [Reuters/LSEG Markets Performance](https://www.reuters.com/markets/companies/1299.H/charts/) — 2026-10-12约07:00访问；支持金、铜、Brent、CBOT大豆屏显值。
3. [Reuters：Saudi Arabia reports injuries in new attack](https://www.reuters.com/world/middle-east/yemens-houthis-renew-warning-over-saudi-airports-after-deadly-riyadh-attack-2026-10-11/) — 2026-10-11；支持机场袭击和Aramco声称未确认。
4. [生意社：RU2701夜盘收20980](https://www.100ppi.com/news/detail-20261010-6320147.html) — 2026-10-10；支持合约级夜收与相对结算涨幅。
5. [RTAS：SGX SICOM官方结算](https://www.rtas.sg/) — 2026-10-09；支持TSR20/RSS3期限结构。
6. [Investing：USD/CNH](https://www.investing.com/currencies/usd-cnh-historical-data) — 2026-10-12访问；支持6.6930与前收6.6927，作fallback/proxy。
7. [新华财经/新浪：10月9日商品日报](https://finance.sina.com.cn/roll/2026-10-09/doc-iniurvzz2728886.shtml) — 2026-10-09；支持甲醇港口样本库存30.51万吨及环比变化。
8. [上期能源：SC/LU参数调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833670.html)｜[上期所：FU/BU参数调整](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833667.html)｜[上期所：FU/BU交易限额](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833668.html) — 2026-10-09；支持10月12日收盘/夜盘后的风控变化。
9. [SHFE：Natural Rubber Contract Specifications](https://www.shfe.com.cn/docview/docview_211235554.htm) — 稳定合约参数页；支持10吨/手、5元/吨tick、实物交割和LTD规则；不用于当前动态保证金/涨跌停。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：09:30后RU2701仅在20750—20900回踩、20700守稳且contango收窄时试仓；MA701与AG2612分别等09:45/09:30再人工确认，不预挂开盘单。
C. 今天应继续观察的机会：RU/SICOM结构、MA低库存与过热消化、AG反转、JM动量，以及沙特事件对SC/LU/FU/BU的真实供应传导。
D. 今天必须避免或退出的交易：避免RU>21200、MA>3480或能源首跳追价；避免无bid/ask期权、DCE缺失链、EC抄底，以及未按新保证金重算的油品隔夜敞口。
