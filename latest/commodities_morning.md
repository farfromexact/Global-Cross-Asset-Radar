# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-16

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:18 BJT；信息截点：07:00；最近完整中国EOD：9月15日；当前交易日：9月16日；下一可交易窗口：09:00日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC、LU、FU夜盘价仓共振，但原油已连续急涨，09:00只做回撤接受，不追第一跳。**

当前regime：**沙特Yanbu与East-West管道扰动把能源由headline行情推向实物流中断；SC重新领涨，LU/FU与PX—TA跟随；强美元、5%美债收益率和FOMC加息预期压制金属与内需估值。**

最接近触发的是SC2611、LU2611、FU2611。三者都缺09:00后回撤接受；SC/LU实体数据缺失，能源期权无可执行双边报价。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按Top候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)和[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-15`，9月16日06:16:43生成；EOD=T-1、Night trading date=T是正常晨间组合。
- Futures：9月15日EOD，五所801合约、77产品；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；9条placeholder排除。
- Market State：同合约1D/3D/5D/20D完整；EB发生主力切换，夜盘代表EB2610不能替代交易卡EB2611。
- Physical：20项目标中18项按原生频率fresh、SC/LU unavailable；无stale、无目标项carried-forward。Basis均为C级或不可用，只作context。
- External：repo日频17/22 fresh、5项unavailable，全部`context_only`；WTI/Brent代理收105.48/108.48美元/桶。Reuters主力结算105.83/108.75，口径差异使其不能构成exact套利。
- Options：9月15日18,936条、340 series、52/64产品；330个surface-ready、81个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖97.73%/69.60%/0。SC及SHFE金属因供应商返回9月16日记录、与请求日不符而失败，不能沿用旧面冒充9月15日截面。
- Metadata：partial；有效合约匹配73.28%，multiplier/tick/margin/limit约29.71%，last-trading-day约67.29%。

Night质量闸门：`trading_date=2026-09-16`、`night_session_date=2026-09-15`，05:58:52生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。801个请求合约中587个有效、覆盖55个产品；204个outside-window、10个no-night-trade；missing timestamp/price/quote、query error、unresolved均为0，warnings为空。

该Night属于今天已经完成的连续交易阶段。逐产品紧凑层可用；原始`night_session/latest.json`经connector返回0字节payload，但状态及统一输入明确存在587条，故读取状态记为`empty connector payload / source not empty`。近次月两腿无法同时审计，Top 3不强拼Night curve；`night_session_fallback_used=false`。

## 三、商品仪表盘

1D/5D为9月15日同合约结算收益；Night为归属9月16日的已完成session。Basis均为C/context或缺失；S/P/E为surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical | Night close；vs close/vs settle；ΔOI；时间 | 07:00海外；Options；信号 |
|---|---|---|---|---|---|
| 原油SC | SC2611；838.6/836.2；+7.69%/+25.74% | 21.47万/3.98万/+1,174；back 7.71%、z1.10 | 缺失 | 860；+2.55%/+2.85%；+2,275；02:30 | WTI 105.83；N/N/N；等45m |
| 低硫LU | LU2611；5639/5624；+2.18%/+9.89% | 14.13万/6.86万/-2,904；back 2.84% | 缺失 | 5793；+2.73%/+3.00%；+5,399；23:00 | Brent 108.75；N/N/N；等30m |
| 燃料油FU | FU2611；4476/4482；+2.68%/+15.13% | 94.57万/21.19万/-7,446；back 15.84%、z2.27 | 现货7362.5，C | 4551；+1.68%/+1.54%；+14,860；23:00 | 油品供应风险；Y/N/N；等30m |
| PX | PX611；9518/9490；+0.89%/+7.04% | 40.96万/16.51万/+2,953；back 0.57%、仅2观测 | 9600，C | 9756；+2.50%/+2.80%；+13,067；23:00 | 原油强；Y/N/N；等45m |
| PTA | TA701；6460/6436；+0.63%/+6.38% | 173.74万/116.93万/-8,222；back 2.16%、仅2观测 | 7045.25，C | 6532；+1.11%/+1.49%；+23,037；23:00 | 成本推动；Y/Y/N；不追 |
| 苯乙烯EB | EB2611；9901/9874；+0.28%/+4.80% | 41.65万/23.38万/+12,931；contango 0.60%、roll | context | 代表EB2610=10375；+1.84%/+2.00%；+5,791 | 非同合约；Y/Y/N；不硬分解 |
| 镍NI | NI2610；123950/124080；-0.80%/-2.25% | 10.95万/12.69万/-2,851；contango 0.28% | context | 121020；-2.36%/-2.47%；+4,509；01:00 | LME 15935、美元强；N/N/N；反抽失败空 |
| 铜CU | CU2610；107030/106930；-1.16%/-3.02% | 10.80万/18.01万/-7,753；back 0.65%、z1.53 | 107675，C | 107200；+0.16%/+0.25%；-4,878；01:00 | LME 14115；N/N/N；旧空头降级 |
| 黄金AU | AU2612；932.3/931.22；-1.62%/-2.84% | 8.19万/16.92万/+4,086；轻contango | C/context | 代表AU2610=932.02；+0.24%/+0.39%；-3,848 | 现货金4293；N/N/N；不追空 |
| 白银AG | AG2612；15452/15460；-1.85%/-4.80% | 10.75万/20.27万/+3,017；轻contango | C/context | 代表AG2610=15600；+1.20%/+1.11%；-860 | 银63.41；N/N/N；换月不硬分解 |
| 玻璃FG | FG701；909/922；-2.33%/-4.65% | 121.22万/123.73万/+19,098；back 1.67%、仅2观测 | 1008，C | 908；-0.11%/-1.52%；+22,179；23:00 | 无exact外盘；Y/Y/N；不追空 |
| 纯碱SA | SA701；1009/1018；-1.83%/-4.95% | 121.62万/128.16万/-9,665；contango 0.81% | 1090，C | 1009；0.00%/-0.88%；+20,575；23:00 | 无exact外盘；局部/N/N；弹性弱 |
| 豆粕M | M2701；3385/3374；-0.30%/-1.20% | 118.40万/271.59万/+38,013；contango 1.06% | 3382，C | 3414；+0.86%/+1.19%；+31,584；23:00 | CBOT豆1319；Y/Y/N；待日盘接受 |
| 棕榈油P | P2701；9992/10031；-0.07%/-3.74% | 55.71万/58.63万/+7,213；contango 0.99% | 9608，C | 10030；+0.38%/-0.01%；-707；23:00 | BMD 4883；Y/Y/N；双锚分歧 |
| 碳酸锂LC | LC2701；129120/129640；-2.94%/-9.33% | 18.72万/41.87万/+7,123；back 1.15%、仅2观测 | 131000，C | 制度无Night | exact海外缺；Y/N/N；不接刀、不追空 |

Reuters显示9月15日WTI结算105.83美元/桶、+4.38%，Brent 108.75、+2.9%；Yanbu装运暂停、部分沙特赴欧货取消，供应冲击得到真实物流确认，而不仅是标题风险。[Reuters油市，2026-09-15](https://www.reuters.com/business/energy/oil-prices-rise-saudi-pipeline-outage-fresh-attacks-raise-supply-concerns-2026-09-15/)｜[Reuters沙特货流，2026-09-15](https://www.reuters.com/business/energy/polands-orlen-rushes-find-alternatives-saudi-oil-supply-traders-say-2026-09-15/)

美元走强、10年美债收益率最高约5.041%，市场在FOMC前高度定价25bp加息；现货金约4293美元/盎司、银约63.41。[Reuters美元与美债，2026-09-15](https://www.reuters.com/world/africa/dollar-near-two-week-high-oil-surge-lifts-yields-fed-hike-bets-2026-09-15/)｜[Reuters贵金属，2026-09-15](https://www.reuters.com/world/india/gold-holds-ground-investors-await-fed-policy-cues-2026-09-15/)

## 四、相比上一期真正变化

1. **SC重新确认领涨。** Night相对前收+2.55%、ΔOI +2,275，且收860接近夜高865；上一晨报的“SC headline弹性衰减”已被新物流中断证据部分推翻，评分81→85。
2. **LU/FU共同跟随，但结构不同。** LU +2.73%且增仓5,399，FU +1.68%且增仓14,860；前者价格弹性更高，后者EOD back更极端、拥挤风险更大。
3. **PX—TA—EB—BZ扩散变宽。** PX/TA/EB/BZ相对前收分别+2.50%/+1.11%/+1.84%/+1.63%，且夜盘代表合约均增仓；这是成本冲击确认，不是下游需求确认。
4. **NI成为非能源最大异常。** NI2610夜盘-2.36%、ΔOI +4,509；强美元和高实际利率支持弱势，但缺新鲜期权面和实体证据，封顶69。
5. **CU旧空头触发降级。** CU夜盘相对前收+0.16%、OI下降，未确认晚报“反抽失败空”；仍偏弱，但不再列Top 5。
6. **Options可用范围进一步收窄。** SC和SHFE金属因source-date冲突失败；FU曲面可用但ATM IV 71.45%、高于RV20约28.59vol，凸性昂贵且无bid/ask。

旧建议台账：

- `COM-E-SC2610-GAP-20260905`：81→85，现交易合约SC2611不变。昨晚825—836/重上840的条件在Night OHLC范围内，但无分钟路径、无成交反馈，触发状态未知；不得假设持仓，今日触发随新价格上移。
- `COM-M-LU2611-PRODUCT-RELATIVE-20260915`：69→81；Night价格与OI新增确认，但实体、期权和完整参数仍缺。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：73→80；Night增仓上涨修复EOD价涨仓减，旧条件是否触发未知。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：69→64；Night未确认弱势，保留观察、不反向。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：维持已退出；9月15日EOD跌破旧止损锚2035且无Night，不重新包装成新多头。
- `COM-E-FG701-WEAK-CONT-20260914`：59维持；Night相对前收仅-0.11%，不追空。

## 五、产业链地图

- **最强：SC—LU—FU能源链，偏多，置信度高。** EOD价格/持仓、近端back、Night价仓以及海外实物装运中断构成1/2/4三层支持；SC/LU实体缺失、FU basis仅C级、期权凸性昂贵或缺失。最大反证是管道数日内修复、需求破坏和FOMC加息。
- **次强：PX—TA—EB—BZ成本扩散，偏多但置信度中。** PX/TA Night价仓共振，EB/BZ也跟涨；曲线历史短、EB代表合约不一致，下游利润与订单缺失，不能称需求牛市。
- **最弱：NI及部分内需金属，偏空但置信度中。** NI夜盘价跌仓增只作归因线索；强美元/高收益率提供第4层，实体和期权缺失。CU已出现反抽，弱势不整齐。
- **黑色建材：价格弱、边际弹性低，置信度中低。** FG/SA相对前收近零，JM/I/RB夜盘小幅反弹；9月15日中国工业增5.2%但零售仅0.4%、房地产投资同比降19.9%，解释内需弱但不构成09:00追空信号。[Reuters中国数据，2026-09-15](https://www.reuters.com/world/china/chinas-factories-rev-up-slower-consumption-highlights-deepening-economic-2026-09-15/)
- **农产品：豆粕局部修复，其余中性。** M夜盘+0.86%且增仓，但EOD趋势、curve和高质量basis未共振；C/P双锚分歧或幅度不足。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2611回撤接受多 | 25/16/20/15/9 | **85** | 1、2、4 | 存在待验证优势｜充分但高位拥挤｜等待09:45 |
| 2 | LU2611供应冲击延续多 | 23/17/20/13/8 | **81** | 1、2、4 | 存在待验证优势｜部分｜等待09:30/参数 |
| 3 | FU2611产品链延续多 | 23/15/20/14/8 | **80** | 1、2、4 | 存在待验证优势｜部分且凸性昂贵｜等待09:30 |
| 4 | PX611成本冲击多 | 21/15/18/9/9 | **72** | 1、2、4 | 存在待验证优势｜部分、curve历史短｜等待09:45 |
| 5 | NI2610弱势延续空 | 19/16/15/9/10 | **69** | 1、4 | 存在待验证优势｜部分｜反抽失败/期权缺失 |

分项均复算且不超过上限。NI只有两层，严格封顶69。SC/LU/FU/PX共享能源成本因子，不能四笔独立叠加；所有期货最大损失均不由计划止损限定。

## 七、前三名交易卡

### 1. SC2611｜条件多｜85

**事实：** previous close/settlement=838.6/836.2；Night OHLC=819.1/865/811.3/860，vs close +2.55%、vs settlement +2.85%，Night ΔOI +2,275；EOD back 7.71%。

**市场定价：** 近端供应中断和沙特替代路线失灵已被高价与back大量计入。  
**我们的分歧：** Yanbu装运取消把事件从风险溢价推进到实物流，但860附近的赔率明显差于方向确定性。最强竞争解释是管道数日内恢复、需求破坏及加息压缩风险资产。

- 最佳表达：SC2611单腿条件多；1手为1单位，不用失败的SC期权面替代有限损失结构。
- 好成交：09:45后842—855获得接受并重上860/VWAP，先1/3仓。
- 中成交：突破866后回踩858—866不破，仓位减半。
- 坏成交：直接高于875、滑点超过计划1R的20%或盘口显著变薄，放弃。
- 止损：45分钟接受836下方；计划止损不保证最大损失。
- 逻辑失效：跌破811、back低于6.5%且Brent低于104，或East-West管道/Yanbu装运明确恢复。
- 退出：TP1 880或+1.5R；TP2 920或+3R；1—2D无扩张退出。
- 风险：0.15%—0.25% NAV；能源成本主题初始合并≤0.60%。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；Night close名义860,000元。repo确认最后交易日10月30日、最后交割日11月6日；实物交割，10月中旬前移仓。[INE原油手册](https://www.ine.cn/eng/market/futures/energy/sc/manual/202004/W020250806318691873930.pdf)
- 动态margin/limit未确认；以待复核的16%压力假设，一板约137,600元/手，两板复合约253,664元/手。

### 2. LU2611｜条件多｜81

**事实：** previous close/settlement=5639/5624；Night OHLC=5553/5797/5470/5793，vs close +2.73%、vs settlement +3.00%，Night ΔOI +5,399；EOD back 2.84%。

**市场定价：** 航运燃料与原油供应冲击已部分计价。  
**我们的分歧：** LU的Night弹性高于SC/FU，可能反映清洁船燃供给更紧；反证是实体模块不可用、EOD曾减仓、back远弱于FU。

- 最佳表达：LU2611单腿条件多；缺可靠跨品种beta，不做伪中性FU/LU篮子。
- 好成交：09:30后5690—5770获得接受并重上5795/VWAP，先1/3仓。
- 中成交：突破5800后回踩5750—5800不破，仓位减半。
- 坏成交：直接高于5900或买卖深度不足，放弃。
- 止损：30分钟接受5650下方。
- 逻辑失效：跌破5639、back低于1.5%、Brent低于104，或相对SC/FU重新显著转弱。
- 退出：TP1 5900或+1.5R；TP2 6100或+3R；1—3D无扩张退出。
- 风险：0.15%—0.25% NAV，并入能源成本主题。
- repo仅确认最后交易日10月30日、最后交割日11月6日；multiplier、tick、tick value、动态margin/limit未确认。参数补齐前只能作为研究条件单，不给伪精确一板/两板金额。

### 3. FU2611｜条件多｜80

**事实：** previous close/settlement=4476/4482；Night OHLC=4400/4564/4350/4551，vs close +1.68%、vs settlement +1.54%，Night ΔOI +14,860；EOD back 15.84%、z2.27。

**市场定价：** 成品油紧张已经体现在极端back和高IV。  
**我们的分歧：** Night增仓修复EOD减仓反证，但FU价格弹性低于LU/SC；竞争解释是拥挤近月仅随原油补涨。

- 最佳表达：FU2611单腿条件多；期权ATM IV约71.45%、execution-ready=false，不以未报价call spread冒充有限风险。
- 好成交：09:30后4480—4540获得接受并重上4555/VWAP，先1/3仓。
- 中成交：突破4565后回踩4535—4565不破，仓位减半。
- 坏成交：直接高于4640、滑点超过1R的20%或相对LU/SC继续走弱，放弃。
- 止损：30分钟接受4450下方。
- 逻辑失效：跌破4400、back低于12%、Brent低于104，或产品相对原油持续走弱。
- 退出：TP1 4650或+1.5R；TP2 4800或+3R；1—3D无扩张退出。
- 风险：0.15%—0.25% NAV，与SC/LU/PX合并。
- 参数：10吨/手、tick 1元/吨、tick value 10元；Night close名义45,510元。repo确认最后交易日10月30日、最后交割日11月3日；实物交割。[SHFE燃料油规则](https://www.shfe.com.cn/eng/services/Rules/SHFERules/202512/t20251231_829986.html)
- 动态margin/limit未确认；以16%压力假设，一板约7,282元/手，两板复合约13,399元/手。

## 八、商品期权专项

最新有效目标截面为9月15日EOD；Night已改变能源、聚酯和金属底层的moneyness与Delta。全部结构`execution_ready=false`。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 71.45%/42.86% | +28.59vol | -3.38/+0.13 | Y/N/N | 事件凸性极贵、OI覆盖89.5% |
| SC2611 | 产品失败 | N/A | N/A | N/N/N | source-date冲突，不沿用旧面 |
| LU2611 | 无可核实series | N/A | N/A | N/N/N | 期权表达不可评 |
| PX611/09-28 | 44.43%/31.13% | +13.30vol | +1.84/+0.39 | Y/N/N | 近到期、Night后Delta失真 |
| TA701/12-11 | 35.39%/26.15% | +9.23vol | +3.41/+1.39 | Y/Y/N | 上行尾已贵 |
| EB2611/10-23 | 40.89%/29.46% | +11.43vol | +2.70/+0.97 | Y/Y/N | 成本扩散已计价一部分 |
| FG701/12-11 | 21.80%/25.35% | -3.56vol | +5.45/+1.98 | Y/Y/N | IV<RV不单独证明便宜 |
| M2701/12-16 | 14.05%/10.45% | +3.59vol | +4.17/+1.91 | Y/Y/N | Night反弹仍缺实体闭环 |
| LC2701/12-07 | 44.99%/38.99% | +6.00vol | +1.84/+1.49 | Y/N/N | 无Night、实体仅C级 |

期权没有优于裸期货的可执行证据。若09:00后取得实时双边报价，才比较FU同到期1:1牛市call spread；执行价、Delta、净支出、Greeks、盈亏平衡、滑点和行权交割均须重算。禁止裸卖event vol；Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月15日；②Current Trading Day Night=归属9月16日、已完成；③07:00 Overseas=9月15日国际结算及截至07:00最新可核实事件。

| 品种 | EOD→Night→海外 | 09:00判断 | 追价/等待 | 核心确认 |
|---|---|---|---|---|
| SC | EOD+7.69%/back7.71%→Night+2.55%/仓增→WTI+4.38% | 偏高，大量信息已交易 | 不追；45m | 836/855/860/866、back、Yanbu |
| LU | EOD+2.18%→Night+2.73%/仓增→Brent+2.9% | 偏高、弹性最强 | 不追；30m | 5650/5770/5795、相对SC/FU |
| FU | EOD+2.68%/深back→Night+1.68%/仓增→物流中断 | 偏高但相对弱 | 不追；30m | 4450/4540/4555、back |
| PX/TA | EOD温和涨→Night+2.50%/+1.11%、仓增→原油强 | 偏高、成本推动 | 45m | PX9756、TA6532、EB/BZ breadth |
| EB/BZ | EOD混合→Night代表合约+1.84%/+1.63%→原油强 | 高开后分化 | 45m | 同合约确认、下游接受、curve |
| NI | EOD-0.80%→Night-2.36%/仓增→美元/收益率强 | 低开概率高 | 不追空；45m | 120690/121500/123000、LME |
| CU/ZN/AL | EOD弱→Night近零/小涨、减仓→美元强 | 平/低开、易反抽 | 30—45m | CU106890/107200/107630、back |
| AU/AG | EOD下跌→代表合约反弹→外盘金弱银强 | 合约错配、双向 | 45m | exact主力、DXY、10Y、换月 |
| FG/SA | EOD弱→相对前收-0.11%/0%→无exact外盘 | 平开、反抽风险 | 不追空；30m | FG907/913、SA1007/1015、OI |
| M/C/P | EOD偏弱→M反弹、C/P近零→外盘日频混合 | 分化 | 45m | M3382/3414/3420、basis与curve |
| EC/LC/AP/JD/SF/SM/SI/PS | 制度无Night | 09:00才有新价格 | 30—45m | 量仓、curve、实体更新 |

外油结算涨幅与中国Night同向，但SC/FU/LU已经吸收相当部分；真正可交易的新信息弹性应看09:00后是否守住Night回撤区，而不是机械映射外油涨幅。美元与美债收益率上行压制金属，repo的USD/CNH不可用，不能量化人民币贡献。

## 十、未来24小时与7日事件

- 9月16日09:00：中国日盘；SC/LU/FU分别至少等待45/30/30分钟。
- 9月16日22:30附近：EIA周度石油数据，重点看商业原油、汽油/馏分油库存、炼厂开工与出口；能源仓提前降Delta，期权仅用有报价的有限净支出结构。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)
- 9月17日02:00附近：FOMC决议与SEP。市场高度定价25bp加息，SC/FU/LU也面临美元与需求端冲击；CU/AU/AG避免裸Vega和隔夜高Delta。[美联储日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 未来24小时：East-West管道修复、Yanbu恢复、沙特取消货物、Hormuz/Perim通航及利比亚油田；任何明确恢复都压缩SC/LU/FU/PX/EC共享因子。
- 9月17日20:30附近：USDA周度出口销售常规窗口；M/C/Y/P/OI只按采购兑现与基差反应调整，不把报告标题直接映射为新仓。
- 9月19日03:30附近：CFTC COT常规窗口，仅作滞后拥挤背景，不映射为中国会员确定方向。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 未来7日：美国玉米/大豆收割天气、中国采购、马棕产量出口；OPEC+/IEA若无计划内新月报，仅跟踪临时供应声明，不虚构催化。

## 十一、覆盖、风险与归档核对

强制63个代码及动态新增品种均进入覆盖核对；对可得数据完成价格、1D/3D/5D/20D、量仓、curve、基差/跨期、跨品种/跨市场、加工链、风格/中性、波动率、偏度和事件凸性扫描。

- 应覆盖：强制63代码；统一输入实际77产品；期权应覆盖64产品。
- 实际取数且已分析：70个期货产品；Night 55产品/587合约；期权52产品、340 series。
- 数据不足：SC/LU实体不可用；期权12产品失败、0 execution-ready；Night逐合约大文件回读payload为空，无法计算Top 3 exact near-next Night curve；A/B级basis、exact import parity、可靠加工利润和可执行期权成本不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为零价、零量或零OI占位；RS/WR流动性极低。它们保留覆盖记录，不进入异常排行。
- 黑色建材9/9：FG/SA EOD弱但Night弹性衰减；JM/I/RB小幅反弹，无三层方向共振。
- 有色贵金属12/12：NI低分入榜；CU旧空头降级，AU/AG代表合约不一致且FOMC前方向冲突。
- 能源炼化化工25/25：SC/LU/FU/PX入榜；TA/EB/BZ扩散但缺需求层，EC旧多头维持退出。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺高质量实体与exact海外映射，LC跌势不追。
- 农产品油脂饲料畜牧22/22：M夜盘修复最显著，但curve/basis/实体不足；C/P/Y/OI无三层优势。
- 航运与软商品全部扫描：EC无Night且旧多逻辑受价格反证；CF/CY/SR/AP/CJ/PK未发现可评分三层异常。

风险预算：单笔试仓最大损失0.15%—0.25% NAV；新增价格、curve及非价格层确认后才考虑0.75%—1.0%。SC/LU/FU/PX/EC共享主题初始合并≤0.60%，确认后总主题≤2.5%。压力测试包含16%一板/两板、管道突然恢复、FOMC加息超预期、夜盘gap、流动性消失、保证金上调、相关性破裂、IV跳升/塌陷、交割挤压和人民币急变。

固定六路径已从main回读验证：历史MD/JSON存在，latest日期与edition正确，status对应本期，manifest中`2026-09-16 + commodities_morning`恰好一条。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-16_commodities_morning.md) `archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2611在09:45后842—855承接并重上860，或LU2611在09:30后5690—5770承接并重上5795，或FU2611在4480—4540承接并重上4555；同主题初始风险合计≤0.60%。  
C. 今天应继续观察的机会：PX611成本冲击、NI2610反抽失败空、M2701夜盘修复、FG/SA弱势弹性衰减，以及能源期权09:00后实时报价。  
D. 今天必须避免或退出的交易：09:00追SC/LU/FU/PX第一跳、低开追空NI/FG/SA、重启EC旧多、把外油或C级basis当exact套利，以及在execution-ready=false时臆测权利金、Greeks或最大损失。
