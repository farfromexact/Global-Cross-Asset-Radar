# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-21

> 数据截点：北京时间2026-08-21 19:31。中国日盘已结束，21:00夜盘尚未开市。本报告仅用于研究和交易决策支持，不自动下单。中国EOD与15:00后海外信息严格分开：海外变动只作为21:00开盘映射，不写成“中国期货已经上涨/下跌”。

## 一、今日一句话结论

**有条件化机会，但没有应在19:30立即下的新仓：白银是今晚最强映射，FU仍有最干净曲线确认，FG重新出现价跌仓增+Contango；全部等待夜盘15–45分钟确认。**

今天值得新增的是**试仓风险**，不是追价风险。前三名均达到70分，但没有80分以上确认交易：AG2610条件多79，FU2611回撤条件多77，FG701失败反弹条件空74。能源不再像昨日那样具备海外同步加速：17:49 BJT附近Brent/WTI当日约-0.5%，但周度仍分别约+5.4%/+4.8%；相反，17:21 BJT附近海外白银约+2.6%、黄金约+1.6%，美元偏弱，使贵金属成为21:00最值得观察的gap主题。

## 二、数据质量与覆盖说明

- 实际优先读取：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需读取`data/latest.json`、`data/physical/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`。
- `report_input_latest.json`：requested_date=`2026-08-21`，generated_at=`2026-08-21T19:02:52.405697+08:00`。
- 核心Futures：2026-08-21，SHFE/INE/DCE/CZCE/GFEX五所齐全，`full_market_ready=true`，`source_date_match_pct=100%`，803个合约；unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、placeholder=5，critical module errors=0，核心期货carried-forward=0。
- Market State：同一具体合约计算1D/3D/5D/20D，未拼接主力；部分较老历史源日期只用于历史窗口，不冒充当日。
- Physical：20个目标中可验证4个。FG企业库存为2026-08-21周度最新水平7441.4重量箱，但本次未验证方向变化，因此只作context，不计完整Physical方向层；JM现货为2026-08-10旬度最新值1908.3元/吨，basis质量C，仅作context；铁矿港口库存值/单位仍需QA；TA加工费为周度水平。
- External仓库EOD层整体`data_fresh=false`，因此不拿旧EOD冒充19:30实时；晚间海外另用Reuters等公开来源补充。
- Options：T日数据已并入统一报告。21816条记录，59/64品种覆盖，368个series；其中360个`surface_ready=true`，70个`positioning_ready=true`，**0个`execution_ready=true`**。全链bid/ask覆盖为0，因此只能使用已验证ATM IV、RR25、BF25、期限结构做研究，不给虚构权利金、成交滑点或“可按某净价成交”的结构。独立`surface_latest.json`本次为空/与统一汇总层不一致，按v2优先级采用`report_input`的per-series状态。
- Contract metadata：官方部分字段可得，但multiplier/tick/night/margin/limit并非仓库全量完备；前三交易卡缺项用交易所公开规则补充，券商保证金均未确认。
- 不能闭环的产业链：大多数现货基差/仓单、进口平价、裂解/加工利润、精确海外同月价差、会员排名；因此不存在可执行的境内外套利结论。

## 三、商品仪表盘

| 板块 | 品种/主力 | 日盘有效价 | 1D/5D结算变化 | Volume / OI | ΔOI | Curve | Physical/Basis | T日期权 | 信号 |
|---|---|---:|---:|---:|---:|---|---|---|---|
| 贵金属 | AG2610 | close 16771 / settle 16611 | +3.11% / +5.45% | 773038 / 306822 | +4403，+1.46% | 轻微Contango，样本仅4 | 无完整实体层 | ATM IV 47.27%，RR25 +7.81，BF25 +1.93；surface=Y,pos=N,exec=N | **强，但IV明显高于RV，不追首跳** |
| 能源 | FU2611 | 3845 / 3850 | +2.12% / +9.81% | 650637 / 285614 | +22573，+8.58% | Backwardation +7.47%，z=+1.70 | 无 | ATM IV 43.00%，RR25 -1.22；surface=Y,pos=N,exec=N | **价/量/OI/曲线最整齐** |
| 能源 | BU2610 | 4508 / 4526 | +2.14% / +7.92% | 486111 / 334627 | -2643，-0.78% | Backwardation +3.16% | 无 | ATM IV 27.75%；surface=Y,exec=N | 趋势强但价涨仓减，降级 |
| 建材 | FG701 | 907 / 906 | -1.09% / -3.10% | 1575371 / 1601238 | +148375，+10.21% | Contango -3.35% | 周度企业库存7441.4重量箱，仅水平context | ATM IV 23.06%，RR25 +7.72；surface=Y,pos=Y,exec=N | **价跌仓增+Contango，空头观察恢复** |
| 新能源 | LC2701 | 158680 / 156360 | +2.60% / +1.41% | 225444 / 353437 | +31875，+9.91% | Contango -0.30% | 缺 | ATM IV 35.37%；surface=Y,exec=N | 高活跃上涨但curve否定短缺叙事 |
| 化工 | MA610 | 2909 / 2880 | close +2.83% | 1957108 / 873688 | — | Backwardation | 缺 | series可用但exec=N | 跟随能源/化工强势，等海外原油确认 |
| 化工 | EG2610 | 5202 / 5159 | close +2.02% | 546862 / 272984 | — | Backwardation | 缺 | exec=N | 价格与curve同向，但产业闭环不足 |
| 农产品 | RM611 | 2238 / 2246 | -1.36%结算 / 3D +0.67% | 747569 / 651265 | — | Backwardation +3.96% | 缺 | surface=Y，部分series positioning ready；exec=N | 价格与curve冲突，不做追空 |
| 农产品 | M2701 | 3228 / 3244 | close -1.10% | 1390344 / 2467335 | — | Contango | 缺 | surface大多可用；exec=N | 偏弱但外盘/进口平价未闭环 |
| 软商品 | CJ701 | 8145 / 8140 | close -1.21% | 161081 / 173096 | — | Contango | 缺 | — | 弱，但不足以升级为交易 |
| 能源化工 | SP2611 | 4892 / 4848 | close +3.42% | 535700 / 260902 | — | Contango | 缺 | — | 单日强但curve不确认 |

注：curve均为仓库定义的“近月—次近月期货曲线”，**不是现货基差**。价格/OI四象限只作为归因线索，不写成确定的新多/新空事实。

## 四、相比上一交易日真正变化

1. **能源从“海外同步加速”变成“国内趋势强、海外短线停顿”**：FU日盘结算+2.12%、5D+9.81%，BU+2.14%；但17:49 BJT附近Brent 93.28、WTI 86.39，日内均约-0.5%。昨日的追涨映射因此不再成立，今晚只买回撤确认。
2. **白银成为最强跨时段映射**：AG2610日盘结算+3.11%、close+4.10%，OI+1.46%；17:21 BJT海外银价再约+2.6%，与弱美元背景同向。但AG ATM IV 47.27%对RV20 30.82%，vol premium约+16.45pts，裸买波动率并不便宜。
3. **FG重新转弱且仓位活跃**：FG701结算-1.09%，ΔOI +10.21%，Contango约-3.35%；这比昨日“减仓反弹、空头确认衰减”明显更接近二次做空触发。
4. **LC价格与仓位急升但curve仍是Contango**：结算+2.60%、ΔOI近+9.91%，volume/OI与z-score显著活跃；但期限结构没有短缺确认，不能把上涨解释为供给紧张。
5. **Options层发生质变**：昨日全局曲面不可用；今天统一报告已有360个T日surface-ready series，可把期权作为第5层研究证据。但bid/ask仍为0、execution-ready仍为0，执行层仍未打开。

## 五、产业链地图

| 链条 | 方向 | 最强/最弱 | Price/Curve | 实体 | Options | 海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|
| 贵金属 | 偏多但高波动 | AG最强 | price强、curve不确认 | 缺 | surface ready；AG IV昂贵 | 银+2.6%、金+1.6%、美元偏弱 | 精确19:30银价/人民币/可执行quote | 高 |
| 能源炼化 | 中期偏多、短线分歧 | FU最强，BU次之 | FU backwardation强；BU价涨仓减 | 缺 | surface ready、exec false | 原油周度强、当日约-0.5% | 现货裂解/进口平价 | 中高 |
| 建材/黑色 | 偏弱 | FG最弱 | FG价跌仓增+Contango | 库存只有水平context | FG surface/positioning ready，exec false | 无直接海外锚 | 库存方向/需求/仓单 | 中高 |
| 新能源材料 | 高波动反弹 | LC强 | 价格强、Contango反证短缺 | 缺 | surface ready | 无可靠实时进口平价 | 库存/排产/成本 | 中 |
| 油脂饲料 | 分化 | RM/M偏弱 | curve冲突 | 缺 | surface可研究 | 未拿到可执行进口平价 | CBOT/BMD同月和压榨链 | 中低 |

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段 | 工具 | 新鲜证据层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| 1 | AG2610 夜盘回撤条件多 | **79** | 多，1–5D | 条件试仓 | 期货；或手工核价后的Call Spread | 3：价格/OI、海外宏观、T日期权 | curve不确认；Physical缺；exec=false；IV贵 |
| 2 | FU2611 夜盘回撤条件多 | **77** | 多，1–5D | 条件试仓 | 期货；或手工核价后的Call Spread | 3：价格/OI、curve、T日期权 | 海外原油当日轻微回落；Physical缺；exec=false |
| 3 | FG701 失败反弹条件空 | **74** | 空，1–5D | 条件试仓 | 期货；或核价后的Put Spread | 3：价格/OI、curve、T日期权 | Physical只有水平；当前保证金/限价未独立确认 |
| 4 | BU2610 能源趋势续涨 | **72** | 条件多，1–5D | 挂条件单 | 期货 | 3：价格、curve、T日期权 | 价涨仓减；海外原油不再加速 |
| 5 | LC2701 高活跃续涨 | **68** | 观察多，2–10D | 观察 | 期货/核价后Call Spread | 2：价格/OI、T日期权 | Contango反对短缺；无Physical/实时海外锚 |

评分拆分：AG 22/18/17/12/10；FU 21/18/16/13/9；FG 21/18/14/12/9；BU 20/17/15/11/9；LC 18/17/13/10/10（逻辑/赔率凸性/催化/价格曲线或vol/拥挤技术）。没有80+，所以没有“确认交易”。

## 七、前三名交易卡

### 1) AG2610｜条件多｜79

**事实**：close 16771、settle 16611；5D结算+5.45%；OI +4403；17:21 BJT附近海外银价约+2.6%。T日2026-09-23期权series：ATM 16600，ATM IV 47.265%，RR25 +7.81，BF25 +1.93，surface-ready=true，positioning-ready=false，execution-ready=false。**市场定价**：趋势强且跨市场映射继续向上，但vol已显著溢价。**推断**：如果21:00首跳回撤后仍守住16600/16611，并重新接受16770上方，说明国内并未一次性price-in海外银价涨幅。**主观判断**：这是今晚最值得冒险的主题，但最不值得追开盘第一根K。

- 入场：21:00后至少等15–30分钟；16600/16611区域不被有效跌破，回撤结束后重新站稳16770附近；海外银价不出现明显反转。
- 分批：首次1/3风险；只有30–45分钟后价格仍在VWAP上方/重新创新高才加第二笔。
- 初始止损：30分钟接受于16600下方，且海外银价回吐大部分欧洲时段涨幅；或日盘低点16201方向快速失守则直接放弃。
- TP1：+1R减仓；TP2：+2R或移动止盈；若IV继续上升而期货不创新高，优先锁利润。
- 时间止损：1–2个夜/日盘没有新高则撤。
- 最佳表达：执行层未ready时优先期货小试；若手工确认逐strike报价与深度，考虑2026-09-23 Call Spread，长腿约35–45Δ、短腿约15–25Δ；**不写精确执行价与净权利金**。
- 最大损失：初始0.40%–0.60% NAV；期权若使用，最大损失=实际确认净支出，未核价前不下单。
- 合约参数：15kg/手；tick 1元/kg，tick value 15元/手；按close名义约251,565元/手。SHFE最近可核实调整：涨跌停14%、一般保证金16%、套保15%，券商保证金未确认。夜盘21:00–02:30。最后交易日按规则为交割月15日，即AG2610为2026-10-15；实物交割。
- 压力：1个14%涨跌停约35,219元/手；连续两个同方向14%复合约75,4xx元/手，未计滑点/保证金上调。
- 放弃：高开>约2%后无回撤承接；美元快速反弹；海外银价转跌；AG 30分钟内跌回16600下方。

### 2) FU2611｜条件多｜77

**事实**：close3845、settle3850；1D结算+2.12%、5D+9.81%；ΔOI +8.58%；near-next backwardation +7.47%，z=+1.70；T日2026-10-19期权ATM IV 43.0%，对RV20 37.93%约+5.07pts，surface-ready但execution-ready=false。海外原油17:49 BJT附近Brent/WTI当日约-0.5%，但周度仍强。**推断**：方向逻辑未死，但“海外加速→国内gap追涨”条件已经消失，今晚只有回撤确认才有赔率。

- 入场：21:00后等30–45分钟；FU守住3810–3850主要日盘支撑区，重新接受3850上方；backwardation不明显压缩；Brent不继续加速下跌。
- 初始止损：有效跌破3810且curve压缩，或Brent跌幅扩大并拖累国内。
- TP1：+1R；TP2：+2R，或backwardation较当前压缩约1/3时主动退出。
- 时间止损：2个交易时段无延续即撤。
- 最大损失：0.35%–0.50% NAV；FU+BU视为同一能源/地缘因子，初始合计≤0.75% NAV。
- 期权替代：若手工确认报价，可考虑有限风险Call Spread；当前IV并不便宜，且execution=false，不给精确权利金。
- 参数：10吨/手；tick 1元/吨，tick value 10元/手；settle名义约38,500元/手。SHFE 2026-06-23通知对应FU2611：涨跌停14%、一般保证金16%、套保15%，券商保证金未确认。夜盘21:00–23:00。最后交易日为交割月前一月最后交易日；具体2026-10日历日需交易所日历复核。实物/保税燃料油交割。
- 压力：1个14%约5,390元/手；连续两个复合约11,535元/手。
- 放弃：21:00高开但30分钟内跌回日盘区间；Brent明显扩大跌幅；curve快速走平。

### 3) FG701｜条件空｜74

**事实**：close907、settle906；1D结算-1.09%、5D约-3.10%；ΔOI +10.21%；near-next Contango约-3.35%；周度企业库存7441.4重量箱为当周最新水平，但没有可验证方向变化，因此不计Physical方向层。T日2026-12-11期权ATM910、ATM IV23.055%、RR25 +7.72、BF25 +1.315，surface-ready=true、positioning-ready=true、execution-ready=false。**推断**：价跌仓增+Contango使“终端弱势/供给压力”交易重新接近触发，但必须防止900附近短线挤压。

- 入场：21:00后等至少30分钟；反弹到910–918区域失败，不能重新站稳昨日结算916/今高918，且期限结构未明显收敛时试空。
- 止损/失效：30分钟有效站稳920上方，或Contango显著收窄同时价格转强。
- TP1：899日盘低点；TP2：880附近或+2R，以先到者为准。
- 时间止损：2个交易日不破899则退出。
- 最大损失：0.25%–0.40% NAV。
- 期权替代：若逐strike报价确认，可用Put Spread限制gap风险；execution=false，当前不提供权利金/具体strike成交建议。
- 参数：CZCE玻璃20吨/手；tick 1元/吨，tick value20元/手；按settle名义约18,120元/手；夜盘21:00–23:00；最后交易日为交割月第10个交易日，FG701具体日历日应在进入交割月前复核；实物交割。交易所合约基准参数曾为最低保证金5%、涨跌停±4%，但**本次未找到足以确认FG701当前动态风控参数的最新专项通知，因此正式执行参数标记未确认**，不得拿基准参数替代当前限价/保证金。
- 放弃：开盘直接跌破899后追空；反弹站稳920；需求/库存出现新的可验证反向变化。

## 八、商品期权专项

今天期权研究层比昨日明显改善，但**执行层仍关闭**。全市场不能声称“最高/最低IV”，因为执行流动性与全series比较未做完；以下只是代表样本：AG2610 ATM IV47.27% vs RV20 30.82%（+16.45pts）；FU2611 43.0% vs 37.93%（+5.07pts）；FG701 23.06% vs 16.20%（+6.86pts）；LC2701 35.37% vs 27.19%（+8.18pts）；BU2610 27.75% vs23.63%（+4.11pts）。

结论：贵金属方向最强，但**裸买AG Vega并不便宜**；若看多，Call Spread优于直接买ATM Call的结构逻辑更好，但必须在21:00后手工确认bid/ask、深度和执行价。FG可用Put Spread替代裸空期货以限制gap；FU可用Call Spread限制地缘反向gap。所有series execution-ready=false，因此不做净权利金、精确交易成本或Dealer Gamma推断。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国日盘结算 | 15:00后海外映射 | 预期开盘 | 置信度 | 是否追价 | 等待 | 开盘后最重要确认 |
|---|---:|---|---|---|---|---|---|
| AG2610 | 16611 | 17:21 BJT银约+2.6%、金约+1.6%，美元偏弱 | 偏高开 | 中高 | **否** | 15–30m | 16600/16611承接、16770再接受、海外银不反转 |
| AU2610 | — | 金约+1.6% | 偏高开 | 中高 | 否 | 15–30m | 海外金/DXY、首跳承接 |
| FU2611 | 3850 | 17:49 BJT Brent/WTI当日约-0.5%，但周度强 | 平至小低/分歧 | 中 | 否 | 30–45m | 3810–3850、backwardation、Brent是否止跌 |
| BU2610 | 4526 | 原油短线偏弱 | 平至小低 | 中 | 否 | 30–45m | 4526附近接受、curve、原油 |
| FG701 | 906 | 无直接海外锚 | 平/偏弱 | 中低 | 否 | 30m | 910–918反弹是否失败、OI与curve |
| MA610/EG2610 | 2880/5159 | 原油影响间接且当日偏弱 | 混合 | 低中 | 否 | 30–45m | 自身curve与首30m成交/OI |
| LC2701 | 156360 | 无可靠实时进口平价；本次未确认GFEX夜盘 | **夜盘安排未确认** | — | — | — | 下一确定窗口按2026-08-24 09:00处理 |

特别纪律：AG若高开太多不要把海外+2.6%简单外推为国内还应涨2.6%；FU若反而高开，也不要把周度原油强势当成追涨许可。今晚最重要的是**gap acceptance而不是gap direction**。

## 十、未来24h / 7d事件日历（北京时间）

- 2026-08-22 03:30：CFTC COT，发布周二持仓快照；只作仓位背景，不当作实时持仓。
- 2026-08-26 22:30：EIA Weekly Petroleum Status Report（常规周三10:30 ET），直接影响SC/FU/LU/BU与裂解逻辑；若能源多头已有利润，数据前宜降低Delta。
- 2026-08-27至29：Jackson Hole Economic Policy Symposium，主题“Financial Innovation: Implications for Payments and Policy”；贵金属/美元/利率Vega在会期前后可能放大，避免无保护裸卖vol。
- 持续：美国对伊朗施压、Hormuz运输受扰、俄炼厂扰动；能源主题必须把FU/BU/SC/LU合并算同一地缘因子。
- 持续：美元与长端美债波动；AG/AU不应把“贵金属多”和“弱美元多”误当两个独立风险预算。

## 十一、风险预算与今天必须回答的结论

- 是否值得新增风险：**值得，但只有条件试仓，不值得19:30或21:00首跳追价。**
- 最强/最弱产业链：最强是贵金属跨时段映射；国内结构最强是FU；最弱是FG建材。
- 当前regime：贵金属外盘加速 / 能源高位分歧 / 建材弱势重新增仓 / 新能源高波动反弹 / 混合高波动。
- Price是否获curve确认：FU是；FG空头方向是；AG不是；LC多头不是。
- 是否获库存/实体确认：多数**没有**；FG仅有库存绝对水平context，不能自动算确认。
- 境内外是否同向：AG是；能源今天短线不是；LC无可用跨市场锚。
- 人民币/美元：弱美元支持贵金属；未取得19:30可审计USD/CNH同口径报价，不量化人民币贡献。
- 期权是否优于裸期货：结构上可降低gap风险，但execution-ready=false；只有手工核价后才能判断真实优劣。
- 跨期/跨品种/跨市场RV：目前没有满足可执行口径对齐的正式套利。
- 单日噪音：SP单日+3.4%但Contango；LC单日强但curve不确认短缺。
- 等30–45分钟：FU、BU、FG、MA/EG；AG至少15–30分钟。
- 不值得交易：追首跳、裸卖商品Vega、把C级basis/库存绝对水平写成套利、在无bid/ask时虚构期权价格。

风险预算：单一试仓最大损失0.25%–0.75% NAV；本晚AG建议0.40%–0.60%，FU0.35%–0.50%，FG0.25%–0.40%。三主题若全部触发，初始合并风险不超过约1.0%–1.25% NAV；能源主题FU+BU初始合并≤0.75%。单一高确信主题总风险仍≤2.5%–3.0%。压力测试至少包括1/2个涨跌停、夜盘gap、相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、人民币急变与中国休市时海外大幅波动。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：AG2610回撤确认多、FU2611回撤确认多、FG701失败反弹确认空；全部等首15–45分钟。
C. 今天应继续观察的机会：BU2610能源趋势、LC2701高活跃上涨但Contango、RM/M价格与curve冲突。
D. 今天必须避免或退出的交易：21:00追首跳、把AG强势直接等同于便宜Call、在execution-ready=false时硬做精确期权结构、把C级basis/库存水平当套利、FU/BU重复加同一能源因子。

## 来源

- China-Commodities-Engine：<https://github.com/farfromexact/China-Commodities-Engine>
- Reuters，2026-08-21 Oil：<https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/>
- Reuters，2026-08-21 Gold/Silver：<https://www.reuters.com/business/gold-steadies-heads-third-straight-weekly-gain-2026-08-21/>
- SHFE FU风险参数通知（2026-06-23）：<https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html>
- SHFE黄金白银风险参数通知（2025-10-17）：<https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html>
- SHFE燃料油业务细则：<https://www.shfe.com.cn/regulation/exchangerules/historicalversion/202508/t20250807_828542.html>
- CZCE玻璃业务细则：<https://www.czce.com.cn/cn/uploadfile/2024/01/09/20240109094204181.pdf>
- CFTC COT release schedule：<https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm>
- EIA WPSR schedule：<https://www.eia.gov/petroleum/supply/weekly/schedule.php>
- Kansas City Fed Jackson Hole FAQ：<https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/>
