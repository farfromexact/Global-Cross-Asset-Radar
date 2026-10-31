# 商品期货期权晨间雷达｜2026-11-01

> 生成时间：2026-11-01T06:59:34+08:00｜信息截点：2026-11-01T06:59:34+08:00｜周末模式｜研究与决策支持，不下单，不假定持仓或成交。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；周日休市，周一只等SC回踩确认与AG反抽失败，BU因活跃布油未达阈值继续等待。**

已研究但优势不足：黑色、有色与大部分农产品没有三层方向证据；研究机会存在但等待条件/报价：SC、AG、BU；数据不足不能判断：期权执行价差、AG精确夜盘、全市场A/B基差、部分合约参数。最有价值的三个待验证观察是：OPEC正式结果、周一09:15 SC/BU近远月曲线、AG反抽时海外银是否仍在49.5以下。下一真实窗口为**2026-11-02 09:00中国日盘**；11月1日周日没有中国夜盘。

## 2. 数据质量与覆盖

|模块|目标/实际|源日期与生成|可用性|关键限制|
|---|---:|---|---|---|
|Futures|806合约/77品种/五所|EOD 2026-10-30；status生成11-01 06:05|available/published/analytically ready|full_market_ready=true、source-date match 100%，但official_complete=false；4个OHLC占位隔离|
|Market State|77品种、20会话窗口|2026-10-30|1/3/5/20D与RV可用|不能把价仓象限解释成新多/新空|
|Physical|20目标、18 fresh；A/B可计分基差0|原生周/月频|局部背景|5条仓单carry；非今日催化；无合格套利基差|
|External|22目标、17 fresh|最新完整海外EOD至10-30|context only|周日无07:00实时会话；跨境品质/税运费/汇率不齐|
|Night|412/806，51.1166%|10-30晚—10-31凌晨，归属11-02|validated/published但不complete|168制度外、12无成交、214 query_error/unresolved；raw latest为空；公共fallback非官方收盘|
|Options|45/64品种、1000合约、45 series|2026-10-30 EOD|ATM44、skew24局部ready|surface/positioning/execution均0；bid/ask 0；full-chain false|
|Metadata|五所部分|2026-10-30|SHFE/INE/CZCE较完整|DCE HTTP412、GFEX日期解析限制；正式卡参数仍需周一复核|
|官方crosscheck|SHFE238/INE63/CZCE243/GFEX48；DCE失败|2026-10-30|已比较settle/close/pre-settle差异0|DCE HTTP412；未核volume/OI|
|Stock|5577证券，5571原始报价；完整财务包2|trade_date 10-30；research_asof 10-31 10:40|利润桥背景|复权、行业、实时交易状态、执行检查未就绪|

**读取状态**：report_input_latest.json=empty（0字节），night_session/latest.json=empty；因此下钻到last_run_status、latest、market_state、physical、external、options、metadata与crosscheck。两个empty不等于全模块空。仓库ref为本次各路径实际main blob版本；未编造统一部署commit。

**日历闸门**：11月1日为周日；仓库night trading_date=11月2日、session_start=10月30、end=10月31，符合“周五夜盘归属下一个有效交易日”，calendar_mismatch=false。历史夜盘不是“今晚夜盘”，其public fallback也不是交易所核验最终收盘。

**后台覆盖**：黑色 I/JM/J/RB/HC/FG/SA/SF/SM；金属 CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG；能源化工 SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP；新能源 LC/SI/PS及GFEX实际新增；农产品 A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK；航运EC均进入77品种EOD/Market State初筛。未入榜最重要异常：油化整体涨幅已大、贵金属去杠杆、CU/SN与弱PMI冲突、AP曲线强而实体缺失、EC高RV但无方向证据。

## 3. 仪表盘

|标的|EOD close/settle|1D/5D|Vol/OI/ΔOI|曲线、Night与海外|Options|信号|
|---|---:|---:|---|---|---|---|
|SC2612|742.4/727.6|-1.128%/1.478%|191821/27364/-262|Night 758.5；+2.168% close/+4.247% settle；SC2612/2701 +1.066%|ATM730 IV66.16；skew否；执行否|条件多，禁追|
|MA701|3480/3463|0.933%/8.32%|3293327/881205/-40955|Night 3613；+3.822%/+4.333%；与MA612曲线+2.325%|MA612 ATM3550 IV48.60；错月|观察|
|BU2701|5284/5204|1.919%/13.13%|612330/236079/+13377|Night5304；+0.379%/+1.922%；曲线约+1.6%|ATM5200 IV46.31；执行否|Brent阈值未到|
|AG2612|12093/12374|-4.211%/-6.647%|545345/238317/-21622|Night 11646 vs11532冲突；不算正式收益/曲线|ATM12400 IV43.25；skew否|只等反抽失败空|
|AU2612|855.18/861.9|-0.879%/-0.84%|见EOD/见EOD/待核|外盘Dec金3898.90；现货3880.97附近|局部ATM可读；执行否|观察去杠杆|
|EB2612|10404/10253|0%/1.716%|见EOD/见EOD/待核|Night10675；+2.605%/+4.116%|局部ATM可读|油化强、禁追|
|PP2701|10433/10433|1.301%/9.59%|见EOD/见EOD/待核|Night10815；+3.662%|局部ATM可读|仅确认腿|
|EG2701|5392/5342|2.044%/10.304%|见EOD/见EOD/待核|Night5423；+0.575%/+1.516%|局部ATM可读|涨幅已大|
|CU2612|108050/108190|-0.77%/0.82%|见EOD/见EOD/待核|Night107250；-0.740% close|局部ATM可读|PMI反证|
|SN2612|360880/370160|-3.373%/-1.28%|见EOD/见EOD/+4771|Night362880；-1.967% settle|局部ATM可读|波动高、参数缺口|
|AP701|5887/5678|2.788%/-0.838%|见EOD/见EOD/+15152|无夜盘；701-703 settle曲线+5.401%|ATM5700 IV32.97；RR25 -3.64；执行否|早期线索|
|EC2612|2625/2648|-0.675%/-11.036%|见EOD/见EOD/+288|无夜盘；曲线-14.218%|无有效执行链|高波动观察|

注：Night价格均为历史会话公共exact-contract fallback或其冲突记录，非官方最终收盘；Sunday没有新增海外实时窗口。

## 4. 相比上一版真正变化

1. **OPEC+七个核心成员会前原则上倾向12月目标不变；正式结果尚未发布。** SC催化从“政策未知”变为“无意外增产为基准”，上行仍依赖地缘供应风险而非减产惊喜。
2. **10月31日晚报把到期Dec Brent 117.64作为主锚；本期改用更活跃Jan Brent 113.43。** SC仍高优先但赔率分下调；BU的Jan Brent≥115条件当前未满足。
3. **11月1日周日无中国日盘、夜盘或海外实时会话，EOD与合法夜盘均沿用10月30日/其后夜盘。** last-good有效但不是新增催化；不把周日06:05刷新称为新行情。
4. **PMI弱势在晚报已纳入，本期进一步把建筑新订单40.0用于BU/黑色反证，不重复计独立事件。** 黑色与沥青多头不得仅凭油价/曲线进入。
5. **Stock引擎未新增完整财务公司；限定检索仅见紫金员工持股计划过户类公告，未取得足以改变商品论点的经营披露。** 股票不增证据层、不提供即时表达。

旧观点处置：所有稳定idea_id保留；无成交回执，实际持仓均为“未提供/未知”。本期参数变化只适用于新候选计划：SC的海外锚明确改为活跃Jan Brent≥113.5；BU原Jan Brent≥115条件保留且当前未满足。该变化属于数据纠错/语义澄清，不回填历史盈利或触发。

## 5. 产业链与公司利润桥

### 1. 原油→SC/BU→油化

方向：供应风险偏多但内需反证；最强/最弱：SC/BU。EOD/Night：SC历史夜盘弹性强于BU；MA/PP/EB涨幅已大。曲线：SC、BU近月结构偏强。实体：无A/B基差；库存/仓单不构成完整支持。海外：Jan Brent113.43、WTI104.12；OPEC会前倾向不变。最大缺口：周日无实时价、OPEC正式结果、官方夜盘收盘。置信度：中。

### 2. 贵金属→AG/AU→矿业股

方向：AG反抽失败偏空；最强/最弱：AU相对抗跌/AG。EOD/Night：AG EOD -4.21%，夜盘报价冲突；海外银约49。曲线：AG近远月偏弱但精确夜盘曲线隔离。实体：工业需求新闻与PMI偏弱；无独立库存支持。海外：现货银-6.5%，金-3.5%；超卖为反证。最大缺口：同标的COMEX实时、AG精确夜盘、skew。置信度：中。

### 3. 黑色/基建→I/RB/HC→宝钢

方向：需求证据偏弱；最强/最弱：无合格方向/顺周期需求。EOD/Night：全板块已扫描、无≥3层新机会。曲线：不以单曲线替代实体需求。实体：制造PMI49.3、建筑48.0、建筑新订单40.0。公司利润桥：宝钢2026H1利润桥=钢价×销量/结构−铁矿煤焦成本±库存/套保/汇率；弱PMI不能直接等于利润下降，亦不能支撑商品多头。股票表达受产品结构、销量、资本开支影响，较期货不纯。最大缺口：最新周频库存、吨钢利润、公司Q3原件交叉核对。置信度：中低。

### 4. 有色/新能源→CU/SN/LC/SI→紫金

方向：分化、不开新仓；最强/最弱：无合格即时方向/SN波动/AG弱。EOD/Night：CU小跌、SN波动大；LC/SI/PS已扫描未入榜。曲线：缺可执行跨境换算。实体：PMI基本金属行业产需低于50为反证。公司利润桥：紫金2026H1利润桥=金铜售价×矿产量−现金成本±套保/汇率−资本开支/少数股东；公司股权不是AG空头替代，经营多元化反而稀释银价信号。最大缺口：逐矿种产量/成本最新公告与证券执行参数。置信度：中低。

限定公司补证范围为宝钢股份、紫金矿业两家公司。巨潮公开检索未取得足以改变商品排序的新经营证据；紫金最新可见事项为员工持股计划非交易过户类公告，不计Physical层。公司旧财报只作利润桥背景，不冒充今日催化。

## 6. 统一机会榜

|#|idea_id|机会|方向|期限|逻辑/赔率/催化/价曲波/拥挤 = 总分|有效支持层|研究/证据/执行|
|---:|---|---|---|---|---:|---|---|
|1|COM-E-SC2612-WEEKEND-RISK-BREAKOUT-LONG-20261030|SC2612确认后回踩多|多|1—4交易日|20/16/16/12/8 = **72**|1价格、2曲线、4海外|高优先/3层支持但外盘合约纠错/not_execution_ready|
|2|COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029|AG2612反抽失败空|空|1—4交易日|21/17/14/11/8 = **71**|1价格、2期限方向、4海外|重点/3层、关键夜盘隔离/not_execution_ready|
|3|COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026|BU2701曲线确认后回踩多|多|1—4交易日|18/15/14/12/9 = **68**|1价格、2曲线、4原油|观察/3层但反证强/condition_not_met|
|4|COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024|MA701油化缺口保留|多|1—5交易日|17/13/14/12/10 = **66**|1价格、2曲线|观察/2层，分数上限69/data_and_condition_gap|
|5|COM-A-AP701-MOMENTUM-CURVE-PULLBACK-LONG-20261030|AP701动量曲线回踩多|多|2—10交易日|17/12/13/11/11 = **64**|1价格、2曲线|观察/2层，实体缺口/not_execution_ready|

分数仅是研究优先级，不是胜率；1层≤59、2层≤69、至少3层才有资格70+。期货结构并非合同限损；未报价期权替代也不把线性仓风险封顶。

## 7. 研究/交易卡

### 1. SC2612｜conditional long

- **窗口与状态**：2026-11-02 09:15—10:00 BJT；未触发、未成交、实际持仓未提供/未知。
- **事实**：EOD 742.4/settle 727.6；历史合法夜盘公共精确合约快照758.5，SC2701 750.5，近月升水1.066%；活跃Jan Brent 113.43。
- **市场已定价**：周末风险升水已部分进入SC；到期Dec Brent 117.64不可再作可比锚。
- **分歧/推断**：若OPEC正式结果未增加供给且周一SC曲线保持强，供应风险仍可能未完全定价。
- **触发与放弃**：AND顺序：OPEC正式结果无意外增产；09:15后SC2612≥758连续15分钟；SC2612/SC2701同一时点曲线≥1.0%；活跃Jan Brent可比报价≥113.5；随后回踩750—756且746不破。先高开>770、曲线<0.5%或Jan Brent<111则放弃。
- **规模**：40%试仓+60%确认；计划风险0.25%—0.75% NAV，主题总预算含BU/MA/油化股票≤2.5%。
- **止损/失效**：计划止损742；逻辑失效为供应风险回落且曲线转平/反套消失。止损不保证最大损失。
- **止盈/时间退出**：TP1 780；TP2 805；2026-11-04 22:45时间退出。
- **好/中/坏成交**：好/中/坏入场750/753/756；每手到计划止损风险8,000/11,000/14,000元；TP1毛R 3.75/2.45/1.71，TP2毛R 6.88/4.73/3.50。手续费和滑点未知，净R必低于毛R，执行前重算。
- **合约参数**：乘数1000桶/手；最小变动0.1元/桶、tick价值100元。保证金约18%、涨跌停约16%为仓库参数，周一须交易所复核；到期/交割/roll字段未全部独立核完。
- **压力**：1个限幅约118,784元/手、2个约237,568元/手（以EOD close×1000×16%线性压力代理）；实际跳空、扩板和流动性枯竭可更差。
- **替代表达**：SC看涨价差仅研究；ATM730 IV66.16为10/30 EOD局部样本，bid/ask 0、execution_ready=false，必须人工询价并限定最高净支出。

### 2. AG2612｜conditional short

- **窗口与状态**：2026-11-02 09:15—10:30 BJT；未触发、未成交、实际持仓未提供/未知。
- **事实**：EOD 12093/settle12374，1D -4.211%、5D -6.647%；现货银周五约49美元、跌6.5%；夜盘公共报价11646与11532冲突。
- **市场已定价**：海外与中国EOD已明显定价下跌，超卖使直接追空赔率下降。
- **分歧/推断**：只有反抽失败且海外银不收复49.5，才说明弱势延续而非被动去杠杆后的均值回归。
- **触发与放弃**：顺序触发：先反抽进入11780—11920；随后价格回落并在11950下方持续15分钟；可比COMEX活跃银或经核验现货≤49.5；AG2612/AG2701同一时点曲线≤0。开盘先破11400、没有反抽、精确报价仍冲突或COMEX>51则放弃。
- **规模**：40%试仓+60%确认；计划风险0.25%—0.50% NAV，与AU/海外贵金属合并主题风险。
- **止损/失效**：计划止损12150；逻辑失效为海外银重回51上方且内盘曲线转强。
- **止盈/时间退出**：TP1 11300；TP2 10700；2026-11-04 14:45时间退出。
- **好/中/坏成交**：好/中/坏做空11920/11850/11780；每手到止损风险3,450/4,500/5,550元；TP1毛R 2.70/1.83/1.30，TP2毛R 5.30/3.83/2.92。费用/滑点未知，净R未验证。
- **合约参数**：乘数15千克/手；tick 1元/千克、tick价值15元。保证金、限幅、到期交割与roll需周一在交易所参数复核后才可执行。
- **压力**：技术止损不能覆盖高开跳空、涨跌停与夜盘流动性消失；期货损失未封顶。
- **替代表达**：AG看跌价差仅研究；10/30 ATM12400 IV43.25，skew不就绪、无bid/ask，不能称已便宜或已限损。

### 3. BU2701｜conditional long

- **窗口与状态**：2026-11-02 09:15—10:30 BJT；未触发、未成交、实际持仓未提供/未知。
- **事实**：EOD 5284/settle5204，1D +1.919%、5D +13.13%；历史夜盘5304；曲线约1.6%；Jan Brent113.43。
- **市场已定价**：油价与曲线强已进入价格，建筑PMI弱削弱终端需求。
- **分歧/推断**：只有活跃Brent重新站上115且BU反套不塌，才值得付出追随成本。
- **触发与放弃**：AND：09:15后BU2701≥5300持续15分钟；BU2701/BU2612同一时点曲线≥1.5%；活跃Jan Brent≥115；随后回踩5235—5265守住5200。先高开>5380、Brent<111或曲线<0.5%放弃。当前Jan Brent 113.43，条件未到。
- **规模**：40%+60%；计划风险0.25%—0.50% NAV，与SC同主题合并。
- **止损/失效**：计划止损5170；逻辑失效为油价回落且曲线转平。
- **止盈/时间退出**：TP1 5380；TP2 5520；2026-11-04 14:45时间退出。
- **好/中/坏成交**：好/中/坏入场5235/5250/5265；每手到止损风险650/800/950元；TP1毛R 2.23/1.63/1.21，TP2毛R 4.38/3.38/2.68。费用/滑点未知。
- **合约参数**：乘数10吨/手；tick 2元/吨、tick价值20元。保证金/限幅/交割/roll需周一复核。
- **压力**：建筑需求反证、原油周末跳空、相关性断裂、保证金上调均可能使计划止损失真。
- **替代表达**：BU期权ATM5200 IV46.31仅局部研究，execution_ready=false，未询价。

## 8. 商品期权专项

- 样本：core_v1、sampled_strikes，10月30日EOD；64目标、45成功、1000合约、45 series。core_atm_ready=44、skew_ready=24；完整surface、positioning、execution均为0。
- 局部ATM：SC2612 730/IV66.16，BU2701 5200/IV46.31，AG2612 12400/IV43.25，AP701 5700/IV32.97；它们是同日局部样本，不是周一实时成交IV。
- 局部skew：AP701 RR25约-3.64、BF25约+1.17可作研究；MA可读skew属于MA612而非MA701，不能错月外推。SC/BU/AG skew未ready。
- IV-RV：只能比较口径相近的局部ATM与EOD RV20作研究线索；事件周末使历史IV与周一moneyness可能失真，低IV/高IV不独立证明便宜/昂贵。
- positioning/dealer gamma：不可用；样本OI不推出全链PCR、拥挤或dealer净Gamma。
- 执行：bid/ask覆盖0，任何价差均“仅研究、执行前人工询价并确认、不提供未经验证权利金”。无可靠净支出就不宣称有限损结构已可交易。

## 9. 9:00开盘风险地图

|三层|已知信息|周一可能反应|动作|
|---|---|---|---|
|Previous China EOD|10-30油化偏强、贵金属偏弱；PMI随后转弱|油化高开但分化；顺周期承压|不追第一跳|
|Current T Night|10-30晚—10-31凌晨归属11-02；SC/MA强、AG弱；仅部分公共fallback|大量信息可能已在历史Night定价|09:15核持续，09:30核曲线，09:45核量仓/海外|
|07:00 Overseas|周日无实时会话；Friday Jan Brent113.43、银约49；OPEC结果待发|周末消息决定gap|结果一致则降催化权重；意外结果重排|

潜在高开：SC/BU/MA/EB/PP，但SC先过770、BU先过5380或MA缺口过大均不追。潜在低开：AG/AU，AG先破11400不追空。无夜盘品种AP、EC下一真实窗口同为11月2日09:00。15/30/45分钟检查顺序是价格持续→准确近远月→量/OI与海外同向；任何一项缺失都只保留研究，不升级执行。

## 10. 未来24h / 7d事件

|窗口|事件|北京时间|处理|
|---|---|---|---|
|未来24小时|OPEC+核心成员周日线上会议正式结果|2026-11-01，具体发布时间待确认|SC/BU/油化Delta与周一gap；若结果与会前倾向一致，新增信息量有限；意外增产/减产才重排。|
|未来24小时|周末地缘与霍尔木兹航运消息|全天|线性期货隔夜gap风险；未报价期权不承担已限损。|
|下一窗口|中国商品日盘开市|2026-11-02 09:00|15/30/45分钟复核曲线、量仓、外盘同步；不追9:00第一跳。|
|7日|EIA周度石油库存|预计2026-11-04 23:30，发布日程需临近复核|SC/BU Delta；已建假设仓降低事件前净Delta或用已询价有限损结构。|
|7日|CFTC周度持仓|预计2026-11-07清晨|贵金属拥挤度仅周频滞后背景，不作dealer gamma。|
|7日|USDA/WASDE|本7日窗口未取得官方确认的重大WASDE日期|农产品不因日历缺口被删；AP等继续等实体与报价，日期待核。|

## 覆盖、输入与发布前校验

- 全范围初筛：77品种已取得EOD/Market State并扫描；Physical 18/20、External 17/22、Options 45/64的缺口只限制依赖项，不代表无机会。
- 分项和复核：72、71、68、66、64均等于25/25/20/15/15五分项之和，且符合证据层上限。
- 确定性计算：SC/AG/BU每手风险与目标R按带方向的价格差×乘数重算；费用/滑点未知，未当作0。
- 语义校验：周末无可交易窗口；历史Night归属11月2日但不是今晚；已过窗口没有写成未来；无成交回执。
- 未解关键缺口：OPEC正式结果、周一准确报价与近远月、DCE官方crosscheck、AG夜盘冲突、全链期权报价、A/B基差、部分元数据。
- Stock贡献：只作两家公司利润校验；不建股票独立榜，不把商品冲击导致的股价变化算第六层。

## 来源

### 关键事实台账

|fact_id|标的|值|口径/单位|观测时间|known_at|支持判断|局限|直达源|
|---|---|---|---|---|---|---|---|---|
|F-EOD-1030|五所商品EOD|806合约/77品种|close/settlement|2026-10-30日盘|2026-11-01 06:05|全市场初筛|vendor ready不等于官方全核|[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)|
|F-NIGHT-1102|历史Night|412/806；51.1166%|公共exact-contract fallback|10-30晚—10-31凌晨|2026-10-31 05:58|周一价格/曲线|非今晚、非官方收盘；214 errors|[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)|
|F-PMI-1031|中国PMI|制造49.3；建筑48.0|官方月度指数|2026-10|2026-10-31 09:30|需求反证|扩散指数不等于品种需求量|[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)|
|F-OPEC-1031|OPEC+核心七国|会前倾向12月目标不变|政策消息|2026-10-31|2026-11-01 00:40前后|政策尾部|匿名来源、未正式发布|[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)|
|F-BRENT-1030|Brent Jan/到期Dec；WTI|113.43/117.64；104.12|USD/bbl settle|2026-10-30美国收盘|2026-10-31|海外锚与纠错|周末非实时、不可直接套利|[源](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)|
|F-PM-1030|银/Dec金期货|约49/3898.90|USD/oz|2026-10-30美国时段|2026-10-30|AG弱势及超卖|银现货与期货不同标的|[源](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html)|
|F-OPT-1030|商品期权core|45/64；ATM44；skew24；exec0|sampled EOD|2026-10-30|2026-10-31 06:04|局部IV/skew|bid/ask 0、非全链|[源](https://www.reuters.com/business/energy/opec-set-keep-production-targets-unchanged-december-source-says-2026-10-31/)|
|F-STOCK-1030|A股输入|5571报价；财务包2|raw EOD|2026-10-30|2026-10-31 10:40|公司利润桥|复权/行业/执行未就绪|[源](https://live.euronext.com/en/financial-news/oil-jumps-2-settles-6-month-highs-fears-escalation-iran)|

实际读取时间统一为2026-11-01T06:59:00+08:00；读取时间不替代观测时间。

### 来源清单

1. [China-Commodities-Engine EOD status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（GitHub / farfromexact，源日期2026-11-01；支持：2026-10-30五所EOD覆盖806合约、77品种；full_market_ready=true但official_complete=false；周日刷新未产生新交易日证据）
2. [China-Commodities-Engine night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（GitHub / farfromexact，源日期2026-10-31；支持：夜盘归属交易日2026-11-02；412/806合约、覆盖51.1166%；raw night file为空且214个query_error/unresolved）
3. [Commodity options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)（GitHub / farfromexact，源日期2026-10-30；支持：45/64品种、1000合约；bid/ask覆盖0，full_chain未验证）
4. [Commodity options local surfaces](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)（GitHub / farfromexact，源日期2026-10-30；支持：ATM-ready 44、skew-ready 24；surface/positioning/execution均0）
5. [Futures official-price crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)（GitHub / farfromexact，源日期2026-10-30；支持：SHFE/INE/CZCE/GFEX已比较字段无观察到差异；DCE官方接口HTTP 412，成交量和持仓未交叉核对）
6. [2026年10月中国采购经理指数运行情况](https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html)（国家统计局，源日期2026-10-31；支持：制造业PMI 49.3、生产49.8、新订单49.4；购进价格56.8、出厂价格51.7；建筑业48.0、建筑新订单40.0）
7. [OPEC+ agrees in principle to keep December targets steady](https://www.reuters.com/business/energy/opec-set-keep-production-targets-unchanged-december-source-says-2026-10-31/)（Reuters，源日期2026-10-31；支持：七个核心产油国会前原则上同意12月目标不变；结果尚待周日会议正式确认）
8. [Oil settles at six-month highs](https://live.euronext.com/en/financial-news/oil-jumps-2-settles-6-month-highs-fears-escalation-iran)（Reuters / Euronext，源日期2026-10-30；支持：到期12月Brent结算117.64；更活跃1月Brent结算113.43；WTI结算104.12）
9. [Precious metals Friday close](https://www.reuters.com/world/india/gold-slips-higher-oil-us-inflation-data-bolster-fed-hike-bets-2026-10-30/)（Reuters，源日期2026-10-30；支持：现货银跌6.5%至约49美元；12月金期货结算3898.90、下跌3.3%；白色贵金属超卖但动量仍弱）
10. [SHFE holiday calendar](https://www.shfe.com.cn/services/calenderandholidays/holiday/)（上海期货交易所，源日期2026-11-01；支持：2026-11-01为周日休市；下一中国日盘窗口为11月2日）
11. [China-Stock-Engine research inputs](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/research_inputs_latest.json)（GitHub / farfromexact，源日期2026-10-31；支持：A股trade_date为2026-10-30、5571条原始报价；完整财务包仅2家公司，执行检查未就绪）
12. [宝钢股份2026年半年度报告](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)（巨潮资讯，源日期2026-08-22；支持：2026H1合并口径营收1607.31亿元、归母利润45.71亿元；铁矿成本与钢材售价/销量/产品结构共同决定利润）
13. [紫金矿业2026年半年度报告](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)（巨潮资讯，源日期2026-08-22；支持：2026H1合并口径营收1941.78亿元、归母利润391.70亿元；矿产量、成本、套保、汇率及少数股东削弱单一金属价格映射）
14. [Previous commodity evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/10/2026-10-31_commodities_evening.md)（Global-Cross-Asset-Radar，源日期2026-10-31；支持：继承稳定idea_id及未触发计划；此前误用到期12月Brent作为主锚，本期纠正）

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：SC2612周一确认后回踩多；AG2612反抽失败空；BU2701仅在活跃Jan Brent≥115且曲线≥1.5%后考虑。
C. 今天继续观察：MA701、AP701、CU/SN、EC及OPEC正式结果、周一量仓曲线、期权人工报价。
D. 今天必须回避或有条件退出：回避周日虚构交易、追SC/油化高开、追AG低开、使用冲突夜盘报价及任何未询价期权；若仅有假设旧仓，触及各卡独立止损/逻辑失效时才条件退出。
