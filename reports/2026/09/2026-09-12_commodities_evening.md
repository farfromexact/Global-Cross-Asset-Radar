# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-12

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-12 19:36 BJT；信息截点：19:30 BJT；最近完整中国交易时段：9月11日日盘；下一实际日盘：9月14日09:00；下一实际夜盘：9月14日21:00，归属9月15日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；沙特东西向管道停运抬高周一能源与航运跳空风险，但周末无中国夜盘且消息尚无价格确认。**

当前regime：**中东能源—航运供给尾部风险再升级、周五外油高位回撤、国内能源深backwardation、热通胀约束金属、WASDE玉米减产基本落在预期内。**

最接近验证的是FU2611、EC2610、SC2610；缺失条件依次为周一产品相对原油的强度、集运对曼德海峡风险的实际定价、以及SC高开后的回撤接受。今晚没有中国21:00连续交易，不存在可下的新条件单。

## 二、数据质量与覆盖

本期先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，再下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)及具体候选的期权曲面和合约元数据。

- 统一输入：schema v2，`requested_date=2026-09-11`，2026-09-12 19:12:28 BJT生成。
- Futures：19:03周末刷新失败，根状态为`full_market_ready=false`、`source_date_match_pct=0`、15个critical errors；但`data/latest.json`仍是9月12日06:00生成并通过验证的9月11日last-good：五所802个合约、源日期匹配100%、原快照critical errors=0，4条placeholder排除。失败属于`run_failure`，不推翻截至周末最新应得EOD。
- Market State：同合约1D/3D/5D/20D窗口截止9月11日；19:03包装状态降级，底层last-good未被新交易时段替代。本期标`carried_last_good`，不冒充周六行情。
- Physical：20项目标中18项保留各自原生频率下的9月11日last-good，SC/LU unavailable；5条GFEX仓单沿用且较旧。所有basis为C级、`eligible_for_physical_score=false`，只作context。
- External：9月12日19:11刷新，源日期为9月11日最后国际交易时段；17/22可用、5项unavailable，均为`context_only`。周末事件单列，不写成可成交价格。
- Options：最新有效截面为9月11日，23,272条chain、384个series、59/64产品；CJ/MA/PL/PR/ZC失败。373个series surface-ready、78个positioning-ready、0个execution-ready；bid/ask覆盖0。周末包装状态为stale/未发布，但该截面仍是最新应得研究快照，不是当前报价。
- Metadata：partial；有效合约匹配约73.32%，动态margin/limit覆盖不足。前三卡静态参数按repo/交易所规则核验，缺项明确留白。

Night状态虽显示`trading_date=2026-09-12`、`night_session_date=2026-09-11`，06:00:26生成，fresh/validated/published/coverage_complete均为true，596个合约、55个品种，且无缺价、缺时间戳、query或unresolved错误；但**9月12日是周六，周五晚制度上没有中国商品夜盘**。因此该日期违反交易日历语义，596条全部标为`calendar_semantic_invalid`并隔离，不自行重标为9月14日，也不用于价格、OI、curve或隔夜—日盘分解。`overnight_day_decomposition_used=false`。

## 三、商品仪表盘

以下全部为9月11日中国last-good EOD。Night列统一为“隔离”，不是数据为空；周末映射只表示事件/最后收盘背景。S/P/E为期权surface/positioning/execution readiness。

| 板块 | 合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | basis/Physical | Night/周末海外 | Options；周一信号 |
|---|---|---|---|---|---|---|
| 燃料油 | FU2611 | 4289/4292；+4.66%/+10.85% | 139.93万/22.09万/+4,920；back 8.69% | C/context | Night隔离；Brent周五104.61，沙特管道周末停运 | Y/Y/N；等30—45m |
| 原油 | SC2610 | 812.9/809.9；+5.40%/+18.56% | 30.53万/3.50万/+697；back 7.03% | SC Physical缺失 | Night隔离；供应右尾升级 | Y/N/N；高开不追、等45m |
| 集运 | EC2610 | 2032/2044；+4.18%/+10.10% | 3.29万/2.59万/+2,200；back 22.36% | 无exact运价曲线 | 制度无Night；胡塞控制Perim岛 | N/N/N；09:30后确认 |
| 低硫燃油 | LU2611 | 5453/5487；+4.53%/+10.85% | 22.06万/7.68万/+2,433；back 1.88% | LU Physical缺失 | Night隔离；外油/航运右尾 | 新链未验证；FU相对优先 |
| 铜 | CU2610 | 108990/108660；-2.75%/-0.41% | 20.93万/19.89万/-35,215；back 0.65% | C/context | Night隔离；LME最后14225.5 | Y/Y/N；反抽失败才空 |
| 白银 | AG2612 | 15623/15676；-4.76%/-4.09% | 17.32万/19.34万/+8,788；contango 0.76%、roll | C/context | Night隔离；COMEX银周五反弹 | Y/N/N；不追空 |
| 黄金 | AU2612 | 944.94/944.54；-1.36%/-2.93% | 10.48万/15.84万/+7,777；轻contango | C/context | Night隔离；现货金周五约+1.1% | Y/N/N；实际利率反证 |
| 碳酸锂 | LC2701 | 134820/133960；-5.60%/-8.90% | 32.27万/40.76万/-1,124；back 1.68% | 仓单沿用、stale | 制度无Night | Y/N/N；不接第一刀 |
| 玻璃 | FG701 | 973/984；+2.29%/+1.34% | 218.6万/115.5万/-41,191；contango 7.37% | C/context | Night隔离 | Y/Y/N；挤压回吐观察 |
| 焦煤 | JM2701 | 1585/1612.5；-1.77%/-3.47% | 87.37万/48.67万/-38,125；back 1.67% | C/context | Night隔离；无exact外盘 | Y/Y/N；价曲冲突 |
| 红枣 | CJ701 | 7580/7630；-2.43%/-3.05% | 20.17万/22.52万/+3,946；contango 15.38% | CZCE仓单-261、fresh | 制度无Night | chain失败；弱但不追 |
| 豆粕 | M2701 | 3402/3422；+0.68%/+0.59% | 193.71万/273.38万/-51,707；contango 0.82% | C/context | Night隔离；美豆周五显著收低 | Y/Y/N；报告后等45m |
| 玉米 | C2611 | 2255/2260；-0.40%/-1.61% | 46.69万/116.20万/-16,426；轻back 0.22% | C/context | Night隔离；USDA降单产但接近预期 | 局部surface/N；等待中国定价 |
| 棕榈油 | P2701 | 10035/10151；-0.26%/-0.60% | 70.48万/58.33万/-7,195；contango 1.52% | C/context | Night隔离；BMD最后4816 | Y/Y/N；无方向优势 |
| 苯乙烯 | EB2610 | 10036/10303；+0.20%/+6.47% | 170.59万/25.50万/-66,811；contango 0.68% | C/context | Night隔离；上游事件正向 | Y/Y/N；弹性衰减反证 |

周五国际市场最后可验证收盘为Brent 104.61美元/桶、WTI 100.05，分别回落2.81%和2.37%，但全周仍涨逾8%；潜在外交安排和极端供应风险同时存在。[Reuters油市，2026-09-11](https://www.reuters.com/business/energy/oil-prices-set-end-week-over-100-first-time-nearly-4-months-2026-09-11/)

周末新增事实：沙特因无人机袭击关闭绕开霍尔木兹的东西向管道，该管道此前输送约400万—500万桶/日；胡塞同时控制Perim岛，增加曼德海峡航运风险。事件发生在主要期货收市后，方向上支持能源/航运右尾，但没有可验证市场价格确认。[Reuters，2026-09-12](https://www.reuters.com/business/energy/saudis-shut-down-oil-pipeline-houthis-tighten-grip-red-sea-shipping-2026-09-12/)

## 四、相比上一交易日/同日晨报真正变化

1. **Saudi East-West绕行能力成为新增风险点。** 与早报相比，FU催化分+2、EC+2、SC+3；但价格尚未开盘，price/curve/tech分不因新闻自动增加。
2. **EC的催化从泛航运风险升级为具体曼德海峡节点。** Perim岛控制权变化直接影响红海通道；竞争解释是实际商业航线可能已绕行、事件影响未必等同EC合约航线利润。
3. **周五外油回撤与周末供应升级形成冲突。** 周一可能向上补价，也可能在管道快速恢复或外交缓和时回吐；双向gap风险上升，追价赔率继续恶化。
4. **WASDE玉米减产不构成惊喜。** USDA将美国玉米单产降至178.5蒲式耳/英亩、产量下调2.13亿蒲式耳，但结果接近市场预期，周五美国玉米仍收低；C2611只保留单层实体观察。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)｜[Agriculture.com收盘与报告](https://www.agriculture.com/)
5. **CPI确认热通胀但未给贵金属单向答案。** 美国8月CPI环比+0.4%、同比+3.4%，核心环比+0.3%；10年美债收益率一度接近5%，但金银周五反弹，AG/AU空头缺少当日外盘延续。[Reuters CPI，2026-09-11](https://www.reuters.com/world/us/us-consumer-inflation-picks-up-august-2026-09-11/)
6. **19:03采集失败与Night日历异常均属数据问题。** 前者不否定9月11日last-good；后者必须整批隔离，不能因为pipeline标fresh就当作周五夜盘事实。

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：同日晨报75→77，原因是新地缘催化；触发仍移至周一，不假设此前成交。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：73→76，原因是Perim岛与East-West管道提供新增事件证据；参数缺口未修复。
- `COM-E-SC2610-GAP-20260905`：70→73；若此前确已按条件建立，周末无法处置，周一按gap风险先复核而非机械加仓。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：68→67，无新增价格确认，国内back仍为反证。
- `COM-M-C2611-WASDE-CORN-20260912`：58→56，原因是报告接近预期且美国价格未确认；继续研究，不冒充可执行。
- AG2610旧多/旧空不自动迁移至AG2612；换月后的AG2612只保留重新定价观察。

## 五、产业链地图

- **最强风险链：FU—SC—LU—EC，偏多尾部、置信度中高。** 9月11日价格/OI、能源与航运backwardation及外部供应事件构成1/2/4层支持；周末新增事件尚无价格反馈，缺SC/LU实体、exact运价曲线和执行级期权。最强反证是管道可能属短暂停运、外交缓和或需求破坏。
- **炼化下游：FU强于EB/BZ/EG/TA，置信度中。** FU深back与价仓相对更完整；EB虽上周涨6.47%，但当日close仅+0.20%、OI大减且转contango，说明原油headline未等量传导至化工利润。
- **有色—贵金属：偏弱但不追空，置信度中。** CU价格和OI下行支持关税溢价回吐，国内back反对趋势空；热CPI支持高实际利率，但金银周五反弹反对机械延续中国日盘跌势。
- **黑色—新能源：最弱价格链、置信度中低。** JM和LC显著偏弱，但JM仍back、LC当日OI仅小降且实体沿用，不能把单日跌幅解释为供需崩塌。
- **农产品：报告后方向混合、置信度低。** 玉米减产低于旧预测但接近预期；大豆产量小幅上调。中国M/C/P尚未交易报告，周一先看gap、curve和OI，而不是预设跨市场套利。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率凸性/催化/价曲波/仓技 | 总分 | 支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 23/14/20/12/8 | **77** | 1、2、4 | 存在待验证优势｜部分｜休市，周一等30—45m |
| 2 | EC2610航运冲击多 | 23/15/19/11/8 | **76** | 1、2、4 | 存在待验证优势｜部分｜休市，周一日盘触发 |
| 3 | SC2610高位接受多 | 23/10/20/12/8 | **73** | 1、2、3/4 | 存在待验证优势｜部分｜休市，周一等45m |
| 4 | CU2610关税回吐空 | 19/15/14/9/10 | **67** | 1、4 | 存在待验证优势｜部分｜反抽失败才空 |
| 5 | C2611 WASDE玉米减产多 | 16/13/14/5/8 | **56** | 3 | 证据不足｜不足｜等待中国价格确认 |

分项和均已复核。分数只作研究排序，不是胜率、期望收益或仓位指令。FU/SC/LU/EC共享中东供应—运输因子；三者不能按独立风险叠加。C只有一个支持层，严格低于59分。

## 七、前三名交易卡

### FU2611｜条件多｜77

事实：9月11日OHLC 4268/4417/4201/4289，settle 4292，1D +4.66%，ΔOI +4,920，near-next back 8.69%。本期Night无合法记录。周五Brent回落、周末沙特管道停运是相反时点的外部信息。

市场隐含：产品短缺和运输中断已被大幅计价。我们的分歧：若周一SC高开后回吐而FU仍守强，产品端紧张可能比原油headline更耐久；若FU只跟随SC，优势消失。

- 下一窗口：9月14日09:00；09:00首跳不追，等30—45分钟。
- 好成交：4210—4260被接受并重上4295/VWAP，先1/3仓；中成交：突破4418并成功回踩，仓位减半；坏成交：直接高于4450或滑点超过计划1R的20%，放弃。
- 止损：30分钟接受4190下方；逻辑失效：跌破4100、back显著收窄且Brent低于100，或管道恢复且航运风险同步缓解。
- 退出：TP1 4420或1.5R，TP2 4600或3R；1—3D不扩张退出。
- 风险：试仓最大损失0.25%—0.35% NAV；与SC/LU/EC合并。最坏情景为周末headline反转、周一低开及流动性消失。
- 参数：10吨/手，tick 1元/吨，tick value 10元；结算名义42,920元。动态margin/limit未确认；最后交易日2026-10-30，实物交割。期货最大损失不由计划止损限定。
- 压力：一板=`42,920×L`；两板=`42,920×[1-(1-L)^2]`，L须在下单前核验。

### EC2610｜条件多｜76

事实：9月11日OHLC 2015.5/2108/1976/2032，settle 2044，1D +4.18%、5D +10.10%，ΔOI +2,200，near-next back 22.36%；EC制度上无Night。Perim岛事件与油运费率跳升支持航运风险，但EC不是VLCC合约，不能把油轮费率当exact套利。

市场隐含：红海绕行与风险溢价已部分进入EC。分歧：新的曼德海峡节点可能延长绕行时间；竞争解释是EC航线已长期适应绕行、边际利润影响小于油轮市场。

- 下一窗口：9月14日09:00；等30分钟。
- 好成交：1990—2035被接受并重上2045/VWAP；中成交：突破2110后回踩不破，仓位减半；坏成交：直接高于2160，放弃。
- 止损：30分钟接受1970下方；逻辑失效：跌破1962、back显著收窄且通航/管道确认恢复。
- 退出：TP1 2150或1.5R，TP2 2300或3R；1—5D时间止损。
- 风险：0.25%—0.35% NAV，与能源/航运主题合并。最坏情景为周末缓和导致低开、曲线快速塌陷。
- repo未提供EC2610完整multiplier、tick、动态margin/limit和确切最后交易日；参数未确认，故不编一板/两板金额，下单前必须核验INE最新规则。最大损失不受结构限定。

### SC2610｜条件多｜73

事实：9月11日OHLC 815/838.3/786.5/812.9，settle 809.9，1D +5.40%、5D +18.56%，ΔOI +697，back 7.03%。本期Night无合法记录。周末管道停运增加右尾，也显著增加坏成交概率。

市场隐含：霍尔木兹和供应中断已经形成高位backwardation。我们的分歧：若East-West停运持续，亚洲到岸供应风险仍可能未完全进入SC；反证是中国成品油调价低于公式幅度、需求破坏及管道快速恢复。[Reuters中国油价政策](https://www.reuters.com/business/energy/china-limits-fuel-price-increases-third-time-since-iran-war-began-2026-09-11/)

- 下一窗口：9月14日09:00；首跳不追，等45分钟。
- 好成交：790—810承接并重上813/VWAP；中成交：突破838.5后回踩不破，仓位减半；坏成交：直接高于850、接近涨停或止损距离超过1R，放弃。
- 止损：45分钟接受786下方；逻辑失效：跌破768.4、back显著收窄、Brent低于100且管道恢复。
- 退出：TP1 840或1.5R，TP2 875或3R；1—2D不扩张退出。
- 风险：0.20%—0.35% NAV，与FU/LU/EC合并；不因事件新鲜度提高仓位。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；结算名义809,900元。最后交易日9月30日、实物交割，最迟9月18日前复核移仓SC2611。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 交易所自9月14日夜盘起将部分SC/LU合约限幅调至16%、套保保证金17%，并限制SC10月合约日内开仓800手；周一09:00与21:00适用时点须分别核验。[Reuters/交易所风控摘要](https://www.reuters.com/business/energy/shanghai-exchange-adjust-trading-limits-some-oil-futures-contracts-2026-09-11/)
- 以16%压力假设，一板约129,584元/手，两板复合约238,435元/手；计划止损不能限制极端gap损失。

## 八、商品期权专项

最新有效样本为9月11日EOD；周末事件后moneyness、Delta、IV和成本均可能跳变。所有目标结构`execution_ready=false`，因此没有证据证明期权优于裸期货，也不能据IV-RV单独断言便宜或昂贵。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 64.47%/43.35% | +21.11vol | -3.19/-0.62 | Y/Y/N | 事件凸性已贵，周一须重报价 |
| SC2611/10-14 | 60.92%/41.07%代理 | +19.84vol | -1.68/+2.16 | Y/N/N | 与SC2610不同底层，仅context |
| CU2610/09-23 | 15.17%/14.80% | +0.36vol | +0.80/+1.89 | Y/Y/N | IV-RV近零不等于可成交便宜 |
| AG2612/11-24 | 51.14%/35.16% | +15.98vol | +6.33/+8.34 | Y/N/N | 上行尾偏贵，positioning不足 |
| LC2701/12-07 | 43.64%/38.62% | +5.02vol | 未稳定 | Y/N/N | 大跌后需重算Delta |
| FG701/12-11 | 21.93%/18.86% | +3.07vol | +7.89/+3.29 | Y/Y/N | 无bid/ask，不发布成本 |

若周一取得人工实时报价，优先比较FU/SC有限损失call spread与期货止损风险；结构、两腿、Delta、最大净支出和Greeks必须届时报价后确定。本期不发布伪权利金。Dealer Gamma方向未知。统一限制：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、下一实际开盘风险地图

四层时间轴：①9月11日中国EOD；②9月12日Night记录日历无效、整批隔离；③9月11日国际市场最后收盘；④9月12日周末新增地缘事件。今晚没有21:00中国夜盘；下一日盘为9月14日09:00，下一夜盘为9月14日21:00并归属9月15日。

| 品种 | 中国EOD→周五海外→周末事件 | 周一可能gap | 追价/等待 | 最重要确认 |
|---|---|---|---|---|
| FU/LU | 强back→外油回落→绕行管道停运 | 高开尾部、亦可能反转 | 不追；30—45m | FU守4210/4295、产品强于SC、back |
| SC | +5.4%/深back→Brent回落→供应右尾升级 | 宽幅高开概率上升 | 不追；45m | 786/810/813/838.5、Brent、管道状态 |
| EC | +4.18%/back22%→无Night→Perim岛 | headline高开风险 | 不追；30m | 1970/2045/2110、实际绕行、curve |
| EB/BZ/TA/PX | 国内弹性衰减→油回落→上游冲击 | 跟油分化 | 两边不追；45m | settlement、OI、curve、FU/SC breadth |
| CU | 国内弱但back→LME最后弱→无周末定价 | 平/低开后反抽 | 不追空；45m | 108180/109200、LME、back |
| AG/AU | 中国跌→海外金银反弹→热CPI | 平/高开反抽 | 不追空；30—45m | 美元、10Y、换月价差 |
| LC/PT/PD | 急跌、实体不足→无Night | 宽幅双向 | 不接第一刀；45m | OI、curve、仓单有效期、风控参数 |
| FG/JM | 价格与curve冲突→无新外盘 | 震荡/偏弱 | 不追；30—45m | FG963/1010、JM1580、钢材breadth |
| C/M/Y/P/OI | 中国未交易WASDE→美盘报告后收低 | 玉米利多预期已部分消化 | 不预挂裸单；45m | 中国gap、OI、near-next、CBOT周一 |
| AP/JD/SF/SM/SI/PS | 无制度Night、无新增exact映射 | 主要由国内信息决定 | 等30—45m | 量仓、curve、实体更新 |

周一06:00后应先刷新Brent/WTI、管道恢复状态、红海通航及CBOT电子盘，再评估09:00条件。当前假设触发位不是已验证信号。

## 十、未来24小时与7天事件

- 未来24小时：持续核验沙特East-West管道是否只是预防性短停、损伤程度及重启时间；任何恢复消息都会同时压缩FU/SC/EC的事件溢价。[Reuters](https://www.reuters.com/business/energy/saudis-shut-down-oil-pipeline-houthis-tighten-grip-red-sea-shipping-2026-09-12/)
- 9月14日09:00：中国商品日盘重开；周末地缘、CPI和WASDE一次性形成gap，方向单至少延迟30—45分钟。
- 9月14日09:30：中国流通领域生产资料价格常规窗口；9月15日10:00工业、投资、消费、房地产及能源数据窗口，以[国家统计局](https://www.stats.gov.cn/)实际发布为准。
- 9月14日21:00：下一合法中国夜盘，归属9月15日；SC/LU部分合约新限幅、保证金和开仓限制开始适用，下单前核验交易所参数。
- 9月15—16日：FOMC及SEP窗口；按美东9月16日14:00推算，北京时间9月17日02:00公布。CU/AU/AG提前降低Delta/Vega。[美联储日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 9月16日：EIA周度石油数据常规发布窗口；关注成品油库存、炼厂开工、出口和战略库存，以[EIA](https://www.eia.gov/petroleum/supply/weekly/)最终日程为准。
- 未来7天：CFTC COT只作滞后拥挤背景；USDA报告已发布，下一步看天气、出口销售和中国采购兑现。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖、风险与归档核对

强制63个代码全部以9月11日last-good完成价格、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差、跨期、跨品种/跨市场、风格/中性、波动率、偏度和事件凸性扫描；LPG按repo代码PG映射。另纳入PL/BZ/LG/RR/PD/PT/OP/WR等动态品种，统一输入共77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为零价、零量或零OI占位，RS/WR流动性不足，均保留在应覆盖清单而列不适用。
- 黑色建材9/9：FG深contango与JM价格/curve冲突最值得跟踪，未发现三层优势。
- 有色贵金属12/12：CU入榜；AG/AU外盘反弹反对追空。
- 能源炼化化工25/25：FU/SC入榜；EB/BZ/EG/TA/PX的弹性衰减是反证。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺新鲜实体与海外确认。
- 农产品油脂饲料畜牧22/22：C进入低分观察，M/P/Y/OI等待WASDE后的中国定价。
- 航运与软商品全部扫描：EC入榜；CJ虽仓单下降，但深contango及弱价反对多头。
- 期权应覆盖64个、实际59个；CJ/MA/PL/PR/ZC数据不足，0个execution-ready。
- A/B级basis、exact import parity、可靠加工利润及beta-neutral篮子不可得；不发布伪套利。跨期只保留curve研究，不把近—次月价差称现货基差。

风险预算：周末事件后单笔试仓最大损失0.20%—0.35% NAV；只有价格、curve和至少一个非价格层新增确认后，才可提高到0.75%—1.0%。FU/SC/LU/EC按同一主题合并，初始总风险不超过0.75%；压力测试包含16%单板、两板复合、相关性破裂、流动性消失、保证金上调、管道突然恢复、人民币急变与海外大幅反转。

归档：六个固定路径将在main写入后回读验证；CI只作独立事后校验，状态记为`pending_or_unverified`。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；周末无中国21:00夜盘，FU2611、EC2610、SC2610均移至9月14日09:00后30—45分钟验证。  
C. 今晚应继续观察的机会：沙特管道重启状态、FU相对SC强度、EC航运back、CU关税回吐，以及WASDE后C/M/P/Y/OI的周一价格确认。  
D. 今晚必须避免或退出的交易：把无效9月12日Night当行情、周一首跳追FU/SC/EC、把油轮运费当EC exact套利、追空CU/AG/LC，以及在execution-ready=false时臆测期权成本。
