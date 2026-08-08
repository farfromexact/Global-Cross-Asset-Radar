# 全球跨资产高风险机会雷达｜晨间补跑｜2026-08-08

> 数据截点：北京时间 2026-08-08 08:36；周末模式。美国采用 8 月 7 日完整收盘，中国采用 8 月 7 日经 CFFEX 验证的最新快照。China-Options-Engine `data_fresh=true`、官方期权 EOD 726/726 匹配；`previous_date=null`，因此不虚构 ΔIV、ΔOI、skew change 或 Gamma migration。

## 一、今日一句话结论

**值得保留凸性，但不值得周末持有大额裸 Delta：当前是 Risk-on / 增长担忧混合状态。弱就业压低加息预期，却与美股新高和信用利差偏紧并存；中国最有价值的是条件式 Long IM / Short IF，而不是直接追 IM。**

最大跨资产背离是：**美国增长信号明显降温，但风险资产仍把它解释成“Fed 更容易按兵不动”而不是衰退确认。** 7 月非农意外减少 2.3 万人，May/June 合计下修 10.3 万，9 月维持利率不变概率升至约 56%；同时 Nasdaq 8 月 7 日上涨 1.3%，S&P 500 创收盘新高。周末新增尾部则来自霍尔木兹：美国官员称伊朗—阿曼谈判接近协议，若兑现，油价周日晚存在明显 gap-down 风险。

## 二、市场仪表盘

| 资产 | 最新值/状态 | 1D | 1W | 信号 | 数据时间/属性 |
|---|---:|---:|---:|---|---|
| US 2Y | 4.245% | -4.2bp | 未核验 | 前端鸽化 | 8/7 Reuters |
| US 5Y | 本轮未取得可靠精确收盘 | — | — | 不编造 | — |
| US 10Y | 4.649% | -2bp | 未核验 | 下行，但长端仍高 | 8/7 Reuters |
| US 30Y | 约 5.21% | 日内下行后回吐部分跌幅 | 未核验 | 财政/期限溢价仍黏 | 本日既有市场快照；未二次取得原始页面 |
| 2s10s | +40.4bp | 约 +2bp steepening | — | 牛陡 | 由 2Y/10Y 计算 |
| 2s30s | 约 +96bp | 前端跑赢长端 | — | 陡峭化核心信号 | 由 2Y/30Y 近似计算 |
| 10Y real | 2.44% | — | — | 陈旧，不作为当日入场值 | FRED 可核最新为 7/27 |
| 10Y term premium | 约 0.87% | — | 上行背景 | 长端风险溢价不低 | NY Fed/FRED 模型，7/31 |
| DXY | 99.50 | -0.44% | -0.31% | 美元转弱 | 8/7 Reuters |
| EUR/USD | 1.1568 | +0.39% | +0.41% | 欧元受益 | 8/7 Reuters |
| USD/JPY | 157.56 | -0.57% | 约 +0.1% | 干预后仍高波动 | 8/7 Reuters |
| USD/CNH | 本轮未取得权威精确收盘 | — | — | 不编造 | — |
| Nasdaq Composite | 26,690.62 | +1.3% | +5.2% | Risk-on 延续 | 8/7 收盘 |
| SOXX/SMH | 精确收盘未可靠取得 | — | — | 半导体仍是指数高 Beta | 结合 8/7 科技板块表现 |
| WTI | $78.18/bbl | +1.15% | 周线明显回落 | 周末下行 gap 风险 | 8/7 结算 |
| Brent | $83.55/bbl | +1.3% | 约 -5% | 同上 | 8/7 结算 |
| Spot Gold | $4,347.29/oz | +2.55% | 约 +7% | 宏观凸性增强 | 8/7 Reuters |
| VIX | 8/7 精确收盘未可靠取得 | — | — | 不用旧值替代 | — |
| MOVE | 8/7 精确 EOD 未可靠取得 | — | — | 不用旧值替代 | — |
| HY OAS | 2.71% | -4bp vs 8/5 | 仍偏紧 | 信用未确认衰退 | FRED 最新可核 8/6 |

**利率联动。** 就业后 2Y 下行幅度大于 10Y，曲线偏牛陡；这与“Fed path 右移/暂停”一致，但 30Y 仍在约 5.2% 一带，说明财政供给、期限溢价和通胀尾部没有被弱就业完全消解。对交易而言，**方向性做多长债不如 2s30s steepener 干净**。

**美元/黄金。** DXY 跌至 99.50、黄金日涨 2.55%，是本轮最清晰的跨资产确认。黄金当前不是单纯“降息交易”，更像同时承载财政信用、真实利率下行预期和地缘风险的复合凸性资产。

**原油。** 8 月 7 日 Brent/WTI 当日反弹，但一周仍显著回落。更关键的是美国官员称伊朗—阿曼就霍尔木兹安排接近协议；如果周末出现正式、可执行的重开条款，**近端油价地缘溢价存在一次性重定价风险**。因此不建议周末裸空，而建议等确认后用 1–2M Put Spread。

## 三、中国 50/300/500/1000 与期权联动

### 数据健康检查

- `date=2026-08-07`
- `generated_at=2026-08-07T23:04:59.647197+08:00`
- `data_fresh=true`
- `source_status.option_chain=ok`
- `source_status.volume=ok`
- CFFEX 官方期权 EOD：726 条；完整链匹配 726/726，覆盖率 100%
- CFFEX 期指：16 个合约，状态 `ok`
- `previous_date=null`
- `errors=[]`

因此：**PCR(volume) 可用；但本期不得声称 ΔIV、ΔOI 的跨日变化、skew change、Gamma migration，也不做伪造的 IV-RV 分位比较。**

### 期指事实

| 主力 | 收盘 | 涨跌 | Volume | OI | OI变化 | 12月-9月 |
|---|---:|---:|---:|---:|---:|---:|
| IH2609 | 2930.0 | +1.36% | 29,990 | 70,624 | +3,455 | -43.0 |
| IF2609 | 4645.6 | +0.95% | 65,609 | 151,018 | +4,447 | -80.0 |
| IC2609 | 7877.8 | +2.13% | 116,150 | 168,332 | -2,089 | -162.2 |
| IM2609 | 7590.6 | +2.13% | 177,728 | 241,397 | -4,787 | -190.6 |

**联合解释：** IC/IM 价格最强，但主力 OI 反而下降；IH/IF 涨幅较小却增仓。换言之，8 月 7 日的小盘强势至少部分具有 short covering / 存量空头撤退特征，**并未形成“价格强 + 新多增仓”的完整趋势确认**。与此同时，远月全部低于 9 月主力，IM 负斜率最陡，说明小盘远期风险补偿仍高。

本轮没有从权威公开源可靠取得上证50、沪深300、中证500、中证1000现货的精确收盘与分红公平值，因此**不构造 spot basis 或年化基差**。跨期结构可用，但现货基差模块明确降级。

### HO / IO / MO surface

| 产品 | ATM IV | RR25 | BF25 | PCR(OI) | PCR(Vol) | 主要 Absolute Gamma 峰 |
|---|---:|---:|---:|---:|---:|---|
| HO2608 | 15.36% | -0.12 vol | +0.36 vol | 0.731 | 0.568 | 2950，其次 3000/2900 |
| HO2609 | 16.12% | -0.13 vol | +0.02 vol | 0.698 | 0.663 | 2900/3000 |
| IO2608 | 17.59% | -1.64 vol | +0.79 vol | 0.681 | 0.606 | 4700，其次 4600/4800 |
| IO2609 | 18.77% | -1.02 vol | +0.09 vol | 0.680 | 0.548 | 4700/4600 |
| MO2608 | 27.18% | -1.03 vol | +0.69 vol | 0.717 | 0.825 | 7500，其次 8000/7600 |
| MO2609 | 27.54% | -2.12 vol | +0.86 vol | 0.704 | 0.630 | 8000，其次 7600/7800 |

MO2609 的 10Δ Put IV 约 33.22%，Put skew 显著强于 HO/IO；MO2608 Call OI 当日变化 -10,616、Put OI +3,797，MO2609 则 Call OI -1,179、Put OI +2,041。**价格强、Put protection 仍贵、Call OI 减少**，不支持“裸多 IM”这一最简单表达。

### 中国固定问题结论

- **今天更适合哪个：** 条件式偏 IM，但只能在周一开盘 30–45 分钟确认后做；若 IM 继续涨而 OI 继续降，则反而 IH 的“价格涨 + OI涨”结构更健康。
- **大小盘是否切换：** 价格上已经切向小盘，仓位结构尚未确认。
- **基差/跨期是否异常：** 跨期为明显远月贴水，IM 最陡；现货基差因权威现货收盘缺失不下结论。
- **期权还是裸期货：** 对 IM 明显优先“Long IM/Short IF + MO Put Spread”或直接用 MO Call Spread，而不是裸 IM。
- **相对价值：** IM-IF 是当前最有吸引力的中国相对价值，但必须等 OI 和 skew 不恶化。
- **中国机会评分：82/100。** 进入全球 Top3，但属于“条件式机会”。

## 四、相比上一交易日真正重要的变化

1. **美国就业从“放缓”升级为负增长。** 7 月非农 -2.3 万，May/June 合计下修 10.3 万；9 月加息概率明显回落。
2. **风险资产没有按衰退剧本交易。** S&P 创纪录、Nasdaq 周涨 5.2%，信用利差仍窄，说明市场把弱就业先解释为政策利好。
3. **美元—黄金给出最清晰确认。** DXY -0.44%，黄金 +2.55%、周涨约 7%。
4. **油价的周末尾部从“战争升级”转向“双向事件风险”。** 霍尔木兹谈判若落地，周日晚油价更容易先下跳；若谈判失败或航运继续遭袭，则反向 squeeze 风险仍大。
5. **中国价格风格切向 IC/IM，但仓位未确认。** IC/IM +2.13%，同时主力 OI 下滑；IH/IF 则增仓上涨。
6. **中国出口继续由 AI/高技术驱动。** 7 月出口同比 +23.9%，半导体出口接近翻倍，高技术出口 +40.7%；这更支持小盘高景气制造/科技相对价值，而不是广义内需 Beta。

## 五、全球统一机会排行榜

| 排名 | 机会 | 分数 | 方向 | 持有期 | 阶段 | 工具 | 最大损失 |
|---|---|---:|---|---|---|---|---|
| 1 | 黄金 3–6M Call Spread | 88 | Long convex gold | 10–60D | 可试仓 | COMEX/GLD Call Spread | 有限 |
| 2 | 2s30s Steepener | 85 | Receive 2Y / Pay 30Y | 5–30D | 可试仓 | DV01-neutral IRS / swaption pair | 用期权可有限 |
| 3 | Long IM / Short IF 相对价值 | 82 | Long small-cap vs large-cap | 2–15D | 条件式 | IM2609/IF2609 + MO Put Spread | 需期权保险 |
| 4 | Brent 下行 Put Spread | 79 | Downside oil convexity | 1–15D | 等霍尔木兹确认 | 1–2M Put Spread | 有限 |
| 5 | Long AI cash-flow / Short AI Capex-beta | 77 | 相对价值 | 5–30D | CPI 后择机 | 股票 pair / option spread | 可设计有限 |

## 六、前三名交易卡

### 1）黄金 3–6M Call Spread｜88

**核心逻辑：** 弱就业使加息路径后移，但长端财政/期限溢价仍高；这比单纯做多长债更适合黄金。  
**错误定价：** 市场仍把黄金部分当作“降息 Beta”，但它现在同时承载政策信用与地缘凸性。  
**最佳表达：** Dec-2026 / Jan-2027 买约 30–35Δ Call，卖约 10–15Δ Call。以现货 4347 为参考，可把 4500 附近作为买腿、4850–4950 附近作为卖腿的**仅供筛选**区间，实际以当时 Delta/盘口重选，不虚构权利金。  
**入场：** 先 1/3；CPI 后若 DXY 仍 <100 且黄金守住约 4250–4300，再加 1/3；再突破本周高位才加最后 1/3。  
**失效：** DXY >101、实际利率明显抬升且黄金跌破 4200。  
**止盈：** spread 理论最大价值的 45%–55%、75%–85% 两档。  
**Greeks：** +Delta、+Gamma、+Vega、-Theta。  
**最大损失：** 净权利金；试仓风险 NAV 0.50%–0.75%。  
**Gap risk：** 周末地缘缓和可能压金，但弱美元/弱就业可部分缓冲。

### 2）2s30s Steepener｜85

**核心逻辑：** 就业弱主要压前端，而 30Y 仍在约 5.2%附近，财政供给、期限溢价与通胀尾部继续钉住长端。  
**最佳表达：** 3M2Y receiver swaption + 3M30Y payer swaption，DV01 匹配；若用 IRS，则 receive 2Y / pay 30Y 并严格 DV01-neutral。  
**入场：** 2s30s 回落至 85–90bp，或 CPI 后前端进一步 rally、长端不跟。  
**失效：** CPI 明显超预期且 9 月加息概率重新 >65%，使前端收益率重新上冲；或 30Y 对增长担忧显著 bull flatten。  
**止盈：** 曲线再陡 +15bp、+25bp 两档。  
**Greeks：** swaption 组合整体偏正凸性；需控制 Vega 不对称。  
**最大损失：** 用期权表达时限于净权利金。  
**Gap risk：** 周末地缘缓和会降低通胀尾部，可能让 30Y 也大幅下行，短期压制 steepener。

### 3）Long IM2609 / Short IF2609 + MO Put Spread｜82

**核心逻辑：** 中国 8 月 7 日小盘价格明显跑赢，但主力 OI 下滑，因此先把它定义为“等待新多确认的相对价值”，不是裸方向。  
**最佳表达：** 先 Dollar-neutral，再 Beta-adjust；Long IM2609 / Short IF2609，同时买 MO2609 20–25Δ Put、卖更低 Delta Put 控成本。  
**入场触发：** 周一开盘后 30–45 分钟，IM/IF 相对强度突破周五高位、IM OI 转为增加、MO RR25 不恶化到 -3vol 以下，且人民币不出现明显风险离岸贬值。  
**失效：** IM 相对突破失败、OI 继续下降且 MO Put skew 进一步走负。  
**止盈：** 相对收益 +2%、+3.5% 两档。  
**Greeks：** 主体为相对 Delta；MO Put Spread 提供负 Delta、正 Gamma、有限 Vega。  
**最大损失：** 期货 pair 本身非有限；必须通过仓位上限与 MO 保险将主题风险压到 NAV 1% 左右。

## 七、黄金专项

黄金“财政、通胀和货币政策信用风险期权”的框架本日判断：**增强**。但现货单周已涨约 7%，因此不追裸 Call。优先级：
1. 3–6M 30–35Δ / 10–15Δ Call Spread；
2. 微型黄金 MGC 仅作为突破确认仓；
3. 对冲组合可考虑 **Long Gold + Long 30Y Treasury Put Spread**，用来表达“财政/期限溢价上升但黄金继续受益”的非典型组合。

## 八、AI 专项

当前更接近**估值压缩/去杠杆后的反弹，而非基本面反转确认**。8 月 7 日科技板块继续领涨，但市场对 hyperscaler AI Capex 与 FCF 的敏感度明显提高；近期 Alphabet 在创纪录营收/利润下仍因高 Capex、FCF恶化受到惩罚，说明“EPS 好 ≠ 现金流好”正在成为关键分化。

优先表达：**Long AI cash-flow leaders / Short AI Capex-beta**，而不是继续追裸 Nasdaq。下周 CPI 前不扩大指数 Vega；若 CPI 温和、10Y 不上破近期高位，再增加多现金流/空长久期 Capex Beta 的相对价值仓位。

## 九、未来 24h / 7天事件日历（北京时间）

| 时间 | 事件 | 交易含义 |
|---|---|---|
| 未来24h | 霍尔木兹谈判/重开条款、航运安全新闻 | 若正式可执行，降低油价 Long Delta；若破裂则保留油价上行尾部 |
| 8/10–8/15 | 中国社融/信贷常见发布窗口 | 检验国内信用脉冲，影响 IH/IF 与内需 Beta |
| 8/12 20:30 | 美国 7 月 CPI | 全周首要 Delta/Vega 事件 |
| 8/13 20:30 | 美国 7 月 PPI | 检验成本通胀和长端收益率 |
| 8/14 20:30 | 美国 7 月零售销售 | 检验“就业弱”是否已传导到需求 |

## 十、行动清单

**A 立即建立：** 黄金 3–6M Call Spread 1/3 试仓；可做 swaption 则轻仓 2s30s steepener。  
**B 只挂条件单：** Long IM2609/Short IF2609 等周一前 30–45 分钟确认；Brent Put Spread 等霍尔木兹重开进一步确认。  
**C 继续观察：** AI cash-flow/Capex Beta、VIX/MOVE 精确收盘、China spot basis/ETF流/两融和 MO skew。  
**D 必须避免/退出：** 周末裸空油、裸多 IM、追高裸 Nasdaq；若 CPI 令 9 月加息概率重新 >65%，减黄金高 Delta，并退出 2s30s steepener。

## 风险预算

单一试仓最大损失 NAV **0.25%–0.75%**；确认交易 **0.75%–1.50%**；高确信主题总风险 **≤2.5%–3.0%**。黄金、2s30s steepener、空长债/空美元若本质暴露同一“财政/通胀/政策信用”因子，必须合并计算；Long IM/Short IF 与 MO Call/Put 也必须按“小盘因子”合并。

## 关键来源

- Reuters, [Dollar drops as weak US jobs data pushes out Fed hike expectations](https://www.reuters.com/world/asia-pacific/dollar-drifts-higher-traders-eye-iran-talks-ahead-us-jobs-data-2026-08-07/)
- Reuters, [S&P closes at record high as soft jobs report eases rate-hike concerns](https://www.reuters.com/business/sp-500-dow-futures-muted-ahead-jobs-data-chips-software-stocks-rise-2026-08-07/)
- Reuters, [US official: We expect a deal soon between Iran and Oman on Strait of Hormuz](https://www.reuters.com/world/middle-east/us-official-we-expect-deal-soon-between-iran-oman-strait-hormuz-2026-08-07/)
- Reuters, [AI demand keeps China's export engine humming, but risks loom](https://www.reuters.com/world/asia-pacific/chinas-july-exports-climb-239-yy-imports-up-275-2026-08-07/)
- U.S. BLS, [2026 release schedule](https://www.bls.gov/schedule/2026/)
- U.S. Census Bureau, [Economic indicator release schedule](https://www.census.gov/economic-indicators/calendar-listview.html)
- GitHub, [China-Options-Engine radar_latest.json](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)
