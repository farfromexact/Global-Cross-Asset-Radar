# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-17｜版本：commodities_morning｜prompt_version：radar_2026-10-12_stock_v1**  
**生成时间：2026-10-17 07:05 北京时间｜研究截点：07:00 北京时间**

## 一、今天一句话结论

**截至本报告时点，无可立即执行的合格新交易；周末休市、油价急升，但中国Night交易日标记异常，周一只验证SC、BR与LH。**

研究机会与“今天能下单”必须分开：境内商品周六无日盘，期权执行报价为零；最有价值的三项验证是SC2612对海外油价的周一映射、BR2612精确合约/曲线确认、LH2701弱势结构是否破位。优势不足的是追涨贵金属与追空LC/AP；数据不足不能判断的是DCE夜盘、当前期权、所有A级/ B级基差套利与受异常日期影响的Friday Night。

## 二、时间、数据质量与覆盖

### 2.1 时点与会话

- 最近完整中国会话：**2026-10-16 EOD**；今日为周六，无中国商品日盘。下一实际可交易窗口为**2026-10-19 09:00北京时间**。
- 上海国际能源交易中心规则把交易日定义为周一至周五（法定假日除外）；上期所连续交易规则又明确“交易日第一节”从前一营业日晚间开始。因此2026-10-16晚间至10-17凌晨的交易应归属**2026-10-19交易日**，而不是周六10月17日。
- 仓库Night却记录 `trading_date=2026-10-17`、`session_start_date=2026-10-16`。本报告将414条夜盘记录整体标为**calendar_semantics_error并隔离**，不自行重标、不计入证据层、不用于触发成交；只把个别原始价格作为待核背景。没有可靠exact-contract替代，`night_session_fallback_used=false`。
- 海外层截至周五收盘：Brent结算109.86美元/桶（+3.7%），WTI 101.41（+3.5%）；仓库公共连续代理为109.64/101.84。周五19:30以后油价继续上冲，是周一中国开盘仍未交易的新信息，不是境内已完成定价。

### 2.2 固定快照与质量

- 商品引擎：[`farfromexact/China-Commodities-Engine@16ebd46fcf8311d64f635eb3415e70d644aaa2f4`](https://github.com/farfromexact/China-Commodities-Engine/tree/16ebd46fcf8311d64f635eb3415e70d644aaa2f4)。统一输入requested_date=2026-10-16，generated_at=2026-10-17T06:15:34.797086+08:00。
- Futures/Market State：806合约、77品种、SHFE/INE/DCE/CZCE/GFEX五所，`full_market_ready=true`、source_date_match=100%、critical errors=0；8条OHLC占位已剔除。1/3/5/20日同合约、RV20、量仓z与near-next曲线可用。
- Physical：20目标中18条在原生频率内有效、SC/LU两条不可得；18条现货基差均为C级，只作背景。仓单28条中5条carried-forward，不算新增催化。
- External：17/22目标fresh，但均为`context_only`；Dubai/Oman、Singapore HSFO/VLSFO、DXY、USDCNH缺官方等价映射。联网补充只用于海外收盘与事件，不称可执行跨市套利。
- Options：module-specific仍为2026-10-14，14506合约、41/64品种、185 series；IV覆盖100%、OI覆盖79.50%、bid/ask覆盖0%。全局surface/positioning/execution均false；局部185个surface与97个positioning也因日期落后和Friday Night标的移动而不能当当前报价。10月16日root尝试10810记录但state=empty、未发布，不能覆盖旧模块。
- Metadata：partial。AG2612/BR2612/SC2612只有上市/到期等部分官方字段；乘数、tick、保证金、限幅、夜盘参数缺失。DCE元数据不可得；因此本报告的期货止损只是计划，不是最大损失上限。
- Night状态：request806、record414、product44、outside-window171、no-night7、query_error/unresolved各214（全部DCE），missing timestamp/price/quote为0，coverage=51.36%但`coverage_complete=false`；明细文件为真实0字节。流程validated/published不能覆盖日期语义错误。
- Stock固定快照：[`farfromexact/China-Stock-Engine@fedd4009648646888f86214bfecae9e545cecb42`](https://github.com/farfromexact/China-Stock-Engine/tree/fedd4009648646888f86214bfecae9e545cecb42)。价量只到10月15日，research_asof=2026-10-16 07:38北京时间；复权公司行动、预测、证券执行状态不完整。本期仅核紫金矿业金/铜利润桥，不列股票候选。

实际读取：商品 `data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`、`data/night_session/latest.json`、`data/contract_meta.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/options/latest.json`、`data/external/latest.json`；股票状态、manifest、reference、research inputs、exposure mapping与 `data/latest/research_9_002.json`。

## 三、商品仪表盘（展示12项；实际扫描77品种）

1D为收盘相对前收；curve为近月减次月占次月比例。Night列均是被隔离的原始背景，不视为合法T=10/19会话。

| 板块/品种 | 精确主力 | 10/16 close/settle | 1D / 5D | 成交量 / OI / ΔOI | curve | Physical | 隔离Night原始背景 | 07:00海外收盘/期权 | 周一信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|
| 原油 SC | SC2612 | 711.8 / 723.0 | -1.85% / +0.64% | 119673 / 32965 / +3173 | +0.84% backwardation | SC实体缺 | O698.5/H740/C739.8，vs前收+3.93%，日期错 | Brent109.86、WTI101.41；exec否 | 高开风险；等30–45分钟，不追首跳 |
| 燃料油 FU | FU2701 | 4819 / 4770 | -0.35% / +7.43% | 327042 / 211067 / +8765 | +7.92% backwardation | C级 | 代表FU2611 +2.78%，不能替代 | 油价强；exec否 | 精确合约缺，观察裂解/曲线 |
| 丁二烯胶 BR | BR2612 | 15915 / 15975 | +1.79% / -2.41% | 105309 / 75757 / +9537 | +1.10% backwardation | 缺 | 代表BR2611 +0.34%，不能替代 | 无高质量国际胶价；exec否 | 价量仓最强，待精确报价 |
| 白银 AG | AG2612 | 14029 / 13889 | +2.49% / -4.31% | 323505 / 282779 / -10546 | -0.10% contango | 缺 | C13835，vs前收-1.38%，日期错 | COMEX银57.13；T-2且exec否 | 偏低/平开，先看13830–13890 |
| 黄金 AU | AU2612 | 901.82 / 898.80 | +1.36% / -0.03% | 194252 / 222956 / -620 | -0.13% contango | 缺 | C895.8，vs前收-0.36%，日期错 | COMEX金4186.5；exec否 | 内外冲突，等15分钟 |
| 铜 CU | CU2611 | 109860 / 109450 | +0.10% / -0.15% | 106448 / 176863 / -12136 | +0.63% backwardation | C级 | C109420，vs前收-0.40%，日期错 | LME3M铜14359；DXY缺 | 平/略低；不把LME当套利 |
| 碳酸锂 LC | LC2701 | 96320 / 99080 | -4.20% / -16.56% | 358976 / 425349 / +6802 | +0.92% backwardation | spot101000、basis C | 制度无夜盘 | 无精确海外映射；exec否 | 跌势与backwardation冲突，禁追空 |
| 苹果 AP | AP701 | 5998 / 6096 | -3.32% / -11.68% | 246249 / 169454 / +8417 | +15.11% backwardation | 缺 | 制度无夜盘 | 国内独立；exec否 | 交割/季节结构优先，禁追空 |
| 豆粕 M | M2701 | 3281 / 3299 | -1.77% / -2.66% | 1234349 / 2321910 / -61019 | -1.69% contango | spot3358、basis C | DCE query_error | CBOT豆1260.5；中国新增采购 | 弱势与外需冲突，等30分钟 |
| 生猪 LH | LH2701 | 10490 / 10475 | +0.24% / -6.89% | 174035 / 182448 / +8124 | -3.72% contango | 缺 | 制度无夜盘 | 国内独立；DCE期权缺 | 只在破10450且不收回时看空 |
| 烧碱 SH | SH701 | 1726 / 1735 | -1.82% / -6.06% | 207684 / 207093 / +41022 | +0.29% backwardation | 缺 | 明细缺；日期错 | T-2局部surface | 增仓下跌但曲线反对追空 |
| 纯碱 SA | SA701 | 939 / 940 | +0.21% / -7.02% | 1039014 / 1365611 / -11911 | +1.98% backwardation | 仓单3163、日减400；basis C | C956，vs前收+1.81%，日期错 | 国内独立；exec否 | 旧空继续取消，周一重新观察 |

## 四、相对前序的3—6项真正变化

1. **SC的“重夺723”已变成周末缺口问题。** 隔离的原始会话从前收711.8升至739.8，但仓库错误写成周六交易日；随后Brent又结算到109.86。方向支持增强、执行赔率变差，原idea不视为已触发或已成交，周一必须等待开盘吸收。
2. **油价在境内停止交易后继续上涨。** 周五19:30附近Brent约106.28、WTI97.78，最终结算109.86/101.41；这是3%以上新增海外冲击。SC/LU/FU不能用此前Night涨幅替代这段外盘新增。
3. **AG的境内修复失去同步确认。** 10/16 EOD上涨且减仓；隔离Night原始收盘13835、相对前收-1.38%，而COMEX银最终57.13，没有形成强外部加速。前序回踩多头下调为观察，不能把13830低点触及当保证成交。
4. **BR仍是国内价格/曲线最干净的异常，但精确Night没补齐。** BR2612 EOD价、量、OI和backwardation同向；统一层只给BR2611代表值，明细空，故排序保留、执行继续冻结。
5. **农产品出现外需信息而国内价格未确认。** 中国国有买家新增采购10–13船美国大豆，连同本周此前采购约18–23船；M2701却EOD下跌并大幅减仓。它是周一的冲突验证，不是直接多豆粕依据。
6. **CFTC 10月13日持仓报告已按计划发布。** 官方页面可用，但本次未完成每个精确合约的净头寸变化复核；不把“报告已发布”当拥挤层支持。

## 五、产业链地图与Stock利润桥

1. **原油—燃料链（偏多、执行置信度低）**：SC EOD弱但曲线backwardation，海外原油急涨；FU/LU曲线更强。最强是外部供应冲击，最大反证是周末gap、IEA/政策供给释放与SC实体缺失。紫金等股票不是该主题的纯表达。
2. **贵金属—矿业（中性偏多、置信度中低）**：EOD AG/AU修复，Friday Night原始背景转弱，COMEX收盘仅温和支持；曲线contango、OI下降。紫金矿业2026H1合并口径收入1941.78亿元、归母净利391.70亿元、经营现金流554.72亿元，确认矿产金/铜业务，但实现售价还受销量、套保、汇率、成本与少数股东影响；股票价量只到10月15日、执行状态未知，**直接商品更纯、股票不列候选**。
3. **橡胶链（BR相对强、置信度中低）**：BR2612强于RU/NR，价量仓与backwardation同向；缺精确BR Night、实体库存/加工利润和国际胶价，不能跨月替代。
4. **黑色—建材链（无明显优势）**：I2701 1D settlement return约+0.30%、5D约-1.39%，黑色整体无同向价格/曲线/实体共振；DCE夜盘214合约报错。SA原始Friday Night上涨但日期异常，旧空不恢复。
5. **油脂油料—养殖 / 新能源（冲突）**：CBOT豆1260.5与中国采购支持外需，M国内弱且减仓；LH中期弱与日盘止跌并存；LC急跌但backwardation。无任何一项同时跨过三层证据与执行门槛。

## 六、统一机会榜（研究吸引力，不是胜率）

| 排名 | idea_id / 方向 / 工具 | 逻辑25 | 赔率25 | 催化20 | 价曲波15 | 拥挤15 | 总分 | 有效支持层 / 反证 | 三轴状态 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | `COM-M-SC2612-EIA-SETTLE-RECLAIM-LONG-20261016` / 条件多SC2612 | 19 | 15 | 15 | 10 | 9 | **68** | 2曲线、4海外；1 EOD反对，3/5缺，Night隔离 | 待验证优势 / 部分 / 周一等触发参数 |
| 2 | `COM-E-BR2612-CURVE-MOMENTUM-LONG-20261016` / 条件多BR2612 | 18 | 15 | 9 | 12 | 10 | **64** | 1价格量仓、2曲线；3/4/5缺 | 待验证优势 / 部分 / 待精确报价 |
| 3 | `COM-E-LH2701-WEAK-CURVE-SHORT-20261013` / 条件空LH2701 | 17 | 14 | 8 | 11 | 11 | **61** | 1中期价格、2contango；3/4/5缺 | 待验证优势 / 部分 / 周一日盘确认 |
| 4 | `COM-M-AG2612-RATE-RELIEF-REBOUND-LONG-20261016` / 观察AG2612 | 16 | 13 | 11 | 8 | 8 | **56** | 4海外弱支持；1/2反对或冲突，3/5缺 | 优势不足 / 不足 / 不执行 |

SC/BR/LH最多只有两层有效独立支持，得分均≤69；AG只有一层弱支持，≤59。隔离Night没有被当成第六层或新增支持。

## 七、研究/交易卡（3张，不构成订单）

### 卡1｜SC2612：海外供应冲击后的周一映射

- **事实**：10/16 close/settle=711.8/723.0，ΔOI=+3173，curve=+0.84% backwardation；隔离Night原始O/H/L/C=713.1/740/698.5/739.8、ΔOI=+763，但交易日字段错误。Brent/WTI周五结算109.86/101.41。
- **定价/推断/主观**：海外新增足以支持高开，但市场错价尚未证实；最大竞争解释是周末风险溢价已被Friday Night和周一集合竞价一次性吸收。主观判断是“方向偏多、赔率不适合首跳”。
- **表达**：只研究SC2612线性多头；期权execution=false，不能编腿、权利金或Greeks。乘数/tick/保证金/限幅缺失，参数确认前不可下单。
- **入场**：好=周一09:30后仍站723且首跳回撤不破730、Brent未回落至106下；中=09:45后745以内重新放量；坏=>750追价，放弃。
- **失效/退出**：计划止损718；逻辑失效为30分钟收回723下方或Brent跌破106。TP1=760，TP2=780；若10月19日14:30仍无跟随则时间退出。期货止损非最大损失。
- **压力**：按1/2涨跌停、流动性消失、周末地缘反转、保证金上调测试；试仓风险预算NAV 0.25%–0.50%，与FU/LU/油运同因子合并。

### 卡2｜BR2612：价量仓与曲线同向，但缺精确Night

- **事实**：10/16 close/settle=15915/15975，1D+1.79%、ΔOI+9537（+14.40%）、curve=+1.10%。隔离Night只有BR2611代表C=16045、vs前收+0.34%，不能替代BR2612。
- **定价/推断/主观**：市场可能在交易近端供应偏紧；最强反证是5D仍-2.41%、实体/国际胶价缺失、Friday Night exact-contract不可核。主观仅保留动量观察。
- **表达**：1手BR2612条件多头研究；不做BR2611替代，不给期权结构。乘数/tick/保证金/限幅未知。
- **入场**：好=周一09:30后BR2612守15900且精确near-next backwardation≥0.8%；中=15960–16020二次确认；坏=>16080追入，放弃。
- **失效/退出**：计划止损15680；30分钟收低15680或backwardation<0.5%失效。TP1=16350、TP2=16800；3个交易日未到TP1时间退出。
- **压力**：一/二板、跨月相关性断裂、流动性骤降；与RU/NR同因子合并，试仓风险≤NAV 0.50%。

### 卡3｜LH2701：弱趋势/contango条件空

- **事实**：10/16 close/settle=10490/10475，1D+0.24%、5D-6.89%、ΔOI+8124，curve=-3.72% contango；无夜盘。DCE元数据、当前期权和高质量本期实体变化缺失。
- **定价/推断/主观**：中期弱势与contango支持空头，但周五止跌是反证。最强竞争解释是现货企稳/季节性补栏预期已被价格提前反映。
- **表达**：只研究LH2701线性空头；周一09:30后跌破10450且30分钟不能收回才成立。好=10430–10450，中=10400–10430，坏=<10350追空，放弃。
- **失效/退出**：计划止损10630；收盘>10700且contango收窄为逻辑失效。TP1=10150、TP2=9800；5个交易日未到TP1退出。合约乘数、tick、保证金、限幅、最后交易日未验证，执行冻结。
- **压力**：猪价政策/疫病headline、无夜盘gap、涨跌停与流动性；试仓风险≤NAV 0.25%，不得与饲料空头伪装分散化。

## 八、商品期权专项

- 样本日期2026-10-14，落后两个交易会话；14506合约、41/64产品、185 series，IV字段全覆盖但不是当前可成交surface。
- 全局surface/positioning/execution=false；局部surface185、positioning97、execution0，bid/ask=0%、OI=79.50%、model Greeks=0%。dealer Gamma方向未知。
- Friday Night标的已大幅移动（尤其SC），旧strike moneyness不可直接比较；不做IV-RV“便宜/昂贵”结论，不给净权利金、最大净支出或具体腿。
- 事件凸性：原油周末地缘与周一中国宏观理论上适合有限亏损结构，但只有在周一取得实时双边报价、合约乘数/行权交割和滑点后再设计；否则线性仓也不因“可买期权”而获得封顶损失。

## 九、下一开盘风险地图（2026-10-19 09:00）

| 品种 | Previous China EOD | Current T Night | 07:00 Overseas | 预期开盘/是否已定价 | 追价与等待 |
|---|---|---|---|---|---|
| SC2612 | 711.8/723.0，curve+0.84% | **无合法T=10/19仓库会话**；739.8原始值隔离 | Brent109.86、WTI101.41 | 高开概率高，但海外尾段未被中国交易 | 不追；等30–45分钟，看723/730、OI、Brent |
| AG2612 | 14029/13889，OI下降 | 13835原始值隔离 | COMEX银57.13、金4186.5 | 平/偏低，境内夜原始值已部分反映 | 等15分钟；13830–13890与OI确认 |
| CU2611 | 109860/109450，OI下降 | 109420原始值隔离 | LME3M铜14359 | 平开附近，内外信号弱 | 等15–30分钟；看109400与人民币 |
| M2701 | 3281/3299、减仓 | DCE query_error | CBOT豆1260.5，中国新增采购 | 不确定，未完成中国预交易验证 | 等30分钟；看3299/3300及成交OI |
| BR2612 | 15915/15975、backwardation | exact-contract缺 | 无可靠国际胶价 | 不可判断 | 等30分钟，必须先取BR2612与curve |
| LH2701 | 10490/10475、contango | 制度无夜盘 | 无直接海外映射 | 平开优先 | 等30分钟；仅破10450且不收回 |

周六不存在“9:00即刻交易窗口”；以上全部是周一待验证方案。已过的Friday Night不被写成未来建议。

## 十、未来24小时 / 7日事件与覆盖核对

### 事件日历（北京时间）

- **已发布，10月17日03:30**：CFTC 10月13日COT。用途=下周拥挤复核；本次未逐合约完成净头寸变化，不增分。
- **未来24小时**：中东/红海/霍尔木兹周末headline与油田、炼厂、航运事件。Delta处理=不持有新增境内线性仓；Vega处理=只有可成交限损结构才讨论。
- **10月18日起**：LME Week。关注铜铝现货升贴水、仓库与贸易流讨论；不把会议观点当库存事实。
- **10月19日（官方精确时刻待核）**：中国Q3 GDP及月度宏观重点。黑色、有色、人民币敏感；周一开盘后延后15/30/45分钟确认。
- **10月21日22:30**：EIA周报标准周三10:30 ET时点；同时EIA调整部分油价数据发布。SC/LU/FU降低线性风险，等待真实报价后才考虑有限凸性。
- **10月24日03:30**：下一次CFTC计划发布。仅作拥挤验证。
- **7日内未核实到确定发布**：OPEC+会议、IEA月报、USDA/WASDE新月报；不编造时点。天气、矿山、油田、炼厂、化工、农业和公司公告若无原始披露，只列为headline风险。

### 覆盖核对

- **应覆盖**：固定63代码全部保留，并扫描引擎77品种、806合约；动态新增包括BZ、PL、PD、PT、RS、RR、OP、WR、LG等。
- **实际取得且分析**：黑色/建材10品种、有色/贵金属14、能源化工26、农产品/油脂畜牧14、新能源3、软商品10；方向、1/3/5/20日、RV、量仓、曲线、实体/海外/期权可得项均初筛。
- **数据不足**：所有Friday Night受交易日语义错隔离；DCE 214合约Night query_error/unresolved；Night明细空；SC/LU实体缺；全部A/B基差缺；当前期权报价缺；DCE元数据缺；海外Dubai/Oman、燃料油、DXY、USDCNH缺精确映射。
- **不适用/低流动性**：JR/PM/RI/WH/ZC等代表行出现零成交/零持仓/占位，不入排行；无夜盘品种不因制度性无夜盘被判失败。
- **未入榜板块最重要异常/无异常依据**：黑色仅I小幅反弹、无跨层共振；有色CU国内去仓且LME反弹弱；能源FU/LU曲线强但精确Night/实体不足；农产品M与美国采购冲突；新能源LC弱价与backwardation冲突；EC 1D近持平但期限结构季节性/合约可比性不足，不称套利。

### 旧观点处置

- SC idea保留同一ID，从“723重夺”改为“周一gap吸收后再验证”，不认定Friday Night触发或成交。
- BR idea保留，因exact-contract Night缺失继续冻结。
- LH idea保留，周一日盘条件不变。
- AG idea由条件多降为观察；不假定此前已成交。
- 旧FU/SC相对价值、SA空头继续取消；不重新开启。

风险预算：试仓最大损失NAV 0.25%–0.75%，确认仓0.75%–1.50%，同一主题总预算≤2.5%–3.0%；油链、橡胶链、贵金属/矿业分别合并因子。压力测试含1/2涨跌停、周末gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压和人民币急变。

## 来源

- [China-Commodities-Engine unified input](https://github.com/farfromexact/China-Commodities-Engine/blob/16ebd46fcf8311d64f635eb3415e70d644aaa2f4/data/report_input_latest.json)（2026-10-16；EOD、Market State、Physical、External、Night、Options、Metadata）
- [Night session status](https://github.com/farfromexact/China-Commodities-Engine/blob/16ebd46fcf8311d64f635eb3415e70d644aaa2f4/data/night_session/last_run_status.json)（2026-10-17生成；日期、覆盖与错误）
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/16ebd46fcf8311d64f635eb3415e70d644aaa2f4/data/options/quality_latest.json)（2026-10-14；readiness与覆盖）
- [China-Stock-Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/fedd4009648646888f86214bfecae9e545cecb42/data/latest/research_inputs_latest.json)及[紫金分片](https://github.com/farfromexact/China-Stock-Engine/blob/fedd4009648646888f86214bfecae9e545cecb42/data/latest/research_9_002.json)（价量至10月15日；公司利润桥）
- [INE General Exchange Rules](https://www.shfe.com.cn/eng/services/Rules/INERules/202606/t20260603_831946.html)与[SHFE continuous trading rules](https://www.shfe.com.cn/upload/20140103/1388740411504.pdf)（交易日及Friday Night归属）
- [Reuters：10月16日油价与供应风险](https://www.reuters.com/business/autos-transportation/oil-edges-down-investors-weigh-possible-us-sanctions-shadow-fleet-2026-10-16/)；[Financial Times：最终结算价](https://www.ft.com/content/8ee22d89-03eb-48dc-99a5-27555373a89c)
- [Reuters：10月16日黄金](https://www.reuters.com/world/india/gold-set-weekly-drop-traders-assess-fed-signals-2026-10-16/)；[Reuters：中国新增采购美国大豆](https://www.reuters.com/world/asia-pacific/china-state-buyers-snap-up-more-us-soybeans-latest-post-summit-purchases-2026-10-16/)
- [CFTC COT发布日历](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)与[10月13日COMEX报告](https://www.cftc.gov/dea/futures/deacmxlf.htm)
- [EIA周报日历](https://www.eia.gov/petroleum/supply/weekly/schedule.php)

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：周末不挂可成交单；预设周一SC2612吸收gap后站稳723/730、BR2612精确合约守15900、LH2701破10450不收回才重评。  
C. 今天继续观察：油价周末headline、AG13830–13890、M2701与美国大豆采购冲突、LC/AP弱价与backwardation、紫金利润桥但股票数据落后一日。  
D. 今天必须回避或有条件退出：追SC首跳、用BR2611替BR2612、追涨AG/AU、追空LC/AP、把异常Night或T-2期权当当前报价；若此前按条件建立且原逻辑失效，依原止损退出。