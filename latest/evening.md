# 全球跨资产高风险机会雷达｜晚间版
## 2026-08-10｜Revision 1

**数据截点：北京时间 20:07。** 美国现金股市尚未开盘，因此美国权益使用 8 月 7 日正式收盘与 8 月 10 日盘前期货；利率、美元、黄金和原油使用截至欧洲/美国盘前可核验的最新报价。中国衍生品严格读取 `China-Options-Engine/data/radar_latest.json` 与 `data/radar_history.json`，但仓库在本次截点仍只更新到 **2026-08-07**；因此所有 HO/IO/MO 与 IH/IF/IC/IM 的 1/3/5/20 日、OI、skew、Gamma 结论均明确标记为 **8/7 EOD 历史状态**，不能冒充 8/10 收盘状态。

## 一句话结论

**2s30s 牛陡仍是第一机会；黄金 Call Spread 保留第二，QQQ Put Spread/Diagonal 因美股 FOMO 与“股涨+波动率涨”的异常组合升至第三；Brent 右尾由早盘追价机会降级为条件式凸性；中国小盘的 5 日反转仍成立于 8/7，但由于 Engine 尚无 8/10 EOD，今晚不能据此新增 IM 风险。**

## 跨资产仪表盘

| 资产 | 最新确认状态 | 交易含义 |
|---|---:|---|
| US 10Y | 约 4.65% | 收益率小幅回落，CPI 前保持高位 |
| 2s30s | 8/7 约 +100bp | 前端政策路径比长端更易下移 |
| DXY | 约 99.70 | 仍在近两个月低位附近，但今日企稳 |
| USD/JPY | 约 158.89 | 日元回落；干预/政策尾部仍大 |
| S&P 500 futures | +0.2% 左右 | 现金开盘前继续偏 Risk-on |
| Nasdaq futures | +0.4% 左右 | AI/成长继续领先，但拥挤升温 |
| Brent | 约 $83.50/bbl | 早盘一度更高，Hormuz 二元尾部仍在 |
| Spot Gold | 约 $4,332.68/oz | -0.2%，美元反弹压制追高 |
| China options/futures | **8/7 EOD** | 8/10 EOD 尚未进入 Engine，数据降级 |
| VIX / MOVE / HY OAS | N/A 精确同刻值 | 未取得可靠统一时点，不填假数 |

## 今晚最重要的五个变化

1. **Fed 路径的鸽化重定价仍在。** 7 月就业意外转弱后，市场对 9 月加息的定价已降到约 45%–48%，一周前约 67%。这继续支持“前端比长端更容易 rally”的曲线逻辑。
2. **美股的边际风险从“基本面坏”转成“拥挤与凸性失衡”。** Reuters 报道 S&P 500 四个交易日上涨约 5.8%，短期限 Call 需求、call/put 比率与 Bullish Percent 同时走高，而且波动率随指数上涨而上升。它不是立即做空信号，但显著提高了用 Put Spread 而不是裸空指数的性价比。
3. **Brent 的右尾仍在，但紧迫性下降。** 伊朗仍把霍尔木兹全面开放与美国让步绑定；同时伊朗与阿曼正在推进航道安排。Brent 从亚洲早盘约 $84.2 一带回到约 $83.5，说明市场更愿意给谈判权重，追涨 Delta 的赔率变差。
4. **黄金没有确认新的加速突破。** 现货金约 $4,332.68，日内 -0.2%，美元 +0.2%。弱就业和地缘风险仍提供中期 convexity，但今晚更适合等回撤或 CPI 后确认，不适合裸追。
5. **中国模块出现“信息时钟错位”。** 8/10 是正常交易日，但 Engine 在 20:07 仍是 8/7 verified EOD。由于本任务明确要求用 Engine 做 IV/OI/skew/Gamma 判断，今晚中国交易评分必须下调，不能拿 8/7 的持仓结构解释 8/10 的收盘。

## 全球统一机会排行榜

| 排名 | 机会 | 分数 | 持有期 | 阶段 | 最佳表达 |
|---|---|---:|---|---|---|
| 1 | **US 2s30s Bull Steepener** | **90** | 5–20D | 可小仓 | 3M2Y Receiver + 3M30Y Payer Swaption |
| 2 | **Gold 3–6M Call Spread** | **86** | 10–60D | 等回撤/确认 | 30–35Δ / 10–15Δ Call Spread |
| 3 | **QQQ 30–60D Put Spread / Diagonal** | **84** | 5–30D | 可作尾部保护 | 有限权利金下行凸性 |
| 4 | **Brent 1–2M Upside Call Spread / Call Fly** | **81** | 1–15D | 条件式 | 不做裸期货 |
| 5 | **Long IM2609 / Short IF2609 + MO Put Spread** | **74** | 2–15D | **等待新鲜 8/10 EOD** | RV + downside hedge |

## 交易卡 1｜US 2s30s Bull Steepener｜90

**逻辑：** 软就业首先作用于近端政策路径；而长端同时承受财政供给、能源/通胀尾部和期限溢价，因此“receive front end / pay long end”比 outright Long 30Y 更干净。

**表达：** 3M2Y receiver swaption + 3M30Y payer swaption，curve-DV01 matched；若 OTC vol 太贵，再退化为 Receive 2Y / Pay 30Y IRS。

**入场：** 维持 1/3 试仓；CPI 后若前端继续 rally、30Y 仍黏，才加仓。

**止损/失效：** 2s30s 回到约 85bp 以下并出现衰退式 bull-flattening，或 CPI 明显偏热导致前端 hawkish repricing。

**TP：** 相对入场继续走陡 +15bp / +30bp。

**风险预算：** 初始最大损失约 NAV 0.50%；确认后主题不超过 NAV 1.25%。

**拒绝替代表达：** outright Long 30Y，因为它直接承担财政/term-premium 风险。

## 交易卡 2｜Gold 3–6M Call Spread｜86

**逻辑：** 弱就业压低加息概率，黄金仍受益于政策路径与地缘不确定性；但今日美元反弹、金价小幅回落说明短线并未进入单边加速。

**表达：** 买 30–35Δ Call / 卖 10–15Δ Call，期限 3–6M。

**入场：** 优先等 1%–2% 回撤，或 CPI 后在 DXY 不上破 100–101、实际利率不明显上冲的情况下做突破确认。

**失效：** DXY >101、10Y real 显著重新上行且 Gold 跌破 $4,200 的组合。

**Greeks：** +Delta / +Gamma / +Vega / -Theta；卖高执行价降低裸 Call 的 premium burn。

**风险预算：** 净权利金最大损失 NAV 0.50%–0.75%。

## 交易卡 3｜QQQ 30–60D Put Spread / Diagonal｜84

**逻辑：** 当前不是“基本面做空科技”，而是“为拥挤 Risk-on 买便宜的非线性保险”。S&P 近四日约 +5.8%，短期限 Call 追逐与上涨中的波动率抬升说明市场越来越依赖正 Gamma/追涨流。

**表达：** 30–60D Put Spread；若前端事件 IV 很贵而后端较平，可用 Put Diagonal。

**入场：** 美股开盘后若 Nasdaq 继续走高、短期限 Call 追逐不退，而 CPI 前 downside skew 未明显爆贵，可建立小规模 hedge。

**失效：** CPI 温和、实际利率回落、市场广度继续扩张，同时上涨中的 implied vol 明显回落。

**TP：** 尾部保护以组合层为目标，不追求单腿最大化；遇 3%–5% QQQ 回撤优先兑现一部分。

**风险预算：** 净权利金 NAV 0.30%–0.50%。

## 中国 50 / 300 / 500 / 1000 专项

### 数据健康状态

- `radar_latest.json`: **date=2026-08-07, data_fresh=true, official coverage=100%**
- `radar_history.json`: **21 个 verified sessions，2026-07-10 至 2026-08-07**
- 本次 20:07 截点：**尚无 2026-08-10 verified EOD**
- 因此下面全部是 **8/7 状态的多周期分析**；不使用 snapshot 自行拼接，也不推测 8/10 的 OI、IV 或 Gamma。

### 股指期货：1 / 3 / 5 / 20 日（截至 8/7）

| 合约 | 1D | 3D | 5D | 20D | 8/7 OIΔ | 次月-主力 |
|---|---:|---:|---:|---:|---:|---:|
| IH2609 | +1.13% | +2.72% | +1.32% | +0.68% | +3,455 | -43.0 |
| IF2609 | +0.73% | +2.04% | +2.37% | -1.25% | +4,447 | -80.0 |
| IC2609 | +1.91% | +4.63% | +6.53% | -5.46% | -2,089 | -162.2 |
| IM2609 | +1.86% | +5.26% | +8.63% | -5.35% | -4,787 | -190.6 |

**截至 8/7 的结构结论：** IM/IC 的 3–5 日反转是真实的，但 20 日仍负；8/4 IM 上涨伴随 OI +7,127，偏新资金，随后 8/6 与 8/7 价格继续上涨而 OI 分别显著下降，后半段越来越像 short covering。IM 的远月贴水仍深，也没有给出结构性新牛市确认。

### HO / IO / MO：1 / 3 / 5 / 20 日 IV（截至 8/7）

| Symbol | ATM IV | 1D ΔIV | 3D | 5D | 20D | RR25 | PCR(OI) |
|---|---:|---:|---:|---:|---:|---:|---:|
| HO2609 | 约 16.12% | -0.87vol* | -2.13 | -2.90 | -4.90 | 约 -0.13vol | 0.698 |
| IO2609 | 约 18.77% | -0.68vol* | -1.39 | -2.33 | -3.19 | 约 -1.02vol | 0.680 |
| MO2609 | 约 27.54% | -1.69vol* | -2.61 | -6.10 | +0.27 | 约 -2.12vol | 0.704 |

* 历史 ΔIV 按 `radar_history.json` 的同 symbol 历史口径；当前 level 以 `radar_latest.json` 为准，避免把不同价格基础机械混用。

MO2609 的 5 日 IV crush 最显著，但 8/7 Put OI +2,041、Call OI -1,179，RR25 仍明显为负。这说明当时的状态是 **vol normalization + downside protection retained**，不是纯 Risk-on。

### Gamma 节点

MO2609 截至 8/7 的主 Gamma 节点仍在 **8000**；5 日前次级节点约 **7200 / 7000**，8/7 已上移至 **7600 / 7800**。这是价格反弹后 gamma density 上移，但由于没有 8/10 EOD，今晚不能声称节点今天又发生了迁移。

### 期指—期权 Forward

8/7 同月份 futures-option forward 差异很小，量级不足以构成独立套利 thesis。当前真正有信息量的是 **price × OI × term structure × skew**，而不是 forward gap 本身。

### 四个强制问题

**1. 一日异常还是趋势延续？**  
截至 8/7，IM/IC 是 3–5 日战术趋势延续，不是 20 日结构性 regime shift。对 8/10 当日，因 EOD 数据缺失，今晚不作确认。

**2. 新资金、short covering、vol repricing 还是事件对冲？**  
8/4 偏新资金；8/6–8/7 明显混入 short covering。期权端则是 vol repricing 向下，同时 downside hedge 仍被保留。

**3. IV 上涨代表风险偏好还是保护需求？**  
8/7 实际是 IV 下行。若下一份新鲜快照出现 IV 上升，必须结合 skew/OI 判断：若 RR25 更负、Put OI 上升，优先解释为保护需求；若 IM OI 增加、Call wing 走强且 RR25 不恶化，才更像风险偏好/追涨。

**4. 当前最优表达？**  
今晚 **不建议基于旧数据裸多 IM**。下一份 fresh EOD 若同时看到 IM/IF 相对强度延续、IM OI 转正、远月贴水收敛、MO RR25 不继续恶化，最优仍是 **Long IM2609 / Short IF2609 + MO Put Spread**；否则不做。

## AI / 科技专项

当前基本面并没有给出“AI earnings collapse”证据；相反，美股盈利和 AI 主题仍支持指数。但流量层开始出现 FOMO：短 Call 需求、call/put 与上涨中的波动率同时偏高。最佳思路不是裸空 AI，而是：

**核心多头保留 + 小额 QQQ Put Spread/Diagonal；相对价值上继续偏 Long cash-flow leaders / Short high-Capex long-duration beta。**

## 未来事件树

- **8 月 12 日 20:30 北京时间：美国 7 月 CPI。** BLS 官方日程确认；Reuters 共识约 headline 3.4% YoY、core 2.5% YoY。
- **8 月 13 日 20:30：美国 7 月 PPI。**
- **8 月 14 日 20:30：美国 7 月 Advance Retail Sales。**
- **霍尔木兹：** 无固定发布时间。真正使 Brent upside thesis 失效的不是一句“谈判进展”，而是可执行开放、船东恢复与保险正常化同时得到验证。
- **China-Options-Engine：** 下一份 `data_fresh=true` 的 8/10 EOD 是今晚中国仓位判断的关键缺口。

## 风险预算

这些机会不是独立因子：Gold、Brent、2s30s 都含有不同程度的能源/通胀/地缘共同因子；QQQ hedge 则与 2s30s 的“政策友好”逻辑部分反向。

**新增总最大可损失建议控制在 NAV 1.5%–2.0%。**  
2s30s 初始 0.50%；Gold 0.50%–0.75%；QQQ hedge 0.30%–0.50%；Brent 只有触发时才分配 0.35%–0.50%；中国 RV 在 fresh EOD 确认前为 0。

## 四行行动清单

**A｜可以做：** 保持小规模 2s30s bull steepener；有黄金回撤时分批做 Call Spread。  
**B｜可以买保险：** QQQ 30–60D Put Spread/Diagonal 小规模建立，核心目的是对冲 FOMO/CPI 尾部。  
**C｜只挂条件：** Brent 只有在未出现可执行 reopen 且重新站稳 $84–85 时做 Call Spread/Fly；中国 RV 等 fresh 8/10 Engine 数据。  
**D｜避免：** 裸追 Brent、裸追 Nasdaq、用 8/7 OI/skew 去解释 8/10 中国收盘、以及在 CPI 前把全部风险预算押在同一个“低利率”因子上。

## 数据与来源

- Reuters, “Global stocks tick up with oil steady on Hormuz plans”, 2026-08-10: https://www.reuters.com/world/china/global-markets-global-markets-2026-08-10/
- Reuters, “FOMO fuels Wall Street's breakout rally as traders pile in”, 2026-08-10: https://www.reuters.com/business/fomo-fuels-wall-streets-breakout-rally-traders-pile-2026-08-10/
- Reuters, “Gold inches down from seven-week high, US inflation data in focus”, 2026-08-10: https://www.reuters.com/world/india/gold-drifts-lower-seven-week-peak-us-inflation-data-looms-2026-08-10/
- Reuters, “Dollar steadies after payrolls drop, yen falls”, 2026-08-10: https://www.reuters.com/world/asia-pacific/dollar-near-two-month-trough-us-inflation-data-awaited-2026-08-10/
- Reuters, “China July factory-gate inflation eases to 3-month low, CPI slows”, 2026-08-09: https://www.reuters.com/world/china/chinas-producer-inflation-eases-july-below-expectations-2026-08-09/
- U.S. BLS August 2026 release calendar: https://www.bls.gov/schedule/2026/08_sched_list.htm
- U.S. Census Retail Release Schedule: https://www.census.gov/retail/release_schedule.html
- CFFEX daily data page: https://www.cffex.com.cn/cn/rtj.html
- China-Options-Engine: https://github.com/farfromexact/China-Options-Engine
