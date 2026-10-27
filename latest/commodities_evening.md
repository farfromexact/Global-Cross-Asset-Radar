# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-27｜edition：commodities_evening｜信息截点：2026-10-27 19:39 BJT**  
**prompt_version：radar_2026-10-12_stock_v1｜data_protocol_version：china_commodities_core_2026-10-17_v1**

> **一句话结论：截至本报告时点，无可立即执行的合格新交易；甲醇、铜仅保留21:15后确认候选，原油方向因海外报价冲突与事件风险暂缓。**

研究机会存在，但条件未到：MA701和CU2612具三层证据；BU2701已研究但追价赔率不足；SC2612有方向假设但海外油价口径冲突；DCE官核、商品期权执行报价和高质量Physical不足使相关结论局部降级。最有价值的下一观察是21:15的MA/PX/曲线、CU/LME/曲线、SC/Brent/曲线三组同步验证。

## 1. 数据质量与覆盖

| 模块 | 实际取得 | 就绪判断 | 主要缺口 |
|---|---:|---|---|
| Futures | 2026-10-27，806合约/77产品；SHFE238、INE63、DCE214、CZCE243、GFEX48 | full_market_ready=true，source-date match=100% | 动态参数覆盖约30.15% |
| Market State | 77产品、20日历史 | 可研究 | 连续主力不替代准确合约 |
| Physical | 18/20 fresh；18条basis | 不可方向评分 | A/B=0；SHFE/DCE/GFEX仓单错误或旧值，5条延续 |
| External | 17/22 fresh，context_only | 映射可用 | repo Brent110.16与Reuters 15:18 BJT的116.24冲突 |
| Historical Night | 10/26晚—10/27凌晨，416/806（51.61%） | 发布/验证通过，但不完整 | raw latest=0 bytes；214 query/unresolved；非今晚 |
| Options | 968 records；44/64成功，ATM44、skew25 | 局部ATM/skew可研究 | surface/positioning/execution均0，bid/ask=0，非全链 |
| 官方crosscheck | SHFE238、INE63、CZCE243、GFEX48 matched | 四所无可信价格差异 | DCE HTTP412；成交量/OI未官核 |
| Stock | 10/21行情5568/5576；最小财务包2公司 | 仅利润桥背景 | execution=false，行情陈旧 |

五层证据严格分为价格/量仓、期限/basis/仓单、实体、海外宏观、期权；历史Night属于第一层而非第六层。今晚21:00属于**2026-10-28交易日**，尚未发生，不能作为证据。

## 2. 全范围扫描与12项仪表盘

后台覆盖原63代码及引擎实际77产品：黑色整体未见跨层新异常；有色以铜供应事件最突出；能源化工价曲最强但地缘与报价口径冲突；新能源LC仅反弹、实体仓单过期；农产品LH/M弱但DCE官核缺；EC移仓与事件噪声高。

| 标的 | EOD close/settle | 1D/5D | ΔOI | 曲线/期权 | 结论 |
|---|---:|---:|---:|---|---|
| MA701 | 3448/3402 | +1.67%/+8.45% | -48,484 | 近月+5.58%；MA612 ATM IV49.66% | 强但不追，等PX同步 |
| CU2612 | 108390/108640 | +0.43%/+0.19% | +524 | +0.64%；ATM IV12.49% vs RV11.40% | HVC条件多 |
| SC2612 | 733.7/731.6 | -1.10%/+0.59% | -1,528 | -0.44%；ATM IV68.28% | 内弱外强冲突 |
| BU2701 | 4965/4893 | +3.27%/+9.51% | +17,992 | +7.27% backwardation | 强但赔率恶化 |
| FU2701 | 5386/5295 | +1.09%/+7.45% | +2,123 | +12.70% | 近月紧，不追 |
| SH701 | 1486/1499 | -3.54%/-13.00% | +1,691 | 曲线+1.17%；RR25 -3.75 | 价空曲线反对 |
| SA701 | 981/968 | +0.62%/+2.33% | -44,376 | contango -2.28% | 上涨减仓 |
| LC2701 | 98500/97840 | +3.08%/-1.91% | -4,815 | ATM IV54.01% | 20D仍-25.36% |
| LH2701 | 9975/9805 | +0.77%/-3.02% | -18,181 | contango -4.90% | 旧空降级 |
| AG2612 | 12763/12986 | -0.49%/-6.31% | -1,182 | IV42% vs RV30.11% | FOMC前不追空 |
| M2701 | 3200/3199 | -1.39%/-2.38% | -80,008 | contango -2.34% | 弱但DCE未官核 |
| PX612 | 9746/9684 | -1.38%/+3.35% | -15,795 | 10/28到期、无bid/ask | 与MA分化；回避期权 |

## 3. 相比前序的真变化

1. **MA**：分数68→73；价格与曲线增强，但PX反向、OI下降构成反证，仍未执行。
2. **CU**：70→72；Teck确认HVC罢工后降负荷运行，但沪铜日内弹性温和，需跨市场确认。
3. **SC**：67→66；国内价曲偏空，Reuters Brent仍在116.24美元/桶，且与repo 110.16冲突，空头条件更严。
4. **BU**：67→71；价、OI、曲线同强，但5日涨幅已大，回踩前不追。
5. **LH**：64→59并移出Top5；反弹且OI下降约9.43%，无法证明趋势空延续。
6. **Options**：T日ATM/skew局部可读，但所有系列execution=false，不把研究信号写成可成交结构。

## 4. 产业链传播与Stock利润桥

- 原油→燃料油/沥青→化工：FU/BU近月最强，SC日盘较弱；外油高位与国内回落并存，置信度中。
- 煤/原油→甲醇→烯烃/PX：MA强、PX弱；只有夜盘同步才确认价差不是短挤，置信度中。
- 铜矿→冶炼→铜材：HVC罢工提供实体催化，CU曲线正向支持，但现货TC新值缺失，置信度中高。
- 黑色链：未见跨层新异常；需求、利润和DCE官核缺口使置信度低。
- 饲料→生猪：LH反弹与OI大降削弱追空，等待10/28日盘。

Stock限定补证仅覆盖映射公司紫金矿业/宝钢股份，并只对紫金三季报做公开补证。紫金2026年1—9月披露收入约2835亿元、归母净利575亿元、经营现金流843亿元；利润桥仍需售价/销量、矿山成本、库存、套保、汇率、资本开支和少数股东共同解释，不能据此给精确铜价弹性。HVC 1—20D事件用CU/LME更纯；紫金是金铜混合暴露且当前证券执行能力未核。

## 5. 统一机会榜

| 排名 | 机会 | 分项（逻辑/赔率/催化/价曲波/拥挤） | 总分 | 五层 | 研究/证据/执行 |
|---:|---|---:|---:|---|---|
| 1 | MA701条件多 | 20/14/14/13/12 | 73 | 支持1/2/5；反对3/4 | 优先/三层/等待顺序触发 |
| 2 | CU2612 HVC条件多 | 20/15/16/11/10 | 72 | 支持1/2/3；反对4/5 | 优先/三层/等待CU-LME |
| 3 | BU2701回踩多 | 19/14/15/14/9 | 71 | 支持1/2/4；反对3/5 | 优先/三层/不追价 |
| 4 | SC2612 contango条件空 | 19/14/13/11/9 | 66 | 支持1/2；反对4/5 | 观察/两层上限/Brent条件失败 |
| 5 | SH701观察空 | 17/13/11/12/11 | 64 | 支持1/5；反对2 | 观察/两层/价曲冲突 |

## 6. 三张研究/交易卡

### MA701条件多｜COM-M-MA701-OIL-CHEMICAL-GAP-RETENTION-20261024

事实是结算3402、5D+8.45%、近月backwardation 5.58%；定价已明显，不把强势包装成未定价。只有**21:15后MA≥3485持续15分钟 AND PX≥9800 AND同一可比近月曲线≥5%**，随后回踩3455—3470守住3440，才按50%/50%分批。计划止损3400；PX<9680或曲线<3%逻辑失效；TP1 3550、TP2 3640，10/30 14:45时间退出。

好/中/坏入场3455/3462.5/3470，对3400风险55/62.5/70点；TP1毛R 1.73/1.40/1.14，TP2 3.36/2.84/2.43，费用滑点未知。合约乘数10吨、tick 1元、tick价值10元；margin 9%、限幅8%、LTD 2027-01-14。按结算价，一限压力约2721.6元/手，两限复利约5660.9元/手；止损不封顶。MA612期权仅研究，最高净支出待询价。

### CU2612条件多｜COM-M-CU2612-HVC-STRIKE-WATCH-20261025

HVC已罢工且降负荷，但影响取决于持续时间；LME/SHFE高位已计价一部分。入场要求**CU≥108950持续15分钟 AND LME 3M≥14450 AND CU2611-12曲线≥0.60%**，随后回踩108700—108850承接，50%/50%。止损107900；Teck复产或LME<14250持续30分钟失效；TP1 110500、TP2 112200，11/05退出。

中位108775风险875点，TP1/TP2毛R约1.97/3.91；坏价108850为1.74/3.53。乘数5吨、tick10元、tick价值50元、LTD 12/15；动态保证金/限幅未核，压力只按公式计算。CU2612期权ATM IV12.49%略高于RV11.40%，但无bid/ask，不称便宜或可执行。

### SC2612条件空｜COM-E-SC2612-CONTANGO-REVERSAL-SHORT-20261026

国内结算731.6、1D-1.10%、contango -0.44%，但Reuters Brent 116.24与repo 110.16冲突，且地缘运输风险仍高。只有**SC≤728持续15分钟 AND精确曲线≤-0.60% AND同一Brent合约≤114**，随后反弹730—733失败才空。止损738；Brent>118或曲线≥0失效；TP1 714、TP2 702，10/29退出。

中位731.5风险6.5点，毛R 2.69/4.54；当前Brent条件未满足。乘数1000桶、tick0.1元、tick价值100元、LTD 11/30；4%只是合约基线，现行动态限幅未核，不能当风险上限。SC2612 ATM IV68.28%高于RV44.44%，且无bid/ask，回避裸买高IV。

## 7. 商品期权专项

口径是core_v1/sampled_strikes：44个产品ATM局部ready、25个skew局部ready，完整surface、positioning、execution均为0，full_chain_verified=false。可研究的局部数值包括MA612 ATM IV49.66%、RR25+1.05；CU2612 ATM IV12.49%；SC2612 ATM IV68.28%；SH701 RR25-3.75；PX612临到期ATM IV32.64%低于RV34.07%。但bid/ask覆盖为0，不能生成可成交权利金、净成本、滑点、全链PCR、dealer gamma或期限曲面。PX期权次日到期且零报价，必须回避。

## 8. 21:00夜盘风险地图

- Previous China EOD：MA/BU/FU强，SC弱，CU温和；这是10/27完整日盘。
- Historical Night：10/26晚至10/27凌晨仅416/806，raw latest空；只能解释前一会话，不能称“今晚”。
- Overseas：15:18 BJT Reuters Brent116.24、WTI102.07；HVC罢工仍在；金银受美元/FOMC预期压制。

21:00第一跳一律不追。21:15查价格持续与精确曲线，21:30查跨市场/产业品同步，21:45再查成交与OI快照是否支持；OI只作线索，不判新多新空。LH/LC等无夜盘品种下一窗口为10/28 09:00，同样等待15/30/45分钟。

## 9. 未来24小时/7日事件

- 10/28 22:30 BJT：EIA周报；SC/BU/FU降Delta，只有合格报价才考虑有限净支出凸性。
- 10/29 02:00/02:30：FOMC声明/记者会；贵金属与铜避免裸Vega和追价。
- 10/29：Teck Q3及运营更新；HVC复产/罢工时长是铜逻辑分水岭。
- 未来7日：中东外交、Houthi袭击与Hormuz航运；止损不防地缘gap。
- CFTC、USDA天气/作物窗口继续监测，但本报告未独立核实精确发布时间；同期无已确认的OPEC+/IEA新增发布，不预置方向。

## 10. 发布前检查与来源

评分加总、证据层上限、MA/CU/SC的R和MA连续限幅压力已重算。未通过项：report_input空、Night raw空、今晚Night尚未发生、期权bid/ask=0、Physical无A/B basis、DCE官核HTTP412、Brent口径冲突、动态合约参数不全。  
主要来源：[EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)、[Options Quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[Crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)、[Reuters油价](https://www.reuters.com/business/energy/oil-eases-middle-east-diplomacy-hopes-saudi-attacks-keep-supply-worries-alive-2026-10-27/)、[Teck HVC](https://www.teck.com/news/news-releases/2026/teck-provides-update-on-highland-valley-copper-operations)、[Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)、[EIA](https://www.eia.gov/petroleum/supply/weekly/schedule.php)。

A. 今晚没有应立即建立的新仓位。  
B. 今晚仅应挂条件的候选：MA701三条件回踩多、CU2612三市场确认多、SC2612三条件反弹空。  
C. 今晚继续观察：BU/FU强曲线、SH价曲线冲突、LH反弹后趋势、AG/金银FOMC风险。  
D. 今晚必须回避或有条件退出：21:00第一跳追价、把历史Night当今晚、Brent口径未统一时交易、PX临到期期权及任何零bid/ask结构、DCE未官核品种即时执行。
