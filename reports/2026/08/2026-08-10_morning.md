# 全球跨资产高风险机会雷达｜晨间版

## 2026-08-10｜周一开盘前｜Revision 1

**数据截点：北京时间 08:03。** 美国现金市场与国债采用 8 月 7 日正式收盘；能源采用 8 月 10 日亚洲早盘可确认报价；中国股指期货/期权采用 China-Options-Engine 最新验证 EOD（8 月 7 日）。中国历史比较固定使用 `data/radar_history.json`，按相同 symbol 做 1/3/5/20 个交易日比较，不从 snapshots 拼接历史。

## 一、今日一句话结论

**今天最值得承担的风险仍是“前端宽松重定价 + 长端能源/财政黏性”的 2s30s 牛陡；霍尔木兹未真正重开且油价亚洲早盘重新跳涨，使 Brent 上行 Call Spread 升至第二；中国 IM/IC 的 5 日反弹是真趋势、但后半段越来越像 short covering，叠加 7 月 CPI/PPI 降温，周一不应裸追小盘，优先等待 OI 与期限结构确认后做 Long IM / Short IF，并用 MO Put Spread 限制尾部。**

## 二、跨资产仪表盘

| 资产 | 最近确认值 | 当前信号 | 数据时点 |
|---|---:|---|---|
| US 2Y / 5Y / 10Y / 30Y | 4.19 / 4.35 / 4.65 / 5.19% | 前端 rally 强于长端 | 8/7 |
| 2s10s / 2s30s / 5s30s | +46 / +100 / +84bp | Bull steepening | 8/7 |
| 10Y real / BEI | 2.40% / ≈2.25% | real yield 回落，通胀尾部未消失 | 8/7 |
| DXY | 99.50 | 美元偏弱 | 8/7 |
| S&P / Nasdaq | 7,757.64 / 26,690.62 | 弱就业未触发衰退式 Risk-off | 8/7 |
| Brent / WTI | ≈84.8 / 79.3 美元 | 霍尔木兹不确定性重新加价 | 8/10 亚洲早盘 |
| Gold spot | ≈4,336 美元/盎司 | real yield + 地缘双重凸性 | 8/7 |
| 中国 CPI / PPI | +0.5% / +3.5% YoY | 价格压力降温、内需偏弱 | 7 月数据，8/9发布 |
| VIX / MOVE / HY OAS | N/A 精确值 | 本轮未可靠重取，不硬填 | — |

7 月美国就业报告令市场重新下调近端加息概率，但美股上周仍强劲，说明市场暂时仍处于“坏增长数据 → 更友好的政策路径”而非“盈利衰退确认”框架。另一方面，伊朗把霍尔木兹全面重开与美国让步挂钩，周日美股期货基本横盘偏弱，而油价周一亚洲早盘重新上涨，能源通胀尾部没有被解除。

## 三、今晨真正发生变化的五件事

1. **Brent 的右尾从“周末风险”变成了已成交的早盘价格确认。** 周一亚洲早盘 Brent/WTI 均较周五结算走高，证明市场没有把伊朗—阿曼航道安排等同于无条件恢复正常航运。
2. **中国 7 月 CPI/PPI 同时降温。** CPI 同比仅 +0.5%，PPI +3.5% 且低于预期；对 A 股的第一层含义不是“全面利空”，而是内需偏弱、政策支持需求上升，利多低实际利率/政策敏感资产，但会压制纯周期利润预期。
3. **2s30s thesis 没有被周末新闻破坏，反而获得能源尾部加固。** 若油价上行使 long-end inflation/term premium 黏住，而弱就业继续压前端，曲线牛陡仍比 outright Long 30Y 更干净。
4. **中国小盘的 5 日趋势很强，但资金性质并不纯。** 8/4 IM 上涨并增仓，是真新多；8/6–8/7 继续上涨却连续减仓，后半段明显掺入 short covering。
5. **MO 是“vol crush + protection re-bid”。** 5 日 ATM IV 大跌约 5.98 vol，但周五 RR25 单日进一步向 Put 侧恶化约 1.01 vol，同时 Call OI -1,179、Put OI +2,041；这不是简单的风险偏好全面扩张。

## 四、全球统一机会排行榜

| 排名 | 机会 | 分数 | 持有期 | 阶段 | 最佳表达 |
|---|---|---:|---|---|---|
| 1 | **US 2s30s Bull Steepener** | **91** | 5–20D | 可试仓 | 3M2Y Receiver + 3M30Y Payer Swaption |
| 2 | **Brent 1–2M Upside Call Spread / Call Fly** | **89** | 1–15D | 等开盘回踩/确认 | Brent options |
| 3 | **Gold 3–6M Call Spread** | **86** | 10–60D | 条件试仓 | 30–35Δ / 10–15Δ Call Spread |
| 4 | **Long IM2609 / Short IF2609 + MO Put Spread** | **82** | 2–15D | 中国开盘确认 | Beta/Dollar-neutral pair + hedge |
| 5 | **QQQ 30–60D Put Spread / Diagonal** | **76** | 5–30D | 观察 | Tail hedge |

## 五、前三名交易卡

### 1. US 2s30s Bull Steepener｜91
- **逻辑：** 弱就业首先压低近端政策利率预期；30Y 仍背负财政供给、能源、通胀与 term premium。
- **表达：** 优先 3M2Y receiver swaption + 3M30Y payer swaption，按 curve DV01 配平；若 option vol 太贵，再退化为 Receive 2Y / Pay 30Y IRS。
- **入场：** 2Y ≤4.20%、30Y ≥5.15%、2s30s 不跌破 90bp，先做 1/3。
- **加仓：** 8/12 CPI 后若前端继续 rally、30Y 黏住再加。
- **TP：** 入场后再陡 +15bp / +30bp。
- **失效：** 2s30s <85bp，或出现真正衰退式 long-end rally，或 CPI 令前端明显 hawkish repricing。
- **风险预算：** optionized 试仓最大损失 NAV 0.50%，确认后主题上限 1.25%。

### 2. Brent 1–2M Upside Call Spread / Call Fly｜89
- **逻辑：** 霍尔木兹重开仍有明确政治条件，亚洲早盘油价已重新加价右尾。
- **表达：** 25–35Δ Call / 10–15Δ Call Spread；若右尾 IV 已极贵，改 Call Fly。
- **入场：** 不追第一根 gap。若回踩仍守住周五结算上方，且未出现“无条件 reopen + 船东/保险恢复”，先 1/3。
- **加仓：** 新袭船、保险费率继续上升、船东拒航或谈判破裂。
- **失效：** 可执行的全面 reopen，且主要商业航运与保险真正恢复。
- **风险预算：** 净权利金最大损失，NAV 0.35%–0.60%。

### 3. Gold 3–6M Call Spread｜86
- **逻辑：** real yield 与美元回落提供传统 beta，霍尔木兹/财政风险提供额外 convexity。
- **表达：** Long 30–35Δ Call / Short 10–15Δ Call；无可靠 live chain 时不虚构 strike、IV、premium。
- **入场：** 相对 8/7 现货约 4,336 回撤 1.5%–2.5%，同时 DXY ≤100、10Y real 不明显反弹；或突破时美元/real yield 不反向确认。
- **失效：** DXY >101、10Y real >2.55%、黄金跌回突破起点三者共振。
- **风险预算：** 净权利金最大损失，NAV 0.50%–0.75%。

## 六、中国 50 / 300 / 500 / 1000 专项

### 6.1 期指：1 / 3 / 5 / 20 个交易日

| 主力合约 | 最新收盘 | 1D | 3D | 5D | 20D | 周五 OIΔ | Dec-Sep |
|---|---:|---:|---:|---:|---:|---:|---:|
| IH2609 | 2930.0 | +1.13% | +2.72% | +1.32% | +0.68% | +3,455 | 约 -43 |
| IF2609 | 4645.6 | +0.73% | +2.04% | +2.37% | -1.25% | +4,447 | 约 -80 |
| IC2609 | 7877.8 | +1.91% | +4.63% | +6.53% | -5.46% | -2,089 | 约 -162 |
| IM2609 | 7590.6 | +1.86% | +5.26% | +8.63% | -5.35% | -4,787 | **-190.6** |

**解释：** 3–5 日小盘相对强度非常明确，但 20 日仍未转正。尤其 IM：8/4 涨 2.65% 且 OI +7,127，属于新资金；8/6 OI -6,044、8/7 OI -4,787 时价格继续涨，说明后半段越来越依赖 short covering。与此同时 IM Dec-Sep 从 8/4 的 -162.6 扩到 8/7 的 -190.6，远月没有确认“新小盘牛市”。

### 6.2 期权：同 symbol 的多周期历史

| 合约 | ATM IV | ΔIV 1D | 3D | 5D | 20D | RR25 | PCR(OI) | 周五 Call/Put OIΔ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| HO2609 | 16.12% | -0.56vol | -1.83 | -2.59 | -4.59 | -0.13vol | 0.698 | -258 / -326 |
| IO2609 | 18.77% | -0.46vol | -1.17 | -2.11 | -2.97 | -1.02vol | 0.680 | -522 / +215 |
| MO2609 | **27.54%** | **-1.58vol** | -2.50 | **-5.98** | **+0.38** | **-2.12vol** | **0.704** | **-1,179 / +2,041** |

MO2609 的 25Δ RR 周五从约 -1.11vol 恶化到 -2.12vol，尽管 ATM IV 单日下跌约 1.58vol；5 日看 RR 反而比 7/31 的极端 -3.36vol 更温和。因此准确表述是：**5 日总体是 vol normalization，但周五出现新一轮 downside protection re-bid。**

Gamma 结构也在向上移动：MO2609 5 日前主节点是 8000，次级集中在 7200/7000；8/7 主节点仍为 8000，但次级节点已经上移至 **7600/7800**。这与标的上涨一致，意味着上方 7600–8000 区域的 dealer gamma 密度明显增加。

### 6.3 期指—期权联动
8/7 同月份 futures-option forward gap 很小：IH/HO 约 **-0.18 点**、IF/IO **-2.87 点**、IM/MO **+0.73 点**。所以当前不是明显 forward arbitrage，而是 **价格 × OI × term structure × skew** 的联合判断。

### 6.4 四个必须回答的问题
1. **一日异常还是趋势延续？** 不是一日异常。IM/IC 的 3–5 日相对强势成立；但 20 日仍为负，尚不足以称为中期 regime shift。
2. **新资金、short covering、vol repricing 还是事件对冲？** 8/4 有明确新多；8/6–8/7 更偏 short covering。期权侧同时存在显著 vol repricing lower 与 Put 保护需求。
3. **IV 变化代表什么？** 这里不是 IV 上涨，而是明显 IV 下跌；它代表 realized/expected vol normalization。可是在 MO 上 Put skew 与 Put OI 周五重新增强，所以不能把 IV crush 直接翻译成“风险偏好全面增强”。
4. **最优表达？** **不裸追 IM。** 优先等待开盘后 30–45 分钟确认：IM/IF 相对强度继续、IM OI 转正、Dec-Sep 向 -180 以内收敛、MO RR25 不继续恶化至 -3vol 以下。若四项中至少三项确认，再做 **Long IM2609 / Short IF2609 + MO2609 Put Spread**；否则只观察。

## 七、今日事件树

- **8/10 中国开盘：** 首次交易 7 月 CPI/PPI 降温与周一能源上涨的组合。重点看 IM/IF、券商/地产/消费与资源股是否出现分化，而不是先验下注指数方向。
- **8/12 20:30 北京时间：美国 7 月 CPI。** 当前最重要的 Fed-path 验证点。
- **8/13 20:30：美国 7 月 PPI。**
- **8/14 20:30：美国 7 月 Advance Retail Sales。**
- **持续事件：霍尔木兹。** 真正可执行的 reopen、商业保险恢复、主要船东恢复通行，才算油价右尾 thesis 的事实失效。

## 八、风险预算与组合相关性

当前三大机会并非独立：Brent 上行与 Gold 上行都含地缘风险，Brent 上行又可能通过 inflation premium 支撑 2s30s。建议新风险总预算控制在 **NAV 1.5%–2.0% 最大可损失**；同一“霍尔木兹升级”因子的直接期权权利金风险不超过 1.0%。中国 pair 若触发，单独预算 0.40%–0.60%，不要同时叠加大额裸 IM Delta。

## 九、四行行动清单

**A 立即建立：** 小规模 2s30s bull steepener；若 Brent 第一轮 gap 后回踩守住，才建立 1/3 upside call spread。  
**B 条件单：** Gold 3–6M Call Spread；Long IM / Short IF + MO Put Spread 等中国开盘 OI/term/skew 确认。  
**C 观察：** QQQ tail hedge、美元是否重回 100 上方、中国弱通胀是否被市场解释为政策利好而非盈利利空。  
**D 避免：** 裸追 Brent、裸追 IM、裸买高 IV Call；霍尔木兹若出现可执行无条件 reopen，则立即撤销油价上行 thesis。

## 十、主要来源

- [U.S. Treasury — Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve)
- [Reuters — China July factory-gate inflation eases to 3-month low, CPI slows](https://www.reuters.com/world/china/chinas-producer-inflation-eases-july-below-expectations-2026-08-09/)
- [Reuters — Iran ties Hormuz reopening to US concessions on several demands](https://www.reuters.com/world/middle-east/iran-ties-hormuz-reopening-us-concessions-several-demands-2026-08-09/)
- [MarketWatch — U.S. stock futures / Iran uncertainty](https://www.marketwatch.com/story/u-s-stock-futures-flat-as-investors-await-inflation-data-grapple-with-more-iran-uncertainty-133212d2)
- [U.S. BLS — August 2026 release calendar](https://www.bls.gov/schedule/2026/08_sched_list.htm)
- [U.S. Census Bureau — Monthly Retail Trade release schedule](https://www.census.gov/retail/release_schedule.html)
- [China-Options-Engine — radar_latest.json](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)
- [China-Options-Engine — radar_history.json](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_history.json)
