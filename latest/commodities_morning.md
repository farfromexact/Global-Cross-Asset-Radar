# 商品期货期权晨间雷达｜2026-10-29

> 生成时间：2026-10-29 07:03（北京时间）｜信息截点：07:03 BJT｜edition=`commodities_morning`  
> 研究用途，不下单；不假定任何建议已成交或用户已有持仓。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；只值得等待BU、SC回踩确认及CU价格—曲线共振，9:00不追夜盘。**

机会分类：研究优势不足的是EC趋势空与MA旧多；机会存在但等待条件/报价的是BU2701、SC2612、CU2612；夜盘全市场价量、BU/SC精确夜盘曲线及大部分期权执行报价不足，不能判断其余品种能否立即执行。最有价值的三个观察依次为：BU2701在09:15后能否守住5050并维持近月升水；SC2612能否在EIA混合库存后守住730且月差继续正向；CU2612能否同时越109600、近月升水0.65%及LME三月铜14500美元。下一真实窗口为2026-10-29 09:00中国日盘，首轮判断分别在09:15/09:30/09:45。

## 2. 数据质量、覆盖与事实台账

本次按63个指定代码全量初筛；`LPG`按交易所代码`PG`映射，63/63均有覆盖记录。引擎还取得JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR等14个额外或新增代码，共77产品、806合约。当前ref为各文件在`main`本次读取SHA；`report_input_latest.json`为0字节，因此使用同日有效last-good模块，不把06:22失败刷新当作新行情。

| 模块 | 日期/范围 | 发布与能力 | 关键缺口 |
|---|---|---|---|
| Futures | 2026-10-28 EOD；806合约/77产品；SHFE/INE/DCE/CZCE/GFEX均同日；`data/latest.json` SHA `11be4c9...` | last-good verified；full_market_ready=true；source_date_match=100%；可用于研究 | 10/29 06:22刷新五所均因iFinD 401 `Device exceed limit`失败，root状态fresh=false；不影响10/28合法last-good，但无新增批次 |
| Market State | 2026-10-28；77产品、同合约20日 | 1/3/5/20D、RV20、量仓z及near-next可用 | 连续主力不替代真实同合约；部分品种滚动/历史不足只保留可得字段 |
| Physical | requested 2026-10-28；18/20原生频率内fresh | 仅背景；A/B级basis=0 | 所有basis均C级或不可用；SHFE/DCE/GFEX仓单刷新失败，不能作为方向或套利层 |
| External | requested 2026-10-28，generated 10/29 06:23；17/22 | context-only；另以公开源补07:00海外 | 非盘中统一快照；时点/品质/税运费未对齐，不能称跨境套利 |
| Night | trading_date=2026-10-29；session_start=10/28、end=10/29；generated 05:59 | 日期归属合法、`calendar_mismatch=false`；但published=false、validation=false | 806/806 query_error、0合约、coverage=0%；raw latest=0字节。CU/MA/BU/SC用公开精确合约fallback；均非交易所核验最终收盘，其他品种不作正式Night证据 |
| Options | 2026-10-28 EOD；19/64产品、430合约；core_v1/sample strikes | ATM ready 19、skew ready 12；planned sample quote coverage=100% | full-chain/surface/positioning/execution均0；bid/ask=0；BU/SC/CU无当前局部面；dealer gamma方向未知 |
| Metadata | 2026-10-28；806合约 | direct match 67.49%、effective 73.45% | 动态参数覆盖30.15%；DCE参数接口412、GFEX源日未核；每张卡只采用已核规则，未知保证金/夜盘截止不猜 |
| Official crosscheck | 2026-10-28 | SHFE 238、INE 63、CZCE 243、GFEX 48合约配对；settle/close/pre-settle真实different均0 | DCE HTTP412，故state=partial；未核成交量/OI；不等于五所全部官方认证 |
| Stock | 私库tape截至2026-10-21，非当前；本次限定查宝钢/CNOOC/Teck | 仅利润桥与事件验证，execution=false | 宝钢Q3沿用前序、非今晨催化；CNOOC九个月业绩定于10/30；Teck Q3将在今夜美股盘前发布，尚无结果 |

Night价格语义：CU/MA/BU公开页为供应商最近成交/页面快照，BU与SC取得接近会话结束的精确合约读数；`official_night_close_verified=false`。其OHLC、成交量和OI不宣称纯夜盘最终口径。相对close衡量夜盘新信息弹性；相对settlement仅为结算/限幅参考。

核心事实台账：

| fact_id | 标的/口径 | 事实、时间与单位 | 支持与限制 |
|---|---|---|---|
| F-EOD-1028 | 中国全市场EOD | 2026-10-28；806合约/77产品；五所同日；读取07:03 | 支持全范围扫描；10/29刷新失败不等于10/28 last-good失效 |
| F-NIGHT-FAIL-1029 | 中国T夜盘 | 归属10/29，05:59生成；0/806，806 query_error，未发布 | 证明仓库夜盘不可用；不能据此说市场无夜盘机会 |
| F-BU-NIGHT | BU2701，元/吨 | 公开精确合约快照5140，open/high/low=5097/5153/5021，约23:00；较EOD close5054 +1.702%、较settle4945 +3.943%；页面OI216456，较EOD +9948 | 价格层与海外油同向；非官方最终夜盘、OI非纯夜盘最终，BU2611-12夜盘精确曲线未取得 |
| F-SC-NIGHT | SC2612，元/桶 | 02:31公开精确合约读数737.5，较close733.4 +0.559%、较settle722.4 +2.090% | EIA后价格修复；无最终OI与同会话SC2701，不构成Night curve确认 |
| F-CU-NIGHT | CU2612/CU2611，元/吨 | 01:00供应商读数109240/109930；CU2612较close +0.037%；近-次月+690/+0.632%；CU2612 high109500、OI193871 | 原109600价格阈值和0.65%曲线阈值均未满足；OI较EOD -1716只作供应商观察 |
| F-MA-NIGHT | MA701，元/吨 | 22:59供应商读数3453，high3486、low3425；较close3464 -0.318%、较settle3417 +1.054%；页面OI约931545 | high穿越不能证明“15分钟确认→回踩”的顺序；最终低于3485，原条件未完成 |
| F-EIA-1028 | 美国石油库存 | EIA周至10/23：商业原油410.625m桶，周减1.892m；汽油209.180m，周增3.870m；馏分油102.824m，周减1.462m | 原油/馏分油偏多、汽油与成品需求偏空；只计一个实体事件，不重复增加层 |
| F-OVERSEAS-1028 | 海外收盘/约07:00 | WTI约101.89—102.78、Brent约115.32—115.36美元/桶；铜约14644美元/吨、黄金4066美元/盎司、白银54.05美元/盎司 | 支持油链、反对追贵金属；来源时点不完全同刻，跨市场只作方向映射 |
| F-FOMC-1028 | 美联储 | 10/28维持3.75%—4.00%；10票赞成、2票主张加息25bp；通胀仍偏高 | 鹰派异议抬高贵金属/铜追涨门槛；非精确价格归因 |
| F-OPT-1028 | 商品期权 | 19/64、430合约；ATM19/skew12；surface/positioning/execution=0 | 可研究局部IV/skew，不能给净权利金、全链PCR、dealer gamma或可成交性 |

## 3. 重点仪表盘（全量扫描后的12项展示）

1D/5D均以结算价同合约口径；Night为公开fallback且仅在精确合约可得时列示。

| 品种/合约 | EOD close/settle | 1D/5D；RV20 | 成交/OI/ΔOI | curve/basis/Physical | Current T Night / 海外 / Options | 信号 |
|---|---:|---:|---:|---|---|---|
| BU2701 | 5054/4945 | +1.06%/+9.67%；30.70% | 397061/206508/+26241 | BU2611-12 +5.479%；basis C | 5140，+1.70% vs close/+3.94% vs settle；Brent约115.3；无局部期权 | 强但过热，只等回踩 |
| SC2612 | 733.4/722.4 | -1.26%/+3.08%；43.84% | 171388/30025/-608 | SC2611-12 +0.706%；现货不可用 | 737.5，+0.56%/+2.09%；EIA混合；无局部期权 | 旧空终止，条件多待确认 |
| CU2612 | 109200/109200 | +0.52%/+0.15%；10.89% | 79060/195587/+4388 | EOD CU2611-12 +0.586%；basis C | 109240，+0.04%；night curve +0.632%；铜约14644；无局部期权 | 阈值未齐，不能追 |
| MA701 | 3464/3417 | +0.44%/+9.87%；39.63% | 2821383/913840/+9742 | MA611-12 +4.467%（非701 pair）；basis C | 3453，-0.32%/+1.05%；MA612 ATM IV50.38%、RR25 +2.42 | 原顺序条件未知/未完成，降级 |
| FU2701 | 5405/5305 | +0.19%/+10.61%；45.79% | 842314/257524/+2744 | near-next +16.328%；basis C | 广谱夜盘报道约+4%但无精确最终合约，不纳正式Night；无当期局部期权 | 高波动强曲线，不追 |
| EC2612 | 2688/2647.5 | -3.46%/-12.23%；52.57% | 8145/12823/+1976 | near-next -15.392%；basis不适用 | 无夜盘；无合格期权 | 趋势弱，等09:30而非预判 |
| AG2612 | 13010/13099 | +0.87%/-6.59%；30.90% | 374631/254824/-18173 | near-next -0.221%；basis C | 精确当前Night未认证；海外银约54.05、FOMC后偏弱；无局部期权 | 修复但趋势/宏观反对 |
| AU2612 | 867.4/870.06 | +0.74%/-2.25%；14.95% | 197994/188406/-2884 | near-next -0.278%；basis C | 当前精确Night未认证；海外金约4066；无局部期权 | 事件已落地，等待实际利率方向 |
| SH701 | 1448/1476 | -1.53%/-13.07%；16.44% | 935272/351629/+33697 | near-next +2.282%；basis C | 广谱夜盘仍弱；SH612 ATM IV39.50%、RR25 -2.31（错月） | 价格弱但近月升水，方向冲突 |
| LC2701 | 93300/96460 | -1.41%/-1.25%；39.36% | 398175/448923/+9791 | near-next +1.321%；basis C | 精确Night缺；无局部期权 | 日内大幅波动，证据仅一层 |
| LH2701 | 9840/9885 | +0.82%/-1.89%；18.78% | 204480/163204/-11511 | near-next -6.070%；basis C | 无制度夜盘；无局部期权 | 减仓反弹，不判趋势反转 |
| RB2701 / I2701 | 3043/3041；672/666 | +0.50%/-1.27%；+0.15%/-2.06% | RB ΔOI-10153；I -10831 | 曲线-0.294%/-0.299%；实体与basis不合格 | I广谱夜盘偏强但精确合约未核；期权执行缺 | 黑色链利润与需求未确认 |

板块未入榜异常：能源化工中EG日盘结算+5.63%、FU/BU曲线极强，但共同油价因子和参数缺口使其不能各算独立机会；黑色JM日盘+2.71%但钢矿5D仍弱；农产品无三层共振，M/Y仅小涨且豆粕曲线contango；新能源LC价格下跌伴OI上升只能作归因线索；贵金属FOMC后海外走弱，未形成方向新仓。

## 4. 相比前序的真变化与旧观点处置

1. **BU2701：71→75。** EOD强曲线后，精确夜盘fallback升至5140，Brent仍约115.3；新信息支持价格层和海外层，但EIA汽油大增与无Night curve反对追价。旧idea保留，参数改为日盘“确认后回踩”，不是把夜盘穿越回填成成交。
2. **SC2612：旧空68终止；新多子idea 72。** 旧空的核心条件是反抽失败且月差侵蚀；EIA后SC2612回到737.5、EOD backwardation仍正，旧方向逻辑已失效。新多必须用新ID并等待日盘曲线确认，不把方向反转抹成旧idea盈利。
3. **CU2612：72→70。** 夜盘最高109500低于109600，最终读数109240；CU2611-12约0.632%低于0.65%，两条硬条件均未满足。FOMC鹰派异议及海外铜仅微弱，保留研究、降低执行优先级。
4. **MA701：73→65。** 夜盘高点虽到3486，但最终3453且无法证明15分钟确认及其后回踩的顺序，PX与精确月差亦未同步核到。原窗口未完成，降为观察，不延长、不移动止损。
5. **EC2612：68不变。** EOD继续弱且contango深，但无夜盘、海外运价/实体缺失，维持两层证据观察空，不能在09:00前预判成交。

实际持仓状态均为“未提供/未知”；没有成交回执，不声明持有、减仓、退出或收益。

## 5. 产业链与传播路径

| 链条 | 强弱与传播 | 曲线/实体/期权 | Stock利润桥与最大缺口 | 置信度 |
|---|---|---|---|---|
| 原油→BU/FU/SC | 原油/馏分油去库与Brent强，先传SC，再传炼厂成本和BU/FU；汽油库存大增反映需求端反证 | BU/SC/FU均backwardation；EIA只算一个实体事件；三者期权执行不可用 | CNOOC九个月业绩10/30才发布；未核当前证券价与交易性，商品期货更直接 | 中高 |
| PX→TA→MA | EOD PX/TA/MA同涨，但MA夜盘较close回落，显示油价冲击未等比例传到甲醇 | MA曲线强；MA612 ATM IV50.38、RR25+2.42，但错月且无bid/ask | 化工企业的售价—原料—库存/套保桥缺数据；股票不是更好表达 | 中 |
| 铜矿→精炼铜→加工材 | 供应扰动先进入长端预期，CU EOD/OI偏强，但夜盘价格与曲线均未越阈值 | EOD和night backwardation均正；无CU局部期权面 | Teck Q3今夜美股盘前；产量/成本/指引才可能验证第三层，当前不能先算利好 | 中 |
| 铁矿/焦煤→钢材→钢厂利润 | I/JM短线反弹、RB弱，原料强于成材可能压缩吨钢利润 | 基差均C级，仓单跨所不完整；无期权执行面 | 宝钢Q3“原料涨幅快于钢价”仅沿用前序、非今晨新催化；股票表达含销量/库存/长协/套保滞后 | 中低 |
| 贵金属→实际利率/美元 | FOMC按兵不动但两票主张加息，海外金银走弱，国内修复缺海外确认 | 曲线轻contango；无当前局部期权面 | 无需股票替代，直接商品/ETF更纯；实际利率与美元精确07:00快照缺 | 中低 |

## 6. 统一机会榜

| 排名 | idea_id | 方向/期限/工具 | 五层支持/反证 | 逻辑25 | 赔率25 | 催化20 | 价曲波15 | 拥挤15 | 总分 | 研究/证据/执行 |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 | 条件多；1—3D；BU2701期货 | 支持1/2/4；缺3/5；反证为汽油累库、夜盘曲线缺 | 20 | 17 | 15 | 13 | 10 | **75** | 高优先/3层/仅条件 |
| 2 | COM-E-SC2612-POST-EIA-GAP-RETENTION-LONG-20261029 | 条件多；日内—2D；SC2612期货 | 支持1/2/4；缺3/5；反证为汽油累库、OI与Night curve缺 | 19 | 16 | 15 | 12 | 10 | **72** | 重点/3层/仅条件；父idea为旧空 |
| 3 | COM-M-CU2612-HVC-STRIKE-WATCH-20261025 | 条件多；3—10D；CU2612期货 | 支持1/2/3；4中性偏反对、5缺；阈值未齐 | 20 | 16 | 15 | 10 | 9 | **70** | 重点/3层/仅条件 |
| 4 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028 | 观察空；1—5D；EC2612 | 支持1/2；缺3/4/5 | 18 | 15 | 12 | 12 | 11 | **68** | 有效观察/2层上限/不可执行 |
| 5 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 | 中性偏多观察；日内—2D；MA701 | 支持2/5局部；价格层冲突，实体/海外缺 | 17 | 14 | 13 | 11 | 10 | **65** | 降级/2层/旧顺序未证实 |

得分仅表示研究优先级，不是胜率或仓位。五层严格去重；Night不新设第六层，EIA库存不在实体与海外重复计分。

## 7. 研究/交易卡（均为未来条件，不是订单）

### 卡1｜BU2701强曲线回踩多｜score 75

- **事实与分歧：** EOD close/settle=5054/4945；夜盘fallback=5140，较close +1.70%；EOD BU2611-12 backwardation 5.479%，Brent约115.3。市场已计价供应风险和原料成本；分歧是EIA原油/馏分油去库能否压过汽油+387万桶与高位获利回吐。
- **入场顺序（AND，缺一不可）：** 09:15后BU2701≥5120连续15分钟 **AND** 同时刻BU2611-12≥5.50% **AND** Brent≥115.0；其后才等BU回踩5070—5100且5分钟不破5050。09:00直接高开不追；首次可交易价>5200或曲线<4.5%放弃。
- **分批与好/中/坏成交：** 5080/5090/5100三种允许价；可实施整数手50%+50%。止损计划4990；逻辑失效为Brent<112.5或月差<4.5%。TP1=5220平50%，TP2=5360平余量；最迟10/30日盘收市退出。
- **确定性计算：** 10吨/手；tick 1元/吨、tick value 10元（交易所规则）；每手计划风险900/1000/1100元；TP1净费用前R=1.56/1.30/1.09，TP2=3.11/2.70/2.36。费用与滑点未实报，不当0；实盘需从上述R中扣除。
- **合约与压力：** BU2701最后交易日2027-01-15；当前交易所公告涨跌停12%、一般保证金14%、套保13%，名义价值约5.1万元/手、公告口径保证金约0.66—0.71万元/手。1/2个停板理论压力约0.61/1.22万元/手，实际可更差；止损不封顶。夜盘截止、交割与roll细则未在元数据完整核实，10/30退出规避交割。

### 卡2｜SC2612 EIA后缺口保留多｜score 72

- **状态修订：** 这是新子idea，父idea `COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026`已因价格和曲线反转终止。旧空不延长、不反向回填成交。
- **事实与分歧：** EOD close/settle=733.4/722.4，EOD SC2611-12 +0.706%；夜盘fallback 737.5（+0.56% vs close）；Brent约115.3。市场已计价原油去库/地缘溢价；主要反证是汽油库存大增、EIA成品需求数据弱。
- **入场顺序：** 09:15后SC2612≥738连续15分钟 **AND** 同时刻SC2612-2701≥0.75% **AND** Brent≥115.0；其后回踩733—736且不破730。首次价>745、月差<0.40%或Brent<113放弃。
- **好/中/坏成交：** 733/734.5/736；止损计划725；TP1=748平50%，TP2=760平余量；最迟10/30日盘收市退出。1000桶/手、tick 0.1元/桶、tick value 100元；计划风险8000/9500/11000元/手；TP1 R=1.88/1.42/1.09，TP2=3.38/2.68/2.18，均未扣未知费用滑点。
- **合约/压力：** 元数据最后交易日2026-11-30、最后交割日12-07；当前保证金/限幅/夜盘截止未在仓库核实，不猜。名义价值约73.5万元/手，单手风险高；若限幅或保证金上调，按账户可用资金重新缩减，止损不保证成交。

### 卡3｜CU2612供应扰动二次确认多｜score 70

- **事实与未触发：** EOD close=settle=109200；night=109240，high109500；CU2611-12约0.632%。原条件要求109600与0.65%，两者均未满足。FOMC鹰派异议与海外铜约14644使第四层不再积极支持。
- **入场顺序：** 09:15后CU2612≥109600连续15分钟 **AND** 同时刻CU2611-12≥0.65% **AND** LME三月铜≥14500美元；之后回踩109200—109400且不破109000。首次价>110200、LME<14250或曲线<0.40%放弃。
- **好/中/坏成交：** 109200/109300/109400；止损计划108300；TP1=111500平50%，TP2=113800平余量；10/30收市或Teck指引明显增供时退出。5吨/手、tick 10元/吨、tick value 50元；每手计划风险4500/5000/5500元；TP1 R=2.56/2.20/1.91，TP2=5.11/4.50/4.00，费用滑点未知。
- **参数与压力：** CU2612最后交易日2026-12-15；交易所细则最低保证金5%，但当前合约实际保证金/涨跌停可能更高且未核，不据此编保证金。名义约54.6万元/手。Teck Q3在北京时间约20:00前发布、23:00电话会，可能造成夜盘gap；若尚未成交，事件前不主动扩大Delta。

组合预算：每个试仓只用NAV 0.25%—0.75%计划止损风险，确认仓0.75%—1.50%；BU/SC同属油价因子合并，油链主题总预算≤2.5%，全组合高确信主题≤3.0%。无NAV与持仓账本，只给公式：手数=floor(允许风险金额/每手计划风险)。压力需另加1—2个停板、流动性消失、相关断裂、保证金提高、汇率与夜盘gap；计划止损绝非最大损失。

## 8. 商品期权专项

- 样本是`core_v1/sampled_strikes`，19/64产品、430合约；19个series core_ATM_ready，12个skew_ready。`quote_coverage_complete=true`只代表计划抽样合约取得，不代表全链。
- MA612（非MA701）ATM3550，ATM IV 50.385%，RR25 +2.42 vol、BF25 +1.985；标的期限错配且夜盘moneyness已变，只能说明局部上行翼略贵，不能直接为MA701交易卡计第五层执行证据。
- PX701 ATM9500、IV32.50%，skew不ready；SH612 ATM1540、IV39.50%，RR25 -2.31、BF25 2.185；后者标的错月且SH701价格弱/曲线强冲突，不做裸卖波动。
- BU、SC、CU、EC、AG、AU本次19个成功品种中均无对应当前局部面；这不是“市场没有期权机会”，只是未取得。
- 全局surface_ready=0、positioning_ready=0、execution_ready=0、bid/ask=0、dealer_gamma_direction_known=false。故不推全链PCR/拥挤、dealer gamma、期限或wing，也不编净权利金、Greeks成本、滑点或有限损性质。若询价，只有在同系列同到期双腿、净支出≤期货方案允许风险且成交价满足理论边界后，才能把看涨价差视作结构限损备选。

## 9. 9:00开盘风险地图

| 三层信息 | 可能开盘 | 不追价规则 | 09:15 / 09:30 / 09:45确认 |
|---|---|---|---|
| Previous China EOD | BU/FU/油化、CU偏强；EC/SH/LC偏弱 | EOD趋势不是今晨入场信号 | 先核主力是否roll、close/settle双锚和第一笔可交易价 |
| Current T Night | BU/SC强、CU近乎平、MA较close回落；其余因仓库失败不作正式Night证据 | BU>5200、SC>745、CU>110200不追；MA不沿用昨晚顺序 | 15分钟核价位；30分钟核near-next；45分钟核成交/OI只作线索，不判新多新空 |
| 07:00 Overseas | Brent约115.3；EIA原油/馏分去库、汽油累库；铜约14644；金银偏弱；FOMC有鹰派异议 | 海外与中国不同步只作映射，不能称套利 | 油链核Brent115/113；CU核LME14500/14250；贵金属等实际利率/美元再定方向 |

预判：BU/SC高开概率高于平开，但夜盘已计价大半，不适合开盘套保式追多；CU更可能平开至小幅高开；MA与贵金属偏平/低开。若09:45仍只有价格而无曲线/海外共振，所有条件卡继续等待，不因错过开盘而放宽阈值。

## 10. 未来24小时/7天事件与行动前清单

| 北京时间 | 事件 | 相关暴露 | 处理 |
|---|---|---|---|
| 10/29 20:30 | USDA周度出口销售 | M/Y/C/CF及CBOT映射 | 不用中国收盘后的报告反填日盘；夜盘前重核Delta |
| 10/29 约20:00；23:00电话会 | Teck Q3业绩及铜业务指引 | CU/LME铜、矿山供应 | 结果前CU只允许小试仓；指引增供则取消多单条件 |
| 10/30（公司日程） | CNOOC九个月业绩 | SC/油链、股票利润桥 | 仅将产量、实现价、成本、套保/汇率分拆后作为实体证据；不先验利好 |
| 10/31 03:30 | CFTC持仓报告（数据截至周二） | COMEX金银铜、能源、农产品 | 只作滞后拥挤验证，不当日内触发 |
| 11/1 | OPEC+七国月度会议 | SC/BU/FU/LU | 事件前减油链净Delta；期权执行不可用则用更小期货风险而非伪造限损 |
| 11/2 05:00 | USDA Crop Progress | C/M/棉花等 | 关注收获进度与天气，不用季节性单独立方向 |
| 11/4 | 下一次EIA周报 | 原油/成品油 | 油链若持有假设仓位，报告前减仓；Vega结构仍须实时报价 |

行动前覆盖：63/63指定代码完成初筛（LPG=PG），14个额外代码亦检查；实取得77产品/806合约；Physical A/B basis=0、夜盘0/806、Options19/64、DCE交叉核对失败均已局部隔离。未解决缺口是全市场精确Night、BU/SC夜盘曲线、现货/仓单高质量变化、期权bid/ask与动态保证金/限幅。前序五个稳定idea均已处置，SC换向保留父idea，未把OHLC穿越当触发/成交。

发布前实证检查：分项评分均未超25/25/20/15/15且加总正确；BU/SC/CU收益、曲线、每手风险和R已重算；合约单位与最后交易日已核，未知参数留缺；FOMC、EIA、Teck、OPEC+、CFTC、USDA日期均查原始来源。未通过的是全市场Night和执行报价，因此所有执行状态保持`not_ready`。

## 来源

- [China-Commodities-Engine：EOD期货](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)
- [External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)
- [Contract metadata](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)
- [Futures official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)
- [EIA weekly stocks, released 2026-10-28](https://www.eia.gov/dnav/pet/pet_stoc_wstk_dcu_NUS_W.htm)
- [Federal Reserve FOMC statement, 2026-10-28](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)
- [Teck Q3 2026 release schedule](https://www.teck.com/news/news-releases/2026/teck-to-release-third-quarter-2026-results-on-october-29%2C-2026)
- [OPEC+ 2026-11-01 meeting notice](https://www.opec.org/pr-detail/616-4-october-2026.html)
- [CFTC 2026 release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- [USDA weekly export sales schedule](https://fas.usda.gov/report-release-announcement/weekly-export-sales-300)
- [SHFE BU margin/limit adjustment](https://www.shfe.com.cn/publicnotice/notice/202610/t20261009_833667.html)
- [SHFE contract units](https://www.shfe.com.cn/reports/tradedata/)
- [INE contract units](https://www.ine.cn/reports/tradedata/dailyandweeklydata/?query_date=20261028&query_options=1&query_params=kx&query_product_code=sc_f)

## 11. 严格四行

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：BU2701、SC2612、CU2612，均须09:15后AND条件、再回踩、且不追高。  
C. 今天继续观察：EC2612、MA701、AG2612/AU2612，以及油化/黑色/农产品未形成三层共振者。  
D. 今天必须回避或有条件退出：回避把失效夜盘批次、旧IV或OHLC穿越当成交；若假设已建仓，按各卡止损/逻辑失效/10月30日时间退出，不默认实际持仓。
