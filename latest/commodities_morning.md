# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-26

> revision: 2  
> generated_at_bjt: 2026-08-26T07:30:21+08:00  
> data_protocol_version: china_commodities_v2

## 一、今日一句话结论

**今天有值得冒险的机会，但只剩两张70+条件单：V2701反弹失败空 > FG701反弹失败空；EG2610夜盘大跌后从多头降级观察，能源不接第一刀。**

昨日日盘最强的EG/FU在8月25日夜盘出现剧烈风险溢价回吐：人民财讯23:04确认燃油、低硫燃油跌超5%、乙二醇跌超3%。这使昨日“紧库存+Back就直接做多”的逻辑失去最新价格层确认。今天真正值得承担风险的是**弱需求、高库存、Contango仍在的PVC/玻璃反弹失败空**，而不是追杀已经大跌的能源化工。

## 二、数据质量与覆盖说明

本期第一读取层来自 `farfromexact/China-Commodities-Engine` main：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；Top候选再按需读取Market State、Physical、External、Options surface/quality、Contract Metadata。统一输入 `requested_date=2026-08-25`，`generated_at=2026-08-26T06:30:05.882004+08:00`。

中国核心期货为8月25日完整EOD：SHFE、INE、DCE、CZCE、GFEX五所齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；unknown/duplicate/invalid OHLC/negative volume-OI均为0；7条placeholder已经排除异常排名；核心carried-forward为0。Market State已有20个有效交易日，可以使用同合约1/3/5/20D、RV20、volume/OI、ΔOI和curve，不拼接连续主力收益。

Physical原生覆盖仍只有4/20。FG拥有可解释的最新周度厂库方向与同比；EG和PVC实体层由明确标注的商业产业数据补充，不冒充交易所仓单。JM basis仍为C级context，不计方向评分、不称套利。

晨间External已在06:30重建：22个目标仅6个映射，5个按自身lag仍fresh、1个stale，无可执行import parity。海外层因此同时使用8月25日欧美收盘和8月26日06:40附近Reuters信息补齐；`context_only`价格不写成跨市场套利。

Options独立流水线日期为2026-08-25：22,014条合约、约59/64品种成功、369个series，其中362 `surface_ready`、71 `positioning_ready`、**0 `execution_ready`**，bid/ask coverage=0。由于今天已经进入8月26日中国交易日，全部期权surface只作为T-1波动率背景，**不计今日fresh evidence**。任何期权结构均遵守：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

Contract Metadata为partial/error：DCE contract-info本次失败，GFEX存在partial/date问题。因此V2701、EG2610等大商所合约的当前动态交易所保证金/涨跌停不拿旧值硬填；broker margin同样需下单前核验。

仓库明确没有中国分钟、逐笔或夜盘session产物。中国夜盘只引用可验证外部来源并与EOD严格分开：人民财讯用于确认涨跌方向；个别精确价使用第三方同步代理，仅作为gap proxy，**不是交易所官方结算/收盘**。

## 三、商品仪表盘

| 板块 | 合约 | 8/25 EOD Close/Settle | 1D / 5D | Volume / OI / ΔOI | Curve / Physical | 夜盘/海外新信息 | T-1 Options | 信号 |
|---|---|---:|---:|---|---|---|---|---|
| 能化 | **V2701** | 4539 / 4576 | **-2.08% / -3.48%** | 133.6万 / 117.2万 / **+17.99万(+18.14%)** | 近端Contango约-0.85%；PVC库存高、需求弱 | 第三方同步代理约4523，较结算-1.16%；V2702约4559，主次月约-0.79% | ATM4600 IV18.47%，IV-RV +6.82vol；surface✓/positioning×/execution× | **第一优先：反弹失败空** |
| 建材 | **FG701** | 913 / 916 | **-0.76% / -0.22%** | 124.5万 / 150.8万 / **+2.82万(+1.90%)** | Contango约-3.34%；厂库7441.4万重箱，同比+17.41% | 第三方同步代理约911，较结算-0.55% | surface可研究；execution× | **第二优先：反弹失败空** |
| 能化 | **EG2610** | 5364 / 5497 | **+3.25% / +10.69%** | 185.9万 / 36.15万 / **+1.81万(+5.27%)** | 主次月Back日盘约+6.26%；港口库存20.6万吨、快速去化 | 人民财讯：夜盘跌超3%；同步代理约5281，较结算-3.93%；EG2611约4996，Back仍约+5.70% | ATM5500 IV40.30%，IV-RV +5.10vol；surface✓/positioning✓/execution× | **多头失去价格确认，观察** |
| 能源 | **FU2611** | 3842 / 3935 | **+2.96% / +6.27%** | 日盘异常放量；ΔOI +2236(+0.79%) | 自动近月curve受交割月扭曲，不作普通curve证据 | 人民财讯：夜盘燃油跌超5%；同步代理约3738，较结算-5.01%；WTI 06:40附近继续下跌 | T-1 surface；execution× | **不接第一刀，也不追空** |
| 能源 | SC2610 | 仓库8/25 EOD有效 | — | 仓库有效 | 需结合海外油 | 夜盘媒体约-0.98%、587.8；Brent 8/25结算88.58、WTI82.36；06:40附近WTI约80.99 | — | 外油继续去风险，观察 |
| 贵金属 | **AG2610** | 16631 / 16775 | **-0.65% / +4.22%** | ΔOI **-1.60万(-5.37%)** | 轻Contango约-0.39% | 同步代理约16751，较结算-0.14%；PCE前不追方向 | T-1上行vol仍昂贵；execution× | 趋势仍强但拥挤降温 |
| 有色 | **CU2610** | 107980 / 108160 | **+0.38% / —** | ΔOI **+1.27万(+6.60%)** | 轻Back约+0.15%，不足以单独确认 | 同步代理约108700，较结算+0.50%；LME铜逼近历史高位但美国库存迁移扭曲显著 | T-1 | **不追LME事件beta** |
| 黑色 | I2701 | 约713.5 / 716.5 | +0.14% / — | 仓库有效 | 港库/到港仅周度context | 可靠夜盘精确价本期未确认 | T-1 | 中性 |
| 新能源 | **LC2701** | 150280 / 153960 | **-3.79% / -0.89%** | ΔOI -1.37% | 仍Contango；实体锂库存闭环不足 | 夜盘精确价本期未确认 | ATM154000 IV37.13%，IV-RV +5.83vol；execution× | **价格反转，不称短缺** |
| 建材 | SA701 | 1045 / 1046 | -1.04% / — | 仓库有效 | Contango约-3.26% | 夜盘精确价未确认 | T-1 | 偏弱但无独立edge |
| 农产品 | RM611 | 2243 / 2236 | -0.18% / — | 仓库有效 | 近期price/curve曾冲突 | 夜盘精确价未确认 | T-1 | No-Trade |
| 航运 | EC2610 | 1894 / 1946.5 | -1.49% / **+10.91%** | 高波动 | 事件驱动，不用普通curve | Hormuz通航谈判与油轮受袭同时存在 | 无执行级vol | **45分钟观察，不追** |

未进入表格的I/JM/J/RB/HC、CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU、SC/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/EB/RU/NR/BR/SH/UR/SP、SI/PS，以及全套油脂饲料畜牧软商品仍在五所全市场扫描范围内；未出现比V/FG/EG更高质量的70+独立证据组合。

## 四、相比上一交易日真正变化

**1. 最大变化不是日盘，而是夜盘：EG/FU多头被最新价格层否定。** 8月25日日盘EG仍是价涨仓增、近远月Back和低库存共振，但当晚人民财讯确认EG跌超3%、FU/LU跌超5%。这不是小噪音，而是地缘成本溢价快速回吐后的regime切换。EG的低库存和Back没有消失，但“立即/回撤做多”的最新价格确认已经消失。

**2. PVC从普通弱势升级成今天最干净的条件空头。** V2701日盘跌2.08%、OI单日增18.14%，近端仍Contango；夜盘代理继续弱约1.16%。与此同时最新周度PVC华东+华南社会库存117.92万吨，周环比-1.31%却同比+37.49%，下游平均开工率约39.18%，需求端仍弱。这里的关键不是“库存周周增加”，而是**高库存绝对/同比水平 + 弱下游 + 价格/curve同向**。

**3. FG继续弱，但低价使赔率不如PVC。** FG701日盘价跌仓增、curve Contango约3.34%，夜盘代理再跌约0.55%；最新周度厂库7441.4万重箱仅环比-0.07%，同比仍+17.41%，库存天数34.1天。空头结构成立，但900附近全产业链亏损和冷修反身性提高，所以只能等反弹失败，不能低开追空。

**4. 国际原油继续跌，说明市场正在交易“有限制裁+潜在通航”，而不是单向供应灾难。** 8月25日Brent收88.58美元/桶、WTI收82.36，分别大跌；8月26日06:40附近Reuters又报WTI约80.99、再跌约1.7%。伊朗与阿曼讨论临时Hormuz航道和扫雷，但大部分航运仍受限、附近又有油轮受袭，因此能源的方向风险变成**低概率高损失上行尾部 + 当前价格下行**。

**5. 铜是“高价但不是纯短缺”。** Reuters称LME三个月铜8月25日一度至14,343美元/吨附近，同时COMEX库存升至纪录675,185吨并连续46日增加；美国潜在关税正在搬运区域库存。沪铜夜盘代理偏强，但这种跨市场错配不等于全球物理短缺，不适合在历史高位追beta。

## 五、产业链地图

**最值得交易的弱链：PVC—地产建材。** V的price/OI、Contango和实体库存/下游三个fresh层同向，置信度高于其他弱品种。最大反证是产业链持续亏损、成本上升和去库仍在进行；因此做的是“反弹失败”，不是趋势无脑追空。

**次弱：浮法玻璃。** FG的价格—OI、curve和高同比厂库同向。Physical不是“重新累库”，而是库存仍处高水平且本周几乎没有真正去化；同时未来供应有点火回升预期。最大缺失是高频终端订单和供给冷修兑现速度。

**最强实体链但当前不是最佳交易：乙二醇。** 港口库存20.6万吨，四日下降6.2万吨，近五年同期低位；夜盘后EG2610-2611仍约5.7% Back。这说明tightness真实存在。但最新价格剧烈下跌，市场正在重估进口/地缘溢价，故从“多头交易”降级为“等价格重新确认”。

**能源：从供应冲击趋势切换为去风险。** 外油和中国夜盘同向下跌，价格最新层明显偏空；但Hormuz仍未正常化，尾部反向跳升风险很高。此时裸追空FU/SC的风险回报也不够好，最优行为是等待45分钟。

**有色/贵金属：等待宏观事件。** 铜的高价带有美国关税库存迁移因素；AG仍有强20D趋势但日盘OI下降，且今日20:30 PCE/GDP会直接冲击美元、实际利率与Vega。今日早盘不应为了方向感而提前放大仓位。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段/工具 | 最大损失 | Fresh证据层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| 1 | **V2701 反弹失败空** | **79** | 空 / 1–5D | 条件试仓；期货为主 | 0.30%–0.45% NAV | **3**：price/OI、curve、physical | 周度库存仍小幅去化；Options T-1且positioning×；DCE动态参数缺 |
| 2 | **FG701 反弹失败空** | **76** | 空 / 1–5D | 条件试仓；期货为主 | 0.25%–0.40% NAV | **3**：price/OI、curve、physical | 低价/亏损下供应收缩尾部；动态参数需复核 |
| 3 | **EG2610 价格恢复后的多头观察** | **69** | 多观察 / 1–2D | 仅观察；不预挂 | ≤0.25% NAV（若重新触发） | **2个支持层**：curve、physical；price最新层冲突 | 夜盘大跌；事件beta高；动态参数缺 |
| 4 | CU2610 高位强势但不追 | 68 | 观察 / 1–3D | No-Trade | — | 2 | LME/COMEX库存迁移扭曲，宏观事件前 |
| 5 | FU2611 暴跌后双向观察 | 66 | 观察 / Intraday–2D | No-Trade | — | 方向冲突 | 夜盘>5%跌幅；Hormuz尾部仍在 |

评分拆解上，V为逻辑23/25、赔率20/25、催化12/20、price-curve/vol14/15、拥挤技术10/15；FG为21/19/12/13/11。**今天没有80+确认加仓交易。**

## 七、前三名交易卡

### 1. V2701｜79分｜反弹失败空

**事实。** 8月25日close/settle 4539/4576，1D -2.08%、3D -3.03%、5D -3.48%、20D -2.03%，RV20约11.64%。成交约133.6万手、OI约117.2万手，ΔOI +179,942手/+18.14%，是显著的“价跌仓增”归因线索，但不把它写成确定“新空入场”。repo近端V2609-2610约-0.85% Contango；夜盘同步代理V2701约4523、V2702约4559，主次月仍约-0.79% Contango。最新周度PVC华东+华南社会库存117.92万吨，环比-1.31%、同比+37.49%；下游平均开工率约39.18%，仍偏低。

**市场已经定价：** 地产/型材/管材弱需求与高库存已反映在低绝对价格中。  
**市场可能错在：** 市场仍低估供应恢复和库存压力，反弹后可能继续寻找更低现金流平衡价格。  
**主观判断：** 空头有edge，但成本端抬升、生产亏损和连续窄幅去库意味着不能追低。

**最佳表达：** V2701小期货空仓；若8月26日fresh option chain恢复真实bid/ask，再比较Put Spread。T-1 V2701期权expiry 2026-12-16、ATM 4600、ATM IV18.465%、RV20 11.6425%，IV-RV +6.82vol、RR25 +3.91、BF25 +0.39，surface_ready=true、positioning_ready=false、execution_ready=false。因此不报净权利金/精确Greeks/滑点。

**入场与分批：** 09:00后至少等30分钟。优先等4535–4570反弹失败并重新跌回4520/VWAP下方，先空1/2；再跌破4490且OI没有快速塌缩、Contango未明显收窄，再加1/2。若直接开在4490以下或gap约>1.5%，等待45分钟，不追第一波。

**初始止损：** 4625上方形成15分钟接受。  
**逻辑失效：** 稳定站上4660，同时后续库存去化明显加快、下游开工/订单持续回升、curve明显收窄。  
**TP1/TP2：** 4450 / 4320。  
**时间止损：** 3个交易日不能有效创新低即退出。  
**风险预算：** 初始最大损失0.30%–0.45% NAV。

**合约参数：** DCE PVC合约5吨/手，tick 1元/吨，tick value 5元/手；按夜盘代理4523计算notional约22,615元/手。repo本期DCE动态metadata失败，因此**当前交易所保证金、broker margin、price limit参数未确认**；夜盘标准时段通常为21:00–23:00，但正式下单前仍在交易所/终端复核。交割为实物交割，持有期仅1–5D，避免进入交割风险窗并提前roll。由于当前涨跌停未官方确认，不把假设值伪装成压力结果；仅作敏感性参考，若价格单日逆向+6%（不是声称当前涨停），损失约1,357元/手；连续两日各+6%复合约2,795元/手。

**1–20D催化：** 地产需求、PVC开工恢复、库存周报、成本电石/乙烯、印度/出口政策。  
**最坏情景：** 宏观政策驱动地产链short squeeze + 上游亏损快速降负 + margin上调。  
**放弃条件：** 开盘直接大幅低开且无反弹；或curve/库存开始持续改善。

### 2. FG701｜76分｜失败反弹空

**事实。** 8月25日close/settle 913/916，1D -0.76%、5D -0.22%、20D约-4.98%，RV20约17.12%；成交约124.5万手、OI约150.8万手，ΔOI +28,183/+1.90%，同样是价跌仓增线索。curve约-3.34% Contango。8月20日隆众81家样本厂库7441.4万重箱，周环比-0.07%、同比+17.41%，库存天数34.1天；夜盘第三方同步代理约911，较EOD结算-0.55%。

**市场已经定价：** 需求疲弱和高库存已经把价格压到低位。  
**市场可能错在：** 市场对供应端点火恢复和需求回升的速度仍过于乐观。  
**主观判断：** 弱势成立，但900元/吨附近产业亏损使下方凸性不如V，所以只在反弹失败时做。

**最佳表达：** FG701期货空；fresh chain有可执行bid/ask后再比较Put Spread，当前不报权利金。

**入场与分批：** 等30分钟。915–925反弹失败、重新跌回910/VWAP下方先空1/2；跌破900且OI没有异常流失再加1/2。若直接低开<895，等待45分钟、不追。

**初始止损：** 934上方形成15分钟接受。  
**逻辑失效：** curve显著收窄/翻Back，同时周度厂库加速去化、深加工订单持续改善或冷修明显超预期。  
**TP1/TP2：** 895 / 875。  
**时间止损：** 3个交易日。  
**风险预算：** 0.25%–0.40% NAV。

**合约参数：** CZCE玻璃20吨/手、tick 1元/吨、tick value 20元/手；按夜盘代理911计算notional约18,220元/手。当前动态exchange margin、broker margin和price limit未取得同等级官方最新确认，不硬填。通常有夜盘，持有期远离交割月份；精确last trading day/交割参数下单前复核。仅作非监管敏感性参考，若价格单日逆向+8%（不是声称当前涨停），损失约1,458元/手；两日各+8%复合约3,032元/手。

**1–20D催化：** 厂库周报、产线点火/冷修、深加工订单、地产政策。  
**最坏情景：** 低价触发集中冷修 + 政策beta + 资金short squeeze。  
**放弃条件：** 930上方直接强势接受或库存快速去化。

### 3. EG2610｜69分｜观察，取消昨日优先多头

**事实。** 8月25日close/settle 5364/5497，1D +3.25%、3D +7.81%、5D +10.69%、20D +18.55%，RV20约35.20%；成交约185.9万手、OI 36.15万手，ΔOI +18,094/+5.27%。8月24日华东主港商业库存20.6万吨，较8月20日下降6.2万吨，处于近五年同期低位。8月25日日盘主次月Back约6.26%。但当晚人民财讯确认EG跌超3%，第三方同步代理EG2610约5281、较结算-3.93%，EG2611约4996，Back仍约5.70%。

**核心矛盾：** Physical+curve仍紧，但最新price层已经反向。**昨天的多头逻辑不能直接沿用。**

**最佳表达：** 09:00不下单。只有在45分钟后出现“5250–5300被吸收→重返5350→再站上5400/VWAP”，同时2610-2611 Back仍大致维持5%附近、亚洲油价停止下跌，才允许把它重新升级为最多0.25% NAV的探索性多头。

**若重新触发多头：** 15分钟接受在5220下方先止；5200进一步失守、Back明显压缩且现货/库存tightness弱化则逻辑失效。TP1 5500，TP2 5650，1–2D不延续退出。反过来，只有跌破5200后形成接受、Back明显压缩、Physical也转松，才考虑空头；否则在低库存+Backwardation中追空gap也没有赔率。

**合约参数：** DCE EG 10吨/手、tick 1元/吨、tick value 10元/手；按代理5281 notional约52,810元/手。当前DCE动态margin/limit未确认；物理交割，短持仓避免进入交割风险窗。T-1 EG2610期权expiry 2026-09-16、ATM5500、ATM IV40.295%、RV20 35.1985%，IV-RV +5.10vol、RR25 -2.31、BF25 +2.30，surface_ready=true、positioning_ready=true、execution_ready=false。若价格恢复，Call Spread优先于裸Call，但必须等fresh quote。

**最坏情景：** 假跌破后低库存挤压重新启动，价格急速反抽并触发margin上调。

## 八、商品期权专项

今天不能称“8月26日实时全市场最高/最低IV”，只能称**8月25日T-1代表样本**。全市场约362/369 surface-ready、71/369 positioning-ready、0/369 execution-ready；bid/ask coverage=0。因此期权适合做结构研究，不适合在报告里制造可成交价格。

- **V2701：** ATM4600 IV18.465% vs RV20 11.6425%，IV-RV +6.82vol，RR25 +3.91，BF25 +0.39；偏空方向若确认，Put Spread优先于裸Put以压低Vega成本，但positioning不完整。
- **EG2610：** ATM5500 IV40.295% vs RV20 35.1985%，IV-RV +5.10vol，RR25 -2.31，BF25 +2.30；波动率不算便宜，且今早方向冲突，先等标的重新确认。
- **LC2701：** ATM154000 IV37.125% vs RV约31.30%，IV-RV +5.83vol，RR25 -3.23，BF25 +5.83；价格大跌+contango，且Physical不足，不因高波动去猜“锂短缺”。
- **AG：** T-1上行vol/skew仍明显偏贵，且20:30 PCE前Vega事件溢价值得尊重。若看多，有限风险Call Spread/Fly优先于裸Call。

必须回避：零bid/ask环境下给净权利金；把partial OI/PCR写成拥挤结论；Dealer Gamma方向推断；AP/CJ/PL/PR/ZC等source-date异常品种的新方向期权仓；裸卖地缘尾部Vega。

## 九、9:00开盘风险地图

| 品种 | 中国8/25 EOD基线 | 可验证夜盘/代理 | 07:00附近外盘映射 | 9:00处理 |
|---|---|---|---|---|
| **V2701** | settle4576 | 代理4523，约-1.16% | 原油弱，对PVC成本/情绪偏空但非一对一 | 等30分钟；<4490直接开等45分钟，不追；优先4535–4570反抽失败 |
| **FG701** | settle916 | 代理911，约-0.55% | 无可靠直接外盘锚 | 等30分钟；<895等45分钟；915–925失败最优 |
| **EG2610** | settle5497 | 人民财讯跌超3%；代理5281，约-3.93% | 外油继续下行 | **等45分钟**；不接第一刀，不在Back+低库存下追空；先看5350/5400能否收复 |
| **FU2611** | settle3935 | 人民财讯跌超5%；代理3738，约-5.01% | WTI约80.99、06:40附近再跌约1.7% | **等45分钟**；多空都不追，先看外油是否止跌及国内Opening Range |
| SC2610 | EOD有效 | 夜盘媒体约587.8/-0.98% | Brent/WTI显著走弱 | 45分钟；Hormuz headline使追空尾部危险 |
| **AG2610** | settle16775 | 代理16751，约-0.14% | PCE前美元/实际利率主导 | 30分钟；异常gap则45分钟；不裸买高IV Call |
| **CU2610** | settle108160 | 代理108700，约+0.50% | LME高位但COMEX库存迁移扭曲 | 30分钟；不追高，观察OI与沪伦结构 |
| LC/EC | EOD高波动 | 夜盘精确价未确认 | 地缘与宏观混合 | 统一45分钟；先看curve和Opening Range |

今天Opening Range之后最重要的posterior更新不是“新闻条数”，而是：**V/FG反弹能否站上VWAP、ΔOI是否保持；EG/FU暴跌后是否出现承接；curve是否与价格重新同向。**

## 十、未来24小时 / 7日事件日历（北京时间）

**8月26日20:30：美国7月Personal Income and Outlays / PCE，同时发布二季度GDP Second Estimate及Corporate Profits。** 对DXY、实际利率、AU/AG、CU以及跨资产Vega是一级事件。贵金属和有色若日内已有盈利，事件前降低裸Delta/裸Vega。

**8月26日22:30：EIA Weekly Petroleum Status Report。** 对SC/FU/LU/BU、原油裂解与能化成本链是一级Delta事件；能源早盘若已经经历大gap，更不适合在EIA前把方向仓放大到主题上限。

**8月27–29日：Jackson Hole Economic Policy Symposium。** Kansas City Fed确认2026年主题为“Financial Innovation: Implications for Payments and Policy”。所有美元/利率敏感商品都应把讲话时点视为Vega事件窗口。

**8月29日03:30：CFTC COT。** CFTC 2026日历列8月28日发布，美东15:30，即北京时间次日03:30；只作滞后拥挤背景，不当作实时flow。

**9月1日04:00：USDA NASS Crop Progress（8月31日16:00 ET）。** 在本7日窗尾部，影响玉米、大豆、棉花等天气/作物条件；农产品新仓应等最新作物进展，而不是仅凭季节性先验。

**持续非定时风险：Hormuz临时航道谈判、扫雷、二级制裁执行、油轮受袭。** Reuters 8月25日确认伊朗与阿曼讨论临时航道，但多数航运仍受限、附近油轮受袭。能源当前price trend向下，尾部却仍可能突然向上，最适合的风险管理是缩小裸Delta、保留有限凸性，而不是在大跌后加杠杆追空。

## 十一、风险预算与行动清单

V试仓最大损失0.30%–0.45% NAV；FG 0.25%–0.40%；EG只有价格重新确认后才允许≤0.25%探索仓。地产需求因子V+FG+SA不能当完全独立仓位，初始合并主题风险建议≤0.75% NAV；能源/能化地缘因子EG+FU+SC+LU+BU合并计算。今天没有80+确认交易，不使用0.75%–1.50%的确认仓预算。

压力测试必须覆盖：两日连续不利大波动、相关性破裂、开盘流动性消失、夜盘gap、保证金上调、PCE/EIA前后IV跳升/坍塌、交割挤压、人民币急变，以及中国休市期间海外Hormuz headline。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：V2701反弹失败空；FG701反弹失败空。  
C. 今天应继续观察的机会：EG2610在45分钟后重新收复5350/5400的恢复多头；CU2610高位强势但不追；FU2611暴跌后的双向承接。  
D. 今天必须避免或退出的交易：沿用昨日EG/FU多头直接接第一刀、低开追空V/FG、追LME铜高位、裸买事件溢价很高的AG Call、任何C/D级basis或context-only跨境价差“套利”。

## 主要来源

- China-Commodities-Engine report input: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json
- China-Commodities-Engine status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json
- China-Commodities-Engine radar: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json
- China-Commodities-Engine options surface: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json
- 人民财讯，2026-08-25 23:04，国内期货夜盘收盘: https://stcn.com/article/detail/4121066.html
- 人民财讯，2026-08-25 21:04，国内期货夜盘开盘: https://stcn.com/article/detail/4120627.html
- Reuters，2026-08-25，Oil settles down more than 3%: https://www.reuters.com/business/energy/oil-prices-steady-investors-weigh-impact-expanded-us-sanctions-against-iran-2026-08-25/
- Reuters，2026-08-25，Iran and Oman discuss temporary Hormuz corridor: https://www.reuters.com/world/china/iran-oman-discuss-temporary-hormuz-corridor-impasse-with-us-drags-2026-08-25/
- Reuters，2026-08-25，US tariff threat upends copper surplus: https://www.reuters.com/business/us-tariff-threat-upends-copper-surplus-prices-test-all-time-peak-2026-08-25/
- 隆众/Mysteel，2026-08-20，浮法玻璃样本企业库存: https://www.mysteel.com/oilchem/a/26082016/2D4AB63D4A779922.html
- PVC库存/需求汇总（引用隆众），2026-08-21: https://goodsfu.10jqka.com.cn/20260821/c679170626.shtml
- 乙二醇港口库存产业信息，2026-08-24/25: https://finance.sina.com.cn/money/future/fmnews/2026-08-24/doc-inipkzxw2942246.shtml
- BEA release schedule: https://www.bea.gov/news/schedule/
- EIA Weekly Petroleum Status Report: https://www.eia.gov/petroleum/supply/weekly/index.php
- Kansas City Fed Jackson Hole FAQ: https://www.kansascityfed.org/research/jackson-hole-economic-policy-symposium/jackson-hole-faqs/
- CFTC COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- USDA NASS August 2026 calendar: https://data.nass.usda.gov/Publications/Calendar/reports_by_date.php?js=1&month=08&view=l&year=2026
