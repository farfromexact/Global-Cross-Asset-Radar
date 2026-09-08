# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-08

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-08 19:52 BJT；研究截点：19:30。最近完整中国时段：9月8日日盘；今晚21:00夜盘尚未发生，归属9月9日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；FU2611、MA610、TA701仅在21:00后回撤确认时值得冒险，SC首跳不追。**

当前regime是：**中东供给风险推动原油与炼化扩散、中国日盘能化补涨、贵金属对地缘冲击钝化、黑色建材夜跌日修复、期权曲面可研究但执行被否决。**

## 二、数据质量与覆盖

本期先读取[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)和[雷达](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，再按候选下钻逐合约、Physical、External、Options surface及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，requested_date=2026-09-08，generated_at=19:15:27。
- Futures/Market State：19:02完成；SHFE/INE/DCE/CZCE/GFEX五所共802合约，802/802源日期匹配，full_market_ready=true，critical errors=0；7条placeholder已排除，无重复、非法OHLC、负成交量/OI。
- Physical：19:14更新，20个目标中18个按原生频率fresh、SC/LU unavailable；可计算basis均为C级，只作context。CZCE仓单为当日，GFEX五项沿用9月1日，SHFE/DCE仓单缺失；仓单不等于社会库存。
- External：19:14更新，17/22 fresh、5 unavailable，均为context_only连续或代理数据，不构成exact import parity。
- Options：9月8日当日截面23,150个合约、391个series、61/64产品；PL/PR/ZC因源日期仍为9月7日而失败。IV覆盖98.07%、OI覆盖69.50%、bid/ask覆盖0；380个series surface-ready、80个positioning-ready、0个execution-ready。全局surface/positioning/execution均为false，Dealer Gamma方向未知。
- Metadata：有效合约匹配73.32%，动态参数覆盖约29.8%，未确认字段不猜测。

Night Session质量闸门通过：trading_date=2026-09-08、night_session_date=2026-09-07、generated_at=06:02:17，data_fresh/validation_passed/published/coverage_complete均为true；610个有效夜盘合约、55个产品，189个合法outside-window、3个no-night-trade，missing timestamp/price/quote、query error、unresolved contract均为0，warnings为空。76.06%是制度与窗口口径，不是采集“只完成76%”。

这批Night是**今天凌晨已完成、属于9月8日交易日的连续交易阶段**，仅用于隔夜→日盘分解，绝不是今晚21:00行情。Top合约与Night exact contract一致；无分钟路径，晨间条件是否实际成交仍记unknown。Night curve未用缺失或不一致合约对强拼，只采用可验证EOD产品曲线。

## 三、商品仪表盘

“Night”依次为close / vs前收 / vs前结算；“Day”是9月8日EOD close相对同合约Night close。量仓均为当日EOD；Night质量均fresh，时间为9月7日23:00，SC/AU/AG为9月8日02:30。

| 板块 | 合约 | EOD close/settle | 1D/5D | Vol/OI/ΔOI | EOD curve | Basis/Physical | Night；Day | 15:00后海外 | Options S/P/E | 21:00信号 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 燃料油 | **FU2611** | 3988/3893 | +2.47%/+2.21% | 691k/217k/+14.4k | FU2610/11 +4.37% back | C级context | 3877；-0.08%/+2.05%；**+2.86%** | 柴油紧、外油续升 | Y/N/N | 回撤确认多 |
| 甲醇 | **MA610** | 3359/3279 | +3.50%/+7.72% | 2.96m/727k/+106k | MA609/610 +0.91% back | C级context | 3245；+1.03%/+2.43%；**+3.51%** | 油价支持、已补涨 | Y/Y/N | 不追，等30m |
| PTA | **TA701** | 6210/6050 | +2.16%/+2.47% | 1.17m/1.13m/+53.3k | 近端+3.36% back | C级context | 5940；+0.27%/+0.30%；**+4.55%** | 原油强，日盘先交易 | Y/Y/N | 等45m |
| 原油 | **SC2610** | 720.6/703.3 | +2.15%/+10.37% | 136k/38.8k/-216 | SC2610/11 +5.76% back | Physical unavailable | 700.4；+0.16%/+1.73%；**+2.88%** | Brent 99.46/WTI 94.73 | Y/N/N | 首跳不追 |
| PX | **PX611** | 9152/8866 | +2.28%/+3.29% | 361k/177k/+19.0k | -3.67% contango | C级context | 8708；-0.09%/+0.46%；**+5.10%** | 油强，但curve反对 | Y/N/N | 高开不追 |
| LPG | **PG2610** | 6857/6677 | +1.95%/+8.15% | 206k/106k/+871 | +3.42% back | C级context | 6702；+1.75%/+2.34%；+2.31% | 能源同向 | Y/N/N | 已到晨报TP1区 |
| 天胶 | **RU2701** | 19635/19465 | +1.86%/+2.66% | 397k/172k/+7.7k | +0.05%，近乎平 | Physical不足 | 19390；+1.09%/+1.47%；+1.26% | 无同日海外确认 | Y/Y/N | 等45m |
| 锌 | **ZN2610** | 27505/27430 | +1.61%/+1.67% | 174k/160k/+3.5k | +0.22% back，z=2.38 | 无完整实体层 | 27340；+0.90%/+1.28%；+0.60% | LME锌约4001 | Y/N/N | 回撤观察 |
| 纯碱 | SA701 | 1083/1071 | -1.83%/+0.94% | 1.70m/1.28m/+28.6k | -4.36% contango | C级；仓单变化 | 1064；-1.39%/-2.47%；**+1.79%** | 无直接锚 | Y/Y/N | 夜跌日修复 |
| 玻璃 | FG701 | 977/967 | -1.12%/+1.47% | 1.20m/1.22m/+35.5k | -4.75% contango | C级 | 964；-1.23%/-1.43%；+1.35% | 无直接锚 | Y/Y/N | 晨间空头降级 |
| PVC | V2701 | 5113/5036 | -0.42%/+3.51% | 1.57m/1.12m/+24.0k | -0.45% contango | Physical不足 | 5011；-0.79%/-0.91%；+2.04% | 无exact映射 | Y/Y/N | failed-squeeze空失效 |
| 大豆一号 | A2611 | 5146/5103 | +1.94%/+2.63% | 437k/383k/+30.1k | -0.27% contango | 实体变化不足 | 5082；+1.21%/+1.52%；+1.26% | CBOT仅context | Y/N/N | WASDE前观察 |
| 黄金 | AU2610 | 953.12/955.90 | +0.14%/-0.53% | 175k/151k/-3.5k | -0.53% contango | 不适用 | 954.1；+0.35%/-0.04%；-0.10% | 现货金约4400、近持平 | Y/Y/N | 无方向优势 |
| 碳酸锂 | LC2701 | 143480/142980 | +0.99%/-10.62% | 121k/399k/+3.6k | +0.35% back | 仓单沿用9/1 | 无夜盘 | 无可靠外盘锚 | Y/N/N | 反弹非反转 |
| 鸡蛋 | JD2611 | 3806/3823 | +0.84%/+3.80% | 313k/260k/+9.9k | +7.48% back | 实体变化不足 | 无夜盘 | 无直接锚 | Y/N/N | 次日日盘观察 |

[Engine External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)于19:14记录WTI 93.81、Brent 98.65、LME铜14686、LME锌4001、BMD棕榈油4976；之后Reuters约在截点附近报Brent **99.46**、WTI **94.73**，说明15:00后的海外油价仍是正增量，但它尚未被今晚中国期货交易。[Reuters油市，2026-09-08](https://www.reuters.com/business/energy/oil-rises-risks-prolonged-mideast-conflict-heighten-supply-worries-2026-09-08/)

美元跌至两周低位附近、美国10年期收益率约4.796%，USD/CNH约6.7098且日内窄幅；人民币没有额外放大进口成本。现货黄金约4399.99美元/盎司、日内-0.1%，地缘升级仍未带来明显避险弹性。[Reuters黄金](https://www.reuters.com/world/india/gold-gains-dollar-eases-with-us-inflation-data-radar-2026-09-08/)｜[USD/CNH代理](https://www.investing.com/currencies/usd-cnh)

## 四、相比上一期真正变化

1. **能化从“SC单点”扩散到炼化与化工日盘。** FU、LU、BU、MA、TA、PX均上涨增仓。FU早前Night相对前收几乎没涨，日盘却+2.86%；TA Night仅+0.27%，日盘+4.55%；PX Night -0.09%，日盘+5.10%。这不是Night重复，而是中国日间对油价、成本和仓位重新定价。

2. **SC继续上涨，但边际结构没有同步增强。** EOD收720.6、back仍陡，然而OI小降、curve由前一日约6.17%收窄至5.76%。15:00后外油再涨只支持今晚gap，不支持无条件追第一跳。

3. **昨日“多SC/空FU”相对价值观点失效。** 原失效条件是FU站稳3920；今天FU高3995、收3988且增仓、back仍强。若此前确已建立，应在下一流动窗口退出组合，不能把对方向的偏好转成对失效价差的执念。

4. **晨间MA与PG条件多达到首个兑现区。** MA高/收3359，超过TP1 3310；PG高6866、收6857，超过TP1 6820。没有分钟路径，是否触发仍unknown；若此前确已按条件建立，应减仓并上移保护，不再按原始低位赔率加仓。

5. **FG/SA/V的夜盘空头线索被日盘明显修复。** FG从964回到977，SA从1064回到1083，V从5011回到5113。contango仍反对供需牛市，但价格没有给空头follow-through；晨间FG/V建议退回观察或按原止损退出。

6. **期权产品覆盖继续修复，但执行质量没有改善。** 产品由61/64覆盖，MA、TA等恢复当日surface；bid/ask仍为0，因此任何“期权更便宜”的结论都不能落到成交。

## 五、产业链地图

**1. 原油—燃料—炼化：最强，偏多但不追，置信度中高。**  
支持：SC/FU/LU/BU价格扩张，FU/LU/BU与SC结构均偏back，外油15:00后续涨；Reuters同时指出全球柴油因炼能、俄出口限制和季节需求而紧张。反对：SC OI下降、back收窄；替代运输、非OPEC供给与库存缓冲令Brent尚未稳定站上100。[Reuters竞争解释](https://www.reuters.com/business/energy/why-isnt-oil-above-100-despite-supply-disruptions-2026-09-08/) 最大缺失：SC/LU实体层、SHFE仓单及exact parity。

**2. MA—PX—TA—EG：日间最强补涨，置信度中。**  
MA量价仓最完整；TA/PX day follow-through极强。反证是PX深contango，MA back明显压缩，实体与加工利润口径不够完整。市场可能把成本冲击当成供需短缺；因此表达应优先选择回撤后的单腿，不发布伪加工套利。

**3. RU—NR—BR：上涨但全球确认不足，置信度中低。**  
RU/NR日盘续涨，RU curve由contango修到近乎平；BR却价涨仓减，海外天然胶没有同日可靠确认。最强竞争解释仍是国内仓位与板块beta，不是全球橡胶短缺。

**4. ZN—CU有色：锌最强，置信度中。**  
ZN价格/OI、轻back与LME锌约4001同向；LME锌此前已出现现货紧张和冶炼加工费压力。[Reuters锌市场，2026-09-02](https://www.reuters.com/commentary/reuters-open-interest/lme-zinc-squeeze-signals-deepening-supply-risks-west-2026-09-02/) 但无exact进口利润和完整库存映射，不能称跨市场套利。

**5. 建材/新能源/农产品：最弱或最缺edge。**  
FG/SA/V夜跌日修复，SF/SM减仓波动，方向噪音高；LC只是5日大跌后的单日反弹；A/P/OI有价格或持仓异常，但WASDE与Crop Progress前实体证据不足。未入榜黑色、软商品和EC未见三层共振。

## 六、机会排行榜

| 排名 | idea_id / 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | **COM-E-FU2611-PRODUCT-TIGHT-20260908｜FU2611回撤多** | 22/18/17/12/9 | **78** | 1、2、4 | 存在待验证优势｜部分｜等30m |
| 2 | **COM-M-MA610-SETTLE-RECLAIM-20260908｜MA610延续多** | 22/17/16/13/9 | **77** | 1、2、4 | 存在待验证优势｜部分｜已扩张，等回撤 |
| 3 | **COM-E-TA701-DAY-REPRICE-20260908｜TA701日间重定价多** | 21/17/15/13/10 | **76** | 1、2、4 | 存在待验证优势｜部分｜等45m |
| 4 | **COM-E-SC2610-GAP-20260905｜SC2610回撤接受多** | 21/15/18/12/9 | **75** | 1、2、4 | 存在优势但赔率下降｜部分｜首跳不追 |
| 5 | **COM-E-ZN2610-LME-SQUEEZE-20260908｜ZN2610回撤多** | 20/17/14/12/9 | **72** | 1、2、4 | 存在待验证优势｜部分｜等30m |

分数仅是研究排序，不是胜率或仓位。五项均未获完整Physical层，期权也没有执行报价；FU/MA/TA/SC属于高度相关的油价—通胀因子，总风险必须合并，不能按四笔独立机会叠加。

## 七、前三名交易卡

### 1. FU2611｜回撤确认多｜78

**事实：** 9月7日前收/前结算3880/3799；早前Night 3888/3905/3850/**3877**，-0.08% vs close、+2.05% vs settlement，ΔOI +1,652；9月8日EOD 3988/3893，day follow-through +2.86%，ΔOI +14,448，FU2610/11 back约4.37%。  
**市场定价：** Night相对前收没有新增强势，真正重定价发生在中国日盘；19:30外油与柴油紧张继续支持，但3995附近已吸收不少信息。  
**推断：** refined-product tightness可能比SC outright更耐久；竞争解释是FU只是滞后补涨，若外油回落会更快失去beta。  
**主观判断：** 今晚最值得等回撤，不值得追首跳。

- 最佳表达：FU2611期货；期权IV高且无bid/ask。
- 好成交：21:00后等30分钟，3930—3960承接，重上3990/VWAP后1/3多。
- 中成交：突破4005并成功回踩，仓位为好成交的一半。
- 坏成交：直接高于4050或止损距离超过计划1R，放弃。
- 初始止损：30分钟接受3890下方；逻辑失效：跌破3850且Brent回到97以下、FU back明显收窄。
- TP1 4100或1.5R；TP2 4250或3R；两日无扩张退出。
- 风险：0.25%—0.45% NAV；与SC/LU/BU/PG/MA/TA合并。期货最大损失不由结构限定。
- 参数：10吨/手，tick 1元/吨，tick value 10元；按3988名义39,880元/手；最后交易日2026-10-30，实物交割，10月中旬前主动roll。动态margin/limit未确认；一板压力=39,880×L，两板长仓下跌压力=39,880×[1-(1-L)^2]。
- Night session：今晚21:00—23:00。最坏情景是中东消息突然缓和、外油跳水、流动性消失，计划止损穿透。

### 2. MA610｜延续多，但先兑现｜77

**事实：** 前收/前结算3212/3168；早前Night 3217/3246/3189/**3245**，+1.03%/+2.43%，ΔOI +46,551；EOD 3359/3279，day follow-through +3.51%，EOD ΔOI +106,367，curve仍back但压缩至0.91%。  
**市场定价：** 晨间“站回settlement”已变成日盘趋势扩张；close位于日高，赔率已从启动变为延续。  
**推断：** 若今晚回撤仍能守住日盘价值区，说明不只是低位修复；最强反证是curve压缩和高IV显示事件溢价已贵。  
**主观判断：** 若此前按晨报建立，应先减仓；新仓只等深一点回撤。

- 好成交：3300—3330承接，30分钟重上3360/VWAP，1/3多。
- 中成交：3375上方突破回踩，仓位减半。
- 坏成交：高于3420无回撤，放弃。
- 初始止损：接受3275下方；逻辑失效：跌破3245且back消失、油价同步回落。
- TP1 3450，TP2 3600；1—3D时间止损。
- 若此前确已按晨间条件建立：3310的TP1已触及，至少减1/3—1/2，并把保护位抬到3300附近；没有成交反馈，不假设真实持仓。
- 风险：新试仓0.25%—0.40% NAV。最大损失不受结构限定。
- 参数：10吨/手、tick 1、tick value 10元，名义33,590元；repo当日margin 11%、limit 9%；一板长仓压力约3,023元，两板复合约5,774元。最后交易日2026-10-21、最后交割日10月26日，实物交割；今晚21:00—23:00，10月中旬前roll。

### 3. TA701｜日间重定价多｜76

**事实：** 前收/前结算5924/5922；早前Night 5940/5970/5908/**5940**，+0.27%/+0.30%，ΔOI仅+137；EOD 6210/6050，day follow-through **+4.55%**，ΔOI +53,285。产品近端curve约+3.36% back，但曲线合约对并非TA701本身，证据降级为板块结构。  
**市场定价：** 绝大部分涨幅发生在中国日盘，说明本地成本/仓位重定价强；同时也意味着今晚追高的剩余赔率更差。  
**推断：** 若回撤后仍守日盘中枢，趋势可能延续；竞争解释是油价冲击造成的短期成本传导，缺库存/加工利润确认。  
**主观判断：** 等45分钟，绝不追首跳。

- 好成交：6120—6170承接，重上6210/VWAP后1/3多。
- 中成交：6240突破回踩，仓位减半。
- 坏成交：直接高于6300，放弃。
- 初始止损：接受6050下方；逻辑失效：跌破5990、近端back明显收窄且PX/EG同步转弱。
- TP1 6400，TP2 6600；1—3D时间止损。
- 风险0.25%—0.40% NAV，与MA/PX/EG/SC合并。期货最大损失不受结构限定。
- 参数：5吨/手、tick 2元/吨、tick value 10元，名义31,050元；margin 7%、limit 6%；一板压力约1,863元，两板复合约3,614元。最后交易日2027-01-14、最后交割日1月19日，实物交割；今晚21:00—23:00，12月中下旬前评估roll。

## 八、商品期权专项

本期是**9月8日当日EOD surface**，不是实时可成交报价：

| Underlying / expiry | ATM | ATM IV | RV20 | IV-RV | RR25 / BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---:|---:|---|---|
| FU2611 / 2026-10-19 | 3900 | 56.42% | 39.23% | +17.18vol | +1.66/+0.16 | Y/N/N | 事件溢价高 |
| MA610 / 2026-09-11 | 3300 | 49.79% | 31.07% | +18.72vol | **+9.01**/-0.13 | Y/Y/N | call skew很贵、临近到期 |
| TA701 / 2026-12-11 | 6000 | 30.33% | 26.38% | +3.95vol | +2.74/+0.98 | Y/Y/N | 研究可用 |
| SC2610 / 2026-09-11 | 700 | 53.72% | 35.45% | +18.27vol | +4.56/+2.91 | Y/N/N | event convexity已贵 |
| ZN2610 / 2026-09-23 | 27500 | 21.58% | 14.39% | +7.19vol | +1.81/+1.33 | Y/N/N | 仍缺执行报价 |
| V2701 / 2026-12-16 | 5000 | 22.73% | 25.46% | -2.74vol | +2.90/+1.63 | Y/Y/N | 长波动线索，非可成交便宜 |

缺bid/ask时，不能输出净权利金、滑点、当前Greeks或认定bull call spread比期货划算。MA与SC短到期凸性已经明显计价，今晚更不适合盲目买call。Dealer Gamma方向未知，禁止Gamma squeeze/pin推断。PL/PR/ZC当日链缺失，只列数据不足。

## 九、21:00夜盘开盘风险地图

时间边界：
1. 9月8日中国EOD已完成。  
2. trading_date=9月8日的Night是今天早前已完成价格发现。  
3. 15:00—19:30海外新增是外油续涨、金价近持平、美元偏弱/收益率高位。  
4. 今晚21:00夜盘尚未发生，归属9月9日交易日。

| 品种 | 可能开盘 | 海内外/已预交易 | 首跳 | 等待 | 最重要确认 |
|---|---|---|---|---|---|
| FU/LU/BU | 小高/宽幅 | 日盘已补涨，海外继续正向 | 不追 | 30—45m | FU 3890/3990/4005、产品强于SC |
| SC | 高开尾部仍在 | 720.6已预交易大部分，15点后仍有增量 | **不追** | 30m | 703/709/723、Brent 99—100、back |
| MA | 高开/宽幅 | 日盘重定价充分 | 不追 | 30m | 3300—3330承接、curve |
| TA/PX/EG | 高开/分化 | day follow-through远大于Night | 不追 | 45m | TA 6050/6210；PX contango；EG breadth |
| PG | 小高 | 晨间多头已到TP1区 | 不追 | 30—45m | 6700、6866、油气联动 |
| RU/NR/BR | 平/偏高 | 国内强，海外胶未确认 | 不追 | 45m | RU 19390/19650、curve、三胶breadth |
| ZN/CU | 小高 | LME同向但非parity | 不追 | 30m | ZN 27340/27715、LME锌4000 |
| AU/AG | 平开 | Night反弹后日盘钝化，海外金近持平 | 不追 | 15—30m | AU 950/956.6/961、10Y收益率 |
| SA/FG/V | 平开/震荡 | 无海外锚，夜跌被日盘修复 | 不追 | 30—45m | FG 964/980；V 5011/5128；contango |
| SF/SM/JD/LC/SI/PS | 无夜盘 | 不适用 | 不适用 | 9月9日09:00 | 量仓、curve及实体更新 |

## 十、未来24小时/7日事件日历

- **9月9日04:00 BJT：USDA Crop Progress。** 报告尚未在本截点发布；A/M/Y/P/OI/C减Delta，不提前猜天气影响。[USDA官方日程](https://www.usda.gov/about-usda/reports-and-data/agency-reports)
- **9月9日09:30 BJT：中国8月CPI/PPI常规窗口。** 黑色、化工、有色在日盘前降低同因子风险；精确时点以[国家统计局日程](https://www.stats.gov.cn/sj/fbrc/)为准。
- **9月10日09:00：热卷、不锈钢、低硫燃料油期权挂牌。** 首日只观察chain、surface与bid/ask，不拿历史IV硬比。[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html)｜[INE](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)
- **9月10日20:30：美国8月PPI。** AU/AG、油价与美元因子仓提前降Delta；无报价时不预埋Vega。[BLS](https://www.bls.gov/schedule/news_release/ppi.htm)
- **9月11日00:00：EIA假期顺延周报。** 原油、燃料与裂解价差优先使用有限风险或减仓等待。[EIA](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **9月11日20:30：美国8月CPI。** 贵金属和工业金属面临Delta/Vega重置。[BLS](https://www.bls.gov/schedule/news_release/cpi.htm)
- **9月12日00:00：USDA 9月WASDE。** M/Y/P/OI/C/CF避免无保护方向重仓。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- 持续监控Hormuz、沙特设施、油轮通行与美伊行动。新闻只改变分布，不自动提供入场；任何油价主题都需压力测试消息反转、连续涨跌停和中国休市期间外盘跳变。

## 十一、覆盖核对、台账与归档

**覆盖核对：** 强制63个代码全部取得9月8日有效主力并完成1D/3D/5D/20D、量仓、curve、产业链和策略类别扫描；另扫描JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR等动态品种。有效分析71个左右；JR/PM/RI/WH/ZC等因零价、零量、零OI或制度性不活跃列为不适用。期权应覆盖64个产品，实际61个；PL/PR/ZC数据不足。方向、跨期、基差、跨品种/跨市场、风格/中性、波动率、偏度、事件凸性与1D—20D周期均已扫描；因无A/B级exact basis、exact parity或完整beta权重，本期不发布伪套利或伪beta-neutral篮子。

**未入榜板块：** 黑色建材最显著是FG/SA夜跌日修复而非新方向；新能源仅LC反弹但5D仍-10.6%；农产品A增仓上涨但curve为contango、P隔夜涨幅日间回吐；软商品与EC没有价格、结构、海外三层共振。IC不属于本商品版63代码，且无可验证商品期权代理映射，本期标不适用，不拿股指代理冒充商品工具。

**旧建议台账：**
- COM-M-PG2610-OIL-BREADTH-20260908：76→70，晨间TP1区域已到；原因=价格变化。触发路径unknown；若已建立，减仓并上移保护，未建立则不追。
- COM-M-MA610-SETTLE-RECLAIM-20260908：73→77，逻辑获日盘量价仓确认；但赔率恶化。若已建立，TP1后减仓；新仓等待回撤。
- COM-M-FG701-FAILED-SQUEEZE-20260908：69→58并退出正式榜；原因=日盘修复。若已建立，按980止损，不加仓。
- COM-E-V2701-SQUEEZE-20260904：研究观点失效；原因=价格重新接受5011/5036上方。若已建立，下一流动窗口减仓/退出，30分钟接受5128以上为完全失效。
- COM-E-SC2610-GAP-20260905：75，若昨日回撤多已建立，723已越过原TP1 715，应减仓并把保护抬至703—709；不假设真实持仓。
- COM-E-SC-FU-RV-20260907：失效并退出；FU站稳3920且收3988，原相对价值反证成立。

风险预算：新试仓0.25%—0.45% NAV；三层确认后上限仍不超过0.75%—1.0%，因为当前价格已延伸。所有油价、炼化、MA/TA/PX/PG敞口合并；单主题不触碰2.5%—3.0%上限。压力测试包括一/两板、gap、保证金上调、止损穿透、相关性破裂、IV跳升/塌陷、交割挤压、人民币急变及中国休市期间海外大波动。

固定六路径已从main回读后方可认定归档成功；CI不轮询，状态保持pending_or_unverified。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：FU2611在30分钟守住3930—3960并重上3990后多；MA610回撤3300—3330承接后多；TA701等待45分钟守6120—6170后多。  
C. 今晚应继续观察的机会：SC2610对723的接受、ZN2610与LME锌共振、RU2701曲线转平、PG2610晨报TP1后的余仓管理，以及A/P/OI在USDA前的量仓变化。  
D. 今晚必须避免或退出的交易：追SC/FU/MA/TA/PX首跳；若此前建立则退出已失效的多SC/空FU与V空头；FG空头不加仓；execution_ready=false时臆测期权成本；把C级basis或连续合约映射称套利。