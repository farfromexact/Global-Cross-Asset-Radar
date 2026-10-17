# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-17｜版本：commodities_evening｜prompt_version：radar_2026-10-12_stock_v1**  
**生成时间：2026-10-17 19:50 北京时间｜研究截点：19:37 北京时间**

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；周末闭市且Night日期异常，油价风险溢价又遭供给政策对冲，只保留周一SC、BR、LH条件验证。**

研究机会与可下单机会分开：境内商品、A股和主要海外商品市场均处周末闭市；无实时有效报价、无已发生触发。已研究但优势不足：追涨油品、贵金属，追空LC/AP/SH。机会存在但等待条件：SC2612、BR2612、LH2701。数据不足不能判断：源Night 414条记录、DCE夜盘、当前商品期权、A级/B级基差、GFEX最新仓单及10月16日A股联动。

## 二、时间、数据质量与全范围覆盖

### 2.1 会话与仓库快照

- 今日为周六。最近完整中国会话是 **2026-10-16 EOD**；今晚没有21:00夜盘。下一实际中国商品窗口为 **2026-10-19 09:00**，下一夜盘为 **2026-10-19 21:00**，归属10月20日交易日。
- 商品仓库固定 ref：[`f299a6dc679255e86680866cddd3d790c2494400`](https://github.com/farfromexact/China-Commodities-Engine/tree/f299a6dc679255e86680866cddd3d790c2494400)。统一输入 `requested_date=2026-10-16`，`generated_at=2026-10-17T19:14:12.667021+08:00`。
- 前序基准：[`2026-10-17 commodities_morning`](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/bebd792a222bac51e7286b8a4ab678f800a7b555/reports/2026/10/2026-10-17_commodities_morning.md)；同版基准：[`2026-10-16 commodities_evening`](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/bebd792a222bac51e7286b8a4ab678f800a7b555/reports/2026/10/2026-10-16_commodities_evening.md)。本次继承idea_id，不把周末重复检查写成新观点。
- Stock仓库固定 ref：[`79c96a9d9e73a7c2a13d340229acc7c64f4ec144`](https://github.com/farfromexact/China-Stock-Engine/tree/79c96a9d9e73a7c2a13d340229acc7c64f4ec144)。10月16日回填失败，last-good交易日为10月15日。

### 2.2 模块质量

| 模块 | 日期/规模 | 状态 | 可用边界 |
|---|---:|---|---|
| Futures | 10/16；806合约、77品种、五所 | `full_market_ready=true`，日期匹配100%，critical=0；但root `official_complete=false`、8条OHLC占位 | 价格与同合约Market State可用；占位剔除 |
| Market State | 9/11—10/16，20个交易日 | 77品种1/3/5/20D、RV20、量仓、曲线 | roll pair与观测不足单列，不拼接主力 |
| Physical | 10/16；18/20 fresh | SC/LU缺失；18个basis全为C、不可评分 | 只作背景，不称套利；孤立现货值不单独算第三层 |
| Warehouse | CZCE 10/16；GFEX 5条为9/1 carried | 5条GFEX stale | LC/SI/PS/PD/PT仓单不作当前证据 |
| External | 10/16；17/22 fresh | WTI/Brent、LME、COMEX、CBOT、ICE、SGX可用；DXY、USD/CNH、实际利率等5项缺映射 | 全部为`context_only`，不可直接称跨市套利 |
| Night | 源写`trading_date=2026-10-17`、start=10/16；414合约 | 周六交易日语义错误；214 query_error/unresolved；`coverage_complete=false`；官方夜收未验证 | 全部隔离，不自行重标、不计证据、不触发；fallback=false |
| Options | 10/16；452合约、21/64品种、21序列 | IV覆盖100%，OI 93.81%，bid/ask 0%；surface/positioning/execution均0 ready | 仅局部研究索引；不能报价、算净支出或判断IV-RV |
| Metadata | 10/16 | SC/BR/AG仅官方partial；DCE为observed-contract-only | 乘数、tick、保证金、限幅、夜盘规则普遍缺失，三张卡均不可执行 |
| Stock | 10/15；全市场PIT索引，2家公司最小财务集 | 10/16 backfill失败；证券实时状态unknown；forecast/TTM未就绪 | 仅利润桥和表达比较，不列今晚股票交易 |

### 2.3 扫描覆盖

- 实际取得并逐项扫描77品种：`AP/CF/CJ/CY/FG/JR/MA/OI/PF/PK/PL/PM/PR/PX/RI/RM/RS/SA/SF/SH/SM/SR/TA/UR/WH/ZC/A/B/BZ/C/CS/EB/EG/I/J/JD/JM/L/LG/LH/M/P/PG/PP/RR/V/Y/LC/PD/PS/PT/SI/BC/EC/LU/NR/SC/AD/AG/AL/AO/AU/BR/BU/CU/FU/HC/NI/OP/PB/RB/RU/SN/SP/SS/WR/ZN`。
- 黑色/建材、金属、能源化工、新能源、农产品、软商品、航运均纳入；PL/BZ/LG/PD/PT/OP等动态代码也保留。
- 数据不足而非“无异常”：DCE夜盘全缺可靠exact-contract确认；43/64期权品种采集失败；SC/LU现货缺；GFEX仓单过期；全市场基差均不具A/B条件。
- 不适用/剔除：JR/PM/RI/WH/ZC等代表合约零价/零量零仓占位，以及全部8条OHLC占位，不进入排行与方向判断。

## 三、周末仪表盘（最近完整会话）

| 板块/合约 | 10/16 close / settle | 1D close；5D settle | Vol / OI / ΔOI | 曲线（近-次，%） | Physical/海外/Options | 周一信号 |
|---|---:|---:|---:|---:|---|---|
| 原油 SC2612 | 711.8 / 723.0 | -1.85%；+0.64% | 119,673 / 32,965 / +3,173 | +0.84 | SC现货缺；Brent结109.86、WTI 101.41；SC期权失败 | 09:30后仅看重返730且不追>750 |
| 橡胶 BR2612 | 15,915 / 15,975 | +1.79%；-2.41% | 105,309 / 75,757 / +9,537 | +1.10 | 无A/B基差；BR期权失败 | 精确合约守15,900且曲线≥0.8% |
| 燃料油 FU2701 | 4,819 / 4,770 | -0.35%；+7.43% | 327,042 / 211,067 / +8,765 | +7.92 | 现货仅C级；全球HSFO紧但追价拥挤 | 不追；观察裂解/曲线回落 |
| 白银 AG2612 | 14,029 / 13,889 | +2.49%；-4.31% | 323,505 / 282,779 / -10,546 | -0.10，pair roll | COMEX银57.13；AG期权失败 | 价格涨、OI降，反弹确认不足 |
| 黄金 AU2612 | 901.82 / 898.80 | +1.36%；-0.03% | 194,252 / 222,956 / -620 | -0.13，pair roll | COMEX金4,186.5；AU期权失败 | 油价通胀与高利率冲突，拒绝追 |
| 铜 CU2611 | 109,860 / 109,450 | +0.10%；-0.15% | 107,082 / 176,863 / -12,136 | +0.63，pair roll | LME铜14,359；现货C级 | LME Week与中国数据前等确认 |
| 豆粕 M2701 | 3,281 / 3,299 | -1.77%；-2.66% | 1,234,349 / 2,321,910 / -61,019 | -1.69，z=-2.73 | CBOT豆粕344.6；现货C；M期权失败 | 中国采购利多与内盘弱势冲突 |
| 生猪 LH2701 | 10,490 / 10,475 | +0.24%；-6.89% | 174,035 / 182,448 / +8,124 | -3.72 | 无可靠DCE夜盘/期权/参数 | 仅跌破10,450后验证空头延续 |
| 碳酸锂 LC2701 | 96,320 / 99,080 | -4.20%；-16.56% | 358,976 / 425,349 / +6,802 | +0.92 | 现货101,000但basis C；仓单stale；期权失败 | 只观察，不接飞刀也不追空 |
| 苹果 AP701 | 5,998 / 6,096 | -3.32%；-11.68% | 246,249 / 169,454 / +8,417 | +15.11，z=1.69 | 期权局部有IV、无bid/ask | 极端趋势但赔率恶化，回避追空 |
| 烧碱 SH701 | 1,726 / 1,735 | -1.82%；-6.06% | 207,684 / 207,093 / +41,022 | +0.29 | CZCE仓单10/16；期权未执行就绪 | 价跌OI增只作线索，不定性资金身份 |
| 航运 EC2611 | 2,774.5 / 2,754 | +0.67%；+0.18% | 8,172 / 19,690 / -1,182 | -19.66 | 周末地缘/航运新闻；无期权执行 | 新闻弹性高但期限与运价错配，观察 |

源Night原始快照显示SC2612 739.8、AG2612 13,835、SA701 956等，但源把周六10月17日标为交易日，且`official_night_close_verified=false`。这些数只用于定位周一需核的价格区，不写成“今晚已上涨/下跌”，不进入上表收益或证据层。

## 四、相比今晨的真变化与旧观点处置

1. **无新市场会话**：10/16 EOD与海外周五收盘未变，所有价格候选维持等待状态；没有用重复快照制造“新催化”。
2. **输入重编译但质量更分化**：19:14统一输入仍有806合约/77品种，核心日期匹配100%；root因contract metadata、仓单carry、basis缺失而`official_complete=false`。结论是研究可继续，执行不能放行。
3. **期权变“更新但更窄”**：从今晨沿用的10/14全局快照切换为10/16 core sample；成功21/64品种、452合约，三类ready仍全为0。所有重点SC/BR/AG/AU/CU/LH/M/LC均失败，不能把日期更新误写成第五层确认。
4. **能源周末新增反证**：美国豁免部分俄油相关制裁与关税，Gulf of Oman至中国VLCC运价从Worldscale 841降至约776；这是供给/物流缓和线索。与Hormuz和Yanbu风险并存，SC由“潜在补涨”维持条件多头但不加分，BR不追。
5. **Stock没有新价格或财务事实**：10/16回填因连接超时失败，紫金、宝钢只保留10/15 tape与2026H1披露。紫金矿产金/铜是条件暴露，但当前股票并不比直接商品更纯；宝钢加工利润需钢材—矿石—煤炭价差与库存结转共同验证，均不进入Top榜。

## 五、产业链地图与公司利润桥

### 5.1 原油—燃料油—运输

- 上游：Brent/WTI周五分别结算109.86/101.41美元/桶，地缘供给风险高；SC2612却以711.8收盘、低于723结算，境内日盘尚未吸收周五后段海外涨幅。
- 中游：FU2701五日+7.43%、曲线+7.92%，全球HSFO供应偏紧；但绝对涨幅、OI高位和周末政策缓和使追多赔率差。
- 运输：VLCC运价仍高但边际回落；周末没有可成交报价。最强是外盘油，最弱是10/16日盘SC；最大缺口是合法夜盘与SC实体数据。置信度中。

### 5.2 贵金属—矿企

- AG/AU日盘反弹，AG价格升而OI降，不能直接认定新增多头；COMEX周五收盘提供外部支撑但无周末实时价。
- 紫金矿业2026H1合并口径YTD收入1,941.78亿元、归母净利391.70亿元、经营现金流554.72亿元；矿产金/铜售价传导受产量、成本、套保、汇率和少数股东影响。该旧披露只验证利润桥，不是10月17日催化。
- 股票表达劣于直接商品：A股已休市、10/16 tape缺失、证券状态unknown、PB约3.79但PE/TTM/共识缺失；不以商品上涨推导股票交易。置信度低至中。

### 5.3 黑色—钢材—宝钢

- I2701 5日-1.39%，JM2701 -2.11%，RB2701 -0.26%；矿石、焦煤弱于成材的方向略有利于钢厂加工差，但RB量能偏低、曲线pair roll，尚无可执行中性比例。
- 宝钢2026H1 YTD收入1,607.31亿元、归母净利45.71亿元、经营现金流148.15亿元；收入同比+6.18%、归母净利同比-6.30%，支持“收入增长未完全转化为利润”。但期货品种与实际产品结构、采购库存、能耗和出口均有错配。
- 最佳表达仍是先观察经验证的钢材/原料价差；股票10/16数据缺、估值和证券状态不完备，不交易。置信度中低。

### 5.4 油籽—饲料—生猪

- M2701跌1.77%、曲线-1.69且OI大减；CBOT豆粕344.6，且中国买入更多美豆的消息增加远期到港预期。内盘弱势与进口节奏同向，但尚缺压榨利润、港口库存和DCE夜盘确认。
- LH2701五日-6.89%、曲线-3.72%，10/16小幅反弹伴OI增加；只说明博弈加剧，不能断言新多或新空。
- 最大缺口是DCE 214个unresolved、M/LH期权和产业量化序列，置信度中低。

## 六、统一机会榜（研究优先，不等于交易指令）

| 排名 | idea_id / 方向 / 期限 | 评分（逻辑/赔率/催化/价曲波/拥挤） | 有效支持层 | 三轴状态 | 主要反证/缺口 |
|---:|---|---:|---|---|---|
| 1 | `COM-M-SC2612-EIA-SETTLE-RECLAIM-LONG-20261016` 条件多，1—3D | **67**（19/15/15/9/9） | 2曲线、4海外 | 待验证优势 / 部分 / 周一等触发参数 | 日盘弱、实体缺、Night隔离、俄油政策缓和 |
| 2 | `COM-E-BR2612-CURVE-MOMENTUM-LONG-20261016` 条件多，1—5D | **63**（18/14/9/12/10） | 1价量、2曲线 | 待验证优势 / 部分 / 待精确报价 | 夜盘代表为BR2611而非2612；参数/期权缺 |
| 3 | `COM-E-LH2701-WEAK-CURVE-SHORT-20261013` 条件空，3—15D | **61**（17/14/8/11/11） | 1趋势、2曲线 | 待验证优势 / 部分 / 周一日盘确认 | 10/16反弹；DCE夜盘、实体、期权、参数缺 |
| 4 | `COM-M-AG2612-RATE-RELIEF-REBOUND-LONG-20261016` 观察，1—5D | **55**（16/13/10/8/8） | 4海外 | 优势不足 / 不足 / 不执行 | 日盘价涨OI降；Night隔离；无曲线/期权确认 |

分项上限复核：逻辑≤25、赔率≤25、催化≤20、价曲波≤15、拥挤≤15；各行合计分别67/63/61/55。四项均只有1—2个有效独立支持层，分数严格不超过69；没有把Night、同一曲线或股票同因子反应重复计层。

## 七、研究/交易卡（均未达到执行就绪）

### 卡1｜SC2612 周一gap吸收条件多

- **事实**：10/16 close/settle=711.8/723；1D close -1.85%，5D settle +0.64%；Vol 119,673、OI 32,965、ΔOI +3,173；近次曲线+0.84%。Brent/WTI周五结109.86/101.41。源Night 739.8因交易日语义错误、官方夜收未验证而隔离。
- **定价/推断**：周一可能高开，但海外油价风险溢价已很大；俄油制裁豁免、SPR/IEA供应与运价边际回落是最强竞争解释。市场可能不是漏定价，而是在折价地缘回落和内盘流动性风险。
- **最佳表达**：仅SC2612期货研究单，不用股票或期权替代。SC期权采集失败；股票没有更纯、更及时的利润暴露。
- **触发与分批**：09:00首跳不追；09:15观察成交/曲线，09:30仅在精确报价重返并守住730、曲线≥0.8%、Brent未跌破106时试仓；09:45二次确认才加。若开盘/复核价>750，放弃追价。
- **风险/退出**：计划止损718（不保证最大损失）；逻辑失效为30分钟收于723下方或Brent<106。TP1 760、TP2 780；10/19 14:30前无延续则时间退出。好/中/坏入场假设为730—735/735—745/>750放弃；无可靠滑点和乘数，不给净R。
- **参数/压力**：last trading day 2026-11-30、last delivery 2026-12-07；乘数、tick、tick value、保证金、限幅、夜盘字段未确认。若1或2个涨跌停、保证金上调、流动性消失，实际亏损可远超计划止损；参数未补齐前不可执行。

### 卡2｜BR2612 曲线—动量条件多

- **事实**：10/16 close/settle=15,915/15,975；1D close +1.79%，5D settle -2.41%；ΔOI +9,537（+14.40%）；近次曲线+1.10%。源Night代表是BR2611而非BR2612，不能替代。
- **定价/推断**：价格、OI与backwardation共同给出两层支持，但可能只是短期供应/交割摩擦；没有实体库存或外盘exact-contract闭环。
- **表达与触发**：只研究BR2612期货。10/19 09:30后精确合约守15,900且近次曲线≥0.8%才试仓；15/30/45分钟依次看价、量、曲线。不追>16,080。
- **退出**：计划止损15,680，曲线<0.5%或30分钟收盘<15,680逻辑失效；TP1 16,350、TP2 16,800；3个交易日不达TP1退出。止损不是合同限损。
- **参数/压力**：last trading day 2026-12-15、last delivery 2026-12-17；乘数/tick/保证金/限幅/夜盘未确认。1—2限幅、胶种基差错配与流动性消失可造成gap损失；参数未补齐前不可执行。

### 卡3｜LH2701 弱曲线条件空

- **事实**：10/16 close/settle=10,490/10,475；5D -6.89%，ΔOI +8,124，曲线-3.72%；10/16价格小幅回升。DCE夜盘、期权、参数均不可用。
- **定价/推断**：趋势与曲线给空头两层支持，但当日反弹和OI上升也可解释为分歧扩大，不能判定资金身份；实体供需未闭环。
- **表达与触发**：仅日盘LH2701期货研究，10/19 09:30后跌破10,450且30分钟无法收复才试仓；低于10,350不追。DCE LH期权失败，不能用未报价put冒充限损。
- **退出**：计划止损10,630；收盘>10,700且contango收窄失效；TP1 10,150、TP2 9,800；5个交易日无TP1退出。
- **参数/压力**：metadata仅`observed_contract_only`，乘数、tick、保证金、限幅、last day、交割均未知。猪价政策/疾病/现货跳变、1—2限幅及流动性消失会使止损失效；参数未确认前不可执行。

共同风险预算：若未来满足全部触发且参数/报价补齐，试仓计划风险0.25%—0.75% NAV，确认后0.75%—1.50%；能源同因子合并，单一高确信主题总风险预算≤2.5%—3.0%。这些是计划预算，不是最大亏损保证。

## 八、商品期权专项

- 样本为10/16 EOD `core_v1 / sampled_strikes`：452合约、21序列、21/64品种。成功范围仅CZCE 20品种及INE NR；重点SC/BR/AG/AU/CU/LH/M/LC全部失败。
- IV覆盖100%、vendor Greeks覆盖100%但单位仅按原样报告；model Greeks 0%、bid/ask 0%、OI 93.81%。`surface_ready=0`、`positioning_ready=0`、`execution_ready=0`，dealer gamma方向未知。
- 因无就绪surface，不给ATM IV、RR25/BF25、term或IV-RV结论；不能把“有IV字段”写成便宜波动。没有当前成交报价，禁止编权利金、净支出、滑点、Delta/Vega或最大损失。
- 事件凸性只保留结构研究：能源可考虑未来有限支出看涨价差，贵金属可考虑有限支出方向价差；在bid/ask、到期、行权交割和完整Greeks验证前一律不执行。周末Vega暴露不能用陈旧截面定价。

## 九、下一个开盘风险地图

| 层次 | 已知事实 | 风险含义 | 行动 |
|---|---|---|---|
| Previous China EOD | 10/16 SC弱、BR强、AG/AU反弹；LC/AP/SH弱 | 国内分化大，不能用单一风险因子解释 | 只保留精确合约条件 |
| Completed Friday Night | 源记录414合约但交易日写成周六、214 unresolved、官方夜收未验证 | 无合法可比Night→Day分解 | 全部隔离，不称“已预交易” |
| Weekend external/news | 周五油价高收；周六俄油制裁豁免、VLCC运价回落，地缘风险未解 | 能源高开概率与回落尾部并存 | 不用新闻追首跳 |
| Next actual session | 10/19 09:00日盘；10:00中国宏观；21:00才有下一夜盘 | 9:00价格可能在10:00数据前二次重定价 | 09:15/09:30/09:45确认；10:00前不满仓 |

潜在高开：SC/FU/BR受油价映射，但政策供给缓和可能削弱幅度；潜在低开/冲突：AG/AU受高油价通胀与高利率预期夹击；M/LH缺合法夜盘。所有首跳均不追，必须同时看精确价、成交、OI、近次曲线和外盘同步性。

## 十、未来24小时/7日事件与行动前复核

- **未来24小时**：周末没有中国商品合法会话；只监测Hormuz/Yanbu、俄油制裁、SPR/IEA释放和航运安全的官方/可靠新闻。新闻只能改变周一情景，不构成今晚报价。
- **10月19日10:00北京**：国家统计局发布三季度国民经济、工业、能源、投资、地产和零售数据；黑色、有色、能源化工的Delta在9:00—10:00之间不宜放大。
- **10月19—20日**：LME Week；19日金属研讨会、20日晚宴。铜铝锌镍以LME曲线和库存事实验证，不用演讲标题下单。
- **10月21日22:30北京（标准时点）**：EIA周度石油报告；能源仓位若届时存在，事件前降线性Delta或使用已核价的有限支出结构。官方排期标准为周三10:30 ET。
- **10月23日/24日**：CFTC下一次COT于美东周五15:30发布（北京时间次日凌晨），反映10月20日头寸；只是滞后拥挤度，不作即时因果。
- USDA 10月WASDE已于10月9日发布，下一次为11月10日，不在7日窗；本窗内未确认新的OPEC+/IEA月报时点。天气、矿山、油田、炼厂、化工装置、农业与公司披露若无原始公告，不预先计催化。

行动前必须复核：SC/BR/LH精确实时报价、参数与限幅；10月19真实交易日；Night日期语义；近次同pair曲线；期权bid/ask与三类ready；SC/LU实体、DCE夜盘、A/B基差、GFEX新仓单；Stock 10月16 tape与证券状态。输入版本为商品`f299a6d`、Stock`79c96a9`、前序归档`bebd792`。

## 十一、来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/f299a6dc679255e86680866cddd3d790c2494400/data/report_input_latest.json)：10/16 EOD、Market State、Physical、External、Night、Options与Metadata。
- [Night运行状态](https://github.com/farfromexact/China-Commodities-Engine/blob/f299a6dc679255e86680866cddd3d790c2494400/data/night_session/last_run_status.json)：日期、414合约、214 errors/unresolved、coverage incomplete。
- [Options质量](https://github.com/farfromexact/China-Commodities-Engine/blob/f299a6dc679255e86680866cddd3d790c2494400/data/options/quality_latest.json)与[Options Surface](https://github.com/farfromexact/China-Commodities-Engine/blob/f299a6dc679255e86680866cddd3d790c2494400/data/options/surface_latest.json)：10/16局部样本及三类ready。
- [Stock研究索引](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/latest/research_inputs_latest.json)、[紫金证据分片](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/latest/research_9_002.json)、[宝钢证据分片](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/data/latest/research_d_003.json)：10/15 tape、2026H1财务和条件暴露。
- [INE交易规则](https://www.shfe.com.cn/eng/services/Rules/INERules/202606/t20260603_831946.html)与[SHFE连续交易规则](https://www.shfe.com.cn/upload/20140103/1388740411504.pdf)：交易日与夜盘归属语义。
- [Reuters：油价触及110美元](https://www.reuters.com/business/autos-transportation/oil-edges-down-investors-weigh-possible-us-sanctions-shadow-fleet-2026-10-16/)：10/16结算与中东/俄罗斯供给风险。
- [Reuters：美国豁免俄油相关制裁](https://www.reuters.com/world/europe/trump-waives-many-russia-related-sanctions-tariffs-before-they-were-take-effect-2026-10-17/)与[Reuters：VLCC运价回落](https://www.reuters.com/business/energy/supertanker-rates-fall-record-highs-2026-10-16/)：周末能源反证。
- [国家统计局2026发布日历](https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html)、[LME Week](https://www.lme.com/Events/LME-Week)、[EIA WPSR排期](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[CFTC COT排期](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)、[USDA WASDE排期](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)：未来事件窗口。

**归档状态：success（六路径回读通过后确认）；CI：pending_or_unverified。**

A. 今晚没有应立即建立的新仓位。  
B. 今晚仅应挂条件的候选：SC2612、BR2612、LH2701，全部等10月19日合法窗口、实时报价、参数与15/30/45分钟确认。  
C. 今晚继续观察：AG/AU贵金属、M油籽、LC/AP/SH弱势、CU/LME Week与紫金/宝钢利润桥；不默认持仓。  
D. 今晚必须回避或有条件退出：回避周末追价、异常Night、无bid/ask期权、DCE未知参数、陈旧GFEX仓单和零价占位；若此前已按条件建立，遇原失效位或流动性/保证金恶化则退出。
