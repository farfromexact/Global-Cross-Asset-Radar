# 全球跨资产机会雷达晚间版｜2026-11-04

生成/分析截点：**2026-11-04 20:03 BJT**。中国现金市场与商品日盘已收；欧洲开盘；美国仍为盘前，DST已于11月1日结束，现金盘于北京时间22:30开。今晚21:00商品夜盘归属11月5日交易日；股指期货与A股今晚没有常规夜盘。仅供投资研究，不代客下单；用户实际持仓未提供/未知。

## 1. 一句话结论

美国两院转蓝令长端利率与美元回落，中国稳市工具叠加超跌修复引爆成长股；但单日脉冲、黄金跳升和能源下跌均不宜追价，今晚只研究条件单。

## 2. 事实台账、数据质量与全覆盖

| fact_id | 标的/单位/口径 | 观测、known_at、读取 | 支持判断 | 局限 |
|---|---|---|---|---|
| F-CN-EOD-01 | A股指数/成交，EOD | 上证3686.17、沪深300 4101.34、科创50 1265.47；15:00 BJT；20:03读取[行情](https://news.10jqka.com.cn/20261104/c681452355.shtml) | 成长主导、成交约2.05万亿元 | 延迟公共行情，不是交易所原始文件 |
| F-CN-POL-01 | 回购增持再贷款，CNY/% | 11/4发布/known；利率降至1%，银行申请超2000亿元；[政策转载](https://jrj.wuhan.gov.cn/ynzx_57/xwzx/202611/t20261104_2873750.shtml) | 稳市资金价格下降 | 申请不等于已放款或已买股 |
| F-US-ELEC-01 | 美国国会控制权 | 11/4 ET结果、20:03读取；民主党取得两院；[Reuters](https://www.reuters.com/legal/government/democrats-seize-congress-sweeping-midterm-repudiation-trump-2026-11-04/) | 网格锁定、财政/关税立法路径收窄 | 总统否决与行政权仍在；不是A股盈利事实 |
| F-US-MKT-01 | ES/NQ盘前，% | 04:22 ET为+0.35/+0.16%，此前低点-1.4/-2.4%；[Reuters](https://www.reuters.com/business/us-stock-index-futures-steady-democrats-seize-congress-2026-11-04/) | 选举冲击已反转 | 不是20:03实时价 |
| F-AI-AMD-01 | AMD财报，USD | 11/3盘后known；Q3收入134亿、数据中心85亿/+97%，Q4约170亿±3%；[AMD IR](https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results) | AI需求与盈利兑现 | 指引是前瞻，盘前已重定价 |
| F-COM-01 | SC2612/AG2612，CNY/桶、CNY/kg | 11/4 15:20：681.6/-1.91%、12420/+3.39%；[准确合约横截面](https://www.9qihuo.com/hangqing) | 能源去风险、贵金属重定价 | 非官方结算，volume/OI未独立复核 |
| F-OPT-01 | HO/IO/MO 2612，IV vol | 11/3 EOD、11/4 07:19生成；ATM 16.62/21.38/37.66、RR25 -1.32/-1.88/-5.11；[引擎](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json) | last-good偏度背景 | 不是11/4当日期权，不可执行 |

仓库身份：Global manifest `f50210…`、11月4日晨报 `9b18cd…`、11月4日商品晚报 `75e2f2…`；China Options `e25a16…`；China Commodities status `808820…`；China Stock status `5a2937…`。仅在真实取得时记录SHA。

| 模块 | requested / source / generated | coverage与能力 | 状态 |
|---|---|---|---|
| China Options | 11/3 / 11/3 EOD / 11/4 07:19 | 760/760官方链匹配；HO/IO/MO多期限可分析 | `available/published/analytically_ready=true`仅对11/3；11/4执行=false；history文件empty |
| Commodity Futures | 11/4 / current run 0；last-good 11/2 806合约/77品种 / 19:06 | 五所目标完整；另取11/4精确合约横截面 | full_market_ready=false、critical errors 15；不把部分失败扩散到其他资产 |
| Market/Physical/External | market last-good 11/2；physical 18/20、external 17/22 fresh 11/4 | basis 18条均C级、0 eligible；external仅context | 可研究背景，不构成可交易basis/跨境套利 |
| Commodity Night | 上一夜盘目标806/实际0；今晚尚未开始 | previous query_error 806；今晚21:00归属11/5 | previous隔离；calendar_mismatch=false；无旧夜盘冒充今晚 |
| Commodity Options | 11/4目标64/成功0；last-good 11/2为19/64、430合约 | core_atm 19、skew 12；sampled strikes | full_chain/surface/positioning/execution均false；不编PCR/Gamma方向/权利金 |
| futures_crosscheck | 11/4 | SHFE238、INE63、CZCE243、GFEX48官方记录；比较对0；DCE HTTP412 | `unavailable`，不是价格不一致；不声称成交/OI官方核对 |
| China Stock | requested至11/3；last-valid 10/30；11/4 08:34失败 | 5571旧报价；events216、完整财务bundle仅2；行业/复权/tradability缺 | research可做限定公告补证；execution=false |

**全范围筛查。** 商品原63代码全部进入初筛，公共主力页另出现AD、BZ、LG、OP、PD、PL、PT等动态新品种：黑色I/JM/J/RB/HC/FG/SA/SF/SM；金属CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG及PT/PD；能化SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP及BZ/OP/PL；GFEX LC/SI/PS；农产品A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK；EC。非入榜异常：I偏强但仓单/基差不足；AG/AU强，CU条件多失败；FU/LU/BU/SC与LC弱；MA近月backwardation反对追空；GFEX和EC今晚无夜盘；农产品缺当日高质实体与期权执行层。

## 3. 全市场仪表盘

| 资产 | 最新/变化 | 时点与属性 | 研究判断 |
|---|---|---|---|
| UST 2Y/10Y/30Y | 4.57% / 4.92% / 5.29%；约-4/-3/-3bp（盘前指示） | 2026-11-04欧洲早盘；11/3官方收盘4.61/4.95/5.32；盘前二级报价/官方前收 | 两院转蓝后的财政网格锁定先利多久期；存量赤字与供给仍是反证 |
| 10Y real / 2s30s | 2.62% last-good / 72bp；— | 实际利率11/2；曲线按盘前2Y与30Y；异时点，不可直接分解breakeven | 实际利率未同窗，黄金利率归因降级 |
| DXY / EURUSD / USDJPY / USDCNH | 101.34 / 1.133 / 158.12 / 6.676；美元广泛走弱 | DXY 04:28UTC；Reuters欧洲早盘；CNH 07:00UTC；盘中/延迟 | 美元走弱支持黄金和非美风险，但CNH未显著单边升值 |
| Nasdaq/QQQ; SOXX/SMH | 25372.01/685.28; 465.00/518.52；+0.83/+0.63%; +2.50/+1.95%（11/3收盘） | 11/3美股收盘；11/4 04:22ET NQ期货+0.16%；前收+盘前方向 | 指数回升但AI监管与资本开支分化加大 |
| WTI / Brent | 约96.37 / 103.17美元/桶；约-0.18% / -0.4% | 11/4欧洲早盘；盘中 | 地缘溢价仍在，EIA前能源链偏弱 |
| Gold spot | 约4035美元/盎司；约+2.44% | 11/4 08:54GMT二级盘中；盘中，非COMEX结算 | 美元与长债利率共同支持，但跳升后赔率变差 |
| VIX / MOVE / HY OAS | 20.83 / 100.0 / 3.43%；VIX -3.83%；HY -1bp | 11/3收盘；EOD last-good | 波动仍高但信用未失控 |
| China cash 50/300/500/1000 | 2808.54/4101.34/6622.03/6511.81；+1.45/+2.31/+4.66/+4.67% | 11/4 15:00 BJT；EOD delayed public quotes | 成长与中小盘强于权重，成交约2.05万亿元 |
| IH/IF/IC/IM 2612 | 2776.0/4071.2/6578.8/6469.2；约+1.83/+2.70/+4.70/+4.78% vs前结 | 11/4 15:00 BJT；二级延迟；成交量/OI未获CFFEX独立回读 | basis约-1.16/-0.73/-0.65/-0.65% |
| HO/IO/MO 2612 | ATM IV 16.62/21.38/37.66%; RR25 -1.32/-1.88/-5.11 vol；+0.41/-0.28/+2.36 vol（截至11/3） | 11/3 EOD，11/4 07:19生成；官方链匹配760/760；不是11/4当日期权 | MO put skew最负；今日大涨后不可沿用为执行报价 |
| China commodities representatives | SC681.6; AG12420; CU106170; EC2425; LC86460；-1.91/+3.39/-0.99/-0.12/-3.91%（按前结重算） | 11/4 15:00-15:20 BJT；精确合约公开横截面；全市场last-good 11/2 | 能源弱、贵金属强、铜与锂弱；21:00只处理有夜盘品种 |
| China-Stock-Engine | last_valid 2026-10-30；— | 11/4 08:34 BJT失败回填；iFinD HTTP401 device limit；5571旧报价索引 | 全市场旧价量不可生成11/4新信号；公告限定检索可研究但不可执行 |


EOD与海外盘中不可直接横比：A股和中国期货为15:00—15:20已完成会话；海外为不同分钟的盘中/盘前价。10Y实际利率、VIX/MOVE/HY OAS是last-good，不把读取时间当观测时间。

## 4. 相较严格前序全球报告的实质变化

1. **晨间中国风格判断失效。** 11月4日CSI1000/500分别约+4.67/+4.66%，显著跑赢SSE50 +1.45%；晨报 `CN-RV-IH-LONG-IM-SHORT-20261104` 未满足原入场且核心假设被当日价格否定。新反向只能作为child idea，不能重置ID或回填损益。
2. **A股大涨是多因子共振，不是“选举单因子”。** 美国民主党两院胜利压缩新增关税/财政扩张立法尾部；中国1000亿元互换便利、1%回购增持再贷款、超2000亿元申请、主动ETF预期、一个月科技超跌和AMD强财报共同作用。成交、宽度和半导体涨停潮证明风险偏好回补，但单日大阳仍不足以证明中期趋势。
3. **美国选举冲击从风险厌恶转为网格锁定交易。** NQ/ES期货由夜间低点转正，10Y约回落至4.92%、美元走弱；反证是民主党控制国会增加AI、数据中心和加密监管不确定性，存量赤字也不会消失。
4. **黄金叙事增强但执行赔率变差。** 金价盘中越过4000、名义长端与美元同向支持；但10Y实际利率未同窗，11/3 GLD持仓下降、CFTC周度头寸陈旧，不能把宏观类比“政策信用期权”误称有限风险合约。
5. **商品方向比执行更清楚。** SC/FU/LU/LC弱、AG/AU强；晨间AG空和CU多均失效。SC/EC虽有条件优势，日线OHLC无法证明“反弹—跌破—回测”的顺序，今晚不可回填成交。

## 5. 全球统一机会Top5

| 排名 / idea_id | 标的、方向、期限 | 研究/证据/执行三轴 | 分项（逻辑/赔率/催化/价曲波/技术） | 总分 | 最强支撑 / 反证 |
|---|---|---|---|---:|---|
| 1 `US-AI-CASHFLOW-LONG-CAPEXBETA-SHORT-20261103` | AI现金流质量多/远端Capex Beta空主题；relative_long_cashflow_quality；2-20D | 相对价值仍有优势 / 公司财报、盘前反应、利率/监管三类；组合权重与成本缺 / 未就绪；等待美股现金盘与同窗报价 | 21/16/18/10/9 | **74** | AMD数据中心收入同比+97%，Q4收入指引约170亿美元 / AMD盘前已跳升，追价赔率下降 |
| 2 `COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103` | SC2612反弹失败空v4；short；1-5D | 有条件优势，不追低 / 价格与海外两层，上限69；曲线仅指示，实体/期权缺 / 21:00后完整顺序触发前不可执行 | 19/17/14/10/9 | **69** | 见详卡 / 数据/触发缺口 |
| 3 `COM-T-EC2612-TREND-CONTANGO-SHORT-20261028` | EC2612反抽失败空；short；3-20D | 近月弱、远月升水仍大，但需现货同窗确认 / 价格/曲线两层，上限69 / EC无夜盘；最早11月5日09:00 | 17/17/13/12/10 | **69** | 见详卡 / 数据/触发缺口 |
| 4 `GLD-POLICY-CREDIT-STABILIZATION-20261103` | 黄金政策信用溢价观察多；watch_long；3-20D | 宏观叙事增强，但日内跳升后不追 / 价格/美元/名义利率支持；实际利率、IV与当日ETF流未同窗 / 期权权利金与Greeks未取得；MGC也需回撤条件 | 19/15/15/10/9 | **68** | 见详卡 / 数据/触发缺口 |
| 5 `CN-RV-IM-LONG-IH-SHORT-20261104` | IM相对IH反转延续观察；long_IM_short_IH；1-5D | 单日反转很强，但追涨风险高 / 价格/宽度两层；当日期权与可确证资金行为缺 / 最早11月5日09:30，等30分钟回撤确认；今天不可交易 | 17/13/13/10/11 | **64** | 见详卡 / 数据/触发缺口 |


分数只是研究优先级，不是胜率。商品SC、EC仅两层有效证据，严格不超过69；中国风格child也仅价格/宽度两层。Top5是展示上限，不是覆盖范围。

## 6. Top3详细交易研究卡

### 卡1｜AI现金流质量多 / 远端Capex Beta空（研究篮子）

- **新增事实→已定价→分歧：** AMD数据中心收入+97%、Q4指引约170亿美元强化需求；AMD盘前约+6.2%已定价一部分。民主党两院胜利压低长端利率，却可能限制数据中心扩建。我们的分歧是：在监管与融资成本同时存在时，经营现金流可覆盖Capex的公司仍应跑赢依赖外部融资的neocloud/data-center Beta。
- **最强竞争解释：** 利率下行可能令所有长久期成长同涨，且AI监管最终弱于预期；这会使高Beta空腿发生挤压。
- **窗口与闸门：** 22:30现金盘。只有开盘30分钟后，质量腿相对高融资Beta跑赢≥1.0个百分点 **AND** 10Y≤4.95% **AND** NQ不破开盘区间低点，才继续询价。组合精确权重、借券、beta、期权IV和成本未核，故不是执行指令。
- **PnL/退出：** 未有同窗权重与报价，不能编净R；相对收益+3/+6个百分点仅作研究检查点，不是TP。若高融资Beta在利率不升时连续跑赢≥2个百分点，逻辑失效。11月20日或下一轮核心财报前重估。
- **预算：** 试仓上限0.50% NAV；AI、QQQ/SOXX、长债和美元共因子合计≤2.5% NAV。当前实际持仓未知。

### 卡2｜SC2612反弹失败空v4

- **工具：** SC2612，1000桶/手、tick 0.1元/桶、实物交割；保证金/限幅须开盘前向交易所/期货商复核。15:20参考681.6；今晚21:00属于11月5日交易日。
- **AND顺序：** 先反弹682—688 → 随后15分钟收盘<680 → 同窗近月升水≤0.80%且Brent≤102.50 → 回测680失败。完成后681/680/679按30/30/40%。直接低开≤670不追；Brent>104.50、曲线>1.50%或EIA后15分钟>688取消。
- **失效/目标：** 计划止损688；TP1 660减50%，TP2 645；11月6日22:45时间退出。止损不限制期货最大亏损。

| 成交 | 风险（含假设成本500元/手） | TP1净利 | 净R |
|---:|---:|---:|---:|
| 681 | 7,500 | 20,500 | 2.73 |
| 680 | 8,500 | 19,500 | 2.29 |
| 679 | 9,500 | 18,500 | 1.95 |

单手1/2个限幅压力约125,082/250,164元；试仓0.50% NAV，能源共因子（SC/FU/LU/BU/中国海油/WTI）≤1.25% NAV。今日OHLC虽触及关键价位，但无法证明顺序，不能认定触发或成交。

### 卡3｜EC2612反抽失败空

- **工具与窗口：** EC2612，50元/点/手、现金交割、无夜盘；参考2425。最早11月5日09:00。
- **AND顺序：** 反弹2435—2470 → 15分钟收盘<2420 → EC2701-EC2612≥180 **AND** 同窗可签W46/W47现货≤3000 → 回测2420失败。2415/2410/2405按30/30/40%。开盘<2360不追；升水<120或现货>3300取消。
- **失效/目标：** 2475止损；TP1 2280减50%，TP2 2150；11月20日收盘时间退出。

| 成交 | 风险（含假设成本250元/手） | TP1净利 | 净R |
|---:|---:|---:|---:|
| 2415 | 3,250 | 6,500 | 2.00 |
| 2410 | 3,500 | 6,250 | 1.79 |
| 2405 | 3,750 | 6,000 | 1.60 |

航运主题上限1.0% NAV。最强反证是旺季现货或绕航冲击；没有可签现货同窗就不执行。

## 7. 黄金特别研究

“政策信用期权”叙事**增强**：民主党两院胜利提高网格锁定概率，10Y约4.92%、DXY约101.34，黄金盘中约4035；央行与全球ETF长期需求仍提供尾部支持。反证同样明确：10Y实际利率只有11月2日2.62%的last-good，不能与今天名义利率直接分解；GLD 11月3日持仓约1037.66吨、日减2.85吨；CFTC截至10月27日managed-money净多约105,562手，既非极端空头也非今日新买盘；可执行IV/skew与权利金未取得。

工具比较：3—6个月call spread最符合有限亏损，但必须取得同一时点双边报价、Delta/Vega、最大净支出和盈亏平衡；MGC提供更干净Delta却不封顶，日内涨逾2%后不追；“黄金多+长债put spread”能防实际利率反转，但会支付两层成本且当前未询价；反向空仅在DXY与实际利率共振上行、金价跌回3970下方后研究。**当前最优是等待回撤而非立即交易。**

## 8. AI、中国50/300/500/1000与公司专项

**AI。** AMD验证芯片/服务器需求，但Alphabet的高Capex与负季度FCF、微软较强FCF说明“AI收入增长”与“股东现金回报”分化。云、芯片、设备、网络/电力、软件要分别核算；没有真实篮子成分、权重和借券就只称主题，不称beta-neutral。今晚QCOM/ARM等财报是下一个现金流—Capex审计点。

**中国指数与期指。** 50/300/500/1000收2808.54/4101.34/6622.03/6511.81，涨1.45/2.31/4.66/4.67%。主力2612为2776.0/4071.2/6578.8/6469.2，basis约-1.16/-0.73/-0.65/-0.65%；次合约2611约2794.8/4094.0/6601.4/6505.4（IH/IC次合约时点略早）。成交量约51,793/117,612/178,923/320,249，OI约70,869/190,412/196,253/320,908；相对11月3日官方OI的跨源推算ΔOI为-6,317/+572/+16,876/+23,158，**不是官方ΔOI，不能据此猜新多新空**。

HO/IO/MO 2612仅有11月3日last-good：ATM IV 16.62/21.38/37.66%，RR25 -1.32/-1.88/-5.11vol，BF25约0.43/0.66/0.75vol；多期限和PCR可研究，但今天大涨后不可沿用。IC没有一一对应指数期权；ETF期权当前快照未取得；全链OI也不推dealer净Gamma。下一股指/股票合法窗口为11月5日09:30，不是今晚21:00。

**公司与主动发现。** Stock引擎11月4日回填因iFinD 401失败，last-valid 10月30；旧价量不能制造今天信号。本期额外检索11月4日半导体设备/CPO公告、长鑫科技回购增额与三家公司IR：长鑫把回购上限从20亿提高至50亿元；中际旭创/光迅科技澄清订单、供应传言。它们解释风险偏好，却不是单股盈利兑现。半导体利润桥应为“订单/售价×交付验收－材料/折旧/R&D－营运资本”，回购属于资本配置而非经营利润。今日多只标的涨停/大涨且停复牌、涨跌停、成本未逐只核，**A股重点执行候选为0**；指数期货或等待回撤优于追单股。

## 9. 下一24小时/7天风险日历与夜盘地图

| 北京时间 | 事件 | 主要风险 |
|---|---|---|
| 11/4 21:00 | 中国商品夜盘（归属11/5） | SC/AG/CU gap；EC与GFEX无夜盘 |
| 11/4 21:15 | ADP就业 | 前端利率、美元 |
| 11/4 21:30 | 美国贸易数据、财政部季度再融资细节 | term premium、美元、长债 |
| 11/4 22:30 | 美股现金盘 | AI监管与现金流分化；先核借券/期权报价 |
| 11/4 23:00/23:30 | ISM Services / EIA | 利率、美元；原油与SC跳变 |
| 11/5 01:15 | Fed Bowman讨论 | 监管/利率标题风险 |
| 11/5 05:00后 | QCOM/ARM/APP等财报 | 芯片、软件、Capex链 |
| 11/5 09:00/09:30 | EC日盘；A股/股指重开 | 验证或回吐11/4脉冲 |
| 11/6 21:30 | 美国10月就业报告 | 7天内核心Delta/Vega与久期冲击 |
| 11/7 04:30 | CFTC COT | 黄金/商品拥挤更新 |
| 11/10 21:30 | 美国10月CPI | 利率、FX、AI、黄金最大共同催化 |
| 11/11 01:00 | USDA WASDE | 谷物/油脂与中国夜盘错时风险 |

今晚三情景：①基准——SC反弹失败、AG高位震荡：只等完整顺序；②风险偏好继续——AG/CU高开、SC修复：不追，15/30/45分钟分别核首根、曲线、回测；③地缘/EIA冲击——油价与IV跳升：取消旧条件、重算滑点和限幅。EC、LC、SI、PS、PT、PD无今晚窗口。期权保护只有拿到当晚双边报价和Greeks后才可称有限风险；否则少仓、延期或不交易。

未来7天另核：11月6日GFEX LC/SI/PS/PT/PD期权最后交易、11月11日CZCE部分期权到期；执行前必须打开交易所文件。风险预算：试仓0.25%—0.75% NAV、确认0.75%—1.5%，同一主题≤2.5%—3%；压力覆盖1/2限幅、追保、流动性消失、相关性断裂、汇率、IV崩/飙、信用与地缘事件。

## 发布前实际校验

已重算五个候选分项与总分、SC/EC好中坏场景、股指basis、2s30s和2IM/3IH名义比；核对DST、21:00交易日归属、EC/GFEX无夜盘、股指下一合法窗口、稳定idea_id与父子关系。MD/JSON方向、分数、行动和风险上限同源。未通过/未解决：11月4日CFFEX官方CSV未能实际打开，期指使用延迟公共快照；商品全市场当次失败；11月4日股指/商品期权执行层缺；Stock引擎陈旧；20:03海外统一实时价不可得。受影响的只是精确执行表达，不把其他资产研究一并取消。CI=`pending_or_unverified`。

## 来源

- [Reuters：美国中期选举结果](https://www.reuters.com/legal/government/democrats-seize-congress-sweeping-midterm-repudiation-trump-2026-11-04/)；[全球市场盘中](https://www.reuters.com/world/china/global-markets-wrapup-1-2026-11-04/)；[美股盘前](https://www.reuters.com/business/us-stock-index-futures-steady-democrats-seize-congress-2026-11-04/)，均为2026-11-04。
- [中国人民银行政策转载](https://jrj.wuhan.gov.cn/ynzx_57/xwzx/202611/t20261104_2873750.shtml)，2026-11-04；[证监会答记者问](https://www.csrc.gov.cn/csrc/c100028/c7668092/content.shtml)，2026-11-02。
- [A股收盘与宽度](https://news.10jqka.com.cn/20261104/c681452355.shtml)；[准确期货合约延迟行情](https://www.9qihuo.com/hangqing)，2026-11-04。
- [AMD Q3 2026原始IR](https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results)，2026-11-03。
- [BLS 11月日历](https://www.bls.gov/schedule/2026/11_sched_list.htm)；[CFTC发布日历](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)；[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)。
- [China Options radar](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)；[China Commodities status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)；[商品crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)；[China Stock status](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/last_run_status.json)。

## 10. 四行行动清单

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：21:00后的SC2612反弹失败空；11月5日09:00后的EC2612反抽失败空；美股现金盘后AI现金流质量相对主题仅待询价。
C. 今天继续观察：黄金回撤、AG2612回撤、IM相对IH是否次日确认，以及QCOM/ARM财报与今晚ISM/EIA。
D. 今天必须回避或若此前已建仓则有条件退出：回避追涨A股半导体、黄金与白银；若此前自行建立AG空、CU多或IH多/IM空，按原失效规则核查并条件化退出，不假定已持仓。
