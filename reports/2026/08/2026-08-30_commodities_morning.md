---
report_date: 2026-08-30
edition: commodities_morning
generated_at_bjt: 2026-08-30T07:05:12+08:00
commodity_trade_date: 2026-08-28
commodity_data_fresh: true
commodity_history_record_count: 0
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-30

> **周末模式。** 中国最近完整EOD仍为2026-08-28；周五夜盘属于8月31日交易日，只使用公开可验证行情并与EOD分开。周日07:00没有新的中国日盘或海外周日电子盘价格。China-Commodities-Engine 的核心五所EOD健康，但 `report_input_latest.json`、`market_state_latest.json`、`data/latest.json` 与 `options/surface_latest.json` 仍为空，因此本期不生成伪造的3D/5D/20D同合约收益、z-score、ΔOI或商品期权surface指标。

## 一、今日一句话结论

**今日商品期货期权无合格交易。周末能源供应尾部风险上升，但SC境内溢价、AG偏鹰去杠杆与JM强势均缺周日/周一价格确认；保留现金，周一开盘后再评分。**

## 二、数据质量与覆盖说明

第一读取层已读取 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。`report_input_latest.json` 当前为空，因此按v2协议下钻。根状态显示2026-08-28 EOD成功完成：SHFE、INE、DCE、CZCE、GFEX五所共803个期货合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0、unknown/duplicate/invalid OHLC/negative volume-OI均为0，placeholder=5且排除异常排行。

但统一聚合层仍未恢复：`market_state_latest.json` 与 `data/latest.json` 为空。因此当前只能可靠使用2026-08-28具体合约1D、Volume、OI和near-next期货曲线；3D/5D/20D、RV20、volume/OI z-score、ΔOI z-score与price/OI quadrant本期一律标记不可用。曲线仅是期货近月—次近月结构，不等于现货基差；当前没有可用于方向评分的A/B级高质量basis。

Physical requested_date=2026-08-28，20个目标仅4个已映射，4个按原生频率fresh、0 stale、0 carried-forward。FG最新周度企业库存为7404.9，较前周7441.4约下降0.49%；TA最新周度加工费677.532元/吨，较前周586.52约上升15.5%；JM仓库内NBS焦煤现货仍为8月20日旬度2043.1元/吨且basis质量C，只作context。周度/旬度fresh不等于周日新增数据。

External repo 22个目标仅6个映射，5 fresh、1 stale；可用日频主要到8月27，因此8月28海外收盘继续以Reuters/官方来源补充。周六新增外部信息包括：俄罗斯将生产商柴油、船用燃料及gas oil出口禁令延长至9月30日；伊朗仍声称控制霍尔木兹并面临更严美国制裁。两者提高能源周一gap右尾，但不能替代周一重新开盘后的价格确认。

独立Options pipeline为2026-08-28：21,806个合约、370个series、61/64产品，IV coverage 98.59%、OI coverage 68.16%；但 `surface_latest.json` 为空，global `surface_ready=false`、`positioning_ready=false`、bid/ask coverage=0、`execution_ready=false`、dealer gamma direction unknown。因此本期不输出ATM IV、RR25、BF25、PCR、Dealer Gamma、具体strike、净权利金或滑点。

Contract metadata仍partial，DCE contract-info采集失败；动态保证金/限幅缺失时按官方交易所规则另行核对，无法确认的字段明确写“未确认”，不以旧参数或其他合约填补。

## 三、商品市场仪表盘

| 板块 | 合约 | 8/28 EOD | 周五夜盘/海外 | 1D | 5D | Volume | OI | ΔOI | Curve / Physical | Options | 信号 |
|---|---|---|---|---:|---|---:|---:|---|---|---|---|
| 双焦 | **JM2701** | close/settle **1629/1623** | 夜盘主力 **+3.05%** | +2.32% | — | 1,039,129 | 597,545 | 不可验证 | Back约**1.53%**；旬度现货仅context | surface unavailable | **69：回撤多观察，不追高** |
| 贵金属 | **AG2610** | **17215/16818** | 沪银夜盘 **-3.62%**；现货银周五约-3.5% | +3.15%日盘 | — | 765,356 | 261,945 | 不可验证 | 轻微Contango约0.14%；美元偏强 | surface unavailable | **69：失败反弹空观察** |
| 原油 | **SC2610** | **596.5/592.3** | 夜盘**614，+3.66%**；Brent周五**89.31，-0.43%** | +3.97% | — | 153,166 | 43,480 | 不可验证 | Contango约1.37%；Hormuz/Russia供给尾部 | surface unavailable | **68：境内溢价待校验** |
| 纯碱 | **SA701** | **1047/1027** | 夜盘主力 **+2.14%** | +3.05% | — | 1,902,641 | 1,154,367 | 不可验证 | Contango约3.41%；repo无SA Physical映射 | surface unavailable | **66：旧空头被price否决** |
| 玻璃 | **FG701** | **927/918** | 夜盘主力 **+2.61%** | +2.32% | — | 1,513,705 | 1,504,372 | 不可验证 | Contango约2.67%；周度库存-0.49% | surface unavailable | squeeze，不追多也不旧逻辑追空 |
| PVC | **V2701** | **4578/4520** | 夜盘主力 **+3.14%** | +2.58% | — | 1,061,521 | 1,214,734 | 不可验证 | Contango约1.09%；Physical缺 | surface unavailable | squeeze观察 |
| 碳酸锂 | **LC2701** | **159600/156000** | — | +4.77% | — | 239,379 | 391,884 | 不可验证 | Contango约1.15%；实体闭环不足 | surface unavailable | 高波动，不追涨 |
| PTA | **TA701** | **5630/5596** | — | +1.85% | — | 746,791 | 868,133 | 不可验证 | Back约1.57%；周度加工费+15.5% | surface unavailable | 66：成本/curve多但供需未闭环 |
| 棉花 | **CF701** | **17180/17200** | — | +0.94% | — | 464,467 | 604,731 | 不可验证 | Contango约1.64%；新疆天气风险 | surface unavailable | 65：天气多观察 |
| 乙二醇 | **EG2610** | **5053/5030** | — | -0.47% | — | 1,240,902 | 349,408 | 不可验证 | Back约4.16%；Physical缺 | surface unavailable | 弱价格/紧curve冲突 |
| 燃料油 | **FU2611** | **3638/3670** | — | -1.33% | — | 1,041,002 | 227,418 | 不可验证 | radar near-next曲线异常，弃用 | surface unavailable | 不做curve交易 |

## 四、相比上一交易日/上一revision真正变化

**1. 能源周末右尾显著上升，但不是“立刻多原油”。** 俄罗斯8月29日把生产商柴油、船用燃料和gas oil出口禁令延长至9月30日，背景是国内燃料短缺与炼厂遭无人机袭击；这首先利多的是成品油/裂解的稀缺凸性，而非自动等价于Brent或SC单边多头。与此同时，伊朗仍声称控制霍尔木兹，美国制裁压力继续加码。周五Brent却收跌0.43%，SC夜盘反而涨3.66%至614，说明周一最大的edge不是追SC，而是判断**海外重开是否确认内盘风险溢价**。

**2. SC的境内外冲突比昨天更值得关注，也更不适合预埋。** 周五SC2610日盘已涨3.97%，夜盘再涨3.66%，而Brent/WTI周五分别收跌约0.43%/0.16%。周末新闻让上行尾部重新变厚，但没有exact-contract、FX、税费、运费和品质闭环，不能把SC-Brent价差称为套利。若周一海外能源不跟涨，SC有gap-fade风险；若海外明显跳涨，则原本看似过高的内盘溢价可能被重新合理化。

**3. AG仍是最干净的宏观空头观察，但低开追空赔率差。** Warsh偏鹰后周五现货黄金跌逾3%、白银跌约3.5%，中国夜盘沪金-2.65%、沪银-3.62%。这一轮已经实现了相当大的第一段去杠杆；周日没有新价格，所以本期仍只有“中国价格+海外宏观/价格”两层fresh方向证据，严格封顶69分。

**4. JM仍是中国工业品最强结构之一，但周一PMI是必须跨过的需求闸门。** JM2701周五日盘+2.32%、近端Back约1.53%、夜盘又+3.05%；然而Physical仍混合，无法形成第三层。Reuters调查预计8月官方制造业PMI约49.6、仍低于50；周一09:30数据与开盘后价格反应将决定这波是可持续补库/紧张，还是工业beta squeeze。

**5. FG/V/SA的强势仍不能解释成短缺。** FG、V、SA周五夜盘分别约+2.61%、+3.14%、+2.14%，但三者仍处Contango；FG只有小幅周度去库，SA在repo没有Physical映射。旧空头要停止机械滚动，但价格上涨也不能被反向包装成需求拐点或库存短缺。

**6. Engine健康问题没有新增恶化，但统一发布层仍未修复。** 8月28五所EOD是完整、可用的；问题仍集中在`report_input / market_state / latest / options surface`空文件。因此今天不回退到更旧EOD，也不为完整表格而编造多周期指标。

## 五、产业链地图

| 产业链 | 当前方向 | 最强/最弱 | Price/Curve | 实体/海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|
| 贵金属—美元—利率 | **偏空** | 弱AG/AU | 中国夜盘已大跌，AG curve近中性 | Warsh偏鹰、美元走强 | 周一海外重开、商品期权surface | 中高 |
| 双焦—钢材 | tape偏多 / Physical混合 | 强JM/J | JM价涨+Back | 焦煤库存口径分化；周一PMI关键 | 铁水、利润、补库持续性 | 中 |
| 原油—成品油 | **右尾上升/方向冲突** | SC境内强；俄柴油供应受限 | SC涨而自身仍Contango | Hormuz限制+俄柴油禁运 vs Brent周五下跌 | exact parity、裂解、周一外盘 | 中 |
| 纯碱—玻璃—PVC | squeeze / 基本面未确认 | FG/V/SA tape强 | 三者仍Contango | FG小去库；SA/V实体覆盖不足 | A/B basis、订单、检修兑现 | 中低 |
| 棉花/农产品 | 天气风险偏多 | CF有凸性 | CF仍Contango | 新疆干旱/东北热雨风险 | ICE/CBOT新鲜映射、高质量basis | 中低 |

当前regime：**中国周五工业品risk-on/挤空，与Warsh偏鹰后的全球美元走强和贵金属去风险并存；周末Hormuz与俄罗斯成品油供应扰动抬高能源gap右尾，但尚未得到重新开盘价格确认。**

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

| 排名 | 机会 | 总分 | 方向 | 持有期 | 阶段 | 工具 | Fresh层 | 数据惩罚 |
|---:|---|---:|---|---|---|---|---:|---|
| 1 | **AG2610 失败反弹空** | **69** | watch short | 1-3D | watch_only | 期货；若surface恢复再研究Put Spread | 2 | 周五夜盘已大跌；无surface/执行报价 |
| 2 | **JM2701 回撤确认多** | **69** | watch long | 1-3D | watch_only | 期货；若surface恢复再研究Call Spread | 2 | Physical混合；周一PMI；夜盘已+3.05% |
| 3 | **SC2610 境内溢价校验/回吐观察** | **68** | watch short if offshore fails | intraday-2D | watch_only | 期货 | 2 | Hormuz/Russia右尾使做空gap风险高；无exact parity |
| 4 | **SA701 失败反弹空** | **66** | watch short | 1-3D | watch_only | 期货 | 2但price反向 | 周五日夜强势正面否决旧空头 |
| 5 | **CF701 天气多** | **65** | watch long | 3-10D | watch_only | 期货 | 1-2 | Contango；缺ICE/basis/仓单闭环 |

评分纪律：没有任何候选拥有≥3个干净fresh独立方向证据层，因此没有70+试仓资格；更没有4层支持的确认加仓。

## 七、前三名预触发研究卡

### 1. AG2610｜失败反弹空｜69

- **事实：** 8/28日盘close/settle 17215/16818，夜盘沪银-3.62%；海外现货白银周五约-3.5%至66.81美元/盎司，黄金约-3%，美元走强。
- **市场可能错在哪里：** 如果Warsh后的加息路径不是一次性headline，而是持续的实际利率/美元重新定价，那么此前贵金属多头仍可能继续去杠杆。
- **推断/主观判断：** 第一段下跌已经很大，周一最差操作是低开追空；更好的edge是等反弹失败。
- **Fresh证据层：** 2（中国价格；海外宏观/价格）。
- **最佳表达：** 当前不下单。若周一低开>2.5%，至少等45分钟；只有反弹无法收复VWAP、海外银仍弱且美元不明显回落时，重新评分。
- **入场/分批：** 重新≥70后1/3；跌破首45分钟低点且海外同步弱再加1/3；剩余仅在美元继续走强时加。
- **初始止损：** 首45分钟高点上方约0.6%，或30分钟重新接受在周五结算16818上方，取更紧者。
- **逻辑失效：** DXY显著回落并收复Warsh后涨幅、海外银收复周五跌幅一半以上，同时沪银重新接受在16818上方。
- **TP1/TP2：** 以实际触发价计-2% / -4%；时间止损1-2个交易日。
- **最大损失：** 当前0；重新≥70后0.25%-0.35% NAV。
- **合约参数：** 15千克/手；tick 1元/千克；tick value 15元/手；以16818计名义约252,270元/手。最新可核验SHFE风险调整为涨跌停14%、一般持仓保证金16%；broker margin未确认。标准最后交易日为交割月份15日，实物交割，交割单位30千克。夜盘时段需下单前终端再次确认。
- **压力：** 以16818及14%限幅敏感度计，一个不利停板约35,318元/手，两个连续14%复合约75,580元/手。
- **Roll：** 2610距交割仍远；9月末前重新评估移仓，避免无意进入交割月。
- **期权：** surface/execution未就绪；若盘中人工取得可执行quote并确认标的触发，可研究Put Spread。**research only; manual quote and manual confirmation required before execution; no premium quoted**。

### 2. JM2701｜回撤确认多｜69

- **事实：** 8/28 close/settle 1629/1623，日盘+2.32%，近端Backwardation约1.53%，周五夜盘主力+3.05%。
- **市场可能错在哪里：** 如果现货提涨与近月紧张最终转化为钢厂/焦企持续补库，目前Back可能仍低估近端紧张；反面是库存口径分化且周一PMI可能打断工业beta。
- **推断/主观判断：** 趋势质量较好，但夜盘已经预支不少；必须买回撤而不是追突破。
- **Fresh证据层：** 2（价格成交持仓层；curve层）。Physical仅混合context，不计完整第三层。
- **最佳表达：** 当前不下单。若周一高开相对周五结算≥3%，放弃追涨；优选9:45后回吐一部分夜盘涨幅、1630-1645区域出现承接并重新站VWAP，同时Back仍>1%。
- **入场/分批：** 重评≥70后1/3；突破首小时高点且OI/curve确认再加。
- **初始止损：** 30分钟接受在1600下方。
- **逻辑失效：** 1585下方稳定 + curve压平至约0.3%以内或转Contango + 港口/焦企库存继续累积且现货转弱。
- **TP1/TP2：** 1700 / 1760；2-3个交易日不创新高则时间止损。
- **最大损失：** 当前0；重新≥70后0.25%-0.35% NAV。
- **合约参数：** 标准60吨/手；tick 0.5元/吨；tick value 30元/手；以1629计名义约97,740元/手。标准最后交易日为交割月份第10个交易日、实物交割。Engine的DCE metadata采集失败，**当前动态margin、price limit、broker margin和夜盘参数均未由官方日参数页闭环确认，下单前必须以DCE/终端为准**。
- **压力：** 因当前动态限幅未确认，不给伪造数值；若实际限幅为L，则单停板敏感度≈97,740×L，两连续同向停板≈97,740×[(1+L)^2-1]。
- **催化：** 8/31中国官方PMI、钢厂利润/铁水、焦企采购、港口与焦企库存。
- **期权：** surface/execution未就绪；触发后仅研究Call Spread。**research only; manual quote and manual confirmation required before execution; no premium quoted**。

### 3. SC2610｜境内溢价校验/回吐观察｜68

- **事实：** 8/28 EOD close/settle 596.5/592.3，夜盘收614、+3.66%；同日Brent周五结算89.31美元/桶、-0.43%，WTI 83.40、-0.16%。周末俄罗斯延长柴油出口禁令，伊朗仍声称控制Hormuz。
- **市场可能错在哪里：** 市场可能低估周末供应右尾，也可能高估SC相对海外的风险溢价。两种错误方向相反，所以此刻没有单边edge。
- **Fresh证据层：** 2（中国价格；海外地缘/供应与价格）。curve仍Contango，不为多头确认；无exact parity。
- **最佳表达：** 当前不下单。周一清晨先看海外能源电子盘重开；若Brent/WTI没有明显上涨，而SC 9:00后仍高开并在30-60分钟内失守夜盘价/VWAP，可把“溢价回吐空”重新评分。若海外原油直接+2%以上并持续，则放弃做空。
- **入场/分批：** 仅重评≥70后1/3；跌破600且海外不强再加。
- **初始止损：** SC重新30分钟接受620上方，或Brent较周五结算持续上涨>2%，任一触发即撤短仓想法。
- **逻辑失效：** Hormuz运输进一步恶化并获船流数据确认、海外原油同步重估，SC高位不再表现为孤立溢价。
- **TP1/TP2：** 600 / 585；时间止损1个交易日。
- **最大损失：** 当前0；若重评≥70，0.25%-0.30% NAV，低于普通试仓上限以反映周末headline gap。
- **合约参数：** 1000桶/手；tick 0.1元/桶；tick value 100元/手；以614计名义约614,000元/手。INE 2026-06-23对SC2610规定涨跌停14%、一般持仓保证金16%、套保持仓15%；broker margin未确认。标准最后交易日为交割月份前第一月最后一个交易日，实物交割，基准中质含硫原油。夜盘时段下单前终端再次确认。
- **压力：** 以614及14%限幅敏感度计，一个不利停板约85,960元/手，两个连续14%复合约183,954元/手。
- **期权：** surface/execution未就绪；周一只有在标的方向确认后才研究有限风险Call/Put Spread。**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 八、商品期权专项

当前只能说**raw chain可用、surface/positioning/execution不可用**。2026-08-28链覆盖21,806个合约、370个series、61/64产品，IV字段覆盖98.59%，但不能据此声称任何series已有可用ATM IV曲面；`surface_latest.json`为空，OI覆盖68.16%，bid/ask=0。

因此：
- 不称“全市场最高/最低IV”；
- 不输出IV-RV、RR25、BF25、PCR或Gamma方向；
- 不给具体strike、权利金、净支出与精确滑点；
- 周一若surface和人工报价恢复，研究优先级为 **AG Put Spread > JM Call Spread > SC方向确认后的有限风险Spread**。

所有上述期权结构均为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、8月31日9:00开盘风险地图

> 8月30日为周日，中国市场不交易；以下针对8月31日周一。

| 品种 | 周末前状态 | 最大gap风险 | 等待时间 | 开盘后最重要确认 |
|---|---|---|---:|---|
| **AG2610** | 夜盘-3.62% | 低开追空赔率极差 | **45分钟** | 海外银、DXY、VWAP、首45分钟高低点 |
| **JM2701** | 日盘+2.32%、夜盘+3.05%、Back | 高开兑现/PMI反转 | **45-60分钟** | 是否守1630-1645、Back、OI、09:30 PMI反应 |
| **SC2610** | 夜盘614 vs Brent周五跌 | 周末Hormuz/Russia headline双向gap | **60分钟** | 海外原油重开方向、SC是否失守614/VWAP |
| **SA701** | 日盘+3.05%、夜盘+2.14%、Contango | squeeze延续或快速回吐 | **45分钟** | 是否跌回1047/VWAP下方；curve是否仍深Contango |
| **FG/V** | 日夜连续强、仍Contango | 工业beta挤空 | **45分钟** | OI、curve、FG库存/现货响应；不执行旧空 |
| **CF701** | 天气风险、Contango | 天气消息gap | **30分钟** | 17000附近承接、curve、外棉/天气更新 |

## 十、未来24小时 / 7d事件

| 北京时间 | 事件 | 主要品种 | Delta/Vega/凸性处理 |
|---|---|---|---|
| 8/30周日全天 | Hormuz谈判/船流、俄炼厂与柴油禁运新消息 | SC/LU/FU/BU/PG、油运 | 不预埋裸方向；保留周一gap预算 |
| 8/31周一清晨 | 海外能源/贵金属电子盘陆续重开 | SC、AG/AU | 先看外盘是否确认周末消息，避免中国开盘前先验固化 |
| **8/31 09:30附近** | 中国8月官方制造业PMI；Reuters调查中值约49.6、前值49.2 | JM/J/I/RB/HC、FG/V/SA、LC、CU | 工业品至少等数据后15-30分钟；PMI<49.3偏空需求beta，>50偏强确认 |
| **9/1 04:00** | USDA Crop Progress | C/CF/M/Y/P等 | 天气仓控制Delta，期权若可用优先有限Vega |
| **9/2 22:30** | EIA Weekly Petroleum Status Report | SC/LU/FU/BU、Brent/WTI | 重点看原油/馏分油库存是否分化，RV优先于裸方向 |
| **9/4 20:30** | 美国8月Employment Situation | AG/AU、CU、原油、美元 | 避免事件前裸卖vol；若做Vega采用有限损失结构 |
| **9/5 03:30** | CFTC COT常规发布时间（通常反映前周二持仓） | 贵金属、能源、农产品 | 只作拥挤背景，不推断最终客户方向 |

## 十一、风险预算

今天没有70+机会，**新增风险预算为0**。周一只有重新达到70-79后才允许单一试仓最大损失0.25%-0.50% NAV；没有第四个独立fresh层，不升级确认仓。

同因子合并：贵金属美元/实际利率≤0.50% NAV；JM/J/RB/HC黑色工业beta≤0.75%；Hormuz+Russia能源因子≤0.50%；SA/FG/V地产化工squeeze≤0.75%；农产品天气≤0.75%。不要同时追JM、FG/V和SC——看似三笔，可能本质上都在买同一个中国工业risk-on或地缘risk premium。

压力测试必须覆盖：一个/两个涨跌停、夜盘gap、保证金上调、相关性断裂、流动性消失、人民币急变及中国休市时海外大幅波动。动态限幅无法确认的品种不得用旧参数做精确压力损失。

## 关键来源

- China-Commodities-Engine: [last_run_status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json), [radar_latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json), [physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json), [external](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json), [options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json).
- Reuters, Aug 29: [Russia extends diesel export ban to September 30](https://www.reuters.com/business/energy/russia-extends-ban-diesel-exports-until-september-30-2026-08-29/).
- Reuters, Aug 29: [War weighs on Iran's economy as US intensifies sanctions](https://www.reuters.com/world/asia-pacific/war-weighs-irans-economy-us-intensifies-sanctions-2026-08-29/).
- Reuters, Aug 28: [Oil settles lower on Fed policy clues and Hormuz rumors](https://www.reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/).
- Reuters, Aug 28: [Gold drops 3% as Warsh comments lift rate-hike bets](https://www.reuters.com/world/india/gold-slips-fed-chief-warshs-jackson-hole-speech-looms-2026-08-28/).
- Reuters, Aug 28: [China factory activity seen contracting again in August](https://www.reuters.com/world/asia-pacific/chinas-factory-activity-seen-contracting-again-august-2026-08-28/).
- Reuters, Aug 27: [Heat, floods threaten China crops](https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/).
- 财联社, Aug 28: [国内商品期市夜盘收盘多数上涨](https://www.cls.cn/detail/2468335).
- 每日经济新闻, Aug 29: [SC2610夜盘614；沪金/沪银下跌](https://www.nbd.com.cn/articles/2026-08-29/4565613.html).
- INE: [SC标准合约](https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html), [2026-06-23 SC风险参数调整](https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html).
- SHFE: [黄金白银风险参数调整](https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html).
- USDA NASS: [Crop Progress release calendar](https://esmis.nal.usda.gov/publication/crop-progress).
- EIA: [Weekly Petroleum Status Report schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php).
- BLS: [September 2026 release calendar](https://www.bls.gov/schedule/2026/09_sched_list.htm).
- CFTC: [COT release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm).

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：没有；周一AG2610、JM2701、SC2610均需先重新评分≥70，当前不预埋。**  
**C. 今天应继续观察的机会：AG失败反弹空、JM回撤多、SC境内溢价校验、SA失败反弹空、CF天气多。**  
**D. 今天必须避免或退出的交易：低位追空AG、追JM/FG/V周五夜盘强势、周末预埋SC单边方向、继续机械执行旧SA空头，以及任何基于空surface/零bid-ask的精确商品期权交易。**
