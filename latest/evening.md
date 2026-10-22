# 全球跨资产机会雷达晚间版｜2026-10-22

**实际生成：** 2026-10-22T20:22:25.310+08:00  
**信息截点：** 2026-10-22T20:12:00+08:00（截点时美国现金盘与中国10月23交易日商品夜盘均未开始）  
**输入版本：** Global b8130bf18df6；China-Options ad367e4c58ee；China-Commodities b0eaf30aa35c；China-Stock 795e149866d7  
**最近完整会话 / 下一窗口：** 中国股票与股指期货10月22日EOD；美国现金10月21日收盘、10月22日欧洲/盘前截至20:12；商品夜盘10月22日21:00（归属10月23交易日）；美股现金21:30；中国股指期货10月23日09:15、A股09:30。

## 1. 一句话结论

混合偏Risk-off：油价与AI资本开支风险压制权益，但长债走强、黄金反跌；只保留TLT、SC与纯碱的条件交易，撤回IM/IF偏多。

## 2. 事实台账与全市场仪表盘

### 关键事实台账

| fact_id | 标的/数值 | 口径与时间 | 支持判断 | 局限 |
|---|---|---|---|---|
| F01 | US 2Y/5Y/10Y/30Y CMT：4.81% / 4.95% / 5.13% / 5.42% | 2026-10-21官方收盘附近，% p.a.；观测2026-10-21 ET；known_at 2026-10-21；U.S. Treasury | 曲线仍陡且实际利率高 | 不是10月22盘中 |
| F02 | US 10Y实际/10Y BEI：2.76% / 2.37% | 官方实际CMT；BEI=5.13%-2.76%；观测2026-10-21 ET；known_at 2026-10-21；U.S. Treasury | 黄金机会成本仍高 | BEI为同期限简单差值 |
| F03 | US 10Y盘中：约5.05%（较前一时点-10bp） | Reuters盘中，不与官方CMT收盘口径混算；观测2026-10-22 约20:00 BJT；known_at 2026-10-22；Reuters | 油涨而债券上涨，增长/避险压过通胀 | 盘中会变 |
| F04 | Brent：约112美元/桶，约+3% | 欧洲时段盘中；观测2026-10-22 约20:00 BJT；known_at 2026-10-22；Reuters | 中东供应尾部与SC夜盘上行条件 | 不是结算价 |
| F05 | 现货黄金：4060.37美元/盎司，-1.9% | 1134 GMT盘中；观测2026-10-22 19:34 BJT；known_at 2026-10-22 20:03 BJT报道；Reuters | 避险失效、政策信用叙事降级 | 无同步期权IV/skew |
| F06 | VIX：开18.29，较前收16.68约+9.05% | Cboe延迟至少20分钟；观测2026-10-22 11:58 ET页面时点；known_at 2026-10-22；Cboe | 跨资产风险升温 | 期限结构未取得 |
| F07 | HY OAS：3.33% | 日度收盘、非季调；观测2026-10-20；known_at 2026-10-21 09:13 CDT；FRED/ICE | 信用未同步显示急性危机 | 滞后两日 |
| F08 | Meta Q3 2026：收入646.01亿美元；Capex349.1亿美元；FCF -21.2亿美元 | 公司季度披露，USD；观测截至2026-09-30季度；known_at 2026-10-21 US；Meta IR | 收入强、现金转化与资本密集度反证 | 含98.9亿美元法律费用影响成本 |
| F09 | Lam Sep-quarter：收入82.19亿美元；12月季指引86±4亿美元 | 公司季度披露，USD；观测截至2026-09-27季度；known_at 2026-10-21 US；Lam Research IR | 设备端需求/定价权较强 | 单家公司不代表全SOXX |
| F10 | 中国四指数EOD：50/300/500/1000=-0.81/-1.84/-2.71/-2.98% | 2026-10-22现金指数收盘；观测2026-10-22 15:00 BJT；known_at 2026-10-22 16:15 BJT；Tencent公开行情/指数官方标的 | 小盘相对大盘反转、撤回IM/IF偏多 | 非官方指数文件直连；异常用CFFEX期货交叉检查 |
| F11 | CFFEX 12月主力：IH/IF/IC/IM结算变动=-0.761/-1.594/-1.952/-2.116% | 结算对前结算；成交/OI为交易所EOD；观测2026-10-22 15:30 BJT；known_at 2026-10-22 16:20 BJT；CFFEX日行情CSV | 小盘风险更弱；四合约OI均增 | OI不识别新多/新空或dealer gamma |
| F12 | 商品Futures EOD：五所full_market_ready；77产品范围 | 供应商主源、10月22日EOD；观测2026-10-22；known_at 2026-10-22 19:03 BJT；China-Commodities-Engine | 全市场扫描与商品候选 | DCE官方交叉核对HTTP 412；成交/OI未官方复核 |
| F13 | 商品期权core_v1：45/64产品、70.3125%；1048行、45 series；bid/ask 0% | sampled_strikes，不是全链；观测2026-10-22 EOD；known_at 2026-10-22 19:04 BJT前；China-Commodities-Engine | 可研究局部ATM/RR，不可报可成交权利金 | surface/positioning/execution均false |
| F14 | China-Options：HO/IO/MO 2611 ATM IV=14.890/18.368/27.263% | 官方CFFEX 672行完整匹配后的10月20日last-good；观测2026-10-20 EOD；known_at 2026-10-21 06:15 BJT；China-Options-Engine | 仅作历史波动背景 | 比当前中国EOD旧两会话 |
| F15 | China-Stock：10月21日5568有效报价；候选并集0；公司财务包2家 | 未复权价格发现；tradability unknown；观测2026-10-21 EOD；known_at 2026-10-22 06:06 BJT前；China-Stock-Engine | 无可排名A股个股；限定公告检索仍需补证 | 对本报告日旧一会话，行业/正式成分/预期修订缺 |

### 仪表盘

| 资产 | 最新值 | 1D/一周 | 信号 | 时点与属性 |
|---|---|---|---|---|
| US 2Y/10Y/30Y | 4.81% / 5.13% / 5.42% | +2/+1/0 bp（10/21）；周未完整同口径 | 官方曲线仍陡；10/22 10Y盘中约5.05%显示避险 | 官方10/21；盘中10/22约20:00 BJT；官方CMT+Reuters盘中，不混算 |
| 10Y实际 / 10Y BEI / 2s30s | 2.76% / 2.37% / +61bp | -1/+2/-1 bp（10/21）；周未完整 | 实际利率仍高；曲线陡峭 | 2026-10-21 ET；Treasury官方，BEI/利差计算 |
| DXY / EURUSD / USDJPY / USDCNH | 日内+0.1% / 1.12 / 157.1 / 缺 | Reuters盘中；CNH缺；周缺 | 日元避险走强；CNH与FX skew不足 | 2026-10-22约20:00 BJT；盘中媒体；CNH不以CNY替代 |
| QQQ / SOXX / SMH | 725.20 / 510.36 / 556.70美元 | +1.06%/+2.07%/+1.86%（上一现金收盘）；周缺 | 财报后风险偏好被欧洲/盘前risk-off反转挑战 | 2026-10-21 16:00 ET附近；延迟现金收盘；非20:12可交易价 |
| WTI / Brent | 97.15（10/21结算）/约112盘中 | WTI -0.7%旧结算；Brent约+3%盘中；周缺 | 事件溢价抬升，国内SC须夜盘确认 | 10/21结算+10/22盘中；不可直接比较 |
| Spot Gold / Dec Gold / GLD | 4060.37 / 4075.70 / 378.95 | 现货-1.9%/期货-1.8%；GLD上一收+0.34%；周缺 | 未获避险流，黄金叙事降级 | 金价10/22 19:34 BJT；GLD 10/21；盘中+上一现金收盘 |
| VIX / MOVE / HY OAS | 约18.19估算 / 101.7 / 3.33% | VIX +9.05%；MOVE与OAS滞后；周未完整 | 权益波动抬升，信用尚未急剧恶化 | VIX 10/22 11:58 ET页面；MOVE 10/20；OAS 10/20；官方/延迟混合；VIX由前收×变动估算 |
| 上证50/沪深300/中证500/中证1000 | 2724.81/4036.30/6655.25/6578.27 | -0.81/-1.84/-2.71/-2.98%；周5日-1.46/-3.11/-1.68/-1.50% | 今日小盘显著跑输；20日四者均负 | 2026-10-22 15:00 BJT；现金指数EOD |
| IH/IF/IC/IM 2612 | 2679.2/3970.0/6543.0/6471.6 | 结算-0.761/-1.594/-1.952/-2.116%；周未列 | 基差-1.674/-1.643/-1.686/-1.621%；OI全增但方向不可识别 | 2026-10-22 15:30 BJT；CFFEX官方EOD；主力按成交/OI |
| HO/IO/MO 2611 ATM IV | 14.890/18.368/27.263% | 仅10/20 last-good；周history不足 | MO左偏最强但数据旧两会话 | 2026-10-20 EOD；China-Options-Engine；不可执行 |
| SC2612 / SA701 / AG2612 | 713.4 / 935 / 13608（EOD close） | SC同口径缺 / SA -1.68% / AG -1.37%；周SA -0.11% / AG +1.04% | 仅条件候选；21:00前无今晚新夜盘价 | 2026-10-22 EOD；供应商EOD；夜盘待发生 |
| A股Stock能力 | trade_date 10/21；5568有效报价；候选0 | 对报告日旧一会话；周原始多窗有；复权缺 | 公司研究可做，今日执行与价量信号不可做 | known by 2026-10-22早间；China-Stock-Engine |

## 3. 相较晨报与前一晚报的实质变化

1. **风险状态从晨间混合偏Risk-on转为混合偏Risk-off**：欧洲科技下跌、美国期货跌1%-1.7%、VIX约+9%；同时10Y降至约5.05%；处置：提高对冲/久期排序，降低AI追多分数。
2. **黄金避险背离恶化**：油价与地缘风险上升、债券上涨但现货金跌至4060.37；处置：政策信用期权由偏弱/证据不足下调为减弱；不做3-6月call spread。
3. **中国小盘相对优势反转**：CSI1000 -2.98%对CSI300 -1.84%，IM主力结算跌幅大于IF；处置：撤回CN-SMALL-LARGE-RV-20261013预入场计划。
4. **商品全市场更新至10月22日**：EOD full_market_ready；SC/SA/AG有多层条件，但今晚21:00尚未开始；处置：只挂顺序条件，不把上一夜盘快照作当前证据。
5. **AI基本面更分化**：Lam收入/指引强，Meta收入强但FCF为负且Capex高，盘前risk-off；处置：SOXX条件多从80降至70；多现金流/空Capex仅主题观察。

## 4. 全球统一机会榜（Top 5上限）

分项顺序为逻辑/赔率凸性/催化/价格曲线波动/拥挤技术；分数是研究排序，不是胜率或仓位。

| 排名 | idea_id / 工具 | 方向与期限 | 三轴状态 | 分数 | 关键分歧与损失边界 |
|---:|---|---|---|---:|---|
| 1 | UST-TACTICAL-RALLY-20261013<br>TLT 2026-11-20 79/83 Call Spread | long_duration_after_cash_confirmation；2-15个交易日 | 存在待验证优势 / 部分 / 等待触发与报价 | 78 (21/20/18/10/9) | 仅两层证据、总分封顶69；保证金待核 |
| 2 | COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021<br>SC2612夜盘确认后多 | long_after_two_stage_night_confirmation；1-3个交易日 | 存在待验证优势 / 部分 / 等待触发 | 76 (21/18/18/11/8) | Brent/EIA支持而国内尚未确认；期货止损不封顶 |
| 3 | COM-M-SA701-CONTANGO-WARRANT-SHORT-20261022<br>SA701夜盘确认后空 | short_after_break_and_failed_reclaim；1-5个交易日 | 存在待验证优势 / 部分 / 等待触发 | 72 (20/17/15/11/9) | contango/仓单支持但IV已贵；期货止损不封顶 |
| 4 | AI-SOXX-EARNINGS-CONFIRM-LONG-20261022<br>SOXX 2026-11-20 510/540 Call Spread | long_only_after_risk_off_reversal；2-15个交易日 | 优势降级且待验证 / 部分 / 等待触发与报价 | 70 (20/18/17/7/8) | Lam强、Meta现金流弱；净借记成交后才限损 |
| 5 | COM-M-AG2612-SILVER-REPAIR-SHORT-20261022<br>AG2612反弹失败后空 | short_after_failed_rebound；1-5个交易日 | 存在待验证优势 / 部分 / 等待触发且保证金待核 | 69 (18/17/14/11/9) | 仅两层证据、总分封顶69；保证金待核 |

未入榜但已完成：外汇、黄金、原油中期、AI相对价值、中国四指数方向/跨期/风格、A股双通道、其余商品板块。未入榜不等于未研究；实时skew/报价不足的项目不能称“无机会”。

## 5. 详细交易研究卡（3张）

### 1) UST-TACTICAL-RALLY-20261013

- **状态修订：** 上次72分 → 本次78分。10Y在Brent上冲时反而跌至约5.05%，新增避险/增长确认；仍无现金盘同步报价。
- **逻辑链：** 新增事实→油价约112美元但10Y跌约10bp至5.05%，说明短线债券避险压过通胀；市场已定价→TLT上一现金收盘80.24、10Y已低于5.10%，已有一部分反弹；分歧→若美股现金盘仍守80.20且10Y持续<5.10%，供给压力被阶段性吸收；主要PnL来自久期价格与有限借记凸性。
- **最强竞争解释：** 5Y TIPS拍卖、油价与期限溢价可令实际利率再上行；当前TLT只得上一现金时点，双腿报价未确认。
- **下一项区分观测：** 21:30 BJT后同时观察TLT、10Y，持续30分钟。
- **工具比较：** 买1张TLT 2026-11-20 79C、卖1张83C；替代是小名义直接多10Y期货/DV01校准，但后者尾损无限，当前不优。
- **触发/顺序：** TLT>80.20 AND 10Y<5.10%，持续30分钟；若TLT>81.20后才同时满足则不追。
- **入场/报价：** 只有净借记≤1.55美元/份额；好≤1.35，中1.35-1.55，坏>1.55放弃。
- **逻辑失效/计划止损：** 10Y日收>5.25% OR TLT<78.70；10Y实际>2.85%亦取消。
- **TP1/TP2/时间退出：** TP1 TLT81.0或价差1.5倍成本；TP2 82.7-83；10月30日时间退出。
- **好/中/坏情景净损益：** 4点宽。借记1.35：最大亏损135美元、最大盈利265美元、毛R=1.96；借记1.55：155/245美元、毛R=1.58；费用/滑点另加。
- **风险预算与尾部：** 每组按真实净借记+费用计合同最大损失；试仓预算NAV 0.25%-0.75%，手数=floor(NAV×预算/(借记×100+费用))。

### 2) COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021

- **状态修订：** 上次未入全球榜分 → 本次76分。从商品晚报接入全球榜单；Brent约112与美国库存下降支持，但必须以今晚新夜盘顺序确认。
- **逻辑链：** 新增事实→EIA原油库存周减306万桶、Brent盘中约112；市场已定价→SC2612日收713.4、结算702且局部ATM IV59.47%，尾部溢价已高；分歧→只有SC把海外冲击转成724上方的持续收盘，国内贴水才算修复；PnL来自价格重估而非卖波。
- **最强竞争解释：** Brent事件溢价回吐、SC近月曲线不能扩至≥0.70%、国内需求弱；期权执行不可用。
- **下一项区分观测：** 21:15第一根15分钟K、21:45前二次确认；旧夜盘快照不计。
- **工具比较：** SC2612多1手起；乘数1000桶/手、tick0.1元/桶、tick价值100元。替代SC call spread因无bid/ask且execution_ready=false，仅研究不执行。
- **触发/顺序：** 21:15首根15分钟收盘≥724 AND Brent≥111.5 AND SC2612-SC2701可比价差≥0.70%；随后至21:45无15分钟收盘<720且至少另一根收盘>724。
- **入场/报价：** 724/727/730三档各1/3；若直接>735放弃。整数手不足3手则只做1手试仓，不伪装分批。
- **逻辑失效/计划止损：** 任一15分钟收盘<714，或Brent<109.5，或可比近月曲线≤0。
- **TP1/TP2/时间退出：** TP1 742减半；TP2 765；最迟10月26日退出。
- **好/中/坏情景净损益：** 含假设成本0.4元/桶=400元/手：好724止714，损10400元，TP1净17600/R1.69、TP2净40600/R3.90；中727损13400，净14600/R1.09、37600/R2.81；坏730损16400，净11600/R0.71、34600/R2.11。
- **风险预算与尾部：** 保证金约18%只是资金占用，不是最大损失；跳空/限幅可穿越714。

### 3) COM-M-SA701-CONTANGO-WARRANT-SHORT-20261022

- **状态修订：** 上次未入全球榜分 → 本次72分。10月22日跌势、contango、仓单与局部IV共同进入候选；日低恰为926，旧的<926未触发。
- **逻辑链：** 新增事实→SA701日收/结算935/936、1日-1.68%、ΔOI+26897；市场已定价→日低已到926且局部ATM IV24.93%高于RV16.16%，空头并不便宜；分歧→若夜盘有效跌破926且不能收复936，contango与仓单压力才成为趋势而非日内过冲；PnL来自线性下跌。
- **最强竞争解释：** 能源/化工夜盘联动反弹、空头回补、局部RR+2.66显示上尾也有需求；OI不说明新空。
- **下一项区分观测：** 21:15后15分钟收盘与随后30分钟是否失败收复。
- **工具比较：** SA701空1手起；乘数20吨/手、tick1元/吨、tick价值20元。替代有限风险put spread因无bid/ask不执行。
- **触发/顺序：** 21:15后15分钟收盘<926；其后30分钟无15分钟收盘>936且最终一根仍<926。
- **入场/报价：** 926/924/922各1/3；直接<918放弃追空。
- **逻辑失效/计划止损：** 计划止损947；若夜盘收复936并保持则逻辑先失效。
- **TP1/TP2/时间退出：** TP1 895减半；TP2 860；10月29日时间退出。
- **好/中/坏情景净损益：** 含2 ticks=40元/手假设成本：好926损460元，TP1净580/R1.26、TP2净1280/R2.78；中924损500，净540/R1.08、1240/R2.48；坏922损540，净500/R0.93、1200/R2.22。
- **风险预算与尾部：** 保证金8%、限幅7%来自当前合约元数据；期货止损不封顶，压力按1-2个限幅及流动性消失另算。


## 6. 黄金专项

判断：**政策信用期权叙事减弱**。现货金在Brent约112美元、全球权益risk-off、10Y收益率下行时仍跌至4060.37美元，说明高实际利率/年末紧缩预期和流动性竞争暂时压过避险。这里“期权”仅是宏观类比，不是合同限损。

- 支持：地缘、油价与长期财政/政策信用风险仍在；央行长期购金逻辑未被单日推翻。
- 反对：今日最关键的跨资产检验失败；最新ETF流、CFTC持仓、目标期限IV/skew未同步取得。
- 3—6月Call Spread：不做。沿用而不重置原始确认：spot>4200 AND GLD>385.2 AND 10Y实际≤2.70% AND DXY≤102.5；同时须取得实时报价。
- 微型黄金期货：只可在上述价格/实际利率重新确认后作为线性验证，止损不封顶。
- 黄金多+长债Put Spread：理论上对冲实际利率上冲，但本期两边期权均无同步报价，无法核算净Vega/成本；不执行。
- 反向：仅当spot<4050且10Y实际>2.85%时研究GLD put spread，仍需权利金、IV和Greeks。现在不追空。

## 7. AI专项

Lam给出设备端强收入与指引；Meta收入同比+26%，但单季FCF为-21.2亿美元、Capex 349.1亿美元，现金流与资本开支出现最清晰分化；Tesla收入280.46亿美元而经营利润率承压。欧洲科技与美股期货risk-off说明市场正在把“收入增长”与“资本密集度/治理/现金转化”分开定价。

- **自然工具：** SOXX 510/540 call spread只在美股现金盘30分钟>515且回踩510不破、净借记≤10时保留；晨报80降至70。
- **替代：** 多Lam/空Meta或Tesla是现金流—Capex主题，缺同步Beta、成分权重、借券与报价，不能称Dollar-neutral或Beta-neutral，只观察。
- **全链覆盖：** 芯片设备获Lam支持；芯片指数需现金盘验证；云/网络/电力仍受 hyperscaler Capex支持；软件现金化相对好；二线融资敏感标的在高利率下风险最大。
- **反证：** 若SOXX现金盘站不上515、Meta电话会不改善现金转化，或10Y重上5.25%，上行分支失效；若订单/指引继续扩散且SOXX站稳515，旧SOXX下行分支正式失效。

## 8. 中国50/300/500/1000、A股公司与商品专项

### 指数与期指

| 标的 | 现金1/3/5/20日 | 2612 close/settle | settle 1D | 成交/OI/ΔOI | close basis / 年化* |
|---|---|---|---:|---:|---:|
| 上证50/IH | -0.810% / -1.784% / -1.462% / -4.903% | 2679.2/2684.8 | -0.761% | 41459/78225/+7173 | -1.674% / -10.72% |
| 沪深300/IF | -1.839% / -3.311% / -3.114% / -9.909% | 3970/3987.6 | -1.594% | 89956/188861/+11439 | -1.643% / -10.52% |
| 中证500/IC | -2.709% / -2.138% / -1.684% / -13.382% | 6543/6621 | -1.952% | 124894/185322/+16646 | -1.687% / -10.80% |
| 中证1000/IM | -2.979% / -1.792% / -1.503% / -13.300% | 6471.6/6549 | -2.116% | 218470/298458/+26635 | -1.622% / -10.38% |

* 年化仅作57个日历日至2026-12-18的简单年化，不含分红、融资与roll；不是可实现收益。

今日CSI1000相对CSI300落后1.14个百分点，50相对1000领先2.17个百分点；IM主力结算跌幅也大于IF。因此 CN-SMALL-LARGE-RV-20261013 在未入场状态下撤回，不反手追空。IH相对防御，但四个主力均贴水且OI增加不能识别新空/套保/换月，最合适结论是“防御观察”，不是多IH确认。

### HO/IO/MO

独立股指期权引擎last-good为10月20日：HO/IO/MO 2611 ATM IV 14.890%/18.368%/27.263%，RR25 -0.546/-1.696/-3.527 vol点，BF25 +0.607/+0.459/+0.397，PCR(OI) 0.644/0.665/0.595，Gamma峰值2800/4200/7000。数据比当前EOD旧两会话，只能作背景，不能据此下HO/IO/MO订单、判断dealer净Gamma或构建今日IV-RV。IC没有一一对应的指数期权；MO代理IC会留下Beta、基差与跟踪误差。

### China-Stock-Engine与主动公告发现

引擎trade_date为10月21日：5568/5576有效报价，3/5/20日原始窗大体可用，但复权收益、行业、正式指数成分、预期修订和交易状态未就绪；候选并集为0，公司证据目录仅宝钢、紫金两家。其证据可做旧事实/利润桥背景，不能生成10月22日新信号。

本次额外检索SSE/SZSE/CNINFO的半导体、能源、钢铁及公司IR新公告。截至20:12没有找到可进入全球Top5的新经营/订单/资本配置事实。唯一明确未来点是长电科技公告：10月23日披露Q3、10月27日15:00召开说明会。它是未来催化，不是已知盈利；下一缺证是先进封装收入、毛利率、Capex与经营现金流同口径利润桥。个股报价/停复牌/涨跌停/成本未核，不称可执行。

### 中国商品全市场覆盖与质量

10月22日EOD覆盖维护中的77品种，包含用户指定63+清单；钢矿煤焦、基本金属/贵金属、能源化工、新能源、农产品、航运均完成价格/1-20日/曲线/可得仓单实体/外盘/局部期权扫描。代表异常：SC获全球油价与EIA支持但等夜盘；SA下跌+contango+仓单进入条件空；AG仅价格/曲线两层，得分封顶69；MA/EB上涨且backwardation，与“化工全面走弱”相反；AP/LH弱但曲线冲突，不入榜。

| 模块 | 源/交易日 | 能力与结论 | 缺口 |
|---|---|---|---|
| Futures | 10/22 EOD，19:03生成 | 五所full_market_ready；供应商主源 | DCE官方HTTP 412；量/OI未官方交叉核验 |
| Market/Physical/External | 10/22及各原生频率 | 曲线可用；仓单部分carry；外盘可作映射 | spot basis、会员排名不可用 |
| Options | 10/22，core_v1 | 45/64产品、1048行、45 series；SC/SA等局部ATM/RR可研究 | 非全链；bid/ask 0%；surface/positioning/execution false |
| Night | 最近归属10/22、session 10/21 | vendor latest-trade snapshot，非官方夜收 | 今晚归属10/23的夜盘在截点尚未开始 |
| Contract metadata | 当前ref | SC/SA乘数/tick等候选参数可用 | 部分错误，AG保证金未确认 |
| Crosscheck | 10/22 | SHFE238、INE63、CZCE243、GFEX48合约的可比close/settle/pre-settle无可信差异 | partial来自DCE源错误，不代表价格不一致 |

商品局部期权：SC ATM IV59.47% vs RV50.25%、RR25 +5.30；SA 24.93% vs16.16%、RR25 +2.66；AL 11.16% vs11.33%、RR25 -2.17。它们是已就绪系列的局部指标，不是完整曲面/PCR/拥挤/dealer gamma，更不是可成交权利金。

## 9. 未来24小时/7天风险日历与夜盘地图

| 北京时间 | 事件 | 状态 | 风险处置 |
|---|---|---|---|
| 2026-10-22 20:30 | US initial jobless claims | scheduled; after cutoff | TLT/SOXX不在数据前预挂市价；只留限损结构 |
| 2026-10-22 21:00 | 中国商品10月23交易日夜盘 | scheduled | SC/SA/AG执行15/30/45分钟顺序闸门；无触发即不做 |
| 2026-10-22 21:30 | 美股现金开盘 | scheduled under US DST | 验证TLT/10Y与SOXX；前30分钟不追价 |
| 2026-10-23 01:00 | 美国5Y TIPS拍卖 | Treasury tentative schedule | 久期结构降低Delta，若实际利率上破2.85取消 |
| 2026-10-23 中国披露时段 | 长电科技Q3 2026报告 | 公司公告已确认 | 只读取正式财报后再做利润桥；今日不抢跑 |
| 2026-10-23 21:45 / 22:00 | S&P Global US PMI / Michigan final | 日历待临近复核 | 限制SOXX/TLT Vega与方向仓位 |
| 2026-10-27 15:00-16:30 | 长电科技业绩说明会 | 公司公告确认 | 核先进封装收入、毛利率、Capex/现金流，不把订单表述当已兑现盈利 |
| 2026-10-28 美国时段 | EIA周度油品库存 | EIA下一期 | SC若仍持有则减隔夜Delta |
| 2026-10-29 02:00 / 02:30 | FOMC决定/发布会 | Fed日历 | 不裸卖Gamma；TLT到会前分批止盈或降Delta |
| 2026-10-29 20:30 | 美国Q3 GDP初值与9月PCE | BEA日历 | 虽略超7日边界仍为主要时间退出锚；黄金/久期不得跨越而无保护 |

今晚商品夜盘三情景：

1. **油继续上冲且SC曲线扩张：** 只按SC两阶段AND触发；21:15/21:30/21:45分别核首收、守720、二次收>724。
2. **油稳而内盘不跟：** 不做SC；SA只在跌破926且不能收复936时空，AG只观察。
3. **油回落或流动性恶化：** 取消SC，多腿期权因无bid/ask不启用；期货只保留未触发状态。

## 10. 覆盖、台账与发布闸门

- **应覆盖：** 七大全球模块、中国四指数及期权、A股双通道、维护77商品与新挂牌核查。
- **实际分析：** 全球利率/FX/AI/油/金/风险；中国现金与CFFEX同日EOD；China-Options last-good；Commodity Futures/Market/Physical/External/Night/Options/Metadata/Crosscheck；Stock价量与公司目录，并做限定公告检索。
- **关键缺口：** USDCNH exact current quote and FX skew；OVX and target option skew；current CTA/dealer gamma；fresh CFTC gold and ETF flow；China options 10/22 analytics；commodity bid/ask/full chain/positioning；DCE official crosscheck；A-share 10/22 stock engine, adjusted returns, industry, official constituents, forecast revisions and tradability。
- **台账：** TLT 72→78；SOXX上行80→70；IM/IF 67→撤回；AL/NI晨间窗口过期、不重置ID；没有成交回执，所有实际持仓状态均“未提供/未知”。
- **计算检查：** 5个分数逐项未越上限且加总通过；CFFEX基差/年化、三张卡情景PnL重算；57天年化、100/1000/20乘数与成本假设均显式；触发和放弃价可达性检查通过。
- **语义检查：** AND/先后/持续时间、禁止追价、独立失效与止损、TP/时间退出、单笔与主题上限均保留。未解项为实时报价、Greeks、用户成交/持仓、截点后触发与CI；因此没有候选被标为立即可执行。

风险预算：试仓NAV 0.25%—0.75%，确认0.75%—1.50%，同一高确信主题合计≤2.5%—3.0%。保证金不是风险预算；期货止损不封顶；股票、商品、指数和FX的同因子风险需合并。无账户数据，不编净敞口。

## 来源（直达链接；日期与支持结论）

- [Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve)（U.S. Treasury，2026-10-21）：2Y/5Y/10Y/30Y CMT；曲线利差。
- [Daily Treasury Par Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)（U.S. Treasury，2026-10-21）：10Y实际收益率；10Y breakeven计算。
- [Stocks fall as Meta dents AI optimism; French bonds under fire](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-22/)（Reuters，2026-10-22）：全球risk-off；Brent约112；10Y约5.05%；EURUSD/USDJPY；黄金未获避险流。
- [Gold hits over two-month low](https://www.reuters.com/world/india/gold-drops-over-1-oil-rally-reinforces-higher-for-longer-rate-outlook-2026-10-22/)（Reuters，2026-10-22）：现货金4060.37；COMEX金4075.70；FOMC/PCE日期。
- [U.S. Stocks of Crude Oil and Petroleum Products](https://www.eia.gov/dnav/pet/pet_stoc_wstk_dcu_NUS_W.htm)（EIA，2026-10-21）：原油/汽油/馏分油库存变化。
- [VIX Volatility Products](https://www.cboe.com/tradable-products/vix/)（Cboe，2026-10-22）：VIX前收、开盘与变动。
- [ICE BofA US High Yield OAS](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)（FRED/ICE，2026-10-20）：HY OAS 3.33%。
- [Meta Reports Third Quarter 2026 Results](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)（Meta IR，2026-10-21）：Q3收入、Capex、FCF、Q4指引。
- [Tesla Q3 2026 update](https://ir.tesla.com/_flysystem/s3/sec/000162828026066738/tsla-20261021-gen.pdf)（Tesla IR/SEC filing，2026-10-21）：收入、利润率、OCF、Capex、FCF。
- [Lam Research Sep-quarter results](https://investor.lamresearch.com/2026-10-21-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-September-27,-2026)（Lam Research IR，2026-10-21）：收入、毛利率、下一季度指引。
- [CFFEX 2026-10-22 daily futures/option CSV](http://www.cffex.com.cn/sj/hqsj/rtj/202610/22/20261022_1.csv)（CFFEX，2026-10-22）：IH/IF/IC/IM价格、结算、成交、OI与变化。
- [Tencent public index quote endpoint](https://qt.gtimg.cn/q=s_sh000016,s_sh000300,s_sh000905,s_sh000852)（Tencent Finance，2026-10-22）：四现金指数EOD。
- [JCET Q3 2026 results briefing notice](https://big5.sse.com.cn/disclosure/listedinfo/announcement/c/new/2026-10-20/600584_20261020_UJTR.pdf)（SSE/JCET，2026-10-20）：10月23日披露三季报；10月27日业绩说明会。
- [BEA release schedule](https://www.bea.gov/news/schedule)（BEA，2026-10-22）：10月29日GDP与PCE。
- [China-Options radar_latest](https://github.com/farfromexact/China-Options-Engine/blob/ad367e4c58ee8e6de0ffcda60ca22dae4c205491/data/radar_latest.json)（China-Options-Engine，2026-10-20）：HO/IO/MO last-good ATM/RR/BF/PCR/Gamma。
- [China-Commodities last run](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/last_run_status.json)（China-Commodities-Engine，2026-10-22）：商品模块日期、范围和质量。
- [China-Commodities options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/options/quality_latest.json)（China-Commodities-Engine，2026-10-22）：core_v1覆盖、full-chain/positioning/execution限制。
- [China-Commodities futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/crosschecks/futures_latest.json)（China-Commodities-Engine，2026-10-22）：四所价格匹配、DCE HTTP 412。
- [China-Commodities night status](https://github.com/farfromexact/China-Commodities-Engine/blob/b0eaf30aa35cac366066f30fab15f1bcfe7e35ab/data/night_session/last_run_status.json)（China-Commodities-Engine，2026-10-22）：上一合法夜盘日期与语义。
- [China-Stock manifest](https://github.com/farfromexact/China-Stock-Engine/blob/795e149866d7f1eefd1efdaf8fe510cd8f1c750e/data/latest/manifest.json)（China-Stock-Engine，2026-10-21）：全市场价量覆盖、能力与交易日。
- [China-Stock research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/795e149866d7f1eefd1efdaf8fe510cd8f1c750e/data/latest/research_inputs_latest.json)（China-Stock-Engine，2026-10-21）：公司目录、候选与能力缺口。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：TLT 79/83 call spread仅在21:30后TLT>80.20且10Y<5.10%持续30分钟、净借记≤1.55；SC2612仅按724/Brent/曲线双阶段确认；SA701仅跌破926且30分钟不能收复936；SOXX仅30分钟>515并回踩510不破且净借记≤10。  
C. 今天继续观察：AG2612反弹失败空、IH相对防御、长电科技10月23正式财报、Lam强需求能否抵消Meta现金流/Capex压力，以及黄金4060附近能否重新获得避险流。  
D. 今天必须回避或若此前已建仓则有条件退出：回避把10月21旧夜盘当今晚行情、追SC>735或SA<918；撤回未触发的IM多/IF空；晨间AL/NI窗口已过期不重置；黄金3-6月call spread在现货<4200且无IV/报价时回避。
