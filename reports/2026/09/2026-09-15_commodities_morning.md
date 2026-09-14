# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-15

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:11 BJT；信息截点：07:00；最近完整中国EOD：9月14日；当前交易日：9月15日；下一可交易窗口：09:00日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；FU/LU夜盘继续扩张而SC相对前收仅微涨，产品强于原油是最值得冒险的条件机会，但09:00仍须等待确认。**

当前regime：**中东供给冲击仍在、原油headline弹性下降、燃料油与聚酯成本链接力、美元与美债收益率压制金属、内需链偏弱。**

最接近触发的是FU2611、LU2611、SC2611。分别缺少09:00后产品端强势接受、LU实体与期权确认、以及SC高位抛压被重新吸收。

## 二、数据质量与覆盖

优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)及[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按重点候选读取[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-14`，9月15日06:13:27生成。
- Futures：9月14日EOD，五所802个合约、77个产品；`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0、excluded exchanges=0。7条OHLC占位记录已排除；同合约20日历史完整。
- Market State：1D/3D/5D/20D、RV20、量仓及curve均截止9月14日；主力换月标记保留，不拼接收益。
- Physical：20项目标中18项按原生频率fresh、2项unavailable（SC/LU），0 stale、0本模块carried-forward；5条仓单由核心状态标为沿用。basis均为C级或不可用，只作context。
- External：repo日频层9月14日17/22 fresh、5项unavailable，全部`context_only`。repo的Brent/WTI代理收盘106.39/101.86美元/桶；Reuters可核实主力结算105.68/101.39，时点/合约口径不同，均不作为exact套利。
- Options：9月14日18,862条、340个series，52/64产品成功；330个surface-ready、80个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖97.72%/69.44%/0。INE的BC/SC与SHFE的AD/AG/AL/AO/AU/CU/NI/PB/SN/ZN共12个产品失败。
- Metadata：partial；有效合约匹配73.32%，multiplier/tick/margin/limit覆盖约29.80%。SC/FU/LU的最后交易日可核验，但动态margin/limit仍须下单前确认。

Night质量闸门：`trading_date=2026-09-15`、`night_session_date=2026-09-14`，9月15日06:01:19生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。请求802个合约，579个有效Night合约、55个产品；216个outside-window、7个no-night-trade；missing timestamp/price/quote、query error、unresolved均为0，warnings为空。72.19%是有夜盘记录占比，不是完整率。

该Night属于今天已经完成的连续交易阶段。逐产品紧凑层可用；`data/night_session/latest.json`原始大文件经connector回读仅返回空payload而状态明确有579条，故标为工具侧`truncated/empty payload`，不写成源文件为空。近次月两腿无法同时核验，Top 3不强拼Night curve；`night_session_fallback_used=false`。

## 三、商品仪表盘

1D/5D为9月14日同一具体合约结算收益；Night均为归属9月15日交易日的已完成session。S/P/E为surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical | Night close；vs close/vs settle；ΔOI | 07:00海外/期权；09:00信号 |
|---|---|---|---|---|---|
| 燃料油FU | FU2611；4392/4365；+1.70%/+14.90% | 126.39万/21.94万/-1,489；back 12.39%、z2.13 | C/context | 4541；+3.39%/+4.03%；+11,454，23:00 fresh | Brent结算105.68；Y/N/N；等30m承接 |
| 低硫LU | LU2611；5515/5504；+0.31%/+10.79% | 16.47万/7.15万/-5,291；back 2.73% | 缺失 | 5701；+3.37%/+3.58%；+2,463，23:00 fresh | 油品现货偏紧；期权缺；等30m |
| 原油SC | SC2611；815.2/776.5；+2.62%/+19.74% | 15.28万/3.86万/+6,460；SC2610-11 back 8.83%、z2.07 | 缺失 | 821.5；+0.77%/+5.80%；-998，02:30 fresh | WTI结算101.39；期权失败；不追第一跳 |
| 集运EC | EC2610；2090.5/2114；+3.42%/+11.15% | 2.32万/2.65万/+524；back 20.13% | exact运价缺 | 制度无Night | 航运事件未转化为exact运价；N/N/N；等30m |
| PTA | TA701；6352/6396；+1.33%/+8.00% | 225.64万/117.75万/+38,898；curve因roll仅1观测 | C/context | 6516；+2.58%/+1.88%；+16,071，23:00 fresh | 成本映射；Y/Y/N；追价优势有限 |
| PX | PX611；9366/9406；+0.47%/+8.51% | ΔOI +2,408；curve仅1观测 | C/context | 9632；+2.84%/+2.40%；+10,592，23:00 fresh | Y/N/N；等45m看TA/PX同步 |
| 苯乙烯EB | EB2610；10094/10138；-1.60%/+5.64% | 111.41万/23.59万/-19,107；contango 0.94% | C/context | 10305；+2.09%/+1.65%；-2,914，23:00 fresh | Y/Y/N；价格反弹但量仓反对 |
| 玻璃FG | FG701；927/944；-4.07%/-3.48% | 190.58万/121.82万/+63,156；curve仅1观测 | C/context | 926；-0.11%/-1.91%；+13,229，23:00 fresh | Y/Y/N；相对前收不再扩跌 |
| 纯碱SA | SA701；1019/1037；-3.89%/-4.95% | ΔOI +21,427；curve仅1观测 | C/context | 1021；+0.20%/-1.54%；+8,204，23:00 fresh | Y/Y/N；结算锚夸大新弱势 |
| 铜CU | CU2610；107840/108190；-0.43%/-0.93% | 11.44万/18.78万/-11,069；back 0.60%、z1.43 | C/context | 106920；-0.85%/-1.17%；-3,283，01:00 fresh | LME铜14023、DXY99.41；期权失败；反抽失败才空 |
| 黄金AU | AU2612；937.6/946.54；+0.21%/-1.04% | 9.88万/16.51万/+6,710；轻back/roll限制 | C/context | 代表合约AU2610 933.98；-0.10%/-1.10%；+302 | 金4312.59、10Y约5%；期权失败；不追空 |
| 白银AG | AG2612；15528/15752；+0.48%/-1.85% | 14.36万/19.97万/+6,322；轻contango | C/context | 代表合约AG2610 15559；+0.42%/-1.01%；-594 | 银-1.2%；期权失败；换月不可硬分解 |
| 玉米C | C2611；2221/2236；-1.06%/-2.32% | 76.30万/114.52万/-16,737；curve仅1观测 | C/context | 2213；-0.36%/-1.03%；-7,735，23:00 fresh | CBOT 534.75；Y/Y/N；WASDE多头未获确认 |
| 豆粕M | M2701；3361/3384；-1.11%/-0.59% | 170.67万/267.79万/-55,842；curve仅1观测 | C/context | 3381；+0.60%/-0.09%；-8,428，23:00 fresh | CBOT豆1304.5；Y/Y/N；反弹非趋势确认 |
| 碳酸锂LC | LC2701；132340/133560；-0.30%/-5.66% | 12.26万/41.16万/+3,985；curve近零、roll | 仓单沿用 | 制度无Night | Y/N/N；不接第一刀也不追空 |

海外最新完成时段：Brent/WTI周一一度接近+5%，最终只结算+1.0%/+1.3%至105.68/101.39，表明headline上冲遭到兑现；亚洲实货Dubai/Oman溢价与炼厂利润仍偏强，支持产品链而非无限追原油。[Reuters油市，2026-09-14](https://www.reuters.com/business/energy/oil-prices-jump-more-than-3-after-new-strikes-saudi-strait-hormuz-2026-09-13/)｜[Reuters亚洲实货，2026-09-14](https://www.reuters.com/business/energy/asias-oil-traders-seeing-no-quick-end-middle-east-war-stay-bullish-prices-2026-09-14/)

美元指数周一约+0.3%至99.41，美国10年期收益率一度突破5%；现货黄金跌0.8%至4312.59美元/盎司、白银跌1.2%。这反对把AU/AG夜盘相对结算跌幅简单解释为信用避险失效，但也不足以建立裸空。[Reuters美元](https://www.reuters.com/world/asia-pacific/dollar-steady-yen-near-7-month-high-ahead-fed-boj-meetings-2026-09-14/)｜[Reuters美债](https://www.reuters.com/business/us-10-year-yields-reach-5-highest-since-2023-2026-09-14/)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-slips-oil-rally-fans-rate-hike-bets-ahead-fed-meeting-2026-09-14/)

## 四、相比上一交易日/今晨真正变化

1. **FU由次席升为第一。** EOD虽价涨仓减，但Night相对前收+3.39%、ΔOI +11,454，价格—持仓层得到新增确认；评分76→84。
2. **SC从82降至77。** Night相对前收仅+0.77%，却相对结算+5.80%，且夜高865.5、收821.5、ΔOI -998；说明大部分“涨幅”来自日盘close与settle的旧偏离，新增信息弹性显著下降。
3. **LU成为新Top候选。** Night相对前收+3.37%、ΔOI +2,463，明显强于SC；但SC/LU实体均缺、LU期权链缺，因此只列条件机会。
4. **聚酯成本链扩散。** PX/TA Night分别+2.84%/+2.58%，ΔOI同向增加；EB/BZ也涨约2%但持仓下降，表明成本传导存在、下游接受仍不完整。
5. **FG/SA的空头弹性衰减。** 相对前收分别-0.11%/+0.20%，而相对结算仍-1.91%/-1.54%；晚报FG弱势空不再入榜，旧条件撤销。
6. **海外从盘中急涨转为结算仅小涨。** 这支持供应风险存在，也反对09:00机械追SC；美元与10Y上行继续压制有色贵金属。

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：76→84；昨晚4310—4380好成交区未触及，突破4525后的分钟级回踩无法核验，触发状态未知；无成交反馈，不假设持仓。新触发因价格变化上移。
- `COM-M-LU2611-PRODUCT-RELATIVE-20260915`：首次提出；等待09:00确认，非已建立模拟仓。
- `COM-E-SC2610-GAP-20260905`：82→77并滚动至SC2611；昨晚795—810区间未触及，直接开830、盘中高于旧TP1不代表收益兑现；旧条件过期，重新报价。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：维持71；制度无Night，今日09:00首次验证。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：维持68；Night续弱但OI下降、国内back仍反对趋势空。
- `COM-E-FG701-WEAK-CONT-20260914`：59→撤出正式榜；Night相对前收未继续走弱，等待实体与可比curve，不反向做多。

## 五、产业链地图

- **最强：FU—LU产品链，偏多，置信度高于SC。** EOD back、Night价格和ΔOI、亚洲实货溢价共同支持1/2/4层；最大缺失是Singapore HSFO/VLSFO exact价差、SC/LU实体和当前执行报价。
- **原油SC：方向仍偏多、追价价值下降，置信度中高。** EOD涨仓增与近端back支持，但Night相对前收弹性弱、盘中高位回落及ΔOI下降反对继续追。Night curve因次月腿未能同时核验，缺确认。
- **PX—TA—EB聚酯芳烃：成本推动偏多，置信度中。** PX/TA夜盘价仓同向，EB价格跟随但仓减、EOD contango；更像成本冲击而非需求闭环。实体仅context，期权凸性已不便宜。
- **最弱：FG—SA—内需黑色，置信度中。** EOD价跌仓增，但Night相对前收不再扩跌；单日弱价未获可比curve与实体确认，不适合追空。
- **有色贵金属：美元/利率压制，置信度中低。** CU夜盘续弱但减仓、国内back仍在；AU/AG受5%美债收益率与地缘避险拉扯，黄金信用主题未形成可交易闭环。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 24/18/20/14/8 | **84** | 1、2、4 | 存在待验证优势｜充分但期权反对追凸性｜等待09:30 |
| 2 | LU2611产品相对强势多 | 23/16/19/12/8 | **78** | 1、2、4 | 存在待验证优势｜部分｜等待09:30/参数 |
| 3 | SC2611高位再接受多 | 24/10/20/14/9 | **77** | 1、2、4 | 存在待验证优势｜部分且弹性衰减｜等待09:45 |
| 4 | EC2610航运冲击多 | 22/13/18/10/8 | **71** | 1、2、4 | 存在待验证优势｜部分｜无Night；等待09:30/参数 |
| 5 | CU2610关税/美元回吐空 | 19/16/14/9/10 | **68** | 1、4 | 存在待验证优势｜部分｜反抽失败才考虑 |

分项均已复算且未超上限。CU只有两层，严格封顶69。FU/SC/LU/EC共享供应—运输因子，不能四笔独立叠加；所有期货最大损失均不由计划止损限定。TA/PX为69以下研究观察，因可比curve、Physical与执行报价不足未替代既有台账。

## 七、前三名交易卡

### 1. FU2611｜条件多｜84

**事实：** previous close/settlement=4392/4365；Night OHLC=4450/4549/4445/4541，vs close +3.39%、vs settlement +4.03%，Night ΔOI +11,454。EOD back 12.39%、z2.13。**市场定价：** 产品短缺已获得二次定价。**分歧：** 亚洲实货紧张可能比原油headline更持久；最强反证是Brent盘中涨幅已大幅回吐、FU期权IV极贵。

- 价格弹性：强，双锚差仅0.64个百分点；但夜盘已完成较多价格发现，09:00不追第一跳。
- 最佳表达：FU2611单腿条件多，1手为一风险单位；未定义可靠beta/dollar-neutral对冲，不构造伪篮子。
- 好成交：09:30后4445—4510获得接受，并重上4545/VWAP，先1/3仓。
- 中成交：突破4550后回踩4525—4550不破，仓位减半。
- 坏成交：直接高于4620、滑点超过计划1R的20%或盘口显著变薄，放弃。
- 止损：30分钟接受4435下方；逻辑失效：跌破4392、back低于10%、Brent低于103或产品相对SC转弱。
- 退出：TP1 4630或+1.5R；TP2 4770或+3R；1—3D无扩张退出。旧TP1 4520已在未确认触发的Night中越过，不能继续当当前目标。
- 风险：试仓0.20%—0.35% NAV；同SC/LU/EC合并初始≤0.60%。最坏情景是通航恢复、原油跳水、产品裂解压缩、跌停和流动性消失。
- 参数：10吨/手、tick 1元/吨、tick value 10元为合约常规参数；repo仅确认最后交易日10月30日、最后交割日11月3日，动态margin/limit未确认。按Night close名义45,410元；一板=`45,410×L`，两板=`45,410×[1-(1-L)^2]`，L下单前核验。10月中旬前移仓，实物交割。

### 2. LU2611｜条件多｜78

**事实：** previous close/settlement=5515/5504；Night OHLC=5555/5748/5555/5701，vs close +3.37%、vs settlement +3.58%，Night ΔOI +2,463。EOD仅+0.31%、back 2.73%，EOD ΔOI -5,291。**市场定价：** 夜盘开始补产品稀缺溢价。**分歧：** LU可能由EOD落后者转为补涨；竞争解释是成本beta和短期回补，并无实体闭环。

- 价格弹性：强，双锚接近；但从夜开至夜收已上涨，09:00等30分钟。
- 最佳表达：LU2611单腿条件多。FU/LU相对价值只作主题观察，因无可靠吨值/波动率中性配比，不发布两腿交易。
- 好成交：09:30后5620—5680获得接受并重上5705/VWAP，先1/3仓。
- 中成交：突破5750并回踩5720—5750不破，仓位减半。
- 坏成交：直接高于5820或买卖深度不足，放弃。
- 止损：30分钟接受5550下方；失效：跌破5515、back低于1.5%、Brent低于103或LU重新显著弱于FU/SC。
- 退出：TP1 5800或+1.5R；TP2 5950或+3R；1—3D无扩张退出。
- 风险：0.20%—0.30% NAV，并入能源航运主题。最坏情景为原油回吐、产品裂解崩塌、保证金上调与跌停。
- 参数：repo确认最后交易日10月30日、最后交割日11月6日；multiplier、tick、margin、limit及夜盘制度字段在元数据中为空，参数未确认，不给伪精确名义与一板/两板金额；实物交割，10月中旬前移仓。

### 3. SC2611｜条件多、禁止追价｜77

**事实：** previous close/settlement=815.2/776.5；Night OHLC=830/865.5/817.7/821.5，vs close +0.77%、vs settlement +5.80%，Night ΔOI -998。EOD ΔOI +6,460，SC2610-11 back 8.83%。**市场定价：** 供应中断与近端挤压高度显性。**分歧：** 方向未反转，但新增信息弹性远低于结算锚显示；竞争解释是上冲兑现和仓位拥挤。

- 价格弹性：弱。5.02个百分点双锚差说明“相对结算大涨”主要是旧日盘偏离；夜高到夜收回撤5.08%，但无分钟路径，不写成确定抛盘身份。
- 最佳表达：SC2611单腿条件多；SC期权9月14日链失败，不以旧SC2611期权面或其他月份替代。
- 好成交：09:45后815—825获得接受并重上830/VWAP，先1/3仓。
- 中成交：先回撤后重上845并回踩不破，仓位减半。
- 坏成交：直接高于850、接近涨停、或止损距离超过1R，放弃。
- 止损：45分钟接受810下方；失效：跌破800、back低于6.5%、Brent低于103且管道/通航恢复。
- 退出：TP1 850或+1.5R；TP2 875或+3R；1—2D无扩张退出。Night高865.5不代表旧建议已获利，因为昨晚条件并无可核实成交。
- 风险：0.15%—0.25% NAV，低于FU/LU；同因子初始合计≤0.60%。最坏情景为外交突破、管道恢复、外油急跌、16%跌停和流动性消失。
- 参数：1,000桶/手、tick 0.1元/桶、tick value 100元；Night close名义821,500元。repo确认最后交易日10月30日、最后交割日11月6日，实物交割；10月中旬前移仓。[INE合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 动态margin未确认；按需复核的16%压力假设，一板约131,440元/手，两板复合约241,850元/手。该压力不是已确认当日参数。

## 八、商品期权专项

最新有效截面为9月14日EOD；这是截至07:00最新应得完整截面，但Night使能源与聚酯底层moneyness、Delta和当前成本改变。所有目标结构`execution_ready=false`。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 76.81%/43.15% | +33.66vol | -4.48/+1.20 | Y/N/N | 事件凸性极贵，Night后须重报价 |
| SC | 9月14日产品失败 | N/A | N/A | N/N/N | 不使用旧面或他月代理 |
| LU2611 | 无可核实series | N/A | N/A | N/N/N | 期权表达不可评 |
| TA701/12-11 | 35.97%/26.32% | +9.65vol | +2.99/+0.66 | Y/Y/N | 上行偏度已贵，不裸追call |
| PX611/09-28 | 41.32%/31.26% | +10.06vol | +2.88/+0.79 | Y/N/N | 到期近、Night后Delta待重算 |
| FG701/12-11 | 22.34%/24.10% | -1.76vol | +6.49/+2.39 | Y/Y/N | IV<RV不单独证明错价 |
| M2701/12-16 | 15.08%/11.00% | +4.07vol | +4.02/+0.55 | Y/Y/N | Night反弹不足以支持call |
| LC2701/12-07 | 44.58%/38.52% | +6.06vol | +0.70/+1.83 | Y/N/N | 无Night且实体不足 |

期权并未显示优于裸期货的可执行证据。FU若取得09:00实时双边报价，只比较等量牛市call spread与线性仓的净支出/盈亏平衡；当前不发布执行价、权利金、Greeks、滑点或最大净支出。禁止裸卖event vol；Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月14日；②Current Trading Day Night=归属9月15日、已完成；③07:00 Overseas=9月14日国际结算与9月15日开盘前可核实事件。

| 品种 | EOD→Night→海外 | 09:00判断 | 是否已定价/等待 | 核心确认 |
|---|---|---|---|---|
| FU | EOD+1.70%/深back→Night+3.39%/仓增→外油结算仅+1% | 偏高开后震荡 | 大部分已夜盘定价；30m | 4445/4510/4545、back、产品强于SC |
| LU | EOD+0.31%→Night+3.37%/仓增→实货溢价强 | 偏高 | 夜盘补价明显；30m | 5555/5680/5705、相对FU/SC |
| SC | EOD close远高settle→Night仅+0.77%且高位回落→WTI+1.3% | 平/高开双向 | 结算锚夸大新增；45m | 815/825/830、Brent103、curve |
| EC | EOD+3.42%/back20%→无Night→航运事件持续 | 双向headline gap | 尚未用中国盘验证；30m | 2035/2090/2115、exact集装箱运价 |
| PX/TA | EOD温和涨→Night+2.8%/+2.6%、仓增→油价高位 | 偏高 | 已部分定价；45m | 两者同步、EB跟随、curve breadth |
| EB/BZ | EOD弱→Night约+2%但仓减→成本上行 | 高开后分化 | 价格有、持仓弱；45m | 10305/contango、下游接受 |
| CU/ZN/AL | EOD弱→Night继续弱→DXY及美债强 | 偏低 | 大部分已定价；30—45m | CU106650/107020、LME、back、CNH |
| AU/AG | EOD混合→代表合约双锚分歧→金银外盘跌 | 偏低/波动 | 合约不完全对齐；45m | exact主力、DXY、10Y、换月价差 |
| FG/SA | EOD急跌→Night相对前收近零→无exact外盘 | 平开/反抽风险 | 旧弱势已大量定价；30m | FG923/932、SA1014/1027、OI |
| C/M/P | EOD偏弱→Night分化→CBOT/BMD日频更新 | 平/分化 | 无独立跨市场套利 | 量仓、near-next、进口口径 |
| LC/PT/PD | EOD弱、无Night→实体/海外不足 | 双向 | 未获新增确认；45m | OI、curve、仓单有效期、风控 |

人民币：公开USD/CNH约6.71、变动很小；美元指数与美债收益率上行压制金属，但人民币并未给出足以量化的额外进口成本冲击。repo明确USDCNH不可用，不编精确贡献率。[Reuters人民币对冲背景](https://www.reuters.com/business/finance/china-urges-more-fx-hedging-strong-yuan-hits-exporters-sources-say-2026-09-14/)

## 十、未来24小时与7天事件

- 9月15日09:00：中国商品日盘；FU/LU/SC至少等待30/30/45分钟。10:00附近中国工业、投资、消费、房地产与能源生产数据，内需链在公布前减少Delta。
- 9月15—16日美国时间FOMC，决议约9月17日02:00 BJT；市场高度押注加息，CU/AU/AG避免裸Vega与隔夜高Delta。[美联储日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 9月16日22:30附近EIA周报；FU/SC/LU检查原油、成品油库存、炼厂开工与出口，优先有限凸性或事件前降仓。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- 未来24小时持续核验East-West管道重启、Hormuz/Perim通航及阿曼会谈重排；恢复会同时压缩FU/LU/SC/EC的共享因子。
- 未来7日：IEA/OPEC+任何临时供应协调、交易所保证金/限幅调整与SC/FU/LU交割月风险；以正式公告为准。
- 农产品：WASDE已公布，转向美国天气、出口销售、中国采购与高燃料运输成本；CFTC仅作滞后拥挤背景，不等同中国会员方向。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)｜[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖、风险与归档核对

强制63个代码及动态新增品种均进入覆盖核对；对可得数据完成9月14日EOD价格、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差/跨期、跨品种/跨市场、加工链、风格/中性、波动率、偏度和事件凸性扫描；统一输入共77个产品。

- 应覆盖：63个强制代码+动态合格品种；实际取数并有效分析70个。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；均保留扫描状态。
- 黑色建材9/9：FG/SA双锚分歧最异常，Night否定追空；I的SGX映射仅context。
- 有色贵金属12/12：CU入榜；ZN/AL弱但合约代表不完全对齐；AU/AG宏观与避险冲突。
- 能源炼化化工25/25：FU/LU/SC/EC入榜；PX/TA Night扩张，EB/BZ仓减反对需求闭环。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺新增实体与exact海外映射。
- 农产品油脂饲料畜牧22/22：C/M Night不足以确认WASDE多头；P小幅反弹，油脂无三层优势。
- 航运与软商品全部扫描：EC待09:00；CF/CY夜弱但无实体闭环，CJ无Night并深contango。
- Night应得且有效55个产品/579个合约；216个制度外、7个无成交不视为错误。原始大文件读取为工具侧truncated，故Night curve逐腿不足。
- 期权应覆盖64、实际52、12个产品失败、0个execution-ready；A/B级basis、exact import parity、可靠加工利润与beta-neutral篮子不足，不发布伪套利。

风险预算：单笔试仓0.15%—0.35% NAV；新增价格、curve及非价格层确认后才提高至0.75%—1.0%。FU/LU/SC/EC初始合并风险≤0.60%，确认后同主题≤2.5%。压力测试包括16%一板、两板复合、相关性破裂、管道突然恢复、夜盘gap、保证金上调、流动性消失、IV跳升/塌陷、交割挤压与人民币急变。

六个固定路径已从main回读验证：历史MD/JSON存在，latest日期与edition正确，status对应本期，manifest中`2026-09-15 + commodities_morning`恰好一条；[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-15_commodities_morning.md)。`archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：FU2611在09:30后4445—4510承接并重上4545，或LU2611在5620—5680承接并重上5705；SC2611仅09:45后815—825承接并重上830，三者同主题初始风险合计≤0.60%。  
C. 今天应继续观察的机会：EC2610在09:30后的集装箱运价映射、PX/TA成本扩散、CU反抽失败、FG/SA弱势弹性衰减，以及能源期权09:00后的实时报价。  
D. 今天必须避免或退出的交易：把SC相对结算+5.80%写成隔夜新增强势、09:00追FU/LU/SC首跳、把油轮或外油代理当exact套利、追空FG/SA/AU/AG，以及在execution-ready=false时臆测期权成本。
