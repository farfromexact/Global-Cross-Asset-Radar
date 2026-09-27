# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-28

`prompt_version=radar_2026-09-06_coverage_v1`  
`data_protocol_version=china_commodities_v2`  
实际生成：07:07 BJT；信息截点：07:00。最近完整中国EOD为9月24日；9月25—27日休市，周日晚无连续交易。下一实际交易窗口为今日09:00。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；节后首日09:00将首次吸收海外累积信息，EC、BR与TA只在09:45后按实盘接受度研究。**

当前regime：长假gap首次释放、海外能源代理与人民币信号互相抵消、航运/橡胶相对强但证据不完整。最接近补证的是EC2611回撤接受多、BR2611回撤接受多、TA701失败回落空；均缺今日具体合约价格、有效期权报价和完整动态参数。

## 二、数据质量与覆盖

本期第一层读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。

- 统一输入：schema v2，`requested_date=2026-09-24`，9月27日19:05生成；这是截至今晨最新应得的完整中国EOD，不因周末而失效。
- Futures：last-good为9月24日，五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；5个placeholder排除异常榜。
- Market State：9月27日19:00重算77产品，但收益、量仓和curve截止9月24日；同合约计算，roll记录不拼接连续主力。
- Physical：18/20序列按原生频率可用，SC/LU不可得；原始模块`validation_passed=false/published=false`，basis均C级或缺失，只作context。
- External：9月27日19:04汇总9月25日海外收盘，17/22可用、5项未映射，全部`context_only`；今晨公开页面代理另列。
- Options：最新正式截面仍为9月17日，16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、**0个execution-ready**，bid/ask覆盖0。
- Metadata：partial；有效合约匹配约73.45%，动态margin/limit等参数覆盖约30.15%，Night时段覆盖不足。

Night原始记录：`trading_date=2026-09-27`、`night_session_date=2026-09-26`、9月27日08:16生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`，有效合约/产品均为0。806条请求中592条outside-window、214条query error/unresolved，missing timestamp/price/quote均为0。9月27日是休市日，本次0合约在市场语义上“不适用”，不是漏掉应有夜盘；9月24日历史Night保留作旧价格发现复盘，不能冒充今晨行情。`night_session_fallback=false`。

## 三、商品仪表盘

EOD均为9月24日；Night为归属9月24日的最后有效连续交易阶段，仅作历史背景。“今晨海外”是公开CFD/连续合约代理，未与中国合约做进口平价对齐。

| 板块 | 合约；EOD收/结；1D/5D | Vol/OI/ΔOI；EOD curve | Basis/Physical | 历史Night收；vs收/vs结；ΔOI | 07:00海外新增；Options S/P/E | 今日信号 |
|---|---|---|---|---|---|---|
| 航运 | EC2611；2800/2747.5；+3.13%/+8.96% | 1.30万/1.94万/+1,458；Back 20.86%；roll | 缺/exact运价缺 | 制度无Night | 无可核实周末运价成交；N/N/N | 09:45回撤接受多 |
| 橡胶 | BR2611；15680/15375；+3.67%/+2.74% | 24.74万/8.67万/-18,359；Back 0.85% | 缺/库存开工缺 | 15380；+1.45%/+3.71%；-13,827 | 早盘exact橡胶未核实；Y/N/N | 高开不追，等45m |
| 聚酯 | TA701；6340/6270；+2.08%/-3.51% | 123.78万/109.81万/+13,920；Back 3.66% | C/加工利润缺 | 6298；+2.91%/+2.54%；+14,498 | Brent公开CFD偏强但绝对价冲突；Y/Y/N | 失守6270才研究空 |
| 燃料 | FU2611；4363/4257；+3.43%/-3.34% | 73.34万/17.48万/-1,492；Back 22.67% | C/EIA产品context | 4253；+3.30%/+3.33%；+8,746 | 油价代理反弹；Y/N/N | deep back反对追空 |
| 原油 | SC2611；743.5/724.8；+4.27%/-9.96% | 24.08万/3.58万/-3,759；Back 1.19% | 缺/实体不可得 | 730；+6.09%/+5.02%；+539 | Brent CFD页面106.18、+1.78%，仅fallback；Y/N/N | 45m核验gap与curve |
| 沥青 | BU2611；5256/5056；+1.34%/-7.26% | 128.28万/25.71万/+4,534；Back 10.68% | C/context | 4997；+2.02%/+0.16%；-12,354 | exact映射不足；Y/Y/N | 双锚分歧，不追 |
| 橡胶 | RU2701；19600/19425；+1.60%/+2.67% | 40.85万/15.14万/-4,202；Contango 0.38% | 缺/库存开工缺 | 19395；-0.31%/+1.44%；-2,631 | exact外盘未核实；Y/Y/N | curve反对强追 |
| 贵金属 | AG2612；15661/15775；-2.53%/+0.69% | 20.82万/24.67万/+10,078；Contango 0.14% | 宏观主导 | 正式合约不可比 | 早盘金银exact报价未核实；Y/N/N | 重上16000才看反转 |
| 有色 | CU2611；110130/110210；-0.51%/+2.29% | 7.34万/17.86万/+7,415；Back 0.52% | C/context | 110190；-0.13%/-0.53%；+638 | DXY 101.1248、USD/CNY 6.7238 proxy；Y/Y/N | 人民币弱，等LME确认 |
| 油脂 | OI701；10264/10236；+0.90%/+0.24% | 24.57万/29.14万/+14,632；Back 1.79% | 缺/进口利润缺 | 10194；+0.41%/+0.48%；+1,910 | 农产品早盘exact未核实；Y/N/N | 跨品种冲突 |
| 黑色 | FG701；914/919；-0.97%/+1.32% | 102.98万/115.69万/-25,634；Back 4.78% | C/仓单context | 921；-0.43%/-0.75%；-10,142 | SGX exact早盘未核实；Y/Y/N | 减仓弱，无共振 |
| 新能源 | LC2701；124420/126220；-3.41%/-3.00% | 28.85万/42.94万/-6,390；Back 2.56% | 缺/库存闭环缺 | 制度无Night | 海外映射不足；Y/N/N | 弱但减仓，不追空 |
| 软商品 | CJ701；7165/7265；-1.49%/-1.09% | 30.83万/24.90万/+21,804；Contango 2.75% | C/context | 无可比Night | 糖棉早盘exact未核实；Y/Y/N | 价跌仓增、实体缺 |

公开页面截至07:00显示Brent CFD约106.18美元/桶、页面日变动+1.78%；但仓库9月25日连续合约为97.43，跨源合约和时点不可比，故只把“今晨代理偏强”作为反对能源空头的背景，不计算跨源收益或套利。[Trading Economics Brent](https://tradingeconomics.com/commodity/brent-crude-oil)

公开页面最后可见DXY约101.1248、+0.15%，USD/CNY约6.7238、+0.03%；人民币温和偏弱对进口品有抬升方向，但无exact import parity，不能量化为国内涨幅。[DXY](https://tradingeconomics.com/united-states/currency)｜[USD/CNY](https://tradingeconomics.com/china/currency)

## 四、相比上一交易日/今晨真正变化

1. **从休市观察转入今日可验证窗口。** 9月24日last-good不变，但今天09:00是节后第一次国内定价；此前所有周末条件都不能当已触发，最早有效判断推迟至09:45。
2. **不存在归属9月28日的周日Night。** 因而Night没有强化、否定或重复EOD，双收益锚和Night curve都没有新观测；不能把0合约写成零涨跌。
3. **海外能源代理由周五弱转为今晨页面偏强，但绝对价不可比。** 该变化反对直接做空SC/FU/TA，却因合约映射冲突不能成为多头确认。
4. **美元与人民币均略强。** DXY与USD/CNY proxy同升，对人民币进口品方向相互抵消一部分外盘跌幅；没有模型，不编贡献权重。
5. **旧建议台账保持稳定。** `COM-E-EC2611-ROLL-20260924`、`COM-E-BR2611-REVERSAL-20260923`与`COM-E-TA701-HOLIDAY-FADE-20260925`继续等待触发；无成交反馈，不假设用户持仓。TA/FU旧多、AG旧空仍不恢复。

## 五、产业链地图

- **相对最强：航运—橡胶，偏多、置信度中低。** EC价涨仓增与back支持，BR价格与海外旧收盘支持；roll、减仓、实体和今晨exact报价缺失反对追价。
- **最不稳定：原油—燃料—聚酯，中性偏事件驱动、置信度低。** 中国9月24日强势与周五海外弱势冲突，今晨Brent CFD又反弹；FU deep back与SC curve收窄进一步分化。09:00第一跳大概率含补价噪音。
- **贵金属反转观察，偏多、置信度低。** 中国AG价跌仓增，海外金银旧收盘偏强；黄金信用主题没有新增实际利率、资金流或期权证据。
- **油脂/饲料分化，中性、置信度低。** OI量仓偏强，但棕榈、豆油、豆类映射不一致，高质量basis与进口利润缺失。
- **黑色—新能源偏弱但不具追空赔率。** FG和LC均有减仓线索，curve、实体与长假gap不支持裸空。

## 六、机会排行榜

| 排名 | 候选/idea_id | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 有效支持层 | 研究判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | EC2611回撤多 / `COM-E-EC2611-ROLL-20260924` | 20/14/14/11/10 | **69** | 1、2 | 存在待验证优势｜部分｜09:45等待触发 |
| 2 | BR2611回撤多 / `COM-E-BR2611-REVERSAL-20260923` | 19/14/13/10/12 | **68** | 1、4 | 存在待验证优势｜部分｜09:45等待触发 |
| 3 | TA701失败回落空 / `COM-E-TA701-HOLIDAY-FADE-20260925` | 18/14/13/8/6 | **59** | 4；1/2反对 | 存在待验证优势｜不足｜09:45等待触发 |
| 4 | AG2612反转多 / `COM-E-AG2612-REVERSAL-20260925` | 18/13/13/8/7 | **59** | 4 | 证据不足｜不足｜待报价 |
| 5 | FU2611回落空 / `COM-E-FU2611-HOLIDAY-FADE-20260925` | 17/13/12/8/7 | **57** | 4 | 证据不足｜不足；deep back与今晨油价代理反对｜等待触发 |

分项均已复算并遵守支持层封顶；无70+候选。分数是研究排序，不是胜率、预期收益或仓位指令。所有期货最大损失均不由计划止损结构性限定。

## 七、前三名研究卡

### 1. EC2611｜回撤接受多｜69

- **事实/市场定价：**9月24日收2800、结2747.5，1D +3.13%、5D +8.96%，Vol 13,031、OI 19,393、ΔOI +1,458，back 20.86%；但发生roll且无Night。
- **分歧/反证：**市场或低估航线风险延续；最强竞争解释是换月和低流动性夸大价格/curve，且缺exact欧洲线运价与船流。支持层1、2；层3—5缺失。
- **最佳表达：**EC2611期货1手研究条件；不是beta-neutral或有限损失结构。
- **好/中/坏成交：**09:45后2748—2800承接并重上2800/VWAP；突破2820后回踩2800不破只用半风险；直接高于2900、跌破2700或盘口深度不足则放弃。
- **止损/失效/退出：**45分钟接受2670下方止损；跌破2700且运价/船流不确认则失效。TP1 2900或+1.5R，TP2 3050或+3R；TP1减半，1—5D无扩张退出。
- **参数/压力：**repo未完整确认multiplier、tick、tick value、margin、limit、last trading day和交割风险；补齐前不可执行，不编一/两板损失。确认EC2611流动性后才建立，交割月前退出。
- **催化/最坏情景：**1—7D航线事件与运价；最坏为高开回落、流动性消失和roll错配。

### 2. BR2611｜回撤接受多｜68

- **事实/双锚：**EOD收15680、结15375，1D +3.67%、5D +2.74%，ΔOI -18,359，back 0.85%。最后有效Night OHLC 15300/15465/15220/15380，vs close +1.45%、vs settlement +3.71%，ΔOI -13,827，时间9月23日23:00；双锚差2.26个百分点，不能把相对结算涨幅当新增夜盘强势。
- **分歧/反证：**海外橡胶旧收盘可能支撑gap；反证是中国EOD与Night均减仓、实体库存/开工缺、RU contango。支持层1、4；2中性，3/5缺失。
- **最佳表达：**BR2611期货1手研究条件；最大损失非结构限定。
- **好/中/坏成交：**09:45后15380—15600承接并重上15680/VWAP；突破15750回踩不破半风险；直接高于16000、跌破15220或外盘转弱则放弃。09:00首跳不追。
- **止损/失效/退出：**45分钟接受15180下方止损；跌破15220、curve转contango且外盘反转则失效。TP1 15950或+1.5R，TP2 16400或+3R；1—5D时间止损。
- **参数/压力：**repo未完整确认multiplier、tick、margin、limit、last trading day及交割参数；补齐前不可执行，不编一/两板金额。交割月前退出。
- **催化/最坏情景：**1—5D产区天气、原料与库存；最坏为gap反转、涨跌停和流动性消失。

### 3. TA701｜失败回落空｜59

- **事实/双锚：**EOD收6340、结6270，1D +2.08%、5D -3.51%，ΔOI +13,920，back 3.66%。最后有效Night OHLC 6172/6324/6158/6298，vs close +2.91%、vs settlement +2.54%，ΔOI +14,498；这是9月24日历史阶段。
- **分歧/反证：**周五油价走弱可能令成本重估，但中国EOD价仓和back、今晨Brent CFD反弹均反对立即做空；加工利润与PX供需缺失。仅第4层支持，封顶59。
- **最佳表达：**TA701期货1手研究条件；期权execution-ready=false。
- **好/中/坏成交：**09:45后失守6270，反抽6260—6310失败；若先跌破6158再追为坏成交；重上6350或PX保持强势则放弃。
- **止损/失效/退出：**45分钟接受6350上方止损；外油与PX价仓同步转强则失效。TP1 6180或+1.5R，TP2 6100或+3R；1—3D无扩张退出。
- **参数/压力：**5吨/手、tick 2元、tick value 10元；按6270与6%静态估算，一板约1,881元/手、两板复合约3,649元。基础margin 7%、最后交易日2027-01-14；开盘前须复核动态参数。
- **催化/最坏情景：**1—3D原油、PX与装置消息；最坏为headline反弹、低开后V形反转。

## 八、商品期权专项

最新正式面为9月17日，已落后于9月24日EOD，更不能代表节后gap后的Delta、moneyness、IV或净成本。

| Underlying/expiry | 历史ATM IV；9/24 RV20 | IV-RV | S/P/E | 判断 |
|---|---:|---:|---|---|
| SC2611/10-14 | 65.57% / 58.66% | +6.91vol | Y/N/N | 历史事件vol偏高，当前不可比 |
| FU2611/10-19 | 60.62% / 38.68% | +21.94vol | Y/N/N | 裸买Vega历史成本高 |
| BU2611/10-26 | 44.91% / 32.83% | +12.08vol | Y/Y/N | 底层已偏离旧面 |
| TA701/12-11 | 31.87% / 24.93% | +6.94vol | Y/Y/N | 净支出与Delta须重算 |
| AG2612/11-24 | 44.14% / 31.85% | +12.29vol | Y/N/N | 历史skew异常，不外推 |

当前没有可证明优于裸期货的期权结构。今日取得实时双边报价后，才比较EC/BR/AG有限净支出call spread与TA/FU put spread；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点和行权交割全部重算。`dealer_gamma_direction_known=false`。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、9:00开盘风险地图

严格三层：①9月24日中国EOD；②9月28日制度上无周日Night；③今晨海外公开代理。09:00是国内首次吸收累积信息，所有预期都必须以交易所具体合约验证。

| 品种 | Previous EOD | Current Night | 07:00海外/预期开盘 | 追价 | 等待 | 开盘确认 |
|---|---|---|---|---|---:|---|
| SC/FU/LU/BU | EOD强、curve分化 | 不适用 | 油价代理反弹，gap方向不确定 | 否 | 45m | SC724.8/743.5、FU4257/4363、near-next |
| TA/PX/PF/PR | EOD反弹、TA/PX价仓偏强 | 不适用 | 成本信号冲突，平/高开均可能 | 否 | 45m | TA6270/6340、PX breadth、加工利润 |
| BR/RU/NR | EOD强但BR/RU减仓 | 不适用 | exact外盘缺，高开风险未确认 | 否 | 45m | BR15375/15680、RU curve |
| AG/AU | AG EOD弱 | 不适用 | 金银exact早盘缺 | 否 | 45m | AG15775/16000、美元/实际利率 |
| CU/AL/ZN/NI | 中国分化 | 不适用 | DXY/CNH均偏强，方向冲突 | 否 | 45m | exact LME、USD/CNY、curve |
| OI/M/RM/Y/P | 国内油脂偏强 | 不适用 | 农产品早盘映射不足 | 否 | 45m | DCE量仓、A/B basis、进口利润 |
| EC | EOD价仓强、roll | 制度无Night | 周末无新运价成交 | 否 | 45m | 2747.5/2800、流动性、exact运价 |
| FG/JM/RB | EOD偏弱或分化 | 不适用 | SGX exact早盘缺 | 否 | 45m | curve、仓单、钢材利润 |
| LC/SI/PS | LC弱但减仓 | 制度无Night | 海外映射不足 | 否 | 45m | LC126220、现货库存响应 |

External move与China Night的信息弹性本期无法测量，因为不存在合法周日Night。所有品种都不值得交易09:00第一跳；最早有效验证窗口为09:45。

## 十、未来24小时与7天事件

- 今日09:00：中国商品恢复日盘；先等45分钟，检查价格接受、near-next curve、量仓和人民币共同确认。
- 今日21:00：下一实际Night，归属9月29日；只在日盘完成后重设条件。
- 9月30日22:30：EIA周报常规窗口；能源仓提前降低Delta，期权仅限取得实时净支出的有限凸性结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 未来7日：北美收割天气、马棕出口、橡胶产区天气、Hormuz/Yanbu船流、矿山与炼厂突发、EC运价及SC/LU/FU移仓风险。
- CFTC数据只作截至周二的滞后拥挤背景，本期未逐品种核验，不计确认层。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月30日晚无Night、10月1—7日国庆休市；保证金/限幅只按交易所正式通知更新。[INE假期通知](https://www.ine.cn/publicnotice/notice/202609/t20260921_833506.html)
- Saudi East-West管线低负荷重启、完全恢复仍需数周是9月22日存量事实，不冒充周末新增催化。[Reuters](https://www.reuters.com/business/energy/saudi-arabia-restarts-east-west-oil-pipeline-resume-exports-yanbu-sources-say-2026-09-22/)

## 十一、覆盖、风险与归档核对

| 板块 | 应覆盖 | 实际取数且已分析 | 数据不足/未入榜异常 | 不适用或流动性不足 |
|---|---:|---:|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM | 9/9 last-good | FG减仓弱、JM实体/利润缺；无三层共振 | 周日无Night |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG | 12/12 | AG内外反转待确认；A/B basis与实时利率缺 | 部分低流动合约不入榜 |
| 能源炼化化工 | SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP | 22/22 | BR/TA入榜；SC/LU实体、加工利润、exact parity缺 | DCE Night/参数历史缺口 |
| 新能源/新材料 | LC/SI/PS及GFEX扩展 | 全部repo可得产品 | LC弱但减仓，现货库存闭环缺 | 制度无Night者不强求 |
| 农产品油脂畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK | 19/19 | OI与外盘映射冲突；CJ价跌仓增但实体缺 | 低流动/历史不足保留扫描 |
| 航运软商品 | EC及棉花/白糖/苹果/红枣/花生 | 全部覆盖 | EC入榜但roll/exact运价缺；软商品无多层异常 | EC制度无Night |

- 应覆盖：强制63代码及动态扩展后77产品；商品期权64产品。
- 实际分析：9月24日五所806合约、77产品last-good全量复核；17个海外日频序列及今晨公开代理分层使用；方向、curve、跨期、跨品种、跨市场proxy、中性、波动率/偏度和事件凸性均扫描。
- 数据不足：今日开盘价格与curve、19个期权产品、9月17日后正式surface、全部实时bid/ask、A/B级basis、exact import parity、SC/LU实体、加工利润、橡胶库存/开工、多数动态参数。
- 不适用/流动性不足：周日中国Night；JR、PM、RI、WH、ZC等placeholder或极低流动记录排除异常榜但保留覆盖；EC、LC等制度无Night。
- 风险预算：条件满足后单笔试仓0.10%—0.15% NAV，确认后最高0.50%；同因子gap风险合计≤0.40%，单一主题总风险≤2.5%。压力测试一/两板、相关性破裂、流动性消失、gap、保证金上调、IV跳变、交割挤压和人民币急变。
- 六路径从main回读验证后才记`archive_status=success`；CI独立事后校验，不等待。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：09:45后，EC2611仅在2748—2800承接并重上2800/VWAP时研究试多；BR2611仅在15380—15600承接并重上15680时研究试多；TA701仅在失守6270且反抽6260—6310失败时研究试空。  
C. 今天应继续观察的机会：SC/FU/TA对海外油价代理反弹的弹性、AG是否重上16000、OI与海外油脂冲突、EC换月流动性和人民币对进口品gap的缓冲。  
D. 今天必须避免或退出的交易：追09:00第一跳、把周日无Night写成数据缺失、用跨源Brent绝对价构造套利、恢复旧TA/FU多或AG空、以及在execution-ready=false时臆测期权成本。
