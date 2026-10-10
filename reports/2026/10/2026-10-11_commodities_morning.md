# 全球商品期货期权高风险机会雷达（晨间版）

- 报告日期：2026-10-11
- 生成/信息截点：2026-10-11 07:08 / 07:06（北京时间）
- prompt_version：`radar_2026-09-06_coverage_v1`
- data_protocol_version：`china_commodities_v2`
- 日历：周日，中国与主要海外商品期货市场休市；最近完整中国EOD为2026-10-09，下一日盘为2026-10-12 09:00。

## 一、今日一句话结论

> **截至本报告时点，无可立即执行的合格新交易；周日无新增价格，周一仅条件验证AG、MA、RU，能源等待复产与gap确认。**

已分析但优势不足：EC抄底、SN续空、LC趋势追空，以及在复产和SPR缓冲下追逐油品单边gap。  
研究机会存在、等待条件/报价：AG2612反转、MA701回踩、RU2701/NR2612曲线修复、JM2701延续、C2611 WASDE后重定价。  
数据不足、暂时无法判断：周五夜盘exact-contract、全市场期权bid/ask、DCE期权、SC/LU实体、部分合约参数。

## 二、数据质量与覆盖

| 模块 | 日期/时点 | 状态与用途 |
|---|---|---|
| Futures | 2026-10-09；生成10月9日19:00 | 806合约、五所齐全、source-date匹配100%、full_market_ready=true、critical errors=0；周日沿用最新应得last-good |
| Market State | EOD 2026-10-09；容器10月10日19:02 | 1/3/5/20D、RV20、OI、near-next curve可用；无周末新价格 |
| Physical | 2026-10-09 latest-good | 18/20；SC/LU不可得；C级/context-only，不计方向层 |
| External | 源日期2026-10-09 | 17/22；周末仅新闻增量，无价格增量；context-only |
| Options | 交易日2026-10-09 | 14,074记录、185 series；181 surface-ready、41 positioning-ready、0 execution-ready；IV覆盖98.78%、OI覆盖69.36%、bid/ask覆盖0 |
| Night | 旧快照trading_date=2026-10-08 | generated 10月8日07:56；fresh=false、validation=false、published=false、coverage=false；0合约、outside 592、query/unresolved 214 |
| Metadata | 2026-10-09 | 48合约参数沿用，整体partial；缺失参数不猜 |

实际读取路径：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`。统一输入schema v2，requested_date=2026-10-09，generated_at=2026-10-10 19:08:23。  
Night旧快照与本期无关；周五21:00开始的夜盘归属2026-10-12交易日，但repo exact-contract缺失。公开媒体主力摘要只保留为fallback背景，不能填return_vs_close、return_vs_settlement、Night ΔOI或Night curve。周六、周日没有应发生的中国夜盘，不把自然日无新记录判成pipeline错误。

## 三、商品仪表盘（全市场扫描后的12项展示）

“1D/5D”为同合约可比指标；curve为near-next而非现货基差。Basis均为C/context-only。07:00海外栏的价格仍为10月9日收盘，周日没有实时交易。

| 板块 | 品种/合约 | EOD close/settle | 1D/5D | Volume/OI/ΔOI | Curve | Physical/Basis | Night双锚/ΔOI | 07:00海外 | Options | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| 贵金属 | AG2612 | 14717/14515 | +0.88%/-7.99% | 303600/290434/-4332 | +0.54% | context/C | exact缺失 | 金4194.36、银60.77为周五收盘 | S✓ P✗ E✗ | 09:30后14650守住再多 |
| 化工 | MA701 | 3338/3321 | +6.04%/+14.83% | 1493099/761175/+70427 | +16.08% | context/C | exact缺失；媒体主力约+2.99%相对结算 | 无新增 | S✓ P✓ E✗ | 等45分钟，严禁追高 |
| 橡胶 | RU2701 | 20645/20220 | +2.89%/— | —/—/+17339 | -3.86% | context/C | exact缺失；媒体主力>3% | 无新增 | S✓ P✓ E✗ | contango收窄再多 |
| 橡胶 | NR2612 | —/— | +0.09%/+3.16% | —/—/+7200 | -2.16% | context/C | exact缺失；媒体主力>4% | 无新增 | S✓ P✗ E✗ | 只作RU确认 |
| 黑色 | JM2701 | 1539.5/1517.5 | +4.30%/— | —/415009/+10394 | +3.48% | context/C | exact缺失；媒体偏强 | 无新增 | DCE chain缺失 | 等30分钟 |
| 有色 | SN2611 | 391410/391170 | -4.23%/— | 134989/34969/+3724 | +0.50% | context/C | exact缺失 | LME锡周五反弹约2.9% | S✓ P✗ E✗ | 旧空头失效 |
| 能源 | SC2611 | 734.1/741.3 | -0.45%/— | —/—/-3400 | +3.19% | SC缺失/C | exact缺失 | 停产69%、复产启动、SPR缓冲 | S✓ P✗ E✗ | 等45分钟，不追gap |
| 橡胶 | BR2612 | 16710/16370 | +2.77%/— | —/—/+3839 | +2.27% | context/C | exact缺失 | 无新增 | S✓ P✗ E✗ | 只观察 |
| 谷物 | C2611 | —/— | -0.42%/— | —/—/-48586 | -1.38% | context/C | exact缺失；媒体与WASDE冲突 | CBOT周五已收盘 | DCE chain缺失 | 等45分钟 |
| 饲料 | M2701 | —/— | +0.03%/— | —/—/+49030 | -1.00% | context/C | exact缺失 | CBOT周五已收盘 | DCE chain缺失 | 等45分钟 |
| 新能源 | LC2701 | 117000/118740 | -3.74%/— | —/—/+11960 | +1.22% | context/C | 制度上无夜盘 | 无新增 | S✓ P✗ E✗ | 日盘等45分钟 |
| 航运 | EC2611 | 2700/2749 | -5.05%/— | —/—/-1776 | -22.48% | context/C | 制度上无夜盘 | 无新增 | S✓ P✗ E✗ | 不抄底 |

S/P/E分别为surface/positioning/execution readiness。Night exact-contract缺失限制价格发现分解，不取消独立EOD研究；媒体相对结算涨跌不能替代相对前收的新增信息。

## 四、相比上一期真正变化

1. **海湾停产仍在，但复产启动。** 约69%美国海湾原油和57%天然气产量仍关闭；Shell、Chevron开始重新派员，说明冲击存量大、持续时间却可能缩短。[Reuters](https://www.reuters.com/business/environment/category-3-hurricane-isaias-makes-landfall-near-destin-florida-nhc-says-2026-10-10/)
2. **美国授权最多400万桶SPR投放。** 这不是完全替代停产，但进一步反对周一追逐原油事件溢价；SC方向必须看gap后弹性，而不是headline。
3. **中东运输尾险上升但未形成原油实体证据。** 利雅得机场遭袭并导致航班扰动，报道未确认油田、管线或出口设施受损，因此只调高压力测试，不计实体供应层。[Reuters](https://www.reuters.com/business/energy/major-saudi-conferences-proceed-organisers-say-despite-deadly-airport-attack-2026-10-10/)
4. **无新增价格、curve、OI或期权截面。** AG71、MA70、RU69、JM66、C59维持；所有沿用明确标记为10月9日last-good。
5. **周一窗口临近。** 下一日盘10月12日09:00；不同品种应分别等待15/30/45分钟，历史条件不能提前当成已触发信号。

## 五、产业链地图

| 产业链 | 判断 | EOD/Night/curve | 实体/海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 甲醇—烯烃 | 最强但过热 | MA 1D约+6%、5D约+14.8%，OI+70427，backwardation 16.08%；Night exact缺失 | 实体context；IV45.66% vs RV35.68% | 高质量基差、实时报价 | 中高 |
| 贵金属 | 海外确认中国日盘反转 | AG近月略backwardation；Night exact缺失 | 金银周五上涨；AG IV36.39% vs RV31.44% | 周一COMEX、参数 | 中 |
| 天然橡胶—轮胎 | 价格强、curve反对 | RU/NR强但contango | 实体context；RU IV27.0% vs RV21.93% | SICOM对齐、Night、参数 | 中 |
| 能源—炼化 | 双边事件风险 | SC EOD偏弱、curve正；Night exact缺失 | 海湾停产支持，复产/SPR反对；SC实体缺失 | 周一Brent/WTI、炼厂损害 | 中低 |
| 谷物—饲料 | WASDE偏空、国内接受度未知 | C价跌仓减，M近乎平，curve偏contango | USDA偏空；DCE期权缺失 | exact Night、周一CBOT | 中低 |

最弱链条仍是航运/新能源：EC和LC价格压力明显，但实体和可执行期权不足；不抄底，也不以单日跌幅追空。MA是最强链，但过热使“逻辑强”不等于“入场赔率好”。

## 六、机会排行榜

分数仅用于研究排序，不是胜率或仓位指令；五分项为逻辑/赔率凸性/催化/价格曲线波动率/拥挤技术。

| 排名 | idea_id | 方向/周期 | 分项=总分 | 支持层 | 研究判断/证据 | 执行 |
|---|---|---|---:|---:|---|---|
| 1 | COM-E-AG2612-DAY-REVERSAL-LONG-20261009 | 条件多，1-5D | 18+18+14+11+10=**71** | 3：价格、海外、期权 | 存在待验证优势；部分 | 休市；等10月12日09:30与实时报价 |
| 2 | COM-M-MA701-MOMENTUM-HOLD-20261009 | 条件多，1-5D | 19+17+14+11+9=**70** | 3：价格、curve、期权 | 存在待验证优势；部分 | 休市；等45分钟回踩 |
| 3 | COM-M-RU2701-SUPPLY-LONG-20261002 | 条件多，3-10D | 18+16+13+12+10=**69** | 2：价格、期权 | 存在待验证优势；部分 | 待curve、外盘、参数 |
| 4 | COM-M-JM2701-MOMENTUM-CONTINUATION-20261010 | 条件多，1-5D | 17+15+13+11+10=**66** | 2：价格、curve | 存在待验证优势；部分 | DCE期权缺失；等30分钟 |
| 5 | COM-M-C2611-WASDE-GAP-WATCH-20261010 | 条件空，1-5D | 16+14+15+8+6=**59** | 1：海外/实体事件 | 证据不足；不足 | 仅观察；内外盘冲突 |

周末能源增量不进入正式榜：停产、复产、SPR和中东运输风险方向相互抵消，只有事件层可用，尚无周一价格/curve确认。

## 七、前三名交易卡

### 1）AG2612条件多

- 市场隐含与分歧：市场仍定价反弹后的高波动；我们的分歧是周五海外金银收涨或使中国日盘反转延续，但必须等待周一承接。
- 事实：EOD close/settle=14717/14515，1D +0.88%，5D -7.99%，volume 303600，OI 290434，ΔOI -4332，near-next +0.54%；Night OHLC、双收益锚和ΔOI缺失。
- 证据：价格、海外、期权支持；curve中性，实体缺失。最强反证是exact Night缺失和周一高开透支。
- 最佳表达：AG2612期货条件多；若实时报价完整，可研究2026-11-24到期30-45Delta一比一call spread。ATM14500、IV36.39%、RV31.44%、RR25 +1.75；positioning/execution不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：10月12日09:30后14650守住；好成交14650-14720，中14720-14800，坏>14850或直接高于15200放弃；分两笔。
- 止损/退出：计划止损14380；日收14250下方失效；TP1 15150减半、TP2 15700；2日无扩张或最长5日退出。
- 风险：期货最大损失不有限；试仓NAV 0.25%-0.50%。仅确认LTD 2026-12-15；乘数、tick、tick value、margin、price limit、night session未确认，不能可靠算一/两板压力。交割月前滚动。
- 最坏情景：白银跌破58.5、美元/实际利率急升、人民币急变或周一流动性gap。9:00不追价，等30分钟。

### 2）MA701条件多

- 市场隐含与分歧：市场已隐含紧张和动量；我们的分歧只在回踩是否仍有承接，不是追涨。
- 事实：close/settle=3338/3321，1D +6.04%，5D +14.83%，volume 1,493,099，OI 761,175，ΔOI +70,427，curve +16.08%；价涨仓增仅为归因线索。
- 证据：价格、curve、期权支持；实体只作context。反证为过热、IV45.66%高于RV35.68%、exact Night缺失。
- 工具：MA701期货；或2026-12-11到期call spread研究，ATM3300、RR25 +2.02、BF25 1.445；execution不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：09:45后3330-3380回踩并收复首15分钟VWAP；好3330-3350，中3350-3380，坏>3480或无回踩放弃。
- 止损/退出：计划3270；日收3250下方失效；TP1 3460减半、TP2 3580；2日无扩张或最长5日退出。
- 参数/压力：乘数10吨/手，tick 1元/吨，tick value 10元；名义33380元；保证金率7%约2336.6元；涨跌停6%；一板约2002.8元/手，两板简单压力约4005.6元/手；LTD 2027-01-14。期货最大损失不有限，交割月前滚动。
- 最坏情景：高开回落、backwardation收窄且价格跌/OI增、保证金上调或夜盘流动性消失。9:00不追，等45分钟。

### 3）RU2701条件多（研究卡，未达70）

- 市场隐含与分歧：价格动量强，但curve仍contango；只有contango同步收窄时，多头分歧才成立。
- 事实：close/settle=20645/20220，1D +2.89%，ΔOI +17339，curve -3.86%；NR curve -2.16%。Night exact-contract缺失。
- 证据：价格、期权支持；curve反对，实体与境外精确映射不足，故受两层69分上限。
- 工具：RU2701期货；或2026-12-25到期call spread研究，ATM20250、IV27.0%、RV21.93%、RR25 +3.22、BF25 0.68；execution不ready，**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 入场：09:30后20500守住且contango收窄；好20500附近，中20600-20800，坏>21200或contango扩大放弃。
- 止损/退出：计划20150；日收19900下方失效；TP1 21200减半、TP2 21800；3日无扩张或最长10日退出。
- 参数/压力：仅确认LTD 2027-01-15；乘数、tick、tick value、margin、price limit、night session未确认，不能编造一/两板压力。交割月前滚动。
- 最坏情景：周一SICOM回落、contango扩大、相关性破裂或夜盘gap。9:00不追，等30分钟。

## 八、商品期权专项

最新有效研究截面为2026-10-09：185 series中181 surface-ready、41 positioning-ready、0 execution-ready；DCE受权限限制，TA/PF/CJ等七个产品失败；bid/ask和模型Greeks覆盖均为0。

- IV-RV：MA约+9.98 vol、AG约+4.95、RU约+5.07；这只说明隐含波动高于20日实现波动，不能单独证明贵/便宜。
- Skew：AG/RU/MA的RR25偏正，call不是明显便宜表达；触发后研究call spread优于裸call。
- Event convexity：油品飓风/SPR、WASDE余波、周一海外重开具备事件性；无bid/ask时不算净支出、滑点、Greeks或盈亏平衡。
- 回避：SC近到期series、DCE缺chain产品、任何把10月9日surface冒充周一可成交报价的结构。
- dealer_gamma_direction_known=false，不推断做市商净Gamma。

## 九、10月12日09:00开盘风险地图

三层严格分离：

1. Previous China EOD：2026-10-09完整EOD；
2. Current trading day Night：周五夜盘归属10月12日，但exact-contract缺失，仅媒体主力摘要；
3. 07:00 Overseas：周日休市，无价格增量；只有海湾停产/复产/SPR及中东运输事件增量。

| 品种组 | 预期 | 夜盘已定价？ | 内外冲突 | 追价 | 等待 | 开盘确认 |
|---|---|---|---|---|---|---|
| AG/AU | 偏高 | 部分，exact缺失 | 周五海外支持，周一仍可变 | 不追 | 30分钟 | COMEX、USD/CNH、AG curve、OI |
| MA/JM | 高开风险 | 媒体摘要显示部分预交易 | 无周末价格增量 | 不追 | 30-45分钟 | VWAP、backwardation、OI弹性 |
| RU/NR/BR | 偏高/分化 | 部分 | 价格强、curve弱 | 不追 | 30分钟 | near-next、SICOM、OI |
| SC/FU/BU/LU | 方向不确定 | 否 | 停产支持；复产/SPR反对 | 不追 | 45分钟 | Brent/WTI、gap回补、近月curve、炼厂损害 |
| C/M/Y | 分化 | 不足 | WASDE与国内媒体夜盘冲突 | 不追 | 45分钟 | CBOT周一、国内gap接受度 |
| LC/SI/PS/EC | 平/弱 | 无夜盘 | 不适用 | 不追 | 45分钟 | 日盘量价、curve、产业信息 |

最可能是单日噪音：没有curve/OI/实体确认的周一首跳、能源headline引发但15分钟内回补的gap、MA/JM在高位继续扩张但OI/curve不跟随的涨幅。

## 十、未来24小时/7日事件日历

| 时间（北京） | 事件 | 处理 |
|---|---|---|
| 10月11-12日 | 美国海湾损害评估、平台复产与SPR投放 | SC/FU/BU/LU不追首跳；线性Delta减半 |
| 10月12日09:00 | 中国商品下一日盘 | 按15/30/45分钟确认，所有旧条件重报价 |
| 10月12日21:00 | 下一中国夜盘，归属10月13日 | 获取exact-contract双收益锚与Night curve |
| 10月14日16:00 | IEA 10月Oil Market Report | 发布前降低油品裸Delta |
| 10月16日00:00 | EIA周度石油报告 | 发布前不扩线性仓 |
| 10月16日03:30 | CFTC COT | 只作拥挤背景，不推断身份 |
| 未来7日 | 中国政策、交易所参数、矿山/炼厂/天气/地缘突发 | 未确认不计催化；参数变化后重算保证金与压力损失 |

## 覆盖核对、未入榜板块与旧建议台账

覆盖要求为63个必扫代码加动态流动性品种；实际引擎77个，72个取得可分析EOD；JR/PM/RI/WH/ZC五个因流动性不足不作交易判断。

- 黑色建材I/JM/J/RB/HC/FG/SA/SF/SM均扫描；JM为未充分确认的最强异常。
- 有色贵金属CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG均扫描；AG入榜，SN内外冲突，CU曲线偏强但价格不足。
- 能源炼化化工SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP均扫描；MA、RU入榜；SC/LU实体缺失；FU处于roll，不能把连续涨幅当可交易合约收益。
- 新能源LC/SI/PS及GFEX新材料均扫描；LC价跌仓增异常，但无夜盘和实体确认。
- 农产品A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK均扫描；C仅事件观察，DCE期权缺失。
- 航运软商品EC及棉花/白糖/苹果/红枣/花生均扫描；EC跌幅大但现货/运价口径不足。

策略类别：方向、curve、跨品种完成；basis仅C级context；跨市场缺exact parity，不称套利；波动率/偏度/事件凸性完成研究扫描但execution-ready=0。周期覆盖1D/3D/5D/20D。

| idea_id | 上次状态 | 当前状态 | 变更原因 |
|---|---|---|---|
| COM-E-AG2612-DAY-REVERSAL-LONG-20261009 | 等待触发 | 维持 | 无新价格 |
| COM-M-MA701-MOMENTUM-HOLD-20261009 | 等待触发 | 维持 | 周日休市 |
| COM-M-RU2701-SUPPLY-LONG-20261002 | 观察 | 观察，需curve收窄 | 反证未消失 |
| SN2611续空（旧晚报） | 已撤销 | 继续撤销 | LME反向，未获新确认 |
| SC2611条件空（旧晚报） | 降级 | 继续降级 | 停产与复产/SPR冲突 |

无成交反馈，不假设用户持仓。风险预算：单一试仓最大损失NAV 0.25%-0.75%，确认交易0.75%-1.50%，同因子合并；单主题总风险≤2.5%-3.0%。压力覆盖一/两板、相关性破裂、流动性消失、周末gap、保证金上调、IV跳升/塌陷、交割挤压及人民币急变。

## 关键来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（2026-10-10生成；支持EOD、Market State、Physical、External、Options和Metadata）
- [Night Session状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（旧失效快照；支持Night质量判断）
- [Reuters：Isaias登陆后海湾停产、复产和SPR](https://www.reuters.com/business/environment/category-3-hurricane-isaias-makes-landfall-near-destin-florida-nhc-says-2026-10-10/)（2026-10-10）
- [Reuters：沙特机场事件](https://www.reuters.com/business/energy/major-saudi-conferences-proceed-organisers-say-despite-deadly-airport-attack-2026-10-10/)（2026-10-10）
- [USDA October WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)（2026-10-09）
- [IEA OMR](https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr)、[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)、[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：无；周日不开盘，10月12日09:30后再验证AG2612、MA701、RU2701。
C. 今天应继续观察的机会：AG反转、MA回踩、RU/NR曲线冲突、JM动量、C2611 WASDE后重定价，以及SC对停产—复产—SPR的价格弹性。
D. 今天必须避免或退出的交易：避免周一首跳追MA/RU/JM/油品，SN2611续空仍撤销；SC旧空头维持降级，不追飓风溢价。