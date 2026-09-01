# 全球商品期货期权高风险机会雷达（晚间版）｜2026-09-01

> **今天的商品市场究竟有没有值得冒险的机会？**
>
> **没有。** 截至本报告生成时，China-Commodities-Engine 的统一 EOD 汇总仍停在 **2026-08-31**，因此 9 月 1 日的 current curve / ΔOI / RV / options surface 不能由引擎闭环验证。今天中国能化强、贵金属弱的方向非常清晰，但按五层证据纪律，最强候选只有两层 fresh evidence，评分上限 69。

**今日商品期货期权无合格交易。**

最接近触发的三个观察项是：**AU 反弹失败空（69）**、**EG2610 回撤承接多（69）**、**SC2610 供应冲击延续（68）**。共同缺口是当前中国 T 日 curve/OI/options 尚未进入引擎；因此今晚的 edge 不是抢第一跳，而是用 21:00 后 30—45 分钟换取信息质量。

## 一、今日一句话结论

**没有合格新仓：能源/化工继续挤风险溢价，贵金属受利率和美元压制，但 T 日中国 curve/OI/options 缺席，所有候选按纪律压在 69 分以下。**

## 二、数据质量与覆盖说明

本次严格按 `china_commodities_v2` 读取，第一层实际读取：
- `data/report_input_latest.json`
- `data/last_run_status.json`
- `data/radar_latest.json`

按异常与候选钻取：
- `data/latest.json`
- `data/market_state_latest.json`
- `data/physical/latest.json`
- `data/external/latest.json`
- `data/options/quality_latest.json`
- `data/options/surface_latest.json`
- `data/contract_meta.json`
- `data/night_session/latest.json`

**关键时点问题**：`report_input_latest.json` 的 `requested_date=2026-08-31`，`generated_at=2026-09-01T07:26:29.522859+08:00`；到晚间报告时仍未切到 9 月 1 日。`data/latest.json` 与 `market_state_latest.json` 同样仍为 8 月 31 日。因此今天不能把 8 月 31 日的 curve、OI attribution、RV20、options surface 冒充 9 月 1 日数据。

8 月 31 日引擎自身的核心 Futures 质量是好的：五所 **SHFE/INE/DCE/CZCE/GFEX** 全覆盖，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0，carried-forward core futures=0。`official_complete=false` 主要来自非核心 metadata/module 问题，而不是核心期货行情失败。换言之：**数据不是“坏”，而是“晚了一天”。**

Physical：4/20 映射，均只能按自身发布频率理解。铁矿港口库存、焦煤现货、玻璃企业库存、PTA加工费有上下文，但没有足够 9 月 1 日方向变化可形成完整 fresh Physical 层。JM basis 为 C 级，不计方向评分；今天没有把任何商业代理基差包装成可套利 basis。

External：仓库 EOD 层与 15:00—19:30 海外实时层分开。仓库里部分海外 series 仍有有效 context，但今晚评分采用 Reuters 的盘中海外变化，不用旧 EOD 冒充实时。

Options：截至 8 月 31 日共 22,674 个 unique contracts、64/64 products、383 series；IV coverage 76.06%，OI coverage 67.70%，bid/ask coverage 0；274/383 `surface_ready`，31/383 `positioning_ready`，0/383 `execution_ready`。由于是 **T-1**，今晚全部只作波动率背景，**不计 9 月 1 日 fresh evidence**；也不提供虚构 strike、bid/ask、净权利金或可成交成本。

Contract metadata：partial；DCE metadata 存在 JSON decode 问题。前三卡片仅使用能重新确认的稳定参数；动态保证金/涨跌停、未确认夜盘安排明确标“未确认”。

## 三、商品仪表盘

| 板块 | 品种/合约 | 9/1最新有效价 | 1D | 5D/1周 | Volume / OI / ΔOI | Curve / Basis | Physical / Options | 信号 |
|---|---|---:|---:|---:|---|---|---|---|
| 能源 | SC2610 | 637.8 | +3.15% | +9.19% | T日引擎缺 | T-1 near-next约 -2.05% contango，仅背景 | 无T日Physical；Options T-1 | 强但curve未获T日确认 |
| 化工 | EG2610 | 5525 | +6.37% | T日引擎5D缺 | T日引擎OI缺 | T-1约 +5.33% backwardation；商业现货5930/基差405仅context | 港口低库存产业信息偏多；Options T-1 | 最强链，但极度延伸 |
| 化工 | MA610 | 3069 | +5.43% | T日引擎5D缺 | Vol 2,370,930；OI 664,801；ΔOI -48,064 | T-1 backwardation仅背景 | Physical映射缺；Options T-1 | 涨价减仓，追价质量下降 |
| 聚酯 | PX/TA/PR | 主力涨 +4.01/+3.17/+4.36% | 强 | — | T日细项缺 | T日curve缺 | 成本冲击主导 | 强beta，不独立追 |
| 贵金属 | AU主力 | 959.94元/克 | -1.87% | — | OI -6,896（代理） | T日curve缺 | spot gold later -1.8%；Options T-1 | 利率/美元压制，候选反弹空 |
| 贵金属 | AG主力 | — | -2.54% | — | T日引擎缺 | T日curve缺 | silver later -2.8%；Options T-1 | 同向弱，但波动更大 |
| 有色 | CU主连 | 109220 / settle 109520 | +0.50% | — | Vol 97,783；OI 224,404 | T日curve缺 | 海外宏观偏空；exact parity缺 | 内外冲突，暂不做 |
| 有色 | ZN主力 | — | +2.71% | — | T日引擎缺 | T日curve缺 | Physical/Options闭环缺 | 国内相对强 |
| 黑色 | I主力 | — | +0.14% | — | T日引擎缺 | T日curve缺 | 港存为最新原频率context | 中性 |
| 黑色 | RB/HC | — | -0.38/-0.47% | — | T日引擎缺 | T日curve缺 | 实体闭环缺 | 明显弱于能化 |
| 农牧 | LH主力 | — | -2.67% | — | T日引擎缺 | — | USDA/养殖新证据缺 | 单日弱，不能直接下注 |
| 航运 | EC | — | 数据未闭环 | — | — | — | **无夜盘** | 下一窗口9/2 09:00 |

中国 9 月 1 日收盘显示能化显著领涨：EG +6.37%、MA +5.43%、PR +4.36%、BU +4.18%、V +4.09%、PX +4.01%、TA +3.17%；贵金属则 AU -1.87%、AG -2.54%。黑色整体偏弱，I +0.14%、RB -0.38%、HC -0.47%。来源：Financial界 15:28 汇总。  
https://finance.jrj.com.cn/2026/09/01152858315214.shtml

MA610 的精确日盘数据：开3013、高3115、低2987、收3069，+5.43%，成交2,370,930，持仓664,801，日减48,064。**“价涨仓减”只能作为归因线索，不等于已经证明空头回补。**  
https://goodsfu.10jqka.com.cn/20260901/c679492438.shtml

EG2610 收5525；生意社基准现货5930，计算代理 basis +405。该口径缺少交割地/品质/税费/时点的完整对齐，因此这里只作为商业 context，不纳入可交易 basis 层。  
https://goodsfu.10jqka.com.cn/20260901/c679496340.shtml

CU 主连 15:00 收109220、结算109520，成交97,783、持仓224,404。  
https://hq.smm.cn/futures/104091439

## 四、相比上一交易日真正变化

**1. 最大变化不是行情，而是数据闸门。** 昨晚 8 月 31 日的报告能直接使用当日引擎 curve/OI；今晚 9 月 1 日统一汇总仍是 T-1。因此昨晚 EG/MA 的“价格+curve+海外”三层证据，今晚不能机械延续为三层。

**2. 能化的价格动量再次扩张。** EG +6.37%、MA +5.43%，且 PX/TA/PR/V/BU 集体上行。这不是一个孤立品种的 spike，而是地缘—原油—进口化工/成本链的系统性 beta 扩散。

**3. 海外原油在中国15:00以后继续上涨。** Reuters 约18:46 BJT 报 Brent 92.21美元/桶，+1.9%；WTI 87.88，+2.47%。这部分信息中国日盘尚未交易，只能作为今晚 gap 映射，不能写成“中国原油已经涨了”。  
https://www.reuters.com/business/energy/oil-prices-rise-latest-fighting-resurrects-middle-east-supply-disruption-risks-2026-09-01/

**4. 贵金属出现“地缘更紧、金银反而更弱”。** Reuters 约18:03 BJT spot gold 4369.24，-1.8%；silver 64.64，-2.8%。核心解释是全球债券抛售与更高收益率抬升持有黄金的机会成本。  
https://www.reuters.com/world/india/gold-muted-traders-await-us-jobs-data-monitor-mideast-tensions-2026-09-01/

**5. 美元与利率方向对金属不友好。** Reuters 报美元指数约 +0.2%，美国10Y收益率升至2025年1月以来高位附近；这强化 AU/AG 的反弹空逻辑，但同时也提高油价—通胀—利率的跨资产联动风险。  
https://www.reuters.com/world/asia-pacific/yen-hangs-near-160-amid-boj-rate-hike-bets-dollar-wobbles-2026-09-01/

**6. MA 的追价质量恶化。** +5.43% 的同时 OI -48,064；这不证明“空头回补”，但至少说明不是一个简单的“价格涨+仓位同步扩张”结构。

## 五、产业链地图

| 产业链 | 方向 | 最强/最弱 | Price | Curve | 库存/仓单/实体 | Options | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|---|
| 原油→进口化工→EG/MA/PX/TA | 强多但过热 | EG最强 | 强确认 | **T日缺**；T-1 EG/MA backwardation仅背景 | EG低港存产业信息偏多，但仓库T日映射不足 | T-1，不计分 | Brent/WTI继续涨 | T日curve/OI/options | 中 |
| 贵金属→利率/美元 | 偏空 | AG弱于AU | 中外同弱 | T日缺 | 实体意义较低 | T-1 | gold/silver弱、USD/yields强 | T日options/curve | 中 |
| 有色→中国增长/美元 | 分化 | ZN强，CU中性 | 国内偏强 | T日缺 | exact parity/升贴水不闭环 | T-1 | 宏观偏逆风 | 沪伦exact parity | 低 |
| 煤焦钢→地产工业需求 | 弱/平 | RB/HC弱 | 弱 | T日缺 | I库存只有原频率context | T-1 | 映射弱 | 当前curve与实体需求 | 低 |
| 油脂饲料畜牧 | 分化 | LH最弱 | 油脂/粕小涨，LH跌 | 缺 | USDA/天气/进口新证据缺 | T-1 | 未形成同向海外层 | fresh physical | 低 |

**最强产业链：原油—进口化工。最弱产业链：贵金属（相对宏观冲击）与黑色成材。**

当前 regime 是 **Hormuz供应通道冲击 + 油价推动通胀/利率重定价 + 中国能化动量挤压 + 贵金属收益率冲击 + 中国EOD时点错配**。这意味着同一条地缘消息既可能利多油，也可能通过通胀/利率利空金；不能用简单“战争=所有避险资产上涨”处理。

## 六、机会排行榜

严格重算五层证据：①价格—成交—持仓；②curve/高质量basis/仓单；③实体供需；④海外/宏观；⑤期权。

今晚 **T日引擎curve/OI/options缺失**；即使有中国收盘价格和实时海外映射，大多数候选最多只有 **①+④两层 fresh evidence，评分上限69**。

| 排名 | 机会 | 分数 | 方向 | 持有期 | 阶段 | 工具 | Fresh层 | 数据惩罚 |
|---|---|---:|---|---|---|---|---|---|
| 1 | AU反弹失败空 | **69** | Short | 1–3D | 条件观察 | Futures；put spread仅研究 | ①④ | 无T日curve/OI/options；地缘反转风险 |
| 2 | EG2610回撤承接多 | **69** | Long | 1–5D | 条件观察 | Futures；call spread仅研究 | ①④ | T-1 backwardation不能计；涨幅极度延伸 |
| 3 | SC2610供应冲击延续 | **68** | Long | 1–3D | 条件观察 | Futures | ①④ | T-1仍contango；无T日physical/options |
| 4 | MA610回撤承接多 | **66** | Long | 1–5D | 观察 | Futures | ①④ | OI下降；current curve缺 |
| 5 | CU2610相对弱化 | **63** | Short watch | 1–3D | 观察 | Futures | ①④ | 中国+0.5%与美元/利率逆风冲突；parity缺 |

**今日商品期货期权无合格交易，保留现金和观察仓。**

## 七、前三名交易卡

### 1）AU：反弹失败空｜69

**方向**：只在反弹失败后做空，不追21:00第一跳。  
**事实**：中国沪金主力日盘959.94元/克、-1.87%；代理数据显示OI减6,896。海外截至约18:03 BJT，spot gold 4369.24美元/盎司、-1.8%，silver -2.8%；美元指数约+0.2%，美债收益率显著上行。  
**市场定价**：当前市场优先交易更高利率/更强美元，而不是单纯地缘避险。  
**推断**：若海外金价持续在4400以下、10Y维持高位，而中国夜盘开盘后的反弹无法收复opening range中枢，延续下行的概率提高。  
**主观判断**：这笔交易真正的 edge 是“等反弹失败”，而不是“猜今晚低开多少”。

**最佳表达**：确认后的 AU 期货空；若之后 live chain `execution_ready=true`，优先有限损失 put spread。今晚不能给精确期权strike/premium。  
**入场**：等21:00后30分钟；要求 spot gold <4400、US10Y大致>4.75%、中国合约反弹失败。  
**分批**：1/3 failure；新低且海外同步再1/3；最后1/3仅在当前curve/OI补齐后。  
**初始止损**：首30分钟结构高点之上；或spot gold收复4420且收益率回落。  
**逻辑失效**：US10Y <4.70、DXY快速转弱、或地缘冲击令gold >4420并站稳。  
**TP1/TP2**：1R / 2R，今晚不在exact T-day contract map缺失时伪造绝对价格目标。  
**时间止损**：1–3D。  
**最大损失**：NAV 0.25%–0.50%。  
**催化**：JOLTS、ADP、NFP、Hormuz headline。  
**最坏情景**：突发停火/再升级皆可造成金价gap；严禁裸卖期权。  
**放弃条件**：>1%下跳直接追空；gold >4420且10Y回落；合约元数据无法确认。

参数：1000g/手；tick 0.02元/g；tick value 20元；按959.94计notional约95.994万元/手。动态margin/limit未确认。夜盘21:00–02:30。实物交割；交割月前退出。

### 2）EG2610：回撤承接多｜69

**事实**：9/1收5525，+6.37%；商业现货基准5930给出+405代理basis，只作context。8/31引擎的 near-next约+5.33% backwardation是T-1背景，不能加今天的分。Reuters晚间Brent继续上涨。产业媒体同时提示EG港口库存低，但远期供应回归/下游负反馈也在累积。  
https://finance.sina.com.cn/money/future/fmnews/2026-09-01/doc-iniqipiw3538815.shtml

**市场定价**：进口受阻和原油成本冲击已经被快速重估。  
**推断**：若今晚当前 near-next 仍保持明显 backwardation、OI没有崩塌，同时5525/首30分钟低点被守住，才说明不是纯headline squeeze。  
**主观判断**：两天连续大涨后，不追首跳比方向判断更重要。

**最佳表达**：确认后EG2610期货；call spread仅在T日链、bid/ask和execution readiness出现后执行。  
**入场**：等待30–45分钟；若gap>2%直接放弃追价；要求5525或首30分钟低点守住、回收opening midpoint/high，同时current curve确认。  
**分批**：1/3价格确认；1/3 curve确认；最后1/3 OI不崩塌。  
**初始止损**：首45分钟结构低点下方。  
**失效**：Brent<90；Hormuz缓和；current curve翻成contango；失守5525且不能快速收复。  
**TP1/TP2**：1R / 2R或随backwardation扩张移动。  
**时间止损**：1–5D。  
**最大损失**：NAV 0.25%–0.50%。  
**最坏情景**：地缘缓和导致跨夜gap-down、保证金上调、流动性骤降。  
**放弃条件**：开盘gap>2%；current curve不确认；live oil反转。

参数：稳定合约规格10吨/手、tick 1元/吨、tick value 10元；5525时notional约55,250元/手。DCE metadata partial，**动态margin/limit、当前精确夜盘资格未独立确认**；不猜。最后交易日稳定规则为交割月倒数第4个交易日，但EG2610具体日期需交易所日历再确认。

### 3）SC2610：供应冲击延续｜68

**事实**：9/1 SC2610收637.8，+3.15%，公开数据5D约+9.19%。15:00以后海外又涨：Reuters约18:46 BJT Brent 92.21 +1.9%，WTI 87.88 +2.47%。同时Hormuz船舶通行仍低，且有油轮遇袭，风险真实存在。  
https://www.reuters.com/business/energy/oil-prices-rise-latest-fighting-resurrects-middle-east-supply-disruption-risks-2026-09-01/

**市场定价**：战争/通道风险已明显进入价格，但8/31中国引擎curve仍约2.05% contango，这个警告不能被价格涨幅抹掉。  
**推断**：真正升级交易的条件不是“Brent又涨了”，而是今晚SC在小幅gap后被接受、且**current contango明显收窄**。  
**主观判断**：愿意错过前45分钟；如果它真是可持续供应冲击，后面还有机会。

**最佳表达**：SC2610期货确认后多。  
**入场**：>=45分钟；Brent>91；中国gap<2%；首45m low守住；current near-next contango收窄。  
**分批**：1/3 price acceptance；curve确认后加1/3；第三份只在shipping disruption继续恶化时。  
**止损/失效**：首45m low下；Brent<90；Hormuz缓和；contango持续/扩大。  
**TP1/TP2**：1R / 2R；若Brent突破约94.8再考虑trail。  
**时间止损**：1–3D。  
**最大损失**：NAV 0.25%–0.50%。  
**最坏情景**：停火或通道恢复造成大幅gap-down。  
**放弃条件**：gap>2%；Brent<90；current curve不改善。

参数：1000桶/手，tick 0.1元/桶，tick value 100元；637.8时notional约637,800元/手。最新已检索INE 2026-06-23通知曾给SC2610涨跌停14%、套保保证金15%、一般保证金16%，但均可能被后续风控通知调整，执行前必须重新确认。按14%**仅作压力测试基准**，单个不利涨跌停约89,292元/手；连续两次复合约191,084元/手。夜盘21:00–02:30。  
https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html

## 八、商品期权专项

**数据状态：T-1（2026-08-31）**。383个series里274 surface-ready、31 positioning-ready、0 execution-ready。全市场 `positioning_ready=false` 不能否定那31个局部ready series，但由于今晚是T-1，它们仍不能算9/1 fresh evidence。bid/ask coverage=0，因此今天不能声称任何结构“可按某价格成交”。

因此今晚不宣布“全市场最高/最低IV”。没有足够T日series扫描就不做这种排名。

研究优先级：
- **AU**：如果夜盘后T日surface出来且skew/quotes正常，反弹失败空更适合 put spread，而不是裸空高波动gamma。
- **EG**：如果当前IV相对RV没有过度抬升，bull call spread可替代追期货；若IV已经爆炸，则宁愿等回撤。
- **SC**：EIA + Hormuz形成event convexity，但当前0 execution-ready，不能给strike/premium。
- **跨品种vol RV**：能源Vega与贵金属Vega的驱动已经分裂，但缺同日、同期限、同Delta的可比surface，不做伪RV。

**必须回避**：裸卖AU/AG/SC/EG事件期权；任何基于缺bid/ask数据计算出的“低成本”；任何dealer gamma方向推断，因为 `dealer_gamma_direction_known=false`。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国最近日盘 | 15:00—19:30海外映射 | 预期 | 置信度 | 追价？ | 等待 | 开盘后最重要确认 | 夜盘 |
|---|---|---|---|---|---|---|---|---|
| SC | 637.8 +3.15% | Brent +1.9%、WTI +2.47% | 偏高开 | 中 | **不追** | 45m | gap大小、Brent>91、current curve contango是否收窄 | 21:00–02:30 |
| MA | 3069 +5.43%，OI -48,064 | oil/Hormuz偏多 | 偏高开 | 中低 | 不追 | 30–45m | 首跳接受度、current curve、OI是否继续掉 | 21:00–23:00 |
| EG | 5525 +6.37% | oil/Hormuz偏多 | 偏高开 | 中低 | **最不该追** | 45m | current backwardation、OI、5525承接 | **当前精确资格未确认** |
| AU/AG | -1.87/-2.54% | gold -1.8%、silver -2.8%，USD/yields强 | 偏低开 | 中 | 不追空 | 30m | overseas metal是否继续弱、10Y、DXY | 21:00–02:30 |
| CU/ZN | +0.50/+2.71% | 美元/利率逆风，金属方向不完全一致 | 分化 | 低 | 否 | 30m | LME/SHFE同步、USD/CNH、OI/curve | 夜盘存在，截止时点执行前再核 |
| EC | 日盘数据 | — | — | 高 | — | — | — | **无夜盘；下一窗口9/2 09:00** |
| LC/SI/PS | 日盘数据不闭环 | 宏观映射弱 | 未确认 | 低 | 否 | — | 先确认交易时段 | **夜盘安排未确认；若无则9/2 09:00** |

今晚真正该等30—45分钟的不是所有品种，而是**已经有大幅日盘趋势、又面临海外二次冲击的品种**：EG/MA/SC/AU/AG。首跳的信息含量很低，尤其是EG/MA这种已经连续扩张的品种。

## 十、未来24h / 7d事件日历（北京时间）

- **9/1 22:00：美国7月JOLTS**。BLS官方日历确认9/1 10:00 ET发布。对AU/AG/CU主要通过USD/利率，对SC通过“增长预期 vs 通胀”二阶影响。今晚事件前不加无上限Vega。  
  https://www.bls.gov/schedule/news_release/jolts.htm
- **9/2约20:15：ADP 8月就业**。具体时间执行前再查live calendar；处理上与JOLTS一致，贵金属仓位不在数据前放大。
- **9/2 22:30：EIA Weekly Petroleum Status Report**。标准周三10:30 ET。SC不能只看headline crude inventory，要一起看成品油、炼厂开工、进出口。  
  https://www.eia.gov/petroleum/supply/weekly/schedule.php
- **9/4 20:30：美国8月非农**。金银/美元/利率的最大周内催化之一。优先有限风险结构。
- **9/6：OPEC+七国月度会议**。OPEC官方8/2公告称9月调整18.8万桶/日，并确认下次会议9/6。需要把OPEC政策供给与Hormuz物理通道风险拆开。  
  https://www.opec.org/pr-detail/1854611-2-august-2026.html
- **未来7天持续：Hormuz船舶通行、油轮事件、美国/伊朗军事与外交消息**。这是最大gap源；对能源多头是正催化，同时可能通过通胀和债券收益率压制贵金属/有色风险偏好。

## 十一、今天到底该怎么做

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：AU反弹失败空（69）、EG2610回撤承接多（69）、SC2610供应冲击延续（68）；都必须等夜盘30—45分钟并补上当前价格/curve/海外确认。  
C. 今天应继续观察的机会：MA610（66）、CU相对弱化（63），以及EG/SC的T日curve是否与价格重新同向。  
D. 今天必须避免或退出的交易：追EG/MA/SC首跳；把T-1 options/curve当9月1日fresh evidence；把商业basis代理包装成可套利basis；裸卖事件期权；动态margin/limit未确认时按旧参数放大仓位。

### 风险预算

单一试仓最大损失 **NAV 0.25%–0.50%**，今晚即使触发也不建议超过0.75%；只有恢复到至少3层fresh evidence后，确认交易才允许进入0.75%–1.50%。EG/MA/SC/PX/TA本质是同一个Hormuz/oil factor，要合并计风险；AU/AG则是同一个rates/USD/Vega factor。单一高确信主题总风险硬上限2.5%–3.0%，今晚应显著低于这个上限。

压力测试必须覆盖：一个/两个涨跌停、地缘突然缓和、相关性破裂、夜盘流动性消失、保证金上调、IV跳升/塌陷、交割挤压、人民币急变、以及中国休市期间海外剧烈波动。

---

**归档数据协议**：`china_commodities_v2`。  
**China-Commodities-Engine交易日**：2026-08-31（T-1；9/1尚未进入统一EOD）。  
**报告日期**：2026-09-01。  
**CI状态**：`pending_or_unverified`；本报告不等待CI。
