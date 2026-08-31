# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-31｜Revision 3

## 一、今日一句话结论

**今日商品期货期权无合格交易。** 8/31中国EOD采集已明确失败：五所期货均遭 iFinD `Device exceed limit`；19:44重建后的汇总仍只指向8/28。Brent上涨逾3%，但没有今日SC结算/OI/curve，不能追夜盘首跳。

当前 regime：**data-quality veto / explicit upstream entitlement-device failure / Hormuz supply-risk rally / PMI改善但仍收缩 / 贵金属利率—避险冲突**。最强外部链是原油—航运供应风险；最重要的“交易”是拒绝用8/28状态冒充8/31。

## 二、数据质量与覆盖说明

本次按 China-Commodities-Engine v2 顺序读取：

1. `data/report_input_latest.json`
2. `data/last_run_status.json`
3. `data/radar_latest.json`
4. 按需钻取 `data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`
5. 根目录失败后检查 `data/scoped/*`，当前只有 `data/scoped/ex-dce/*`

**关键修正：19:44附近看到的“关键文件为空”只是中间态，不是最终根因。** 到本次复核时，`report_input_latest.json` 已于 **19:44:56** 重建，但 `requested_date=2026-08-28`；`data/latest.json` 与 `market_state_latest.json` 也都是 **2026-08-28**。因此真正的问题不是文件永久为空，而是**8/31采集失败后系统重新发布了8/28 last-good/stale状态**。

`data/last_run_status.json` 对8/31给出硬性失败证据：run date 2026-08-31、generated 19:44:17，`data_fresh=false`、`source_date_match_pct=0%`、`critical_module_errors=15`、`full_market_ready=false`。SHFE、INE、DCE、CZCE、GFEX 五所期货接口全部返回 iFinD HTTP 401，错误码 `-1303`，信息为 **`Device exceed limit.`**。因此今日没有任何交易所可以被当成fresh核心期货层。

根目录最近一次完整可用中国EOD仍为 **2026-08-28**：五所、803个合约、source-date match 100%、critical errors 0、full-market-ready true，但它只能作为历史参考。8/28有5个OHLC placeholder，继续剔除异常排行。

范围化回退也不可用：仓库只有 `data/scoped/ex-dce/`，最近状态日期为 **2026-08-18**，且本身排除DCE。它既不满足8/31时点，也会缺失铁矿、焦煤、焦炭、豆粕、豆油、棕榈油、生猪、玉米、聚烯烃等关键链条，所以本次不拼接、不启用。

Physical 最近请求日为8/28，20个目标仅4个已验证映射：铁矿港口库存（8/26周度）、焦煤主焦煤旬度现货（8/20，basis质量C）、浮法玻璃企业库存（8/28周度）、PTA周度加工费（8/28）。这些都是 native-frequency context，不是8/31新增变化；C级JM basis不计方向评分。

External 仓库层也停留在8/28请求，22个目标映射6个，其中5 fresh/1 stale；均属EOD/context，不能冒充19:30实时。本次另用公开实时/延迟来源补充海外：Reuters在 **19:20 BJT左右（11:20 GMT）**记录 Brent约90.97美元/桶、+3.26%，WTI约86.31、+3.49%，原因是美伊重新互袭及Hormuz航运风险；这只能计入海外/宏观层，不能写成“中国SC已经上涨”。

Options 最近完整日期为8/28：21,806条合约、370个series、IV coverage 98.59%、OI coverage 68.16%、bid/ask coverage 0；series-level surface有 **363/370 surface-ready、74/370 positioning-ready、0 execution-ready**。由于是T-1/last-good背景，**不计8/31 fresh证据**；execution-ready为0，禁止给bid/ask、净权利金、精确滑点或dealer-gamma方向。

结论：`current_day_full_market_ready=false`、`current_day_source_date_match_pct=0%`。今日中国商品方向交易在五层证据框架下最多只有外部/宏观一层fresh信息，正式评分上限≤59。

## 三、商品仪表盘（8/28 last-good参考，不是8/31行情）

| 板块 | 品种/具体合约 | 最近可验证中国数据 | 5D/结构（8/28） | Physical/Options | 8/31晚间判断 |
|---|---|---|---|---|---|
| 能源 | SC2610 | 596.5 close / 592.3 settle | 5D约-0.02%；约1.37% contango | SC实体未映射；T-1 options仅背景 | **海外油强，但今日中国price-in未知；不追** |
| 贵金属 | AG2610 | 8/28 close return +3.15% | contango | T-1 surface可研究、不可执行 | gold弱、silver强，双向 |
| 黑色 | JM2701 | 8/28 close return +2.32% | backwardation | 8/20旬度spot 2043.1元/吨；basis C | PMI略改善，但今日price/OI/curve缺 |
| 建材 | SA701 | +3.05% | contango | Physical未映射 | 旧日冲高信号不延用 |
| 建材 | FG701 | +2.32% | contango | 8/28周度企业库存7404.9重量箱 | 不能把库存level当今日确认 |
| 能化 | V2701 | +2.58% | contango | Physical缺 | 今日状态缺失，No-Trade |
| 能化 | TA701 | +1.85% | backwardation | 8/28周度加工费677.532元/吨 | 旧curve/加工费仅背景 |
| 新能源 | LC2701 | +4.77% | contango | Physical未映射 | “涨价+contango”不能解释为短缺 |
| 油脂 | Y2701 | +1.67% | contango | 今日DCE期货采集失败 | 等CBOT/天气与新中国EOD |
| 软商品 | AP610 | +4.57% | backwardation | T-1 surface可研究 | 旧动量不可续推 |
| 能化 | BU2610 | +2.09% | backwardation | 无今日实体闭环 | 原油beta可能，但中国今日敏感度未知 |

表中收益和curve均为8/28具体合约/固定pair口径，只作为last-good参考；不把不同主力拼接为真实收益，也不把price/OI quadrant解释成确定新多或新空。

## 四、相比上一交易日/上一revision真正变化

1. **数据问题从“暂时看不到文件”升级为“明确上游失败”。** 8/31五所期货都因 iFinD `Device exceed limit` 返回401，source-date match=0%、critical errors=15。这是本次No-Trade最重要的新信息。
2. **19:44:56后的统一输入已经恢复可读，但它是8/28 stale rebuild。** 因此不能把“report_input有数据”误认为T日修复完成；相反，它证明系统是在降级回last-good。
3. **SC旧的“溢价回吐空”逻辑不再是今晚主方向。** Reuters 19:20 BJT附近显示Brent约90.97、+3.26%，WTI约86.31、+3.49%；Hormuz可见商品船通行降至约5艘/日，并有油轮受袭报告。海外层偏多，但没有8/31 SC日盘状态，不足以把它升级为中国夜盘多单。
4. **中国PMI属于“less bad”，不是工业品全面确认。** 国家统计局8月制造业PMI 49.8，较7月上升0.6个百分点；生产50.4、新订单50.6，但总指数仍低于50，且化学原料、黑色冶炼相关产需指数仍低于临界点。宏观层略正，不替代品种层price/curve/OI。
5. **贵金属驱动仍冲突。** Reuters 18:30 BJT附近：现货黄金约4448.19美元/盎司、-0.1%，白银约67美元、+1%；9月加息概率升至约62%。地缘与油价带来避险/通胀溢价，鹰派利率又压制duration，AG不具备干净方向。
6. **人民币不构成额外单边商品beta。** Reuters当晚报道美元/人民币约6.72附近，政策信号倾向放缓人民币进一步快速升值；不能把FX简单包装成进口商品单边利多。

## 五、产业链地图

| 产业链 | 当前方向 | Price/Curve确认 | 实体/海外确认 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 原油—航运—炼化 | 海外偏多/供应尾部 | **中国今日无法确认** | Brent/WTI强、Hormuz风险高 | 8/31 SC/FU/LU settle/OI/curve | 中（研究），低（执行） |
| 双焦—钢材 | 宏观略正，趋势未知 | 无法确认 | PMI改善；JM只有旬度context | 今日I/JM/J/RB/HC与铁水/补库 | 低 |
| 贵金属 | 双向 | 无法确认 | gold弱、silver强；利率/地缘冲突 | 8/31 AG/AU + DXY/实际利率同步 | 低 |
| 有色—新能源 | 不追 | 无法确认 | PMI改善但headline<50 | 今日CU/LC curve/OI/Physical | 低 |
| 农产品—油脂 | 观察 | 无法确认 | USDA Crop Progress待发布 | 今日M/Y/P/OI + CBOT映射 | 低 |

最强产业链是**原油—航运供应风险**；最弱的交易方式是**在中国T日数据缺失时追任何国内首跳**。当前无法回答“price是否获curve确认”，因为今日curve根本不存在；这本身就是No-Trade信息。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

按评分纪律，正式 `top_opportunities=[]`。最接近触发的1—3个观察项如下：

| 观察项 | Pre-screen | Fresh独立层 | 尚缺确认 | 暂不交易原因 |
|---|---:|---|---|---|
| SC2610 地缘供给冲击延续多 | **59/100** | 4 海外/宏观 | 8/31 SC close/settle、ΔOI、curve、21:00真实报价、T日期权 | 外盘方向强，但中国白天已经price-in多少完全未知 |
| AG2610 双向breakout | **56/100** | 4 海外/宏观 | 8/31 AG结算/OI/curve、DXY/实际利率、T日surface | gold与silver分化；利率和避险冲突 |
| JM2701 PMI后趋势延续 | **55/100** | 4 中国宏观 | 今日JM price/OI/backwardation、方向性Physical、A/B basis | PMI仍<50；旬度spot和C级basis不能升级证据 |

不存在70+机会；风险偏好高不改变数据闸门。

## 七、前三名交易卡

**本期没有正式交易卡。** 没有8/31当日可交易合约状态时，写精确入场、止损、TP、notional、margin、涨跌停压力或期权权利金会制造伪精确。

仅保留触发诊断：

- **SC2610**：21:00后至少等30—45分钟。只有手工/终端恢复8/31官方结算、OI、curve，并且Brent仍保持约90美元上方、SC不是一次性高开回落，才重启多头评分。若油价回落至冲突前区间或出现可信缓和/航运恢复，放弃。若重启，试仓最大损失NAV 0.25%—0.50%。
- **AG2610**：至少等30—45分钟，不预判高低开。若银价继续强、黄金企稳，同时美元/实际利率不再抬升，才评估多；若金银同步走弱且实际利率继续上行，才评估空。没有T日surface前不做精确期权结构。
- **JM2701**：不因PMI 49.8直接追多。必须先补回8/31 price/OI/backwardation，并看到至少一个方向性Physical变化或A/B级basis，才可能从55分升级。

合约动态margin、price limit、LTD、broker margin等本次不以旧参数填补；DCE contract metadata本轮仍存在JSON decode error。

## 八、商品期权专项

8/31没有新鲜期权面。本次只记录8/28背景：21,806条、370 series；363个surface-ready、74个positioning-ready、0 execution-ready，bid/ask coverage=0。故不称“全市场最高/最低IV”，也不复用8/28 ATM IV/RR25/BF25作为8/31方向证据。

研究优先级：
- SC：地缘事件vol是否在T日大幅抬升，以及IV-RV是否已经过度收费；
- AG/AU：利率冲击后skew是否从upside premium转向downside protection；
- JM：若趋势恢复，检查IV-RV与positioning是否同向。

**必须回避**：任何基于旧surface直接给strike、净权利金、bid/ask、滑点或dealer-gamma的交易描述。`execution_ready=false`。

## 九、21:00夜盘开盘风险地图

| 品种 | 15:00—20:00海外映射 | 预期开盘 | 是否追价 | 等待 | 开盘后最重要确认 |
|---|---|---|---|---|---|
| SC | Brent/WTI +3%附近，Hormuz尾部高 | **不预测** | **否** | 30—45m | 8/31 settle/OI/curve、夜盘VWAP、Brent、Hormuz headlines |
| AG/AU | gold略弱、silver偏强；加息概率上升 | 不预测 | 否 | 30—45m | 金银同步性、DXY/实际利率、OI |
| CU | PMI改善但无今日中国状态 | 不预测 | 否 | 30—45m | LME/CNH + 中国日盘结算/curve |
| JM | 海外直接映射弱 | 不预测 | 否 | 30—45m | 今日settle/OI/backwardation；夜盘安排需按最新规则确认 |
| SA/FG | 海外映射弱 | 不预测 | 否 | 30—45m | OI/curve与实体方向 |
| EC | 无夜盘 | — | — | — | 下一交易窗口 9月1日09:00 |

对于夜盘资格当前metadata不能完整确认的品种，明确标记“夜盘安排未确认”，不猜测。任何海外15:00后的涨跌都只是21:00 gap映射证据，不写成中国期货已经发生的涨跌。

## 十、未来24h / 7d事件

- **9月1日 04:00 BJT**：USDA Crop Progress。只在作物状况变化与CBOT价格确认同时出现时升级农产品实体层。
- **9月1日 22:00 BJT**：美国7月JOLTS。主要经美元/前端利率传导到金银、有色。
- **9月2日 22:30 BJT**：EIA Weekly Petroleum Status Report。原油必须同时看crude、汽柴油、炼厂开工、进出口，不能只看headline库存。
- **9月3日 20:30 BJT**：美国Q2 Productivity and Costs修订。关注利率—贵金属。
- **9月4日 20:30 BJT**：美国8月Employment Situation。贵金属与美元可能出现大幅Delta/Vega重定价，优先有限风险表达。
- **9月6日，时间待确认**：OPEC+七国月度会议。官方8月2日会议决定9月调整188 kb/d，并将下一次会议定于9月6日；需把Hormuz战争冲击与OPEC政策供给分开。

## 十一、风险预算与行动

今天新增中国商品方向风险预算为 **0**。如果21:00后手工/终端补齐T日状态并触发，单一试仓最大损失NAV 0.25%—0.50%；未恢复三层fresh证据前不得升级到确认交易。能源/Hormuz、金银/USD-real-yield、中国工业需求三个因子分别合并计算，不允许用多品种表面分散重复加杠杆。

压力测试至少覆盖：夜盘gap、1/2个涨跌停、保证金上调、headline reversal、流动性消失、人民币急变，以及“稍后补回的8/31数据证明白天已经price-in全部外盘信息”。

## 来源

- China-Commodities-Engine（GitHub）：https://github.com/farfromexact/China-Commodities-Engine
- 国家统计局，2026年8月PMI：https://www.stats.gov.cn/sj/sjjd/202608/t20260831_1965155.html
- Reuters，Oil rises over 3% as US and Iran resume military attacks：https://www.reuters.com/business/energy/oil-jumps-more-than-2-after-us-attack-irans-larak-island-2026-08-30/
- Reuters，Gold dips as Fed rate-hike bets rise：https://www.reuters.com/world/india/gold-hits-near-two-week-low-fed-chiefs-hawkish-stance-2026-08-31/
- Reuters，China reins in rising yuan：https://www.reuters.com/world/asia-pacific/china-reins-rising-yuan-weak-domestic-demand-clouds-outlook-2026-08-31/
- USDA Crop Progress：https://esmis.nal.usda.gov/publication/crop-progress
- BLS September 2026 release schedule：https://www.bls.gov/schedule/2026/09_sched_list.htm
- EIA WPSR schedule：https://www.eia.gov/petroleum/supply/weekly/schedule.php
- OPEC 2 Aug 2026 statement：https://www.opec.org/pr-detail/611-2-august-2026.html

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：无；SC2610也必须先恢复8/31真实结算/OI/curve并观察夜盘30—45分钟后再重评。  
C. 今天应继续观察的机会：SC2610地缘供给冲击延续、AG2610双向breakout、JM2701 PMI后趋势；均不进入正式排行榜。  
D. 今天必须避免或退出的交易：用8/28 last-good追8/31夜盘、追SC首跳、把T-1期权surface当T日、把C级basis/周度Physical包装成今日确认。  
