# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-03

> revision: 1  
> generated_at_bjt: 2026-09-03T19:32:18+08:00  
> data_protocol_version: china_commodities_v2  
> 决策切点：19:30后；中国T日应为2026-09-03，但仓库最新完整EOD仍为2026-09-02。2026-09-03 trading_date的Night Session是今天凌晨已经完成的连续交易阶段，不是今晚21:00未来行情。

## 一、今晚一句话结论

**今日商品期货期权无合格交易。** 19:30时T日EOD尚未入库；能源、甲醇/乙二醇与贵金属虽有“已完成Night + 海外实时”双层共振，但按证据上限均不得超过69分，今晚只挂条件，不追21:00首跳。

## 二、数据质量与覆盖

第一读取层已读取 `data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`，并按需下钻 `data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/night_session/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`。

统一输入层 `schema_version=2`，generated_at=`2026-09-03T18:20:22+08:00`，但 requested_date=`2026-09-02`。核心Futures实际交易日为9月2日，五所SHFE/INE/DCE/CZCE/GFEX均覆盖，802个合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；4条OHLC placeholder应排除。root状态仍 `official_complete=false`，主要是官方元数据/部分源异常，不改变“9月2日五所vendor-primary EOD可用”的事实，但它不是9月3日EOD。

Market State同样止于9月2日，已有同合约1D/3D/5D/20D、RV20、Volume/OI z-score与近月—次近月curve；这些可用于背景和T-1结构，但不能冒充9月3日日盘。由于T日EOD缺失，本报告**无法计算 `day_follow_through = T_EOD_close / night_close - 1`**，也无法判断9月3日日盘究竟follow-through、横盘消化还是reversal。这一缺失是今晚否决立即下单的核心原因。

Physical requested/source date均为9月2日，20目标中18个按原生频率仍fresh、2个不可用；本次常用品种spot/basis多为C级，不能计入正式方向评分或套利层。仓单/社会库存/港口库存不得混同；未获得T日新增库存/仓单确认。

External repo日频基线为9月2日；19:30前另行联网补充。最新Reuters显示Brent约97.39美元/桶（+1.8%）、WTI约92.92（+2.1%），中东冲突与霍尔木兹运输受扰继续提供供应风险；黄金现货约4425.83美元/盎司（+0.9%）、COMEX黄金期货约4472（+1.3%），美元与美债收益率回落提供支撑。USD/CNH约6.72附近，人民币并未出现足以单独解释商品大幅gap的急贬。

Night Session状态：`trading_date=2026-09-03`、`night_session_date=2026-09-02`、generated_at=`2026-09-03T06:02:01+08:00`、fresh/validated/published=true，覆盖611个有夜盘合约。这是**今天凌晨已经完成、属于9月3日交易日的连续交易阶段**。它只能复盘隔夜价格发现；今晚21:00后开始的是下一中国交易日的连续交易阶段，尚未发生。

Options为9月2日T-1链：18,860 records、343 series，IV coverage约97.7%、OI coverage约68.2%、bid/ask coverage=0；`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`、`dealer_gamma_direction_known=false`。因此T-1 Options只作背景，不计T日fresh evidence；禁止输出ATM IV、RR25、BF25、term structure、Dealer Gamma方向、具体权利金/滑点或可成交净成本。

Contract metadata为partial：仓库可提供部分最后交易日等字段，但multiplier/tick/margin/price-limit/night-session大量为空，DCE合约信息源失败。前三张卡按需用交易所官方标准合约/最新可检索调整补齐；凡动态参数无法确认均明确标为“下单前复核”。

## 三、商品仪表盘（正式基线为最后完整EOD 2026-09-02；非T日EOD）

| 板块 | 品种/合约 | 9/2 close/settle | 1D / 5D settle | 9/2量仓与ΔOI | Curve | Physical | 已完成9/3 Night | day follow-through | 15:00-19:30海外映射 | Options | 21:00信号 |
|---|---|---:|---:|---|---|---|---|---|---|---|---|
| 原油 | SC2610 | 693.3 / 677.3 | +6.29% / +19.98% | V约24.5万；OI 3.94万；ΔOI -574 | Back +4.25%，仅2 obs | SC spot不可用 | 694.7；vs close +0.20%；ΔOI -300 | N/A：T EOD缺失 | Brent/WTI约+1.8%/+2.1% | T-1 not ready | 偏高开；30m后才判断 |
| 甲醇 | MA610 | 3183 / 3157 | +3.71% / +11.55% | V 275万；OI 62.5万；ΔOI -3.93万 | Back +3.01%，z约1.66 | C级basis context | 3250；+2.10%；ΔOI +3.39万 | N/A | 原油同向偏强，仅映射证据 | T-1 not ready | 高开风险；等30-45m |
| 乙二醇 | EG2610 | 5809 / 5726 | +4.47% / +9.13% | V 188.9万；OI 38.0万；ΔOI +4.53万 | Back +5.96%，z约1.29 | T日无新增实体确认 | 5915；+1.82%；ΔOI +2.85万 | N/A | 原油同向；进口成本方向支持 | T-1 not ready | 强但最怕拥挤追高 |
| 燃料油 | FU2611 | 3970 / 3971 | +4.25% / +8.05% | V 120.6万；OI 22.6万；ΔOI +7475 | Back +8.18%，仅2 obs | C级现货不可比 | 3929；-1.03%；ΔOI -3432 | N/A | 海外原油随后转强，与早前Night冲突 | T-1 not ready | 容易首跳修复，勿直接追 |
| 黄金 | AU2610 | 938.22 / 约940.3 | -2.16% / -6.26% | ΔOI -5300；OI处低z区 | Contango约-0.36% | 宏观主导 | 948.32；+1.08%；ΔOI +2405 | N/A | Spot gold +0.9%，美元/收益率回落 | T-1 not ready | 20:30数据后再看15-30m |
| 白银 | AG2610 | 15631 / 15720 | -3.32% / -5.70% | V 56.4万；OI 22.4万；ΔOI -9098 | Contango约-0.53%，z约-1.97 | 宏观/工业混合 | 15886；+1.63%；ΔOI近零 | N/A | Silver约+0.5%；gold同向 | T-1 not ready | 反弹但不追第一跳 |
| 铜 | CU2610 | 108040 / 约108110 | -1.29% / -0.63% | ΔOI -1.72万，z约-2.27 | Back +0.46%，z约1.72 | C级basis context | 108390；+0.32%；ΔOI -876 | N/A | LME铜约14,200美元上方、偏平 | T-1 not ready | 海外确认不足；观望 |
| 螺纹 | RB2701 | 3142 / 约3158 | -0.54% / +1.35% | ΔOI +11.25万；V/OI活跃 | Contango约-1.58% | C级basis context | 约-0.3%隔夜 | N/A | 无高质量直接海外锚 | T-1 not ready | 不值得做gap方向 |
| 涤纶短纤 | PF611 | 7990 / — | +2.04% / +7.24% | ΔOI +2.74万（+19.6%） | Back +2.26%，z约2.76 | T日实体缺口 | 8026；+0.45%；ΔOI +4080 | N/A | 原油偏强但非exact parity | T-1 not ready | 观察化纤链扩散 |
| 焦煤 | JM2701 | 1663.5 / 1703 | +0.35% / +7.89% | V 150万；OI 55.3万；ΔOI -2.65万 | Back +0.62% | C级basis context | 已完成Night，但本卡不作exact分解 | N/A | 海外映射弱 | T-1 not ready | 黑色链冲突，避免 |

注：Curve为近月减次近月的期货结构，不是现货基差；正值在本仓库定义下对应近月相对强。表中9月2日为最后完整EOD，不得解读为9月3日白天已交易完后的价格。

## 四、相比上一交易日真正变化

1. **最大的变化其实是数据状态恶化**：上一版能够以9月2日完整五所EOD交易；今晚19:30仓库仍停在9月2日，无法知道9月3日日盘如何吸收今天凌晨Night与白天产业信息，所以昨天84分的EG、79分的MA都必须重新降到70以下。
2. **能源外盘在中国收盘后继续增加风险溢价**：Brent/WTI约升1.8%/2.1%，但中国T日EOD缺失，不能说SC/MA/EG“已经跟涨”。这只意味着21:00潜在gap压力更大。
3. **今天凌晨的Night已提前给出能化分化**：MA +2.10%、EG +1.82%，且两者Night ΔOI为正；SC仅+0.20%；FU反而-1.03%。所以“油价涨=所有能化今晚都该追”明显过度简化。
4. **贵金属出现隔夜→海外的连续修复线索**：AU/AG在9月2日EOD分别-2.16%/-3.32%，今天凌晨Night分别+1.08%/+1.63%，晚间国际黄金继续+0.9%。这是潜在reversal，但由于9月3日日盘路径缺失，不能确认中国市场是否已在白天完成大部分修复。
5. **期权仍不能执行化**：T-1链IV覆盖高，但surface/positioning/execution均未达标，bid/ask覆盖0；事件凸性存在，不等于可以买到合适的vol。

## 五、产业链地图

**1）原油—燃料油—沥青—化工：最强，但“强”不等于可追。** 9月2日SC/FU/BU/MA/EG/PX/EB普遍处在强势或高波动状态；今天凌晨MA、EG继续涨而FU回落，说明链内已经出现beta与个体供需分化。19:30 Brent/WTI再次走高，宏观/地缘层支持21:00高开。最大缺失是9月3日日盘EOD与T日Physical，置信度中等。

**2）甲醇—烯烃/EG—聚酯：当前最有条件单价值。** MA Night +2.10%、EG +1.82%，且Night OI同向增加；9月2日EG本身价涨仓增、深back，MA则价涨仓减。若21:00后EG继续强于MA、TA/PF也扩散，才说明不是单纯原油gap。最大缺失是T日实体库存/开工与当日日盘路径，置信度中等。

**3）贵金属：前一EOD最弱、现在最有reversal味道。** AU/AG从9月2日显著下跌转为今天凌晨上涨，晚间海外gold/silver继续偏强；美元和收益率回落也同向。问题是20:30美国数据与Waller、22:00 ISM可以迅速反转利率预期。置信度中等，适合等事件后的opening-range，不适合提前赌方向。

**4）铜—有色：中性偏冲突。** CU 9月2日价跌仓减、curve仍偏back；今天凌晨仅小幅回升，LME铜约14,200美元上方但没有像黄金/原油那样明显的晚间加速。锌有结构性供应紧张背景，但不能把LME锌squeeze直接映射成国内所有有色多头。置信度中低。

**5）黑色建材：最不值得今晚主动冒险。** I/RB/J/JM之间价仓与curve线索分裂，T日现货/仓单又不可验证；海外没有一个足以在21:00前形成高质量直接锚的增量。把单日涨跌解释成供需趋势风险很高。置信度低。

## 六、机会排行榜

按五层证据纪律，本次没有任何70+机会：

1. **SC2610 21:00 opening-range确认后顺外盘多｜68分｜观察/条件单。** 逻辑18/25，赔率17/25，催化17/20，price/curve/vol 9/15，技术7/15。fresh层=2（已完成Night价格层 + 海外宏观/原油层）。
2. **MA610 21:00回撤承接多｜67分｜观察/条件单。** 逻辑18，赔率18，催化14，price/curve 10，技术7。fresh层=2。Night价仓同向，但T日EOD/实体缺失。
3. **EG2610 21:00不追高、回撤后再确认多｜66分｜观察。** 逻辑19，赔率15，催化14，price/curve 11，技术7。fresh层=2。最强国内旧结构之一，但拥挤与DCE动态参数缺失扣分。
4. **AU2610 事件后reversal多｜65分｜观察/条件单。** 逻辑17，赔率18，催化15，price/vol 9，技术6。fresh层=2。海外与已完成Night同向，但20:30/22:00宏观风险高。
5. **AG2610 reversal多｜63分｜观察。** 逻辑16，赔率18，催化14，price/vol 9，技术6。fresh层=2；银的工业beta使其比AU更容易发生假突破。

**今日商品期货期权无合格交易，保留现金和观察仓。**

## 七、前三名交易卡（全部为条件卡，不是立即订单）

### 1. SC2610｜条件多｜68

- **事实**：最后完整EOD为9/2 close/settle 693.3/677.3；9/2 settlement +6.29%；今天凌晨已完成Night high/low/close=706.3/681.9/694.7，`overnight_return=+0.20%`，Night ΔOI=-300。9/3 day follow-through无法计算。
- **市场定价**：19:30 Brent约97.39、WTI约92.92，分别约+1.8%/+2.1%；地缘和霍尔木兹风险仍在抬升油价。
- **推断**：若21:00 gap并不极端、30分钟后仍能维持外盘映射，SC可能二次补涨；若高开后迅速回到opening VWAP下方，则说明中国白天可能已经预交易或边际信息弹性下降。
- **主观判断**：不追首跳。21:00后至少等30分钟。
- **最佳表达**：SC2610单腿期货仅在触发后小试；期权因execution not ready不作为可执行主表达。
- **入场**：以交易终端9/3实际结算价为锚；若21:00开盘gap≤约1.5%，Brent/WTI仍不低于19:30附近，且前30分钟价格在VWAP上方完成higher-low后突破30m high，才开1/3风险仓。gap>3%直接放弃追价。
- **止损/失效**：30m opening-range low下方；或WTI/Brent回吐当日涨幅一半以上且SC跌回VWAP下方。逻辑失效：地缘明确降级、Hormuz运输快速恢复、油价转跌且SC back显著收窄。
- **TP1/TP2**：1.5R / 3R；不提供伪造固定价位，因为T日结算价缺失。时间止损=1个夜盘；第二天仍无follow-through即退出。
- **风险**：最大损失0.25%-0.50% NAV；不做确认仓。SC标准合约1000桶/手、tick 0.1元/桶、tick value 100元/手；按9/2 close名义约69.33万元/手。最新检索到的INE 2026-06-25起SC2610涨跌停14%、一般持仓保证金16%、套保15%，但下单前必须再次检查是否有更新公告。按677.3结算粗算，单一-14%停板约-9.48万元/手，连续两次各-14%约-17.64万元/手（未计保证金追加与滑点）。
- **交易时段/交割**：连续交易21:00-次日02:30；标准合约最后交易日为交割月前第一月最后一个交易日，SC2610规则上接近2026-09-30，须以交易所最终日历为准；实物交割，临近交割月必须提前roll，天然人客户还有更严格清仓要求。

### 2. MA610｜条件多｜67

- **事实**：9/2 close/settle 3183/3157，settlement 1D +3.71%、5D +11.55%；9/2 ΔOI约-3.93万；近月—次近月back约3.01%。今天凌晨已完成Night open/high/low/close=3160/3252/3141/3250，`overnight_return=+2.10%`，Night ΔOI=+3.39万。
- **市场定价/推断**：Night从“9/2价涨仓减”切到“Night价涨仓增”是改善线索；海外原油晚间继续强。但原油不是甲醇exact parity，且9/3 day EOD与港口/开工当日确认缺失。
- **最佳表达**：MA610期货条件多；与EG/TA/PF链宽度作为确认，不构造无exact parity的跨市场套利。
- **入场**：等30-45分钟。若开盘gap≤1.5%、回踩VWAP/开盘区间中值不破，且EG/TA/PF至少2个同步维持正收益，再突破45m high开1/3风险仓。若直接高开>2.5%不追。
- **止损/失效**：45m low下方；或MA转弱同时EG/TA/PF链宽度转负。TP1 1.5R，TP2 2.5R；时间止损2个session。
- **风险/参数**：最大损失0.25%-0.50% NAV。郑商所标准合约10吨/手、tick 1元/吨、tick value 10元/手；9/2 close名义约3.183万元/手。标准合约写明基础限幅±4%、最低保证金5%，但当前动态参数可能更高，必须下单前复核。以标准4%仅作压力示例：一停板约-1263元/手，两次连续-4%约-2475元/手。夜盘21:00-23:00；最后交易日为交割月份第10个交易日，实物交割，具体日期按郑商所2026年日历确认。

### 3. AU2610｜事件后条件多｜65

- **事实**：9/2 close约938.22，settlement 1D -2.16%、5D -6.26%，ΔOI -5300；今天凌晨已完成Night close 948.32，`overnight_return=+1.08%`，Night ΔOI +2405。9/3 day路径缺失。
- **市场定价**：19:30前国际现货金约4425.83（+0.9%），美金期货约4472（+1.3%），美元和美债收益率回落；20:30美国数据/Waller与22:00 ISM会直接改变利率预期。
- **最佳表达**：先等20:30数据落地，再用AU2610 opening range；不在20:30前用中国期权预赌，因为surface/execution均not ready。
- **入场**：21:00后等15-30分钟；国际金仍维持在约4420上方、DXY未强力反转，AU站稳实际T日结算价和948.32历史Night锚后，突破opening-range high才试1/3仓。
- **止损/失效**：opening-range low；或国际金跌回4400下方且美元/实际利率同时反向。TP1 1.5R，TP2 3R；时间止损=当夜。
- **风险/参数**：最大损失0.25%-0.50% NAV。上期所黄金1000克/手、tick 0.02元/克、tick value 20元/手；按9/2 close名义约93.82万元/手。夜盘21:00-02:30；AU2610 repo可确认最后交易日为2026-10-15附近规则，实物交割。当前动态保证金与限幅本次未从T日repo确认，**参数未确认，禁止据旧参数计算杠杆**。

## 八、商品期权专项

本次Options是**2026-09-02 T-1**：18,860 records、343 series、IV coverage约97.7%、OI coverage约68.2%、bid/ask=0；surface/positioning/execution均not ready。T-1 Options不计9月3日fresh evidence。

因此：
- 无法可靠比较ATM IV vs RV20；
- 无法使用RR25/BF25/期限结构；
- 无法判定dealer gamma方向；
- 无法给出具体strike、权利金、净debit、滑点、成交性或最大实际净支出。

事件凸性层面，SC/AU在未来数小时有宏观/地缘催化，理论上有限亏损call spread可能比裸期货更适合gap风险，但当前链路不能证明vol便宜或执行可行。**research only; manual quote and manual confirmation required before execution; no premium quoted.** 在surface与bid/ask恢复前，期权只列研究优先级：SC/AU event convexity、MA/EG skew/term、AG vs AU vol RV。

## 九、21:00夜盘开盘风险地图

严格区分四层：①中国最后完整EOD仍是9/2，不是T日；②`trading_date=9/3`的Night已在今天凌晨完成；③15:00-19:30海外为新增信息；④今晚21:00后的连续交易尚未发生，属于下一中国交易日的价格发现阶段。

- **SC/FU/BU/LU**：海外原油明显高于9/2外盘基线，偏高开。SC先等30m；FU由于今天凌晨先跌而海外后涨，首跳修复概率高但最容易过度追价，等30m。关键确认：Brent/WTI是否继续创新高、opening OI、SC/FU价差与back是否扩大。
- **MA/EG/TA/PX/PF/EB**：偏高开，但Night已经提前涨过一轮，说明一部分信息可能已在凌晨交易。MA/EG等30-45m，关键看化工链breadth和是否“价涨仓增”继续，而不是单看原油。
- **AU/AG**：20:30美国数据/Waller先于21:00发生，开盘方向应以事件后的美元/收益率/COMEX为主。等15-30m；若海外冲高回落，不追中国补涨。
- **CU/AL/ZN/NI/SN**：平到小幅高开概率更高，铜海外并未同步加速；等30m。锌有全球供应紧张背景，但需看LME/SHFE结构而非故事。
- **RB/HC/I/J/JM**：黑色链海外直接锚弱、国内T日现货缺失。即便开盘跳动也应等45m，不做第一跳方向盘。
- **LC/SI/PS及大多数GFEX品种**：无夜盘则**下一窗口次日9:00**；不得用19:30海外变化虚构今晚中国成交。
- **多数农产品**：对有夜盘的油脂粕类等，也因本次T日EOD缺失降级为观察；无可靠CBOT/ICE exact-contract映射时不做跨市场套利。无夜盘品种下一窗口次日9:00。

## 十、未来24h / 7d事件

- **9月3日20:30 北京时间**：美国Q2 Productivity修订、周度初请/贸易数据窗口，以及Fed Governor Waller公开活动；最直接影响美元、收益率、AU/AG，次级影响工业品risk beta。处理：贵金属延迟至数据后，降低Delta，优先有限亏损结构但需live quotes。
- **9月3日22:00**：美国8月ISM Services。若强于预期并推高收益率，AU/AG reversal容易失败；若明显弱，贵金属与部分风险资产可能相反方向波动。
- **9月3日22:30**：EIA Weekly Natural Gas Storage标准周四窗口；对Henry Hub、LNG与部分化工成本预期更敏感，避免用中国化工单腿去赌美国气库数据。
- **9月4日20:30**：美国8月Employment Situation/NFP。未来24h最重要全球宏观波动源；AU/AG、铜、原油都要预留gap预算。
- **9月5日03:30**：CFTC COT常规周五15:30 ET发布（9月4日排期），用于下一轮拥挤/持仓背景，不把COT分类等同于“机构方向”。
- **9月6日**：OPEC+七个自愿减产国下次月度会议，具体北京时间待官方确认。对SC/Brent/W​​TI是1-3D核心催化，宜控制周末Delta与gap风险。
- **9月7日**：美国Labor Day，海外流动性与EIA周度发布时间可能调整；不要按平常周三节奏机械下注。
- **9月9日**：EIA September STEO预计发布（因Labor Day顺延至周三），影响原油/气供需预期。
- **9月10日附近**：EIA WPSR因Labor Day周可能延后；当前EIA页面显示9/2之后的下一期为9/10，具体发布时间以EIA当周页面为准。
- **9月11日12:00 ET（北京9月12日00:00，略超7日窗口）**：最近一份USDA WASDE；农产品仓位需提前检查天气、单产和期末库存预期。

风险预算：由于T日中国EOD缺失，本版任何触发后的**单一试仓最大损失仅0.25%-0.50% NAV**；不允许直接上0.75%-1.50%确认仓。能源相关SC/MA/EG/FU视为同一地缘/油价因子合并计风险，今晚合并上限建议≤1.0% NAV；若20:30/22:00宏观造成相关性断裂，进一步减半。压力测试必须包含夜盘gap、1/2个涨跌停、保证金上调、流动性消失、人民币急变和周末OPEC+跳空。

## 归档与来源

- China-Commodities-Engine统一输入：[report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- 核心健康：[last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- 已完成Night健康：[night_session/last_run_status.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- 市场状态：[market_state_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)
- Options质量：[options/quality_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- Reuters oil, 2026-09-03: https://www.reuters.com/business/energy/oil-edges-down-investors-weigh-uncertainty-over-us-iran-strikes-2026-09-03/
- Reuters gold, 2026-09-03: https://www.reuters.com/world/india/gold-rises-dollar-yields-ease-with-us-nonfarm-payrolls-report-spotlight-2026-09-03/
- BLS Sep-2026 schedule: https://www.bls.gov/schedule/2026/09_sched_list.htm
- ISM release calendar: https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/
- OPEC+ 2026-09-06 next meeting notice: https://www.opec.org/pr-detail/611-2-august-2026.html
- CFTC COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- EIA STEO schedule: https://www.eia.gov/outlooks/steo/release_schedule.php
- INE SC standard contract: https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html
- SHFE gold rules: https://www.shfe.com.cn/regulation/exchangerules/productrules/202512/t20251231_829960.html
- CZCE MA contract: https://www.czce.com.cn/cn/rootfiles/2024/03/26/1708572241789969-1708572241836105.pdf

## 十一、行动清单

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2610、MA610、AU2610，均需等待15/30/45分钟并以实际T日结算价/开盘区间重新定锚。  
C. 今晚应继续观察的机会：EG2610、AG2610、FU2611及化纤链PF/TA扩散；等待T日EOD、curve/仓单/实体与live options补齐。  
D. 今晚必须避免或退出的交易：21:00首跳追涨、用T-1 Options伪装为可执行结构、无exact parity跨市场套利、黑色链仅凭单日涨跌下注。