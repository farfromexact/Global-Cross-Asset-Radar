# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-22

> 数据截点：北京时间2026-08-22 19:36。今天是周六，中国商品期货/期权没有日盘或21:00夜盘；中国市场最新完整交易日为2026-08-21。海外标准WTI、Brent、COMEX银等也处周末停盘期，因此不存在可被称为“15:00—19:30实时价格变化”的新报价。本报告严格把**8月21日收盘数据、8月22日周末新闻、尚未发生的下周一开盘**分开。研究与交易决策支持，不自动下单。

## 一、今日一句话结论

**今天没有可立即建立的新仓；但周末地缘并未让周一机会失效。FU2611仍是最高质量条件多，AG次之，FG为失败反弹空；真正的edge是等周一价格确认，而不是为周末新闻提前付gap溢价。**

今天的答案不是“没有机会”，而是**“有值得冒险的条件机会，但今天市场关闭，不能把条件机会伪装成可立即执行交易”**。排名仍为FU2611 79、AG2610 76、FG701 74、BU2610 72、EC2610 69；没有80分以上确认交易。

## 二、数据质量与覆盖说明

本轮第一读取层严格使用`farfromexact/China-Commodities-Engine`的`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需钻取`data/market_state_latest.json`、`data/options/quality_latest.json`和`data/options/surface_latest.json`。统一输入requested_date=`2026-08-21`，generated_at=`2026-08-21T19:02:52.405697+08:00`。周六没有新的中国交易日，因此这不是“T-1误用”，而是**最近完整交易日**。

核心Futures为2026-08-21：SHFE、INE、DCE、CZCE、GFEX五所齐全，`full_market_ready=true`、`source_date_match_pct=100%`、803个合约；unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、critical errors=0，placeholder=5个并已排除异常解释。核心行情是iFinD vendor-primary，`official_complete=false`只表示不是全量官方原始源，不代表核心EOD不可用。

Market State有20个交易日历史，1D/3D/5D/20D均锁定当前具体合约计算，不拼接日度主力。Physical仍稀疏：20个目标仅4个verified mapping且按自身发布频率fresh，其中FG周度企业库存8月21日为7441.4重量箱，但只有绝对水平，不能自动算成方向性确认；JM旬度现货/基差质量不足，I港口库存单位仍需QA，TA加工费只作context。仓单模块中DCE抓取报JSON错误，因此涉及DCE仓单的结论降级。

External仓库EOD层整体`data_fresh=false`，但per-series不能一刀切：Brent、LME铜、SGX铁矿、USDCNH、DXY中仍有按各自状态可用的context；BMD棕榈油为stale，不计证据。更重要的是今天为周六，标准海外商品市场没有19:30实时价格窗口，本轮只使用**8月21日正式收盘价+8月22日周末新闻**。Reuters显示8月21日Brent结算94.39美元/桶（+0.65%）、WTI 87.06美元/桶（+0.26%），周涨幅分别6.39%和5.66%。8月22日新增信息一边是美国周一将公布更严厉对伊制裁、Hormuz油运仍大幅受阻，另一边是伊朗允许若干伊拉克油轮特别通行；这是典型的**上行供应风险仍主导、但存在边际缓和跳空反例**。[Reuters油价](https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/) [Reuters制裁](https://www.reuters.com/world/middle-east/us-iran-keep-up-hostile-rhetoric-ahead-new-sanctions-2026-08-22/) [Reuters伊拉克油轮](https://www.reuters.com/business/energy/iran-grants-permission-number-iraqi-oil-tankers-pass-through-hormuz-2026-08-22/)

Options是最近完整交易日2026-08-21：21,816条合约记录、59/64品种、368个series；360个`surface_ready=true`、70个`positioning_ready=true`、0个`execution_ready=true`。质量文件显示IV coverage约99.69%、OI coverage约92.47%、bid/ask coverage=0。因此可以使用ATM IV、RR25、BF25、term structure和IV-RV研究，但所有具体Call Spread/Put Spread必须等真实quote；不得报净权利金、滑点或“当前可成交价”。Dealer Gamma方向未知。

Contract Metadata总体partial，contract match coverage约67.4%、effective match约73.3%，multiplier/tick coverage约29.8%。前三交易卡只使用已经由仓库/交易所规则确认的参数；未确认动态保证金或涨跌停的品种明确留空。

## 三、商品仪表盘

| 板块 | 品种/主力 | 8月21日最新有效价 | 1D / 5D | Volume / OI | ΔOI | Curve | Physical / Options | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 能源 | **FU2611** | close 3845 / settle 3850 | +2.12% / +9.81% | 650,637 / 285,614 | +8.58% | **Backwardation +7.47%** | ATM IV约43%，surface Y / exec N | **周一第一候选：回撤确认多** |
| 贵金属 | **AG2610** | 16771 / 16611 | +3.11% / +5.45% | 773,038 / 306,822 | +1.46% | 轻微Contango约-0.14% | ATM IV 47.27%，RR25 +7.81，exec N | 强趋势但Vega贵 |
| 建材 | **FG701** | 907 / 906 | -1.09% / -3.10% | 1,575,371 / 1,601,238 | +10.21% | **Contango -3.35%** | 周度库存仅level context；ATM IV 23.06%，pos Y / exec N | **失败反弹空** |
| 能源 | **BU2610** | 4508 / 4526 | +2.14% / +7.92% | 486,111 / 334,627 | -0.78% | Backwardation +3.16% | ATM IV约27.75%，exec N | 同能源因子，弱于FU |
| 原油 | **SC2610** | EOD有效 | +1.28% / +7.61% | 活跃 | +1.08% | Backwardation +4.17% | surface可研究 | 能源链确认，但不重复叠加 |
| 化工 | **MA610** | 2909 / 2880 | +1.80% / +8.56% | 1,957,108 / 873,688 | +0.69% | Backwardation +0.35% | surface Y / exec N | 等周一30–45m |
| 航运 | **EC2610** | 1957 / 1885.5 | +7.56% / +18.66% | 41,149 / OI高位 | +11.84% | 近月结构受近月效应污染 | 无完整Options闭环 | 极端动量，**不追** |
| 新能源 | **LC2701** | 158680 / 156360 | +2.60% / +1.41% | 225,444 / 353,437 | +9.91% | Contango约-0.30% | ATM IV约35.37%，exec N | 反弹≠短缺 |
| 油粕 | **RM611** | 2238 / 2246 | -1.36% / — | 747,569 / 651,265 | — | Backwardation +3.96% | surface可研究 | price/curve冲突 |
| 豆粕 | **M2701** | 3228 / 3244 | close -1.10% / — | 1,390,344 / 2,467,335 | — | Contango | BMD/进口平价不闭环 | 不追空 |
| 纸浆 | **SP2611** | 4892 / 4848 | close +3.42% / — | 535,700 / 260,902 | — | Contango | surface可研究 | 单日强、结构不确认 |
| 铁矿 | **I2701** | settle为8月21 EOD | +0.14% / — | 仓库有完整EOD | — | Market State可用 | 港口库存8/19 fresh-by-frequency；DCE仓单抓取失败 | 中性，缺闭环 |

注：Curve是期货近月—次近月结构，不是现货基差。周末没有新中国成交，表中所有中国价格均明确是8月21日EOD。

## 四、相比上一交易日晚报真正变化

1. **不是价格变化，而是周末事件分布变化。** Friday oil close进一步确认能源周线强势；Saturday美国周一制裁预告使供应尾部风险继续存在，但伊朗给予部分伊拉克油轮通行许可，说明“完全封死Hormuz”的最极端路径并非单向确定。对FU而言，这提高保留凸性的价值，却降低“周一无条件追高”的赔率。
2. **FU的国内证据没有被周末推翻。** 8月21日settle +2.12%、ΔOI +8.58%、5D +9.81%、Backwardation约7.47%，仍是最干净的price/OI/curve组合；但结构较前一日约8.16%有所收窄，不能写成供应紧张持续加速。
3. **AG的核心风险从方向转成支付价格。** 8月21日海外黄金突破三个月高位附近，弱美元/财政信用交易支撑贵金属；但AG ATM IV 47.27% vs RV20约30.82%，IV-RV约+16.45vol，周一如果gap-up，裸买Call的赔率可能明显差于方向判断本身。
4. **FG没有周末新实体数据，所以空头逻辑没有升级。** 价跌、OI增、Contango仍成立，周度库存绝对水平不算新的方向性Physical证据。它是一个等待反弹失败的交易，不是“周末越空越确定”。
5. **周末不能生成新的EC/LC确认。** 两者8月21日动量很强，但EC缺同口径欧线即期/期权闭环，LC价格上涨同时仍Contango；周末新闻不能替代缺失的产业证据。

## 五、产业链地图

| 链条 | 方向 | Price/Curve | 实体/仓单 | Options | 海外/事件 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| 原油—燃料油—沥青 | **偏多、两侧gap都大** | FU/SC backwardation确认 | 裂解/产品库存缺 | surface研究可用，exec false | Hormuz受阻+周一新制裁；伊拉克油轮获特别通行 | exact裂解、进口平价、周日重开价格 | 高 |
| 贵金属 | **偏多、高IV** | price强，curve弱 | 实体层非核心 | AG IV/skew可用但很贵 | 弱美元/财政信用；Jackson Hole在前 | 周一真实外盘与人民币映射 | 中高 |
| 建材 | **偏弱** | FG价跌/OI增+Contango | 周度库存仅level context | FG surface+positioning可用，exec false | 海外映射弱 | 库存方向、地产/深加工 | 中高 |
| 航运 | 极端强但过热 | EC动量爆发 | 即期同口径缺 | 无完整闭环 | Hormuz仅宏观背景 | SCFIS/欧线即时运价 | 中 |
| 新能源 | 高波动反弹 | LC上涨但Contango | 库存/排产缺 | surface可研究 | 无可靠进口平价 | 成本、排产、库存 | 中 |

**最强产业链仍是能源；最弱的可交易结构仍是FG建材。当前regime不是全面商品Risk-on，而是“地缘能源+贵金属信用交易”对“国内需求链偏弱”，夹杂航运/新能源高波动异常。**

## 六、机会排行榜

| Rank | 机会 | Score | 方向/持有期 | 阶段/工具 | 新鲜证据层 | 数据惩罚 |
|---:|---|---:|---|---|---:|---|
| **1** | **FU2611 周一回撤确认多** | **79** | 多 / 1–5D | 条件试仓；期货或核价后Call Spread | **4** | Physical缺；周末gap；exec=false |
| **2** | **AG2610 周一回撤确认多** | **76** | 多 / 1–5D | 条件试仓；优先有限风险Call Spread | **3** | curve弱；IV极贵；exec=false |
| **3** | **FG701 失败反弹空** | **74** | 空 / 1–5D | 条件试仓；期货或核价后Put Spread | **3** | Physical仅level；动态参数未全确认 |
| 4 | BU2610 能源趋势条件多 | 72 | 多 / 1–5D | 条件单 | 4 | 与FU高度重复；OI线索较弱 |
| 5 | EC2610 极端动量观察 | 69 | 观察 / 1–3D | 不追 | 2 | 过热；缺实体/期权/同口径运价 |

没有80+确认交易。**周末最大的No-Trade edge就是不把新闻变成“必须持仓”的冲动。**

## 七、前三名交易卡

### 1）FU2611｜条件多｜79

**事实：** 8月21日close/settle 3845/3850，1D +2.12%，5D +9.81%，ΔOI +8.58%，Backwardation约7.47%；ATM IV约43% vs RV20约37.93%。Friday Brent/WTI分别收94.39/87.06美元，周涨6.39%/5.66%。Saturday Hormuz运力仍显著受限、周一美国将公布新制裁，但若干伊拉克油轮获得特别许可。

**市场定价：** 国内已经给了显著能源风险溢价；周一再高开意味着“方向更对、入场更差”。**推断：** edge来自第一次回撤仍能被买回，而不是预测周末新闻标题。**主观判断：** 79分，仍不足以确认加仓。

**最佳表达：** 周一日盘先用FU期货确认；若Monday night仍成立，再比较2026-10-19 expiry 35–45Δ Call / 15–25Δ Call Spread。`execution_ready=false`，不报净权利金。

**入场：** 8月24日09:00以后不追第一跳；等30–45分钟。若3810–3850区域守住、重新接受3850上方且backwardation不明显压缩，先1/3风险。若日盘直接gap-up超过约2%且没有回测，放弃。周一21:00夜盘同样遵守“首次回撤守VWAP再加”的纪律。

**止损/失效：** 有效跌破3810，同时curve快速收窄；或周日/周一Brent明显回吐Friday涨幅且出现可信Hormuz缓和。**TP1/TP2：** +1R / +2R；curve较7.47%收窄约1/3时提前减仓。**时间止损：** 两个交易时段不延续即撤。**最大损失：** 0.35%–0.50% NAV；FU+BU合并初始≤0.75% NAV。

**参数：** multiplier 10吨/手；tick 1元/吨；tick value 10元；3850名义约38,500元/手。8月21日已核实的SHFE动态参数为限价14%、套保保证金15%、一般保证金16%，券商保证金另行确认；1个14%板约5,390元/手，连续两板复合约11,535元/手。常规夜盘21:00–23:00；周六今晚无交易，下一中国窗口8月24日09:00，下一夜盘8月24日21:00。交割与LTD执行前再次复核。

**1–20D催化：** 周日/周一海外重开；北京时间8月25日02:00美国财政部对伊制裁发布会；8月26日22:30 EIA；8月27–29 Jackson Hole。**最坏情景：** 周末和平/通航突变导致低开，或反向制裁升级导致涨停后流动性消失。前者用小仓位和止损，后者用有限风险期权表达而非追板。

### 2）AG2610｜条件多｜76

**事实：** 8月21日close/settle 16771/16611，1D +3.11%、5D +5.45%、ΔOI +1.46%；ATM IV 47.27%，RV20约30.82%，IV-RV约+16.45vol，RR25约+7.81。海外金价Friday继续突破，弱美元和美国财政期限溢价/信用讨论是主要宏观映射。

**市场定价：** 上行skew和Vega已经很贵。**推断：** 方向即使正确，裸Call也可能因支付过高IV而低效。**主观判断：** 更喜欢“回撤确认后的期货小仓+核价后Call Spread”，不喜欢周一追高裸Call。

**入场：** 8月24日09:00等15–30分钟；16600/16611守住并重新站稳16770附近，同时海外金银重开后没有反向。**分批：** 1/3先行，30–45分钟仍在VWAP上且创新高再加。**止损：** 30分钟接受16600下方且外盘金银同步回吐。**TP1/TP2：** +1R/+2R，IV继续抬升但期货不创新高则优先减仓。**时间止损：** 1–2个交易时段无新高。

**最大损失：** 0.35%–0.55% NAV。**期权：** 2026-09-23 expiry，长35–45Δ Call、短15–25Δ Call；真实strike与权利金等quote确认后再定。**参数：** 15kg/手，tick 1元/kg，tick value 15元，16771附近名义约251,565元；已核实限价14%、一般保证金16%/套保15%的8月21日动态状态，券商保证金未确认；白银常规夜盘21:00–02:30，但周六今晚无盘。一个14%压力约35,219元/手，两板复合约75,369元/手。

**催化：** 周末小型1-Ounce Gold已具备CME 24/7技术交易，但不拿它替代标准GC/SI流动性；标准贵金属周日晚重开后才是主要价格发现。Jackson Hole 8月27–29是未来一周最大Vega/美元事件。[CME 24/7 Gold](https://www.cmegroup.com/notices/electronic-trading/2026/07/20260713.html) [Kansas City Fed](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/)

### 3）FG701｜条件空｜74

**事实：** 8月21日907/906，1D -1.09%、5D -3.10%、ΔOI +10.21%、Contango约-3.35%；周度企业库存7441.4重量箱仅作level context；ATM IV约23.06%，FG相关series有positioning-ready样本，但全市场execution-ready仍为0。

**市场定价/推断：** 这是“价格弱+持仓扩张线索+远月贴水/近月弱结构”的失败反弹空，不是已被实体库存完全确认的供需崩塌。**入场：** 8月24日09:00等30分钟；反弹910–918失败且curve不明显收窄后空，重新跌破899才加。**止损：** 30分钟有效站稳920。**TP1/TP2：** 899 / 880附近或+2R。**时间止损：** 两交易日不破899撤。**最大损失：** 0.25%–0.40% NAV。

**参数：** 20吨/手，tick 1元/吨，tick value 20元，906附近名义约18,120元；郑商所玻璃规则确认常规夜盘21:00–23:00，但周六无交易；当前动态保证金/涨跌停本轮未得到足够新确认，因此不虚构1/2板压力金额。[CZCE玻璃业务细则](https://www.czce.com.cn/cn/uploadfile/2024/02/07/20240207103949576.pdf)

**放弃条件：** 周一直接低开跌破899不追；站稳920；或出现可验证的库存下降+深加工需求改善+curve同步收窄。

## 八、商品期权专项

代表性可复核series中，AG仍是最需要警惕的高IV：ATM IV约47.27% vs RV20约30.82%，IV-RV约+16.45vol；FU约43% vs 37.93%，+5.1vol；FG约23.06% vs 16.20%，+6.9vol；LC约35.37% vs 27.19%，+8.2vol。因为没有对全部360个surface逐一排序，本报告只称“代表样本”，不称全市场最高/最低。

Options readiness必须同时看四级：最近完整交易日共有368 series，360 surface-ready、70 positioning-ready、0 execution-ready；bid/ask coverage=0。结论很清楚：**研究可以做，精确定价不能做。** AG适合用spread压Vega；FU适合在gap风险大时把尾部损失封顶；FG适合Put Spread而不是追空期货。禁止裸卖周末事件Vega，也禁止在dealer gamma未知时编造Gamma squeeze结论。

## 九、21:00夜盘开盘风险地图（周六模式）

**今晚2026-08-22 21:00中国没有夜盘。** 上期所/郑商所连续交易均为工作日夜盘；例如白银常规21:00–02:30、燃料油21:00–23:00、玻璃21:00–23:00。下一中国交易窗口是**8月24日09:00日盘**；下一夜盘窗口是**8月24日21:00**。因此今天所谓“21:00风险地图”实际上是下周一的gap预案，而不是预测一个不存在的周六夜盘。[SHFE交易时间参考](https://www.shfe.com.cn/upload/20211110/1636525208614.pdf)

| 品种 | Friday中国结算 | 周末映射 | 周一开盘倾向 | 追价？ | 等待 | 最重要确认 |
|---|---:|---|---|---|---|---|
| **FU2611** | 3850 | 油价Friday强收；Saturday制裁升级与伊拉克通行许可并存 | 偏高但双侧gap | **否** | 30–45m | 3850接受、3810、VWAP、curve、Sunday Brent |
| **AG2610** | 16611 | 金价强、美元信用交易；周末无标准银价 | 偏高 | **否** | 15–30m | 16600、16770、GC/SI重开、DXY/收益率 |
| **BU2610** | 4526 | 同能源 | 偏高 | 否 | 30–45m | FU/SC同步、curve、外油 |
| **FG701** | 906 | 无新实体催化 | 平/偏弱 | 否 | 30m | 910–918失败、899、curve |
| **EC2610** | 1885.5 settle | Hormuz新闻只做宏观映射，非欧线即期锚 | 高波动未知 | **禁止追** | 日盘45m | SCFIS/现货运价、OI、近月污染 |
| **LC2701** | 156360 | 无周末产业闭环 | 平/高波动 | 否 | 30–45m | curve能否转强、库存/排产 |

标准WTI期货正常Globex周日18:00 ET重开，即北京时间8月24日06:00；新10-Barrel WTI的24/7产品要到8月30日才计划上线，因此**这个周末不能拿“WTI周末实时价”做FU依据**。[CME WTI交易时间](https://www.cmegroup.com/articles/faqs/faq-tuesday-and-thursday-weekly-wti-options.html) [CME新10-Barrel WTI](https://www.cmegroup.com/notices/electronic-trading/2026/08/20260817.html)

## 十、未来24h / 7d事件日历（北京时间）

- **8月24日06:00左右：** 标准CME能源/贵金属主要周日Globex重开窗口。先看Brent/WTI/GC/SI对周末Hormuz新闻的真实价格反应，再决定中国09:00是否允许试仓。
- **8月25日02:00：** 美国财政部长Bessent计划就新一轮伊朗制裁举行发布会（周一14:00 EDT）。这发生在AG夜盘尾段，但FU/FG常规夜盘已经收市；能源仓若隔夜，必须把“海外突变、中国不能即时交易”作为gap压力测试。
- **8月25日03:00 / 04:00：** USDA Cold Storage / Crop Progress（周一15:00/16:00 ET），影响肉类、玉米、豆类、棉花等农业链的次日映射。[USDA日历](https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=08&view=l&year=2026)
- **8月26日22:30：** EIA Weekly Petroleum Status Report，下一发布日期已明确为8月26日；能源多头若已有利润，数据前优先降Delta而非加码。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **8月27–29日：** Jackson Hole Economic Policy Symposium，主题“Financial Innovation: Implications for Payments and Policy”。贵金属最大风险来自美元、实际利率与政策信用重新定价；会议前不裸卖vol。[Kansas City Fed](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/)

## 十一、决策清单与风险预算

最强链条能源，最弱可交易结构FG建材；FU的price得到curve确认但没有实体闭环；AG的海外宏观确认强、curve弱、IV很贵；FG的price/curve确认较干净但Physical仍不足。没有满足exact-contract、品质、税费、运费、币种和时点一致性的正式跨市场套利。周末信息最大的价值是**决定周一要不要撤销条件单**，而不是给今天制造仓位。

单一试仓最大损失维持0.25%–0.75% NAV；确认交易0.75%–1.50%；单一高确信主题≤2.5%–3.0%。FU/BU/SC是同一能源/地缘因子，合并计算；AG/AU属于美元/真实利率/财政信用因子；所有期权结构都要压力测试IV塌陷、gap、涨跌停、保证金上调和流动性消失。

A. 今天没有应立即建立的新仓位。

B. 今天只应挂条件单的仓位：FU2611周一回撤确认多、AG2610周一回撤确认多、FG701周一失败反弹空；BU2610只作为FU替代，不重复叠加。

C. 今天应继续观察的机会：EC2610极端动量、LC2701高波动反弹、RM/M价格与curve冲突；先看周日海外重开和周一09:00第一轮价格发现。

D. 今天必须避免或退出的交易：为周末新闻预判gap、周一开盘追第一跳、裸买AG高IV ATM Call、裸卖周末事件Vega、把FG库存绝对水平当方向确认、把伊拉克油轮特别通行等同于Hormuz全面恢复、FU/BU/SC重复堆同一地缘因子。

---

### 主要来源

- China-Commodities-Engine：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`、`data/market_state_latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`，main分支，最近完整交易日2026-08-21。
- Reuters，2026-08-21/22：油价周收盘、美国对伊制裁预告、Hormuz与伊拉克油轮通行。
- EIA：Weekly Petroleum Status Report，下一发布日期2026-08-26。
- USDA NASS：2026年8月发布日历。
- Federal Reserve Bank of Kansas City：2026 Jackson Hole 8月27–29日。
- SHFE/CZCE/CME：连续交易与周末/周日重开规则。
