# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-11

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:48 BJT；信息截点：19:30；最近完整中国交易时段：9月11日日盘。周五晚无中国商品连续交易；下一日盘为9月14日09:00，下一夜盘为9月14日21:00并归属9月15日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；FU、EC、SC保留周一条件优势，但周末无中国夜盘，且20:30美国CPI、00:00 WASDE前不追风险。**

当前regime：**中东供给冲击仍支撑原油、燃料和航运曲线，但15:00后外油明显回撤；铜与贵金属重定价向下，锂电材料继续去风险，周末事件跳空主导赔率。**

最接近验证的是FU2611、EC2610、SC2610；缺失条件分别为周一产品链强于原油、航运backwardation继续维持、以及油价回撤后SC仍被接受。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，再按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、Options quality/surface及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。逐合约Night大文件由连接器返回截断内容；本期使用同一repo ref下统一输入的具体合约紧凑层，状态记为`truncated`，不是源文件为空。

- 统一输入：schema v2，`requested_date=2026-09-11`，19:18:53生成。
- Futures/Market State：五所802个合约、77个品种，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；4条placeholder已排除，无重复、非法OHLC、负成交量或负持仓。
- Physical：20项目标中18项按原生频率fresh，SC/LU unavailable；0项stale、0项carried-forward。所有basis均为C级且`eligible_for_physical_score=false`，只作背景。GFEX五项仓单仍是沿用快照，不计新增支持。
- External：17/22项按原生频率fresh、5项unavailable，全部`context_only`；不构成exact import parity。
- Options：9月11日当日截面，23,272条chain、384个series、59/64产品；CJ/MA/PL/PR/ZC失败。373个series局部surface-ready、78个positioning-ready、0个execution-ready；IV覆盖98.07%、OI覆盖69.35%、bid/ask覆盖0。Dealer Gamma方向未知。
- Metadata：partial；有效合约匹配73.32%，动态margin/limit覆盖不足。前三卡静态合约参数仅在可核实处使用，动态参数标未确认。

Night质量闸门通过：`trading_date=2026-09-11`、`night_session_date=2026-09-10`，06:00:37生成；`data_fresh/validation_passed/published/coverage_complete=true`。598个有效夜盘合约、55个品种，191个合法outside-window、13个no-night-trade；缺价格、缺时间戳、缺报价、查询错误与未解析合约均为0。

这批Night属于**今天早前已经完成、归属9月11日交易日的连续交易阶段**，只用于隔夜—日盘复盘，绝不是今晚未来行情。

## 三、商品仪表盘

1D/5D为同一具体合约结算收益；`Day`为今日close相对同一合约早前Night close。S/P/E为期权surface/positioning/execution readiness。海外报价为repo 19:18与公开市场15:00—19:30叠加层，不能写成中国期货已交易该信息。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | Basis/Physical | 早前Night close；vs close；Day | 海外/Options | 下一信号 |
|---|---|---|---|---|---|---|
| 燃料油FU | FU2611；4289/4292；+4.66%/+10.85% | 139.9万/22.09万/+4,920；back 8.69% | C/实体缺 | 4248；+5.04%；+0.97% | Brent 103.88；S/P/N | 周一回撤确认多 |
| 原油SC | SC2610；812.9/809.9；+5.40%/+18.56% | 30.53万/3.50万/+697；back 7.03% | C/不可得 | 816；+6.11%；-0.38% | 外油回撤；S/N/N | 不追，等45m |
| 集运EC | EC2610；2032/2044；+4.18%/+10.10% | 3.29万/2.59万/+2,200；back 22.36% | 不适用/无exact现货 | 无制度夜盘 | Hormuz航运风险；N/N/N | 周一日盘确认 |
| 低硫LU | LU2611；5453/5487；+4.53%/+10.85% | 22.06万/7.68万/+2,433；back 1.88% | C/不可得 | 5418；+3.65%；+0.65% | 外油回撤；新期权不足 | FU强于LU |
| 铜CU | CU2610；108990/108660；-2.75%/-0.41% | 20.93万/19.89万/-35,215；back 0.65% | C/现货仅context | 108360；-3.42%；+0.58% | LME 14190.5；S/P/N | 反抽失败空观察 |
| 白银AG | AG2612；15623/15676；-4.76%/-4.09% | 17.32万/19.34万/+8,788；contango 0.76%，roll | C/无实体 | Night为AG2610，不可比 | COMEX 64.28；S/N/N | CPI后再评估 |
| 碳酸锂LC | LC2701；134820/133960；-5.60%/-8.90% | 32.27万/40.76万/-1,124；back 1.68% | C；仓单沿用 | 无夜盘 | 无可靠exact外盘；S/N/N | 不是确认趋势空 |
| 玻璃FG | FG701；973/984；+2.29%/+1.34% | 218.6万/115.5万/-41,191；contango 7.37% | C；仓单0 | 982；+1.87%；-0.92% | 无exact外盘；S/P/N | 挤压回吐观察 |
| 焦煤JM | JM2701；1585/1612.5；-1.77%/-3.47% | 87.37万/48.67万/-38,125；back 1.67% | C/实体不足 | 1636；-0.79%；-3.12% | 无exact外盘；S/P/N | 价格弱、curve反对 |
| 红枣CJ | CJ701；7580/7630；-2.43%/-3.05% | 20.17万/22.52万/+3,946；contango 15.38% | C；仓单-261 | 无夜盘 | chain失败 | 弱势但不追空 |
| 豆粕M | M2701；3402/3422；+0.68%/+0.59% | 193.7万/273.4万/-51,707；contango 0.82% | C；现货仅context | 3440；+1.12%；-1.10% | CBOT豆1317.5；S/P/N | WASDE前不做 |
| 棕榈油P | P2701；10035/10151；-0.26%/-0.60% | 70.48万/58.33万/-7,195；contango 1.52% | C/实体不足 | 10228；+0.62%；-1.89% | BMD 4816；S/P/N | Night被日盘否定 |
| 苯乙烯EB | EB2610；10036/10303；+0.20%/+6.47% | 170.6万/25.50万/-66,811；contango 0.68% | C/实体不足 | 10370；+0.61%；-3.22% | 油强但弹性衰减；S/P/N | 不抄底、不追多 |
| PTA | TA701；6250/6312；+0.86%/+5.94% | 155.3万/113.9万/+7,444；back 5.54% | C/实体不足 | 6288；+0.87%；-0.60% | 油价context；S/P/N | 曲线确认但价格钝化 |
| LPG | PG2610；6893/7002；+1.18%/+7.34% | 24.10万/9.05万/-7,289；back 2.88% | C/实体不足 | 6970；+1.53%；-1.10% | 油价context；S/N/N | 价升仓减线索 |

19:18 repo记录Brent 103.73、WTI 99.21美元/桶。公开市场截至18:12 BJT附近为Brent约103.88、WTI约99.15，较前一时段分别回落约3.5%和3.3%；潜在海湾临时安排预期令外油回吐，而燃料品仍受紧张库存支撑。[Reuters油市，2026-09-11](https://www.reuters.com/business/energy/oil-prices-set-end-week-over-100-first-time-nearly-4-months-2026-09-11/)

美元指数约99.09、美国10年收益率接近5%；现货金在美国CPI前反弹约0.7%，说明中国AU/AG日盘下跌后，海外新增信息已转为部分反对追空。[Reuters美元](https://www.reuters.com/world/asia-pacific/dollar-holds-gains-yen-slips-mideast-energy-shock-deepens-2026-09-11/)｜[Reuters黄金](https://www.reuters.com/world/india/gold-track-third-weekly-loss-us-inflation-data-looms-2026-09-11/)

## 四、相比上一期真正变化

1. **完整T日EOD恢复并覆盖五所。** 昨晚因9月10日EOD缺失而无法做日盘判断；本期9月11日五所802合约、源日期100%一致，数据缺口解除。
2. **能化仍强，但外油在中国收盘后反向。** SC/FU/LU日盘继续上涨，FU、SC曲线back扩大；15:00后Brent/WTI明显回撤，周一gap不再是单向高开假设。
3. **EC成为新增三层候选。** 价格+4.18%、OI+9.27%、curve back 22.36%，同时海湾运输风险抬高；但EC没有夜盘、没有exact运价曲线和实体源，不能升级为立即交易。
4. **CU/AG晨间空头方向获EOD确认，但追空赔率下降。** CU日盘相对Night反弹0.58%，AG主力已roll到AG2612且海外金银反弹；20:30 CPI会再次重置美元和实际利率。
5. **LC/PT/PD的大跌缺少独立确认。** LC跌5.60%但OI微降且近月仍back；更像去风险与波动冲击，不能仅凭单日跌幅断言供需崩塌。
6. **期权截面更新到T日，执行闸门仍关闭。** 59/64产品可研究，bid/ask覆盖仍为0；新上市LU期权没有形成可用执行链。

旧建议台账：

- `COM-E-SC2610-GAP-20260905`：75降至71；日盘高838.3、低786.5，但无分钟路径，晨报条件是否按顺序触发未知。若此前确已建立，周末前至少减仓并把风险降至试仓级。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：74升至76；日盘延续和back确认，但晨报条件路径未知，且外油收盘后回撤。新触发移至周一。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：69维持；方向获EOD确认，但不能事后认定成交，周一只做反抽失败。
- `COM-M-AG2610-PPI-REPRICE-20260911`：主力换月后降为观察，原AG2610触发不迁移到AG2612；海外反弹与CPI是新反证。
- `COM-M-M2701-US-BUY-20260911`：Night上涨被日盘回吐，降出正式榜；等待WASDE，不把采购新闻当供需闭环。

## 五、产业链地图

- **最强：SC—FU—LU与EC运输链，偏多但周末不可执行，置信度中高。** 价格/OI、backwardation及IEA供给缺口形成1/2/3或4层支持；最强反证是外油回撤、需求破坏和潜在航运安排。IEA称2026年供应下降约570万桶/日、8月库存下降约310万桶/日，但同时需求下降约250万桶/日。[Reuters/IEA，2026-09-11](https://www.reuters.com/business/energy/global-2026-oil-supply-gap-deepen-delayed-return-normal-gulf-flows-iea-says-2026-09-11/)
- **最弱：锂电新材料和贵金属，偏弱但不追，置信度中。** LC、PT、PD与AG大跌；LC OI没有扩张且curve仍back，AG又受海外反弹与换月影响，方向证据没有形成三层闭环。
- **有色：CU关税溢价回吐，偏空，置信度中。** 价格与LME同向下跌，但国内backwardation反对过度空头；美国铜关税推迟是催化而非长期需求证据。[Reuters铜政策，2026-09-10](https://www.reuters.com/world/us/white-house-copper-tariff-plan-stalls-amid-affordability-concerns-sources-say-2026-09-10/)
- **聚酯—芳烃：上游强、下游弹性衰减。** EB/BZ早前Night仍涨，日盘却分别回吐约3.2%/3.7%；TA保留back但未扩张。竞争解释是成本冲击已被中国日盘预交易。
- **农产品与黑色：相对弱，无70分候选。** M/P的Night强度被日盘否定，J/JM日盘下行但curve不一致；WASDE和国内需求数据前不建立裸方向。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 22/16/18/12/8 | **76** | 1、2、4 | 存在待验证优势｜部分｜周一等30—45m |
| 2 | EC2610航运冲击多 | 22/16/17/11/8 | **74** | 1、2、4 | 存在待验证优势｜部分｜周一日盘触发 |
| 3 | SC2610高位接受多 | 22/11/18/12/8 | **71** | 1、2、3/4 | 存在待验证优势｜部分｜周一等45m |
| 4 | CU2610关税回吐空 | 19/17/15/9/9 | **69** | 1、4 | 存在待验证优势｜部分｜CPI后反抽失败 |
| 5 | AG2612实际利率空 | 18/16/15/10/9 | **68** | 1、2 | 证据冲突｜部分｜换月后待重定价 |

分项均已复算，未超过25/25/20/15/15上限。分数是研究排序，不是胜率或仓位指令。SC/FU/LU/EC共享中东供应—运输因子，不能按四笔独立风险叠加；所有期货最大损失均不由结构限定。

## 七、前三名交易卡

### 1. FU2611｜条件多｜76

**事实：** 9月11日EOD 4289/4292；早前Night OHLC 4268/4300/4201/4248，+5.04% vs前收、+3.58% vs前结算，Night ΔOI +6,392；日盘follow-through +0.97%，EOD ΔOI +4,920，back 8.69%。  
**市场定价：** 成品油紧张及运输中断已被大幅计价。  
**分歧与推断：** 若周一外油继续回落而FU仍守强，产品短缺溢价可能比原油headline更耐久；竞争解释是周五只是供应冲击的滞后补涨。  
**工具：** 具体FU2611期货；期权没有执行报价，不能以旧surface替代。

- 下一窗口：9月14日09:00；不把周五21:00当交易窗口。
- 好成交：开盘后等30—45分钟，4210—4260承接并重上4295/VWAP，先1/3仓。
- 中成交：突破4418并成功回踩，按好成交仓位的一半。
- 坏成交：直接高于4450或止损距离令滑点超过1R的20%，放弃。
- 止损：30分钟接受4190下方；逻辑失效：跌破4100、back明显收窄且Brent低于100。
- 退出：TP1 4420或1.5R；TP2 4600或3R；1—3D时间止损；周末前不存在新仓管理。
- 风险：0.25%—0.40% NAV；与SC/LU/EC合并不超过0.75%初始风险。
- 参数：10吨/手、tick 1元/吨、tick value 10元；按结算名义42,920元。动态margin/limit未确认；最后交易日2026-10-30，实物交割。
- 压力：一板损失=`42,920×L`；两板复合不利=`42,920×[1-(1-L)^2]`。计划止损不等于最大损失有限。

### 2. EC2610｜条件多｜74

**事实：** EOD 2032/2044，日高2108、低1976；1D +4.18%、5D +10.10%，ΔOI +2,200，near-next back 22.36%。EC制度上无夜盘。  
**市场定价：** 航运延误和运力稀缺已进入近月，但波动率61.47%说明追价成本高。  
**分歧与推断：** 若周末实际通航改善弱于市场预期，航运溢价可延续；最强反证是临时安排恢复流量、curve快速回落。  
**工具：** EC2610期货；没有exact运价篮子、beta中性或期权执行链，不称套利。

- 下一窗口：9月14日09:00；等30分钟。
- 好成交：1990—2035被接受并重上2045/VWAP，先1/3仓。
- 中成交：突破2110后回踩不破，仓位减半。
- 坏成交：直接高于2160，放弃。
- 止损：30分钟接受1970下方；逻辑失效：跌破1962且back明显收窄、海湾通航确认恢复。
- 退出：TP1 2150或1.5R；TP2 2300或3R；1—5D时间止损。
- 风险：0.25%—0.35% NAV，与能源/航运事件风险合并。
- 参数：repo未给出EC2610完整multiplier、tick、动态margin/limit及确切最后交易日，本卡标“参数未确认”，下单前须用INE最新规则复核；交割/结算风险不得用经验假设替代。
- 压力：因关键参数未确认，不给伪精确一板/两板金额；按账户实际保证金、交易所限幅及流动性消失做压力测试。

### 3. SC2610｜条件多｜71

**事实：** EOD 812.9/809.9；早前Night OHLC 815/819.4/786.5/816，+6.11% vs前收、+6.19% vs前结算，Night ΔOI +2,022；日盘相对Night -0.38%，EOD ΔOI +697，back 7.03%。  
**市场定价：** 高供应中断溢价仍在，但日盘没有继续扩大，且15:00后外油回撤。  
**主观判断：** 方向仍有支持，赔率明显差于FU；只做周一回撤后的重新接受。  
**工具：** SC2610期货；SC2611期权仅作期限研究，不能替代当前合约报价。

- 下一窗口：9月14日09:00；等45分钟，首跳不追。
- 好成交：790—810承接并重上813/VWAP，先1/3仓。
- 中成交：突破838.5并成功回踩，仓位减半。
- 坏成交：直接高于850或接近涨停，放弃。
- 止损：45分钟接受786下方；逻辑失效：跌破768.4、back显著收窄且Brent低于100。
- 退出：TP1 840或1.5R；TP2 875或3R；1—2D无扩张退出。
- 风险：0.25%—0.35% NAV；与FU/LU/EC合并。
- 参数：1,000桶/手、tick 0.1元/桶、tick value 100元；按结算名义809,900元。动态margin/limit未确认；最后交易日2026-09-30、实物交割；最迟9月18日前核验移仓SC2611。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 压力：一板=`809,900×L`；两板=`809,900×[1-(1-L)^2]`。周末gap与流动性消失可令实际损失超过计划止损。

## 八、商品期权专项

最新有效截面为9月11日T日，但所有目标结构`execution_ready=false`；以下只是surface研究，不是当前成交报价。

| Underlying/expiry | ATM IV | RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---:|---|---|
| FU2611/10-19 | 64.47% | 43.35% | +21.11vol | -3.19/-0.62 | Y/Y/N | 事件凸性已贵，不裸追call |
| SC2611/10-14 | 60.92% | 41.07%代理 | +19.84vol | -1.68/+2.16 | Y/N/N | 与SC2610不完全同合约，仅期限context |
| CU2610/09-23 | 15.17% | 14.80% | +0.36vol | +0.80/+1.89 | Y/Y/N | IV-RV近零不等于可成交便宜 |
| AG2612/11-24 | 51.14% | 35.16% | +15.98vol | +6.33/+8.34 | Y/N/N | 上行尾偏贵，CPI前不卖裸波动 |
| LC2701/12-07 | 43.64% | 38.62% | +5.02vol | 未稳定 | Y/N/N | 大跌后波动不宜用旧Delta |
| FG701/12-11 | 21.93% | 18.86% | +3.07vol | +7.89/+3.29 | Y/Y/N | 上行偏度贵，但无bid/ask |

HC、SS、LU新期权尚未形成可核实的执行链。Dealer Gamma方向未知；不输出权利金、净成本、当前Greeks或Gamma squeeze。若周一人工取得实时双边报价，才比较FU/SC有限损失call spread与期货；统一标记：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、下一实际开盘风险地图

四层时间轴：①9月11日中国EOD已完成；②今晨Night已完成且同属9月11日；③15:00—19:30海外油价回撤、金银反弹；④**周五晚无中国商品夜盘**。下一日盘是9月14日09:00，下一连续交易是9月14日21:00、归属9月15日交易日。

| 品种 | EOD→早前Night→海外新增 | 下一开盘预期 | 追价/等待 | 最重要确认 |
|---|---|---|---|---|
| FU/LU | EOD强、Night已涨、外油回撤 | 周一gap不确定 | 不追；30—45m | FU守4210、back、产品强于SC |
| SC | EOD强、Night完成大部定价、Brent回落 | 平/低开风险上升 | 不追；45m | 786/810/813、Brent 100、curve |
| EC | EOD强、无Night、周末航运headline | 大幅双向gap | 不追；30m | 1970/2045/2110、通航与back |
| CU | EOD弱、Night更弱、日盘小修复 | CPI后再定价 | 不追空；45m | 108180/109200、LME、back |
| AG/AU | 中国弱、海外金银反弹 | 低开优势下降 | 不追空；30—45m | CPI、美元、10Y、换月价差 |
| LC/PT/PD | 日盘急跌、无Night | 周一波动高 | 不接第一刀；45m | OI、curve、交易所参数 |
| FG/SA | Night偏强、日盘分化、深contango | 平/震荡 | 两边不追；30m | FG963/1010、仓单、contango |
| J/JM/RB | Night弱、日盘继续弱、curve冲突 | 偏低 | 不追空；45m | JM1580、钢材breadth、OI |
| M/P/Y/OI | Night上涨、日盘回吐、WASDE在前 | 周一gap依报告 | 不预挂裸单；45m | USDA产量/库存、CBOT/BMD |
| EB/BZ/TA/PX | Night强度有限、日盘弹性衰减 | 随油但分化 | 不抄底；45m | settlement、curve、FU/SC breadth |

## 十、未来24小时与7天事件

- **9月11日20:30 BJT：美国8月CPI。** CU/AU/AG、美元和实际利率将重定价；周末不能用中国期货即时对冲，已有风险宜降Delta/Vega。[BLS日程](https://www.bls.gov/schedule/news_release/cpi.htm)
- **9月12日00:00 BJT：USDA WASDE/Crop Production。** M/Y/P/OI/C/CF只保留有限风险表达或等待周一，不以旧CBOT context预判报告方向。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **9月12日约03:30 BJT：CFTC COT。** 只作滞后拥挤背景，不将会员或基金分类直接映射成中国市场方向。[CFTC发布日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **9月14日09:00 BJT：中国商品日盘重开。** CPI、WASDE和周末地缘信息将一次性形成gap；前45分钟只验证，不补追已过去的条件。
- **9月14日中国8月工业、投资、消费常规发布窗口附近：** 黑色、有色、化工需降低同因子风险，以国家统计局最终日程为准。[国家统计局日程](https://www.stats.gov.cn/sj/fbrc/)
- **未来7天EIA周度石油报告：** 关注成品油库存、炼厂开工与出口；SC/FU/LU在发布前合并降风险，以[EIA官方日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)为准。
- 持续监控Hormuz实际通航、港口等待、油轮/炼厂损失及中国成品油零售价上限。中国9月12日起汽油、柴油调价低于公式幅度，是下游需求与政策传导反证。[Reuters中国油价政策](https://www.reuters.com/business/energy/china-limits-fuel-price-increases-third-time-since-iran-war-began-2026-09-11/)

## 十一、覆盖核对、风险与归档

强制63个代码全部完成9月11日EOD、同合约1D/3D/5D/20D、量仓、curve及方向、基差、跨期、跨品种/跨市场、风格/中性、波动率、偏度与事件凸性扫描；LPG按repo代码PG映射。统一输入另含BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态品种，共77个产品。

- 实际取数且完成有效分析：70个；JR/PM/RI/WH/ZC为零价、零量或零OI占位，RS/WR为极低成交持仓，列不适用/流动性不足但不从范围删除。
- 黑色建材9/9：JM日盘继续弱但back反对；未入榜最异常为FG深contango与挤压回吐。
- 有色贵金属12/12：CU/AG入榜；未入榜AO/AD/NI/SN等为弱势但没有三层确认。
- 能源炼化化工25/25：FU/SC入榜；EC归航运单列；未入榜EB/BZ为Night强、Day大幅回吐。
- 新能源及GFEX新材料全部扫描：LC/PT/PD急跌，但仓单沿用、实体与海外缺失。
- 农产品油脂饲料畜牧22/22：M/P的Night被日盘否定；WASDE前无可执行优势。
- 航运与软商品全部扫描：EC入榜；CJ价格/OI/contango偏空但无Night与期权链。
- 期权应覆盖64个，实际59个；CJ/MA/PL/PR/ZC为数据不足，0个execution-ready。A级/B级basis、exact import parity、可靠beta-neutral篮子均不可得，本期不发布伪套利。

风险预算：单笔新试仓最大损失0.25%—0.40% NAV；出现周一价格确认后单主题仍不超过0.75%。SC/FU/LU/EC按同一中东供应—运输因子合并；CU/AG按美元—实际利率因子合并。压力测试包括周末gap、1/2个涨跌停、相关性破裂、保证金上调、流动性消失、IV跳升/塌陷、交割挤压与人民币急变。

归档状态在六路径从main回读后更新；CI仅作push后独立校验，不等待。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；周五晚无中国商品夜盘，FU2611、EC2610、SC2610条件全部移至9月14日09:00后30—45分钟验证。  
C. 今晚应继续观察的机会：FU产品强于SC、EC航运back、CU关税回吐、AG换月后的实际利率重定价，以及WASDE后的M/P/Y/OI。  
D. 今晚必须避免或退出的交易：把21:00当成周五可交易夜盘、周一首跳追FU/SC/EC、CPI前追空CU/AG、把LC单日大跌解释成供需崩塌、以及在execution-ready=false时臆测期权成本。
