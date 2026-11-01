# 商品期货期权晨间雷达｜2026-11-02

生成时间：2026-11-02 07:02:39（北京时间）  
信息截点：2026-11-02 07:02（北京时间）；中国期货最新完整日盘为2026-10-30，归属2026-11-02交易日的合法夜盘起于2026-10-30晚、止于2026-10-31凌晨。  
版本：`prompt=radar_2026-10-12_stock_v1`｜`consumer=core_2026-10-17_v1`｜`research_quality=2026-10-21_v1`  
性质：研究与决策支持；不下单，不假定持仓、触发或成交。

## 1. 一句话结论

截至本报告时点，无可立即执行的合格新交易；最值得承担的是AG反抽失败空、SC确认回踩多，均须等09:15价格—曲线—外盘同向。

今天不是“没有研究机会”，而是即时执行条件没有闭环：

- **研究机会存在但等待条件/报价**：AG2612空、SC2612多、BU2701多；准确夜盘与曲线提供了方向线索，但07:02仍无可靠的周一活跃COMEX银与Brent首笔，且中国09:15确认未发生。
- **已研究但优势不足**：MA701油化补涨与AP701动量/曲线多，分数分别66、65；实体证据或赔率不够，暂不进入交易卡。
- **数据不足不能判断**：DCE官方价格交叉核对及合约元数据仍因HTTP 412未完成；所有期权`execution_ready=false`，不能判断具体权利金是否便宜或可成交。
- **最有价值的下一观察**：①07:00后活跃Jan Brent与Dec COMEX银可靠首笔；②09:15 SC2612/2701、BU2612/2701同月对是否保住正价差；③09:15 AG2612反抽是否止于11,950下方且AG2612/2701不转正。下一合法窗口为2026-11-02 09:00中国日盘，执行判断最早09:15。

## 2. 数据质量、覆盖与事实台账

### 2.1 模块覆盖

| 模块 | 本次路径/版本 | 目标与实际 | 日期/生成时间 | 状态与局限 |
|---|---|---:|---|---|
| Futures | `China-Commodities-Engine/data/last_run_status.json` @ `0b535a17…` | 5所、806合约、77产品；SHFE238/INE63/DCE214/CZCE243/GFEX48 | source=2026-10-30；generated=2026-11-02 06:01:51 BJT | `full_market_ready=true`、source_date_match=100%、critical=0；4个占位项；vendor全市场就绪不等于五所官方认证 |
| Market State | `data/market_state_latest.json` @ `10468…` | 77产品，20个同合约交易日 | 2026-09-28至10-30 | exact-contract、不拼接；部分near/next因换月或缺月不可比 |
| Physical | `data/physical/latest.json` @ `0a2b…` | target20/configured20，fresh18、unavailable2 | requested=10-30；generated=10-31 06:04 BJT | 18条均为C级context，A/B且可计分=0；周/月延续不当今日催化 |
| External | `data/external/latest.json` @ `321a…` | target22/configured17，fresh17、unavailable5 | 10-30 EOD；generated=10-31 06:04 BJT | 全部context-only；Dubai/Oman、Singapore HSFO/VLSFO、USD/CNH、DXY缺失；另行核验07:00后海外，首笔未确认 |
| Night | `data/night_session/last_run_status.json` @ `519304df…` | request806；night412；outside168；no-trade12；query/unresolved214 | trading_date=11-02；start=10-30；end=10-31；generated=10-31 05:58 | fresh/validated/published=true，coverage_complete=false，coverage=51.12%；日期合法，`calendar_mismatch=false`；Top3用exact-contract fallback |
| Options | `data/options/quality_latest.json` @ `624bf…`; `surface_latest.json` @ `83d4…` | 45/64产品=70.31%，1000样本；45 series，ATM ready44、skew ready24 | trade_date=10-30；generated=10-31 06:04 BJT前 | `core_v1/sampled_strikes`；full_chain=false；surface/positioning/execution=0；bid/ask=0；vendor Greeks有值但未统一单位，不能作仓位输入 |
| Metadata | root contract metadata | 806合约；match67.49%，effective73.45%；乘数/tick/margin/limit覆盖30.15% | generated=11-02 06:01 | partial；DCE HTTP412；GFEX源交易日回显缺失；Top3参数另用交易所公告核验 |
| Futures crosscheck | `data/crosschecks/futures_latest.json` @ `dc64f8…` | SHFE238、INE63、CZCE243、GFEX48均matched；DCE失败 | generated=11-02 06:03 BJT | SHFE/INE/GFEX/CZCE可比较字段0差异；DCE HTTP412使全局partial；未核成交量/OI |
| Stock | `China-Stock-Engine` 10-30批次；mapping @ `b2c86f…` | universe5577/raw5571；完整/最小财务bundle仅2 | trade_date=10-30；research_asof=10-31 10:40 BJT | 复权、行业、tradability、execution未就绪；只补证中国海油、紫金矿业两家公司，不扩为选股 |

Night价格语义：Top3 exact-contract fallback为交易所托管延迟行情页的会话末“Last”，不是交易所结算价；`night_session_fallback=true`、`official_night_close_verified=false`。root夜盘的`night_close`若为供应商快照别名，不称官方最终收盘；OHLC/量仓不用于叙述精确盘中路径。

### 2.2 全范围初筛与板块结论

引擎实际取得77个产品，覆盖用户列明的黑色、金属、能源化工、新能源、农产品、航运及动态新增；后台对方向、1/5/20日、量仓、near-next、实体、外盘和期权局部能力逐项扫描。展示上限不缩小扫描范围。

| 板块 | 应覆盖/实际分析 | 未入榜最重要异常或无异常依据 | 数据不足/不适用 |
|---|---|---|---|
| 黑色 I/JM/J/RB/HC/FG/SA/SF/SM | 9/9 | JM2701 1D -1.39%、曲线+6.81%，但C级现货基差813.25仅context；钢材未见三层同向 | DCE官方交叉核对失败；基差均无A/B级 |
| 金属 CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | AG夜盘大跌、曲线转小幅contango；SN2612 1D -3.37%而ΔOI +11.26%，仅归因线索 | 期权无bid/ask；贵金属周一海外首笔未核 |
| 能化 SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 24/24 | SC/BU/MA/EG/PP价格与曲线最强；BU 5D +13.13%、量仓z显著；不追未确认周一油价 | DCE合同参数/官方价核验不完整；实体A/B级为0 |
| 新能源 LC/SI/PS及GFEX新增 | 引擎现有全取 | LC2701 1D -1.19%、5D -3.99%，C级现货仅背景 | GFEX元数据日期回显缺失；不据93000现货构造套利 |
| 农产品 A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 19/19 | AP701 1D +2.79%、ΔOI +9.68%、curve +10.82%；OI701 ΔOI +6.85%、curve z +2.62 | DCE官方核对失败；天气/现货缺少新频率证据 |
| 航运 EC | 1/1 | EC2612 5D -11.04%、RV20 50.58、curve -14.22%，但无夜盘且交割/事件噪声高 | 只观察，缺实体运价同口径与可执行参数闭环 |

### 2.3 可追溯事实台账（关键项）

| fact_id | 准确标的/口径 | 观测/known_at/读取 | 来源 | 支持判断与局限 |
|---|---|---|---|---|
| F01 | SC2612 EOD close 742.4、settle 727.6元/桶；夜盘Last 758.5；vs close +2.17%、vs settle +4.25%；OI 27,364→29,929 | EOD 10-30；night 10-31 02:30 BJT；读取11-02 | Engine root + exact-contract exchange-hosted fallback | 支持价格层；Last非官方夜盘结算，close-settle差不算隔夜新增 |
| F02 | SC2612/2701夜盘758.5/750.5，近月升水1.07% | 10-31 02:30 BJT | exact-contract fallback | 支持期限层；同一会话同月对，非第六层 |
| F03 | AG2612 EOD close12,093、settle12,374元/kg；夜盘Last11,532；vs close -4.64%、vs settle -6.81%；OI -1,872 | 10-30/10-31 02:30 BJT | Engine + exact-contract fallback | 支持价格层；不能从价跌OI降断言“多头止损” |
| F04 | AG2612/2701=11,532/11,547，curve -0.13% | 10-31 02:30 BJT | exact-contract fallback | 期限层支持近月偏弱；幅度小，09:15须复核 |
| F05 | BU2701 EOD close5,284、settle5,204元/吨；night Last5,304；BU2612/2701=5,395/5,304，升水1.72% | 10-30 23:00 BJT | Engine + exact-contract fallback | 支持价格/期限层；夜盘ΔOI -5,332仅线索 |
| F06 | OPEC+七国决定12月维持2026年9月所需产量，下一次会议11月29日 | 发布11-01；读取11-02 07:00 | [OPEC官方](https://www.opec.org/pr-detail/620-1-november-2026.html) | 消除“额外增产”尾部风险，但结果符合预期，不能单独抬高多头分数 |
| F07 | 活跃Jan Brent 10-30结算113.43美元/桶；WTI Dec 104.12；截至07:02未核得周一可靠首笔 | 10-30结算；读取11-02 07:02 | [ICE曲线页](https://www.ice.com/products/219/Brent-Crude-Futures/data?marketId=5049381)、公开市场复核 | 海外层仅保留周五背景；117.64为到期Dec Brent，不可冒充活跃月 |
| F08 | COMEX Silver Dec 10-30 close 49.276美元/盎司，日内低48.895 | 10-30；读取11-02 07:02 | [历史合约页](https://www.investing.com/commodities/silver-historical-data) | 支持AG海外映射；周一首笔未核，不能说今晨继续下跌 |
| F09 | Options 45/64，ATM44、skew24；SC ATM IV66.16、AG43.25、BU46.31；均无bid/ask且execution=false | 10-30 EOD；读取11-02 | Engine quality/surface | 可作IV-RV与第五层背景，不能报权利金、Greeks仓位或成交性 |
| F10 | 制造业PMI49.3、生产49.8、新订单49.4、投入价格56.8；建筑业48.0 | 发布10-31；读取11-02 | [国家统计局](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html) | 需求/成本分化，反对无差别追多工业品；已被周末市场知晓 |

## 3. 重点市场仪表盘

| 品种/合约 | EOD close/settle | 1D / 5D | 量仓/RV20 | EOD curve/实体 | 合法Night快照 | 海外/Options | 信号 |
|---|---:|---:|---|---|---|---|---|
| SC2612 | 742.4/727.6 | -1.13% / +1.48% | OI27,364，ΔOI-0.95%，RV39.58 | SC2611/12 +0.22%；无A/B实体 | 758.5，+2.17%/+4.25%，OI+2,565；2612/2701 +1.07% | Jan Brent周五113.43；ATM IV66.16>RV20约26.58点 | 条件多，不追09:00 |
| AG2612 | 12,093/12,374 | -4.21% / -6.65% | OI238,317，ΔOI-8.32%，RV32.06 | 2611/12 -0.50%，z -2.80 | 11,532，-4.64%/-6.81%，OI-1,872；2612/2701 -0.13% | COMEX Dec周五49.276；ATM IV43.25>RV约11.19点 | 反抽失败空 |
| BU2701 | 5,284/5,204 | +1.92% / +13.13% | ΔOI+6.01%，vol z2.82，OI z2.31，RV31.29 | 2611/12 +3.74%，z -2.20 | 5,304，+0.38%/+1.92%，OI-5,332；2612/2701 +1.72% | 油价背景；ATM IV46.31>RV约15.02点 | 强但拥挤，等回踩 |
| MA701 | 3,480/3,463 | +0.93% / +8.32% | ΔOI-4.44%，RV38.15 | 611/612 +1.96%；C级基差+442 | 夜盘准确701未形成可执行闭环 | Options是MA612，不可代替701 | 观察补涨 |
| AP701 | 5,887/5,678 | +2.79% / -0.84% | ΔOI+9.68%，vol z2.73，RV29.15 | 611/612 +10.82% | 无夜盘 | ATM IV32.97；RR25 -3.64、BF +1.17 | 动量观察 |
| EG2701 | 5,392/5,342 | +2.04% / +10.30% | vol z2.95，RV27.94 | 近远月+2.00% | DCE夜盘/官方核对受限 | 无执行期权报价 | 强势但不加榜 |
| PP2701 | 10,433/10,433 | +1.30% / +9.59% | OI638,237 | 近远月+2.79% | DCE质量限制 | 无执行报价 | 油化共振背景 |
| EB2612 | 10,404/10,253 | 0.00% / +1.72% | ΔOI+3,871，vol z2.41，RV32.30 | 近远月+3.85% | DCE质量限制 | 无执行报价 | 曲线强、价格未确认 |
| CU2612 | 108,050/108,190 | -0.77% / +0.82% | ΔOI-2.08%，RV11.11 | curve+0.76%；C级基差+2,165 | 非Top3，未用夜盘正式证据 | LME CU周五14,129.5；ATM IV13.36 | 中性偏弱 |
| SN2612 | 360,880/370,160 | -3.37% / -1.28% | ΔOI+11.26%，vol z2.92，RV28.00 | curve+0.80% | 未升级为正式证据 | LME Tin映射未完整 | 价仓冲突观察 |
| LC2701 | 88,500/90,060 | -1.19% / -3.99% | ΔOI约-4.00%，RV41.36 | curve+0.82%；C级spot93,000 | 无有效夜盘执行结论 | GFEX参数部分缺 | 不能做现货套利 |
| EC2612 | 2,625/2,648 | -0.68% / -11.04% | ΔOI+1.91%，RV50.58 | curve -14.22% | 制度无夜盘 | 无期权 | 高波动观察，日盘-only |

## 4. 相比前序的五项真变化

1. **OPEC事件已落地但不是方向惊喜**：从“周末待结果”变为“12月维持9月所需产量”。SC旧多头不因结果失效，但催化从未知事件变为已知基线，评分73→71；不把“没增产”重复计入实体和海外两层。
2. **官方交叉核对范围改善**：SHFE、INE、GFEX与CZCE可比较字段均0差异；前序缺口已收窄。DCE仍HTTP412，因此BU/AG/SC的vendor价格可用不等于所有DCE数据官方核完，且成交量/OI从未被该crosscheck认证。
3. **活跃海外周一首笔仍缺**：07:02前能核实的是Jan Brent 113.43、COMEX Dec银49.276等周五结算/收盘；因此不把OPEC结果后的海外反应写成事实。SC/BU执行状态仍为等待，AG也须等COMEX新时点。
4. **AG证据仍比油多更干净**：AG的中国夜盘跌幅、近月小幅contango、COMEX Dec周五收49.276三者同向；旧“反抽失败空”保留72分。反证是夜盘已大幅下跌、ATM IV高于RV，追空赔率差。
5. **Stock补证改变表达而非方向**：中国海油Q3/9M证明高实现油价能进入利润，但套保、产量、成本与汇率使其不适合替代今日SC触发；紫金Q3银业务毛利率环比回落但公司多金属利润仍强，不适合作AG空头的直接股票替代。

## 5. 产业链传播与公司利润桥

| 链条 | 最强/最弱与传播 | 曲线/实体/期权 | Stock利润验证与表达比较 | 最大缺失/置信度 |
|---|---|---|---|---|
| 原油→SC/LU/FU→BU | SC夜盘最强；BU日盘及量仓最强；OPEC维持产量减轻供给上修风险 | SC、BU近月升水；无A/B实体；SC/BU ATM IV显著高于RV | 中国海油600938：2026Q3营收1,129.14亿元、归母333.00亿元；9M归母1,191.18亿元、经营现金流1,995.86亿元。9M实现油价86.32美元/桶、净产量593.7百万桶油当量、单位作业费30.57美元/桶油当量。利润桥=售价上升+产量小增−成本/税费−套保与时滞。股票更适合中期现金流/分红，不适合今日SC精确触发；公司已公告商品衍生品套保计划，削弱现货一比一映射。[公司新闻](https://ltd.cnooc.com.cn/xwzx/gsxw/2026/202610/t20261030_123123.html) [三季报](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12684727&stockid=600938) [套保公告](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12684724&stockid=600938) | 周一活跃油价首笔、国内库存/仓单A/B级缺失；中等偏高 |
| 贵金属→COMEX银→AG | AG为最弱；COMEX Dec周五亦弱 | AG近月小幅contango；ATM IV>RV，追空成本高 | 紫金矿业601899：9M营收2,834.53亿元、归母575.26亿元；矿产银销量342,961千克、均价12.81元/克、单位成本2.34元/克、毛利率81.75%；Q3银价10.64、成本2.44、毛利率77.02%，较Q2 81.66%回落。利润桥支持“银价回撤压缩银业务边际”，但金铜锂多元化及强合并利润是竞争解释，故直接AG空优于空股票。[三季报](https://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?id=12658030&stockid=601899) | 周一COMEX首笔与美元/实利率未核；高方向、低执行 |
| 原油→芳烃/烯烃→MA/EG/PP/EB | EG、PP、MA补涨；EB价格确认弱于曲线 | 多品种正价差；MA期权只有612，不能外推701 | 未新增公司：缺少可在截点前核验的经营增量，避免固定名单重复 | DCE官方价/元数据、加工利润、装置负荷缺失；中等 |
| 苹果/油脂→AP/OI | AP量价仓强，OI曲线z异常；均未形成实体层确认 | AP局部ATM/skew可读，execution=false | 无需股票表达，期货更精确 | 天气、库存、现货A/B级和DCE官方核验不足；中低 |

## 6. 统一机会榜

评分分项依次为逻辑/赔率与凸性/催化/价格曲线波动/拥挤技术；总分仅研究优先级，不是胜率。

| 排名 | idea_id / 方向 / 期限 | 分项=总分 | 五层证据（支持/反对/缺失） | 三轴状态 | 工具与限损 |
|---:|---|---:|---|---|---|
| 1 | `COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029` 空，1–5D | 21/18/14/12/7=**72** | 支持：1价格、2曲线、4海外；反对：夜盘已跌深、IV高；缺失：3实体、5方向性期权 | 研究=重点；证据=3层合格；执行=等09:15及COMEX新报价 | 首选期货条件空；看跌价差仅待询价，未证实有限损成本 |
| 2 | `COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030` 多，1–5D | 20/16/14/12/9=**71** | 支持：1价格、2曲线、4周五油价/供应风险；中性：OPEC预期内；反对：弱PMI、IV高；缺失：3实体 | 研究=重点；证据=3层；执行=周一油价+09:15双确认 | 首选期货回踩多；看涨价差待询价，不编净支出 |
| 3 | `COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026` 多，1–10D | 19/15/14/12/9=**69** | 支持：1价格/量仓、2曲线、4油价；反对：5D涨幅与拥挤、夜盘OI回落；缺失：3实体 | 研究=观察上沿；证据=3层；执行=Brent≥115+回踩 | 期货条件多；BU期权只作待询价备选 |
| 4 | `COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024` 多，3–15D | 18/16/12/11/9=**66** | 支持：1价格、2曲线；中性：C级基差；缺失：3/4/5准确同月 | 研究=观察；证据=2层；执行=不就绪 | 不交易优于用MA612期权错配701 |
| 5 | `COM-A-AP701-MOMENTUM-CURVE-PULLBACK-LONG-20261030` 多，3–15D | 18/16/12/10/9=**65** | 支持：1价量仓、2曲线、5局部期权；反对：5D仍负；缺失：3实体、4海外 | 研究=观察；证据=3层但赔率一般；执行=不就绪 | 等回踩与实体确认；期权无bid/ask |

## 7. 三张研究/交易卡

### 7.1 AG2612反抽失败空｜`COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029`

- **事实/定价/推断/主观**：事实是EOD12,093/12,374、夜盘Last11,532、2612/2701=-0.13%、COMEX Dec周五49.276；定价显示中国夜盘已抢跑海外周五弱势；推断是反抽失败仍有去杠杆延续；主观判断是不在11,400以下追空。
- **市场可能错在何处**：若市场把单日跌幅当作充分出清，而近月仍偏弱、反抽不能站回11,950，则剩余多头风险未完全定价。最强竞争解释是夜盘已完成大部分调整，周一海外反弹会造成空头挤压。
- **触发顺序（AND）**：09:00后先反抽至11,780–11,920；再在11,950下方连续15分钟；同时可比时点COMEX Dec≤49.50且AG2612/2701≤0。三者缺一不做。首笔40%，条件持续30分钟再加30%，跌破11,600且曲线仍≤0再加30%。
- **放弃/失效/退出**：开盘直接<11,400且无反抽，放弃；COMEX>51或曲线转正，放弃。计划止损12,150；逻辑失效为15分钟站上12,150且COMEX/曲线同向修复。TP1 11,300减50%，TP2 10,700减余仓；最迟11月4日14:45退出。
- **好/中/坏成交（未含未知费用与滑点，不把未知当0）**：11,920/11,850/11,780；每手计划风险3,450/4,500/5,550元；TP1毛R 2.70/1.83/1.30，TP2毛R 5.30/3.83/2.92。费用与跳空会降低净R。
- **参数/压力**：15千克/手，1元/千克tick=15元/手；夜盘21:00–02:30；AG2612最后交易日2026-12-15。已核限制口径为20%涨跌停、一般保证金22%；一/两板压力约36,279/72,558元/手（以EOD close估算，实际规则与扩大板需再核）。计划止损不封顶，09:00跳空、流动性消失、保证金上调均可超损。
- **期权替代**：AG2612、到期11月24、ATM12,400、IV43.25；skew不ready、bid/ask=0、execution=false。只可询价1×1看跌价差；最高净支出须≤该主题NAV预算且以询得可成交价重算，不能称当前“便宜”或已有限损。

### 7.2 SC2612确认回踩多｜`COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030`

- **事实/定价/推断/主观**：EOD742.4/727.6，night Last758.5，OI+2,565，SC2612/2701+1.07%；OPEC维持12月产量要求。市场已计入部分供应风险；预期内OPEC不构成新alpha。主观上只买回踩确认，不追758以上第一跳。
- **市场可能错在何处**：若活跃Brent仍≥113.5并在亚洲盘扩张，而SC曲线保持≥1%，中国弱PMI对近端供应风险的折价可能过大。竞争解释是油价周五涨幅已透支，OPEC结果无惊喜，周一海外低开会使夜盘高点成为陷阱。
- **触发顺序（AND）**：09:15前后SC≥758连续15分钟；同可比时点SC2612/2701≥1.0%；活跃Jan Brent可靠报价≥113.5；随后回踩750–756且746不破。回踩后30%/再站758 30%/突破765且曲线不弱化40%。
- **放弃/失效/退出**：开盘>770不追；曲线<0.5%、Brent<111或回踩破746则放弃。计划止损742；逻辑失效为SC与Brent、曲线同步转弱。TP1 780减50%，TP2 805减余仓；最迟11月4日22:45退出。
- **好/中/坏成交**：750/753/756；每手计划风险8,000/11,000/14,000元；TP1毛R 3.75/2.45/1.71，TP2毛R 6.88/4.73/3.50；未知费用/滑点另扣。
- **参数/压力**：1,000桶/手，0.1元/桶tick=100元/手；夜盘21:00–02:30；最后交易日11月30日、交割期至12月7日。11月3日结算起限幅18%、一般保证金20%，此前核验口径16%/18%；一/两板压力至少约118,784/237,568元/手（按742.4和16%线性情景，规则调整/连续板非线性，非保证最大亏损）。[INE参数公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833903.html)
- **期权替代**：SC2612、到期11月12、ATM730、IV66.16；距到期短、skew不ready、无bid/ask。仅作事件看涨价差待询价；若净支出超过该主题NAV0.75%或盈亏平衡要求SC在时间退出前超过TP2，放弃。

### 7.3 BU2701强曲线回踩多｜`COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026`

- **事实/定价/推断/主观**：EOD5,284/5,204，1D+1.92%、5D+13.13%，ΔOI+6.01%、volume z2.82；night Last5,304，BU2612/2701+1.72%，但夜盘OI较EOD少5,332。推断是近端供给溢价仍在，主观上不追强势。
- **错价与竞争解释**：若Brent≥115、近月升水≥1.5%且回踩守住，BU或仍未充分计入原油成本；反面是5D涨幅、量仓z已拥挤，且周一活跃Brent首笔尚未核。
- **触发顺序（AND）**：09:15 BU≥5,300连续15分钟；BU2612/2701≥1.5%；活跃Jan Brent≥115；随后回踩5,235–5,265守5,200。首笔40%、重返5,300加30%、曲线≥2%再加30%。
- **放弃/失效/退出**：开盘>5,380不追；Brent<111、curve<0.5%或回踩破5,200放弃。计划止损5,170；TP1 5,380减50%，TP2 5,520；最迟11月4日14:45退出。
- **好/中/坏成交**：5,235/5,250/5,265；每手计划风险650/800/950元；TP1毛R 2.23/1.63/1.21，TP2毛R 4.38/3.38/2.68；费用/滑点未知另扣。
- **参数/压力**：10吨/手，1元/吨tick=10元/手；夜盘21:00–23:00；BU2701最后交易日2027-01-15。11月3日结算起限幅14%、一般保证金16%；此前12%/14%。按5,284、旧12%估算一/两板压力6,341/12,682元/手，相关性断裂、跳空和规则再扩大可超出。[SHFE参数公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833901.html)
- **期权替代**：BU2701到期12月25、ATM5,200、IV46.31；无bid/ask、skew/positioning/execution不ready，只能列看涨价差询价备选，不替期货计划封顶。

## 8. 商品期权专项

- **样本口径**：10月30日EOD、`core_v1/sampled_strikes`，45/64产品、1000合约样本；ATM44、25Δ skew24，完整曲面/持仓/执行均0。`quote_coverage_complete`只代表计划采样腿，不是全链。
- **IV-RV**：SC 66.16% vs RV20 39.58%（+26.58点），AG 43.25% vs 32.06%（+11.19），BU 46.31% vs31.29%（+15.02），AP32.97% vs29.15%（+3.82），OI15.74% vs12.06%（+3.68）。这是不同窗口/口径的研究差，不等于期权昂贵或便宜，未扣跳跃与事件风险。
- **偏度**：AP701 RR25 -3.64、BF25 +1.17；OI701 RR25 +2.70、BF25 +0.55可作为局部偏度。SC/AG/BU skew均不ready，禁止用“最近点”伪造25Δ。
- **期限/曲面**：单一核心月份不外推term；`surface_ready=false`不否定局部ATM，但禁止研究wing/tail和全曲面相对价值。
- **持仓/执行**：`positioning_ready=false`，不推PCR、拥挤或dealer gamma；`dealer_gamma_direction_known=false`。`execution_ready=false`、bid/ask=0，因此所有结构均待询价，不能列权利金、净成本、滑点、精确Greeks或称即时可执行。
- **回避**：SC短到期高IV追买、AG夜盘大幅移动后用旧Delta追买、用MA612期权表达MA701、用采样OI推全链持仓，全部回避。

## 9. 09:00开盘风险地图

| 层 | 已知事实 | 潜在开盘 | 操作纪律 |
|---|---|---|---|
| Previous China EOD | SC742.4、AG12,093、BU5,284；弱PMI与工业品分化 | 仅为基准，不把close-settle差当隔夜 | 09:00不凭结算偏差追价 |
| Current T Night | 合法归属11月2；SC758.5/曲线+1.07%，AG11,532/曲线-0.13%，BU5,304/曲线+1.72% | SC偏高开、AG偏低开、BU小幅高开概率较高；不是胜率预测 | 09:15核准确合约、同月曲线与量仓；15分钟只做第一确认，30分钟复核曲线，45分钟才允许第二次加仓 |
| 07:00 Overseas | OPEC维持产量；截至07:02活跃Brent、WTI、COMEX银周一首笔未可靠核得 | 方向未知，不能把周五收盘写成今晨反应 | SC/BU必须取得活跃Brent新报价；AG必须取得COMEX Dec新报价；缺则执行受限 |

不追价边界：SC首开>770、BU>5,380、AG<11,400且无反抽，均放弃；因报告生成早于09:00，15/30/45分钟均为未来合法检查窗口。

## 10. 未来24小时与7日事件

| 北京时间 | 事件 | 主要暴露 | Delta/Vega与处理 |
|---|---|---|---|
| 11月2日07:00后 | ICE/CME/COMEX周一首笔与OPEC后首轮定价 | SC/BU/AG | 未核报价前不开放触发；SC短到期期权Vega风险高 |
| 11月2日09:00–09:45 | 中国日盘开盘与三段确认 | Top3 | 先价格、再同月曲线、再海外；不凭OHLC猜顺序 |
| 11月3日结算起 | SC2612/2701及LU限幅/保证金上调；BU2611/12/2701及FU上调 | SC/BU/FU/LU | 线性仓保证金需求与gap风险上升；见[INE](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833903.html)、[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202610/t20261030_833901.html) |
| 11月4日23:30 | EIA Weekly Petroleum Status Report（周三10:30 ET） | 原油/成品油 | 数据前降Delta；无执行报价不提前买Vega。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 11月7日04:30 | CFTC COT（11月6日15:30 ET） | 贵金属、农产品、能源拥挤 | 只作次周持仓验证，不把周二持仓数据当实时。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) |
| 7日内持续 | 中东供给/运输、美国选举后政策信号、中国需求与装置负荷 | 油化、金属、航运 | 地缘gap、相关性断裂、汇率急变压力；无新原始公告不重复计证据 |
| 11月29日（超7日、约20D边界外） | 下一次OPEC+会议 | 原油 | 只记远端催化，不把它当本周Vega理由 |

## 11. 风险预算、旧观点与发布校验

- **预算**：试仓NAV0.25%–0.75%，确认0.75%–1.50%；原油因子（SC、BU、中国海油及相关期权）合并，高确信主题总预算不超过2.5%–3.0%。无NAV只给公式：手数=`floor(单笔NAV风险额/每手计划风险)`，保证金不是风险预算。
- **压力**：一/两涨跌停、09:00/21:00 gap、流动性消失、相关性断裂、保证金提高、IV跃升/塌陷、交割挤压、人民币急变及中国休市海外大波动。期货止损不是合同限损；未询价期权不能给线性仓封顶。
- **旧观点台账**：五个idea_id全部继承，未重置首次提出、触发、失效、TP与时间退出；SC仅因OPEC落地与海外首笔缺失由73调至71，AG维持72，BU 70→69，MA66不变，AP65不变。变更属新证据/执行窗口，不是已成交损益。实际持仓状态=未提供/未知。
- **行动前覆盖**：已分析77产品；Options成功45/64，未取得19产品不等于无机会；DCE官方crosscheck与metadata失败限制对应结论；EC等无夜盘按制度正常；Top3参数以交易所公告核验；Stock只补证两家公司，证券报价、停牌、流动性和交收未核，不称股票即时可执行。
- **发布闸门**：评分已重算且分项和为72/71/69/66/65；Top3好/中/坏R按乘数重算；日历归属通过、`calendar_mismatch=false`；MD/JSON须同源；未解缺口为周一海外首笔、DCE官方核对、期权bid/ask、实体A/B级。CI状态仅`pending_or_unverified`。

### 来源

- [China-Commodities-Engine report input](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)
- [External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)
- [Futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)
- [Stock Engine manifest](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json)
- [Company commodity exposures](https://github.com/farfromexact/China-Stock-Engine/blob/main/config/company_commodity_exposures.json)
- [OPEC官方声明](https://www.opec.org/pr-detail/620-1-november-2026.html)
- [Reuters OPEC报道](https://www.reuters.com/business/energy/opec-set-keep-oil-output-targets-steady-sources-say-2026-11-01/)
- [国家统计局PMI](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html)

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：AG2612反抽失败空、SC2612确认回踩多、BU2701强曲线回踩多；均须09:15价格—同月曲线—海外新报价AND确认。
C. 今天继续观察：MA701、AP701、EG2701、PP2701、EB2612、SN2612、LC2701、EC2612，以及中国海油/紫金矿业利润映射；不默认持仓。
D. 今天必须回避或有条件退出：回避09:00第一跳、缺海外首笔追单、DCE未核合约执行、无bid/ask期权和错月替代；若假设已建仓，按各卡止损、逻辑失效或时间退出处理。
