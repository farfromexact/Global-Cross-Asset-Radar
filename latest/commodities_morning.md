# 全球商品期货期权高风险机会雷达｜晨间版｜2026-10-02

`prompt_version=radar_2026-09-06_coverage_v1` · `data_protocol_version=china_commodities_v2`

生成时间：2026-10-02 07:03 北京时间｜信息截点：07:00｜中国最近完整交易时段：2026-09-30日盘｜下一实际窗口：2026-10-08 08:55集合竞价、09:00日盘；下一夜盘为10月8日21:00。

> **今天的商品市场究竟有没有值得冒险的机会？**
>
> **截至本报告时点，无可立即执行的合格新交易。** 海外能源风险溢价显著上升，但中国国庆休市、境内报价与期权双边价不可得；节后最值得验证的是能源补涨/裂解、RU强势延续与OI相对强势。

## 一、今日一句话结论

中国休市期间Brent收涨4.37%至102.31美元，能源链节后跳空风险升高；不追不可成交的“影子价格”，10月8日只在重报价后等30—45分钟。

研究分类：①**存在待验证优势**：RU2701、能源产品紧张主题、OI701、BR2611；②**已分析但优势不足**：AU/AG方向、AO追涨、EC近月曲线；③**数据不足、暂时无法判断**：AP701空头、FU/SC相对价值和全部需要当前bid/ask的商品期权结构。

## 二、数据质量、时间与覆盖

实际读取：[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[根状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)。四者均为main当前快照；未用网页搜索替代仓库读取。

| 模块 | 实际日期/生成时点 | 读取状态 | 本期用途与限制 |
|---|---|---|---|
| Futures | EOD 2026-09-30；10/1 08:02生成 | `ok_last_good` | 五所齐全，806合约/77品种，source-date match 100%，critical errors 0，full_market_ready=true；10/1休市刷新失败不使last-good失效 |
| Market State | 9/2—9/30；10/1 18:57生成 | `ok_last_good` | 同合约1/3/5/20D、RV20、OI、curve可用；不冒充10/1或10/2境内行情 |
| Physical | requested/source 9/30；10/1 08:12生成 | `partial_native_frequency` | 20目标中18个按原生频率有效；SC/LU unavailable；无A/B exact-contract basis用于套利 |
| External(repo) | 10/1；19:02生成 | `ok_context_only` | 17/22 fresh、5 unavailable；与07:00海外收盘分层，不能称中国已交易 |
| Night Session | last-good trading_date 9/30、session_start 9/29 | `historical_last_good` | 属于9/30已完成阶段；10/1 holiday刷新未发布，不存在10/2新夜盘 |
| Options | 9/30；10/1 08:03 BJT可得 | `research_only` | 14,468记录、196 series；192 surface-ready、47 positioning-ready、0 execution-ready；bid/ask=0 |
| Contract metadata | 9/30 | `partial` | effective match 73.45%；乘数/tick/margin/limit覆盖30.15%，LTD覆盖67.49%；缺失参数不推断 |

Night质量闸门：仓库状态文件的10月1日holiday run为`data_fresh=false / validation_passed=false / published=false / coverage_complete=false`，0个night contract、214 query/unresolved，且`previous_valid_snapshot_retained=true`。可使用的最近合法last-good仍是trading_date=2026-09-30、night_session_date=2026-09-29、generated_at=2026-09-30 08:01:30，423合约/37品种；它只作历史价格发现分解。本期`night_session_fallback=false`，因为假日期间本就没有应得新夜盘。

Options四级readiness：chain成功42/64预期品种（coverage 65.63%）；surface 192/196 series；positioning 47/196；execution 0/196；IV覆盖98.84%、OI覆盖68.88%、bid/ask覆盖0，dealer Gamma方向未知。DCE期权18个品种被跳过，CJ/PL/ZC/A失败，故相关期权结论为缺失，不是“无机会”。

交易日历：SHFE/INE官方通知确认10月1—7日休市，10月8日08:55—09:00集合竞价并恢复日盘，当晚恢复连续交易；GFEX同样10月8日恢复。来源：[SHFE](https://www.shfe.com.cn/eng/CircularNews/Circular/202609/t20260921_833508.html)、[INE](https://www.shfe.cn/eng/CircularNews/Circular/202609/t20260921_833510.html)、[GFEX](https://www.gfex.com.cn/en/Notices/202601/ecd5e39ce8a04d2eb0a88d47ba2abd26.shtml)。

## 三、商品仪表盘（展示12项；境内列均为9月30日历史锚）

| 板块/品种 | 具体合约 | EOD close/settle | 1D/5D | Volume/OI/ΔOI | EOD curve；basis/Physical | 最近合法Night close；vs close/vs settle；ΔOI | 07:00海外新增 | Options | 信号 |
|---|---:|---:|---:|---:|---|---|---|---|---|
| 橡胶 RU | RU2701 | 20095/19710 | +3.52%/+3.96% | 513683/150478/+18323 | back +0.237%；无A/B；泰国降雨与青岛库存周降为支持 | 19665；+3.45%/+3.28%；+11873 | 油价强，但无新的exact SICOM收盘核验 | surface+position yes；exec no | 最强存量候选；复市等45m |
| 橡胶 NR | NR2612 | 17390/17000 | +3.53%/+5.56% | 86314/80028/+4484 | back +0.293%，z1.86；无A/B | 代表为NR2611，不可比 | 同上，仅方向代理 | surface yes；position/exec no | 不用NR2611替代正式合约 |
| 橡胶 BR | BR2611 | 16000/15870 | +3.12%/+6.58% | 288172/51622/-4127 | back +1.134%；原油只作成本代理 | 16155；+4.50%/+4.97%；+8194 | Brent/WTI上行支持成本端 | surface yes；exec no | 日盘较Night回吐，次选 |
| 油脂 OI | OI701 | 10230/10217 | +1.72%/-0.25% | 272992/283749/+9681 | back +1.820%；无A/B | 10234；+1.76%/+1.89%；+6681 | 油籽缺新的可核实收盘增量 | surface yes；position/exec no | 强势守住但需复市确认 |
| 原油 SC | SC2611 | 711.0/696.1 | -2.90%/-2.93% | 175510/24979/-4690 | contango -0.057%，z-1.78；Physical unavailable | 705.2；-0.94%/-1.63%；-1162 | Brent102.31(+4.37%)，WTI92.87(+2.71%) | surface yes；exec no | 境外反向增量最大；高gap风险 |
| 燃料油 FU | FU2611 | 4434/4376 | -0.95%/+4.59% | 663508/126742/-23873 | back +30.142%，z2.01；现货仅context | 4373；-1.46%/-1.02%；-5144 | 中国暂停多数成品油出口强化产品紧张 | surface yes；exec no | 曲线强/价格弱；先验补涨，不追首跳 |
| 沥青 BU | BU2611 | 5013/5091 | -2.00%/-0.29% | 880746/155550/-53419 | back +12.610%；无A/B | 5142；-1.98%/-1.02%；-24314 | 原油涨而国内节前弱 | surface+position yes；exec no | 等45m辨别补涨或需求压制 |
| 黄金 AU | AU2612 | 910.58/905.04 | +0.80%/-3.75% | 184362/225591/-229 | contango -0.248%；无A/B | 905.02；+0.69%/+0.61%；同约ΔOI未采用 | 现货金4165.29，+0.2%；美元/高利率反对 | surface yes；exec no | 信用主题未形成新方向优势 |
| 白银 AG | AG2612 | 14980/14928 | +0.15%/-7.41% | 273904/283220/+6039 | contango -0.215%；无A/B | 14958；+0.74%/+0.15%；同约ΔOI未采用 | 现货银60.51，+0.2% | surface yes；exec no | 高波动，缺境内重报价 |
| 铜 CU | CU2611 | 109680/109570 | +0.25%/-1.03% | 69830/185404/+183 | back +0.730%，z1.95；现货仅context | 无完整同约分解 | LME铜约14351.5美元/吨、美元偏强 | surface yes；exec no | 曲线支持但外盘偏弱，等复市价差 |
| 碳酸锂 LC | LC2701 | 118420/118820 | -0.60%/-10.77% | 160461/412703/-2984 | back +0.435%；仓单carried且stale | 无可核实同约Night | 无exact海外代理 | exec no | 弱势但无新实体确认，不追空 |
| 苹果 AP | AP701 | 6854/6834 | -1.75%/-3.15% | 141807/142083/+4066 | back +9.376%，z1.89；无实体确认 | 无夜盘 | 无直接海外映射 | surface yes；exec no | 价跌仓增与backwardation冲突 |

## 四、相比上一期真正变化

1. **能源增量最重要**：Brent 12月合约收102.31美元/桶、日涨4.37%；WTI收92.87、涨2.71%。支持因素是中国炼厂暂停对港澳以外多数成品油出口，以及美国向中东增派兵力的报道；这提高SC/FU/BU在10月8日的累计gap风险，不等于它们已经上涨。[Reuters，2026-10-01](https://www.reuters.com/business/energy/oil-prices-barely-changed-investors-assess-us-iran-peace-talks-gulf-exports-2026-10-01/)
2. **能源最强竞争解释仍在**：海湾原油出口逐步恢复，原油并非单向短缺；真正更紧的是柴油/成品油。因此“多成品油裂解”研究逻辑强于机械追SC，但国内exact-contract跨品种比率、乘数与当前报价缺失，暂不能列可执行RV。
3. **美元与长端利率没有给贵金属宽松环境**：美元仍在高位，全球债券抛售令美债10年期一度触及2002年以来高位；黄金仅小涨0.2%至4165.29美元，未出现对高利率的新增突破确认。[Reuters美元/债券，2026-10-01](https://www.reuters.com/world/africa/dollar-gets-lift-higher-yields-2026-10-01/)；[Reuters黄金，2026-10-01](https://www.reuters.com/world/india/gold-inches-higher-softer-us-inflation-dims-october-fed-hike-bets-2026-10-01/)
4. **宏观催化更偏“通胀而非需求崩塌”**：美国9月ISM制造业PMI 54.5，投入价格指数升至77.9；初请失业金19.7万。它支持高油价/高美元的宏观组合，也增加今晚美国非农造成利率与金属二次重定价的概率。[Reuters，2026-10-01](https://www.reuters.com/business/us-manufacturing-steady-september-input-prices-increase-2026-10-01/)
5. **中国层无变化**：没有10月1或10月2 EOD/Night/Options新截面，所有国内分数变化仅来自海外催化或证据权重调整；不把holiday pipeline失败写成行情缺失。

旧建议台账：相对10月1晨报，9月30 EOD已在10月1晚报补齐，故采用10月1晚报作为最近跨版对照、10月1晨报作为上一同版。RU、OI、BR idea_id保持不变；能源idea_id保持不变但因Brent收盘上冲而从64升至74；AP保持55。没有成交反馈，不假设用户持仓；所有“继续/退出”均仅适用于此前已按条件建立者，而本台账没有证据表明条件已成交。

## 五、产业链地图

| 产业链 | 方向与强弱 | 价格/Night/curve | 实体、期权、海外 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|
| 原油—燃料油—沥青 | **海外最强，境内待补价** | SC/FU/BU节前偏弱；FU/BU backwardation强，价格与曲线冲突 | 成品油出口暂停与Brent突破支持；期权exec=0 | 10/8中国重报价、裂解精确腿比、SC/LU physical | 中高研究、零执行 |
| 天然橡胶—20号胶 | **境内存量最强** | RU/NR价涨仓增且backwardation；RU夜盘后日盘继续+2.19% | 库存周降/天气支持；RU IV-RV为正不便宜 | 假期SICOM exact close、当前bid/ask、RU参数 | 中高 |
| 油脂油料 | OI相对强、豆系不确认 | OI夜盘涨幅日盘守住；curve偏back | 期权call skew偏贵；海外油籽本期无新可核实收盘 | A/B basis、DCE期权、10/8棕榈/豆油联动 | 中 |
| 贵金属—美元—实际利率 | 方向优势不足 | AU/AG节前弱势，curve不支持追多 | 金银小涨但美元/利率反对；黄金信用主题未获新增确认 | 中国重报价、实际利率最新精确值 | 中低 |
| 黑色—地产—航运 | 整体无高质量新异常 | EC曲线样本仅2个；黑色无假期新增 | DCE期权缺失，海外映射不完整 | 日盘、实体库存/利润和DCE options | 低 |

## 六、机会排行榜（分数是研究排序，不是胜率或仓位）

| 排名 | idea_id / 方向 / 周期 | 逻辑25 | 赔率25 | 催化20 | price/curve/vol15 | 拥挤技术15 | 总分 | 有效支持层；反证/缺失 | 研究判断 / 证据 / 执行 |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | `COM-E-RU2701-RUBBER-TIGHTNESS-20261001` 多RU2701，1—5D | 22 | 16 | 16 | 13 | 9 | **76** | 1价格/OI、2曲线、3实体、4境外；IV>RV、长假gap、参数与bid/ask缺 | 存在待验证优势 / 充分 / **休市，等10/8触发** |
| 2 | `COM-E-ENERGY-POSTEIA-20260930` 能源产品紧张/SC补价，1—10D | 21 | 16 | 18 | 11 | 8 | **74** | 2曲线、3产品供给、4海外；中国价格反向、海湾出口恢复、精确腿比缺 | 存在待验证优势 / 部分 / **休市，待重报价** |
| 3 | `COM-E-OI701-RELSTRENGTH-20260930` 多OI701，1—5D | 19 | 15 | 13 | 11 | 10 | **68** | 1价格/OI、2曲线；海外油籽/实体和A/B basis不足 | 存在待验证优势 / 部分 / **休市，等待触发** |
| 4 | `COM-E-BR2611-RELSTRENGTH-20260930` 多BR2611，1—5D | 18 | 14 | 13 | 9 | 9 | **63** | 1价格、2曲线；日盘回吐、仓减，实体与报价缺 | 存在待验证优势 / 部分 / **休市，次选** |
| 5 | `COM-E-AP701-DOWNSIDE-20261001` 空AP701观察，1—10D | 15 | 11 | 9 | 10 | 10 | **55** | 1价格/OI；backwardation反对，实体/期权缺 | 证据不足 / 不足 / **研究观察** |

分项均未超上限，复算分别为76、74、68、63、55。RU与能源具备至少3个独立支持层，达到70分资格；OI/BR/AP按支持层上限压分。相较前期：RU +1来自海外油价对合成胶成本的温和支持；能源 +10来自Brent收盘与成品油出口催化；OI +2来自不确定性下降而非新增行情；BR +1；AP不变。

## 七、前三名交易卡（均为休市研究卡，不是当前订单）

### 1. RU2701多头延续

- **事实**：9/30 close/settle 20095/19710；Night OHLC 19080/19780/19040/19665，vs close +3.45%、vs settle +3.28%，Night ΔOI +11873；日盘相对Night +2.19%。价格、OI、curve与实体/海外四层支持。
- **市场可能隐含/我们的分歧**：市场可能已计入短期降雨与库存下降；分歧是供应扰动若延续，backwardation和仓量可能使强势多维持1—5日。最强反证是长假后供应预期修复、SICOM回落或>5%跳空透支。
- **最佳表达**：RU2701期货；期权仅备选为同到期35—45 Delta call spread，因execution_ready=false不得指定权利金。两腿期权配比1:1；未取到当前bid/ask前不成交。
- **入场/好中坏成交**：10/8等45分钟；好=回踩20095附近守住且curve不塌，试仓0.25% NAV风险；中=突破首45分钟高点后回测确认，风险≤0.50%；坏=>5%高开或价涨仓减且近月转contango，放弃。20095为节前技术锚，不是实时信号。
- **止损/失效/退出**：期货计划止损为跌破19710并在30分钟内不能收复；逻辑失效为RU近月转contango且SICOM/NR同时走弱。TP1 20500减1/3，TP2 21000再减1/2，余仓2个交易日无扩张退出；时间止损5日。期货最大损失不有限，止损风险不等于结构最大损失。
- **参数/交割**：multiplier、tick、tick value、margin、price limit、night session参数未确认；LTD 2027-01-15。notional及1/2涨跌停压力损失无法可靠计算；交割风险当前中低，进入交割月前至少10个交易日滚动。最坏情景是长假gap、涨跌停和流动性消失。

### 2. 能源产品紧张—SC2611补价观察

- **事实**：SC2611 9/30 close/settle 711.0/696.1，Night 705.2，vs close -0.94%、vs settle -1.63%，Night ΔOI -1162，日盘相对Night +0.82%；而10/1 Brent收102.31、+4.37%，WTI收92.87、+2.71%。海外是新增信息，不是中国已交易价格。
- **市场可能隐含/我们的分歧**：节前SC定价偏弱，市场隐含海湾出口恢复；新增分歧是成品油出口限制和中东军事风险提高产品/原油风险溢价。竞争解释是原油供应恢复足以压制持续涨幅，真正短缺只在柴油。
- **最佳表达**：若只能单腿，SC2611仅作条件多头；理论上FU/SC相对价值更贴近产品紧张，但缺乘数、beta与同刻报价，不能定义可执行basket。
- **入场**：10/8不得首跳追价，等45分钟。仅当Brent仍>100美元、SC守住首45分钟区间中位并上破区间高点，才以0.25%—0.50% NAV计划止损风险试仓。好=小幅高开后回踩；中=区间突破；坏=>5%跳空或Brent跌回98以下，放弃。
- **止损/退出**：止损为跌破首45分钟低点；逻辑失效为海湾出口继续恢复且柴油裂解显著回落。TP1按入场价+1R减1/3，TP2 +2R再减1/2；3日无扩张退出，最长10日。合约乘数/tick/margin/limit未确认，LTD 2026-10-30，交割风险高于RU；不持有进入最后交易日前5个交易日。1/2涨跌停压力损失待参数。

### 3. OI701相对强势

- **事实**：9/30 close/settle 10230/10217；Night 10057/10256/10051/10234，vs close +1.76%、vs settle +1.89%，Night ΔOI +6681，日盘相对Night -0.04%；EOD ΔOI +9681，backwardation +1.82%。
- **分歧/反证**：市场可能已计入短期油脂偏紧；我们的分歧是强势被日盘完整保留，若复市跨油脂相对强度仍在可延续。反证是中国大豆需求偏弱、海外豆油/棕榈未确认、无A/B基差。
- **最佳表达**：OI701期货；备选OI701同到期35—45 Delta call spread 1:1，但ATM IV15.26%、RR25 +3.92，call skew偏贵且exec=false，期货暂优于期权。
- **入场/退出**：10/8等60分钟；仅在价格守住10230且OI/Y/P相对收益为正时试仓。好=回踩10230；中=首小时高点突破；坏=>2%高开或Y/P更强，放弃。止损10050；TP1 10450、TP2 10700；3日无扩张退出，最长5日。
- **参数/压力**：multiplier 10吨/手、tick 1元/吨、tick value 10元；参考保证金9%、涨跌停8%、LTD 2027-01-14。以10230计名义102,300元、参考保证金9,207元；1/2个涨跌停压力约8,184/16,368元每手。期货最大损失不有限；交割月前10个交易日滚动。

## 八、商品期权专项

- RU2701（12/25到期）ATM 19750、ATM IV27.94%、RR25 +1.91、BF25 +0.24；RV20 22.25%，IV-RV +5.69个百分点。方向若看多，call spread优于裸call，但旧IV不能替代10/8报价。
- OI701（12/11到期）ATM 10200、ATM IV15.26%、RR25 +3.92、BF25 +0.64；RV20 14.24%，IV-RV +1.02。call skew偏贵，暂不证明期权便宜。
- BU2611 IV50.59%、RR25 -4.81；FU2611 IV68.10%、RR25 -3.42。高IV与负RR仅说明尾部定价，不足以证明买put或卖vol有优势。
- Event convexity：今晚20:30美国非农可引发美元、利率、金银与铜波动，但中国期权休市，无法在国内提前建立有限损失结构。境外工具若使用，最大净支出必须≤单笔NAV 0.25%—0.50%，并以实时双边价为前提。
- 回避：所有execution_ready=false的中国期权、DCE缺失期权、用OI推断dealer Gamma、把T-1 IV当当前成交IV、未核实交割方式的深度虚值合约。

## 九、9:00开盘风险地图（当前休市）

三层严格分开：①Previous China EOD=9/30；②Current Trading Day Night Session=不存在（国庆休市；最近Night仅属9/30历史）；③07:00 Overseas=Brent/WTI已完成10/1收盘，金银小涨，美元/利率偏强。下一实际日盘为10/8。

| 品种 | 10/8潜在开盘 | 海外与境内 | 是否追价 | 等待 | 开盘后确认 |
|---|---|---|---|---|---|
| SC/FU/BU | 偏高开，幅度高度不确定 | 海外油强、境内节前弱，冲突最大 | 否 | 45分钟 | Brent是否守100、SC/FU曲线、OI与裂解 |
| RU/NR/BR | 偏高或高位震荡 | 境内已强；油价支持成本但假期橡胶路径未核实 | 否 | 45分钟 | SICOM/NR同步、RU backwardation、价仓同向性 |
| OI/Y/P | 平至偏高 | OI节前强，海外油籽新增不足 | 否 | 60分钟 | OI相对Y/P、前后月、OI变化 |
| AU/AG | 平开方向不明 | 金银小涨，但美元/利率反对 | 否 | 30分钟 | USD/CNH、实际利率、金银比、curve |
| CU/AL | 平至偏低 | LME偏弱、美元偏强 | 否 | 30分钟 | LME/SHFE比、现货升贴水、curve |
| AP/LC/EC | 不作方向预判 | 缺可靠海外映射 | 否 | 30—45分钟 | 实体/库存、OI、首日curve；EC排除roll错觉 |

## 十、未来24小时与7日事件日历（北京时间）

| 时间 | 事件 | 受影响 | 处理 |
|---|---|---|---|
| 10/2 20:30 | 美国9月非农、失业率、工资；BLS官方8:30 ET发布 | 美元、实际利率、AU/AG/CU、油 | 中国休市；境外仅用有限损失结构，数据后15—30分钟再决策。[BLS](https://www.dol.gov/newsroom/economicdata/empsit_09042026.pdf) |
| 10/3 03:30 | CFTC COT通常周五15:30 ET发布，反映周二持仓 | 能源、金属、农产品 | 只作拥挤度背景，不把会员/投机分类当方向确定性。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) |
| 10/4—5 | 泰国强降雨风险窗口（此前公开天气警示） | RU/NR/SICOM | 检查实际降雨与割胶影响；没有实测不重复加分 |
| 10/6 | EIA Short-Term Energy Outlook / Winter Fuels Outlook | 原油、柴油、天然气、裂解 | 关注库存/产量预测；Vega优先有限损失。[EIA](https://www.eia.gov/outlooks/steo/release_schedule.php) |
| 10/7 22:30 | EIA Weekly Petroleum Status Report，10:30 ET | SC/FU/BU/LPG | 中国复市前最后关键能源数据；若与Brent趋势冲突，取消追价。[EIA](https://www.eia.gov/petroleum/supply/weekly/) |
| 10/8 08:55/09:00；21:00 | 中国期货期权恢复集合竞价/日盘；当晚恢复夜盘 | 全市场 | 所有旧条件重新报价；先验触发无效，等15/30/45分钟 |
| 10/9 00:00 | USDA 10月WASDE，12:00 ET（落在7日边界） | 豆粕、油脂、玉米、小麦、棉糖 | 国内复市后隔夜事件；优先价差或有限凸性。[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report) |

OPEC月报在10月13日，超出7日窗口；不把它冒充本周催化。IEA具体月报时间未核实，不列精确时点。地缘与中东部署为非定时风险，能源仓位必须计入夜盘gap、涨跌停、保证金上调与流动性消失。

## 覆盖核对与未入榜板块

应覆盖：中国强制63个不同代码加动态合格品种；引擎Futures实际取数并分析77个品种（63+14动态：JR/PL/PM/RI/RS/WH/ZC/BZ/LG/RR/PD/PT/OP/WR），五所均在9/30 last-good。策略类别覆盖方向、curve/跨期、基差、跨品种/跨市场、期权方向与vol/skew、事件凸性、中性组合；周期覆盖1—5D、1—10D与至20D状态。真正可执行扫描为0，因为中国休市且Options execution为0。

| 板块 | 应覆盖/实际期货分析 | 数据不足 | 未入榜最值得跟踪异常或无异常依据 |
|---|---:|---|---|
| 黑色建材 | 9/9 | DCE期权链缺I/JM/J；实体与利润需复市更新 | 未见同时获price/curve/physical确认的方向；不交易节前单日波动 |
| 有色贵金属 | 12/12 | 当前境内报价、部分参数、期权执行 | CU curve偏back但美元/LME反对；AU/AG信用主题未形成优势 |
| 能源炼化化工 | 21/21 | SC/LU physical、exact crack比率、当前期权价 | FU/BU极端backwardation与节前弱价冲突，是能源榜外最重要RV线索 |
| 新能源 | 3/3及GFEX动态 | LC仓单stale、海外proxy缺失 | LC 5D -10.77%但价跌仓减、无实体确认，不追空 |
| 农产品油脂畜牧 | 强制范围全部期货 | DCE 18个期权跳过；CJ options失败；A/B basis缺 | OI入榜；RM偏强但curve与海外油籽不足，其他无多层异常 |
| 航运软商品 | EC/CF/CY/SR/AP/CJ/PK均分析 | EC curve仅2 obs；AP实体缺；CJ options失败 | EC 5D +7.62%但ΔOI -10.43%且curve不可用，不作趋势交易 |

未覆盖/不适用原因：不存在10/1—10/2中国EOD与Night是交易日历“不适用”，不是missing；DCE options和失败series为真实missing；SC/LU physical unavailable；A/B basis不足；bid/ask与model Greeks缺失。覆盖核对不能把“提到名字”视为完成分析，本期实际分析基于77品种同合约价格/OI/curve初筛，再对12个展示品种与5个候选下钻。

风险预算：休市阶段新增中国风险=0。复市试仓单笔计划止损风险NAV 0.25%—0.50%，确认后0.75%—1.50%，同因子能源或橡胶主题合并≤2.5%；压力覆盖1/2涨跌停、相关性破裂、流动性消失、假期gap、保证金上调、IV跳升/塌陷、交割挤压与人民币急变。

### 来源

- China-Commodities-Engine统一快照与状态文件，source dates 2026-09-30/10-01，支持境内EOD、Night、Options与质量结论。
- [Reuters：Oil jumps 4%](https://www.reuters.com/business/energy/oil-prices-barely-changed-investors-assess-us-iran-peace-talks-gulf-exports-2026-10-01/)，2026-10-01，支持Brent/WTI收盘、燃料出口与地缘催化。
- [Reuters：Gold edges up](https://www.reuters.com/world/india/gold-inches-higher-softer-us-inflation-dims-october-fed-hike-bets-2026-10-01/)，2026-10-01，支持金银价格。
- [Reuters：Dollar and bond selloff](https://www.reuters.com/world/africa/dollar-gets-lift-higher-yields-2026-10-01/)，2026-10-01，支持美元与利率背景。
- [Reuters：US manufacturing](https://www.reuters.com/business/us-manufacturing-steady-september-input-prices-increase-2026-10-01/)，2026-10-01，支持ISM与投入价格。
- SHFE/INE/GFEX、BLS、EIA、CFTC、USDA官方日历，链接见正文，支持交易与事件窗口。

A. 今天没有应立即建立的新仓位。
B. 今天没有可在中国市场生效的条件单；仅预备10月8日RU2701、SC2611、OI701重报价后的30—60分钟触发方案。
C. 今天应继续观察Brent能否守住100美元、柴油/燃料油裂解、SICOM与泰国降雨、RU/NR curve及美元—实际利率。
D. 今天必须避免或退出追逐不存在的中国假期报价、用旧IV下期权单、把海外涨幅等同境内已涨，以及无参数的跨品种伪套利。
