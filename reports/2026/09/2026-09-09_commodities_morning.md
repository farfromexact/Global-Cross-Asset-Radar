# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-09

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：2026-09-09 07:18:45 北京时间；研究截点：07:00；最近完整中国EOD：2026-09-08；当前交易日：2026-09-09；下一实际交易窗口：今日09:00，首个合格验证窗口不早于09:45。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；铜与甲醇获三层确认，但09:30中国CPI/PPI将重置信号，最早等09:45再判断。**

当前regime：**LME铜创纪录带动有色外盘重估；甲醇维持国内高弹性；原油、燃油、LPG、聚酯的日盘收盘溢价在Night明显回吐；09:30中国通胀数据构成开盘后二次定价。**

## 二、数据质量与覆盖

本期按第一读取层读取[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)和[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并因候选合约、Night curve、期权series和交易参数下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[逐合约Night](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json)、[Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)及[Contract metadata](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：`schema_version=2`，`requested_date=2026-09-08`，2026-09-09 06:15:29+08:00生成。
- Futures/Market State：9月8日SHFE、INE、DCE、CZCE、GFEX五所共802个合约；802/802源日期匹配，`source_date_match_pct=100%`，`full_market_ready=true`，critical errors=0。7条OHLC placeholder已排除；无重复、非法OHLC、负成交量或负OI。`official_complete=false`来自basis、会员排名、仓单及metadata缺口，不否定核心EOD。
- Night Session：`trading_date=2026-09-09`、`night_session_date=2026-09-08`，06:03:03生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。594个有效夜盘合约、55个品种、193个合法outside-window、15个no-night-trade；missing timestamp/price/quote、query error、unresolved contract均为0，无coverage warning。这是**属于9月9日交易日、今晨已经完成的连续交易阶段**，不是未来行情。
- Physical：9月8日20个目标中18个按原生频率fresh，SC/LU unavailable。全部可算basis为C级且`eligible_for_physical_score=false`，只作context。CZCE仓单为当日；GFEX的LC/PD/PS/PT/SI沿用9月1日且已stale；SHFE/DCE仓单缺失。仓单不冒充社会库存。
- External：repo日频17/22有效，全部`context_only`；07:00另补充海外最终收盘/最新报价。repo连续合约与Reuters最终结算口径存在差异，故不做exact import parity。
- Options：9月8日18,886条chain、350个series、52/64产品；IV coverage 97.64%、OI coverage 84.94%、bid/ask coverage 0。局部339个series可研究surface、248个可研究positioning；全局surface/positioning/execution均未就绪，0个execution-ready。BC/SC及AD/AG/AL/AO/AU/CU/NI/PB/SN/ZN缺失，Dealer Gamma方向未知。
- Contract Metadata：有效合约匹配73.32%，动态margin/limit等约29.8%，last-trading-day约67.3%，night-session字段0。未确认字段不猜；CU/AL静态合约规则由交易所页面交叉核实。

## 三、商品仪表盘

Night收益以相对9月8日close为隔夜新增信息主锚，相对settlement仅作辅助。Volume/OI/ΔOI单位为手；所有Night行均为fresh exact-contract，时间为北京时间。

| 板块/合约 | EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Basis/Physical | Night close；vs close/settle；ΔOI；时间 | 07:00海外 / Options S-P-E | 09:00信号 |
|---|---|---|---|---|---|---|
| 有色 **CU2610** | 110620/110260；+0.96%/+0.68% | 111190/229937/+15488；BWD +0.59% | 铜现货仅C级context | 111300；**+0.61%/+0.94%**；+13；00:59 | LME铜约14720、纪录区；Options缺失 | **多头优先，等09:45** |
| 化工 **MA610** | 3359/3279；+3.50%/+7.72% | 2956989/727099/+106367；BWD +0.91% | C级spot/basis | 3408；**+1.46%/+3.93%**；-30275；23:00 | 油价支持；surface底层价不一致，E=false | **回撤确认多，等09:45** |
| 有色 **AL2610** | 24460/24450；+0.43%/+1.58% | 133622/258395/+395；近月约平 | 现货仅C级context | 24645；**+0.76%/+0.80%**；+122；00:59 | LME铝3333；Options缺失 | 条件多，等09:45 |
| 贵金属 **AU2610** | 953.12/955.90；+0.14%/-0.53% | 174632/151058/-3491；Contango -0.53% | 实体层不足 | 949.24；**-0.41%/-0.70%**；+910；02:30 | 现货金-0.4%；Options缺失 | 反抽失败空观察 |
| 原油 **SC2610** | 720.6/703.3；+2.15%/+10.37% | 136321/38758/-216；BWD +5.76% | SC Physical不可得 | 714.7；**-0.82%/+1.62%**；-849；02:30 | Brent97.92、WTI93.03 | 日盘溢价回吐，不追多 |
| 燃油 **FU2611** | 3988/3893；+2.47%/+2.21% | 691185/217481/+14448；BWD +4.37% | C级basis | 3895；**-2.33%/+0.05%**；-17335；23:00 | 海外油仍涨；local surface可研究/E=false | close溢价全失，先观望 |
| LPG **PG2610** | 6857/6677；+1.95%/+8.15% | 206067/106203/+871；BWD +3.42% | 实体层不足 | 6691；**-2.42%/+0.21%**；-5376；23:00 | 油价支持；IV偏高/E=false | 上期多头条件失效 |
| 聚酯 **EG2610** | 5925/5801；0.00%/+5.84% | 2316223/360872/+11439；BWD +7.34% | 实体层不足 | 5772；**-2.58%/-0.50%**；-22490；23:00 | 油强、EG弱；IV-RV约+8.8vol | 不抄底，等45m |
| 聚酯 **TA701** | 6210/6050；+2.16%/+2.47% | 1170065/1129128/+53285；BWD +3.36% | C级context | 6142；**-1.10%/+1.52%**；-18118；23:00 | 油价支持；E=false | 昨晚触发未出现 |
| 芳烃 **PX611** | 9152/8866；+2.28%/+3.29% | 361046/177048/+18971；Contango -3.67% | 实体层不足 | 9010；**-1.55%/+1.62%**；-10841；23:00 | 无exact映射；surface口径冲突 | 不追日盘强势 |
| 建材 **FG701** | 977/967；-1.12%/+1.47% | 1195017/1216889/+35467；Contango -4.75% | 仓单+1984；basis C | 973；**-0.41%/+0.62%**；+26956；23:00 | 无exact外盘；surface Y/Y/N | failed-squeeze空观察 |
| 氯碱 **SH611** | 1968/1948；-0.31%/+1.25% | 533459/224638/+1909；Contango -0.82% | 仓单-64 | 1984；**+0.81%/+1.85%**；+12397；22:59 | IV约26.1% vs RV20 16.2%；E=false | 价格强、curve反对 |
| 黑色 **I2701** | 744.5/740；+0.75%/+2.49% | 302940/590593/+1396；轻contango | C级basis | 739；**-0.74%/-0.14%**；+12437；23:00 | SGX铁矿约100.15 | 内外/curve混合 |
| 油料 **RM611** | 2366/2362；-0.17%/+1.33% | 556169/599327/-3710；BWD +3.56% | 仓单+4730 | 2342；**-1.01%/-0.85%**；+460；23:00 | CBOT豆粕仅context；E=false | 仓单与back冲突 |
| 塑化 **V2701** | 5113/5036；-0.42%/+3.51% | 1572977/1121515/+24005；Contango -0.45% | 实体层不足 | 5118；**+0.10%/+1.63%**；+45423；23:00 | IV低于RV但无报价 | 前期空头观察失效 |

海外截至最新完整时段：Reuters记录9月8日Brent结算97.92美元/桶、WTI 93.03，分别约+0.9%/+1.7%；油价仍强，但SC、FU、PG、EG相对日盘close全部回吐，说明中国夜盘对新增headline的边际弹性下降。[Reuters油市，2026-09-08](https://www.reuters.com/business/energy/oil-rises-risks-prolonged-mideast-conflict-heighten-supply-worries-2026-09-08/) LME铜约14720美元/吨并处纪录区，铜是今晨少数“海外↑—中国Night↑—国内curve仍back”的同向品种。[LME铜](https://www.lme.com/metals/non-ferrous/lme-copper) 美元/离岸人民币九月期货约6.7045、变化极小，人民币不是本期排序主因。[HKEX USD/CNH](https://www.hkex.com.hk/Market-Data/Futures-and-Options-Prices/Foreign-Exchange/CUS---USD_CNH-Futures-and-Options?sc_lang=en)

## 四、相比上一期真正变化

1. **CU成为新第一候选。** 9月8日结算+0.96%、ΔOI +15488、EOD back约0.59%；Night再涨0.61% vs close，LME铜进入约14720纪录区。支持来自价格量仓、curve和境外定价三层；反证是Night back略收窄至约0.45%、国内Physical只够context。
2. **MA延续三层强势，但昨晚条件没有触发。** Night低点3341，高于昨晚要求的3300—3330回撤区，随后close 3408；因此不能事后宣称条件单成交。双锚均强且Night curve由约0.91%扩至1.67%，但ΔOI减少30275，且期权surface底层结算价与期货不一致。
3. **能化“日盘强、Night弱”的分裂扩大。** FU/PG/EG/PX/TA相对close分别-2.33%/-2.42%/-2.58%/-1.55%/-1.10%，但多数相对settlement仍为正。这意味着夜盘主要抹去了日盘尾段溢价，而不是形成了完整的新空趋势；强backwardation也反对无条件追空。
4. **油价仍涨，但中国原油弹性转负。** SC相对close -0.82%，相对settlement仍+1.62%，Night curve基本维持。市场隐含供应风险仍高，但新增新闻不再带来同幅国内追价；昨晚SC和FU多头触发均未出现。
5. **贵金属的“黄金信用”仍不成立。** 国际金约-0.4%，AU Night -0.41%，而美元并未显著走强；更强竞争解释是油价抬升通胀与加息概率，压过地缘避险。地缘升级仍是空头最大反证。[Reuters黄金，2026-09-08](https://www.reuters.com/world/india/gold-gains-dollar-eases-with-us-inflation-data-radar-2026-09-08/)
6. **中国8月外贸强、内需验证仍不足。** 出口同比+25%、进口+28.2%，但报道同时指出国内消费与投资仍弱；这支持铜的外需/全球定价，不足以把所有黑色和化工都升级为国内需求牛市。[Reuters中国贸易，2026-09-08](https://www.reuters.com/world/asia-pacific/chinas-exports-up-25-yy-august-imports-surge-282-2026-09-08/)

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：昨晚要求3930—3960承接后重上3990或突破4005；Night high仅3939，未触发，当前降为观察。
- `COM-M-MA610-SETTLE-RECLAIM-20260908`：延续，原3300—3330回撤未发生；因新数据改为09:45后重新定价，不追认成交。
- `COM-E-TA701-DAY-REPRICE-20260908`：Night high 6188，未重上6210，原触发未发生，降级。
- `COM-E-SC2610-GAP-20260905`：日盘close溢价被Night部分回吐，降为已预交易观察。
- `COM-E-ZN2610-LME-SQUEEZE-20260908`：Night仅+0.09% vs close且curve转轻contango，降级。
- `COM-M-PG2610-OIL-BREADTH-20260908`：Night -2.42% vs close，原多头研究失效；若此前确已按条件建立，应按原止损/时间纪律退出，不假设真实持仓。
- `COM-E-V2701-SQUEEZE-20260904`：Night重新站回close附近且增仓，failed-squeeze空头观察失效。

## 五、产业链地图

- **最强：铜—铝全球有色链，偏多，置信度中高。** CU价格量仓、EOD/Night back与LME纪录同向；AL也获外盘和Night支持。最大缺口是中国高质量Physical/basis、CU/AL期权缺失及09:30数据风险。CU比AL更优，因为其curve和成交活跃度确认更强。
- **最强国内单品：甲醇，偏多，置信度中高。** EOD价涨仓增、Night两个收益锚均强、curve加深；但Night ΔOI转负、期权底层价冲突，不能把层数自动转成确认仓。
- **最弱边际弹性：油—燃油—LPG—聚酯，方向混合，置信度中。** 海外油涨而中国多数Night相对close下跌；这是对日盘尾部溢价的否定。curve仍back且供应风险未消失，故“不追多”优于“直接反手空”。
- **建材/氯碱：FG偏空、SH偏多但结构冲突，置信度中低。** FG contango和仓单增加支持failed-squeeze空；SH价格/OI偏强却contango扩大，只够早期异常。
- **农产品/新能源/航运：无70分机会。** RM下跌与仓单增加偏空，但backwardation反对；LC 5D仍弱且GFEX仓单过时；EC缺exact海外映射。USDA Crop Progress虽按日程应发布，但截至截点未取得可核实新报告，不以缺失数据补叙事。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | **CU2610回撤确认多** | 22/18/17/13/9 | **79** | 1、2、4 | 存在待验证优势｜部分｜等09:45触发 |
| 2 | **MA610回撤/突破确认多** | 22/18/15/13/10 | **78** | 1、2、4 | 存在待验证优势｜部分｜等09:45触发 |
| 3 | **AL2610跟随LME的回撤确认多** | 20/16/14/10/9 | **69** | 1、4 | 存在待验证优势｜部分｜等09:45触发 |
| 4 | **AU2610反抽失败空** | 19/16/14/10/9 | **68** | 1、4 | 存在待验证优势｜部分｜等30m及数据 |
| 5 | **FG701 failed-squeeze空** | 18/17/8/12/12 | **67** | 1、2 | 存在待验证优势｜部分｜等30—45m |

分项总和已复核。分数是研究排序，不是胜率、期望收益或仓位指令。CU与AL属于同一全球有色/美元因子，风险必须合并；所有期货卡的计划止损都不等于结构限定最大损失。

## 七、前三名交易卡

### 1. CU2610｜回撤确认多｜79

**事实：** EOD OHLC 109540/110890/109320/110620，settle 110260；Night OHLC 111170/111720/110960/111300，+0.61% vs close、+0.94% vs settlement，Night ΔOI +13。EOD CU2609/CU2610 back约0.59%，Night约0.45%，方向仍确认但边际收窄。LME铜处纪录区。  
**市场定价：** 已经在交易矿端约束、美国关税/库存重排及电网/AI需求，但中国开盘尚未吸收09:30通胀数据。  
**分歧：** 只要09:30后价格仍接受Night价值区，国内铜对全球纪录价的跟随可能未完成；最强反证是纪录区获利回吐、curve转contango及PPI弱于预期。  
**最佳表达：** CU2610期货；CU期权链缺失，不能证明有限损失结构价格合格。

- 等待：至少到09:45，即CPI/PPI发布后15分钟。
- 好成交：110800—111200承接，重新站上111350/VWAP，先1/3仓。
- 中成交：突破111750后成功回踩，仓位为好情景一半。
- 坏成交：直接高于112500且无回撤，放弃。
- 止损：30分钟接受110500下方；逻辑失效：跌破110260、curve转contango且LME回落至约14400下方。
- 退出：TP1 113000或1.5R，TP2 115500或3R；1—3日无扩张退出。
- 成本：限价；手续费按经纪商实收，允许总滑点≤计划1R的10%，10%—20%减半，>20%放弃。
- 风险：0.25%—0.45% NAV；若与AL/BC同做合并计算，未出现第四层前不升至确认仓。
- 参数：5吨/手、tick 10元/吨、tick value 50元；Night close名义约556500元。CU2610最后交易日2026-10-15、实物交割，交割风险窗口前roll/exit。[SHFE铜合约](https://www.shfe.com.cn/eng/Market/Futures/Metal/cu_f/ContractText/)
- 动态margin/limit未确认；一板压力=`556500×L`，两板连续不利=`556500×[1-(1-L)^2]`。期货最大损失不受结构限定。

### 2. MA610｜回撤/突破确认多｜78

**事实：** EOD 3359/3279，1D +3.50%、5D +7.72%，ΔOI +106367；Night 3351/3410/3341/3408，+1.46% vs close、+3.93% vs settlement，ΔOI -30275；near-next back约0.91%扩至1.67%。  
**市场定价：** 日盘close已远离settlement，但Night相对close仍继续上涨，新增弹性真实存在。  
**分歧：** 市场可能低估甲醇自身结构强度；竞争解释是油价beta与拥挤追价，Night减仓以及Physical不足支持这一反证。  
**最佳表达：** MA610期货。MA期权surface的underlying settlement=3374，与期货EOD settlement=3279不一致，不能用其IV/Greeks定价。

- 等待：09:45以后。
- 好成交：3360—3390承接后重新站上3410/VWAP，先1/3仓。
- 中成交：3420突破并回踩成功，仓位减半。
- 坏成交：高于3470无回撤，放弃。
- 止损：30分钟接受3335下方；逻辑失效：跌破3279且back显著收窄。
- 退出：TP1 3480或1.5R，TP2 3600或3R；1—2日时间止损。
- 风险：0.25%—0.45% NAV；与SC/FU/PG/TA/PX视为同一油价/能化因子。
- 参数：10吨/手、tick 1元/吨、tick value 10元；Night close名义约34080元。repo记录margin 11%、limit 9%、最后交易日2026-10-21、最后交割日10月26日，实物交割。[CZCE甲醇规则](https://english.czce.com.cn/en/Rulebook/DetailedRules/webinfo/2024/02/1708568086958539.htm)
- 以3279结算作压力锚，一板不利约2951元/手，两板复合不利约5637元/手；止损穿透和涨跌停流动性消失时风险更高。

### 3. AL2610｜LME跟随回撤多｜69

**事实：** EOD 24460/24450，1D +0.43%、5D +1.58%，ΔOI +395；Night 24470/24665/24415/24645，+0.76%/+0.80%，ΔOI +122。LME铝日频约3333，但国内curve近乎平，未构成独立结构层。  
**市场定价：** 海外供应/运输风险已进入铝价；国内仅温和跟随。  
**分歧：** 若09:30后仍守Night高位，进口成本映射可能继续；反证是国内curve和Physical均未确认，且与CU高度同因子。  
**最佳表达：** AL2610期货；AL期权缺失，不能给可成交有限损失替代。

- 等待：09:45以后。
- 好成交：24520—24600承接后重上24670，先1/3仓。
- 中成交：24720突破回踩，仓位减半。
- 坏成交：高于24900无回撤，放弃。
- 止损：30分钟接受24440下方；逻辑失效：跌破24335且LME铝回落至3300下方。
- 退出：TP1 24950/1.5R，TP2 25400/3R；1—3日时间止损。
- 风险：0.25%—0.40% NAV；与CU/BC合并，总有色试仓风险不超过0.75% NAV。
- 参数：5吨/手、tick 5元/吨、tick value 25元；Night close名义约123225元。AL2610最后交易日2026-10-15，实物交割；进入交割月前roll/exit。
- 动态margin/limit未确认；一板=`123225×L`，两板连续不利=`123225×[1-(1-L)^2]`。最大损失不受结构限定。

## 八、商品期权专项

最新有效截面为9月8日，但不是当前可执行报价：

- 全局52/64产品、339个surface-ready series、248个positioning-ready series、0个execution-ready；bid/ask coverage=0。
- CU/AL/AU/AG/SC等11个重点产品缺失，不能评估ATM IV、RR25、event convexity或“期权是否优于裸期货”。
- MA610 9月11日到期series表面ATM IV约53.8%、RV20约31.1%，但surface底层settlement 3374与期货3279冲突；该IV差仅作异常审计，不计证据层。
- EG2610局部ATM IV约47.5% vs RV20 38.7%，SH611约26.1% vs 16.2%，均显示波动溢价；没有bid/ask时不能认定能卖、能买或能成交。
- V2701等局部IV低于RV只代表研究线索，不是“便宜”的充分证据；Dealer Gamma方向未知，禁止Gamma squeeze/pin推断。
- 若开盘后取得人工实时报价，优先比较CU/AL有限损失call spread与期货；在此之前不报权利金、Greeks、滑点或净成本。

结论：**期权当前不优于裸期货，不是因为全部昂贵，而是关键产品缺失且execution readiness为零。**

## 九、9:00开盘风险地图

三层必须分开：Layer 1是9月8日完整中国EOD；Layer 2是归属9月9日、已经完成的Night；Layer 3是截至07:00的海外收盘/最新报价。09:30中国CPI/PPI是开盘后新事件，因此所有工业品条件单最早09:45验证。

| 合约 | 三层映射/预期 | Night是否已大量定价 | 追价与等待 | 开盘后最重要确认 |
|---|---|---|---|---|
| CU2610 | EOD↑、Night↑、LME纪录区↑；偏高开 | 较多 | 不追；等09:45 | 110800/111350/111750、curve、LME |
| MA610 | EOD强、Night继续↑、油价↑；偏高 | 是 | 不追；等09:45 | 3360/3410、Night curve、OI |
| AL2610 | EOD温和↑、Night↑、LME↑；偏高 | 部分 | 不追；等09:45 | 24520/24670、LME、CU breadth |
| AU2610 | EOD近平、Night↓、海外金↓；偏低 | 部分 | 不追空；等30—45m | 948.2/953.1/955.9、美元/收益率 |
| SC2610 | EOD close极强、Night相对close↓、外油↑；宽幅平/偏低 | EOD已大量预交易 | 不追；等45m | 703.3/714.7/720.6、back |
| FU/PG | EOD尾段强、Night完全回吐close溢价、外油↑ | 是且被否定 | 两边不追；等45m | settlement能否守住、OI、curve |
| EG/TA/PX | EOD强、Night相对close↓、外油↑ | 日盘尾段被回吐 | 不抄底；等45m | settlement、back、能化breadth |
| FG701 | EOD弱、Night微跌、contango/仓单偏空 | 较多 | 不追首跌；等30—45m | 967/973/981、contango |
| SH611 | EOD混合、Night↑、curve更contango | 部分 | 不追；等45m | 1962/1995、curve是否收窄 |
| I2701 | EOD↑、Night↓、SGX约平；平/偏低 | 混合 | 不追；等09:45 | 739/745、curve、PPI |
| RM611 | EOD平、Night↓、仓单↑但back | 部分 | 不追空；等45m | 2333/2362、back、油粕联动 |
| LC/SI/PS | 无制度夜盘；实体/仓单部分过时 | 不适用 | 09:00不接第一刀；等09:45 | CPI/PPI、GFEX新数据 |

典型信息弹性：`LME copper↑ → CU Night↑`，弹性为正；`External oil↑ → SC/FU/PG/EG Night relative-to-close↓`，弹性为负。后者说明边际国内买盘衰减，不等于供应风险消失。

## 十、未来24小时 / 7日事件

- **9月9日09:30：** 中国8月CPI/PPI。铜、铝、黑色、能化不在09:00—09:30建立无保护新仓；至少等发布后15分钟。[国家统计局发布日程](https://www.stats.gov.cn/sj/fbrc/)
- **9月10日09:00：** HC、SS和LU期权挂牌；首日只观察chain、surface、bid/ask和滑点，不使用伪历史IV。[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202608/t20260831_833165.html)｜[INE](https://www.ine.cn/eng/circularnews/circular/202608/t20260831_833166.html)
- **9月10日20:30：** 美国8月PPI；**9月11日20:30：** 美国8月CPI。贵金属、有色和油价仓提前降低Delta；无执行报价时不强行用期权买Vega。[BLS PPI](https://www.bls.gov/schedule/news_release/ppi.htm)｜[BLS CPI](https://www.bls.gov/cpi/)
- **9月11日00:00—02:00：** 劳动节顺延的EIA周报窗口；SC/FU/LU/PG及裂解相关敞口合并降风险。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- **9月11日约16:00：** IEA Oil Market Report；headline与库存冲突时只做条件触发，不预设方向。[IEA OMR](https://www.iea.org/reports/oil-market-report)
- **9月12日00:00：** USDA 9月WASDE；M/Y/P/OI/C/CF避免无保护重仓，若有实时报价优先有限损失结构。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **9月12日约03:30：** CFTC COT常规发布窗口，只作滞后拥挤背景，不解释今晨Night。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 持续监控Hormuz通行、也门对沙特能源设施袭击和俄乌谈判。Reuters显示替代供应与流量仍在，解释了油价尚未持续突破100美元；这是油价多头的实质反证。[Reuters解释，2026-09-08](https://www.reuters.com/business/energy/why-isnt-oil-above-100-despite-supply-disruptions-2026-09-08/)

## 十一、覆盖、风险与归档核对

63个强制代码全部取得9月8日有效主力合约，并完成1D/3D/5D/20D、量仓、curve、方向/跨期/跨品种/跨市场/RV/波动率/偏度/事件凸性扫描。另扫描14个动态品种；其中PL/PD/PT/BZ/LG/RR/OP/WR等8个满足有效分析条件，JR/PM/RI/RS/WH/ZC因零价、零量或零OI列为不适用/流动性不足。因此实际分析71个有效品种，而不是把77个产品键全部视为可交易。

- 黑色建材9/9：FG是最值得跟踪的异常；其余没有三层共振。
- 有色贵金属12/12：CU、AL入榜；AU为空头观察；期权关键链缺失。
- 能源炼化化工25/25：MA入榜；SC/FU/PG/EG/TA/PX的close溢价回吐是板块核心异常。
- 新能源/GFEX新材料全部扫描：LC/SI/PS无制度夜盘，五项仓单沿用9月1日，不能计新增证据。
- 农产品油脂饲料畜牧22/22：RM最异常，但仓单偏空与back冲突；其余无三层优势。
- 航运与软商品全部扫描：EC及CF/CY/SR/AP/CJ/PK没有可验证exact海外/Physical共振。
- 期权应覆盖64个产品，实际52个；12个数据不足、0个执行就绪。
- 高质量basis、exact import parity、beta-neutral篮子均不可得；本期不把proxy、C级basis或近似美元中性称套利。

风险预算：单一试仓最大损失0.25%—0.45% NAV；确认交易仍需第四层与价格触发，才可上调至0.75%—1.0%。CU+AL+BC按有色因子合并；MA+SC+FU+PG+TA+PX按油价/能化因子合并。压力测试必须覆盖1/2个涨跌停、止损穿透、保证金上调、流动性消失、相关性破裂、人民币急变、期权IV跳升/塌陷和交割挤压。

固定六路径已写入main并回读；manifest中`2026-09-09 + commodities_morning`恰好一条时方可判定`archive_status=success`。CI不轮询，`ci_validation_status=pending_or_unverified`。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：09:45后CU2610在110800—111200承接并重上111350，或MA610在3360—3390承接并重上3410；均先1/3仓。  
C. 今天应继续观察的机会：AL2610跟随LME的回撤多、AU2610反抽失败空、FG701 failed-squeeze、SH611价格强与curve弱的冲突。  
D. 今天必须避免或退出的交易：09:00—09:30抢跑CPI/PPI、追CU/MA首跳、把FU/PG/EG的close回吐直接当趋势空、延续已失效的PG/V旧观察、以及在execution_ready=false时臆测期权成本。
