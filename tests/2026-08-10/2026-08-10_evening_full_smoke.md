# 全球跨资产高风险机会雷达｜晚间版完整链路测试
## 2026-08-10

**数据截点：北京时间 2026-08-10 22:28 左右。** 本报告是独立测试产物，不覆盖正式 morning/evening 报告。美国现金股市已开盘不久，因此美股、油价与部分利率使用 8 月 10 日盘中可核验快照；美国财政部官方收益率曲线使用最近完整官方日 8 月 7 日。中国衍生品严格读取 `farfromexact/China-Options-Engine/data/radar_latest.json` 与 `data/radar_history.json`：最新数据日期 **2026-08-10**，`generated_at=2026-08-10T20:34:26.951229+08:00`，`data_fresh=true`，CFFEX official EOD 与 futures 均为 `ok`，期权官方匹配 **730/730=100%**，`previous_date=2026-08-07`，`errors=[]`。

> **数据纪律**：能确认的写具体数值；不能确认的明确写 N/A。当前没有可靠同刻的 VIX、MOVE、HY OAS、EUR/USD、USD/CNH、上证50/沪深300/中证1000现货指数收盘与 ETF 资金流统一快照，因此不填假数。中国“基差”部分以 **期指—同月期权隐含 forward 差**补充观察，明确不冒充现金指数基差。

## 一、今日一句话结论

**有机会，但应买凸性而非追裸 Delta：软就业压低近端加息概率，而油价、长端收益率与美元在 CPI 前同步走高；中国 IM 最强却伴随 OI 收缩，说明 Risk-on 与通胀/事件风险并存。**

**状态判定：Mixed Risk-on + Event-risk repricing。** 最大跨资产背离是：美国股市仍贴近纪录高位、上周 Nasdaq +5.2%，但 Brent/WTI 今日约 +2%、2Y/10Y 收益率回升、美元反弹，黄金仍维持 4,300 美元以上高位。风险资产并未给出“低波动、低通胀”的干净确认。

## 二、隔夜 / 国内市场仪表盘

| 资产 | 最新确认值 | 单日变化 | 一周变化 | 当前信号 | 数据时间/属性 |
|---|---:|---:|---:|---|---|
| US 2Y | **4.222%** | 约 +3bp | 8/3→8/7 官方 -6bp | CPI 前前端重新抬升，但仍低于弱就业前定价 | 8/10 美盘盘中，WSJ |
| US 5Y | **4.35%** | N/A | 8/3→8/7 -5bp | 仅用最近完整官方日，不伪装实时 | 8/7 Treasury official close |
| US 10Y | **4.662%** | 约 +1bp vs 8/7 4.65% | 8/3→8/7 -5bp | 长端黏性高，财政/油价/CPI压制 duration | 8/10 盘中；8/7官方 |
| US 30Y | **5.19%** | N/A | 8/3→8/7 -4bp | 当前盘中未取得可靠独立报价 | 8/7 Treasury official |
| 2s10s | **+46bp** | N/A | 8/3 约 +45bp | 曲线已陡，仍偏向前端比长端更易 rally | 8/7 official derived |
| 2s30s | **+100bp** | N/A | 8/3 +98bp | 牛陡逻辑仍在，但已非便宜起点 | 8/7 official derived |
| 5s30s | **+84bp** | N/A | 8/3 +83bp | 长端期限/财政溢价仍难消 | 8/7 official derived |
| 10Y real | **2.40%** | N/A | 8/3 2.43%→8/7 2.40% | 高实际利率仍是黄金上方约束 | 8/7 Treasury/FRED口径 |
| 10Y BEI | **约2.25%** | N/A | 约持平 | 名义4.65%-实际2.40%的推导，不是直接报价 | 8/7估算 |
| DXY | **约99.70** | 大致持平至小涨 | N/A | 从两个月低位附近反弹 | 8/10 Reuters早盘快照 |
| USD/JPY | **约158.89** | 美元约 +0.6% | N/A | 日元重新走弱，BOJ/干预尾部仍大 | 8/10 Reuters |
| EUR/USD | **N/A** | N/A | N/A | 本次未独立核验，不猜 | — |
| USD/CNH | **N/A** | N/A | N/A | 只确认 PBOC 今日强调人民币基本稳定 | — |
| Nasdaq Composite | **盘中约 -0.2%** | -0.2% | **上周 +5.2%** | 纪录高附近 FOMO 后进入事件等待 | 8/10 美盘早段 |
| SOXX/SMH | **N/A 精确同刻值** | N/A | N/A | AI/半导体继续受本周财报催化，但不填假报价 | — |
| Brent | **约 $85.23/bbl** | **约 +2%** | N/A | Hormuz 右尾重新升温，事件溢价高 | 8/10 美盘早段 |
| WTI | **约 $79.80/bbl** | **约 +2%** | 上周五结算约 $78.18 | 地缘驱动多于需求驱动 | 8/10 美盘早段 |
| Spot Gold | **$4,335.27/oz** | **-0.2%** | N/A | 美元/收益率走高下仍坚挺，信用/地缘属性未消 | 8/10 Reuters |
| COMEX Gold futures | **约 $4,394** | -0.1% | N/A | 不追裸 Delta，偏 3–6M Call Spread | 8/10 Reuters |
| VIX | **N/A可靠同刻值** | — | — | Reuters 指出近期“股涨 + 波动率涨”异常组合，拥挤风险升高 | 8/10 |
| MOVE | **N/A可靠同刻值** | — | — | ICE 定义有效，但本次未取得可核验实时值 | — |
| US HY OAS | **N/A当前值** | — | — | FRED/ICE 当前索引数据滞后，不能当成 8/10 实时 | — |
| IH2609 | **2936.0** | **+0.390%** | 5D **+2.66%** | 上涨但 OI -4.63%，偏 short-covering | 8/10 CFFEX EOD |
| IF2609 | **4644.6** | **+0.186%** | 5D **+2.93%** | 四大期指最弱，OI -5.02% | 8/10 CFFEX EOD |
| IC2609 | **7881.4** | **+0.334%** | 5D **+7.14%** | 反弹延续，但 OI -2.74% | 8/10 CFFEX EOD |
| IM2609 | **7607.2** | **+0.563%** | 5D **+8.31%** | 最强 Beta，但 OI -1.87%，不是干净新多 | 8/10 CFFEX EOD |
| HO2609 ATM IV | **16.02%** | **-0.10 vol** | 5D **-2.96 vol** | 大盘波动率持续压缩 | 8/10 Engine |
| IO2609 ATM IV | **18.28%** | **-0.49 vol** | 5D **-3.50 vol** | 300 波动率继续压缩 | 8/10 Engine |
| MO2609 ATM IV | **27.65%** | **+0.11 vol** | 5D **-5.45 vol** | 小盘 IV 已大幅回落，但今日停止压缩 | 8/10 Engine |

### 中国期指—期权隐含 forward 差（不是现金基差）

- **IH2609 2936.0 vs HO2609 implied forward 2937.24：-1.24点 / -0.042%**
- **IF2609 4644.6 vs IO2609 implied forward 4647.96：-3.36点 / -0.072%**
- **IM2609 7607.2 vs MO2609 implied forward 7614.92：-7.72点 / -0.101%**

三者量级都很小，当前没有足以单独构成 futures-option forward arbitrage 的异常。

## 三、相比上一完整交易日真正发生了什么变化

1. **美国“弱就业→鸽化”没有变成单向 duration rally。** 8/7 官方 2Y/10Y/30Y 为 4.19%/4.65%/5.19%；8/10 盘中 2Y、10Y 已回到约 4.222%/4.662%。市场仍只给 9 月加息约 46% 概率，但油价与 CPI 风险让长端不愿大幅下行。**交易含义：曲线优于 outright long duration。**
2. **油价重新上调地缘右尾。** Brent 约 $85.23、WTI 约 $79.80，日内均约 +2%。Hormuz 全面开放仍附带政治条件。**交易含义：若参与，只买有限损失的 call spread/call fly，不追裸期货。**
3. **黄金在美元和收益率反弹下仅小跌。** Spot Gold 约 $4,335，日内 -0.2%。这是比“金价上涨”更重要的信号：传统实际利率/美元逆风出现时，金价仍维持高位，说明财政、地缘与政策信用需求没有消失。**交易含义：中期多头 thesis 不变，但短线等待 CPI 后确认。**
4. **中国风格继续向小盘倾斜，但资金性质不够好。** 8/10 主力涨幅 IM +0.563% > IH +0.390% > IC +0.334% > IF +0.186%，然而四个主力 OI 全下降。尤其 IF OI -7,585 手，IH -3,272，IM -4,505。**推断：今日上涨更像 short-covering/风险减仓后的价格抬升，而非一致的新多入场。**
5. **中国小盘 downside protection 仍贵。** MO2609 ATM IV 27.65%，25Δ RR = **-1.595 vol**，25Δ Put IV 29.17% > Call IV 27.57%；Gamma 峰集中在 8000/7600/7800。尽管 IM 上涨，put skew 仍显著为负，说明尾部保险需求没有被 Risk-on 消灭。
6. **AI/科技的边际风险是“拥挤 + 财报”，不是立即基本面崩塌。** 上周 Nasdaq +5.2%，Reuters 报道此前 S&P 四个交易日约 +5.8%，并出现 call 追逐与波动率随股价上升的异常组合；同时 Applied Materials 将于北京时间 8/14 04:30 举行 FY26 Q3 电话会。**交易含义：保护性 put spread 的赔率优于裸空科技。**

## 四、机会排行榜（全球统一竞争）

评分 = 逻辑强度25 + 赔率/凸性25 + 催化剂20 + 价格/波动率条件15 + 拥挤/技术确认15。

| 排名 | 机会 | 总分 | 分项 | 方向/期限 | 阶段 | 最佳工具 | 最大损失 |
|---|---|---:|---|---|---|---|---|
| 1 | **US 2s30s Bull Steepener** | **88** | 23/22/18/13/12 | 5–20D | 试仓/等 CPI 加仓 | 3M2Y receiver + 3M30Y payer swaption，DV01 matched | 有限（若用 swaptions） |
| 2 | **Gold 3–6M Call Spread** | **84** | 22/23/17/11/11 | 10–60D | 观察→确认 | 买30–35Δ Call / 卖10–15Δ Call | 有限净权利金 |
| 3 | **Brent 1–2M Upside Call Spread / Call Fly** | **82** | 22/23/18/9/10 | 1–15D | 条件单 | 有限风险油价上行凸性 | 有限净权利金 |
| 4 | **QQQ 30–60D Put Spread / Put Diagonal** | **80** | 20/22/16/11/11 | 5–30D | 小仓保护 | 30–35Δ put / 10–15Δ put | 有限净权利金 |
| 5 | **IM-IF 相对价值 + MO 限险对冲** | **72** | 19/18/13/11/11 | 2–15D | **观察，不达交易阈值** | Dollar/Beta-neutral long IM2609 / short IF2609 + MO put spread | 可限制 |

**今日中国股指无合格交易。** 最接近触发的是 IM 相对 IF 的风格延续，但必须看到下一交易日 **IM 价格继续相对走强且 OI 不再收缩/转为增加**，同时 MO2609 RR25 不再明显变得更负，才升级为试仓。

## 五、前三名交易卡

### 交易卡 1｜US 2s30s Bull Steepener｜88

**核心逻辑**：软就业首先作用于近端政策路径；而长端同时承受财政供给、能源/通胀尾部和期限溢价。8/7 2s30s 已约 +100bp，不是极端便宜起点，因此只做小仓和事件后确认。

**结构**：优先 **3M2Y receiver swaption + 3M30Y payer swaption，curve-DV01 matched**；若 OTC vol 太贵，退化为 receive 2Y / pay 30Y IRS。不给未核验的 swaption premium。

**入场触发**：CPI 前仅 1/3 试仓；若 CPI 核心不高于预期且 2Y 下行≥5bp、30Y下行不超过2Y的一半，加至2/3；PPI/零售后曲线继续走陡再完成仓位。

**失效**：CPI 显著偏热并使 2s30s 压回 **85bp 以下**；或出现明确衰退式 bull-flattening，30Y rally 明显强于2Y。

**止盈**：TP1 相对入场 +15bp；TP2 +30bp。到 TP1 后把剩余仓位最大可损降至初始风险一半。

**Greeks/风险**：前端 receiver 正 duration convexity，长端 payer 提供财政/通胀对冲；净 Vega 取决于两腿名义和期限，要求 DV01 而非名义金额匹配。初始最大损失 **NAV 0.50%**；确认后本交易不超过 **1.25% NAV**。

### 交易卡 2｜Gold 3–6M Call Spread｜84

**核心逻辑**：8/10 Spot Gold $4,335.27，美元走强、收益率回升时仅跌0.2%。市场可能仍把黄金过多当作“降息 beta”，而低估财政/货币政策信用、地缘与央行需求提供的独立溢价。

**结构**：期限3–6个月；买 **30–35Δ Call**，卖 **10–15Δ Call**。若 CPI 后 IV 突增，不追价；当前未取得完整 COMEX 期权链，因此**不虚构具体权利金和精确 strike**。

**入场触发**：A）金价回撤1%–2%，DXY不持续突破100–101；或 B）CPI后 Gold 创新高，同时10Y real不明显上破此前高位。

**失效**：DXY >101并持续；10Y real显著抬升；Gold跌破 **$4,200** 且地缘风险同步降温。

**止盈**：TP1 标的较入场 +5% 或 spread 约1.8x；TP2 标的 +10% 或 spread 接近最大价值的75%–80%。

**Greeks**：+Delta / +Gamma / +Vega / -Theta；卖高执行价降低 Vega 和 Theta 消耗。最大损失=净权利金；初始风险 **0.50% NAV**，确认后≤**0.75% NAV**。

### 交易卡 3｜Brent 1–2M Upside Call Spread / Call Fly｜82

**核心逻辑**：Brent约$85.23、WTI约$79.80，今日均约+2%；Hormuz全面恢复仍受政治条件约束。现货已经付了部分地缘溢价，但航道再次受阻的跳空尾部仍可能被低估。

**结构**：1–2个月 Brent Call Spread，买 **30–40Δ Call** / 卖 **10–15Δ Call**；若前端 skew/IV 极贵，改 Call Fly。不虚构 ICE 期权具体 premium。

**入场触发**：Brent 回到 $83–84 区间但 Hormuz 协议仍无实质进展；或突破$86且出现可核验航运/供应恶化新闻再确认。

**失效**：Hormuz出现可核验的持续开放、船运量显著恢复；Brent跌破$80且EIA库存/需求数据同步偏空。

**止盈**：TP1 Brent $90附近或spread约1.7x；TP2 $95或spread达最大价值70%–80%。

**Greeks**：+Delta/+Gamma/+Vega/-Theta；最大损失=净权利金；初始 **0.40%–0.60% NAV**，确认后≤**1.0% NAV**。不得用裸空期权或高杠杆裸期货替代。

### 组合层风险合并

Gold、Brent、long-end payer/steepener 的表面资产不同，但都部分暴露于 **能源通胀 + 美国政策信用 + 地缘风险**。三者初始合并风险建议 **≤1.5% NAV**，确认后主题总风险 **≤2.5%–3.0% NAV**，不能把每腿限损额度机械相加。

## 六、黄金专项跟踪

**判定：不变偏增强。**

1. 弱就业使9月加息概率降至约46%，对黄金有利。
2. 8/7 10Y real约2.40%，并不低；黄金仍在4,300美元以上，说明高real yield并未把金价压回旧regime。
3. DXY从低位反弹，Gold只小幅回落，负相关弹性下降。
4. 本周Treasury供给、Fed政策独立性讨论与地缘不确定性仍给黄金非传统风险溢价。
5. ETF/CFTC/期权IV-skew：本次没有拿到足够新鲜且同口径的8/10数据，明确N/A，不以旧数据冒充实时。

**优选表达**：①3–6M 30–35Δ/10–15Δ Call Spread；②突破确认后才考虑微型黄金期货小仓；③若“Gold强+长端收益率升”同时加强，可用Gold Call Spread + long-end Treasury Put/Payer组成政策信用组合，但两腿必须合并风险预算。

## 七、AI股票专项跟踪

**当前判断：不是趋势性基本面反转，而是“强盈利/强订单 + 高拥挤 + 事件风险”并存。**

- Nasdaq上周+5.2%，8/10开盘后约-0.2%，Risk-on仍强但边际速度放缓。
- Cisco Q3 FY26官方披露：季度收入 **$15.8bn、+12%**；hyperscaler AI infrastructure orders YTD **$5.3bn**，公司将FY26 AI orders预期上调至 **$9bn**，支持“有现金流、有订单的AI网络/基础设施龙头”。
- Applied Materials将于 **8/14 04:30 北京时间**举行FY26 Q3 earnings call，是半导体设备链明确短期催化。
- Reuters报道近期出现短期限Call追逐、广度偏强且波动率随股价上涨，说明风险更多来自 **positioning/convexity**，不是立即证明AI需求崩塌。

**策略**：多现金流/订单已验证的AI基础设施龙头；空/对冲高度依赖远期Capex叙事、现金流兑现弱的二线高Beta；指数层若CPI前后继续FOMO，优先QQQ/SMH **Put Spread或Put Diagonal**，而非裸空。失效条件是AI earnings breadth继续扩张、实际利率回落、隐含波动率同时下降。

## 八、中国50 / 300 / 1000专项跟踪

### 8.1 数据健康

- `radar_latest.json`：**2026-08-10**，fresh；
- CFFEX official EOD：**ok**；futures：**16 records / ok**；
- option official match：**730/730，100%**；
- `previous_date=2026-08-07`；`errors=[]`。

这是本次链路测试最关键的修复验证：**8/10中国数据已在20:34后进入Engine**，不再是正式20:07晚报当时的8/7数据时钟。

### 8.2 期指：价格、OI、跨期

| 品种 | 主力 | Close | 1D | OI变化 | 3D* | 5D* | 20D* | 次月-主力 | 年化roll推导 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| IH | IH2609 | 2936.0 | +0.390% | -3,272 / -4.63% | +1.47% | +2.66% | +2.21% | -42.8 | -5.85% |
| IF | IF2609 | 4644.6 | +0.186% | -7,585 / -5.02% | +0.51% | +2.93% | +0.22% | -79.4 | -6.86% |
| IC | IC2609 | 7881.4 | +0.334% | -4,618 / -2.74% | +1.77% | +7.14% | -1.75% | -173.8 | -8.85% |
| IM | IM2609 | 7607.2 | +0.563% | -4,505 / -1.87% | +2.33% | +8.31% | -1.00% | -194.0 | -10.23% |

* 3D/5D/20D 使用同一2609主力合约相对8/5、8/3、7/13 close；1D使用CFFEX当日官方涨跌口径。混合口径已明确。

**结论**：今天最适合观察 **IM**，因为相对强度最高、5D反弹最强；但IM上涨+OI下降，不能叫“新资金确认”。IM远月贴水最深，结构性风险溢价仍高。因此“追IM裸多”不如等待OI确认，或用MO做有限风险表达。

### 8.3 HO / IO / MO多周期IV

统一比较2609合约：

| 期权 | ATM IV | 1D Δ | 3D Δ | 5D Δ | 20D Δ | RR25 | PCR(OI) |
|---|---:|---:|---:|---:|---:|---:|---:|
| HO2609 | **16.02%** | -0.10 vol | -0.95 | -2.96 | -6.71 | **+0.375 vol** | 0.653 |
| IO2609 | **18.28%** | -0.49 vol | -0.90 | -3.50 | -5.02 | **-0.638 vol** | 0.666 |
| MO2609 | **27.65%** | +0.11 vol | -1.14 | -5.45 | -3.50 | **-1.595 vol** | 0.707 |

HO/IO中期IV压缩仍明显；MO 5D IV crush最大，但今日ATM IV反而+0.11vol，说明小盘波动率压缩开始遇阻。MO 25Δ put IV 29.17%高于call 27.57%，downside skew明显。因此小盘下行保护优先put spread/put butterfly；做short vol也只能有限风险，不卖裸尾。

### 8.4 Gamma节点

- HO2609：2900 / 3000 / 2800；
- IO2609：4700 / 4600 / 4800；
- MO2609：**8000 / 7600 / 7800 / 7400 / 7200**。

MO的7600已成为主要gamma density节点之一，且IM2609 close=7607.2，下一交易日若围绕7600反复，短期pinning/加速切换值得观察；这里只能称 **absolute gamma concentration**，不能冒充dealer signed GEX。

### 8.5 五个强制问题

**今天更适合IH、IF还是IM？** IM最值得观察，但不适合追裸多；若必须做方向，等待IM相对IF继续走强且OI转增。

**大小盘是否风格切换？** 战术上是IM>IH>IC>IF，5D IM +8.31%。但20D IM仍-1.00%，且今日OI收缩，所以是 **战术小盘反弹/short covering延续**，尚不是结构性regime shift。

**基差/跨期是否异常？** 期指—期权forward差只有-0.04%~-0.10%，无明显套利；跨期贴水则IM最深，风险补偿明显，但不足以单独做多carry。

**期权是否优于裸期货？** 是。尤其IM/MO：下行skew贵，适合spread/fly；若做上行，Call Spread能限制事件后IV crush。裸期货承受隔夜gap和保证金放大，不占优。

**是否有IF-IH / IM-IF / IM-IH相对价值？** IM-IF最接近：5D强弱差显著。但今天OI没确认，故只观察。触发条件：下一交易日IM/IF ratio再创新高 + IM OI转正 + MO RR25不进一步恶化。

### 8.6 合约乘数与保证金/Gap风险

- IH、IF：**300元/指数点**；IM：**200元/指数点**；HO/IO/MO期权：**100元/指数点**。
- 中金所产品页显示IH最低交易保证金为合约价值8%；实际经纪商/交易所临时参数可能更高，本报告不把8%当作账户实际保证金。
- 名义价值 = 指数点 × 乘数 × 手数，而不是按保证金金额看风险。隔夜跳空2%对IM2609单手名义P&L约为 `7607.2×200×2%≈30,429元`。

## 九、未来24小时与7天事件日历（北京时间）

| 北京时间 | 事件 | 确认度 | 交易前处理 |
|---|---|---|---|
| **8/12 20:30** | 美国7月CPI | BLS官方确认 | CPI前减少裸Delta；保留有限损失convexity；曲线仓只1/3 |
| **8/12 22:30** | EIA Weekly Petroleum Status Report | EIA标准周三10:30 ET，非节假周 | 油价结构不加裸杠杆；事件前可保留call spread |
| **8/13 20:30** | 美国7月PPI | BLS官方确认 | 若CPI已热，进一步降duration/成长Delta |
| **8/14 04:30** | Applied Materials FY26 Q3 earnings call | 公司IR确认 | 半导体设备链降单名Delta，保留put spread/defined-risk event vol |
| **8/14 20:30** | 美国7月零售销售 | Census官方确认 | 观察“通胀热+消费强”是否重启hawkish repricing |
| **8/10–8/15窗口** | 中国7月信贷/M2/社融 | Reuters：PBOC预计该窗口发布，具体时点未预先确认 | A股风格仓不在数据前加满；若信用明显弱于预期，IM高Beta优先降风险 |
| **未来7天，具体时点待官网确认** | 中国7月工业/零售/投资等月度数据 | NBS例行月中；本次未取得2026年8月精确日程 | 不伪造时间；数据前控制IM/消费/周期暴露 |
| 持续 | Hormuz / 伊朗—美国谈判与航运恢复 | 高不确定性 | Brent只做限险结构；周末前降低裸Delta |
| 持续 | 美国财政部本周约 **$125bn** 新发行供给 | Reuters确认周供给规模；具体拍卖细节未完全独立核验 | 长端duration不追，曲线交易优先 |

补充：中国7月CPI **+0.5% YoY**、PPI **+3.5% YoY** 已于8/9发布，不再列作未来事件；市场重点转向信贷与月度活动数据。

## 十、今日行动清单

**A. 今天可以立即建立：** 2s30s Bull Steepener仅1/3试仓（优先限损swaption结构），组合风险约NAV 0.5%。  
**B. 今天只应挂条件单：** Gold 3–6M Call Spread、Brent 1–2M Call Spread/Call Fly；等待回撤或CPI/Hormuz确认。  
**C. 今天应继续观察：** QQQ Put Spread/Diagonal；中国IM-IF相对价值，必须等IM OI转增与MO skew稳定。  
**D. 今天必须避免或退出：** CPI/Hormuz前追裸Brent、追裸IM、裸卖MO downside、以及把Gold+short bonds+long oil当成三个独立风险因子分别满额下注。

---

## 风险预算总则

- 单一试仓最大损失：NAV **0.25%–0.75%**；
- 单一确认交易最大损失：NAV **0.75%–1.50%**；
- 高确信主题总风险预算：**≤2.5%–3.0% NAV**；
- Gold、Brent、long-end bearish/steepener同时出现时，合并视为“通胀/政策信用/地缘”因子；
- 中国IM、MO Call、small-cap ETF多头视作同一高Beta风格因子。

## 关键来源与审计痕迹

**中国衍生品**
1. `farfromexact/China-Options-Engine/data/radar_latest.json` — 2026-08-10 EOD，CFFEX official quote coverage 100%。
2. `farfromexact/China-Options-Engine/data/radar_history.json` — 22个已验证交易日，2026-07-10至2026-08-10。
3. CFFEX product specifications — IH/IF 300元/点，IM 200元/点，HO/IO/MO 100元/点。

**美国宏观/市场**
4. U.S. Treasury Daily Treasury Par Yield Curve Rates — 2026-08-07 official close。
5. Reuters, 2026-08-10, Global stocks / Hormuz / inflation focus — Brent约85美元，市场等待CPI。
6. WSJ, 2026-08-10 — 2Y约4.222%，10Y约4.662%，9月加息概率约46%。
7. Reuters, 2026-08-10, Gold eases on firm dollar — Spot Gold $4,335.27，COMEX约$4,394。
8. Reuters, 2026-08-10, Dollar steadies — DXY约99.70，USD/JPY约158.89。
9. BLS 2026 release calendar — CPI 8/12 08:30 ET，PPI 8/13 08:30 ET。
10. U.S. Census release calendar — July retail sales 8/14 08:30 ET。
11. EIA Weekly Petroleum Status Report schedule — 周三10:30 ET标准发布。
12. Applied Materials IR — FY26 Q3 call 8/13 16:30 EDT。
13. Cisco IR Q3 FY26 — revenue $15.8bn，AI infrastructure orders YTD $5.3bn，FY26 AI orders guide $9bn。
14. Reuters 2026-08-09/10 China macro — July CPI/PPI、PBOC信贷发布时间窗口及人民币稳定表述。

## 测试结论占位

本报告正文已经生成；最终 `overall_status` 由 GitHub 三份测试归档全部写入并回读验证后决定。若任一文件写入/回读失败，状态必须为 FAIL。
