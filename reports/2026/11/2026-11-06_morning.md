# 全球跨资产高风险机会雷达｜晨间版

- **报告日期**：2026-11-06（北京时间）
- **实际生成**：2026-11-06T08:08:59+08:00
- **信息截止**：美国现金市场11月5日收盘；中国期货/现货11月5日EOD；商品夜盘为归属11月6日交易日的供应商延迟快照
- **研究边界**：研究与交易决策支持，不自动下单；账户权限、借券、保证金、合约流动性与实时报价须另核。
- **仓库固定ref**：Global `259d8a4...`；Options `25f3336...`；Commodities `8492051...`；Stock `3fd9a7a...`

## 1. 一句话风险状态

混合Risk-off：美股AI去杠杆与VIX飙升，但美债牛陡、美元未急升且信用尚未同步恶化；优先相对价值与顺序触发，不追单边。

## 2. 全球仪表盘

| 资产 | 最新 | 1D/周变化 | 信号 | 时点 | 缺口 |
|---|---:|---:|---|---|---|
| UST 2Y/10Y/30Y | 4.46% / 4.84% / 5.25% | 1D -12/-6/-3bp；周 -10/-10/-6bp | 前端领跌、牛陡峭；2s30s +79bp | 11/5 official close | 亚洲实时缺失 |
| 10Y real / BEI | 2.60% / 2.24% | 1D -4bp / -2bp；周 0bp / -10bp | 实际利率仍高，黄金却走强 | 11/5 official close | BEI为简化同日差 |
| DXY / EURUSD | ~101.5 / 1.1229 | DXY 1D近持平；周约-0.3%~-0.5% | 美元未确认避险急升 | 11/5 late snapshot | 非同步；skew缺 |
| USDJPY / USDCNY | 157.63 / 6.6652 | JPY约+0.46% 1D；CNH变化未同刻核 | 亚洲FX并非单向risk-off | 11/5 snapshot | carry与期权缺 |
| Nasdaq / QQQ | Nasdaq 24,315 / QQQ 647.05 | 1D -5.5% / -6.33%；QQQ周约-7.6% | 宽科技去杠杆 | 11/5 close | 下一现金窗口22:30 BJT |
| SOXX / SMH | 131.90 / 447.73 | 1D -12.75%/-11.46%；周 -16.08%/-14.31% | 半导体Beta显著弱于QQQ | 11/5 close | SOXX拆股已调整；权重不同 |
| WTI / Brent | 90.52 / 98.29 | 1D +2.72%/+3.88% | 冲击后反弹，供需与事件溢价未分离 | 11/5 settlement | curve/crack/OVX/skew缺 |
| Gold / GLD | spot ~4,134.83 / 375.49 | GLD 1D +0.83%；周 +5.54% | 政策信用/避险代理增强但拥挤 | 11/5 | spot/ETF非同步；IV缺 |
| VIX / MOVE / HY OAS | 28.15 / 93.88 / 3.40% | VIX +69.48%；MOVE 11/4 -6.09%；OAS 11/3 | 权益恐慌高，利率波动与信用未同步确认 | 11/3-11/5 | MOVE/OAS陈旧 |
| IH/IF/IC/IM2612 | 2786 / 4097.6 / 6703.6 / 6605 | 1D +0.36/+0.65/+1.90/+2.10% | 小盘相对强；全线贴水 | 11/5 EOD | 09:30后确认 |
| SSE50/CSI300/CSI500/CSI1000 | 2811.16/4113.41/6740.93/6650.14 | 1D +0.09/+0.29/+1.80/+2.12% | 宽度偏小盘 | 11/5 EOD | 实时广度/行业贡献缺 |
| HO/IO/MO2612 | ATM 14.51/18.93/32.11；RR25 -1.01/-1.02/-3.80 | ATM 1D约-0.97/-0.63/-1.57 vol | MO IV与左尾最贵 | 11/5 EOD | dealer gamma sign、实时价差缺 |

### 中国商品紧凑附录

- **Futures**：11月5日五所77品种/806合约，vendor source-date match 100%，`full_market_ready=true`。官方EOD交叉核对SHFE/INE/CZCE/GFEX已比较行均匹配；DCE因HTTP 412未比较，不能写成有差价，也不能声称成交量/OI经官方核验。
- **Market/Physical/External**：Market State可用但basis质量均C；Physical 18/20，GFEX仓单last-good为9月1日；External 17/22，仅作背景。
- **Options Core**：64个预期品种、45个成功（70.31%），44个局部ATM-ready、26个skew-ready；`full_chain_verified=false`、`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`。因此可研究局部IV/RR，不可编全链PCR、dealer gamma、可执行净权利金或限损成本。
- **Night**：原文件`trading_date=2026-11-06`、会话11月5日晚至6日晨，日历归属无异常；420/806合约有观察值（52.1092%）。语义是`vendor_latest_trade_asof_snapshot`，不是官方最终夜盘收盘；OHLCV会话范围未验证。
- **Metadata**：806合约，effective match 73.45%；乘数、tick、保证金和限幅的原生字段约30.15%，未核字段不得用于执行。

### 可追溯事实台账（关键项）

| fact_id | 标的/值 | 口径与观测时点 | 支持判断 | 局限 | 来源 |
|---|---|---|---|---|---|
| F001 | UST 2Y/5Y/10Y/30Y: 4.46% / 4.59% / 4.84% / 5.25% yield | official close; 2026-11-05 ET | 前端领跌、曲线牛陡峭；2s10s/2s30s/5s30s=+38/+79/+66bp | 日终，不是亚洲时段实时 | SRC-TREASURY |
| F002 | UST 10Y real / BEI: 2.60% / 2.24% yield | official close / derived; 2026-11-05 ET | 实际利率仍高但未压制黄金；BEI=4.84%-2.60% | BEI为同日名义减实际的简化口径 | SRC-TREASURY-REAL |
| F003 | QQQ / SOXX / SMH: 647.05 (-6.33%) / 131.90 (-12.75%) / 447.73 (-11.46%) USD close and 1D | cash close; 2026-11-05 16:00 ET | AI/半导体去杠杆远强于宽科技 | SOXX 11/5拆股，周变动用调整后历史 | SRC-US-ETF |
| F004 | VIX / VX Nov / VX Dec: 28.15 / 24.5355 / 22.1918 index / futures settlement | close / official settlement; 2026-11-05 ET | 现货恐慌与期货倒挂并存，近端事件风险高 | 现货与期货结算时点及构成不同 | SRC-CBOE |
| F005 | MOVE / US HY OAS / HYG: 93.88 (11/4) / 3.40% (11/3) / 77.28 (-0.30%,11/5) index / spread / USD | last-good / close; 2026-11-03 to 2026-11-05 | 尚无同步信用断裂证据，权益冲击更像去杠杆与久期重定价 | MOVE与HY OAS陈旧，不能证明11/5信用安然 | SRC-FRED-CREDIT |
| F006 | DXY / EURUSD / USDJPY / USDCNY: ~101.5 / 1.1229 / 157.63 / 6.6652 FX | late-session snapshots; 2026-11-05 | 美元未随风险急升，黄金与美债反应不完全由美元驱动 | 非同步；FX期权skew缺失 | SRC-REUTERS-FX |
| F007 | WTI / Brent: 90.52 / 98.29 USD/bbl | official futures settlement; 2026-11-05 | 前一日大跌后反弹，事件溢价仍高 | 准确期限曲线、裂解和OVX未取得 | SRC-REUTERS-OIL |
| F008 | US commercial crude inventory: 409.760 million bbl; -0.865 million w/w bbl | official weekly; week ended 2026-10-30 | 库存未给出供应过剩确认 | 下一份WPSR延至11/12；不是11/5新催化 | SRC-EIA |
| F009 | GLD / gold spot: 375.49 (+0.83% 1D,+5.54% week) / spot intraday ~4134.83 USD | cash close / intraday; 2026-11-05 | 黄金在高实际利率下仍强，政策信用与避险解释增强 | spot与ETF非同一时点；IV/skew缺失 | SRC-GOLD |
| F010 | WGC Q3 demand: central banks +321t; ETF inflow +211t; holdings 4,256t tonnes | industry quarterly; 2026-Q3 | 黄金需求不只是短期美元交易 | 季度数据，不能解释单日价格 | SRC-WGC |
| F011 | CFTC COMEX gold: managed money net +105,562; noncommercial net +186,451 contracts | official weekly last-good; 2026-10-27 | 多头拥挤是黄金反证 | 11/3持仓将在本报告后发布 | SRC-CFTC |
| F012 | Microsoft / Meta / Alphabet: MSFT OCF $58.0bn capex $45.2bn FCF $18.6bn; META OCF $32.79bn capex $34.91bn FCF -$2.12bn; GOOGL OCF $42.3bn capex $51.4bn FCF -$9.1bn USD quarterly | company reported; latest reported quarter | 现金流定价权与Capex Beta出现可量化分化 | 公司会计口径与季度不同，不能直接估值 | SRC-AI-IR |
| F013 | AMD / Arm / NVIDIA: AMD data-center revenue $8.546bn +97%; Arm revenue $1.443bn +27%; NVIDIA latest revenue $96.221bn +106% USD / y/y | company reported; latest reported quarter | 半导体下跌不能简单归因为基本面坍塌 | 估值、订单质量与最新盘中报价未统一 | SRC-AI-IR |
| F014 | IH/IF/IC/IM2612 vs cash: 2786/4097.6/6703.6/6605; basis -0.895%/-0.384%/-0.554%/-0.679% index points | official settlement basis; 2026-11-05 | 小盘相对强但各合约仍贴水 | 下一交易窗09:30；不代表盘中路径 | SRC-CHINA-OPTIONS |
| F015 | HO/IO/MO2612: ATM 14.51/18.93/32.11 vol; RR25 -1.01/-1.02/-3.80 vol annualized IV points | engine EOD; 2026-11-05 | MO绝对IV与下行偏斜最高 | dealer gamma方向未知；实时bid/ask未核 | SRC-CHINA-OPTIONS |
| F016 | China commodities full scan: 77 products / 806 contracts / five exchanges coverage | engine EOD; 2026-11-05 | 63个旧代码及新增挂牌的可得数据均纳入初筛 | External 17/22、Physical 18/20且basis均C级 | SRC-COMMODITY |
| F017 | Commodity options core_v1: 45/64 products; 44 ATM-ready; 26 skew-ready; full_chain=false; execution_ready=false coverage | sampled strikes; 2026-11-05 | 局部ATM/skew可研究 | 无bid/ask、非全链、positioning与dealer gamma不可推 | SRC-COMMODITY |
| F018 | Commodity night session: 420/806 contracts observed; 52.1092% coverage coverage | vendor latest-trade snapshot; session 2026-11-05/06 for trading date 2026-11-06 | SC/SN/CU等提供亚洲开盘前方向线索 | 非官方最终收盘；OHLCV会话范围未验证；latest文件为空而fallback可读 | SRC-COMMODITY |
| F019 | SC2612 / SN2612: SC close/settle 624.3/638.4, night snapshot639.8; SN 357400/353520, night343040 CNY per unit | EOD + delayed vendor snapshot; 2026-11-05 EOD / 2026-11-06 pre-open | SC旧空失效、SN反弹失败空候选 | 夜盘非官方收盘；SN动态保证金/限幅未核 | SRC-COMMODITY |
| F020 | China-Stock-Engine: last valid trade date 2026-10-30; candidate_union=0; HTTP 401 refresh failure status | repository status; 2026-11-05 run | 不得用旧价量生成11/6新执行信号 | 不等于全市场无公司机会 | SRC-STOCK-ENGINE |
| F021 | A-share bounded disclosure discovery: 002546 State Grid awards CNY55.585m; 600506 coolant framework no minimum; 688368 buyback CNY120m complete; 688167 cancel 349,642 shares proposed company disclosures | official portal discovery; 2026-10-30 to 2026-11-05 | 完成经营/资本配置/风险线索的限定检索，未形成可执行Top5公司股 | 缺11/5价格、复权、停复牌/限价与完整利润桥 | SRC-A-SHARE-DISCLOSURES |

## 3. 较前序真正变化

1. 美股冲击从估值压缩升级为强制去杠杆：QQQ -6.33%、SOXX -12.75%、SMH -11.46%，VIX 28.15；但HYG仅-0.30%，HY OAS/MOVE又非同日，因此不升级为已证实信用衰退。
2. 美债2Y/10Y/30Y单日分别-12/-6/-3bp，2s30s陡峭至+79bp；增长/政策路径重定价比通胀失控更符合当日价格，但就业报告可推翻。
3. AI旧主题从不可执行的公司篮子拆为QQQ/SMH代理；现金流分化支持相对判断，AMD/Arm/NVIDIA强经营事实反对把芯片下跌写成基本面坍塌。
4. SC旧反弹失败空未完成原顺序，延迟夜盘回到639.8且Brent98.29；旧方向明确失效，建立条件多的子idea，不追价。
5. 中国IM相对IH延续至1/3/5日+1.73/+2.93/+2.06%，但20日仍-9.95%；从观察升为等开盘确认，不称已触发。
6. Stock引擎仍停留10/30；限定公告检索获得四条资本配置/合同线索，但缺现价、可交易状态与完整利润桥，A股公司Top5为0。

## 4. 全球统一Top 5

| 排名 | 方向/期限 | 工具 | 逻辑/赔率/催化/价曲波/拥挤 = 总分 | 研究结论 / 证据 / 执行 |
|---:|---|---|---:|---|
| 1. 多QQQ、空SMH的AI现金流/Capex Beta相对价值 | relative long/short; 3-10D | 154 QQQ long / 223 SMH short per ~$100k leg after trigger | 21/17/16/11/10 = **75** | 待验证优势 / 部分 / 等22:30后顺序触发；待借券、费用与账户资格 |
| 2. 黄金政策信用凸性：只等回撤，不追涨 | long bias / optionality research; 5-20D | GLD or 3-6M call spread only after live chain quote | 20/16/16/11/10 = **73** | 有边际优势 / 部分 / 等回撤；期权待报价与参数 |
| 3. 多IM2612、空IH2612的小盘相对价值 | relative long/short; 3-10D | 2×IM2612 long / 3×IH2612 short | 19/16/14/11/11 = **71** | 待验证优势 / 部分 / 等09:30后30-45分钟确认 |
| 4. SC2612夜盘反弹、曲线维持后的条件多 | long; 1-3D | SC2612 futures | 19/16/15/11/8 = **69** | 待验证优势 / 部分 / 等09:15后回撤—再收复顺序触发 |
| 5. SN2612相对LME背离后的反弹失败空 | short; 2-5D | SN2612 futures | 18/15/12/12/9 = **66** | 待验证优势 / 部分 / 等09:15后反弹失败与LME同向确认 |

评分是研究优先级，不是胜率、收益率或仓位。利率、FX、原油和A股公司未单独入榜：利率已发生大幅牛陡但就业前方向赔率不足；FX缺期权与同步报价；油价供需/事件溢价未分离；Stock引擎陈旧且无11月5日可交易闭环。

## 5. Top 3详卡

### 5.1 多QQQ、空SMH的AI现金流/Capex Beta相对价值

- **新增事实→定价→分歧**：QQQ、SOXX、SMH分别跌6.33%、12.75%、11.46%；市场已定价系统性去杠杆与芯片高Beta，但MSFT/META/Alphabet现金流分化和AMD/Arm/NVIDIA仍强的经营证据说明“全部AI基本面坍塌”过度。主要PnL来自QQQ相对SMH修复，不来自猜指数绝对底。
- **竞争解释**：差异可能全是机械卖盘和ETF成份差异；若SMH相对反弹且信用稳定，策略失效。
- **合同/数量**：QQQ / SMH cash ETFs；154×647.05=$99,645.70 long; 223×447.73=$99,843.79 short; net -$198.09。仅Dollar-near-neutral，**不是beta-neutral**。
- **触发**：先观察前30分钟；要求30分钟QQQ/SMH收盘>=1.45 AND VIX不突破11/5高点28.36 AND QQQ守住638.94；随后回踩比率1.44不破，再分批。
- **分批/放弃**：46/67、46/67、62/89三批（30/30/40）；比率跳空>=1.52不追；VIX>32、HYG单日跌幅>1%或无法核借券/实时价差则取消。
- **失效/目标/时间**：30分钟比率<1.40，或QQQ<638.94且广度继续恶化；TP1 ratio 1.52，TP2 ratio 1.58；2026-11-12 US close。
- **计算**：PnL USD = 154×ΔQQQ - 223×ΔSMH。实时佣金、借券费与滑点未取得；好/中/坏净R不可核，机器表示not execution-ready。
- **最坏压力**：二次跳空、SMH借券召回、两腿流动性断裂、相关性反转；止损不保证成交。
- **风险上限**：试仓<=0.50% NAV；确认<=1.00%；AI相对主题<=1.50%。实际持仓：未提供/未知。

### 5.2 多IM2612、空IH2612的小盘相对价值

- **新增事实→定价→分歧**：IM相对IH的1/3/5日收益约+1.73/+2.93/+2.06%，但20日仍-9.95%。市场只定价了短期小盘修复，是否从超跌变风格趋势必须靠开盘广度、同期现货与basis确认。
- **合同/中性**：IM2612 / IH2612；2×6605×200=CNY2,642,000 long；3×2786×300=CNY2,507,400 short；净多CNY134,600。PnL CNY = 400×ΔIM - 900×ΔIH；名义近似中性，不是beta-neutral。
- **顺序触发**：先观察30分钟；要求IM/IH>=2.38 AND 现金CSI1000/SSE50相对收益非负 AND IM基差不差于-1.10%；随后15分钟再创新高。
- **分批**：以2IM/3IH为不可再分的原子组合，三批各1组，实际33%/33%/34%（整数手近似）。
- **放弃/失效**：比率跳空>=2.44不追；IM基差<-1.10%、无法获得同期现货或实时广度则取消；15分钟比率<2.31，或IM基差<-1.40%。
- **目标/时间**：TP1 ratio 2.48，TP2 ratio 2.55；2026-11-13 14:45 BJT。
- **期权对比**：MO ATM与左尾均显著高于HO，有限风险价差值得询价；无实时链时线性组合反而透明，但仍有保证金与跳空风险。
- **成本/压力**：保证金、手续费、滑点与beta未实时取得；不能给净R，not execution-ready；压力包括连续跌停、basis扩大和风格相关性断裂。
- **风险上限**：试仓<=0.35% NAV；确认<=0.75%；中国风格主题<=1.25%。实际持仓：未提供/未知。

### 5.3 SC2612夜盘反弹、曲线维持后的条件多

- **父idea处置**：旧 `COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103` v6没有完成“反弹—跌破—失败回抽”的顺序，延迟夜盘回到639.8；旧空方向失效，不事后移动止损或重置历史。
- **新增事实→定价→分歧**：EOD close/settle为624.3/638.4，延迟夜盘639.8；近月backwardation仍约1.11%，Brent98.29。市场已回补部分地缘溢价；分歧是曲线并未确认近端完全宽松。
- **合同**：INE SC2612，乘数1000、tick0.1、每tick100元；先回撤636-640，15分钟不收于632下 AND SC2612/SC2701 backwardation>=1.00% AND 同时Brent>=98；随后15分钟收复642。
- **分批/放弃**：640/642/644按30/30/40；开盘/跳涨>=650不追；Brent<96.5、曲线<0.80%或无同刻跨境报价取消。
- **止损/目标/时间**：632；TP1 660，TP2 680；2026-11-10 22:45 BJT。
- **成交情景**：好/中/坏入场640/642/644，计500元情景成本后TP1净R 2.29/1.67/1.24，TP2净R 4.65/3.57/2.84；加权入场642.2，风险10,700元/手，TP1/TP2约1.60R/3.50R。
- **压力**：20%保证金不是风险上限；从642单次18%跌停约-115,600元/手，连续两次复合约-210,000元/手（均未含流动性与追加保证金）。夜盘并非官方收盘，无同刻Brent与曲线即放弃。
- **风险上限**：试仓<=0.35% NAV；确认<=0.75%；SC主题<=1.50%。实际持仓：未提供/未知。

## 6. 黄金专题

**结论：增强，但仅等回撤。** “政策信用期权”是经济比喻：黄金可受益于财政/货币可信度下降和避险需求，但不具备期权合同的确定限损。GLD周涨5.54%、WGC的央行与ETF需求强化论证；10Y实际2.60%、美元可能反弹、CFTC拥挤与流动性抛售是强竞争解释。

- 3—6月Call Spread：只有取得同到期链、bid/ask、IV、skew和净成本上限后才可称有限风险；不得沿用旧strike。
- 微型黄金期货：只作方向确认；保证金不是风险边界，跳空/限幅仍可能穿透计划止损。
- 黄金多头+长债Put Spread：可对冲名义利率上冲，但两腿IV和相关性未核。
- 反向/不交易：若GLD跌破11月5日低点且10Y实际上破2.70%、DXY同步上行，则减持/不交易优先；未经持仓回执不写“减仓”。

来源：[U.S. Treasury real yields](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)、[WGC Q3 demand](https://www.gold.org/news-and-events/press-releases/central-bank-buying-and-etf-inflows-support-gold-demand-q3)、[CFTC](https://www.cftc.gov/dea/futures/other_sf.htm)。

## 7. AI专题

本期不是“AI基本面崩塌”，而是**现金流质量分化叠加强制去杠杆**。MSFT OCF58.0bn、capex45.2bn、FCF18.6bn；META OCF32.79bn、capex34.91bn、FCF-2.12bn；Alphabet OCF42.3bn、capex51.4bn、FCF-9.1bn。平台龙头内部已分化，而AMD数据中心收入+97%、Arm总收入+27%、NVIDIA最近季度收入+106%反驳简单的产业需求断裂。

覆盖结论：

- 龙头/云：现金流定价权仍强，但capex兑现速度是估值核心。
- 二线/芯片：经营数据强、股价Beta更高，当前更像估值与流动性压缩。
- 设备/网络：只有SOXX/SMH代理，未形成完整成员权重，不称可执行篮子。
- 软件：缺单独同步报价，不能说软件已成为防守。
- 电力：Vistra 11月6日事件观察，未形成公司交易信号。
- 工具：QQQ/SMH条件相对价值优于裸抄底；反向工具是相对多SMH，但只有在SMH重新取得相对强度且信用稳定后才研究。

公司原件：[Microsoft](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)、[Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/)、[Alphabet](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx)、[AMD](https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results)、[Arm](https://investors.arm.com/node/8506/html)、[NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/)。

## 8. 中国50/300/500/1000及公司专题

| 标的 | 1/3/5/20日收益 | EOD basis | 期权能力 |
|---|---|---|---|
| IH2612 | +0.36/+2.29/+2.65/-0.23% | -25.16点/-0.895%，年化-7.597% | HO2612 ATM14.51、RR25 -1.01 |
| IF2612 | +0.65/+3.09/+2.94/-6.33% | -15.81/-0.384%，年化-3.263% | IO2612 ATM18.93、RR25 -1.02 |
| IC2612 | +1.90/+5.24/+5.16/-10.23% | -37.33/-0.554%，年化-4.701% | 无默认同标的HO/IO/MO；代理有残余风险 |
| IM2612 | +2.10/+5.29/+4.77/-10.16% | -45.14/-0.679%，年化-5.762% | MO2612 ATM32.11、RR25 -3.80 |

现货50/300/500/1000当日+0.09/+0.29/+1.80/+2.12%。没有同期涨跌家数、行业贡献、两融与可核实机构订单，因此不猜“国家队”。期权PCR、forward与绝对gamma峰可读，但10Δ wings、完整期限结构和dealer净gamma方向不足；MO/IO/ETF代理IC必须披露指数、beta与basis残差。

**公司研究**：Stock引擎最新有效价量为10月30日，11月5日刷新HTTP401、candidate_union=0；不能由旧Top100生成今日信号。额外限定检索覆盖沪深公告的经营、订单、资本配置和负面风险：新大陆002546国网中标5558.5万元（约2025收入8.08%，但10月30日已预告）；统一600506冷却液框架无数量/价格/最低采购；京丰688368完成1.2亿元回购但拟未来出售；炬光688167拟注销34.96万股、仅0.27%且待股东会。四者均缺11月5日复权价、可交易状态与完整利润桥，故A股公司Top5为0；这是执行与证据不足，不是全市场无机会。

## 9. 未来24小时/7天事件与行动前核对

| 北京时间 | 事件 | Delta/Vega计划 |
|---|---|---|
| 2026-11-06 21:30 | 美国10月就业报告 | 发布前不加AI/黄金方向Delta；数据后30分钟再看收益率、美元、VIX与信用共同反应 |
| 2026-11-06 22:30 | 美国现金市场开盘 | QQQ/SMH只按顺序触发；禁止把盘前或首根K线称确认 |
| 2026-11-07 01:15 | Fed Bowman讲话 | 若政策路径再鹰、2Y反弹，则减少成长Delta/黄金Vega |
| 2026-11-07 04:30 | CFTC持仓（截至11/3） | 更新黄金拥挤判断，不回填为08:09已知 |
| 2026-11-09 09:30 | 中国CPI/PPI | IM/IH若已触发，事件前降低30%-50%名义或仅保留可承受跳空的整数手 |
| 2026-11-10/11/13 02:00 | 美国3Y/10Y/30Y拍卖（$58bn/$42bn/$25bn） | 黄金与长久期风险按尾部拍卖预留，不把期限溢价单因子化 |
| 2026-11-10 21:30 | 美国CPI | 高Vega结构在数据前核成本上限；无报价则不建仓 |
| 2026-11-13 01:00 | EIA WPSR（延期） | SC催化超过时间退出，不能据此延长旧计划 |
| 2026-11-10至15（未定） | 中国社融/信贷可能窗口 | 确切发布时间未公布；只作日历风险，不写成确定事件 |

行动前必须重核：完整AND/THEN顺序、实时报价/价差、合约乘数/保证金/限幅、借券与账户资格、同刻basis/Brent/现货、禁止追价、分批比例、独立止损/逻辑失效、TP与时间退出。模块版本与旧观点台账见JSON；CI仅push后独立校验，本报告不等待，状态`pending_or_unverified`。

### 风险预算与压力

通用试仓0.25%—0.75% NAV，确认0.75%—1.50%，同一高确信主题2.5%—3.0%；三张卡的更紧专属上限优先。期货手数=`floor(允许风险金额/计划每手损失)`，保证金不是风险预算。组合须压力测试跳空、连续涨跌停、保证金上调、隐波重定价、借券召回、流动性消失、跨市场假期冲击与相关性断裂。用户持仓未提供，不能计算净敞口。

---

## 来源与发布校验

关键来源均为可打开原始页或固定仓库ref；前序报告仅支持idea历史，不支持当前行情。发布前已重算评分、曲线、比率、名义、PnL公式和SC情景；无法取得的执行量均隔离为not execution-ready。MD/JSON由同一对象生成。归档目标为六路径；CI状态`pending_or_unverified`。

## 10. 今日行动清单

A. 没有。08:09 BJT时中国股票/股指尚未开盘、商品顺序尚未验证、美国现金市场未开；全部候选仍缺至少一个触发或实时执行参数。
B. 09:15后SC2612条件多、09:30后IM2612/IH2612相对多、22:30后QQQ/SMH相对多；均须完整AND/THEN顺序与放弃条件。
C. 黄金回撤型3—6月Call Spread待询价；SN2612失败反弹空；EC/FU/LU/MA/AG/CU/AP与A股公告候选继续观察。
D. 回避在VIX高位追空QQQ/SMH、低开追空SN、跳涨追多SC/黄金；旧SC空与AG2612多已失效，如用户另有真实持仓须按原失效条件独立核对，不假设已持有。