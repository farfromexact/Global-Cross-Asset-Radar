# 商品 Radar｜乙二醇缺的是近货，镍涨的是哪一种镍？

**2026年11月18日，北京时间18:04。** 中国日盘已结束。期货价格以人民币计，表内涨跌采用同合约结算对结算。公开资料于当晚18:04—18:15核读，只采用截点前已披露的事实。

## 1. 一句话结论

未来两至五个交易日倾向等待，确信度中等：乙二醇现货升水随交期迅速下降，豆棕收敛已越过旧目标，镍铁供应担忧尚需电解镍现货和近月价差共同确认。

## 2. 数据质量与覆盖数表

| 范围 | 本轮实得 | 能回答的问题 |
| --- | --- | --- |
| 五家商品交易所的Wind快照 | 11月18日15:00，77个品种、806份合约，四页品种记录和质量说明齐备；77个代表合约中72个有成交 | 可判断日终广度、同合约动量及期限结构。早籼稻、普麦、粳稻、强麦、动力煤的代表合约成交为零；成交为零与当日价格稳定的经济含义不同。[市场概要](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/overview.json)、[产品一](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-016.json)、[二](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-017.json)、[三](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-018.json)、[四](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-019.json) |
| 最新已完成夜盘 | 17日晚至18日凌晨，归18日交易日；55个品种有代表报价，806份目录里517份有夜盘成交，289份无夜盘成交 | 采用最后一根有成交的已完成5分钟线末值。无夜盘持仓，夜盘价格已反映在18日整日行情，不能再加一次。[夜盘原件](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-020.json)、[质量说明](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-025.json) |
| 期权与合约参数 | 18日日终64个商品系列、456份抽样合约，IV覆盖85.31%，买卖盘口覆盖为零。合约元数据源日11月9日，部分字段为空 | 有效的同到期、同执行价认购认沽可以读局部波动；完整偏斜、净Gamma和下一窗口的成交成本各需额外数据。新挂牌和不同系列仍须单独核对。[期权质量](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/overview.json)、[镍合约档案](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/contract_meta/part-003.json) |
| 范围外新增与外部材料 | 郑商所葵花籽油期货（SO）11月12日上市，仓内77品种不含SO。11月18日的交易所日终收盘价和结算价尚未核实 | 纳入油脂替代链。SO每手20吨，不能把大商所另两种油脂每手10吨的比例直接套用。现货、机构统计、交易制度分别使用各自日期。[郑商所11月6日业务细则](https://www.czce.com.cn/cn/content_file/flfg/zcjywgz/pzxz/2026/11/cd4d36000a5d4b63aecb80aeaa914efc.pdf) |

## 3. 商品仪表盘

**按主力结算数，14涨、57跌、6平。** 当天真正逆势的是镍与不锈钢；有色内部的铜、锡以及能源化工中的对二甲苯、乙二醇大幅走弱。下表是11月18日收盘／结算，单位除注明外为元／吨。五日比较锚为11月11日，同一合约，持仓增减单位为手。[全品种结算变化一](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-016.json)、[二](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-017.json)、[三](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-018.json)、[四](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-019.json)。

| 板块与准确合约 | 收盘／结算 | 一日／五日 | 量仓或曲线 |
| --- | ---: | ---: | --- |
| 能源·原油 SC2701，元／桶 | 576.1／589.4 | −0.77%／+0.91% | SC2612−SC2701收盘升水13.2元／桶 |
| 化工·乙二醇 EG2701 | 4,900／4,993 | −2.56%／+2.34% | 主力减仓25,915，近端相对1月更紧 |
| 化工·对二甲苯 PX701（2027年1月） | 8,044／8,182 | −2.22%／−1.71% | 增仓8,096 |
| 黑色·焦煤 JM2701 | 1,364／1,377.5 | −3.03%／−2.51% | 增仓6,889 |
| 黑色·铁矿石 I2701 | 646／645 | −0.08%／−5.43% | 减仓24,393；日内低点638.5 |
| 建材·玻璃 FG701（2027年1月） | 899／900 | +1.24%／+1.58% | 增仓18,811 |
| 有色·镍 NI2701 | 122,200／123,120 | +2.33%／+0.94% | 增仓4,735；12月收盘较1月低210 |
| 有色·不锈钢 SS2701 | 14,125／14,140 | +1.40%／+1.40% | 增仓17,084 |
| 有色·铜 CU2701 | 97,920／99,780 | −1.54%／−4.06% | 增仓17,150；12月较1月收盘升水3,030 |
| 贵金属·铂 PT2702，元／克 | 342.40／343.80 | −3.71%／−9.76% | 增仓533；扩大到工业金属整体会误判镍 |
| 新能源·碳酸锂 LC2701 | 91,520／91,000 | +1.13%／+2.87% | 减仓6,323 |
| 油脂·棕榈油 P2701 | 8,606／8,700 | −1.96%／−0.83% | 1月收盘低于5月509 |
| 油脂·豆油 Y2701 | 8,528／8,576 | −1.00%／−1.78% | 1月收盘高于5月288 |
| 航运·集运欧线 EC2612，点 | 2,650／2,594 | −1.67%／+5.06% | 日收高于结算56点，报价与最终结算指数存在时间差 |

准确月份日行情见[有色](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-002.json)、[不锈钢](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-003.json)、[集运](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-004.json)、[原油](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-005.json)、[黑色与乙二醇](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-006.json)、[棕榈](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-007.json)、[豆油与玻璃](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-008.json)、[对二甲苯](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-009.json)、[广期所合约](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-011.json)。锡SN2701跌2.58%、持仓增15.9%，银AG2702五日跌9.96%；均缺乏据此确认持仓双方身份或可交割供给的依据。铜价跌而12月收盘升水比17日的2,680再扩350，追空近端会额外承受货源挤压。

## 4. Delta Research｜今天为什么需要重新判断

**乙二醇：今晨还在问港存低能否支撑1月，今天下午已经能直接看到不同交货日的报价。** EG2701从17日23:00的5,072降到18日收盘4,900，跌破旧5,010不利情景；12月减1月的收盘差从夜末353扩到396，同时1月减5月从430缩至371。生意社14:51记录同一EG2701作基准的进口聚酯级乙二醇港口报价，本周交货升水1,100—1,115元／吨，12月下旬交货只升480。交期延后一个多月，升水少620—635。早期供应紧张仍有交易商报价支持，但用它解释1月该反弹至5,379的证据反而变弱。[18日晨报，截点07:35](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/18/20261118T075346+0800_2ee0ae3c009803b0ba55fd32be3e8acc/commodities.md)、[三个月份日行情](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-006.json)、[生意社化纤撮合交易中心11月18日原始报价](https://www.rawmex.cn/trade/market/m108-1072)。

**豆棕：方向被价格验证，原方案的收益空间已经用完。** 卖P2701、买Y2701所赚的是P−Y下降。价差从17日日收203、夜末133，到了今天收盘的78，已低于原先设的97好情景；同日两腿结算差为124。一个交易者在18日收盘重建组合，重返97反而亏钱。今天结束旧目标作为新入口的研究，保留24日14:55原观察终点，不凭两份收盘成交记录推定有人做成价差。[17日首次豆棕方案](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/17/20261117T160901+0800_1920c55c6945f5d6281ec42104188592/commodities.md)、[18日晨间重算](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/18/20261118T075346+0800_2ee0ae3c009803b0ba55fd32be3e8acc/commodities.md)、[棕榈两腿月份](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-007.json)、[豆油两腿月份](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-008.json)。

**镍与不锈钢：18日结算逆势走强，隔夜冲击在日盘有明显回吐。** NI2701的夜盘末值124,000，随后日收122,200，比夜末低1,800元／吨；SS2701从夜末14,310收至14,125。11月18日整交易日的持仓增加属实，无法定位为哪一段时间、哪类参与者所为。本期把镍新增为期限与交割品种核对的候选。[NI2701本身的夜盘](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/night/part-012.json)、[不锈钢夜盘](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-020.json)、[镍日行情](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-002.json)、[不锈钢日行情](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-003.json)。

## 5. 产业链图

**镍铁—不锈钢—电解镍。** 欧委会异议针对欧洲经济区不锈钢厂获得低碳镍铁的竞争条件。英美资源10月20日披露，三季度产镍10,400吨、同比增3%，部分反映巴罗阿尔托检修提前；公司产品是镍铁。五矿资源11月3日披露欧委会审查期限为12月21日、交易协议长期截止日改为12月31日。原件支持“可能改变供货去向和投资安排”，已公布的产量还没有给出减供证据。沪镍标准交割品是镍钴含量至少99.96%的电解镍；要把欧洲镍铁担忧变成中国1月可交割品短缺，中间要出现钢厂替代采购、精炼镍库存下降或近端升水。今天NI2612收121,990、NI2701收122,200，近月仍便宜210，对即时短缺构成反证。另一条合理路径是低碳镍铁在欧洲变贵、中国精炼镍供给平稳，NI和SS因消息上涨后再分化。[欧委会9月16日异议原文](https://ec.europa.eu/commission/presscorner/api/files/document/print/en/ip_26_1877/IP_26_1877_EN.pdf)、[英美资源三季产量报告](https://www.angloamerican.com/media/press-releases/2026/20-10-2026)、[五矿资源11月3日公告](https://www.mmg.com/content/uploads/2026/11/e_2026-11-03_VA-Change-of-Long-Stop-Day.pdf)、[上期所镍交割品级](https://www.shfe.cn/products/futures/metal/nonferrousmetal/ni_f/)、[近远月原价](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-002.json)。

**原油—运输—中国炼厂。** IEA 11月13日报告估计，10月全球原油及油品可观测库存合计增加5,200万桶，其中水上油增加8,600万桶；两者之差意味着其余可观测库存合计减少约3,400万桶。海湾离港改善能压远期价格，货尚未到岸则能同时抬升近端便利价值。国内10月规模以上工业原油加工量5,830万吨，同比下降8.1%，也可能是原料受约束或利润不足。SC2612／2701今收589.3／576.1，对应价差13.2元／桶，几乎等于本交易日夜末13.1；远月绝对价格下行没有解除近月交付约束。需要中国到岸供应和炼厂实际接货改善，并看到近月升水收窄，才有理由增配供给恢复交易。[IEA 11月13日月报](https://www.iea.org/reports/oil-market-report-november-2026)、[国家统计局11月16日发布](https://www.stats.gov.cn/sj/zxfb/202611/t20261116_1965842.html)、[原油合约及成交量](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-005.json)。

**乙二醇—港口—聚酯。** 500吨起售的港口纸货对EG2701报价随交期延后而下降，11月25日前仍升水1,000—1,030元／吨，12月25日前为480。这些是特定等级和起售量的报价，能够识别缺货发生在哪段时间；税费、仓储地点及成交价未逐笔对齐，不能把报价差直接变成可交割套利。12月、1月、5月期货分别收5,296、4,900、4,529。当天在近端交割便利仍贵的同时，1月相对5月降价；这符合市场预期装置复产或到港缓和。竞争解释是供给恢复过慢，届时1月也要补涨。判别点是下轮卸货与实际提货量，以及12月下旬同一等级报价是否也重新扩大。[生意社11月18日港口分交期报价](https://www.rawmex.cn/trade/market/m108-1072)、[精确三合约](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-006.json)。

**油籽—油脂替代。** 马来西亚棕榈油局10月暂定库存362.12万吨，9月修订值351.06万吨；10月出口170.87万吨，较9月109.71万吨增加，库存依然累积，说明单看出口增速容易高估紧张程度。中国1月棕榈较5月折价509元，而豆油1月较5月升水288元。两条曲线相差797元，近端相对供需分化已被大幅计价；若冬季进口收缩、产地去库加速，1月棕榈反而有相对修复风险。国内油脂同口径后续库存及进口排船可区分这一反证，本日没有用月度马来库存推算中国两品种的可交割均衡差。[MPOB十月暂定月表，9月经修订](https://bepi.mpob.gov.my/stat/web_report1.php?val=202684)、[P2701与2705](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-007.json)、[Y2701与2705](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-008.json)。

## 6. 统一机会榜

所有分数针对11月18日15:00收盘参考做同一工具的持有期比较。五项依次为逻辑／赔率／催化／价格期限波动／拥挤技术，满分25／25／20／15／15。以下新增风险预算均为零。

| 方案、参考价格 | 比较终点（北京） | 分项及总分 | 现价决定 |
| --- | --- | --- | --- |
| 买1手沪镍NI2701，122,200元／吨 | 11月23日14:55，三个交易日 | 14／10／7／8／9＝**48** | 相对强势可研究，交割品和审查期限错配，不追多 |
| 买1手乙二醇EG2701，4,900元／吨 | 11月20日14:55，两个交易日 | 14／11／6／8／6＝**45** | 本周近货吃紧成立；1月短缺缺独立支持，旧5,010不利情景已被跌破 |
| 买1手豆油Y2701、卖1手棕榈P2701，8,528／8,606，P−Y＝78元／吨 | 11月24日14:55 | 14／3／4／5／7＝**33** | 继续收窄需要更新的下界；旧97已有反向距离，结束追入 |

镍的有效方向支持只有价格和量仓一层；企业公告证明存在审查，对中国1月交割方向仍属不确定因素，故催化仅7分。乙二醇的交期曲线与物理报价支持近端，五日同合约结算仍涨2.34%，但日收跌破先前下行情景，且港口报价与期货近端升水不应算作两个独立的1月方向证据。豆棕同时具备期货表现与产地库存佐证，却缺新的国内替代均衡区间，给赔率3分。原油空头和铜跨期未取得足够的新入场价值锚，保留观察，不把方向主题另打一套总分。

**旧方案的约束。** 11月15日版原油SC2701空头仅在16日09:00—10:15反弹失败、12−01升水不超过8.1，完成原反测且625.5—626.5可卖时开放；入口已到期。确有该版成交才适用640止损、价差连续两根完整5分钟高于10.6或供给逻辑失效提前退，607.1／587.8分半目标，最迟20日14:55。今天价差13.2和期货日高低都不能证明原先的连续条件或成交顺序。更早父卡在可检原文中是转引，635止损、600／585目标、19日14:55终点只供识别，不能与新卡拼接。铁矿I2701原拟665—668反弹空、成本不高于1.5元／吨、674失效、640目标；17日最高653、最低638.5后，作者在17日16:00主动取消后续入场。若持有对应旧仓，20日14:55仍是最迟退出。白糖SR701原先5100／5233的20日比较保留作跟踪，今收5121无法重启旧空头。铜旧月差、白银和集运已结束的方向均不因本日变化重开。[原油11月15日完整修订](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/15/20261115T110709+0800_d8dd392e3d29405dad12ef4bdb213ed7/commodities.md)、[11月15日乙二醇与白糖原情景](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/15/20261115T181852+0800_68e1639d399a432796ff00d357e6154e/commodities.md)、[铁矿11月16日原案](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/16/20261116T182033+0800_725c6aaf13d4de4c473d1dae587c4979/commodities.md)、[11月17日午间修订](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/17/20261117T121416+0800_aab1690764f22f580929df153f4bf94e/commodities.md)、[铁矿取消与豆棕原案](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/17/20261117T160901+0800_1920c55c6945f5d6281ec42104188592/commodities.md)、[11月18日晨间追溯及父卡出处限制](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/17fdf1a74fec8ea4a224698e5d29c84768602fc1/reports/2026/11/18/20261118T075346+0800_2ee0ae3c009803b0ba55fd32be3e8acc/commodities.md)。

## 7. 研究与交易卡

**卡一　沪镍NI2701。** 18日收盘较夜末低1,800元，仍较17日日收120,110高2,090元。同日已有市场重新定价，也有获利空间流失；若欧洲低碳镍铁溢价留在当地，沪镍做多的产业链会在跨品级这一步中断。与买不锈钢相比，NI没有钢厂能否转嫁成本、成品库存和终端订单的新增变量；但商品品级距离最初事件更远。现阶段等待精炼镍量价验证优于承担任一方向，尤其不宜把两个同向工具当作分散。[准确日行情](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-002.json)、[NI2701独立历史](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/market_state/part-014.json)。

| 项目 | 当前假设与决定 |
| --- | --- |
| 准确表达和窗口 | 多NI2701一手，1吨，最小价位10元／吨。用122,200测算至23日14:55，不设自动入场。1月15日为该合约最后交易日，研究期内不展期、不交割。[上期所合约](https://www.shfe.com.cn/products/futures/metal/nonferrousmetal/ni_f/)、[合约档案](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/contract_meta/part-003.json) |
| 重新评估的条件 | 有明确数量与时间的镍铁供货削减，同时国内精炼镍可比现货走强、NI2612−NI2701由负转正并获得交割库存变化支持。若只见远期监管新闻，或现货供货平稳、近月仍贴水，放弃。即使出现条件，也按当时价格重算 |
| 止损、目标及时间 | 这是预算为零的现价比较。125,350为本日已见高点，120,320为消息前17日结算，116,210为11月2日结算压力；都不是止损委托。到23日仍不能把事件连接到可交割品则结束本次比较 |

假设一手往返交易、滑点、融资共120元，不含跨月成本。至23日回到125,350、维持122,200、回到120,320、跌至116,210，净损益依次为**+3,030、−120、−2,000、−6,110元**；盈亏平衡122,320。好／普通不利情景约1.52倍，换作较宽压力只剩0.50倍。按20日实际波动率20.95%折算的三交易日价格尺度约2,790元，近期高点只是有市场先例的情景，不能把重新触及当作基准。11月18日中信期货标准投机保证金19%、限幅8%；按今结123,120估算一手占用约23,393元。若下一交易日沿用8%，从今结依次下移一／两次，较122,200参考价、含成本损失约9,050／18,111元；第二日扩板、无法平仓或经纪加保证金会继续放大现金需求。未核实新交易日个人费率与参数，不据此下单。[中信期货11月17日发布的18日参数](https://www.citicsf.com/e-futures/content/000205/826934)。

**卡二　乙二醇EG2701。** 从5,072跌到4,900确实改善了买价，但同一合约今天最低4,856，距离11月10日结算4,837只有19元；仅以4,837作最坏情况会系统性夸大赔率。便宜需要独立的1月交货价值和持有期内的催化。12月对1月升水396、1月对5月升水371，改做多1月空5月也已经支付这段升水；明年1月出现新缺口才适合持有该月差。[逐月价格](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/futures/part-006.json)、[乙二醇结算史](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/market_state/part-007.json)。

| 项目 | 当前假设与决定 |
| --- | --- |
| 参考与工具 | 多EG2701一手，10吨，收盘4,900；比较截止11月20日14:55，期内无交割或展期。[大商所合约条款转载](https://www.bocifco.com/newsinfo.aspx?cid=4&id=42074) |
| 入场、放弃与退出 | 无新入场或价格止损。若不同港口实际卸货低于排船、聚酯提货同步回升，且12月下旬按同一月份报价的升水也扩大，才重估；若货已抵港或到港覆盖提货、远交期报价继续松动，结束看多假设 |
| 原比较范围 | 原上行5,379、原技术不利5,010、后加压力4,837；今天日收已低于5,010。到20日时间退出不变，再以10月22日结算4,777检验更宽不利路径 |

假设每吨往返、滑点与持有合计12元；每手净额等于10×（退出价−4,900−12）。到20日若回到今结4,993，净赚810元；留在4,900亏120元；回到4,837亏750元；回到4,777亏1,350元。净盈亏平衡4,912。回到旧5,379可赚4,670元，但需两交易日涨约9.8%，是基于33.65%年化历史波动所得两日尺度约3.0%的三倍多，不能与较温和的下行情景等权当作基准。按中信期货18日EG投机保证金15%、今结4,993测，一手约7,490元。若下个交易日沿用该日6%限幅，按今结连续一／两次跌停的机械尺度、含成本约亏2,186／5,002元，流动性消失时实际退出损失可超出此数。[中信期货18日参数](https://www.citicsf.com/e-futures/content/000205/826934)。

**豆棕旧结构的退出价值。** 一手Y多、一手P空各10吨，四次买卖、滑点及持有成本合计假设240元／对。如今若Y从8,528升至8,600，同时P从8,606升至8,697，价差回到97，Y腿赚720元、P腿亏910元，合计**亏430元**。价差留在78亏240元，扩大到旧347亏2,930元；新入场盈亏平衡需降到54。11月10日同合约结算差曾为−44；即使把它当作更激进的下行情景，也只赚980元，约为回到347所亏金额的三分之一，且那是结算历史点，不是可成交的价值底。故既不追原方向，也不因穿越97就反手。若假设相关性破裂，Y跌8%、P涨8%一次／连续两次，等吨组合扣成本约亏13,947／27,659元；8%是场景，非核准两腿限板。[大商所豆油细则](https://np-newsimg.dfcfw.com/download/A2_cms_f_20260331153412056337?abc3853.pdf=&direct=1)、[棕榈油细则](https://np-newsimg.dfcfw.com/download/A2_cms_f_20260331153420560245?abc8746.pdf%3F=&direct=1)、[P历史](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/market_state/part-009.json)、[Y历史](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/market_state/part-010.json)。

本期三种表达合计新增预算为零。未来出现完整方案时试仓计划损失可从净值0.25%起评估，试仓范围0.25%—0.75%，确认后0.75%—1.50%；同一中国需求或能源主题连同全球报告持仓合并，风险上限采用2.5%。未取得账户成交与保证金信息，以上一手损失供核对，没有推算用户持仓数量。

## 8. 商品期权专项

| 11月18日期权标的、到期日 | 结算附近ATM IV／20日同合约实现波动率 | 持有期解释 |
| --- | ---: | --- |
| NI2701，12月25日 | 22.69%／20.95% | 124,000认购今收2,950元／吨。到期前跨越欧委会审查期限；本报告至23日的比较只覆盖三个交易日，不能把12月事件的凸性当成本周收益 |
| EG2701，12月16日 | 33.30%／33.65% | 仅相差0.35个百分点。两个交易日买波动需要未来实际振幅与路径足以覆盖买卖价差和耗时 |
| P2701／Y2701，同为12月16日 | 20.64%／19.73%；12.27%／14.14% | Y波动较低、P较高，但两个单腿的IV无法给出二者未来相关性或价差应付权利金 |
| SC2701，12月15日 | 52.34%／44.11% | 今日日终已恢复可用平值IV，不能沿用“供应商IV缺失”的晨间判断；库存公告与地缘跳空令裸卖尾部暴露较大 |

每个标的这里只取得一个到期；四类样本均无标准两翼同时可用的证据，不能据此比较期限溢价或25Delta偏斜。合约持仓不识别做市商净Gamma。[EG平值样本](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/options_surface/part-002.json)、[P／Y平值样本](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/options_surface/part-003.json)、[NI和SC样本](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/options_surface/part-004.json)、[NI认购原始价格](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/options_SHFE_NI/part-001.json)。

**乙二醇看涨价差给出一个可核的替代成本。** 买EG2701-C-5000、卖EG2701-C-5400各一手，收盘成交价140、43.5，参考净支出96.5元／吨；按结算则是199−67＝132。两个时点口径能给出相反的便宜程度，选择收盘价是为配合同期货收盘4,900，仍非同步可成交盘口。另设组合费用、滑点合计2元／吨，到期最大净损失985元、最大净收益3,015元、到期盈亏平衡5,098.5，均按10吨一组。美式提前行权与卖腿指派可能产生临时期货和额外资金需求。[11月18日乙二醇期权两腿成交及条款](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/options_DCE_EG/part-001.json)。

下表按11月20日计划退出，12月16日才到期。用欧式Black-76近似，年利率假设1.5%，初始28日、余26个自然日，按两腿收盘价分别反解有效IV为34.00%与35.64%，再平行上下移5个百分点。数字为每组净损益，扣2元／吨假设摩擦；无概率权重，未纳入提前行权和偏斜非平行变化。

| 20日EG2701 | IV降5个百分点 | IV不变 | IV升5个百分点 |
| --- | ---: | ---: | ---: |
| 涨至旧上行情景5,379 | +1,519元 | +1,422元 | +1,343元 |
| 平在4,900 | −148元 | −41元 | +43元 |
| 跌至4,708（10月22日的前结） | −596元 | −477元 | −372元 |

平盘时耗时和波动回落可令有限损失结构亏钱，反之在标的接近上腿时，提高IV也可能压低组合价值。到期3,015元的上限不能当作本周目标。两腿无买卖盘、期货行动条件尚未满足，因此保留上述模型比较，不买入波动。

## 9. 下一合法交易窗口风险地图

下一窗口是**11月18日周三21:00，归11月19日交易日**。原油可交易至次日02:30，镍和不锈钢至01:00，乙二醇和豆棕至23:00；集运欧线及碳酸锂、铂等无该夜盘，下一窗口为19日09:00。本轮使用的590.5元／桶原油夜末和12.4万元／吨镍夜末均发生在18日白天收盘之前，不能用作今晚开盘预测。[上期所交易时间表](https://www.shfe.com.cn/services/calenderandholidays/tradinghours/)、[大商所乙二醇交易安排](https://www.bocifco.com/newsinfo.aspx?cid=4&id=42074)、[已完成夜盘的归属](https://github.com/farfromexact/China-Commodities-Engine/blob/c9cdaf205de35f9c8ebf360f97a73913a8be326f/data/chat/report/part-025.json)。

今晚23:30若美国原油库存改变到岸紧张预期，国内原油还在交易，乙二醇及油脂已经休市。19日03:00美联储纪要又落在原油、镍收盘后，相关品种无法同步调整。外盘、汇率或跳空可能同时改变油脂替代与能源成本，不能假定跨品种头寸总能配平。不把尚未发布的统计结果、18:04后海外收盘或研究期内未知的交易所临时调整写入本轮行情。

## 10. 未来24小时／7天事件

| 北京时间 | 事件或观察节点 | 哪种结果会改变本期判断 |
| --- | --- | --- |
| 11月18日23:30 | 美国EIA周度石油报告，周三美东10:30。当周不属假日延期 | 若原油与成品油可用库存同步改善，且SC近月升水也收窄，供给恢复才更有交易意义；只一项累库须结合净进口、炼厂开工解读。[EIA发布时间](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 11月19日03:00 | 美联储10月会议纪要，美东18日14:00 | 若实际利率和美元显著重定价，先重估人民币计价金属和油的隔夜缺口；不把宏观反应重复算作产业证据。[美联储11月日历](https://www.federalreserve.gov/newsevents/2026-November.htm) |
| 11月19—20日，业内实际更新时 | 华东乙二醇各交期的同等级报价、实际卸货和聚酯提货；19日14:55是历史SC父卡所转引的固定退出 | 若远交期升水与实际提货同步增强，且到货未改善，重新评估卡二。20日14:55结束乙二醇／白糖原比较；有确切成交记录的SC修订卡、I原案按所属日期处理 |
| 11月23日14:55／24日14:55 | NI事件传导观察／原P−Y比较终点 | 镍铁消息若仍未传到中国交割品，结束当期追多比较。豆棕若无新替代价值锚，即便继续收窄也不延期 |
| 至11月25日18:04 | 观察后续同样本油脂库存、港口与精炼镍实际补货；确切披露时分未核 | 棕榈累库是否停止、镍近端是否持续转强，分别决定要否另起研究。12月21日欧委会审查时点在七日窗口之外 |

## 11. 最终行动四行

A. 今天没有值得新加风险的商品交易，新增预算为零。

B. 镍等中国可交割电解镍出现实际紧张再按卡一评估；乙二醇等12月下旬实货升水和实际提货共同加强再按卡二评估。

C. 今晚23:30看美国油库存及SC近月升水，本周看乙二醇不同交付期报价，23日检查镍与不锈钢的强势是否得到现货支持。

D. 结束以97为目标的新豆棕收敛研究，回避追空原油近月和重启铁矿旧入口；若持有已核实的历史方案，执行对应止损、目标和固定退出。

