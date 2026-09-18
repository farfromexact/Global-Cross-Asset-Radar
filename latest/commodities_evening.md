# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-18

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:42 BJT；信息截点：19:30；最近完整中国交易时段：9月18日日盘。未见特殊休市公告，今晚21:00连续交易按正常周五安排归属9月21日交易日；EC、LC等无夜盘品种下一窗口为9月21日09:00。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；LU相对SC的价差获curve确认，但已快速扩张，今晚只等比价回撤，绝不在能源暴跌后追单边。**

当前regime：**沙特经Sohar增运与管道修复预期压缩原油供应溢价，SC及芳烃链去杠杆；低硫近端结构仍紧，贵金属在油价回落、美元/收益率缓和与地缘需求下反弹。**

最接近触发的是多LU2611/空SC2611相对价值、SC2611反弹失败空和AG2612回撤接受多。三者分别缺比价回撤、单边反抽失败、白银回撤接受；所有中国商品期权仍缺可执行双边报价。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Night逐合约文件](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json)和[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-18`，19:12:31生成。
- Futures：五所806合约、77产品；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；4条placeholder排除。
- Market State：77产品，同合约1D/3D/5D/20D历史可用；多品种短曲线样本与roll限制已单列。
- Physical：9月18日18/20序列按日频fresh，SC/LU unavailable；所有basis为C级或缺失，只作context，不计完整实体层。
- External：repo日频17/22 fresh、5项unavailable，均为`context_only`。repo WTI/Brent 95.75/98.62与18:08 BJT附近Reuters 101.30/103.17显著冲突，隔离repo油价，不构造exact跨市场套利。
- Options：截至19:30最新有效截面为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖99.11%/69.50%/0。DCE因供应商安全拒绝缺失；T日截面尚不可得，9月17面只作可比品种的存量研究背景。
- Metadata：partial；有效合约匹配73.45%，multiplier/tick/margin/limit约30.15%，last-trading-day约67.49%。

Night状态：`trading_date=2026-09-18`、`night_session_date=2026-09-17`，06:01:29生成；`data_fresh=true`、`validation_passed=true`、`published=true`，但`coverage_complete=false`。806个请求合约中423条有效、37产品；165条合法outside-window、4条no-night-trade；214条query error且214个unresolved contract，missing timestamp/price/quote均为0，warning明确指向DCE安全拒绝。

这批Night属于今天早前已完成的连续交易阶段，**不是今晚21:00行情**。原始逐合约文件经connector返回空payload，而状态与统一输入明确存在423条；读取状态记为`empty connector payload / source not empty`。Top候选使用统一输入中的exact representative contract；近次月双腿不能同时审计，故不强拼Night curve。

## 三、商品仪表盘

1D/5D为9月18日同合约结算收益；`day`为EOD close相对早前Night close，仅在合约完全一致时计算。curve是near-minus-next期货结构，不是现货基差；S/P/E为9月17日surface/positioning/execution readiness。

| 板块 | 品种/合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical/basis | 早前Night close；vs close/vs settle；ΔOI；day | 15:00—19:30海外；S/P/E；21:00信号 |
|---|---|---|---|---|---|
| 原油 | SC2611；728/754.4；-6.29%/-0.30% | 28.52万/4.22万/-2,115；back **1.59%**、z-2.49 | 缺失 | 762.5；-2.89%/-5.28%；-980；**-4.52%** | Brent103.17；Y/N/N；反抽失败空 |
| 成品油 | LU2611；5440/5515；-2.10%/+0.51% | 15.64万/7.14万/+1,703；back **4.79%**、z2.30 | 缺失 | 5574；+0.60%/-1.05%；+1,334；**-2.40%** | 原油弱、产品库存/裂解仍紧；无成熟series；相对多 |
| 成品油 | FU2611；4200/4259；-3.29%/-0.77% | 81.04万/19.09万/-12,686；back12.80% | 7525，C/context | 4298；-0.26%/-2.41%；-1,990；-2.28% | 原油弱；Y/N/N；不追空 |
| 聚酯 | PX611；9160/9238；-3.47%/-1.33% | 41.25万/17.76万/-10,325；back0.65% | 9800，C | 9338；-0.41%/-2.42%；-5,006；-1.91% | 原油续跌；Y/Y/N；弱势延续 |
| 聚酯 | TA701；6238/6312；-2.86%/0.00% | 226.73万/121.16万/+10,883；back2.14% | 7108.8，C | 6398；+0.16%/-1.54%；-10,146；-2.50% | 成本回落；Y/Y/N；反抽失败空 |
| 芳烃 | EB2611；9470/9477；-2.99%/-5.06% | 59.54万/28.80万/+11,276；back4.86%、z2.20 | 缺失 | DCE缺失 | 上游弱；DCE option缺；curve反对追空 |
| 黑色 | JM2701；1487/1527；-5.30%/-5.30% | 111.29万/45.72万/-42,633；back2.81% | 2423.75，C | DCE缺失 | 无exact外盘；DCE option缺；不追空 |
| 黑色 | J2701；1952.5/1985.5；-3.85%/-5.20% | 6.97万/3.20万/-561；轻contango0.13% | 2290，C | DCE缺失 | 内需弱；无执行面；观察 |
| 贵金属 | AG2612；16304/16104；+2.79%/+2.73% | 16.59万/21.50万/+8,244；轻contango0.12% | context | 代表AG2610，不能分解 | 现货银66.92、+2.7%；Y/N/N；回撤多 |
| 贵金属 | AU2612；951.38/946.18；+0.96%/+0.17% | 11.96万/19.75万/+13,041；轻contango0.08% | context | 代表AU2610，不能分解 | 现货金4378.19、+0.9%；Y/N/N；不追 |
| 有色 | CU2610；109620/109530；+1.31%/+0.80% | 9.27万/15.78万/-7,625；back0.33%、短样本 | 110235，C | 109650；+1.06%/+1.42%；-776；-0.03% | LME代理14515.5；Y/Y/N；Night已定价 |
| 有色 | ZN2611；26565/26575；+1.63%/-1.04% | 13.17万/15.54万/+5,940；轻contango0.15% | 缺失 | 26590；+1.18%/+1.68%；+3,522；-0.09% | LME代理3920；局部/N/N；Night已定价 |
| 农产品 | M2701；3397/3429；-1.47%/+0.21% | 204.64万/273.12万/-196,992；contango1.10% | 3448，C | DCE缺失 | CBOT豆1308.75/粕354.4；DCE option缺；旧多失效 |
| 建材 | FG701；907/912；+0.55%/-7.32% | 108.62万/129.52万/-70,452；back3.70% | 1008，C | 913；+0.88%/+0.66%；-47,960；-0.66% | 无exact外盘；Y/Y/N；单日噪音 |
| 航运 | EC2610；2172.5/2189；+2.99%/+7.09% | 2.54万/2.53万/-1,176；back21.29% | exact运价缺 | 制度无Night | Hormuz船流低但非exact集运；N/N/N；周一再核 |

Reuters截至18:08 BJT附近报价为Brent 103.17、WTI 101.30美元/桶；沙特经阿曼增运、产品库存上升与中国成品油出口增加压制油价，但Hormuz周四可识别商品船仅4艘、低于10日均值约16艘，供应右尾仍在。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-fall-1-hopes-limited-supply-disruptions-2026-09-18/) [Reuters沙特增运](https://www.reuters.com/business/energy/aramco-boost-exports-strait-hormuz-60-million-bbl-september-october-traders-say-2026-09-18/)

现货金截至16:29 BJT附近报4378.19美元/盎司、+0.9%，银报66.92、+2.7%；BOJ加息至31年高位，但油价回落与地缘需求支撑贵金属。该信息是海外增量，不是中国21:00已成交价格。[Reuters贵金属](https://www.reuters.com/business/gold-extends-gains-scale-one-week-high-crude-prices-ease-2026-09-18/)

## 四、相比上一交易日/今晨真正变化

1. **LU/SC相对交易从两层升级为三层。** SC结算-6.29%、LU仅-2.10%；LU全日增仓而SC减仓，SC back从6.80%坍缩至1.59%，LU back扩至4.79%。价格量仓、curve和外部产品/原油分化共同支持，但比价已扩张，不能追。
2. **SC弱势不是Night重复，而是日盘继续发现价格。** 早前Night相对前收-2.89%，日盘相对Night再-4.52%；供应溢价在日盘进一步出清。EOD低于晨报TP2 760，但无成交反馈，不声称用户已获利。
3. **RM晨间多头明确失效。** RM701收2357、最低2343，跌破原卡2390止损与2396逻辑失效位；若此前按条件建立，应按原规则退出。仓单9月18日仍为11,708、日变动0，不把昨日下降重复写成新催化。
4. **M、PX、PR的强势研究被价格否定。** M收跌且减仓19.70万，PX/PR日盘继续回吐；聚酯由成本扩张切换为去杠杆，实体订单仍缺。
5. **贵金属成为最强板块，但大部分海外涨幅已被日盘预交易。** AG/AU价涨仓增，海外金银继续强；正式合约早前Night不匹配、curve不确认、期权无执行报价，因此只够两层、封顶69。
6. **数据结构一好一坏。** 五所EOD完全恢复；Night因DCE安全拒绝降至37产品，T日期权尚不可得，不能把全市场恢复误写为所有模块完成。

旧建议台账：

- `COM-M-LUSC-RELATIVE-20260918`：69→80；新增curve分化确认。晨间14:1条件是否成交无法由OHLC证明，触发状态未知；新卡按当前价格改为13:1近似名义中性，不假设既有仓位。
- `COM-M-SC2611-REVERSAL-20260917`：66→76；日盘继续下跌且back坍缩，但赔率变差，改为反弹失败才空。若此前建立，按原TP/时间止损管理。
- `COM-M-RM701-WAREHOUSE-TIGHT-20260918`：68→退出；价格跌破止损与逻辑失效位，原因是价格反证，不以仓单旧数据续命。
- `COM-M-EC2610-FREIGHT-REPRICE-20260918`：67→66；日盘上涨但收盘低于晨报重上2220条件、OI下降；触发状态未知，周末不新增。
- `COM-M-AP701-RELATIVE-WEAK-20260918`：59→退出正式榜；日盘反弹、OI下降，旧弱势未延续。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：继续观察而非重启多头；深back支持、价格和外油反对。

## 五、产业链地图

- **最强相对链：LU强于SC，偏多LU/空SC，置信度中高。** EOD相对收益、OI方向、curve分化与海外原油/产品分化三层支持；最大反证是SC供应风险突然重燃或LU back跌破3%。
- **最弱单边：SC—PX—TA—PR与焦煤焦炭，偏空但追价赔率差。** SC及芳烃日盘继续弱，TA/EB价跌仓增提供归因线索；JM/J主要为减仓下跌，back反对把去杠杆直接解释成新空趋势。
- **最强绝对板块：AG—AU贵金属，偏多但置信度中。** 国内价仓与海外同向，油价回落缓解再加息路径；curve、正式合约Night和可执行期权均未确认。
- **农产品：由相对强转为普遍去杠杆，置信度中低。** M/RM价格下跌，M大幅减仓；CBOT豆类高位和中美采购预期只作外部支持，不构成进口平价。
- **航运与新能源：事件与价格分化。** EC上涨但减仓、back收窄；LC反弹后再跌且无Night。缺exact运价、锂盐库存和A级basis，不发布伪套利。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | 多13 LU2611/空1 SC2611近似名义中性 | 23/16/18/14/9 | **80** | 1、2、4 | 存在待验证优势｜充分但比价已扩张｜等21:45回撤 |
| 2 | SC2611反弹失败空 | 22/14/18/13/9 | **76** | 1、2、4 | 存在待验证优势｜部分、Hormuz反证｜等21:45 |
| 3 | AG2612回撤接受多 | 20/15/14/9/11 | **69** | 1、4 | 存在待验证优势｜部分、curve/正式Night缺失｜等21:45 |
| 4 | TA701弱势延续空 | 19/16/15/8/10 | **68** | 1、4 | 存在待验证优势｜部分、back反对｜反抽失败 |
| 5 | EC2610事件风险多 | 18/15/15/9/9 | **66** | 1、2 | 证据不足｜exact运价缺失、OI下降｜9月21日待核 |

分项均已复算且不超上限。AG、TA、EC只有两层，严格封顶69。LU/SC与SC单边属于同一原油溢价因子，二选一；所有期货及期货组合的最大损失均不由计划止损限定。

## 七、前三名交易卡

### 1. 多13手LU2611 / 空1手SC2611｜回撤型相对价值｜80

**事实：** LU close/settle=5440/5515，早前Night=5574，overnight +0.60%，day -2.40%，ΔOI +1,703，back4.79%；SC close/settle=728/754.4，早前Night=762.5，overnight -2.89%，day -4.52%，ΔOI -2,115，back1.59%。  
**市场定价：** 原油供应溢价快速出清，而低硫近端紧张被保留。  
**分歧：** LU相对SC仍可能延续，但EOD比价7.47已计入大量分化；最强竞争解释是LU只是滞后补跌，或Hormuz再恶化令SC反向跳升。

- 最佳表达：多13手LU2611、空1手SC2611；EOD名义约707,200元对728,000元，差2.86%，只称**近似dollar-neutral**，绝非beta-neutral。
- 收益公式：`130×(LU退出-LU入场)-1000×(SC退出-SC入场)`元。
- 好成交：21:45后LU/SC回撤至7.30—7.45并重新站稳7.40；同时LU守5380、SC反弹735—750后转弱，先1/3单位。
- 中成交：比价突破7.55后回踩7.46—7.55不破，仓位减半。
- 坏成交：比价直接高于7.65、任一腿深度不足或两腿滑点合计超过计划1R的20%，放弃。
- 止损：45分钟接受7.20下方；计划止损不限制跳空和相关性破裂损失。
- 失效：LU back低于3%、SC back重上4%，或Brent重上106且Saudi/Hormuz供应重新恶化。
- TP1比价7.65或+1.5R；TP2 7.90或+3R；1—3D无扩张退出。
- 风险：单单位很大，仅适合NAV与保证金匹配账户；试仓最大损失0.25% NAV，与任何SC/FU/LU方向仓合并≤0.50%。
- 参数：LU 10吨/手、tick 1元/吨、tick value 10元；SC 1,000桶/手、tick 0.1元/桶、tick value 100元。两者最后交易日10月30日、最后交割日11月6日，实物交割；10月中旬前移仓。
- 交易所9月14日起将SC/LU 10月与11月合约限幅调至16%、套保保证金17%；客户/投机实际保证金须下单前核验。[Reuters/交易所风控调整](https://www.reuters.com/business/energy/shanghai-exchange-adjust-trading-limits-some-oil-futures-contracts-2026-09-11/)
- 以16%压力、EOD名义计，一板两腿反向约229,632元；连续两板复合约459,796元。周五Night建仓须承受整个周末事件gap。

### 2. SC2611｜反弹失败条件空｜76

**事实：** T日OHLC=770/775.9/725.2/728，结算754.4；1D -6.29%，ΔOI -2,115，back1.59%。早前Night OHLC=787/791.9/750/762.5，vs close -2.89%、vs settlement -5.28%，Night ΔOI -980；day follow-through -4.52%。

- 市场隐含：Sohar替代装运、管道部分恢复和产品库存上升压缩近端溢价。
- 分歧：back坍缩显示结构确认，但价格已接近极端，Hormuz船流低位提供强右尾反证。
- 好成交：21:45后反抽740—760失败并重新跌破730/VWAP，先1/3仓。
- 中成交：先跌破725，再回抽728—735失败，仓位减半。
- 坏成交：直接低于710、盘口变薄或Brent急升，放弃。
- 止损：45分钟接受776上方；失效为back重上4%、Brent高于106且供应恢复预期逆转。
- TP1 705或+1.5R；TP2 670或+3R；1—2D无扩张退出。
- 风险0.15%—0.25% NAV；若使用LU/SC组合，不再叠加SC单边。
- 1,000桶/手、tick0.1、tick value100；EOD名义728,000元。限幅16%，一板反向压力约116,480元、两板复合约251,597元；客户保证金下单前确认。最后交易日10月30日、最后交割日11月6日，实物交割。[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)

### 3. AG2612｜回撤接受条件多｜69

**事实：** T日OHLC=15970/16321/15940/16304，结算16104；1D +2.79%、ΔOI +8,244，curve轻contango0.12%。早前Night代表合约为AG2610，无法对AG2612做exact分解；海外银截至16:29 BJT附近+2.7%。

- 市场定价：油价回落降低进一步激进加息的边际压力，地缘与贵金属资金流重新占优。
- 分歧：国内价仓与海外同向仍可能延续；反证是高利率、正式合约Night缺失、curve未确认以及9月17期权偏度异常。
- 好成交：21:45后16020—16150获得接受并重上16280/VWAP，先1/4仓。
- 中成交：突破16330后回踩16250—16320不破，仓位减半。
- 坏成交：直接高于16700或海外银跌回65下方，放弃。
- 止损：45分钟接受15920下方；失效为跌破15650、现货金跌破4300且银跌破64。
- TP1 16650或+1.5R；TP2 17200或+3R；1—3D无扩张退出。
- 风险0.15%—0.20% NAV；与AU/CU同宏观因子合并≤0.40%。
- 15千克/手、tick 1元/千克、tick value 15元；EOD名义244,560元。repo仅确认最后交易日12月15日、最后交割日12月17日；动态margin/limit未确认，不编一板金额。实物交割，11月末前复核移仓。

## 八、商品期权专项

最新可得为**9月17日T-1截面**；能源、聚酯与贵金属9月18日大幅变动后，moneyness、Delta和IV-RV可比性明显下降。全市场212/54/0个series分别surface/positioning/execution-ready；DCE产品缺失。

| Underlying/expiry | 9/17 ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/56.54% | +9.02vol | +0.73/+1.41 | Y/N/N | 底层再跌，旧面不可执行 |
| FU2611/10-19 | 60.62%/45.36% | +15.26vol | -1.82/+6.25 | Y/N/N | event convexity仍贵 |
| TA701/12-11 | 33.33%/30.24% | +3.09vol | +4.27/-0.09 | Y/Y/N | 底层下移，须重报价 |
| RM701/12-11 | 20.80%/约16.2% | 约+4.6vol | +5.11/+0.13 | Y/Y/N | 价格已跌破旧多失效位 |
| FG701/12-11 | 23.28%/25.43% | -2.15vol | +6.33/+1.15 | Y/Y/N | IV<RV不单独证明便宜 |
| CU2610/09-23 | 13.73%/约15% | 约-1.3vol | -2.82/+0.81 | Y/Y/N | 临近到期，先核交割 |
| AG2612/11-24 | 曲面ready但偏度异常 | N/A | 异常值隔离 | Y/N/N | 不据此构造结构 |
| M/EB/JM/LU/EC | DCE缺失或无series | N/A | N/A | N/N/N | 数据不足 |

期权目前不优于裸期货或明确配比的期货组合。只有取得21:00实时双边报价后，才研究SC有限净支出put spread或AG有限净支出call spread；执行价、Delta、净支出、盈亏平衡、Greeks、滑点和行权交割均须重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、21:00夜盘开盘风险地图

严格四层：①9月18日中国EOD；②属于9月18交易日的早前Night；③15:00—19:30海外增量；④今晚21:00尚未发生、正常归属9月21日交易日。周五Night后的持仓跨周末，事件gap权重大于普通工作日。

| 品种 | 早前Night→日盘→海外 | 21:00判断 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| LU/SC | LU +0.60%→-2.40%，SC -2.89%→-4.52%；外油续跌 | 比价可能高开，单边偏低 | 不追；45m | 比价7.30—7.45、双curve、Brent |
| SC | Night弱、日盘再跌、back坍缩；Hormuz右尾仍高 | 低开/反抽双向 | 不追空；45m | 725/730/760/776、back |
| FU | Night近零、日盘-2.28%、深back；外油弱 | 偏低但结构冲突 | 45m | 4190/4260、back、相对LU |
| PX/TA/PR/PF | Night温和弱→日盘再跌→油价续弱 | 偏低 | 不追；45m | TA6230/6310、PX9150、breadth |
| EB/EG/BZ | DCE Night缺失、日盘弱、curve仍back | 低/平开不确定 | 45m | exact盘口、OI、curve |
| JM/J/I | DCE Night缺失、日盘去杠杆 | 低开概率高 | 不追；45m | JM1485/1530、板块breadth |
| AG/AU | 中国价仓强→海外金银继续涨 | 偏高 | 不追；45m | AG15920/16280、金4378、银66.9 |
| CU/ZN/AL | Night完成多数涨幅、日盘横盘→外盘代理高位 | 平/小高开 | 30—45m | CU109650/110000、LME、CNH |
| M/RM | DCE Night缺失、日盘反转→CBOT豆类高位 | 平/偏低 | 45m | M3387/3430、RM2343、OI |
| FG/SA | Night反弹被日盘回吐 | 平开、噪音高 | 30m | FG904/913、SA1005/1014 |
| EC/LC/AP/JD/SF/SM/SI/PS | 制度无Night | 今晚不交易 | 9月21日09:00后30—45m | 量仓、curve、实体 |

人民币/美元：repo没有exact USD/CNH和DXY，公开宏观只支持“美元压力较前日缓和”的定性判断；不编人民币进口成本贡献率。最不值得交易的是低开追SC/JM/PX、追AG第一跳、把LU/SC价差当无风险套利，以及任何未重报价的期权。

## 十、未来24小时与7天事件

- 9月18日21:00：周五Night，归属9月21日；所有新仓考虑周末Hormuz、Saudi管道和外交headline gap，至少等待30—45分钟。
- 9月19日03:30附近：CFTC COT常规发布窗口，只作滞后拥挤背景。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 周末：East-West管道恢复节奏、Sohar船到船转运、Hormuz可识别船流、Saudi—Houthi冲突；能源相对价值也需按共享事件因子计风险。
- 9月21日09:00：中国下一日盘；EC、LC、AP等无夜盘品种只在开盘后30—45分钟重评。
- 未来一周：中美元首会晤及农业、能源、稀土议题；M/RM/C与有色只按实际协议和价格响应调整，不先验押注。[Reuters商品议题](https://uk.marketscreener.com/news/what-commodity-markets-can-expect-from-the-trump-xi-summit-ce785bd3d081f620)
- 9月23日22:30：EIA周度石油数据；能源仓数据前减Delta。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)
- 9月24日20:30附近：USDA出口销售常规窗口；豆粕、玉米和油脂等待真实采购兑现。[USDA出口销售](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 未来7日：交易所动态保证金/限幅、SC/LU/FU交割月与期权到期；禁止跨事件裸卖vol，只有实时报价下的有限净支出结构可留Vega。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态新增，共77产品；期权64产品。
- 实际取数且已分析：77产品进入全量扫描，70个具备有效趋势/量仓/curve；五所EOD806合约完整；Night 37产品/423合约；期权45产品/216 series。
- 数据不足：DCE Night 214合约查询/解析失败；T日期权未完成、19个产品失败或跳过、0 execution-ready；SC/LU实体不可用；A/B级basis、exact import parity、可靠加工利润、正式合约AG/AU Night与可执行期权成本不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；均保留覆盖记录。
- 黑色建材9/9：JM/J日盘跌幅最大但多为减仓，FG/SA是Night反弹后回吐；I/RB无三层优势。
- 有色贵金属12/12：AG/AU最强，CU/ZN多数涨幅在Night完成；NI/SN/SS未出现三层共振。
- 能源炼化化工25/25：LU/SC相对交易入榜；SC、TA入榜；FU/PX/PR/EB/BZ弱但back反对追空。
- 新能源及GFEX新材料全部扫描：LC跌势反复，PT/PD随海外贵金属但缺足够历史与参数；SI/PS无三层异常。
- 农产品油脂饲料畜牧22/22：RM旧多失效，M减仓下跌；油脂、玉米、养殖无三层优势。
- 航运及软商品全部扫描：EC入低分观察，CF/CY/SR/AP/CJ/PK无可验证三层错价。
- 策略覆盖：方向、跨期、curve、跨品种/跨市场、近似名义中性、波动率/偏度/事件凸性均已扫描；exact套利、beta-neutral篮子与可执行期权因输入不足不发布。

风险预算：单笔试仓最大损失0.15%—0.25% NAV；LU/SC组合上限0.25%，与SC/FU/LU方向仓共享因子合并≤0.50%；贵金属合并≤0.40%；任何主题确认后总风险仍≤2.5%。压力测试覆盖1/2个涨跌停、周末地缘gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压和人民币急变。

归档状态将在六路径main回读后写入最终交付；CI只作独立事后校验，不等待。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：21:45后多13手LU2611/空1手SC2611，仅在比价回撤至7.30—7.45并重上7.40时试仓；或SC2611反抽740—760失败并重破730时试空，二者二选一、共享风险≤0.50%。  
C. 今晚应继续观察的机会：AG2612回撤接受多、TA701反抽失败空、EC2610周一事件重估、FU深back以及DCE Night/期权数据恢复。  
D. 今晚必须避免或退出的交易：若此前建立则按原规则退出RM701多头；避免低开追SC/JM/PX、追AG第一跳、把LU/SC称无风险或beta-neutral、恢复EC旧多，以及在execution-ready=false时臆测期权成本。
