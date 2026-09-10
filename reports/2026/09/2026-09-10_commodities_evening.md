# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-10

prompt_version=radar_2026-09-06_coverage_v1  
实际生成：2026-09-10 19:48 BJT；研究截点：19:30 BJT。最近可验证中国完整EOD为9月9日；9月10日EOD流水线截至截点未发布。今晨已完成Night归属9月10日交易日；今晚21:00尚未发生的Night归属9月11日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；9月10日EOD缺失且20:30美国PPI在即，SC、FU、MA只保留事件后条件观察。**

当前regime：**中东供给冲击推动外油与中国今晨能化跳升，但当日日盘吸收路径不可见；铜的关税预期出现反证；期权仅有落后一日的研究截面，执行报价仍为零。**

最接近触发的三项是SC2610、FU2611、MA610。共同缺口为9月10日EOD close/settle、日盘量仓与曲线、PPI后的海外价格、21:00当前盘口；最早有效复核窗口为21:45。

## 二、数据质量与覆盖

本期实际读取[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并下钻latest、market_state、physical、external、night_session、options quality/surface和contract_meta。根级有效输入仍是9月9日last-good；备用scoped/ex-dce停在8月18日，不能拼接。

- **Futures / Market State：stale但last-good有效。** report_input requested_date=2026-09-09，9月10日06:00生成；latest为9月9日五所802合约、802/802源日期一致、full_market_ready=true、critical errors=0，7个placeholder已剔除。但截至19:30没有9月10日EOD，故本期T日source_date_match_pct不适用，不能计算day follow-through。
- **根状态：failed。** 9月10日05:59的刷新对五所均报设备数限制，data_fresh=false、full_market_ready=false、critical_module_errors=15。它不使9月9日last-good失效，但也不证明9月10日EOD完成。
- **Night Session：partial。** trading_date=2026-09-10，night_session_date=2026-09-09，05:59生成；data_fresh=true、validation_passed=true、published=true，但coverage_complete=false。588个有效具体合约、55个产品；192个合法outside-window、20个no-night-trade、2个query_error和2个unresolved contract；缺报价/时间戳/价格均为0。
- 这批Night是**今天早前已经完成、属于9月10日交易日的连续交易阶段**，绝不是今晚21:00行情。受影响的2个未解析合约不用于候选。
- **Physical：沿用9月9日模块。** 20项中18项按原生频率有效，SC/LU unavailable；所有basis为C级，只作context；GFEX五项仓单沿用9月1日，不是本期新增。
- **External：repo日频沿用。** 17/22有效，全部context_only；19:30海外另用公开实时/准实时来源补充，不构成exact import parity。
- **Options：stale / execution missing。** 最新完整截面为9月9日：22,302合约、375 series、57/64产品；IV覆盖97.98%、OI覆盖68.77%、bid/ask覆盖0；364个series可研究surface、70个可研究positioning、0个execution-ready。AP/CJ/MA/PF/PL/PR/ZC失败。由于9月10日期权截面截至晚间应已可得却未发布，9月9日数据仅作历史背景，不计当日方向证据。
- **Contract Metadata：partial。** 有效合约匹配73.32%；multiplier/tick覆盖35.79%，动态margin/limit约29.8%。未确认参数不猜。

因此本期不是9月10日完整中国商品市场EOD报告，而是“**9月9日有效EOD＋9月10日已完成Night＋19:30海外**”的降级决策更新。读取状态分别为：EOD stale、T日EOD missing、Night partial、Physical ok/carried、External ok/context、Options stale、metadata partial；没有把工具截断或未更新写成源文件为空。

## 三、商品仪表盘

表中EOD均为9月9日last-good，不冒充9月10日；Night为归属9月10日交易日的已完成阶段。Day栏因9月10日EOD缺失统一为missing。volume/OI/ΔOI为9月9日EOD；basis均C级context，Physical无独立方向确认。S/P/E分别为9月9日历史surface/positioning/execution readiness。

| 板块/合约 | 9/9 EOD close/settle；1D/5D | volume / OI / ΔOI；curve | 9/10已完成Night close；vs close/settle；ΔOI | 9/10 Day | 15:00—19:30海外 / Options | 21:00信号 |
|---|---|---|---|---|---|---|
| 原油 **SC2610** | 741.5/722.5；+2.73%/+6.67% | 182,056 / 39,234 / +476；back +5.61% | 773.1；+4.26%/+7.00%；-1,081 | missing | Brent 18:11约102.15；Y/N/N历史 | PPI后等45m |
| 燃料 **FU2611** | 3999/3934；+1.05%/-0.93% | 834,763 / 215,840 / -1,641；back +5.97% | 4119；+3.00%/+4.70%；+11,725 | missing | 外油同向；Y/N/N历史 | 不追首跳 |
| 芳烃 **EB2610** | 9928/9786；+1.26%/+3.81% | 913,840 / 293,492 / +1,541；back +3.22% | 10329；+4.04%/+5.55%；+49,452 | missing | 油价同向；Y/Y/N历史 | 扩散观察 |
| 甲醇 **MA610** | 3411/3402；+3.75%/+7.76% | 3,167,916 / 578,650 / -148,449；back +6.88% | 3494；+2.43%/+2.70%；+55,842 | missing | 油强；9/9 chain失败 | PPI后等45m |
| 乙二醇 **EG2610** | 5849/5804；+0.05%/+1.36% | 1,892,680 / 340,158 / -20,714；back +6.17% | 6020；+2.92%/+3.72%；+22,111 | missing | 成本映射同向；E=false | 看breadth |
| 新材料 **PL611** | 8968/8901；+2.15%/+3.62% | 75,723 / 25,367 / -1,281；back +2.84% | 9261；+3.27%/+4.04%；+1,453 | missing | 无exact映射；9/9 chain失败 | 只观察 |
| 有色 **CU2610** | 111080/111120；+0.78%/+2.78% | 106,322 / 228,584 / -1,353；back +0.32% | 111910；+0.75%/+0.71%；+3,238 | missing | 美国铜关税预期受挫；Y/Y/N历史 | 先查LME |
| 贵金属 **AG2610** | 16224/16141；-0.35%/+2.68% | 392,013 / 197,407 / -1,932；contango -0.17% | 16529；+1.88%/+2.40%；+2,015 | missing | 银16:24约-0.2%；Y/N/N历史 | 等PPI 30m |
| 贵金属 **AU2610** | 952.22/950.14；-0.60%/+1.05% | 202,896 / 149,475 / -1,583；contango -0.14% | 956.04；+0.40%/+0.62%；+846 | missing | 金约4405、+0.1%；Y/N/N历史 | 无优势 |
| 黑色 **J2701** | 2160.5/2164；+0.12%/-2.76% | 41,389 / 64,530 / -2,710；contango -1.14% | 2118；-1.97%/-2.13%；-2,238 | missing | 无exact海外；E=false | 不追空 |
| 黑色 **JM2701** | 1655/1662；+0.73%/-2.41% | 882,283 / 539,172 / -21,070；back +1.08% | 1630；-1.51%/-1.93%；-14,224 | missing | 内部结构冲突 | 等45m |
| 建材 **FG701** | 969/970；+0.31%/+0.52% | 1,051,293 / 1,211,311 / -5,578；contango -5.18% | 956；-1.34%/-1.44%；+4,850 | missing | 无exact外盘；Y/Y/N历史 | 低开不追 |
| 油脂 **P2701** | 10307/10306；-1.10%/+0.43% | 673,123 / 603,175 / -29,048；back +1.25% | 10196；-1.08%/-1.07%；-4,253 | missing | BMD/CBOT当时点未可靠对齐 | 等45m |
| 饲料 **M2701** | 3425/3397；-0.53%/+0.62% | 1,469,587 / 2,812,847 / -2,008；contango -0.36% | 3397；-0.82%/0.00%；-24,958 | missing | 中国新增采购美豆；Y/Y/N历史 | 等价格响应 |
| 铁矿 **I2701** | 738/737.5；-0.34%/+2.86% | 247,689 / 612,127 / +21,534；back +0.20% | 732；-0.81%/-0.75%；+360 | missing | SGX exact时点未确认 | 不追首跌 |

15:00—19:30海外新增信息：截至18:11 BJT，Brent约102.15美元/桶、WTI约97.50，较前一时段分别约+0.93%和+1.51%；这是今晚潜在gap映射，不是中国9月10日日盘已交易的事实。[Reuters油市，2026-09-10](https://www.reuters.com/business/energy/brent-holds-above-100-tanker-attacks-deepen-supply-fear-2026-09-10/) 中国独立炼厂正转买替代原油，现货升水抬升，为原油physical背景增加支持，但不是与SC2610全口径对齐的进口平价。[Reuters炼厂，2026-09-10](https://www.reuters.com/business/energy/china-independent-refiners-scramble-oil-underpinning-spot-premiums-2026-09-10/)

现货金截至16:24 BJT约4405.09美元/盎司、+0.1%，银约67.11、-0.2%；美元偏弱但美国通胀数据尚未发布。[Reuters贵金属，2026-09-10](https://www.reuters.com/world/india/gold-edges-higher-weaker-dollar-us-inflation-data-focus-2026-09-10/) 美元指数仅有方向性小幅反弹、人民币接近多年高位的报道，没有可对齐的19:30 USD/CNH成交，因此人民币不计独立支持层。

## 四、相比上一期真正变化

1. **数据状态由完整EOD降级。** 上一期可用9月9日完整日盘；本期9月10日EOD缺失，任何“今日日盘follow-through/reversal”都无法验证。这是结论收缩的首要原因，不是市场优势消失的证据。
2. **今晨能化形成最强新增信息。** SC、FU、EB、MA相对9月9日close分别+4.26%、+3.00%、+4.04%、+2.43%，外油晚间继续走强；但缺9月10日日盘，无法判断这些涨幅被延续、横盘消化还是反转。
3. **SC/FU的close与settlement双锚同向。** 不存在“仅修复结算价”的假强势；SC Night OI减少、FU/EB/MA增加只是归因线索，不能认定资金身份。
4. **铜多头出现新的竞争解释。** 美国对精炼铜关税决定未落地，削弱此前关税溢价；缺当前LME和中国EOD，CU从76降至66，不反向追空。[Reuters铜关税，2026-09-10](https://www.reuters.com/world/us/white-house-copper-tariff-plan-stalls-amid-affordability-concerns-sources-say-2026-09-10/)
5. **大豆链出现政策/采购催化。** 中国本周采购约100万吨美国大豆，USDA已确认其中34万吨；这是供给来源与政策变量，不等于M/A/Y已经上涨，须等待价格、curve与压榨链响应。[Reuters大豆，2026-09-10](https://www.reuters.com/world/china/china-buys-1-million-tons-us-soybeans-ahead-xi-visit-sources-say-2026-09-10/)
6. **HC、SS、LU期权已挂牌，但首日readiness无法验证。** 9月10日期权文件未更新，不能把挂牌等同surface、positioning或execution就绪。[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html)｜[INE](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)

## 五、产业链地图

- **原油—燃料—芳烃：最强，偏多但不可立即执行，置信度中。** 第1层Night价格/量仓、第2层强back、第4层外油与替代原油升水支持；第3层只有非exact背景，第5层落后一日且不可执行。最大反证是9月10日日盘吸收路径完全缺失，竞争解释是今晨已完成大部分事件定价。
- **MA—EG—PL化工扩散：偏多，置信度中。** Night breadth广、MA/EG曲线back；缺加工利润、库存与当日EOD。MA Night OI回升不能抵消9月9日EOD的大幅减仓线索。
- **铜—铝有色：由偏多转为待核实，置信度中低。** CU Night与轻back支持，但美国关税预期反证增加；无当日LME精确报价、无A级/B级实体映射，不做跨市场套利。
- **焦煤—焦炭—玻璃：边际最弱，偏空观察，置信度中低。** J/JM/FG今晨走弱，FG深contango；但当日日盘缺失使首跌是否延续未知，低开追空赔率差。
- **大豆—粕—油与新能源：催化存在、价格证据不足。** 美豆采购是新增信息；GFEX仓单偏旧、LC/SI/PS无可验证当日日盘，均不进入70分榜。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | **SC2610 PPI后回撤接受多** | 22/13/19/12/9 | **75** | 1、2、4 | 存在待验证优势｜部分｜先补T日EOD，21:45后 |
| 2 | **FU2611 PPI后产品强势多** | 21/14/17/12/9 | **73** | 1、2、4 | 存在待验证优势｜部分｜等待触发 |
| 3 | **EB2610能化扩散多** | 20/14/16/12/9 | **71** | 1、2、4 | 存在待验证优势｜部分｜参数与EOD待补 |
| 4 | **MA610高位接受多** | 20/14/15/12/9 | **70** | 1、2、4 | 存在待验证优势｜部分｜等待触发 |
| 5 | **CU2610关税反证后的双向观察** | 18/17/11/10/10 | **66** | 1、2；4层反对 | 证据不足｜部分｜待LME与T日EOD |

分项均未超上限，总分已复算。数据缺失直接压低赔率、price/curve与技术分，不以叙事补分。SC、FU、EB、MA同属油价—供应冲击因子，不能按四笔独立风险叠加。CU不是正式空头；关税消息只是否定原多头催化的一部分。

## 七、前三名交易卡

以下均为研究卡，不是当前订单。共同前置条件：20:30美国PPI已发布、人工核验9月10日具体合约EOD与curve、21:00后当前报价有效；最早21:45评估。卡内价位来自9月9日EOD与9月10日已完成Night技术锚，不是缺失的9月10日日盘信号。

### 1. SC2610｜条件多｜75

**事实：** 9月9日741.5/722.5；今晨Night 753.5/776.4/752.4/773.1，+4.26% vs close、+7.00% vs settlement，ΔOI -1,081；EOD back +5.61%。18:11 BJT Brent约102.15。  
**市场隐含：** 供应受扰与替代原油升水已有高溢价。  
**分歧与竞争解释：** 若PPI后回撤仍被接受，外油强度可能继续映射；反之今晨或已完成大部分价格发现。选择期货仅因当前期权execution-ready=false，期货最大损失不由结构限定。

- 好成交：先确认T日EOD；21:45后回到760—776承接，重上776.4/当时VWAP，1/3仓。
- 中成交：突破790并成功回踩，仓位为好成交的一半。
- 坏成交：相对人工核验的T日settlement高开超过2%且无回撤，放弃。
- 初始止损：45分钟接受752.4下方。
- 逻辑失效：人工核验T日close低于741.5、near-next back低于3%，且Brent跌回100下方。
- TP1 795或1.5R；TP2 825或3R；1—3日无扩张退出。
- 风险：仅试仓0.25%—0.40% NAV；SC/FU/EB/MA主题合计不超过0.75%，直至EOD和报价补齐。
- 参数：1,000桶/手，tick 0.1元/桶，tick value 100元；以773.1估算名义77.31万元。Night 21:00—02:30；最后交易日2026-09-30，实物交割。动态margin/limit未确认。
- 压力：一板约773,100×L元；两板复合约773,100×[1−(1−L)^2]元。gap、涨跌停和流动性消失可使计划止损失效；9月合约临近交割，未离场则滚动至远月。

### 2. FU2611｜条件多｜73

**事实：** 9月9日3999/3934；今晨Night 4080/4142/4069/4119，+3.00%/+4.70%，ΔOI +11,725；EOD back +5.97%。  
**推断：** 产品端弹性可能强于原油单腿；反证是缺9月10日日盘与油品库存，不能称裂解套利。

- 好成交：补齐T日EOD后，21:45回撤4070—4142承接并重上4145/VWAP，1/3仓。
- 中成交：突破4200回踩成功，减半仓。
- 坏成交：相对T日settlement高开超过2%或深度不足，放弃。
- 止损：45分钟接受4060下方。
- 失效：T日close低于3999、back低于3%且Brent低于100。
- TP1 4250/1.5R；TP2 4400/3R；1—2日时间止损。
- 风险：0.25%—0.35% NAV，与SC/EB/MA合并。
- 参数：10吨/手，tick 1元/吨，tick value 10元；按4119名义约41,190元。Night 21:00—23:00；最后交易日2026-10-30，实物交割；动态margin/limit未确认。
- 压力：一板41,190×L元，两板41,190×[1−(1−L)^2]元。若SC强而FU弱，不将价差后验改称套利。

### 3. MA610｜条件多｜70

**事实：** 9月9日3411/3402，EOD ΔOI -148,449、back +6.88%；今晨Night 3415/3500/3415/3494，+2.43%/+2.70%，ΔOI +55,842。  
**判断：** 价格与curve支持，但EOD大减仓和缺实体是强反证；只交易高位接受，不追价。

- 好成交：21:45后3415—3500区间承接并重上3500，1/3仓。
- 中成交：3520突破回踩，减半仓。
- 坏成交：高于3570无回撤或人工核验T日curve不再back，放弃。
- 止损：45分钟接受3400下方。
- 失效：T日close低于3411、back低于3%，或SC/FU/EB同时转弱。
- TP1 3600/1.5R；TP2 3720/3R；1—2日时间止损。
- 风险0.25%—0.35% NAV，同油价因子合并。
- 参数：10吨/手，tick 1元/吨，tick value 10元；名义约34,940元。margin 7%、limit 6%；Night 21:00—23:00；最后交易日2026-10-21，实物交割。
- 以9月9日settlement 3402计，一板不利约2,041元/手，两板复合约3,959元；T日真实settlement缺失，不能把该数当今晚最新压力值。

## 八、商品期权专项

9月10日截面missing；以下仅为9月9日历史研究背景，本期无新增，标的今晨大幅变化已改变moneyness，不能用作当前成交判断。

| Underlying/expiry | ATM IV / RV20 | IV-RV | RR25/BF25 | S/P/E | 用途 |
|---|---:|---:|---:|---|---|
| SC2610 / 09-11 | 55.15% / 35.74% | +19.41vol | -1.55/-0.84 | Y/N/N | 到期与moneyness均已变化，回避 |
| FU2611 / 10-19 | 54.13% / 39.22% | +14.91vol | -4.41/-2.38 | Y/N/N | 只作历史波动背景 |
| EB2610 / 09-16 | 33.31% / 25.35% | +7.96vol | +3.39/+2.12 | Y/Y/N | 需当前chain复核 |
| CU2610 / 09-23 | 17.37% / 10.61% | +6.75vol | +4.43/+0.13 | Y/Y/N | 关税事件后不可沿用 |
| AG2610 / 09-23 | 43.26% / 30.11% | +13.15vol | +6.41/+2.45 | Y/N/N | PPI/CPI前仅观察 |
| AU2610 / 09-23 | 25.72% / 21.36% | +4.36vol | +3.58/+1.47 | Y/N/N | 无当前执行报价 |

历史IV-RV为正不能单独证明期权昂贵；HC/SS/LU首日chain也未被9月10日文件验证。Dealer Gamma方向未知。没有bid/ask、净权利金、滑点和当前Greeks，任何call spread、put spread或vol RV都只是待报价结构；当前没有证据表明期权优于裸期货。

## 九、21:00夜盘开盘风险地图

四层时间边界：①9月9日为最近有效中国完整EOD；②归属9月10日的今晨Night已完成；③15:00—19:30海外油价继续上涨、铜关税预期转弱、金银等待PPI；④今晚21:00尚未发生，归属9月11日交易日。由于9月10日EOD缺失，下表不给伪精确gap方向；20:30 PPI后的重新定价优先于19:30静态映射。

| 品种 | 可能开盘 / 冲突 | 首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|
| SC | 高波动；外油强、T日中国EOD未知 | 不追 | 45m | 手工T close/settle、776.4、Brent 100/102、back |
| FU/EB | 偏高风险；今晨强、日盘路径缺失 | 不追 | 45m | 产品端是否继续强于SC、OI、curve |
| MA/EG/PL | 偏高但易回吐；成本支持、实体缺失 | 不追 | 45m | MA 3415/3500、链内breadth、back |
| CU/AL | 双向；Night强、铜关税催化受挫 | 不追 | 45m | 实时LME、T日close、curve |
| AU/AG | PPI敏感；金银分化 | 不追 | 30m | DXY、美债实际利率、AU 950/956、AG 16141/16529 |
| J/JM/FG | 低开风险；今晨弱、日盘未知 | 不追空 | 45m | FG 956/970、J 2118、contango与量仓 |
| P/Y/OI/M/A | 双向；美豆采购与此前弱价格冲突 | 不追 | 45m | CBOT/BMD、M 3397/3425、curve |
| RU/NR/BR | 方向不足；海外胶exact数据缺 | 不追 | 45m | 三胶breadth、curve、当前报价 |
| LC/SI/PS/SF/SM/JD | 制度上无对应夜盘 | 不适用 | 9月11日09:00 | T日EOD补档、实体与量仓 |

若21:45仍拿不到9月10日EOD与当前具体合约报价，所有条件单自动失效，下一有效窗口为9月11日09:00后15—45分钟，而不是继续沿用本报告价位。

## 十、未来24小时 / 7日事件

- **9月10日20:30：美国8月PPI。** 所有能源、有色、贵金属条件单延迟至发布后至少45分钟；无报价期权不以Vega替代Delta管理。[BLS PPI日程](https://www.bls.gov/schedule/news_release/ppi.htm)
- **9月11日00:00：EIA周度石油数据（劳动节顺延）。** SC/FU/EB/MA同因子风险合并，事件前不把试仓升为确认仓。[EIA发布日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月11日约16:00：IEA Oil Market Report。** 检查霍尔木兹流量、需求与替代供应，油价多头用分批退出处理。[IEA OMR](https://www.iea.org/reports/oil-market-report)
- **9月11日20:30：美国8月CPI。** AU/AG、CU/AL及油价再度面临美元—实际利率重置；优先有限凸性，但只有在取得可执行期权报价后。[BLS CPI](https://www.bls.gov/cpi/)
- **9月12日00:00：USDA WASDE。** A/B/M/Y/P/OI/C/CF避免无保护方向重仓；中国美豆采购是催化，不是WASDE结论。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **9月12日约03:30：CFTC COT。** 仅作滞后拥挤背景，不能把会员或管理基金排名当实时方向。
- **未来7日持续：** 霍尔木兹通行、油轮安全、中国独立炼厂替代采购及美国铜政策。headline改变收益分布，不自动提供入场价。

## 十一、覆盖核对、旧建议台账与风险

**覆盖核对：** 应覆盖63个强制代码及14个动态代码，共77个扫描槽位。9月9日last-good中71个流动性合格品种完成1D/3D/5D/20D、价格/量仓、curve、方向、跨期、基差、跨品种/跨市场、风格/中性、波动率、偏度和事件凸性扫描；JR/PM/RI/RS/WH/ZC因零价、零成交/持仓或制度性低活跃列为不适用。对9月10日日盘，77个槽位均因T日EOD未发布而列为“数据不足”，没有把提到品种名称当成完成当日分析。

- 黑色建材9个强制品种均有last-good；J/JM/FG今晨偏弱是未入榜最大异常，T日EOD不足。
- 有色贵金属12个均有last-good；CU政策反证最重要，AU/AG等待PPI，T日LME/国内EOD不足。
- 能源炼化化工25个均有last-good；SC/FU/EB/MA/EG/PL今晨breadth最强，SC/LU Physical缺失。
- 新能源及GFEX新材料完成last-good扫描；GFEX仓单沿用9月1日，LC/SI/PS无夜盘且T日EOD缺失。
- 农产品油脂畜牧完成last-good扫描；P/M弱与美豆采购催化冲突，CBOT/BMD exact时点与T日国内反应不足。
- 航运与软商品完成last-good扫描；无exact海外映射与三层共振。
- 期权应覆盖64个产品：9月9日实际57个历史可研究、7个失败；9月10日当前截面全部缺失，0个可执行。
- A/B级basis、exact import parity、加工利润、完整仓单、beta-neutral校准和当前期权报价均不足，因此不发布伪套利。IC及代理期权边界不属于本商品版强制资产范围，未以股指代理冒充商品证据。

**旧建议处置：**

- COM-E-SC2610-GAP-20260905：79降至75；今晨强、外油仍支持，但9月10日EOD缺失。晨报触发路径unknown，不假设成交；若此前确已按条件建立，PPI前只按原风险纪律管理。
- COM-E-FU2611-PRODUCT-TIGHT-20260908：78降至73；今晨价格与OI支持，日盘路径unknown。
- COM-E-EB2610-DAY-REVERSAL-20260909：75降至71；保留扩散研究，metadata与T日EOD缺口扩大。
- COM-M-MA610-SETTLE-RECLAIM-20260908：保留70；Night强但9月9日EOD减仓与实体缺口反对。
- COM-M-CU2610-LME-RECORD-20260909：76降至66；原因是铜关税催化变化与T日数据缺失，不反向建立空头。
- COM-M-AG2610-PPI-BREAKOUT-20260910：移出前五；PPI未发布且当前surface/报价缺失。
- COM-E-AP701-MOMENTUM-20260909：暂停；无夜盘、9月10日EOD和当日期权均不可验证。

风险预算：只有在补齐T日EOD、当前报价并越过PPI窗口后，单笔试仓最大损失0.25%—0.40% NAV；确认交易暂不超过0.75%。油价—供应主题总风险不超过0.75%，低于常规2.5%—3.0%上限。压力测试覆盖1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变与中国休市时海外大波动。

归档结果：六条固定路径已从main回读验证，manifest中2026-09-10 + commodities_evening恰好一条；archive_status=success，ci_validation_status=pending_or_unverified。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：不在20:30美国PPI前挂单；仅在人工核验9月10日EOD后，SC2610、FU2611、MA610于21:45后满足卡片回撤接受条件再试仓。  
C. 今晚应继续观察的机会：EB2610与EG/PL能化扩散、CU关税预期回撤后的LME确认、A/B/M对中国美豆采购的价格反应，以及HC/SS/LU期权次日流动性。  
D. 今晚必须避免或退出的交易：把9月9日EOD冒充9月10日、把今晨Night冒充今晚行情、PPI前追能化、无T日EOD反手铜，以及在execution-ready=false时臆测期权成本。