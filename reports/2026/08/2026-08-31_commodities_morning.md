---
report_date: 2026-08-31
edition: commodities_morning
generated_at_bjt: 2026-08-31T07:06:29+08:00
commodity_trade_date: 2026-08-28
commodity_data_fresh: true
commodity_history_record_count: 0
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-31

> **数据截点：** 中国基线为2026-08-28完整EOD；8月28日晚中国夜盘属于8月31交易日，只使用公开可验证行情并与EOD分开；海外实时层截至北京时间约07:06。China-Commodities-Engine核心五所EOD健康，但`report_input_latest.json`、`market_state_latest.json`和`options/surface_latest.json`仍为空，因此不生成伪造的3D/5D/20D、RV20、z-score或商品期权surface指标。

## 一、今日一句话结论

**今天有一个值得冒险的条件机会：SC2610回撤承接多。美伊冲突令Brent/WTI今晨跳涨逾2%，开始确认周五SC风险溢价；但不开盘追涨，JM等09:30 PMI，其他品种仍观察。**

## 二、数据质量与覆盖说明

第一读取层已读取`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。`report_input_latest.json`当前为空，因此按v2协议下钻。最近完整中国EOD仍为2026-08-28：SHFE、INE、DCE、CZCE、GFEX五所共803个期货合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，unknown/duplicate/invalid OHLC/negative volume-OI均为0；placeholder=5且不进入异常排行。

统一聚合层仍未恢复：`market_state_latest.json`为空。因此当前可靠使用的是2026-08-28具体合约1D、Volume、OI和near-next期货曲线；3D/5D/20D、RV20、volume/OI z-score、ΔOI z-score与price/OI quadrant均标记不可用。near-next curve只是期货期限结构，不等于现货基差；当前没有A/B级闭环basis可进入方向评分。

Physical requested_date=2026-08-28，20个目标仅4个映射，4个按原生频率fresh、0 stale、0 carried-forward。FG最新周度企业库存7404.9，较前周7441.4约-0.49%；TA最新周度加工费677.532元/吨，较前周586.52约+15.5%；JM的NBS焦煤现货仍是8月20日旬度2043.1元/吨、basis质量C，仅作context。周度/旬度fresh不等于今晨新发布。

External repo 22个目标仅6个映射、5 fresh、1 stale，仓库日频主要到8月27，因此今晨海外层用实时网页补充。北京时间约06:02，Brent报90.32美元/桶、+2.52%，WTI报85.41美元/桶、+2.41%；触发因素是美国周日打击霍尔木兹海峡Larak岛上的伊朗发射装置，且美方称其与布设水雷准备有关，伊朗革命卫队随后扬言报复。该信息是今晨最重要的新增价格与供应航运风险信号。

独立Options pipeline仍为2026-08-28：21,806个合约、370个series、61/64产品，IV coverage 98.59%、OI coverage 68.16%；但`surface_latest.json`为空，global `surface_ready=false`、`positioning_ready=false`、bid/ask coverage=0、`execution_ready=false`、dealer gamma direction unknown。因此本期不输出ATM IV、RR25、BF25、PCR、Dealer Gamma、具体strike、净权利金或滑点。

Contract metadata仍partial，DCE contract-info采集失败。SC参数另用INE官方最新公告核验；JM/SA动态保证金和当日限幅未在仓库闭环，正式下单前必须以交易所/终端为准。

## 三、商品市场仪表盘

| 板块 | 合约 | 8/28 EOD | 8/28夜盘/今晨海外 | 1D | Volume | OI | Curve / Physical | Options | 信号 |
|---|---|---|---|---:|---:|---:|---|---|---|
| 原油 | **SC2610** | close/settle **596.5/592.3** | 夜盘**614，+3.66%**；今晨Brent **90.32,+2.52%** | +3.97% | 153,166 | 43,480 | Contango约1.37%；Hormuz供应航运右尾上升 | surface unavailable | **73：回撤承接多，条件试仓** |
| 双焦 | **JM2701** | **1629/1623** | 夜盘主力约**+3.05%** | +2.32% | 1,039,129 | 597,545 | Back约1.53%；旬度现货仅context | surface unavailable | **69：PMI后回撤多观察** |
| 纯碱 | **SA701** | **1047/1027** | 夜盘主力约**+2.14%** | +3.05% | 1,902,641 | 1,154,367 | Contango约3.41%；repo无SA Physical映射 | surface unavailable | **65：squeeze失败空观察** |
| 贵金属 | **AG2610** | **17215/16818** | 周五夜盘约**-3.62%**；今晨海外金银精确价未可靠核验 | +3.15%日盘 | 765,356 | 261,945 | Contango约0.14%；偏鹰宏观与地缘避险冲突 | surface unavailable | **64：不追空** |
| PTA | **TA701** | **5630/5596** | — | +1.85% | 746,791 | 868,133 | Back约1.57%；周度加工费+15.5% | surface unavailable | **64：成本/curve多观察** |
| 玻璃 | **FG701** | **927/918** | 夜盘主力约**+2.61%** | +2.32% | 1,513,705 | 1,504,372 | Contango约2.67%；周度企业库存-0.49% | surface unavailable | squeeze，不追多也不按旧逻辑追空 |
| PVC | **V2701** | **4578/4520** | 夜盘主力约**+3.14%** | +2.58% | 1,061,521 | 1,214,734 | Contango约1.09%；Physical缺 | surface unavailable | squeeze观察 |
| 碳酸锂 | **LC2701** | **159600/156000** | — | +4.77% | 239,379 | 391,884 | Contango约1.15%；实体闭环不足 | surface unavailable | 高波动，不追涨 |
| 棉花 | **CF701** | **17180/17200** | — | +0.94% | 464,467 | 604,731 | Contango约1.64%；天气风险仅先验/context | surface unavailable | 天气多观察 |
| 乙二醇 | **EG2610** | **5053/5030** | — | -0.47% | 1,240,902 | 349,408 | Back约4.16%；Physical缺 | surface unavailable | 弱价格/紧curve冲突 |
| 燃料油 | **FU2611** | **3638/3670** | — | -1.33% | 1,041,002 | 227,418 | radar near-next曲线异常，弃用 | surface unavailable | 不做curve交易 |

## 四、相比上一交易日/今晨真正变化

**1. SC此前的“境内溢价是否过高”疑问，被今晨海外油价部分向上验证。** 周五SC2610夜盘已涨3.66%至614，而当时Brent周五收盘偏弱；今晨美伊冲突升级后Brent/WTI同步跳涨2%以上，说明内盘提前计入的地缘风险并非纯粹噪音。此前“SC溢价回吐空”不再是首选，方向切换为**只做回撤承接多**。

**2. 但SC依然不是开盘追涨交易。** 当前SC自身仍约1.37% Contango，且没有exact-contract、汇率、税费、运费、品质对齐的import parity。今晨新增的是“风险溢价获得外盘确认”，不是“现货短缺已被证明”。若09:00直接跳到625以上，赔率会显著恶化。

**3. 能源的第三层证据来自供应航运风险，而不是库存数据。** 美国打击Larak岛发射装置，美方称IRGC正准备部署海上水雷；伊朗革命卫队随后承诺报复。由于尚未验证实际通航量进一步恶化，这一层按Physical/logistics evidence计入但折扣，因此SC只给73，不给80+。

**4. JM仍被严格封顶69。** Price与Backwardation两层很强，但Physical仍是旬度context，无法凑第三层。今天09:30中国官方制造业PMI是需求闸门；Reuters调查中值49.6、前值49.2、仍低于50。若数据偏弱但JM开盘后45—60分钟拒绝下跌，信息含量反而高于PMI数字本身。

**5. AG空头清晰度下降。** 周五Warsh偏鹰后的金银去杠杆仍是事实，但今晨美伊冲突升级带来新的避险反向催化；本期又没有可靠核验到07:00附近海外金银精确报价，因此不能延续昨天的“失败反弹空”优先级，更不能低开追空。

**6. Engine核心EOD健康，但统一发布层仍未修复。** 今天不是中国EOD失败：8月28五所EOD完整可用；问题仍是`report_input / market_state / options surface`空文件。本期继续拒绝为完整表格伪造多周期和波动率指标。

## 五、产业链地图

| 产业链 | 当前方向 | 最强/最弱 | Price/Curve | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 原油—成品油 | **右尾上升，SC条件多** | SC最有信息量 | 中国夜盘强、SC自身Contango | Brent/WTI今晨+2%以上；Hormuz军事升级 | actual flow、exact parity、裂解 | 中高 |
| 双焦—钢材 | tape偏多 / Physical未闭环 | JM强 | JM价涨+Back | 09:30 PMI是需求闸门 | 铁水、利润、补库持续性 | 中 |
| 贵金属—美元—利率 | **双向冲突** | AG波动最大 | 周五夜盘已大跌 | 偏鹰利率冲击 vs 今晨地缘避险 | 当前海外金银可靠实时价、surface | 中低 |
| 纯碱—玻璃—PVC | squeeze / 基本面未确认 | FG/V/SA tape强 | 三者仍Contango | FG小幅周度去库；SA/V实体覆盖不足 | A/B basis、订单、检修兑现 | 中低 |
| PTA—聚酯 | 成本/curve偏多 | TA | Backwardation | 加工费周度显著上升 | PX/聚酯利润和终端订单闭环 | 中 |
| 农产品 | 天气风险先验 | CF | 仍Contango | 天气仅context | ICE/CBOT新鲜映射、高质量basis | 中低 |

当前regime：**Hormuz军事升级触发油价gap-up；中国工业品周五risk-on等待PMI需求检验；贵金属处于偏鹰利率与地缘避险的反向拉扯。**

## 六、机会排行榜

| 排名 | 机会 | 总分 | 方向 | 持有期 | 阶段 | 新鲜证据层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| **1** | **SC2610 回撤承接多** | **73** | Long | 1–3D | conditional_trial | **3** | curve仍Contango；无exact parity；实际通航恶化未确认 |
| 2 | **JM2701 PMI后回撤多** | **69** | Long | 1–3D | watch_only | 2 | Physical仅旬度context；开盘前已累积较大夜盘涨幅 |
| 3 | **SA701 squeeze失败空** | **65** | Short | 1–3D | watch_only | 1 | Price强烈反向；repo无SA Physical映射 |
| 4 | **AG2610 宏观空重评** | **64** | Short/Watch | Intraday–2D | watch_only | 1–2 | 地缘避险反向；07:00海外精确金银价未核验 |
| 5 | **TA701 成本/curve多** | **64** | Long | 1–3D | watch_only | 2 | 加工费改善不等于标的必涨；下游需求未闭环 |

没有80+确认交易。只有SC达到70—79区间，而且必须等开盘触发，不允许07:00预埋市价仓。

## 七、前三名交易卡

### 1. SC2610｜回撤承接多｜73

- **事实：** 8/28 EOD close/settle 596.5/592.3，日盘+3.97%；周五夜盘收614、+3.66%。今晨约06:02 Brent 90.32、+2.52%，WTI 85.41、+2.41%。
- **市场可能错在哪里：** 周五SC已经提前交易Hormuz升级，但市场可能仍低估实际水雷/报复导致的航运中断尾部；反面是目前尚无实际流量进一步恶化证据，且SC仍Contango。
- **新鲜证据层：** 价格层 + 海外定价层 + 供应航运事件层（第三层折扣）。
- **最佳表达：** 期货条件试仓；若盘中商品期权surface和可执行quote恢复，可研究有限风险Call Spread，但当前不报strike/权利金。
- **入场：** 09:00后至少等30—45分钟。首选回撤至606—612守住，再重新站上614和VWAP，同时Brent仍保持在约89.5以上/周五收盘上方明显区域；先1/3。
- **分批：** 620上方突破首45分钟高点，且海外油价未回吐、成交/OI不恶化，再加1/3；最后1/3只在实际Hormuz通航/供应扰动进一步确认时考虑。
- **初始止损：** 30分钟接受在600下方。
- **逻辑失效：** SC跌回592附近以下，同时Brent回落至约88.5以下，或出现可信的迅速降级/通航恢复证据。
- **TP1/TP2：** 628 / 645。
- **时间止损：** 1—2个交易日；若headline风险没有转化为持续价格强势，主动退出。
- **最大损失：** 0.35%—0.50% NAV；能源同因子合计≤0.75% NAV。
- **最坏情景/gap：** 周一高开后突然降级，或海外油价在中国开盘前快速回吐。**若SC直接开在625以上，不追，等待45—60分钟。**
- **合约参数：** 1000桶/手；tick 0.1元/桶，tick value 100元/手；按614名义约614,000元/手。INE 2026-06-23公告所列SC2610当前可核验涨跌停为±14%、一般持仓保证金16%（券商保证金可能更高）；夜盘21:00—02:30。最后交易日为交割月前一月最后交易日，实物交割；SC2610应在9月进入交割风险管理前主动规划移仓。
- **压力敏感度：** 以614仅作敏感度，一次不利14%约85,960元/手；两次连续向下14%复合约159,886元/手。不是官方最大损失估计。

### 2. JM2701｜PMI后回撤确认多｜69

- **事实：** 8/28 close/settle 1629/1623，日盘+2.32%，near-next Back约1.53%，周五夜盘主力约+3.05%。
- **市场可能错在哪里：** 如果弱PMI已被充分预期而盘面仍拒绝下跌，市场可能低估补库/供给约束；反面是当前实体层没有形成第三票。
- **新鲜证据层：** 价格—成交—持仓层 + curve层；Physical旬度数据只作context。
- **最佳表达：** 现在不下单。09:30 PMI后重新评分。
- **入场：** 09:45以后，回吐夜盘涨幅后仍守住1630附近，重新站上VWAP，且Back维持>1%。若PMI低于预期但价格不破1620，反而是更强的posterior信号。
- **分批：** 达到70后1/3；突破首小时高点且curve/OI继续确认再加。
- **初始止损：** 30分钟接受在1600下方。
- **逻辑失效：** 1585以下稳定 + Back明显压平/转Contango + 现货/库存方向转弱。
- **TP1/TP2：** 1700 / 1760。
- **时间止损：** 2—3个交易日不创新高退出。
- **最大损失：** 当前0；重新≥70后0.25%—0.35% NAV。
- **合约参数：** 静态交易单位60吨/手；当前DCE contract metadata采集失败，因此tick、动态保证金、动态限幅和当日夜盘参数在本报告不以旧值填补，开仓前必须由DCE/终端重新核验。按1629、60吨估算名义约97,740元/手。
- **交割/roll：** 远离2701交割月仍有时间，但若进入交割月前流动性迁移必须跟随主力滚动；不把近交割合约误当普通curve基准。

### 3. SA701｜squeeze失败空｜65

- **事实：** 8/28 close/settle 1047/1027，日盘+3.05%，近端Contango约3.41%，周五夜盘主力仍约+2.14%。
- **市场可能错在哪里：** 基本面宽松叙事可能最终重新主导，但当前最重要的事实是价格拒绝下跌；因此旧空头不能机械滚动。
- **新鲜证据层：** curve可用；Price当前与做空方向冲突；repo没有SA Physical映射，因此不计第三层。
- **最佳表达：** 只观察“squeeze失败”，不预埋空。
- **入场：** 至少等45分钟；只有反弹/高开失败、重新跌破1047和VWAP，同时Contango仍>3%，才重评是否升到70。
- **分批：** 重评≥70后1/3；1025以下且OI重新扩张才加。
- **初始止损：** 15—30分钟接受在1070上方。
- **逻辑失效：** 1080上方稳定 + curve显著收窄 + 后续库存/检修开始支持紧张。
- **TP1/TP2：** 1020 / 980。
- **时间止损：** 2个交易日不延续则退出。
- **最大损失：** 当前0；重新≥70后0.25%—0.35% NAV。
- **合约参数：** 静态规格20吨/手、tick 1元/吨、tick value 20元/手；1047对应名义约20,940元/手。仓库未闭环当前动态保证金/限幅，必须下单前核验；最后交易日为交割月第10个交易日，实物交割。夜盘时间和当日风险参数以郑商所最新交易日历/终端为准。
- **压力敏感度：** 不用静态±4%替代当日动态涨跌停，因此本期不输出1/2个停板损失的伪精确值。

## 八、商品期权专项

当前结论仍是：**raw chain有，surface与execution没有。**

2026-08-28链覆盖21,806个合约、370个series、61/64产品，IV字段覆盖率98.59%；但`surface_latest.json`为空、positioning coverage不足、bid/ask=0、execution not ready。故不能声称“全市场最高/最低IV”，也不能输出IV-RV、RR25/BF25、PCR或Dealer Gamma方向。

如果盘中surface和人工可执行quote恢复，研究优先级是：**SC确认后的Call Spread > JM确认后的Call Spread > SA squeeze失败后的Put Spread**。固定执行纪律：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、9:00开盘风险地图

| 品种 | 可能开盘形态 | 主要风险 | 等待时间 | 最关键确认 |
|---|---|---|---:|---|
| **SC2610** | 高开概率高 | 追涨后headline回吐 | **30—45分钟；>625等60分钟** | 606—612承接、614/VWAP、Brent是否仍强 |
| **JM2701** | 高开/强震荡 | 09:30 PMI打断趋势 | **45—60分钟** | PMI后1620—1630是否守住、Back是否>1% |
| **SA701** | squeeze延续或冲高回落 | 旧空头过早重启 | **45分钟** | 1047与VWAP、Contango是否仍深 |
| **FG/V** | 周五强势延续 | 把squeeze误判成短缺 | **45分钟** | OI、curve、库存/订单是否跟上 |
| **AG/AU** | 可能受避险支撑 | 偏鹰空头与地缘避险冲突 | **45分钟** | 先核验海外实时金银/美元，再决定方向 |
| **CF701** | 温和偏多/震荡 | 天气叙事未获curve确认 | **30分钟** | 价格能否让Contango收窄 |

## 十、未来24小时与7天事件

| 北京时间 | 事件 | 主要品种 | 处理 |
|---|---|---|---|
| **08/31 09:30** | 中国8月官方制造业PMI；Reuters调查中值49.6 | JM/J/RB/HC/I/FG/SA/CU | JM至少等数据后15分钟；弱数据打不下去才是多头确认 |
| **持续** | Larak/Hormuz冲突、伊朗报复与通航情况 | SC/LU/FU/BU/PG | 控制gap；优先有限风险，避免追高 |
| **09/01 04:00** | USDA Crop Progress | C/CF/大豆油粕映射 | 农产品Delta控制；天气交易不裸追 |
| **09/02 22:30** | EIA Weekly Petroleum Status Report | SC/FU/LU/BU/PG | 关注原油/成品油库存分化，减少裸事件风险 |
| **09/04 20:30** | 美国8月非农 | AU/AG/CU/原油/美元 | 控制美元/实际利率重复风险 |
| **09/05 03:30** | CFTC COT | 全球商品 | 仅用于拥挤背景，不把分类持仓等同最终客户方向 |

## 十一、风险预算

今天唯一70+是SC条件交易，但**A类立即仓位仍为0**。SC触发后单笔最大损失0.35%—0.50% NAV；JM/SA若盘中重新达到70，只给0.25%—0.35% NAV试仓。能源同因子SC/LU/FU/BU/PG合计≤0.75%；黑色JM/J/RB/HC/I合计≤0.75%；地产化工SA/FG/V合计≤0.60%；贵金属美元/实际利率+地缘避险因子≤0.50%。

最重要的压力测试是：SC在高开后出现快速外交降级、保证金进一步上调或夜盘gap；JM则是PMI与工业beta反向冲击。今天不允许把“有一个73分机会”理解成“开盘就必须有仓”。

## 数据与模型说明

事实数据、市场定价、模型推断与主观判断已分开。期货curve不等于现货basis；Physical的周度/旬度fresh不等于今晨发布；`surface_ready=false`时不生成ATM IV/偏度；报告不使用拼接主力构造多周期收益。当前`market_state_latest.json`为空，因此所有3D/5D/20D与z-score均主动省略。

## 关键来源

- China-Commodities-Engine：<https://github.com/farfromexact/China-Commodities-Engine>
- Reuters｜Oil jumps more than 2% after US attack on Iran's Larak island：<https://www.reuters.com/business/energy/oil-jumps-more-than-2-after-us-attack-irans-larak-island-2026-08-30/>
- Reuters｜US forces strike two Iranian launchers on Larak island：<https://www.reuters.com/world/middle-east/us-forces-strike-two-iranian-launchers-irans-larak-island-us-official-says-2026-08-30/>
- Reuters｜Iran's Revolutionary Guards vow response：<https://www.reuters.com/world/middle-east/irans-revolutionary-guards-vow-response-us-attack-larak-island-2026-08-30/>
- Reuters｜China's factory activity seen contracting again in August：<https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/>
- INE交易时间：<https://www.ine.cn/services/calenderandholidays/tradinghours/>
- INE 2026-06-23 SC/LU风险参数公告：<https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html>
- EIA Weekly Petroleum Status Report schedule：<https://www.eia.gov/petroleum/supply/weekly/schedule.php>
- USDA Crop Progress：<https://esmis.nal.usda.gov/publication/crop-progress>
- BLS Employment Situation schedule：<https://www.bls.gov/schedule/news_release/empsit.htm>
- CFTC COT release schedule：<https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm>

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：SC2610回撤承接多（需09:00后30—45分钟确认；若直接高开>625不追）。**  
**C. 今天应继续观察的机会：JM2701 PMI后回撤多、SA701 squeeze失败空、TA701成本/curve多、AG2610偏鹰宏观空与地缘避险冲突。**  
**D. 今天必须避免或退出的交易：追SC高开、PMI前追JM、机械滚动旧SA/FG/V空头、未核验当前海外金银报价就追空AG，以及任何基于空surface/零bid-ask的精确商品期权交易。**