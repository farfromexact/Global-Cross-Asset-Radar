# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-21

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：2026-09-21 07:13 BJT；信息截点：07:00。最近完整中国EOD为9月18日；当前交易日为9月21日，下一可交易窗口为09:00。周一交易日前制度上没有周日夜盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；外油仅上涨约0.8%，地缘方向得到确认但弹性有限，09:00不追能源与EC第一跳，只验证gap接受。**

当前regime：**周末地缘右尾与周五原油风险溢价回吐相互对冲；产品端back仍深，贵金属保持韧性，中国内需链偏弱。**

最接近触发的是EC2610事件gap接受、AG2612回撤接受多和LU2611/SC2611相对价值。三者均需要09:00后的真实价格、curve、量仓与交易参数；“有研究优势”不等于开盘即买。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。

- 统一输入：schema v2，`requested_date=2026-09-18`，9月21日06:24:53生成。周一晨间使用周五EOD是正常组合。
- Futures：9月18日五所806合约、77产品；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；4条placeholder排除。
- Market State：77产品，70个具备同合约1D/3D/5D/20D、RV20、量仓与curve。
- Physical：9月21日06:24重建，18/20序列按原生频率fresh、validated、published；SC/LU unavailable。Basis全部C级或缺失，仅作context。
- External：repo于06:24刷新，17/22序列有效、5项不可得，均为`context_only`。repo油价代理与近月市场报价冲突，继续隔离；07:00海外由可靠公开源补充。
- Options：最新仍为9月17日16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖99.11%/69.50%/0。
- Metadata：partial；有效合约匹配73.45%，乘数/tick/保证金/限幅覆盖30.15%，last-trading-day覆盖67.49%。

### Night Session质量闸门

module-specific状态：`trading_date=2026-09-21`、`night_session_date=2026-09-20`，06:04:08生成；`data_fresh=false`、validation/published/coverage均为false。806个请求中0条Night、592条outside-window、214条query error/unresolved，previous valid snapshot retained。

**周一前没有周日夜盘，0条有效Night符合交易日历，不是应得市场数据缺失。** 但214条query error仍是技术错误；本期不使用旧的`trading_date=2026-09-19`快照，也不通过媒体伪造exact-contract Night。对制度上有夜盘的重点候选，因最近实际应发生的周五Night快照校验失败，评分上限79；`night_session_fallback_used=false`。

## 三、商品仪表盘

EOD均为9月18日；Night栏统一为“周一前无合法session”。1D/5D为同合约结算收益，curve为near-minus-next，不是现货basis。

| 板块 | 品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | Night close/vs close/vs settle/ΔOI | 07:00海外；Options S/P/E；信号 |
|---|---|---|---|---|---|
| 航运 | EC | EC2610；2172.5/2189；+2.99%/+7.09% | 2.54万/2.53万/-1,176；back 21.29% | 制度无周日Night | Gulf风险仍在；N/N/N；gap接受 |
| 能源 | SC | SC2611；728/754.4；-6.29%/-0.30% | 28.52万/4.22万/-2,115；back 1.59% | 无合法session | Brent104.68、+0.78%；Y/N/N；双向gap |
| 能源 | LU | LU2611；5440/5515；-2.10%/+0.51% | 15.64万/7.14万/+1,703；back 4.79% | 无合法session | 外油温和涨；无可执行链；相对SC |
| 能源 | FU | FU2611；4200/4259；-3.29%/-0.77% | 81.04万/19.09万/-12,686；back 12.80% | 无合法session | WTI101.06、+0.76%；Y/N/N；深back反弹 |
| 贵金属 | AG | AG2612；16304/16104；+2.79%/+2.73% | 16.59万/21.50万/+8,244；contango0.12% | 无合法session | 地缘支持、美元/利率反对；Y/N/N |
| 贵金属 | AU | AU2612；951.38/946.18；+0.96%/+0.17% | 11.96万/19.75万/+13,041；轻contango | 无合法session | 最近金4385.9；Y/N/N；不追 |
| 有色 | CU | CU2610；109620/109530；+1.31%/+0.80% | 8.10万/15.19万/-7,625；back0.33% | 无合法session | 最近LME14562；N/N/N；等LME/CNH |
| 聚酯 | TA | TA701；6238/6312；-2.86%/0.00% | 136.76万/117.12万/+10,883；back2.14% | 无合法session | 油价温和反弹；Y/Y/N；空头降级 |
| 聚酯 | PR | PR611；8132/8244；-3.06%/+1.10% | 10.10万/6.16万/-1,405；back1.58% | 无合法session | 成本反弹；Y/N/N；旧多仍退出 |
| 饲料 | M | M2701；3397/3429；-1.47%/+0.21% | 204.64万/273.12万/-196,992；contango1.10% | 无合法session | 最近CBOT粕351.1；N/N/N |
| 建材 | FG | FG701；907/912；+0.55%/-7.32% | 108.62万/129.52万/-70,452；back3.70% | 无合法session | 无exact外盘；Y/Y/N；反弹噪音 |
| 新能源 | LC | LC2701；127160/128460；-1.28%/-4.11% | 18.69万/42.54万/+9,528；back1.25% | 制度无Night | 实体C级；Y/N/N；不追空 |
| 黑色 | JM | JM2701；last-good | 旧趋势偏弱、curve支持不足 | 无合法session | 无新海外定价；无执行期权 |

07:00附近Brent约104.68美元/桶、上涨0.78%，WTI约101.06、上涨0.76%。上涨方向确认周末风险，但幅度不足1%，说明市场尚未按重大设施损害或新增大规模断供定价。[Reuters油市](https://www.reuters.com/business/energy/oil-rises-after-houthi-attack-saudi-capital-2026-09-20/)

周日沙特主指数最终收跌0.3%，Aramco从早盘下跌转为收涨1.3%，卡塔尔跌1.1%；这是“地区风险偏好受压、油设施实损尚未得到股价确认”的混合证据。[Reuters海湾市场](https://www.reuters.com/world/middle-east/saudi-gulf-stocks-fall-after-houthis-claim-riyadh-attacks-2026-09-20/)

## 四、相比昨晚真正变化

1. **海外原油已经开盘，但只涨约0.8%。** 方向支持能源高开，弹性却明显弱于设施实损情景；SC不追多，也不恢复单向空卡。
2. **Aramco最终收涨1.3%，修正昨晚盘中-0.6%的观察。** 这是价格更新，不是观点随意修改；它削弱“延布已实损”的竞争解释。
3. **EC仍居首但75→72。** 航运右尾、周五强价和深back支持；温和油价反应、OI下降和exact运价缺失降低赔率。
4. **TA空头从54降至49并退出正式可执行研究。** 原油回升与无Night使开盘空头赔率更差，只保留覆盖记录。
5. **LPR已经发布且不变。** 1年期3.00%、5年期3.50%，不再是09:15未来催化；对内需商品为中性偏弱背景。[Reuters LPR](https://www.reuters.com/business/finance/china-keeps-benchmark-lending-rates-unchanged-16th-month-september-2026-09-20/)
6. **台账：** `COM-M-EC2610-FREIGHT-REPRICE-20260918` 75→72；`COM-E-AG2612-PRECIOUS-REBOUND-20260918`维持69；`COM-M-LUSC-RELATIVE-20260918` 65→63；`COM-M-SC2611-REVERSAL-20260917`继续停止。无成交反馈，不假设用户持仓。

## 五、产业链地图

- **事件敏感度最高：EC—SC能源航运，偏高开但不追，置信度中。** 外油方向确认，幅度温和；EC深back支持，exact船流、运价和设施损害缺失。
- **产品端相对强：LU/FU相对SC，置信度中低。** back结构支持产品端；周一SC可能因地缘补涨，旧比价优势需09:45重新验证。
- **贵金属偏强，置信度中。** AG/AU周五价仓与地缘支持；高美元、高收益率和无实时金银报价反对第一跳。
- **聚酯链由偏空转为冲突，置信度低。** 周五TA/PR弱，今晨外油反弹；缺加工利润和需求层，暂不做多腿。
- **内需与农产品偏弱背景，置信度中低。** M大幅减仓、FG反弹减仓、LC跌势伴随back；C级basis不能确认方向。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | EC2610事件gap接受多 | 20/14/18/12/8 | **72** | 1、2、4 | 存在待验证优势｜部分｜等待09:45/参数 |
| 2 | AG2612回撤接受多 | 20/15/16/10/8 | **69** | 1、4 | 存在待验证优势｜部分｜等待09:30 |
| 3 | 多13手LU2611/空1手SC2611 | 19/14/13/9/8 | **63** | 1、2 | 存在待验证优势｜部分、SC gap反证｜等待09:45 |
| 4 | FU2611深back反弹 | 18/13/16/9/7 | **63** | 2、4 | 存在待验证优势｜部分、价格层反对｜等待09:45 |
| 5 | TA701成本回吐空 | 15/12/10/6/6 | **49** | 1 | 证据不足｜原油反对｜仅观察 |

分项均已复算。没有execution-ready期权；所有期货最大损失均不由计划止损限定。EC虽达到70+，仍缺当前报价、参数和触发，不能立即建仓。

## 七、前三名研究卡

### 1. EC2610｜事件gap接受多｜72

**事实：** previous close/settlement=2172.5/2189；1D +2.99%、ΔOI -1,176、back21.29%；周一前无合法Night。  
**市场定价：** 周五已计入部分航运风险，今晨油价只温和反应。  
**分歧：** 若09:00高开后仍守住结算并扩张back，EC可能重新定价红海右尾；最强反证是油价仅涨0.8%、Aramco收涨且无设施实损。

- 最佳表达：EC2610单腿条件多；不以SC或媒体船流构造伪套利。
- 好成交：09:45后2180—2215承接、守住2189并重上2220/VWAP，先1/3仓。
- 中成交：突破2264后回踩2240—2264不破，半仓。
- 坏成交：直接高于2350、跌破2122或盘口深度不足，放弃。
- 止损：45分钟接受2120下方。
- 失效：无新增损害、船流恢复、back低于15%且跌破周五低点。
- TP1 2264或+1.5R；TP2 2380或+3R；1—3D时间止损。
- 风险≤0.25% NAV；与能源事件共享风险≤0.75%。
- metadata仅确认最后交易日2026-10-26；multiplier、tick、tick value、margin、limit及交割参数未确认，**参数补齐前仅为研究卡**。

### 2. AG2612｜回撤接受多｜69

**事实：** previous close/settlement=16304/16104；1D +2.79%，ΔOI +8,244，轻contango；周一前无合法Night。  
**市场定价：** 地缘和信用风险部分计入金银。  
**分歧：** 若回撤仍被接受，AG可能继续强于工业品；竞争解释是高实际利率与美元会压制贵金属。

- 好成交：09:30后16100—16250承接并重上16320/VWAP。
- 中成交：突破16350后回踩不破，半仓。
- 坏成交：直接高于16700或跌破15940，放弃。
- 止损15880；失效为外银<64、黄金<4300且收益率再升。
- TP1 16650；TP2 17100；1—5D时间止损。
- 风险≤0.25% NAV；贵金属共享风险≤0.40%。
- repo仅确认最后交易日12月15日、交割日12月17日；其余参数未确认，不编一板、两板金额。

### 3. 多13手LU2611/空1手SC2611｜相对价值｜63

周五名义约707,200元对728,000元，偏差-2.86%；近似dollar-neutral，**不是beta-neutral**。  
收益公式：`130×(LU退出价−入场价)−1000×(SC退出价−入场价)`。

- 市场隐含：产品端紧张持续时间可能长于原油风险溢价。
- 新反证：今晨外油上涨令短SC腿先承受gap；没有Night curve可确认。
- 好成交：09:45后比值7.35—7.55获得接受并重上7.50，且未确认延布设施损害。
- 中成交：突破7.60后回踩成功，半风险。
- 坏成交：比值<7.20、>7.80或任一腿深度不足，放弃。
- 止损：45分钟接受7.20下方。
- 失效：SC相对强3个百分点以上、SC back>4%，或Brent>108且确认设施受损。
- TP1 7.70；TP2 8.00；1—5D时间止损。
- 风险≤0.25% NAV；两腿保证金、限幅和交割风险开盘前复核。

## 八、商品期权专项

最新截面为9月17日，已经落后于最新应得9月18日截面；周五底层变化和周末事件使旧Delta、moneyness及event vol不可执行。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/56.54% | +9.02vol | +0.73/+1.41 | Y/N/N | 历史事件vol偏贵，须重报 |
| FU2611/10-19 | 60.62%/45.36% | +15.26vol | -0.50/+1.42 | Y/N/N | 裸买凸性成本高 |
| TA701/12-11 | 31.87%/28.17% | +3.70vol | +2.43/+0.72 | Y/Y/N | 旧Delta失真 |
| PR611/10-13 | 27.81%/30.82% | -3.02vol | +2.35/+0.95 | Y/N/N | IV<RV不证明便宜 |
| AG2612/11-24 | 44.14%/31.14% | +12.99vol | 历史曲面异常 | Y/N/N | skew隔离 |
| EC/LU/M | 无成熟可执行series | N/A | N/A | N/N/N | 不使用代理面 |

当前没有可证明优于裸期货的期权。09:00后只有取得目标结构双边报价，才比较SC put spread、AG call spread或EC场外有限净支出结构；执行价、净支出、盈亏平衡、Greeks和滑点全部重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月18日；②Current Trading Day Night=周一前制度上无Night；③07:00 Overseas=Brent/WTI约+0.8%及最新地缘信息。

| 品种 | EOD→无Night→海外 | 09:00判断 | 追价/等待 | 确认指标 |
|---|---|---|---|---|
| EC | 周五强价深back→无Night→航运尾部仍在 | 高开风险 | 不追；45m | 2189/2220/2264、back、船流 |
| SC | 周五-6.29%、back压缩→无Night→Brent+0.78% | 高开/双向 | 不追；45m | 728/754/776、Brent、curve |
| LU | 周五-2.10%、back4.79%→无Night→外油涨 | 偏高 | 45m | 5440/5515、LU/SC |
| FU | 周五-3.29%、back12.8%→无Night→WTI涨 | 偏高但减仓 | 45m | 4200/4259、back、FU/SC |
| AG/AU | 周五价仓强→无Night→地缘支持 | 偏高 | 不追；30—45m | AG16100/16320、DXY、收益率 |
| TA/PX/PR | 周五弱→无Night→成本温和反弹 | 平/高开分化 | 45m | 链内breadth、OI、curve |
| CU/AL/ZN/NI | 周五外盘为最后完整价→无Night | 平开不确定 | 45m | LME重开、CNH、roll |
| M/RM/油脂 | 周五价仓偏弱→无Night→农业外盘增量不足 | 平/低开 | 30—45m | ΔOI、CBOT、basis |
| FG/SA | 周五反弹减仓→无Night | 平开、噪音 | 30m | OI、curve、实体 |
| LC等无Night品种 | 09:00首次价格发现 | gap敏感 | 45m | 量仓、curve、盘口深度 |

外油只涨约0.8%，说明周末新闻尚未产生极端弹性；若SC开盘涨幅显著超过外油且back没有同步扩大，优先理解为gap过冲，不追价。Exact USD/CNH同一时点不可得，不量化人民币贡献。

## 十、未来24小时与7天事件

- 9月21日09:00：中国商品市场重开；EC、SC、LU/FU、AG等待30—45分钟。
- 9月21日21:00：下一合法Night，归属9月22日；必须依据日盘价格接受重新建图。
- 未来24小时：Riyadh/Yanbu损害核实、Aramco声明、Hormuz/Perim及红海船流；确认实损将提高SC/EC上行gap风险。
- 9月23日22:30：EIA周报；能源仓提前降低Delta。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 未来一周：USDA出口销售、北美收割天气、中国采购和马棕出口；只按实际数据及国内响应调整。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- CFTC COT仅作滞后拥挤背景。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 美国—伊朗言辞升级及潜在会谈均可能使能源风险溢价双向跳变；线性仓必须缩小，期权仅在实时可执行报价下使用有限净支出。[Reuters地区局势](https://www.reuters.com/world/asia-pacific/iran-warns-against-new-escalation-by-us-allies-2026-09-20/)

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码；动态扩展后77产品；期权64产品。
- 实际取数并分析：77产品全部完成9月18日EOD初筛，70个具备有效趋势、量仓和curve；期权45产品/216 series有历史截面。
- 数据不足：周一前无Night；214条技术查询错误；SC/LU实体缺失；19个期权产品缺失；0个execution-ready；A/B级basis、exact import parity、加工利润和当前双边报价不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；全部保留覆盖记录。
- 黑色建材9/9：FG反弹减仓，I/JM/RB无三层共振。
- 有色贵金属12/12：AG入榜；AU/CU观察，黄金信用主题仍为冲突。
- 能源炼化化工25/25：EC、LU/SC、FU、TA入榜；SC单向空停止；PR旧多退出。
- 新能源及GFEX新材料全部扫描：LC跌势与back冲突；SI/PS/PT/PD缺实体闭环。
- 农产品油脂饲料畜牧22/22：M价仓弱但海外与basis不足；其余无三层优势。
- 航运与软商品全部扫描：EC为事件候选；CF/CY/SR/AP/CJ/PK无高分共振。
- 风险预算：当前新增风险0；09:00确认后单笔试仓≤0.25% NAV，确认交易最高0.75%；能源—航运共享因子≤0.75%，单主题总风险≤2.5%。压力测试包含两板、设施实损、船流中断、流动性消失、保证金上调及人民币急变。

归档状态在main回读验证后更新；CI仅作独立校验，不等待。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：EC2610仅在09:45后2180—2215承接、守住2189并重上2220时研究试多；AG2612仅在09:30后16100—16250承接并重上16320时研究试多，均须先补齐参数。  
C. 今天应继续观察的机会：LU2611/SC2611重新配比、FU2611深back反弹、SC高开是否过冲、TA/PX/PR成本传导，以及Riyadh/Yanbu损害与船流核实。  
D. 今天必须避免或退出的交易：追EC/SC/LU/FU第一跳、恢复SC单向空卡、低开追TA/M/LC、把无周日Night视为数据遗漏、把C级basis或外盘proxy称套利，以及在execution-ready=false时臆测期权成本。
