# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-22

> 数据截点：北京时间2026-08-22 19:36。今天是周六，中国商品期货/期权没有日盘或21:00夜盘；最新完整中国交易日为2026-08-21。标准WTI、Brent、COMEX银等也处周末停盘期，因此不把旧报价冒充15:00—19:30实时价格。本版采用8月21日EOD + 8月22日周末新闻，下一中国价格发现窗口为8月24日09:00。

## 一、今日一句话结论

**今天没有可立即建立的新仓；但周末地缘并未让周一机会失效。FU2611仍是最高质量条件多，AG次之，FG为失败反弹空；真正的edge是等周一价格确认，而不是为周末新闻提前付gap溢价。**

没有80分以上确认交易：FU2611 79、AG2610 76、FG701 74、BU2610 72、EC2610 69。

## 二、数据质量与覆盖说明

第一读取层为`farfromexact/China-Commodities-Engine`的`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；并按需读取`data/market_state_latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`。report_input requested_date=`2026-08-21`，generated_at=`2026-08-21T19:02:52.405697+08:00`。周六无新中国交易日，因此8月21日是最近完整交易日而非错误滞后。

核心Futures五所齐全：SHFE/INE/DCE/CZCE/GFEX，`full_market_ready=true`、`source_date_match_pct=100%`、803合约，unknown/duplicate/invalid OHLC/negative volume-or-OI/critical errors均为0，placeholder=5。Market State有20个交易日且全部锁定当前具体合约计算，不拼主力。

Physical覆盖仍稀疏：20个目标仅4个verified且fresh-by-native-frequency；FG 8月21日周度企业库存7441.4重量箱只是绝对水平，不能自动算方向确认；JM basis质量不足，I港口库存单位仍需QA，TA加工费只作context。DCE仓单抓取报JSON错误。External仓库EOD整体`data_fresh=false`，仅按per-series作context；无满足exact-contract/品质/税费/运费/币种/时点对齐的可执行进口平价。

Options最近完整交易日为8月21日：21,816条、59/64品种、368 series；360 surface-ready、70 positioning-ready、0 execution-ready；IV coverage约99.69%、OI coverage约92.47%、bid/ask coverage=0。可以使用ATM IV/RR25/BF25/term structure/IV-RV研究，但不得虚构权利金、bid/ask、滑点或可成交成本。

Contract Metadata总体partial：contract match约67.4%、effective match约73.3%，multiplier/tick覆盖约29.8%；参数未确认的交易卡明确留空。

## 三、商品仪表盘

| 板块 | 主力 | 8/21 EOD | 1D / 5D | Volume / OI | ΔOI | Curve | Options/Physical | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 能源 | **FU2611** | 3845 / 3850 | +2.12% / +9.81% | 650,637 / 285,614 | +8.58% | **Bwd +7.47%** | ATM IV~43%，exec N | **周一第一候选** |
| 贵金属 | **AG2610** | 16771 / 16611 | +3.11% / +5.45% | 773,038 / 306,822 | +1.46% | Contango约-0.14% | IV47.27%，RR25+7.81，exec N | 多，但Vega贵 |
| 建材 | **FG701** | 907 / 906 | -1.09% / -3.10% | 1,575,371 / 1,601,238 | +10.21% | **Contango -3.35%** | 周度库存仅level；IV23.06 | **失败反弹空** |
| 能源 | BU2610 | 4508 / 4526 | +2.14% / +7.92% | 486,111 / 334,627 | -0.78% | Bwd +3.16% | exec N | FU替代，不叠加 |
| 原油 | SC2610 | 8/21 EOD | +1.28% / +7.61% | 活跃 | +1.08% | Bwd +4.17% | surface可用 | 能源确认 |
| 化工 | MA610 | 2909 / 2880 | +1.80% / +8.56% | 1,957,108 / 873,688 | +0.69% | Bwd +0.35% | surface Y | 等30–45m |
| 航运 | EC2610 | 1957 / 1885.5 | +7.56% / +18.66% | 41,149 / 高位 | +11.84% | 近月污染 | 闭环不足 | 过热不追 |
| 新能源 | LC2701 | 158680 / 156360 | +2.60% / +1.41% | 225,444 / 353,437 | +9.91% | Contango约-0.30% | IV~35.37% | 反弹≠短缺 |
| 油粕 | RM611 | 2238 / 2246 | -1.36% / — | 747,569 / 651,265 | — | Bwd +3.96% | surface可研究 | price/curve冲突 |
| 豆粕 | M2701 | 3228 / 3244 | close -1.10% | 1,390,344 / 2,467,335 | — | Contango | 外盘闭环缺 | 不追空 |
| 纸浆 | SP2611 | 4892 / 4848 | close +3.42% | 535,700 / 260,902 | — | Contango | surface可研究 | 单日强 |
| 铁矿 | I2701 | 8/21 EOD | settle +0.14% | 完整EOD | — | Market State可用 | 港库8/19；DCE仓单失败 | 中性 |

Curve均指近月—次近月期货结构，不是现货基差。

## 四、真正发生了什么

1. 周末没有新的中国K线，变化来自**事件分布**：Friday Brent/WTI分别结算94.39/87.06美元，周涨6.39%/5.66%；Saturday美国预告周一更严厉对伊制裁，同时伊朗又给予若干伊拉克油轮Hormuz特别通行。供应上行尾部仍在，但不是单向封锁路径。[Reuters 8/21](https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/) [Reuters 8/22](https://www.reuters.com/world/middle-east/us-iran-keep-up-hostile-rhetoric-ahead-new-sanctions-2026-08-22/) [Reuters通行许可](https://www.reuters.com/business/energy/iran-grants-permission-number-iraqi-oil-tankers-pass-through-hormuz-2026-08-22/)
2. FU国内price/OI/curve组合没有被周末推翻，但Backwardation较前一日约8.16%收窄至7.47%，不能写成紧张持续加速。
3. AG方向仍强，但ATM IV 47.27% vs RV20约30.82%，贵约16.45vol；周一gap-up时裸Call赔率可能比方向判断差。
4. FG没有周末新Physical确认，因此仍是“等失败反弹”而非追空。
5. EC/LC没有新增结构证据；周末新闻不能替代缺失的欧线即期运价、库存/排产与期权闭环。

## 五、产业链地图

| 链条 | 方向 | 确认 | 缺口 | 置信度 |
|---|---|---|---|---|
| 原油—燃料油—沥青 | **偏多、双侧gap大** | FU/SC price+curve；Friday外油强 | 裂解、产品库存、进口平价、周日重开价 | 高 |
| 贵金属 | 偏多、高IV | price+海外宏观+options | curve弱、周一真实外盘/人民币映射 | 中高 |
| 建材 | **偏弱** | FG price/OI+Contango | 库存方向、地产/深加工 | 中高 |
| 航运 | 极端强但过热 | EC price/OI | 同口径SCFIS/即期、Options | 中 |
| 新能源 | 高波动反弹 | LC price/OI | curve不确认、库存/排产缺 | 中 |

最强链条能源，最弱可交易结构FG建材。Regime不是全面商品Risk-on，而是“地缘能源+贵金属信用交易”对“国内需求链偏弱”。

## 六、机会排行榜

| Rank | 机会 | Score | 分项（逻辑/赔率/催化/结构/技术） | 方向/持有 | 阶段 | Fresh层 |
|---:|---|---:|---|---|---|---:|
| **1** | **FU2611 周一回撤确认多** | **79** | 21/20/18/12/8 | 多 / 1–5D | 条件试仓 | 4 |
| **2** | **AG2610 周一回撤确认多** | **76** | 21/18/17/12/8 | 多 / 1–5D | 条件试仓 | 3 |
| **3** | **FG701 失败反弹空** | **74** | 20/20/13/13/8 | 空 / 1–5D | 条件试仓 | 3 |
| 4 | BU2610 能源趋势多 | 72 | 19/16/18/12/7 | 多 / 1–5D | 条件单 | 4 |
| 5 | EC2610 极端动量 | 69 | 20/15/16/10/8 | 观察 / 1–3D | 观察 | 2 |

## 七、前三名交易卡

### FU2611｜79｜回撤确认多
**事实**：3850结算、1D+2.12%、5D+9.81%、ΔOI+8.58%、Bwd约7.47%、ATM IV约43% vs RV20约37.93%。**市场定价**：供应风险溢价已很高。**推断**：第一次回撤是否仍被买回，比周末标题方向更有信息。**主观判断**：79分，未达到确认加仓阈值。

最佳表达先期货确认；若周一夜盘仍成立，再比较2026-10-19 expiry 35–45Δ Call / 15–25Δ Call Spread，1:1 vertical；`execution_ready=false`，真实strike和权利金待quote后定，不报Greeks绝对值。8月24日09:00后等30–45分钟；3810–3850守住并重新接受3850上方，先1/3风险；gap-up约2%以上且不回测则放弃。有效跌破3810并伴curve压缩失效。TP1 +1R，TP2 +2R或curve收窄约1/3；两交易时段无延续撤。最大损失0.35%–0.50% NAV，FU+BU合并初始≤0.75%。

参数：10吨/手，tick 1元/吨，tick value 10元，名义约38,500元；8/21参考限价14%、一般保证金16%、套保15%，周一执行前重新核对；券商保证金未确认。**对多头方向**一个跌停压力约5,390元/手，连续两个14%跌停复合压力约10,025元/手。常规夜盘21:00–23:00，周六无盘。LTD/交割参数本轮metadata未完整确认，执行前复核；不持入交割月，流动性/持仓迁移时提前roll。

### AG2610｜76｜回撤确认多
**事实**：16771/16611，1D+3.11%、5D+5.45%、ΔOI+1.46%，ATM IV47.27%、RR25+7.81，IV-RV约+16.45vol。**市场定价**：上行skew和Vega昂贵。**推断**：方向正确也可能被过高IV吃掉赔率。**主观判断**：小期货确认或核价后Call Spread优于追裸Call。

8月24日09:00等15–30分钟，16600/16611守住并重新站稳16770且海外金银重开不反向；30分钟接受16600下且外盘同步回吐止损。TP1/TP2=+1R/+2R；最大损失0.35%–0.55% NAV。期权为2026-09-23 expiry 1:1 Call Spread：长35–45Δ、短15–25Δ；执行层未ready，不报权利金和Greeks绝对值。

参数：15kg/手，tick 1元/kg，tick value15元，名义约251,565元；8/21参考限价14%、一般16%、套保15%，周一复核；常规夜盘21:00–02:30，周六无盘。**对多头方向**一个跌停压力约35,219元/手，连续两个14%跌停复合压力约65,508元/手。LTD参考2026-10-15，执行前再次核实；实物交割风险随交割月临近上升，提前roll。

### FG701｜74｜失败反弹空
**事实**：907/906，1D-1.09%、5D-3.10%、ΔOI+10.21%、Contango约-3.35%；周度库存7441.4重量箱只是level context。**市场定价/推断**：这是价格弱+OI扩张线索+弱curve，不是已经被Physical完全确认的需求崩塌。

8月24日09:00等30分钟，910–918反弹失败且curve不收窄后空，重新跌破899才加；30分钟站稳920止损。TP1=899，TP2=880附近或+2R；两交易日不破899撤；最大损失0.25%–0.40% NAV。期权替代为1:1 Put Spread，长约35–45|Δ|、短15–25|Δ|，真实strike/权利金待quote。20吨/手、tick 1元/吨、tick value20元、名义约18,120元；动态保证金/涨跌停本轮未充分确认，因此不虚构1/2板压力金额。常规夜盘21:00–23:00，周六无盘；LTD按交割月第10个交易日规则执行前复核，避免进入交割窗口。

## 八、商品期权专项

代表样本：AG IV-RV约+16.45vol，FU约+5.1vol，FG约+6.9vol，LC约+8.2vol。没有对全部360个surface逐一排序，所以不称“全市场最高/最低”。360/368 surface-ready、70/368 positioning-ready、0/368 execution-ready，bid/ask coverage=0；研究可以做，精确定价不能做。AG优先spread压Vega，FU优先有限损失表达gap，FG优先Put Spread；禁止裸卖周末事件Vega，Dealer Gamma方向未知。

## 九、21:00夜盘开盘风险地图｜周六模式

**今晚2026-08-22 21:00没有中国夜盘。** 下一中国交易窗口为8月24日09:00，下一夜盘为8月24日21:00。

| 品种 | 8/21结算 | 周末映射 | 周一倾向 | 追价 | 等待 | 确认 |
|---|---:|---|---|---|---|---|
| FU2611 | 3850 | 外油强收；制裁升级/有限通行并存 | 偏高、双侧gap | **否** | 30–45m | 3850、3810、VWAP、curve、Sunday Brent |
| AG2610 | 16611 | 金价强、美元信用交易；标准银周末无价 | 偏高 | **否** | 15–30m | 16600、16770、GC/SI、DXY/收益率 |
| BU2610 | 4526 | 同能源 | 偏高 | 否 | 30–45m | FU/SC同步、curve |
| FG701 | 906 | 无新实体催化 | 平/偏弱 | 否 | 30m | 910–918、899、curve |
| EC2610 | 1885.5 | Hormuz仅宏观映射 | 高波动未知 | **禁止追** | 45m | SCFIS/现货运价/OI |
| LC2701 | 156360 | 无周末产业闭环 | 平/高波动 | 否 | 30–45m | curve、库存/排产 |

标准WTI正常Globex周日18:00 ET重开，约北京时间8月24日06:00；新10-Barrel WTI的24/7产品要到8月30日才计划上线，因此这个周末不能拿“WTI周末实时价”做FU依据。[CME](https://www.cmegroup.com/articles/faqs/faq-tuesday-and-thursday-weekly-wti-options.html)

## 十、未来24h / 7d事件日历

- 8月24日06:00左右：标准CME能源/贵金属周日Globex重开，先看真实周末repricing。
- 8月25日02:00：美国财政部长Bessent计划就新一轮伊朗制裁举行发布会；能源中国夜盘已闭市，隔夜gap风险尤其重要。
- 8月25日03:00 / 04:00：USDA Cold Storage / Crop Progress。[USDA](https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=08&view=l&year=2026)
- 8月26日22:30：EIA Weekly Petroleum Status Report；能源已有利润则数据前优先降Delta。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 8月27–29日：Jackson Hole，主题“Financial Innovation: Implications for Payments and Policy”；贵金属重点管美元、真实利率和Vega。[Kansas City Fed](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/)

## 十一、风险预算与行动

单一试仓最大损失0.25%–0.75% NAV；确认交易0.75%–1.50%；单一高确信主题≤2.5%–3.0%。FU/BU/SC按同一能源地缘因子合并；AG/AU按美元/真实利率/财政信用合并。压力测试1/2涨跌停、相关性破裂、流动性消失、周末gap、保证金上调、IV跳升/塌陷、交割挤压和人民币急变。

A. 今天没有应立即建立的新仓位。

B. 今天只应挂条件单的仓位：FU2611周一回撤确认多、AG2610周一回撤确认多、FG701周一失败反弹空；BU2610仅作FU替代，不重复叠加。

C. 今天应继续观察的机会：EC2610极端动量、LC2701高波动反弹、RM/M价格与curve冲突；先看周日海外重开和周一09:00第一轮价格发现。

D. 今天必须避免或退出的交易：为周末新闻预判gap、周一开盘追第一跳、裸买AG高IV ATM Call、裸卖周末事件Vega、把FG库存绝对水平当方向确认、把伊拉克油轮特别通行等同于Hormuz全面恢复、FU/BU/SC重复堆同一地缘因子。
