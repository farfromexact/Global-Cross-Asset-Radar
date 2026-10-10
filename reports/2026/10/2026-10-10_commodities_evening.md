# 全球商品期货期权高风险机会雷达（晚间版）

- 报告日期：2026-10-10
- 生成/信息截点：2026-10-10 19:48 / 19:45（北京时间）
- prompt_version：`radar_2026-09-06_coverage_v1`
- data_protocol_version：`china_commodities_v2`
- 市场日历：周六，中国商品休市；最近完整EOD为2026-10-09，下一日盘为2026-10-12 09:00，下一夜盘为2026-10-12 21:00且归属2026-10-13交易日。

## 一、今晚一句话结论

> **截至本报告时点，无可立即执行的合格新交易；周末无国内新行情，周一仅条件验证AG、MA、RU，能源不追飓风溢价。**

已分析但优势不足：EC抄底、SN续空、SC单边空、LC趋势追空。  
研究机会存在、等待条件/报价：AG2612反转、MA701回踩、RU2701/NR2612曲线修复、JM2701延续、C2611 WASDE后重定价。  
数据不足、暂时无法判断：周五夜盘exact-contract、全市场期权bid/ask、DCE期权、SC/LU实体、前三卡部分合约参数。

## 二、数据质量与覆盖

| 模块 | 原生/观测日期 | 状态与本期用途 |
|---|---|---|
| Futures | 2026-10-09；生成2026-10-09 19:00 | 806合约；五所齐全；source-date match 100%；full_market_ready=true；critical errors=0；周六沿用最新应得last-good |
| Market State | EOD 2026-10-09；容器2026-10-10 19:02 | 1/3/5/20D、RV20、OI、near-next curve可用；没有周六新行情 |
| Physical | 2026-10-09 latest-good | 18/20；SC/LU不可得；C级/context-only，不计方向层 |
| External | 源日期2026-10-09；容器2026-10-10 19:07 | 17/22；容器刷新但周末无新价格发现；只作context |
| Options | 交易日2026-10-09 | 14,074记录、185 series；surface 181、positioning 41、execution 0；研究可用、执行不可用 |
| Night Session | 旧快照trading_date=2026-10-08 | data_fresh=false、validation_passed=false、published=false、coverage_complete=false；0合约，outside-window 592，query/unresolved 214；与本报告所需周五夜盘无关 |
| Metadata | 2026-10-09 | 覆盖48合约，部分参数缺失；缺失项不猜测 |

实际读取：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`。统一输入schema v2，requested_date=2026-10-09，generated_at=2026-10-10 19:08:23。  
读取状态：report_input=ok；root status=ok；radar=ok；Night status=stale/invalid；无工具截断冒充源为空。周五21:00开始的夜盘本应归属2026-10-12交易日，但repo exact-contract缺失；晨报采用的媒体主力摘要仅保留为历史背景，不能计算return_vs_close、day_follow_through或夜盘curve。周六没有应发生的中国夜盘，故不要求生成10月10日自然日行情。

## 三、商品仪表盘（全市场扫描后的12项展示子集）

“1D/5D”为同合约可比指标；curve为near-next，不是现货基差。basis均为C/context-only。周末海外增量均为“无交易”。

| 板块 | 品种/合约 | EOD close/settle | 1D/5D | Volume / OI / ΔOI | Curve | Physical/Basis | 周五夜盘 | 周末海外 | Options | 周一信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| 贵金属 | AG2612 | 14717/14515 | +0.88%/-7.99% | 303600/290434/-4332 | +0.54% | context/C | exact缺失；媒体仅主力摘要 | 金4194.36、银60.77为周五收盘 | S✓ P✗ E✗ | 09:30后14650守住再多 |
| 化工 | MA701 | 3338/3321 | +6.04%/+14.83% | 1493099/761175/+70427 | +16.08% | context/C | exact缺失；媒体主力约+2.99%相对结算 | 无新增 | S✓ P✓ E✗ | 等45分钟，严禁追高 |
| 橡胶 | RU2701 | 20645/20220 | +2.89%/— | —/—/+17339 | -3.86% | context/C | exact缺失；媒体主力>3% | 无新增 | S✓ P✓ E✗ | contango收窄再多 |
| 橡胶 | NR2612 | —/— | +0.09%/+3.16% | —/—/+7200 | -2.16% | context/C | exact缺失；媒体主力>4% | 无新增 | S✓ P✗ E✗ | 只作RU确认 |
| 黑色 | JM2701 | 1539.5/1517.5 | +4.30%/— | —/415009/+10394 | +3.48% | context/C | exact缺失；媒体主力偏强 | 无新增 | DCE chain缺失 | 等30分钟 |
| 有色 | SN2611 | 391410/391170 | -4.23%/— | 134989/34969/+3724 | +0.50% | context/C | exact缺失 | LME锡周五反弹约2.9% | S✓ P✗ E✗ | 旧空头失效 |
| 能源 | SC2611 | 734.1/741.3 | -0.45%/— | —/—/-3400 | +3.19% | SC缺失/C | exact缺失 | 飓风已登陆；复产速度待定 | S✓ P✗ E✗ | 不追多、不恢复激进空 |
| 橡胶 | BR2612 | 16710/16370 | +2.77%/— | —/—/+3839 | +2.27% | context/C | exact缺失 | 无新增 | S✓ P✗ E✗ | 只观察 |
| 谷物 | C2611 | —/— | -0.42%/— | —/—/-48586 | -1.38% | context/C | exact缺失；媒体方向与WASDE冲突 | CBOT周五已收盘 | DCE chain缺失 | 等45分钟 |
| 饲料 | M2701 | —/— | +0.03%/— | —/—/+49030 | -1.00% | context/C | exact缺失 | CBOT周五已收盘 | DCE chain缺失 | 等45分钟 |
| 新能源 | LC2701 | 117000/118740 | -3.74%/— | —/—/+11960 | +1.22% | context/C | 制度上无夜盘 | 无新增 | S✓ P✗ E✗ | 日盘等45分钟 |
| 航运 | EC2611 | 2700/2749 | -5.05%/— | —/—/-1776 | -22.48% | context/C | 制度上无夜盘 | 无新增 | S✓ P✗ E✗ | 不抄底 |

S/P/E分别为surface/positioning/execution readiness。Night双收益锚、Night ΔOI、source timestamp均因exact-contract缺失而不能填写；这限制夜盘路径判断，不取消独立的EOD研究。

## 四、相比上一期真正变化

1. **飓风事件从“即将登陆”转为“已登陆、等待损害评估”。** 已关闭的美国海湾原油产量约150万桶/日，但若基础设施未受损，复产可较快；这使SC旧空头仍需防事件风险，也使新增追多周末风险溢价的赔率下降。[Reuters](https://www.reuters.com/business/energy/us-gulf-producers-shut-more-oil-gas-isaias-nears-landfall-2026-10-09/)；[AP](https://apnews.com/article/65ac97bf16477d89ec6f847b09ccb6fc)
2. **周末没有新价格发现。** 10月9日EOD、周五海外收盘、10月9日期权截面仍是最新应得数据；External容器19:07刷新不等于价格更新。
3. **AG、MA、RU排序不变。** 没有新的curve、OI、实体或期权证据，分数维持71/70/69；执行状态仍是休市/等待触发。
4. **能源双边机会进一步收窄。** SC空头不恢复，原油多头也不追；周一观察“海外复产证据—内盘gap—近月curve”三者是否一致。
5. **旧SN空头继续撤销。** 中国EOD下跌与LME周五反弹冲突未被新数据化解；不能把价跌仓增写成已知“新空”。

## 五、产业链地图

| 产业链 | 判断 | 价格/curve/库存 | 海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 甲醇—烯烃 | 最强但过热 | MA 1D约+6%、5D约+14.8%，OI+70427，backwardation约16.08%；实体仅context | MA IV45.66% vs RV35.68%，执行报价缺失 | exact Night、现货高质量基差 | 中高 |
| 贵金属 | 海外确认中国日盘反转 | AG近月略backwardation；库存/信用归因不足 | 金/银周五上涨；AG IV36.39% vs RV31.44% | 周一外盘、exact Night、参数 | 中 |
| 天然橡胶—轮胎 | 价格强、curve反对 | RU/NR涨，仍contango；库存仅context | RU IV27.0% vs RV21.93% | SICOM对齐、参数、Night | 中 |
| 黑色—焦化 | JM最强，钢材确认不足 | JM价涨仓增线索、curve正；实体层不完整 | 无周末海外新增；DCE期权缺失 | 焦煤现货/库存、期权 | 中 |
| 谷物—饲料 | WASDE偏空、国内接受度未知 | C价跌仓减，M近乎平；curve偏contango | USDA上调美国玉米结转，周五夜盘媒体方向冲突 | exact Night、DCE期权 | 中低 |

最弱链条为航运/新能源：EC大跌与深度负near-next、LC价跌仓增均显示压力，但缺现货/运价或电池产业高质量确认，追空赔率不足。油品受飓风与复产两端拉扯，不列方向榜。

## 六、机会排行榜

分数仅用于研究排序，不是胜率、收益或仓位指令；五分项依次为逻辑/赔率凸性/催化/价格曲线波动率/拥挤技术。

| 排名 | idea_id | 方向/周期 | 分项=总分 | 支持层 | 研究判断/证据 | 执行 |
|---|---|---|---:|---:|---|---|
| 1 | COM-E-AG2612-DAY-REVERSAL-LONG-20261009 | 条件多，1-5D | 18+18+14+11+10=**71** | 3：价格、海外、期权 | 存在待验证优势；部分 | 休市；等10月12日09:30与实时报价 |
| 2 | COM-M-MA701-MOMENTUM-HOLD-20261009 | 条件多，1-5D | 19+17+14+11+9=**70** | 3：价格、curve、期权 | 存在待验证优势；部分 | 休市；等45分钟回踩 |
| 3 | COM-M-RU2701-SUPPLY-LONG-20261002 | 条件多，3-10D | 18+16+13+12+10=**69** | 2：价格、期权 | 存在待验证优势；部分 | 待curve、外盘、参数 |
| 4 | COM-M-JM2701-MOMENTUM-CONTINUATION-20261010 | 条件多，1-5D | 17+15+13+11+10=**66** | 2：价格、curve | 存在待验证优势；部分 | DCE期权缺失；等30分钟 |
| 5 | COM-M-C2611-WASDE-GAP-WATCH-20261010 | 条件空，1-5D | 16+14+15+8+6=**59** | 1：海外/实体事件 | 证据不足；不足 | 仅观察；内外盘冲突 |

反证：AG缺实体和exact Night；MA已过热且IV高于RV；RU/NR contango反对多头；JM钢材端未确认；C的中国夜盘媒体摘要与WASDE方向冲突。周末无新证据，评分相对晨报不变。

## 七、前三名交易卡

### 1）AG2612 条件多

- 市场隐含/分歧：市场仍定价快速反弹后的高波动；我们的分歧是周五海外金银收涨可能使中国日盘反转延续，但必须看到周一承接，不能预判gap。
- 事实：EOD close/settle=14717/14515，1D +0.88%，5D -7.99%，OI -4332，near-next +0.54%；金4194.36、银60.77为周五收盘。
- 推断：价格层、海外层、期权层支持；curve中性，实体缺失。最强反证是exact Night缺失且周一可能高开透支。
- 最佳表达：AG2612期货条件多；若期权实时报价完整，可研究2026-11-24到期30-45Delta一比一call spread。ATM14500、ATM IV36.39%、RV20 31.44%、RR25 +1.75；positioning/execution均不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：10月12日09:30后14650守住；好成交14650-14720，中14720-14800，坏>14850或高开>15200放弃。分两笔。
- 止损/失效/退出：计划止损14380；日收14250下方逻辑失效；TP1 15150减半，TP2 15700；2日无扩张或最长5日退出。
- 最大损失：期货不受结构限定；试仓风险NAV 0.25%-0.50%。multiplier/tick/tick value/margin/price limit/night session参数未确认，1/2涨跌停压力损失无法可靠计算；LTD 2026-12-15，需在交割月前滚动。
- 1-20D催化：周一海外贵金属开盘、美元/实际利率、COMEX资金重返。最坏情景为白银跌破58.5、人民币急变和流动性gap。

### 2）MA701 条件多

- 市场隐含/分歧：市场已隐含紧张和强动量；我们的分歧只在“回踩是否仍有承接”，不是追涨。
- 事实：close/settle=3338/3321，1D +6.04%，5D +14.83%，volume 1,493,099，OI 761,175，ΔOI +70,427，curve +16.08%。价涨仓增只是归因线索。
- 证据：价格、curve、期权支持；实体只有context。反证是过热、IV45.66%高于RV35.68%、周五夜盘exact缺失。
- 工具：MA701期货；或2026-12-11到期call spread研究，ATM3300、RR25 +2.02、BF25 1.445，surface/positioning ready、execution不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：09:45后3330-3380回踩并收复首15分钟VWAP；好3330-3350，中3350-3380，坏>3480或无回踩放弃。分两笔。
- 止损/退出：计划3270；日收3250下方失效；TP1 3460减半，TP2 3580；2日无扩张或最长5日退出。
- 参数/压力：乘数10吨/手，tick 1元/吨，tick value 10元；EOD名义33380元；保证金率7%约2336.6元；涨跌停6%；一板约2002.8元/手、两板简单压力约4005.6元/手；LTD 2027-01-14。期货最大损失不有限，交割月前滚动。
- 最坏情景：高开回落、backwardation收窄且价格下跌/OI上升、保证金上调和夜盘流动性消失。

### 3）RU2701 条件多（研究卡，未达到70）

- 市场隐含/分歧：价格动量强，但curve仍contango；分歧只有当contango同步收窄时才成立。
- 事实：close/settle=20645/20220，1D +2.89%，ΔOI +17339，curve -3.86%；NR curve -2.16%。媒体主力摘要不能替代exact-contract Night。
- 证据：价格、期权两层支持；curve反对，实体和外盘精确映射不足。因此总分受69上限。
- 工具：RU2701期货；或2026-12-25到期call spread研究，ATM20250、IV27.0%、RV21.93%、RR25 +3.22、BF25 0.68；execution不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：09:30后20500守住且contango收窄；好20500附近，中20600-20800，坏>21200或contango扩大放弃。
- 止损/退出：计划20150；日收19900下方失效；TP1 21200减半，TP2 21800；3日无扩张或最长10日退出。
- 参数/压力：仅确认LTD 2027-01-15；乘数、tick、tick value、保证金、涨跌停、夜盘参数未确认，不能编造1/2涨跌停压力损失。期货最大损失不有限；交割月前滚动。
- 最坏情景：外盘橡胶回落、国内curve继续走弱、相关性破裂或夜盘gap。

## 八、商品期权专项

最新有效研究截面为2026-10-09：185 series中181 surface-ready、41 positioning-ready、0 execution-ready；IV覆盖98.78%、OI覆盖69.36%、bid/ask覆盖0%。因此：

- IV-RV：MA约+9.98 vol、AG约+4.95、RU约+5.07；只能说明隐含波动高于20日实现波动，不能单独证明期权贵或便宜。
- Skew：AG/RU/MA的RR25均偏正，方向性call并不便宜；若触发，call spread优于裸call，但仍须实时报价。
- Event convexity：油品飓风、WASDE余波、周一海外重开具备事件性；没有bid/ask时不计算净支出、Greeks、滑点或盈亏平衡。
- 回避：SC近到期2026-10-14 series、DCE缺chain产品、任何以T-1 surface冒充周一可成交报价的结构。
- dealer_gamma_direction_known=false；不推断做市商净Gamma。

## 九、21:00夜盘风险地图

**今晚2026-10-10 21:00没有中国商品夜盘。** 四层严格分离：

1. 中国最近完整EOD：2026-10-09；
2. 今天早前已完成Night：不存在；旧repo Night为10月8日且无效；
3. 15:00-19:30海外：周六休市，无新增价格；
4. 下一实际Night：2026-10-12 21:00，归属2026-10-13交易日；不是今晚。

| 品种组 | 下一日盘预期 | 是否已充分定价 | 追价 | 等待 | 开盘确认 |
|---|---|---|---|---|---|
| AG/AU | 偏高 | 否；周一海外仍会变化 | 不追 | 30分钟 | 白银、USD/CNH、AG curve、成交/OI |
| MA/JM | 高开风险 | 部分；国内已大涨 | 不追 | 30-45分钟 | VWAP、backwardation、OI弹性 |
| RU/NR/BR | 偏高/分化 | 否；curve反对 | 不追 | 30分钟 | near-next、SICOM、OI |
| SC/FU/BU/LU | 事件驱动、方向不确定 | 否；飓风损害/复产未完成 | 不追 | 45分钟 | 海湾复产、Brent/WTI、近月curve |
| C/M/Y | 分化 | 否；WASDE与媒体夜盘方向冲突 | 不追 | 45分钟 | CBOT周一、国内gap是否回补 |
| LC/SI/PS/EC | 无夜盘品种 | 不适用 | 不追 | 45分钟 | 日盘量价、curve、产业信息 |

## 十、未来24小时/7日事件日历（北京时间）

| 时间 | 事件 | 处理 |
|---|---|---|
| 10月10-12日 | Hurricane Isaias损害评估与美国海湾复产 | SC/FU/BU/LU不追headline；线性Delta减半，只有实时价差后研究有限凸性 |
| 10月12日09:00 | 中国商品下一日盘 | 首跳不追；按15/30/45分钟验证 |
| 10月12日21:00 | 下一实际中国夜盘，归属10月13日 | 重新核验exact-contract、双收益锚、Night curve |
| 10月14日16:00 | IEA 10月Oil Market Report | 油品裸Delta提前降低 |
| 10月16日00:00 | EIA周度石油报告 | 发布前不扩线性仓 |
| 10月16日03:30 | CFTC COT | 只作拥挤背景，不推断身份 |
| 未来7日 | 中国政策、交易所参数、矿山/炼厂/天气突发 | 未确认前不计催化；保证金/限价变更即时重算风险 |

## 覆盖核对与旧建议台账

覆盖要求：原文63个必扫代码及动态流动性品种；实际引擎77个，72个取得可分析EOD，JR/PM/RI/WH/ZC五个因流动性不足不作交易判断。板块核对：

- 黑色建材：I/JM/J/RB/HC/FG/SA/SF/SM均扫描；未入榜异常为JM动量，钢材端确认不足。
- 有色贵金属：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG均扫描；AG入榜，SN内外冲突，CU曲线偏强但价格未确认。
- 能源炼化化工：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP均扫描；MA/RU入榜；SC/LU实体缺失；FU处于roll，不把连续涨幅当可交易合约收益。
- 新能源：LC/SI/PS及GFEX新材料均按可得数据扫描；LC价跌仓增异常，但无夜盘和实体确认。
- 农产品：A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK均扫描；C仅事件观察，DCE期权缺失。
- 航运软商品：EC及棉花/白糖/苹果/红枣/花生均扫描；EC大跌但curve/现货口径不足，不抄底也不追空。

策略类别：方向、curve、跨品种均完成扫描；basis仅C级context；跨市场缺exact parity不称套利；波动率/偏度/事件凸性完成研究层扫描但execution_ready=0。周期覆盖1D/3D/5D/20D。

旧建议：

| idea_id | 首次提出/原条件 | 上次状态 | 当前状态 | 变更原因 |
|---|---|---|---|---|
| COM-E-AG2612-DAY-REVERSAL-LONG-20261009 | 10月9日；日盘反转+海外确认 | 晨报等待触发 | 维持等待 | 无新数据 |
| COM-M-MA701-MOMENTUM-HOLD-20261009 | 10月9日；回踩承接 | 晨报等待触发 | 维持等待 | 周末休市 |
| COM-M-RU2701-SUPPLY-LONG-20261002 | 10月2日；供给/动量 | 观察 | 观察，需curve收窄 | 反证未消失 |
| SN2611续空（旧晚报） | 10月9日EOD延续 | 晨报已撤销 | 继续撤销 | LME反向、无新确认 |
| SC2611条件空（旧晚报） | 复产/需求走弱 | 晨报降级 | 继续降级，不追多 | 飓风已登陆但复产节奏未定 |

无成交反馈，不能假设用户持仓；“若此前已按条件建立”才适用减仓/退出措辞。风险预算：试仓最大损失NAV 0.25%-0.75%，确认交易0.75%-1.50%，同因子合并；单主题总风险≤2.5%-3.0%。压力覆盖一/两板、相关性破裂、流动性消失、周末gap、保证金上调、IV跳升/塌陷、交割挤压与人民币急变。

## 关键来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（仓库，2026-10-10生成；支持EOD/Market State/Physical/External/Options/Metadata）
- [Night Session状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（仓库，旧快照；支持Night无效判断）
- [Reuters：10月9日油价与海湾停产](https://www.reuters.com/business/energy/oil-falls-trump-comments-iran-talks-ease-supply-concerns-2026-10-09/)（2026-10-09）
- [Reuters：10月9日黄金白银收盘](https://www.reuters.com/world/india/gold-rises-softer-dollar-easing-yields-fed-outlook-focus-2026-10-09/)（2026-10-09）
- [USDA October WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)（2026-10-09）
- [IEA Oil Market Report](https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr)、[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[CFTC COT日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：无；周六中国商品不开盘，不把10月12日条件提前挂成可执行单。
C. 今晚应继续观察的机会：AG2612反转、MA701回踩、RU2701/NR2612曲线冲突、JM2701动量、C2611 WASDE后重定价。
D. 今晚必须避免或退出的交易：避免追逐飓风油价溢价、避免周一首跳追MA/RU/JM；SN2611续空仍撤销，SC旧空头仍降级。