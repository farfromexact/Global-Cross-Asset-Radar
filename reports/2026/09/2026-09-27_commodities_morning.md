# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-27

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：07:04 BJT；信息截点：07:00。中国9月25—27日休市，最近完整EOD为9月24日；下一实际日盘为9月28日09:00，下一实际夜盘为9月28日21:00（归属9月29日）。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；周末未出现足以改变周一gap框架的新证据，橡胶、航运偏强与能源偏弱均须等09:45确认。**

当前regime为“休市期gap累积＋能源回吐＋橡胶/贵金属相对强”。最接近补证的是EC2611回撤接受多、BR2611回撤接受多、TA701失败回落空；均处于休市，缺周一具体合约报价、当日curve/量仓及可执行期权报价。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并为仪表盘下钻[EOD具体合约](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)与[External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)。

- 统一输入：schema v2，`requested_date=2026-09-24`，9月27日06:42:04生成；这是同一repo main快照下的统一只读层。
- Futures：9月24日五所806合约、77产品last-good；原快照`verified=true`、`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、placeholder=5。9月25日休市刷新仍为0合约/15项错误；该run失败不覆盖已验证last-good。
- Market State：9月27日06:36重算，77产品；价格、量仓、1/3/5/20D与curve仍以9月24日具体合约为截止，`data_fresh=false`是日历沿用而非新增行情。
- Physical：9月24日请求，18/20序列按原生频率可用、SC/LU不可得；模块原始`validation_passed=false/published=false`，basis均C级或缺失，只作context，不计方向或套利确认。
- External：9月27日06:41重新汇总9月25日收盘；17/22目标fresh、5项未映射、0失败，全部`context_only`。WTI 92.43美元/桶、仓库Brent连续合约97.43美元/桶；后者与昨日公开页面代理约104.37存在不可比差异，不构造跨源价差。
- Options：最新正式截面仍为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖0，不能冒充周一报价。
- Contract Metadata：partial；有效合约匹配约73.45%，乘数/tick/margin/limit覆盖约30.15%，Night时段覆盖0。空值不推断。

Night模块原始记录：`trading_date=2026-09-27`、`night_session_date=2026-09-26`、06:29:34生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`。806条请求中592条outside-window、214条query error/unresolved；有效Night合约/产品为0，missing timestamp/price/quote均为0。9月27日为休市日，市场语义是“本次不适用”，不是“应有夜盘缺失”；`previous_valid_snapshot_retained=true`。表中Night仅回看归属9月24日的最后有效连续交易阶段，不作为本期新增或周一当前报价，`night_session_fallback=false`。

## 三、商品仪表盘

EOD均为9月24日；1D/5D按同一具体合约结算收益。Basis/Physical均不具A/B级执行资格。Night为归属9月24日的历史有效阶段；“—”表示制度无Night或正式合约不可比，不等于0。

| 板块 | 合约；EOD收/结；1D/5D | Vol/OI/ΔOI；EOD curve | Basis/Physical | 历史Night收；vs收/vs结；ΔOI；质量/时间 | 07:00海外（9/25收盘） | Options S/P/E | 周一信号 |
|---|---|---|---|---|---|---|---|
| 聚酯 | TA701；6340/6270；+2.08%/-3.51% | 123.78万/109.81万/+13,920；Back 3.66% | C/加工利润缺 | 6298；+2.91%/+2.54%；+14,498；fresh 9/23 23:00 | 油与石脑油周五走弱 | Y/Y/N | 失守6270才研究空 |
| 燃料 | FU2611；4363/4257；+3.43%/-3.34% | 73.34万/17.48万/-1,492；Back 22.67% | C/EIA产品端context | 4253；+3.30%/+3.33%；+8,746；fresh 9/23 23:00 | 原油弱、产品映射分化 | Y/N/N | deep back反对追空 |
| 原油 | SC2611；743.5/724.8；+4.27%/-9.96% | 24.08万/3.58万/-3,759；Back 1.19% | 缺/实体不可得 | 730；+6.09%/+5.02%；+539；fresh 9/24 02:30 | WTI 92.43；Brent 97.43 proxy | Y/N/N | 低开风险，45m确认 |
| 沥青 | BU2611；5256/5056；+1.34%/-7.26% | 128.28万/25.71万/+4,534；Back 10.68% | C/context | 4997；+2.02%/+0.16%；-12,354；fresh 9/23 23:00 | exact映射不足 | Y/Y/N | 双锚分歧大，不追 |
| 橡胶 | BR2611；15680/15375；+3.67%/+2.74% | 24.74万/8.67万/-18,359；Back 0.85% | 缺/库存开工缺 | 15380；+1.45%/+3.71%；-13,827；fresh 9/23 23:00 | 橡胶周五收涨 | Y/N/N | 回撤接受多候选 |
| 橡胶 | RU2701；19600/19425；+1.60%/+2.67% | 40.85万/15.14万/-4,202；Contango 0.38% | 缺/库存开工缺 | 19395；-0.31%/+1.44%；-2,631；fresh 9/23 23:00 | 橡胶偏强 | Y/Y/N | 外强、curve反对 |
| 航运 | EC2611；2800/2747.5；+3.13%/+8.96% | 1.30万/1.94万/+1,458；Back 20.86%；roll | 缺/exact运价缺 | 制度无Night | 综合运价proxy无新周末交易 | N/N/N | 回撤多，先验流动性 |
| 贵金属 | AG2612；15661/15775；-2.53%/+0.69% | 20.82万/24.67万/+10,078；Contango 0.14% | 宏观主导 | 正式合约不可比 | COMEX金4320.3、银64.71 | Y/N/N | 反转需重上16000 |
| 有色 | CU2611；110130/110210；-0.51%/+2.29% | 7.34万/17.86万/+7,415；Back 0.52% | C/context | 110190；-0.13%/-0.53%；+638；fresh 9/24 01:00 | LME铜14625.5 proxy；CNH偏弱 | Y/Y/N | 内外强弱不可直接套算 |
| 油脂 | OI701；10264/10236；+0.90%/+0.24% | 24.57万/29.14万/+14,632；Back 1.79% | 缺/进口利润缺 | 10194；+0.41%/+0.48%；+1,910；fresh 9/23 23:00 | 棕榈4671；豆油68.21 | Y/N/N | 跨品种冲突 |
| 黑色建材 | FG701；914/919；-0.97%/+1.32% | 102.98万/115.69万/-25,634；Back 4.78% | C/仓单仅context | 921；-0.43%/-0.75%；-10,142；fresh 9/23 23:00 | SGX铁矿95.05 proxy | Y/Y/N | 减仓弱，无共振 |
| 新能源 | LC2701；124420/126220；-3.41%/-3.00% | 28.85万/42.94万/-6,390；Back 2.56% | 缺/现货库存闭环缺 | 制度无Night | 锂proxy未映射 | Y/N/N | 弱但减仓，不追空 |
| 软商品 | CJ701；7165/7265；-1.49%/-1.09% | 30.83万/24.90万/+21,804；Contango 2.75% | C/context | 无当前可比Night | ICE糖18.52、棉82.59仅代理 | Y/Y/N | 价跌仓增但实体缺 |

人民币方面，上一可见USD/CNY约6.72，人民币偏弱可温和缓冲进口品外盘跌幅；无exact import parity，不能量化为中国合约涨跌。

## 四、相比上一交易日/今晨真正变化

1. **没有新的中国EOD或Night。** 休市期不存在9月27日EOD，也不存在归属9月27日的新Night；根状态的0合约/15项错误和Night的214项query error保留原始标签，但不使9月24日last-good失效。
2. **External完成同源重采。** 今晨仓库确认9月25日17条日频序列fresh；WTI 92.43与昨日公开代理近似，但Brent仓库连续合约97.43与公开页面约104.37不可比。本期不再沿用104.37做绝对锚，只保留油价周五走弱这一方向证据。
3. **周末事件未给出新增确认。** 截至07:00，未检索到比9月22日“Saudi East-West管线低负荷重启、完全恢复尚需数周”更晚且可独立验证的供给事实；这不是新的周日催化。[Reuters，2026-09-22](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)
4. **排名做机械一致性纠正，而非观点反转。** EC2611分数69高于BR2611的68，因此正式榜按分数降序排列；EC仍因roll、流动性和exact运价缺口不可立即执行。
5. **旧建议状态不变。** `COM-E-BR2611-REVERSAL-20260923`、`COM-E-EC2611-ROLL-20260924`、`COM-E-TA701-HOLIDAY-FADE-20260925`沿用；TA/FU旧多与AG旧空继续停止新增。无成交反馈，不假设用户持仓。

## 五、产业链地图

- **相对最强：航运—橡胶，偏多、置信度中低。** EC EOD价涨仓增且back，但处于roll且缺exact运价；BR国内价强却减仓，海外橡胶支持仅属第4层。两者均不追周一第一跳。
- **相对最弱：原油—石脑油—聚酯成本链，偏空、置信度中。** 周五海外油价走弱；中国9月24日SC/TA价格仍强、FU/BU深back，方向与curve并非全面确认。
- **贵金属反转观察，偏多、置信度低。** 海外金银周五收高，而AG中国EOD价跌仓增；“黄金信用”主题没有新增实际利率、资金流或期权证据。
- **油脂/饲料分化，中性、置信度低。** 棕榈、豆油、豆类代理不同向，高质量basis与进口利润缺失，不能把OI单品信号扩为全链。
- **黑色—新能源偏弱但不具追空赔率。** FG减仓、LC价跌仓减；curve、实体和休市gap均反对线性追空。

## 六、机会排行榜

| 排名 | 候选/idea_id | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 有效支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | EC2611趋势回撤多 / `COM-E-EC2611-ROLL-20260924` | 20/14/14/11/10 | **69** | 1、2 | 存在待验证优势｜部分；roll/exact运价缺｜9/28 09:45等待触发 |
| 2 | BR2611 gap延续多 / `COM-E-BR2611-REVERSAL-20260923` | 19/14/13/10/12 | **68** | 1、4 | 存在待验证优势｜部分；减仓/实体缺｜9/28 09:45等待触发 |
| 3 | TA701失败回落空 / `COM-E-TA701-HOLIDAY-FADE-20260925` | 18/14/13/8/6 | **59** | 4；1/2反对 | 存在待验证优势｜不足｜9/28等待触发 |
| 4 | AG2612海外反转多 / `COM-E-AG2612-REVERSAL-20260925` | 18/13/13/8/7 | **59** | 4 | 证据不足｜不足；中国层反对｜待报价 |
| 5 | FU2611能源回落空 / `COM-E-FU2611-HOLIDAY-FADE-20260925` | 17/14/12/8/7 | **58** | 4 | 证据不足｜不足；deep back反对｜休市观察 |

分项均已复算并遵守支持层封顶；无70+候选。分数是研究排序，不是胜率、期望收益或仓位指令。所有期货最大损失均不由计划止损结构性限定。

## 七、前三名研究卡

### 1. EC2611｜趋势回撤多｜69

- **事实/市场定价：**9月24日收2800、结2747.5，1D +3.13%、5D +8.96%，Vol 13,031、OI 19,393、ΔOI +1,458；near-next back 20.86%，但主力发生roll且历史警告存在。制度无Night，周一09:00才首次补价。
- **分歧与反证：**市场可能低估航线风险延续；最强竞争解释是换月和低流动性夸大价格/curve，且缺exact欧洲线运价与船流。支持层1、2；层3、4、5缺失。
- **最佳表达：**EC2611期货单腿1手研究条件；不是beta-neutral或有限损失结构。期权无ready结构。
- **好/中/坏成交：**09:45后2748—2800承接并重上2800/VWAP；突破2820后回踩2800不破只用半风险；直接高于2900、跌破2700或盘口深度不足则放弃。
- **止损/失效/退出：**45分钟接受2670下方止损；跌破2700且运价/船流不确认则逻辑失效。TP1 2900或+1.5R，TP2 3050或+3R，TP1减半；1—5D无扩张退出。
- **参数与压力：**repo元数据未完整确认multiplier、tick、tick value、margin、limit、last trading day与交割风险；补齐前不可执行，不编一/两板金额。roll计划为确认EC2611流动性后才建立、交割月前退出。
- **催化/最坏情景：**1—7D航线事件与运价；最坏为周一高开回落、流动性消失和roll错配。最大损失不由止损限定。

### 2. BR2611｜回撤接受多｜68

- **事实/双锚：**EOD收15680、结15375，1D +3.67%、5D +2.74%，ΔOI -18,359，back 0.85%。最后有效Night OHLC 15300/15465/15220/15380，vs previous close +1.45%、vs settlement +3.71%，ΔOI -13,827，source timestamp 9月23日23:00；双锚差2.26个百分点，说明日间close/settlement差异大，不能把结算锚涨幅当新增夜盘强势。
- **分歧与反证：**海外橡胶周五偏强可能支撑gap；反证是中国EOD与Night均减仓、实体库存/开工缺、RU contango。支持层1、4；2中性，3/5缺失。
- **最佳表达：**BR2611期货1手研究条件；最大损失非结构限定。
- **好/中/坏成交：**09:45后15380—15600承接并重上15680/VWAP；突破15750回踩不破只用半风险；直接高于16000、跌破15220或海外橡胶转弱则放弃。9:00首跳不追。
- **止损/失效/退出：**45分钟接受15180下方止损；跌破15220、curve转contango且海外橡胶反转则失效。TP1 15950或+1.5R，TP2 16400或+3R；1—5D时间止损。
- **参数与压力：**repo未完整确认multiplier、tick、margin、limit、last trading day及交割参数；补齐前不可执行，不编一/两板压力金额。交割月前退出并在流动性迁移时移仓。
- **催化/最坏情景：**1—5D产区天气、原料与库存；最坏为gap反转、涨跌停和流动性消失。

### 3. TA701｜失败回落空｜59

- **事实/双锚：**EOD收6340、结6270，1D +2.08%、5D -3.51%，ΔOI +13,920，back 3.66%。最后有效Night OHLC 6172/6324/6158/6298，vs previous close +2.91%、vs settlement +2.54%，ΔOI +14,498；该Night属于9月24日历史阶段，不是周一报价。
- **分歧与反证：**周五油价走弱可能令成本重估，但中国EOD价仓和back反对立即做空；加工利润与PX供需缺失。仅第4层支持，按评分纪律封顶59，较上一版机械60下调1分；这是评分纠错，不是新增价格信号。
- **最佳表达：**TA701期货1手研究条件；期权execution-ready=false。
- **好/中/坏成交：**09:45后失守6270，反抽6260—6310失败；若先跌破6158再追为坏成交；重上6350或PX保持强势则放弃。
- **止损/失效/退出：**45分钟接受6350上方止损；外油反弹且PX价仓确认则失效。TP1 6180或+1.5R，TP2 6100或+3R；1—3D无扩张退出。
- **参数与压力：**5吨/手、tick 2元、tick value 10元；按6270与6%静态估算，一板约1,881元/手、两板复合约3,649元。基础margin 7%、最后交易日2027-01-14；周一须复核动态参数与交割风险。
- **催化/最坏情景：**1—3D原油、PX与装置消息；最坏为油价headline反弹、低开后V形反转。能源化工共享gap风险合并计算。

## 八、商品期权专项

最新正式面仍为9月17日，已落后于中国9月24日EOD，更无法代表周一gap后的Delta、moneyness、IV与净成本。

| Underlying/expiry | 历史ATM IV；9/24 RV20 | IV-RV | S/P/E | 研究判断 |
|---|---:|---:|---|---|
| SC2611/10-14 | 65.57% / 58.66% | +6.91vol | Y/N/N | 事件vol历史偏高；当前不可比 |
| FU2611/10-19 | 60.62% / 38.68% | +21.94vol | Y/N/N | 裸买Vega历史成本高 |
| BU2611/10-26 | 44.91% / 32.83% | +12.08vol | Y/Y/N | 底层已偏离旧面 |
| TA701/12-11 | 31.87% / 24.93% | +6.94vol | Y/Y/N | 净支出与Delta须重算 |
| AG2612/11-24 | 44.14% / 31.85% | +12.29vol | Y/N/N | 历史skew异常，不外推 |

当前没有可证明优于裸期货的期权结构。周一取得实时双边报价后，才比较EC/BR/AG有限净支出call spread与TA/FU put spread；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点和行权交割全部重算。`dealer_gamma_direction_known=false`，不推断做市商净Gamma。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

今日休市；下一实际日盘为9月28日09:00。三层严格区分：①9月24日中国EOD；②9月27日无应发生Night；③海外最新为9月25日收盘，周日没有新交易。

| 品种 | Previous China EOD | Current Trading Day Night | 07:00 Overseas / 周一预期 | 是否追价 | 等待 | 开盘确认 |
|---|---|---|---|---|---:|---|
| SC/FU/LU/BU | EOD强、curve分化 | 休市不适用 | 油价走弱；偏低开 | 否 | 45m | SC724.8/743.5、FU4257/4363、near-next |
| TA/PX/PF/PR | EOD反弹，TA/PX价仓偏强 | 休市不适用 | 成本回落；偏低开 | 否 | 45m | TA6270/6340、PX breadth与加工利润 |
| BR/RU/NR | EOD强但BR/RU减仓 | 休市不适用 | 橡胶偏强；高开风险 | 否 | 45m | BR15375/15680、RU curve |
| AG/AU | AG EOD弱 | 休市不适用 | 金银周五偏强；高开反转风险 | 否 | 45m | AG15775/16000、美元/实际利率 |
| CU/AL/ZN/NI | 中国分化 | 休市不适用 | LME proxy分化、CNH偏弱 | 否 | 45m | exact LME、USD/CNY、curve |
| OI/M/RM/Y/P | 国内油脂偏强 | 休市不适用 | 棕榈/豆油映射冲突 | 否 | 45m | DCE量仓、高质basis、进口利润 |
| EC | EOD价仓强、roll | 制度无Night | 周末无新运价交易 | 否 | 45m | 2747.5/2800、流动性、exact运价 |
| FG/JM/RB | EOD偏弱或分化 | 休市不适用 | SGX铁矿仅proxy | 否 | 45m | curve、仓单与钢材利润 |
| LC/SI/PS | LC弱但减仓 | 制度无Night | 海外映射不足 | 否 | 45m | LC126220、现货库存响应 |

External move与China Night的信息弹性本期无法测量，因为周五以来没有合法中国Night。所有品种都不值得交易周一09:00第一跳；最早有效验证窗口为09:45。

## 十、未来24小时与7天事件

- 9月27日：中国商品休市，无日盘或夜盘；周末未经独立确认的地缘、管线或船流消息只作gap压力情景。
- 9月28日09:00：中国商品恢复日盘；先等45分钟，检查价格接受、near-next curve、量仓与人民币共同确认。
- 9月28日21:00：下一实际Night，归属9月29日；只在日盘完成后重设条件。
- 9月30日22:30：EIA周报常规窗口；能源仓提前降低Delta，期权仅限取得实时净支出的有限凸性结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 未来7日：北美收割天气、马棕出口、橡胶产区天气、Hormuz/Yanbu船流、矿山与炼厂突发、EC运价及SC/LU/FU移仓风险。
- CFTC本周发布仅反映截至周二的滞后持仓；本期未逐品种核验，不计拥挤确认。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月30日晚无Night、10月1—7日国庆休市；保证金/限幅只按交易所正式通知更新。[INE假期通知](https://www.ine.cn/publicnotice/notice/202609/t20260921_833506.html)

## 十一、覆盖、风险与归档核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足/最值得跟踪异常 | 不适用或流动性不足 |
|---|---:|---:|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/9 last-good | FG减仓弱、JM实体/利润缺；无三层共振 | 休市无新EOD/Night |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | AG内外反转待确认；A/B basis、实时利率缺 | 休市；部分低流动合约不入榜 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 22/22 | EC/BR入榜；SC/LU实体、加工利润、exact parity缺 | DCE Night/参数历史缺口 |
| 新能源/新材料 | LC/SI/PS及GFEX扩展 | 全部repo可得产品 | LC弱但减仓，现货库存闭环缺 | 制度无Night者不强求 |
| 农产品油脂畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 19/19 | OI与海外油脂冲突；CJ价跌仓增但实体缺 | 低流动/历史不足者保留扫描 |
| 航运软商品 | EC及棉花/白糖/苹果/红枣/花生 | 全部覆盖 | EC roll/exact运价缺；软商品无多层异常 | EC制度无Night |

- 应覆盖：强制63代码及动态扩展后77产品；商品期权64产品。
- 实际分析：9月24日五所806合约、77产品last-good全量复核；17个海外日频序列完成同源刷新；方向、curve、跨期、跨品种、跨市场proxy、中性、波动率/偏度和事件凸性均扫描。
- 数据不足：19个期权产品、9月17日后正式surface、全部实时bid/ask、A/B级basis、exact import parity、SC/LU实体、加工利润、橡胶库存/开工、多数动态参数与周一实际gap。
- 不适用/流动性不足：9月25—27日中国EOD/Night；JR、PM、RI、WH、ZC等placeholder或极低流动记录排除异常榜但保留覆盖；EC、LC等制度无Night。
- 风险预算：休市预案不建仓；周一条件满足后单笔试仓0.10%—0.15% NAV，确认后最高0.50%；同因子gap风险合计≤0.40%，单一主题总风险≤2.5%。压力测试一/两板、相关性破裂、流动性消失、gap、保证金上调、IV跳变、交割挤压与人民币急变。
- 固定六路径从main回读验证后才记`archive_status=success`；CI独立事后校验，不等待。

A. 今天没有应立即建立的新仓位。  
B. 今天没有可挂的中国商品条件单；仅预设9月28日09:45后的研究条件：EC2611守住2748—2800并重上2800，BR2611守住15380—15600并重上15680，TA701失守6270且反抽失败。  
C. 今天应继续观察的机会：周末能源设施与船流、橡胶和金银相对强势、EC运价、棕榈油弱势及人民币对周一gap的缓冲。  
D. 今天必须避免或退出的交易：任何中国商品新单、预判周一第一跳、把休市写成行情缺失、沿用旧TA/FU多或AG空条件、把旧期权面或海外proxy称可执行套利。
