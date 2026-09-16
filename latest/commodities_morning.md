# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-17

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：07:06 BJT；信息截点：07:00；最近完整中国EOD：9月16日；当前交易日：9月17日；下一可交易窗口：09:00日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；能源夜盘在EIA与FOMC后转弱，09:00只做SC反弹失败空或M回撤接受多，严禁低开追空。**

当前regime：**沙特替代路线缓解原油极端短缺定价、成品油实货仍紧；美联储加息与强美元压制贵金属和高估值工业品，中国内需链偏弱，农产品局部独立。**

最接近触发的是SC2611反弹失败空与M2701回撤接受多。SC缺09:45后的失败确认，M缺09:30后的承接和量仓恢复；FG701弱势延续只有一层证据，暂不进入可执行条件单。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)和[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-16`，9月17日06:16:07生成；EOD=T-1、Night `trading_date=T`是正常晨间组合。
- Futures：9月16日EOD，五所806合约、77产品；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；7条OHLC占位记录排除。
- Market State：同合约1D/3D/5D/20D历史完整；NI主力为NI2611，但Night代表NI2610，不能硬做同合约分解。
- Physical：9月16日刷新失败，模块`data_fresh=false/validation_passed=false/published=false`；沿用的9月15日last-good仍有18/20序列，SC/LU不可用。全部basis为C级或缺失，只作context，不计完整实体层。
- External：17/22 fresh、5项unavailable，均为`context_only`。repo WTI代理97.29与Reuters主力结算102.43明显冲突，隔离该WTI数值；Brent代理105.42与主力105.83接近但仍不构成exact套利。
- Options：9月16日18,098条、337个series、52/64产品；330个surface-ready、73个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖97.92%/67.81%/0。SC及SHFE金属因source-date跳到9月17日而失败，不用错误日期截面。
- Metadata：partial；有效合约匹配73.45%，multiplier/tick覆盖36.10%，margin/limit覆盖30.15%，last-trading-day覆盖73.45%；DCE参数端点失败。

Night质量闸门：`trading_date=2026-09-17`、`night_session_date=2026-09-16`，06:01:11生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。806个请求合约中610条有效、55个产品；189条合法outside-window、7条no-night-trade；missing timestamp/price/quote、query error、unresolved均为0，warnings为空。

该Night属于今天已经完成的连续交易阶段。原始`night_session/latest.json`经connector返回0字节payload，而状态与统一输入明确存在610条；读取状态记为`empty connector payload / source not empty`。Top候选具体合约均使用紧凑层exact record；近次月两腿无法同时审计，不强拼Night curve；`night_session_fallback_used=false`。

## 三、商品仪表盘

1D/5D为9月16日同合约结算收益；Night为归属9月17日的已完成session。曲线为near-minus-next期货结构，不是现货基差；S/P/E为surface/positioning/execution readiness。

| 品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical/basis | Night close；vs close/vs settle；ΔOI | 07:00海外；Options；信号 |
|---|---|---|---|---|---|
| SC | SC2611；827/838.4；+0.26%/+22.56% | 24.08万/4.15万/+1,704；back 6.32% | 缺失 | 804.8；-2.68%/-4.01%；+2,620 | WTI结算102.43；N/N/N；反抽失败空 |
| LU | LU2611；5673/5687；+1.12%/+10.06% | 16.35万/6.92万/+625；back 2.81% | 缺失 | 5609；-1.13%/-1.37%；+1,154 | Brent105.83；无成熟chain；不追空 |
| FU | FU2611；4488/4493；+0.25%/+14.21% | 99.38万/21.41万/+2,116；back 18.14%、z2.11 | 9月15日现货7362.5，C | 4405；-1.85%/-1.96%；+83 | 柴油裂解仍极高；Y/N/N；冲突 |
| PR | PR611；8646/8570；+3.18%/+8.34% | 15.81万/6.91万/+4,770；back 2.40%、z1.57 | 缺失 | 8584；-0.72%/+0.16%；-3,009 | 上游回落；Y/Y/N；旧多降级 |
| PX | PX611；9650/9692；+2.13%/+7.09% | 49.49万/17.73万/+12,172；back 0.97% | 9月15日9600，C | 9664；+0.15%/-0.29%；-1,950 | 油价回落；Y/N/N；横盘 |
| TA | TA701；6556/6520；+1.31%/+6.09% | 208.21万/117.31万/+3,752；back 3.44% | 9月15日7045.25，C | 6550；-0.09%/+0.46%；+2,226 | 上游回落；Y/Y/N；不追 |
| M | M2701；3479/3434；+1.78%/+1.09% | 171.44万/289.00万/+174,015；contango 1.10% | 9月15日3382，C | 3463；-0.46%/+0.84%；-6,556 | CBOT豆1321.5/粕354.5；Y/Y/N；回撤接受 |
| NI | NI2611；122240/122060；-1.78%/-4.33% | 11.10万/12.96万/+6,040；roll/轻contango | 缺失 | 代表NI2610=122430；+0.32%/+0.48%；-5,295 | LME镍16100；N/N/N；旧空降级 |
| CU | CU2610；107740/107430；+0.47%/-3.32% | 7.99万/16.54万/-14,719；轻back0.31%、roll | 9月15日107675，C | 107960；+0.20%/+0.49%；-2,822 | LME铜14226.5；N/N/N；不追方向 |
| AU | AU2612；940.52/934.2；+0.32%/-1.91% | 8.49万/17.79万/+8,727；轻contango | context | 代表AU2610=935.18；-0.27%/+0.41% | Fed后现货金一度4240.1；N/N/N |
| AG | AG2612；15832/15653；+1.25%/-3.25% | 12.79万/20.43万/+1,580；roll | context | 代表AG2610=15603；-1.21%/+0.04% | 银约-1.7%；N/N/N |
| FG | FG701；910/910；-1.30%/-6.19% | 104.96万/130.57万/+68,443；back 3.27% | 9月15日1008，C | 905；-0.55%/-0.55%；+40,308 | 无exact外盘；Y/Y/N；反弹失败空 |
| SA | SA701；1011/1012；-0.59%/-5.86% | 103.84万/129.67万/+15,153；contango0.61% | 9月15日1090，C | 1008；-0.30%/-0.40%；+11,810 | 无exact外盘；局部/N/N；不追 |
| LC | LC2701；125820/126380；-2.51%/-11.03% | 21.31万/41.75万/-1,204；back0.49% | 9月15日131000，C | 制度无Night | Y/N/N；减仓跌不追空 |
| EC | EC2610；2080/2050；-0.89%/+6.11% | 0.93万/2.39万/-482；back28.71% | exact运价缺 | 制度无Night | 事件映射不纯；N/N/N；旧多仍退出 |

9月16日Brent结算105.83美元/桶、-2.7%，WTI结算102.43、-3.2%；沙特经阿曼Sohar增加转运缓解短缺，而EIA仅录得原油库存减少64万桶、汽油增加79.4万桶、馏分油增加160万桶，低于原油多头的预期。[Reuters油市](https://www.reuters.com/business/energy/oil-falls-us-crude-inventories-rise-despite-saudi-supply-concerns-2026-09-16/)｜[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)

美联储9月16日一致决定加息25bp至3.75%—4.00%，美元指数约升至100.05、10年美债收益率约5.02%；现货金会后一度跌至4240.10美元/盎司，白银跌约1.7%。这些是07:00附近外盘/事件信息，不是中国09:00日盘已经成交的价格。[FOMC声明](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)｜[Reuters美元](https://www.reuters.com/world/asia-pacific/dollar-girded-by-bets-us-hiking-cycle-2026-09-16/)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-muted-investors-brace-fed-rate-decision-2026-09-16/)

## 四、相比上一交易日/今晨真正变化

1. **能源旧多逻辑完成失效，而不是正常回撤。** SC相对前收-2.68%、FU-1.85%、LU-1.13%；SC在晚报已因EOD日内反转停止新增，本期FOMC/EIA后再下台阶，旧多不恢复。
2. **SC相对close与settlement方向一致。** -2.68%与-4.01%没有“结算锚夸大新弱势”的问题；Night增仓2,620只提供价仓归因线索，不证明新空身份。
3. **FU最强反证仍是18.14% back和创纪录柴油裂解。** Night下跌获得外油确认，但成品油实货紧张反对裸空，故短端只允许反弹失败，不允许低开追击。[Reuters亚洲柴油](https://www.reuters.com/business/energy/asia-diesel-refining-margins-record-high-more-than-87-barrel-data-shows-2026-09-16/)
4. **PR与M的日盘突破均未获Night延续。** PR相对前收-0.72%、ΔOI -3,009；M相对前收-0.46%、ΔOI -6,556。M仍高于结算0.84%，比PR保留更多回撤接受价值。
5. **FOMC把贵金属信用主题再次否定。** AU/AG正式合约Night无法同合约分解，外盘金银在加息与美元走强后回落；不将避险叙事强行解释为多头。
6. **期权数据已恢复到9月16日，但执行仍为零。** FU ATM IV从事件高位回落至63.56%，仍高于RV20约21.07vol；PR/M曲面可研究，但bid/ask覆盖为0。

旧建议台账：

- `COM-E-SC2610-GAP-20260905`：维持停止；本期不因反弹预期重启。新反向研究使用`COM-M-SC2611-REVERSAL-20260917`，避免把旧多ID偷换为空头。
- `COM-M-LU2611-PRODUCT-RELATIVE-20260915`：75→停止新增；Night回落且外油转弱。昨晚条件在OHLC内是否先触发无法核实，无成交反馈，不假设持仓。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：73→观察；旧多并未触及“back低于15%”的结构失效，但价格层反对，暂停条件单，不反向满仓。
- `COM-C-PR611-POLYESTER-PASS-20260916`：69→58；Night价跌仓减、上游外油回落，回到研究观察。
- `COM-M-M2701-SOYMEAL-FOLLOWTHROUGH-20260916`：59→65；仍以回撤接受多研究，Night回吐使其不能升级为确认交易。
- `COM-M-NI2610-DOLLAR-PRESSURE-20260916`：69→退出正式榜；主力切至NI2611且Night代表NI2610反弹，不能拼接。

## 五、产业链地图

- **最弱：SC—LU—FU能源价格链，偏空但置信度仅中。** EIA、外油和中国Night同向回落，支持1/4两层；EOD深back、沙特部分供货仍取消、柴油裂解高位强烈反对追空，实体层对SC/LU缺失。
- **最强实货子链：柴油/燃料产品，方向冲突。** 亚洲柴油裂解超过87美元/桶、近月价差紧，但FU/LU Night下跌；这是供应紧与宏观去风险的冲突，不是可直接做跨市场套利。
- **聚酯：PR/PX/TA从扩张转为消化，置信度中低。** PR EOD价仓和curve支持，Night价跌仓减；PX/TA近乎横盘。缺利润、订单和A级basis，不发布多腿篮子。
- **农产品：M相对最强，置信度中。** EOD价涨仓增、CBOT豆/粕维持高位支持，Night小幅回吐、contango与C级basis反对追价。
- **最弱内需链：FG—SA—LC，置信度中低。** FG价跌仓增并在Night续弱，SA类似；LC五日跌幅扩大但减仓。高质量库存与仓单方向不足，均不适合低开追空。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | SC2611反弹失败空 | 19/17/16/8/9 | **69** | 1、4 | 存在待验证优势｜部分、curve/供应反对｜等待09:45 |
| 2 | M2701回撤接受多 | 20/15/12/9/9 | **65** | 1、4 | 存在待验证优势｜部分、Night减仓反对｜等待09:30 |
| 3 | LU2611弱势延续空 | 17/15/15/8/8 | **63** | 1、4 | 存在待验证优势｜部分、实体缺失/back反对｜等待09:45 |
| 4 | FG701弱势延续空 | 18/14/11/8/8 | **59** | 1 | 证据不足｜不足｜等待反弹失败/实体 |

分项均已复算。SC/M/LU只有两层支持，严格封顶69；FG只有一层，封顶59。本期无70+候选。所有期货最大损失均不由计划止损限定；分数只是研究排序，不是胜率或仓位指令。

## 七、前三名交易卡

### 1. SC2611｜反弹失败条件空｜69

**事实：** previous close/settlement=827/838.4；Night OHLC=829.9/832.3/788.1/804.8，vs close -2.68%、vs settlement -4.01%，Night ΔOI +2,620；EOD back 6.32%。  
**市场定价：** 极端供应中断溢价开始让位于阿曼替代装运、库存数据与紧缩宏观。  
**分歧：** 价格回落可能继续，但back和剩余实物流风险意味着不能在Night低位追空。最强反证是Yanbu/East-West再恶化或Brent重新站上108。

- 最佳表达：SC2611单腿条件空；期权产品失败，不能伪装成有限损失结构。
- 好成交：09:45后反抽812—825失败并重新跌破805/VWAP，先1/3仓。
- 中成交：先跌破788.1，再回抽800—805失败，仓位减半。
- 坏成交：直接低于780、盘口变薄或止损距离超过1R，放弃。
- 止损：45分钟接受833上方；计划止损不保证最大损失。
- 失效：重上838.4、back重新高于7%且Brent高于108，或沙特装运中断恶化。
- TP1 788或+1.5R；TP2 760或+3R；1—2D无扩张退出。
- 风险0.15%—0.25% NAV；与LU/FU方向交易合并≤0.40%。
- 1,000桶/手、tick 0.1元/桶、tick value 100元；Night名义804,800元。最后交易日10月30日、最后交割日11月6日，实物交割。[INE原油手册](https://www.ine.cn/eng/market/futures/energy/sc/manual/202004/W020250806318691873930.pdf)
- 动态margin/limit未确认；以待复核16%压力假设，一板约128,768元/手、两板复合约236,933元/手。最迟10月中旬前移仓，交割月前禁止被动持有。

### 2. M2701｜回撤接受条件多｜65

**事实：** previous close/settlement=3479/3434；Night OHLC=3479/3482/3456/3463，vs close -0.46%、vs settlement +0.84%，Night ΔOI -6,556；EOD ΔOI +174,015、contango 1.10%。  
**市场定价：** 日盘已重价采购/成本预期，Night只保留相对结算强度。  
**分歧：** 若3450附近被接受，日盘大量增仓可能还有延续；竞争解释是EOD冲高与Night减仓代表催化已经透支。

- 最佳表达：M2701单腿条件多；不把CBOT豆/粕代理当exact进口套利。
- 好成交：09:30后3445—3465获得接受并重上3475/VWAP，先1/3仓。
- 中成交：突破3482后回踩3470—3482不破，仓位减半。
- 坏成交：直接高于3510或低开跌破3430，放弃。
- 止损：30分钟接受3430下方。
- 失效：跌破3414、Night/EOD新增OI继续回吐，或CBOT大豆跌破1300且国内basis不改善。
- TP1 3505或+1.5R；TP2 3550或+3R；1—3D不扩张退出。
- 风险0.20%—0.30% NAV；与油脂和玉米方向交易合并≤0.50%。
- DCE合约参数端点本期失败；multiplier、tick、tick value、margin、limit、last trading day和交割参数均未确认，参数补齐前仅作研究条件单，不编压力损失。

### 3. FG701｜反弹失败条件空｜59

**事实：** previous close/settlement=910/910；Night OHLC=907/912/902/905，vs close/vs settlement均-0.55%，Night ΔOI +40,308；EOD ΔOI +68,443、curve back 3.27%。  
**判断：** 价格—持仓层支持弱势，但back、C级现货和缺失库存方向只够一层证据。

- 好成交：09:30后反抽909—914失败并重新跌破904，先1/4仓。
- 中成交：跌破902后回抽不破905，仓位减半。
- 坏成交：直接低于895，放弃追空。
- 止损：30分钟接受918上方。
- 失效：重上922、back继续扩大且库存/仓单出现可验证收紧。
- TP1 895或+1.5R；TP2 880或+3R；1—3D时间止损。
- 风险0.15%—0.20% NAV；低分研究卡，不是确认交易。
- 20吨/手、tick 1元/吨、tick value 20元；Night名义18,100元。保证金9%、限幅8%，最后交易日2027年1月14日、实物交割；一板反向压力约1,448元/手，两板复合上行约3,012元/手。临近2026年12月复核移仓。

## 八、商品期权专项

最新有效截面为9月16日EOD；Night与FOMC已经改变底层moneyness和Delta。全部目标结构`execution_ready=false`。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 63.56%/42.49% | +21.07vol | -1.22/+5.67 | Y/N/N | 事件凸性仍贵，put蝶形高 |
| PR611/10-13 | 32.97%/27.65% | +5.32vol | +2.12/-1.20 | Y/Y/N | Night回落后须重算Delta |
| M2701/12-16 | 15.88%/11.61% | +4.27vol | +4.02/+1.01 | Y/Y/N | call skew偏贵 |
| PX611/09-28 | 40.45%/31.44% | +9.00vol | +1.43/+0.72 | Y/N/N | 近到期，不裸买凸性 |
| TA701/12-11 | 35.48%/26.18% | +9.30vol | +3.44/+0.59 | Y/Y/N | 成本冲击已计价 |
| FG701/12-11 | 24.40%/25.69% | -1.28vol | +7.39/+1.34 | Y/Y/N | IV<RV不单独证明put便宜 |
| LC2701/12-07 | 44.42%/39.03% | +5.38vol | +1.77/+1.69 | Y/N/N | positioning不足 |
| SC/LU/NI/AU/AG/CU | 产品失败或无series | N/A | N/A | N/N/N | 不用错误日期或代理面 |

期权目前不优于裸期货：没有任何bid/ask覆盖，SC又缺有效曲面。只有取得09:00实时双边报价后，才比较M2701有限净支出call spread或SC2611 put spread；执行价、Delta、净支出、盈亏平衡、Greeks、滑点与行权交割均须重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月16日；②Current Trading Day Night=归属9月17日、已完成；③07:00 Overseas=EIA、FOMC及国际市场最新可核实变化。

| 品种 | EOD→Night→海外 | 09:00判断 | 追价/等待 | 核心确认 |
|---|---|---|---|---|
| SC | EOD日内反转/back6.32%→Night-2.68%/仓增→油价-3%、EIA偏空 | 低开概率高 | 不追空；45m | 788/805/825/833、back、Brent |
| LU | EOD+1.12%→Night-1.13%/仓增→Brent回落 | 低开，但实货仍紧 | 45m | 5605/5650/5713、相对FU |
| FU | EOD平稳/back18%→Night-1.85%→柴油裂解纪录高 | 低开、内外冲突最大 | 45m | 4388/4405/4473、back |
| PR/PX/TA | EOD强→PR回落、PX/TA近零→油价跌 | 平/低开，成本降温 | 30—45m | PR8582/8646、链内breadth |
| M | EOD价仓强→Night小跌但高于settle→CBOT高位 | 平开/回撤 | 30m | 3430/3465/3475、OI |
| FG/SA | EOD弱→Night继续小跌→无exact外盘 | 低开/震荡 | 不追；30m | FG902/905/914、SA1005 |
| NI | EOD弱→代表合约反弹/减仓→美元强 | 平开、易反抽 | 45m | exact NI2611、122000/123300 |
| CU | EOD反弹减仓→Night+0.20%/减仓→美元强 | 平开/双向 | 45m | 107430/107960/108170、LME |
| AU/AG | EOD反弹→代表合约回落→Fed加息、金银跌 | 低开概率高 | 不追；45m | exact主力、DXY100、10Y5% |
| LC/EC/AP/JD/SF/SM/SI/PS | 制度无Night | 09:00才有新价格 | 30—45m | 量仓、curve、实体 |

外油回落与中国能源Night同向，信息已经被部分吸收；09:00真正的新弹性取决于SC能否反抽805—825失败、以及FU深back是否阻止进一步下跌。repo与可靠公开源均没有同一时点exact USD/CNH，本期只确认美元走强，不量化人民币贡献。

## 十、未来24小时与7天事件

- 9月17日09:00：中国日盘；SC/LU/FU至少等待45分钟，M/FG至少等待30分钟。
- 未来24小时：Yanbu与East-West管道修复、Sohar替代装运、Hormuz通航、沙特欧洲货取消；任何重新中断会伤害能源空头，恢复则压缩back。[Reuters沙特替代路线](https://www.reuters.com/business/energy/saudi-offers-more-crude-via-oman-loading-after-pipeline-attacks-sources-say-2026-09-16/)
- 9月17日20:30附近：USDA周度出口销售常规窗口；M/C/Y/P/OI只按实际销售、采购与basis反应调整Delta。
- 9月18日—19日：美联储会后利率与美元二次定价；AU/AG/CU/NI避免隔夜高Delta，商品期权禁止裸Vega。
- 9月19日03:30附近：CFTC COT常规窗口，仅作滞后拥挤背景。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月23日22:30：下一次EIA周报；能源仓在数据前减仓，若用期权只允许有实时报价的有限净支出结构。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/)
- 未来7日：北美收割天气、中国大豆采购、马棕出口、交易所风控与SC/FU/LU交割月风险；OPEC+/IEA无计划内新月报时不制造虚假催化。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码；统一输入实际77产品；期权应覆盖64产品。
- 实际取数且已分析：77个产品进入扫描，70个具备有效趋势/量仓/curve分析；Night 55产品/610合约；期权52产品、337 series。
- 数据不足：Physical刷新失败但保留9月15日last-good 18/20；SC/LU实体缺失；期权12产品失败、0 execution-ready；Night逐合约大文件回读payload为空，无法计算Top 3 exact near-next Night curve；A/B级basis、exact import parity、可靠加工利润和可执行期权成本不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；均保留覆盖记录，没有提高门槛后静默删除。
- 黑色建材9/9：FG入榜；SA弱、JM夜盘+0.50%与内需弱冲突，I/RB无三层共振。
- 有色贵金属12/12：NI/CU正式方向降级；AU/AG在FOMC后弱，但Night代表合约不一致且期权失败。
- 能源炼化化工25/25：SC/LU入榜；FU深back与Night弱冲突；PR/PX/TA降温，EC旧多继续退出。
- 新能源及GFEX新材料全部扫描：LC五日-11.03%但减仓，PT/PD/PS/SI缺高质量实体和exact海外映射。
- 农产品油脂饲料畜牧22/22：M入榜；C/P/Y/OI Night偏弱或减仓，无三层优势。
- 航运及软商品全部扫描：EC无Night、旧多不重启；CF/CY/SR/AP/CJ/PK未发现可评分三层异常。

风险预算：单笔试仓最大损失0.15%—0.30% NAV；只有09:00价格、curve及非价格层确认后才考虑0.75%。SC/LU/FU方向风险合并≤0.40%；农产品方向合并≤0.50%；任一主题总风险≤2.5%。压力测试覆盖1/2个涨跌停、Saudi路线再中断、流动性消失、保证金上调、FOMC二次冲击、IV跳升/塌陷、交割挤压和人民币急变。

固定六路径已从main回读验证，manifest中`2026-09-17 + commodities_morning`恰好一条；[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-17_commodities_morning.md)。`archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：SC2611在09:45后反抽812—825失败并重新跌破805时试空，或M2701在09:30后3445—3465承接并重上3475时试多；单笔风险0.15%—0.30%。  
C. 今天应继续观察的机会：LU/FU低开后的深back支撑、PR/PX/TA成本扩散是否止跌、FG701反弹失败空，以及M/PR期权09:00后的实时报价。  
D. 今天必须避免或退出的交易：重启SC/LU旧多、低开追空SC/FU/LU/AU/AG、把Night增仓解释为确定资金身份、把repo冲突WTI或C级basis当exact套利，以及在execution-ready=false时臆测权利金或Greeks。

