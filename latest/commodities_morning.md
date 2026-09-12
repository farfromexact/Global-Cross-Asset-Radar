# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-13

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:02 BJT；信息截点：07:00；最近完整中国EOD：9月11日；今日为周日。下一实际日盘为9月14日09:00，下一夜盘为9月14日21:00、归属9月15日交易日。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；霍尔木兹不会立即重开且沙特管道尚无恢复确认，FU/EC/SC周一跳空风险上升，但休市期不能追价。**

当前regime：**中东油运尾部风险持续、周五外油回撤尚未消化周末消息、国内能源与航运深backwardation、热通胀限制金属、WASDE玉米减产已接近预期。**

最接近验证的是FU2611、EC2610和SC2610。新增证据只是事件持续性：伊朗—阿曼谅解不意味着立即开放霍尔木兹，周一会谈预计也不会签署协议；国际电子盘和中国价格尚未对此定价。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、期权曲面及合约元数据。

- 统一输入：schema v2，`requested_date=2026-09-11`，9月13日06:20:44生成。
- Futures：9月13日06:03重新核验9月11日EOD。五所802合约、77个产品，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；4条placeholder排除，20个交易日同合约历史完整。根状态`official_complete=false`源于contract metadata/仓单等非核心模块不完整，不等同于核心期货不完整。
- Market State：使用9月11日同合约1D/3D/5D/20D；不拼接主力。当前缺curve z-score、量仓z-score等部分衍生项，已有值之外不猜测。
- Physical：20项目标中18项按原生日频fresh，SC/LU unavailable；5条仓单沿用。basis均为C级，缺地区、品质、税和交割地，不能进方向评分。
- External：9月13日06:20刷新，源日期仍为9月11日最后完整国际交易时段；17/22 fresh、5项unavailable，全部`context_only`。周末新闻为事件层，不是实时行情。
- Options：最新有效截面为9月11日，23,272条chain、384个series、59/64产品；CJ/MA/PL/PR/ZC失败。373个surface-ready、78个positioning-ready、0个execution-ready；bid/ask覆盖0。
- Metadata：partial。SHFE/INE/CZCE可用，DCE接口失败，GFEX源日期未匹配；动态margin/limit覆盖不足。重点卡缺项不补猜。

Night质量闸门：本次状态为`trading_date=2026-09-13`、`night_session_date=2026-09-12`，06:03:38生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=true`。802条全部为`outside_night_window`，有效Night合约0、产品0，缺时间戳/价格/报价、query error及unresolved均为0；validation error为“合法窗口内没有具体合约报价”。

这是**周末制度性无夜盘**，不是数据截断，也不要求fallback。上一份错误标为9月12日的快照虽被模块保留，但继续隔离，不用于价格、OI或Night curve。`overnight_day_decomposition_used=false`。

## 三、商品仪表盘

1D/5D均为9月11日同一具体合约结算收益；Night因周末不适用，明确列为N/A。S/P/E为期权surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | Basis/Physical | Current Night | 07:00海外/事件；Options | 周一信号 |
|---|---|---|---|---|---|---|
| 燃料油FU | FU2611；4289/4292；+4.66%/+10.85% | 139.93万/22.09万/+4,920；back 8.69% | C/context | N/A，周末无session | Brent最后104.61；管道停运；Y/Y/N | 产品强于SC才多 |
| 原油SC | SC2610；812.9/809.9；+5.40%/+18.56% | 30.53万/3.50万/+697；back 7.03% | Physical缺失 | N/A | 霍尔木兹不立即重开；SC2611 Y/N/N | 等45m接受 |
| 集运EC | EC2610；2032/2044；+4.18%/+10.10% | 3.29万/2.59万/+2,200；back 22.36% | exact运价缺 | 制度无夜盘 | Perim岛及曼德海峡风险；N/N/N | 周一双向gap |
| 低硫LU | LU2611；5453/5487；+4.53%/+10.85% | 22.06万/7.68万/+2,433；back 1.88% | Physical缺失 | N/A | 供应风险；新期权未就绪 | 相对FU偏弱 |
| 铜CU | CU2610；108990/108660；-2.75%/-0.41% | 20.93万/19.89万/-35,215；back 0.65% | C/context | N/A | LME最后14225.5；Y/Y/N | 反抽失败才空 |
| 白银AG | AG2612；15623/15676；-4.76%/-4.09% | 17.32万/19.34万/+8,788；contango 0.76%，roll | C/context | N/A | COMEX银最后约64.27；Y/N/N | 不追空 |
| 黄金AU | AU2612；944.94/944.54；-1.36%/-2.93% | 10.48万/15.84万/+7,777；轻contango | C/context | N/A | 金最后约4350；Y/N/N | 实际利率与避险冲突 |
| 碳酸锂LC | LC2701；134820/133960；-5.60%/-8.90% | 32.27万/40.76万/-1,124；back 1.68% | 现货135000，basis C；仓单沿用 | 制度无夜盘 | 无exact外盘；Y/N/N | 不接第一刀 |
| 玻璃FG | FG701；973/984；+2.29%/+1.34% | 218.62万/115.50万/-41,191；contango 7.37% | 现货992，basis C | N/A | 无exact外盘；Y/Y/N | 挤压/contango冲突 |
| 焦煤JM | JM2701；1585/1612.5；-1.77%/-3.47% | 87.37万/48.67万/-38,125；back 1.67% | 现货2462.5但basis C | N/A | 无exact外盘；Y/Y/N | 不追减仓下跌 |
| 红枣CJ | CJ701；7580/7630；-2.43%/-3.05% | 20.17万/22.52万/+3,946；contango 15.38% | CZCE仓单-261 | 制度无夜盘 | chain失败 | 等实体确认 |
| 豆粕M | M2701；3402/3422；+0.68%/+0.59% | 193.71万/273.38万/-51,707；contango 0.82% | 现货3394，basis C | N/A | 美豆最后1280.25；Y/Y/N | 报告不确认多头 |
| 玉米C | C2611；2255/2260；-0.40%/-1.61% | 46.69万/116.20万/-16,426；轻back 0.22% | C/context | N/A | USDA减产但接近预期；Y/Y/N | 高低开均不追 |
| 棕榈油P | P2701；10035/10151；-0.26%/-0.60% | 70.48万/58.33万/-7,195；contango 1.52% | 现货9624，basis C | N/A | BMD最后4816；Y/Y/N | 无方向优势 |
| 苯乙烯EB | EB2610；10036/10303；+0.20%/+6.47% | 170.59万/25.50万/-66,811；contango 0.68% | C/context | N/A | 原油右尾但成本传导不确定；Y/Y/N | 弹性衰减 |

周五国际收盘：Brent 104.61美元/桶、WTI 100.05，分别回落2.81%和2.37%，但全周涨幅仍超过8%。[Reuters油市，2026-09-11](https://www.reuters.com/business/energy/oil-prices-set-end-week-over-100-first-time-nearly-4-months-2026-09-11/)

截至07:00未见East-West管道恢复的权威确认。伊朗方面称与阿曼的谅解不包含立即重开霍尔木兹，周一会谈预计也不会签署正式协议；这支持供应风险持续，但没有周末成交价确认。[Reuters管道与红海](https://www.reuters.com/business/energy/saudis-shut-down-oil-pipeline-houthis-tighten-grip-red-sea-shipping-2026-09-12/)｜[Reuters霍尔木兹](https://www.reuters.com/world/middle-east/no-signed-hormuz-deal-expected-yet-oman-meeting-monday-iranian-official-says-2026-09-12/)

## 四、相比上一期真正变化

1. **核心期货质量从周六晚的run_failure恢复为重新验证成功。** 五所802合约100%同日、零critical error；这是数据质量变化，不是新行情。
2. **Night本次正确返回0条有效合约。** 802条均在合法窗口外，符合周末制度；不再把旧异常快照描述为本期Night。
3. **霍尔木兹短期外交缓和被削弱。** 周一会谈不预计签约，也没有立即开放安排；SC/FU/EC的催化持续性提高，但没有新增价格层。
4. **BRICS声明提供反证。** 伊朗与阿联酋共同支持“最大克制”和外交解决，说明尾部风险并非单向升级。[Reuters BRICS](https://www.reuters.com/world/china/brics-adopts-joint-declaration-urges-maximum-restraint-mideast-2026-09-12/)
5. **农业没有第二轮确认。** WASDE下调玉米单产，但结果接近预期，周五玉米、豆类收低；中国周一价格仍是首个有效验证。
6. **期权和实体模块无周末新增。** 最新有效截面仍为9月11日；不能把“无新增”写成数据失效，也不能冒充当前报价。

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：维持77；事件持续但未定价，周一等待相对SC强度。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：76→77；霍尔木兹无即时开放及Perim风险强化催化，但exact航线映射和参数仍缺。
- `COM-E-SC2610-GAP-20260905`：维持73；催化已满分，赔率不因新闻继续上调。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：维持67；无新增价格证据。
- `COM-M-C2611-WASDE-CORN-20260912`：维持56；仅实体一层。
- 没有成交反馈，不假设用户持仓；若此前确已建立能源多头，周末无法处置，周一应先把gap计入风险预算而非机械加仓。

## 五、产业链地图

- **最强尾部：FU—SC—LU—EC，方向偏多、置信度中高。** 9月11日价格量仓、深back及外部供应/航运事件支持；缺周末价格、SC/LU实体、exact运价与执行报价。最强反证是BRICS外交表态、管道可能迅速恢复及高油价需求破坏。
- **成品油强于化工扩散，置信度中。** FU back 8.69%，而EB仅小涨、OI大减并转contango；若周一FU强、EB/BZ/TA不跟，交易应保持产品相对价值思路，不能整条能化链一起追。
- **有色—贵金属方向冲突，置信度中低。** CU价格/OI支持关税溢价回吐，国内back反对趋势空；热CPI抬高实际利率，但金银周五反弹，黄金信用主题仍不成立。
- **最弱价格链：LC/PT/PD与黑色，置信度中低。** LC大跌但OI微降、近月仍back；JM价格弱但curve反向，不足以建立确认空头。
- **农产品：玉米偏多先验，大豆/油脂中性偏弱，置信度低。** WASDE属于C的实体层新增，尚未获中国价格、量仓和跨市场全口径确认。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 23/14/20/12/8 | **77** | 1、2、4 | 存在待验证优势｜部分｜休市，周一等30—45m |
| 2 | EC2610航运冲击多 | 23/15/20/11/8 | **77** | 1、2、4 | 存在待验证优势｜部分｜休市，周一日盘触发 |
| 3 | SC2610高位接受多 | 23/10/20/12/8 | **73** | 1、2、4 | 存在待验证优势｜部分｜休市，周一等45m |
| 4 | CU2610关税回吐空 | 19/15/14/9/10 | **67** | 1、4 | 存在待验证优势｜部分｜反抽失败才空 |
| 5 | C2611 WASDE玉米减产多 | 16/13/14/5/8 | **56** | 3 | 证据不足｜不足｜等待中国价格确认 |

分项均已复核。分数是研究排序，不是胜率或仓位。FU/SC/LU/EC共享中东供应—运输因子；不能独立叠加。C只有一个支持层，严格低于59。

## 七、前三名交易卡

### FU2611｜条件多｜77

事实：9月11日OHLC 4268/4417/4201/4289，settle 4292，1D +4.66%，ΔOI +4,920，back 8.69%。Current Night不适用，无OHLC、双收益锚或Night ΔOI。

- 市场隐含：产品短缺和运输风险已大幅计价；分歧是FU可能比SC更耐久。竞争解释是周五仅为成本滞后补涨。
- 窗口：9月14日09:00后等30—45分钟；首跳不追。
- 好成交：4210—4260获接受并重上4295/VWAP，先1/3仓；中成交：突破4418后成功回踩，仓位减半；直接高于4450为坏成交。
- 止损：30分钟接受4190下方；失效：跌破4100、back明显收窄且Brent低于100，或管道恢复并伴随运费回落。
- TP1 4420或1.5R；TP2 4600或3R；1—3D无扩张退出。
- 风险0.25%—0.35% NAV；与SC/LU/EC合并。
- 10吨/手，tick 1元/吨，tick value 10元；名义42,920元。动态margin/limit未确认；最后交易日10月30日，实物交割。最大损失不由计划止损限定。
- 压力：一板=`42,920×L`；两板=`42,920×[1-(1-L)^2]`，L下单前核验。

### EC2610｜条件多｜77

事实：EOD OHLC 2015.5/2108/1976/2032，settle 2044，1D +4.18%、5D +10.10%，ΔOI +2,200，back 22.36%。EC无制度Night。

- 市场隐含：红海绕行和近端运力稀缺已被部分计价。分歧是Hormuz不立即开放、Perim节点变化可能延长航运风险；竞争解释是EC航线已适应绕行，油轮风险不等于集装箱利润。
- 窗口：9月14日09:00后等30分钟。
- 好成交：1990—2035获接受并重上2045/VWAP；中成交：突破2110并回踩不破；直接高于2160放弃。
- 止损：30分钟接受1970下方；失效：跌破1962、back明显收窄且通航/管道确认恢复。
- TP1 2150或1.5R；TP2 2300或3R；1—5D时间止损。
- 风险0.25%—0.35% NAV，与能源/航运主题合并。
- repo未确认EC2610 multiplier、tick、动态margin/limit及确切最后交易日；参数未确认，不编一板/两板金额。

### SC2610｜条件多｜73

事实：EOD OHLC 815/838.3/786.5/812.9，settle 809.9，1D +5.40%、5D +18.56%，ΔOI +697，back 7.03%。Current Night不适用。

- 市场隐含：Hormuz和供给中断已形成高位back；分歧是绕行通道受损可能仍未完全计价。反证是中国零售油价传导受限、需求破坏及外交缓和。
- 窗口：9月14日首跳不追，等45分钟。
- 好成交：790—810承接并重上813/VWAP；中成交：突破838.5后回踩；直接高于850或接近涨停放弃。
- 止损：45分钟接受786下方；失效：跌破768.4、back收窄、Brent低于100且管道恢复。
- TP1 840或1.5R；TP2 875或3R；1—2D不扩张退出。
- 风险0.20%—0.35% NAV，与FU/LU/EC合并；不因新闻新鲜度增加仓位。
- 1,000桶/手，tick 0.1元/桶，tick value 100元；名义809,900元。最后交易日9月30日，实物交割；最迟9月18日前复核移仓SC2611。[INE合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 9月14日夜盘起相关合约限幅、保证金及开仓限制调整；以16%压力假设，一板约129,584元/手，两板复合约238,435元/手。[Reuters风控摘要](https://www.reuters.com/business/energy/shanghai-exchange-adjust-trading-limits-some-oil-futures-contracts-2026-09-11/)

## 八、商品期权专项

最新有效截面为9月11日EOD，本期无新增；周末事件后moneyness、Delta、IV和成本可能跳变。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 64.47%/43.35% | +21.11vol | -3.19/-0.62 | Y/Y/N | 事件凸性已贵，须周一重报价 |
| SC2611/10-14 | 60.92%/41.07%代理 | +19.84vol | -1.68/+2.16 | Y/N/N | 非SC2610同底层，仅context |
| CU2610/09-23 | 15.17%/14.80% | +0.36vol | +0.80/+1.89 | Y/Y/N | IV-RV近零不证明可成交便宜 |
| AG2612/11-24 | 51.14%/35.16% | +15.98vol | +6.33/+8.34 | Y/N/N | 上行尾偏贵、positioning不足 |
| LC2701/12-07 | 43.64%/38.62% | +5.02vol | 未稳定 | Y/N/N | 大跌后重算Delta |
| FG701/12-11 | 21.93%/18.86% | +3.07vol | +7.89/+3.29 | Y/Y/N | 无bid/ask |

期权目前没有优于裸期货的可执行证据，但这不等于全部期权昂贵。若周一取得人工实时双边报价，优先比较FU/SC有限损失call spread与线性期货；结构、Delta、最大净支出及Greeks必须届时确定。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、下一实际开盘风险地图

三层时间轴：①9月11日中国EOD；②周末没有Current Trading Day Night Session；③9月11日国际收盘与9月12—13日事件。下一交易窗口为9月14日09:00。

| 品种 | EOD→Night→海外/事件 | 周一可能gap | 等待 | 核心确认 |
|---|---|---|---|---|
| FU/LU | 强back→无Night→管道停运/Hormuz不即开 | 高开右尾但双向 | 30—45m | FU守4210/4295、产品强于SC |
| SC | +5.4%/深back→无Night→Brent最后回落、周末风险升 | 宽幅高开概率上升 | 45m | 786/810/813/838.5、Brent、管道状态 |
| EC | +4.18%/back22%→制度无Night→Perim/Hormuz | headline高开 | 30m | 1970/2045/2110、实际绕行和curve |
| EB/BZ/TA/PX | 国内弹性衰减→无Night→上游风险 | 跟油分化 | 45m | settlement、OI、curve、FU/SC breadth |
| CU | 国内弱但back→无Night→LME最后企稳 | 平/低开后反抽 | 45m | 108180/109200、LME、back |
| AG/AU | 中国跌→无Night→海外反弹、热CPI | 跌幅部分修复 | 30—45m | 美元、10Y、换月价差 |
| C/M/Y/P/OI | 中国未交易WASDE→无Night→美盘收低 | 报告影响不确定 | 45m | 中国gap、OI、near-next、CBOT电子盘 |
| LC/PT/PD | 急跌、实体不足→无Night | 双向高波动 | 45m | OI、curve、仓单有效期、风控 |
| FG/JM/RB | 价格与curve冲突→无Night | 震荡/偏弱 | 30—45m | FG963/1010、JM1580、钢材breadth |
| AP/JD/SF/SM/SI/PS | 制度无Night、无新增exact映射 | 国内信息主导 | 30—45m | 量仓、curve、实体更新 |

周一06:00后必须刷新Brent/WTI电子盘、Hormuz谈判预期、管道状态、红海通航和CBOT，再决定旧触发是否仍有效。

## 十、未来24小时与7天事件

- 未来24小时：沙特East-West管道损伤与重启、Perim岛控制及红海通航；任何恢复都可能压缩FU/SC/EC溢价。
- 9月14日：阿曼主持伊朗与海湾国家会谈；伊朗官员称不预计签署Hormuz协议。能源仓等待事实而不是标题。[Reuters](https://www.reuters.com/world/middle-east/no-signed-hormuz-deal-expected-yet-oman-meeting-monday-iranian-official-says-2026-09-12/)
- 9月14日09:00：中国商品日盘重开；所有条件至少延迟30—45分钟。
- 9月14日09:30：中国流通领域生产资料价格窗口；9月15日10:00工业、投资、消费、房地产及能源数据，以[国家统计局](https://www.stats.gov.cn/)为准。
- 9月14日21:00：下一合法中国夜盘，归属9月15日；核验SC/LU新限幅、保证金和开仓限制。
- 9月16日EIA周报常规窗口：关注成品油库存、炼厂开工与出口。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月15—16日美国时间FOMC，决议约9月17日02:00 BJT：CU/AU/AG提前降低Delta/Vega。[美联储](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- CFTC COT仅作滞后拥挤背景，不映射成中国会员确定方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月11日last-good价格、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差、跨期、跨品种/跨市场、风格/中性、波动率、偏度和事件凸性扫描；LPG按repo代码PG映射。另扫描动态品种，统一输入共77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为占位，RS/WR流动性不足。
- 黑色建材9/9：FG深contango、JM价曲冲突最显著。
- 有色贵金属12/12：CU入榜；AG/AU海外反弹反对追空。
- 能源炼化化工25/25：FU/SC入榜；EB/BZ/EG/TA/PX弹性衰减。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺新增实体与海外确认。
- 农产品油脂饲料畜牧22/22：C低分观察；M/P/Y/OI等待中国对WASDE定价。
- 航运与软商品全部扫描：EC入榜；CJ仓单变化不足以抵消弱价及深contango。
- Current Night应为0且实际0；上一异常快照仍隔离。
- 期权应覆盖64个、实际59个；5个数据不足，0个execution-ready。
- A/B级basis、exact import parity、可靠加工利润及beta-neutral篮子不可得，不发布伪套利。

风险预算：休市期间不新增风险。周一单笔试仓最大损失0.20%—0.35% NAV；新增价格与非价格层确认后才提高至0.75%—1.0%。FU/SC/LU/EC初始合并风险不超过0.75%。压力测试包括16%单板、两板复合、周末gap、流动性消失、保证金上调、相关性破裂、管道突然恢复及人民币急变。

固定六路径已从main回读验证：历史MD/JSON存在，latest日期与edition正确，status对应本期，manifest中`2026-09-13 + commodities_morning`恰好一条。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-13_commodities_morning.md) `archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无；周末休市，FU2611、EC2610、SC2610均移至9月14日09:00后30—45分钟重新验证。  
C. 今天应继续观察的机会：Hormuz会谈与沙特管道状态、FU相对SC强度、EC航运back、CU关税回吐，以及WASDE后C/M/P/Y/OI的中国价格确认。  
D. 今天必须避免或退出的交易：把周末0条Night写成缺失行情、周一首跳追FU/SC/EC/C、把油轮费率当EC exact套利、追空CU/AG/LC，以及在execution-ready=false时臆测期权成本。
