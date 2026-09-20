# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-20

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：2026-09-20 19:44 BJT；信息截点：19:30。今天为周日，中国商品市场休市；最近完整中国EOD为9月18日。今晚没有21:00夜盘，下一实际可交易窗口为9月21日09:00；下一连续交易窗口为9月21日21:00并归属9月22日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；沙特及海湾股市已对袭击作出负面定价，但油设施损害未确认，周一只验证EC事件gap、AG回撤及LU/SC相对强弱。**

当前regime：**地缘右尾重新抬升，原油供应风险与宏观需求疲软冲突；贵金属保持韧性，中国内需链偏弱，周末仍处于中国价格发现真空。**

最接近触发的是EC2610事件gap接受多、AG2612回撤接受多和多LU2611/空SC2611相对价值。三者均缺周一实时价格、量仓、curve和有效报价，今晚只能研究，不能挂单。

## 二、数据质量与覆盖

本期读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。

- 统一输入：schema v2，`requested_date=2026-09-18`，9月20日19:07:50生成。
- Futures last-good：9月18日五所806合约、77产品，已验证`full_market_ready=true`、日期匹配100%、critical errors=0；4条placeholder排除。
- 周日根流水线：五所均因非交易日请求返回0条，`full_market_ready=false`、日期匹配0%、critical module errors=15。该run failure不使9月18日last-good失效，也不构成周日行情。
- Market State：77产品完成初筛，70个具备同合约1D/3D/5D/20D、量仓和curve；周日重新生成但无新交易日，标为沿用。
- Physical：原始模块`data_fresh=false/validation_passed=false/published=false`；其中9月18日18/20序列仍是最新应得last-good，SC/LU unavailable。全部basis为C级或缺失，仅作context。
- External：9月20日19:07刷新，17/22序列在原生频率下有效、5项不可得，全部`context_only`。美欧商品周末休市，最新价格仍是周五收盘；repo WTI/Brent代理与可靠近月结算冲突，继续隔离。
- Options：最新为9月17日16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready，bid/ask覆盖0。9月20日根状态显示0条，属于周日空采集，不冒充T日截面。
- Metadata：partial；有效合约匹配73.45%，乘数/tick/保证金/限幅覆盖30.15%，last-trading-day覆盖67.49%。

### Night日期与周末状态

9月20日Night状态原始字段为`trading_date=2026-09-20`、`night_session_date=2026-09-19`，05:58生成；`data_fresh=false`、validation/published/coverage均失败，806个请求中0条Night、592条outside-window、214条query error/unresolved，previous valid snapshot retained。

周日没有应得Night，因此“0条新Night”本身不是市场缺失；但该raw标签不符合下一实际交易日语义，已整体隔离，不自行重标、不用于证据。今晚也没有未来21:00价格。[INE交易规则](https://www.ine.cn/eng/services/rules/rulebook/202202/t20220222_821734.html)

## 三、商品仪表盘

以下EOD、量仓和curve均截至9月18日；周末没有合法Night，`day_follow_through`不适用。S/P/E为9月17日历史期权surface/positioning/execution readiness。

| 板块 | 品种 | 合约；close/settle；1D/5D | Volume/OI/ΔOI；curve | Physical/basis | 周末海外/事件；S/P/E；周一信号 |
|---|---|---|---|---|---|
| 航运 | EC | EC2610；2172.5/2189；+2.99%/+7.09% | 2.54万/2.53万/-1,176；back 21.29% | exact运价缺 | Gulf股跌；N/N/N；事件gap接受 |
| 能源 | SC | SC2611；728/754.4；-6.29%/-0.30% | 28.52万/4.22万/-2,115；back 1.59% | 缺失 | 油设施损害未确认；Y/N/N；双向gap |
| 能源 | LU | LU2611；5440/5515；-2.10%/+0.51% | 15.64万/7.14万/+1,703；back 4.79% | 缺失 | 相对SC强；无成熟执行链；重配比 |
| 能源 | FU | FU2611；4200/4259；-3.29%/-0.77% | 81.04万/19.09万/-12,686；back 12.80% | 7525/C级 | 深back反对追空；Y/N/N；反弹研究 |
| 贵金属 | AG | AG2612；16304/16104；+2.79%/+2.73% | 16.59万/21.50万/+8,244；contango 0.12% | context | 地缘支持、高利率反对；Y/N/N；回撤多 |
| 贵金属 | AU | AU2612；951.38/946.18；+0.96%/+0.17% | 11.96万/19.75万/+13,041；轻contango | context | 金周五4385.9；Y/N/N；不追 |
| 有色 | CU | CU2610；109620/109530；+1.31%/+0.80% | 8.10万/15.19万/-7,625；back 0.33% | 110235/C级 | LME周五14562；N/N/N；等待CNH |
| 聚酯 | TA | TA701；6238/6312；-2.86%/0.00% | 136.76万/117.12万/+10,883；back 2.14% | 7108.8/C级 | 原油右尾反对追空；Y/Y/N |
| 聚酯 | PR | PR611；8132/8244；-3.06%/+1.10% | 10.10万/6.16万/-1,405；back 1.58% | 缺失 | 成本与事件冲突；Y/N/N；旧多退出 |
| 饲料 | M | M2701；3397/3429；-1.47%/+0.21% | 204.64万/273.12万/-196,992；contango 1.10% | C级 | CBOT粕351.1；无有效期权；弱势观察 |
| 建材 | FG | FG701；907/912；+0.55%/-7.32% | 108.62万/129.52万/-70,452；back 3.70% | 1008/C级 | 无exact外盘；Y/Y/N；反弹噪音 |
| 新能源 | LC | LC2701；127160/128460；-1.28%/-4.11% | 18.69万/42.54万/+9,528；back 1.25% | 131000/C级 | 无Night；Y/N/N；不追空 |
| 黑色 | JM | JM2701；周五last-good | 趋势偏弱、curve不足 | 2423.75/C级 | 无新海外定价；不入榜 |

周日沙特TASI下跌0.5%、Aramco跌0.6%，卡塔尔股指跌0.9%，说明袭击风险已经进入当地风险资产定价；但没有独立确认延布油设施受损，不能直接换算成周一SC或EC涨幅。[Reuters海湾市场](https://www.reuters.com/world/middle-east/saudi-gulf-stocks-fall-after-houthis-claim-riyadh-attacks-2026-09-20/)

沙特确认拦截飞向利雅得的弹道导弹，胡塞武装还宣称袭击延布等地；截至截点无人员伤亡和油设施损害的独立确认。[AP](https://apnews.com/article/b1286cad816dd3e553f50f6dd5205972)

## 四、相比晨报/上一晚报真正变化

1. **地缘冲击从新闻进入当地资产价格。** TASI、Aramco和卡塔尔股市下跌，为EC/能源事件层增加了独立市场映射，但不是油设施物理损害证明。
2. **SC单向空卡继续停止。** 周五弱价和back压缩仍支持供应溢价回吐，但周末攻击扩大空头gap与涨停尾部，只有周一双向验证价值。
3. **EC维持第一但不能追第一跳。** 周五价涨、深back与周末航运风险形成三层支持；OI下降、exact船流和运价缺失是最强反证。
4. **中国LPR按期维持1年期3.00%、5年期3.50%。** 这是已发布事实，不再是周一潜在催化；对商品内需仅属中性偏弱背景。[Reuters LPR](https://www.reuters.com/business/finance/china-keeps-benchmark-lending-rates-unchanged-16th-month-september-2026-09-20/)
5. **没有新增可验证中国价格或期权截面。** 周末run error、Night 0条和期权0条均未改变9月18日last-good的原生有效性，也不能成为方向证据。
6. **旧建议台账：** `COM-M-EC2610-FREIGHT-REPRICE-20260918` 74→75；`COM-E-AG2612-PRECIOUS-REBOUND-20260918`维持69；`COM-M-LUSC-RELATIVE-20260918` 68→65，因SC事件右尾增大；`COM-M-SC2611-REVERSAL-20260917`保持停止。无成交反馈，不假设用户持仓。

## 五、产业链地图

- **事件敏感度最强：EC—SC能源航运链，方向偏右尾、置信度中。** EC周五强价和深back、周日Gulf股市反应支持；油设施损害、船流和exact运价仍缺。
- **产品端相对强：LU/FU相对SC，置信度中低。** LU/FU的back深于SC；但攻击可能令原油先补涨，LU/SC配比需要周一重算。
- **贵金属偏强，置信度中。** AG/AU周五价仓和地缘支持；轻contango、高实际利率与旧期权面反对追价。
- **最弱背景：TA—PR—M，置信度中低。** 周五价格或持仓转弱；原油事件右尾、低质量basis和缺加工利润限制空头。
- **黑色—建材—新能源：未发现三层共振。** FG反弹但减仓、LC跌势伴随back，I/JM/RB无新海外或实体闭环。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | EC2610事件gap接受多 | 21/15/19/12/8 | **75** | 1、2、4 | 存在待验证优势｜部分｜休市，周一09:45 |
| 2 | AG2612回撤接受多 | 20/15/16/10/8 | **69** | 1、4 | 存在待验证优势｜部分｜周一09:30 |
| 3 | 多13手LU2611/空1手SC2611 | 20/15/13/9/8 | **65** | 1、2 | 存在待验证优势｜部分、事件反证扩大｜重报价 |
| 4 | FU2611深back反弹 | 18/14/16/9/7 | **64** | 2、4 | 存在待验证优势｜部分、价格层反对｜等待触发 |
| 5 | TA701成本回吐空 | 16/13/11/7/7 | **54** | 1 | 证据不足｜不足、原油右尾反对｜早期异常 |

分项均已复算；两层候选封顶69，一层封顶59。分数只是研究排序，不是胜率或仓位指令。所有期货最大损失均不由计划止损限定。

## 七、前三名研究卡

### 1. EC2610｜事件gap接受多｜75

**事实：** 周五close/settle=2172.5/2189，1D +2.99%、5D +7.09%，ΔOI -1,176，back 21.29%。周日Saudi/Gulf股市下跌确认风险情绪传导。  
**市场隐含：** 航运中断风险已经部分进入价格，但尚未按延布设施实损或红海重新封锁计价。  
**分歧：** 若周一gap后仍守住结算并扩张back，事件可能继续定价；竞争解释是袭击被拦截、没有设施损害，周一高开将迅速回吐。

- 最佳表达：EC2610单腿条件多；不以SC或公开船流构造伪套利。
- 好成交：周一09:45后2180—2215承接，守住2189并重上2220/VWAP，先1/3仓。
- 中成交：突破2264后回踩2240—2264不破，仓位减半。
- 坏成交：直接高于2350、跌破2122或盘口深度不足，放弃。
- 止损：45分钟接受2120下方；逻辑失效为确认无持续损害、船流恢复、back低于15%且跌破周五低点。
- TP1 2264或+1.5R；TP2 2380或+3R；1—3D无扩张退出。
- 风险：试仓≤0.25% NAV；与能源共享事件风险合计≤0.75%。
- 参数：repo仅确认最后交易日2026-10-26；multiplier、tick、tick value、动态margin/limit和交割参数未确认，**补齐前不可下单**。

### 2. AG2612｜回撤接受多｜69

**事实：** 周五close/settle=16304/16104，1D +2.79%、ΔOI +8,244，curve轻contango。  
**市场定价：** 地缘尾部与贵金属韧性已被部分计价。  
**分歧：** 若回撤仍获接受，AG可能继续强于工业品；最强反证是实际利率接近高位、美元再升及外银跌破64。

- 好成交：周一09:30后16100—16250承接并重上16320/VWAP。
- 中成交：突破16350后回踩不破，以半仓表达。
- 坏成交：直接高于16700或跌破15940，放弃。
- 止损15880；失效为外银<64、黄金<4300且收益率再升。
- TP1 16650；TP2 17100；1—5D时间止损。
- 风险≤0.25% NAV；贵金属共享风险≤0.40%。
- repo仅确认最后交易日12月15日、交割日12月17日；交易参数未完整，动态压力损失不得编造。

### 3. 多13手LU2611/空1手SC2611｜相对价值｜65

按周五收盘，13手LU名义约707,200元、1手SC约728,000元，偏差-2.86%；仅为近似dollar-neutral，**不是beta-neutral**。  
收益公式：`130×(LU退出价−入场价)−1000×(SC退出价−入场价)`。

- 市场隐含：SC供应溢价快速回吐，产品端紧张相对更持久。
- 新反证：周末攻击直接提高SC补涨与gap风险，使短SC腿比晨报更危险。
- 好成交：周一09:45后比值7.35—7.55获得接受并重上7.50，且未确认延布设施损害。
- 中成交：突破7.60后回踩成功，半风险。
- 坏成交：低于7.20、高于7.80或任一腿深度不足，放弃。
- 止损：45分钟接受7.20下方。
- 失效：SC相对强3个百分点以上、SC back重扩至4%以上，或Brent>108且确认设施受损。
- TP1 7.70；TP2 8.00；1—5D时间止损。
- 两腿合并风险≤0.25% NAV；参数和保证金周一向经纪端复核，10月中旬前检查移仓。

## 八、商品期权专项

最新有效但已落后的截面为9月17日；周五底层行情与周末事件已改变moneyness、Delta和event vol。全部目标结构`execution_ready=false`。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/56.54% | +9.02vol | +0.73/+1.41 | Y/N/N | 事件vol历史上偏贵，须重报 |
| FU2611/10-19 | 60.62%/45.36% | +15.26vol | -0.50/+1.42 | Y/N/N | 裸买凸性成本高 |
| TA701/12-11 | 31.87%/28.17% | +3.70vol | +2.43/+0.72 | Y/Y/N | 旧Delta不可执行 |
| PR611/10-13 | 27.81%/30.82% | -3.02vol | +2.35/+0.95 | Y/N/N | IV<RV不证明便宜 |
| AG2612/11-24 | 44.14%/31.14% | +12.99vol | 历史曲面异常 | Y/N/N | skew隔离 |
| EC/LU/M | 无成熟可执行series | N/A | N/A | N/N/N | 不用代理面 |

当前没有可证明优于裸期货的期权结构。周一取得实时报价后，才比较SC put spread、AG call spread或EC场外有限净支出结构；执行价、Delta、净支出、盈亏平衡、Greeks、滑点与交割均须重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、下一实际开盘风险地图

严格区分：①中国最近EOD=9月18日；②周末无合法Night；③周日新增只有Gulf股市和地缘信息，美欧商品仍以周五收盘为最近价格；④今晚无21:00交易，下一窗口为9月21日09:00。

| 品种 | 周末新增与周五EOD冲突 | 周一倾向 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| EC | 周五强价深back；周末Gulf风险上升 | 偏高开 | 不追；45m | 2189/2220/2264、back、船流 |
| SC | 周五大跌；周末油设施右尾上升 | 双向大gap | 不做第一跳；45m | 728/754/776、Brent、curve |
| LU/FU | 周五弱但back深；事件利多原油 | 高开后分化 | 45m | LU/SC、FU/SC、back |
| AG/AU | 周五强；地缘支持、高利率反对 | 偏高 | 不追；30—45m | AG16100/16320、DXY、收益率 |
| TA/PX/PR | 周五弱；周末原油右尾反向 | 平/高开分化 | 45m | 链内breadth、OI、curve |
| CU/AL/ZN/NI | 周五外盘为最新；无周日商品价 | 平开不确定 | 45m | LME重开、CNH、roll |
| M/RM/油脂 | 周五弱；无新农业盘 | 平/低开 | 30—45m | ΔOI、CBOT、basis |
| FG/SA | 周五反弹噪音、实体低质量 | 平开 | 30m | OI、curve、实体 |
| LC/EC等无Night品种 | 周一09:00首次定价 | gap风险高 | 45m | 量仓、curve、盘口深度 |

LPR已于9月20日维持不变，不能再列为周一未来催化。Exact USD/CNH同一时点不可得，本期不量化人民币进口成本贡献。

## 十、未来24小时与7天事件

- 未来24小时：Riyadh/Yanbu实际损害、Aramco声明、Hormuz/Perim及红海船流；确认设施受损将提高SC/EC上行gap和空头压力损失。
- 9月21日09:00：中国商品市场重开；EC、SC、LU/FU、AG至少等待30—45分钟。
- 9月21日21:00：下一实际连续交易窗口，归属9月22日；根据日盘price acceptance重新建图，不沿用本报告静态锚。
- 9月23日22:30：EIA周报；能源仓提前降Delta。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 未来一周：USDA出口销售、北美收割天气、中国采购与马棕出口；只按实际数据和国内价格响应调整。[USDA](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- CFTC COT只作滞后拥挤背景，不确认周一方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 中国AI与制造扩张主题：新存储平台量产是产业进展，但尚无可识别的铜、铝或化工边际需求模型，不增加商品方向分数。[Reuters CXMT](https://www.reuters.com/world/asia-pacific/chinas-cxmt-says-new-memory-chip-platform-enters-mass-production-2026-09-20/)

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码；动态扩展后77产品；期权64产品。
- 实际取数并分析：77产品全部完成9月18日last-good初筛，70个具备有效趋势、量仓和curve；期权45产品/216 series有历史截面。
- 数据不足：周末无中国新价格；Night raw状态异常；SC/LU实体缺失；19个期权产品缺失；0个execution-ready；A/B级basis、exact import parity、加工利润和当前双边报价不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；均保留覆盖记录。
- 黑色建材9/9：FG反弹减仓，I/JM/RB无三层共振。
- 有色贵金属12/12：AG入榜；AU、CU只观察，黄金信用主题维持“冲突而非确认”。
- 能源炼化化工25/25：EC、LU/SC、FU、TA入榜；SC单向空停止；PR旧多退出。
- 新能源及GFEX新材料全部扫描：LC跌势与back冲突；SI/PS/PT/PD缺实体闭环。
- 农产品油脂饲料畜牧22/22：M价仓弱但海外与basis不足；其余无三层优势。
- 航运与软商品全部扫描：EC为首要事件候选；CF/CY/SR/AP/CJ/PK未发现高分共振。
- 风险预算：今晚新增风险0；周一单笔试仓≤0.25% NAV，确认后≤0.75%；能源—航运事件因子≤0.75%，单主题总风险≤2.5%。压力测试覆盖双涨跌停、油设施实损、船流消失、保证金上调、流动性断裂和人民币急变。

归档状态在main回读验证后更新；CI仅作独立校验，不等待。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；周日休市且今晚无21:00夜盘，周一09:00后重新报价，EC/SC/能源与贵金属至少等待30—45分钟。  
C. 今晚应继续观察的机会：EC2610事件gap接受、AG2612回撤多、LU2611/SC2611重新配比、FU深back，以及Riyadh/Yanbu损害与船流核实。  
D. 今晚必须避免或退出的交易：沿用SC单向空卡、平移周五或异常Night锚、追周一EC/能源第一跳、恢复RM/PR旧多、把C级basis或外盘proxy称套利，以及在execution-ready=false时臆测期权成本。
