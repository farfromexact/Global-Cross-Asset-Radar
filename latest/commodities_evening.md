# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-03

> revision: 1  
> generated_at_bjt: 2026-09-03T19:32:18+08:00  
> data_protocol_version: china_commodities_v2  
> 中国T日=2026-09-03；仓库最新完整EOD仍为2026-09-02。`night_session.trading_date=2026-09-03`是今天凌晨已经完成的连续交易阶段，不是今晚21:00未来行情。

## 一、今晚一句话结论

**今日商品期货期权无合格交易。** 19:30时T日EOD尚未入库；能化与贵金属只有“已完成Night + 海外实时”两层fresh共振，按评分纪律上限69。今晚只挂条件单，不追21:00首跳。

## 二、数据质量与覆盖

第一读取层已完成：`data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`；并按需读取`latest.json`、`market_state_latest.json`、`physical/latest.json`、`night_session/latest.json`、`options/quality_latest.json`、`options/surface_latest.json`、`contract_meta.json`。

`report_input_latest.json`为schema v2，generated_at=`2026-09-03T18:20:22+08:00`，但requested_date=`2026-09-02`。核心Futures实际交易日仍是9月2日：SHFE/INE/DCE/CZCE/GFEX五所、802合约、`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；4条OHLC placeholder排除。root `official_complete=false`主要来自官方元数据/部分源异常，不改变9月2日核心行情可用，但它**不是9月3日EOD**。

Market State也止于9月2日，1D/3D/5D/20D、RV20、成交/持仓z-score、near-next curve只能作T-1背景。因为缺少9月3日EOD，所有品种的`day_follow_through = T_EOD_close / night_close - 1`均不可计算，也不能判定今天日盘究竟是follow-through、消化还是reversal。

Physical requested/source date为9月2日，20目标中18个按原生频率仍fresh、2个不可用；常用spot/basis多为C级，只作context，不计正式Physical层。External repo日频也为9月2日；15:00-19:30海外另行联网补充。

Night Session：`trading_date=2026-09-03`、`night_session_date=2026-09-02`、generated_at=`2026-09-03T06:02:01+08:00`，fresh/validated/published=true，611个夜盘合约。这是**今天凌晨已经完成的、属于9月3日交易日的连续交易阶段**。今晚21:00后才是下一交易日的连续交易，尚未发生。

Options为9月2日T-1：18,860 records、343 series，IV coverage约97.7%、OI coverage约68.2%、bid/ask=0；`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`、dealer gamma方向未知。不能输出ATM IV、RR25/BF25、Dealer Gamma、具体权利金、滑点或可成交净成本。Contract metadata仍partial，DCE contract-info失败，动态保证金/限幅下单前必须复核。

## 三、商品仪表盘

| 板块 | 合约 | 最后完整EOD 9/2 close/settle | 1D / 5D settle | ΔOI / Curve | 已完成9/3 Night | 15:00-19:30海外 | 21:00信号 |
|---|---|---:|---:|---|---|---|---|
| 原油 | SC2610 | 693.3 / 677.3 | +6.29% / +19.98% | -574 / Back +4.25%（2 obs） | 694.7，+0.20%，ΔOI -300 | Brent/WTI约+1.8%/+2.1% | 偏高开；等30m |
| 能化 | MA610 | 3183 / 3157 | +3.71% / +11.55% | -3.93万 / Back +3.01% | 3250，+2.10%，ΔOI +3.39万 | 原油同向，仅映射 | 等30-45m |
| 能化 | EG2610 | 5809 / 5726 | +4.47% / +9.13% | +4.53万 / Back +5.96% | 5915，+1.82%，ΔOI +2.85万 | 原油同向 | 强但不追gap |
| 能源 | FU2611 | 3970 / 3971 | +4.25% / +8.05% | +7475 / Back +8.18%（2 obs） | 3929，-1.03%，ΔOI -3432 | 后续原油转强 | 易首跳修复；等30m |
| 贵金属 | AU2610 | 938.22 / 约940.3 | -2.16% / -6.26% | -5300 / Contango约-0.36% | 948.32，+1.08%，ΔOI +2405 | 国际金约+0.9%，美元/收益率回落 | 20:30后等15-30m |
| 贵金属 | AG2610 | 15631 / 15720 | -3.32% / -5.70% | -9098 / Contango约-0.53% | 15886，+1.63%，ΔOI近零 | 国际银约+0.5% | reversal观察，不追 |
| 有色 | CU2610 | 108040 / 约108110 | -1.29% / -0.63% | -1.72万 / Back +0.46% | 108390，+0.32%，ΔOI -876 | LME铜约14,200上方、偏平 | 确认不足 |
| 黑色 | RB2701 | 3142 / 约3158 | -0.54% / +1.35% | +11.25万 / Contango约-1.58% | 约-0.29% | 直接海外锚弱 | 等45m/不做gap |
| 化纤 | PF611 | 7990 / — | +2.04% / +7.24% | +2.74万 / Back +2.26% | 8026，+0.45%，ΔOI +4080 | 原油偏强、非exact parity | 看链宽度 |
| 黑色 | JM2701 | 1663.5 / 1703 | +0.35% / +7.89% | -2.65万 / Back +0.62% | 已完成但不作本卡exact分解 | 映射弱 | 避免 |

Curve是near-minus-next futures，不是现货基差。以上9月2日价格不得写成9月3日白天行情；`day_follow_through`全部N/A。

## 四、相比上一交易日真正变化

1. **数据状态反而是今晚最大变化**：昨天晚报能使用9月2日完整EOD；今天19:30仓库仍停在9月2日，因此昨天84分EG、79分MA必须降到70以下。
2. **海外油价在中国收盘后继续加风险溢价**：Brent/WTI约+1.8%/+2.1%，只代表21:00潜在gap，不代表中国SC/MA/EG已跟涨。
3. **今天凌晨Night已经显示链内分化**：MA +2.10%、EG +1.82%，两者Night ΔOI为正；SC仅+0.20%，FU反而-1.03%。不能把“油价上涨”机械外推到全部能化。
4. **贵金属从上一EOD弱势切到reversal观察**：AU/AG上一EOD显著下跌，今天凌晨分别+1.08%/+1.63%，晚间国际黄金继续偏强；但缺T日日盘路径，无法证明中国白天没提前交易。
5. **Options仍不可执行化**：IV覆盖高不等于surface/positioning/execution ready，bid/ask=0使具体期权结构只能停留在研究层。

## 五、产业链地图

**原油—炼化—化工：当前最强，但不等于可追。** SC/FU/BU/MA/EG/PX/EB在9月2日已处于强势/高波动；已完成Night中MA/EG继续涨、FU回落，链内开始分化。海外原油晚间再涨，21:00可能高开；最大缺口是9月3日EOD和T日Physical，置信度中等。

**MA—EG—聚酯：最有条件单价值。** MA Night +2.10%、EG +1.82%，Night OI均增加。若今晚EG/MA强势同时扩散到TA/PF，才说明不是单纯原油gap。最大缺失是T日库存/开工/现货与白天价格路径，置信度中等。

**贵金属：上一EOD最弱、现在最像reversal。** AU/AG Night与海外同向修复，但20:30美国数据/Waller、22:00 ISM可能瞬间反转美元和实际利率，适合事件后opening-range，不适合提前赌方向。

**铜—有色：中性偏冲突。** CU上一EOD价跌仓减但curve偏back；Night仅小涨，海外铜没有同步明显加速。锌全球供应紧张是背景，不能直接映射成国内全有色多头。

**黑色建材：今晚最不值得主动冒险。** I/RB/J/JM价仓与curve线索分裂，T日现货/仓单缺失、海外直接锚弱；首跳方向信息含量低。

## 六、机会排行榜

1. **SC2610 opening-range确认后顺外盘多｜68分｜条件观察**：fresh层=2。若外盘维持、gap不过度、30m后仍站VWAP再试。
2. **MA610 回撤承接多｜67分｜条件观察**：fresh层=2。Night价仓转同向改善，但缺T日实体和日盘路径。
3. **EG2610 不追高、回撤确认多｜66分｜观察**：fresh层=2。旧结构最强之一，但拥挤与数据时效扣分。
4. **AU2610 事件后reversal多｜65分｜条件观察**：fresh层=2。Night+海外同向，但20:30/22:00宏观事件高风险。
5. **AG2610 reversal多｜63分｜观察**：fresh层=2；工业beta使假突破风险高于AU。

**今日商品期货期权无合格交易，保留现金和观察仓。**

## 七、前三名交易卡

### SC2610｜条件多｜68
最后完整EOD 693.3/677.3；已完成Night close 694.7、overnight +0.20%、ΔOI -300；T日day follow-through不可算。19:30 Brent/WTI约97.39/92.92、约+1.8%/+2.1%。**不追首跳**：若21:00 gap≤约1.5%、外盘保持、前30m在VWAP上方形成higher-low，再突破30m high仅开1/3试仓。30m low或外盘回吐当日涨幅一半以上且SC失守VWAP止损；TP1 1.5R、TP2 3R，时间止损1个夜盘，最大损失0.25%-0.50% NAV。SC标准1000桶/手、tick 0.1元/桶，tick value 100元/手；连续交易21:00-02:30。最新可检索INE调整中SC2610限幅14%、一般保证金16%/套保15%，下单前仍必须再次确认。实物交割，临近交割月提前roll。

### MA610｜条件多｜67
9/2 EOD 3183/3157，1D +3.71%、5D +11.55%，ΔOI -3.93万，Back +3.01%；已完成Night close 3250、+2.10%、Night ΔOI +3.39万。等30-45m：gap≤1.5%、回踩VWAP/开盘中值不破，且EG/TA/PF至少2个仍正，再突破45m high试1/3。45m low或链宽度转负止损；TP1 1.5R、TP2 2.5R，时间止损2个session，最大损失0.25%-0.50% NAV。标准10吨/手、tick 1元/吨、tick value 10元/手；基础限幅±4%、最低保证金5%仅是标准合约参数，动态参数下单前复核。夜盘21:00-23:00，实物交割。

### AU2610｜事件后条件多｜65
9/2 close约938.22，1D -2.16%、5D -6.26%、ΔOI -5300；已完成Night close 948.32、+1.08%、ΔOI +2405。国际金晚间约4425.8（+0.9%），美元/收益率偏回落。20:30数据落地后再等21:00的15-30m：若国际金仍强、DXY/收益率不强反转，AU站稳live结算锚并突破opening-range high才试1/3。opening-range low，或国际金跌回4400下方且美元/实际利率同时走强止损；TP1 1.5R、TP2 3R，时间止损当夜，最大损失0.25%-0.50% NAV。黄金1000克/手、tick 0.02元/克、tick value 20元/手；夜盘21:00-02:30。动态保证金/限幅本次T日未确认，禁止用旧参数放大杠杆。

## 八、商品期权专项

Options是**2026-09-02 T-1**：18,860 records、343 series、IV coverage约97.7%、OI coverage约68.2%、bid/ask=0；surface/positioning/execution均not ready。因此不能可靠做ATM IV-RV、RR25/BF25、term structure、Dealer Gamma，也不提供strike、权利金、净debit或滑点。

SC/AU存在event convexity，理论上有限亏损call spread可能优于裸期货处理gap，但当前无法证明vol便宜或可成交。**research only; manual quote and manual confirmation required before execution; no premium quoted.** 恢复后优先研究SC/AU事件凸性、MA/EG skew/term、AG vs AU vol RV。

## 九、21:00夜盘开盘风险地图

必须区分：①最后完整中国EOD=9/2；②`trading_date=9/3` Night已在今天凌晨完成；③15:00-19:30海外是新信息；④今晚21:00后的下一段连续交易尚未发生。

- SC/FU/BU/LU：偏高开；SC/FU至少等30m。关键看Brent/WTI、opening OI、VWAP、curve。
- MA/EG/TA/PX/PF/EB：偏高开，但Night已先涨过；等30-45m，看化工链breadth和价仓是否继续同向。
- AU/AG：20:30美国数据先发生，21:00后等15-30m，以美元、收益率、COMEX反应为锚。
- CU/AL/ZN/NI/SN：平到小幅高开概率更高；等30m，海外确认不足不追。
- RB/HC/I/J/JM：等45m；T日现货缺失，首跳不做方向盘。
- LC/SI/PS等无夜盘合约：**下一窗口次日9:00**。

## 十、未来24h / 7d事件

- 9/3 20:30 BJT：美国Q2 productivity修订、周度claims/贸易窗口，Fed Waller活动；直接影响美元/收益率/AU/AG。
- 9/3 22:00：美国8月ISM Services；贵金属和广义risk beta的重要第二波催化。
- 9/3 22:30：EIA天然气库存常规周四窗口；不要用中国化工单腿直接赌美国气库。
- 9/4 20:30：美国8月Employment Situation/NFP；未来24h最重要全球宏观vol事件。
- 9/5 03:30：CFTC COT常规周五发布；只作crowding背景，不把分类账户等同机构方向。
- 9/6：OPEC+七个自愿减产国会议，具体北京时间待官方确认；是原油1-3D核心gap催化。
- 9/9：EIA September STEO；Labor Day周石油周报节奏可能顺延，具体发布时间交易前复核。
- 9/11 12:00 ET（北京9/12 00:00，略超7日）：USDA WASDE，农产品持仓需提前检查天气、单产与库存预期。

本版因T日EOD缺失，触发后的单一试仓最大损失只给0.25%-0.50% NAV，不允许直接上0.75%-1.50%确认仓。SC/MA/EG/FU视为同一油价/地缘因子，合并风险建议≤1.0% NAV。压力测试至少包含夜盘gap、1/2个涨跌停、保证金上调、流动性消失、相关性破裂、人民币急变和周末OPEC+跳空。

### 主要来源

- [China-Commodities-Engine report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [Night Session status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [Reuters oil 2026-09-03](https://www.reuters.com/business/energy/oil-edges-down-investors-weigh-uncertainty-over-us-iran-strikes-2026-09-03/)
- [Reuters gold 2026-09-03](https://www.reuters.com/world/india/gold-rises-dollar-yields-ease-with-us-nonfarm-payrolls-report-spotlight-2026-09-03/)
- [BLS Sep-2026 schedule](https://www.bls.gov/schedule/2026/09_sched_list.htm)
- [OPEC meeting notice](https://www.opec.org/pr-detail/611-2-august-2026.html)

## 十一、行动清单

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：SC2610、MA610、AU2610，均需等待15/30/45分钟并以实际T日结算价/开盘区间重新定锚。  
C. 今晚应继续观察的机会：EG2610、AG2610、FU2611及化纤链PF/TA扩散；等待T日EOD、curve/仓单/实体与live options补齐。  
D. 今晚必须避免或退出的交易：21:00首跳追涨、用T-1 Options伪装为可执行结构、无exact parity跨市场套利、黑色链仅凭单日涨跌下注。