# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-19

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-19 19:46 BJT；信息截点：19:30。今天是周六，中国商品市场休市；最近完整中国EOD为9月18日，下一实际中国交易窗口为9月21日09:00。今晚没有21:00中国夜盘。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；原油溢价继续回吐、金银保持韧性，但周末无中国价格发现且周五夜盘日期异常，全部候选只等周一重报价。**

当前regime：**原油极端短缺溢价消退与成品油/运输尾部并存；贵金属在接近5%的美债收益率下仍有韧性；中国内需与聚酯链偏弱，周末处于价格发现真空。**

最接近补证的三项是：LU2611相对SC2611、SC2611反弹失败空、AG2612回撤接受多。缺口分别是合法归属的exact-contract周五夜盘、周一实时curve/盘口、以及可比期权报价。周五晚间旧条件窗口已经过去，不得平移为周一委托。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、9月18日Night历史快照及[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，`requested_date=2026-09-18`，9月19日19:08:21生成。周末没有新EOD，应以周五last-good判断，而不是机械要求9月19日行情。
- Futures：9月18日五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；4条placeholder排除。
- 周六刷新：根状态尝试以9月19日取数，五所均返回0条并产生15个critical errors；这是非交易日刷新失败，**不使9月18日已验证last-good失效**，但也不提供任何周六新增中国价格证据。
- Market State：77产品完成同合约1D/3D/5D/20D初筛；70个具备可用趋势/量仓/curve，主力切换和短历史产品不强算z-score。
- Physical：目标20项中18项序列在自身频率下可用，SC/LU unavailable；模块本次发布状态为failed/unpublished。所有basis为C级或缺失，仅作context，不计完整Physical层。
- External：9月18日观测，17/22 fresh、5项unavailable，均为`context_only`。repo WTI/Brent 95.47/99.03与可靠近月结算100.30/103.87冲突，repo油价已隔离。
- Options：最新为9月17日16,016条、216 series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖99.11%/69.50%/0。相对9月18日底层已落后，只作历史研究面。
- Metadata：partial；有效合约匹配67.49%，multiplier/tick/margin/limit覆盖30.15%，last-trading-day覆盖67.49%；空参数不推断。

### Night Session日历隔离

Night状态原始字段为`trading_date=2026-09-19`、`night_session_date=2026-09-18`、06:02:53生成，raw `data_fresh=true`、validation passed、published；但只有423个有效合约、37个产品，另有165个outside-window、4个no-trade、214个query error和214个unresolved，`coverage_complete=false`。

9月19日是周六，不是交易日。交易所规则规定交易日为周一至周五，连续交易属于随后实际交易日；因此9月18日晚间记录应归属9月21日，而仓库却标成9月19日。按协议整批隔离，**不自行重标**，也不把它称为今晚行情。[INE交易规则](https://www.ine.cn/eng/services/rules/rulebook/202202/t20220222_821734.html)

下表的“早前Night”仅用于分解9月18日日盘，来自合法归属9月18日的历史快照；它不是周五晚间、也不是今晚未来行情。当前周五夜盘exact fallback不可得，`night_session_fallback_used=false`。所有制度上应有夜盘的候选因此最高79分。

## 三、商品仪表盘

1D/5D均为9月18日同合约结算收益；curve为near-minus-next期货结构，不是现货基差。Night→Day仅在具体合约一致时计算。海外为周五最后有效收盘，不冒充周六实时盘。S/P/E表示surface/positioning/execution readiness。

| 板块 | 品种/合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical/basis | 早前Night close；vs close/vs settle；ΔOI；Day | 周五海外；Options；周一信号 |
|---|---|---|---|---|---|---|---|
| 能源 | SC2611 | 728/754.4；-6.29%/-0.30% | 28.52万/4.22万/-2,115；back 1.59%、z-2.49 | SC缺失 | 762.5；-2.89%/-5.28%；-980；Day -4.52% | WTI100.30、Brent103.87；Y/N/N；反抽失败空 |
| 能源 | LU2611 | 5440/5515；-2.10%/+0.51% | 15.64万/7.14万/+1,703；back 4.79%、z2.30 | LU缺失 | 5574；+0.60%/-1.05%；+1,334；Day -2.40% | 原油弱、产品相对紧；无成熟执行面；相对SC |
| 能源 | FU2611 | 4200/4259；-3.29%/-0.77% | 81.04万/19.09万/-12,686；back 12.80% | C/context | 4298；-0.26%/-2.41%；-1,990；Day -2.28% | 原油弱、深back反对追空；Y/N/N |
| 贵金属 | AG2612 | 16304/16104；+2.79%/+2.73% | 16.59万/21.50万/+8,244；contango 0.12% | C/context | 16032；+2.82%/+2.33%；+1,660；Day +1.70% | 银66.556、周涨3.1%；Y/N/N且skew异常；回撤接受 |
| 贵金属 | AU2612 | 951.38/946.18；+0.96%/+0.17% | 11.96万/19.75万/+13,041；轻contango 0.08% | C/context | 944.52；+1.02%/+0.78%；+4,191；Day +0.73% | 金4385.90；N/N/N；不追 |
| 有色 | CU2610 | 109620/109530；+1.31%/+0.80% | 8.10万/15.19万/-7,625；back 0.33%、短历史 | C/context | 109650；+1.06%/+1.42%；-776；Day -0.03% | LME铜14562 proxy；N/N/N；Night已定价大部 |
| 聚酯 | TA701 | 6238/6312；-2.86%/0.00% | 136.76万/117.12万/+10,883；back 2.14% | C/context | 6398；+0.16%/-1.54%；-10,146；Day -2.50% | 原油回落；Y/Y/N；反抽失败 |
| 聚酯 | PR611 | 8132/8244；-3.06%/+1.10% | 10.10万/6.16万/-1,405；back 1.58% | 缺失 | 8348；-0.41%/-1.83%；+206；Day -2.59% | 成本下移；Y/N/N；不追空 |
| 农产品 | RM701 | 2357/2389；-1.32%/+0.84% | 60.64万/60.82万/+5,568；contango 0.92% | C/context | 2404；-0.87%/-0.70%；+13,828；Day -1.96% | CBOT豆1302.75；Y/Y/N；旧多已失效 |
| 农产品 | M2701 | 3397/3429；-1.47%/+0.21% | 204.64万/273.12万/-196,992；contango 1.10% | C/context | DCE query_error | CBOT粕351.1；失败产品；等待量仓 |
| 建材 | FG701 | 907/912；+0.55%/-7.32% | 108.62万/129.52万/-70,452；back 3.70% | 现货1008、C | 913；+0.88%/+0.66%；-47,960；Day -0.66% | 无exact外盘；局部Y/Y/N；单日噪音 |
| 新能源 | LC2701 | 127160/128460；-1.28%/-4.11% | 18.69万/42.54万/+9,528；back 1.25% | C/context | 制度无Night | 无exact海外；Y/N/N；不追空 |
| 航运 | EC2610 | 2172.5/2189；+2.99%/+7.09% | 2.54万/2.53万/-1,176；back 21.29% | exact运价缺 | 制度无Night | 运输事件映射不纯；N/N/N；周一重估 |

周五WTI结算100.30美元/桶，Brent结算103.87；两者当日分别约跌1.6%和0.9%。这支持原油风险溢价继续回吐，但并未消除沙特部分欧洲货源暂停、管道全面修复约需数周的右尾。[WSJ油市](https://www.wsj.com/finance/commodities-futures/oil-falls-as-worries-over-middle-east-supply-disruptions-ease-36be861a)｜[Reuters沙特供应](https://www.reuters.com/business/energy/aramco-halts-october-crude-deliveries-some-european-refiners-after-pipeline-2026-09-18/)

周五黄金期货4385.90美元/盎司、白银66.556，分别日涨约0.6%和1.7%；与此同时美国2年/10年收益率约4.744%/4.998%。这说明贵金属仍有韧性，但高利率是实质反证，不能把“信用主题”直接等同于追多。[WSJ贵金属](https://www.wsj.com/finance/commodities-futures/gold-rises-likely-supported-by-oil-pullback-0023a879)｜[WSJ美债](https://www.wsj.com/finance/investing/two-year-u-s-treasury-yield-reaches-new-multi-year-high-99d3112b)

## 四、相比上一期真正变化

1. **没有新的中国交易时段。** 周五EOD仍是最近完整快照；周六五所0条刷新不自动使last-good失效，也不能被写成市场“没有成交”。
2. **Night日期错误成为新的执行否决。** 周五晚记录标为周六交易日且有214个query error；LU/SC最高分由80降至79，周五21:45旧条件全部过期。
3. **原油周五最终结算继续回吐。** 它支持SC弱势和LU相对SC，但Aramco暂停部分欧洲10月货与较长修复期是最强竞争解释。
4. **金银在高收益率下仍强。** AG/AU的价格—量仓和海外同向保留研究价值；AG期权RR/BF出现不可信极值，曲面形状隔离。
5. **期权又落后一日。** 最新9月17日面只能作历史研究，0个execution-ready；不存在可证明优于期货的当前结构。
6. **旧建议处置：** `COM-M-LUSC-RELATIVE-20260918` 80→79且转休市；`COM-M-SC2611-REVERSAL-20260917` 76维持研究、旧入场失效；`COM-E-AG2612-PRECIOUS-REBOUND-20260918` 69维持；TA/EC维持观察；RM旧多继续退出。没有成交反馈，不假设用户持仓。

## 五、产业链地图

- **相对最强：LU相对SC，置信度中。** Friday EOD表现、OI方向与curve分化支持1/2层，海外“产品紧、原油溢价回吐”支持第4层；反证是缺SC/LU实体、exact crack与合法周五Night。
- **绝对最弱：SC—PX—TA—PR原油成本链，置信度中。** SC日内续跌，聚酯链同步回吐；SC仍back且沙特/Hormuz尾部反对周一低开追空。
- **贵金属：AG/AU偏强，置信度中。** 中国价仓与海外金银同向，但curve轻contango、高真实利率和不可执行期权阻止升级。
- **农产品：M/RM偏弱，置信度中低。** 国内价跌、M大幅减仓与contango支持弱势；CBOT仍高、C级basis与DCE Night缺失反对追空。
- **内需/新能源/航运：FG—SA—LC弱趋势，EC事件风险，置信度低。** FG与LC曲线并未确认追空；EC上涨但OI下降且缺exact运价，不构造伪套利。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 有效支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | 多13手LU2611/空1手SC2611近似名义中性 | 24/18/17/12/8 | **79** | 1、2、4 | 存在待验证优势｜部分充分、Night失效｜休市/周一重报价 |
| 2 | SC2611反弹失败空 | 22/16/18/12/8 | **76** | 1、2、4 | 存在待验证优势｜部分、供应尾部反对｜休市/周一重设锚 |
| 3 | AG2612回撤接受多 | 19/16/15/10/9 | **69** | 1、4 | 存在待验证优势｜部分、curve/利率反对｜休市/待报价 |
| 4 | TA701弱势延续空 | 19/16/14/10/9 | **68** | 1、4 | 存在待验证优势｜部分、back反对｜休市/反抽失败 |
| 5 | EC2610事件风险多 | 20/14/15/9/8 | **66** | 1、2 | 证据不足｜exact运价缺失、OI下降｜周一日盘观察 |

分项均已复算。AG/TA/EC只有两层支持，严格低于70；LU/SC因应有Night无法核实，最高79。分数是研究排序，不是胜率或仓位指令。所有期货结构的计划止损都不能把最大损失变成有限。

## 七、前三名研究交易卡

### 1. 多13手LU2611 / 空1手SC2611｜相对价值｜79

**事实：** 周五LU/SC收盘5440/728，比价7.4725；LU ΔOI +1,703、back 4.79%，SC ΔOI -2,115、back仅1.59%。13手LU与1手SC按稳定合约单位对应名义约707,200与728,000元，偏差-2.86%，只能叫近似dollar-neutral，绝不是beta-neutral。收益公式为`130×(LU出-入)-1000×(SC出-入)`。

- 市场隐含：原油风险溢价回吐速度快于低硫产品紧张消退。
- 我们的分歧：若产品链短缺延续，LU相对SC仍可扩张；最强反证是原油供应再中断导致SC凸性重新占优。
- 最佳表达：上述13:1静态篮子；不开跨市场“柴油裂解”伪套利。
- 好成交：周一09:45后实时比价在7.35—7.50获得接受并重上7.45，先1/3。
- 中成交：突破7.60后回踩7.50—7.60成功，仓位减半。
- 坏成交：开盘直接高于7.75、低于7.20，或任一腿深度不足，放弃。
- 止损/失效：45分钟接受7.20下方；或LU back低于3%、SC back高于4%、Brent重上108并有新增供应中断证据。
- 退出：TP1 7.65或+1.5R；TP2 7.90或+3R；1—3D无扩张退出。
- 风险：试仓最大损失0.15%—0.25% NAV；与所有能源方向合并≤0.50%。相关性破裂会显著放大损失。
- 参数：SC 1,000桶/手、tick 0.1元/桶、tick value 100元；LU合约单位按10吨、tick 1元/吨、tick value 10元作研究换算，动态margin/limit必须向经纪端确认。两者最后交易日10月30日、交割日11月6日，实物交割，10月中旬前移仓。
- 压力：一板不利损失=`707,200×L_LU+728,000×L_SC`；两板按复合限幅计算。L未确认，不编固定金额。
- 周末gap：沙特/Hormuz新冲击可能令SC短腿先跳空；周一首跳不追。

### 2. SC2611｜反弹失败条件空｜76

**事实：** EOD close/settle=728/754.4，1D -6.29%，ΔOI -2,115，back 1.59%。合法早前Night收762.5，vs previous close -2.89%、vs settlement -5.28%、ΔOI -980；日盘再跌4.52%。

- 市场定价：替代装船与修复预期正在挤出极端短缺溢价。
- 分歧：回吐仍可能延续；竞争解释是周末新增中断、Hormuz运输或欧洲货暂停重新抬升右尾。
- 好成交：周一09:45后反抽735—755失败并重新跌破728/VWAP。
- 中成交：先破720，再回抽728失败；仓位减半。
- 坏成交：直接低于700、盘口变薄或止损距离过大，放弃。
- 止损：45分钟接受760上方。
- 失效：重上775.9、back重扩至3%以上且Brent高于108，或供应中断明确恶化。
- 退出：TP1 720或+1.5R；TP2 690或+3R；1—2D无扩张退出。
- 风险：0.15%—0.25% NAV；最大损失不由止损限定。
- 参数：1,000桶/手、tick 0.1、tick value 100元，周五收盘名义728,000元；动态margin/limit未确认。最后交易日10月30日、交割日11月6日，实物交割。
- 压力：一板空头损失`728,000×L`；两板`728,000×[(1+L)^2-1]`。周一先核L。
- 放弃条件：油价跳空高开且curve同步变陡，或经纪端保证金上调导致风险预算超限。

### 3. AG2612｜回撤接受条件多｜69

**事实：** EOD close/settle=16304/16104，1D +2.79%、5D +2.73%，ΔOI +8,244，轻contango 0.12%。早前Night收16032，vs close +2.82%、vs settlement +2.33%、ΔOI +1,660；日盘再涨1.70%。周五COMEX银66.556、周涨3.1%。

- 市场定价：信用/地缘需求与美元波动对冲仍在，但高收益率限制估值。
- 分歧：若周一回撤被接受，金银的非利率需求仍可能延续；最强反证是10年美债继续站稳5%、美元再走强。
- 好成交：周一09:30后16050—16200获得接受并重上16320/VWAP。
- 中成交：突破16350后回踩不破；仓位减半。
- 坏成交：直接高于16700、跌破15900或外银低于64，放弃。
- 止损/失效：30分钟接受15880下方；或外银跌破64且黄金跌破4300。
- 退出：TP1 16650或+1.5R；TP2 17100或+3R；1—3D时间止损。
- 风险：0.15%—0.20% NAV；贵金属共享因子≤0.40%。
- 参数：15千克/手、tick 1元/千克、tick value 15元，名义约244,560元；repo动态margin/limit缺失，最后交易日12月15日、交割日12月17日。
- 期权未替代：9月17日AG曲面RR/BF出现不可信极值且execution-ready=false，不以历史面包装成有限损失。
- 压力：一板多头损失`244,560×L`；两板`244,560×[1-(1-L)^2]`，L待经纪端确认。

## 八、商品期权专项

最新有效截面为9月17日，已经落后于9月18日底层和周五国际收盘；只能研究IV/偏度，不能当周一报价。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/56.54% | +9.02vol | +0.73/+1.41 | Y/N/N | 事件vol仍贵，待实时put spread |
| FU2611/10-19 | 60.62%/45.36% | +15.26vol | -0.50/+1.42 | Y/N/N | 裸买凸性成本高 |
| TA701/12-11 | 31.87%/28.17% | +3.70vol | +2.43/+0.72 | Y/Y/N | 当前Delta已失真 |
| RM701/12-11 | 20.80%/16.53% | +4.27vol | +6.39/+0.98 | Y/Y/N | 旧多失效，不能沿用 |
| PR611/10-13 | 27.81%/30.82% | -3.02vol | +2.35/+0.95 | Y/N/N | IV<RV不单独证明便宜 |
| AG2612/11-24 | 44.14%/31.14% | +12.99vol | 异常极值 | Y/N/N | 曲面形状隔离，不推Dealer Gamma |

当前没有可证明优于裸期货的期权。周一取得双边实时报价后，才比较SC有限净支出put spread或AG有限净支出call spread；执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点与行权交割均须重算。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、下一实际开盘风险地图

严格区分：①9月18日中国完整EOD；②属于9月18日的早前Night，仅作历史分解；③周五海外最终收盘；④9月18日晚至9月19日凌晨的仓库Night日历异常并已隔离。**今晚无21:00夜盘；下一窗口为9月21日09:00。**

| 品种 | EOD→早前Night/Day→海外 | 周一倾向 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| LU/SC | SC日盘再跌、LU相对强→原油周五再跌 | 比价偏强但已扩张 | 不追；45m | 7.20/7.45/7.60、两腿curve |
| SC | -6.29%、back压缩→油价回吐但供应尾部 | 低/平开不确定 | 不追空；45m | 720/728/755/760、Brent |
| FU | -3.29%、深back→原油弱 | 低开与结构冲突 | 45m | 4200/4259、back12% |
| PX/TA/PR | 成本链下跌→油价续弱 | 偏低，但已预交易 | 45m | 链内breadth、OI、curve |
| AG/AU | 中国价仓强→外盘金银收高 | 偏高，但利率反对 | 不追；30—45m | AG16200/16320、DXY、10Y |
| CU/AL/ZN/NI | 中国有色修复→LME代理偏强 | 平/高开分化 | 45m | exact LME、CNH、roll |
| M/RM | 国内跌、contango→CBOT尚高 | 平/低开分化 | 45m | M/RM ΔOI、basis、near-next |
| FG/SA | 中期弱但Friday close混合 | 平开/噪音 | 30m | FG907/913、curve |
| EC/LC/AP/JD/SF/SM/SI/PS | 制度无Night | 周一09:00首次定价 | 45m | 量仓、curve、实体 |

周末没有15:00—19:30实时海外盘，也没有中国21:00窗口。exact USD/CNH与DXY同一时点不可得，不编人民币贡献率。最不值得交易的是：周一低开追SC/FU/TA、追AG第一跳、把LU/SC称无风险、以及用周五期权面直接下单。

## 十、未来24小时与7天事件

- 未来24小时：Saudi East-West/Yanbu修复、Sohar替代装船、Hormuz/Perim船流及部分欧洲10月货取消。能源任何周末头条都以gap压力测试处理，不提前押方向。
- 9月21日09:00：中国下一实际日盘；全部候选重取close/settle参照和盘口，等待30—45分钟。
- 9月21日当周：欧盟电工钢临时保障措施将于9月25日起生效，涉及配额与最低进口价；关注硅钢/铁合金链，但不直接映射为可交易价差。[Reuters欧盟电工钢](https://www.reuters.com/business/energy/eu-impose-provisional-safeguards-protect-electrical-steel-imports-2026-09-18/)
- 9月23日22:30：EIA周度石油数据；能源Delta提前降低，期权仅允许有报价的有限净支出结构。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- 9月24日前后：USDA周度出口销售窗口；M/RM/C/油脂只按实际销售、中国采购和basis反应调整。[USDA出口销售](https://www.fas.usda.gov/data/export-sales-weekly-export-sales)
- 未来7天：北美收割天气、马棕出口、中国交易所风控、SC/FU/LU交割月移仓；CFTC COT仅作滞后拥挤背景。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 下一WASDE按官方日程核对，不制造未确认催化。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码及动态新增，共77个产品；期权64产品。
- 实际取数且已分析：9月18日五所77产品全部进入方向、1D/3D/5D/20D、量仓、curve、跨期/跨品种/跨市场、加工利润、风格/中性、波动率、偏度和事件凸性扫描；70个具备有效趋势/量仓/curve。
- 周六新增中国取数：0/77，原因是休市，不是遗漏；周五last-good继续有效。原始最新Night 423合约/37产品但日期异常且214 query errors，整批隔离。
- 数据不足：SC/LU实体；A/B级basis；exact import parity；可靠加工利润；合法归属的周五Night；9月18日期权；全部实时bid/ask；动态交易参数多数不完整。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；保留覆盖记录，不提高门槛后静默删除。
- 黑色建材9/9：FG/SA中期弱但curve或单日价格冲突，JM/I/RB无三层共振。
- 有色贵金属12/12：AG入榜，AU次之；CU大部涨幅已在早前Night完成，NI/SS无独立优势。
- 能源炼化化工25/25：LU/SC、SC、TA入榜；FU深back反对追空，PX/PR/EB/EG成本传导仍分化。
- 新能源及GFEX新材料全部扫描：LC五日弱但back与实体不足；SI/PS及新材料无三层优势。
- 农产品油脂饲料畜牧22/22：M/RM国内偏弱、CBOT反对追空；油脂、玉米、棉糖果链未发现三层共振。
- 航运与软商品全部扫描：EC入低分观察；exact运价缺失，CF/CY/SR/AP/CJ/PK无可执行异常。
- 策略/周期：方向、基差/跨期、curve、跨品种、跨市场、风格/近似中性、波动率/偏度/事件凸性；1—3D、5D、20D均完成。没有定义合格beta-neutral篮子，也没有可执行跨市场套利。
- 风险预算：周末新增风险为0；周一重报价后，单笔试仓0.15%—0.25% NAV，确认交易最高0.75%；能源共享因子初始≤0.50%，贵金属≤0.40%，单主题确认后≤2.5%。
- 压力测试：1/2个涨跌停、周末地缘gap、两腿相关性破裂、流动性消失、保证金上调、IV跳升/塌陷、交割挤压、人民币急变。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；周末休市，周五旧锚全部过期，周一09:00后重新报价并等待30—45分钟。  
C. 今晚应继续观察的机会：LU2611相对SC2611、SC2611反弹失败空、AG2612回撤接受多、TA701成本回吐及EC2610事件重估。  
D. 今晚必须避免或退出的交易：平移周五条件单、低开追SC/FU/TA、追AG第一跳、把LU/SC称无风险或beta-neutral、恢复RM旧多，以及在execution-ready=false时臆测期权成本。