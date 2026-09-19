# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-20

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：2026-09-20 07:18 BJT；信息截点：07:00。今天为周日，中国商品市场休市；最近完整中国EOD为9月18日，下一实际日盘为9月21日09:00。周日不存在新的中国夜盘或海外商品收盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；周末袭击重抬能源与航运gap右尾，周一首选EC确认而非追SC，LU/SC与SC空头均降级。**

当前regime：**周末价格发现真空 + 沙特设施袭击风险重新升温 + 原油风险溢价与成品油紧张并存 + 贵金属韧性 + 中国内需偏弱。**

最接近补证的是EC2610事件gap接受多、AG2612回撤接受多、LU2611/SC2611相对价值。三者分别缺exact运价与实时参数、可执行期权报价、以及合法归属的周五Night与周一两腿curve。任何周五或周六数值条件均不是当前委托。

## 二、数据质量与覆盖

本期第一读取层为[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)；按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- **统一输入：** schema v2，`requested_date=2026-09-18`，9月20日06:14:34生成。周末以最近完整交易日为requested date是正确语义。
- **Futures：** 9月18日五所806合约、77产品，9月20日06:03重新核验；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0，4条placeholder排除。
- **Market State：** 77产品均进入同合约1D/3D/5D/20D扫描；70个产品有可用趋势、量仓与curve。短历史与roll产品不强算z-score。
- **Physical：** 9月18日观测，9月19日06:18生成；`data_fresh=true`、validation passed、published，18/20序列有效，SC/LU unavailable。所有basis为C级或缺失，因地区、品质、税费和交割地未对齐，仅作context。
- **External：** 9月18日观测，9月20日06:13生成；17/22 fresh、5项unavailable，全部`context_only`。repo WTI/Brent 95.47/99.03与可靠近月结算100.30/103.87冲突，油价代理已隔离；LME、COMEX、CBOT、ICE、SGX值仅作周五EOD背景。
- **Options：** 最新仍为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready，IV/OI/bid-ask覆盖99.11%/69.50%/0。相对最新应得9月18日截面已经落后，只作历史研究。
- **Metadata：** partial；合约匹配67.49%，multiplier/tick/margin/limit覆盖30.15%，last-trading-day覆盖67.49%；空字段未推断。

### Night Session质量闸门

9月20日05:58的Night状态原样为：

- `trading_date=2026-09-20`
- `night_session_date=2026-09-19`
- `data_fresh=false`
- `validation_passed=false`
- `published=false`
- `coverage_complete=false`
- 0条有效Night、592条outside-window、214条query error、214条unresolved
- validation error：没有具体合约在所列窗口取得报价
- `previous_valid_snapshot_retained=true`

9月20日是周日，制度上本就不应产生新Night。该失败不使周五EOD失效。统一输入仍保留一批原始标记为`trading_date=2026-09-19`的423条记录，但9月19日同样是周六；按交易所日历，周五晚连续交易应归属9月21日。由于字段违反日历语义，记录整体隔离，**不自行重标、不计方向证据**。[INE交易规则](https://www.ine.cn/eng/services/rules/rulebook/202202/t20220222_821734.html)

当前没有可靠exact-contract外部fallback，`night_session_fallback_used=false`。因此无有效Night curve，所有应有夜盘的候选最高79分。下表仅披露隔离快照的原始值供审计，不把它冒充有效市场证据。

## 三、商品仪表盘

1D/5D为9月18日同合约结算收益；curve为near-minus-next期货曲线，不是现货基差。Night栏标“隔离”的记录均不参与评分。海外栏为周五最终价格或周末事件，不是周日实时行情。S/P/E为surface/positioning/execution readiness。

| 板块 | 品种/合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | Physical/basis | 隔离Night close；vs close/vs settle；ΔOI；时间 | 07:00海外/事件；Options；信号 |
|---|---|---|---|---|---|---|
| 航运 | EC2610 | 2172.5/2189；+2.99%/+7.09% | 2.54万/2.53万/-1,176；back 21.29% | exact运价缺 | 制度无Night | Riyadh/Yanbu袭击风险；N/N/N；周一gap接受 |
| 能源 | SC2611 | 728/754.4；-6.29%/-0.30% | 28.52万/4.22万/-2,115；back 1.59%、z-2.49 | SC缺失 | 734.8；+0.93%/-2.60%；-1,246；9/19 02:30，隔离 | Yanbu设施遇袭主张未获损害确认；Y/N/N；双向gap |
| 能源 | LU2611 | 5440/5515；-2.10%/+0.51% | 15.64万/7.14万/+1,703；back 4.79%、z2.30 | LU缺失 | 5589；+2.74%/+1.34%；+2,847；9/18 23:00，隔离 | 原油尾部重升；无执行面；相对SC降级 |
| 能源 | FU2611 | 4200/4259；-3.29%/-0.77% | 81.04万/19.09万/-12,686；back 12.80% | 现货7525、C | 4297；+2.31%/+0.89%；+1,597；隔离 | 深back与事件支持、Friday价格反对；Y/N/N |
| 贵金属 | AG2612 | 16304/16104；+2.79%/+2.73% | 16.59万/21.50万/+8,244；contango 0.12% | C/context | 代表AG2610，合约错位且隔离 | 银66.556、地缘升温；Y/N/N且skew异常；回撤接受 |
| 贵金属 | AU2612 | 951.38/946.18；+0.96%/+0.17% | 11.96万/19.75万/+13,041；轻contango | C/context | 代表AU2610，合约错位且隔离 | 金4385.90、高收益率反对；N/N/N；不追 |
| 有色 | CU2610 | 109620/109530；+1.31%/+0.80% | 8.10万/15.19万/-7,625；back 0.33%、短历史 | 现货110235、C | 109900；+0.26%/+0.34%；-766；隔离 | LME铜14562 proxy；N/N/N；减仓反弹 |
| 聚酯 | TA701 | 6238/6312；-2.86%/0.00% | 136.76万/117.12万/+10,883；back 2.14% | 现货7108.8、C | 6304；+1.06%/-0.13%；-25,427；隔离 | 新能源事件反对继续追空；Y/Y/N |
| 聚酯 | PR611 | 8132/8244；-3.06%/+1.10% | 10.10万/6.16万/-1,405；back 1.58% | 缺失 | 8228；+1.18%/-0.19%；-1,504；隔离 | 成本方向不确定；Y/N/N |
| 农产品 | RM701 | 2357/2389；-1.32%/+0.84% | 60.64万/60.82万/+5,568；contango 0.92% | C/context | 代表RM611，合约错位且隔离 | CBOT豆1302.75；Y/Y/N；旧多失效 |
| 农产品 | M2701 | 3397/3429；-1.47%/+0.21% | 204.64万/273.12万/-196,992；contango 1.10% | 现货3448、C | DCE query_error | CBOT粕351.1；失败产品；等待量仓 |
| 建材 | FG701 | 907/912；+0.55%/-7.32% | 108.62万/129.52万/-70,452；back 3.70% | 现货1008、C | 910；+0.33%/-0.22%；-2,559；隔离 | 无exact外盘；局部Y/Y/N；噪音 |
| 新能源 | LC2701 | 127160/128460；-1.28%/-4.11% | 18.69万/42.54万/+9,528；back 1.25% | 现货130000、C | 制度无Night | 无exact海外；Y/N/N；不追空 |

隔离快照中，SC相对前收+0.93%、相对结算-2.60%，方向相反，只能说明前收与结算锚差异很大；不能据此宣称周一已完成利多定价。LU与FU相对前收涨幅明显高于相对结算涨幅，也不能在日历错误下升级为支持证据。

周六胡塞武装袭击利雅得，沙特方面称针对利雅得及延布等地的多次袭击被拦截；胡塞方面宣称攻击延布Aramco设施，但截至截点没有设施受损的独立确认或Aramco说明。这是**周一能源与航运的新增gap右尾，不是已经成交的油价**。[Reuters](https://www.reuters.com/world/middle-east/saudi-civil-defence-sends-all-clear-after-danger-warning-capital-riyadh-2026-09-19/)｜[AP](https://apnews.com/article/b1286cad816dd3e553f50f6dd5205972)

周五WTI/Brent结算约100.30/103.87美元/桶，仍体现供应溢价回吐；周末袭击使“延续下跌”与“事件跳涨”成为竞争情景。[WSJ油市](https://www.wsj.com/finance/commodities-futures/oil-falls-as-worries-over-middle-east-supply-disruptions-ease-36be861a)

## 四、相比上一期真正变化

1. **核心数据状态修复而行情未变。** Futures以9月18日重新核验，五所完整、critical errors归零；Physical恢复为fresh/published 18/20。没有新的中国价格。
2. **Night新增运行正确失败。** 周日窗口0条报价并明确validation failure、保留previous snapshot；这比把无交易日数据写成fresh更符合实际，但不能修复周五夜盘标签错误。
3. **周末地缘成为唯一方向性新增。** Riyadh遭袭，Yanbu Aramco设施被宣称为目标；损害未确认，因此只提高gap尾部与催化分，不直接判定SC必涨。
4. **EC升为第一研究候选。** 周五价涨、深back与新运输事件形成三层支持，但OI下降、exact运价和交易参数缺失，仍不具备当前执行条件。
5. **SC空头和LU/SC相对交易降级。** 新袭击直接威胁SC短腿；`COM-M-SC2611-REVERSAL-20260917`停止作为单向空卡，转为双向gap问题。`COM-M-LUSC-RELATIVE-20260918`由79降至68。
6. **政策边际仍偏弱需求。** 央行货币政策委员会委员黄益平周六强调强供给、弱需求及修复资产负债表的必要性；这支持内需链中期谨慎，却不是周一即时交易触发。[Reuters](https://www.reuters.com/world/asia-pacific/china-central-bank-adviser-says-ai-could-deepen-supply-demand-imbalance-2026-09-19/)

旧建议台账：

- `COM-M-EC2610-FREIGHT-REPRICE-20260918`：66→74；变更原因=新地缘事件，但仍待exact运价与周一价格确认。
- `COM-E-AG2612-PRECIOUS-REBOUND-20260918`：69维持；新增地缘支持被高收益率、contango与期权异常抵消。
- `COM-M-LUSC-RELATIVE-20260918`：79→68；新袭击伤害SC短腿，外部层从支持转为反对。9月19晨报重复ID后缀视为台账纠错，沿用最早ID。
- `COM-M-SC2611-REVERSAL-20260917`：76→停止单向空头；周一只做gap接受/失败后的新评估。
- `COM-M-FU-REBOUND-20260919`：74→67；深back和事件支持，但Friday价格层及Night缺失反对。
- RM旧多继续退出；没有成交反馈，不假设用户持仓。

## 五、产业链地图

- **航运EC：偏多研究，置信度中。** Friday价涨、21.29% back及Red Sea/Saudi事件支持；OI下降、无exact运价、无夜盘和参数缺失是主要反证。
- **SC—LU—FU：双向高gap，置信度中低。** Friday原油溢价回吐，但周末袭击重新抬高供应尾部；SC实体缺失，FU深back，不能追第一跳。
- **贵金属AG—AU：偏多但不追，置信度中。** 中国价仓与周五海外金银支持，地缘再添催化；高收益率、轻contango和不可执行期权反对。
- **PX—TA—PR聚酯：成本回吐逻辑受周末事件反对，置信度低。** Friday弱势与价仓支持空头，但新油价gap可能先修复成本端；缺加工利润与A级basis。
- **内需与农产品：偏弱背景，置信度中低。** M/RM、FG/SA、LC有弱势或价仓异常，但curve、CBOT和C级现货互相冲突，均不适合周一首跳追价。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | EC2610事件gap接受多 | 21/15/18/12/8 | **74** | 1、2、4 | 存在待验证优势｜部分、exact运价缺｜休市/周一09:45确认 |
| 2 | AG2612回撤接受多 | 20/15/16/10/8 | **69** | 1、4 | 存在待验证优势｜部分、利率/curve反对｜休市/待报价 |
| 3 | 多13手LU2611/空1手SC2611 | 21/16/13/10/8 | **68** | 1、2 | 存在待验证优势｜部分、新事件反对｜周一重新配比 |
| 4 | FU2611事件后反弹多 | 19/15/16/10/7 | **67** | 2、4 | 存在待验证优势｜部分、Friday价格反对｜等待触发 |
| 5 | TA701弱势延续空 | 17/14/12/8/8 | **59** | 1 | 证据不足｜能源gap反对｜仅反抽失败观察 |

分项已复算。AG、LU/SC、FU只有两层支持，严格不超过69；TA只有一层，封顶59。EC虽有三层，exact运价、OI和参数缺口令其仅为重点研究候选。所有期货最大损失均不由计划止损限定。

## 七、前三名研究交易卡

### 1. EC2610｜事件gap接受多｜74

**事实：** Friday OHLC=2205/2264/2122/2172.5，结算2189；1D +2.99%、5D +7.09%，ΔOI -1,176，near-next back 21.29%。制度上无Night。  
**市场定价：** Friday已计入部分航运风险，但OI下降说明上涨也可能是减仓/事件溢价，而不是确定增量多头。  
**分歧：** Riyadh/Yanbu袭击若持续改变Red Sea与Saudi出口路径，EC可能重新扩张；最强竞争解释是袭击被拦截、未证实设施受损，而且SC/EC映射并不纯。

- 最佳表达：EC2610单腿条件多；没有exact运价，不构造现货套利。
- 好成交：周一09:45后回撤2180—2215守住结算2189，并重上2220/VWAP，先1/4仓。
- 中成交：突破Friday高点2264后回踩2240—2264不破，仓位减半。
- 坏成交：直接高于2350、跌破2122或盘口深度不足，放弃。
- 止损：45分钟接受2120下方。
- 失效：袭击无后续、船流恢复、back低于15%且价格跌破Friday低点。
- 退出：TP1 2264或+1.5R；TP2 2380或+3R；1—3D无新增事件/运价确认退出。
- 风险：最大计划损失0.25% NAV；航运与能源共享地缘因子合计≤0.75%。
- 参数：repo只确认最后交易/交割日为10月26日；multiplier、tick、tick value、margin、limit及交割参数未确认，**参数补齐前仅为研究卡，不得下单**。
- 压力：因参数缺失，不编一板/两板金额；须另测周末gap、限价无法止损和交割月流动性。10月上旬前主动移仓。
- 期权：无execution-ready结构，不能把未报价期权当有限损失替代。

### 2. AG2612｜回撤接受多｜69

**事实：** Friday OHLC=15970/16321/15940/16304，结算16104；1D +2.79%、5D +2.73%，ΔOI +8,244，轻contango 0.12%。正式合约Night因日历与代表合约错位不可用。周五外银66.556、黄金4385.90。

- 市场隐含：信用、地缘和避险需求抵消高收益率压力。
- 分歧：周末事件可能强化非利率需求；竞争解释是10Y接近5%，任何美元再强都可能令金银高位回吐。
- 好成交：周一09:30后16100—16250承接并重上16320/VWAP，先1/4仓。
- 中成交：突破16350后回踩16300—16350不破，仓位减半。
- 坏成交：直接高于16700、跌破15940或外银低于64，放弃。
- 止损：30分钟接受15880下方。
- 失效：银跌破64、黄金跌破4300且美元/实际利率继续上行。
- 退出：TP1 16650或+1.5R；TP2 17100或+3R；1—3D时间止损。
- 风险：计划损失0.25% NAV；贵金属共享风险≤0.50%。
- 参数：repo仅确认最后交易日12月15日、最后交割日12月17日；multiplier、tick、margin与limit未确认，参数补齐前不执行，不编限幅压力金额。
- 期权：9月17日AG曲面RR/BF出现不可信极值，且execution-ready=false；隔离偏度，不推断Dealer Gamma。

### 3. 多13手LU2611/空1手SC2611｜相对价值｜68

**事实：** Friday收盘LU/SC=5440/728，比价7.4725；按稳定合约单位研究换算，两腿名义约707,200与728,000元，偏差-2.86%，仅近似dollar-neutral，绝非beta-neutral。Friday EOD中LU back 4.79%、ΔOI +1,703，SC back 1.59%、ΔOI -2,115。  
**变化：** 周末袭击直接增加SC短腿gap风险，外部层由支持改为反对。

- 收益公式：`130×(LU出场-入场)-1000×(SC出场-入场)`。
- 好成交：周一09:45后实时比价在7.35—7.55获得接受并重上7.50，且没有确认Yanbu设施受损，先1/4仓。
- 中成交：突破7.60后回踩不破；仓位减半。
- 坏成交：SC事件高开导致比价低于7.20、直接高于7.80或任一腿深度不足，放弃。
- 止损：45分钟接受7.20下方。
- 失效：SC相对LU强3个百分点以上、SC back高于4%，或Brent重上108且供应损害得到确认。
- 退出：TP1 7.70或+1.5R；TP2 8.00或+3R；1—3D无扩张退出。
- 风险：计划损失0.25% NAV；与EC、FU、SC合并≤0.75%。两腿相关性破裂时止损不保证最大损失。
- 参数：SC/LU动态margin、limit及LU静态参数在repo中不完整；经纪端确认前不执行。两合约最后交易日10月30日、交割日11月6日，10月中旬前移仓。

## 八、商品期权专项

最新研究截面为9月17日，已落后于9月18日EOD与周末事件，不能用作周一成交报价或第五层支持。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/56.54% | +9.02vol | +0.73/+1.41 | Y/N/N | 周末事件后必须重报价 |
| FU2611/10-19 | 60.62%/45.36% | +15.26vol | -0.50/+1.42 | Y/N/N | 事件凸性偏贵 |
| TA701/12-11 | 31.87%/28.17% | +3.70vol | +2.43/+0.72 | Y/Y/N | 能源gap令旧Delta失真 |
| RM701/12-11 | 20.80%/16.53% | +4.27vol | +6.39/+0.98 | Y/Y/N | 旧多失效，不沿用 |
| PR611/10-13 | 27.81%/30.82% | -3.02vol | +2.35/+0.95 | Y/N/N | IV<RV不等于便宜 |
| AG2612/11-24 | 44.14%/31.14% | +12.99vol | 异常极值 | Y/N/N | 偏度隔离 |

若周一取得实时报价，可研究EC无期权时以小期货试仓，或比较SC有限净支出call/put spread与线性期货；但执行价、Delta、净支出、盈亏平衡、Greeks、滑点和行权交割必须重算。当前期权不优于裸期货，Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、下一实际9:00开盘风险地图

严格三层：①Previous China EOD=9月18日；②Current Trading Day Night=应归属9月21日但repo标签异常，已隔离；③07:00 Overseas=国际市场休市，只有周末事件，没有新价格。

| 品种 | EOD→隔离Night→周末事件 | 周一判断 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| EC | +2.99%、深back→无Night→Saudi/Red Sea风险升温 | 高开概率上升 | 不追；45m | 2189/2220/2264、curve、船流 |
| SC | Friday暴跌、back压缩→raw +0.93%但隔离→Yanbu风险 | 双向高gap | 不追；45m | 728/754/776、Brent、设施损害 |
| LU/FU | Friday弱、back较深→raw修复但隔离→事件利多成本 | 偏高但冲突 | 45m | LU/SC比价、FU back、成交量 |
| AG/AU | Friday价仓强→代表合约错位→地缘升温 | 偏高 | 不追；30—45m | AG16100/16320、金银、10Y |
| PX/TA/PR | Friday跌→raw修复但隔离→油价gap风险 | 高开/回吐皆可能 | 45m | 链内breadth、OI、加工利润 |
| CU/AL/ZN/NI | Friday反弹→无有效新Night→宏观无新价 | 平/小高开 | 45m | LME、CNH、roll |
| M/RM | Friday弱→DCE缺失→CBOT无周末新价 | 平/低开 | 45m | ΔOI、basis、near-next |
| FG/SA | 中期弱→raw小涨但隔离 | 平开/噪音 | 30m | FG904/912/919、curve |
| LC/SI/PS及软商品 | 无制度Night | 周一首次定价 | 45m | 量仓、curve、实体 |

周末事件可能使EC、SC先高开，但是否已被周五晚盘部分交易无法合法验证。周一应把首跳视为价格发现，不把它误写成可追趋势。Exact USD/CNH、DXY和实际利率没有周末新成交，本期不量化人民币贡献。

## 十、未来24小时与7天事件

- 周末至9月21日开盘前：核实Riyadh/Yanbu袭击是否造成实物损害、Saudi East-West修复、Sohar替代装船及Hormuz/Red Sea船流。未确认损害只作为gap右尾。
- 9月21日09:00：中国下一实际日盘；EC、SC、LU/FU、贵金属等待30—45分钟。
- 9月21日LPR窗口：Reuters调查预期1Y/5Y LPR维持3.00%/3.50%；意外下调偏利多内需链，持平则更看价格自身反应。[Reuters](https://www.reuters.com/world/china/china-set-keep-loan-rates-steady-16th-consecutive-month-september-2026-09-18/)
- 9月23日22:30：EIA周度石油数据；能源Delta事前降低，期权只允许有报价的有限净支出结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月24日前后：USDA出口销售；M/RM/C/油脂按实际销售、中国采购和basis反应调整。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 9月25日：欧盟电工钢临时保障措施生效，关注硅钢、铁合金与贸易流，不直接构造不可比套利。
- 未来7日：北美收割天气、马棕出口、CFTC滞后仓位、交易所动态margin/limit与SC/FU/LU移仓。OPEC+/IEA若无计划内新发布，不制造催化。

## 十一、覆盖、风险与归档核对

- **应覆盖：** 强制63代码及动态新增，共77产品；期权64产品。
- **实际取数且已分析：** 9月18日五所77产品全部完成方向、1D/3D/5D/20D、量仓、curve、跨期、跨品种/跨市场、加工利润、风格/近似中性、波动率、偏度及事件凸性扫描；70个具有可用趋势/量仓/curve。
- **Night：** 周日新运行0合约且正确失败；previous snapshot retained。统一输入保留423合约/37产品，但日期异常且214项query error，整体隔离。
- **期权：** 应覆盖64，实际45，0 execution-ready；DCE 18产品跳过、A失败。
- **数据不足：** SC/LU实体、A级/B级basis、exact import parity、可靠加工利润、合法归属的周五Night、9月18日期权、所有实时bid/ask及多数动态交易参数。
- **不适用/流动性不足：** JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；未静默删除。
- **黑色建材9/9：** JM/I/RB仍弱，FG/SA的曲线或单日修复反对追空；未发现三层共振。
- **有色贵金属12/12：** AG入榜；AU次之，CU减仓反弹，NI/SS无独立优势。
- **能源化工25/25：** EC、LU/SC、FU、TA入榜或观察；SC转双向gap，PX/PR/EB/EG成本传导待周一重定价。
- **新能源及GFEX新材料：** LC价跌仓增但back与C级现货反对追空；SI/PS及新材料无三层优势。
- **农产品22/22：** M/RM弱势但CBOT和basis不支持追空；油脂、玉米、棉糖果链未见三层共振。
- **航运软商品：** EC为唯一70+研究候选；CF/CY/SR/AP/CJ/PK无可执行异常。
- **周期与策略：** 1D/3D/5D/20D，以及方向、curve、跨期、跨品种、跨市场、近似中性、波动率、偏度、事件凸性全部覆盖；没有合格beta-neutral篮子或exact跨市场套利。
- **风险预算：** 休市新增风险为0；周一试仓单笔最大计划损失0.25% NAV，取得价格、curve及非价格层确认后最高0.75%；航运—能源共享因子≤0.75%，单一高确信主题确认后≤2.5%。
- **压力测试：** 1/2个涨跌停、周末gap、两腿相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压及人民币急变。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无；周日休市，周一09:00后重新报价，EC/SC/能源与贵金属至少等待30—45分钟。  
C. 今天应继续观察的机会：EC2610事件gap接受、AG2612回撤多、LU2611/SC2611重新配比、FU深back，以及Riyadh/Yanbu损害与船流核实。  
D. 今天必须避免或退出的交易：沿用SC单向空卡、平移周五Night锚、追周一能源/EC第一跳、恢复RM旧多、把C级basis或外盘proxy称套利，以及在execution-ready=false时臆测期权成本。