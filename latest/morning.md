# 全球跨资产机会雷达晨间版｜2026-11-08

- 生成时间：2026-11-08T08:01:47+08:00
- 信息截止：2026-11-08T08:01:47+08:00
- edition：morning
- 前序基准：2026-11-07 evening；同版基准：2026-11-07 morning
- 仓库固定ref：Global 5e6f0812f308b45241faa2d926badd92240af5a0；Commodities 14b121cef4aa7d29b117d8fdd81c5575953278dd；Options 471a8ad421abf9c01f51e25954230b865e77abc7；Stock 80485af92e8499513e966c9ef916e2c7be25c8e2
- 周末口径：周日无新EOD；美国、全球商品与中国资产最近完整交易时段均为11月6日，新增周末事件与价格证据严格分开。下一合法窗口：中国商品11月9日09:00、股票/股指09:30；美国现金市场22:30。

## 1. 一句话风险状态

周末混合去杠杆：强就业与高实际利率压制估值/黄金，芯片仅超跌反弹；海湾事件抬升油价尾部但无价格确认，中国CU跨期仍居首。

## 2. 全球仪表盘、事实台账与覆盖

| 模块 | 最新值 | 1D | 周变化 | 信号 | 观测时点 | 缺口/局限 |
|---|---:|---:|---:|---|---|---|
| 美国国债 | 2Y 4.51% / 5Y 4.64% / 10Y 4.86% / 30Y 5.26% | +5/+5/+2/+1bp | -5/-7/-8/-5bp | 长端高位但周度回落；就业后前端重定价 | 11-06 EOD | 官方名义收益率 |
| 实际/通胀 | 10Y实际2.63%；BEI估算2.23% | +3bp / -1bp | 约+3bp / -11bp | 实际利率继续压估值与黄金短线 | 11-06 EOD | BEI=同日名义-实际 |
| 曲线 | 2s10s +35bp；2s30s +75bp；5s30s +62bp | -3/0/-1bp | -3/0/+2bp | 曲线未给出单一衰退或供给答案 | 11-06 EOD | 计算值 |
| FX | DXY 102.26；EUR/USD 1.11437；USD/JPY≈158.49；USD/CNH 6.6735 | DXY +0.77% | 周变未统一核验 | 美元反弹，亚洲风险资产需等开盘确认 | 11-06 | Reuters；无可比FX期权skew |
| 科技 | Nasdaq 24579.42；QQQ 656.10；SOXX 136.53；SMH 463.96 | +1.09/+1.40/+3.46/+3.57% | Nasdaq -3.4%；ETF周变未独立核验 | 芯片超跌反弹，尚非基本面确认 | 11-06 close | QQQ/SMH=1.414，旧1.45确认未满足 |
| 原油 | WTI 90.83；Brent 98.32 | 约+0.34/+0.03% | 约-13/-17% | 周末航运风险抬尾部，尚无周末价格确认 | 11-06 settlement | 期限曲线/OVX/skew公开实时不足 |
| 黄金 | 现货≈4074；GLD 372.52 | 现货约-0.3%；GLD -0.79% | 现货约+5.2% | 政策信用中期叙事仍在，强美元/实际利率短线反证 | 11-06 | ETF日流、期权IV/skew未取得 |
| 风险 | VIX 25.56；MOVE 92.77；HY OAS 3.48% | -9.0% / -5.26% / — | MOVE约-7.4%；其余未核 | 波动仍高于安静区，信用仅last-good | 11-06；HY至11-05 | CTA与dealer净Gamma不可得 |
| 中国现货 | 上证50 2787.41；沪深300 4054.28；中证500 6597.35；中证1000 6505.35 | -0.84/-1.44/-2.13/-2.18% | 指数3/5/20日不可得 | 大盘防御相对占优，小盘承压 | 11-06 close | 周日休市 |
| 中国期指 | IH2612 2757；IF2612 4018.4；IC2612 6545.8；IM2612 6460.8 | OI变动 -854/-3233/-3601/+2807 | — | basis -1.091/-0.885/-0.781/-0.685%；不可据OI判新空 | 11-06 close | 年化约-9.48/-7.69/-6.79/-5.95% |
| 中国期权 | HO2612 ATM16.71/RR25 -1.97；IO2612 21.15/-1.86；MO2612 35.64/-4.82 | 仅1D可比 | 3/5/20历史不可得 | MO波动与put skew最高；dealer方向未知 | 11-06 EOD | history文件读取为空；PCR OI 0.660/0.639/0.607 |
| 商品 | 77品种/806合约；CU2612结算105110；SC2612结算636.8 | 源日11-06 | — | CU跨期和SC事件凸性进入统一榜 | 引擎生成11-08 05:57 | 新生成不等于新市场价格 |

### 可追溯事实台账（关键项）

| fact_id | 标的 | 数值/事实 | 口径 | 观测时间 | known_at | 支持判断 | 局限 |
|---|---|---|---|---|---|---|---|
| F-US-RATES-1106 | UST 2/5/10/30Y | 4.51/4.64/4.86/5.26% | official par yield EOD | 2026-11-06 ET | 2026-11-06 | 强就业后前端上行，周度仍回落 | 现金收益率，不等于期货可成交价 |
| F-US-REAL-1106 | 10Y TIPS real yield | 2.63% | official real par yield EOD | 2026-11-06 ET | 2026-11-06 | 黄金与成长估值短线逆风 | BEI为同日差值估算 |
| F-OIL-1106 | WTI/Brent | 90.83/98.32 USD/bbl | Friday settlement | 2026-11-06 NY | 2026-11-06 | 油价已大幅周跌，周末事件尚无价格确认 | 周末无合法新结算 |
| F-GULF-1107 | Gulf shipping event | 爆炸、触雷说法及美军拦截事件 | reliable media event report | 2026-11-07 local | 2026-11-07 | SC尾部催化上升 | 归属与因果未确认，不能量化供应损失 |
| F-CU-1106 | CU2612/CU2701 | 结算价差1080 CNY/t；夜盘观察1230 | official EOD + vendor snapshot | 2026-11-06 close / night snapshot | 2026-11-07 | 近月结构韧性但不宜追价 | 夜盘价非官方最终收盘 |
| F-SC-1106 | SC2612 | close 644; settlement 636.8; vendor night 639.1 | official EOD + vendor snapshot | 2026-11-06 | 2026-11-07 | 事件前价格未确认上破 | 周末无新盘 |
| F-CNIDX-1106 | SSE50/CSI300/CSI500/CSI1000 | 2787.41/4054.28/6597.35/6505.35 | cash close | 2026-11-06 CST | 2026-11-06 | 大盘相对防御、小盘更弱 | history文件为空，指数3/5/20日不可核 |
| F-STOCK-1106 | A-share universe | 5579 universe; 5573 quotes; 758 adv/4741 decl | raw EOD engine scan | 2026-11-06 CST | 2026-11-07T00:32:53Z | 广度显著偏弱 | 无复权、行业与正式指数成份，不等于指数宽度 |

所有读取时间仅是本次访问时间，不替代行情观测时间；旧报告只用于idea_id、历史条件和修订记录。关键异常输入已尽量回到官方或独立媒体；未取得的盘口、成交与曲面均留缺。

### 中国商品Core协议紧凑附录

- Futures：trade_date=2026-11-06；806合约/77品种；五所vendor full_market_ready=true；占位4；generated=2026-11-08 05:57 BJT。
- Market State：77品种有1/5/20日、RV20、OI和曲线；3日缺失。
- Physical：目标20，fresh18、missing2；仓单5项沿用；无合格A/B基差。
- External：目标22，fresh17、missing5；generated=2026-11-07 19:04 BJT，仅作情境。
- Night：trading_date=2026-11-09，session=11月6日晚至7日；420/806可见，coverage52.1092%，calendar_mismatch=false；night_last_price为vendor_latest_trade_asof_snapshot，非官方最终夜盘收盘；OHLC/vol/OI不声明完整纯夜盘。
- Options：target64、attempted46、successful45、1068条/45 series；core_atm_ready 44、skew_ready 29；surface/positioning/execution均0，bid/ask 0，full_chain_verified=false，dealer_gamma_direction_known=false。
- Contract Metadata：806合约partial；乘数/tick 36.10%，保证金/涨跌停30.15%，夜盘字段0%，最后交易日73.45%。
- futures_crosscheck：SHFE/INE/CZCE/GFEX有可比且无可信差异；DCE官方HTTP 412，未核。官方核对不覆盖成交量/OI。
- 研究影响：方向、曲线和局部ATM/skew可用于研究；缺完整曲面/全链/双边报价限制期权执行，不影响其他商品或全球资产评分。

63个原列表代码与动态挂牌品种均按引擎实际77品种扫描；黑色、有色、能源化工、新能源、农产品及EC均覆盖。重点非入榜异常：EC2612 5日大跌约11.2%但地缘/运价反抽风险高，研究空头得分64、未触发；SN2612曲线倒挂、库存偏紧且put skew约-8.78vol，反对立即追空；SA/FG备用观察为空，不据此认定无机会。

## 3. 较前序真正变化

1. 周末唯一新市场事实是伊朗南部爆炸、油轮触雷说法与美军阿曼湾拦截；它提高油价/航运尾部风险，但周日没有可验证新价格，SC催化+1、赔率-1、总分仍69。
2. 商品引擎11月8日05:57重新生成，但Futures/Market/Options源日仍为11月6日；这是质量状态更新，不是新催化或新行情。
3. MOVE核验为92.77、VIX官方文章为25.56；修正前序来源混杂后，风险水平仍偏高但未继续恶化。
4. CU与SC周五夜盘供应商快照未改变；SA/FG备用合约观察为空。合法last-good保留，不冒充周末新价格。
5. 限定检索紫金矿业与宝钢股份11月7—8日IR/公告，未发现新增经营披露；紫金保留观察而非执行升级。
6. 无用户成交回执；全部idea实际持仓状态仍为未提供/未知，CU、AP、SC原始触发均未在休市期间被视为满足。

## 4. 全球统一Top5

| 排名 | idea_id | 机会 | 方向 | 期限 | 工具 | 逻辑/赔率/催化/价格/拥挤=总分 | 研究结论/证据/执行 | 本期变化 |
|---:|---|---|---|---|---|---:|---|---|
| 1 | CN-CU-CAL-202611 | CU2612/2701跨期正套 | 多近空远 | 1—5交易日 | 上期所铜期货1:1 | 20/17/15/12/7=71 | 待验证优势/部分/等触发 | 总分不变；铜净多周减与夜盘跳升降低追价意愿，曲线韧性保留 |
| 2 | CN-AP-VOL-202611 | AP701局部事件波动 | 多波动候选 | 至到期前 | 苹果期权有限风险结构，待双边报价 | 18/16/15/12/9=70 | 待验证优势/部分/待报价与参数 | ATM IV低于RV20且put skew存在；无bid/ask与全链，不能称便宜或可执行 |
| 3 | CN-SC-EVENT-202611 | SC2612地缘事件凸性 | 条件做多 | 1—2交易日 | INE原油期货；期权仅研究 | 19/16/15/10/9=69 | 待验证优势/部分/等触发 | 周末事件令催化+1、缺口风险令赔率-1；总分不变，禁止高开追价 |
| 4 | GLD-POLICY-CREDIT-202610 | 黄金政策信用期权 | 中期偏多、短线等待 | 3—6个月 | 黄金Call Spread或MGC，均待报价/确认 | 19/15/15/10/9=68 | 待验证优势/部分/待报价与参数 | 周涨与避险支持；10Y实际2.63%、DXY102.26、CFTC净多下降压低短线确信 |
| 5 | CN-EQ-601899-202610 | 紫金矿业利润桥 | 研究多头 | 1—3个月 | 601899现货，执行未就绪 | 18/13/10/11/14=66 | 待验证优势/部分/休市/待执行核验 | 11月7—8日限定IR检索未发现新经营披露；财务强但非新催化 |

Top5是上限而非配额；评分仅表示研究优先级，不是胜率、预期回报或仓位。利率、FX、AI反弹、原油绝对方向、中国风格及个股均完成扫描；没有更高分者，是因为新增定价确认、完整执行参数或独立基本面证据不足，而非因商品模块挤占。

## 5. 详卡（2张）

### 5.1 CN-CU-CAL-202611｜CU2612/2701跨期正套

- 新增事实→已定价→分歧：官方11月6日结算价差1080元/吨；供应商周五夜盘观察价差1230，非官方夜盘收盘。夜盘价差扩张已反映部分近月紧张，我们的分歧只在“回落后结构能否重新站稳”，不是追逐现有跳升。
- 工具与中性：多CU2612、空CU2701，1:1；每腿5吨/手；价差按近月结算价减远月结算价。这是吨数匹配的跨期，不等于风险完全中性；两腿期限、流动性与基差风险仍在。
- 触发：11月9日09:15后：价差先回落至950—1000且不破800，然后15分钟收盘重新站上1050；同时LME铜≥13750且两腿深度可接受。全部AND，顺序必须满足。
- 分批：触发后50%；回踩1050守住再加50%；禁止在未回踩的跳空上追价
- 止损/失效：计划止损800；逻辑失效为价差<800，或LME<13750且曲线同步失败
- 目标/时间：TP1 1400减半；TP2 1650；最迟11月13日日盘收盘退出
- 催化：近月库存/仓单、LME价格与周一曲线重定价；最强竞争解释是夜盘扩张仅为低流动性或一次性挤压。下一项区分观测是回落后能否以成交和两腿深度共同确认。
- 成本情景：双腿合计500元/对，仅为压力情景，不是实报

| 成交 | 计划风险CNY | TP1净损益/R | TP2净损益/R |
|---|---:|---:|---:|
| 好950 | 1250 | 1750 / 1.40R | 3000 / 2.40R |
| 中975 | 1375 | 1625 / 1.18R | 2875 / 2.09R |
| 坏1000 | 1500 | 1500 / 1.00R | 2750 / 1.83R |

- 预算：试仓风险≤NAV 0.50%；手数=floor(0.005×NAV/最差情景风险)；铜+紫金主题≤NAV 1.25%
- 压力：流动性消失、两腿不同步、夜盘跳空可使实际损失超过止损；保证金不是风险预算
- 替代：若价差不回落，选择不交易；若只看铜方向，期权须重新取得双边报价

### 5.2 CN-SC-EVENT-202611｜SC2612事件凸性

- 新增事实→已定价→分歧：11月6日结算636.8、收盘644；供应商夜盘最近价639.1，相对收盘-0.76%、相对结算+0.36%，非官方夜盘收盘；SC2612-SC2701观察价差5.2。周末伊朗/航运新闻增加尾部，但没有周末可成交价格；因此催化提升、赔率同时下调。主要PnL来源只允许来自周一价格与近月结构确认。
- 合同：多SC2612；1000桶/手；最小变动0.1元/桶
- 触发：11月9日09:15后先守住636—640并有15分钟收盘≥640，SC2612-SC2701≥5且Brent≥98，随后再收复646。全部AND，顺序必须满足；若开盘≥650且无回踩，放弃。
- 分批：646确认50%；回踩确认位守住再加50%；648以上不新开
- 止损/失效：计划止损636；逻辑失效为Brent<96.5且SC近月价差<3
- 目标/时间：TP1 660减半；TP2 680；最迟11月10日日盘收盘退出
- 催化与反证：海湾航运中断/供应扰动；最强竞争解释是事件未造成实质供应损失且周跌趋势继续。下一项区分观测是Brent、SC近月价差与中国开盘顺序是否共振。
- 成本情景：往返成本/滑点1500元/手压力假设，不是实报

| 成交 | 计划风险CNY | TP1净损益/R | TP2净损益/R |
|---|---:|---:|---:|
| 好646 | 11500 | 12500 / 1.09R | 32500 / 2.83R |
| 中647 | 12500 | 11500 / 0.92R | 31500 / 2.52R |
| 坏648 | 13500 | 10500 / 0.78R | 30500 / 2.26R |

- 648以上不新开；坏情景TP1仅0.78R，必须依靠TP2或放弃。
- 预算：试仓风险≤NAV 0.50%；手数=floor(0.005×NAV/最差情景风险)；油价/航运主题≤NAV 1.25%
- 压力：周末跳空、连续涨跌停、外盘先行和人民币基差可使损失超过计划止损
- 替代：若高开不回踩则不交易；SC期权虽ATM IV约63.86%、RV20约44.65%，但无bid/ask且11月12日临近到期，不进入执行

两张期货卡的计划止损都不构成合同最大损失；跳空、限板与流动性消失时可超损。无用户成交回执，实际持仓=未提供/未知。

## 6. 黄金专题

- 结论：中期比喻不变、短线确信弱化。
- 支持/反对/缺失：现货周涨约5.2%与地缘风险支持；10Y实际2.63%、DXY 102.26及CFTC净多周减6903手反对；每日ETF流、央行当期购金与目标期权IV/skew缺失。
- 竞争机制：“政策信用期权”仅是经济比喻，不是合同限损。若实际利率与美元继续上行，流动性/机会成本解释强于信用叙事；若黄金在高实际利率下仍守4000且ETF重新净流入，才增强分歧。
- 工具比较：优先不交易；其次在取得现价、期限、IV与双边报价后研究3—6月Call Spread；MGC只在价格确认后；黄金多头+长债Put Spread须双边报价和组合DV01重算。跌破4000且DXY/实际利率再上破才研究反向有限风险结构。
- 执行：待报价与参数；不得沿用旧strike。现价、期限、IV、skew和可成交权利金不足时，不给strike、成本上限以外的精确净成本或“合同限损”承诺。

## 7. AI专题

- 判断：超跌反弹，不足以证明基本面修复。
- 市场证据：Nasdaq +1.09%、QQQ +1.40%、SOXX +3.46%、SMH +3.57%，但Nasdaq周跌3.4%；QQQ/SMH=1.414，旧1.45相对确认未满足。
- 全链覆盖：龙头/云平台看FCF与Capex回报；芯片与设备看订单、毛利和监管；网络设备等Cisco财报；软件/电力未取得新增公司原件。完整板块均扫描但无新独立公司事实。
- 相对价值：多现金流定价权、空远期Capex Beta仅保留主题；缺完整成员权重、beta、借券和同期报价，不能称Dollar-neutral或Beta-neutral。
- 处置：旧反向组合已退休；不追SMH反弹，等待Cisco与新财报原件。财报后IV与完整期权结构报价未取得，不能由VIX或单日反弹断言期权便宜。

## 8. 中国50/300/500/1000与公司专题

- 指数与basis：11月6日50/300/500/1000分别-0.84/-1.44/-2.13/-2.18%；IH/IF/IC/IM basis为-1.091/-0.885/-0.781/-0.685%。IM OI增加2807不能解释为新空。
- 期权：HO/IO/MO 2612 ATM IV 16.71/21.15/35.64%，RR25 -1.97/-1.86/-4.82vol；MO保护性put溢价最明显。绝对Gamma节点可见但dealer净方向未知。
- 风格：IH相对IM防御值得周一开盘30—45分钟验证；无可靠beta与同口径历史，不构造Beta-neutral交易。IC无同标的一一对应HO/IO/MO期权。
- 广度：全市场5573只行情中758涨/4741跌/74平，等权约-1.86%；3/5/20日原始等权约+3.19/+4.50/-8.17%，因无复权/成份只作市场背景。
- 紫金矿业：2026H1合并YTD：营收1941.78亿元、归母净利391.70亿元、经营现金流554.72亿元、资本开支129.43亿元；FCF代理425.29亿元。售价/销量、单位成本、库存、套保、汇率、少数股东与Kamoa维护仍是利润桥缺口。 收盘28.28，1D -4.07%；研究候选；休市且执行未就绪。铜/金上涨并不自动等于归母盈利改善；若销量/单位成本、套保、少数股东和Kamoa影响不支持，净受益假设可被推翻。
- 宝钢股份：2026H1合并YTD：营收1607.31亿元、归母净利45.71亿元、经营现金流148.15亿元、资本开支91.84亿元；收入增但归母净利降，钢价—矿煤—库存/合同滞后使净受益不确定。 收盘6.11，1D +0.49%；观察；不入Top5。
- 能力缺口：Stock引擎复权、公司行动、行业、正式指数成份、预期修订和执行可行性未就绪；限定IR检索范围仅紫金/宝钢，不能推断全市场无新机会。

IH↔HO、IF↔IO、IM↔MO映射准确；IC没有默认同标的一一对应期权。任何IO/MO/ETF代理均保留不同指数beta、basis及跟踪误差。周一09:30后的30—45分钟是未来验证计划，不是已经发生的盘中确认。

## 9. 未来24小时/7天事件、风险预算与发布校验

| 北京时间 | 事件 | 计划 |
|---|---|---|
| 11-09 09:00/09:30 | 中国商品/股票与股指下一合法窗口；中国CPI/PPI | 先验证SC/CU条件；股指开盘30—45分钟只作未来确认 |
| 11-09 21:00 | 中国下一夜盘窗口 | 重新核会话归属与官方日历 |
| 11-09 22:30 | 美国现金市场开盘 | 观察芯片反弹与美元/实际利率是否背离 |
| 11-10 02:00 | 美国3年期国债拍卖 | 关注前端与曲线，不以单次尾差断言供给冲击 |
| 11-10 21:30 | 美国CPI | 事件前不新增裸Delta/Vega；有限风险结构也需报价 |
| 11-11 01:00/02:00 | USDA/WASDE；美国10年期国债拍卖 | AP与利率候选分别重核 |
| 11-13 01:00/02:00 | EIA周报；美国30年期国债拍卖 | 检验油价供需与期限溢价 |
| 11-13 05:30/21:30 | Cisco Q1 FY27；美国PPI | AI网络设备盈利兑现；控制科技与通胀事件Vega |

- 通用风险预算：单笔试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同一高确信主题总预算≤NAV 2.5%—3.0%。
- 专属上限：CU与SC各≤0.50% NAV；铜+紫金与油价/航运主题各≤1.25% NAV，以更紧限制为准。
- 相关因子：黄金/长债/美元属于政策信用—实际利率簇；CU/紫金属于铜与中国增长簇；SC/航运属于地缘油价簇；IH/IM/A股共享中国beta，不能视作天然分散。
- 压力测试：跳空、连续涨跌停、保证金追缴、隐波重定价、流动性消失、相关性断裂及跨假期外盘冲击。未得用户持仓，净敞口不可计算。
- 发布校验：评分加总、CU/SC情景损益、合同乘数/单位、日历/DST、历史idea_id与MD/JSON同源渲染已实际检查；期权报价、用户账户权限、实时流动性与成交未全面认证，因此相关表达保持not execution-ready。CI状态为pending_or_unverified。

### 覆盖与来源

应覆盖且已分析：美债2/5/10/30Y、实际利率/BEI/曲线/Fed路径代理、DXY/EURUSD/USDJPY/USDCNH、AI全链、WTI/Brent、黄金、VIX/MOVE/HY OAS、中国四指数/期指/HO-IO-MO、77个中国商品品种、A股5579只全市场价量扫描与公司事实目录。受限：Fed精确隐含路径、FX/油/金期权skew、CTA、dealer净Gamma、ETF当日流、商品完整曲面、中国指数3/5/20日、A股复权/成份/执行资格。缺失只限制对应判断，不使其他模块失效。

1. [U.S. Treasury Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202611&type=daily_treasury_yield_curve)（U.S. Department of the Treasury；源日2026-11-06；支持：美国2/5/10/30年名义收益率及日周变化、2s10s、2s30s、5s30s曲线）
2. [U.S. Treasury Daily Treasury Real Long-Term Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)（U.S. Department of the Treasury；源日2026-11-06；支持：10年实际收益率2.63%、名义减实际估算10年BEI约2.23%）
3. [Employment Situation — October 2026](https://www.bls.gov/news.release/archives/empsit_11062026.htm)（U.S. Bureau of Labor Statistics；源日2026-11-06；支持：非农新增16.5万、失业率4.1%、平均时薪环比0.4%、同比3.1%）
4. [Dollar holds gains after solid jobs report](https://www.reuters.com/world/asia-pacific/dollar-holds-yen-gains-equity-rout-saps-risk-appetite-ahead-payrolls-2026-11-06/)（Reuters；源日2026-11-06；支持：DXY 102.26、EUR/USD 1.11437、USD/JPY约158.49、USD/CNH 6.6735、强就业后美元走强）
5. [Tech Stocks Rebound, But Nasdaq Is Still in Correction Territory](https://www.cboe.com/insights/posts/tech-stocks-rebound-but-nasdaq-is-still-in-correction-territory)（Cboe Global Markets；源日2026-11-06；支持：Nasdaq单日反弹1.09%但周跌3.4%、VIX收25.56并回落约9%）
6. [Oil set for sharp weekly drop](https://www.reuters.com/business/energy/oil-set-sharp-weekly-drop-middle-east-supply-concerns-provide-floor-2026-11-06/)（Reuters；源日2026-11-06；支持：WTI 90.83、Brent 98.32、周跌幅约13%与17%）
7. [Explosions heard in Iran's Qeshm island](https://www.reuters.com/world/middle-east/explosions-heard-irans-qeshm-island-iranian-media-reports-2026-11-07/)（Reuters；源日2026-11-07；支持：伊朗南部爆炸及两艘油轮触雷说法、因果与归属尚未确认）
8. [US military says it disabled cargo vessel in Gulf of Oman](https://www.reuters.com/world/middle-east/us-military-says-it-disabled-cargo-vessel-gulf-oman-2026-11-07/)（Reuters；源日2026-11-07；支持：美军称在阿曼湾使一艘试图突破封锁的货轮失去航行能力、周末航运尾部风险上升）
9. [Gold eases after strong U.S. payrolls](https://www.reuters.com/world/india/gold-eases-inflation-worries-higher-oil-us-payrolls-data-focus-2026-11-06/)（Reuters；源日2026-11-06；支持：现货金约4074美元/盎司、周涨约5.2%、强就业、美元和收益率抬升构成短线压力）
10. [CFTC Commitments of Traders COMEX](https://www.cftc.gov/dea/futures/deacmxsf.htm)（U.S. Commodity Futures Trading Commission；源日2026-11-03；支持：黄金非商业净多约179548手、周减6903手、铜非商业净多约37710手、周减10607手）
11. [ICE BofA MOVE Historical Data](https://www.investing.com/indices/ice-bofaml-move-historical-data)（Investing.com；源日2026-11-06；支持：MOVE 92.77、单日约-5.26%、较10月30日约-7.4%）
12. [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/data/BAMLH0A0HYM2)（Federal Reserve Bank of St. Louis；源日2026-11-05；支持：HY OAS合法last-good为3.48%、11月6日数据尚未取得）
13. [Economic News Release Schedule November 2026](https://www.bls.gov/schedule/2026/11_sched_list.htm)（U.S. Bureau of Labor Statistics；源日2026-11；支持：美国CPI与PPI发布时间）
14. [Cisco Schedules Q1 FY2027 Results Call](https://investor.cisco.com/news/news-details/2026/Cisco-Schedules-Conference-Call-for-Q1-Fiscal-Year-2027-Financial-Results/default.aspx)（Cisco Investor Relations；源日2026-11；支持：Cisco财报电话会为北京时间11月13日05:30）
15. [Global Cross Asset Radar previous evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/5e6f0812f308b45241faa2d926badd92240af5a0/reports/2026/11/2026-11-07_evening.json)（farfromexact；源日2026-11-07；支持：稳定idea_id、前序分数和原始条件、不用于证明当前报价）
16. [China Commodities Engine report input and radar](https://github.com/farfromexact/China-Commodities-Engine/tree/14b121cef4aa7d29b117d8fdd81c5575953278dd/data)（farfromexact；源日2026-11-06；支持：77品种、806合约期货扫描及五层证据、夜盘、期权Core、元数据与官方核对能力）
17. [China Options Engine radar](https://github.com/farfromexact/China-Options-Engine/blob/471a8ad421abf9c01f51e25954230b865e77abc7/data/radar_latest.json)（farfromexact；源日2026-11-06；支持：IH/IF/IC/IM及现货、basis、HO/IO/MO ATM与RR、radar_history读取为空，历史能力受限）
18. [China Stock Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/tree/80485af92e8499513e966c9ef916e2c7be25c8e2/data/latest)（farfromexact；源日2026-11-06；支持：5579只全市场扫描与5573只行情可用、紫金矿业和宝钢股份财务/公告证据目录及能力缺口）

## 10. 今日严格四行

A. 今天可立即建立的新仓：没有；周日休市，且周末事件尚无价格确认。
B. 今天仅应挂条件的候选：CU2612/2701按“回落→15分钟收复”顺序；SC2612按636—640守稳、Brent与跨期确认后再收复646；AP701仅待双边报价与完整腿参数。
C. 今天继续观察的机会：黄金政策信用中期假设、IH相对IM防御、紫金利润桥、AI现金流定价权对Capex Beta。
D. 今天必须回避或有条件退出的交易：回避追高油/铜/苹果期权、无报价期权、SMH超跌反弹及未触发的SN/EC空头；仅按原始失效条件处理假设持仓，不假定用户已成交。
