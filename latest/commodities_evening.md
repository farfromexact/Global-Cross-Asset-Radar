# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-31

## 一、今日一句话结论

**今日商品期货期权无合格交易。** 8/31中国EOD未入库且关键汇总文件为空；Brent 17:03已涨3.58%，但缺今日SC结算/OI/curve，禁止拿8/28数据替代。

当前regime：**data-quality veto / Hormuz supply-risk rally / PMI“改善但仍收缩” / 贵金属利率—避险双向冲突**。最强外部链是原油—航运供给风险；最不值得做的是在缺少今日中国结算、持仓和curve的情况下追国内首跳。

## 二、数据质量与覆盖说明

本次首先通过已连接GitHub读取 `farfromexact/China-Commodities-Engine`。四个关键现状构成硬性数据闸门：

- `data/report_input_latest.json`：当前为空文件；无法取得8/31 `requested_date/generated_at/module_freshness`。
- `data/latest.json`：当前为空文件。
- `data/market_state_latest.json`：当前为空文件，因此8/31同合约1D/3D/5D/20D、RV20、volume/OI z-score、ΔOI、near-next curve均不可用。
- `data/options/surface_latest.json`：当前为空文件，因此没有可用于8/31评分的series-level ATM IV、RR25、BF25或期限结构。

`data/last_run_status.json`与`data/radar_latest.json`的最近完整中国EOD仍是 **2026-08-28**：五所SHFE/INE/DCE/CZCE/GFEX均覆盖，803个期货合约，`source_date_match_pct=100%`、`critical_module_errors=0`、`full_market_ready=true`；但这些质量结论只属于8/28，不能移植为8/31的“当日完整市场”。8/28另有5个OHLC placeholder，继续排除出异常排行；DCE contract metadata仍有JSON decode error，GFEX metadata部分字段不新鲜。

独立期权质量文件也停留在8/28：21,806条合约、370个series，IV coverage 98.59%、OI coverage 68.16%、bid/ask coverage 0，61/64产品成功；全局`positioning_ready=false`、`execution_ready=false`，且当前surface文件为空。故本次**不复用旧报告中的精确ATM IV/skew数值作为今日证据**，不输出bid/ask、权利金、滑点、dealer gamma或可成交strike。

Physical最近也是8/28请求口径，映射4/20：铁矿港口库存为8/26周度值；焦煤现货为8/20旬度值且basis质量C，只作context；玻璃企业库存、PTA加工费为8/28周度值。它们不能包装成8/31今日变化，也不足以替代今日价格—curve—OI层。

另有一个需要修复的数据工程问题：仓库 `.github/workflows/daily.yml` 当前晚间cron是 **18:03 BJT**，而同一文件注释/collection planner说明“18:15前安全重试上一完整EOD”。这与本雷达协议预期的18:15后启动存在结构性错位。截至本报告切点，Actions最新可见成功运行是8/31 08:24启动的一次，尚未看到新的8/31晚间EOD发布。这个配置错位**可能增加晚报拿不到T日EOD的概率，但不能据此断言就是今天缺数的唯一原因**。

因此本期当前日状态为：`current_day_full_market_ready=false`、`current_session_data_fresh=false`；仅保留8/28 last-good作为历史参考。按五层证据纪律，任何依赖中国商品今日价格/OI/curve/options的方向交易都不能达到70分。

## 三、商品仪表盘（8/28 last-good参考；8/31当日字段缺失）

> 下表“参考价/结构”均为最近可验证的8/28数据，不是8/31实时或收盘价。8/31 volume/OI/ΔOI/curve在仓库中不可用，禁止据此推断21:00 gap已定价多少。

| 板块 | 品种/合约 | 8/28参考价或涨幅 | 8/28 Volume / OI | 8/28 Curve/Physical | 8/31 Options | 今晚信号 |
|---|---|---:|---:|---|---|---|
| 能源 | SC2610 | 596.5 close / 592.3 settle；5D约-0.02% | 8/31不可用 | 8/28约1.37% contango；Physical无闭环 | 当前surface为空 | **外盘强，但中国今日定价未知；不追** |
| 贵金属 | AG2610 | 8/28 close return +3.15% | 765,356 / 261,945 | contango；无实体层 | 当前surface为空 | 金弱银强、利率与避险冲突 |
| 黑色 | JM2701 | 8/28 close return +2.32% | 1,039,129 / 597,545 | backwardation；8/20旬度spot 2043.1，basis C | 当前surface为空 | PMI略好，但今日trend/curve未确认 |
| 建材 | SA701 | +3.05% | 1,902,641 / 1,154,367 | contango；Physical缺 | 当前surface为空 | 旧日挤仓/反转信号不延用 |
| 建材 | FG701 | +2.32% | 1,513,705 / 1,504,372 | contango；8/28周度企业库存7404.9重量箱 | 当前surface为空 | 不把库存level当今日方向 |
| 能化 | V2701 | +2.58% | 1,061,521 / 1,214,734 | contango | 当前surface为空 | 缺8/31结构，No-Trade |
| 能化 | TA701 | +1.85% | 746,791 / 868,133 | backwardation；8/28周度加工费677.532元/吨 | 当前surface为空 | 成本/curve旧信号仅作背景 |
| 新能源 | LC2701 | +4.77% | 239,379 / 391,884 | contango；Physical未映射 | 当前surface为空 | “价格涨+contango”不能叫短缺 |
| 油脂 | Y2701 | +1.67% | 499,122 / 772,448 | contango；Physical未映射 | 当前surface为空 | 等CBOT/天气和中国新数据 |
| 软商品 | AP610 | +4.57% | 199,772 / 78,095 | backwardation | 当前surface为空 | 旧日动量不可直接续推 |
| 能化 | BU2610 | +2.09% | 466,325 / 266,197 | backwardation | 当前surface为空 | 原油上行映射存在，但中国beta未知 |

## 四、相比上一交易日/上一revision真正变化

1. **从“周末等开盘”变成“数据质量硬否决”。** 今天中国实际已经交易，但仓库没有8/31完整EOD；`report_input/latest/market_state/options surface`均为空。周末时可以合理使用8/28 last-good，正常交易日晚间则不能继续这么做。
2. **SC旧的“溢价回吐空”进一步失效，但尚不足以反手做多。** Reuters在17:03 BJT附近记录Brent约91.25美元/桶、+3.58%，WTI约86.36、+3.55%；同时可见穿越霍尔木兹海峡的商品船数量周末降至约5艘/日，且有油轮遇袭报道。外部方向明确偏强，但没有8/31 SC日盘结算/OI/curve，就不知道中国白天已经price-in多少。
3. **中国PMI是“less bad”，不是工业品全面牛市确认。** 官方制造业PMI 49.8，高于7月49.2，生产50.4、新订单50.6回到扩张；但总指数仍低于50，非制造业商务活动49.0，化工和黑色部分行业仍偏弱。对JM/CU/FG/SA只能算宏观层的温和正向信息。
4. **贵金属仍是双向冲突。** 18:30 BJT附近现货黄金约4448.19美元/盎司、-0.1%，白银约67.00美元/盎司、+1%；市场对9月Fed加息概率约62%。高油价/地缘支持避险与通胀溢价，但鹰派利率压制金属duration，因此AG没有干净方向。
5. **人民币不是额外的商品多头加速器。** Reuters 18:51 BJT更新称美元/人民币约6.72，政策信号倾向抑制人民币进一步快速升值；这意味着进口品的汇率传导今晚不构成明确单边催化。

## 五、产业链地图

| 产业链 | 当前方向 | Price/Curve确认 | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 原油—航运—炼化 | **海外偏多/供应尾部** | 中国今日无法确认 | Brent/WTI强；Hormuz船流与安全风险偏紧 | 8/31 SC/FU/LU结算、OI、curve | 中：外盘高，中国执行低 |
| 双焦—钢材 | 宏观略正、趋势未知 | **无法确认** | PMI 49.8且新订单/生产>50；JM实体仅旬度context | 今日JM/I/J/RB/HC结构与库存 | 中低 |
| 贵金属 | 双向 | **无法确认** | gold弱、silver强；鹰派利率 vs 地缘避险 | 今日AG/AU与实时DXY/实际利率联动 | 中低 |
| 新能源/有色 | 不追 | **无法确认** | PMI改善但仍收缩；人民币升值动能受抑 | 今日CU/LC curve/OI/Physical | 低 |
| 农产品/油脂 | 观察 | **无法确认** | USDA Crop Progress今晚后发布；天气仅背景 | 今日Y/M/P/OI + CBOT映射 | 低 |

**最强链：原油—航运供给风险。最弱的交易方式：追中国工业品首跳。** 当前无法回答“price是否获curve确认”——因为今日curve缺失；这本身就是No-Trade信息，而不是可以用8/28 curve补齐的空白。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

按用户纪律，**<60分不进入正式排行榜**，因此本期 `top_opportunities = []`。最接近触发的3个观察项如下，仅为pre-screen：

| 观察项 | Pre-screen | Fresh层 | 尚缺确认 | 为什么现在不交易 |
|---|---:|---|---|---|
| SC2610 地缘供给冲击延续多 | **59/100** | 3实体物流 + 4海外宏观 | 8/31 SC close/settle、ΔOI、curve、night quote、option surface | 外部油价强，但中国白天已price-in多少未知；追21:00首跳可能买在重复信息尾端 |
| AG2610 双向breakout | **56/100** | 4海外宏观 | 今日AG结算/OI/curve；可用surface；DXY/实际利率同步 | gold -0.1%、silver +1%，驱动冲突；没有中国状态无法判断哪一边更拥挤 |
| JM2701 PMI后趋势续涨 | **55/100** | 4中国宏观 | 今日JM price/OI/backwardation；方向性Physical；A/B basis | PMI改善但仍<50；旬度spot level与C级basis不能升级成实体确认 |

## 七、前三名交易卡

**本期没有正式交易卡。** 原因不是“参数懒得查”，而是最基本的8/31可交易合约状态缺失：没有当日结算、持仓变化、curve和surface。若在这种情况下写出精确入场、止损、TP、notional和涨跌停压力，会造成伪精确。

仅保留三张**触发诊断卡**，不构成下单建议：

- **SC2610**：21:00后至少等30–45分钟。只有在手工/终端确认今日官方结算与当前报价后，且Brent仍维持约91美元上方、SC回撤不破日盘关键参考并重新站上夜盘VWAP，才重启多头评估；若Brent跌回89附近或出现可信的快速降级/船流恢复，放弃。风险预算即便重启也仅NAV 0.25%–0.50%。合约动态margin/limit/LTD本次不以旧参数填补。
- **AG2610**：等待30–45分钟，不预测高开/低开。若国际银继续强、黄金企稳、美元/实际利率不再上行，才评估多；若gold/silver同时转弱且实际利率再上行，才评估空。当前surface为空，禁止给Put/Call spread具体strike与权利金。
- **JM2701**：除非能确认今日仍保持price/OI/curve同向，并且回踩后重新接受日盘关键价位，否则不延续8/28趋势逻辑。DCE metadata当前有错误，margin/limit/night/LTD均标记**参数未确认**。

## 八、商品期权专项

可确认的最近独立链质量仍是8/28：21,806合约、370 series、IV coverage 98.59%、OI coverage 68.16%、bid/ask coverage 0、61/64产品成功。但**当前 `surface_latest.json` 为空**，所以今天不能可靠列出代表样本ATM IV、RR25、BF25、term structure，更不能声称“全市场最高/最低IV”。

本期Options状态：

- chain：**T-1/last-good quality background only**；
- surface：**unavailable in current artifact**；
- positioning：**not ready**；
- execution：**not ready**；
- dealer gamma：**unknown**；
- 可成交结构：**无**。研究上SC可关注Call Spread/AG可关注双向有限风险结构，但必须等手工实时quotes与surface恢复，本报告不提供执行价或权利金。

因此今天**期权不优于裸期货，也不能证明裸期货优于期权**；真正的结论是执行数据不足，先不选表达方式。

## 九、21:00夜盘开盘风险地图

由于8/31中国日盘结算缺失，本期**不做高开/低开方向预测**。海外15:00—19:30变化不能写成“中国期货已经上涨”。

| 品种 | 15:00—19:30海外映射 | Gap判断 | 追首跳？ | 等待 | 开盘后第一确认 | 夜盘资格 |
|---|---|---|---|---|---|---|
| SC | Brent 17:03约+3.58%至91.25；供应/航运尾部偏强 | **无法确认** | **否** | 30–45m | 今日SC结算、night VWAP、Brent、Hormuz实物流 | 正常规则有夜盘；动态参数执行前复核 |
| AG/AU | gold 18:30约-0.1%，silver约+1% | **无法确认，方向冲突** | 否 | 30–45m | gold/silver共振、DXY/实际利率、今日中国结算 | 正常规则有夜盘；执行前复核 |
| JM | PMI略正但无可靠直接海外腿 | **无法确认** | 否 | 30–45m | 今日JM结算、OI、curve | **夜盘安排未确认** |
| CU | PMI改善、人民币升值被政策抑制 | **无法确认** | 否 | 30–45m | LME、CNH、今日CU curve/OI | **夜盘安排未确认** |
| SA/FG | 海外映射弱 | **无法确认** | 否 | 45m | 今日settle、OI、contango/库存方向 | **夜盘安排未确认** |
| EC | 无可用夜盘映射 | — | — | — | 次日09:00日盘 | **无夜盘；下一窗口9/1 09:00** |

核心纪律：**今天最重要的夜盘确认指标不是某个技术位，而是先取得“8/31日盘真实状态”。** 没有它，任何gap百分比都没有合法分母。

## 十、未来24h / 7d事件

- **9月1日 04:00 BJT｜USDA Crop Progress**：周度种植/成熟/收获与作物状况。对玉米、大豆、棉花只在“作物状态变化 + CBOT价格”同向时升级实体层。
- **9月1日 22:00 BJT｜美国JOLTS（7月）**：通过美元/前端利率影响金银、有色；事件前不为贵金属昂贵Vega无条件付费。
- **9月2日 22:30 BJT｜EIA Weekly Petroleum Status Report**：SC/FU/LU重点看crude、gasoline/distillate、炼厂开工、进口出口的组合，而非只看headline库存。
- **9月3日 20:30 BJT｜美国Q2 Productivity and Costs修订**：影响工资—通胀—利率链，贵金属与美元敏感。
- **9月4日 20:30 BJT｜美国8月Employment Situation**：本周金银最大宏观gamma点之一；优先有限风险凸性，避免事件前裸Vega放大。
- **9月6日｜OPEC+七国月度会议**：OPEC官方确认9月调整188 kb/d，下一次会议9月6日；能源持仓在会议前要把Hormuz供应冲击与OPEC供给政策分开压力测试。

## 十一、风险预算与决策归纳

今天**不新增风险**。SC即使是最强观察项，也只能在夜盘拿到今日中国真实价/curve后重评；若重启，首仓最大损失NAV 0.25%–0.50%，不得因为海外油价上涨而直接使用“确认交易”0.75%–1.50%预算。能源SC/FU/LU/海外Brent/WTI合并计入同一Hormuz因子；AG/AU归入美元—实际利率—避险复合因子；JM/I/J/RB/HC归入中国工业需求因子。

压力测试必须覆盖：夜盘gap、1/2个涨跌停、保证金上调、Hormuz新闻反转、流动性消失、相关性破裂、人民币急变，以及“8/31数据随后补发后发现白天已经完成大部分price-in”的模型风险。

数据工程建议也很明确：**把China-Commodities-Engine晚间cron从18:03移到18:15之后（例如18:18/18:20），或修改planner使18:03能够识别并抓取当日已完成EOD；同时对report_input/latest/market_state/surface空文件加CI硬失败。** 今天这个No-Trade不是坏结果，它暴露的是一个会系统性污染19:30晚报的时点问题。

### 来源

- 国家统计局，2026-08-31，中国8月PMI：https://www.stats.gov.cn/sj/zxfbhjd/202608/t20260831_1965154.html
- Reuters，2026-08-31，Oil rises over 3% as US, Iran resumes military attacks：https://www.reuters.com/business/energy/oil-jumps-more-than-2-after-us-attack-irans-larak-island-2026-08-30/
- Reuters，2026-08-31，Gold dips as Fed rate-hike bets rise：https://www.reuters.com/world/india/gold-hits-near-two-week-low-fed-chiefs-hawkish-stance-2026-08-31/
- Reuters，2026-08-31，China reins in rising yuan：https://www.reuters.com/world/asia-pacific/china-reins-rising-yuan-weak-domestic-demand-clouds-outlook-2026-08-31/
- USDA NASS Crop Progress：https://esmis.nal.usda.gov/publication/crop-progress
- U.S. BLS September 2026 release calendar：https://www.bls.gov/schedule/2026/09_sched_list.htm
- EIA Weekly Petroleum Status Report：https://www.eia.gov/petroleum/supply/weekly/
- OPEC，2026-08-02，September adjustment and Sep 6 meeting：https://www.opec.org/pr-detail/611-2-august-2026.html
- China-Commodities-Engine workflow：https://github.com/farfromexact/China-Commodities-Engine/blob/main/.github/workflows/daily.yml

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无；SC2610也必须先取得8/31日盘真实结算/OI/curve并观察夜盘30—45分钟后再重评。  
C. 今天应继续观察的机会：SC2610地缘供给冲击延续、AG2610双向breakout、JM2701 PMI后趋势；均不进入正式排行榜。  
D. 今天必须避免或退出的交易：沿用8/28数据追8/31中国夜盘、追SC首跳、把旧期权surface当T日、把C级basis/周度Physical包装成今日确认。