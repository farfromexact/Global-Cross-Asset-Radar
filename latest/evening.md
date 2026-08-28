# 全球跨资产高风险机会雷达｜晚间版

## 2026-08-28｜周五｜北京时间20:00｜Revision 1

**今天究竟有没有值得冒险的机会：有，但不是追A股小盘，也不是追NVIDIA。当前最优是“日元升值凸性（USD/JPY Put Spread）”与“成品油稀缺/中性原油Beta”；黄金等待22:00 Warsh确认。昨日Long IM/Short IH条件交易已经失效，今天明确撤销。**

> 数据切点：A股/CFFEX为2026-08-28完整收盘；美国现金股市尚未开盘，股票使用2026-08-27完整收盘及8/28盘前数据；美国国债使用8/27财政部完整收盘并辅以8/28 Reuters盘中；商品/FX使用8/28 Reuters盘中。China-Options-Engine `data/radar_latest.json` 已刷新至8/28 18:00、CFFEX期权686/686官方匹配；`data/radar_history.json` 仍为空，因此3/5日用审计快照重建，20日仅保留同一Sep合约审计口径，不伪装成精确rolling window。

## 一、今日一句话结论

**混合Risk-on/事件前去风险：AI基本面强、油价风险溢价回落，但Warsh前美元/美债偏紧；A股小盘现金流入与期指大减仓背离，今日中国股指无合格交易。**

## 二、隔夜/国内市场仪表盘

| 资产 | 最新值 | 单日变化 | 一周变化 | 当前信号 | 数据时间/属性 |
|---|---:|---:|---:|---|---|
| UST 2Y | 4.20% | +1bp | 约-4bp | 前端仍定价加息风险 | 8/27 Treasury完整收盘 |
| UST 10Y | 4.67% | +1bp | 约-6bp | 高位但本周回落 | 8/27 Treasury完整收盘；8/28 Reuters约4.68% |
| UST 30Y | 5.19% | +1bp | 约-8bp | 期限溢价/财政供给仍高 | 8/27 Treasury完整收盘；8/28 Reuters约5.20% |
| 10Y实际利率 | 2.34% | 0bp | — | 对黄金/成长股仍属高压 | 8/27 Treasury real curve |
| 2s30s | +99bp | 0bp | 约-4bp | 曲线仍陡但近期被前端鹰派压制 | 8/27官方收盘计算 |
| 10Y BEI | 约2.33% | — | — | 通胀风险未消失 | 4.67%-2.34%，同日估算 |
| DXY | 99.18 | 约持平 | 周线偏强 | Warsh前美元偏硬 | 8/28 Reuters盘中 |
| EUR/USD | 1.1647 | 小幅变动 | 周线偏弱 | 美元利差仍占优 | 8/28 Reuters盘中 |
| USD/JPY | 约159.5 | 小幅变动 | — | 逼近政策干预敏感区 | 8/28 Reuters；日本过去月干预¥15.4tn |
| Nasdaq Composite | 26,541.35 | +1.57% | 约+1.4% | AI财报驱动Risk-on | 8/27完整收盘；8/28 NQ期货约-0.3%盘前 |
| SMH | 573.00 | +3.10% | +2.24% | 半导体强，但盘前降温 | 8/27完整收盘 |
| Brent | $89.66/bbl | 近持平 | -5.1% | 地缘风险溢价回吐 | 8/28 17:43 BJT附近 Reuters盘中 |
| WTI | $83.21/bbl | -0.38% | -4.5% | 同上 | 8/28 Reuters盘中 |
| 现货黄金 | $4,606.73/oz | +0.1% | — | 高real yield/强美元下仍韧 | 8/28 18:32 BJT Reuters盘中 |
| COMEX黄金 | $4,660.10/oz | 近持平 | — | 等Warsh定方向 | 8/28 Reuters期货盘中 |
| VIX | 14.51 | -4.6% vs 8/26 15.21 | — | 宏观事件前保护偏便宜 | 8/27 Cboe完整收盘 |
| MOVE | 约73.4 | — | — | **陈旧值，不作为入场依据** | 8/21延迟数据，未确认8/28 |
| US HY OAS | 2.67% | -3bp vs 8/25 | -3bp vs 8/21 | 信用未确认Risk-off | 8/26 ICE/FRED完整收盘 |
| IH2609 / 上证50 | 2911.4 / 2923.33 | 期货close-to-close -0.09%；现货-0.24% | 5D期货+1.76% | 轻度去风险 | 8/28 CFFEX/现金收盘 |
| IF2609 / 沪深300 | 4593.6 / 4609.18 | -0.24%；现货-0.46% | 5D+0.38% | 大盘弱于IH | 8/28收盘 |
| IM2609 / 中证1000 | 7666.6 / 7705.03 | -0.26%；现货-0.36% | 5D+1.85% | **昨日fresh-long确认被OI大减仓推翻** | 8/28收盘 |
| IH/IF/IM主力基差 | -0.408% / -0.338% / -0.499% | 均较昨日收敛 | — | IF基差最强，IM不再具备明显优势 | 8/28收盘；未扣股息/carry |
| HO/IO/MO 2609 ATM IV | 13.95% / 16.85% / 26.47% | -0.51 / -0.86 / -1.18 vol | 多周期方向仍向下 | 周末前vol继续被卖 | 8/28 EOD |

## 三、相比昨天真正发生了什么变化

1. **昨日中国第一名交易被证伪。** IM2609今天仅小跌，但主力OI从245,325降到230,428，单日-14,897（-6.1%）；IC也-7,976。昨日IM“上涨+增仓”的fresh-long结构没有延续，今天更像周末/事件前获利了结与去杠杆，而不是新空单大举建立。
2. **现金ETF与期指发生真正的跨市场背离。** 510500份额变化估算约+18.51亿元、512100约+5.32亿元，而510050约-10.22亿元、510300约-12.84亿元；即现金一级市场仍偏中小盘，但期指小盘OI被大幅削减。结论不是“转空小盘”，而是**不应该隔夜追Long IM/Short IH**。
3. **中国波动率继续压缩，但小盘尾部保险没有消失。** MO2609 ATM IV降至26.47%，RR25从-3.23vol修复到-2.69vol；然而put OI仍+3,779，高于call OI +1,701，8000仍是最大Gamma节点。多头风险偏好与尾部保护同时存在。
4. **全球油价风险溢价本周明显回吐，但精炼品物理紧张没有同步消失。** Brent/WTI周跌约5.1%/4.5%，Hormuz流量部分恢复但仍低于10日均值；欧洲柴油利润率接近纪录、俄罗斯出口限制与炼厂受损使产品端比原油端更紧。
5. **AI从“需求是否存在”切换成“谁能把需求变成现金流”。** NVIDIA财报使AI需求周期延长，但NVIDIA暂停部分给AI云公司的信用/收入分成安排，MRVL强长期故事却因收入兑现时间盘前跌约8%。这正强化“Long现金流质量 / Short融资-Capex Beta”，而不是全面追半导体Beta。
6. **日元政策不对称突然上升。** 日本财务省确认7/30—8/26累计干预¥15.4万亿（约$96.5bn），USD/JPY仍在159.5附近。说明单纯做空USD/JPY现货并不容易，但**有限损失的日元升值凸性**现在比裸方向更有赔率。

## 四、机会排行榜

| 排名 | 机会 | 总分 | 逻辑/25 | 赔率凸性/25 | 催化/20 | 价格波动/15 | 拥挤技术/15 | 阶段 | 工具 | 最大损失有限 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | USD/JPY下行凸性（Long JPY） | **93** | 25 | 24 | 19 | 12 | 13 | Warsh前微仓/讲话后确认 | 2-6W USDJPY Put Spread / Put Fly | 是 |
| 2 | ULSD/Gasoil成品油稀缺 / 中性原油Beta | **92** | 25 | 23 | 18 | 13 | 13 | 条件试仓 | Oct/Nov Call Spread + 部分Brent hedge | 是 |
| 3 | 黄金3-6M政策信用Call Spread | **90** | 24 | 24 | 20 | 10 | 12 | 22:00后确认 | Dec-26/Feb-27 Call Spread/Fly | 是 |
| 4 | Long AI现金流质量 / Short融资-Capex Beta | **88** | 24 | 23 | 18 | 11 | 12 | 美股开盘后确认 | 30-60D双腿Debit Spreads | 是 |
| 5 | Warsh鹰派条件下2s30s战术flatten | **82** | 22 | 19 | 18 | 11 | 12 | 观察 | DV01中性曲线/期权结构 | 可设计为有限风险 |

**今日中国股指无合格交易，评分81。** 最接近触发的是“重新Long IM/Short IH”，但必须等周一PMI后看到IM/IC OI重建、512100/510500 creation继续、MO skew不重新恶化，才恢复资格。

## 五、前三名交易卡

### 1）USD/JPY 2—6周 Put Spread｜Long JPY凸性｜93

**核心逻辑（事实）：** 日本一个月内已投入¥15.4tn干预，美元兑日元仍约159.5；BOJ 9月加息概率上升，Warsh今晚22:00又是美元利差催化剂。**市场错误定价（判断）：** 现货告诉你干预效果不持久，但这恰恰使“直接空美元兑日元”赔率一般；期权的下行凸性则同时拥有政策尾部与Fed意外偏鸽两个催化。

**表达：** 2—6周USD/JPY，买约35Δ Put、卖约15Δ Put；若下侧skew极贵则改Put Butterfly。不开裸空现货、不裸卖Call。完整FX IV/skew报价未同步，因此不虚构权利金。

**入场：** Warsh前只允许最大损失NAV 0.25%的微仓；主仓等22:00后，若USD/JPY测试160附近失败，或跌破159.20后30分钟不能回到159.80以上，开1/3；跌破158.50加1/3；余下仅在DXY同步转弱或日本出现新增干预信号时加。

**失效：** 日线站稳161.50以上，且美日利差继续走阔、日方不再口头/实际干预；硬退出在162.5附近或vertical剩余价值低于初始debit的35%。**止盈：** TP1 157.0或spread约1.8x debit；TP2 154.5—155.0或2.5x debit/达到理论最大价值70%—80%。**Greeks：** -USDJPY Delta、+Gamma、+Vega、-Theta。**最不利情景：** Warsh强鹰+美国前端收益率跳升+日本选择暂不再干预；最大损失为净debit。

### 2）ULSD/Gasoil 1—2个月 Call Spread + Brent Beta Hedge｜92

**核心逻辑：** 原油周跌4.5%—5.1%，表明谈判/航运恢复压低headline premium；但Hormuz流量仍低于正常、俄罗斯柴油出口受限、欧洲柴油炼厂利润率接近纪录，产品端物理短缺比原油端更硬。**市场错误定价：** 把“原油地缘溢价下降”等同于“成品油供给压力解除”。

**表达：** Oct/Nov-2026 ULSD或ICE Gasoil买30—40Δ Call、卖10—15Δ Call；若需要，把初始Delta的30%—50%用Brent空头对冲，目标是产品scarcity而不是油价大方向。完整ULSD/Gasoil IV/skew未同步，不给虚构strike/premium。

**入场：** 仅当美国能源时段产品裂解/相对Brent仍强、Brent不突破90.5追涨时开1/3；若Brent回落但产品价差不收窄加1/3；EIA/航运数据再次确认短缺后完成。**失效：** Hormuz流量持续恢复到常态、俄罗斯出口禁令解除/炼厂恢复，同时两期EIA馏分油明显累库；或产品相对Brent连续两个交易日显著走弱。**止盈：** 1.6x debit、2.3—2.5x debit。**Greeks：** +Delta/+Gamma/+Vega/-Theta，Brent hedge压低净原油Beta。**最大损失：** 净期权debit；试仓0.25%—0.50% NAV。

### 3）黄金3—6个月政策信用Call Spread / Call Fly｜90

**核心逻辑：** 10Y real 2.34%、DXY约99.18仍高，但黄金仍在$4,606附近，说明“财政/货币政策信用保险”没有失效；同时Treasury 7Y拍卖4.512%轻微tail、间接投标偏弱，长端供给问题仍在。**市场错误定价：** 市场仍主要用实际利率解释黄金，而黄金对财政政策干预与美元信用风险的弹性已提高。

**表达：** 按当日$4,607现货/$4,660 COMEX重新选：Dec-26或Feb-27买30—35Δ Call、卖10—15Δ Call（大致103%—106% / 112%—118% moneyness）；若上翼IV很贵，用Call Fly。**不机械沿用昨日4800/5200。**

**入场：** 22:00 Warsh后满足任一条件才加仓：A）10Y/30Y与DXY上涨但gold守住4580—4600；B）10Y>4.72%但gold突破4640—4660，形成“坏利率上升”背离；C）Warsh偏鸽导致DXY跌破99且gold站回4660。**失效：** gold<4520同时DXY>99.8且10Y real>2.40%；硬退出<4480。**止盈：** 4750、5000或spread达到理论最大值70%—80%。**Greeks：** +Delta/+Gamma/+Vega/-Theta。最大损失为净debit，试仓0.25%—0.50% NAV；与空长债/空美元等政策信用仓合并计风险。

## 六、黄金专项跟踪

**结论：不变偏增强，但必须等Warsh验证。** 8/27 10Y名义4.67%、10Y real 2.34%、DXY 8/28约99.18，传统模型对黄金并不友好；黄金仍守在4600上方，说明信用保险权重存在。7Y拍卖轻微tail且海外间接需求低于近期均值，使“财政供给/政策干预”仍是独立因子。若今晚出现“长端利率上、美元上、黄金也上”，这是最强的政策信用确认；若黄金随real yield和美元同步下跌，则该叙事应降权。

ETF当日资金、完整COMEX IV/skew和最新CFTC仓位在本次切点无法同步高质量确认，因此不把它们写成实时事实。优先结构仍为3—6M Call Spread/Fly；微型黄金期货只在突破确认后作为第二层仓位，不能替代有限损失期权核心仓。

## 七、AI股票专项跟踪

**状态：基本面需求确认 + 现金流/融资质量分化加剧。** 8/27 Nasdaq +1.57%、SMH +3.10%、NVIDIA +8.7%，说明AI需求担忧被财报显著缓解；但8/28盘前NQ约-0.3%、NVIDIA约-0.5%、MRVL约-8%。更关键的是NVIDIA暂停部分AI云信用支持/收入分成安排，说明“谁融资、谁承担利用率风险”正在被市场重新审视。

因此不做“所有AI都多”。首选30—60D：多有现金流、定价权、短期订单可见度的AI龙头Call Spread，同时用融资依赖/远期Capex Beta的Put Spread做Beta调整。触发：美股开盘60—90分钟后质量篮子相对融资Beta跑赢>=0.75pct且SOXX/SMH守住opening range；失效：融资Beta在利率下降背景下反超>1.5pct，或龙头财报后的订单/FCF优势被后续数据否定。TP相对收益+5%/+10%；最大损失为双腿debit之和。

## 八、中国50/300/1000专项跟踪

**今天更适合IH、IF还是IM？** 如果只选绝对方向，今天都不值得隔夜建仓；若必须排序，**IF的基差最健康（-0.338%）但价格趋势最弱，IM中期趋势最强但今日去杠杆最重**。所以答案不是“选一个做多”，而是等待结构重新确认。

| 指标 | IH2609 | IF2609 | IC2609 | IM2609 |
|---|---:|---:|---:|---:|
| 收盘 | 2911.4 | 4593.6 | 7853.8 | 7666.6 |
| CFFEX结算口径日变 | +0.02% | -0.16% | -0.32% | -0.03% |
| Close-to-close | -0.09% | -0.24% | -0.62% | -0.26% |
| Volume | 22,615 | 48,813 | 82,901 | 134,286 |
| OI | 67,042 | 140,177 | 151,720 | 230,428 |
| OI变化 | -1,726 | -2,703 | -7,976 | **-14,897** |
| 主力基差 | -0.408% | **-0.338%** | -0.528% | -0.499% |
| 次月-主力 | -15.8 | -28.0 | -55.8 | -61.0 |
| ETF creation/redemption估算 | 510050 -10.22亿 | 510300 -12.84亿 | 510500 +18.51亿 | 512100 +5.32亿 |

**价格多周期（同一Sep合约审计口径）：** 1D IH/IF/IC/IM分别-0.09/-0.24/-0.62/-0.26%；3D +1.97/+1.59/+2.84/+2.68%；5D +1.76/+0.38/+1.18/+1.85%。20D因`radar_history.json`为空，不能给伪精确rolling值；沿用截至8/27的同合约审计基线并叠加今日后，IH约+0.89%、IF约+1.89%、IM约+12.0%，仅用于趋势背景。

**期权：** HO/IO/MO ATM IV 13.95/16.85/26.47%，1D分别-0.51/-0.86/-1.18vol；RR25 +0.13/-1.92/-2.69vol；BF25 +0.75/+0.85/+1.15vol；PCR(OI) 0.664/0.748/0.811。10Δ Put IV分别16.72/20.84/31.28%，MO尾部仍最贵。Gamma主节点HO 2900、IO 4600、MO 8000，与昨日主节点基本未迁移。IM-MO forward差仅约+0.011%，IH-HO和IF-IO也接近零，暂无明显期指-期权forward错价。

**风格判断：** 3D/5D仍偏小盘，但8/28期货OI的剧烈下降意味着昨日fresh-risk信号未延续；现金ETF creation却偏中小盘，因此不是明确的大小盘反转，而是“现金配置继续、杠杆资金周末前收缩”。**今日中国股指无合格交易。** 最接近触发：周一PMI后，IM/IC OI重新增加、512100/510500 creation延续、IM基差保持>-0.6%、MO ATM IV不重新冲破28%且RR25>-3.5vol；满足后再考虑MO Call Spread + HO Put Spread表达Long IM/Short IH。

## 九、今日事件日历（北京时间）

| 时间 | 事件 | 风险动作 |
|---|---|---|
| **8/28 22:00** | Fed Chair Kevin Warsh Jackson Hole讲话 | 黄金/USDJPY/美债：讲话前降低裸Delta，保留有限损失Gamma；不要裸卖波动率 |
| 8/28 22:00 | BLS CES 2026年3月基准初步修订 | 若就业历史被大幅下修，前端利率与USDJPY下行凸性受益；与Warsh同窗，避免单因子过仓 |
| **8/31 09:30附近** | 中国8月官方PMI（惯例时间，最终以NBS发布为准） | A股风格交易等数据后30—45分钟，不周末预埋大Delta |
| **9/1 22:00** | 美国7月JOLTS + ISM制造业8月 | AI/长债/美元风险集中，期权仓保留凸性、减少裸期货 |
| **9/2 22:30** | EIA Weekly Petroleum Status Report | ULSD/Gasoil仓前不提前加满；若馏分油累库+crack转弱则减仓 |
| **9/3 20:30** | 美国7月国际贸易 | 美元/增长定价次级催化 |
| **9/4 20:30** | 美国8月非农就业 | 本周最大宏观尾部；9/3后主动降低净Delta，优先保留有限风险期权 |

未来7天无主要CFFEX股指/指数期权到期；下一主要HO/IO/MO与IH/IF/IC/IM 2609到期日为9/18。

## 十、今日行动清单

**A. 今天可以立即建立的仓位：** 仅允许0.25% NAV最大损失的USD/JPY 2—6W Put Spread微仓；不做裸JPY方向，主仓等22:00。  
**B. 今天只应挂条件单的仓位：** ULSD/Gasoil Call Spread（产品相对Brent确认）；Warsh后Gold 3—6M Call Spread；美股开盘后AI质量/融资Beta双腿Debit Spread。  
**C. 今天应继续观察的机会：** 周一PMI后的IM/IC OI重建与ETF creation、2s30s对Warsh的反应、MRVL与NVIDIA/SMH的相对强弱。  
**D. 今天必须避免或退出的交易：** 撤销昨日Long IM/Short IH条件单；避免裸卖期权、Warsh前大额裸黄金/美元/美债方向、headline驱动追WTI，以及把黄金+空长债+空美元或多IM+小盘Call重复计成独立风险。

## 风险预算

单一试仓最大损失NAV 0.25%—0.75%；单一确认交易0.75%—1.50%；高确信度主题总风险<=2.5%—3.0%。因子合并：Gold/short long Treasury/short USD/long BEI归为同一美国政策信用/实际利率因子；USDJPY Put与Gold在Warsh偏鸽情景下有共同美元因子，合计风险需折减；中国Long IM/Short IH、MO Call、1000ETF Call属于同一小盘Beta因子；AI质量多头、SMH/SOXX和中国小盘亦共享高Beta/real-yield暴露。

## 关键来源

- U.S. Treasury Daily Treasury Par Yield Curve, 2026-08-27: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve
- U.S. Treasury Daily Real Yield Curve, 2026-08-27: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve
- Reuters Global Markets, 2026-08-28: https://www.reuters.com/world/china/global-markets-global-markets-2026-08-28/
- Reuters Dollar/Warsh, 2026-08-28: https://www.reuters.com/world/asia-pacific/dollar-flat-near-one-week-high-investors-await-warshs-jackson-hole-debut-2026-08-28/
- Reuters Japan FX intervention, 2026-08-28: https://www.reuters.com/world/asia-pacific/japan-spent-record-965-billion-support-yen-over-past-month-ministry-data-shows-2026-08-28/
- Reuters Gold, 2026-08-28: https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/
- Reuters Oil, 2026-08-28: https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/
- Reuters Nvidia financing, 2026-08-27/28: https://www.reuters.com/business/nvidia-pauses-revenue-sharing-deals-with-ai-cloud-companies-wsj-reports-2026-08-27/
- Reuters Marvell, 2026-08-28: https://www.reuters.com/business/marvell-shares-slide-concerns-over-timing-google-ai-deal-revenue-eclipse-strong-2026-08-28/
- Cboe VIX, 2026-08-27 close: https://www.cboe.com/tradable-products/vix
- ICE BofA US HY OAS via FRED, 2026-08-26: https://fred.stlouisfed.org/data/BAMLH0A0HYM2
- EIA WPSR, release 2026-08-26 / next 2026-09-02: https://www.eia.gov/petroleum/supply/weekly/
- BLS release calendar: https://www.bls.gov/schedule/2026/
- ISM report calendar: https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/
- BEA release calendar: https://www.bea.gov/news/schedule
- NBS PMI: https://www.stats.gov.cn/
- China-Options-Engine `data/radar_latest.json` @ main, date 2026-08-28
- China-Options-Engine `data/radar_history.json` @ main, **empty/unusable at this run**

**数据缺口：** `radar_history.json`为空；MOVE当日值、同步USD/CNH/DR007、CTA暴露、dealer net gamma、完整海外期权IV/skew/premium、黄金ETF当日流及最新完整CFTC仓位未在切点高质量确认。以上均未猜测。