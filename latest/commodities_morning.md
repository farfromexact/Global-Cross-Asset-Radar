# 商品期货期权晨间雷达｜2026-10-30

生成时间：2026-10-30 07:05:30（北京时间）  
信息截点：2026-10-30 07:05（北京时间）；中国最新完整EOD为2026-10-29，当前夜盘归属交易日2026-10-30。  
研究属性：高风险偏好、只研究与决策支持，不下单，不假定持仓或成交。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；银与原油下行得到隔夜确认但已不宜追空，最值得等待的是AG反抽失败、BU强曲线回踩与MA二次确认。**

已研究但优势不足：CU供应扰动多头被Teck产量与成本改善反证；LC急跌与现货/曲线相冲突；FU近月极端结构受交割月低流动性污染。  
研究机会存在但等待条件/报价：AG2612反抽失败空、BU2701回踩多、MA701二次确认多、SC2612反弹失败空。  
数据不足不能判断：Night仓库状态称413/806有记录但发布文件为空；214合约未解析，无法用仓库确认昨夜顺序、最终OI或Night Curve；DXY、USD/CNH、Dubai/Oman、燃料油裂解价和USDA分项实数未取得。

最有价值的待验证观察：

1. 09:15后AG2612能否反抽12480—12530后再次跌破，且COMEX银不回到52.50上方。
2. 09:15后BU2701能否守住5070—5100，BU2612-BU2701保持至少1.5%的近强远弱。
3. 09:15后SC2612相对Brent的隔夜超跌能否修复；若反弹失败且主力曲线显著走平，才转为条件空。

## 2. 数据质量与全范围覆盖

| 模块 | 实际取得 | 日期/生成 | 就绪判断与缺口 |
|---|---:|---|---|
| report_input | 0字节 | main当前ref | empty；未用其推导任何结论 |
| Futures | 806合约、77产品、五所238/63/214/243/48 | EOD 10-29；06:08生成 | source_date_match=100%，full_market_ready=true，invalid=0，placeholder=3，critical=0；vendor有效，但official_complete=false |
| Market State | 77产品、20个交易日 | 截止10-29 | 同合约1/3/5/20D、RV20、量仓可用；部分curve z与roll不可用 |
| Physical | 18/20目标fresh | 06:14生成 | SC、LU不可用；18项均为C级现货代理，A/B级可计分basis=0 |
| External | 17/22目标fresh | 06:14生成 | WTI/Brent/LME/COMEX/CBOT/ICE/SGX可用；DXY、USD/CNH、Dubai/Oman、HSFO/VLSFO缺 |
| Night status | 413/806夜盘记录；165 outside-window；14 no-trade；214 query_error/unresolved | T=10-30；会话10-29至10-30；06:02生成 | 日期语义合法、validation=true、published=true，但coverage_complete=false且实际2026-10-30.json为空；calendar_mismatch=false，重点报价只能用独立exact-contract fallback |
| Night语义 | 仓库无法读取逐合约字段 | 同上 | price_semantics/ohlcv_scope/official_night_close_verified均无法由原始文件确认；不将fallback称官方夜盘收盘 |
| Options | 730合约、33/64品种、33 series | EOD 10-29；06:09生成 | IV覆盖100%，OI覆盖94.79%，bid/ask=0；core_atm_ready=32、skew_ready=22，surface/positioning/execution=0，full_chain_verified=false |
| Metadata | contract match 67.49% | 10-29 | effective multiplier/tick约36.10%，margin/limit约30.15%，night session 0%；DCE参数接口失败、GFEX源日不匹配 |
| Official crosscheck | SHFE238、INE63、CZCE243、GFEX48全部可比字段差异0 | 10-29 22:15Z | DCE HTTP412；state=partial仅因源错误，不代表已有价格差异；量/OI未独立核对 |
| Stock | 5570条原始行情、5576参考证券 | 交易日10-28；10-29 09:25 BJT入库 | 调整因子、行业、tradability覆盖均0；完整财务最小包仅2家公司，不能宣称股票即时可执行 |

全范围扫描：按实际77个产品覆盖了用户列示63个代码及已上市扩展；展示仅取12项。黑色最重要异常为I2701涨2.10%但OI减40423、曲线contango；金属为AG跌价增仓与CU减仓；能化为BU/FU强、SC夜盘回落、EB价弱曲线强；新能源为LC急跌但现货代理和backwardation反对追空；农产品为JD上涨、LH/CJ下跌，USDA分项实数缺；航运EC中期弱而当日反弹。其余未入榜品种未形成三层共振。

## 3. 市场仪表盘

Night列为独立公开行情fallback，不等同仓库原始Night数据；收益分别相对10-29 close/settle。

| 品种/主力 | EOD close/settle | 1D/5D结算 | 量/OI/ΔOI | 近月曲线 | 实体/期权 | Night或海外新增 | 信号 |
|---|---:|---:|---:|---:|---|---|---|
| BU2701 | 5110/5106 | +3.26%/+13.52% | 478995/222702/+16194 | BU2611-12 +4.72%；液态BU2612-2701约+1.74% | basis C；BU2612 ATM IV43.995%，RR25 -1.28，执行0 | BU主力5107，vs close -0.06%、vs settle +0.02% | 强势停顿，不追 |
| SC2612 | 730.8/735.9 | +1.87%/+4.83% | 137858/27626/-2399 | SC2612-2701 +1.38%；SC2611低量不计 | SC Physical缺；Options缺 | 721.5，vs close -1.27%、vs settle -1.96%；Brent结算114.88(-0.38%) | 国内跌幅大于外油，等修复或反弹失败 |
| FU2701 | 5418/5475 | +3.20%/+13.78% | 933744/243843/-13681 | 显示+30.44%，但FU2611仅333手 | FU现货代理7875，basis C；ATM IV73.3%在FU2612 | WTI结算102(-0.76%) | 交割月污染，回避追价 |
| MA701 | 3413/3431 | +0.41%/+8.85% | 2292447/922160/+8320 | MA611-12 +3.67%；MA612-701约+3.21% | 现货3953，basis C；MA612 ATM IV48.205%、RR25 -0.55 | 3429，vs close +0.47%、vs settle -0.06% | 趋势停顿，等二次确认 |
| AG2612 | 12682/12918 | -1.38%/-6.60% | 457223/259939/+5115 | -0.147% contango | 当期Options未覆盖 | 主力页12388，约vs close -2.32%、vs settle -4.10%；00:57的AG2612快照12481；现货银52.44(-2.85%) | 下行确认但禁止追空 |
| CU2612 | 108660/109030 | -0.16%/+0.88% | 79005/190792/-4795 | +0.624% backwardation | 现货110910，basis C；当期Options未覆盖 | LME 3M铜14477.5；Teck供给改善 | 多头确认不足 |
| LC2701 | 88360/91140 | -5.52%/-3.56% | 344836/461555/+12632 | +0.790% backwardation | 现货93000，basis C；ATM IV55.135%，skew未ready | 无合法夜盘 | 急跌与结构冲突，不追空 |
| EC2612 | 2681.5/2666 | +0.70%/-12.07% | 12539/15061/+2238 | -15.49% contango | 实体/期权缺 | 无夜盘 | 趋势弱，等日盘再确认 |
| EB2612 | 10106/10253 | -1.08%/+3.96% | 1195215/331882/+2632 | +3.66% backwardation | basis/期权缺 | 夜盘逐合约不可核 | 价弱曲线强，方向冲突 |
| I2701 | 682/680 | +2.10%/+1.34% | 407832/575774/-40423 | -0.658% contango | 现货665，basis C | SGX铁矿90.9日线 | 反弹减仓，优势不足 |
| LH2701 | 9550/9630 | -2.58%/-3.12% | 152402/161994/-1210 | -5.87% contango | 实体/期权缺 | 无夜盘 | 下跌减仓，未到三层 |
| M2701 | 3161/3181 | -0.87%/-1.82% | 894950/2099452/+314 | -2.90% contango | 现货3248，basis C | CBOT豆1234；USDA分项实数缺 | 事件后仍待核 |

## 4. 相比前序真正变化

1. **Night从完全失败改善为状态层部分成功，但原始发布仍不可用。** 前序0/806；本次状态显示413/806、日期合法，但214未解析且文件为空。改变的是采集状态，不是执行证据。
2. **Options真实恢复。** 从10-28 last-good的19/64、430合约、ATM19/skew12，升至10-29的33/64、730合约、ATM32/skew22；但bid/ask仍0，完整曲面/持仓/执行仍0。
3. **AG下行得到海外与Night双重确认。** AG fallback相对结算-4.10%，现货银-2.85%；旧“破位反抽空”方向增强，但因反抽步骤未发生、价位已远离原入场区，不能追空，得分66升至73。
4. **SC旧多头子观点失效。** 10-29晨间的SC gap-retention long要求SC>=738、曲线和Brent共振；日盘结算735.9且夜盘721.5，条件失败。新建反弹失败空头子观点，保留原short父idea，不移动旧止损、不回填收益。
5. **BU与MA没有获得强隔夜确认。** BU近乎持平，MA相对close小涨但相对settle略跌；旧条件仍是“等待”，不是已触发。
6. **CU供应论证进一步降级。** LME铜仍高但Teck披露铜产量同比+11%、成本下降及年度产量指引维持，供给响应是对纯粹短缺多头的独立反证。

## 5. 产业链与公司利润桥

### 油—SC/FU—BU

外油高风险溢价仍在，但Brent结算仅-0.38%，SC夜盘相对结算约-1.96%，BU近乎持平；国内品种的信息弹性分化。FU近月曲线被交割月低量污染，不能作为裂解或现货紧张的无风险证据。最大缺失是Dubai/Oman、HSFO/VLSFO、炼厂利润与A/B级basis。置信度：中。

### 油—MA/L/EB

MA与塑料链5日仍强，MA夜盘只维持而未扩张；EB日盘价格弱、曲线强，显示供需与资金未同向。MA现货代理3953相对期货较高但为C级，不能做套利。置信度：中低。

### 贵金属—AG/AU

AG日盘跌价增仓，夜盘与现货银继续下行；AU跌幅相对温和，说明银的高beta去风险更强。曲线轻度contango支持空头，但当期AG期权缺失，无法验证put skew或可成交保护结构。置信度：中高；表达首选等待期货反抽，不是追价put。

### 铜—CU—Teck/紫金

Teck Q3铜产量115700吨、同比+11%，铜净现金成本1.77美元/磅低于去年2.09；铜分部折旧前毛利16亿加元，高于7.4亿。利润桥是“实现铜价6.40美元/磅+产量提升+副产品/成本改善”共同驱动，而不是单一现货上涨。最强竞争解释：天气和罢工仍可能扰动短期供给；推翻供给改善判断需看到产量指引下修或LME/CU重新同步突破。紫金映射仅来自旧半年报，Stock私库截至10-28且复权/行业/tradability缺，股权表达不优于直接CU，决策贡献为降低CU多头确信度。置信度：中高。

### 锂—LC—相关股

LC急跌但93000元/吨现货代理、backwardation和期权ATM IV55.135%均不支持盲目追空；skew未ready、Stock目录没有可靠锂公司利润桥，数据不足而非无机会。置信度：低。

Stock限定公开补证实际检索：Teck Q3原始披露、Teck电话会资料页、CNOOC季度报告页。CNOOC页面截至07:05尚未出现2026Q3，故油价对CNOOC利润只保留“实现售价—产量—成本—税费—汇率—套保/长协—兑现时滞”的待验证桥；不宣称股票即时可执行。

## 6. 统一机会榜

| 排名 | idea_id / 方向 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 五层证据 | 三轴状态 |
|---:|---|---:|---:|---|---|
| 1 | COM-M-AG2612-POST-FOMC-BREAKDOWN-SHORT-20261029 条件空 | 20/16/15/12/10 | **73** | 支持1/2/4；实体和期权缺 | 研究优先；三层；等待反抽、不可追 |
| 2 | COM-E-BU2701-STRONG-CURVE-PULLBACK-LONG-20261026 条件多 | 19/15/13/12/9 | **68** | 支持1/2；4中性偏反对，5反对 | 重点；两层上限；等待回踩 |
| 3 | COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024 条件多 | 18/14/12/12/9 | **65** | 支持1/2；3仅C级，4/5不支持 | 观察；两层上限；等待二次确认 |
| 4 | COM-E-SC2612-CONTANGO-REBREAK-SHORT-20261030 条件空 | 18/14/13/10/9 | **64** | 支持1/4；主力曲线反对，3/5缺 | 观察；两层上限；仅反弹失败 |
| 5 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028 观察空 | 17/14/11/12/9 | **63** | 支持1/2；海外运价、实体、期权缺 | 观察；两层上限；无Night执行证据 |

评分仅为研究优先级，不是胜率。BU/MA/SC/EC均受两层证据上限约束；AG虽有三层，也因追价赔率、期权报价和Night原始文件缺失而不具备即时执行条件。

## 7. 研究/交易卡

### 卡1｜AG2612反抽失败空

- 事实：EOD close/settle 12682/12918；1D -1.38%、5D -6.60%；OI +5115；曲线-0.147%。公开主力页为12388（约相对close -2.32%、相对settle -4.10%），AG2612在00:57的准确合约快照为12481；两者均非交易所核验终值，并与现货银52.44(-2.85%)同向。
- 定价/分歧：下行已被明显定价；分歧不是“还会立刻大跌”，而是反抽若无法收复12580，趋势可能延续。
- 入场顺序：09:15后先反抽12480—12530，再在12580下方失败15分钟，且COMEX银<=52.50、AG2611-12<=0.10%；40%/60%。首价<12250或未反抽，放弃。
- 好/中/坏：12530/12505/12480；计划止损12820；TP1 12150、TP2 11800；11月4日14:45退出。
- 每手计划风险：4350/4725/5100元；TP1毛R约1.31/1.13/0.97，TP2约2.52/2.24/2.00；费用与滑点未知，不能当0。
- 合约参数：15千克/手、tick 1元/千克、tick value 15元；AG2612当前涨跌停20%、一般保证金22%，最后交易日2026-12-15，夜盘21:00—02:30。
- 压力：按12918结算的一/二个涨停，空头中档约损4.49万/9.15万元每手；计划止损不封顶。
- 期权替代：AG put spread仅研究；当期AG未进入33个成功品种，不能给strike、权利金、Greeks或最大净支出。
- 风险预算：试仓NAV0.25%，确认后<=0.60%，贵金属共同因子<=1.5%。

### 卡2｜BU2701强曲线回踩多

- 事实：EOD 5110/5106，1D +3.26%、5D +13.52%，OI +16194；液态BU2612-BU2701结算近强远弱约1.74%。Night fallback 5107，未延续冲高。
- 定价/分歧：强势已部分定价；只有回踩守住且液态曲线不塌，才说明供应风险尚未完全透支。
- 入场顺序：09:15后BU>=5120持续15分钟，且BU2612-BU2701>=1.50%、Brent>=114；随后回踩5070—5100守5050，40%/60%。首价>5180或曲线<1.0%放弃。
- 好/中/坏：5070/5085/5100；计划止损4990；TP1 5220、TP2 5360；11月2日14:45退出。
- 每手计划风险：800/950/1100元；TP1毛R约1.88/1.42/1.09，TP2约3.63/2.89/2.36；费用与滑点未知。
- 参数：10吨/手、tick 2元/吨、tick value 20元；涨跌停12%、一般保证金14%；最后交易日2027-01-15，夜盘21:00—23:00。
- 压力：中档一/二跌停约5917/11309元每手；保证金不是风险预算，止损不保证成交。
- 期权替代：BU2612期权11月24到期、ATM5200、ATM IV43.995%、RR25 -1.28，标的月份与BU2701不同，bid/ask为0；只研究，必须人工询价与重新核moneyness。
- 风险预算：试仓NAV0.25%—0.50%，确认后<=1.00%，油品主题<=2.5%。

### 卡3｜SC2612反弹失败空

- 父观点：COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026；同胞多头COM-E-SC2612-POST-EIA-GAP-RETENTION-LONG-20261029已因738确认失败和夜盘721.5而失效。
- 事实：EOD 730.8/735.9，1D +1.87%、5D +4.83%，OI -2399；SC2612-2701仍backwardation约1.38%，这是空头反证。Night exact fallback 721.5，相对settle -1.96%；Brent仅-0.38%。
- 定价/分歧：国内已比外油跌得更多；只有反弹失败且主力曲线显著走平，空头才有赔率。
- 入场顺序：09:15后反弹724—727，在730下方失败15分钟，且Brent<=113.5、SC2612-2701<=0.60%；40%/60%。首价<712或曲线仍>1.0%，放弃。
- 好/中/坏：727/725.5/724；计划止损738；TP1 710、TP2 695；11月2日14:45退出。
- 每手计划风险：11000/12500/14000元；TP1毛R约1.55/1.24/1.00，TP2约2.91/2.44/2.07；费用未知。
- 参数：1000桶/手、tick 0.1元/桶、tick value 100元；最后交易日2026-11-30。当前margin/limit仓库为空，独立参数页显示18%/16%，正式执行前必须由INE/经纪商复核。
- 压力：按735.9结算的一/二个涨停，空头中档约损12.8万/26.5万元每手；最坏gap与流动性枯竭可超过该情景。
- 风险预算：仅试仓NAV0.25%，确认后<=0.60%，与BU/FU/油股合并计油品主题。

## 8. 商品期权专项

- 口径：core_v1、sampled_strikes，33/64品种、730合约、33 series；quote_coverage_complete只表示计划样本完成，不是全链。
- 局部就绪：ATM 32组、skew 22组；完整surface、positioning、execution均0。vendor Greeks覆盖100%但单位原样，不能跨品种直接比较；dealer方向未知。
- IV-RV：BU2612 ATM IV43.995%高于BU2701 RV20 31.72%；MA612 48.205%高于MA701 38.15%；LC2701 55.135%高于RV20 41.78%；FU2612 73.3%高于FU2701 44.31%。月份/到期不一致时仅作背景，不能称便宜或昂贵已可交易。
- Skew：BU RR25 -1.28、MA -0.55，均显示样本put相对更贵；LC skew未ready；AG/SC未进入成功样本。BF只在对应series ready时使用，不外推完整wing。
- 回避：不从样本OI推全链PCR、拥挤或dealer gamma；不编bid/ask、净权利金、滑点和有限损失。事件凸性优先等CFTC/OPEC+/PMI前人工询价后再评估。
- Vol RV：若要表达AG尾部风险，首选人工询价后的限损put spread；未报价前不替代期货止损，也不计作风险封顶。

## 9. 09:00开盘风险地图

| 主题 | Previous China EOD | Current T Night/海外 | 09:00—09:45动作 |
|---|---|---|---|
| AG | 12682/12918、跌价增仓、contango | 12388 fallback；现货银-2.85% | 可能低开；不追。09:15看反抽，09:30看12580，09:45才决定是否进入条件空 |
| SC | 730.8/735.9、主力曲线backwardation | 721.5 fallback；Brent114.88 | 可能低开但国内超跌；先看修复。曲线不走平则不空 |
| BU | 5110/5106、强量仓、液态曲线近强远弱 | 5107 fallback；油价小跌 | 偏平开；5120与液态曲线同向后再等回踩 |
| MA | 3413/3431、5日强、曲线backwardation | 3429 fallback | 偏平；09:15看3450，09:30看MA612-701，09:45仍无共振则取消 |
| CU | 108660/109030、OI减少 | LME3M 14477.5；Teck供给改善 | 平弱；不追供应扰动多，需109600/LME14500再确认 |
| LC | 急跌、OI增加但backwardation/现货反对 | 制度无夜盘 | 可能延续波动；不接飞刀、不追空，等15/30/45分钟结构 |

已过夜盘条件仅作历史审计，不写成未来条件；没有成交回执，实际持仓状态均为未提供/未知。

## 10. 未来24h / 7d事件与行动前检查

- 10月30日中国日盘：上期所周度仓单、SC2611临近最后交易日与限仓切换；Delta方向需等曲线，Vega表达必须人工询价。
- 10月30日CNOOC Q3窗口：截至07:05官网未出现2026Q3。若产量/实现油价/成本/Capex显著改变，重评油链和股权表达。
- 10月31日03:30：CFTC COT，数据通常截至周二；AG/AU/油的拥挤判断在发布前保持缺失。
- 10月31日09:30：中国10月PMI。黑色、有色、化工对新订单/原材料库存分项敏感。
- 11月1日：OPEC+月度会议；10月4日决定维持9月所需产量用于11月，会议前油品承担跳空与Vega风险。
- 11月2日/3日：美国ISM制造业、USDA Crop Progress与美国政治事件窗口；农产品、DXY和实际利率传导需复核DST。
- 11月4日23:30：EIA WPSR常规时间（美国转冬令时后）；油链期货止损不能替代事件gap风险。
- 11月5日21:30：USDA Export Sales常规窗口；当前10月29报告分项实数未取得，M/RM/Y/P仅观察。
- 地缘与天气：霍尔木兹/沙特基础设施消息与美伊外交并存，多个转述不增加独立证据；南美播种天气在USDA原始数据前不写精确概率。

行动前必须复核：exact-contract实时双边价、BU/SC/MA液态曲线、AG/SC海外锚、乘数/保证金/限幅/最后交易日、Night原始文件修复、期权bid/ask、账户共同因子风险和旧观点失效状态。风险预算：试仓NAV0.25%—0.75%，确认0.75%—1.50%，同一高确信主题总计不超过2.5%—3.0%；本期各卡使用更紧上限。压力包括1/2限幅、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、汇率急变与中国休市海外波动。

发布校验：分项加总均等于总分；AG/BU/SC卡的每手风险与毛R已重算；Night归属日期合法但原始文件为空，已隔离；MD/JSON将同源生成；未取得bid/ask、USDA实数、Stock tradability与DCE官方交叉核对，未宣称通过。

## 主要来源

- [China-Commodities-Engine EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)
- [Night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)
- [External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)
- [Futures crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)
- [Brent/WTI 10月29日结算与地缘背景](https://www.reuters.com/business/energy/us-oil-prices-fall-investors-gauge-risks-mideast-supply-2026-10-29/)
- [LME Closing Prices](https://www.lme.com/market-data/reports-and-data/lme-closing-prices)
- [Teck Q3 2026原始披露](https://www.teck.com/news/news-releases/2026/teck-reports-unaudited-third-quarter-results-for-2026)
- [CNOOC季度报告页](https://www.cnoocltd.com/english/investorrelations/reports/quarterlyreport/)
- [OPEC+ 10月4日决定](https://www.opec.org/pr-detail/616-4-october-2026.html)
- [CFTC发布日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- [EIA WPSR日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [USDA Weekly Export Sales日程](https://fas.usda.gov/report-release-announcement/weekly-export-sales-300)
- [白银主力夜盘fallback](https://beichenlabs.com/futures/ag)
- [AG2612 00:57准确合约快照](https://www.iweiai.com/hangqing/ag2612)
- [SC2612夜盘fallback](https://www.iweiai.com/hangqing/sc2612)
- [MA701夜盘fallback](https://www.iweiai.com/hangqing/MA701)

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：AG2612反抽失败空、BU2701强曲线回踩多、MA701二次确认多、SC2612反弹失败空；均须09:15后顺序与有效报价。  
C. 今天继续观察：EC2612、CU2612、LC2701、M2701，以及CNOOC Q3、CFTC、PMI和OPEC+。  
D. 今天必须回避或有条件退出：回避追AG/SC低开、追FU交割月极端曲线、追LC急跌及任何未询价期权；若假设已建仓，按各卡止损/逻辑失效/时间退出，不默认实际持仓。

