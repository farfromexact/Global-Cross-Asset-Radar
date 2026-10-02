# 全球商品期货期权高风险机会雷达｜晚间版｜2026-10-02

`prompt_version=radar_2026-09-06_coverage_v1` · `data_protocol_version=china_commodities_v2`

生成时间：2026-10-02 19:31 北京时间｜信息截点：19:25｜中国最近完整交易时段：2026-09-30日盘｜下一实际窗口：2026-10-08 08:55集合竞价、09:00日盘；下一夜盘为10月8日21:00。

> **今晚的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。** 中国国庆休市；油价在昨日暴涨后明显回吐，直接追能源补涨的赔率下降，只保留成品油裂解、RU强势和OI相对强度的节后验证。

## 一、今晚一句话结论

Brent跌回100美元下方、WTI约89.3美元，能源从“补涨”降为“裂解相对价值”；今晚中国无夜盘，10月8日复市前不建立中国商品风险。

最接近验证的三项：①RU2701强势能否跨假期保持；②亚洲成品油裂解是否在储备释放讨论后仍维持异常backwardation；③OI701能否在海外油籽偏弱时继续相对抗跌。缺失条件均是10月8日具体合约重报价、curve、量仓及实时bid/ask。

## 二、数据质量、时间与覆盖

第一读取层：[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。四者均从main直接读取；网页行情只补充15:00—19:30海外层，没有替代仓库。

| 模块 | 实际日期/生成时点 | 状态 | 本期用途与限制 |
|---|---|---|---|
| 统一输入 | requested 2026-09-30；generated 10/2 19:02:16 | schema v2 | 合并9/30中国last-good及10/2 External |
| Futures | 9/30；10/1 08:02生成 | `ok_last_good` | 五所、806合约/77品种；source-date match 100%，critical errors 0，full_market_ready=true |
| 10/2 root refresh | 10/2 18:57 | `holiday_no_eod` | 当日无记录、full_market=false属于休市刷新；不得覆盖9/30 last-good |
| Market State | 9/2—9/30；10/2 18:57重生成 | `ok_last_good` | 同合约1/3/5/20D、RV20、量仓和curve仍为最新应得中国状态 |
| Physical | source 9/30 | `partial_native_frequency` | 18/20原生频率有效；SC/LU unavailable；无A/B exact-contract basis |
| External(repo) | requested/source 10/2；19:01:51 | `ok_context_only` | 17/22 fresh；5 unavailable；与Reuters临近19:30行情分层 |
| Night Session | 可用last-good trading_date 9/30、session 9/29 | `historical_only` | 属于9/30已完成阶段，不是今晚行情；10/2 holiday run为0合约且未发布 |
| Options | 9/30 | `research_only` | 14,468记录/196 series；192 surface、47 positioning、0 execution |
| Contract metadata | 9/30 | `partial` | effective match 73.45%；交易参数覆盖30.15%；LTD覆盖67.49% |

Night状态必须分开：10/2状态文件记录`trading_date=2026-10-02`、`night_session_date=2026-10-01`、generated 07:57:28，但`data_fresh=false / validation_passed=false / published=false / coverage_complete=false`，night contract=0，query/unresolved=214，且`previous_valid_snapshot_retained=true`。这是国庆休市期间没有应得session，不是行情丢失。最近合法last-good仍为9/30交易日的423合约/37品种，仅用于历史Night→Day分解。

Options：42/64预期品种成功、18个DCE品种跳过，CJ/PL/ZC/A失败；IV覆盖98.84%、OI覆盖68.88%、bid/ask覆盖0，dealer Gamma方向未知。旧surface可支持研究存量结构，但不能代表复市后的Delta、moneyness、权利金或成交性。

交易所日历确认10月1—7日休市，10月8日08:55集合竞价、09:00恢复日盘，当晚恢复连续交易：[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202609/t20260921_833508.html)、[INE](https://www.shfe.cn/eng/CircularNews/Circular/202609/t20260921_833510.html)、[GFEX](https://www.gfex.com.cn/en/Notices/202601/ecd5e39ce8a04d2eb0a88d47ba2abd26.shtml)。

## 三、商品仪表盘（中国列为9月30日历史锚）

| 板块/品种 | 合约 | EOD close/settle | 1D/5D | Vol/OI/ΔOI | Curve；Physical/basis | 早前Night close；overnight/day | 10/2 19:02 repo / 19:25海外 | Options S/P/E | 信号 |
|---|---:|---:|---:|---:|---|---|---|---|---|
| 橡胶 RU | RU2701 | 20095/19710 | +3.52%/+3.96% | 513683/150478/+18323 | back +0.237%；天气/库存支持，无A/B | 19665；+3.45% / +2.19% | 无新的exact SICOM；油价回吐削弱成本支持 | Y/Y/N | 最强存量候选；复市等45m |
| 橡胶 NR | NR2612 | 17390/17000 | +3.53%/+5.56% | 86314/80028/+4484 | back +0.293%，z1.86 | Night代表NR2611，不可比 | 无exact进口平价 | Y/N/N | 不用代表合约替代交易腿 |
| 橡胶 BR | BR2611 | 16000/15870 | +3.12%/+6.58% | 288172/51622/-4127 | back +1.134%；无实体闭环 | 16155；+4.50% / -0.96% | WTI约89.3、Brent约99.7，成本支持回撤 | Y/N/N | 降级次选 |
| 油脂 OI | OI701 | 10230/10217 | +1.72%/-0.25% | 272992/283749/+9681 | back +1.820%；无A/B | 10234；+1.76% / -0.04% | 豆-1.12%、豆粕-0.69%、豆油-0.37%、棕榈-0.46% | Y/N/N | 海外反对；复市只看相对强度 |
| 原油 SC | SC2611 | 711.0/696.1 | -2.90%/-2.93% | 175510/24979/-4690 | contango -0.057%，z-1.78；physical缺 | 705.2；-0.94% / +0.82% | Reuters Brent99.74(-2.51%)、WTI89.34(-3.8%) | Y/N/N | “直接补涨”降级，不追 |
| 燃料油 FU | FU2611 | 4434/4376 | -0.95%/+4.59% | 663508/126742/-23873 | back +30.142%，z2.01；现货仅context | 4373；-1.46% / +1.39% | 亚洲汽油裂解一度>50美元，但气油约跌5% | Y/N/N | 裂解RV研究，等待back是否维持 |
| 沥青 BU | BU2611 | 5013/5091 | -2.00%/-0.29% | 880746/155550/-53419 | back +12.610%；无A/B | 5142；-1.98% / -2.51% | 原油回吐；需求端未更新 | Y/Y/N | 补涨依据减弱 |
| 黄金 AU | AU2612 | 910.58/905.04 | +0.80%/-3.75% | 184362/225591/-229 | contango -0.248% | 905.02；+0.69% / +0.61% | repo COMEX 4210.5；现货约4181.6，周跌>2% | Y/N/N | 非农前中性，信用主题未确认 |
| 白银 AG | AG2612 | 14980/14928 | +0.15%/-7.41% | 273904/283220/+6039 | contango -0.215% | 14958；+0.74% / +0.15% | repo61.37；现货约61.21，日内+0.6% | Y/N/N | 波动高但无境内报价 |
| 铜 CU | CU2611 | 109680/109570 | +0.25%/-1.03% | 69830/185404/+183 | back +0.730%，z1.95；现货仅context | 无完整同约分解 | LME 14293，较10/1 repo -0.26%；美元偏强 | Y/N/N | curve支持、海外反对 |
| 铁矿 I | I2701 | 9/30 last-good | 未展示精确收益 | 已扫描 | curve已扫描；DCE期权缺 | 具体同约Night未核实 | SGX 91.35，较10/1 -1.03% | DCE缺 | 黑色外盘偏弱，非交易卡 |
| 白糖 SR | SR701 | 9/30 last-good | 已扫描 | 已扫描 | 境内无新实体闭环 | 无新Night | ICE糖19.27，较10/1 +2.45%；FAO糖价月升6.1% | Y/partial/N | 新研究异常，最高仅58分 |

## 四、相比晨报与上一晚报的真正变化

1. **油价反转是核心变化**：10月1日Brent收102.31美元后，10月2日约19:25跌至99.74（-2.51%），WTI跌至89.34（-3.8%），欧洲气油约跌5%。触发因素是欧洲讨论释放柴油库存、同时存在释放更多原油储备的磋商。原先“节后SC直接补涨”不再成立为当前主路径。[Reuters，2026-10-02](https://www.reuters.com/business/energy/oil-rises-slightly-market-weighs-mixed-supply-signals-2026-10-02/)
2. **产品紧张并未完全消失**：中国燃料出口暂停曾把亚洲汽油裂解推至逾50美元/桶，气油和航煤月差显著backwardation；储备释放讨论压低当日价格，但未证明结构性紧张结束。因此能源从单边Delta降为裂解/期限结构研究。[Reuters，2026-10-02](https://www.reuters.com/business/energy/china-fuel-export-suspension-choke-supplies-asia-2026-10-02/)
3. **油脂外盘转为明确反证**：repo截至19:02显示豆、豆粕、豆油、棕榈较前日分别约-1.12%、-0.69%、-0.37%、-0.46%；中国大豆需求与压榨利润偏弱继续限制OI多头分数。
4. **贵金属仍是事件等待而非方向交易**：现货金约4181.59美元、周跌逾2%，银约61.21、日内+0.6%；美元周线偏强、10年期美债收益率约5.247%，今晚20:30非农才是下一次重定价。[Reuters黄金](https://www.reuters.com/world/india/gold-slips-before-us-payrolls-data-set-second-weekly-loss-2026-10-02/)；[Reuters利率](https://www.reuters.com/markets/europe/global-markets-view-europe-2026-10-02/)
5. **白糖成为新研究异常**：ICE糖由18.81升至19.27，FAO 9月糖价指数月升6.1%，但中国SR价格、curve与实体未提供本期新增确认，故只给58分早期观察。[Reuters/FAO，2026-10-02](https://www.reuters.com/markets/us/world-food-prices-near-four-year-high-september-un-says-2026-10-02/)
6. **中国层没有新增**：没有10月2日EOD、早前Night、Physical或Options新截面；休市刷新失败不改变9月30 last-good有效性。

旧建议台账：RU、OI、BR和能源idea_id沿用。相较今晨，RU由76降至74（油价成本支持反转）；能源由74降至72并明确改为产品裂解/RV研究，放弃SC直接追多；OI由68降至66（海外油籽反证）；BR由63降至60；AP退出前五但保留观察，原因不是观点反向，而是白糖出现更强的新异常。没有成交反馈，不假设持仓。

## 五、产业链地图

| 产业链 | 方向/强弱 | 价格、Night与curve | 实体/海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 天然橡胶—20号胶 | **境内存量最强，偏多** | RU/NR价仓与back支持；RU Night后日盘续涨 | 天气/库存支持；无新SICOM；油价回吐 | 假期橡胶exact路径、bid/ask、RU参数 | 中高研究/零执行 |
| 原油—燃料油—沥青 | **分化：产品强于原油** | SC节前弱、FU/BU deep back；原油日内回吐 | 出口暂停支持裂解；储备释放是强反证 | 同刻裂解报价、腿比、SC/LU physical | 中高研究 |
| 油脂油料 | OI相对强但海外转弱 | OI隔夜涨幅日盘守住、back支持 | 豆系/棕榈下跌；期权call skew偏贵 | A/B basis、DCE options、复市量仓 | 中 |
| 贵金属—美元—利率 | 中性偏事件驱动 | AU/AG节前弱，curve不支持追多 | 金周跌、银小涨；美元/利率反对，非农临近 | 非农后价格、实际利率、境内重报价 | 中低 |
| 白糖—软商品 | 早期偏多异常 | 中国SR无新增 | ICE糖与FAO支持；国内实体缺 | SR exact EOD下钻、库存/产量、期权执行 | 低至中 |

## 六、机会排行榜

| 排名 | idea_id / 方向 / 周期 | 逻辑25 | 赔率25 | 催化20 | 价曲波15 | 仓技15 | 总分 | 有效支持层；反证/缺失 | 判断 / 证据 / 执行 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | `COM-E-RU2701-RUBBER-TIGHTNESS-20261001` 多RU2701，1—5D | 22 | 16 | 15 | 13 | 8 | **74** | 1价格/OI、2曲线、3实体、4境外；油价回吐、IV>RV、gap与参数缺 | 存在待验证优势 / 充分 / **休市等10/8** |
| 2 | `COM-E-ENERGY-POSTEIA-20260930` 多产品裂解/期限结构，1—10D | 21 | 16 | 17 | 11 | 7 | **72** | 2曲线、3产品供给、4海外；储备释放、原油回吐、精确腿比缺 | 存在待验证优势 / 部分 / **休市待报价** |
| 3 | `COM-E-OI701-RELSTRENGTH-20260930` 多OI701相对强度，1—5D | 19 | 14 | 12 | 11 | 10 | **66** | 1价格/OI、2曲线；海外油籽与需求反对 | 存在待验证优势 / 部分 / **休市等待触发** |
| 4 | `COM-E-BR2611-RELSTRENGTH-20260930` 多BR2611，1—5D | 18 | 13 | 11 | 9 | 9 | **60** | 1价格、2曲线；油价回吐、仓减、日盘回撤 | 存在待验证优势 / 部分 / **次选观察** |
| 5 | `COM-E-SR701-SUGAR-TIGHTNESS-20261002` 多SR701研究，1—10D | 17 | 12 | 12 | 8 | 9 | **58** | 3供给背景、4海外；中国price/curve/options无新增 | 证据不足 / 不足 / **研究观察** |

复算总分为74、72、66、60、58，分项均未超上限。RU与能源分别至少3个独立支持层，具备70分资格；OI/BR仅两层，分数不超过69；SR当前只有海外/供给背景，不超过59。分数不是胜率或仓位指令。

## 七、前三名研究卡（休市；不冒充当前订单）

### 1. RU2701强势延续｜74

- **事实**：9/30 close/settle 20095/19710；早前Night OHLC 19080/19780/19040/19665，overnight +3.45%，vs settlement +3.28%，Night ΔOI +11873；日盘相对Night +2.19%。四层支持仍在。
- **市场隐含/分歧**：市场可能已经计入降雨与库存下降；分歧是若复市后backwardation和价仓仍维持，供应扰动可延续1—5日。最强反证是SICOM回吐、油价下跌和>5%假期gap透支。
- **工具**：RU2701期货；期权只在10/8取得bid/ask后比较35—45 Delta、同到期1:1 call spread。旧ATM IV27.94%高于RV20 22.25%，不证明call便宜。
- **入场/情景**：好=10/8回踩20095守住且curve不塌，0.25% NAV计划止损风险；中=首45分钟高点突破后回测，≤0.50%；坏=>5%高开、近月转contango或价涨仓减，放弃。
- **失效/退出**：跌破19710且30分钟不能收复；TP1 20500减1/3、TP2 21000再减1/2，余仓2日无扩张退出；最长5日。
- **参数/压力**：multiplier、tick、margin、limit及night参数未确认，LTD 2027-01-15；notional和1/2涨跌停压力不得猜。期货最大损失不有限；交割月前至少10个交易日滚动。

### 2. FU2611—SC2611产品裂解研究｜72

- **事实**：FU2611 close/settle 4434/4376、EOD back +30.142%；SC2611 711.0/696.1、近月轻contango。10/2亚洲汽油裂解此前超过50美元，但随后Brent/WTI和欧洲气油大跌。
- **市场隐含/分歧**：市场正在交易储备释放可缓解短缺；分歧是中国出口暂停造成的亚洲产品结构紧张可能比原油更持久。反证是储备实际释放、海湾出口恢复和裂解快速坍塌。
- **最佳表达**：研究篮子为**多FU2611、空SC2611，按人民币名义金额50%/50%配平**；收益定义为0.5×FU百分比收益−0.5×SC百分比收益，属于dollar-notional-neutral，**不是beta-neutral**。当前乘数、同步报价和beta缺失，不能换算手数，故不可执行。
- **入场**：10/8等45分钟；仅当FU/SC归一化价差高于首45分钟中枢、FU backwardation维持且Brent不再单边下坠时才重新估算。好=价差回踩承接；中=突破后回测；坏=产品裂解/near spread显著压缩，放弃。
- **失效/退出**：裂解连续30分钟跌破复市首45分钟低点，或储备释放落地后产品月差快速转弱；TP1 +1R减1/3、TP2 +2R再减1/2，3日无扩张退出，最长10日。两腿均为线性期货，最大损失不有限；相关性破裂需单独压力测试。
- **参数/交割**：FU/SC动态乘数、margin、limit需复核；SC2611 LTD 2026-10-30，交割风险高，最后交易日前至少5个交易日平仓/滚动。

### 3. OI701相对强势｜66

- **事实**：9/30 close/settle 10230/10217；Night 10057/10256/10051/10234，overnight +1.76%，vs settlement +1.89%，Night ΔOI +6681；日盘相对Night -0.04%，EOD ΔOI +9681，back +1.82%。
- **市场隐含/分歧**：市场可能已计入短期油脂偏紧；分歧是跨油脂相对强度若能抵抗海外豆系下跌，可延续。反证是豆、豆粕、豆油和棕榈同步偏弱，且中国大豆需求/压榨利润不强。
- **工具**：OI701期货优先；OI701 call spread只有实时双边报价后才可比较。历史ATM IV15.26%、RR25 +3.92，call skew偏贵。
- **入场/情景**：10/8等60分钟；好=回踩10230守住且OI相对Y/P收益为正；中=首小时高点突破回测；坏=>2%高开或Y/P更强，放弃。
- **止损/退出**：10050止损；TP1 10450、TP2 10700；3日无扩张退出，最长5日。
- **参数/压力**：multiplier 10吨、tick 1元、tick value 10元；参考margin 9%、limit 8%、LTD 2027-01-14。以10230计notional 102,300元，参考margin 9,207元；1/2涨跌停压力约8,184/16,368元每手。期货最大损失不有限。

## 八、商品期权专项

期权仍是9/30最新有效研究截面，本期没有中国新增。RU2701 ATM IV27.94%、IV-RV +5.69vol、RR25 +1.91；OI701 ATM IV15.26%、IV-RV +1.02、RR25 +3.92；FU2611 IV68.10%、RR25 -3.42；SC2611旧面仅能作历史背景。所有series execution-ready=false，不提供权利金、净支出、滑点、盈亏平衡或Greeks。

今晚20:30美国非农适合境外有限凸性研究，但并不证明黄金/原油期权便宜。若用境外工具，最大净支出≤NAV 0.25%—0.50%，事件后15—30分钟再评估；国内期权休市，无法建立或动态对冲。回避DCE缺失链、旧Delta、裸卖event vol及任何dealer Gamma方向推断。

## 九、21:00夜盘风险地图

严格四层：①中国完整EOD=9/30；②最近Night=归属9/30的历史阶段；③15:00—19:30海外=油价回吐、金银等待非农、工业金属/油籽偏弱；④今晚21:00中国Night=**不存在**。下一实际Night为10月8日21:00。

| 品种 | 10/8潜在重开 | 海外冲突 | 首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|---|
| SC/FU/BU | 不再预设高开；高波动分化 | 出口暂停支持产品，储备释放压制原油/气油 | 不追 | 45m | Brent100、亚洲裂解、FU/SC curve与价差 |
| RU/NR/BR | 偏高或高位震荡 | 境内强，但成本油回吐且SICOM缺新exact | 不追 | 45m | SICOM、RU/NR同步、back与OI |
| OI/Y/P | 平至偏低 | 境内OI强、海外油籽普弱 | 不追 | 60m | OI相对Y/P、前后月、压榨利润 |
| AU/AG | 取决于非农后路径 | 黄金周弱，美元/利率仍高 | 不追 | 30m | 非农、美元、实际利率、金银比 |
| CU/AL/NI | 平至偏低 | LME偏弱、美元偏强 | 不追 | 30m | LME/SHFE映射、USD/CNH、curve |
| SR | 偏高先验但低置信 | ICE/FAO支持、中国无新增 | 不追 | 45m | SR curve、库存/产量、量仓 |
| AP/LC/EC | 不预判 | 缺可靠海外映射 | 不追 | 30—45m | 实体、OI和首日curve |

## 十、未来24小时与7日事件

- **10/2 20:30 BJT**：美国9月非农，市场预期新增约9万、失业率4.1%；重点看工资和修正值。中国休市；境外Delta/Vega仅用有限损失结构，等待15—30分钟。[Reuters](https://www.reuters.com/business/us-job-growth-expected-slow-september-unemployment-rate-likely-steady-2026-10-02/)
- **10/3 03:30**：CFTC COT常规发布时间，只作截至周二的滞后拥挤背景。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **10/4—5**：泰国强降雨风险窗口；只有实测降雨和割胶影响才可作为RU新增催化。
- **10/6**：EIA Short-Term Energy Outlook / Winter Fuels Outlook；关注产品库存与供应预测。[EIA](https://www.eia.gov/outlooks/steo/release_schedule.php)
- **10/7 22:30**：EIA Weekly Petroleum Status Report，是中国复市前最后关键能源数据。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **10/8 08:55/09:00；21:00**：中国集合竞价/日盘恢复，当晚恢复Night；所有旧条件重新报价。
- **10/9 00:00**：USDA 10月WASDE，国内复市后首个重要农业事件。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)

OPEC月报为10月13日，超出7日窗口；IEA月报精确时间未核实，不编时点。地缘、中东部署和储备释放属于非定时事件，能源风险必须同时压力测试正负两侧gap。

## 十一、覆盖核对、未入榜异常与风险

应覆盖63个指定代码及动态新增品种；Futures实际取数并扫描77品种（63+14动态：JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR）。策略覆盖方向、curve/跨期、高质量基差、跨品种/跨市场、期权方向与vol/skew、事件凸性、中性组合；周期覆盖1—5D、1—10D和20D状态。

| 板块 | 实际期货分析 | 数据不足 | 未入榜最重要异常/无异常依据 |
|---|---:|---|---|
| 黑色建材 | 9/9 | DCE期权、复市实体/利润 | SGX矿-1.03%，但中国无新增price/curve确认 |
| 有色贵金属 | 12/12 | 当前境内报价、期权执行、部分参数 | CU curve偏back而LME/美元反对；AU/AG等待非农 |
| 能源炼化化工 | 21/21 | SC/LU physical、exact crack与同步报价 | FU/BU deep back与原油回吐的分化仍是核心RV问题 |
| 新能源 | 3/3及GFEX动态 | LC仓单stale、海外proxy | LC 5D弱但无新实体确认，不追空 |
| 农产品油脂畜牧 | 指定品种全部期货 | DCE 18个期权跳过，CJ/A失败，basis不足 | OI入榜；豆系外盘偏弱，RM/Y/P无多层共振 |
| 航运软商品 | EC/CF/CY/SR/AP/CJ/PK全扫描 | EC curve样本少；SR/AP实体；CJ option | SR新异常；AP原观察仍为55分但退出Top5；EC不作伪套利 |

数据不足与不适用严格区分：10月2日中国EOD/Night为日历不适用；DCE options、SC/LU physical、A/B basis、exact import parity、实时bid/ask和多数动态参数是真缺失。正式可执行候选为0，不等于研究机会为0。

风险预算：休市期中国新增风险=0；复市试仓计划止损风险NAV 0.25%—0.50%，确认后0.75%—1.50%，同因子能源/橡胶合并≤2.5%。压力覆盖1/2涨跌停、相关性破裂、流动性消失、长假gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变和海外事件反转。

### 来源

- China-Commodities-Engine统一输入与状态，source dates 2026-09-30/10-02，支持中国EOD、External、Night、Options及质量判断。
- [Reuters：油价跌逾2%](https://www.reuters.com/business/energy/oil-rises-slightly-market-weighs-mixed-supply-signals-2026-10-02/)，2026-10-02，支持Brent/WTI/气油与储备释放讨论。
- [Reuters：亚洲燃料供应收紧](https://www.reuters.com/business/energy/china-fuel-export-suspension-choke-supplies-asia-2026-10-02/)，2026-10-02，支持裂解与backwardation。
- [Reuters：黄金等待非农](https://www.reuters.com/world/india/gold-slips-before-us-payrolls-data-set-second-weekly-loss-2026-10-02/)，2026-10-02，支持金银、美元与利率背景。
- [Reuters/FAO：食品价格](https://www.reuters.com/markets/us/world-food-prices-near-four-year-high-september-un-says-2026-10-02/)，2026-10-02，支持糖与植物油月度背景。
- SHFE/INE/GFEX、EIA、CFTC、USDA官方日历，链接见正文。

A. 今晚没有应立即建立的新仓位。
B. 今晚没有可在中国市场生效的条件单；10月8日仅重估RU2701、FU2611/SC2611裂解篮子和OI701条件。
C. 今晚应继续观察20:30美国非农、Brent能否重上100美元、亚洲汽柴油裂解、SICOM/泰国降雨、油籽弱势及ICE糖。
D. 今晚必须避免或退出把昨日油价暴涨线性外推、追逐不存在的中国夜盘、用旧IV下单、未定义手数的跨品种篮子及任何休市proxy套利。
