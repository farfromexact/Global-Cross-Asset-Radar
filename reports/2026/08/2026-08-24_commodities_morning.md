# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-24

> 数据截点：北京时间 2026-08-24 07:20 左右。仅用于研究与交易决策支持，不自动下单。中国国内基线为最近完整交易日 2026-08-21 EOD；China-Commodities-Engine 不生产中国分钟、逐笔、夜盘/session 产品，因此本报告不从仓库推断周五中国夜盘。海外层使用仓库 06:24 重建后的日频 External，并补充 07:00 附近公开实时衍生报价；两者与中国 EOD 严格分开。

## 一、今日一句话结论

**今天有值得冒险的机会，但没有开盘前可立即建立的新仓：FU2611 回撤确认多仍是第一选择；FG701 失败反弹空升至第二；AG2610 只做回撤多且不裸追Call。周一海外重开后油价反而小幅走弱，最重要的信息已从“周末新闻”切换为“9:00后的价格接受度”。**

## 二、数据质量与覆盖

第一读取层已直接从 `farfromexact/China-Commodities-Engine` main 读取：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需进一步读取 `data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/contract_meta.json`。协议版本：`china_commodities_v2`。

统一输入 `requested_date=2026-08-21`，但晨间已于 `2026-08-24T06:24:20.563750+08:00` 重建。中国 Futures 仍是 8/21 最近完整 EOD：SHFE/INE/DCE/CZCE/GFEX 五所齐全，`full_market_ready=true`，`source_date_match_pct=100%`，803 个期货合约，critical errors=0，unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0，核心 carried-forward=0；placeholder=5，不进入异常排行。

Market State 同合约 1D/3D/5D/20D、RV20、成交/OI z-score、ΔOI 和 near-next curve 可用，不拼接不同主力收益。Physical 仍仅 4/20 映射：I 港口库存（最新周度 8/19）、JM NBS 现货（最新旬度 8/10）、FG 企业库存（最新周度 8/20-21）、TA 加工费（最新周度 8/21）。JM basis 只有 C 级，不能计分、不能称套利。

External 本次晨间已经重建：`requested_date=2026-08-24`，`generated_at=2026-08-24T06:24:19.226673+08:00`。22 个目标中 6 个有验证映射，5 fresh、1 stale；overall `data_fresh=false` 是由部分缺失/陈旧序列造成，不能一刀切丢弃 fresh series。仓库可用 Brent、LME Cu、SGX iron ore、USD/CNH、DXY 都只作 context，且没有 executable import parity。本报告另外使用 07:00 前后公开实时衍生报价做开盘 gap 映射。

Options 独立流水线仍是 8/21：21,816 条记录，59/64 品种成功，368 个 series 中约 360 surface-ready、70 positioning-ready、0 execution-ready，bid/ask coverage=0；AP/CJ/PL/PR/ZC source-date 不匹配。**因为今天已经进入下一中国交易日，8/21 Options 只作背景，不计今天 fresh evidence 层。** Dealer gamma 方向未知，禁止推断。

Contract Metadata 为 partial；FU/AG 通过上期所官方规则与最新风控公告补齐交易单位、tick、动态涨跌停和交易所保证金。FG701 的交易单位、tick、交割规则可由郑商所规则确认；公开同步数据指向交易所保证金约9%、涨跌停约8%，但未找到同等强度的郑商所当日官方动态公告，因此正式下单前仍需终端/交易所复核，券商加收保证金均视为未确认。

## 三、商品仪表盘

| 板块 | 合约 | 8/21 close / settle | 1D结算 | 5D | 成交/OI/ΔOI | curve | Physical / basis | Options背景 | 07:00海外映射 / 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能源 | **FU2611** | 3845 / 3850 | +2.12% | **+9.81%** | 650,637 / 285,614 / +22,573（+8.58%） | **Back约+7.47%** | 实体层缺失 | ATM IV约43%，8/21 T-1背景 | Brent Nov约91.88（-0.85%）、WTI Oct约86.4（-0.3%）实时衍生；**回撤确认多** |
| 能源 | BU2610 | 4508 / 4526 | +2.14% | +7.92% | 486,111 / 334,627 / -2,643（-0.78%） | Back约+3.16% | 实体层缺失 | ATM IV约27.75%，T-1 | 与油同因子；仅FU替代 |
| 贵金属 | **AG2610** | 16771 / 16611 | +3.11% | +5.45% | 773,038 / 306,822 / +4,403（+1.46%） | 轻Contango约-0.14% | 实体层缺失 | ATM IV47.265%、RR25 +7.81，T-1 | COMEX Sep银约69.06、近乎持平；**回撤多，不追Call** |
| 建材 | **FG701** | 907 / 906 | -1.09% | -3.10% | 1,575,371 / 1,601,238 / +148,375（+10.21%） | **Contango约-3.35%** | 浮法厂库7441.4万重箱，周环比-0.07%、同比+17.41% | surface可研究但T-1 | **失败反弹空**；高库存与弱需求仍压制 |
| 黑色 | I2701 | — / 约707 | +0.14% | -0.63% | 数据可用，未列精确量 | 近端结构无强信号 | 港口库存最新周度8/19 | T-1 | SGX铁矿8/21日频仍约低90美元区间；中性 |
| 新能源 | LC2701 | 158680 / 156360 | +2.60% | +1.41% | 225,444 / 353,437 / +31,875（+9.91%） | **仍Contango约-0.30%** | 锂实体库存缺失 | surface可研究，T-1 | price/OI强但curve不确认；不称短缺 |
| 有色 | CU2610 | 107520 / 107010 | +0.14% | -0.39% | ΔOI +7,165（+4.22%） | 近端轻Back约+0.26%，样本短 | 无A/B基差 | ATM IV约14.3%、RR25 +4.14，T-1 | COMEX铜约-0.1%；不追LME squeeze |
| 化工 | MA610 | — / 2880 | +1.80% | **+8.56%** | 价涨仓增线索；volume z≈2.24 | Back约+0.35% | 实体层缺失 | T-1 | 油价重开转弱，油链扩散交易需降温 |
| 农产品 | RM611 | 2238 / 2246 | -1.36% | +2.60% | 747,569 / 651,265 / — | **Back约+3.96%** | 实体层缺失 | T-1 | 价格/curve冲突；CBOT豆类仅小幅上行，观望 |
| 软商品 | CF701 | — | +0.29% | +2.18% | ΔOI约+0.1% | Contango约-1.58% | 实体层缺失 | T-1 | 无足够edge |
| 航运 | EC2610 | 1957 / 1885.5 | +7.56% | **+18.66%** | ΔOI约+11.84% | 不作普通curve套利 | 事件驱动 | 无执行级vol | 极端动量；**45分钟内不追** |

海外实时口径说明：Investing 页面明确标记为 `Real-time derived`，不是交易所官方结算。07:00 前后页面显示 Brent 已滚至 Nov-26 合约，约 91.88、较该页面同合约前收低约0.85%；WTI Oct-26 约 86.4、低约0.3%；Gold Dec-26 约4663、近乎持平，Silver Sep-26 约69.06、近乎持平，DXY约98.79、小涨约0.06%。不能把这些价格与8/21不同月份连续合约直接计算跨期收益。

## 四、相比上一期真正变化

1. **最重要变化：海外周一重开没有继续追能源风险溢价。** 周末伊朗制裁威胁仍在，但 Brent Nov 与 WTI Oct 早盘反而分别约 -0.85% / -0.3%。这使 FU 从“可能高开追趋势”进一步收敛为“只等回撤被承接”。
2. **伊朗风险仍是双尾，而不是解除。** 美国财政部长 Scott Bessent 计划周一 14:00 EDT（北京时间8/25 02:00）说明新一轮伊朗制裁；伊朗公开反对。Hormuz 非授权船舶通行仍接近停滞，但伊朗已允许部分伊拉克油轮通行。事件分布同时包含供应收紧与选择性恢复流量两条路径。
3. **贵金属外盘不再加速。** 周五 COMEX 金银强收，但周一亚洲早盘 Gold/Silver 仅在前收附近，AG 若国内显著高开将更像相对过冲，而不是海外新信息确认。
4. **FG 的实体层比周末版更清晰但不是单向利空。** 隆众/Mysteel 8/20 样本企业库存 7441.4 万重箱，周环比仅 -0.07%（轻微去库），但同比仍 +17.41%，库存天数34.1天不变；供应日产14.22万吨环比持平。实体层结论是“高库存没有真正缓解”，而不是“本周重新累库”。
5. **Options从今天起全部降为T-1背景。** 8/21 surface 可以描述IV/skew，但按v2规则不再算今天 fresh evidence，因此 FU/AG/FG 都不能靠期权层凑到四层确认。
6. **中国量价本身没有新数据。** 周五夜盘没有来自仓库的可审计session产物，本报告也没有用低质量第三方价冒充官方夜盘。

## 五、产业链地图

**能源/炼化仍最强，但regime变为“高风险溢价 + 重开不追价”。** FU 的价仓和Backwardation是国内最干净组合；Hormuz与制裁是外部催化，但海外重开下跌说明边际买盘并没有继续扩张。最大缺失是国内燃料油现货/库存/裂解和周一真实新增OI。

**建材仍最弱。** FG价格跌、OI大增、contango清晰；最新周度库存虽微降0.07%，但同比高17.41%，地产/深加工需求仍弱。做空逻辑的主要风险不是基本面突然转牛，而是低价、亏损与政策headline导致短挤压。

**贵金属强趋势转为高IV盘整。** AG趋势强，海外金银也在高位，但周一重开没有继续加速；8/21 ATM IV47.265%相对RV20约30.82%高约16.45 vol，RR25 +7.81。期权背景仍表明上行尾部贵，但今天没有fresh option报价可执行。

**新能源仍是反弹而非短缺。** LC价格和OI很强，curve却仍contango，且没有库存/现货方向闭环；必须等curve收窄与实体层同步才升级。

**农产品与航运的headline beta高于可交易edge。** Black Sea风险仍抬高粮运尾部，但RM自身价格与curve冲突；EC已经5D接近+19%，开盘追价的负凸性很明显。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段/工具 | 今日fresh证据层 | 数据惩罚 |
|---:|---|---:|---|---|---:|---|
| 1 | **FU2611 回撤确认多** | **77** | 多 / 1–5D | 条件试仓；期货优先 | 3：价仓、curve、海外/宏观 | Physical缺；Options仅T-1；海外重开转弱 |
| 2 | **FG701 失败反弹空** | **74** | 空 / 1–5D | 条件试仓；期货优先 | 3：价仓、curve、最新周度Physical | 库存周环比微降；动态参数需复核 |
| 3 | **AG2610 回撤确认多** | **72** | 多 / 1–3D | 条件试仓；小期货，期权待fresh quote | 3：价仓、curve、海外/宏观 | curve弱；海外重开不加速；Options仅T-1 |
| 4 | BU2610 能源替代多 | 70 | 多 / 1–3D | 仅不持FU时 | 3：价仓、curve、海外/宏观 | 价涨仓减；与FU高度重复 |

没有80+确认交易，也没有四层fresh且无关键错误的加仓级机会；因此今天所有70+都只允许条件试仓。

## 七、前三名交易卡

### 1）FU2611｜77分｜回撤确认多

**事实**：8/21 settle 3850；1D +2.12%、5D +9.81%；ΔOI +8.58%；近端Backwardation约+7.47%。**市场定价**：高供应风险已经计入相当比例。**推断**：周一重开油价转弱后，国内第一回撤能否被吸收比周末headline更有信息量。**主观判断**：不追高，只有“回撤不破+重新接受”才值得冒险。

**Fresh层**：价-量-OI；curve；海外/宏观。Options 8/21 仅背景，不计fresh；Physical缺失。

**最佳表达**：期货优先。若日盘后拿到fresh bid/ask，才考虑1:1 Call Spread（长约35–45Δ、短约15–25Δ），不预设净权利金。

**入场/分批**：09:00后至少等30分钟。若开盘在3810–3850附近或先下探后收回，且重新站上VWAP/3850，先1/3；突破Opening Range High再1/3；只有ΔOI继续增加且Backwardation不明显压缩，再加最后1/3。若直接高开>2%，至少等45分钟；若开盘<3810，不接第一刀。

**止损/失效**：3810下方形成15分钟接受先减半；约3770失守，同时FU Back明显收窄且Brent/WTI继续走弱，逻辑失效。

**退出**：TP1 3970；TP2 4080；2个交易日不延续则时间止损。最大初始损失 0.35%–0.50% NAV；FU+BU+SC+LU初始合并≤0.75% NAV。

**合约参数**：上期所官方：10吨/手；tick 1元/吨；tick value 10元/手；按3850名义约38,500元/手。2026-06-23公告适用于FU2611：涨跌停14%、套保保证金15%、一般持仓16%；券商保证金未确认。夜盘属于交易所“其他交易时间”，精确当日时段下单前复核。repo元数据确认FU2611最后交易日2026-10-30；实物保税交割，交割月前必须滚动/退出。按14%静态压力：一板逆向约5,390元/手；连续两板复合约10,025元/手。

**最坏情景**：Hormuz突然实质恢复、制裁弱于预期、周一油价继续跌且中国高位多头集中撤退；此时backwardation与OI应同步恶化，不能用“地缘仍紧张”给亏损仓找理由。

### 2）FG701｜74分｜失败反弹空

**事实**：8/21 settle 906；1D -1.09%、5D -3.10%、20D -7.46%；ΔOI +10.21%；near-next约-3.35% contango。隆众/Mysteel最新周度样本库存7441.4万重箱，周环比-0.07%、同比+17.41%，库存天数34.1天不变。**市场定价**：弱地产/深加工需求已部分进入低价。**推断**：高库存未解，但低价与政策beta使直接追空赔率一般。**主观判断**：只做反弹失败，不在集合竞价卖。

**Fresh层**：价-量-OI；curve；最新周度Physical（有方向变化和同比比较）。Options仅T-1背景。

**最佳表达**：期货短。fresh option quote出现且执行质量合格后，可转1:1 Put Spread降低跳空风险；目前不报权利金。

**入场/分批**：等待30分钟。910–918反弹失败、重新跌回VWAP下方，先1/2；跌破899且ΔOI不塌缩再加1/2。若开盘直接<895，不追，等反抽。

**止损/失效**：30分钟接受在920上方止损；若curve显著收窄，同时厂库去化明显加快/下游订单实质改善，则逻辑失效。

**退出**：TP1 899；TP2 880；2个交易日不能有效跌破899则退出。最大初始损失0.25%–0.40% NAV。

**合约参数**：郑商所规则可确认20吨/手、tick 1元/吨、tick value 20元/手；按906名义约18,120元/手；最后交易日为交割月第10个交易日，实物交割，repo partial metadata给出2027-01-15作为当前last-trading-day字段。公开同步表显示FG701交易所保证金约9%、涨跌停约8%，但本次未取得同强度的郑商所当日官方动态公告，故这两个参数标记“下单前必须复核”，券商保证金未确认。**因此不把8%写成正式压力损失数字**；确认实际L后，一板压力=18,120×L，两板复合压力=18,120×[1-(1-L)^2]。夜盘存在，但精确当日安排下单前复核。交割前至少20个交易日完成滚动/退出。

**最坏情景**：政策/地产headline触发beta short squeeze，同时玻璃现货提涨、库存去化加速；低位空头的gap风险高于表面波动。

### 3）AG2610｜72分｜回撤确认多

**事实**：8/21 close/settle 16771/16611；1D +3.11%、5D +5.45%、20D +17.59%；ΔOI +1.46%；curve轻contango。8/21期权ATM IV47.265%、RR25 +7.81、BF25 +1.93，但今天仅T-1背景。07:00前后COMEX Sep银约69.06，基本持平，黄金Dec也接近前收。**市场定价**：趋势和上行尾部已经很贵。**推断**：若中国AG显著高开而外盘不跟，反而是负面信息。**主观判断**：只买回撤，不追突破。

**Fresh层**：价-量-OI；curve；海外/宏观。Options不计fresh。

**最佳表达**：小仓期货。若拿到8/24 fresh quotes，优先1:1 Call Spread或Call Butterfly；背景Delta区间可用长35–45Δ/短15–25Δ，但实际strike、净支出、Delta/Gamma/Theta/Vega必须用fresh链重算。

**入场/分批**：等15–30分钟。16600/16611区域守住并重新突破16770，同时COMEX银不跌破亚洲开盘区间低点，先1/2；突破Opening Range High再加。若AG高开>1.5%而外盘仅平盘，至少等45分钟。

**止损/失效**：16480下方形成接受先减；16200失守且外盘金银同步转弱则失效。

**退出**：TP1 17350；TP2 17800；1–2个交易日不延续退出。最大初始损失0.30%–0.50% NAV。

**合约参数**：上期所白银15千克/手、tick 1元/千克、tick value 15元；按16611名义约249,165元/手。最新检索到的上期所贵金属动态风控公告为涨跌停14%、套保保证金15%、一般持仓16%；券商保证金未确认。repo metadata给出AG2610最后交易日2026-10-15；实物交割，交割月前滚动。按14%静态压力，一板约34,883元/手，两板复合约64,883元/手。

**最坏情景**：美元/实际利率急升、周五金银上冲被证明是短期拥挤，AG高开后Vega与Delta同时回撤；因此不能裸买高IV Call来表达同一方向。

## 八、商品期权专项

今天不能称“全市场最高/最低IV”，只能称8/21代表样本；更重要的是，**所有8/21 option surface在8/24晨间都属于T-1背景，不计fresh evidence**。独立pipeline：360/368 surface-ready、70/368 positioning-ready、0/368 execution-ready，bid/ask coverage=0。

代表样本：AG2610 ATM IV47.265% vs RV20约30.82%，IV-RV约+16.45 vol，RR25 +7.81；FU2611 ATM IV约43.0% vs RV20约37.9%，溢价约5 vol；BU2610 IV约27.75% vs RV20约23.6%，溢价约4 vol；CU2610 IV约14.3%、RR25 +4.14。结论仍是：AG裸Call最不划算；FU若趋势确认后更适合Call Spread；FG若fresh quote恢复后Put Spread比裸空期货更能定义gap风险。

必须回避：AP/CJ/PL/PR/ZC 8/21不合格链的新方向交易；任何基于bid/ask=0推算的“便宜价差”；任何dealer-gamma方向故事。

## 九、9:00开盘风险地图

**FU/BU**：昨天的“偏高开”假设已经下调。07:00附近 Brent Nov约-0.85%、WTI Oct约-0.3%，说明周末制裁headline没有在重开后继续扩张风险溢价。中国周五夜盘缺乏可靠审计价，所以不预测精确gap。FU开盘若>2%不追；3810以下先等；30/45分钟最重要看VWAP、Opening Range、ΔOI和Back是否收窄。

**AG**：外盘金银重开基本平盘；如果AG国内高开>1.5%，先把它当相对过冲而非确认。等15–30分钟；高开越大，等待越接近45分钟。

**FG**：没有高质量外盘锚，政策/地产headline才是gap来源。910–918失败反弹比开盘直接卖更有赔率；若直接低开<895，禁止追空。

**CU**：COMEX铜轻微偏弱、DXY轻微偏强，短线对沪铜不构成追多确认；等待30分钟。

**LC/EC**：两者都属于高动量但证据闭环不足。LC看contango是否收窄；EC至少45分钟后再判断，避免事件gap里的负凸性追价。

## 十、未来24小时 / 7日事件日历（北京时间）

- **8/25 02:00**：美国财政部长Bessent计划说明新一轮伊朗制裁。能源Delta最高；持FU只能保留已定义止损或有限凸性，不应在事件前加满裸Delta。
- **8/25 03:00**：USDA NASS Cold Storage / Chickens & Eggs（8/24 15:00 ET）。肉类、乳品与饲料链二阶影响。
- **8/25 04:00**：USDA NASS Crop Progress（8/24 16:00 ET）。玉米、大豆、棉花天气/作物状况Delta；国内M/RM/Y/P更多是隔夜映射而非直接套利。
- **8/26 22:30**：EIA Weekly Petroleum Status Report。对SC/FU/LU/BU与裂解链是本周最重要定时能源事件。
- **8/27–29**：Kansas City Fed Jackson Hole Symposium，主题为“Financial Innovation: Implications for Payments and Policy”。对美元、实际利率、金银Vega比对工业品更重要。
- **8/29 03:30**：CFTC COT（8/28 15:30 ET），数据基于前一周二持仓，只作滞后拥挤背景。
- **持续监控**：Hormuz通航许可、美国对伊朗二级制裁、中国买家是否受影响、俄乌炼厂/黑海港口袭击。非定时事件优先用减仓与有限风险结构处理，而不是扩大裸Gamma/Delta。

## 十一、风险预算与结论

试仓单笔最大损失0.25%–0.75% NAV；今天没有80+，不使用确认交易0.75%–1.50%的上沿。FU/BU/SC/LU视为同一能源/Hormuz因子，初始合并≤0.75% NAV；AG/AU视为美元-实际利率-贵金属Vega因子；EC与能源存在地缘运输相关性，不能当完全独立风险。

重点压力场景：连续1/2个涨跌停、夜盘gap、保证金上调、Hormuz突然恢复/进一步封锁、IV crush、相关性破裂、人民币急变、中国休市期间海外单边波动。当前regime下，**开盘后确认能力本身比预判方向更值钱。**

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：FU2611回撤确认多；FG701失败反弹空；AG2610回撤确认多；BU2610仅在不持FU时作替代。
C. 今天应继续观察的机会：LC2701价仓强但contango、EC2610极端动量、CU2610挤仓退潮后的skew/价格正常化、Black Sea风险向RM/油脂传导。
D. 今天必须避免或退出的交易：追FU/BU能源高开、追AG高开或裸买高IV Call、低开追空FG、把LC上涨解释成短缺、任何C/D级basis或context-only跨境价差“套利”。

## 来源

- China-Commodities-Engine main：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/contract_meta.json`。
- Reuters, 2026-08-23：[Iran says new sanctions threatened by 'desperate' US will fail](https://www.reuters.com/world/asia-pacific/iran-says-new-sanctions-threatened-by-desperate-us-will-fail-2026-08-23/)。
- Reuters, 2026-08-23：[Gulf markets rise as oil gains lift sentiment](https://www.reuters.com/world/middle-east/gulf-markets-rise-oil-gains-lift-sentiment-2026-08-23/)。
- Reuters, 2026-08-21：[Oil rises as Trump threatens sanctions on Iran partners](https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/)。
- Investing.com, 2026-08-24 early Asia：WTI / Brent / Gold / Silver real-time-derived pages（仅gap proxy，不当官方结算）。
- 隆众资讯 / Mysteel, 2026-08-20：[中国浮法玻璃样本生产厂库库存量周数据分析](https://www.mysteel.com/oilchem/a/26082016/2D4AB63D4A779922.html)。
- SHFE：[燃料油业务细则](https://www.shfe.com.cn/regulation/exchangerules/historicalversion/202508/t20250807_828542.html)；[2026-06-23燃料油风控调整](https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html)；[2025-10-17黄金白银风控调整](https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html)。
- CZCE：[玻璃期货业务细则](https://www.czce.com.cn/cn/uploadfile/2024/01/09/20240109094204181.pdf)。
- EIA：[Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)；USDA NASS：[August 2026 release calendar](https://www.nass.usda.gov/Publications/Calendar/reports_by_date.php?month=08&view=l&year=2026)；CFTC：[COT Release Schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)；Kansas City Fed：[Jackson Hole FAQs](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/)。