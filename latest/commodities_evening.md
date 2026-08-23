# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-23

> 数据截点：北京时间 2026-08-23 19:36。周日模式。中国商品期货/期权今天无日盘、无21:00夜盘；最近完整中国交易日为2026-08-21。标准CME/ICE能源与COMEX贵金属尚未在本报告截点重开，因此不把8月21日收盘价冒充周日实时价。下一关键价格发现窗口：8月24日约06:00海外Globex重开；中国下一日盘8月24日09:00，下一常规夜盘8月24日21:00。

## 一、今日一句话结论

**值得为周一保留风险预算，但今天没有可立即执行的新仓。FU2611仍是第一条件多，AG2610次之，FG701为失败反弹空；周日下午新增的伊朗斡旋与中国炼化需求偏弱信息，使能源更像“双侧gap+高开不追”，而非无条件追多。**

严格执行触发纪律：**今日商品期货期权无可立即执行的合格交易。** 最接近触发的是FU2611、AG2610、FG701；缺少的共同确认是周一真实价格发现、开盘后OI/curve延续以及可执行期权bid/ask。

## 二、数据质量与覆盖说明

第一读取层实际读取：`farfromexact/China-Commodities-Engine/data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需读取`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`，并使用`report_input`内嵌的具体surface series。`report_input requested_date=2026-08-21`，`generated_at=2026-08-21T19:02:52.405697+08:00`。周日使用8月21日EOD是正常周末模式，不是静默滞后。

核心Futures五所SHFE/INE/DCE/CZCE/GFEX齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；unknown/duplicate/invalid OHLC/negative volume-or-OI均为0，placeholder=5且不进入异常排行，核心Futures无carried-forward。Market State按同一具体合约计算1D/3D/5D/20D，20日历史可用，不拼接主力。

Physical仍稀疏：20个目标仅4个按原生频率可用，FG最新周度企业库存7441.4重量箱只是绝对水平，没有可验证方向变化时只作context；JM basis为C级且不满足交割地/税口径闭环，不进入评分；DCE仓单抓取仍有JSON异常。External仓库整体`data_fresh=false`，但按per-series使用；本次15:00—19:30新增信息来自公开实时新闻而非旧EOD External。

Options T日仍为8月21日：21,816条、368个series、59/64品种成功。**本次按module-specific `quality_latest.json`纠正聚合覆盖率：IV coverage=98.47%，OI coverage=68.74%，bid/ask coverage=0；昨日归档中的99.69%/92.47%不是当前quality文件的聚合口径。** `report_input`内嵌series显示360/368 surface-ready、70/368 positioning-ready、0/368 execution-ready。独立`data/options/surface_latest.json`当前为空文件，因此本次surface研究仅以`report_input`内嵌series为正式读取层，并对审计完整性扣分。具体FU2611、AG2610、FG701 series均`surface_ready=true`；execution均false，不报净权利金、bid/ask、精确滑点。Dealer Gamma方向未知。

Contract metadata为partial。FU2611、AG2610的LTD可由official-partial metadata/交易所规则核验；乘数、tick等使用交易所合约规则；券商保证金仍未确认。FU2611当前交易所风险参数14%涨跌停、一般保证金16%、套保15%来自2026-06-23上期所公告，周一执行前仍需复核临时风控调整。

## 三、商品仪表盘

| 板块 | 合约 | 8/21 close / settle | 1D / 5D | Volume / OI / ΔOI | Curve | Physical / basis | Options | 信号 |
|---|---|---:|---:|---|---|---|---|---|
| 能源 | **FU2611** | 3845 / 3850 | +2.12% / +9.81% | 650,637 / 285,614 / +8.58% | **Backwardation +7.47%** | 实体层缺 | ATM3850，IV43.0%，RR25 -1.22；surface✓/pos×/exec× | **周一第一候选** |
| 贵金属 | **AG2610** | 16771 / 16611 | +3.11% / +5.45% | 773,038 / 306,822 / +1.46% | 轻Contango约-0.14% | 实体层缺 | ATM16600，IV47.265%，RR25 +7.81，BF25 +1.93；surface✓/pos×/exec× | 趋势强、Vega贵 |
| 建材 | **FG701** | 907 / 906 | -1.09% / -3.10% | 1,575,371 / 1,601,238 / +10.21% | **Contango -3.35%** | 周度库存仅level | ATM910，IV23.055%，RR25 +7.72；surface✓/pos✓/exec× | **失败反弹空** |
| 能源 | BU2610 | 4508 / 4526 | +2.14% / +7.92% | 486,111 / 334,627 / -0.78% | Back +3.16% | 实体层缺 | surface可研究，exec× | FU替代，不叠加 |
| 原油 | SC2610 | 8/21 EOD | +1.28% / +7.61% | ΔOI +1.08% | Back +4.17% | 进口平价不可执行 | surface可研究 | 能源结构确认 |
| 化工 | MA610 | 2909 / 2880 | +1.80% / +8.56% | 1,957,108 / 873,688 / +0.69% | Back +0.35% | 需求证据不足 | surface✓/exec× | 受炼化弱需求约束 |
| 有色 | CU2610 | 107520 / 107010 | +0.14% / -0.39% | ΔOI +4.22% | 近端约+0.26% | 无A/B基差 | ATM约108000，IV约14.3%，pos✓/exec× | LME squeeze不等于追涨 |
| 新能源 | LC2701 | 158680 / 156360 | +2.60% / +1.41% | 225,444 / 353,437 / +9.91% | Contango约-0.30% | 库存/排产缺 | 代表IV约35.37%，exec× | 反弹≠短缺 |
| 农产品 | RM611 | 2238 / 2246 | -1.36% / +2.60% | 747,569 / 651,265 | Back +3.96% | 实体层缺 | surface✓/exec× | price/curve冲突 |
| 航运 | EC2610 | 1957 / 1885.5 | +7.56% / +18.66% | ΔOI +11.84% | 极端结构，不作普通curve套利 | 即期运价闭环缺 | 精确vol执行缺 | **过热不追** |
| 纸浆 | SP2611 | 4892 / 4848 | close +3.42% | 535,700 / 260,902 | Contango | Physical不足 | surface可研究 | 单日强、证据不足 |
| 铁矿 | I2701 | 8/21 EOD | settle +0.14% | 完整EOD | Market State可用 | 港库为8/19周度；仓单模块异常 | Options非核心 | 中性 |

Curve均为近月—次近月期货结构，不是现货基差。国内所有价格均是2026-08-21 EOD。

## 四、相比上一交易日/今晨真正变化

1. **周日下午出现新的双向能源信息。** Reuters 8月23日15:44 BJT报道，巴基斯坦陆军参谋长Asim Munir周一赴德黑兰参与斡旋；这不是和平协议，但增加周一能源向下gap/高开回落的尾部。与此同时Hormuz油运仍近乎停滞，供应风险没有解除。[Reuters](https://www.reuters.com/world/asia-pacific/iran-says-pakistans-army-chief-visit-tehran-monday-2026-08-23/)
2. **18:06 BJT新增中国炼化需求证据偏弱。** Sinopec半年数据显示原油加工量同比下降5.6%，乙烯产量下降15.5%；公司仍预计下半年原油加工量大致持平。这强化“上游供应风险强、国内成品油/化工需求弱”的分化，不支持把FU/BU/化工全部当成同一方向Beta。[Reuters](https://www.reuters.com/business/energy/sinopecs-half-year-profit-grew-193-year-despite-iran-war-falling-demand-2026-08-23/)
3. **能源不是简单单边。** Brent/WTI 8月21日结算94.39/87.06美元，周涨6.39%/5.66%；但周一制裁细节与斡旋同日发生，周日晚海外重开后的第一小时比周末headline更重要。[Reuters 8/21](https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/)
4. **Options质量口径被纠正。** 当前`quality_latest`为IV覆盖98.47%、OI覆盖68.74%，而非昨日归档的99.69%/92.47%；这降低全市场positioning可信度，但不影响已在`report_input`中明确`surface_ready=true`的FU/AG/FG具体series研究用途。
5. **AG逻辑未改变：方向强、工具贵。** 8月21日现货黄金最高至4631.99美元附近，贵金属受弱美元/财政信用交易支持；但AG2610 IV47.265%比RV20约30.82%高约16.45 vol，追裸Call赔率仍差。[Reuters](https://in.marketscreener.com/news/gold-climbs-to-near-three-month-peak-after-us-treasury-move-ce7858dad98aff25)

## 五、产业链地图

| 链条 | 方向 | 价格/curve | 实体/海外 | 期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| **原油—燃料油—沥青** | 偏多但双侧gap | FU/SC Back确认 | Hormuz受限；同时周一斡旋 | FU surface可研究 | 裂解、产品库存、周日重开价 | **高** |
| **贵金属** | 偏多、高IV | AG价格强、curve弱 | 金银/弱美元同向 | IV/skew昂贵 | 周一DXY/真实利率 | 中高 |
| **建材** | **偏弱** | FG价跌/OI增+Contango | Physical只有level | FG surface/pos可研究 | 库存方向、地产/深加工 | 中高 |
| **炼化化工** | 上游强、下游弱 | MA/EG偏强但需求证据弱 | Sinopec加工量/乙烯同比下降 | surface可研究 | 现货利润、库存 | 中 |
| **新能源/航运** | 高波动、赔率差 | LC仍Contango；EC过热 | 实体闭环不足 | execution不足 | 库存/排产/即期运价 | 中低 |

最强产业链仍是能源供应风险；最弱可交易结构仍是FG建材。Regime是**“地缘供应风险 + 财政信用贵金属”对“国内炼化/工业需求偏弱”**，不是商品全面Risk-on。

## 六、机会排行榜

| Rank | 机会 | Score | 分项（逻辑/赔率/催化/结构/技术） | 方向/持有 | 阶段 | Fresh层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| **1** | **FU2611 周一回撤确认多** | **79** | 21/20/18/12/8 | 多 / 1–5D | 条件试仓 | 4 | 周末双侧gap、Physical缺、exec× |
| **2** | **AG2610 回撤确认多** | **76** | 21/18/17/12/8 | 多 / 1–5D | 条件试仓 | 3 | IV/skew贵、curve弱、exec× |
| **3** | **FG701 失败反弹空** | **74** | 20/20/13/13/8 | 空 / 1–5D | 条件试仓 | 3 | 实体仅level、动态风控需复核 |
| 4 | BU2610 能源替代多 | 70 | 18/15/18/12/7 | 多 / 1–3D | 条件 | 4 | 与FU同因子且价涨仓减；国内需求弱 |
| 5 | EC2610 极端动量 | 68 | 20/14/15/10/9 | 观察 / 1–3D | 观察 | 2 | 过热、即期/Options闭环不足 |

没有80+确认交易；≥70仅允许触发后的试仓/条件单。

## 七、前三名交易卡

### 1）FU2611｜79｜回撤确认多

**事实**：8/21结算3850，1D+2.12%、5D+9.81%、ΔOI+8.58%，Backwardation约+7.47%；FU2611 2026-10-19期权ATM3850、IV43.0%、RR25 -1.22，surface-ready但positioning/execution not ready。**市场定价**：供应风险溢价已高。**推断**：周一高开后的第一次回撤承接比headline方向更有信息。**主观判断**：仍是第一机会，但周一斡旋增加反向gap，禁止开盘追多。

最佳表达：先期货确认；若真实bid/ask出现，再比较1:1 Call Spread，长35–45Δ、短15–25Δ。入场：8/24 09:00后等30–45分钟，3810–3850区域守住并重新接受3850上方；若海外06:00重开大涨、中国09:00直接高开约2%以上且无回测，放弃。分批：1/3初始，VWAP上方承接并新高再加。初始止损：有效跌破3810且curve同步压缩。逻辑失效：Hormuz出现可信缓和/通行明显恢复，或价格涨而OI、Backwardation同时衰减。TP1 +1R，TP2 +2R或curve收窄约1/3。时间止损：两个交易时段无延续。最大损失0.35%–0.50% NAV；FU/BU/SC初始合并≤0.75%。

参数：10吨/手；tick 1元/吨；tick value 10元；3850名义约38,500元/手。交易所当前参考：涨跌停14%、一般保证金16%、套保15%（2026-06-23公告，执行前复核）；券商保证金未确认。FU业务规则最后交易日为交割月前一月最后一个交易日，metadata显示FU2611 LTD=2026-10-30；实物交割风险高，不持入交割月。常规夜盘21:00–23:00；今晚周日无盘。对多头，一个14%不利跌停压力约5,390元/手；连续两个14%复合下跌约26.04%，损失约10,025元/手。

### 2）AG2610｜76｜回撤确认多

**事实**：8/21 close/settle 16771/16611，1D+3.11%、5D+5.45%、ΔOI+1.46%；ATM IV47.265%，RR25 +7.81，BF25 +1.93，RV20约30.82%。**市场定价**：上行skew和Vega都贵。**推断**：方向可以继续对，但裸Call很可能买贵。**主观判断**：小期货确认或quote后Call Spread优于追裸Call。

入场：8/24 09:00后等15–30分钟；16600/16611守住、重新站稳16770，且海外GC/SI重开不反向。加仓：30–45分钟保持VWAP上且创新高。止损：30分钟接受在16600下方且海外金银同步回吐。TP1 +1R，TP2 +2R/移动止盈；1–2个交易时段无新高即撤。最大损失0.35%–0.55% NAV。期权：2026-09-23 expiry，1:1 Call Spread长35–45Δ、短15–25Δ；execution=false，不报净权利金和Greeks绝对值。

参数：15kg/手；tick 1元/kg；tick value 15元；16771附近名义约251,565元。上期所当前参考黄金/白银涨跌停14%、一般保证金16%、套保15%；券商保证金未确认。AG2610 metadata/规则LTD=2026-10-15，实物交割，提前roll。常规夜盘21:00–02:30；今晚周日无盘。一个14%不利跌停压力约35,219元/手；连续两个14%复合下跌损失约65,508元/手。

### 3）FG701｜74｜失败反弹空

**事实**：8/21 close/settle 907/906，1D-1.09%、5D-3.10%、ΔOI+10.21%，Contango约-3.35%；FG701 ATM910、IV23.055%、RR25 +7.72，surface/positioning ready、execution false。Physical只有最新周度库存绝对水平。**市场定价**：price/OI/curve共同偏空。**推断**：弱需求仍占优，但没有实体方向层，不应追breakdown。**主观判断**：等反弹失败的赔率最好。

入场：8/24 09:00后等30分钟，910–918反弹失败、curve未明显收窄再空；重新跌破899才加。止损：30分钟有效站稳920。逻辑失效：curve明显收窄并出现可验证库存下降/深加工改善。TP1 899，TP2 880或+2R。时间止损：两个交易日不破899。最大损失0.25%–0.40% NAV。若周一直接gap-down跌破899，禁止追空。期权替代：1:1 Put Spread，长35–45|Δ|、短15–25|Δ|，真实strike/权利金待quote。

参数：20吨/手；tick 1元/吨；tick value 20元；906名义约18,120元。当前动态保证金/涨跌停本轮没有足够新的官方确认，因此不虚构1/2板损失；LTD按郑商所交割月第10个交易日规则执行前复核。常规夜盘21:00–23:00；今晚周日无盘。

## 八、商品期权专项

本次不称“全市场最高/最低IV”，只列代表样本。AG2610 ATM IV47.265% vs RV20约30.82%，IV-RV约+16.45vol；FU2611约43.0% vs 37.93%，+5.07vol；FG701约23.055% vs 16.20%，+6.86vol；LC代表series约35.37% vs 27.19%，+8.18vol。

全市场quality：21,816合约、59/64品种、368 series；IV coverage 98.47%、OI coverage 68.74%、bid/ask coverage 0。`report_input`内嵌series：360 surface-ready、70 positioning-ready、0 execution-ready。由于独立`surface_latest.json`为空，surface审计链条不完整，但具体series在统一输入中仍有验证字段。适合：AG/FU用有限风险Call Spread，FG用Put Spread；必须回避：裸买AG高IV ATM Call、任何依赖精确bid/ask的结构定价、依据不完整OI推全市场crowding、推断Dealer Gamma方向。

## 九、21:00夜盘开盘风险地图

**今天是周日，今晚21:00没有中国夜盘。** 下表指8月24日09:00日盘与8月24日21:00常规夜盘的风险地图；海外标准能源/贵金属预计先在8月24日约06:00 BJT重开。

| 品种 | 中国8/21结算 | 周日下午新增映射 | 周一倾向 | 追价 | 等待 | 开盘确认 |
|---|---:|---|---|---|---|---|
| **FU2611** | 3850 | Hormuz仍受限；Pakistan周一斡旋；Sinopec需求偏弱 | 偏高但双侧gap | **否** | **30–45m** | 3850/3810、VWAP、OI、curve、Brent |
| **AG2610** | 16611 | 周末无新价格；财政信用逻辑未变 | 偏高 | **否** | 15–30m | 16600/16770、GC/SI、DXY/真实利率 |
| BU2610 | 4526 | 上游强、国内燃料需求偏弱 | 小高/分化 | 否 | 30–45m | FU/SC同步、OI、curve |
| **FG701** | 906 | 无新玻璃实体利多 | 平/偏弱 | 否 | 30m | 910–918失败、899、curve |
| MA/EG | 2880/5159附近 | Sinopec乙烯/加工量偏弱 | 高位分化 | 否 | 30–45m | VWAP、OI、现货利润 |
| EC2610 | 1885.5 | Hormuz事件仍高风险 | 高波动未知 | **禁止追** | 45m | 即期运价/OI/风险溢价 |
| LC2701 | 156360 | 无周末实体闭环 | 平/高波动 | 否 | 30–45m | curve、库存/排产 |

## 十、未来24h / 7d事件日历（北京时间）

- **8月24日约06:00**：CME能源/贵金属周日Globex重开。策略：先观察第一小时，不用周末headline替代真实价格。
- **8月24日白天**：Pakistan陆军参谋长Asim Munir赴德黑兰斡旋，时间未精确公布。策略：能源Delta保持小、避免无保护追高。
- **8月25日02:00**：美国财政部长Bessent 14:00 EDT记者会，预计公布对伊朗更严厉制裁细节。策略：FU常规夜盘届时已结束，需给中国能源仓留海外隔夜gap缓冲；AG仍在夜盘窗口。[Reuters](https://www.reuters.com/world/us-treasury-secretary-bessent-hold-press-conference-monday-2026-08-21/)
- **8月25日03:00 / 04:00**：USDA Cold Storage / Crop Progress。策略：油粕/谷物有仓时控制事件Delta，弱证据不提前下注。
- **8月26日22:30**：EIA Weekly Petroleum Status Report。能源已有利润则数据前降Delta，不加码。
- **8月27—29日**：Jackson Hole Economic Policy Symposium，主题“Financial Innovation: Implications for Payments and Policy”。策略：AG/AU关注美元、实际利率和长端期限溢价，避免会前裸卖vol。[Kansas City Fed](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/)

风险预算：单一试仓最大损失0.25%–0.75% NAV；确认交易0.75%–1.50%；单一高确信主题总风险≤2.5%–3.0%。FU/BU/SC按同一能源/地缘因子合并；AG/AU按美元/真实利率/财政信用因子合并。重点压力测试周一gap、一个/两个涨跌停、保证金上调、相关性失效、流动性消失、IV跳升/塌陷和中国休市时海外大波动。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：FU2611周一回撤确认多、AG2610周一回撤确认多、FG701周一失败反弹空；BU仅在不持FU时作为替代。
C. 今天应继续观察的机会：EC2610极端动量、LC2701高波动反弹、CU2610与LME squeeze的结构错位、RM611 price/curve冲突。
D. 今天必须避免或退出的交易：周一开盘追第一跳、把周末headline当实时价格、裸买AG高IV ATM Call、在execution=false时硬报期权权利金/滑点、把FG库存绝对水平当方向确认、FU/BU/SC重复堆同一地缘因子。