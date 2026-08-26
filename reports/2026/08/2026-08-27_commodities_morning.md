# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-27

> revision: 1  
> generated_at_bjt: 2026-08-27T07:10:20+08:00  
> data_protocol_version: china_commodities_v2  
> 中国基线：2026-08-26完整EOD；当前8月26日晚夜盘正式repo snapshot尚未滚动到8月27交易日，因此今晨中国夜盘只采用可验证媒体方向，不与EOD结算混写。

## 一、今日一句话结论

**今日商品期货期权无合格交易。V/FG空头已接近上一版目标且供给收缩/去库抬高追空风险；菜粕虽强，但curve与供应未确认。保留现金，等9:00后30—45分钟再做posterior更新。**

## 二、数据质量与覆盖说明

第一读取层来自 `farfromexact/China-Commodities-Engine` main 的 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。统一报告输入 `requested_date=2026-08-26`，`generated_at=2026-08-26T19:05:02.243742+08:00`。为Top候选进一步读取了 `data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json` 与 `data/night_session/last_run_status.json`。

核心期货为2026-08-26完整EOD：SHFE、INE、DCE、CZCE、GFEX五所齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0；11条placeholder不进入异常排名。Market State拥有20个有效交易日，1D/3D/5D/20D均按当前同一具体合约计算，没有拼接主力。

Physical本期20个目标仅4个已映射，fresh=4、stale=0、carried-forward=0；覆盖I港口库存、JM现货、FG周度企业库存、TA周度加工费。对V、RM、EG、能源产品等实体层仍需行业数据补充，且商业社会库存/企业库存不冒充交易所仓单。Basis仍无可用于方向评分的A/B级闭环；会员排名不可用。

External仓库整体尚未完成今晨滚动，report_input的外部数据最晚主要到8月25日，因此本期海外层用8月26日美国收盘及官方/Reuters补充：BEA公布7月PCE同比3.7%、核心3.3%；Brent 8月26日结算87.84美元/桶、WTI 82.23美元/桶；美元偏强、黄金和白银回落。仓库External整体stale不等于逐条废弃，但stale序列不计fresh evidence。

中国正式夜盘repo当前仍显示 `trading_date=2026-08-26 / night_session_date=2026-08-25`，不是昨晚8月26日至今晨的8月27交易日夜盘，因此不得复用其精确价格。当前夜盘只采用人民财讯23:07方向：菜粕、LPG、豆粕、沥青涨超1%，乙二醇、纯碱跌超2%；其他品种未给精确收盘价则写“无法确认”。

独立Options流水线为2026-08-26：20,346条期权记录、344个series、56/64品种成功；330个series `surface_ready`、62个`positioning_ready`、0个`execution_ready`，bid/ask coverage=0。因为报告已经进入8月27中国交易日，这些期权是T-1背景，**不计今日fresh evidence**；所有结构仅研究，不报净权利金、真实bid/ask或成交滑点。

Contract Metadata仍partial：DCE contract-info失败，GFEX metadata日期/完整性仍有问题。FG/RM的静态合约规则可由郑商所官方细则核对；当前动态保证金和涨跌停若无当日公告/终端确认，一律写“未确认”。

## 三、商品仪表盘

| 板块 | 品种/合约 | 8/26 EOD | 1D / 5D | Volume / OI / ΔOI | Curve / Physical | T-1 Options | 今晨信号 |
|---|---|---:|---:|---|---|---|---|
| 建材 | **FG701** | close 898 / settle 905 | settle **-1.20%** / **-0.77%** | 123.6万 / 164.5万 / **+13.69万(+9.08%)** | near-next约-2.91% Contango；8/21企业库存7441.4万重箱，连续三周小去库但绝对高；8/26仓单1273张，日减11 | ATM900 IV **22.80%**，RR25 +7.48，BF25 +1.04；surface✓ positioning✓ execution× | **空头逻辑仍在，但新开追空赔率不足** |
| 能化 | **V2701** | close 4466 / settle 4497 | **-1.73% / -5.31%** | 99.4万 / 124.5万 / **+7.27万(+6.20%)** | repo近端Contango约-1.05%；V2701-2702 close约-0.78%但次月流动性低；PVC库存仍高但周度去库、开工回落 | surface背景可用；execution× | **昨日空头兑现，今天不在低位续空** |
| 农产品 | **RM611** | close 2314 / settle 2282 | **+2.06% / +1.06%** | 99.0万 / 67.1万 / **+3.37万(+5.28%)** | main-secondary RM611-RM701约-1.04% Contango；供应/库存数据偏松，季节需求支持 | ATM2275 IV **18.18%**，RR25 +4.82，BF25 +1.88；surface✓ positioning✓ execution× | **价格最强，但基本面/curve未确认** |
| 能化 | **EG2610** | close 5168 / settle 5247 | close **-5.99%** | 94.2万 / 37.6万 | 仍为Backwardation；实体低库存旧背景与价格继续冲突 | T-1可研究；execution× | **昨日日盘跌停，昨夜夜盘再跌>2%；不接刀也不追空** |
| 能源 | **BU2610** | close 4487 / settle 4506 | close **-2.63%** | 57.9万 / 28.6万（产品级） | 海外炼化/成品油短缺仍强于原油本身；国内昨夜夜盘沥青>1%反弹 | T-1 | **产品端相对强，等45分钟确认反弹** |
| 能源 | **FU2611** | 日盘大跌 | settle约**-6.61%** / 3D约-4.55% | 高活跃 | 海外原油继续回落，但成品油裂解偏紧 | T-1 | **继续禁止追空** |
| 有色 | **CU2610** | close 108750 / settle 108800 | **+0.59%**结算口径附近 | 12.7万 | 高价含美国关税库存迁移因素，不等于纯全球短缺 | T-1 | **强但不追；美元/PCE逆风** |
| 贵金属 | **AG2610** | close 16756 / settle 16670 | close -0.11% | 64.3万 | PCE后美元偏强；COMEX银约-1% | T-1 | **事件溢价回吐，No-Trade** |
| 能化 | **MA610** | close 2769 / settle 2830 | close **-6.01%** | 239.0万 / 82.4万 | curve仍Backwardation | T-1 | **价格跌停与紧curve冲突，不追空** |
| 黑色 | **I2701** | 仓库有效 | 数据完整 | 仓库有效 | 周度港口库存仅context | T-1 | 中性，无独立edge |

中国主要黑色、有色、能化、新能源、农产品与软商品仍在五所全市场扫描中；本表保留今天最重要的异常与跨板块代表。GFEX LC/PS、部分软商品和实体供需链仍因Physical/metadata不足而无法闭环。

## 四、相比上一交易日真正变化

**1. 昨天的V/FG空头方向兑现，但今天“继续做空”与“昨天做空正确”不是一回事。** V2701 8月26日再跌，5D已约-5.31%，OI又增6.20%；FG701收898、价跌仓增9.08%。上一晨报的V TP1 4450、FG TP1 895都已非常接近。此时新增空头面对更差的entry，必须要求新的第三层确认，而不能把已经发生的收益当成未来edge。

**2. FG/PVC的Physical开始对空头形成反身性约束。** 玻璃企业库存仍高，但最新周度已经连续小幅去化；郑商所玻璃仓单8月26日降至1273张、日减11。PVC库存绝对量仍显著高于去年同期、需求弱，但开工负荷回落且库存周环比下降。于是“弱需求+高库存”仍成立，“供给持续扩张+库存继续累积”却不成立。空头只能等反弹失败，不能追低。

**3. 菜粕成为新的价格强势品种，但不是合格多头。** RM611日盘close +3.49%、结算+2.06%，ΔOI +5.28%，夜盘媒体又确认菜粕涨超1%。但RM611-RM701仍是Contango约1%，且最新产业信息显示国内菜粕产量、菜籽库存及菜粕库存并不紧，进口同比也高。价格强势是真，供应紧张不是当前可证实事实。

**4. 能化从“去风险”进一步演变为内部大分化。** 8月26日日盘PX、MA、丙烯、EG跌停，LU跌超8%、FU近8%、SC近6%；当晚LPG、BU却反弹超1%，EG仍跌超2%。这说明市场开始区分“原油/地缘风险溢价回吐”和“成品油/炼化瓶颈仍紧”，简单做空整个能化因子已经不再干净。

**5. PCE事件落地后，贵金属的短期宏观环境转差。** 美国7月PCE同比3.7%、核心3.3%，美元上涨，Reuters记录现货黄金跌约1.3%、白银跌约1%。贵金属长期逻辑没有被一份数据摧毁，但今晨没有必要为方向感支付高Vega。

## 五、产业链地图

| 产业链 | 方向 | Price | Curve | Physical/仓单 | 海外/宏观 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|
| **玻璃/地产** | 弱，但空头已成熟 | FG价跌仓增 | Contango | 高库存但连续小去库；仓单下降 | 无直接海外锚 | 高频订单、供给冷修兑现 | 中高 |
| **PVC/地产** | 弱，但接近成本/供给反馈区 | V 5D明显下跌、OI继续增 | Contango | 库存高、需求弱；但去库+开工回落 | 原油弱降低成本支撑 | 8/27新夜盘精确价、最新库存周报 | 中高 |
| **菜粕/饲料** | 价格强、供需未确认 | RM价涨仓增、夜盘续涨 | 主次月Contango | 季节需求支持；供应/库存数据偏松 | 需CBOT/加拿大菜籽进一步确认 | 进口到港/压榨/库存高频 | 中 |
| **原油—炼化产品** | 原油弱、产品端相对强 | FU/SC暴跌，BU/LPG夜盘反弹 | 多品种仍Back | repo Physical不足 | Brent87.84/WTI82.23；Hormuz谈判与炼化瓶颈并存 | 中国裂解/库存可执行闭环 | 中 |
| **贵金属/有色** | 高位事件去风险 | 铜强、金银回落 | mixed | Physical有限 | PCE偏黏、美元偏强 | 最新跨市场库存/FX传导 | 中 |

最弱产业链仍是地产化工/建材，但“最弱”不等于“最值得现在追空”；最强price action是菜粕，但供应确认不足。当前regime更接近**高波动去风险后的分化与均值回归窗口**，不是单边趋势扩张窗口。

## 六、机会排行榜

**今日没有70+机会，因此正式结论是：今日商品期货期权无合格交易，保留现金和观察仓。** 下列只列60—69分观察项，不是可直接下单的条件单。

| 排名 | 观察项 | 分数 | 方向/持有期 | Fresh证据层 | 为什么不到70 |
|---:|---|---:|---|---:|---|
| 1 | **FG701 反弹失败再空观察** | **69** | 空观察 / 1–3D | 2 | price/OI与Contango支持；但库存/仓单在去化，T-1 options不计fresh，追空位置差 |
| 2 | **V2701 反弹失败再空观察** | **68** | 空观察 / 1–3D | 2 | 价跌仓增+Contango；但5D跌幅已大、库存去化/供给收缩，Physical不再单向确认 |
| 3 | **BU2610 产品端反弹观察** | **65** | 多观察 / Intraday–2D | 2 | 国内夜盘BU>1%与海外成品油紧张同向；但无精确夜盘价、国内Physical不足 |
| 4 | **CU2610 高位强势观察** | **63** | 多观察 / 1–3D | 2 | 中国价格强+海外铜高位；但关税库存迁移扭曲且PCE/美元逆风 |

RM611虽然最强，但只有价格—成交—持仓层最干净，curve与供应并未同向，因此严格按证据上限不进入60+榜单。

## 七、前三名交易卡（均为观察卡，未达到正式入场资格）

### 1. FG701｜69分｜反弹失败再空观察

**事实：** 8/26 close/settle 898/905；同合约1D结算-1.20%、5D-0.77%；成交123.6万、OI164.5万、ΔOI +13.69万/+9.08%，属于价跌仓增归因线索。repo近端curve约-2.91% Contango。最新周度玻璃企业库存7441.4万重箱，连续三周小幅去库但绝对量高；8/26郑商所玻璃仓单1273张，日减11。T-1 FG701 ATM900 IV22.795%、RR25 +7.48、BF25 +1.035，surface/positioning ready但execution=false。

**市场已经定价：** 地产需求弱、高库存、现货贴水和产业亏损。  
**市场可能错在：** 低价下供给收缩比市场预期更快，使进一步下跌空间收窄。  
**主观判断：** 昨天空头正确，今天新空不够便宜；只有反弹失败并得到新Physical/仓单确认才重新升级。

**最佳表达：** 暂不下单。若后续重新≥70，优先小FG701期货空；Put Spread只在fresh可执行quote出现后研究。  
**再资格触发：** 9:00后至少30分钟，反弹至905—915失败，重新跌回900下方；同时OI不快速下降，且现货/库存没有出现加速去化。  
**分批：** 重新合格后先1/2；跌破890且OI/curve继续确认再加1/2。  
**初始止损：** 若触发后15分钟接受在920上方。  
**逻辑失效：** 930上方稳定接受 + curve明显收窄/翻Back + 库存/仓单加速去化。  
**TP1/TP2：** 880 / 850。  
**时间止损：** 2—3个交易日不能创新低即撤。  
**最大损失：** 只有重新≥70后才允许0.25% NAV级试仓。

**合约参数：** 郑商所FG交易单位20吨/手、tick 1元/吨、tick value 20元/手；按898估算notional约17,960元/手；夜盘21:00—23:00；最后交易日为交割月第10个交易日，最后交割日第13个交易日，实物交割/厂库标准仓单。当前动态exchange margin、broker margin、price limit未确认。非官方压力敏感性：若价格单日逆向8%，约损失1,437元/手；连续两日各逆向8%复合约2,988元/手，**这不是当前涨跌停声明**。

### 2. V2701｜68分｜反弹失败再空观察

**事实：** 8/26 close/settle 4466/4497；1D结算-1.73%、3D-3.91%、5D-5.31%；成交99.4万、OI124.5万、ΔOI +72,684/+6.20%，价跌仓增。repo近端curve约-1.05% Contango；V2701与低流动性V2702收盘差约-0.78%。PVC最新产业周度信息仍显示高库存和低下游开工，但库存继续环比去化、PVC开工负荷回落。

**市场已经定价：** 弱地产需求、高库存、油价回落。  
**市场可能错在：** 供给收缩和成本底部比空头预期更快出现。  
**主观判断：** 不追低。昨天从4520附近向下的edge已经兑现大半。

**最佳表达：** 暂不下单；若重新≥70，优先V2701小期货空。  
**再资格触发：** 30—45分钟反弹4490—4540失败，再回4470下；OI稳定、Contango不收窄，并出现新的库存停止去化或开工恢复证据。  
**初始止损：** 若触发后15分钟接受4580上方。  
**逻辑失效：** 4600上方稳定 + 库存去化加速 + 开工进一步下降。  
**TP1/TP2：** 4400 / 4300。  
**最大损失：** 重新合格后0.25%—0.35% NAV。  
**合约参数：** DCE PVC静态交易单位5吨/手、tick 1元/吨、tick value 5元/手；按4466 notional约22,330元/手。DCE本期contract metadata失败，当前动态保证金、涨跌停、broker margin必须下单前在交易所/终端核验；实物交割，短持仓远离交割窗口。

### 3. BU2610｜65分｜产品端反弹观察

**事实：** BU2610 8/26 close/settle 4487/4506，close约-2.63%；当晚人民财讯确认沥青主力涨超1%。海外方面，8/26 Brent收87.84、WTI收82.23，原油继续偏弱；但Reuters仍记录Hormuz通行远低于战前，且成品油/炼化瓶颈明显强于原油本身。

**市场已经定价：** 原油地缘溢价回吐。  
**市场可能错在：** 市场把“原油供给改善”过度外推成“炼化产品也宽松”。  
**主观判断：** BU是比FU更干净的相对强观察，但国内实体/裂解数据不足，不能立即做多。

**最佳表达：** No-Trade；如果9:00后45分钟仍显著强于FU/SC、重新站稳8/26结算4506并有OI支持，再研究小多或BU多/FU空的beta受控RV。跨品种配比必须按波动率或回归beta重新估，不用1:1手数。  
**初始止损/失效：** 触发后重新跌回8/26低点4438下，或海外成品油裂解快速回落。  
**TP1/TP2：** 4580 / 4680（仅在正式触发后）。  
**时间止损：** 1—2D。  
**最大损失：** 若未来重新≥70，≤0.25% NAV。  
**参数：** SHFE沥青静态合约参数与当日动态保证金/涨跌停需在下单前官方复核；本报告不以旧参数填补。

## 八、商品期权专项

2026-08-26独立Options链为20,346条、344个series，56/64品种成功；330 surface-ready、62 positioning-ready、0 execution-ready，bid/ask=0。今天已经是8月27，因此全部是T-1背景，不计fresh evidence。

代表样本：FG701 ATM900 IV22.795%、RR25 +7.48、BF25 +1.035；RM611 ATM2275 IV18.18%、RR25 +4.82、BF25 +1.88。FG的IV相对RV20约高5.6vol，若未来空头重新确认，Put Spread比裸Put更适合控制Vega成本；RM上行skew偏贵，价格强但基本面未确认，不追裸Call。

今天不称“全市场最高/最低IV”，因为只有56/64产品成功且执行层为0。必须回避：虚构bid/ask或净权利金、把T-1 surface当今日实时、推断Dealer Gamma方向、在PCE后仍盲目买贵金属高Vega、裸卖Hormuz尾部。

所有期权结构固定为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。

## 九、9:00开盘风险地图

| 品种 | 8/26中国EOD | 昨夜夜盘可验证信息 | 海外映射 | 9:00处理 |
|---|---|---|---|---|
| **FG701** | 898/905，价跌仓增 | 未取得精确收盘，不推断 | 无直接外盘锚 | **30分钟**；若反抽905—915失败再评估，低开不追 |
| **V2701** | 4466/4497，5D-5.31% | 未取得精确收盘 | 原油偏弱但PVC供给也收缩 | **30—45分钟**；4490—4540反弹失败才重新打分 |
| **RM611** | 2314/2282，价涨仓增 | **菜粕涨超1%** | 供应端并不紧 | 高开概率较高；**45分钟不追高**，看能否站住2300/日内VWAP及curve是否改善 |
| **EG2610** | 5168/5247，日盘跌停 | **夜盘再跌超2%** | 原油偏弱 | **45分钟**；禁止第一刀抄底，也不在Back中追空 |
| **BU2610** | 4487/4506 | **沥青涨超1%** | 原油弱、产品端紧 | **45分钟**；看相对FU/SC强弱和4506接受度 |
| **FU/SC** | 8/26暴跌 | FU精确夜盘无法确认 | Brent87.84/WTI82.23 | 不追空；观察产品裂解与opening range |
| **AG/AU** | 中国EOD混合 | 无精确夜盘价 | PCE后金-1.3%、银-1%、美元偏强 | 30分钟；低开不追空，高开需验证美元/实际利率 |
| **CU** | 108750/108800，偏强 | 无精确夜盘价 | LME高位但美元逆风 | 30分钟；不追高，看109000附近接受与OI |

开盘后最重要的posterior不是新闻条数，而是：**FG/V反弹是否失败且OI继续增加；RM高开后能否维持价格/OI共振并改善curve；BU是否持续强于FU/SC；EG是否继续出现“价格下跌但Back不松”的矛盾。**

## 十、未来24h / 7d事件

- **8月27—29日：Jackson Hole Economic Policy Symposium。** Kansas City Fed确认主题为“Financial Innovation: Implications for Payments and Policy”。美元、实际利率、AU/AG、CU及所有长久期商品Vega都应缩小裸事件仓。
- **8月29日03:30北京时间：CFTC COT。** CFTC日历列8月28日15:30 ET发布；只作滞后仓位背景，不当作实时flow。
- **8月31日09:30北京时间：中国8月官方PMI。** 国家统计局2026日历确认8月31日发布。对黑色、建材、有色和中国需求beta是一阶事件；不要在此前把多个“中国增长空头/多头”当成独立风险。
- **9月1日04:00北京时间附近：USDA NASS Crop Progress。** 更新玉米/大豆/棉花等作物条件，农产品季节性先验应让位于最新报告。
- **9月2日22:30北京时间：EIA Weekly Petroleum Status Report。** EIA确认下一次发布为9月2日。能源方向仓和BU/FU/LU/SC相对价值在事件前缩仓。
- **9月6日：OPEC+核心成员会议。** Reuters此前报道9月配额上调约18.8万桶/日后，市场预期四季度可能暂停进一步增产；任何新headline都会直接影响SC/FU/LU与化工成本链。
- **持续非定时：Hormuz通航、伊朗—阿曼谈判、俄乌炼厂袭击与替代出口路线。** Aramco正增加Hormuz外装运并已有货发往中国，但Reuters同时显示海峡实际通行仍明显低于正常水平；最危险的是把“谈判”直接等同于“物流完全正常化”。

## 十一、风险预算与行动清单

因为今天没有70+新交易，**新增方向风险预算为0**。已有昨日V/FG空仓若仍持有，应把“盈利仓管理”与“新开仓”分开：接近目标区优先减仓/移动止损，而不是因为逻辑正确继续加仓。同因子V+FG+SA仍合并为地产需求因子；EG+FU+SC+BU+LPG合并为能源/地缘/炼化因子；AU+AG为美元实际利率Vega因子；CU为中国增长+全球库存迁移因子。

若未来重新出现70—79分条件单，单一试仓最大损失0.25%—0.75% NAV；80+且≥4 fresh独立层才允许0.75%—1.50%确认仓。压力测试继续覆盖两日极端波动、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变和中国休市时海外地缘冲击。

A. 今天没有应立即建立的新仓位。  
B. 今天没有合格条件单；FG701/V2701只设价格提醒，不挂真实订单。  
C. 今天应继续观察：FG/V反弹失败是否获得新的第三层确认；RM611高开后的curve/库存确认；BU2610是否持续强于FU/SC。  
D. 今天必须避免或退出：低位继续追空V/FG、追空EG/FU/MA/PX的大跌、追高RM、PCE后裸买贵金属高Vega，以及任何未完成口径对齐的跨市场“套利”。

## 主要来源

- China-Commodities-Engine report input: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json
- China-Commodities-Engine last run status: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json
- China-Commodities-Engine market state: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json
- China-Commodities-Engine physical: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json
- China-Commodities-Engine options quality/surface: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json ; https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json
- 人民财讯，2026-08-26 23:07，国内期货夜盘收盘: https://stcn.com/article/detail/4132420.html
- 人民财讯，2026-08-26 15:06，国内期市收盘: https://stcn.com/article/detail/4126870.html
- BEA，Personal Income and Outlays, July 2026: https://www.bea.gov/news/2026/personal-income-and-outlays-july-2026
- Reuters，2026-08-26，Oil settles down after choppy session as investors weigh Hormuz talks: https://www.reuters.com/world/asia-pacific/us-oil-prices-extend-losses-hopes-iran-oman-talks-strait-hormuz-2026-08-25/
- Reuters，2026-08-26，Gold drops over 1% after US inflation data: https://www.reuters.com/world/india/gold-little-changed-with-us-inflation-data-spotlight-2026-08-26/
- 郑商所玻璃业务细则: https://www.czce.com.cn/cn/uploadfile/2024/02/07/20240207103949576.pdf
- 郑商所菜粕业务细则: https://www.czce.com.cn/cn/content_file/flfg/zcjywgz/pzxz/2026/5/338bbcd6027246f792a776ca7c59f5f4.pdf
- 国家统计局2026发布日历: https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html
- EIA WPSR: https://www.eia.gov/petroleum/supply/weekly/index.php
- CFTC COT schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- Kansas City Fed Jackson Hole: https://www.kansascityfed.org/research/jackson-hole-economic-symposium/
