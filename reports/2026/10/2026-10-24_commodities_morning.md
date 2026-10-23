# 全球商品期货期权高风险机会雷达｜晨间版｜2026-10-24

> 生成时间 / 信息截点：2026-10-24 06:56:40（北京时间）  
> 最新完整中国日盘：2026-10-23；已完成夜盘：2026-10-23晚—10-24凌晨，依法归属2026-10-26交易日。  
> 周六无中国日盘；下一真实窗口：2026-10-26 09:00（EC 09:30）。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；油链有条件多头价值，但周末闭市且周五夜盘已大涨，须等10月26日回踩与曲线再确认。**

最有价值的三个待验证观察：① SC2612/FU2701在周一回踩后能否维持近月升水；② MA701的+5.28%快照是否能获得实体或同月证据；③ AG2612是否先反抽再失败，而不是在13100附近继续追空。已研究但优势不足：AL、Y、EC、LC；研究机会存在但等待条件：SC/FU/AG；数据不足不能判断：DCE夜盘、全市场期权执行价、所有高质量Physical basis。

## 2. 数据质量与覆盖

| 模块 | 实际取得 | 质量与限制 |
|---|---|---|
| Futures | 2026-10-23；806合约、77产品、五所；原63代码全覆盖，LPG→PG，另14动态品种 | source-date match 100%，full_market_ready=true，critical/invalid/duplicate/unknown=0；5个零价/零量占位已隔离，warehouse carry 5 |
| Market State | 77产品、20个交易日，exact-contract、history complete | roll与部分near-next缺失单列；不同主力不拼连续收益 |
| Physical | 20目标、18 fresh、2 unavailable（SC/LU） | 18个spot-basis全为C级且eligible=false；无独立第二供应商 |
| External | 22目标、17 fresh、5 unavailable | 全部context_only；不当跨境套利报价 |
| Night | T=2026-10-26，start=10-23、end=10-24；416/806合约、37品种 | fresh/validated/published；coverage 51.61%，outside 165、no-trade 11、query_error/unresolved 214；calendar_mismatch=false |
| Night语义 | vendor_latest_trade_asof_snapshot | night_close为兼容别名；official_night_close_verified=false；OHLC/量仓为vendor_realtime_unverified_session_scope |
| Options | 2026-10-23；45/64产品、1050合约；core ATM 44、skew 26 | sampled_strikes；surface/positioning/execution=0，bid/ask覆盖0，full_chain=false；quality limitations中“1.0<0.8”与结构字段冲突，未据此升级 |
| Crosscheck | SHFE238、INE63、CZCE243、GFEX48全部匹配，比较价字段different=0 | DCE HTTP412；未核volume/OI |
| Metadata | contract match 73.45%，multiplier/tick 36.10%，margin/limit 30.15% | SC/FU仓库动态参数缺；静态规格另查交易所，当前动态保证金/限幅仍待核 |
| Stock | ref `795e149866d7f1eefd1efdaf8fe510cd8f1c750e`；trade_date 10-21，research_asof 10-22 | 5568报价可读；复权、行业、execution未就绪；暴露配置4条且无油企映射；限定补证600028/600938无新增经营数字 |

读取路径均在 ref `2d3a2c91041f0ed35ae4e7153f1f92df58d737f7` 下，包括 [report_input](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/report_input_latest.json)、[latest](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/latest.json)、[market state](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/market_state_latest.json)、[physical](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/physical/latest.json)、[external](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/external/latest.json)、[night](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/night_session/latest.json)、[options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/options/quality_latest.json)、[crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/2d3a2c91041f0ed35ae4e7153f1f92df58d737f7/data/crosschecks/futures_latest.json)。前序基准为[10月23日晚报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/9fd68d880ba257b9809eca21cfa046b290f54b08/reports/2026/10/2026-10-23_commodities_evening.json)与[10月23日晨报](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/9fd68d880ba257b9809eca21cfa046b290f54b08/reports/2026/10/2026-10-23_commodities_morning.json)。

全范围实际扫描结论：黑色以SH弱、RB偏弱为主但无高质量实体确认；金属为AG/AU去杠杆与AL修复并存；能化出现唯一全板块异常；新能源LC高波动但无夜盘；农产品Y价仓较强但DCE核验缺口；航运EC 5D大跌但缺同窗运价证据。

## 3. 仪表盘（EOD → 合法Night → 海外）

| 品种/合约 | EOD close/settle | 1D / 5D；RV20；ΔOI | 曲线 | 合法Night snapshot | 海外 / Options | 信号 |
|---|---:|---|---|---|---|---|
| SC/SC2612 | 724.9/717 元/桶 | +2.14% / -0.83%；49.45%；ΔOI +611 | 2612-2701 close +1.13%→night +1.38% | 744.4；+2.69% vs close / +3.82% vs settle；02:30；快照ΔOI +2959 | Brent 116.72结算；repo 117.38 context；ATM IV64.89%，IV-RV +15.44pct；不可执行 | 只等回踩，不追周一高开 |
| FU/FU2701 | 5139/5028 元/吨 | +4.49% / +5.41%；48.81%；ΔOI +20124 | 2701-2702 close +4.03%→night +4.74% | 5349；+4.09%/+6.38%；23:00；快照ΔOI +6048 | WTI 103.27、Brent 116.72结算；ATM IV64.36%，IV-RV +15.55pct；不可执行 | 强但拥挤，旧入场已过 |
| MA/MA701 | 3219/3197 元/吨 | +1.43% / +0.31%；37.95%；ΔOI -45882 | 701-702 close +2.88%→night +3.23% | 3389；+5.28%/+6.01%；23:00；快照ΔOI +39604 | 原油仅间接代理；MA612 ATM IV42.82%，错月 | 价格最强，证据仅2层 |
| PX/PX612 | 9576/9462 元/吨 | +1.52% / +0.40%；33.70%；ΔOI +4655 | 612-701 close +2.33%→night +2.93% | 9974；+4.16%/+5.41%；23:00；快照ΔOI +18404 | 油价成本冲击；10/28到期ATM IV28.42%；夜盘后moneyness已变 | 不追近到期gamma |
| TA/TA701 | 6542/6502 元/吨 | +1.25% / +0.25%；30.62%；ΔOI -12387 | 701-703 close +2.96%→night +3.21% | 6762；+3.36%/+4.00%；23:00；快照ΔOI +23506 | PX/原油共振；TA612错月 | 成本驱动待需求验证 |
| BU/BU2701 | 4650/4600 元/吨 | +2.27% / +2.91%；33.85%；ΔOI +7607 | 2701-2702 close +0.91%→night +1.19% | 4766；+2.49%/+3.61%；23:00；快照ΔOI +5070 | 油链共振；ATM IV37.28%，IV-RV +3.43pct；不可执行 | 确认油链广度 |
| AL/AL2612 | 23350/23200 元/吨 | +0.04% / +1.33%；11.20%；ΔOI +1695 | 2612-2701 close +1.39%→night +1.38% | 23575；+0.96%/+1.62%；01:00；快照ΔOI +5862 | LME铝repo 3040.5美元/吨；ATM IV10.53%，RR25 -2.40pct；不可执行 | 结构尚可、催化不足 |
| CU/CU2612 | 107900/107310 元/吨 | -0.71% / -1.34%；12.01%；ΔOI +2167 | 近月升水但无套利对齐 | 108370；+0.44%/+0.99%；01:00；快照ΔOI +3387 | LME铜repo 14285美元/吨；无执行报价 | 内弱外稳，观察 |
| AG/AG2612 | 13108/13255 元/千克 | -4.16% / -4.56%；33.61%；ΔOI +44 | 2612-2702 close -0.25%→night -0.29% | 13116；+0.06%/-1.05%；02:30；快照ΔOI +2071 | 现货银53.97美元/盎司，日内-1%；ATM IV40.65%，IV-RV +7.03pct；不可执行 | 等待反抽失败 |
| Y/Y2701 | 9125/9080 元/吨 | +1.53% / +2.78%；11.45%；ΔOI +49944 | 仓库pair非当前主力 | DCE query_error，未取得夜盘 | CBOT豆油66.78美分/磅；BMD棕榈4817令吉/吨；不可执行 | 价仓强但核验缺口 |
| LC/LC2701 | 97280/93800 元/吨 | -0.74% / -5.33%；38.31%；ΔOI -10445 | 仓库pair非主力 | 制度无夜盘 | 海外锂链未统一对齐；不可执行 | 高波动、休市观察 |
| EC/EC2611 | 2443/2432 点 | -0.80% / -11.69%；42.53%；ΔOI -2434 | 2610-2611 -8.98%（月份临近/需roll审计） | 制度无夜盘 | 运价/地缘路径未取得同窗指数；不适用 | 跌幅大但缺实体运价核验 |

注：所有Night涨跌均是供应商快照相对10月23日EOD close/settle，不是交易所核验最终夜盘收益；OHLC不用于叙述“先涨后跌”等分钟路径。

## 4. 相比前序的真变化

1. **油链从SC单点变为广谱油化冲击。** MA +5.28%、PX +4.16%、FU +4.09%、TA +3.36%、SC +2.69%、LU +2.63%、BU +2.49%（Night snapshot vs close）。这提高主题置信度，也显著恶化追价赔率。
2. **曲线给出同方向信息。** SC2612-2701由1.13%扩至1.38%，FU2701-2702由4.03%扩至4.74%，MA701-702由2.88%扩至3.23%。均以同一合法会话、准确合约计算。
3. **海外完成确认。** Reuters显示Brent 116.72美元/桶（+3.14%）、WTI 103.27（+3.8%）周五结算；repo连续合约117.38/103.43只作context，差异不拼成套利。
4. **贵金属没有给出新的低位追空赔率。** AG EOD -4.16%，但Night仅较close +0.06%；现货银周五约-1%。旧反抽区未观察到，继续等反抽失败。
5. **期权数据更新但执行性仍为零。** 45/64、ATM44、skew26均可做局部研究；bid/ask=0、execution=0，且Night后SC/FU/PX的moneyness已变，不能把EOD面当周一报价。
6. **旧计划处置。** SC旧727.5—731、FU旧5085—5130窗口均被越过；OHLC不能证明触发先后、成交或盈利。本期不是“上移止损”，而是旧执行方案失效后建立新的周一候选。

## 5. 产业链与传播

| 链条 | 最强 / 最弱 | 曲线与量仓 | 实体 / 期权 / 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 中东供应/航运→Brent/WTI→SC→FU/LU/BU→PX/TA/MA | MA、FU、PX / SC相对涨幅最低但曲线更干净 | SC/FU/MA/PX近月升水扩大；SC/FU/MA快照OI增 | 海外油价强；SC/FU IV高于RV且无执行 | SC/LU Physical不可用，其余basis C | 中—高 |
| 高油价通胀→利率预期→AU/AG | 无合格做多；AG最弱 | AG近月轻贴水 | 金银周五续弱；AG IV-RV +7.03pct | 中国现货需求与可成交期权 | 中 |
| LME→SHFE有色 | AL / NI | AL曲线+1.38%，快照OI增 | LME repo支持；AL局部IV略低于RV | Physical basis C、跨境对齐 | 中低 |
| CBOT/BMD→Y/P/M→养殖 | Y / LH | Y ΔOI +49944 | 海外油脂context | DCE夜盘与官方crosscheck | 低 |
| 铁矿/煤焦→钢材→EC | 无 / SH、EC | EC临近月roll风险 | 无合格实体运价 | 仓单/需求/运价同窗 | 低 |

**公司利润桥：** 中国海油的上游售价对油价更直接，中国石化同时承受原料成本、库存损益、裂解价差、长协与套保。10月23日官方公告只新增三季报说明会通知/董事会事项，没有产量、炼化毛利或套保数字；因此股票既未为商品第三层补证，也不比SC/FU直接表达更优。下一验证是10月30日前后的中国海油三季报与油企经营数据。

## 6. 统一机会榜

| 排名 | idea_id | 方向/期限/阶段 | 逻辑/赔率/催化/价曲波/拥挤 | 总分 | 五层支持 | 研究 / 证据 / 执行 |
|---:|---|---|---:|---:|---|---|
| 1 | `COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021` | SC2612 条件多；1—5D；等待周一回踩确认 | 22/17/19/15/4 | 77 | 3/5层支持 | 看多研究成立但明显追价风险 / 3/5层支持 / closed_market_and_trigger_not_met |
| 2 | `COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022` | FU2701 条件多；1—5D；等待周一回踩确认 | 21/16/18/15/5 | 75 | 3/5层支持 | 紧张曲线支持延续但过度伸展 / 3/5层支持 / closed_market_and_old_entry_passed |
| 3 | `COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024` | MA701 等待确认后多；1—3D；研究卡 | 19/15/15/14/5 | 68 | 2/5层支持，分数封顶≤69 | 方向假设，错价尚未证实 / 2/5层支持，分数封顶≤69 / not_execution_ready |
| 4 | `COM-M-AG2612-SILVER-REPAIR-LONG-20261021` | AG2612 只等反抽失败再空；1—5D；观察 | 19/15/15/13/3 | 65 | 2/5层支持 | 趋势偏空但禁止低位追 / 2/5层支持 / wait_for_rebound_failure |
| 5 | `COM-M-AL2612-CURVE-LONG-WATCH-20261024` | AL2612 偏多观察；3—10D；观察 | 18/14/13/13/5 | 63 | 3/5层支持但赔率不足 | 有结构线索但催化不足 / 3/5层支持但赔率不足 / observe_only |

分数是研究优先级，不是胜率。MA与AG仅2层支持，严格受69分上限；AL虽3层但催化/赔率不足。没有80+候选。

## 7. 研究 / 交易卡

### 7.1 SC2612｜`COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021`｜77分

- **新增事实→定价→分歧：** Night snapshot 744.4、较close +2.69%，曲线升水扩至1.38%，Brent 116.72。市场已经计入相当一部分供应冲击；我们的分歧只在“回踩后近月紧张是否仍保留”，不是继续追首跳。
- **触发顺序（仅10月26日）：** 09:15仍≥742 **AND** Brent最新可核报价≥114 **AND** SC2612-2701同窗升水≥1.20%；随后必须**先**回踩738—744，再出现5分钟收盘≥746。满足后按30%/70%在744—748；开盘≥760或无回踩直冲则放弃。
- **风险/退出：** 价格止损732；Brent<110或升水<0.70%持续15分钟为逻辑失效。TP1 766减50%，TP2 788；10月30日14:45时间退出。
- **可达性与R：** 好/中/坏入场744/746/748，至732风险1.2/1.4/1.6万元/手；TP1毛R 1.83/1.43/1.13，TP2 3.67/3.00/2.50。手续费/滑点未知，未当0。
- **合约：** 1000桶/手，tick0.1元=100元/手；仓库last trading day 2026-11-30。动态保证金/限幅10月26日再核；每1元不利变动=1000元/手。
- **期权：** 11月12日到期、EOD ATM720、IV64.89%；Night后ATM/Delta已变且无bid/ask，不能作为已报价限损结构。
- **压力：** 周末gap、1/2动态限幅、保证金上调、流动性消失、交割月逼近。试仓NAV 0.50%，确认后≤1.00%；油链合并≤1.50%。

### 7.2 FU2701｜`COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022`｜75分

- **新增事实→定价→分歧：** EOD结算+4.49%、ΔOI +20124；Night 5349、较close +4.09%，2701-2702升水4.74%。旧5130方案已完全失效。
- **触发顺序：** 10月26日先回踩5300—5350，随后5分钟收盘≥5360 **AND** 同窗升水≥4.50% **AND** Brent≥114；按40%/60%在5350—5380。首个可成交价≥5420或价差<4.0%则放弃。
- **风险/退出：** 止损5190；价差<3.5%持续15分钟或Brent<110逻辑失效。TP1 5600减50%，TP2 5850；10月29日14:45时间退出。
- **R：** 5350/5365/5380入场，风险1600/1750/1900元/手；TP1毛R 1.56/1.34/1.16，TP2 3.13/2.77/2.47。
- **合约：** 10吨/手、tick1元=10元/手；合约文本静态最低保证金8%、涨跌停5%，但当前动态参数未核；last trading day 2026-12-31，实物交割。
- **期权：** 12月18日到期、EOD ATM5000、IV64.36%；Night后moneyness已变、零bid/ask。
- **风险预算：** 试仓NAV 0.35%，确认后≤0.75%，与SC/LU/BU/PX共同因子合并≤1.50%。

### 7.3 MA701｜`COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024`｜68分｜研究卡

- **新增事实：** Night +5.28%、快照ΔOI +39604，701-702升水2.88%→3.23%。
- **为何未证实错价：** 现货basis为C级；原油只是间接代理；期权underlying是MA612而非MA701。
- **研究闸门：** 先回踩3300—3340，再15分钟收盘≥3380 **AND** 701-702升水≥3.0% **AND** PX/TA均保留≥2%相对周五close。即使价格满足，实体或同月证据未补齐仍不执行。
- **仅供可达性核算的假设框架：** 若未来放行，3380—3400、stop3290、TP3530/3670；毛R约1.18—1.67 / 2.45—3.22。它不是当前报价或挂单。
- **合约：** 10吨/手、tick1元=10元/手；仓库静态margin7%、limit6%，last trading day 2027-01-14；night_session元数据缺失，下单前复核。若未来放行，试仓≤NAV0.25%。

## 8. 商品期权专项

样本是2026-10-23 EOD的core_v1 / sampled_strikes，共45个series、1050合约；ATM ready 44、skew ready 26，完整曲面/positioning/execution均为0。SC ATM IV64.89%对RV49.45%（+15.44pct），FU 64.36%对48.81%（+15.55pct），AG 40.65%对33.61%（+7.03pct）：这是波动溢价观察，不证明“贵得可卖”。AL局部ATM IV10.53%略低于RV11.20%、RR25 -2.40pct；PX ATM IV28.42%低于RV33.70%，但10月28日近到期且Night后标的跳升，旧Delta/ATM不可用。

结构备选仅能写为“待询价”：SC/FU call spread的最高净支出必须由账户风险预算倒推，并在真实bid/ask、到期、两腿同窗报价、行权交割核实后才有限损。禁止从样本OI推PCR/crowding/dealer gamma；禁止单月外推term/wing。

## 9. 下一开盘风险地图

周六没有9:00日盘。下一真实窗口是**2026-10-26 09:00**（EC 09:30）。

| 三层 | 已知 | 风险 | 10月26日动作 |
|---|---|---|---|
| Previous China EOD | 油链已强，FU/LU单日约+4.5%；AG -4.16% | 已有高波动和拥挤 | 不用周五结算追价 |
| Current T Night | 油化广谱+2.5%—+5.3%，SC/FU/MA近月升水扩大 | 仅vendor snapshot，且周末新闻gap未计入 | 09:00不追；09:15看留存，09:30看回踩，09:45才确认 |
| Overseas close | Brent/WTI强收；金银续弱 | 周末供应正常化或升级都可制造大gap | 重新核实Brent、运费/保险和周末事件 |

潜在高开：SC/FU/LU/BU/PX/TA/MA；平开/冲突：AL/CU；低开风险：若周末地缘降温则油链反向，AG/AU则取决于美元/利率。DCE夜盘缺失，Y/M/P/LH不因缺数据受罚，但不升级执行。

## 10. 未来24小时 / 7日事件与行动前缺口

- **未来24h：** 中东、海湾出口、油轮/保险与战略储备消息。中国闭市；按油链统一主题做周末gap和相关性断裂压力，不创建仓位。
- **10月26日：** 中国下一日盘；USDA Crop Progress。谷物只有异常天气/进度才改Delta。
- **10月27—28日：** 美联储议息；贵金属降低裸Delta/Vega，FedWatch不是本报告胜率。
- **10月28日22:30附近：** [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)常规发布时间；SC/FU不跨数据裸追。
- **10月29日：** 美国PCE；复核美元、实际利率与AU/AG。
- **10月30日：** CFTC下一COT、EIA Petroleum Supply Monthly、中国海油三季报/说明会窗口；COT只反映截至周二持仓，不是dealer gamma。

行动前必须补：周一精确盘口与同窗curve、DCE夜盘/官方crosscheck、SC/FU/MA动态margin/limit、期权bid/ask及新ATM/Delta、SC/LU实体数据、用户NAV与实际成交/持仓回执。发布校验：五项分数重算通过；SC/FU/MA exact curve通过；情景R与乘数重算通过；周六/周一日历通过；JSON/Markdown/四行行动清单同源；未解决项未报通过。

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：10月26日SC2612、FU2701先回踩再收复且近远月升水/Brent同步；MA701仅研究，不执行。  
C. 今天继续观察：AG2612反抽失败、AL2612曲线、Y2701价仓、LC/EC高波动及油企三季报利润桥。  
D. 今天必须回避或有条件退出：周一油品高开追涨、13100附近追空AG、把vendor snapshot当官方夜盘收盘、用零bid/ask期权或错月MA612替代MA701；若旧计划曾成交，按原规则独立管理，不倒推持仓。
