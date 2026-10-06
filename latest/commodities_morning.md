# 全球商品期货期权高风险机会雷达（晨间版）

- 报告日期：2026-10-07
- 生成/信息截点：2026-10-07 07:00 北京时间
- edition：`commodities_morning`
- prompt_version：`radar_2026-09-06_coverage_v1`
- data_protocol_version：`china_commodities_v2`
- 中国市场状态：国庆休市；最近完整交易日为2026-09-30；下一集合竞价为2026-10-08 08:55—09:00，下一日盘09:00，下一夜盘2026-10-08 21:00（归属10月9日交易日）
- 免责声明：research only; manual quote and manual confirmation required before execution; no premium quoted

## 一、今日一句话结论

> **截至本报告时点，无可立即执行的合格新交易。SICOM新结算强化RU，但原油跌破100后收复、贵金属及原糖反弹；10月8日只交易开盘后确认，不押第一跳。**

研究机会存在但等待条件/报价：RU2701回踩多、SC2611反弹失败空、柴油物流相对价值。已分析但优势不足：OI701、SR701、BR2611、贵金属反弹。数据不足、暂时无法判断：中国期权实际成交成本、DCE期权定位、精确进口平价及实时加工利润。

## 二、数据质量、时间语义与覆盖

### 2.1 实际读取与状态

| 模块 | 实际路径 | requested/source | generated | 状态与用途 |
|---|---|---:|---:|---|
| 统一输入 | [report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) | 2026-09-30 | 2026-10-06 08:13 BJT | ok，schema v2；同一repo ref的统一只读层 |
| Futures | report_input + [root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) | 2026-09-30 | last-good 10/1；假期任务10/6 08:08 | 806合约、77产品、五所齐全；last-good full_market_ready=true、source-date match 100%、critical errors=0；6条占位OHLC排除 |
| Market State | report_input.products | 2026-09-30 | 2026-10-06 08:08 | 77产品同合约1D/3D/5D/20D、OI与curve已扫描；假期无新增 |
| Physical | report_input.physical | 2026-09-30 | 2026-10-01 08:12 | 20组目标、18组carried_forward；SC/LU缺失；basis均C或缺失，只作context |
| External（日频） | report_input.external | 2026-10-05 | 2026-10-06 08:13 | 17/22 fresh、validated、published；全部context_only；另联网更新10/6海外收盘 |
| Night Session | report_input + [night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) | 尝试trading_date=2026-10-06、night_session_date=10-05 | 2026-10-06 08:03 | data_fresh=false、validation=false、published=false、coverage_complete=false；假期本就无应有夜盘，不作错误行情 |
| Options | report_input.options | 2026-09-30 | 2026-10-01 00:03 UTC | 14,468记录、196 series；surface 192、positioning 47、execution 0；bid/ask覆盖0 |
| Contract Metadata | report_input.contract_metadata | 2026-09-30 | 2026-10-01 | partial；contract match 67.49%、effective 73.45%，动态margin/limit等约30.15% |

Night质量计数：selected/requested 806；night-session contracts 0；outside-window 592；no-night-trade 0；missing timestamp/price/quote均0；query error与unresolved各214；previous_valid_snapshot_retained=true。10月1—7日中国休市，因此10月6日没有应有的中国Night；这不是“最新session缺失”。旧9月29日晚、归属9月30日的有效Night只用于历史分解，不计本期新增层。[上期所国庆安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)

读取状态：核心输入ok/last-good；假期根任务和Night为stale/validation failure；期权surface可研究、execution missing；surface_latest空文件判为empty而非parse error。没有工具截断记录被误写成源文件为空。

### 2.2 07:00海外新增

- **原油**：10月6日Brent结算100.58美元/桶（+0.3%）、WTI 89.44（近持平）；Brent盘中曾跌至100以下后收复。中东近7—10日约有1,200万桶/日原油、200万桶/日成品油离港，沙特东西管线吞吐升至580万桶，但胡塞袭击、Gulf cyclone风险仍使尾部存在。[Reuters油价与流量](https://www.reuters.com/business/energy/oil-prices-slip-traders-weigh-strong-mideast-exports-against-gulf-tensions-2026-10-06/)
- **能源平衡**：EIA把2026Q4 Brent均价预测上调至105美元，并预计柴油10月仍高于6美元/加仑；这是SC空头和柴油多头的共同反证/支持，不能只选一边。[Reuters/EIA](https://www.reuters.com/business/energy/us-eia-hikes-oil-price-forecasts-again-as-iran-war-drains-global-stockpile-2026-10-06/)
- **橡胶/铁矿**：SGX页面10月6日16:54新加坡时间显示TSR20 Dec-26结算259.2美分/公斤、SGX铁矿Nov-26结算91.65美元/吨；TSR20较10月2日同月257.1约高0.82%，是RU本期新增外盘确认，但不是RU2701可执行进口平价。[SGX](https://www.sgx.com/)
- **贵金属/美元**：现货黄金约4,168.33美元/盎司（+0.7%）、白银61.56（+0.8%）；美元指数期货约101.63（-0.3%），USD/CNH约6.702、近持平。贵金属获一日反弹，但中国AG 5D弱势和高收益率环境尚未被推翻。[Reuters黄金](https://www.reuters.com/world/india/gold-inches-lower-firmer-dollar-higher-yields-weigh-2026-10-06/)
- **铜/谷物/糖**：LME三月铜10月6日欧洲早盘约14,446美元/吨、+0.2%，不是收盘；CBOT玉米/大豆/小麦亚洲时段分别约-0.1%/-0.2%/-0.2%；ICE原糖触及20.81美分/磅、19个月高位。均只作10月8日gap映射，不称中国已经交易。

## 三、商品仪表盘（展示12项；全市场77产品已扫描）

> 中国EOD均为2026-09-30。Night为9月29日开始、归属9月30日的旧session；海外为10月6日收盘或明确标注的盘中值。Basis C不进入方向评分。

| 板块 | 品种/合约 | EOD close/settle | 1D/5D | Volume/OI/ΔOI | EOD curve | Basis/Physical | 旧Night close；vs close/vs settle；ΔOI | 07:00 Overseas | Options S/P/E | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 橡胶 | RU2701 | 20,095/19,710 | +3.52%/+3.96% | 513,683/150,478/+18,323 | 轻back +0.24% | C；实体沿用 | 19,665；+3.45%/+3.28%；+11,873 | TSR20 Dec 259.2，较10/2约+0.82% | Y/Y/N | **最强；10/8等45分钟** |
| 原油 | SC2611 | 711.0/696.1 | -2.90%/-2.93% | 175,510/24,979/-4,690 | 近乎平坦，轻contango | Physical missing | 705.2；-0.94%/-1.63%；-1,162 | Brent100.58、WTI89.44；流量恢复但尾险在 | Y/N/N | 反弹失败空研究；不追首跳 |
| 能源RV | ICE Gasoil/Brent | — | — | — | 需同步期限结构 | 物流实体部分支持 | 不适用 | EIA抬柴油/Brent预测；两腿实时价缺失 | 未核 | 待报价，不可执行 |
| 油脂 | OI701 | 10,230/10,217 | +1.72%/-0.25% | 272,992/283,749/+9,681 | back 1.82% | 仓单1,463、日减40；basis C | 10,234；+1.76%/+1.89%；+6,681 | CBOT大豆约-0.2%，BMD终盘未核 | Y/N/N | 曲线强、外盘未确认 |
| 合成胶 | BR2611 | 16,000/15,870 | +3.12%/+6.58% | 288,172/51,622/-4,127 | back 1.13% | 实体缺失 | 16,155；+4.50%/+4.97%；+8,194 | TSR20支持，原油仅稳定 | Y/N/N | 跟随RU观察，不单独追 |
| 软商品 | SR701 | 5,354/5,336 | -0.15%/-0.15% | 302,888/564,277/-12,444 | contango 2.77% | 仓单26,313、日减779；C | 5,341；+0.24%/-0.06%；+744 | ICE糖20.81，19个月高位 | Y/Y/N | 海外强、国内曲线反对 |
| 贵金属 | AG2612 | 14,980/14,928 | +0.15%/-7.41% | 273,904/283,220/+6,039 | 轻contango | 无有效实体层 | 14,958；+0.74%/+0.35% | 银61.56 +0.8%，金+0.7%，DXY回落 | Y/N/N | 反弹观察，不抄底 |
| 有色 | CU2611 | 109,680/109,570 | +0.25%/-1.03% | 69,830/185,404/+183 | back 0.73% | basis C | 109,420；-0.14%/+0.11% | LME铜盘中14,446、+0.2% | Y/N/N | 温和正映射，等国内curve |
| 黑色 | I2701 | 702.5/704.5 | +0.43%/-0.98% | 218,646/552,096/-28,979 | 轻contango | basis C | DCE unresolved | SGX Nov 91.65 | DCE不足 | 无三层共振 |
| 沥青 | BU2611 | 5,013/5,091 | -2.00%/-0.29% | 880,746/155,550/-53,419 | deep back/roll caveat | 实体缺失 | 5,142；-1.98%/-1.02%；-24,314 | 原油终盘稳定 | N/N/N | 深曲线不可当套利 |
| 聚酯 | TA701 | 6,300/6,268 | +0.22%/+0.10% | 1,191,682/1,016,989/-69,523 | back 5.35% | basis C | 6,306；-0.69%/+0.83%；-30,011 | 原油稳定、产品物流仍紧 | Y/N/N | 双锚分歧，等45分钟 |
| 航运 | EC2611 | 2,794/2,823.5 | -1.67%/+7.62% | 13,089/22,057/-2,569 | contango 26.12%，仅2观测 | 无 | 不适用 | 原油流量恢复、油轮风险仍高 | 无 | 交割/roll噪音，不交易曲线 |

## 四、相比上一期真正变化与旧建议台账

1. **中国层仍无新增。** 9/30 last-good继续有效，10/6假期刷新失败不增加也不删除证据；没有Current Trading Day Night。
2. **RU获新外盘确认。** SGX TSR20 Dec结算259.2，较10/2同月约+0.82%；RU由75升至77，新增来自外部层更新，不把SGX代理当进口套利。
3. **原油从盘中急跌中收复。** Brent最终100.58、WTI89.44，说明供应恢复压制上涨，但尾部风险仍有买盘；SC条件空头只能等国内失败反弹，不能在节后首跳追空。
4. **柴油紧张逻辑强化但政策缓冲也增强。** EIA抬高Q4 Brent和柴油预测；G7释放储备、美国扩大免税柴油使用是反证。柴油篮子升至65，但仍缺同步bid/ask与保证金。
5. **贵金属反弹、美元回落。** 黄金/白银约+0.7%/+0.8%，只修复一日；黄金信用主题仍未获得中国价格、实际利率趋势和期权执行面的共同确认。
6. **原糖外强进一步扩大。** ICE糖20.81创19个月高位，但SR中国价格弱、contango且减仓，维持59分研究观察，不把背离当套利。

| idea_id | 首次提出 | 上次状态 | 当前状态 | 变更原因/旧建议处置 |
|---|---:|---|---|---|
| COM-E-RU2701-RUBBER-TIGHTNESS-20261001 | 10/1 | 晨报75、晚报75 | **77，休市等待** | 新SICOM/SGX结算；原入场、止损和目标不重置 |
| COM-E-SC2611-CONDITIONAL-SHORT-20261006 | 10/6晚 | 67，等待10/8 | 66，等待10/8 | Brent收复100；供应恢复支持与尾险反证并存 |
| COM-E-DIESEL-LOGISTICS-20261005 | 10/5 | 晨报62、晚报65 | 65，待报价 | EIA确认产品紧张；政策放储反对 |
| COM-E-OI701-RELSTRENGTH-20260930 | 9/30 | 晨报65、晚报63 | 63，休市等待 | 外盘油籽偏弱、无国内新增 |
| COM-SR-DIVERGENCE-20260930 | 9/30 | 59，观察 | 59，观察 | ICE糖创新高，但国内层反对 |
| COM-E-BR2611-RELSTRENGTH-20260930 | 9/30 | 晨报60、晚报59 | 59，观察 | 橡胶外盘支持与国内减仓/原油成本弱化抵消 |
| COM-E-SC2611-SUPPLY-TAIL-20261005 | 10/5 | 多头尾险观察 | **取消，不恢复** | 中东流量恢复且中国旧价格/curve不支持多头 |

无成交反馈，不假设用户持仓；任何“退出”仅适用于若此前已按条件建立。

## 五、产业链地图与固定问题

| 产业链 | 方向/强弱 | EOD/Night | Curve/实体 | 海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 天然橡胶—合成胶 | **最强：RU条件多** | RU价涨仓增；旧Night已完成部分定价 | 轻back；实体沿用 | TSR20新结算支持；RU IV>RV且无报价 | 10/8中国接受度、实时SICOM | 中高 |
| 原油—炼化—物流 | SC反弹失败空；柴油相对强 | SC旧EOD/Night弱 | SC近乎平；SC/LU实体缺失 | 流量恢复支持空；EIA/地缘反对；期权昂贵 | 国内gap、gasoil/Brent同步价 | 中 |
| 油脂—饲料 | OI相对强、P偏弱 | OI价涨仓增；旧Night重复 | OI back+仓单小降 | CBOT偏弱；DCE options不足 | BMD终盘、A/B basis | 中低 |
| 贵金属—有色 | 海外修复、国内未确认 | AG 5D弱；CU近中性 | AG contango、CU小back | 金银反弹、DXY回落；execution 0 | 实际利率趋势与国内gap | 低 |
| 黑色—建材—新能源 | **最弱：无共振** | I/FG/LC弱或去仓 | basis多为C | SGX铁矿91.65，仅proxy | 节后需求/库存、DCE期权 | 低 |

Regime：**中国长假最后一日 + RU外盘继续确认 + 原油供应恢复与地缘尾险拉锯 + 成品油物流紧 + 贵金属/糖反弹。**

固定问题答复：9/30 EOD仅RU/OI价格获curve部分确认；旧Night强化RU/BR、重复OI、削弱SC，但不是本期新增。TA与SR的return-vs-close和return-vs-settlement分歧显著，禁止用结算锚冒充新增信息。当前无Night curve。实体仅部分确认橡胶/OI/SR；SC/LU缺失。海外对RU同向，对SC是“流量偏空、尾险偏多”的冲突，对贵金属偏多；USD/CNH稳定，人民币不是本期主要驱动。期权execution-ready为0，不能证明优于裸期货。唯一跨市场/RV研究是柴油/Brent，尚不可执行。BU/EC深曲线、OP/AD换月和大幅去仓更像roll噪音。10月8日RU/BR/TA/EC等45分钟，SC/贵金属至少30—45分钟。不值得交易：追RU高开、追SC第一跳、AG抄底、C级basis和不可比价差。

## 六、机会排行榜

| 排名 | idea_id /方向/周期 | 逻辑25 | 赔率25 | 催化20 | 价/曲/波15 | 拥挤技术15 | 总分 | 支持层 | 判断/证据/执行 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | COM-E-RU2701-RUBBER-TIGHTNESS-20261001；多；2—10D | 22 | 16 | 17 | 14 | 8 | **77** | 4：价格持仓、curve、实体、外部 | 待验证优势/部分充分/休市等待 |
| 2 | COM-E-SC2611-CONDITIONAL-SHORT-20261006；空；1—7D | 19 | 15 | 13 | 11 | 8 | **66** | 2：价格curve、外部流量 | 待验证优势/部分/等待触发 |
| 3 | COM-E-DIESEL-LOGISTICS-20261005；多柴油空Brent；1—7D | 20 | 13 | 16 | 10 | 6 | **65** | 2：海外相对价格、物流实体 | 待验证优势/部分/待报价参数 |
| 4 | COM-E-OI701-RELSTRENGTH-20260930；多；3—15D | 18 | 14 | 10 | 11 | 10 | **63** | 2：价格持仓、curve/仓单 | 待验证优势/部分/休市等待 |
| 5 | COM-SR-DIVERGENCE-20260930；观察多；3—10D | 17 | 12 | 13 | 8 | 9 | **59** | 1：外部糖价；国内层反对 | 证据不足/不足/研究观察 |

无80+候选；仅RU达到70+研究门槛。分数不是胜率或仓位指令，风险偏好高未增加评分。

## 七、前三名交易卡

### 7.1 RU2701回踩确认多——非当前条件单

- **事实**：9/30 close/settle 20,095/19,710；1D +3.52%、5D +3.96%；OI +18,323。旧Night O/H/L/C=19,125/19,730/19,090/19,665，vs close +3.45%、vs settle +3.28%，ΔOI +11,873；SGX TSR20 Dec 10/6结算259.2，较10/2同月约+0.82%。
- **市场隐含/分歧**：市场已计入供给紧张，但可能低估持续性；竞争解释是长假gap和IV已充分定价。
- **五层**：支持①价格持仓、②curve、③实体last-good、④新外盘；反对⑤IV溢价且无bid/ask。Night不另算层。
- **工具**：RU2701单腿多，1:0；期权仅研究12/25到期0.35—0.45 Delta买Call/0.15—0.25 Delta卖Call的1×1价差，execution-ready=false，不报价。
- **入场/分批**：10/8 09:45后20,000—20,200回踩持稳、近月结构不收窄；40%/30%/30%。高开>20,500或45分钟不能收复20,000放弃。
- **退出**：30分钟收于19,600下方，或SICOM转弱且curve转contango；TP1 20,750、TP2 21,400；两日不扩张时间止损。
- **好/中/坏成交**：20,020/20,100/20,200；以19,600止损，TP1约1.74R/1.30R/0.92R，TP2约3.29R/2.60R/2.00R；坏成交放弃。
- **参数/压力**：10吨/手、tick 5元/吨、tick value 50元；名义约200,950元/手；假期安排limit 9%、一般margin 11%；夜盘21:00—23:00；LTD 2027-01-15。按settle一板约17,739元、两板复合约37,070元/手。期货最大损失不有限；12月中下旬前滚动，严禁进入交割月。
- **风险**：试仓计划损失≤NAV 0.50%；与BR/NR同因子合并≤1%。最坏情景是假期外盘回落、国内高开低走及保证金再上调。

### 7.2 SC2611反弹失败空——非当前条件单

- **事实**：9/30 close/settle 711.0/696.1；1D -2.90%、5D -2.93%；OI -4,690；curve近乎平坦。旧Night close 705.2，vs close -0.94%、vs settle -1.63%，ΔOI -1,162；日盘相对Night约+0.82%，说明下跌并非单边延续。10/6 Brent/WTI结算100.58/89.44。
- **市场隐含/分歧**：市场仍给地缘尾险高溢价；分歧是中东流量恢复、G7放储和沙特管线是否足以压低中国SC。最强反证是Brent从盘中低位收复、EIA将Q4均价抬至105以及胡塞/气旋风险。
- **五层**：支持①旧价格/持仓线索、②平坦curve与④外部流量合并后共2层；反对③实体缺失、⑤短到期期权昂贵。两层约束总分≤69。
- **工具**：SC2611期货空，1:0；SC2611期权10/14到期过近且execution-ready=false，不作为替代有限损失承诺。
- **入场/分批**：10/8 09:45后，690—700反弹失败且Brent未重新突破102；或680下破后反抽失败。40%/30%/30%。直接低开<665不追。
- **止损/失效**：反弹空方案30分钟接受711上方；破位方案收回700上方；Brent>103且SC近月转back时逻辑失效。TP1 665/655，TP2 630/625；两日不扩张退出。
- **好/中/坏成交**：700/695/690；统一711止损、以665为TP1，对应约3.18R/1.88R/1.19R；低于690为坏成交。
- **参数/压力**：1,000桶/手、tick 0.1元/桶、tick value 100元；名义约711,000元；参考margin 22%、limit 20%、LTD 2026-10-30。按settle一板压力约139,220元/手、两板复合约306,000—307,000元；不是最大损失。10月中旬前完成移仓/退出，避开交割。
- **风险**：试仓≤NAV 0.25%；与BU/FU/LU/TA同能源因子合并≤0.75%。最坏情景是复市高开涨停、境内外错时与保证金上调。

### 7.3 ICE柴油物流篮子——待报价研究卡

- **结构**：多5手ICE Low Sulphur Gasoil Nov-26、空7手ICE Brent Dec-26；P&L=`500×ΔGasoil(美元/吨)−7,000×ΔBrent(美元/桶)`。5:7仅为10/5快照附近美元名义近似中性，不是Beta中性、裂解收益率中性或质量中性。
- **逻辑/反证**：成品油出口、炼厂与物流瓶颈及EIA柴油预测支持；中东原油流量恢复、G7放储和免税柴油政策反对。市场可能低估产品相对原油的物流溢价，也可能已在裂解和backwardation中完全定价。
- **支持层**：④相对价格、③物流实体；缺①当前双边报价、②同期限curve、⑤期权面。
- **入场**：仅在下一流动性充足时段取得两腿同步bid/ask、保证金和last-trade参数后；15分钟篮子相对同步中价上破1%，Brent不同时急涨，40%/30%/30%。任一腿滑点>0.25%放弃。
- **退出**：篮子较成交中价-0.75%止损；TP1 +1.5%、TP2 +3%；两场交易时段不扩张退出。先平较差流动性腿，再同步对冲剩余Delta。
- **成本/参数**：gasoil常规100吨/手、tick 0.25美元/吨（25美元/手）；Brent 1,000桶/手、tick 0.01美元/桶（10美元/手）。保证金、LTD和交割参数未由引擎确认；至少到期前5个营业日滚动。
- **最大损失/风险**：非有限风险结构；计划损失≤NAV 0.25%，错腿、断市和相关性破裂可超出。无可靠实时价，不编净R、胜率或期望收益。

## 八、商品期权专项

最新有效截面仍为2026-09-30，本期无中国期权新增：surface-ready 192/196、positioning-ready 47/196、execution-ready 0/196，bid/ask覆盖0，dealer gamma方向未知。

| underlying/expiry | ATM IV/RV20/差 | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---|---|
| RU2701 / 2026-12-25 | 27.94/22.25/+5.69vol | +1.91/+0.24 | Y/Y/N | 新外盘上行改变moneyness；call不证明便宜，等复市重建 |
| SC2611 / 2026-10-14 | 67.18/60.56/+6.61 | -2.58/+2.53 | Y/N/N | 到期太近、事件凸性贵，旧面不可成交 |
| OI701 / 2026-12-11 | 15.26/14.24/+1.02 | +3.92/+0.64 | Y/N/N | 上偏贵、positioning不完整 |
| BR2611 / 2026-10-26 | 37.00/29.01/+8.00 | -1.36/-0.35 | Y/N/N | 短到期高IV，避免追买单腿gamma |
| SR701 / 2026-12-11 | 10.36/6.97/+3.39 | +3.01/+1.34 | Y/Y/N | 外盘糖上涨后旧moneyness不可比 |

IV-RV不是便宜证据。没有实时bid/ask，不写权利金、净成本、滑点或精确Greeks。回避裸卖SC/BR事件尾部以及把PCR/OI解释成机构或做市商方向。期权目前不优于可核验的线性触发表达。

## 九、10月8日09:00开盘风险地图

**今天中国仍休市，没有09:00开盘。** 下一实际日盘为10月8日09:00；以下只是不晚于本截点的预案，10月8日08:45必须刷新海外、人民币、交易所参数与当前报价。

严格三层：
1. Previous China EOD：2026-09-30；
2. Current Trading Day Night Session：不存在；10/6假期记录不可用，9/29 Night仅历史；
3. 07:00 Overseas：TSR20新高于10/2、油价终盘稳定、金银与糖反弹、美元回落。

| 品种 | 初步gap | 是否已在旧Night定价 | 内外冲突 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|---|
| RU2701 | 偏高 | 9/30已定价一部分；10/6外盘新增未定价 | 无明显冲突，但gap赔率差 | 不追；45分钟 | 20,000—20,200、SICOM、curve |
| SC2611 | 平/偏低但尾部大 | 旧Night偏弱 | 流量偏空 vs 地缘/EIA偏多 | 不追空；45分钟 | 690—700接受度、Brent、人民币、curve |
| BR2611 | 偏高/高波动 | 旧Night强、EOD回吐 | 橡胶强 vs 原油不强 | 不追；45—60分钟 | RU/BR、丁二烯、OI |
| OI701 | 平/略低 | 旧Night基本定价 | 国内curve强 vs CBOT略弱 | 不追；30—45分钟 | 10,120—10,220、back>1.5%、P/Y |
| SR701 | 偏高 | 旧Night信息有限 | ICE强 vs 国内contango/减仓 | 不追；45分钟 | 5,336/5,354、curve与现货 |
| AU/AG | 偏高 | 旧Night过时 | 海外反弹 vs 国内5D弱 | 不抄底；45分钟 | DXY、实际利率、USD/CNH |
| CU/I | 平/小高 | 旧Night不完整 | 海外仅温和支持 | 30分钟 | LME/SGX、curve、OI |
| EC | 不判断 | 无Night | 流量恢复 vs 船舶风险 | 45—60分钟 | 运价、舱位、近月成交 |

海外变动与旧China Night不在同一事件窗口，不能计算当前信息弹性。集合竞价若已一次性吸收累计变动，所有首跳交易都应放弃。

## 十、未来24小时/7日事件日历（北京时间）

| 时间 | 事件 | Delta/Vega处理 |
|---|---|---|
| 10月7日22:30 | [EIA周度石油库存](https://www.eia.gov/petroleum/supply/weekly/schedule.php) | 重点看原油、馏分油、炼厂开工；能源Delta先减，发布后等15分钟 |
| 10月8日02:00 | [FOMC会议纪要](https://www.federalreserve.gov/monetarypolicy.htm) | 黄金/白银、美元与实际利率；贵金属不押单边，期权须有限损失且有实时报价 |
| 10月8日08:55/09:00 | 中国商品复市 | 刷新所有价格、curve、bid/ask与参数；等待30—60分钟 |
| 10月8日21:00 | 中国夜盘恢复，归属10月9日 | 使用exact-contract新Night，不沿用9/30快照 |
| 10月10日00:00 | [USDA WASDE（10/9 12:00 ET）](https://usda.azureedge.us/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report) | 农产品Delta减半；事件期权只做定义损失结构 |
| 10月10日03:30常规时点 | [CFTC COT](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) | 只作海外拥挤度后验，不推断国内资金身份 |
| 未来7日持续 | Gulf cyclone、Hormuz/Bab al-Mandeb船流、沙特设施、橡胶产区天气、矿山/炼厂 | 事件跳空优先等待或有限凸性；无报价不卖裸尾部 |

## 十一、覆盖核对

| 板块 | 应覆盖 | 实际取数并分析 | 数据不足 | 未入榜异常/无异常依据 |
|---|---:|---:|---|---|
| 黑色建材 | 10：I/JM/J/RB/HC/FG/SA/SF/SM/WR | 10 | DCE Night/Options、A/B basis | FG与SF去仓但缺curve/实体共振；SGX铁矿仅温和 |
| 有色贵金属 | 14：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG/PD/PT | 14 | 国内实时价、部分新代码历史 | AG海外反弹最强；AO/AD仍有roll异常 |
| 能源炼化化工 | 26：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP/EC/BZ/OP/ZC/PL | 26 | SC/LU实体、加工利润、exact gasoil/Brent | RU外盘确认最强；BU/OP深曲线/roll；SC多空冲突 |
| 新能源 | 3：LC/SI/PS | 3 | LC实体与执行期权 | LC 5D弱但无实体/波动率确认，不抄底 |
| 农产品油脂畜牧 | 14：A/B/M/RM/Y/P/OI/C/CS/LH/JD/LG/RR/RS | 14 | DCE期权、A/B basis、BMD终盘 | OI曲线最强；豆系外盘略弱；LG/B/CS去杠杆 |
| 航运软商品 | 10：EC/CF/CY/SR/AP/CJ/PK/PM/RI/WH | 10 | EC运价/舱位、多品种期权 | SR外盘创新高但国内反对；EC曲线不可比 |

汇总：应覆盖至少63个强制代码；实际77产品均有期货/Market State初筛，64个期权产品中42个成功、196个series完成质量扫描。数据不足不缩小覆盖。策略维度：方向、curve、basis、跨品种、跨市场、波动率/偏度/事件均已扫描；周期覆盖1D/3D/5D/20D。没有A/B级basis可执行机会，没有exact import parity，没有execution-ready期权。风险预算：试仓最大计划损失NAV 0.25%—0.75%，确认交易0.75%—1.50%，单主题≤2.5%—3.0%；同因子合并。压力覆盖一/两个涨跌停、相关性破裂、断流动性、gap、保证金上调、IV跳升/坍塌、交割挤压和人民币急变。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：无；RU2701、SC2611及OI701均须10月8日重报价并完成30—60分钟确认，柴油篮子须先取得同步bid/ask与参数。
C. 今天应继续观察的机会：RU外盘强度能否被国内接受、SC对Brent与EIA数据的弹性、柴油/Brent物流价差、SR外强内弱及金银反弹延续性。
D. 今天必须避免或退出的交易：追逐10月8日第一跳、裸多SC、追高RU/BR、抄底AG、恢复旧SC供应尾险多头、使用C级basis或无bid/ask期权建立所谓套利。
