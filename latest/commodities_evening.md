# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-03

> revision: 2  
> generated_at_bjt: 2026-09-03T21:32:49+08:00  
> data_protocol_version: china_commodities_v2  
> 正式决策切点仍冻结在北京时间19:30：本次只用9月3日中国日盘EOD、今天凌晨已完成Night Session，以及15:00–19:30海外增量；不把19:30后的海外行情倒灌进正式评分。

## 一、今晚一句话结论

**今晚值得冒险，但只值得做条件交易，不值得追价。** 9月3日T日EOD补齐后，AU2610的“隔夜修复→日盘继续确认”最干净；SC多周期趋势仍强但日盘对凌晨夜盘明显回吐且OI下降，贵金属优于追油。

## 二、数据质量与覆盖

China-Commodities-Engine统一输入已升级为 `requested_date=2026-09-03`，generated_at=`2026-09-03T21:10:10+08:00`。核心Futures为9月3日五所SHFE/INE/DCE/CZCE/GFEX共802合约，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0；5条OHLC placeholder排除。`official_complete=false`主要来自合约元数据/部分辅助官方源，DCE contract-info仍失败，因此动态保证金、限幅等下单前必须复核。

Market State为T日同合约历史，1D/3D/5D/20D、RV20、Volume/OI z-score、ΔOI和near-next curve均可使用。Night Session的`trading_date=2026-09-03`仍指今天凌晨已完成的连续交易阶段，不是今晚21:00后的未来行情，因此可以计算“Night close→T日EOD”的day follow-through。

Physical为9月3日fresh；多数100ppi spot/basis为C级，因地区/品质/税口径/交割地不完整，只作context，不计高质量basis。仓单为独立交易所数据：例如SF仓单6025、日增1406，RM仓单6806、日增800，SA仓单6263、日减191；仓单变化属于结构/库存证据，不等同社会库存。

Options为9月3日完整64/64品种、24,200合约、402 series；IV coverage约98.18%，全链验证通过，`surface_ready=true`。但全市场OI coverage约67.43%，`positioning_ready=false`（逐series可单独ready），bid/ask coverage=0，因此`execution_ready=false`。可以使用ready series的ATM IV/RR25/BF25，但禁止臆测权利金、bid/ask、滑点和可成交净成本；dealer gamma方向未知。

## 三、商品仪表盘

| 板块 | 合约 | 9/3 EOD close/settle | 结构/量仓 | 凌晨Night→日盘 | Options | 19:30风险信号 |
|---|---|---:|---|---|---|---|
| 贵金属 | AU2610 | 958.38 / 952.06 | 1D settle +1.25%；curve +0.41%，z 1.88；价涨仓减 | Night 948.32 → EOD 958.38，day +1.06% | ATM IV 24.70，RR25 +3.21，BF25 +1.66；surface+positioning ready，execution false | 最干净条件多；15–30m确认 |
| 贵金属 | AG2610 | 16045 / 15960 | 1D settle +1.53%；curve +0.11%，z 1.38；价涨仓减 | Night 15886 → EOD 16045，day +1.00% | ATM IV 42.72，RR25 +4.87，BF25 +2.55；execution false | 条件多，假突破风险高于AU |
| 原油 | SC2610 | 681.7 / 690.9 | 5D +20.43%；ΔOI -2368/-6.01%；Back +6.67% | Night 694.7 → EOD 681.7，day -1.87% | ATM IV 60.86 vs RV20 35.82；RR25 +3.72；execution false | 外盘强但内盘日间消化；必须重夺 |
| 硅铁 | SF611 | 6364 / 6248 | V z 2.97；ΔOI +2.16万；Back +3.82%，z1.81 | 无可靠exact Night分解用于本卡 | ATM IV 23.19 vs RV20 9.75；positioning ready，execution false | 趋势强但仓单+1406；不追 |
| PTA | TA701 | 5942 / 6012 | 5D +8.76%；ΔOI +4.64万；Back +3.32%，z2.62 | 不作exact Night分解 | T日surface可用，execution false | 价跌仓增，先重夺6010附近 |
| 甲醇 | MA610 | 3158 / 3188 | 5D +13.98%；V z2.01；ΔOI -1.23万；Back +3.73%，z1.90 | Night 3250 → EOD3158，day -2.83% | surface ready，execution false | 多日趋势强但日盘完整回吐；观察reclaim |
| 燃料油 | FU2611 | 3813 / 3864 | 1D -2.69%；ΔOI -1.22万；Back +8.36% | Night3929 → EOD3813，day -2.95% | ATM IV45.10；RR25+8.01；BF25+13.76；execution false | 与海外油强势背离，优先观察failed-gap/RV |
| 碳酸锂 | LC2701 | 149880 / 153300 | close -3.71%；OI 39.4万；curve仍back | 无夜盘结论写入本卡 | surface可用，execution false | 弱势，暂不接刀 |
| 纯碱 | SA701 | 1056 / 1061 | close -1.03%；OI119.7万；contango；仓单-191 | 不作exact Night分解 | surface ready，execution false | 结构偏弱，观察而非交易 |

## 四、相比revision 1真正变化

1. **数据否决被解除。** revision 1因统一输入停在9月2日，所有机会被压在69分以下；现在9月3日五所EOD、Market State、Physical与Options均已落库，因此可以重新恢复70+条件交易。
2. **贵金属从“疑似reversal”升级为日盘确认。** AU凌晨Night收948.32，T日收958.38，日盘继续+1.06%；AG对应+1.00%。这不是只靠海外映射，而是中国价格自己给出了follow-through。
3. **原油反而没有想象中干净。** SC多周期趋势和backwardation很强，但凌晨Night 694.7之后日盘收681.7，回吐约1.87%，同时OI下降6.0%；这更像高位换手/减仓线索，而不是新增长仓确认。
4. **能化内部出现明显分裂。** FU从Night3929继续跌到EOD3813（约-2.95%），MA从3250回到3158（约-2.83%）；因此19:30海外油价走强只能作为未来gap催化，不能覆盖中国日盘已经出现的弱弹性。
5. **期权研究层大幅改善，但仍不可直接执行。** 64/64品种、surface ready；AU/SC/AG/SF等可读ATM IV与skew。但bid/ask覆盖仍为0，所以本报告不报任何具体权利金和净成本。

## 五、产业链地图

**贵金属：今晚最强的“价格路径确认”。** AU/AG都完成“凌晨反弹→日盘继续抬升”，且19:30前美元/美债收益率回落仍提供外部支撑。最大风险是美国数据重新推高收益率。AU优于AG，因为AG工业beta更高、IV更贵、假突破概率更大。

**原油—炼化：趋势仍强，但边际价格弹性下降。** SC 5D涨幅仍超过20%，curve深back；然而T日价格相对Night回落、OI减少，说明追涨赔率明显下降。FU更弱，形成“油价强—内盘燃料油弱”的相对价值线索。优先等SC重夺，不做首跳。

**黑色/合金：SF611是非能源独立候选。** 量、价、OI和curve同时偏强，且不依赖19:30海外油价；但仓单单日增加1406，是对多头最重要的反证。只有价格继续吸收仓单增加，才值得试仓。

**聚酯/甲醇：中期结构强、T日弹性弱。** TA curve z约2.62、MA curve z约1.90，但两者日盘表现均没有把凌晨/中期强势完全延续。更适合reclaim而不是顺势追价。

## 六、机会排行榜

1. **AU2610 开盘确认多｜82分｜确认交易但需触发**  
   fresh层=1/2/4/5。夜盘→日盘follow-through、curve与19:30前海外金价同向；价涨仓减使其仍必须等开盘确认。评分：逻辑22 / 赔率凸性18 / 催化17 / price-curve-vol14 / 持仓技术11。
2. **SC2610 回踩后重夺确认多｜79分｜条件试仓**  
   fresh层=1/2/4/5。多周期趋势+backwardation+海外油价支持，但day follow-through -1.87%、ΔOI -6.0%是核心扣分。评分：22 / 16 / 19 / 13 / 9。
3. **AG2610 开盘确认多｜76分｜条件试仓**  
   fresh层=1/2/4/5。与AU相同的价格路径确认，但工业beta和更高IV降低赔率。评分：20 / 17 / 16 / 12 / 11。
4. **SF611 回撤确认多｜75分｜条件试仓**  
   fresh层=1/2/5。价涨仓增、volume z≈2.97、curve z≈1.81；仓单+1406是明确反证，不能追6412高点。评分：21 / 14 / 11 / 15 / 14。
5. **TA701 重夺确认多｜72分｜条件试仓**  
   fresh层=1/2/4/5。中期趋势和curve强，但T日价跌仓增，必须先重夺6010附近并观察链内扩散。评分：19 / 14 / 14 / 14 / 11。

## 七、前三名交易卡

### 1）AU2610｜条件多｜82
- **事实**：T日close/settle=958.38/952.06；凌晨Night close=948.32；day follow-through=+1.06%。AU2610 9/23期权ATM IV=24.70%，RR25=+3.21，BF25=+1.66，surface/positioning ready、execution false。
- **入场**：今晚21:00后等15–30分钟；若开盘区间能守住约952结算锚，国际金仍强且美元/收益率没有急反转，再突破15/30m high开1/3。若相对952高开>约1.5%，必须先回撤再reclaim，禁止首跳追。
- **止损/失效**：opening-range low；或跌回948附近且国际金同步转弱、收益率急升。TP1=1.5R，TP2=3R；时间止损同一夜盘至1–3D；试仓最大损失0.35%–0.50% NAV。
- **合约**：上期所黄金1000克/手，tick 0.02元/克，tick value 20元/手；按952.06结算名义约95.21万元/手。最后交易日规则为交割月15日（节假日可调整）；黄金连续交易通常21:00–02:30。当前动态保证金/涨跌停参数**下单前复核**。
- **期权表达**：只把Bull Call Spread作为研究备选；`research only; manual quote and manual confirmation required before execution; no premium quoted`。

### 2）SC2610｜条件多｜79
- **事实**：T日close/settle=681.7/690.9；5D settle +20.43%；凌晨Night close=694.7，day follow-through=-1.87%；ΔOI=-2368/-6.01%；SC2610-SC2611 back约6.67%。SC2610 9/11 ATM IV=60.86%，显著高于RV20 35.82%，RR25=+3.72，execution false。
- **入场**：等30分钟。只有价格先重夺690.9，再对694.7夜盘锚形成接受，同时19:30外盘油价的供应风险逻辑未逆转，才开1/3；若首跳超过约701且无回撤，不追。
- **止损/失效**：opening-range low；硬失效参考T日日内低点671.1，同时海外油价快速回吐/地缘明显降级。TP1=1.5R，TP2=3R；1夜盘–3D；试仓最大损失0.35%–0.50% NAV。
- **合约**：INE原油1000桶/手，tick 0.1元/桶，tick value 100元/手；按690.9结算名义69.09万元/手。标准合约最低保证金5%、基准限幅±4%，但当前临时/券商参数**下单前复核**；连续交易21:00–02:30；实物交割。
- **期权表达**：IV过贵，优先期货；Call Spread仅研究，不报权利金。`research only; manual quote and manual confirmation required before execution; no premium quoted`。

### 3）AG2610｜条件多｜76
- **事实**：T日close/settle=16045/15960；凌晨Night close=15886，day follow-through=+1.00%；1D settle +1.53%，curve轻微近强。AG2610 9/23 ATM IV=42.72%，RR25=+4.87，BF25=+2.55，surface ready、positioning/execution false。
- **入场**：等15–30分钟；15960–16000区域不失守且海外gold/silver仍同向，再突破opening-range high试1/3。若高开至约16200以上但无回撤确认，不追。
- **止损/失效**：跌破15886/开盘区间低点，或美元与真实利率反向急升。TP1=1.5R、TP2=3R；同夜–2D；最大损失0.25%–0.40% NAV。
- **合约**：上期所白银15千克/手，tick 1元/千克，tick value 15元/手；按15960结算名义约23.94万元/手。最后交易日规则为交割月15日；黄金/白银连续交易21:00–02:30。当前动态保证金/限幅**下单前复核**。
- **期权表达**：IV偏贵，优先期货；有限风险Call Spread仅研究。`research only; manual quote and manual confirmation required before execution; no premium quoted`。

## 八、商品期权专项

T日期权链已从revision 1的T-1/not-ready升级为64/64全品种与surface-ready。代表性series：AU2610 IV24.70/RR+3.21；SC2610 IV60.86/RR+3.72；AG2610 IV42.72/RR+4.87；SF611 IV23.19/RR+2.59。SC的IV-RV溢价约25 vol points、SF约13 vol points，裸买Gamma的赔率明显受限。全市场execution仍false，dealer gamma方向未知，因此任何结构都必须先手工核报价。

## 九、21:00夜盘风险地图

- **AU/AG**：正式19:30地图偏高开/偏强，但不追首跳；等15–30m，确认美元、收益率和opening range。
- **SC**：外盘供应风险偏多，但中国T日日盘已经相对Night回吐；最关键是能否重夺690.9/694.7。等30m。
- **FU**：国内显著弱于SC和海外油价；若高开后仍不能重夺3864/3929，优先观察failed-gap或SC-FU相对价值，而不是机械追多FU。
- **MA/TA**：等30–45m；必须看到链内EG/PF/PX等同步扩散才做reclaim。
- **SF**：连续交易安排/动态参数未在本次官方核验中完整确认；若无夜盘则下一决策窗口为次日9:00，参数未确认前不下单。

## 十、未来24h / 7d事件

- **9月3日22:00北京**：美国ISM Services；贵金属和美元/利率敏感仓位在数据前不加满Delta。
- **9月4日20:30北京**：美国8月Employment Situation/NFP；AU/AG与油价都需预留隔夜gap预算。
- **9月5日约03:30北京**：CFTC COT常规发布时间；仅作为拥挤度背景，不把会员/持仓结构机械解释成机构方向。
- **未来7日**：持续跟踪美伊冲突、霍尔木兹运输与OPEC+相关正式公告；未独立确认的会议具体时点不作为硬入场锚。

## 十一、最终四行

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：AU2610开盘确认多、SC2610回踩/重夺确认多、AG2610开盘确认多、TA701重夺确认多；SF611仅在确认交易窗口和参数后做回撤多。  
C. 今晚应继续观察的机会：MA610日盘反转后的reclaim、FU2611“海外油强/内盘弱”的failed-gap与SC-FU相对价值、RM611/SF611仓单增加后价格能否继续吸收。  
D. 今晚必须避免或退出的交易：21:00首跳追多SC/贵金属、把价涨仓减写成新增多头、在execution_ready=false时臆测期权成本、把C级spot/basis当可执行套利、忽略FU日盘弱弹性而机械追油价映射。