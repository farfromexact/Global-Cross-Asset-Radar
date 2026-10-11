# 全球跨资产高风险机会雷达（晚间版）— 2026-10-11

- **prompt_version**：radar_2026-09-06_coverage_v1
- **生成时间**：2026-10-11T20:08:34+08:00
- **信息截点**：2026-10-11 20:05 北京时间
- **最近完整时段**：海外与中国均为2026-10-09收盘；周日不存在新的全球现金/期货完整EOD。
- **下一实际窗口**：CME Globex预计10月12日06:00、中国市场09:30、美股21:30；美国现金国债因Columbus Day关闭。
- **前序基准**：最近全球报告为2026-10-11晨报；最近同版为2026-10-10晚报。两者均严格早于本次截点。
- **研究性质**：只作研究和决策支持，不自动下单；没有成交反馈，不假设用户持仓。

## 一、今日一句话结论

**周日无立即新仓、但有周一条件机会：沙特风险已压低本地股市，却尚未获油价确认；黄金韧性与AI内部轮动仍是首要背离。**

今天究竟有没有值得冒险的机会：**没有可立即建立的新仓**。有三项周一条件候选（GLD、SOXX、CL），但价格仍沿用周五，周日新闻只能改变先验，不能替代重开后的价格、曲线和期权报价。市场是“政策信用/地缘通胀尾部 + AI内部轮动”的混合状态；最重要背离仍是黄金抗高实际利率，以及QQQ强而半导体弱。

## 二、时间、数据与市场仪表盘

读取状态严格区分：全球价格与中国期指为ok但沿用周五；HY OAS按原生频率滞后一日；MOVE为延迟值；中国期权为stale，历史层为empty；中国商品当前刷新为error，但经验证的10月9日last-good仍有效，不将刷新失败写成源文件为空。

| 资产 | 最新值 | 单日变化 | 一周变化 | 信号 | 数据时间 |
|---|---:|---:|---:|---|---|
| US2Y | 4.80% | +5bp | +2bp | front-end hawkish | 沿用2026-10-09 official close |
| US5Y | 5.02% | +3bp | about +1bp | CPI selling pressure | 沿用2026-10-09 official close |
| US10Y | 5.24% | +2bp | about flat | auction relief failed to extend | 沿用2026-10-09 official close |
| US30Y | 5.60% | 0bp | -1bp | 5.55 trigger not met | 沿用2026-10-09 official close |
| US10Y real | 2.91% | +4bp | about +3bp | gold headwind | 沿用2026-10-09 official close |
| 10Y BEI | 2.33% | -2bp | about -3bp | real-rate led move | 沿用2026-10-09 derived |
| 2s30s | +80bp | -5bp | about -3bp | flattening after relief | 沿用2026-10-09 derived |
| DXY | 102.10 | about flat | about +0.7% | high but gold resilient | 沿用2026-10-09 close-like |
| QQQ | 751.27 | +0.47% | about +0.6% Nasdaq proxy | index resilient | 沿用2026-10-09 close |
| SOXX | 559.40 | -0.61% | about -3% | underperforming QQQ | 沿用2026-10-09 close |
| WTI | 91.85 | +0.4% | +0.8% | geopolitical tail | 沿用2026-10-09 settlement-like |
| Brent | 104.72 | +0.4% | +2.4% | shipping premium | 沿用2026-10-09 settlement-like |
| Gold spot | 4194.36 | up | +1.3% | up despite real yields | 沿用2026-10-09 close-like |
| Gold Dec26 | 4216.30 | +1.4% | unverified | breakout candidate | 沿用2026-10-09 settlement-like |
| VIX | 14.84 | -3.70% | about -3.1% | index tail calm | 沿用2026-10-09 close |
| MOVE | 98.47 | -1.8% | about -5% | payer skew still elevated | 沿用2026-10-09 delayed |
| US HY OAS | 315bp | +6bp | +5bp | caution not crisis | 沿用2026-10-08 FRED |
| IH2612 / SSE50 | 2764.0 / 2807.46 | +0.23% / +0.08% | 20D spot -3.84% | basis -43.46, ann -8.07% | 沿用2026-10-09 close |
| IF2612 / CSI300 | 4244.8 / 4317.25 | +0.21% / +0.16% | 20D spot -5.17% | basis -72.45, ann -8.75% | 沿用2026-10-09 close |
| IC2612 / CSI500 | 7111.0 / 7251.01 | +0.23% / +0.04% | 20D spot -6.50% | basis -140.01, ann -10.06% | 沿用2026-10-09 close |
| IM2612 / CSI1000 | 7015.8 / 7155.91 | +0.36% / +0.24% | 20D spot -5.84% | basis -140.11, ann -10.21% | 沿用2026-10-09 close |
| HO/IO/MO ATM IV | missing | missing | missing | stale last-good 2026-09-23 | not current |

2s30s、实际利率与BEI均由同一收益率冲击派生，不重复当成三层独立证据；价格/OI象限只能提供归因线索，不能唯一识别新多、新空或空头回补。

## 三、相比晨报真正发生了什么

1. **支持油价事件凸性、但不是油价确认**：10月11日胡塞再次警告沙特机场，利雅得机场仍关闭；沙特TASI跌1%、Saudi Aramco跌0.6%，卡塔尔指数跌1%。这是当地风险资产反应，不是WTI、Brent或OVX重定价证据。
2. **油价反证也更清楚**：墨西哥湾生产仍大面积关闭，但人员开始回撤复产；美国准备释放至多400万桶SPR，且替代出口线路减轻部分短缺。故只上调蝶式，不追裸Delta。
3. **GLD与SOXX维持**：周日没有新的金价、美股或期权面。晨报的金价—实际利率背离及QQQ—半导体分化仍有效，分数不因新闻机械增加。
4. **中国IM/IF降级**：财政、就业支持不变，但台海与全球地缘风险增加高Beta小盘跳空风险；当前HO/IO/MO曲面不可用，60降至58。
5. **TLT降级**：能源通胀尾部与周一现金国债休市降低锚质量，68降至67；不以稀薄TLT交易反推完整收益率信号。

### 旧建议台账

| idea_id | 首次提出 | 上次状态 | 当前状态 | 变更原因 |
|---|---|---|---|---|
| GOLD-CREDIT-GLD-CALL-20261009 | 2026-10-09 | morning 84; wait trigger/quote | 84; unchanged | Saudi reaction supports tail but no gold price reset |
| AI-SOXX-DOWNSIDE-20261009 | 2026-10-09 | morning 81; wait failed rebound | 81; unchanged | no new price |
| OIL-HORMUZ-BFLY-20261008 | 2026-10-08 | morning 77; wait reopen/quote | 80; wait price/curve/quote | new Houthi warning and Saudi equity selloff; restart/SPR offset |
| US-RATES-TLT-CALL-20261009 | 2026-10-09 | morning 68; observe | 67; defer cash bond reopen | oil inflation tail and Monday holiday |
| CN-EQ-IM-IF-REVERSAL-20261010 | 2026-10-10 morning | morning 60; wait 10:15 | 58; stricter risk filter | view revision: weekend risk increases high-beta gap |
| CN-EQ-IH-IM-STYLE-20261008 | 2026-10-08 | withdraw new order | withdrawal maintained | view revision; no re-entry |
| US-RATES-TLT-PUT-20261008 | 2026-10-08 | withdraw research | withdrawal maintained | prior data correction; no re-entry |

“持有/退出”仅适用于**若此前已按条件建立**；本报告不把研究候选、模拟交易与真实仓位混同。

## 四、机会排行榜

评分顺序为逻辑/赔率凸性/催化/价格曲线波动率/拥挤技术；总分已复核。分数不是胜率、预期收益或仓位指令。

| 排名 | 机会 | 总分与分项 | 研究判断/证据 | 执行 | 最大损失 |
|---:|---|---|---|---|---|
| 1 | GLD 2027-01-15 380/410 Call Spread | 84（23/22/18/11/10） | 存在待验证优势；部分 | 休市/等待触发 | 有限 |
| 2 | SOXX 2026-11-20 560/520 Put Spread | 81（22/21/19/10/9） | 存在待验证优势；部分 | 休市/等待触发 | 有限 |
| 3 | CL Dec-26 100/110/120 Call Butterfly | 80（20/21/20/9/10） | 存在待验证优势；部分 | 待报价或参数 | 有限 |
| 4 | TLT 2026-11-20 78/82 Call Spread | 67（17/20/18/6/6） | 优势减弱但未失效；部分 | 等待触发 | 有限 |
| 5 | Long IM2612 / short IF2612 nominal-neutral | 58（16/12/16/7/7） | 存在待验证优势；部分 | 等待2026-10-12 10:15三重触发 | 非有限 |

| 机会 | 逻辑依据/缺口 | 赔率凸性 | 催化 | 价格/曲线/波动率 | 拥挤/技术 | 较晨报 |
|---|---|---|---|---|---|---|
| GLD Call Spread | 23：实际利率/DXY逆风下金价韧性；缺ETF/CFTC当日流 | 22 | 18：CPI、Fed独立性与地缘 | 11：价格有、IV/偏度缺 | 10：突破有、仓位细项缺 | 不变 |
| SOXX Put Spread | 22：QQQ与半导体背离 | 21 | 19：ASML/TSMC/CPI | 10：现价有、IV缺 | 9：相对弱势有、宽度缺 | 不变 |
| CL Call Butterfly | 20：沙特股市已有风险反应 | 21 | 20：重开、升级/缓和、复产/EIA | 9：周日油价/OVX缺 | 10：曲线待重开 | +3 |
| TLT Call Spread | 17：高收益率支持、通胀尾部反对 | 20 | 18 | 6：现金债周一休市 | 6：触发未到 | -1 |
| IM/IF | 16：超跌与政策支持 | 12：线性止损非最大损失 | 16 | 7：期权面陈旧 | 7：贴水/OI意图不明 | -2 |

## 五、前三名交易卡

### 1. GLD 2027-01-15 380/410 Call Spread（84）

- **市场隐含**：金价主要反映降息与一般避险，政策信用溢价未必可持续。
- **分歧**：10Y实际利率2.91%、DXY约102而黄金仍强，使单一降息解释不足；周日沙特股市下跌支持尾部，但ETF流、CFTC与当前IV/偏度缺失，错价待验证。
- **结构**：买1张GLD 2027-01-15 380C，卖1张同到期410C。
- **入场**：周一开盘后30—60分钟，GLD仍高于385.20、现货/最近月黄金守4200、10Y实际利率不高于3.00%；净支出上限11美元。
- **好/中/坏成交**：≤9美元可用0.50% NAV试仓；9—11美元半风险；>11美元或GLD跳空>400放弃。
- **失效/退出**：GLD日收<378，或黄金<4100且实际利率>3.00失效；价差+50%减半，+100%或GLD 405—410再减，12月18日时间退出。
- **风险与Greeks**：最大损失=净支出×100美元/组；初始通常+Delta/+Gamma/-Theta/+Vega，接近410短腿后局部Gamma/Vega下降。实时Greeks未取得。
- **最强反证**：实际利率持续>3%且黄金恢复与DXY/实际利率稳定反向；ETF持续流出或央行购金显著放缓。

### 2. SOXX 2026-11-20 560/520 Put Spread（81）

- **市场隐含**：QQQ韧性可外推至半导体，AI盈利足以吸收高融资成本与供应链风险。
- **分歧**：周五QQQ上涨而SOXX/SMH下跌，IGV/ORCL上涨，显示内部轮动而非全面AI崩塌；因此做指数有限风险下行，不裸空单一公司。
- **结构**：买1张SOXX 2026-11-20 560P，卖1张520P。
- **入场**：首小时反弹至563—566失败，或跌破557且SMH与半导体宽度同步；SOXX<552不追。净支出≤13美元。
- **好/中/坏成交**：≤10.5美元用0.50% NAV；10.5—13美元半风险；>13美元或低开<552放弃。
- **失效/退出**：SOXX日收>575或SMH>615并连续两日宽度改善失效；价差+50%减半，SOXX近540或+100%再减；若盈利，TSMC前降风险。
- **风险与Greeks**：最大损失=净支出×100美元/组；初始通常-Delta/+Gamma/-Theta/+Vega，接近520后凸性下降。
- **最强反证**：ASML与TSMC同时确认订单、毛利韧性，且云软件与半导体宽度共同改善。

### 3. CL Dec-26 100/110/120 Call Butterfly（80）

- **市场隐含**：中东与天气停产推高油价，但替代出口、SPR与复产会限制上行；周日沙特股票已开始反映风险。
- **分歧**：再次警告机场与当地股市下跌使100—120区间事件凸性更有吸引力；但油价和OVX尚未重开，不能认定期权便宜。
- **结构**：买1张CL Dec-26 100C、卖2张110C、买1张120C。
- **入场**：Globex重开30分钟后，WTI守92.50且近月backwardation不弱化，净支出≤2.80美元/桶；WTI开盘>98不追。
- **好/中/坏成交**：≤2.20美元/桶用0.35%—0.50% NAV；2.20—2.80半风险；>2.80或曲线转弱放弃。
- **失效/退出**：WTI结算<90.50或运输/平台复产使实货风险明显消退；价差+50%减半，+100%或WTI 107—112再减，10个交易日退出。
- **风险与Greeks**：最大损失=净支出×1000美元/组；Greeks状态依赖，初始通常+Delta/+Gamma/+Vega，靠近110后Delta/Gamma可能翻转；直接越过120也不会继续受益。
- **最强反证**：复产快于预期、SPR/替代航线消除近端紧张，backwardation持续弱化。

## 六、美国利率、美元、原油与风险指标

- **利率事实**：2Y/5Y/10Y/30Y分别约4.80%/5.02%/5.24%/5.60%；10Y实际利率2.91%，10Y BEI约2.33%，2s30s约+80bp。长端高位更像通胀、财政供给与期限溢价的“坏利率上升”，而非纯增长改善。
- **曲线策略**：2s10s、2s30s、5s30s均已扫描；缺少实时掉期/期货DV01与周一现券价格，不发布DV01中性可执行单。
- **美元/FX**：DXY约102.10；EUR/USD、USD/JPY、USD/CNH背景已筛选，但FX期权偏度和拥挤数据缺失，未发现独立合格交易。
- **原油**：方向、近远月、跨品种及事件凸性已筛选；支持为机场升级、库存缓冲偏薄与天气停产，反对为复产、SPR和替代航线。OVX/偏度缺失，只保留蝶式待报价。
- **风险指标**：VIX 14.84、MOVE 98.47、HY OAS 315bp（10月8日）。低VIX不能单独证明Put便宜；CTA与做市商净Gamma缺失。

## 七、黄金专项

主假设“黄金可体现财政、通胀和货币政策信用风险的期权属性”评估为**增强但未证实为单一主因，较晨报不变**。这里的“期权属性”是经济机制比喻，不表示黄金现货/期货具有合约限定损失。

- **支持**：实际利率和美元偏高时金价仍强；Fed独立性争议、周日海湾风险及财政供给共同提高政策信用尾部。
- **竞争解释**：一般地缘避险、技术突破、周末对冲或美元短线波动也能解释；油价上行若先抬实际利率反而压金。
- **最可能推翻**：黄金在实际利率下行时持续下跌；ETF持续流出；央行购金显著放缓；政策信用新闻不再带来相对强势。
- **候选表达**：3—6个月Call Spread仍优于微型黄金裸期货；微型期货只有现货与期货双突破后确认。黄金+长债Put Spread暂不叠加，避免政策信用/实际利率因子重复。
- **缺口**：当日ETF流、央行购金、最新CFTC细项、黄金3—6个月IV/偏度和实时权利金。

## 八、AI股票专项

判断仍为**估值压缩与内部轮动，叠加供应链尾部；尚非趋势性基本面恶化已确认**。

- 现金流/定价权龙头与软件相对较强；半导体/设备对利率与台海双敏感；网络、电力基础设施需订单验证；高Beta Capex链受融资成本约束。
- “多优质现金流/空Capex Beta”仍是待验证假设，不因Capex高就预设做空。ORCL与IGV走强是重要反证。
- 最合适表达是SOXX有限风险Put Spread；篮子尚未完成权重与Beta校准，不能声称Beta-neutral。财报后IV结构待ASML/TSMC报价。
- 最可能推翻空头：ASML订单、TSMC毛利与云变现共同改善；最可能升级空头：半导体宽度、订单与价格同步恶化。

## 九、中国50/300/500/1000专项

**暂无法确认可执行交易**，不是“今日中国股指无合格交易”：周末无新价格，HO/IO/MO当前曲面缺失，证据不足以排除周一IM/IF机会。中国研究吸引力58，证据部分，执行等待触发。

| 指数 | 1D | 3D | 5D | 20D |
|---|---:|---:|---:|---:|
| 上证50 | +0.08% | -0.56% | +0.02% | -3.84% |
| 沪深300 | +0.16% | -0.93% | -0.54% | -5.17% |
| 中证500 | +0.04% | -2.48% | -2.04% | -6.50% |
| 中证1000 | +0.24% | -1.96% | -1.89% | -5.84% |

- **更适合谁**：若周一宽度与贴水确认，IM比IH/IF/IC更适合超跌修复；否则宁可空仓。IM2612/IF2612名义中性并非Beta中性。
- **相对价值**：最接近触发的是IM-IF；IF-IH、IM-IH、IC-IF、IM-IC未见经验证可执行异常。
- **基差/跨期**：四个主力均贴水，IM/IC更深；无足够借贷、分红和跨月成本数据认定套利错价。
- **期权**：HO/IO/MO last-good停在9月23日，1/3/5/20日ATM IV、25Δ/10Δ wings、RR25、BF25、PCR、成交/OI与Gamma节点均缺。不能比较IV-RV，也不能发布Calendar/Butterfly/Short Gamma。
- **联动边界**：IH↔HO、IF↔IO、IM↔MO；IC只能用MO/IO/50ETF/300ETF期权代理，存在Beta、基差和跟踪误差，不能完全对冲。
- **条件单**：10月12日10:15后，IM-IF前45分钟相对收益>0.35个百分点、CSI1000上涨家数>60%、IM年化贴水相对IF收窄≥25bp，且人民币/台海风险未恶化。
- **失效/退出**：相对收益-0.60个百分点或IM贴水比IF更差>75bp失效；+1.0个百分点减半、+1.8再减，10日退出。
- **合约风险**：IM乘数200元/点、IF 300元/点；保证金不是最大损失，隔夜跳空可穿越止损，名义错配须控制在3%以内。

## 十、中国商品全域扫描

China-Commodities-Engine固定commit为8996bd8604398a263fd1f5838d607de595229cda。10月11日19:01—19:06刷新五所均失败/零记录，但经验证的10月9日last-good包含77个品种、806合约、20期历史且source_date_match=100%，仍按原生频率有效。基差和会员排名缺失；期权面为空、不可执行。

| 品种/主力 | 1D | 3D | 5D | 20D | OI 1D | 近次月差 | 归因线索 |
|---|---:|---:|---:|---:|---:|---:|---|
| MA/MA701 | 5.50% | 12.69% | 14.83% | 15.15% | 10.20% | 16.0775% | price_up_oi_up |
| PG/PG2611 | 4.34% | 12.22% | 13.94% | 20.82% | 0.61% | 9.3482% | price_up_oi_up |
| SN/SN2611 | -4.29% | -4.36% | -5.05% | -5.92% | 11.92% | 0.0051% | price_down_oi_up |
| EC/EC2611 | -3.32% | -4.27% | 0.05% | 31.47% | -7.70% | -22.4809% | price_down_oi_down |
| EG/EG2611 | -2.88% | 0.11% | -0.68% | -2.43% | -1.27% | 9.9163% | price_down_oi_down |
| JM/JM2701 | 2.81% | 4.55% | 1.57% | -8.31% | 2.50% | 3.478% | price_up_oi_up |
| L/L2701 | 2.49% | 7.09% | 8.01% | 5.64% | 7.39% | 3.1645% | price_up_oi_up |
| PP/PP2701 | 2.31% | 7.84% | 9.31% | 8.95% | 7.98% | 3.0702% | price_up_oi_up |
| LC/LC2701 | -2.30% | -0.67% | -5.93% | -22.54% | 2.92% | 1.2155% | price_down_oi_up |
| FU/FU2701 | 2.19% | 11.17% | 14.32% | 22.08% | 0.40% | 8.7022% | price_up_oi_up |
| PT/PT2612 | 0.99% | -1.46% | -5.20% | -6.54% | 4.19% | 3.6457% | price_up_oi_up |
| AU/AU2612 | 0.48% | 0.14% | -3.46% | -5.89% | 0.63% | -0.6323% | price_up_oi_up |

未入榜板块：能源化工中MA/PG/L/PP强、EG弱；黑色JM反弹但20日仍跌；新能源LC持续弱；贵金属AU需外盘重开验证；农产品无统一异常。上述价格/OI仅为线索，不能证明资金方向。

## 十一、事件日历（北京时间）

| 时间 | 事件 | 风险动作 |
|---|---|---|
| 2026-10-11晚间 | 中东、台海与墨西哥湾复产消息 | 不开新仓；只维护周一有限损失条件单 |
| 2026-10-12T06:00:00+08:00 | 预计CME Globex重开 | 等待至少30分钟；不追油金跳空，核验backwardation |
| 2026-10-12T09:30:00+08:00 | 中国市场重开 | 风格交易延后到10:15，联看人民币、宽度、贴水 |
| 2026-10-12 | Columbus Day：美国国债现金市场关闭，美股预计正常开市 | TLT不立即入场 |
| 2026-10-13 | IMF世界经济展望；JPM/GS/C/WFC盘前财报 | 降低金融Delta，保留有限凸性 |
| 2026-10-14T09:30:00+08:00 | 中国9月CPI/PPI | 期权面仍缺时不做Vega结构 |
| 2026-10-14 欧洲盘前 | ASML Q3业绩 | SOXX Put若盈利先减 |
| 2026-10-14T20:30:00+08:00 | 美国9月CPI（预期总3.7%、核心2.5%，以发布为准） | 降低裸Delta，保留有限凸性 |
| 2026-10-15T14:00:00+08:00 | TSMC Q3业绩会 | 订单/毛利上修使SOXX空头失效 |
| 2026-10-15T17:00:00+08:00 | 中国社融/信贷可能窗口（时点未官方确认） | 暂定事件，压低中国风格风险 |
| 2026-10-15T20:30:00+08:00 | 美国PPI与零售销售 | 通胀因子总风险不超1.50% |
| 2026-10-16T00:00:00+08:00 | EIA周度石油报告（假期顺延） | 油价结构发布前不加码 |
| 2026-10-16T15:00:00+08:00 | CFFEX股指期货期权月度到期 | 区分移仓流与真实趋势 |

## 十二、覆盖核对

| 项目 | 状态 | 说明 |
|---|---|---|
| 应覆盖 | 完整 | 全球利率/FX/股票/AI/油/金/风险；中国IH/IF/IC/IM、HO/IO/MO及ETF期权；77个商品；方向、曲线、跨期、相对价值、波动率/偏度/事件凸性；1/3/5/20日。 |
| 实际取数且分析 | 部分完整 | 全球及中国价格沿用10月9日；周日沙特/卡塔尔股市与新闻新增；77个商品last-good全部分析。 |
| 数据不足 | 明确 | 全球同步期权IV/偏度/Greeks、OVX、当前HO/IO/MO、CTA/净Gamma、商品现货基差/会员排名/可执行期权面、黄金当日ETF/CFTC/央行购金。 |
| 不适用/流动性不足 | 明确 | 周日现金与场内衍生品不可执行；IC无一一对应指数期权；没有可靠曲面时拒绝短Gamma/裸卖。 |

逐品种商品状态已保存在JSON；实际应覆盖77、已取数分析77、数据不足77（每个品种均缺当前可执行期权/基差中的至少一类）。这不是缩小覆盖，而是对每个工具边界逐项降级。

## 十三、数据引擎与主要来源

- China-Options-Engine固定commit：2e336cbe016f9452f9214f0b8fc234e4e9265283；data/radar_latest.json和data/latest.json为2026-09-23，radar_history.json为**empty**，不是missing/parse_error。
- China-Commodities-Engine固定commit：8996bd8604398a263fd1f5838d607de595229cda；本次刷新错误不使已验证last-good自动失效。
- [Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)（U.S. Treasury，2026-10-09）：US 2Y/5Y/10Y/30Y yields。
- [Daily Treasury Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026)（U.S. Treasury，2026-10-09）：10Y real yield。
- [ICE BofA US High Yield Index Option-Adjusted Spread](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)（FRED，2026-10-08）：HY OAS。
- [Stocks advance ahead of earnings, navigating still-high Treasury yields and oil prices](https://www.reuters.com/world/china/global-markets-wrapup-1-2026-10-09/)（Reuters，2026-10-09）：Friday cross-asset close context；semiconductor relative weakness。
- [Houthi attack on Saudi airport kills 12, over 300 wounded](https://www.reuters.com/world/middle-east/loud-blast-heard-riyadh-airport-airlines-cancel-more-flights-2026-10-10/)（Reuters，2026-10-10）：weekend Middle East escalation。
- [Hormuz transits lowest in over two months while alternative exports rise](https://www.reuters.com/business/energy/hormuz-transits-lowest-over-two-months-after-attacks-data-shows-2026-10-08/)（Reuters，2026-10-08）：alternative-route counterevidence to oil shortage。
- [US says Chinese actions off Taiwan are deeply destabilising](https://www.reuters.com/world/china/us-says-chinese-actions-off-taiwan-are-deeply-destabilising-2026-10-10/)（Reuters，2026-10-10）：weekend Taiwan risk。
- [China ramps up fiscal push to meet growth target](https://www.reuters.com/world/china/china-ramps-up-fiscal-push-meet-growth-target-2026-10-09/)（Reuters，2026-10-09）：CNY550bn unused debt quota。
- [China adds 10.52 million urban jobs in Jan-Sept](https://www.reuters.com/world/asia-pacific/china-adds-1052-million-urban-jobs-jan-sept-roll-out-services-jobs-policy-2026-10-10/)（Reuters，2026-10-10）：employment support。
- [China issues guidelines on new productive forces including AI](https://www.reuters.com/world/asia-pacific/china-issues-guidelines-new-productive-forces-including-ai-2026-10-09/)（Reuters，2026-10-09）：China AI policy supports core tech and warns against blind investment。
- [White House launches probe involving Fed Governor Lisa Cook](https://www.reuters.com/world/us/trump-launches-committee-probe-feds-lisa-cook-white-house-statement-2026-10-09/)（Reuters，2026-10-09）：Fed independence tail。
- [China-Options-Engine radar latest](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)（GitHub/farfromexact，2026-09-23）：last-good option snapshot；630 official matches。
- [China-Options-Engine last run status](https://github.com/farfromexact/China-Options-Engine/blob/main/data/last_run_status.json)（GitHub/farfromexact，2026-10-10）：current refresh missing；restored latest 2026-09-23。
- [China-Commodities-Engine report input latest](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)（GitHub/farfromexact，2026-10-09）：77-product full scan；20-session comparisons。
- [China-Commodities-Engine last run status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)（GitHub/farfromexact，2026-10-10）：weekend refresh errors；last-good preservation。
- [US CPI release calendar](https://www.bls.gov/schedule/news_release/cpi.htm)（BLS，2026-10）：US CPI timing。
- [Columbus Day market schedule](https://www.sifma.org/resources/general/holiday-schedule/)（SIFMA，2026-10）：US bond cash holiday。
- [Yemen's Houthis renew warning over Saudi airports after deadly Riyadh attack](https://www.reuters.com/world/middle-east/yemens-houthis-renew-warning-over-saudi-airports-after-deadly-riyadh-attack-2026-10-11/)（Reuters，2026-10-11）：renewed airport warning；Riyadh airport remains closed；escalation threat。
- [Saudi stocks slide after attack on Riyadh airport](https://www.reuters.com/world/middle-east/saudi-stocks-slide-after-attack-riyadh-airport-2026-10-11/)（Reuters，2026-10-11）：Saudi TASI -1%；Saudi Aramco -0.6%；Qatar index -1%。
- [Middle East war, high debt levels to dominate IMF-World Bank meetings](https://www.reuters.com/world/china/middle-east-war-high-debt-levels-dominate-imf-world-bank-meetings-bangkok-2026-10-11/)（Reuters，2026-10-11）：energy supply and inflation risks；limited oil storage buffers。
- [Wall St Week Ahead: Bank earnings, CPI headline busy markets week](https://www.reuters.com/business/wall-st-week-ahead-bank-earnings-cpi-headline-busy-markets-week-sp-500-hovers-2026-10-09/)（Reuters，2026-10-09）：bank earnings calendar；US CPI consensus；10Y yield 5.24%。
- [Isaias kills four, about 670,000 without power after landfall](https://www.reuters.com/business/environment/category-3-hurricane-isaias-makes-landfall-near-destin-florida-nhc-says-2026-10-10/)（Reuters，2026-10-10）：Gulf production shutdown；crews redeploying；up to 4mb SPR。

## 十四、风险预算

单一试仓最大损失0.25%—0.75% NAV；单一确认交易0.75%—1.50%；高确信度主题合并不超过2.5%—3.0%。GLD、长黄金、空长债、空美元和多通胀共同暴露于政策信用/实际利率，应合并；CL与通胀、黄金也有重叠。IM/IF、IM-IH与小盘ETF看涨均属中国小盘高Beta因子，不能分开计预算。期货止损不等于最大损失有限，隔夜Gap与保证金追缴必须另留压力预算。

## 十五、今日行动清单

A. 今天可以立即建立的仓位：无；周日休市，且没有可核验实时期权报价。
B. 今天只应挂条件单的仓位：周一仅挂条件单：GLD 2027-01-15 380/410 Call Spread、SOXX 2026-11-20 560/520 Put Spread、CL Dec-26 100/110/120 Call Butterfly；IM2612/IF2612须等10:15三重确认。
C. 今天应继续观察的机会：继续观察TLT 78/82 Call Spread、金价—实际利率背离、油价backwardation、ASML/TSMC前AI内部轮动，以及HO/IO/MO数据恢复。
D. 今天必须避免或退出的交易：避免追逐油金/半导体跳空、用9月23日期权面交易、裸卖波动率、把IC代理期权当完全对冲；继续撤回IH/IM旧风格单与TLT Put旧观点。