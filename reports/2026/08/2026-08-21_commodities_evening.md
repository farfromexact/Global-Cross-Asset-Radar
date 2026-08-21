# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-21

> 数据截点：北京时间2026-08-21 20:24。中国日盘已经结束，21:00夜盘尚未开市。本次任务实际生成晚于19:30，因此把**15:00—19:30海外窗口**与**19:30—20:02新增信息**分开：后者只用于更新21:00开盘风险地图，不冒充19:30时已知信息。研究与交易决策支持，不自动下单。

## 一、今日一句话结论

**有条件机会，但仍没有应立即建立的新仓：20:02 BJT Brent/WTI已从17:49约-0.5%转为小幅上涨，FU2611条件多升至79分；AG/FG逻辑不变，21:00首跳仍不追。**

今天值得冒的是**“确认后的小风险”**，不是方向猜测风险。没有80分以上确认交易；FU2611 79分、AG2610 76分、FG701 74分、BU2610 73分，全部只能条件试仓/条件单。EC2610只有两层可完整计分证据，严格封顶69分。

## 二、数据质量与覆盖说明

- 第一读取层：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；为交易参数/合约明细按需读取`data/latest.json`。本报告执行`china_commodities_v2`，不以`radar_latest.evidence_count`代替五层证据重算。
- `report_input_latest.json`：requested_date=`2026-08-21`；generated_at=`2026-08-21T19:02:52.405697+08:00`。
- 核心Futures：2026-08-21，SHFE/INE/DCE/CZCE/GFEX五所齐全；`full_market_ready=true`，`source_date_match_pct=100%`，803个合约；unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、placeholder=5、critical errors=0。核心行情为iFinD vendor-primary，因此`official_complete=false`不等同于行情失败。
- Market State：1D/3D/5D/20D均使用当前**同一具体合约**历史，不拼接不同主力；价涨仓增/价跌仓增等仅作归因线索。
- Physical：20个目标仅4个有可验证且按原生频率fresh的序列。FG 8月21日周度企业库存7441.4重量箱仅有绝对水平，不能自动算方向确认；JM 8月10日旬度现货1908.3元/吨的basis为C级、`eligible_for_physical_score=false`；I港口库存数值/单位仍需QA；TA周度加工费586.52元/吨仅作context。
- External仓库EOD层整体`data_fresh=false`，但不能一刀切：Brent/LME铜/SGX铁矿/DXY/USDCNH等部分series按自身状态仍可作context；BMD棕榈油为stale，不计分。所有进口平价均未满足exact-contract、币种、品质、税费、运费、时点对齐，**无可执行跨市场套利**。
- 晚间海外增量：17:49 BJT Reuters快照中Brent/WTI约-0.53%/-0.51%；到20:02 BJT，Reuters更新为Brent约93.97美元/桶、WTI约86.97美元/桶，已转为约+0.20%/+0.16%，相对17:49价格约再涨0.74%/0.67%。这是19:30后的新增信息，只用于21:00风险地图。贵金属最近可核实快照为19:01 BJT：现货黄金4587.23美元/盎司、+1.5%，白银69.48美元/盎司、+2.0%；DXY约98.65、接近三个月低位。
- Options：T日2026-08-21，21,816条记录，59/64品种，368个series；360个`surface_ready=true`、70个`positioning_ready=true`、**0个`execution_ready=true`**；IV coverage 98.47%，OI coverage 68.74%，bid/ask coverage 0。可用ATM IV、RR25、BF25与term structure做研究，但不能虚构净权利金、滑点或“可按某价成交”；`dealer_gamma_direction_known=false`。
- Contract Metadata：部分可用、总体partial；DCE合约元数据抓取存在错误、GFEX元数据日期匹配不完整。前三交易卡仅落数已由仓库或交易所公开规则复核的参数；券商保证金未确认。
- 上一期可比基准：2026-08-20 commodities_evening；另有同日20:00版，本次属于**20:24增量修订**，最重要修订是原油外盘从负转正。

## 三、商品仪表盘

| 板块 | 品种/主力 | 最新有效价（中国EOD） | 1D / 5D | Volume / OI | ΔOI | Curve | Physical / Options | 当前信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 能源 | **FU2611** | close 3845 / settle 3850 | +2.12% / +9.81% | 650,637 / 285,614 | +22,573，+8.58% | **Backwardation +7.47%，z +1.70** | ATM IV约43.0%；surface Y / exec N | 国内共振最强；20:02外盘再转强，但只买回撤确认 |
| 贵金属 | **AG2610** | 16771 / 16611 | +3.11% / +5.45% | 773,038 / 306,822 | +4,403，+1.46% | 轻微Contango -0.14%，仅4个obs | ATM IV 47.27%，RR25 +7.81；surface Y / pos N / exec N | 强趋势+弱美元；Vega昂贵，不能追 |
| 建材 | **FG701** | 907 / 906 | -1.09% / -3.10% | 1,575,371 / 1,601,238 | +148,375，+10.21% | **Contango -3.35%** | 周度库存仅水平；ATM IV 23.06%，pos Y / exec N | 价跌仓增线索+Contango；条件空 |
| 能源 | **BU2610** | 4508 / 4526 | +2.14% / +7.92% | 486,111 / 334,627 | -2,643，-0.78% | Backwardation +3.16% | ATM IV约27.75%；exec N | 能源同向，但价涨仓减线索，次于FU |
| 能源 | **SC2610** | 具体close/settle本表不重复展开 | +1.28% / +7.61% | activity高 | +465，+1.08% | Backwardation +4.17%，z +1.81 | surface可研究 | 原油链强，但FU表达更干净 |
| 化工 | **MA610** | 2909 / 2880 | settle +1.80% / +8.56% | 1,957,108 / 873,688 | +5,954，+0.69% | Backwardation +0.35%，z +1.34 | surface ready / exec N | 等原油映射与自身30–45分钟确认 |
| 化工 | **EG2610** | 5202 / 5159 | close +2.02% | 546,862 / 272,984 | 未单独展开 | Backwardation | surface ready / exec N | 价格/curve偏强，实体闭环不足 |
| 航运 | **EC2610** | 1957 / 1885.5 | settle +7.56% / +18.66% | 41,149 / OI高位 | +2,998，+11.84% | 近月结构+28.41%，受近月效应污染 | 无完整Options层 | 极端动量，不追；两层证据封顶69 |
| 新能源 | **LC2701** | 158680 / 156360 | +2.60% / +1.41% | 225,444 / 353,437 | +31,875，+9.91% | Contango -0.30% | ATM IV约35.37%；exec N | price/OI强但curve不确认“短缺” |
| 油粕 | **RM611** | 2238 / 2246 | -1.36% | 747,569 / 651,265 | 未单独展开 | Backwardation +3.96% | surface可研究 | 价格与curve冲突，不追空 |
| 豆粕 | **M2701** | 3228 / 3244 | close -1.10% | 1,390,344 / 2,467,335 | 未单独展开 | Contango | 进口平价缺；surface部分可用 | 弱但海外/压榨链不闭环 |
| 纸浆 | **SP2611** | 4892 / 4848 | close +3.42% | 535,700 / 260,902 | 未单独展开 | Contango | surface可研究 | 单日强而curve不确认，暂不交易 |

注：Curve是期货近月—次近月结构，不是现货基差。周度/旬度Physical的`fresh`只表示仍在原生发布频率有效窗口内，不代表“今天新变化”。

## 四、相比上一交易日真正变化

1. **FU从8月20日“价格回撤、曲线很紧”重新变成价格/OI/curve共振。** 8月21日settle +2.12%、ΔOI +8.58%、5D +9.81%，Backwardation仍约7.47%；较8月20日约8.16%的结构有所收敛，所以不能把趋势写成无限加强。
2. **本次20:24修订最重要的增量是海外油价从负转正。** 17:49 BJT Brent/WTI约-0.53%/-0.51%，20:02 BJT已约+0.20%/+0.16%，价格较17:49再升约0.74%/0.67%。这提高FU/BU偏高开的概率，同时**降低追价赔率**。
3. **AG延续而非新启动。** 日盘settle +3.11%、5D +5.45%；19:01 BJT白银+2.0%、黄金+1.5%，DXY约98.65。方向仍同向，但AG ATM IV 47.27%相对RV20约30.82%贵约16.45 vol，买错时点的Theta/Vega风险很大。
4. **FG空头组合重新建立。** 8月20日曾是反弹+减仓，8月21日变成settle -1.09%、ΔOI +10.21%、Contango -3.35%；这是一组更有价值的“价跌仓增归因线索+弱curve”，但Physical仍只有绝对库存水平。
5. **EC成为全市场极端动量异常。** close +11.64%、settle +7.56%、5D +18.66%、ΔOI +11.84%；海外航运地缘风险只是背景，不是EC欧洲线同口径实时运价，因此不能把外部层硬算满。
6. **Options研究层今天明显可用，但执行层仍完全关闭。** 360/368 series surface-ready，execution-ready仍为0；因此“Call Spread/Put Spread优于裸期货”只能是结构方向，不能是假定可成交成本比较。

## 五、产业链地图

| 链条 | 方向 | 最强/最弱 | Price / Curve | 实体/仓单 | Options | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|
| 原油—燃料油—沥青 | **偏多但开盘gap风险升高** | FU最强，BU次强 | FU price/OI/Backwardation共振 | 裂解/产品库存缺 | surface ready / exec false | 20:02 Brent/WTI转正；Hormuz/伊朗供给风险高 | exact裂解、进口平价 | 高 |
| 贵金属 | **偏多、高IV** | AG强于AU的弹性 | price强，curve确认弱 | 实体层非核心 | AG skew/IV可用，exec false | 金银上涨、美元弱 | 19:30后人民币同口径映射 | 中高 |
| 建材/黑色 | **偏弱** | FG最弱 | FG价跌仓增+Contango | 库存只有水平context | FG surface+positioning ready | 无直接海外锚 | 库存方向、地产/深加工需求 | 中高 |
| 航运 | 极端上行、过热 | EC | price/OI爆发，curve受近月效应 | 实体运价同口径缺 | 无完整期权层 | Hormuz航运扰动仅宏观背景 | SCFIS/即期欧线实时锚 | 中 |
| 新能源材料 | 高波动反弹 | LC | price/OI强但Contango | 库存/排产缺 | surface ready / exec false | 无可靠进口平价 | 成本、库存、排产 | 中 |
| 油脂饲料 | 分化偏弱 | RM/M偏弱 | price与curve冲突 | 压榨/库存缺 | 部分surface可用 | BMD stale、无可执行同月平价 | CBOT/BMD/压榨闭环 | 中低 |

**最强链条：能源。最弱链条：建材中的FG。当前regime不是全面商品牛市，而是地缘能源+贵金属宏观强势与中国内需链偏弱并存。**

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段 | 工具 | 新鲜证据层 | 数据惩罚 |
|---:|---|---:|---|---|---|---|---|
| 1 | **FU2611 夜盘回撤条件多** | **79** | 多，1–5D | 条件试仓 | 期货；手工核价后Call Spread | **4**：price/OI、curve、20:02海外、T日期权 | Physical缺；exec=false；高开追价风险 |
| 2 | **AG2610 夜盘回撤条件多** | **76** | 多，1–5D | 条件试仓 | 期货；手工核价后Call Spread | **3**：price/OI、海外宏观、T日期权 | curve样本不足；IV很贵；19:01后无更晚可信快照 |
| 3 | **FG701 失败反弹条件空** | **74** | 空，1–5D | 条件试仓 | 期货；手工核价后Put Spread | **3**：price/OI、curve、T日期权 | Physical仅水平；动态保证金/限价未确认 |
| 4 | **BU2610 能源趋势条件多** | **73** | 多，1–5D | 条件单 | 期货 | **4**：price、curve、海外、T日期权 | 价涨仓减；与FU重复同因子 |
| 5 | **EC2610 极端动量观察** | **69** | 观察多，1–3D | 观察 | 下一确认日盘期货 | **2**：price/OI、curve | 海外非同口径；无Physical/Options闭环；当天过热 |

评分拆解（逻辑25 / 赔率凸性25 / 催化20 / 价格curve/vol15 / 拥挤持仓技术15）：
- FU：22 / 19 / 17 / 13 / 8 = **79**
- AG：21 / 17 / 16 / 12 / 10 = **76**
- FG：21 / 18 / 14 / 12 / 9 = **74**
- BU：20 / 16 / 16 / 12 / 9 = **73**
- EC：19 / 15 / 15 / 10 / 10 = **69**

**没有80+确认交易。** 风险偏好高不能突破数据与证据纪律；四层证据只意味着允许更高置信度，不意味着必须追价。

## 七、前三名交易卡

### 1) FU2611｜条件多｜79

**事实**：close 3845、settle 3850；1D +2.12%、5D +9.81%；ΔOI +8.58%；Backwardation +7.47%、z +1.70；T日2026-10-19期权ATM IV约43.0%，RV20约37.93%，surface-ready=true、execution-ready=false。20:02 BJT Reuters：Brent约93.97、WTI约86.97，均由17:49的日内下跌转为小幅上涨。  
**市场定价**：供应风险溢价很高，国内curve仍紧；20:02外盘转强会提高21:00 gap-up概率。  
**推断**：真正赔率来自**高开/回撤后仍被承接**，而不是“消息更强所以追得更高”。  
**主观判断**：这是今晚最值得等的setup，但最差的执行方式就是21:00第一跳直接追多。  
**市场可能错在哪里**：Hormuz/伊朗风险突然缓和、海外原油重新转跌、国内Backwardation快速压缩。

- **入场**：21:00后至少等30分钟，优先30–45分钟。3810–3850区域守住，回到/接受3850上方；若直接高开，则等首次回撤不破开盘VWAP后再看。
- **分批**：1/3风险试仓；45分钟后仍在VWAP上方且重新创新高才加第二笔；除非4层证据继续一致，不做第三笔。
- **初始止损**：有效跌破3810且curve同步压缩，或Brent重新显著转弱。
- **逻辑失效**：价格继续涨但Backwardation快速压缩、OI明显撤退；或地缘供给风险出现可信缓和。
- **TP1/TP2**：TP1 +1R；TP2 +2R，或Backwardation较当前收窄约1/3时主动减/退。
- **时间止损**：2个交易时段无延续即撤。
- **最大损失**：0.35%–0.50% NAV；FU+BU初始合并≤0.75% NAV。
- **1–20D催化**：伊朗制裁/封锁细节、Hormuz流量、EIA库存、俄炼厂扰动。
- **最坏情景**：夜盘高开后地缘缓和+原油跳水，国内多头拥挤反转；涨跌停/流动性收缩使止损失真。
- **期权替代**：仅在逐strike报价人工核实后，用2026-10-19 Call Spread，长腿约35–45Δ、短腿约15–25Δ；`execution_ready=false`，不写净权利金。
- **合约参数**：10吨/手；tick 1元/吨；tick value 10元；按settle名义约38,500元/手。SHFE 2026-06-23可核实通知：FU2611涨跌停14%、套保保证金15%、一般保证金16%；券商保证金未确认。夜盘21:00–23:00。最后交易日为交割月前一月最后交易日，具体日历日执行前复核；实物/保税燃料油交割。
- **压力**：1个14%约5,390元/手；两个连续同向14%复合约11,535元/手，未计保证金上调/滑点。
- **放弃条件**：高开后30分钟无法守住日盘结算区；Brent再度快速转跌；curve明显走平。

### 2) AG2610｜条件多｜76

**事实**：close 16771、settle 16611；1D +3.11%、5D +5.45%；ΔOI +1.46%。T日2026-09-23 series：ATM 16600、ATM IV 47.265%、RR25 +7.81、BF25 +1.93；surface-ready=true、positioning-ready=false、execution-ready=false。19:01 BJT Reuters：银69.48、+2.0%；金4587.23、+1.5%；DXY约98.65、近三个月低位。  
**市场定价**：方向强，但Vega非常贵，call skew也偏贵。  
**推断**：只有夜盘回撤仍守16600/16611、再接受16770，才说明外盘强势未被中国日盘完全price-in。  
**市场可能错在哪里**：美元反弹、长端收益率再冲高、银价快速回吐、国内高开透支。

- **入场**：等15–30分钟；16600/16611守住，随后重新站稳16770附近，海外银不反转。
- **分批**：1/3试仓；30–45分钟仍在VWAP上且创新高才加。
- **止损/失效**：30分钟接受于16600下方并伴海外银明显回吐；若快速接近日盘低点16201，直接放弃。
- **TP1/TP2**：+1R / +2R或移动止盈；若IV继续升而期货不创新高，优先锁利润。
- **时间止损**：1–2个夜/日盘无新高即撤。
- **最大损失**：0.35%–0.55% NAV。
- **催化**：美元/美债长端、Jackson Hole预期、贵金属技术突破与仓位再配置。
- **最坏情景**：高开追多遇美元/收益率反向，期货和IV同时回落。
- **期权替代**：手工核价后2026-09-23 Call Spread，长35–45Δ、短15–25Δ；不裸买高IV ATM Call。
- **合约参数**：15kg/手；tick 1元/kg；tick value 15元；按close名义约251,565元/手。最近可核实SHFE风险参数：涨跌停14%、套保保证金15%、一般保证金16%；券商保证金未确认。夜盘21:00–02:30。最后交易日按规则为交割月15日，即AG2610为2026-10-15；实物交割。
- **压力**：1个14%约35,219元/手；两个连续14%复合约75,369元/手。
- **放弃条件**：高开约2%以上且无回撤承接；DXY快速反弹；海外银转跌；30分钟接受16600下。

### 3) FG701｜条件空｜74

**事实**：close 907、settle 906；1D -1.09%、5D -3.10%；ΔOI +10.21%；Contango -3.35%。周度企业库存7441.4重量箱只是最新绝对水平，不计Physical方向层。T日2026-12-11期权ATM 910、ATM IV 23.055%、RR25 +7.72、BF25 +1.315；surface-ready=true、positioning-ready=true、execution-ready=false。  
**市场定价**：弱价格+扩仓+Contango重新形成压力组合。  
**推断**：最好的空点是反弹失败，不是900附近追破位。  
**市场可能错在哪里**：需求/库存出现真正拐点，或政策驱动建材快速修复。

- **入场**：21:00后至少等30分钟；反弹910–918失败、不能站稳今高918附近，且Contango不明显收窄时试空。
- **分批**：先1/3；重新跌破899再加。
- **初始止损**：30分钟有效站稳920上方。
- **逻辑失效**：curve显著收窄且价格转强；或出现可验证的库存下降/需求改善。
- **TP1/TP2**：899 / 880附近或+2R，以先到者为准。
- **时间止损**：2个交易日不破899即撤。
- **最大损失**：0.25%–0.40% NAV。
- **最坏情景**：政策/产业消息引发跳空反弹，空头流动性恶化。
- **期权替代**：人工确认流动性后Put Spread；`execution_ready=false`，不提供权利金或精确成交strike。
- **合约参数**：20吨/手；tick 1元/吨；tick value 20元；按settle名义约18,120元/手；夜盘21:00–23:00。最后交易日为交割月第10个交易日，具体日期进入交割月前复核；实物交割。**当前动态保证金与涨跌停参数未确认**，不拿旧参数或其他合约参数代填。
- **压力**：因当前动态涨跌停未确认，不虚构1/2板金额；风险预算以账户级最大损失硬限制。
- **放弃条件**：开盘直接跌破899不追；反弹站稳920；出现新的可验证Physical反向变化。

## 八、商品期权专项

T日期权研究层已经可用，执行层仍关闭。以下是**直接复核代表series**，不声称“全市场最高/最低”：

| Series | ATM IV | RV20 | IV-RV | RR25 / BF25 | Readiness | 结构含义 |
|---|---:|---:|---:|---|---|---|
| AG2610 2026-09-23 | 47.27% | 30.82% | **+16.45 vol** | +7.81 / +1.93 | surface Y / pos N / exec N | Call skew贵；方向多更偏Call Spread而非裸Call |
| FU2611 2026-10-19 | ~43.0% | 37.93% | **+5.07 vol** | 已有surface，细值不重复 | surface Y / exec N | 事件凸性仍有价值，但不能追高Vega |
| FG701 2026-12-11 | 23.06% | 16.20% | **+6.86 vol** | +7.72 / +1.315 | surface Y / pos Y / exec N | 做空优先有限风险Put Spread |
| LC2701 | ~35.37% | ~27.19% | **+8.18 vol** | surface可用 | surface Y / exec N | 高IV不是看涨确认；curve仍Contango |
| OI701 | **~12.90%** | 未在本表复核同口径RV | — | surface可用 | surface Y / pos N / exec N | 只是复核样本中的低IV，不称全市场最低 |

- **Event convexity**：能源地缘事件仍最有凸性价值，但FU的IV已高于RV；若做方向，有限风险spread优于无限gap风险的裸期货，但必须先确认真实bid/ask。
- **Skew**：AG与FG的RR25明显为正，说明call wing相对更贵；AG追买call尤其需要控制Vega/Theta。
- **Positioning**：只有70/368 series达到positioning-ready，不能由局部OI/PCR推断“全市场拥挤”。
- **Execution**：0/368 execution-ready，禁止写精确净支出、成交滑点或dealer gamma方向。
- **Vol RV**：当前没有同时满足跨品种流动性、执行报价和风险口径的正式vol RV交易；保留研究，不建仓。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国日盘settle | 15:00–19:30海外映射 | 19:30后增量 | 预期开盘 | 置信度 | 是否追价 | 等待 | 开盘后确认 |
|---|---:|---|---|---|---|---|---|---|
| **FU2611** | 3850 | 17:49 Brent/WTI约-0.5% | **20:02已转约+0.2%/+0.16%** | 小幅高开概率上升 | 中高 | **否** | 30–45m | 3850接受、3810支撑、VWAP、curve、Brent是否继续强 |
| **AG2610** | 16611 | 19:01银+2.0%、金+1.5%，美元弱 | 无更晚可信快照 | 偏高开 | 中高 | **否** | 15–30m | 16600/16611、16770再接受、海外银不反转 |
| **BU2610** | 4526 | 17:49原油略弱 | 20:02原油转正 | 小高/偏强 | 中 | 否 | 30–45m | 4526附近接受、curve、海外油 |
| **FG701** | 906 | 无直接海外锚 | 无 | 平/偏弱 | 中低 | 否 | 30m | 910–918失败、899、OI/curve |
| **MA610 / EG2610** | 2880 / 5159 | 原油间接映射 | 20:02油价转正 | 混合至小高 | 低中 | 否 | 30–45m | 自身VWAP、curve、首小时OI |
| **EC2610** | 1885.5 | 航运地缘背景强，但非同口径欧线锚 | — | **夜盘未确认** | — | — | — | 下一确定窗口2026-08-24 09:00，不追周五极端涨幅 |
| **LC2701** | 156360 | 无可靠实时进口平价 | — | **夜盘安排未确认** | — | — | — | 下一确定窗口2026-08-24 09:00处理 |

关键纪律：即使FU/BU高开，也**不能把20:02海外上涨写成“中国期货已经上涨”**。夜盘第一跳只提供gap信息，不提供趋势确认；能源至少等30分钟，最好45分钟。

## 十、未来24h / 7d事件日历（北京时间）

- **2026-08-22 03:00**：USDA NASS Cattle on Feed、Milk Production、Peanut Prices等（美东8月21日15:00）。对玉米/豆粕/饲料和LH的边际需求预期有影响；不建议数据前裸露大Delta。
- **2026-08-22 03:30**：CFTC COT（美东周五15:30；持仓截至此前周二）。只作仓位背景，不能当实时仓位。
- **2026-08-25 03:00**：USDA Cold Storage、Chickens and Eggs；关注畜牧/饲料库存与需求映射。
- **2026-08-25 04:00**：USDA Crop Progress；天气/优良率变化是谷物油籽的方向催化。
- **2026-08-26 22:30**：EIA Weekly Petroleum Status Report（常规周三10:30 ET）。FU/SC/LU/BU若已有盈利，数据前降低Delta而非加杠杆。
- **2026-08-27至29**：Jackson Hole Economic Policy Symposium，主题“Financial Innovation: Implications for Payments and Policy”；具体重要发言时点需等官方议程。AG/AU对美元与实际利率的Vega会放大。
- **持续24h/7d**：美国对伊朗进一步制裁/封锁细节、Hormuz通行量、俄炼厂与中东供应中断。SC/FU/LU/BU本质是同一地缘能源因子，必须合并计算风险。
- **交易所/到期**：前三交易合约均未进入临近最后交易日5–10交易日的普通curve禁用区，但AG/FU/FG执行前仍复核最新交易所风险参数与临近交割规则。

## 十一、固定回答、风险预算与行动

- **是否值得新增风险**：值得，但只值得条件试仓；不值得21:00首跳追价。
- **最强/最弱产业链**：最强能源，最弱FG建材；贵金属强但IV更贵；EC最过热。
- **当前regime**：能源供应风险重新同步偏强 / 贵金属高IV强势 / 建材弱势增仓 / 航运极端动量 / 新能源高波动反弹。
- **price是否获curve确认**：FU是；FG空头是；AG不是；LC多头不是；EC的curve受近月效应污染。
- **库存/实体确认**：大多数没有；FG只有库存绝对水平，不能自动算确认。
- **境内外是否同向**：能源到20:02重新同向偏强；AG与海外金银仍同向；EC无同口径海外锚。
- **人民币/美元作用**：美元弱支持AG/AU；仓库USDCNH为较早EOD context，本次不虚构19:30人民币精确贡献。
- **期权是否优于裸期货**：结构上能限制gap，但`execution_ready=false`；只有交易时段手工核价后才能判断真实赔率。
- **跨期/跨品种/跨市场RV**：没有满足完整口径的正式套利；FU curve是方向证据，不是“无风险跨期”。
- **单日噪音/过热**：SP单日强但Contango；LC price/OI强但curve不确认；EC不是普通噪音但已极端过热。
- **应等30–45分钟**：FU、BU、FG、MA、EG；AG至少15–30分钟。
- **不值得交易**：21:00追首跳、裸卖商品Vega、无bid/ask时硬做精确期权结构、用C级basis/库存绝对水平包装套利。

风险预算：单一试仓0.25%–0.75% NAV；FU 0.35%–0.50%，AG 0.35%–0.55%，FG 0.25%–0.40%。若FU/AG/FG同时触发，初始合并风险≤1.0%–1.25% NAV；FU+BU初始合并≤0.75%。单一高确信主题总风险≤2.5%–3.0%。压力测试至少包含1/2个涨跌停、夜盘gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、人民币急变和中国休市期间海外剧烈波动。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：FU2611回撤确认多、AG2610回撤确认多、FG701失败反弹确认空、BU2610能源趋势条件多。  
C. 今天应继续观察的机会：EC2610极端动量但不追、LC2701高活跃上涨但Contango、RM/M价格与curve冲突。  
D. 今天必须避免或退出的交易：21:00追首跳、裸买AG高IV或裸卖商品Vega、在execution-ready=false时硬做精确期权结构、把C级basis/库存水平当套利、FU/BU重复叠加同一能源因子。

## 来源

- China-Commodities-Engine：<https://github.com/farfromexact/China-Commodities-Engine>
- Reuters 2026-08-21 Oil：<https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/>
- Reuters 2026-08-21 Gold/Silver：<https://www.reuters.com/business/gold-steadies-heads-third-straight-weekly-gain-2026-08-21/>
- Reuters 2026-08-21 Dollar：<https://www.reuters.com/business/dollar-wobbles-investors-balk-us-treasurys-rescue-efforts-2026-08-21/>
- Reuters 2026-08-21 Iranian oil / China buyers：<https://www.reuters.com/business/energy/iranian-oil-offers-chinese-buyers-fall-us-blockade-bites-sources-say-2026-08-21/>
- SHFE FU风险参数通知（2026-06-23）：<https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html>
- SHFE黄金白银风险参数通知（2025-10-17）：<https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html>
- CFTC COT Release Schedule：<https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm>
- USDA NASS 2026-08 Calendar：<https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=08&view=l&year=2026>
- EIA WPSR Schedule：<https://www.eia.gov/petroleum/supply/weekly/schedule.php>
- Kansas City Fed Jackson Hole 2026：<https://www.kansascityfed.org/research/jackson-hole-economic-symposium/>
