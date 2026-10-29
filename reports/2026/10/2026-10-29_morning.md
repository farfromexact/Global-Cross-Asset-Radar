# 全球跨资产机会雷达晨间版｜2026-10-29

- 生成时间：2026-10-29T08:08:19+08:00
- 信息截止：美国10月28日完整交易时段与盘后财报；中国10月28日EOD；商品夜盘主批次失效，仅精确合约公共回退观察。
- 性质：研究与交易决策支持；不自动下单，不推定历史建议已执行。

## 1. 一句话风险状态

风险偏好温和但分化：FOMC维持限制性利率、长端实际收益率抬升，油价与小盘偏强；微软现金流兑现而Alphabet资本开支吞噬现金，首选财报后相对价值，商品只做条件单。

## 2. 全球仪表盘

| 资产 | 最新值 | 1D | 周变化 | 信号 | 观察时点/口径 |
|---|---:|---:|---:|---|---|
| UST 2Y/10Y/30Y | 4.67% / 5.05% / 5.37% | -3bp / +6bp / +7bp | 未重算 | 2s30s 70bp，较前日陡10bp；长端供给/通胀溢价压制久期 | 2026-10-28 official；Treasury par yield |
| UST 10Y real / approximate BEI | 2.67% / 2.38% | +3bp / +3bp | 未重算 | 真实利率仍是黄金与长久期估值阻力 | 2026-10-28；Treasury nominal-real |
| DXY / EURUSD / USDJPY / USDCNH | 102.15 / 1.1160 / 157.87 / 6.6620 | DXY -0.2%; other exact close unavailable | DXY约+0.37%; others unavailable | 美元走弱但日元仍弱；CNH仅次级源 | 2026-10-28 NY / CNH 10-28；Reuters/secondary |
| Nasdaq / QQQ | 26549.85 / 725.61 USD | +0.27% / +0.60% | QQQ约+0.06% | 指数温和risk-on，盘后个股分化远大于指数 | 2026-10-28 close；Reuters/finance |
| SOXX / SMH | 521.94 / 567.67 USD | +2.09% / +1.81% | 未核 | 半导体继续领跑，拥挤与Capex Beta风险上升 | 2026-10-28 close；finance |
| WTI / Brent | 102.78 / 115.32 USD/bbl | +3.0% / +1.0% | WTI约+5.0%; Brent未核 | 供应风险溢价强，但汽油库存增加是反证 | 2026-10-28 settlement；Reuters |
| spot gold / COMEX Dec / GLD | 4070.28 / 4051.60 / 373.51 | +0.27% / -0.60% / +0.32% | 未核 | 政策信用韧性未失效；高真实利率阻止追涨 | 2026-10-28；spot/settlement/ETF close |
| VIX / MOVE / HY OAS | 16.91 / 93.44 / 318bp | -3.48% / -4.53% pre-FOMC / -12bp | VIX约+1.38%; others未核 | 股权波动平静；利率/信用指标口径滞后 | 10-28 / HY 10-27；secondary/FRED |
| IH2612 / SSE50 | 2713.4 / 2753.01 | -0.25% / +0.23% | 不可得 | basis -39.61pt/-1.44%，年化-10.30%未调息差股息 | 2026-10-28 close；CFFEX/cash |
| IF2612 / CSI300 | 4027.2 / 4083.87 | +0.23% / +0.85% | 不可得 | basis -56.67pt/-1.39%，年化-9.93% | 2026-10-28 close；CFFEX/cash |
| IC2612 / CSI500 | 6564.0 / 6640.89 | +1.37% / +1.99% | 不可得 | basis -76.89pt/-1.16%，OI+2965 | 2026-10-28 close；CFFEX/cash |
| IM2612 / CSI1000 | 6502.0 / 6578.10 | +1.53% / +2.35% | 不可得 | basis -76.10pt/-1.16%，OI+1931；旧多IH/空IM失效 | 2026-10-28 close；CFFEX/cash |
| HO/IO/MO2612 ATM / RR25 | 16.00/-1.37 \| 19.68/-1.86 \| 30.87/-3.66 vol | ATM -0.56/-0.52/-1.61 vol | history empty | MO仍最贵且put skew最深；不推dealer净Gamma | 2026-10-28 EOD；China-Options-Engine |
| BU2701 / SC2612 / CU2612 | 5140 fallback / 737.5 fallback / 109240 snapshot | EOD基准+1.06%/-1.26%/+0.52% | 5D +9.67%/+3.08%/+0.15% | 只等09:15价格+曲线+外盘AND条件 | 10-28 EOD; fallback through 10-29 02:31；engine EOD + nonofficial exact-contract fallback |
| China Stock capability | trade_date 2026-10-21 | stale | candidate_union empty | 公司研究可继续，执行信号不可用 | engine generated 2026-10-22；China-Stock-Engine |

### 商品能力紧凑附录

- Futures/Market：2026-10-28，806合约/77产品EOD可分析；Market State含1/3/5/20D、RV与near-minus-next曲线。
- Physical/External：18/20与17/22，部分且多为背景；basis_count=0，不能把近月曲线称现货基差。
- Night：交易日2026-10-29、会话归属无日历异常，但主批次0/806、806查询错误；公共精确合约latest不是官方夜盘收盘，OHLC/量仓和Night→Day分解禁用。
- Options Core：expected64、successful19、ATM ready19、skew ready12；full_chain/surface/positioning/execution均false，dealer gamma方向未知。局部IV可研究，不可编成交价、净成本或全链PCR。
- Crosscheck：SHFE/INE/CZCE/GFEX已比对且差异0；DCE为HTTP412/source_error，并非发现可信价差。
- Metadata：有效合约匹配73.45%、动态参数30.15%；因此只在卡片写已核乘数/到期，其他参数留缺。

## 3. 较前序真正变化

1. **FOMC由事件风险转为事实：3.75%-4.00%不变，但两票主张加息；10Y/30Y较前日升6/7bp，2s30s扩大到70bp。** 久期与黄金继续承受真实利率约束；单凭美元回落不能判定宽松。 旧观点处置：黄金维持观察，不把会后波动称触发。
2. **微软FY27 Q1 Azure +48%、FCF 18.6bn；Alphabet Cloud +103%却FCF -9.07bn，盘后分别约+5%与-8%至-10%。** AI主题从财报前观察升级为现金流定价权相对价值。 旧观点处置：继承AI-CASHFLOW-VS-CAPEX-BETA-20261028，新增可验证pair子方案，不追盘后缺口。
3. **EIA商业原油降1.892m桶但汽油增3.870m桶；Brent/WTI结算升1%/3%。** 油链供应溢价被价格确认，但需求端反证使BU/SC只保留回踩条件单。 旧观点处置：BU提高至75；SC旧空保持失效，创建新多子ID。
4. **中国小盘反转延续到现货与期货：CSI1000 +2.35%、IM2612 +1.53%，MO2611 ATM IV单日下降约3.79vol。** 旧多IH/空IM已失效；不反手追小盘，也不在缺bid/ask时做空波动。 旧观点处置：中国相对价值降为观察。
5. **商品夜盘主批次0/806，公共回退只有准确合约最新价；Options core成功19/64，execution_ready=false。** 不使用夜盘OHLC/量仓或编权利金；EOD全市场扫描仍有效。 旧观点处置：MA降为观察，BU/SC/CU需日盘重新确认。

## 4. 全球统一Top5

| 排名 | idea_id | 方向/期限 | 阶段 | 工具 | 逻辑/赔率/催化/价格/拥挤 | 总分 | 三轴判断 |
|---:|---|---|---|---|---:|---:|---|
| 1 | AI-MSFT-LONG-GOOGL-SHORT-POST-EARNINGS-20261029 | 等美元相对价值：多MSFT、空GOOGL；1—5D | 等10/29美股开盘30分钟与缺口回踩 | MSFT common/GOOGL common；非结构限损 | 23/16/18/10/11 | 78 | 研究：待验证优势；证据：充分于经营分化、部分于价格执行；执行：not_ready_wait_open |
| 2 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 | 条件多；1—3D | 等待09:15 AND条件后回踩 | BU2701 futures；非结构限损 | 20/17/15/13/10 | 75 | 研究：有边际但已部分计价；证据：三层、夜盘受限；执行：not_ready_wait_sequence |
| 3 | COM-E-SC2612-POST-EIA-GAP-RETENTION-LONG-20261029 | 条件多；日内—2D | 等待09:15价格/曲线/Brent确认 | SC2612 futures；非结构限损 | 19/16/15/12/10 | 72 | 研究：新子方向，优势待验证；证据：三层、夜盘量仓缺失；执行：not_ready_new_child |
| 4 | COM-M-CU2612-HVC-STRIKE-WATCH-20261025 | 条件多；3—10D | 等待SHFE/LME/曲线共振 | CU2612 futures；非结构限损 | 20/16/15/10/9 | 70 | 研究：有边际，外盘未确认；证据：三层但价格与曲线低于阈值；执行：not_ready_wait_09:15 |
| 5 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028 | 观察空；1—5D | 等待日盘与海外运价 | EC2612 futures；非结构限损 | 18/15/12/12/11 | 68 | 研究：方向假设/错价待验证；证据：仅价格与曲线两层；执行：not_ready_missing_external_physical |

分数是研究优先级，不是胜率、期望回报或仓位。Top5以外仍完成扫描：黄金、中国指数/期权、其余商品与A股公司均有结论。

## 5. Top3详卡

### 1) MSFT/GOOGL｜多MSFT、空GOOGL；等美元中性，不是Beta中性

- **新增事实→已定价→分歧**：MSFT Azure33.17bn(+48%)、FCF18.6bn、下一季Azure指引+49%—50%；GOOGL Cloud30.71bn(+103%)但FCF-9.07bn、广告低于预期且2027 Capex将显著增加。 10/28常规收盘MSFT531.01、GOOGL324.89；盘后约+5%与-8%至-10%，市场已大幅预付分化。 若开盘后分化回撤但不消失，现金流质量仍可能继续获得相对溢价；若Alphabet云增速使市场忽略现金流，pair会快速均值回归。
- **PnL/催化/竞争解释**：同一美元名义下MSFT收益率减GOOGL收益率，不以单腿代理组合PnL。 催化：10/29美国GDP/PCE、10/29盘后Amazon AWS/Capex、未来1—5交易日分析师指引修订。 最强竞争解释：Alphabet估值更低、Cloud增长更快；微软Capex偏低部分来自交付延迟而非永久节省。
- **下一观察与触发**：10/29 22:00 BJT后两腿相对缺口及成交量；不是盘后价触发。 触发顺序：22:00后MSFT相对10/28收盘>=+3%持续15分钟 AND GOOGL<=-6%持续15分钟 AND 相对收益差>=9个百分点；随后相对差回踩8.5—9.5个百分点并守8个百分点15分钟才进入。
- **入场与分批**：好/中/坏=relative gap 8.5pp/9.0pp/9.5pp；50%+50%；两腿同步，按实际价等美元；整数股取整后净美元敞口≤单腿1%；若多MSFT N股，则空GOOGL M=round(N×MSFT入场价/GOOGL入场价)；实际Beta未知，因此不称Beta-neutral。
- **止损/逻辑失效**：相对收益差跌破5pp持续15分钟；或MSFT跌破10/28收盘且GOOGL修复至>-3%时退出两腿。；Amazon披露显示全行业现金流/Capex同时改善，或Alphabet明确给出资本开支回报与现金流快速修复路径。
- **TP/时间/放弃**：TP1 相对收益差14pp减半；TP2 18pp再减/退出；时间退出 2026-11-04美股收盘；Amazon财报前将总风险降至≤试仓上限；放弃 开盘首个可交易相对差>14pp或借券/点差/停牌任一不可核。
- **成本与情景**：以每腿名义G计，组合PnL=G×(r_MSFT-r_GOOGL)。好/中/坏入场差8.5/9.0/9.5pp，止损5pp，风险3.5/4.0/4.5%×G；TP1毛R1.57/1.25/1.00，TP2 2.71/2.25/1.89。佣金、借券费、税费、滑点未知，不当0。
- **期权替代**：Call/Put spread可将单腿风险有限化，但缺10/29到期/strike/IV/bid-ask，待询价，不称更优。
- **风险预算/压力**：试仓计划损失≤NAV0.35%，确认≤NAV0.75%，单腿名义≤NAV10%、总毛名义≤NAV20%；AI/半导体主题合并≤NAV2.5%。 短腿理论损失不封顶；Alphabet向上跳空、MSFT下跳、借券召回、相关性断裂、美元汇兑均可令实际损失超过止损。


### 2) BU2701｜条件多

- **新增事实→已定价→分歧**：10/28 EOD close/settle5054/4945，5D+9.67%；公共精确合约夜间回退约5140，Brent结算115.32；汽油库存增加为反证。 高位与近月强曲线已计入相当供应风险；回退价不是官方夜盘收盘。 只有09:15后BU、曲线与Brent同时保持，且回踩承接，剩余趋势赔率才成立。
- **PnL/催化/竞争解释**：BU2701线性价格变化；不把保证金当风险。 催化：1—3D地缘、OPEC+ 11/1、下一周EIA。 最强竞争解释：风险溢价回落、汽油库存/需求担忧、夜盘曲线缺失。
- **下一观察与触发**：09:15/09:30/09:45的价格、BU2611-12曲线及同一Brent合约。 触发顺序：09:15后BU>=5120持续15分钟 AND BU2611-12>=5.50% AND Brent>=115.0；随后回踩5070—5100守5050。
- **入场与分批**：好/中/坏=5080/5090/5100；50%+50%，整数手
- **止损/逻辑失效**：4990；Brent<112.5 OR curve<4.5%
- **TP/时间/放弃**：TP1 5220；TP2 5360；时间退出 2026-10-30日盘收盘；放弃 首个可交易价>5200或曲线<4.5%
- **成本与情景**：乘数10。好/中/坏风险900/1000/1100元/手；TP1毛R1.56/1.30/1.09，TP2 3.11/2.70/2.36；费用/滑点未知。
- **期权替代**：商品期权execution_ready=false；不编权利金或有限损失成本。
- **风险预算/压力**：试仓NAV0.25%—0.50%，确认≤1.0%；与SC/FU/油气股主题合并≤NAV2.0%。 单日/连续跌停、保证金上调、夜盘流动性消失、Brent相关性断裂；计划止损不保证成交。
- **合同**：{"symbol":"BU2701","multiplier":10,"tick":1,"tick_value":10,"last_trading_day":"2027-01-15","margin_limit":"涨跌停12%；一般保证金14%、套保13%（SHFE通知，自2026-10-12）"}

### 3) SC2612｜条件多；旧空父ID仍为失效

- **新增事实→已定价→分歧**：10/28 EOD close约733.4，公共夜间回退约737.5；WTI/Brent结算上涨且商业原油下降，但汽油库存增加。 海外油价与夜间回退已计价，夜间最终曲线/OI缺失。 只有日盘价格、SC2612-2701曲线和Brent共振，才把新多从研究假设升级为执行候选。
- **PnL/催化/竞争解释**：SC2612线性上涨；不将旧空止损重置为新多。 催化：1—2D地缘/OPEC+及国内盘面对海外油的补涨或失败。 最强竞争解释：汽油库存、需求破坏、地缘回落、进口利润与汇率传导。
- **下一观察与触发**：09:15后738/730、0.75%曲线与Brent115。 触发顺序：09:15后SC>=738持续15分钟 AND SC2612-2701>=0.75% AND Brent>=115.0；随后回踩733—736守730。
- **入场与分批**：好/中/坏=733/734.5/736；50%+50%，整数手
- **止损/逻辑失效**：725；Brent<113 OR curve<0.40%
- **TP/时间/放弃**：TP1 748；TP2 760；时间退出 2026-10-30日盘收盘；放弃 首个可交易价>745
- **成本与情景**：乘数1000。好/中/坏风险8000/9500/11000元/手；TP1毛R1.88/1.42/1.09，TP2 3.38/2.68/2.18；费用/滑点未知。
- **期权替代**：SC期权局部研究能力不等于可执行；无全链/bid-ask/净成本。
- **风险预算/压力**：试仓NAV0.25%—0.50%，确认≤1.0%；与BU/FU/油气股主题合并≤NAV2.0%。 单日/连续跌停、SC与Brent脱钩、汇率与仓储冲击、流动性消失；期货损失不被止损封顶。
- **合同**：{"symbol":"SC2612","multiplier":1000,"tick":0.1,"tick_value":100,"last_trading_day":"2026-11-30","margin_limit":"当日动态保证金/限幅未在本次资料中独立核验"}

## 6. 黄金专题

- 状态：policy_credit_narrative_resilient_but_not_strengthened_not_executable。
- 证据：spot约4070.28、COMEX Dec settle4051.60；10Y real2.67%、DXY102.15；CFTC 10/20非商业净多191791，周降7942（last-good）；WGC 9月全球金ETF净流入100亿美元、持仓4256吨（last-good）；缺最新ETF日流、COMEX/GLD IV/skew和可执行权利金。
- 市场隐含与分歧：FOMC hold与鹰派异议已被利率和December hike定价；黄金现货韧性含有政策/地缘保险，但期货结算与高真实利率不支持追涨。 美元会后回落而黄金守住4000说明“政策信用期权”经济比喻尚未失效；竞争解释是地缘油价与流动性对冲，而非政策信用独占。
- 结论与证伪：不变，未增强；real10<2.55且黄金守4070会增强；real10>2.75、DXY>103且黄金<4000则失效。
- 表达比较：3—6月Call Spread仅在真实expiry/strike/IV/bid-ask后且净权利金≤宽度35%才候选；Micro Gold期货只作确认，线性且止损不封顶；黄金多+长债Put Spread需DV01/相关性/两套报价，不称天然对冲；跌破4000且真实利率/美元共振才研究Put Spread；当前首选不交易。
- 关键缺口：fresh official ETF creations/redemptions；COMEX/GLD live skew/term/Greeks；actual option premiums。

## 7. AI专题

- 状态：post_earnings_cashflow_dispersion_pair_is_conditional。
- 新事实：MSFT收入92.3bn、Azure33.17bn(+48%)、FCF18.6bn、capex45.2bn；Alphabet收入127.6bn、Cloud30.71bn(+103%)、FCF-9.07bn、capex51.36bn；QQQ+0.60%、SOXX+2.09%、SMH+1.81%；盘后MSFT约+5%、GOOGL约-8%至-10%；Amazon 10/30 05:00 BJT电话会将检验AWS与Capex。
- 完整覆盖：现金流龙头=MSFT/Alphabet issuer facts; Amazon pending；二线=未取得同步官方财报，不硬编；云=Azure/Google Cloud/AWS catalyst；软件=MSFT分发与Google广告/搜索；NOW仅价格事件未下钻；设备/半导体=SOXX/SMH领涨，缺公司级同步现金流；电力=未取得新一手公司事实，视为Capex Beta观察。
- 核心分歧：现金流定价权不等于云增速最高；本期分歧在于MSFT已把需求转成FCF，而Alphabet的Cloud增长被广告miss和Capex现金消耗抵消。 已定价：盘后大幅分化已计价，不追价。
- 最强反证：Alphabet Cloud增速远高于Azure且估值更低；若市场转而奖励规模扩张，空腿可能快速反弹。
- 工具比较：等美元多MSFT/空GOOGL；明确不是Beta-neutral。替代为只多MSFT、用QQQ对冲或不交易；期权因无价待询。
- 缺口：10/29 live open/volume；borrow fee and locates；pair beta/correlation；post-event IV crush and option chains。

## 8. 中国50/300/500/1000及公司专题

- 现货风格：SSE50 +0.23%；CSI300 +0.85%；CSI500 +1.99%；CSI1000 +2.35% 1D有效；3D/5D/20D同口径历史未由China-Options-Engine提供，不编。
- 期货与basis：IH2612 2713.4(-0.25%,vol34751,OI69410,ΔOI-1479); IF4027.2(+0.23%,68017,176426,ΔOI-1726); IC6564(+1.37%,130658,179327,ΔOI+2965); IM6502(+1.53%,239759,293240,ΔOI+1931) IH -1.44%；IF -1.39%；IC -1.16%；IM -1.16%；annualized -10.30/-9.93/-8.29/-8.28%，未调股息/资金成本
- 期现/风格表达：IF-IH与IM-IF当日偏小盘；Dollar-neutral需按合约乘数×价格配比，Beta-neutral另需滚动Beta；本期不因单日反转建仓。
- 期权映射与能力：IH↔HO；IF↔IO；IM↔MO；IC没有直接CFFEX中证500期权，MO/IO/ETF只可做代理并有Beta/basis/跟踪风险 HO/IO/MO2612 ATM16.00/19.68/30.87%；RR25 -1.37/-1.86/-3.66；BF25 0.41/0.57/1.23；PCR OI0.627/0.642/0.627；gamma峰仅绝对敏感度，dealer方向未知；MO2611 ATM单日约-3.79vol。
- ETF份额：510050份额-1.84%(估算-6.73亿CNY)；510300+0.38%(+5.79亿)；510500+0.94%(+4.40亿)；512100+3.68%(+11.07亿)。这是份额变动×收盘估算，不是二级市场净买卖。
- 研究结论：不追小盘；旧多IH2612/空IM2612失效，待至少两日风格确认
- Stock引擎：stale to 2026-10-21; candidate_union empty; 5568/5576 quotes; current execution unavailable
- 主动发现范围：限定检索CNINFO/SSE 10/28—10/29的三季报、订单、回购与负面风险；另核赛意信息10/23原始季报作为AI产业反证。
- 公司观察：赛意信息300687：Q3收入+8.63%、归母净利+604.45%，AI项目255个、算力合同累计>83亿元；但9M经营现金流-15.95亿元、短借25.24亿元、租赁负债16.28亿元，Capex/营运资金风险高。无新鲜价格/估值/可交易状态，不入Top5。
- 利润桥/证伪：算力业务利润桥=合同收入×交付/收费进度 - 服务器采购/租赁 - 电力/机房 - 融资利息 - 营运资金占用；收入增长不足以抵消现金流与杠杆时，净受益假设被推翻。
- 下一缺口：10/29开盘价量、公司行动调整、借款成本、合同回款与毛利、可交易状态/估值

## 9. 未来24小时/7天、覆盖核对与旧观点台账

### 事件日历

| 北京时间 | 事件 | 风险动作 |
|---|---|---|
| 2026-10-29 09:00/09:30 | 中国商品日盘/A股与CFFEX开盘 | BU/SC/CU自09:15验证；中国风格只观察前30—45分钟，不称已发生 |
| 2026-10-29 20:30 | 美国Q3 GDP初值 + 9月Personal Income/Outlays(PCE) | 若高于预期，削减长久期/黄金Delta；pair总风险不超过试仓 |
| 2026-10-29 21:30/22:00 | 美股开盘/30分钟验证 | MSFT/GOOGL只在相对缺口回踩顺序满足时进入 |
| 2026-10-30 05:00 | Amazon Q3电话会 | AWS/Capex/FCF；pair在事件前降至试仓或退出 |
| 2026-10-30 时间待定 | 日本银行政策决定 | USDJPY与全球久期；不预设结果 |
| 2026-10-30 20:30 | 美国Q3 Employment Cost Index | 工资通胀/收益率；减少裸Delta |
| 2026-10-31 09:30 | 中国官方PMI | 周期品/中国风格；只保留有界风险或降低期货仓位 |
| 2026-11-01 | OPEC+会议 | 油链跳空；BU/SC卡在10/30前时间退出 |
| 2026-11-04 20:30 | 美国9月贸易数据；EIA周报当周 | 增长/油品库存；精确EIA发布时间按官方日历再核 |

### 覆盖核对

| 模块 | 实际分析 | 缺失/受限 | 结论 |
|---|---|---|---|
| 美国国债/利率 | 全部利率与Fed；曲线=38/70/52bp | 拍卖明细/期限溢价模型 | 长端真实利率是更强约束；不是单纯增长担忧 |
| FX | 前三与CNH次级价、利率背离 | 同一时点官方CNH与FX skew/carry | 美元跌而曲线陡，不能单因子交易 |
| AI/科技 | QQQ/SOXX/SMH、MSFT/GOOGL、AMZN事件 | 二线/设备/电力同步公司级财报与期权 | 现金流兑现优于纯Capex Beta |
| 原油 | 结算、EIA、OPEC+、国内BU/SC | 准确海外月差、裂解、OVX/skew | 供应溢价强但需求反证要求回踩 |
| 黄金 | 价格、real、USD、last-good ETF/CFTC | fresh ETF/IV/skew/premium | 政策信用叙事不变、不可执行 |
| 中国股指/期权 | 10/28现货/期货/basis/ATM/RR/BF/PCR/gamma/ETF份额 | 3/5/20历史、IC直接期权、dealer方向 | 小盘反弹强但不追；旧pair失效 |
| 中国商品 | 实际77产品/806合约及模块状态 | 夜主批次、全链、DCE crosscheck、fresh部分实体 | BU/SC/CU条件化；其他未形成共振 |
| 中国股票 | engine能力与有限公共公告/赛意信息原件 | 10/28 EOD全市场、预期修订、公司行动/执行状态 | 0个可执行公司候选；赛意信息仅研究反证 |
| 市场风险 | VIX/MOVE/HY与中国风格/期权gamma峰 | VIX完整term、CTA和dealer净gamma | 表面平静，不足以证明卖波动便宜 |

### 风险预算

- 试仓：通用0.25%—0.75%；AI pair专属≤0.35%，商品卡0.25%—0.50%
- 确认：通用0.75%—1.50%；AI pair专属≤0.75%，BU/SC各≤1.0%
- 主题上限：通用2.5%—3.0%；能源主题≤2.0%，AI/半导体≤2.5%
- 规模公式：期货手数=floor(允许损失CNY/每手情景风险)；pair每腿名义G≤允许损失/止损相对差，且受总毛名义上限约束
- 持仓状态：未提供/未知；无成交回执，不推定触发、持仓或盈利
- 压力：跳空越过止损；连续涨跌停和保证金上调；隐波重定价/流动性消失；相关性断裂与pair短腿逼空；假期跨市场冲击；美元汇兑与借券召回。

### 状态与修订记录

| idea_id | 前序 | 当前 | 信号/持仓 | 修订 |
|---|---|---|---|---|
| AI-CASHFLOW-VS-CAPEX-BETA-20261028 | score65财报后观察 | 拆分子方案score78 | 财报经营证据满足；价格/执行未满足；未提供/未知 | 新证据：MSFT/GOOGL实际财报与盘后分化；保留父ID |
| AI-MSFT-LONG-GOOGL-SHORT-POST-EARNINGS-20261029 | 新 | score78等触发 | 等10/29 22:00后AND+回踩；未提供/未知 | 新证据/新子工具；不是追认盘后成交 |
| COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 | score71 evening/75 commodity morning | score75等触发 | 夜回退价不等于触发；等09:15顺序；未提供/未知 | EIA/Brent新证据；参数沿用商品晨报 |
| COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026 | 旧空score68 | invalidated | 原曲线/海外条件失败；未提供/未知 | 不移动旧止损、不重置ID |
| COM-E-SC2612-POST-EIA-GAP-RETENTION-LONG-20261029 | 新方向子ID | score72等触发 | 等09:15 AND+回踩；未提供/未知 | 新EIA/油价证据；换向明确拆分 |
| COM-M-CU2612-HVC-STRIKE-WATCH-20261025 | score72 evening/70 commodity morning | score70等触发 | 价格/曲线仍低于阈值；未提供/未知 | FOMC鹰派异议与未突破下调 |
| CN-IDX-IH-LONG-IM-SHORT-20261027 | score76 conditional | invalidated | 风格反向，原确认失败；无成交推断；未提供/未知 | 价格变化；不反手追小盘 |

### 发布前校验

- pass:78,75,72,70,68；各分项≤25/25/20/15/15且加总一致
- pass: 2s10s38bp,2s30s70bp,5s30s52bp,BEI2.38%; pair/BU/SC情景R按同一输入重算
- pass: futures minus spot; 51 calendar day annualization; no dividend/carry adjustment
- pass: 10/29美国仍EDT；US open21:30 BJT，验证22:00；中国09:15为未来验证
- pass for BU/SC multipliers and expiries from auxiliary; SC dynamic margin/limit left unknown
- pass: strict prior evening and same-edition morning deduplicated; stable IDs/parent IDs retained; no fills inferred
- single structured object rendered into MD/JSON；ordered AND/pullback/abandon/risk caps preserved
- 未解缺口：USDCNH/FX skew；MOVE final post-FOMC；HY OAS through 10/28；commodity night0/806；DCE official HTTP412；commodity option bid-ask/full-chain/dealer direction；China option3/5/20 history；Stock fresh EOD/tradability；actual account permissions/positions/fills。
- CI：pending_or_unverified。

### 事实台账（关键项）

| fact_id | 标的/事实 | 数值/口径 | 观察/known_at | 支持判断 | 局限 |
|---|---|---|---|---|---|
| F-RATE-001 | UST 2Y/5Y/10Y/30Y | 4.67/4.85/5.05/5.37%；official daily par yield | 2026-10-28 ET；2026-10-28 | 2s30s=+70bp and long-end real discount pressure | not intraday |
| F-REAL-002 | UST 10Y real / approximate 10Y BEI | 2.67% / 2.38%；official daily par real; nominal-real arithmetic | 2026-10-28 ET；2026-10-28 | gold opportunity cost remains high | BEI approximate, not swap inflation |
| F-FOMC-003 | Fed funds target | 3.75%-4.00%; 10-2 hold；policy decision | 2026-10-28 14:00 ET；2026-10-29 02:00 BJT | policy remains restrictive; two members preferred +25bp | does not by itself imply future hike |
| F-FX-004 | DXY/EURUSD/USDJPY | 102.15/1.1160/157.87；post-FOMC snapshot | 2026-10-28 NY；2026-10-29 BJT | dollar softened despite curve steepening | not common official close |
| F-US-EQ-005 | Nasdaq/QQQ/SOXX/SMH | 26549.85/725.61/521.94/567.67；cash close/latest consolidated | 2026-10-28 US close；2026-10-29 BJT | risk-on but semiconductor leadership | weekly changes incomplete |
| F-RISK-006 | VIX/MOVE/HY OAS | 16.91/93.44/318bp；close/pre-FOMC snapshot/10-27 | 2026-10-28/2026-10-27；2026-10-29 | equity vol calm while rate/credit data are lagged | MOVE not final post-FOMC; HY lagged |
| F-OIL-007 | WTI/Brent front futures | 102.78/115.32；settlement | 2026-10-28 US close；2026-10-29 | oil risk premium rose | exact futures month not independently captured |
| F-EIA-008 | US commercial crude/gasoline | 410.625m/209.180m；weekly stock | week ended 2026-10-23；2026-10-28 | crude -1.892m but gasoline +3.870m, mixed demand signal | weekly lag |
| F-GOLD-009 | spot gold/COMEX Dec/GLD | 4070.28/4051.60/373.51；spot snapshot/settlement/ETF close | 2026-10-28；2026-10-29 | spot resilience but futures settlement softer | time mismatch |
| F-MSFT-010 | Microsoft FY27 Q1 | revenue92.3bn; Azure33.17bn,+48%; FCF18.6bn; capex45.2bn；issuer results/Reuters calculated FCF | quarter ended 2026-09-30；2026-10-28 after close | cash-flow monetization and cloud demand | after-hours +5% not executable close |
| F-GOOGL-011 | Alphabet 2026 Q3 | revenue127.6bn; Cloud30.71bn,+103%; FCF-9.07bn; capex51.36bn；reported quarter | quarter ended 2026-09-30；2026-10-28 after close | cloud acceleration but capex cash burn | forecast miss context partly consensus-based |
| F-CN-IDX-012 | SSE50/CSI300/CSI500/CSI1000 | 2753.01/4083.87/6640.89/6578.10；cash close | 2026-10-28 16:14 BJT；2026-10-28 | small-cap rebound led | 3/5/20 cash history unavailable in engine |
| F-CN-FUT-013 | IH/IF/IC/IM2612 | 2713.4/4027.2/6564.0/6502.0；CFFEX close | 2026-10-28 EOD；2026-10-29 06:14 BJT | IH weak, IC/IM strong; basis all negative | no intraday sequence inference |
| F-CN-OPT-014 | HO/IO/MO2612 | ATM IV16.00/19.68/30.87%; RR25 -1.37/-1.86/-3.66vol；EOD model metrics | 2026-10-28 EOD；2026-10-29 06:14 BJT | small-cap IV highest; puts richer | dealer gamma direction unknown; history empty |
| F-COM-015 | China commodity universe | 806 contracts/77 products EOD; night0/806；engine status | EOD 2026-10-28/night trade date 2026-10-29；2026-10-29 07:03 BJT | EOD full scan valid; night primary unusable | public fallbacks are not official night closes |
| F-COM-OPT-016 | China commodity options core | 19/64 products; ATM19; skew12; full_chain=false; execution=false；sampled strikes | 2026-10-28 EOD；2026-10-29 | local research only | no bid/ask, positioning, term structure or dealer direction |
| F-STOCK-017 | China-Stock-Engine | trade_date2026-10-21; 5568/5576 quotes; candidate_union empty；engine snapshot | 2026-10-21；2026-10-22 | company research but not current execution | stale and no current corporate-action-adjusted price |
| F-A-CO-018 | 赛意信息300687 | Q3 revenue650.50m,+8.63%; net66.28m,+604.45%; 9M CFO-1.595bn；unaudited quarterly report | Q3/9M 2026；2026-10-23 | AI application/compute growth paired with severe cash conversion risk | not a 10/29 catalyst; no fresh tradability/valuation |

### 原始来源

1. [Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202610&type=daily_treasury_yield_curve)（U.S. Treasury，源日2026-10-28；支持：2/5/10/30Y nominal yields、curve slopes）
2. [Daily Treasury Par Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202610&type=daily_treasury_real_yield_curve)（U.S. Treasury，源日2026-10-28；支持：10Y real yield、approximate breakeven）
3. [FOMC statement](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)（Federal Reserve，源日2026-10-28；支持：3.75%-4.00% target、10-2 vote and dissents）
4. [Global markets after FOMC](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-28/)（Reuters，源日2026-10-28；支持：US index closes、oil/gold settlements、December hike pricing）
5. [Dollar after FOMC](https://www.reuters.com/business/dollar-holds-gains-ahead-fed-policy-signal-rbnz-decision-2026-10-28/)（Reuters，源日2026-10-28；支持：DXY/EURUSD/USDJPY snapshot、curve steepening interpretation）
6. [U.S. petroleum stocks](https://www.eia.gov/dnav/pet/pet_stoc_wstk_dcu_NUS_W.htm)（EIA，源日2026-10-28；支持：commercial crude inventory、gasoline inventory）
7. [Microsoft FY27 Q1 results](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)（Microsoft，源日2026-10-28；支持：revenue/operating income/EPS、Azure/cloud/RPO growth）
8. [Microsoft cloud growth and cash flow](https://www.reuters.com/business/retail-consumer/microsoft-beats-quarterly-cloud-revenue-estimates-2026-10-28/)（Reuters，源日2026-10-28；支持：FCF18.6bn、capex45.2bn、Azure guidance、after-hours reaction）
9. [Alphabet results and cash burn](https://www.reuters.com/business/alphabets-google-cloud-unit-beats-quarterly-revenue-estimates-steady-ai-demand-2026-10-28/)（Reuters，源日2026-10-28；支持：revenue/Cloud/FCF、ad miss/capex outlook、after-hours reaction）
10. [BEA release schedule](https://www.bea.gov/news/schedule)（BEA，源日2026-10-28；支持：Oct29 GDP、Oct29 Personal Income and Outlays、Nov4 trade）
11. [Amazon Q3 call notice](https://press.aboutamazon.com/2026/10/amazon-com-to-webcast-third-quarter-2026-financial-results-conference-call)（Amazon，源日2026-10-15；支持：Oct29 5PM ET call）
12. [BOJ release schedule](https://www.boj.or.jp/en/about/calendar/index.htm)（Bank of Japan，源日2026-10-29；支持：Oct30 policy decision window）
13. [China NBS 2026 release calendar](https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html)（NBS，源日2025-12-26；支持：Oct31 09:30 PMI）
14. [CFTC gold combined COT](https://www.cftc.gov/dea/options/deacmxsof.htm)（CFTC，源日2026-10-20；支持：gold noncommercial positioning）
15. [Global gold ETF holdings and flows](https://www.gold.org/goldhub/data/global-gold-backed-etf-holdings-and-flows)（World Gold Council，源日2026-10-07；支持：September inflow、global holdings）
16. [China Options radar](https://github.com/farfromexact/China-Options-Engine/blob/0427555a12998af2ab4131f7dd05176f9f6b67df/data/radar_latest.json)（China-Options-Engine，源日2026-10-28；支持：IH/IF/IC/IM and cash/basis、HO/IO/MO metrics and data quality）
17. [China Commodities unified input](https://github.com/farfromexact/China-Commodities-Engine/blob/1784fa4b651501d07c759c2cbcacb37abd431d0e/data/report_input_latest.json)（China-Commodities-Engine，源日2026-10-29；支持：entry empty status）
18. [China Commodities status](https://github.com/farfromexact/China-Commodities-Engine/blob/1784fa4b651501d07c759c2cbcacb37abd431d0e/data/last_run_status.json)（China-Commodities-Engine，源日2026-10-28；支持：806 contracts/77 products、module coverage）
19. [China Commodities night status](https://github.com/farfromexact/China-Commodities-Engine/blob/1784fa4b651501d07c759c2cbcacb37abd431d0e/data/night_session/last_run_status.json)（China-Commodities-Engine，源日2026-10-29；支持：0/806 primary night、query errors and fallback limits）
20. [China Commodities options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/1784fa4b651501d07c759c2cbcacb37abd431d0e/data/options/quality_latest.json)（China-Commodities-Engine，源日2026-10-28；支持：19/64 core products、no full chain/execution）
21. [China Commodities futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/1784fa4b651501d07c759c2cbcacb37abd431d0e/data/crosschecks/futures_latest.json)（China-Commodities-Engine，源日2026-10-28；支持：four exchanges matched、DCE HTTP412、differences0）
22. [China Stock engine manifest](https://github.com/farfromexact/China-Stock-Engine/blob/795e149866d7f1eefd1efdaf8fe510cd8f1c750e/data/latest/manifest.json)（China-Stock-Engine，源日2026-10-21；支持：staleness、universe and research capabilities）
23. [赛意信息2026年第三季度报告](https://static.cninfo.com.cn/finalpage/2026-10-23/1225616992.PDF)（CNINFO，源日2026-10-23；支持：Q3/9M financials、AI/compute contracts、cash-flow and leverage risks）
24. [Prior global evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/55deec1ab60d17b8b5f5349c2a18a9c7b3c32407/reports/2026/10/2026-10-28_evening.json)（Global-Cross-Asset-Radar，源日2026-10-28；支持：idea lineage only、prior scores/conditions）
25. [Commodity morning auxiliary](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/55deec1ab60d17b8b5f5349c2a18a9c7b3c32407/reports/2026/10/2026-10-29_commodities_morning.json)（Global-Cross-Asset-Radar，源日2026-10-29；支持：commodity fact ledger、candidate scenario math）

## 10. 今日四行

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：09:15后BU2701、SC2612、CU2612各自AND条件+回踩；22:00后MSFT/GOOGL等美元pair仅在相对缺口回踩且借券/点差可核时。
C. 今天继续观察：EC2612、黄金政策信用韧性、MO隐波压缩后的实际报价、赛意信息现金流/杠杆反证，以及Amazon对AI Capex回报的读穿。
D. 今天必须回避或有条件退出：回避追盘后AI缺口、已失效多IH/空IM与SC旧空、把夜盘回退价当官方收盘、无bid/ask期权及裸卖波动；若此前按条件建立，只按原止损/逻辑失效退出。

- 归档状态：success（首次六路径回读通过；CI pending_or_unverified）。

> 研究用途；具体账户权限、借券、保证金、合约流动性、报价、税费及执行资格须在下单前单独核验。