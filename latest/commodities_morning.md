# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-14

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:09 BJT；信息截点：07:00；最近完整中国EOD：9月11日；今日为中国交易日。下一实际可交易窗口：9月14日09:00日盘；下一夜盘：9月14日21:00，归属9月15日交易日。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；外油跳涨且阿曼会谈推迟强化能源/航运右尾，但中国没有Current Night预定价，09:00首跳必须等待。**

当前regime：**中东能源—航运供给冲击、国内能源与集运深backwardation、周末信息待中国一次性定价、热通胀约束金属、WASDE对玉米偏多但接近预期。**

最接近触发的是FU2611、EC2610、SC2610；缺失条件依次为产品端相对原油继续强、EC对实际集装箱绕行而非油轮冲击的确认，以及SC高开后能否接受。09:00前均是研究候选，不是立即新仓。

## 二、数据质量与覆盖

第一层已读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并因前三卡合约核验下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)。

- 统一输入：schema v2，`requested_date=2026-09-11`，9月14日06:16:14生成。周一07:00以9月11日完整EOD为基准是正常的T-1组合。
- Futures：06:02重新核验；五所802合约、77产品，`source_date_match_pct=100%`、`full_market_ready=true`、critical module errors=0、excluded exchanges=0。4条OHLC placeholder已排除；20个交易日的同合约窗口完整。`official_complete=false`反映部分官方辅助模块不足，不否定核心期货质量闸门。
- Market State：1D/3D/5D/20D均为同一具体合约；部分volume/OI/curve z-score和near-next pair缺失，不猜测。
- Physical：06:15刷新，20项中18项按原生频率fresh、SC/LU unavailable；本期不是18条新观测的统称。5条仓单沿用；basis模块不可用，旧C级现货差仅作context，不能称套利。
- External：06:15刷新到9月11日国际最后完整时段，17/22可用、5项unavailable，全部`context_only`。另以公开市场补充9月14日亚洲开盘后的ICE Brent/NYMEX WTI；LME、COMEX、CBOT、ICE软商品、SGX、DXY、USD/CNH与实际利率若尚无同一时点可核实新成交，沿用周五收盘并明确非实时。
- Options：最新有效完整截面为9月11日，23,272条chain、384个series、59/64产品；CJ/MA/PL/PR/ZC失败。373个series局部surface-ready、78个positioning-ready、0个execution-ready；IV覆盖98.07%、OI覆盖69.35%、bid/ask和模型Greeks覆盖均为0。机器`data_fresh=false/published=false`来自周末无新截面；9月11日仍是07:00最新应得EOD，只能研究，不能替代当前报价。
- Contract Metadata：partial；核心合约有效匹配约73.32%，交易参数覆盖约29.8%。DCE合约参数接口失败、GFEX源日期未匹配；前三卡缺项逐项标出。

**Night质量闸门：** `trading_date=2026-09-14`、`night_session_date=2026-09-13`、06:02:03生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=true`。selected/requested均802，`night_session_contract_count=0`、product count=0、outside-window=802；missing timestamp/price/quote、query error、unresolved contract均为0，warning为空。周日夜间制度上没有这段中国商品连续交易，因此0条是日历语义结果，不是截断、空文件或fallback失败；`night_session_fallback_used=false`，不做Night curve和隔夜分解。

## 三、商品仪表盘

以下EOD、1D/5D、量仓和curve均截止9月11日；Night OHLC、双收益锚、ΔOI和source timestamp因本次无合法session统一为N/A。S/P/E为期权surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Basis/Physical | Current Night | 07:00 Overseas；Options | 09:00信号 |
|---|---|---|---|---|---|---|
| 燃料油FU | FU2611；4289/4292；+4.66%/+10.85% | 139.93万/22.09万/+4,920；back 8.69% | basis缺；现货仅context | N/A；无合法session | Brent 108.23；Y/Y/N | 高开不追，产品强于SC才多 |
| 原油SC | SC2610；812.9/809.9；+5.40%/+18.56% | 30.53万/3.50万/+697；back 7.03% | basis/Physical缺 | N/A；无合法session | WTI 103.20；SC2611 Y/N/N | 等45m接受，不把外油涨幅机械映射 |
| 集运EC | EC2610；2032/2044；+4.18%/+10.10% | 3.29万/2.59万/+2,200；back 22.36% | exact运价缺 | 制度无Night | Hormuz/Perim事件；N/N/N | 高开不追，等集装箱路径确认 |
| 低硫燃油LU | LU2611；5453/5487；+4.53%/+10.85% | 22.06万/7.68万/+2,433；back 1.88% | basis/Physical缺 | N/A | 外油跳涨；新期权未就绪 | FU相对优先 |
| 铜CU | CU2610；108990/108660；-2.75%/-0.41% | 20.93万/19.89万/-35,215；back 0.65% | C级context | N/A | LME周五14225.5，非周一实时；Y/Y/N | 反抽失败才空 |
| 白银AG | AG2612；15623/15676；-4.76%/-4.09% | 17.32万/19.34万/+8,788；contango 0.76%、roll | C级context | N/A | COMEX周五约64.3；Y/N/N | 换月后不追空 |
| 黄金AU | AU2612；944.94/944.54；-1.36%/-2.93% | 10.48万/15.84万/+7,777；轻contango | C级context | N/A | 金周五约4350；Y/N/N | 避险/实际利率冲突 |
| 碳酸锂LC | LC2701；134820/133960；-5.60%/-8.90% | 32.27万/40.76万/-1,124；back 1.68% | C级；仓单沿用 | 制度无Night | exact外盘缺；Y/N/N | 不接第一刀、不追空 |
| 玻璃FG | FG701；973/984；+2.29%/+1.34% | 218.62万/115.50万/-41,191；contango 7.37% | C级context | N/A | exact外盘缺；Y/Y/N | 挤压与contango冲突 |
| 焦煤JM | JM2701；1585/1612.5；-1.77%/-3.47% | 87.37万/48.67万/-38,125；back 1.67% | C级context | N/A | exact外盘缺；Y/Y/N | 不追减仓下跌 |
| 红枣CJ | CJ701；7580/7630；-2.43%/-3.05% | 20.17万/22.52万/+3,946；contango 15.38% | CZCE仓单-261 | 制度无Night | chain失败 | 弱价需实体确认 |
| 豆粕M | M2701；3402/3422；+0.68%/+0.59% | 193.71万/273.38万/-51,707；contango 0.82% | C级context | N/A | CBOT周五收盘沿用；Y/Y/N | WASDE后等45m |
| 玉米C | C2611；2255/2260；-0.40%/-1.61% | 46.69万/116.20万/-16,426；back 0.22% | C级context | N/A | USDA减产近预期；Y/Y/N | 首个中国确认，涨跌均不追 |
| 棕榈油P | P2701；10035/10151；-0.26%/-0.60% | 70.48万/58.33万/-7,195；contango 1.52% | C级context | N/A | BMD周五4816；Y/Y/N | 无方向优势 |
| 苯乙烯EB | EB2610；10036/10303；+0.20%/+6.47% | 170.59万/25.50万/-66,811；contango 0.68% | C级context | N/A | 成本上行、需求未知；Y/Y/N | 与FU相对强弱最重要 |

截至亚洲交易开始后，ICE Brent约**108.23美元/桶**、NYMEX WTI约**103.20美元/桶**，较周五结算分别上涨3.62和3.15美元；原定周一的阿曼—海湾—伊朗会谈已推迟。沙特East-West管道仍无恢复确认，叠加Hormuz船只受袭，说明周末事件已获外油价格确认，但中国尚未交易。[Reuters油价，2026-09-14亚洲开盘](https://www.reuters.com/business/energy/oil-prices-jump-more-than-3-after-new-strikes-saudi-strait-hormuz-2026-09-13/)｜[Reuters会谈推迟，2026-09-13](https://www.reuters.com/world/middle-east/oman-meeting-between-gulf-states-iran-postponed-omani-foreign-minister-says-2026-09-13/)

## 四、相比上一期真正变化

1. **外油完成第一轮周末补价。** Brent/WTI分别较周五结算高3.62/3.15美元；能源链第4层由“事件未定价”升级为“海外价格确认”，但不能写成SC/FU已经上涨。
2. **外交缓和窗口后移。** 阿曼会谈被推迟且无新日期，SC/FU/EC催化持续性上升；同时headline高开后回吐的竞争解释仍强。
3. **Current Night正确为0。** 9月14日交易日没有9月13日晚合法中国连续交易，802个合约全部outside-window；这是日期制度，不是行情或pipeline错误。
4. **核心期货last-good重新核验成功。** 五所802合约、100%同源日期、零critical error；价格本身仍是9月11日，不冒充周一行情。
5. **期权、Physical和仓单无周末新增。** 9月11日surface可继续研究，但油价跳变使FU/SC moneyness、Delta与IV-RV可比性下降；所有执行结构09:00后必须重新报价。
6. **金属与农产品缺少同一时点新增确认。** CU空与C多均维持观察，不能因油价或WASDE叙事提高分数。

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：77→78；新增原因=外油价格确认与会谈推迟，赔率因潜在高开不升。原始触发/止损/退出不变。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：77→78；新增原因=双航道风险持续，但油轮冲击并非EC exact集装箱证据。
- `COM-E-SC2610-GAP-20260905`：74→75；海外确认增强，然而方向最拥挤、追价赔率最差。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：67→66；无LME周一同一时点确认，国内back仍为反证。
- `COM-M-C2611-WASDE-CORN-20260912`：56→55；报告已成为已知信息，等待中国价格、OI、curve确认。
- 没有成交反馈，不假设用户持仓。若此前确已建立能源多头，09:00 gap先计入总主题风险，不机械加仓。

## 五、产业链地图

- **最强：FU—SC—LU能源供应链，偏多尾部，置信度中高。** EOD价量仓、back与周一外油跳涨形成1/2/4层支持；SC/LU实体缺失、无Current Night及可能需求破坏是反证。FU若强于SC且EB/BZ/TA不跟，产品端相对价值优于链条普涨。
- **航运EC：偏多但映射有边界，置信度中。** EC深back和OI增加支持，Hormuz/Perim风险延长绕行；最大缺口是EC对应集装箱航线、现货运价与合约参数，不能把油轮费率当EC套利。
- **有色—贵金属：偏弱但不追空，置信度中低。** CU价跌仓减与海外政策支持回吐，国内back和缺周一LME确认反对；AU/AG同时受避险与实际利率影响，黄金信用主题仍无独立模型闭环。
- **黑色—新能源：最弱价格链但证据冲突，置信度中低。** LC大跌但OI仅小降、curve仍back；JM弱价与back冲突。单日跌幅不是实体需求崩塌证据。
- **农产品：玉米偏多先验，大豆油脂中性，置信度低。** WASDE属于C的实体层，但接近预期；M/P/Y/OI没有exact进口平价和周一电子盘同一时点确认。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 24/13/20/13/8 | **78** | 1、2、4 | 存在待验证优势｜部分｜等待09:30—09:45触发 |
| 2 | EC2610航运冲击多 | 24/14/20/12/8 | **78** | 1、2、4 | 存在待验证优势｜部分｜等待09:30日盘触发 |
| 3 | SC2610高位接受多 | 24/9/20/13/9 | **75** | 1、2、4 | 存在待验证优势｜部分｜等待09:45触发 |
| 4 | CU2610关税溢价回吐空 | 19/15/13/9/10 | **66** | 1、4 | 存在待验证优势｜部分｜反抽失败才空 |
| 5 | C2611 WASDE玉米减产多 | 16/13/13/5/8 | **55** | 3 | 证据不足｜不足｜等待中国价格确认 |

分项均已复算，未超过各分项上限。分数仅是研究优先级，不是胜率或仓位。FU/SC/LU/EC共享中东供应—运输因子，不能作为独立交易叠加风险；C只有一个支持层，严格低于59。前三个期货的最大损失都不由结构限定。

## 七、前三名交易卡

### 1. FU2611｜条件多｜78

**事实：** 9月11日previous close/settlement=4289/4292，OHLC=4268/4417/4201/4289，ΔOI +4,920，back 8.69%。Current Night不存在：OHLC、close、return vs close、return vs settlement、Night ΔOI、source timestamp均N/A。海外Brent约108.23。

**市场定价：** 周五已计入产品紧张，周一外油再计入管道和Hormuz冲击。**推断/分歧：** FU可能比SC更能保留成品油稀缺溢价；最强反证是周五仅为成本滞后补涨，管道恢复会令back和价格同步回吐。支持层1/2/4，实体与期权执行层缺失。

- 最佳表达：单腿FU2611条件多，1手为一单位；不是delta-neutral或beta-neutral篮子。
- 入场：09:00首跳不追。好成交=09:30—09:45在4210—4260获接受并重上4295/VWAP，先1/3；中成交=突破4418后回踩成功，仓位减半；坏成交=直接高于4450、滑点>计划1R的20%或流动性明显变薄，放弃。
- 止损/失效：30分钟接受4190下方止损；跌破4100、back明显收窄且Brent<100，或管道恢复并伴随产品裂解溢价回落则逻辑失效。
- 退出：TP1=4420或+1.5R，减半；TP2=4600或+3R；1—3D不扩张全部退出。催化=1—5D管道修复、航运与EIA产品库存。
- 最大风险：试仓0.20%—0.35% NAV；期货最大损失不有限。最坏情景=高开后headline反转、流动性消失或连续跌停。
- 参数：10吨/手，tick=1元/吨，tick value=10元；结算名义=42,920元。margin与当日price limit未确认；夜盘制度通常21:00—23:00但本次09:00前无Current Night；最后交易日2026-10-30，实物交割。10月中旬前移仓，交割月前退出非交割意图仓位。
- 压力：若限幅为L，一板=`42,920×L`，两板复合=`42,920×[1-(1-L)^2]`；参数未确认前不写伪精确金额。

### 2. EC2610｜条件多｜78

**事实：** 9月11日previous close/settlement=2032/2044，OHLC=2015.5/2108/1976/2032，ΔOI +2,200，back 22.36%。EC制度上无Night，所有Night字段N/A。Hormuz袭船、Perim及沙特管道风险支持绕行时间尾部，但不等于EC对应航线现货运价已上涨。

**市场定价：** 近端运力稀缺已被深back部分计价。**分歧：** 外交会谈推迟可能延长风险；最强竞争解释是油轮与集装箱暴露不一致。支持层1/2/4，exact Physical、期权和参数缺失。

- 最佳表达：单腿EC2610条件多，1手为一单位；无可靠对冲比率，不构造伪中性篮子。
- 入场：09:00首跳不追。好成交=09:30后1990—2035获接受并重上2045/VWAP；中成交=突破2110并回踩不破，仓位减半；坏成交=直接高于2160，放弃。
- 止损/失效：30分钟接受1970下方止损；跌破1962、back明显收窄且通航/管道恢复则失效。
- 退出：TP1=2150或+1.5R；TP2=2300或+3R；1—5D无运价或curve扩张退出。催化=1—10D实际绕行、班轮公告、运价指数与港口拥堵。
- 风险：0.20%—0.35% NAV，与FU/SC/LU合并。最坏情景=消息澄清后低开/跌停、指数现货与合约脱节、深back快速坍缩。
- 参数：repo未确认multiplier、tick、tick value、margin、price limit、最后交易日和现金结算细节；EC无夜盘。上述参数及一板/两板压力金额在下单前按INE最新规则核实，当前不编数。交割/结算与移仓风险使近交割期仓位必须提前退出。

### 3. SC2610｜条件多｜75

**事实：** 9月11日previous close/settlement=812.9/809.9，OHLC=815/838.3/786.5/812.9，ΔOI +697，back 7.03%。Current Night不存在，OHLC、双收益锚、ΔOI和Night价格弹性均N/A；Brent/WTI周一亚洲开盘约108.23/103.20。

**市场定价：** 高供应中断溢价与拥挤已在价格和back中。**主观判断：** 海外新增确认支持方向，但09:00跳空后的赔率差于FU；最强反证是中国需求弹性、人民币变动与交易所风控会限制跟涨。支持层1/2/4，Physical和执行期权缺失。

- 最佳表达：单腿SC2610条件多，1手为一单位；不拿SC2611期权冒充同底层有限损失表达。
- 入场：09:00不追价，至少等45分钟。好成交=790—810承接并重上813/VWAP；中成交=突破838.5后回踩成功、仓位减半；坏成交=直接高于850、接近涨停或止损距离>1R，放弃。
- 止损/失效：45分钟接受786下方止损；跌破768.4、back明显收窄、Brent<100且管道恢复则失效。
- 退出：TP1=840或+1.5R；TP2=875或+3R；1—2D不扩张退出。催化=1—7D管道状态、Hormuz运输、EIA和中国成品油传导。
- 风险：0.20%—0.30% NAV，与FU/LU/EC合并；最坏情景=海外冲高回落、中国高开跌停、保证金上调与交割流动性消失。
- 参数：1,000桶/手，tick=0.1元/桶，tick value=100元；结算名义=809,900元。最后交易日9月30日、实物交割，最迟9月18日前复核移仓SC2611；夜盘通常21:00开。部分SC/LU风控自9月14日夜盘起调整，下单前核实保证金、限幅和开仓限制。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)｜[风控摘要](https://www.reuters.com/business/energy/shanghai-exchange-adjust-trading-limits-some-oil-futures-contracts-2026-09-11/)
- 压力：按16%假设，一板约129,584元/手；两板复合约238,435元/手。该压力损失与计划止损风险分开。

## 八、商品期权专项

最新有效样本为9月11日EOD，本期无新截面；周一外油跳变使能源期权的当前moneyness、Delta、Greeks与成本不可沿用。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 研究结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 64.47%/43.35% | +21.11vol | -3.19/-0.62 | Y/Y/N | event convexity已贵；当前价差成本未知 |
| SC2611/10-14 | 60.92%/41.07%代理 | +19.84vol | -1.68/+2.16 | Y/N/N | 非SC2610同底层，仅context |
| CU2610/09-23 | 15.17%/14.80% | +0.36vol | +0.80/+1.89 | Y/Y/N | IV-RV近零不证明可成交便宜 |
| AG2612/11-24 | 51.14%/35.16% | +15.98vol | +6.33/+8.34 | Y/N/N | 上行尾偏贵，positioning不足 |
| LC2701/12-07 | 43.64%/38.62% | +5.02vol | 未稳定 | Y/N/N | 需按09:00标的重算Delta |
| FG701/12-11 | 21.93%/18.86% | +3.07vol | +7.89/+3.29 | Y/Y/N | 无bid/ask，不能评执行赔率 |

若09:00后取得人工双边报价，可比较FU2611 10月Delta约35—55的牛市价差与期货：买低执行价call、卖等量高执行价call，1:1；最大净支出=最大损失。但当前执行价、权利金、盈亏平衡、Greeks、滑点和行权交割参数均待报价，**不是可执行卡**。禁止裸卖event vol，禁止从OI推断Dealer Gamma方向。vol RV只保留研究层，暂无可靠可成交跨期限/跨品种波动套利。

统一状态：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月11日；②Current Trading Day Night Session=无合法记录；③07:00 Overseas=外油已跳涨，其他主要市场按可核实的周五最后价格。中国没有预交易周末信息。

| 品种 | EOD → Current Night → 07:00 Overseas | 预期开盘/定价 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| FU/LU | 强back → 无 → Brent +3.62美元 | 偏高，信息未在中国预交易 | 不追；30—45m | FU 4210/4295/4418、产品强于SC、back |
| SC | +5.4%/back7% → 无 → WTI +3.15美元 | 高开概率高；海外先定价 | 不追；45m | 786/810/813/838.5、Brent/人民币、curve |
| EC | +4.18%/back22% → 制度无 → 航运事件持续 | headline高开，exact映射不足 | 不追；30m | 1970/2045/2110、实际集装箱绕行与curve |
| EB/BZ/TA/PX | 周五弹性衰减 → 无 → 原油上行 | 高开后链内分化 | 不抄底/追涨；45m | settlement、OI、curve breadth、FU/SC |
| CU | 国内跌且back → 无 → LME周五价沿用 | 平/低开后反抽风险 | 不追空；45m | 108180/109200、LME开盘、back、USD/CNH |
| AG/AU | 中国跌/换月 → 无 → 周五海外反弹 | 可能修复，双因子冲突 | 两边不追；30—45m | DXY、10Y、实际利率、换月价差 |
| C/M/Y/P/OI | 中国未交易WASDE → 无 → 周五美盘已消化 | 方向不确定 | 45m | 中国gap、OI、near-next、CBOT/BMD |
| LC/PT/PD | 急跌、实体不足 → 无 | 宽幅双向 | 不接第一刀；45m | OI、curve、GFEX仓单有效期、风控 |
| FG/JM/RB | 价格与curve冲突 → 无 | 震荡/偏弱 | 30—45m | FG963/1010、JM1580、黑色breadth |
| AP/JD/SF/SM/SI/PS | 无制度Night、无exact海外映射 | 国内信息主导 | 30—45m | 量仓、curve、实体更新 |

外油与中国周五EOD同向，但新增涨幅尚未被中国Night吸收；因此能源首跳信息弹性可能最高，也最容易出现高开低走。人民币若因油价和避险走弱，会抬高进口成本；截至截点缺同一时点可核实USD/CNH变动，不给伪精确贡献率。

## 十、未来24小时与7日事件

- **9月14日09:00：中国商品日盘重开。** FU/SC/EC至少延迟30—45分钟；只在价格、curve和量仓同步时给Delta。
- **9月14日09:30：中国流通领域生产资料价格窗口。** 仅在地区、品质、含税与日期可比时进入Physical层。[国家统计局](https://www.stats.gov.cn/)
- **阿曼会谈已推迟、无新日期。** 未来24小时核验East-West管道修复、Hormuz/Perim通航与Saudi出口；恢复消息会压缩能源与航运溢价。[Reuters](https://www.reuters.com/world/middle-east/oman-meeting-between-gulf-states-iran-postponed-omani-foreign-minister-says-2026-09-13/)
- **9月14日21:00：** 下一合法夜盘，归属9月15日；SC/LU交易参数变化前复核限幅、保证金与开仓限制。
- **9月15日10:00附近：中国工业、投资、消费、房地产及能源生产数据。** 工业品在发布前合并降低方向风险。
- **9月16日22:30附近：EIA周报。** 关注原油/成品油库存、炼厂开工、出口与战略库存；FU/SC宜延迟入场或以有限凸性处理。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **9月17日02:00附近：FOMC决议及SEP。** CU/AU/AG在事件前降低Delta/Vega，不把油价驱动通胀单独当方向。[美联储日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- **未来7日：** USDA之后转向美国天气、出口销售与中国采购兑现；CFTC COT只作滞后拥挤背景，不映射成中国会员确定方向。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)｜[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月11日last-good的同合约1D/3D/5D/20D、量仓、curve，以及方向、基差、跨期、跨品种/跨市场、风格/中性、波动率、偏度和事件凸性初筛；另纳入BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态品种，共77个产品。没有把提到名字等同于完成分析：逐品种扫描状态以可用价格、历史窗口、curve、Physical、External和Options模块交叉核验。

- 实际取数且有效分析70个；JR/PM/RI/WH/ZC为零价/零量/零OI占位，RS/WR流动性不足；均保留覆盖记录。
- 黑色建材9/9：FG深contango、JM价曲冲突为未入榜异常；无三层同向优势。
- 有色贵金属12/12：CU低分入榜；AG/AU的避险与实际利率冲突，无可执行信用/黄金主题。
- 能源炼化化工25/25：FU/SC入榜；LU相对FU弱，EB/BZ/EG/TA/PX成本扩散弹性不足。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺新增实体、仓单有效性和exact海外确认。
- 农产品油脂饲料畜牧22/22：C为低分WASDE观察；M/P/Y/OI等待中国price/OI/curve确认。
- 航运与软商品全部扫描：EC入榜；CJ弱价、深contango与仓单下降相互冲突。
- Night应得记录=0、实际有效=0，不缩小全品种覆盖；Options应覆盖64、实际59、5个失败、0个execution-ready。
- 策略类别：方向、基差/跨期、curve、跨品种、跨市场、风格/中性、波动率/偏度/事件凸性及1—20D周期均已扫描；A/B级basis、exact import parity、可靠加工利润、完整beta-neutral篮子和可执行期权报价不足，故不发布伪套利。

风险预算：单笔试仓最大损失0.20%—0.35% NAV；只有新增中国价格、curve和非价格层确认后，才考虑0.75%—1.0%。FU/SC/LU/EC共享主题初始合并风险≤0.75%，确认后总主题风险仍≤2.5%。压力测试含1/2个涨跌停、周末gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、人民币急变与管道突然恢复。

固定六路径已从main回读验证：历史MD/JSON存在，latest日期与edition正确，status对应本期，manifest中`2026-09-14 + commodities_morning`恰好一条。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-14_commodities_morning.md) `archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：FU2611在09:30—09:45于4210—4260承接并重上4295，或EC2610在09:30后1990—2035承接并重上2045；SC2610仅09:45后790—810承接并重上813，三者合并风险≤0.75%。  
C. 今天应继续观察的机会：FU相对SC强度、EC实际集装箱绕行与back、CU反抽失败、C2611对WASDE的中国价格确认，以及09:00后能源期权重新报价。  
D. 今天必须避免或退出的交易：09:00追FU/SC/EC首跳、把不存在的Current Night写成缺失行情、把油轮冲击当EC exact套利、追空CU/AG/LC，以及在execution-ready=false时臆测权利金、Greeks或最大损失。
