# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-09

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成/研究截点：2026-09-09 19:40 BJT；最近完整中国时段：9月9日日盘；今晚21:00夜盘尚未发生，归属9月10日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；SC、FU、EB获日盘与海外油价确认，但首跳赔率不足，只等回撤接受。**

当前regime：**中东供给冲击与输入性通胀共振、原油及芳烃日盘重定价、炼化强于内需、金属高位消化、期权可研究但不可执行。**

## 二、数据质量与覆盖

本期按协议读取了[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻逐合约EOD、Night、Options surface及合约元数据。

- 统一输入：schema v2，`requested_date=2026-09-09`，19:17生成。
- Futures/Market State：19:02生成；SHFE/INE/DCE/CZCE/GFEX共802合约，802/802源日期匹配，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0。8条placeholder已排除；无重复、非法OHLC或负量仓。20个同合约交易日历史完整。
- `official_complete=false`来自basis、会员排名、部分仓单及DCE/GFEX元数据缺口，不影响核心EOD有效性。仓单仅CZCE当日可用；GFEX五项沿用9月1日，SHFE/DCE仓单缺失。
- Physical：19:17生成，20项中18项按原生频率fresh、SC/LU unavailable；可计算basis均为C级，只作context，不计方向层。
- External：19:17生成，17/22 fresh、5项unavailable，均为`context_only`，无exact import parity。
- Options：9月9日22,302个合约、375个series、57/64产品；AP/CJ/MA/PF/PL/PR/ZC失败。IV覆盖97.98%、OI覆盖68.77%、bid/ask覆盖0；364个series可研究surface、70个可研究positioning、0个可执行。全局surface/positioning/execution均false，Dealer Gamma方向未知。
- Metadata：质量partial；有效合约匹配73.32%，multiplier/tick有效覆盖35.79%，margin/limit约29.80%，last-trading-day 73.32%，夜盘字段未发布；未确认参数不推断。

Night Session质量闸门通过：`trading_date=2026-09-09`、`night_session_date=2026-09-08`，06:03生成；data_fresh、validation_passed、published、coverage_complete均true；594个有效夜盘合约、55个产品，193个合法outside-window、15个no-night-trade，missing timestamp/price/quote、query error、unresolved contract均为0。

这批Night是**今天早前已完成、属于9月9日交易日的连续交易阶段**，只用于隔夜→日盘分解；绝不是今晚21:00未来行情。

## 三、商品仪表盘

Night栏为早前Night close、相对9月8日close/settlement；Day为9月9日EOD close相对同合约Night close。量仓单位为手，海外为19:17—19:40可得参考。

| 板块 | 合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；curve | Basis/Physical | Night；vs close/settle；ΔOI；Day | 15:00后海外/Options S-P-E | 21:00信号 |
|---|---|---|---|---|---|---|---|
| 原油 | **SC2610** | 741.5/722.5；+2.73%/+6.67% | 18.2万/3.92万/+476；+5.61% back | SC不可得 | 714.7；-0.82%/+1.62%；-849；**+3.75%** | Brent 100.69；Y-N-N | 回撤接受多，不追 |
| 燃料 | **FU2611** | 3999/3934；+1.05%/-0.93% | 83.5万/21.6万/-1,641；+5.97% back | C级context | 3895；-2.33%/+0.05%；-17,335；**+2.67%** | 柴油紧；Y-N-N | 等30m |
| 甲醇 | **MA610** | 3411/3402；+3.75%/+7.76% | 316.8万/57.9万/-148,449；+6.88% back、roll警告 | C级 | 3408；+1.46%/+3.93%；-30,275；+0.09% | 油价支持；N-N-N | 高位消化，不追 |
| 芳烃 | **EB2610** | 9928/9786；+1.26%/+3.81% | 91.4万/29.3万/+1,541；+3.22% back | 缺完整实体层 | 9688；-1.59%/+0.25%；-14,989；**+2.48%** | 油/芳烃支持；Y-Y-N | 回撤确认多 |
| 聚酯 | **TA701** | 6188/6146；+1.59%/+1.75% | 109.4万/113.0万/+759；产品近端+7.09% back | C级 | 6142；-1.10%/+1.52%；-18,118；+0.75% | 成本支持；Y-Y-N | 仅守位观察 |
| 芳烃 | **PX611** | 9118/9050；+2.08%/+2.65% | 30.9万/16.6万/-10,929；-1.75% contango | C级 | 9010；-1.55%/+1.62%；-10,841；+1.20% | 油强/结构反对；Y-N-N | 不追 |
| 铜 | **CU2610** | 111080/111120；+0.78%/+2.78% | 10.6万/22.9万/-1,353；+0.32% back | C级 | 111300；+0.61%/+0.94%；+13；-0.20% | LME铜14674；Y-Y-N | 晨间多未扩张 |
| 铝 | **AL2610** | 24560/24560；+0.45%/+2.08% | 17.3万/24.7万/-11,326；近乎平坦 | C级 | 24645；+0.76%/+0.80%；+122；-0.34% | LME铝3337；Y-Y-N | 不追纪录价 |
| 氧化铝 | **AO2701** | 2773/2791；+1.16%/+1.53% | 20.6万/18.8万/+30,274；-3.18% contango | 无A级basis | 2798；+0.50%/+1.41%；+25,908；-0.89% | 无exact映射；Y-Y-N | 价仓强/结构反对 |
| 苹果 | **AP701** | 7546/7555；+1.22%/+2.33% | 13.2万/11.6万/+14,689；+1.14% back | 无完整实体层 | 无夜盘 | 无直接海外锚；N-N-N | 次日日盘观察 |
| 黄金 | **AU2610** | 952.22/950.14；-0.60%/+1.05% | 20.3万/14.9万/-1,583；-0.14% contango | 不适用 | 949.24；-0.41%/-0.70%；+910；+0.31% | 金约4401；Y-Y-N | 地缘信用仍弱 |
| 棕榈油 | **P2701** | 10307/10306；-1.10%/+0.22% | 67.3万/60.3万/-29,048；+1.25% back | C级 | 10324；-0.78%/-0.93%；-9,450；-0.16% | BMD 4968；Y-N-N | 无共振 |
| 铁矿 | **I2701** | 738/737.5；-0.34%/+2.86% | 24.8万/61.2万/+21,534；近乎平坦 | C级 | 739；-0.74%/-0.14%；+12,437；-0.14% | SGX 99.25；Y-Y-N | 弱、等实体 |
| PVC | **V2701** | 5103/5079；+0.85%/+3.89% | 182.6万/117.4万/+52,708；-0.95% contango | 缺完整实体层 | 5118；+0.10%/+1.63%；+45,423；-0.29% | 无exact映射；Y-Y-N | 结构冲突 |
| 锂 | **LC2701** | 142000/142040；-0.66%/-8.75% | 14.8万/40.5万/+6,860；曲线近平 | 仓单沿用9/1 | 无夜盘 | 无可靠外盘锚；Y-N-N | 不接第一刀 |

15:00后最重要的新信息是Brent越过100美元、WTI约95.21美元，金价约4401美元/盎司；这是今晚中国潜在gap映射，不是中国已成交事实。[Reuters全球市场，2026-09-09](https://www.reuters.com/world/china/global-markets-global-markets-2026-09-09/) 人民币升至约三年半高位，方向上略抵消进口成本冲击，但本期没有exact USD/CNH报价，不量化传导。[Reuters外汇，2026-09-09](https://www.reuters.com/world/asia-pacific/yen-stands-tall-dollar-wobbles-oils-run-towards-100-chills-sentiment-2026-09-09/)

## 四、相比上一交易日/今晨真正变化

1. **SC完成“早前Night弱→日盘强”的反转。** Night相对前收-0.82%，日盘相对Night +3.75%，EOD价涨仓增且back仍陡；今晚外油再越100美元提供第三层支持。但close已在日高附近，21:00首跳赔率反而下降。

2. **FU与芳烃获得日间而非隔夜确认。** FU早前Night -2.33%，日盘+2.67%；EB早前Night -1.59%，日盘+2.48%。欧洲柴油接近199美元/桶、炼厂利润处纪录区，支持“产品紧于原油”的竞争性解释。[Reuters油市，2026-09-09](https://www.reuters.com/business/energy/brent-crude-rises-above-100-barrel-middle-east-conflict-escalates-2026-09-09/)

3. **MA晨间强势主要已在Night完成。** Night +1.46%，日盘收盘相对Night仅+0.09%，且EOD ΔOI -148,449；价格站稳但边际弹性与持仓确认下降，昨晚77分延续多降级。

4. **中国PPI公布为输入性通胀，而非广谱需求牛市。** 8月PPI同比+3.8%、环比+0.4%；国家统计局称原油、有色带动石油开采、成品油、有机化工和有色冶炼上涨，而黑色与非金属矿物仍跌。这支持能化/有色成本链，不支持把黑色建材整体做多。[国家统计局解读，2026-09-09](https://www.stats.gov.cn/sj/sjjd/202609/t20260909_1965261.html)

5. **CU/AL晨间突破没有获得日盘扩张。** 两者EOD close都低于早前Night close且OI下降；晨间触发路径因无分钟数据仍记unknown，不假设成交。LME高位仅维持外部背景。

6. **SC outright新增最强反证。** 中石化研究预计2026年中国石油需求同比下降约8.9%，汽油、柴油与乙烯当量消费均降；地缘供给冲击与内需疲弱同时存在，故不把100美元Brent直接等同SC无条件多。[Reuters，2026-09-09](https://www.reuters.com/business/energy/china-oil-demand-fall-89-2026-sinopec-research-says-2026-09-09/)

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：继续观察；9月9日OHLC跨越原止损与入场区，缺分钟路径，触发状态unknown。原因：新EOD及海外柴油数据。
- `COM-M-MA610-SETTLE-RECLAIM-20260908`：77降至71；价格延续但Night后无follow-through、OI大减。若此前确已建立，按原计划在3450附近减仓；本期不假设持仓。
- `COM-E-TA701-DAY-REPRICE-20260908`：76降至69；日高6218未触及第二入场6240，原6120—6170承接路径unknown。
- `COM-E-SC2610-GAP-20260905`：75升至78；价格、curve、海外三层确认，但原卡执行窗口已过，今晚改为新回撤条件。
- `COM-M-CU2610-LME-RECORD-20260909`与`COM-M-AL2610-LME-FOLLOW-20260909`：均降为观察，因日盘未扩张且OI下降。
- `COM-M-PG2610-OIL-BREADTH-20260908`、`COM-M-FG701-FAILED-SQUEEZE-20260908`与`COM-E-V2701-SQUEEZE-20260904`维持失效/退出观察池，不因单日反弹重置观点。

没有成交反馈，不假设任何真实持仓。

## 五、产业链地图

- **原油—燃料—芳烃：最强，偏多但高度延伸，置信度中高。** SC/FU/EB价格与back同向，SC/EB日盘价涨仓增，外油与柴油裂解支持；SC需求预测、FU减仓及全部高质量实体缺失是反证。
- **MA—PX—TA：成本推动、链内分化，置信度中。** MA大部分价格发现已在Night，PX价格上涨但contango且减仓，TA温和follow-through。最大缺口是加工利润、库存及exact同月份curve。
- **铜铝：高位消化，置信度中。** 境外价格维持高位、PPI输入性通胀支持，但CU/AL日盘低于Night、OI下降；AI/Capex主题缺可识别现金流—需求模型，本期不能增加独立层。
- **黑色建材：最弱，置信度中。** PPI显示黑色冶炼、非金属矿物价格环比下降；I价跌仓增只是归因线索，curve近平，未形成可交易趋势。
- **农产品与新能源：最缺edge。** P/Y与BMD/CBOT缺方向共振；AP仅价仓与curve两层；LC五日仍跌8.75%，仓单沿用快照，不能把低位当反转。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | **SC2610回撤接受多** | 22/15/19/13/9 | **78** | 1、2、4 | 待验证优势｜部分｜等30m |
| 2 | **FU2611产品紧张延续多** | 22/18/17/12/8 | **77** | 1、2、4 | 待验证优势｜部分｜等30m |
| 3 | **EB2610日间反转多** | 21/17/16/13/9 | **76** | 1、2、4 | 待验证优势｜部分｜等30—45m |
| 4 | **MA610高位消化后续多** | 20/15/15/12/9 | **71** | 1、2、4 | 待验证优势｜部分｜等回撤 |
| 5 | **AP701价仓突破观察** | 20/17/8/13/11 | **69** | 1、2 | 待验证优势｜部分｜等9/10日盘 |

分项总和已复核；分数不是胜率或仓位指令。SC/FU/EB/MA属于同一油价—输入通胀因子，合并计风险。第5层期权对SC/FU/EB均未形成方向支持，只提供波动定价与执行否决。

## 七、前三名交易卡

### 1. SC2610｜回撤接受多｜78

**事实：** 9月8日前收/前结算720.6/703.3；早前Night OHLC 716.2/725.0/705.2/714.7，-0.82% vs close、+1.62% vs settlement，ΔOI -849；9月9日EOD 741.5/722.5，day follow-through +3.75%，ΔOI +476，near-next back 5.61%。19:40前Brent约100.69。

**市场定价：** 中国日盘已大幅交易地缘供给风险；今晚外油新涨只增加gap尾部。  
**分歧：** 产品/航运冲击可能继续，但中国需求下修意味着SC outright不应获得无限溢价。  
**最强反证：** 地缘缓和、替代运输恢复或Brent跌回99以下。  
**最佳表达：** SC2610期货；近月期权IV显著高于RV且无bid/ask，不优于线性工具。

- 好成交：21:00后等30分钟，733—740回撤被接受，再重上744/VWAP，先1/3仓。
- 中成交：744—752横盘后突破752并成功回踩，仓位为好成交的一半。
- 坏成交：直接高于760无回撤，放弃。
- 止损：30分钟接受722.5下方；逻辑失效：跌破714.7、back明显收窄且Brent低于99。
- TP1 760或1.5R；TP2 790或3R；1—3D无扩张退出。
- 风险0.30%—0.50% NAV；限价，首30分钟预留2—4 ticks及滑点，滑点>计划1R的15%放弃。
- 1,000桶/手，tick 0.1元/桶，tick value 100元；按741.5名义约741,500元。最后交易日2026-09-30、最后交割日10月14日，实物交割，9月中旬起只减不加并准备roll。动态margin/limit未确认。
- 一板/两板压力损失分别为`741,500×L`与`741,500×[1-(1-L)^2]`；期货最大损失不受结构限定。

### 2. FU2611｜产品紧张延续多｜77

**事实：** 前收/前结算3988/3893；早前Night OHLC 3938/3939/3833/3895，-2.33%/+0.05%，ΔOI -17,335；EOD 3999/3934，day follow-through +2.67%，ΔOI -1,641，back 5.97%。  
**市场定价：** FU日盘重新计入成品油紧张，但减仓说明持仓层只中性偏支持。  
**分歧：** 海外柴油紧张可能比SC outright更耐久；竞争解释是FU只是滞后beta补涨。  
**最佳表达：** FU2611期货；不把它与SC的近似美元中性腿称裂解套利或beta-neutral。

- 好成交：等30分钟，3950—3990承接，再站上4000/VWAP，1/3多。
- 中成交：突破4020、回踩不破，仓位减半。
- 坏成交：直接高于4070无回撤，放弃。
- 止损：30分钟接受3930下方；逻辑失效：跌破3895、back收窄且Brent回到99以下。
- TP1 4120/1.5R；TP2 4280/3R；两日时间止损。
- 风险0.25%—0.45% NAV，与SC/EB/MA合并。
- 10吨/手，tick 1元/吨，tick value 10元；名义约39,990元。最后交易日2026-10-30、最后交割日11月3日，实物交割；10月中旬前roll。动态margin/limit未确认。
- 一板/两板压力为`39,990×L`与`39,990×[1-(1-L)^2]`；极端gap与流动性消失可穿透计划止损。

### 3. EB2610｜日间反转多｜76

**事实：** 前收/前结算9804/9664；早前Night OHLC 9804/9815/9625/9688，-1.59%/+0.25%，ΔOI -14,989；EOD 9928/9786，day follow-through +2.48%，ΔOI +1,541，near-next back 3.22%。  
**市场定价：** 芳烃在中国日盘重新获得成本与供应溢价。  
**分歧：** EB比PX更有结构确认；竞争解释是油价推动的一次性补涨，缺实体供需验证。  
**最佳表达：** EB2610期货；期权surface可研究、execution=false。

- 好成交：等30—45分钟，9850—9910承接后重上9945/VWAP。
- 中成交：突破9970并成功回踩，仓位减半。
- 坏成交：直接高于10150无回撤，放弃。
- 止损：30分钟接受9775下方；逻辑失效：跌破9688、back压至2%以下且SC/FU同步反转。
- TP1 10200/1.5R；TP2 10600/3R；两日时间止损。
- 风险0.25%—0.40% NAV；与SC/FU/MA合并，单一主题未确认前总风险不超过1.25% NAV。
- 5吨/手、tick 1元/吨、tick value 5元；名义约49,640元。DCE动态margin/limit、EB2610确切最后交易日与交割参数本次未可靠取得；下单前须向交易所/经纪商复核并提前roll。
- 压力损失仅能写成`49,640×L`及`49,640×[1-(1-L)^2]`，不能在L未确认时伪造数值。

## 八、商品期权专项

Options为9月9日最新EOD截面，不是21:00实时报价：

| Underlying/expiry | ATM IV | RV20 | IV-RV | RR25/BF25 | S/P/E |
|---|---:|---:|---:|---:|---|
| SC2610/09-11 | 55.15% | 35.74% | +19.41vol | -1.55/-0.84 | Y/N/N |
| FU2611/10-19 | 54.13% | 39.22% | +14.91vol | -4.41/-2.38 | Y/N/N |
| EB2610/09-16 | 33.31% | 25.35% | +7.96vol | +3.39/+2.12 | Y/Y/N |
| TA701/12-11 | 30.43% | 26.68% | +3.74vol | +2.74/+1.10 | Y/Y/N |
| PX611/09-28 | 32.31% | 31.58% | +0.73vol | +2.26/待复核 | Y/N/N |
| AO2701 | 18.19% | 13.45% | +4.74vol | 待复核 | Y/Y/N |

SC/FU短期event vol已经很贵，不能仅凭地缘风险认定Call便宜；EB/TA/PX的IV-RV较温和，但bid/ask覆盖为0，仍不能给净权利金、滑点或当前Greeks。MA/AP当日期权链失败。Dealer Gamma方向未知。

所有结构仅为：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 九、21:00夜盘开盘风险地图

四层时间边界：①9月9日中国EOD已完成；②上述Night是今天早前已完成阶段；③15:00—19:40外油、金价和汇率只是gap映射；④今晚21:00尚未发生，归属9月10日。

| 品种 | 可能开盘 | 内外/历史冲突 | 首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|---|
| SC | 高开/宽幅 | 日盘已涨、外油再涨 | **不追** | 30m | 733/741.5/752、Brent 100、back |
| FU/LU/BU | 偏高 | 产品紧，但FU减仓 | 不追 | 30—45m | FU 3930/4000、产品相对SC |
| EB/BZ | 偏高 | 日盘反转、实体缺 | 不追 | 30—45m | EB 9850/9945、curve、SC联动 |
| MA | 偏高/震荡 | Night已定价、日盘无follow-through | 不追 | 30m | 3340/3400/3490、OI |
| TA/PX/EG | 小高/分化 | 成本支持、PX contango | 不追 | 45m | TA 6140/6218、PX curve |
| CU/AL/ZN | 平/小高 | LME高位、中国日盘消化 | 不追 | 30m | CU 110400/111720、LME |
| AU/AG | 平/偏高 | 金价+1%，但收益率高 | 不追 | 15—30m | AU 949/955、金4400、10Y |
| RU/NR/BR | 平/偏高 | 国内趋势强、海外确认不足 | 不追 | 45m | curve与三胶breadth |
| I/RB/HC | 平/偏弱 | PPI实体反证 | 不追 | 30—45m | I 733/742、钢材量仓 |
| P/Y/M/RM | 平开 | 海外日频仅context | 不追 | 30m | CBOT/BMD、油脂裂解 |
| AP/SF/SM/JD/LC/SI/PS | 无夜盘 | 不适用 | 不适用 | 9月10日09:00 | 当日量仓、curve、实体 |

哪些是噪音：AO的价仓强但深contango、V的增仓上涨但日盘低于Night、AP单日突破缺实体，均不能直接升级趋势。哪些不值得交易：PX高开追多、P/Y方向赌注、LC第一刀、任何缺exact parity的跨市场“套利”。

## 十、未来24小时 / 7日事件

- **9月10日09:00：** HC、SS与LU期权挂牌；首日只观察chain、surface、持仓与bid/ask，不使用伪历史IV。[SHFE/INE公告](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html)
- **9月10日20:30：** 美国8月PPI；油价、贵金属与美元因子在公布前降低Delta，若期权报价仍不可验证则不用“有限凸性”名义代替风险控制。[BLS日程](https://www.bls.gov/schedule/2026/home.htm)
- **9月10日晚至9月11日凌晨：** 劳动节顺延后的EIA周度石油数据；SC/FU/LU/BU/PG在发布前降低同因子风险，执行前以[EIA假期日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)复核准确分钟。
- **9月11日16:00附近：** IEA 9月Oil Market Report；对“供给中断vs需求下修”最关键。[IEA发布页](https://www.iea.org/reports/oil-market-report-september-2026)
- **9月11日20:30：** 美国8月CPI；AU/AG及工业金属面临Delta/Vega重置。[BLS CPI](https://www.bls.gov/schedule/news_release/cpi.htm)
- **9月12日00:00：** USDA WASDE与Crop Production；M/Y/P/OI/C/CF避免无保护事件仓。[USDA日程](https://www.usda.gov/about-usda/reports-and-data/agency-reports)
- CFTC COT属于滞后至周二的拥挤背景，不能解释今晚price/OI；持续监控Hormuz、红海航运、沙特能源设施和炼厂运行。

## 十一、覆盖核对、风险与归档

强制63个代码全部取得9月9日有效主力合约并完成同合约1D/3D/5D/20D、量仓、curve、产业链和策略类别扫描；另扫描JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR共14个动态品种。

- 实际取数并分析：63个强制品种全部；动态BZ/LG/OP/PD/PL/PT/RR/WR有效，77个产品记录中71个具备可用价格层。
- 不适用/流动性不足：JR/PM/RI/RS/WH/ZC的代表记录为零价、零量或极低OI，不入榜；无夜盘品种按制度列不适用，不视为缺失。
- 数据不足：期权AP/CJ/MA/PF/PL/PR/ZC；全部期权执行报价；SC/LU Physical；A级/B级exact basis；Dubai/Oman、HSFO/VLSFO、DXY、USD/CNH exact映射；SHFE/DCE仓单及GFEX最新仓单；DCE/GFEX完整动态合约参数。
- 未入榜板块异常：黑色I价跌仓增但无curve/实体共振；有色AO价仓强而contango反对；新能源LC仍弱；油脂P/Y缺内外同向；软商品AP两层突破；EC缺exact海外映射，均不足70分。
- 已扫描方向、跨期、曲线、基差、跨品种/跨市场、近似dollar-neutral、波动率、偏度、事件凸性与1D—20D；没有定义完整权重与beta的篮子，不发布伪中性组合。

风险预算：单笔试仓0.25%—0.50% NAV，确认后0.75%—1.0%；SC/FU/EB/MA/TA/PX同因子合并，未出现实体第四层前总风险≤1.25%，远低于2.5%—3.0%主题上限。压力测试包含两板、gap、止损穿透、保证金上调、相关性破裂、人民币急升、地缘缓和与炼厂恢复。

固定六路径已按main直接发布并回读；manifest中`2026-09-09 + commodities_evening`恰好一条，`archive_status=success`；CI未轮询，`ci_validation_status=pending_or_unverified`。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2610等30分钟在733—740承接并重上744；FU2611守3950—3990并重上4000；EB2610守9850—9910并重上9945。  
C. 今晚应继续观察的机会：MA610高位消化、AP701次日日盘突破、CU/AL与LME共振、TA/PX curve分化，以及多FU/空SC的产品紧张RV研究。  
D. 今晚必须避免或退出的交易：追SC/FU/EB/MA首跳；重启已失效PG/FG/V观点；把C级basis、连续外盘或近似美元中性称套利；在execution_ready=false时臆测期权成本。
