---
report_date: 2026-09-03
edition: commodities_morning
revision: 2
generated_at_bjt: 2026-09-03T09:15:16+08:00
commodity_trade_date: 2026-09-02
night_session_trading_date: 2026-09-03
commodity_data_fresh: true
archive_status: partial
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-03｜Revision 2

> **补跑说明：** 本版在北京时间09:15补跑，按新的 `EOD T-1 → Night Session T → Overseas → 9:00 decision` 协议重建。为避免事后偏差，不把9:00后的中国日盘价格倒灌进“晨间”判断。中国EOD为2026-09-02，Night Session交易日为2026-09-03。

## 一、今日一句话结论

**有值得冒险的机会，但只做回撤确认：EG2610 85分、MA610 82分；SC2610 76分只适合深回撤承接。新夜盘层纠正了BU/JM的错误弱势印象，9:00不追能化高开。**

最重要的变化不是方向，而是**信息质量**：现在能把“相对昨收的新增夜盘信息”和“相对昨结算的会计/风控锚”彻底拆开。结果显示EG/MA的夜盘确实继续上涨；SC几乎没有新增上涨；而BU、JM此前看起来的夜盘下跌，主要是结算锚造成的错觉。

## 二、数据质量与覆盖

第一读取层：`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`。

`report_input_latest.json` 已为schema v2，generated_at 2026-09-03 08:48:43+08，requested_date 2026-09-02，frequency=`EOD+night_session`。核心Futures五所SHFE/INE/DCE/CZCE/GFEX全覆盖，802个合约，`source_date_match_pct=100%`，`full_market_ready=true`，critical errors=0；placeholder 4条，unknown/duplicate/invalid OHLC/negative volume-OI均为0。

Night Session：`trading_date=2026-09-03`、`night_session_date=2026-09-02`，fresh/validated/published均为true；802个选定合约全部被解析，其中611个有效夜盘、187个outside-night-window、4个no-night-trade，missing/query/unresolved均为0，`coverage_complete=true`。**76.18%是有效夜盘记录占比，不是数据完整率。**

Physical：18/20 fresh，0 stale、0 carried-forward、2 unavailable。多数AKShare/100ppi现货映射缺地区/品质/含税/交割地，C级basis只作context，不计可交易基差。

External：17/22 fresh，覆盖WTI/Brent、LME Cu/Al/Zn/Ni、COMEX Au/Ag、SGX铁矿、CBOT主要农产品、BMD棕榈油、ICE糖/棉；无exact import parity时只作境内外映射。

Options：2026-09-02链18,860个合约、343个series；IV coverage 97.7%、OI coverage 68.1%、bid/ask=0。332个series已surface-ready、72个positioning-ready，但全局`surface_ready=false / positioning_ready=false / execution_ready=false`，且今天已进入9月3日交易日，所以**T-1 Options只作背景，不计今日fresh evidence，也不给精确权利金。**

Contract Metadata仍partial，尤其DCE contract-info失败；缺失动态保证金/涨跌停/交割参数必须在交易终端或交易所复核。

## 三、商品仪表盘

| 板块 | 合约 | 9/2 EOD close/settle | 5D结算收益 | Night Close | Night vs Close | Night vs Settle | Night ΔOI | EOD Curve | 信号 |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 能化 | **EG2610** | 5809 / 5726 | +9.13% | **5915** | **+1.82%** | +3.30% | **+28,490** | Back 5.96% | **85 条件多** |
| 能化 | **MA610** | 3183 / 3157 | +11.55% | **3250** | **+2.10%** | +2.95% | **+33,871** | Back 3.01% | **82 条件多** |
| 原油 | **SC2610** | 693.3 / 677.3 | +19.98% | **694.7** | **+0.20%** | +2.57% | **-300** | Back 4.25% | **76 深回撤多** |
| 沥青 | BU2610 | 4974 / 5049 | — | **5005** | **+0.62%** | **-0.87%** | -2,050 | Back 3.62% | 69 观察 |
| 贵金属 | AG2610 | 15631 / 15720 | — | **15886** | **+1.63%** | +1.06% | — | Contango 0.53% | 69 反弹检验 |
| 有色 | CU2610 | 108040 / 108110 | — | **108390** | +0.32% | +0.26% | — | 近月升水 | 观察 |
| 有色 | ZN2610 | 26585 / 26645 | — | **26520** | -0.24% | -0.47% | — | 轻Contango | 海内外背离观察 |
| 油脂 | Y2701 | 9113 / 9135 | — | **9215** | **+1.12%** | +0.88% | — | — | 66 观察 |
| 黑色 | JM2701 | 1663.5 / 1703 | — | **1668.5** | **+0.30%** | **-2.03%** | — | Back | **不再作为空头确认** |
| 新能源 | LC2701 | 154780 / 155660 | — | 无制度性有效夜盘记录 | — | — | — | Contango | 无交易 |

### Night Curve同合约对复核

必须用同一价格类型比较，不能拿EOD settlement-curve直接和Night close-curve混比：

- **EG2609/2610：EOD close-based Back约6.78% → Night close-based约6.71%：基本持平/微收窄。**
- **MA609/610：3.64% → 2.95%：明显收窄。**
- **SC2610/2611：6.29% → 6.16%：基本持平/微收窄。**

因此EG/MA夜盘上涨是真实的，但**都没有获得“Backwardation继续扩张”的二次确认**；MA尤其要因此扣分。

## 四、相比上一交易日/上一Revision真正变化

**1. EG夜盘不是“约+3%”，而是对昨收真正新增+1.82%。** EG2610夜盘O/H/L/C=5780/5915/5711/5915，夜盘OI从379,746升至408,236，ΔOI +28,490。价格、OI都继续强化，但近远月close-based Back没有扩大，因此85分而不是更高。华东主港最新库存约14.2万吨，较前一统计周期下降约3.6万吨，仍支持近端tightness；反方是国内供应恢复与聚酯负荷变化。

**2. MA夜盘对昨收+2.10%，而且Night ΔOI转为+33,871。** 白天OI下降，夜盘OI又明显回升，但这只能叫归因线索，不能直接写“新多进场”。9月2日港口库存64.15万吨，周降4.41万吨/-6.43%；华东和华南都去库，且当周有14.92万吨显性外轮卸入。问题是MA609/610的close-based Back夜盘从3.64%收窄到2.95%，说明近端紧张并未进一步加速，所以82分。

**3. SC的“利多钝化”得到正式repo确认。** 美国商业原油库存单周下降450万桶至424.5百万桶，显著超过市场预期的110万桶降幅；炼厂利用率98%。Brent收95.63、WTI收91.01，Hormuz通行仍高度不稳定。但SC2610夜盘694.7仅比日盘close 693.3高0.20%，Night ΔOI -300。**相对结算+2.57%不能再被解释为新增强势。**

**4. BU上一版“夜盘弱”需要纠正。** BU2610夜盘5005实际上比日盘close 4974高0.62%；只有相对settlement 5049才是-0.87%。所以“夜盘价格否决基本面”说得太重了。但Night ΔOI -2,050、日盘OI也下降，且相对强度明显不如EG/MA，因此仍只给69分。

**5. JM空头确认被撤销。** JM2701夜盘1668.5比日盘close 1663.5高0.30%，所谓“-2.03%”来自对1703 settlement的比较。**因此上一版“焦煤夜盘再跌2%”的交易含义是错误的。** 黑色终端需求仍弱，但焦煤现货/竞拍并不形成三层一致空头，JM从机会榜删除。

**6. 贵金属反弹强度也被低估。** AG2610夜盘对昨收实际+1.63%，而不是只看结算锚的+1.06%。海外黄金反弹超过1%、白银约+1.2%，美债收益率和美元从高位回落。低位继续追空的赔率进一步恶化。

## 五、产业链地图

| 产业链 | 方向 | EOD→Night | Curve | Physical/海外 | 最大反证 | 置信度 |
|---|---|---|---|---|---|---|
| **EG—聚酯** | 偏多 | +1.82%，ΔOI +28,490 | 高Back但夜盘未扩 | 港库极低；进口物流风险 | 国内供应恢复 | 高 |
| **MA—MTO** | 偏多 | +2.10%，ΔOI +33,871 | **夜盘Back收窄** | 港库-6.43% w/w | MTO偏弱、curve未强化 | 高- |
| **SC原油** | 多但赔率差 | **仅+0.20%** | 高Back但微收窄 | EIA大去库、Hormuz风险 | 利多弹性衰减 | 中高 |
| BU—沥青 | 中性偏多 | +0.62%，ΔOI -2,050 | Back | 低库存背景 | OI不确认、相对弱 | 中 |
| 贵金属 | 反弹检验 | AG +1.63% | Contango | 美元/收益率回落 | 能源再冲高→实际利率压力 | 中 |

## 六、机会排行榜

| Rank | 机会 | 分数 | Fresh层 | 阶段 | 核心约束 |
|---:|---|---:|---:|---|---|
| 1 | **EG2610 回撤承接多** | **85** | 4 | confirmed_wait_trigger | 5D已涨9.1%，Night curve未继续扩 |
| 2 | **MA610 回撤承接多** | **82** | 4 | confirmed_wait_trigger | Night Back收窄，不能追3250以上 |
| 3 | **SC2610 深回撤承接多** | **76** | 4 | conditional_trial | 超强利多后vs close仅+0.20% |
| 4 | BU2610 重新获得OI确认后多 | 69 | 3 | watch | 价格修复但OI仍弱 |
| 5 | AG2610 反弹失败/延续二选一观察 | 69 | 2 | watch | 宏观反弹尚未形成趋势证据 |

JM不再进入榜单：夜盘对昨收并未下跌，缺乏新的空头价格确认。

## 七、前三名交易卡

### 1. EG2610｜85｜回撤承接多

**事实：** EOD 5809/5726；Night 5780/5915/5711/5915；vs close +1.82%，vs settlement +3.30%；Night ΔOI +28,490。EOD close-based EG2609/2610 Back约6.78%，夜盘约6.71%。

**判断：** 方向仍多，但夜盘已经把一部分tightness重新定价，且curve没有进一步扩张，所以只买回撤，不买首跳。

**入场：** 若开盘/盘中重新回到5860—5910并出现承接，重新站回VWAP或首30—45分钟高点后先1/3；直接大幅高于5915不追。  
**初始止损：** 30分钟接受低于5750。  
**逻辑失效：** 5650下方 + 近端Back明显压缩 + 港库/进口正常化。  
**TP1/TP2：** 6050 / 6250。  
**时间止损：** 2个交易日没有继续扩张。  
**风险预算：** 0.50%—0.75% NAV。

DCE动态保证金、price limit和最后交易日当前metadata仍未闭环，执行前必须终端复核。

### 2. MA610｜82｜回撤承接多

**事实：** EOD 3183/3157；Night 3160/3252/3141/3250；vs close +2.10%，vs settlement +2.95%；Night ΔOI +33,871。港口库存64.15万吨，周降6.43%。MA609/610 close-based Back从3.64%收窄到2.95%。

**判断：** Physical和夜盘价格都支持多头，但curve没有确认“更紧”，所以比EG低一档。

**入场：** 3180—3230回撤被吸收，重新站回VWAP/3250附近再做1/3；明显高于3250不追。  
**初始止损：** 3130下方形成30分钟接受。  
**逻辑失效：** 3050下方 + 近端Back继续明显收窄 + 港口重新持续累库。  
**TP1/TP2：** 3320 / 3450。  
**时间止损：** 2—3日。  
**风险预算：** 0.35%—0.50% NAV。

### 3. SC2610｜76｜只做深回撤承接

**事实：** EOD 693.3/677.3；Night 686/706.3/681.9/694.7；vs close仅+0.20%，vs settlement +2.57%；Night ΔOI -300。EIA原油库存-450万桶，Brent 95.63、WTI 91.01。

**判断：** 基本面强，但新增信息对价格的边际弹性明显不足。最容易犯的错误是“新闻越利多，仓位越大”。

**入场：** 不追700以上；至少等待45分钟。只有680—690区域获得承接后重新站回695/VWAP才试1/3。  
**初始止损：** 670下方30分钟接受。  
**逻辑失效：** 660下方 + Brent跌破约93 + Hormuz/外交出现可信快速正常化。  
**TP1/TP2：** 715 / 740。  
**时间止损：** 1—2日。  
**风险预算：** 0.25%—0.35% NAV。

## 八、商品期权专项

9月2日期权链本身并非“没有surface”：343个series里332个surface-ready，MA等多个品种有可研究的曲面；但今天是9月3日，**它们是T-1背景**。同时执行层仍为0个series ready，bid/ask覆盖为0。

因此可用于理解昨日vol regime，但不能作为今日fresh第5层；不报精确strike/净权利金/滑点；不推Dealer Gamma。若盘中人工拿到同日quote，优先研究EG/MA有限风险Call Spread，而不是裸期货追高。

## 九、9:00开盘风险地图（补跑时保留晨间ex-ante口径）

| 品种 | Previous EOD | Night新增 | Overseas映射 | 晨间动作 |
|---|---|---|---|---|
| **EG2610** | 强+高Back | **+1.82%，ΔOI显著增** | 能源/物流风险支持 | **等30—45m，不追高** |
| **MA610** | 强+去库 | **+2.10%，但Back收窄** | 中东进口风险支持 | **等30—45m，3250上方不追** |
| **SC2610** | 已大涨 | **仅+0.20%** | Brent/WTI/EIA仍利多 | **等45—60m，只做深回撤** |
| BU2610 | 相对弱 | +0.62%，但ΔOI负 | 原油支持 | 先看OI是否重新扩张 |
| AG2610 | EOD大跌 | **反弹+1.63%** | 金银同步反弹 | 禁止低位追空 |
| JM2701 | EOD close偏弱 | **+0.30% vs close** | 产业需求仍弱 | 不追空，重新评估 |

## 十、未来24小时 / 7日事件

- **9月3日20:30 BJT**：美国Q2 Productivity and Costs修订值；利率/美元/贵金属敏感。
- **9月3日22:30 BJT**：EIA Weekly Natural Gas Storage Report。
- **9月4日20:30 BJT**：美国8月Employment Situation / 非农；金银、美元、实际利率、铜、原油一级宏观节点。
- **9月6日**：OPEC+核心成员会议；Reuters基准预期为10月产量政策大概率维持不变。
- **持续**：Hormuz航运、美国—伊朗冲突、矿山/炼厂/港口扰动。

## 十一、风险预算

EG/MA/SC/BU/FU等共享“中东供应冲击 + 中国能化beta”，不能当独立alpha叠加。EG 0.50%—0.75% NAV；MA 0.35%—0.50%；SC 0.25%—0.35%；初始同因子总风险 **≤1.25% NAV**。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：EG2610回撤承接多；MA610回撤承接多；SC2610仅深回撤承接多。  
C. 今天应继续观察的机会：BU2610能否重新获得OI确认；AG反弹是延续还是失败；ZN的LME—SHFE方向背离；Y2701夜盘强势是否获日盘确认。  
D. 今天必须避免或退出的交易：追EG/MA/SC高开；把vs settlement涨跌误当夜盘新增信息；追空JM；低位追空AG；任何基于T-1且execution-not-ready期权数据的精确成交建议。

## 来源

1. China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
2. Reuters — US crude stocks fall on strong refining activity and exports: https://www.reuters.com/business/energy/us-crude-gasoline-inventories-fell-last-week-distillates-rose-eia-says-2026-09-02/
3. Reuters — Oil settles 1% higher as US-Iran strikes threaten supplies: https://www.reuters.com/business/energy/oil-up-nearly-1-us-iran-trade-fresh-strikes-2026-09-02/
4. Reuters — Gold rebounds over 1% as dollar/yields pull back: https://www.reuters.com/world/india/gold-hits-over-3-week-low-mideast-tensions-fan-rate-hike-fears-2026-09-02/
5. 隆众资讯/同花顺 — 甲醇港口库存: https://news.10jqka.com.cn/20260902/c679526274.shtml
6. Mysteel — 乙二醇主港库存: https://www.mysteel.com/hot/1600630.html
7. BLS release calendar: https://www.bls.gov/schedule/2026/
8. EIA Weekly Natural Gas Storage Report: https://ir.eia.gov/ngs/ngs.html
9. Reuters — OPEC+ likely to keep output policy unchanged: https://www.reuters.com/business/energy/opec-likely-to-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-02/
