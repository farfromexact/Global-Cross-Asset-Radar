# 全球商品期货期权高风险机会雷达（晚间版）

- 报告日期：2026-10-06
- 生成/信息截点：2026-10-06 19:30 北京时间
- edition：`commodities_evening`
- prompt_version：`radar_2026-09-06_coverage_v1`
- data_protocol_version：`china_commodities_v2`
- 中国市场状态：国庆休市；最近完整交易日 2026-09-30；今晚无 21:00 夜盘。下一实际窗口为 2026-10-08 08:55—09:00 集合竞价/日盘，下一夜盘为 2026-10-08 21:00（归属 10 月 9 日交易日）
- 免责声明：research only; manual quote and manual confirmation required before execution; no premium quoted

## 一、今晚一句话结论

> **截至本报告时点，无可立即执行的合格新交易。原油跌破100美元削弱SC多头，但成品油物流仍紧；RU保持节后首选，所有国内方案须10月8日重报价。**

最接近验证的三项：RU2701 回踩确认多、SC2611 低位反抽失败空、ICE 柴油/Brent 物流价差。已分析但优势不足：OI701、BR2611、SR701、贵金属反转。数据不足：国内期权当前 bid/ask、DCE 期权定位、精确 import parity、当前 SICOM 橡胶结算及 USD/CNH。

## 二、数据质量、覆盖与时间语义

| 模块 | 实际读取 | 日期/生成时点 | 状态 | 使用纪律 |
|---|---|---|---|---|
| 统一输入 | [report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) | requested 9/30；generated 10/6 08:13 BJT | ok，schema v2 | 主输入；不是 10/6 中国行情 |
| Futures | report_input + [latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json) | source 9/30；generated 10/1 08:02 | last-good verified | 806 合约、77 产品、五所完整，full_market_ready=true、source-date 100%、critical errors 0；6 条占位 OHLC 已排除 |
| Root status | [last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json) | run_date 10/5；generated 10/6 08:08 | holiday refresh failed | 15 个错误与 0 合约来自非交易日刷新；不自动使 9/30 last-good 失效 |
| Market State | report_input.products | 指标截止 9/30；generated 10/6 08:08 | last-good usable | 77 产品的同合约 1D/3D/5D/20D、OI、curve 已全扫 |
| Physical | report_input.physical | source 9/30；generated 10/1 08:12 | carried/partial | 20 组目标，18 组沿用；SC/LU 缺失；basis 均 C 或缺失，只作 context |
| External repo | report_input.external | source 10/5；generated 10/6 08:13 | fresh/validated | 17/22 series；全部 context_only，不构成跨市场套利 |
| Night status | [night status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) | trading_date 10/6；night_session_date 10/5；generated 10/6 08:03 | holiday-failed | data_fresh=false、validation=false、published=false、coverage_complete=false、night contracts=0；今晚也无应有 Night |
| Options | [quality_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json) + report_input series | source 9/30；generated 10/1 00:03 UTC | research-ready / execution-missing | 14,468 records、196 series；surface 192、positioning 47、execution 0；IV 98.84%、OI 68.88%、bid/ask 0 |
| Surface file | [surface_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json) | 当前 repo ref | **empty** | 是源文件空，不是工具截断；逐 series 研究指标来自统一输入 |
| Metadata | report_input + [contract_meta.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json) | 9/30 | partial | contract match 67.49%、effective 73.45%；动态 margin/limit 等覆盖约 30.15% |

当前 Night 尝试：selected/request 806、outside-window 592、query_error 214、unresolved 214、其余 missing quote/timestamp/price 均 0，previous_valid_snapshot_retained=true。10 月 1—7 日休市，因此“无当前 Night”属日历不适用，不是行情漏取；统一输入中的 trading_date=9/30、night_session_date=9/29 只用于历史价格发现分解，与今晚未来行情无关。[上期所国庆安排](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)

## 三、商品仪表盘（展示 12 项；全量 77 产品扫描见覆盖核对）

> 中国列均为 2026-09-30 last-good。早前 Night 为 9 月 29 日开始、归属 9 月 30 日的旧 session；不是今晚行情。15:00—19:30 海外是下一交易窗口的映射证据，不是中国期货已成交的变化。

| 板块 | 品种/合约 | EOD close/settle | 1D/5D | Volume/OI/ΔOI | Curve | Basis/Physical | 早前 Night close / overnight | day follow-through | 15:00—19:30 Overseas | S/P/E | 下一窗口信号 |
|---|---|---:|---:|---:|---|---|---:|---:|---|---|---|
| 橡胶 | RU2701 | 20,095/19,710 | +3.52%/+3.96% | 513,683/150,478/+18,323 | 轻 back +0.24% | basis C；实体沿用 | 19,665/+3.45% | +2.19% | SICOM 10/6精确价未核实 | Y/Y/N | 10/8 等45分钟回踩确认 |
| 油脂 | OI701 | 10,230/10,217 | +1.72%/-0.25% | 272,992/283,749/+9,681 | back +1.82% | 仓单1,463，日减40；basis C | 10,234/+1.76% | -0.04% | 棕榈最新约-0.5%，库存压力偏反对 | Y/N/N | 分数下调，等30分钟 |
| 合成胶 | BR2611 | 16,000/15,870 | +3.12%/+6.58% | 288,172/51,622/-4,127 | back +1.13% | 实体缺失 | 16,155/+4.50% | -0.96% | 原油再跌、橡胶新价缺失 | Y/N/N | 成本端反对，降级 |
| 原油 | SC2611 | 711.0/696.1 | -2.90%/-2.93% | 175,510/24,979/-4,690 | 轻 contango -0.06% | Physical missing | 705.2/-0.94% | +0.82% | Brent 98.62、WTI 87.60，较10/5结算再跌 | Y/N/N | 若10/8反抽失败才研究空 |
| 沥青 | BU2611 | 5,013/5,091 | -2.00%/-0.29% | 880,746/155,550/-53,419 | 深 back +12.61% | 实体缺失 | 5,142/-1.98% | -2.51% | 原油偏空，物流成本偏多 | N/N/N | roll/交割扭曲，不做伪套利 |
| 铜 | CU2611 | 109,680/109,570 | +0.25%/-1.03% | 69,830/185,404/+183 | back +0.73% | basis C | 109,420/-0.14% | +0.24% | LME铜约14,431.5，变化有限 | Y/partial/N | 内外未共振，等30分钟 |
| 白银 | AG2612 | 14,980/14,928 | +0.15%/-7.41% | 273,904/283,220/+6,039 | 轻 contango -0.22% | 无实体确认 | 14,958/+0.74% | +0.15% | 现货银约61.80、日内反弹；黄金约4,159.9 | Y/partial/N | 反弹不足以确认底部 |
| 铁矿 | I2701 | 702.5/704.5 | +0.43%/-0.98% | 218,646/552,096/-28,979 | 轻 contango -0.21% | basis C | — | — | SGX 10/5 close 91.85；无强新增 | DCE缺 | 证据不足 |
| 棕榈 | P2701 | 9,581/9,593 | +0.23%/-2.70% | 373,884/546,979/-5,820 | contango -0.37% | basis C | — | — | BMD回落且库存高，但属外部 context | DCE缺 | 弱于OI，不追空 |
| PTA | TA701 | 6,300/6,268 | +0.22%/+0.10% | 1,191,682/1,016,989/-69,523 | back +5.35% | basis C | 6,306/-0.69% | -0.10% | 原油下跌 vs 产品物流紧张 | Y/partial/N | 锚点冲突，等45分钟 |
| 白糖 | SR701 | 5,354/5,336 | -0.15%/-0.15% | 302,888/564,277/-12,444 | contango -2.77% | 仓单26,313，日减779；basis C | 5,341/+0.24% | +0.24% | ICE糖约19—20美分区间，天气叙事偏多 | Y/Y/N | 内外分化，不是套利 |
| 航运 | EC2611 | 2,794/2,823.5 | -1.67%/+7.62% | 13,089/22,057/-2,569 | -26.12%，仅2观测/roll | 无 | 不适用 | 不适用 | 海湾原油流恢复但油轮袭击仍多 | — | 无夜盘；曲线不可直接交易 |

## 四、相比今晨与上一晚真正变化

1. **原油绝对价格继续下修。** 10 月 6 日约 18:13 BJT，Brent 98.62、WTI 87.60，较 10 月 5 日 repo close 100.23/89.28 再跌约 1.6%/1.9%。海湾流量恢复和 G7 储备释放成为边际主导，SC 裸多进一步失去依据。[Reuters，2026-10-06](https://www.reuters.com/business/energy/oil-prices-slip-traders-weigh-strong-mideast-exports-against-gulf-tensions-2026-10-06/)
2. **“原油恢复、成品油仍紧”的分化更清晰。** 海湾总流量恢复至战前约 81%，原油/凝析油恢复约 91%，但成品油出口仅约 60%；这支持柴油相对 Brent 的物流 RV，却不支持追多 Brent。[Reuters 海湾流量](https://www.reuters.com/business/energy/gulf-oil-flows-rise-average-81-pre-war-rate-september-data-shows-2026-10-06/)
3. **贵金属日内修复但未形成反转证据。** 黄金约 +0.4% 至 4,159.9、白银约 +2.3% 至 61.80；DXY约102.0、10Y收益率回落至约5.28%。这是对今晨强美元压力的边际缓和，但中国仍未交易，且AG 5D仍弱，不恢复多头卡。[Reuters 黄金](https://www.reuters.com/world/india/gold-inches-lower-firmer-dollar-higher-yields-weigh-2026-10-06/)；[Reuters 全球市场](https://www.reuters.com/world/china/global-markets-global-markets-2026-10-06/)
4. **OI 外部确认减弱。** 棕榈油最新约跌0.5%，高库存背景反对把9/30国内backwardation直接外推；OI由65降至63。
5. **RU没有新增官方外盘结算。** 仍为75分，但没有新催化；任何节后高开都要先观察价格弹性。
6. **EIA新展望提供中期锚而非当下交易信号。** EIA预计Brent 2026年下半年均价约90、2027年约74；当前现货风险溢价仍高，但不能把年度均价直接作为SC短线目标。[EIA STEO](https://www.eia.gov/outlooks/steo/)

## 五、产业链地图

| 产业链 | 方向/强弱 | 中国旧价与Night→Day | Curve/实体 | 海外/期权 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 天然胶—合成胶 | **最强：RU条件多；BR降级** | RU旧Night+3.45%、日盘再+2.19%；BR日盘回吐 | 轻back；实体沿用 | 橡胶新价缺失；RU IV>RV | 当前SICOM与复市bid/ask | 中 |
| 原油—成品油 | **绝对原油偏空，柴油物流RV偏多** | SC 9/30弱、curve近平；BU深back受roll | SC/LU实体缺失；成品油流恢复滞后 | Brent/WTI续跌；SC IV高 | 同刻gasoil/Brent、运费和保证金 | 中 |
| 油脂—饲料 | OI相对强度降级 | OI旧Night涨后日盘横盘 | back+仓单小降；basis C | 棕榈回落与库存压力反对 | 节后现货、DCE期权 | 中低 |
| 有色—贵金属 | 金银修复、工业金属中性 | AG 5D弱；CU近中性 | CU小幅back；实体不足 | 金银反弹、DXY/收益率回落 | USD/CNH、节后中国弹性 | 低 |
| 黑色—建材—新能源 | **最弱：无新增确认** | I/FG/LC等旧数据偏弱或去仓 | 多数basis C | 海外proxy有限 | 节后需求、库存、DCE期权 | 低 |

当前 regime：**中国长假休市 + 海湾原油流恢复压低绝对油价 + 成品油/航运物流仍紧 + 美元高位回落 + 国内last-good分化。**

固定问题答复：今晚不值得新增中国风险；没有今日 EOD/Night 可分解，9/29 Night→9/30 Day仅作历史；RU/OI旧EOD分别获curve部分确认，SC弱势获海外原油进一步确认；实体仅仓单与海外物流部分支持；15:00—19:30海外油跌、金银反弹，均未被中国白天预交易；USD偏高但回落，USD/CNH未核实，人民币作用不量化；期权execution-ready为0，不优于可核价期货；柴油/Brent仅为待报价RV，无exact import parity套利。BU/EC深曲线、OP/AD换月、单日去仓多属噪音。节后RU/BR/TA等45分钟，SC/CU/OI至少30分钟。避免：追首跳、抄底AG、把C级basis或EC/BU曲线当套利。

## 六、机会排行榜

| 排名 | idea_id / 方向 / 周期 | 分项与总分 | 支持层 | 研究判断｜证据｜执行 | 工具/损失 | 反证与变化 |
|---:|---|---:|---|---|---|---|
| 1 | COM-E-RU2701-RUBBER-TIGHTNESS-20261001；多；2—10D | 22+16+16+13+8=**75** | 4：价仓、curve、实体沿用、外盘沿用 | 待验证优势｜部分｜休市等待 | RU2701；损失不限定 | 无10/6橡胶价；不变 |
| 2 | COM-E-SC2611-SUPPLY-FADE-20261006；空；1—5D | 20+16+14+10+7=**67** | 2：国内价/curve、海外流量/价格 | 待验证优势｜部分｜休市等待 | SC2611；损失不限定 | 地缘/炼化尾险；新增 |
| 3 | COM-E-DIESEL-LOGISTICS-20261005；多柴油/空Brent；1—7D | 21+13+15+10+6=**65** | 2：海外相对价格、物流实体 | 待验证优势｜部分｜待报价/参数 | 5 Gasoil vs 7 Brent；损失不限定 | 原油跌有利RV，但无同刻报价；+3分 |
| 4 | COM-E-OI701-RELSTRENGTH-20260930；多；3—15D | 18+14+10+11+10=**63** | 2：价仓、curve/仓单 | 待验证优势｜部分｜休市等待 | OI701；损失不限定 | 棕榈/库存反对；-2分 |
| 5 | COM-E-BR2611-RELSTRENGTH-20260930；多；2—8D | 17+12+10+9+11=**59** | 2：国内价/curve、橡胶外盘沿用 | 证据不足｜不足｜休市观察 | BR2611；损失不限定 | 原油成本下跌、EOD减仓；-3分 |

无80+项。RU虽为70+，但没有当前国内交易窗口、外盘新价与执行报价，不能转为立即新仓。SC与柴油候选均只有两层，分数严格不超过69。

## 七、前三名交易卡

### 7.1 RU2701：节后回踩确认多（75，未触发）

- **事实**：9/30 close/settle=20,095/19,710；1D +3.52%、5D +3.96%；OI +18,323。旧Night OHLC=19,125/19,730/19,090/19,665，overnight +3.45%，日盘 follow-through +2.19%，Night ΔOI +11,873。
- **定价/分歧**：轻back与价仓支持，但ATM IV 27.94% 对 RV20 22.25%，上行尾部已不便宜。分歧是供给紧张能否在长假后产生第二段行情，而非一次性gap。
- **支持/反证**：①价仓、②curve、③实体last-good、④外盘last-good支持；⑤期权偏贵且无报价反对。旧Night不另算层。
- **表达**：RU2701单腿，腿比1:0；12/25到期call spread仅作备选，execution_ready=false。
- **入场**：10/8 09:45后20,000—20,200回踩持稳且back不收窄；40%/30%/30%。高开>20,500或45分钟不能收复20,000放弃。
- **止损/退出**：30分钟接受19,600下方，或SICOM同步转弱且curve转contango；TP1 20,750，TP2 21,400；2日无扩张退出。
- **好/中/坏**：20,020/20,100/20,200；止损19,600，TP1约1.74R/1.30R/0.92R，TP2约3.29R/2.60R/2.00R。
- **参数**：常规规格10吨/手、tick 5元/吨、tick value 50元；名义约200,950元。国庆后参考限幅9%、一般保证金11%；夜盘21:00—23:00，10/8恢复；LTD 2027-01-15、last delivery 1/19，12月下旬前滚动。[上期所国庆参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)
- **压力/最大损失**：一板约17,739元/手，两板复合约37,070元/手；期货最大损失不由止损限定。试仓≤NAV 0.50%，与BR/NR合并≤1.0%。

### 7.2 SC2611：节后反抽失败空（67，新增研究卡）

- **事实**：9/30 close/settle=711.0/696.1；1D -2.90%、5D -2.93%；OI -4,690。旧Night close 705.2，overnight -0.94%，日盘 follow-through +0.82%；curve轻contango。10/6 18:13 BJT Brent/WTI约98.62/87.60。
- **市场隐含/分歧**：市场仍保留物流与地缘溢价；我们的分歧是原油流量恢复与储备释放会先压缩SC绝对价，成品油紧张更多留在裂解而非原油。最强竞争解释是油轮/基础设施新袭击令Brent快速重返102上方。
- **支持/反证**：①国内旧价/curve、④海外流量与价格支持空；③炼化与产品紧张反对；②高质physical缺失；⑤IV高且无报价。
- **表达**：SC2611单腿空，腿比0:1；不以未报价put spread冒充有限损失。
- **入场**：仅10/8 09:45后且Brent仍<99。好成交：SC反抽690—700失败并回到VWAP下；中成交：跌破680后反抽680—685失败，半风险；坏成交：直接<670，不追。
- **止损/失效**：好成交止损711，中成交止损700；或Brent重上102且海湾流量再受阻。TP1分别665/655，TP2 630/625；2个交易日无扩张退出。
- **情景R**：695空、711止损，TP665/630约1.88R/4.06R；685空、700止损，TP655/625约2.00R/4.00R。gap可能突破计划止损。
- **参数**：标准乘数1,000桶、tick 0.1元/桶、tick value 100元；close名义约711,000元。仓库LTD 2026-10-30、last delivery 11/6；国庆后SC2611参考限幅20%、保证金22%，夜盘21:00—02:30，10/8恢复；10月中旬前完成滚动，避免临近交割。[INE国庆参数](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833507.html)
- **压力/最大损失**：按settle 696.1与20%限幅，空头一板约139,220元/手，两板复合约306,284元/手；最大损失不限定。仅试仓≤NAV 0.25%，能源同因子合并≤0.75%。

### 7.3 ICE柴油物流篮子：多Gasoil/空Brent（65，待报价研究卡）

- **合约/权重**：多5手ICE Low Sulphur Gasoil Nov-2026，空7手ICE Brent Dec-2026。P&L=`500×ΔGasoil(美元/吨)−7,000×ΔBrent(美元/桶)`。5:7仅是10/5同步快照下的近似**美元名义中性**，不是Beta、裂解收益率或质量中性；入场前必须按实时中价重算。
- **事实/定价**：原油/凝析油出口恢复约91%，成品油仅约60%；Brent下跌而亚洲到岸物理油、运费和炼化约束仍高。市场可能把“原油流恢复”过度外推到成品油。
- **支持/缺失**：③物流实体与④海外相对价格支持；缺①同刻bid/ask、②精确curve/运费、⑤期权面。
- **入场**：下一高流动性时段取得两腿实时bid/ask与保证金后，15分钟篮子相对同步中价上破1%，且Brent不反向急涨；40%/30%/30%。任一腿滑点>0.25%或不能同步成交即放弃。
- **止损/退出**：篮子-0.75%，或油轮费率/产品短缺被证实快速正常化；TP1 +1.5%、TP2 +3%；两场流动性时段不扩张退出。先平流动性差腿并同步对冲残余Delta。
- **好/中/坏**：总滑点≤0.10% / 0.10—0.25% / >0.25%；坏成交放弃。无实时报价，不编净R、胜率或期望收益。
- **参数**：Gasoil常规100吨/手、tick 0.25美元/吨（25美元/手）；Brent 1,000桶/手、tick 0.01美元/桶（10美元/手）。保证金与最后交易日未在中国引擎确认，须ICE/经纪商复核；到期前至少5个营业日滚动。无涨跌停，存在错腿、保证金和相关性破裂。
- **最大损失/预算**：不限定；计划止损≤NAV 0.25%。最坏情景为Brent受突发供应冲击急涨而gasoil不跟。

## 八、商品期权专项

9/30为最新有效研究截面，本期无新增。surface文件本身为空，但统一输入有196个series摘要：surface-ready 192、positioning-ready 47、execution-ready 0，dealer gamma方向未知。

| 标的/到期 | ATM IV/RV20/IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---|---|
| RU2701 / 12-25 | 27.94/22.25/+5.69vol | +1.91/+0.24 | Y/Y/N | call不便宜；只研究价差 |
| OI701 / 12-11 | 15.26/14.24/+1.02 | +3.92/+0.64 | Y/N/N | 上偏贵且定位不完整 |
| BR2611 / 10-26 | 37.00/29.01/+8.00 | -1.36/-0.35 | Y/N/N | 短到期Vega昂贵 |
| SC2611 / 10-14 | 67.18/60.56/+6.61 | -2.58/+2.53 | Y/N/N | 事件凸性贵，不裸追put |
| SR701 / 12-11 | 10.36/6.97/+3.39 | +3.01/+1.34 | Y/Y/N | 内外分化不足以证明vol错价 |

没有bid/ask，禁止写净支出、权利金、滑点、盈亏平衡或可靠Greeks。回避SC/BR短到期裸买/裸卖、把IV-RV正差当“贵”的充分证明、把OI/PCR当机构方向。当前无法证明期权优于期货。

## 九、21:00夜盘风险地图

**今晚无21:00夜盘。** 严格四层：

1. 中国完整EOD：9月30日；
2. 早前已完成Night：9月29日晚、归属9月30日，仅作历史；
3. 15:00—19:30海外：原油继续下跌、金银反弹、美元和收益率从高位回落；
4. 下一实际Night：10月8日21:00，归属10月9日；在此之前先有10月8日09:00日盘。

| 品种 | 下一日盘初步偏向 | 是否在旧Night完成定价 | 海外冲突 | 追首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|---:|---|
| RU2701 | 平/偏高但不确定 | 旧Night已完成大部上行 | 橡胶新价缺失 | 否 | 45m | SICOM、20,000、near-next |
| SC2611 | 偏低 | 旧Night弱但非当前事件 | 原油流恢复偏空、地缘偏多 | 否 | 30—45m | Brent、海湾流量、SC curve/VWAP |
| BU/TA | 偏低但产品物流抵消 | 锚点分歧 | 原油跌 vs 裂解/物流紧 | 否 | 45m | 裂解、加工差、近远月 |
| OI/P | 平/偏低 | OI旧Night后横盘 | 棕榈库存偏空 | 否 | 30m | OI/P/Y、仓单、现货 |
| BR | 平/偏低 | 旧Night强、日盘回吐 | 原油成本跌、橡胶未知 | 否 | 45m | RU/BR、16,050、curve |
| CU | 平开 | 旧Night几乎无增量 | LME小涨、美元回落 | 否 | 30m | LME、USD/CNH、back |
| AU/AG | 平/偏高 | 旧Night过时 | 金银反弹但5D弱 | 否 | 45m | DXY、实际利率、AG 15,000附近 |
| I/EC/LC | 不判断 | DCE缺/无夜盘 | proxy不充分 | 否 | 45m | exact contract、实体、量仓 |

当前地图不是10月8日有效条件单；10月8日08:45必须更新两天海外累计变化、USD/CNH和交易所参数。外盘变化没有被中国白天预交易，gap弹性不可由旧Night推算。

## 十、未来24小时/7日事件日历（北京时间）

| 时间 | 事件 | 处理 |
|---|---|---|
| 10月6日已发布 | [EIA STEO/Winter Fuels Outlook](https://www.eia.gov/outlooks/steo/) | 中期Brent锚约90/74；不直接映射短线SC |
| 10月7日22:30（常规窗口，以官网为准） | [EIA周度石油库存](https://www.eia.gov/petroleum/supply/weekly/schedule.php) | 重点看馏分油、炼厂开工；国内重开前降低能源Delta |
| 10月8日08:55/09:00 | 中国期货重开 | 全部条件重报价；延迟30—45分钟 |
| 10月8日21:00 | 中国夜盘恢复 | 用当日exact contract重新评估延续 |
| 10月10日00:00 | [USDA WASDE](https://usda.azureedge.us/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report) | 农产品Delta减半；期权仅限可核价定义损失结构 |
| 10月10日03:30（常规） | [CFTC COT](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) | 只作后验拥挤度，不推断国内资金身份 |
| 未来7日持续 | Hormuz/油轮袭击、运费、炼厂运行；东南亚橡胶天气 | 事件gap优先有限凸性；无报价则等待 |

未来7日内未核实到新的OPEC+/IEA定时会议；临时消息出现时须按实际发布时间重评。季节性只作先验。

## 十一、覆盖核对与旧建议台账

### 11.1 覆盖核对

| 板块 | 应覆盖 | 实际分析 | 数据不足 | 未入榜异常/无异常依据 |
|---|---:|---:|---|---|
| 黑色建材 | 10 | 10 | DCE Night/Options、basis多C | FG 5D -3.65%、SF ΔOI -10.47%，无三层共振 |
| 有色贵金属 | 14 | 14 | 当前USD/CNH、部分新代码历史短 | AG 5D -7.41%但OI增；AO去仓、AD roll |
| 能源炼化化工 | 26 | 26 | SC/LU实体、exact裂解/运费 | BU深back与大减仓、OP/AD roll、PX去仓 |
| 新能源 | 3 | 3 | LC实体与执行期权 | LC 5D -10.77%，无实体/波动确认 |
| 农产品 | 14 | 14 | DCE options、A/B basis | LG/B/CS去仓；更像去杠杆线索 |
| 航运软商品 | 10 | 10 | EC运价/舱位、部分期权 | AP 5D -3.15%但curve强；PK去仓 |
| **合计** | 原63代码+动态新增 | **77/77** | options 42/64产品成功、execution 0 | 无板块因未入榜而跳过 |

策略：方向、curve、basis、跨品种、跨市场、风格/中性、IV/skew/event convexity均已扫描；exact可执行RV为0。周期：1D/3D/5D/20D均在同合约可得处检查。缺口不缩小覆盖：无当前中国EOD/Night、22个期权产品失败/跳过、surface文件空、0 bid/ask、basis C、import parity不全、USD/CNH和橡胶精确价缺失。

### 11.2 旧建议台账

| idea_id | 首次提出 | 上次 | 当前 | 原因/处置 |
|---|---:|---|---|---|
| COM-E-RU2701-RUBBER-TIGHTNESS-20261001 | 10/1 | 75，等待 | 75，等待 | 无新橡胶价；触发/止损不重置 |
| COM-E-SC2611-SUPPLY-FADE-20261006 | 10/6 | 今晨仅供给尾险观察 | 67，节后反抽失败空观察 | 新数据：原油跌破100、流量恢复 |
| COM-E-DIESEL-LOGISTICS-20261005 | 10/5 | 62，待报价 | 65，待报价 | 新数据：原油/成品油恢复分化更清晰 |
| COM-E-OI701-RELSTRENGTH-20260930 | 9/30 | 65，等待 | 63，等待 | 棕榈回落与库存反证 |
| COM-E-BR2611-RELSTRENGTH-20260930 | 9/30 | 60，等待 | 59，观察 | 原油成本再跌、橡胶无新增 |
| COM-FU-SC-SPREAD-20260930 | 9/30 | 已取消 | 继续取消 | 工具错配；不得用新柴油RV恢复旧篮子 |

无成交反馈，不假设真实仓位；触发状态未知。风险预算：单一试仓计划损失NAV 0.25%—0.75%，确认交易0.75%—1.50%，单主题≤2.5%—3.0%；能源与橡胶各自合并。同因子压力覆盖一/两板、相关性破裂、错腿、流动性消失、保证金上调、IV跳变、交割挤压、人民币急变与长假累计gap。

A. 今晚没有应立即建立的新仓位。
B. 今晚只应挂条件单的仓位：无；中国休市，RU2701、SC2611及OI701方案均须10月8日重报价；柴油篮子缺同步bid/ask与参数。
C. 今晚应继续观察的机会：RU2701回踩强度、Brent跌破100后的SC价格弹性、原油/成品油恢复分化及柴油物流价差、金银反弹是否延续。
D. 今晚必须避免或退出的交易：裸多SC、追空节后首跳、追高RU/BR、抄底AG、恢复旧多FU/空SC、使用C级basis或无bid/ask期权建立所谓套利。