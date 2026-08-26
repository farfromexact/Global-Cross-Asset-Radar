# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-26

> 数据截点：北京时间2026-08-26 19:30。中国日盘为2026-08-26完整EOD；15:00—19:30海外变化单独使用实时/准实时公开来源。21:00中国夜盘尚未发生。

## 一、今日一句话结论

**有值得冒险的条件机会，但没有19:30可立即建立的新仓：RM611回撤多最优，FG701/EG2610只做失败反弹空；21:00首跳均禁追。**

今天不是“全面Risk-off”的简单一天。最值得交易的是结构已经获得期限和期权确认的个别品种；能源/化工的单日暴跌却与Backwardation严重冲突，追空赔率并不好。

## 二、数据质量与覆盖说明

第一读取层实际读取`farfromexact/China-Commodities-Engine`的`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；为Top候选继续读取`data/market_state_latest.json`、`data/physical/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`。`report_input requested_date=2026-08-26`，`generated_at=2026-08-26T19:05:02.243742+08:00`。

核心Futures五所SHFE/INE/DCE/CZCE/GFEX齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical module errors=0；unknown、duplicate、invalid OHLC、negative volume/OI均为0。当前module-specific汇总记录placeholder=11，已排除异常排行；根目录旧状态与其有轻微计数差异时，按v2协议以report_input/module-specific为准。Market State具备20个交易日历史，1D/3D/5D/20D均按同一具体合约计算，不拼连续主力。

Physical于19:04:56生成：20个目标中4个按原生发布频率可用、16个不可用、0 stale、0 carried-forward。可用品种为I港口库存、JM现货、FG企业库存、TA加工费；其中FG仍只是最新周度绝对水平，未形成可验证方向变化，因此不计完整实体方向证据。没有RM/EG/FU的可用实体闭环。

External仓库日频层最新source date主要为2026-08-25，整体`data_fresh=false`；逐series仍可作context，但没有exact-contract、币种、品质、税费、运费和时点全部对齐的可执行进口平价。今晚15:00—19:30海外变化另用Reuters等实时来源，不把它倒写成中国日盘已经发生的变化。

Options为**2026-08-26 T日数据**：20,346条链、覆盖约87.5%的品种、344个series；330 surface-ready、62 positioning-ready、0 execution-ready。IV coverage约94.46%，OI coverage约67.19%，bid/ask coverage=0。因而ATM IV/RR25/BF25/IV-RV可以研究；任何Spread都不能声称可按某净权利金成交，dealer gamma方向也未知。RM/FG/EG具体T日series均surface-ready；RM具体series positioning-ready；全部execution=false。

Contract metadata为official-partial：具体最后交易日可部分读取，但multiplier/tick/margin/price-limit/night-session字段并非所有合约都完整。前三名合约基础规格可由交易所长期合约规则交叉核对；**今晚动态保证金、动态涨跌停和券商加收保证金均未可靠确认，不拿静态最低标准冒充执行参数。**

## 三、商品仪表盘

| 板块 | 合约 | 8/26 Close / Settle | 1D / 5D | Volume / OI | ΔOI | Curve | Physical / Options | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|
| 油粕 | **RM611** | **2314 / 2282** | **+2.06% / +1.06%** | 989,630 / 671,302 | **+5.28%** | **Back +3.33%** | 无Physical；ATM IV 18.18%，surface+positioning✓/exec× | **第一候选多** |
| 建材 | **FG701** | **895 / 905** | **-1.20% / -0.77%** | 1,236,286 / 1,645,325 | **+9.08%** | **Contango -2.91%** | 周度库存仅level；ATM IV 22.80%，surface✓/exec× | **失败反弹空** |
| 化工 | **EG2610** | **5168 / 5247** | **-4.55% / +4.56%** | 941,964 / 376,074 | **+4.04%** | **Back +2.88%** | 无Physical；ATM IV 43.95%，surface✓/exec× | **冲突型条件空** |
| 能源 | **FU2611** | 3622 / 3675 | **-6.61% / -3.29%** | 1,098,439 / 261,424 | **-8.88%** | **Back +16.04%** | 无Physical；T日期权可研究 | **价格/curve极端冲突** |
| 贵金属 | **AG2610** | — / 16670 | **-0.63% / +6.69%** | 643,479 / 269,980 | **-4.34%** | 轻Contango -0.22% | T日期权总体可研究 | **PCE前观察** |
| 化工 | MA610 | 2769 / 2830 | settle约-3.94% | 2,389,984 / 823,697 | — | Back +0.71% | Physical缺 | 价格弱、curve未转空 |
| 塑化 | PP2701 | 7769 / 7875 | settle约-3.72% | 818,380 / 538,637 | — | Back +2.85% | Physical缺 | 不追空 |
| 聚酯 | TA701 | 5492 / 5566 | settle约-3.74% | 1,293,895 / 865,893 | — | Back +1.19% | 最新周度加工费context | 价格弱、结构仍紧 |
| 新能源 | LC2701 | — | close约-1.17% | 217,163 / 358,778 | — | Contango | 实体方向闭环不足 | 观察 |
| 豆粕 | M2701 | — | close约+2.14% | 1,762,183 / 2,682,712 | — | Contango | 外盘/进口闭环不足 | 与RM分化 |
| 有色 | AO2610 | — | close约-1.97% | 275,656 / 264,269 | — | Contango | basis/库存闭环不足 | 中性偏弱 |

Curve全部是近月—次近月期货结构，不是现货基差。近月接近交割导致的曲线污染会降权，不把不可比价差写成套利。

## 四、相比上一交易日真正变化

**第一，昨天第一名EG多头逻辑今天被价格直接否定。** EG2610结算从5497降到5247，1D -4.55%，同时OI增加4.04%；昨晚“回撤后重获5500才多”的条件没有成立。更关键的是它仍保持约2.88% Backwardation，因此今天也不能机械反手追空，只能把策略改成“反弹失败且curve松动后空”。

**第二，RM611升级为最干净的国内强势结构。** settle +2.06%、close 2314、OI +5.28%、volume z约+2.66，同时近端Backwardation约3.33%；T日期权ATM IV 18.18%，具体series surface与positioning均ready。价格—持仓—期限—期权四个观察维度中，前三个方向至少不互相打架；但Physical为空、海外油籽映射并未同步确认，所以仍停在79分。

**第三，FG空头结构比昨天更完整。** settle -1.20%，OI一天增加约9.08%，近端仍为约2.91% Contango。这里“价跌仓增”只是方向压力线索，不能写成确定的新空。FG的最新周度企业库存只有绝对水平，尚未给出今日实体确认。

**第四，FU出现全市场最值得警惕的price/curve分叉之一。** 结算-6.61%、OI -8.88%，但Backwardation反而扩到约16.04%。与此同时18:12 BJT左右Brent约85.85美元、-3.08%，WTI约80.15美元、-2.68%。海外确实在继续回吐Hormuz风险溢价，但如此紧的中国curve意味着“价格暴跌=供应松弛”这个解释并未被结构确认，追空很差。Reuters同时报道伊朗与阿曼在讨论临时通航走廊和扫雷，但实际船舶通行仍明显低于常态。
来源：https://www.reuters.com/world/asia-pacific/us-oil-prices-extend-losses-hopes-iran-oman-talks-strait-hormuz-2026-08-25/

**第五，AG进入典型事件前低信息区。** 17:27 BJT附近现货黄金约4618美元、-0.8%，白银约68.48美元、-0.2%；20:30 BJT还有美国7月PCE和二季度GDP二次估计。中国21:00开盘前还会先经历一次宏观重定价，因此19:30提前押贵金属方向没有明显edge。
来源：https://www.reuters.com/world/india/gold-little-changed-with-us-inflation-data-spotlight-2026-08-26/

## 五、产业链地图

| 链条 | 方向 | Price / Curve | 实体 | 海外/宏观 | Options | 最大缺口 | 置信度 |
|---|---|---|---|---|---|---|---|
| **菜粕/油粕** | 国内偏强 | RM价涨仓增+Back | **缺** | 外部油籽未同向闭环 | RM T日surface/positioning可用 | 压榨、进口、库存方向 | **中高** |
| **玻璃建材** | **偏弱** | FG价跌仓增+Contango | 周度库存仅level | 海外影响较小 | T日surface可用 | 库存变化、深加工订单 | **中高** |
| **MEG/聚酯化工** | 价格急弱、结构仍紧 | EG/TA价跌但Back | EG缺；TA仅加工费context | 原油继续跌 | EG T日IV/skew应激 | 进口/库存/下游减产 | **中** |
| **原油—燃料油** | 风险溢价回吐 | FU价格崩而Back极强 | 缺 | Brent/WTI继续跌 | 研究可用 | Hormuz真实通行、库存/EIA | **中** |
| **贵金属** | 事件前中性 | AG短跌但5D仍强 | 非核心 | PCE/Jackson Hole | T日期权总体可用 | 20:30宏观结果 | **中低** |

**最强可交易结构是RM，不等于整个农产品链全面转多；最弱价格链是EG/MA/PP/TA，但其Backwardation没有全面转弱，因此更像高波动去风险而非已确认的供给宽松。** 当前regime是“地缘能源风险溢价快速回吐 + 化工price/curve分叉 + 国内油粕相对强势 + 贵金属等待宏观事件”。

## 六、机会排行榜

| Rank | 机会 | Score | 逻辑/赔率/催化/结构/技术 | Fresh层 | 工具 | 阶段 |
|---:|---|---:|---|---:|---|---|
| **1** | **RM611 回撤确认多** | **79** | 21 / 20 / 14 / 13 / 11 | **3** | Futures / Call Spread | 条件试仓 |
| **2** | **FG701 失败反弹空** | **77** | 21 / 20 / 12 / 13 / 11 | **3** | Futures / Put Spread | 条件试仓 |
| **3** | **EG2610 失败反弹空** | **76** | 20 / 18 / 15 / 12 / 11 | **3** | Futures / Put Spread | 条件试仓 |
| 4 | FU2611 price-curve错位 | 69 | 18 / 16 / 15 / 10 / 10 | 2 | 观察 | No-Trade |
| 5 | AG2610 PCE事件观察 | 66 | 17 / 15 / 17 / 8 / 9 | 2 | 观察 | No-Trade |

没有80+确认交易。RM达到70+但没有Physical/海外同向闭环；FG没有方向性Physical；EG则被Backwardation强烈反驳。**因此今天值得冒险的是“触发后的小风险”，不是现在就有仓。**

## 七、前三名交易卡

### 1. RM611｜回撤确认多｜79

**事实：** settle 2282，close 2314，1D +2.06%、5D +1.06%，volume 989,630、OI 671,302、ΔOI +5.28%，近端Backwardation约3.33%；RV20约13.86%。T日期权2026-10-13 expiry，ATM strike 2275、ATM IV 18.18%、RR25 +4.82vol、BF25 +1.88vol，surface-ready、positioning-ready、execution-ready=false。

**市场定价：** 国内菜粕正在交易相对强势和近端紧张，但海外油籽没有形成可执行进口平价确认。  
**推断：** 21:00后如果2280附近承接成立、2300—2315重新被接受，今天的日盘强势有延续价值；如果只是日盘短暂挤压，夜盘会很快跌回2280下方。  
**主观判断：** 这是今晚最值得承担的小风险，但不追2314附近第一跳。

**新鲜证据层：3层。** 价格/OI、curve、T日期权；Physical缺失，海外映射不计同向层。  
**最佳表达：** 先用小期货确认；若真实期权quote出来后流动性足够，可替换成2026-10-13的1:1 Call Spread，长35—45Δ、短15—25Δ。execution=false，当前不报premium。  
**入场：** 21:00后等15—30分钟；2275—2285守住，并重新接受2300—2315，先做1/3风险。  
**加仓：** 突破首30分钟高点，同时OI继续增加、Backwardation不快速塌缩。  
**初始止损：** 30分钟有效接受2250—2260下方。  
**逻辑失效：** 跌破2280后无法收回，且近端Back压到约1.5%以下；或海外油籽继续走弱并出现可信进口/压榨供应宽松证据。  
**TP1 / TP2：** 2335—2350 / 2380附近或+2R。  
**时间止损：** 1—2个交易时段不能创新高即撤。  
**最大损失：** 初始0.35%—0.55% NAV；若用Call Spread则最大损失为人工核价后的净权利金。  
**1—20D催化：** 8/27 USDA出口销售、后续油籽天气/进口到港、压榨开机与菜粕库存。  
**最坏情景：** 外盘油籽下跌+人民币走强+进口供应改善，夜盘高开低走并触发流动性滑点。  
**放弃条件：** 开盘直接拉升超过约1.5%且无回测，或首30分钟跌破2260。

合约基础规格：CZCE RM，10吨/手，tick 1元/吨，tick value 10元；按2282结算名义约22,820元/手。长期合约规则可核对最低保证金/基础涨跌幅，但**今晚动态交易所保证金、实际price limit与券商加收未确认，不用旧静态参数代替**；因此1/2板压力损失不做伪精确数字，公式为“名义×今晚有效涨跌停比例”，连续两板需按第二日重新计算。最后交易日规则为交割月第10个交易日，实物交割；建议最迟T-10前开始roll。仓库存在RM夜盘记录，21:00开盘资格确认；结束时点以郑商所当日公告为准。

### 2. FG701｜失败反弹空｜77

**事实：** settle 905，1D -1.20%、5D -0.77%，volume 1,236,286、OI 1,645,325、ΔOI +9.08%，近端Contango约-2.91%；RV20约17.23%。T日期权2026-12-11 expiry，ATM 900、ATM IV 22.80%、RR25 +7.48vol、BF25 +1.04vol，surface-ready、execution=false。

**市场定价：** 价格、OI与curve都更偏弱，但FG最新周度企业库存只有绝对水平，不能称实体端已经确认下跌。  
**推断：** 真正的edge是反弹无法穿回前结算/日内价值区，而不是在低位继续追空。  
**市场可能错在哪里：** 供给端临时减产、地产/深加工订单改善，或库存突然转为持续去化，都会快速收窄Contango。

**新鲜证据层：3层。** 价格/OI、curve、T日期权；Physical仅context不计层。  
**最佳表达：** 期货失败反弹空；或者2026-12-11 1:1 Put Spread，长35—45|Δ|、短15—25|Δ|。由于RR25已经明显倾斜且execution=false，不建议凭理论IV直接买单腿Put。  
**入场：** 等30分钟；908—916反弹失败、VWAP下方承压后重新跌破900/898。  
**加仓：** 跌破890且反抽不能收回。  
**初始止损：** 30分钟有效接受920上方。  
**逻辑失效：** Contango收窄到约1.5%以内，同时出现可验证的库存下降或深加工需求改善。  
**TP1 / TP2：** 890 / 870附近或+2R。  
**时间止损：** 两个交易日没有新低即撤。  
**最大损失：** 0.25%—0.40% NAV；Put Spread最大损失为人工核价后的净权利金。  
**最坏情景：** 政策/供给突发触发高OI环境下挤空。  
**放弃条件：** 21:00直接大幅gap-down跌破890，禁止追空。

合约基础规格：CZCE FG，20吨/手，tick 1元/吨，tick value 20元；905对应名义约18,100元/手。动态保证金/涨跌停/券商加收今晚未确认，不计算板损数字；最后交易日按交割月第10个交易日规则、实物交割，T-10前开始roll。仓库存在FG夜盘记录，21:00开盘资格确认，具体结束时点仍以交易所当日公告为准。

### 3. EG2610｜失败反弹空｜76

**事实：** close 5168、settle 5247、pre-settle 5497，1D settlement -4.55%、close约-5.99%，OI +4.04%，5D仍+4.56%，近端Backwardation约2.88%。T日期权2026-09-16 expiry，ATM strike 5200、ATM IV 43.95%、RR25 -20.66vol、BF25 +0.37vol，surface-ready、execution=false。

**市场定价：** 昨日供应短缺多头发生剧烈去风险；但curve仍在Back，说明现货/近端紧张没有被价格暴跌完全否定。  
**推断：** 如果今晚外油继续偏弱，EG反弹到5200—5280/5300仍失败，且Back开始收窄，才说明“价格弱”终于得到结构层部分确认。  
**主观判断：** 可以做条件空，但绝对不追低开第一跳；这是三张卡里冲突最大、最容易被V形反转的一张。

**新鲜证据层：3层。** 价格/OI、15:00—19:30海外原油、T日期权；curve方向冲突，Physical缺失。  
**最佳表达：** 小期货确认空，或2026-09-16 Put Spread；ATM IV 43.95%且skew极端，裸买Put赔率不佳。  
**入场：** 等30—45分钟；5200—5280/5300反弹失败，且Back从2.88%向2%以下压缩，先1/3风险。  
**加仓：** 跌破5120、反抽无法收回。  
**初始止损：** 30分钟有效接受5335—5360上方，并且Backwardation重新扩张。  
**逻辑失效：** 重回5350上方、OI不再扩张且出现可信进口/库存紧张重新强化证据。  
**TP1 / TP2：** 5100 / 4950附近或+2R。  
**时间止损：** 两个交易时段无新低即撤。  
**最大损失：** 0.35%—0.50% NAV。  
**1—20D催化：** 原油/Hormuz、MEG进口船期、港口库存、聚酯开工与EIA。  
**最坏情景：** Hormuz谈判突然恶化，原油与MEG同时V形反转，EG在Back结构下出现快速逼空。  
**放弃条件：** 21:00直接深低开且Back不缩，或价格重回5350。

合约基础规格：DCE EG，10吨/手，tick 1元/吨，tick value 10元；5247对应名义约52,470元/手。当前contract metadata为partial，今晚动态交易所保证金、price limit、券商加收和具体最后交易日日历日未完整确认，所以不计算1/2板固定损失；DCE公开交易制度对有夜盘品种给出21:00—23:00夜盘框架，仓库也有EG对应夜盘记录。实物交割，建议T-10前主动roll。

## 八、商品期权专项

今天Options是T日，研究层明显好于执行层：**344个series中330 surface-ready、62 positioning-ready、0 execution-ready；IV coverage约94.46%，OI coverage约67.19%，bid/ask coverage=0。** 因此不称全市场“最高/最低IV”，只做已复核代表series比较。

RM611：ATM IV 18.18% vs RV20 13.86%，IV-RV约+4.3vol；RR25 +4.82。  
FG701：ATM IV 22.80% vs RV20 17.23%，IV-RV约+5.6vol；RR25 +7.48。  
EG2610：ATM IV 43.95%，高波动且RR25约-20.66vol，明显反映尾部不对称；在没有bid/ask时不解释成“便宜Put”。

**结构选择：** RM方向若确认，Call Spread优于在夜盘首跳后裸追期货；FG/EG空头若确认，Put Spread用于封顶gap风险。**必须回避：** 裸卖Hormuz/EIA/PCE事件Vega、用理论IV臆造净权利金、用全市场OI coverage 67%推dealer positioning。Dealer gamma方向未知。

没有满足exact-contract、品质、币种、税费、运费和同步quote的跨市场套利；跨期限/跨品种RV也没有达到正式交易卡标准。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国8/26结算 | 15:00—19:30海外映射 | 预期首跳 | 置信度 | 追价 | 等待 | 开盘后最重要确认 |
|---|---:|---|---|---|---|---|---|
| **RM611** | 2282 | 海外油籽proxy未同向确认 | 平/小高 | 中 | **否** | 15—30m | 2280、2300—2315、OI、Back |
| **FG701** | 905 | 海外映射弱 | 平/偏低 | 中高 | **否** | 30m | 908—916失败、900/898、Contango |
| **EG2610** | 5247 | Brent/WTI约-3%/-2.7% | **偏低** | 中高 | **否** | **30—45m** | 5200—5300反弹、Back是否缩 |
| **FU2611** | 3675 | Brent 85.85、WTI 80.15，继续下跌 | **偏低** | 高 | **绝不追空** | 30—45m | 16% Back、SC/FU联动、EIA |
| **AG2610** | 16670 | 17:27金银偏弱；20:30 PCE尚未发布 | **20:30后重估** | 低 | **否** | 15—30m | DXY、实际利率、GC/SI、16600 |
| MA610 | 2830 | 原油偏弱 | 偏低 | 中 | 否 | 30—45m | 反弹质量、Back |
| TA701 | 5566 | 原油偏弱 | 偏低 | 中 | 否 | 30—45m | 现货加工费、Back、EG联动 |
| PP2701 | 7875 | 原油偏弱 | 偏低 | 中 | 否 | 30—45m | 7800附近承接、Back |
| LC2701 | — | 无可靠同品种海外实时映射 | 未定 | 低 | — | — | **本轮夜盘安排未确认；下一确定窗口8/27 09:00** |

注意：20:30 BJT的PCE发生在中国夜盘开盘前30分钟，贵金属/美元相关品种的“预期gap”在19:30本来就低置信；22:30 BJT EIA则会落在部分能源/化工夜盘交易时段内。任何21:00前的海外价格都只是映射证据，不是中国夜盘已经交易。

## 十、未来24h / 7d事件日历（北京时间）

**8月26日20:30**：BEA发布7月Personal Income and Outlays/PCE，同时发布二季度GDP第二次估计。对AG/AU、美元、实际利率最直接；数据前不新增贵金属裸Delta，若必须持有优先有限风险结构。  
官方：https://www.bea.gov/news/schedule

**8月26日22:30**：EIA Weekly Petroleum Status Report。对SC/FU/LU/BU及化工Beta直接；若21:00已有盈利，EIA前减Delta，而不是把能源链多个合约叠成同一方向。  
官方：https://www.eia.gov/petroleum/supply/weekly/

**8月27日**：USDA FAS Weekly Export Sales，覆盖大豆、豆粕、豆油、玉米、棉花等；RM/M/Y/P等农产品需关注外盘出口节奏，具体发布时间以FAS当日页面为准。  
官方：https://fas.usda.gov/data

**8月27—29日**：Jackson Hole Economic Policy Symposium，2026主题“Financial Innovation: Implications for Payments and Policy”。对黄金、美元、利率与长久期风险资产主要通过政策路径和实际利率传导。  
官方：https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/

**8月29日03:30**：CFTC COT常规周五15:30 ET发布，对能源、贵金属、农产品positioning提供背景；数据是此前周二快照，不作即时流量。  
官方：https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm

**持续事件：Iran/Oman—Hormuz临时通航走廊、扫雷与实际船舶通行量。** 新闻改善可以压低油价risk premium，但实际通行仍低于常态，因此FU/EG既有低开风险，也有谈判反复造成的V形gap风险。Reuters：https://www.reuters.com/world/asia-pacific/us-oil-prices-extend-losses-hopes-iran-oman-talks-strait-hormuz-2026-08-25/

风险预算：单一试仓最大损失0.25%—0.75% NAV；确认交易0.75%—1.50%；单一高确信主题≤2.5%—3.0%。RM/M/Y/P按油籽/饲料因子合并；EG/TA/MA/PP/FU/SC按能源—化工因子合并；AG/AU按美元—实际利率因子合并。对所有结构都压力测试1/2个涨跌停、相关性破裂、夜盘gap、保证金上调、IV跳升/塌陷、流动性消失、交割挤压和人民币急变。

## 十一、行动清单

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：RM611回撤确认多；FG701失败反弹空；EG2610失败反弹且Backwardation收窄后空。  
C. 今天应继续观察的机会：FU2611价格/curve极端错位、AG2610 PCE后重定价、MA/TA/PP化工链是否由价格弱转为curve弱。  
D. 今天必须避免或退出的交易：21:00追首跳、追空FU/EG深低开、把FG周度库存绝对水平当方向确认、在execution=false时虚构期权权利金/滑点、在PCE/EIA前堆叠同因子裸Delta或裸Vega。
