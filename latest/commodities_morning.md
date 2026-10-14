# 商品期货期权晨间雷达｜2026-10-15

**信息截点：2026-10-15 07:12（北京时间）｜prompt_version：`radar_2026-10-12_stock_v1`**

## 一、今日一句话结论

> **截至本报告时点，无可立即执行的合格新交易。热通胀推动美元、利率与贵金属去风险，但多数空头已在夜盘跳空兑现；最值得等的是AG/SN反抽失败，而非9:00追空。**

当前regime是**高波动、宏观再定价、商品内部显著分化**：贵金属和橡胶最弱，海外原油仍有地缘溢价，但中国SC夜盘反向走弱。研究机会存在，执行均须等09:15—09:45的成交区间和曲线确认；期权没有bid/ask，不能作为当前订单。

## 二、数据质量、时间语义与覆盖

- 中国下一日盘真实交易日T为 **2026-10-15**；最近完整EOD为 **2026-10-14**。统一输入 `requested_date=2026-10-14`、`generated_at=2026-10-15T06:17:24+08:00`。EOD=T-1与Night `trading_date=T`是正常晨间组合。
- 固定读取ref：商品引擎 `5b4044a77d32df95d98e0ff7190d234bcd532326`；归档仓库基准 `16573830a7e8ce13404492822f30bfa2f36a691b`；股票引擎 `b27e99097b2c7d212519864ecfbeea935ade3f77`。
- 核心读取：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/5b4044a77d32df95d98e0ff7190d234bcd532326/data/report_input_latest.json)、[last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/5b4044a77d32df95d98e0ff7190d234bcd532326/data/last_run_status.json)、[Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/5b4044a77d32df95d98e0ff7190d234bcd532326/data/night_session/last_run_status.json)、[radar_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/5b4044a77d32df95d98e0ff7190d234bcd532326/data/radar_latest.json)；按需下钻核心EOD和contract metadata。`night_session/latest.json`有非零blob SHA但连接器正文未返回，按`truncated`而非empty处理。
- Futures：2026-10-14五所806合约、77品种；`full_market_ready=true`、source-date-match=100%、critical errors=0、excluded exchanges=0。5条OHLC占位记录已从排行剔除；负量/负OI、duplicate、invalid OHLC均为0。五所分别SHFE 238、INE 63、DCE 214、CZCE 243、GFEX 48条。
- Market State：20个交易日、exact-contract，不拼接连续主力；部分curve roll品种只作警示。Physical于06:16刷新，18/20 fresh、2 unavailable、0 stale；全部basis缺地区/品质/含税/交割地，为C级且不得计入方向层。仓单与社会库存严格分开。
- External：仓库日频17/22 fresh、5 unavailable，全部`context_only`；07:00层另核实美国CPI、COMEX、Brent/WTI、美元与LME信息。无法完成全口径进口平价，故不称跨市套利。
- Night：`trading_date=2026-10-15`、`night_session_date/session_start_date=2026-10-14`，generated_at=06:00:27；fresh/validated/published均true，407合约、37品种。`coverage_complete=false`，query_error与unresolved各214；missing timestamp/price/quote均0，169条合法outside-window、16条no-night-trade不自动算错。所有重点卡仅用统一层的同一具体合约记录。
- Options：2026-10-14 EOD、14,506合约、41/64品种成功、185个series；局部185 surface-ready、97 positioning-ready、**0 execution-ready**，IV覆盖100%、OI覆盖79.50%、bid/ask覆盖0。整体模块因范围不全标data_fresh=false/published=false，但局部同日ready series可作研究；绝不冒充当前报价或dealer净Gamma。
- Contract Metadata：partial；有效匹配73.45%，乘数/tick/margin/limit约30.15%，last-trading-day 67.49%。DCE参数源失败、GFEX source-date不匹配；前三卡仅列仓库或交易所已核值，动态限幅/保证金未知就不猜。
- Stock联动：[Stock manifest](https://github.com/farfromexact/China-Stock-Engine/blob/b27e99097b2c7d212519864ecfbeea935ade3f77/data/latest/manifest.json) 的trade_date=2026-10-13，落后于最新股票EOD；日价量ready，但复权、5D/20D、RV/ADT、行业与执行检查未就绪。紫金矿业的矿产金/铜映射仅验证业务暴露，套保、产量、成本、少数股东与实现价约束未量化；因此本期**没有股票交易候选**，直接商品表达更纯粹。

## 三、商品仪表盘（展示12项；全77品种扫描见覆盖核对）

1D/5D为同合约结算收益；曲线为引擎near-next指标，roll标记品种不作强结论；Basis均C级。Night均为当前T已完成阶段，非未来行情。

|板块|品种/具体主力|EOD close/settle；1D/5D|Volume/OI/ΔOI|曲线/实体|Night close；vs close/vs settle；ΔOI|07:00海外/Options|09:00信号|
|---|---|---|---|---|---|---|---|
|贵金属|AG2612|14289/14430；-1.76%/-3.34%|311,695/289,589/+5,314|near-next +0.42%、z=+1.73；实体缺|13523；-5.36%/-6.29%；+13,230，02:30 fresh|COMEX银55.55、-6.10%；ATM IV34.63，S/P/X=是/是/否|低开已定价；不追，等30分钟反抽|
|有色|SN2611|377490/385910；-2.85%/-6.21%|161,357/37,512/+4,743|near-next -0.20%、z=-1.69，曲线混合|372820；-1.24%/-3.39%；+188，01:00 fresh|LME锡精确收盘未核；ATM IV31.60，S/P/X=是/是/否|偏低开；等375k上方反抽|
|能源|SC2612|742.4/746.5；+1.98%/+12.07%|75,361/31,641/+4,605|backwardation指标+1.30%、z=-1.77；进口平价不可用|729.5；-1.74%/-2.28%；-451，02:30 fresh|Brent106.06、+0.35%，WTI95.09、+1.01%；IV56.30，S/P/X=是/是/否|内外冲突；等45分钟，不做首跳|
|化工|SA701|944/954；-2.15%/-5.26%|1,210,981/1,377,631/+1,781|曲线0、z=+2.01；仓单3,582、日增382|929；-1.59%/-2.62%；+16,456，23:00 fresh|ATM IV23.78，S/P/X=是/是/否|低开；反抽940—950失败才看空|
|橡胶|NR2612|17110/17230；-1.71%/+1.35%|118,036/81,020/+130|曲线+0.35%，roll，z不可用|16625；-2.83%/-3.51%；-2,209，23:00 fresh|海外橡胶精确锚缺；IV29.54，S/P/X=是/是/否|弱开但不追；等30分钟|
|橡胶|RU2701|20065/20215；-1.46%/+2.56%|546,053/163,185/-9,626|曲线-1.39%、z=-2.42，roll|19640；-2.12%/-2.84%；-5,716，23:00 fresh|海外橡胶精确锚缺；IV27.65，S/P/X=是/是/否|弱开，需OI企稳再评估|
|有色|CU2611|111080/111010；+0.10%/+1.31%|70,993/196,764/+1,054|曲线+0.54%、z=-0.09；C级basis|110110；-0.87%/-0.81%；-2,076，01:00 fresh|LME铜约14436仓库EOD，美元走强；IV13.34，S/P/X=是/是/否|偏低开；等LME/沪铜同向15分钟|
|油脂饲料|RM701|2407/2393；+0.63%/+2.62%|792,236/748,429/+46,266|曲线-1.55%、z=-1.09；仓单7,130不变|2366；-1.70%/-1.13%；-15,699，23:00 fresh|Options失败，无执行价|前日强势被否；等30分钟|
|油脂|OI701|10466/10459；+0.63%/+2.37%|290,265/373,506/+22,559|backwardation +2.76%、z=+2.02；仓单1,274不变|10390；-0.73%/-0.66%；-5,951，23:00 fresh|Options失败，无执行价|旧多头触发撤销；先看10420能否收复|
|畜牧|LH2701|10425/10565；-1.12%/-6.71%|138,377/179,320/+8,094|contango -3.93%、z=+1.71；实体缺|制度无夜盘|DCE Options缺|09:00后等30分钟，不以无夜盘判错|
|新能源|AO2701|2626/2635；-0.68%/-2.23%|117,484/280,840/+11,587|曲线+1.11%、z=+2.66|2593；-1.26%/-1.59%；+22,662，01:00 fresh|IV15.32，S/P/X=是/是/否|弱开；价跌仓增仅归因线索|
|建材|FG701|856/858；-0.12%/-4.35%|1,010,652/1,600,702/-21,615|曲线+1.74%、z=-1.59；仓单2,885、日增500|849；-0.82%/-1.05%；+31,247，23:00 fresh|IV21.77，S/P/X=是/是/否|弱开但绝对价低，等30分钟|

**双锚分歧**：AG、SN、SA相对settlement跌幅明显大于相对close，说明10月14日日盘close已先弱于settlement；不能把全部相对昨结跌幅都算成昨夜新增信息。另有BU/SP代表合约出现`vs close`与`vs settlement`异号，进一步说明结算锚不适合替代隔夜新增收益。

## 四、相比前序报告的真正变化

1. **美国通胀冲击已落地**：美国9月CPI环比+0.6%、同比+3.7%，核心同比+2.6%；美元指数约升0.5%，10年期美债收益率升向5.3%。贵金属下跌由“事件风险”变为已发生的宏观再定价。[BLS原始发布](https://www.bls.gov/news.release/archives/cpi_10142026.htm)
2. **AG旧条件单未触发且已过期**：前序要求先反抽14250—14400再破14200；本夜AG2612最高仅14000，未进入反抽区，随后收13523。不能假定成交；当前只保留新的反抽失败研究卡，不沿用旧入场。
3. **SN、SA同样跳过旧入场区**：SN夜高378380，未到旧反抽382000—386000；SA夜高946，未到旧950—965。旧条件状态是“未满足、窗口过期”，不是已持仓盈利。
4. **SC出现最重要的跨市场冲突**：10月14日EOD上涨1.98%，但T夜盘相对前收下跌1.74%，同时Brent/WTI收涨。中国SC对海外供应风险呈负信息弹性，说明追海外油价映射的赔率下降；但进口平价未对齐，不能直接做跨市套利。
5. **OI多头逻辑降级**：EOD仍是价涨仓增和backwardation，但夜盘跌0.73%、OI减少5,951；前序多头条件撤销，至少需日盘重新收复10420—10480。
6. **Options仍只研究、不可执行**：最新同日截面可用，但全市场bid/ask覆盖仍为0。AG2612 RR字段出现极端异常值，禁止用其推断偏度；没有因为宏观事件已发生就把旧surface当当前价格。

## 五、产业链地图

|产业链|方向与强弱|EOD→Night/曲线/实体|海外与期权|Stock利润桥|最大缺口/置信度|
|---|---|---|---|---|---|
|贵金属|**最弱**；AG空头趋势但追价赔率差|EOD跌、Night再-5.36%且OI增加；曲线仅部分确认，实体缺|COMEX银-6.10%、金-1.64%；AG IV略高于RV且无盘口|紫金矿业有矿产金/铜暴露，但实现价、产量、套保与成本未量化；股票不是更纯表达|动态参数和现货/仓单缺；中高|
|原油—炼化|EOD最强、Night反转；结构性分歧|SC EOD+1.98%、5D+12.07%，Night-1.74%；backwardation仍在但z偏弱|Brent/WTI收涨；SC IV约56.3接近RV58.4，无vol错价|无足够当期公司证据；不把油价上涨直接等同炼化利润|进口平价、运费税费、裂解和同刻报价缺；中|
|橡胶|Night显著转弱|NR/RU夜跌2.83%/2.12%，OI下降；curve均有roll警告|海外橡胶精确收盘缺，期权不可执行|无已核利润映射|实体库存/海外锚缺；中低|
|纯碱—玻璃|SA弱、FG次弱|SA夜跌1.59%且仓单日增382；FG夜跌0.82%、仓单日增500|局部surface可研究但IV不便宜，无盘口|无足够公司证据|basis均C级，成本/开工/库存链不完整；中|
|油脂饲料—畜牧|RM/OI夜盘否定日盘强势；LH仍弱|RM/OI夜跌且OI下降；LH contango与EOD弱势延续但无夜盘|DCE/CZCE相关Options失败或无执行价|无当期公司证据|实体供需与海外油籽精确锚不足；中低|

未入榜板块：黑色的最明显异常是FG弱而非钢矿链全面破位；新能源AO/PS/LC主要是量仓或波动异常但缺实体确认；软商品CF夜跌0.47%，不足以单独形成方向；EC无夜盘且缺海外同刻运价，本期未发现可执行优势。

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

|排名|idea_id / 方向 / 期限|逻辑/赔率/催化/价曲波/拥挤＝总分|有效支持层；反证/缺失|研究/证据/执行|
|---|---|---|---|---|
|1|`COM-M-AG2612-CPI-BREAK-SHORT-20261014`；条件空；1—3D|19/16/17/13/9＝**74**|①价量OI、②曲线部分、④外盘宏观；③缺、⑤异常且无报价；跳空已消耗赔率|存在待验证优势/部分/等待09:30反抽|
|2|`COM-E-SN2611-TWO-STAGE-SHORT-20261014`；条件空；1—3D|18/15/13/12/11＝**69**|①价格OI、⑤put-skew研究信号；②混合、③④不足；已连续两阶段下跌|存在待验证优势/部分/等待触发|
|3|`COM-M-SC2612-EXTERNAL-DIVERGENCE-SHORT-20261015`；条件空；1—2D|17/14/14/12/11＝**68**|①夜盘反转、②curve弱化、④内外负弹性；③缺、⑤无执行；跨市口径不齐|存在待验证优势/部分/等待45分钟|
|4|`COM-E-SA701-DAY-FAILURE-SHORT-20261014`；条件空；1—4D|17/16/12/12/10＝**67**|①价仓、②contango/仓单；③④缺，⑤call skew反对追空|存在待验证优势/部分/等待反抽|
|5|`COM-E-LH2701-WEAK-CURVE-SHORT-20261013`；条件空；2—5D|17/15/12/12/10＝**66**|①EOD价仓、②contango；③④⑤缺，DCE参数缺、无夜盘|存在待验证优势/部分/等09:30|

无80+高优先级，也没有立即新仓。SC虽有三层方向线索，进口平价、动态参数和执行价不足使其仍低于70；支持层数只是评分上限条件，不是加分器。

## 七、前三名研究/交易卡

### 卡1：AG2612反抽失败空（74，条件卡）

- **事实**：EOD O/H/L/C=14644/14662/14203/14289，settle=14430；Night O/H/L/C=14000/14000/13480/13523，vs close=-5.36%、vs settle=-6.29%、Night ΔOI=+13,230。COMEX银10月14日结算55.55美元/盎司、-6.10%，美国CPI高于预期。[贵金属收盘](https://www.wsj.com/finance/commodities-futures/gold-steady-ahead-of-u-s-inflation-data-5b71987b)
- **市场定价/分歧**：市场已计入热通胀、美元和收益率上升；我们的分歧仅是若开盘反抽不能收复夜盘中段，二次去杠杆仍可能延续。最强竞争解释是夜盘已完成主要价格发现，9:00继续追空只是在卖波动低点。
- **表达**：只用AG2612期货条件单研究；期权AG2612/2026-11-24 ATM IV34.63、surface/positioning ready但execution=false，RR极值异常，暂不列具体腿和权利金。股票不是更优表达。
- **入场/分批**：09:00首跳不追。09:15—09:45若反抽13650—13850失败，随后15分钟收盘再破13480，先1/2风险；跌破13380且OI未骤降再加1/2。好/中/坏成交=13800/13600/<13300；坏成交放弃。价位来自Night high/low与波动尺度，不是已验证信号。
- **止损/失效/退出**：计划止损14050；30分钟收上14100且COMEX银重返57.2上方则逻辑失效。TP1=13000减半，TP2=12500；10月15日14:30无延续退出。期货最大损失不封顶，gap可越过止损。
- **参数与压力**：上期所核实标准乘数15千克/手、tick 1元/千克、tick value 15元；13523对应名义约202,845元/手。[SHFE银合约](https://www.shfe.com.cn/eng/Market/Futures/Metal/ag_f/) 仓库只确认last trading day=2026-12-15，当前动态margin/limit未确认。若仅作“20%临时限幅仍在”的压力情景，一板/两板约43,290/86,580元/手；这不是已核当前参数。临近12月前主动滚动，避免实物交割。
- **风险预算**：计划风险NAV 0.25%—0.50%；与SN及任何贵金属期权合并计同因子。

### 卡2：SN2611反抽失败空（69，条件卡）

- **事实**：EOD O/H/L/C=394530/395060/375500/377490，settle=385910；Night O/H/L/C=374990/378380/371200/372820，vs close=-1.24%、vs settle=-3.39%、Night ΔOI=+188。旧反抽区未触及，旧卡未成交。
- **定价/反证**：价格已反映连续两阶段下跌；night新增跌幅小于相对settlement跌幅，边际弹性下降。near-next与主力跨月方向混合，LME锡精确终值未核，是主要反证。
- **表达/入场**：SN2611期货。09:15后若反抽375000—379000失败，再以15分钟收盘跌破371000试1/2；破369500并且量能扩大再加。好/中/坏=378000/374000/<368000；坏成交放弃。
- **止损/退出**：计划止损382000；30分钟收上383500且曲线转为明显backwardation则失效。TP1=365000、TP2=352000；10月15日收盘无延续退出。最大损失不封顶。
- **期权/参数**：SN2611期权到期2026-10-26，ATM 385000、IV31.60 vs RV20 26.03，RR25=-5.76、BF25=1.31；无bid/ask，裸put面临高IV与时间损耗。上期所标准乘数1吨/手、tick10元/吨、tick value10元；last trading day=2026-11-16。[SHFE锡合约](https://www.shfe.com.cn/eng/Market/Futures/Metal/sn_f/ContractText/) 当前动态margin/limit未确认；若仅以先前12%情景，一板/两板约46,309/92,618元/手，不视为已核参数。
- **风险预算**：NAV 0.25%—0.50%，与AG合并；因相关性可能在美元冲击下升高，不把分品种当分散化。

### 卡3：SC2612内外分歧空（68，研究卡）

- **事实**：EOD O/H/L/C=726.7/760.8/726.7/742.4，settle=746.5；Night O/H/L/C=752.0/752.4/725.3/729.5，vs close=-1.74%、vs settle=-2.28%、Night ΔOI=-451。同期Brent/WTI收涨至106.06/95.09美元/桶；海外供应风险没有映射成SC强势。[Reuters油价](https://www.reuters.com/business/energy/oil-prices-climb-traders-weigh-saudi-supply-risk-russian-diesel-flow-2026-10-14/)
- **推断/竞争解释**：负信息弹性可能表示国内需求、人民币或进口结构更弱；也可能只是合约品质、税费、时间差和跨市basis变化。因import parity未对齐，本卡不是套利，只是方向研究。
- **表达/入场**：SC2612期货，09:00不追。Brent仍≥105.5而SC在09:30前反抽736—744失败，且15分钟收盘跌破725，才试1/2；好/中/坏=740/730/<718。坏成交放弃。
- **止损/退出**：计划止损752.5；30分钟收上756且Brent突破108、backwardation扩大则失效。TP1=715、TP2=700；10月16日10:15仍无相对弱势则退出。
- **参数/压力**：INE标准乘数1,000桶/手、tick0.1元/桶、tick value100元；729.5对应名义729,500元/手，单手风险很大。[INE原油合约](https://tsite.shfe.com.cn/eng/market/futures/energy/sc/contract/) 仓库last trading day=2026-11-30；当前动态margin/limit未确认。仅按合约文本4%基础限幅作压力情景，一板/两板约29,860/59,720元/手，实际临时参数可能更高。11月前滚动并避开交割。
- **风险预算**：只有账户能在单手下把计划风险控制于NAV 0.25%—0.50%时才有资格；否则直接放弃，不用更远止损迁就合约尺寸。

## 八、商品期权专项

- **样本口径**：2026-10-14 EOD局部surface；185个series surface-ready，97 positioning-ready，0 execution-ready。夜盘后标的moneyness已改变，旧ATM不是当前ATM。
- **AG**：ATM IV34.63 vs RV20 31.13，事件前并不显著便宜；RR/BF出现经济上异常极值，不计方向证据。若日盘报价恢复，只研究有限损失put spread，最大净支出须≤NAV 0.50%，但本报不编strike、权利金或Greeks。
- **SN**：ATM IV31.60 vs RV20 26.03、到期10月26日；负RR显示下行保护需求的研究线索，但高IV和短theta反对裸买put。
- **SC**：ATM IV56.30 vs RV20 58.38，未显示清晰IV-RV错价；地缘headline会放大vega/gap，期货也因合约大而不适合小账户。
- **SA/NR/RU/AO/FG**：局部surface可用但全无bid/ask；只能比较方向和事件凸性。禁止做“高IV自动卖波动”、禁止推dealer净Gamma。
- **Vol RV**：可研究AG短前端/长后端波动或SN期限结构，但没有同时刻可成交报价、保证金和vega，暂不构造订单。

## 九、9:00开盘风险地图

|重点|Previous China EOD|Current T Night|07:00 Overseas|开盘预案|
|---|---|---|---|---|
|AG|EOD已跌1.76%、OI增|再跌5.36%，夜高即开盘14000，主要信息已定价|COMEX银-6.10%、美元与收益率升|大幅低开；绝不首跳追，等30分钟反抽13650—13850及COMEX同步|
|SN|EOD跌2.85%、量仓z高|再跌1.24%，相对settle跌3.39%，边际弹性较AG弱|LME锡精确锚缺|低开；等15—30分钟，只有反抽失败再破371k才空|
|SC|EOD涨1.98%、5D+12.07%|反跌1.74%，已否定部分日盘强势|Brent/WTI上涨，内外冲突|可能低开；等45分钟，看725、backwardation和Brent是否仍强|
|SA/FG|EOD弱、仓单增加|分别-1.59%/-0.82%|无一一海外锚|偏低开；等30分钟，关注价跌仓增是否延续与contango|
|NR/RU|EOD已弱|再跌2.83%/2.12%，OI下降|海外橡胶精确收盘缺|低开；等30分钟，OI继续降可能是去杠杆而非新趋势确认|
|RM/OI|EOD偏强|夜盘-1.70%/-0.73%，均减仓|海外油籽映射不完整|旧多头信号被削弱；等30分钟收复2385/10420再评估|
|LH|EOD跌1.12%、contango|制度无夜盘|无可执行海外锚|09:00日盘后等30分钟；不以缺Night判错|

人民币/美元：DXY在CPI后约升0.5%，是贵金属和有色的逆风；USD/CNH公开代理约6.70附近、变化有限，人民币不是当前最强独立驱动。金属若09:00跌幅显著小于外盘，说明夜盘已过度定价；若反弹无量且OI继续增，才支持延续空。

## 十、未来24小时/7天事件、覆盖核对与台账

### 事件日历（北京时间）

- **10月15日20:30**：美国9月PPI与零售销售。PPI和消费若再偏热，将延长贵金属/有色的负Delta冲击；不在数据前裸卖短vega。[BLS PPI日历](https://www.bls.gov/schedule/2026/10_sched_list.htm) [美国零售日历](https://www.census.gov/economic-indicators/calendar-listview.html)
- **10月16日00:00与02:00**：EIA因假日延后发布周度石油统计的两批表。SC/FU/LU风险以有限仓位或等待数据后15分钟处理，不用单边止损冒充有限损失。[EIA官方安排](https://www.eia.gov/petroleum/supply/weekly/)
- **10月17日03:30**：CFTC周度COT（报告日10月16日、数据通常截至周二），用于拥挤度背景，不解释中国会员身份。[CFTC日历](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **未来7日**：10月WASDE已于10月9日发布，下一份不在本周；持续监测美国/南美天气、海湾航运与沙特设施、矿山/冶炼检修及中国交易所临时参数。未核实到重点公司在未来24小时有决定性披露，Stock不构成新催化。

### 覆盖核对

|板块|应覆盖|实际取得且分析|数据不足|不适用/低流动性说明|
|---|---:|---:|---|---|
|黑色建材|9|9|Physical多为C级；部分仓单源失败|无；FG为板块最弱异常|
|有色贵金属|13|13|海外锡/部分LME实时、SHFE仓单、动态参数不足|无；AG/SN/AO为重点|
|能源化工|21|21|进口平价、裂解、部分仓单及Options执行不足|无；SC/SA/FG重点|
|新能源|3+GFEX新增|LC/SI/PS及PD/PT共5|实体、执行报价不足|PD/PT为动态新增，仍纳入|
|农产品油脂饲料畜牧|19|19|DCE Options、实体供需及海外映射不足|无；LH无夜盘为制度事实|
|航运|1|1|实时运价/海外同刻锚不足|EC无夜盘|
|动态/历史品种|14|14|JR/PM/RI/WH/ZC等出现占位或低活跃数据|不进入排行，但未从扫描删除|

固定63个代码全部在77品种统一层出现；额外扫描JR、PL、PM、RI、RS、WH、ZC、BZ、LG、RR、PD、PT、OP、WR。策略覆盖方向、跨期、曲线、跨品种/跨市场、产业链RV和波动率；因高质量basis、同期进口平价和可执行期权报价不足，本期没有把不可比价差写成套利。

### 旧观点台账与输入缺口

- `COM-M-AG2612-CPI-BREAK-SHORT-20261014`：首次提出10月14日晚；旧反抽区未触及，未成交，当前改为更低的新条件，原因=新宏观事实+价格跳空。
- `COM-E-SN2611-TWO-STAGE-SHORT-20261014`：旧反抽区未触及，未成交；保留idea_id并下调赔率，原因=价格变化。
- `COM-E-SA701-DAY-FAILURE-SHORT-20261014`：旧反抽区未触及，未成交；保留观察，原因=价格跳空与仓单新增。
- `COM-M-OI701-CURVE-LONG-20261014`：夜盘跌破旧确认区，状态改为deactivated；若此前并无成交反馈，不假定持仓。重新收复10420—10480前不恢复。
- `COM-E-LH2701-WEAK-CURVE-SHORT-20261013`：维持研究观察，下一真实窗口09:00，09:30后确认。

关键缺口：Night明细文件truncated导致Top3 night near-next双合约曲线无法可靠重算；Options无bid/ask；Physical无A/B basis；DCE合约参数失败；海外锡/橡胶精确终值缺。以上缺口限制对应工具，不抹掉可验证的价格异常。

风险预算：试仓计划风险NAV 0.25%—0.75%，确认0.75%—1.50%，同一主题总预算≤2.5%—3.0%；AG/SN/贵金属期权合并，SC/FU/LU/油股合并。所有期货止损都可能被gap、涨跌停、流动性消失和保证金上调穿透。

### 关键来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/5b4044a77d32df95d98e0ff7190d234bcd532326/data/report_input_latest.json)
- [2026-10-14商品晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/16573830a7e8ce13404492822f30bfa2f36a691b/reports/2026/10/2026-10-14_commodities_evening.md)
- [美国9月CPI原始发布](https://www.bls.gov/news.release/archives/cpi_10142026.htm)
- [Reuters 10月14日原油收盘](https://www.reuters.com/business/energy/oil-prices-climb-traders-weigh-saudi-supply-risk-russian-diesel-flow-2026-10-14/)
- [Reuters 10月14日黄金与美元](https://www.reuters.com/world/india/gold-prices-hold-firm-ahead-us-inflation-data-2026-10-14/)
- [Stock商品暴露映射](https://github.com/farfromexact/China-Stock-Engine/blob/b27e99097b2c7d212519864ecfbeea935ade3f77/config/company_commodity_exposures.json)

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：AG2612反抽13650—13850失败后再破13480；SN2611反抽375000—379000失败后再破371000；SC2612在Brent仍强时反抽736—744失败并破725。
C. 今天继续观察：SA701、LH2701、NR2612/RU2701、RM701/OI701的09:30量仓与曲线确认；所有期权等待真实bid/ask。
D. 今天必须回避或有条件退出：回避9:00追空AG/SN/橡胶、回避把外盘油涨直接等同SC高开；旧AG/SN/SA条件单未触发且已过期，OI旧多头条件撤销。
