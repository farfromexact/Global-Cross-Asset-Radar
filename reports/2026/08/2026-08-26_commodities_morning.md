# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-26

> 数据截点：北京时间 2026-08-26 07:25。仅用于研究和交易决策支持，不自动下单。中国国内基线为最近完整交易日 2026-08-25 EOD。China-Commodities-Engine 不生产中国分钟、逐笔、夜盘/session 产品，因此本报告不从仓库推断 8 月 25 日中国夜盘。海外层除 8 月 25 日完整收盘外，补充 Reuters 06:40 BJT 可验证实时代理：WTI 约 80.99 美元/桶、较前结算再跌约1.7%；该实时价格只用于9:00 gap风险判断，不与中国EOD结算混写。

## 一、今日一句话结论

**今天有值得冒险的机会，但只适合开盘后条件试仓：EG2610低库存Back挤压多第一，V2701高库存弱需求空第二，FG701反弹失败空第三；能源和锂不追。**

## 二、数据质量与覆盖

第一读取层已从 `farfromexact/China-Commodities-Engine` main 读取 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需进一步读取 `data/latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`。协议版本 `china_commodities_v2`。

统一输入 `requested_date=2026-08-25`，`generated_at=2026-08-26T06:30:05.882004+08:00`。Futures 为8/25完整EOD：SHFE/INE/DCE/CZCE/GFEX五所齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0、核心carried-forward=0；placeholder=7，已排除异常排名。

Market State具备20个有效交易日，可使用同合约1D/3D/5D/20D、RV20、volume/OI z-score、ΔOI及curve。Physical仍为4/20映射：I港口库存、JM旬度现货、FG周度企业库存、TA周度加工费；`fresh`只表示按原生频率仍有效。JM basis为C级，只作context。EG和V的实体确认来自明确标注的商业产业数据，分别为华东主港EG库存与华东+华南PVC社会库存，不与交易所仓单混用。

External今晨已刷新：`requested_date=2026-08-26`、`generated_at=2026-08-26T06:30:04+08:00`，22个目标6个映射，5个fresh-by-lag、1个stale，全部context_only，无可执行import parity。仓库Brent仍停在8/24，因此海外最新收盘用8/25 Reuters补齐；此外06:40 BJT Reuters显示WTI继续跌至约80.99，作为晨间实时proxy。

独立Options pipeline为8/25：22,014个合约、59/64品种成功、369个series；362 surface-ready、71 positioning-ready、0 execution-ready，bid/ask coverage=0。今天已进入8/26中国交易日，因此这些期权只作T-1背景，不算当日fresh evidence。Dealer gamma direction unknown，禁止推断。

Contract Metadata仍为partial_error：DCE contract-info失败，GFEX字段有日期/完整性问题。EG2610、V2701动态保证金/涨跌停不得用旧值硬填；FG静态规则可确认，但临时风控仍须下单前复核。

## 三、商品仪表盘

| 板块 | 合约 | 8/25 close / settle | 1D结算 | 5D | 成交 / OI / ΔOI | Curve | Physical / Basis | Options T-1 | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能化 | **EG2610** | 5364 / 5497 | **+3.25%** | **+10.69%** | 1,859,195 / 361,462 / **+18,094（+5.27%）** | **2610-2611 Back约+6.26%** | 8/24华东主港库存20.6万吨，较8/20降6.2万吨；商业港库≠仓单 | ATM IV40.30% vs RV20 35.20%，RR25 -2.31；surface✓ position✓ exec× | **回撤确认多** |
| 塑化 | **V2701** | 4539 / 4576 | **-2.08%** | **-3.48%** | 1,335,984 / 1,172,046 / **+179,942（+18.14%）** | Contango约-0.85% | PVC社会库存117.92万吨，WoW -1.31%、YoY +37.49%；下游开工39.18% | ATM IV18.47% vs RV20 11.64%，RR25 +3.91；surface✓ position× exec× | **反弹失败空** |
| 建材 | **FG701** | 913 / 916 | **-0.76%** | -0.22% | 1,244,642 / 1,508,419 / **+28,183（+1.90%）** | **Contango约-3.34%** | 8/20样本厂库7441.4万重箱，WoW -0.07%、YoY +17.41% | surface-ready；exec× | **反弹失败空** |
| 能源 | FU2611 | 3842 / 3935 | **+2.96%** | +6.27% | 1,366,745 / 约286,895 / +2,236（+0.79%） | 结构偏Back | repo实体层缺 | T-1 surface | **国内强、WTI 06:40再跌；不追** |
| 贵金属 | AG2610 | 16631 / 16775 | -0.65% | +4.22% | 752,304 / 282,243 / **-16,027（-5.37%）** | 轻Contango约-0.39% | 实体层缺 | T-1；上行vol仍贵 | PCE前不追 |
| 有色 | CU2610 | 107980 / 108160 | +0.38% | +0.35% | 78,507 / 204,454 / **+12,663（+6.60%）** | 轻Back约+0.15% | 无A/B可交易basis | T-1 | 区域库存/关税挤压，不追 |
| 黑色 | I2701 | 713.5 / 716.5 | +0.14% | +1.42% | 233,317 / 553,477 / +1.10% | 约+0.55% | 最新周度港库只作context | T-1 | 中性偏强 |
| 新能源 | LC2701 | **150280 / 153960** | **-3.79%** | -0.89% | 229,133 / 354,226 / -4,912（-1.37%） | 轻Back | repo锂实体库存缺 | ATM IV37.13% vs RV20 31.30% | 巨幅反转，**不追空** |
| 建材 | SA701 | 1045 / 1046 | -1.04% | +0.77% | 1,608,290 / 1,078,079 / 约平 | Contango约-3.26% | 实体层缺 | T-1 | 弱势但赔率一般 |
| 农产品 | RM611 | 2243 / 2236 | -0.18% | 弱震荡 | 476,354 / 637,652 | 主-次价差约-31元 | 实体闭环缺 | T-1 | 无合格edge |
| 软商品 | CF701 | 16885 / 16960 | -0.67% | +0.95% | 457,361 / 537,105 / -4.37% | Contango约-1.37% | 实体闭环缺 | T-1 | 单日噪音偏大 |
| 航运 | EC2610 | 1894 / 1946.5 | -1.49% | **+10.91%** | 28,159 / 数据可用 / -1.53% | 不作普通curve套利 | 地缘运输驱动 | 无执行级vol | 极端波动，45分钟不追 |

海外8月25日收盘：Brent 88.58美元/桶（-3.9%），WTI 82.36（-3.1%）；06:40 BJT WTI又跌至约80.99（-1.7% vs前结算），市场交易Iran-Oman讨论Hormuz临时通航走廊的降风险预期。与此同时，Hormuz大部分航运仍未正常化，油轮遇袭说明上行尾部未消失。黄金约4647美元/盎司、白银约68.86美元/盎司，接近平盘；DXY约98.9。LME三月铜一度14343美元/吨，逼近纪录，但核心驱动是美国潜在关税造成的区域库存错配，而非已确认全球短缺。

## 四、相比上一交易日真正变化

1. **EG仍是第一，但从“顺畅挤压”变成“拥挤挤压”。** 结算再涨3.25%、OI再增5.27%，2610-2611 Back扩大到约6.26%；但5631高点后收5364，说明高位抛压和日内反转风险明显上升。
2. **V2701成为新进入前三的空头。** 结算-2.08%、OI单日+18.14%，Contango仍在；社会库存虽周降1.31%，但同比仍高37.49%，下游开工只有约39.18%。
3. **FG空头确认改善。** 8/25重新转跌且OI+1.90%，形成价跌仓增线索；Contango约-3.34%，厂库同比+17.41%，但本周库存只是轻微去化，所以只做反弹失败。
4. **能源国内外冲突进一步扩大。** FU2611结算+2.96%，但Brent/WTI隔夜先跌3%–4%，随后WTI在06:40 BJT又跌约1.7%。能源多头今天从“条件多”降到“No-Trade/等待承接”。
5. **LC昨日多头叙事被价格打断。** LC2701收在日内低位附近，结算-3.79%、OI下降；没有实体库存闭环，既不能继续讲短缺，也不应追空。
6. **AG/AU进入事件等待区。** AG结算-0.65%、OI-5.37%，外盘金银基本平；今晚PCE与随后Jackson Hole的信息量显著高于昨日技术信号。

## 五、产业链地图

**最强：乙二醇/聚酯上游。** 价格—OI、主次月Backwardation、商业港库去化三层同向，置信度高；但日内冲高回落说明拥挤度高。最佳策略是等回撤被接受，不追第一脚突破。

**最弱：PVC与玻璃地产链。** V的高同比社会库存、低下游开工和价跌仓增更完整；FG的Contango与高同比厂库仍压制。两者都只能做“反弹失败空”，低开追空容易被供应收缩/政策beta挤压。

**能源炼化：国内强、海外急跌。** 这是今天最清晰的No-Trade冲突区。Hormuz仍有跳空尾部，但WTI 06:40继续下跌表明市场正在交易通航改善概率，FU/SC/LU/BU不适合第一刀抄底。

**贵金属/有色：事件与区域库存主导。** 金银等待PCE/Jackson Hole；铜逼近纪录主要受COMEX吸货与关税预期导致区域库存失衡影响，不能直接称“全球铜短缺”。

**新能源：高波动反转而非供需确认。** LC大跌没有实体层闭环，价格本身不足以定义短缺或宽松。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向 / 持有期 | 阶段 | 工具 | fresh层 | 主要惩罚 |
|---:|---|---:|---|---|---|---:|---|
| 1 | **EG2610 回撤确认多** | **78** | 多 / 1–5D | 条件试仓 | 期货；fresh quote后Call Spread | **3** | 冲高回落、T-1 Options、DCE动态参数缺、外油反向 |
| 2 | **V2701 反弹失败空** | **76** | 空 / 1–5D | 条件试仓 | 期货；必要时Put Spread | **3** | 周度库存仍在去化、positioning不完整、DCE动态参数缺 |
| 3 | **FG701 反弹失败空** | **74** | 空 / 1–5D | 条件试仓 | 期货；fresh quote后Put Spread | **3** | 库存微降、低价供应响应风险 |
| 4 | FU2611 国内强/外油弱冲突 | 66 | 观察 / 1–3D | 观察 | 暂不建仓 | 2 | WTI晨间继续跌、Physical缺 |
| 5 | LC2701 暴跌后结构观察 | 63 | 观察 / 1–3D | 观察 | 暂不建仓 | 2 | 实体缺、波动过大 |

没有80+确认交易。前三名都必须等9:00后的价格接受和结构确认。

## 七、前三名交易卡

### 1. EG2610｜78分｜回撤确认多

**事实：** 8/25 close/settle 5364/5497；1D +3.25%、5D +10.69%、20D +18.55%；ΔOI +18,094手/+5.27%；2610-2611 Back约+6.26%；8/24商业口径华东主港库存20.6万吨，较8/20降6.2万吨。**市场定价：** 低库存与近端稀缺已被大幅资本化。**推断：** 挤压未结束，但5631后收5364说明拥挤交易的左尾也在变大。**主观判断：** 买回撤，不买第一脚突破。

入场：09:00后至少等30分钟；gap绝对值>1.5%等45分钟。5350–5400获得接受后重新站回5495附近/VWAP先1/3，突破Opening Range High再1/3；只有ΔOI继续健康、Back不快速压缩才加最后1/3。直接冲5630以上不追。

5290下方15分钟接受先减半；跌破5240且Back压缩至约4.5%以下、港库去化停止/到港明显恢复则逻辑失效。TP1 5650，TP2 5850；2个交易日不能有效创新高时间止损。初始最大损失0.35%–0.50% NAV，二次确认后最多0.75%。

参数：10吨/手、tick 1元/吨、tick value 10元，按5497结算名义约54,970元/手。DCE动态margin/limit本次未确认；合约规则基准5%保证金、4%限幅只作静态压力参照，当前实际参数必须下单前复核。按4%基准一板约2,199元/手、两板复合约4,310元/手。夜盘规则基准21:00–23:00；实物交割；计划1–5D，不进入交割窗口。

### 2. V2701｜76分｜反弹失败空

**事实：** close/settle 4539/4576，1D -2.08%、5D -3.48%、20D -2.03%；ΔOI +179,942手/+18.14%；Contango约-0.85%。PVC社会库存117.92万吨，周降1.31%但同比高37.49%，下游开工约39.18%。**市场定价：** 弱地产与高库存已部分反映在低价。**推断：** 价跌仓增+高库存让反弹失败后的二次下行更有赔率。**主观判断：** 这是弱需求交易，不是“库存本周继续累积”交易。

入场：等30分钟。4550–4600反弹失败并重新跌回4535/VWAP下方先1/2；跌破4500且OI没有快速流失再加1/2。直接低开4480以下不追。

4675上方15分钟接受止损；4700上方稳定、同时库存去化加速/下游开工持续回升或curve显著收窄则失效。TP1 4450，TP2 4320；3个交易日不能创新低退出。初始最大损失0.30%–0.45% NAV。

参数：5吨/手、tick 1元/吨、tick value 5元，按4576结算名义约22,880元/手。当前DCE动态margin/limit未确认；4%只作规则基准压力，一板约915元/手、两板复合约1,794元/手。实物交割，最后交易日按规则为交割月第10个交易日；本交易持有期交割风险低。

### 3. FG701｜74分｜失败反弹空

**事实：** close/settle 913/916，1D -0.76%、20D -4.98%；ΔOI +28,183/+1.90%；Contango约-3.34%。最新周度样本厂库7441.4万重箱，WoW -0.07%，YoY +17.41%。**市场定价：** 弱需求与高库存已经压到很低的绝对价格。**推断：** 价跌仓增+Contango支持反弹失败后的再下行，但库存轻微去化与亏损减产限制追空赔率。

入场：等30分钟。918–930反弹失败并重新落回913/VWAP下方先1/2；跌破905且OI不异常流失再加1/2。直接低开900以下不追。

940上方15分钟接受止损；curve明显收窄/翻Back，并伴随库存加速去化和终端订单改善时失效。TP1 900，TP2 875；3个交易日不能有效跌破900退出。初始最大损失0.25%–0.40% NAV。

参数：20吨/手、tick 1元/吨、tick value 20元，按916结算名义约18,320元/手。郑商所规则基准最低保证金5%、价格限制±4%、实物交割、最后交易日为交割月第10个交易日；临时风控和broker加收需下单前复核。按4%基准一板约733元/手、两板复合约1,436元/手。

## 八、商品期权专项

本期只能称**8月25日代表性series**，不能称8月26日实时全市场最高/最低IV。整体readiness：369 series中362 surface-ready、71 positioning-ready、0 execution-ready，bid/ask coverage=0。

- EG2610：2026-09-16到期，ATM 5500，ATM IV约40.30%，RV20约35.20%，IV-RV约+5.10 vol，RR25 -2.31，BF25 +2.30；surface✓ positioning✓ execution×。方向确认后优先Call Spread而非裸Call。
- V2701：2026-12-16到期，ATM 4600，ATM IV约18.47%，RV20约11.64%，IV-RV约+6.82 vol，RR25 +3.91；surface✓ positioning× execution×。看空方向下期货更直接；只有需要有限损失时才研究Put Spread。
- LC2701：ATM IV约37.13% vs RV20约31.30%，IV-RV约+5.83 vol；巨大反转下没有足够方向证据。

所有期权结构均为：**research only; manual quote and manual confirmation required before execution; no premium quoted**。不得虚构bid/ask、净权利金、滑点、精确Greeks或Dealer Gamma方向。

## 九、9:00开盘风险地图

**EG：** 国内挤压强、海外油弱，方向冲突。gap≤1.5%等30分钟；>1.5%等45分钟。核心看5350–5400承接、VWAP/Opening Range、ΔOI、2610-2611 Back。高开冲5630不追。

**V：** 无可靠境外PVC实时锚。低开>1.5%不追第一波，等30分钟反抽；看4550–4600是否重新出现供应压制、OI是否继续堆积、Contango是否保持。

**FG：** 918–930冲高失败优于直接破900追空；低开<900等反抽。30分钟后若站稳930以上，撤销空头计划。

**FU/SC/LU/BU：** 风险显著偏低开/回吐。WTI 06:40 BJT约80.99，再跌1.7%；Hormuz尾部仍在，但今天至少等45分钟，禁止第一刀抄底。观察亚洲时段油价是否止跌与国内Back是否压缩。

**AG/AU：** 外盘平稳而PCE在20:30 BJT，早盘方向信号价值较低；异常gap等45分钟，不放大裸Vega。

**LC/EC：** 45分钟组。LC容易剧烈均值回归；EC地缘headline密度高、5D仍双位数动量，追价赔率差。

## 十、未来24h / 7d事件

- **8月26日20:30 BJT：美国7月Personal Income and Outlays / PCE。** 对DXY、实际利率、AU/AG与有色Vega为第一档事件。
- **8月26日22:30 BJT：EIA Weekly Petroleum Status Report。** 对SC/FU/LU/BU及化工成本端是高Delta事件。
- **8月27–29日：Jackson Hole Economic Policy Symposium。** 主题为“Financial Innovation: Implications for Payments and Policy”，利率路径与美元波动继续传导至金银、有色与人民币。
- **8月29日03:30 BJT：CFTC COT。** 只作滞后的拥挤背景，不能解释为当日flow。
- **持续非定时风险：Hormuz通航、Iran-Oman协商、伊朗制裁/反制、油轮安全。** 当前价格正交易“通航概率上升”，但航运尚未正常化，夜盘与周末gap仍可能双向放大。

## 十一、风险预算与归档

今天没有80+确认交易。EG初始0.35%–0.50% NAV、V 0.30%–0.45%、FG 0.25%–0.40%；只有第二次价格/结构确认后才允许单笔放到0.75%。EG、FU/SC/LU/BU共享能化/中东因子；V、FG共享地产弱需求因子；AU/AG/CU共享美元—实际利率因子，均合并计算。单一高确信主题总风险不超过2.5%–3.0% NAV。

压力测试覆盖1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷、交割挤压、人民币急变。六个固定归档路径均已写入main并回读；status与manifest标记`archive_status=success`，CI维持`pending_or_unverified`，不等待。

### 主要来源

- [China-Commodities-Engine report_input_latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [Reuters：8月25日油价结算](https://www.reuters.com/business/energy/oil-prices-steady-investors-weigh-impact-expanded-us-sanctions-against-iran-2026-08-25/)
- [Reuters：8月26日早盘WTI继续下跌、Iran-Oman通航谈判](https://www.reuters.com/world/asia-pacific/us-oil-prices-extend-losses-hopes-iran-oman-talks-strait-hormuz-2026-08-25/)
- [Reuters：8月25日黄金/白银](https://www.reuters.com/world/india/gold-rises-highest-since-mid-may-buying-momentum-builds-2026-08-25/)
- [Reuters：铜价与区域库存错配](https://www.reuters.com/business/us-tariff-threat-upends-copper-surplus-prices-test-all-time-peak-2026-08-25/)
- [隆众资讯 via Mysteel：浮法玻璃厂库](https://www.mysteel.com/oilchem/a/26082016/2D4AB63D4A779922.html)
- [PVC供需与库存](https://goodsfu.10jqka.com.cn/20260825/c679251894.shtml)
- [BEA：Personal Income and Outlays日历](https://www.bea.gov/sites/default/files/2026-02/pi1225.pdf)
- [EIA：Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/index.php)
- [Kansas City Fed：2026 Jackson Hole](https://www.kansascityfed.org/research/jackson-hole-economic-symposium/)
- [CFTC：COT Release Schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：EG2610回撤确认多；V2701反弹失败空；FG701反弹失败空。
C. 今天应继续观察的机会：FU2611/SC在WTI继续下跌后的重新定价、LC2701暴跌后的curve/实体确认、CU2610关税驱动区域库存错配。
D. 今天必须避免或退出的交易：追EG突破、低开追空V/FG、第一刀抄底FU/SC、追空LC、PCE前裸买高IV贵金属期权、任何C/D级basis或临交割curve“套利”。