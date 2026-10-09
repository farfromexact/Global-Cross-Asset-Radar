# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-10｜生成时间：07:12 BJT｜信息截点：07:05 BJT｜prompt_version：radar_2026-09-06_coverage_v1**

> **今天的商品市场究竟有没有值得冒险的机会？截至本报告时点，无可立即执行的合格新交易。**

## 一、今日一句话结论

中国周末休市；白银、甲醇和橡胶存在周一条件机会，但具体夜盘合约数据及期权买卖价缺失，必须等待10月12日09:15—09:45确认。

## 二、数据质量与覆盖

- **时间语义**：最近完整中国EOD为2026-10-09；周五21:00开始的连续交易归属下一中国交易日2026-10-12。2026-10-10为周六，无09:00中国日盘；下一实际窗口是2026-10-12 09:00 BJT。
- **统一输入**：China-Commodities-Engine `data/report_input_latest.json`，requested_date=2026-10-09，generated_at=2026-10-09 19:12:02 BJT，schema_version=2。
- **核心期货**：五所齐全，806个合约、77个品种、72个达到引擎分析条件；source_date_match_pct=100%，full_market_ready=true，critical errors=0，unknown/duplicate/invalid OHLC/negative volume or OI均为0；5条OHLC占位记录已排除。合约元数据48条沿用，仓单5条沿用。
- **Market State**：2026-10-09，同合约1D/3D/5D/20D、RV20、量仓z-score和近—次月曲线可用；roll flag单独披露，未拼接主力。
- **Physical**：20个目标中18个按原生频率有效，SC/LU缺失；现货映射普遍为C级、缺交割地/品质等字段，只作context，不进入方向分数；仓单不等于社会库存。
- **External**：仓库17/22序列有效但均为context_only；本报告另补10月9日欧美收盘。跨市场映射不满足币种、品质、税费、运费和exact-contract全口径，不称套利。
- **Night Session**：模块状态仍停在trading_date=2026-10-08、night_session_date=2026-10-07、generated_at=2026-10-08 07:56:58；data_fresh=false、validation_passed=false、published=false、coverage_complete=false、contract_count=0、outside_window=592、query_error/unresolved=214。该快照与本期周五夜盘无关。读取 `data/night_session/latest.json` 时工具返回截断，记为truncated而非empty。公开来源仅有主力品种涨跌，无法核实具体合约OHLC、相对前收/前结算双锚、ΔOI及夜盘曲线；night_session_fallback=true且仅partial。
- **Options**：2026-10-09共14,074条、185个series；181个surface-ready、41个positioning-ready、0个execution-ready；IV覆盖98.78%、OI覆盖69.36%、bid/ask覆盖0。DCE期权因权限拒绝缺失；TA等7个品种出现日期错配。曲面研究可用不等于可成交。
- **Contract metadata**：有效合约匹配73.45%，乘数/最小变动/保证金/涨跌停覆盖30.15%，夜盘时段字段覆盖0；前三卡只在仓库明确处给参数，其余标“未确认”。
- **读取状态**：report_input=ok；root status=ok；radar=ok；night status=stale/invalid；night latest=truncated；options=partial；web overseas=ok。
- **归档前序**：最近同版为2026-10-09晨报；最近同类报告为2026-10-09晚报。未使用截点后的报告。

## 三、商品仪表盘（展示12项；全市场扫描见覆盖核对）

|板块|品种/合约|10/9 close / settle|1D / 5D|量 / 仓 / ΔOI|EOD curve|Physical/basis|周五夜盘（归属10/12）|海外10/9收盘|Options readiness|周一信号|
|---|---|---:|---:|---:|---:|---|---|---|---|---|
|贵金属|AG2612|14717 / 14515|+0.88% / -7.99%|303600 / 290434 / -4332|backwardation 0.54%|缺失|exact-contract缺失|现货银60.77，+2.4%；金4194.36，+1.5%|surface Y；position N；execution N|09:30后回踩不破再多|
|化工|MA701|3338 / 3321|+6.04% / +14.83%|1493099 / 761175 / +70427|backwardation 16.08%|C/context|媒体主力+2.99%，非close锚|无同质外盘；油价小涨|ATM IV45.66、RV20 35.68、RR25 +2.02；execution N|45分钟，严禁追高|
|橡胶|RU2701|20645 / 20220|+2.89% / n/a|— / — / +17339|contango -3.86%|缺失|媒体主力涨超3%，无exact|SICOM exact更新缺失|ATM IV27.00、RV20 21.93、RR25 +3.22；execution N|30分钟确认|
|橡胶|NR2612|— / —|+0.09% / +3.16%|— / — / +7200|contango -2.16%|缺失|媒体主力涨超4%，无exact|SICOM exact更新缺失|surface可用；execution N|作为RU确认，不单独追|
|黑色|JM2701|1539.5 / 1517.5|+4.30% / n/a|756k附近 / 415009 / +10394|backwardation 3.48%|C/context|媒体主力+3.39%，非exact|无可执行外盘映射|DCE链缺失|等30分钟|
|有色|SN2611|391410 / 391170|-4.23% / n/a|134989 / 34969 / +3724|backwardation 约0.5%|缺失|exact缺失|LME锡52935，+2.9%|ATM IV24.35、RV20 23.65、RR25 -2.89；execution N|旧空头失效，不追空|
|能源|SC2611|734.1 / 741.3|-0.45% / n/a|— / — / -3400|backwardation 3.19%|缺失|exact缺失|Brent104.72、WTI91.85，均小涨|ATM IV60.91、RV20 59.93；execution N|旧空头降级，等30分钟|
|合成胶|BR2612|16710 / 16370|+2.77% / n/a|— / — / +3839|backwardation 2.27%|缺失|媒体主力涨超2%，非exact|无同质外盘|surface Y；execution N|只观察|
|谷物|C2611|— / —|-0.42% / n/a|— / — / -48586|contango -1.38%|C/context|媒体主力涨超1%，与WASDE冲突|USDA玉米结转库存上调|DCE链缺失|开盘冲突，等45分钟|
|油料|M2701|— / —|+0.03% / n/a|— / — / +49030|contango -1.00%|C/context|未取得exact|CBOT大豆收盘小涨，WASDE略偏空|DCE链缺失|不追空，等45分钟|
|新能源|LC2701|117000 / 118740|-3.74% / n/a|— / — / +11960|backwardation 1.22%|缺失|制度上无夜盘|无可靠同质映射|surface Y；execution N|10/12 09:00等45分钟|
|航运|EC2611|2700 / 2749|-5.05% / n/a|— / — / -1776|contango 22.48%|缺失|无夜盘|运价映射缺失|期权不适用/缺失|不抄底|

注：周五夜盘公开百分比通常为“主力相对昨结算”的媒体口径，不能替代exact-contract的return_vs_close_pct；因此本期不计算night ΔOI、夜盘曲线或相对前收新增弹性。

## 四、相比上一交易日真正变化

1. **白银反转获得海外确认**：AG2612日盘收于14717并较结算高202点；其后现货银收涨2.4%、金涨1.5%。这支持“急跌后的反转”而非10月9日晨报的反抽空，但AG具体夜盘仍缺失。
2. **甲醇从强势转为过热**：10/9 close较前收约+6.0%、5D约+14.8%，持仓增加70427，近—次月backwardation扩大到16.08%；媒体夜盘又报+2.99%。支持趋势，但赔率因拥挤和跳空风险下降。
3. **橡胶链扩张但curve反对**：RU日盘+2.89%、ΔOI+17339，媒体夜盘RU超3%/NR超4%；然而RU、NR仍为contango，实体与外盘exact映射缺失，只能列条件候选。
4. **锡空头竞争解释变强**：SN日盘-4.23%且仓增，但LME锡随后+2.9%至52935美元/吨；境内弱势可能是时段错位或短期获利了结，原SN空头不再具备同向外盘确认。
5. **WASDE新增利空主要落在玉米、小麦**：美国玉米单产181.2蒲式耳/英亩、期末库存18.49亿蒲式耳，均高于9月；小麦期末库存7.40亿蒲式耳。报告在中国收盘后发布，周一国内谷物需重新定价，但周五夜盘媒体又报玉米上涨，形成冲突。
6. **原油风险从趋势空转为双向事件**：Brent/WTI小幅收高，飓风导致美国海上产量超过70%停产；这反对直接续空SC，但高价、伊朗谈判和IEA储备释放仍限制追多。

## 五、产业链地图

|产业链|方向/强弱|EOD→Night/海外|curve与实体|期权|最大缺失|置信度|
|---|---|---|---|---|---|---|
|甲醇—烯烃|最强、过热|MA日盘强；媒体夜盘再涨|强backwardation；Physical仅C级|call skew正、IV-RV正|exact-night、现货可交割口径|中高|
|天然橡胶—轮胎|次强、待验证|RU/NR日盘与媒体夜盘同向|contango反证；实体缺失|RU call skew明显|SICOM exact、社会库存/仓单方向|中|
|贵金属|海外反转强|AG日盘反转，海外金银再涨|curve仅轻微支持；实体不适用|AG正RR但无报价|AG夜盘exact、当前权利金|中|
|黑色—焦化|价格强、宏观驱动|JM日盘+媒体夜盘延续|backwardation支持；Physical C级|DCE链缺失|焦煤库存/钢材需求更新|中|
|谷物—饲料|WASDE利空但内外冲突|C日盘微跌，夜盘媒体上涨|contango弱；实体未更新|DCE链缺失|exact夜盘、进口成本全口径|中低|

**当前regime**：节后高波动、化工/橡胶动量与贵金属海外反转并存；周末事件风险高、execution readiness低。最强链为甲醇—烯烃，最弱价格链为航运/锂，但最具新增基本面压力的是玉米—小麦。EOD价格获curve确认的主要是MA/JM/AG；RU的contango构成反证。Night Session无法以exact-contract检验，只能说媒体口径强化MA/RU/JM、但不能量化相对close新增弹性。

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

|排名|idea_id / 方向|逻辑25|赔率25|催化20|价/曲/波15|拥挤技术15|总分|有效支持层|研究判断 / 证据 / 执行|
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
|1|COM-E-AG2612-DAY-REVERSAL-LONG-20261009 / 条件多|18|18|14|11|10|**71**|3：价格、海外、期权|存在待验证优势 / 部分 / 周末休市，等待10/12触发与报价|
|2|COM-M-MA701-MOMENTUM-HOLD-20261009 / 条件多|19|17|14|11|9|**70**|3：价格、curve、期权|存在待验证优势 / 部分 / 等待45分钟回踩|
|3|COM-M-RU2701-SUPPLY-LONG-20261002 / 条件多|18|16|13|12|10|**69**|2：价格、期权；curve反对|存在待验证优势 / 部分 / 等待exact报价|
|4|COM-M-JM2701-MOMENTUM-CONTINUATION-20261010 / 条件多|17|15|13|11|10|**66**|2：价格、curve|存在待验证优势 / 部分 / DCE期权缺失，等30分钟|
|5|COM-M-C2611-WASDE-GAP-WATCH-20261010 / 条件空|16|14|15|8|6|**59**|1：海外基本面；夜盘反对|证据不足 / 不足 / 仅观察周一gap，不下单|

分数复核无超上限。AG/MA有3个独立支持层方可达到70；RU/JM只有2层，封顶69；C只有1个有效方向层，封顶59。风险偏好未加分。

## 七、前三名交易卡

### 1. AG2612 条件多（延续10/9晚报idea_id）

- **市场隐含/分歧**：5D仍跌约8%，市场隐含反转脆弱；我们的分歧是海外金银收盘已经提供独立确认，但不能在周末把确认等同于周一可成交。
- **事实**：EOD close/settle=14717/14515；1D +0.88%，ΔOI=-4332；轻微backwardation 0.54%。现货银+2.4%、金+1.5%。AG夜盘OHLC、return_vs_close、return_vs_settlement和ΔOI均缺失。
- **五层**：价格层支持但OI下降；curve中性略支持；实体不适用；海外支持；期权支持（AG2612、2026-11-24到期、ATM 14500、IV36.39%、RV20 31.44%、RR25 +1.75），positioning/execution均不ready。
- **最佳表达**：AG2612期货条件多。期权只研究同到期30–45Δ看涨价差；未取得bid/ask，不给权利金、净支出或Greeks。
- **入场/分批**：10/12 09:30后，价格守住14650且现货银仍≥60美元；1/2在14650–14800回踩企稳，1/2突破14850后回测不破。
- **止损/失效/退出**：计划止损14380；日收<14250或现货银跌回58.5下方为逻辑失效；TP1=15150、TP2=15700；2个交易日无扩张退出，最长5D。若开盘>15200不追。
- **好/中/坏成交**：14650附近好，14800中，>15200坏并放弃；TP1对应约1.2–1.6R，TP2约2.5R，未计滑点。
- **参数与压力**：仓库仅确认LTD=2026-12-15；乘数、tick、保证金、涨跌停和夜盘时段字段未确认，故不提供虚假压力金额。交割月前至少10个交易日移仓。期货损失不由结构限定。
- **风险预算**：试仓最大损失NAV 0.25%–0.50%；金银同因子合并计入主题风险。
- **最坏情景/放弃**：周末美元/实际利率急升造成低开并穿14380；exact-night无法补齐、参数未核实或首30分钟价格—OI明显背离则放弃。

### 2. MA701 条件多（延续10/9晨报idea_id）

- **市场隐含/分歧**：市场已计入强势供需/成本，5D上涨14.83%且曲线极度backwardation；分歧不在方向而在“是否仍有正赔率”。只有回踩承接才有优势。
- **事实**：close/settle=3338/3321，1D +6.04%，volume=1,493,099，OI=761,175，ΔOI=+70,427；近—次月backwardation=16.08%。媒体夜盘主力+2.99%，但非exact-contract且主要是结算锚。
- **五层**：价格支持；curve支持；实体缺失（C级basis不计）；海外中性；期权支持（MA701、2026-12-11到期、ATM3300、IV45.66%、RV20 35.68%、RR25 +2.02、BF25 1.45），execution不ready。
- **最佳表达**：MA701期货条件多；期权仅研究3300/3500附近看涨价差，具体行权价须随10/12标的与报价重定位。
- **入场/分批**：10/12 09:45后回踩3330–3380并重新站上首15分钟VWAP；1/2承接确认，1/2突破3420后回测。
- **止损/失效/退出**：计划止损3270；日收<3250或backwardation明显收窄且价跌仓增为失效；TP1=3460、TP2=3580；2D无扩张退出，最长5D。开盘>3480不追。
- **好/中/坏成交**：3330–3350好，3360–3400中，>3480坏；以3350入场/3270止损估算，TP1约1.4R、TP2约2.9R。
- **参数**：乘数10吨/手，tick 1元/吨，tick value 10元，EOD名义本金约33,380元；保证金基准7%约2,337元；涨跌停6%；LTD=2027-01-14。单个涨停简单压力约2,003元/手，两个连续涨停简单线性约4,006元/手，未含保证金上调/跳空。
- **交割/移仓**：非产业客户不进入交割月；距LTD至少10个交易日滚动。期货最大损失不有限。
- **最坏情景/放弃**：政策/现货证伪导致高位踩踏，或夜盘媒体涨幅主要来自结算锚而相对前收无增量；exact报价缺失、首45分钟量价不确认即放弃。

### 3. RU2701 条件多（研究卡，未满足正式执行）

- **市场隐含/分歧**：价格与媒体夜盘隐含供应风险，但RU/NR contango暗示现货紧张尚未被曲线确认。我们的分歧只是“值得验证”，不是已经错价。
- **事实**：RU2701 close/settle=20645/20220，1D +2.89%，ΔOI=+17,339；curve=-3.86% contango。媒体夜盘RU超3%、NR超4%，无exact OHLC/双锚/ΔOI。
- **五层**：价格支持；curve反对；实体缺失；外盘exact缺失；期权支持（RU2701、2026-12-25到期、ATM20250、IV27.00%、RV20 21.93%、RR25 +3.22），execution不ready。
- **最佳表达**：RU2701期货条件多；NR2612只作确认，不构造未定义篮子。期权仅研究看涨价差。
- **入场/分批**：10/12 09:30后守住20500，且RU强于NR并出现contango收窄；1/2在20550–20700，1/2突破20900回测不破。
- **止损/失效/退出**：计划止损20150；日收<19900或contango进一步扩大为失效；TP1=21200、TP2=21800；3D无扩张退出，最长10D。开盘>21200不追。
- **参数与压力**：仓库仅确认LTD=2027-01-15；乘数、tick、保证金、涨跌停、夜盘时段未确认，不给虚假压力金额。非产业客户在交割月前滚动。期货最大损失不有限。
- **风险预算**：NAV 0.25%试仓上限；RU/NR/BR视为同一橡胶因子合并。
- **最坏情景/放弃**：海外橡胶低开、库存上升或contango扩大造成冲高回落；没有exact夜盘、SICOM更新或参数确认则不执行。

## 八、商品期权专项

- **截面**：最新有效T日=2026-10-09；本期周末没有新中国期权截面。所有series执行前必须重取10/12当前bid/ask。
- **Readiness**：chain 39/64产品成功；surface 181/185 series；positioning 41/185；execution 0/185。DCE全链受权限拒绝；bid/ask覆盖0；dealer_gamma_direction_known=false。
- **IV-RV**：MA IV-RV约+9.98个百分点、RU约+5.07、AG约+4.95、SN约+0.70、SC约+0.98。正差只说明隐含波动高于历史波动，不单独证明期权贵或便宜。
- **Skew/event convexity**：MA、RU、AG的RR25为正，偏向call需求；SN RR25为负。WASDE已发布，不应再为已过去事件支付事件波动；周末飓风/地缘仍给能源Vega，但SC曲面没有execution readiness。
- **优选结构**：AG、MA、RU均仅研究有限损失call spread；**research only; manual quote and manual confirmation required before execution; no premium quoted**。未取得当前净支出，不给最大亏损金额、Greeks或盈亏平衡点。
- **回避**：DCE期权、TA日期错配series、临近到期且moneyness因夜盘变化失真的旧截面、所有无双边报价结构。

## 九、10月12日09:00开盘风险地图

三层必须分开：

1. **Previous China EOD**：2026-10-09 15:00后完整EOD；
2. **Current Trading Day Night Session**：2026-10-09 21:00开始、归属2026-10-12；仓库exact数据缺失，仅有媒体主力摘要；
3. **07:00 Overseas**：2026-10-09欧美最终收盘；周末之后还会有新的事件/外汇变化，周一开盘前需再刷新。

|品种|EOD|周五夜盘/海外|预期|追价？|等待|首要确认|
|---|---|---|---|---|---|---|
|AG|日盘反转|海外金银显著上行；AG exact缺失|偏高开|否|30分钟|银价≥60、AG守14650、OI|
|MA|强涨+强backwardation|媒体夜盘+2.99%|高开风险|绝不首跳|45分钟|相对前收真实涨幅、VWAP、curve|
|RU/NR|日盘强、curve contango|媒体夜盘RU>3%/NR>4%|高开|否|30分钟|contango是否收窄、SICOM、OI|
|JM|日盘+4.3%|媒体夜盘+3.39%|高开|否|30分钟|钢材成交、焦化利润、backwardation|
|C/M|EOD平弱|WASDE偏空但C夜盘媒体上涨|冲突/易震荡|否|45分钟|CBOT周末后价格、人民币、进口成本|
|SN|日盘急跌|LME锡+2.9%|可能修复高开|不空首跳|30分钟|沪伦方向、390000附近承接|
|SC|日盘小跌|Brent/WTI小涨、飓风停产|偏高开但双向|否|30分钟|海外周末gap、人民币、curve|
|LC/EC|日盘弱|无夜盘|低/平开|否|45分钟|首小时OI、政策/运价|

如果周末出现新的地缘、飓风路径或政策信息，上表只作历史重建，周一08:45必须更新；任何已越过的触发位不作为追价条件。

## 十、未来24h / 7d事件

|北京时间|事件|涉及|处理|
|---|---|---|---|
|周末持续|飓风Isaias与美国海上产量恢复进度|SC/FU/BU/LU、油价|能源Delta降低；只有有限损失结构可隔周末，但当前报价缺失|
|10/12 09:00|中国商品下一实际日盘|全品种|首跳不追；AG/RU等30分钟，MA/C等45分钟|
|10/14 16:00左右|IEA 10月Oil Market Report（10:00 Paris）|原油/炼化|报告前降低裸Delta；SC优先有限凸性|
|10/15 24:00（即10/16 00:00）|EIA周度石油状态报告|原油/成品油|避免在数据前扩大线性仓|
|10/16 03:30|CFTC周度持仓|COMEX/NYMEX/农产品|只作拥挤度，不能当方向身份|
|未来一周|美国CPI及利率路径（日期需周一复核）|金银、美元、实际利率|AG仓位与黄金同因子合并；若事件前IV跳升则不追Vega|
|未来一周|USDA报告后的天气、出口与收割反馈|C/M/小麦|WASDE后的价格确认优先于静态叙事|

来源：[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)、[IEA OMR日程](https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr)、[EIA周报日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[CFTC发布日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)。

## 十一、旧建议台账

|idea_id|首次提出|上次状态|当前状态|变更原因|若此前按条件建立|
|---|---|---|---|---|---|
|COM-E-AG2612-DAY-REVERSAL-LONG-20261009|10/9晚报|等待触发|继续等待，71分|海外金银收盘新增支持；exact夜盘仍缺|不假设成交；周一按新触发重新确认|
|COM-M-MA701-MOMENTUM-HOLD-20261009|10/9晨报|条件多，72分|70分等待回踩|价格更高、赔率下降；curve仍支持|开盘过高不加仓，跌破3270执行计划止损|
|COM-M-RU2701-SUPPLY-LONG-20261002|10/2|观察|69分等待验证|媒体夜盘强化，contango反证未消|无成交反馈，不声称持仓|
|COM-E-SN2611-REVERSAL-SHORT-20261009|10/9晚报|条件空，70分|**撤销/失效**|LME锡+2.9%构成强反证|若此前建立，周一不加仓；不能接受高开修复则退出|
|COM-E-SC2611-RISK-PREMIUM-FADE-20261009|10/9晚报|条件空，68分|降级观察|海外油价收高且飓风停产|若此前建立，周一先减事件敞口；不把止损称最大损失|
|COM-E-BR2612-SUPPLY-SQUEEZE-LONG-20261009|10/9晚报|条件多，67分|继续观察|媒体夜盘同向但exact和参数缺失|不假设成交|

## 十二、覆盖核对

- **应覆盖**：强制63代码、动态新增合格品种及商品期权；方向、curve、基差/仓单、实体、境内外、跨期/跨品种/跨市场RV、波动率/偏度、1–20D周期。
- **实际取数且分析**：77个期货品种，72个满足引擎分析条件；五所均覆盖。按板块：黑色建材9/9、有色贵金属12/12、能源炼化化工全列示代码均进入扫描、新能源LC/SI/PS及GFEX新材料、农产品油脂饲料畜牧、航运软商品均进入扫描。
- **数据不足**：Night exact-contract全市场缺失；Physical SC/LU缺失；DCE期权全链缺失；TA/CJ/PF/PL/PR等期权日期错配；所有期权无bid/ask；多数合约夜盘时段和动态参数缺失；海外import parity不完整。
- **不适用/流动性不足**：JR/PM/RI/WH/ZC成交量和持仓为0，被列为illiquid而非删除；EC/LC等无制度夜盘不判作采集错误。
- **未入榜板块异常**：
  - 黑色建材：JM最强已入榜；FG/SA夜盘转弱且backwardation与价格冲突，不追空。
  - 有色贵金属：SN日盘最弱但LME反向，取消空头；CU周线受供应与中国需求支撑但沪铜EOD不强，观察。
  - 能源炼化：SC受飓风与需求/储备释放双向驱动，无单边优势；BR/FU仅观察。
  - 新能源：LC日盘-3.74%但无夜盘与实体确认，不抄底；SI/PS无跨层异常。
  - 农产品：WASDE使C最值得跟踪；M/Y/OI仍需进口成本与周一开盘确认。
  - 航运软商品：EC弱且contango陡，但运价和持仓确认不足；CF/SR/AP/CJ/PK未发现达到两层证据的新增优势。
- **RV结论**：MA近—次月强backwardation值得跟踪但不直接建跨期；RU/NR contango与价格上涨冲突，是最值得验证的curve RV；境内外套利均不满足全口径，不执行。

## 风险预算与压力测试

单一试仓最大损失NAV 0.25%–0.75%，确认交易0.75%–1.50%，单一高确信主题总风险≤2.5%–3.0%；金银、RU/NR/BR、SC/FU/BU等同因子合并。周末压力必须包含1/2个涨跌停、相关性破裂、夜盘gap、保证金上调、流动性消失、交割挤压、IV跳升/塌陷、人民币急变和海外两天累积波动。当前缺参数/报价时不得用风险预算反推出“可执行”。

## 关键来源

- [China-Commodities-Engine report_input_latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)，源日期2026-10-09：核心期货、Market State、Physical、External、Options和metadata。
- [China-Commodities-Engine Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)，访问2026-10-10：失败/陈旧模块状态。
- [国内商品期货夜盘收盘（第一财经）](https://www.yicai.com/brief/103388344.html)，2026-10-09：主力夜盘涨跌摘要，仅代理。
- [国内部分商品期货夜盘收盘（东方财富）](https://qhweb.eastmoney.com/news/202610093891576432.html)，2026-10-09：RU/NR/BR等夜盘板块摘要，仅代理。
- [Reuters：飓风停产与油价收盘](https://www.reuters.com/business/energy/oil-falls-trump-comments-iran-talks-ease-supply-concerns-2026-10-09/)，2026-10-09。
- [Reuters：金银收盘](https://www.reuters.com/world/india/gold-rises-softer-dollar-easing-yields-fed-outlook-focus-2026-10-09/)，2026-10-09。
- [Reuters转引：LME金属收盘](https://es.marketscreener.com/noticias/cobre-se-dirige-a-alza-semanal-por-riesgos-ligados-a-suministro-minero-y-demanda-china-ce785ddfd08cf524)，2026-10-09。
- [USDA 10月WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)，发布2026-10-09 12:00 ET。
- [USD/CNH历史数据](https://www.investing.com/currencies/usd-cnh-historical-data)，2026-10-09收6.6932、-0.15%；人民币走强对进口商品人民币计价构成轻微逆风。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：无；周末不挂中国期货条件单，10月12日09:30后再验证AG2612、MA701、RU2701。
C. 今天应继续观察的机会：AG反转、MA回踩、RU/NR曲线冲突、JM动量、C2611 WASDE后重定价。
D. 今天必须避免或退出的交易：避免周一首跳追MA/RU/JM，撤销SN2611续空；若此前建立SC空头，先降周末飓风事件敞口。