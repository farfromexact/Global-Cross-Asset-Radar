# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-02

> revision: 2  
> generated_at_bjt: 2026-09-02T20:52:30+08:00  
> data_protocol_version: china_commodities_v2  
> 中国基线：2026-09-02五所完整EOD；21:00夜盘尚未开始；海外为晚间可验证报价。

## 一、今日一句话结论

**今晚有值得冒险的机会：EG2610回撤承接多84分；MA610 79分、BU2610 74分。SC基本面强但已严重price-in且22:30有EIA，不追。**

19:30 revision 1因9月2日EOD未入库而做数据质量否决；20:19后五所EOD已补齐，因此该否决失效，本版重新按五层证据评分。

## 二、数据质量与覆盖说明

第一读取层：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。统一`report_input_latest.json`仍为空，因此按v2优先级使用module-specific/root层。

9月2日Futures健康：SHFE/INE/DCE/CZCE/GFEX五所、803个合约、`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，4条placeholder排除异常排名。`market_state_latest.json`仍为空，所以不输出伪造的3D/5D/20D、RV20与z-score。

Physical requested_date=2026-09-02，20个目标仅4个映射；JM现货仍为8月20日旬度且basis C级。Options为9月2日22,866合约、380 series、60/64品种，IV coverage约90%、OI coverage约68.5%、bid/ask=0；module-specific `surface_latest.json`为空，按surface/positioning/execution均not ready处理，不输出ATM IV、RR25、BF25、PCR、Dealer Gamma或具体权利金。

Contract metadata仍partial，DCE contract-info失败；缺失动态保证金/限幅必须下单前复核。

## 三、商品市场仪表盘

| 板块 | 合约 | 9/2 close/settle | 1D close | Volume | OI | Curve | 信号 |
|---|---|---:|---:|---:|---:|---|---|
| 能化 | **EG2610** | **5809/5726** | **+5.98%** | 1,889,416 | **379,746** | **Back +5.96%** | **84 条件多** |
| 能化 | **MA610** | **3183/3157** | **+4.57%** | 2,753,905 | 625,478 | **Back +3.01%** | **79 条件多** |
| 能源 | **BU2610** | **4974/5049** | +1.43% | 661,367 | 219,879 | **Back +3.62%** | **74 降级条件多** |
| 原油 | **SC2610** | **693.3/677.3** | **+8.80%** | 245,258 | 39,427 | **Back +4.25%** | **71 EIA后优先** |
| 燃料油 | FU2611 | 3970/3971 | +4.23% | 1,205,970 | 226,371 | Back +8.18% | 不追 |
| PTA | TA701 | 6010/6040 | +1.80% | 1,251,524 | 1,002,816 | Back +2.51% | 69观察 |
| 焦煤 | JM2701 | 1663.5/1703 | -1.97% | 1,502,959 | 552,549 | Back +0.62% | 降温 |
| 玻璃 | FG701 | 961/965 | +0.84% | 1,620,073 | 1,255,495 | Contango | 非短缺 |
| 白银 | AG2610 | 15631/15720 | -3.86% | 564,387 | 223,865 | 轻Contango | 68不追空 |
| 新能源 | LC2701 | 154780/155660 | -3.24% | 186,331 | — | Contango | 不交易 |

Curve为期货期限结构，不等于Spot-Futures basis；C/D basis及context-only海外映射不称套利。

## 四、相比19:30 revision 1真正变化

1. **数据闸门解除。** 20:19后9月2日五所EOD全部fresh，原先“只有海外一层fresh”的结论失效。
2. **EG升为第一。** EG2610 +5.98%，较上一EOD OI约+13.5%，Back由约3.36%扩至5.96%；8月31日华东主港MEG库存14.2万吨、较上期-3.6万吨。国内周产量环比+4.5%是主要反证，因此是近端tightness而非永久短缺。
3. **MA获得今日Physical确认。** MA610 +4.57%、Back 3.01%；9月2日甲醇港口库存64.15万吨、周降4.41万吨/-6.43%。但OI较上一EOD约-5.9%，只能称涨价减仓线索，评分79。
4. **BU从晨间82降至74。** 仍有Back与偏紧Physical，但收盘低于结算、OI较上一EOD约-8%，资金确认明显弱化。
5. **SC观点强、赔率差。** SC日盘+8.8%，Brent却从97.04日内高位回到约94.08；22:30还有EIA，21:00追价不合算。
6. **ADP偏弱不足以扭转贵金属高利率压力。** 美国8月ADP私人就业+3.8万，低于约+4.8万预期；但美元仍处两周高位、10Y约4.8%，AG中国日盘已-3.86%，不追空。

关键来源：
- [Reuters Oil](https://www.reuters.com/business/energy/oil-up-nearly-1-us-iran-trade-fresh-strikes-2026-09-02/)
- [Reuters Hormuz traffic](https://www.reuters.com/business/energy/shipping-traffic-via-strait-hormuz-stays-below-10-day-average-data-shows-2026-09-02/)
- [Reuters Gold](https://www.reuters.com/world/india/gold-hits-over-3-week-low-mideast-tensions-fan-rate-hike-fears-2026-09-02/)
- [Reuters ADP](https://www.reuters.com/business/us-private-payrolls-growth-slows-august-adp-says-2026-09-02/)
- [隆众/东方财富：甲醇库存](https://qhweb.eastmoney.com/news/202609023862683458.html)
- [Mysteel/隆众：MEG库存](https://www.mysteel.com/oilchem/a/26083110/5C0F1416F97D0BD5.html)

## 五、产业链地图

| 产业链 | 方向 | 最强证据 | 最大反证 | 置信度 |
|---|---|---|---|---|
| EG—聚酯 | 偏多 | 价涨仓增+深Back+极低港库+进口约束 | 国内复产 | 高 |
| MA—MTO | 偏多 | Back+港口库存周降6.43%+中东供应风险 | OI下降/MTO不强 | 中高 |
| 原油—沥青 | 偏多但过度延伸 | BU供应库存紧、Hormuz风险 | Brent回吐、EIA、BU OI降 | 中高 |
| 贵金属 | 偏空但不追 | 中国金银弱+美元/长端利率高 | ADP偏弱/地缘避险 | 中 |
| 双焦—钢材 | 降温 | JM仍Back | price下跌、Physical低频 | 中低 |

当前regime：**中东供应冲击进入二阶分化；最有价值的是被库存与curve确认的化工品，而不是继续追原油。**

## 六、机会排行榜

| 排名 | 机会 | 分数 | Fresh方向层 | 阶段 |
|---:|---|---:|---:|---|
| 1 | **EG2610 回撤承接多** | **84** | **4** | confirmed_wait_trigger |
| 2 | **MA610 回撤承接多** | **79** | **4** | conditional_trial |
| 3 | **BU2610 回撤重新确认多** | **74** | **3** | conditional_trial |
| 4 | SC2610 EIA后深回撤多 | 71 | 3 | watch/conditional_after_event |
| 5 | AG2610 失败反弹空 | 68 | 2 | watch |

## 七、前三名交易卡

### EG2610｜84｜回撤承接多
- 21:00后至少等30分钟；5700—5770被吸收并重回5800/VWAP，先1/3；直接>5900等45分钟，不追。
- 首30—45分钟高点突破且Back仍>4.5%再加1/3。
- 30分钟接受5650以下止损；5550以下+Back<3%+港库/进口正常化为逻辑失效。
- TP1 5950，TP2 6150；2个交易日不延续退出；最大损失0.50%—0.75% NAV。
- 常用规格10吨/手、tick 1元/吨、tick value 10元，5809名义约58,090元/手。DCE动态margin、price limit与last trading day本次未确认，1/2个涨跌停压力损失不伪造。

### MA610｜79｜回撤承接多
- 3110—3160守住并重回3180/VWAP，先1/3；直接>3250不追。
- 首45分钟高点突破且Back>2.5%再加。
- 3070下方30分钟接受止损；3000以下+Back<1.5%+库存转累库/进口恢复为失效。
- TP1 3280，TP2 3400；2—3日退出；最大损失0.35%—0.50% NAV。
- CZCE甲醇10吨/手、tick 1元/吨、tick value 10元；3183名义31,830元/手；夜盘21:00—23:00，标准最低保证金5%、标准限幅±4%，动态参数下单前复核；最后交易日为交割月第10个交易日，实物交割。标准4%仅作敏感度：一次不利约1,273元/手，两次连续不利约2,495元/手。

### BU2610｜74｜回撤重新确认多
- 不买21:00首跳。4950—4980守住后收复5040—5050/VWAP，且Brent稳定约94以上，才1/3。
- 4900下方30分钟接受止损；4850以下+Back<2%/转Contango+供应库存改善为失效。
- TP1 5150，TP2 5300；2—3日退出；最大损失0.25%—0.35% NAV。
- SHFE BU为10吨/手、tick 1元/吨、tick value 10元；4974名义约49,740元/手；最后交易日通常为交割月15日，实物交割。当前动态margin/price limit未确认，不硬算停板压力。

## 八、商品期权专项

9月2日raw chain存在，但module-specific surface为空、positioning不ready、execution不ready。研究优先级仅为EG/MA/BU有限风险Bull Call Spread与AG失败反弹后的Put Spread；在surface和真实bid/ask恢复前不报strike、净权利金或Greeks，不裸卖事件Vega。

## 九、21:00夜盘风险地图

| 品种 | 等待 | 操作 |
|---|---:|---|
| EG2610 | 30m；>5900等45m | 5700—5770承接、重回5800才多 |
| MA610 | 30—45m | 3110—3160守住、重回3180才多 |
| BU2610 | 30—45m | 4950—4980守住并收复5040/5050才重新多 |
| SC2610 | 优先等22:30 EIA | EIA前不追；670—680深回撤承接再评估 |
| AU/AG | 30m | 低开不追空；失败反弹+美元/收益率强才看空 |

## 十、未来24h / 7d事件

- 20:15 BJT ADP已公布：8月私人就业+3.8万，低于约+4.8万预期。
- **22:30 BJT EIA Weekly Petroleum Status Report**：今夜SC/FU/BU/LU一级事件，SC新仓优先等数据后。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月4日20:30 BJT美国8月非农：美元/实际利率/金银一级事件。
- Hormuz持续事件：Kpler称周二仅4艘商品船通过，低于前一日10艘和10日均值约13艘；但美国能源部长称周一约1700万桶原油通过，流量高度不稳定。

## 十一、行动清单与风险预算

EG触发后0.50%—0.75% NAV；MA 0.35%—0.50%；BU 0.25%—0.35%；SC若EIA后重新合格≤0.25%。EG/MA/BU/SC/FU/LU共享中东供应冲击与能化beta，初始总最大损失建议≤1.25% NAV。

**A. 今天没有应立即建立的新仓位。**  
**B. 今天只应挂条件单的仓位：EG2610回撤承接多；MA610回撤承接多；BU2610仅在收复5040—5050并重新确认后多。**  
**C. 今天应继续观察的机会：SC2610优先等22:30 EIA后深回撤多、AG2610失败反弹空、TA701成本/curve多。**  
**D. 今天必须避免或退出的交易：21:00追EG/MA/SC高开、机械沿用晨间BU82分、低位追空AU/AG，以及任何基于空surface/零bid-ask的精确商品期权交易。**