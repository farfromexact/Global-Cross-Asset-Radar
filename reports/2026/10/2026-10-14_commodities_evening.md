# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-14｜信息截点：19:30 北京时间｜prompt_version：`radar_2026-10-12_stock_v1`**

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易。** 贵金属与部分农化下行动量最清晰，但20:30美国CPI、期权零执行报价及曲线反证使今晚只宜等触发；能源强势更像事件溢价，不宜追首跳。

## 二、数据质量、时间语义与覆盖

- 中国最近完整交易日为 **2026-10-14（T）**；下一正常夜盘自今晚21:00开始，归属 **2026-10-15（T+1）**。上期所公告确认国庆后10月8日起恢复夜盘，本日不是节前停夜盘日。[上期所休市及恢复安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)
- 固定读取 ref：商品引擎 `026e0b7d79c24a884392b21e0cb09d91adfca66d`；归档仓库基准 `4b752760befc0b3302e53290381f30b504851f5f`；股票引擎 `b27e99097b2c7d212519864ecfbeea935ade3f77`。
- 统一输入：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/026e0b7d79c24a884392b21e0cb09d91adfca66d/data/report_input_latest.json) requested_date=2026-10-14，generated_at=19:14:23；核心期货EOD generated_at=19:00:13。
- Futures：五所、806合约、77品种；`full_market_ready=true`、source-date-match=100%、critical errors=0、excluded exchanges=0。5条OHLC占位（JR/PM/RI/WH/ZC等零价低流动性记录）已剔除排行；`official_complete=false`来自附属模块未齐，不否定核心期货闭环。
- Market State：同合约1/3/5/20日、RV20、量仓z值、near-next曲线可用；roll-flag品种不拼接收益。
- Physical：19:13:46生成，18/20在原生频率内fresh、2 unavailable、0 stale；基差均未达到A/B可评分质量。仓单只按仓单解释，不冒充社会库存。
- External：仓库日频17/22 fresh、用途为`context_only`；本报另补15:00—19:30海外报价，不能当作中国已交易的价格。
- Night Session：[状态](https://github.com/farfromexact/China-Commodities-Engine/blob/026e0b7d79c24a884392b21e0cb09d91adfca66d/data/night_session/last_run_status.json) 的 trading_date=2026-10-14、night_session_date=2026-10-13、generated_at=05:59，data_fresh/validation_passed/published均为true；417合约、37品种。它是**今天凌晨前已完成、属于T的连续交易阶段**，绝非今晚21:00未来行情。coverage_complete=false，query_error/unresolved各214；missing timestamp/price/quote均0。`night_session/latest.json`本次连接器返回被截断，按`truncated`处理；重点精确合约仅使用统一层已明确记录。
- Options：2026-10-14共14,506合约、185个series；surface-ready 185、positioning-ready 97、execution-ready **0**；IV覆盖100%、OI覆盖79.50%、bid/ask覆盖0。DCE因安全拒绝跳过且OI抓取失败；任何期权结构均是研究方向，不是当前成交报价，dealer gamma方向未知。
- Contract Metadata：partial；有效匹配73.45%，乘数/tick/margin/limit约30.15%，last-trading-day 67.49%，night/delivery字段近乎空。详卡只给已核参数，缺项不猜。
- Stock联动只读重点商品映射，不做全市场重复选股。股票引擎trade_date=2026-10-13、research_asof=2026-10-14 07:29；报价覆盖约5,561只，但仅原始1D/3D能力可用，5D/20D、复权、RV/ADT、行业和实时执行未就绪。紫金矿业、宝钢股份旧半年报仅作产业利润桥，不构成今天催化或交易候选。

**读取状态**：统一输入、root status、Night status、radar、core futures、contract metadata、前序报告及Stock索引/相关分片均ok；Night明细truncated；DCE options为permission/security error；不存在把工具截断写成源为空的情况。

## 三、商品仪表盘（展示12项；全范围扫描见覆盖核对）

收益均以结算价同合约计算；“夜→日”为T日EOD close / 已完成T夜盘close - 1。`—`表示精确合约或模块不可用，不猜数。

|板块|品种/主力|T日 close/settle；1D/5D|量/OI/ΔOI|曲线、实体|已完成T夜盘；夜→日|15:00后海外/期权|21:00判断|
|---|---|---|---|---|---|---|---|
|贵金属|AG2612|14289/14430；-1.76%/-3.34%|311,695/289,589/+5,314|near-next反向为+0.42%，主力对AG2702贴水0.29%；实体缺|14466，vs close -1.88%，vs settle -1.51%，夜ΔOI+7,149；-1.22%|现货银约58.57美元、-1.5%；AG2612 ATM IV34.63、无报价|CPI后等30分钟，拒绝追低开|
|有色|SN2611|377490/385910；-2.85%/-6.21%|161,357/37,512/+4,743|near-next contango 0.20%，主力对SN2612略升水0.32%，曲线冲突|383250，vs close -3.34%，vs settle -3.52%，夜ΔOI+3,907；-1.50%|海外锡精确价缺；ATM IV31.60、RR25 -5.76、无报价|只等反抽失败，不首跳追空|
|化工|SA701|944/954；-2.15%/-5.26%|1,210,981/1,377,631/+1,781|主力对次月contango 3.15%；仓单3,582、日增382|960，vs close -0.10%，vs settle -1.54%，夜ΔOI+21,786；-1.67%|ATM IV23.78、RR25 +4.14（反证）、无报价|21:30后才看942确认|
|畜牧|LH2701|10425/10565；-1.12%/-6.71%|138,377/179,320/+8,094|LH2611/2701 contango 3.93%；实体缺|制度无夜盘/精确记录不适用|DCE期权缺|下个日盘09:30确认，不是今晚单|
|油脂|OI701|10466/10459；+0.63%/+2.37%|290,265/373,506/+22,559|near-next backwardation 2.76%，仓单1,274不变|10446，vs close +0.45%，vs settle +0.50%，夜ΔOI+5,484；+0.19%|CBOT油籽代理偏弱；期权抓取失败|强弱冲突，等30分钟|
|能源|FU2701|4807/4767；+2.54%/+20.68%|316,469/193,336/+14,384|近月pair backwardation 7.57%，主力跨月受roll/合约错位影响|代表合约为FU2611，不能替FU2701分解|Brent 106.60、+0.9%；期权无报价|事件溢价极高，首跳不追|
|化工|EG2611|5295/5243；+2.28%/+1.35%|1,159,222/269,574/+12,261|near-next backwardation 8.47%|DCE精确夜盘缺|原油强但映射非一一；期权缺|等45分钟验证加工链|
|软商品|AP701|6242/6426；-4.20%/-5.97%|320,355/170,103/+17,915|near-next backwardation9.93%，强烈反对追空|无夜盘|ATM IV37.84，BF25异常，positioning/execution不就绪|不交易，等日盘结构修复|
|新能源|LC2701|100900/102800；-2.54%/-13.48%|339,357/427,300/+4,908|near-next backwardation0.63%；现货C级且仓单旧|无夜盘|ATM IV54.01，无报价|不追空，等日盘30分钟|
|能源|BZ2611|9740/9774；+2.62%/+12.75%|115,814/27,031/-1,016|near-next backwardation6.63%，但涨价减仓|DCE精确夜盘缺|Brent强；期权缺|旧多头触发状态未知，不新追|
|能源|SC2612|742.4/—；+1.98%/+12.07%|75,361/31,641/+4,605|near-next backwardation1.30%，样本仅5日|代表合约SC2611，不能替代|Brent 106.60、WTI 95.79；无执行报价|已部分预交易，等45分钟|
|浆纸|SP2701|4730/4784；-0.42%/-3.00%|330,569/294,269/+41,760|near-next contango0.30%，pair roll flag|4810，vs close +0.04%；夜→日-1.66%|ATM IV14.84、RR25 +4.29、无报价|量仓异常但价格未确认，不做|

## 四、相比前序的真正变化与旧观点处置

1. **AG下跌从夜盘延伸至日盘**：前夜相对close -1.88%，日盘再-1.22%；价格下跌且OI增加只是看空归因线索。海外银截至截点再跌约1.5%，把晨间“条件空”升级为最高研究优先，但20:30 CPI之前不执行。
2. **SN早期异常转为两阶段下跌**：前夜-3.34%、日盘再-1.50%，ΔOI同向增加；近月contango支持但主力次月略backwardation反对，故仍只有部分证据、最高69分以下。
3. **SA的主要弱势发生在日盘**：前夜相对close几乎持平（-0.10%），日盘-1.67%；仓单增加与主力跨月contango支持空头，但期权call skew反对，不能把“多层可用”误算成多层支持。
4. **能源继续强但内部开始分化**：FU2701价涨仓增，SC价涨仓增；LU2612却收5940、结算-0.34%且OI下降。10/13晚报LU多条件（5965）未保持，现按价格变化撤销；旧BZ多条件日内是否触发无分钟路径，状态未知、不假定成交。
5. **晨报OI多得到日盘小幅确认**，夜盘+0.45%后日盘仅+0.19%，边际弹性有限且海外油籽代理偏弱，维持条件观察而非追多。
6. **股票利润桥没有新增公司催化**：紫金H1数据只是历史背景；宝钢H1收入增长而归母净利下降验证成本传导受限，均不优于直接商品工具，未进入统一Top5。

## 五、产业链地图

|链条|方向与强弱|价格/曲线/实体|海外与期权|最大缺失|置信度|
|---|---|---|---|---|---|
|贵金属|最弱之一；AG条件空|夜盘与日盘同向下跌，主力远月contango但near-next相反；无高质量实体|银价同步下跌，美元仅小幅走弱；IV高于RV、无执行报价|CPI结果、当前盘口、有效RR|中高|
|锡及有色|SN弱，其他有色未形成统一方向|价跌仓增；近端曲线和主力曲线冲突|海外锡精确价缺；put skew支持下行但不能成交|LME exact-contract与参数|中|
|能源炼化|FU/SC最强，LU转弱|油系高波动、近端backwardation；实体日频只context|Brent+0.9%，IEA指中馏分紧张；但俄罗斯柴油供应和炼厂利润压缩是反证|跨品种精确裂解价差、当前内盘报价|中|
|纯碱—玻璃|SA弱于FG链|日盘主导下跌，contango与仓单增加；实体只仓单|期权call skew反对空头且无报价|社会库存、现货A/B级基差|中|
|油脂饲料|OI偏强但外盘冲突|价涨仓增、backwardation，仓单不变|海外油籽代理偏弱；DCE期权缺|CBOT精确实时、进口利润全口径|中低|

**公司利润传导**：能源成本上行对钢铁下游并非自动利好。宝钢股份2026H1合并口径收入1,607.31亿元、归母净利45.71亿元，收入同比+6.18%但利润同比-6.30%，仅说明成本/产品结构传导可能受限；这是旧中报验证，不是10月14日新催化。紫金矿业H1金铜敞口方向正确但套保、产量、汇率和估值反应未拆清，直接AG/CU工具更纯粹。

## 六、统一机会排行榜（研究吸引力，不是胜率或仓位）

|排名 / idea_id|方向/期限/工具|逻辑/赔率/催化/价曲波/拥挤|总分|有效支持层；反证|研究/证据/执行|
|---|---|---|---:|---|---|
|1 `COM-M-AG2612-CPI-BREAK-SHORT-20261014`|空AG2612，1—3日，期货；期权仅备选|19/17/17/12/9|74|3层：①价量OI、②主力跨月、④海外银；near-next相反、CPI跳空、期权无报价|待验证优势/部分/等待触发|
|2 `COM-E-SN2611-TWO-STAGE-SHORT-20261014`|空SN2611，1—3日，期货|17/16/13/12/10|68|2层：①价量OI、⑤put skew；主力曲线反向、LME与参数缺|待验证优势/部分/等待触发|
|3 `COM-E-LH2701-WEAK-CURVE-SHORT-20261013`|空LH2701，2—5日，期货|18/16/13/12/9|68|2层：①价量OI、②contango；无Night、DCE期权和实体|待验证优势/部分/下个日盘等待|
|4 `COM-M-OI701-CURVE-LONG-20261014`|多OI701，2—5日，期货|17/16/13/12/9|67|2层：①价量OI、②backwardation；外盘代理偏弱、期权缺|待验证优势/部分/等待触发|
|5 `COM-E-SA701-DAY-FAILURE-SHORT-20261014`|空SA701，1—4日，期货|17/15/13/12/9|66|2层：①价量OI、②曲线/仓单；call skew与低绝对价反对|待验证优势/部分/等待触发|

正式榜无80+，没有满足“证据+触发+当前报价+参数”的立即交易。AP/LC虽跌幅大，但曲线反对且期权执行缺口显著，只列早期异常，不以低分掩盖数据不足。

## 七、前三研究/交易卡

### 卡1：AG2612事件后延续空（74，条件卡）

- **事实**：T日O/H/L/C=14644/14662/14203/14289，settle=14430；前夜O/H/L/C=14644/14662/14355/14466，vs previous close=-1.88%、vs settlement=-1.51%、Night ΔOI=+7,149；日盘follow-through=-1.22%，EOD ΔOI=+5,314。
- **市场可能隐含/我们的分歧**：价格已计入部分贵金属去风险，但若CPI后海外银仍≤58.5且AG不能收复14400，国内日盘的二次下行尚未被证明是终点；竞争解释是大部分信息已在两阶段下跌中完成、CPI可能反向挤仓。
- **五层**：①支持；②主力跨月支持但near-next反对；③缺；④支持；⑤ATM IV34.63对RV20 31.13偏高且execution=false，方向中性、工具反对追买期权。
- **表达/入场**：今晚有夜盘。20:30 CPI后等至至少21:30；AG反抽14250—14400失败且再破14200才卖1手。好/中/坏成交：14350/14230/<13950；坏成交放弃，不用更宽止损补偿追价。
- **止损与退出**：计划止损14530；若30分钟收在14580上且海外银>60.3则逻辑失效。TP1=13800减半，TP2=13450；10月15日10:15无延续退出。线性期货最大损失不封顶，gap可穿越止损。
- **参数/压力**：仓库缺乘数、tick、tick value；官方临时参数显示AG2612限幅20%、一般保证金22%，故无法可靠给现金名义与1/2板金额。[上期所参数公告](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html) last trading day=2026-12-15；临近交割月前滚动，避免交割资格风险。
- **风险预算**：只允许NAV 0.25%—0.50%计划风险；与SN、贵金属期权合并计同因子。

### 卡2：SN2611反抽失败空（68，条件卡）

- **事实**：T日O/H/L/C=394530/395060/375240/377490，settle=385910；前夜O/H/L/C=394530/395060/382000/383250，vs close=-3.34%、vs settle=-3.52%、Night ΔOI=+3,907；day follow-through=-1.50%，EOD ΔOI=+4,743。
- **定价与反证**：两阶段下跌和put skew显示防守，但near-next contango仅0.20%，主力对SN2612反而backwardation0.32%，不能称曲线全面确认；海外锡精确报价缺失是关键反证缺口。
- **表达/入场**：今晚有夜盘；等21:30以后反抽382000—386000失败，再破377000才卖1手。好/中/坏：385000/378000/<370000；低于370000不追。
- **止损/失效/退出**：计划止损390500；30分钟收于392000且曲线扩大为>1% backwardation时失效。TP1=365000、TP2=350000；10月15日收盘前无延续则退。期货最大损失不封顶。
- **期权/参数**：SN2611期权到期2026-10-26，ATM 385000、IV31.60、RR25 -5.76、BF25 1.31；无bid/ask，禁止编权利金。官方当前限幅12%、一般保证金14%；乘数/tick/tick-value在本次元数据未确认，1/2板现金压力不报伪精度。last trading day=2026-11-16。

### 卡3：SA701日盘破位空（66，条件卡）

- **事实**：T日close/settle=944/954，1D=-2.15%，5D=-5.26%，ΔOI=+1,781；前夜close=960、vs close=-0.10%、vs settle=-1.54%、Night ΔOI=+21,786，day follow-through=-1.67%。弱势主要来自日盘。主力对次月contango 3.15%，仓单3,582、日增382。
- **反证**：SA701期权ATM 950、IV23.78对RV20 18.88不便宜，RR25 +4.14为call skew；现货基差仅C级，不能用于套利；绝对价格低增加政策/成本反弹风险。
- **表达/入场**：今晚有夜盘。21:30后若反抽950—965失败，再破942卖1手；好/中/坏=955/944/<920，坏成交放弃。
- **止损/退出**：计划止损978，30分钟收上985且contango明显收窄则失效；TP1=910减半、TP2=875；两交易日无兑现退出。最大损失不封顶。
- **参数/压力**：乘数20吨、tick 1元、tick value 20元；944元名义18,880元/手，按8%最低保证金约1,510元/手（实际经纪商更高）；限幅7%，简单一板压力约1,322元/手、两板约2,643元/手，未含连续复位、gap和保证金上调。last trading day=2027-01-14，远离交割但需在流动性迁移时滚动。

## 八、商品期权专项

- **样本**：2026-10-14 EOD，185个surface-ready series；ATM/RR25/BF25仅对局部surface-ready使用。全市场execution-ready=0，因此本节不能变成订单。
- **AG**：ATM IV34.63 vs RV20 31.13，事件前并不显著便宜；RR字段出现极端值，视作质量异常，不用于偏度方向。
- **SN**：ATM IV31.60 vs RV20 26.03，RR25 -5.76支持下行保护需求，但临近10月26日到期、无盘口；裸买put可能同时承受高IV与时间损耗。
- **SA**：ATM IV23.78 vs RV20 18.88，RR25 +4.14反对追空；更适合等待报价后评估有限损失put spread，而非裸买波动。
- **AP/LC**：IV高（约37.84/54.01）但positioning或execution未就绪；AP BF25异常，不以“高IV”自动做空波动。
- **回避**：所有目标结构bid/ask、净权利金、滑点、Greeks均缺；不推dealer净Gamma，不把旧/无报价surface当当前可成交性。

## 九、21:00夜盘风险地图

|重点|T日EOD|已完成T夜盘（历史）|15:00后海外|下一夜盘预案|
|---|---|---|---|---|
|AG/SN|两者日盘继续下跌|均已先跌，AG/SN夜→日再-1.22%/-1.50%|银约-1.5%；DXY -0.1%，CPI 20:30|倾向低开但事件可反转；不追首跳，等30分钟及外盘同向确认|
|SA|日盘破位、contango|前夜几乎未跌，日盘承担主要价格发现|无一一海外锚|可能弱开；等30分钟，确认942与contango是否同向|
|FU/SC/LU|FU/SC强、LU弱|具体主力不全可比|Brent 106.60（+0.9%）、WTI 95.79（+1.8%）|高开概率偏高但国内已预交易；等45分钟、看近月曲线和LU是否补涨|
|OI|价涨仓增、backwardation|夜盘+0.45%，日盘仅+0.19%|油籽代理偏弱|内外冲突；等30分钟，10480上方才能谈延续|
|LH/AP/LC|日盘弱|制度无夜盘|代理映射有限|今晚不可交易；下一实际窗口10月15日09:00，至少等30分钟|

海外关键事实：19:10左右Brent 106.60美元/桶、+0.9%，WTI 95.79、+1.8%，支撑油系潜在高开，但不代表中国已经交易了该信息。[Reuters油价](https://www.reuters.com/business/energy/oil-prices-climb-traders-weigh-saudi-supply-risk-russian-diesel-flow-2026-10-14/) IEA称9月柴油裂解价差接近95美元/桶、供应紧张可能延续至2027，但2027年全球供应反转为过剩是中期反证。[Reuters/IEA](https://www.reuters.com/business/energy/diesel-shortages-could-persist-well-into-2027-iea-says-2026-10-14/) USD/CNH约6.694、近乎持平，人民币不是今晚主要驱动；DXY小跌也未阻止银下跌。

## 十、未来24小时/7日事件与风险处理

- **10月14日20:30 北京时间**：美国CPI；AG/SN先降Delta，至少等30分钟。若要事件凸性，只能在当前报价核验后用净支出封顶结构。[Reuters贵金属/CPI时间](https://www.reuters.com/world/india/gold-prices-hold-firm-ahead-us-inflation-data-2026-10-14/)
- **10月15日20:30**：美国PPI与零售销售；能源、贵金属与美元敏感，线性仓在数据前减半或设置时间退出。
- **10月16日00:00/02:00**：EIA因假期分阶段发布周度石油报告；SC/FU/LU不在数据前追涨。[EIA官方日程](https://www.eia.gov/petroleum/supply/weekly/)
- **10月17日03:30左右**：CFTC COT通常发布；仅作滞后拥挤背景，不当实时机构方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm)
- **未来7日持续**：霍尔木兹航运、沙特能源设施与俄柴油流向；使用小Delta或有限支出结构，不能把新闻同源转述重复计证据。
- **中国宏观**：9月PPI同比+5.0%、CPI同比+0.9%，工业成本向消费端传导仍弱；对能源化工是宏观背景而非单品种直接因果。[Reuters中国通胀](https://www.reuters.com/world/asia-pacific/chinas-factory-gate-inflation-accelerates-september-2026-10-14/)
- 相关公司未来披露未在本次Stock索引中形成可核实24小时催化；股票已收盘，不列今晚21:00表达。

## 十一、覆盖核对、台账与关键缺口

|板块|应覆盖|实际取数且分析|数据不足/不适用|未入榜最值得跟踪异常|
|---|---|---|---|---|
|黑色建材|I/JM/J/RB/HC/FG/SA/SF/SM|9/9期货EOD与曲线；SA有Night/Options|DCE Night/Options部分缺，高质量实体普遍不足|JM五日仍强但当日价仓同降；FG/SA链中SA日盘更弱|
|有色贵金属|CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG|12/12扫描；AG、SN下钻|重点合约参数不全，海外锡精确价缺|SN两阶段下跌；AG内外同步弱|
|能源化工|SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP|23/23期货初筛；SC/FU/LU/EG/SP下钻|DCE夜盘/期权、裂解全口径不足；PR/SH流动性适用性逐合约受限|FU 5D+20.68%，EG backwardation；SP量仓大增但价弱|
|新能源|LC/SI/PS及GFEX新增|LC/SI/PS扫描|夜盘不适用，LC实体/期权执行不足；新增品种以77产品动态全集核验|LC 20D -28.10%但曲线反对追空|
|农产品畜牧|A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK|19/19 EOD扫描；OI/LH/AP/CJ/JD下钻|DCE Night/Options缺，高质量进口利润/实体不足|AP、CJ跌幅大但AP backwardation；OI曲线强、外盘弱|
|航运及其他|EC|1/1扫描|无夜盘；跨市场运价口径未对齐|无达到榜单门槛的独立异常|

- 应覆盖63个去重代码及动态新增；核心期货实际77个产品全部进入初筛，63个指定代码均有覆盖状态。策略维度已扫描方向、曲线/跨期、跨品种/跨市场映射、期权vol/skew/事件凸性；因basis、import parity和execution报价不合格，没有把它们伪装为可执行套利。
- 旧观点：AG/OI/LH延续同一idea_id；10/13 BZ与晨报FU的盘中触发无可核路径，均标未知且不假定成交；LU多因价格未守5965撤销。没有真实持仓信息，所有“退出”仅适用于若此前确已按条件建立。
- 最关键缺口：全市场期权bid/ask=0、DCE options缺、部分重点合约参数不全、Night明细读取截断、Physical高质量basis为零。这些缺口限制对应工具，不抹掉方向研究。
- 风险预算：试仓计划风险NAV 0.25%—0.75%，确认交易0.75%—1.50%，同因子总风险≤2.5%—3.0%；AG/SN视为同一金属风险簇，SC/FU/LU视为同一油系风险簇。止损不是最大损失；须压力测试1/2板、流动性消失、保证金上调、IV跳升/塌陷、交割挤压及人民币急变。

## 来源与版本

- 商品原始输入：[China-Commodities-Engine report_input](https://github.com/farfromexact/China-Commodities-Engine/blob/026e0b7d79c24a884392b21e0cb09d91adfca66d/data/report_input_latest.json)、[核心期货](https://github.com/farfromexact/China-Commodities-Engine/blob/026e0b7d79c24a884392b21e0cb09d91adfca66d/data/latest.json)、[root status](https://github.com/farfromexact/China-Commodities-Engine/blob/026e0b7d79c24a884392b21e0cb09d91adfca66d/data/last_run_status.json)。
- 前序基准：[2026-10-14晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/4b752760befc0b3302e53290381f30b504851f5f/reports/2026/10/2026-10-14_commodities_morning.md)、[2026-10-13晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/4b752760befc0b3302e53290381f30b504851f5f/reports/2026/10/2026-10-13_commodities_evening.md)。
- Stock背景：[research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/b27e99097b2c7d212519864ecfbeea935ade3f77/data/latest/research_inputs_latest.json)、[商品公司映射](https://github.com/farfromexact/China-Stock-Engine/blob/b27e99097b2c7d212519864ecfbeea935ade3f77/config/company_commodity_exposures.json)。

A. 今晚没有应立即建立的新仓位。
B. 今晚仅应挂条件的候选：CPI后AG2612反抽失败并破14200；SN2611反抽失败并破377000；SA701 21:30后破942。
C. 今晚继续观察：LH2701/OI701的下个日盘确认，SC—FU—LU事件溢价与曲线，AP/LC超跌但曲线反证。
D. 今晚必须回避或有条件退出：回避21:00首跳追油、无bid/ask期权及低开追空；若此前按条件建立LU多而未守5965，则退出。
