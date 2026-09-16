# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-16

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:40 BJT；信息截点：19:30；最近完整中国交易时段：9月16日日盘。今晚21:00连续交易归属9月17日交易日；EC、LC等无夜盘品种下一窗口为9月17日09:00。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；能源夜盘强势被日盘显著回吐，瓶片与豆粕出现日盘接力，但前者只有两层证据、后者curve反对，今晚只挂回撤确认单。**

当前regime：**中东供给风险仍高但原油边际弹性下降，亚洲柴油紧张与中国SC/FU/LU日盘回吐并存；聚酯成本传导分化，豆粕独立走强，FOMC前贵金属反弹而方向风险升高。**

最接近触发的是LU2611、FU2611与PR611。LU/FU缺少今晚对日盘回吐的重新吸收；PR缺少第三个独立支持层与当前期权报价。SC旧多逻辑因日盘反转且back降至旧失效阈值下方而停止新增。

## 二、数据质量与覆盖

本期读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按需下钻[9月16日逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)及期权曲面。

- 统一输入：schema v2，`requested_date=2026-09-16`，19:13:10生成。
- Futures：五所806合约、77产品，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0；7条placeholder排除。
- Market State：同合约1D/3D/5D/20D历史20个交易日完整；CU/NI等存在pair roll，相关curve不作稳定z-score。
- Physical：本次仍是9月15日输入，模块级`data_fresh=false/validation_passed=false/published=false`；18/20序列在各自日频上为最新last-good，SC/LU unavailable。所有basis为C级或不可用，仅作context，不计方向层。
- External：repo日频层17/22 fresh、5项unavailable，全部`context_only`；另以Reuters补充19:30前海外。repo WTI 98.79与Reuters主力104.63口径明显不一致，隔离repo WTI，不据此作跨市场套利；Brent约107.58—108.16。
- Options：9月16日采集因SSL握手超时失败；最新有效截面仍为9月15日18,936条、340个series、52/64产品，330个surface-ready、81个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖97.73%/69.60%/0。T日完整截面已应得而缺失，故T-1仅作历史背景，不计第五层。
- Metadata：partial；有效合约匹配73.45%，multiplier/tick/margin/limit约30.15%，last-trading-day约67.49%。前三卡逐一披露缺口。

Night状态：`trading_date=2026-09-16`、`night_session_date=2026-09-15`，05:58:52生成；`data_fresh=true`、`validation_passed=true`、`published=true`、`coverage_complete=true`。801个请求合约中587条有效、55个产品；204条合法outside-window、10条no-night-trade；missing timestamp/price/quote、query error、unresolved contract均为0，warnings为空。

这批Night属于今天已经完成的连续交易阶段，**不是今晚21:00未来行情**。本期对同一具体合约计算`day_follow_through=9月16日EOD close / Night close - 1`；代表合约不同者不硬算。

## 三、商品仪表盘

1D/5D均为9月16日同合约结算收益；curve为near-minus-next期货结构，不是现货基差。S/P/E为最新有效9月15日期权截面的surface/positioning/execution readiness。

| 板块/品种 | 合约；close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical/basis | 早前Night close；vs close；日盘续涨 | 19:30海外；S/P/E；21:00信号 |
|---|---|---|---|---|---|
| 原油SC | SC2611；827/838.4；+0.26%/+22.56% | 24.08万/4.15万/+1,704；back 6.32% | 缺失 | 860；+2.55%；**-3.84%** | Brent 108附近；N/N/N；旧多失效 |
| 低硫燃油LU | LU2611；5673/5687；+1.12%/+10.06% | 16.35万/6.92万/+625；back 2.81% | 缺失 | 5793；+2.73%；**-2.07%** | 亚洲柴油裂解创高；无可靠series；回撤确认 |
| 燃料油FU | FU2611；4488/4493；+0.25%/+14.21% | 99.38万/21.41万/+2,116；back 18.14%、z2.11 | 9/15 C/context | 4551；+1.68%；**-1.38%** | 产品紧张；Y/N/N；恢复型条件 |
| 瓶片PR | PR611；8646/8570；+3.18%/+8.34% | 15.81万/6.91万/+4,770；back 2.40%、z1.57 | 缺失 | 8592；+2.19%；**+0.63%** | 原油回落；Y/Y/N；不追高 |
| PX | PX611；9650/9692；+2.13%/+7.09% | 49.49万/17.73万/+12,172；back 0.97% | 9/15现货9600，C | 9756；+2.50%；**-1.09%** | 油价高位回落；Y/N/N；等45m |
| PTA | TA701；6556/6520；+1.31%/+6.09% | 208.21万/117.31万/+3,752；back 3.44% | 9/15现货7045，C | 6532；+1.11%；**+0.37%** | 成本链混合；Y/Y/N；看breadth |
| 苯乙烯EB | EB2611；9961/9992；+1.20%/+4.66% | 52.61万/26.18万/+28,085；curve -0.62%、z-1.98 | C/context | 代表EB2610，不分解 | 上游偏强；Y/Y/N；换月限制 |
| 豆粕M | M2701；3479/3434；+1.78%/+1.09% | 171.44万/288.996万/+174,015；contango 1.10% | 9/15现货3382，C | 3414；+0.86%；**+1.90%** | CBOT豆粕351.6；Y/Y/N；等回撤 |
| 镍NI | NI2611；122240/122060；-1.78%/-4.33% | 11.10万/12.96万/+6,040；roll、轻contango | 缺失 | 代表NI2610 -2.36%，不分解 | LME约16250；N/N/N；反抽失败空 |
| 铜CU | CU2610；107740/107430；+0.47%/-3.32% | 7.99万/16.54万/-14,719；roll、back 0.31% | 9/15现货107675，C | 107200；+0.16%；**+0.50%** | LME约14227.5；N/N/N；旧空降级 |
| 黄金AU | AU2612；940.52/934.2；+0.32%/-1.91% | 8.49万/17.79万/+8,727；轻contango | C/context | 代表合约不同 | 现货金约4346、+1.3%；失败产品；不跨FOMC |
| 白银AG | AG2612；15832/15653；+1.25%/-3.25% | 12.79万/20.43万/+1,580；roll | C/context | 代表合约不同 | 银约64.54、+1.4%；失败产品；不追 |
| 玻璃FG | FG701；910/910；-1.30%/-6.19% | 104.96万/130.57万/+68,443；back 3.27% | 9/15现货1008，C | 908；-0.11%；+0.22% | 无exact外盘；Y/Y/N；弱价强curve冲突 |
| 碳酸锂LC | LC2701；125820/126380；-2.51%/-11.03% | 21.31万/41.75万/-1,204；back 0.49% | 9/15现货131000，C | 制度无Night | 无exact外盘；Y/N/N；不追空 |
| 集运EC | EC2610；2080/2050；-0.89%/+6.11% | 0.93万/2.39万/-482；back 28.71% | exact运价缺 | 制度无Night | 航道风险仍在；N/N/N；旧多不恢复 |

海外新增：Reuters 17:26 BJT附近报价为Brent 108.16、WTI 104.63，较当日早段回落，原因是沙特通过阿曼Sohar增加装船且API显示原油库存+710万桶；这反对把中国能源日盘回吐直接视为低风险买点。[Reuters油市](https://www.reuters.com/business/energy/oil-falls-us-crude-inventories-rise-despite-saudi-supply-concerns-2026-09-16/)

但亚洲10ppm柴油裂解超过87美元/桶、创纪录，近月月差超过11美元/桶，说明产品端紧张尚未消失；它支持产品链研究，却不是LU/FU exact可套利价差。[Reuters亚洲柴油](https://www.reuters.com/business/energy/asia-diesel-refining-margins-record-high-more-than-87-barrel-data-shows-2026-09-16/)

## 四、相比上一交易日/今晨真正变化

1. **SC由“夜盘确认”转为日盘反转。** Night收860，EOD收827，日盘-3.84%；back由7.71%降至6.32%，跌破旧卡6.5%失效锚。虽全日OI +1,704，但只作归因线索，旧多停止新增。
2. **LU/FU也未把夜盘涨幅保住。** 日盘相对Night close分别-2.07%/-1.38%；但全日OI转为+625/+2,116且curve仍back，故从趋势多降为恢复型条件多，而非反向做空。
3. **PR成为最清晰的日盘接力。** Night +2.19%后日盘再+0.63%，结算+3.18%、OI +7.42%、curve z=1.57；但只有价格量仓与curve两层，严格封顶69。
4. **M2701出现独立农产品强势。** Night +0.86%后日盘+1.90%，收在日高、OI +17.40万；contango 1.10%与C级现货反对把它升格为确认交易。
5. **CU/贵金属反转，宏观交易等待FOMC。** CU日盘较Night +0.50%，AU/AG中国收盘反弹；海外金银同步上涨，但02:00决议前不把信用主题判为成立。
6. **T日期权失败。** 9月15日曲面仍可作历史背景，但能源/PR/M底层已大幅移动，moneyness、Delta和IV-RV不可直接外推为今晚报价。

旧建议台账：

- `COM-E-SC2610-GAP-20260905`：85→66；继续映射SC2611，但因日盘反转、back跌破6.5%和阿曼替代装船而停止新增。若此前已按条件建立，按旧失效规则退出或至少降至零新增风险；未有成交反馈，不假设持仓。
- `COM-M-LU2611-PRODUCT-RELATIVE-20260915`：81→75；Night强、日盘回吐，亚洲柴油实体代理支持但不是exact LU价差，触发改为恢复确认。
- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：80→73；Night强、日盘回吐，curve扩大与全日OI转增保留候选。
- `COM-C-PR611-POLYESTER-PASS-20260916`：首次提出；只列两层证据重点观察，不冒充70+。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：69→55并退出正式榜；日盘和LME反弹、OI下降，不再保留趋势空条件。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：继续退出；9月16反弹不恢复旧卡。

## 五、产业链地图

- **最强可验证日盘：PR—TA—PX聚酯成本链，偏多但分化，置信度中。** PR/TA有日盘follow-through，PX回吐；价仓和curve支持，原油15:00后回落反对追高，缺加工利润、A级现货与可执行期权。
- **能源SC—FU—LU：存量紧张、边际价格弹性下降，置信度中。** 三者夜盘上涨后日盘全回吐，SC最弱；FU/LU back及亚洲柴油紧张支持恢复型机会，阿曼替代装船与API库存是竞争解释。
- **农产品：M/RM偏强，C与油脂混合，置信度中低。** M价仓强但contango，RM上涨而curve同样偏弱；缺高质量basis和进口平价，不能构造伪跨市场套利。
- **最弱：NI/SS与LC—FG，置信度中低。** NI/SS价跌仓增仅是线索且roll限制curve；LC跌势获价格支持但OI下降、back与C级现货反对追空；FG弱价与back冲突。
- **贵金属—有色：FOMC前反弹，置信度低。** 海外金银、LME铜回升反对旧空；黄金信用主题有财政/地缘支持，但利率决议风险尚未闭环。AI现金流/Capex未形成可识别商品定价优势。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | LU2611产品紧张恢复多 | 22/15/18/12/8 | **75** | 1、2、4 | 存在待验证优势｜部分、日盘反证｜等21:30—21:45 |
| 2 | FU2611深back恢复多 | 22/14/18/12/7 | **73** | 1、2、4 | 存在待验证优势｜部分、日盘反证｜等21:30 |
| 3 | PR611聚酯传导多 | 20/16/14/11/8 | **69** | 1、2 | 存在待验证优势｜部分｜等待回撤/第三层 |
| 4 | NI2611弱势延续空 | 18/16/14/10/11 | **69** | 1、4 | 存在待验证优势｜部分、roll/合约错位｜反抽失败才空 |
| 5 | M2701豆粕强势观察 | 17/14/12/8/8 | **59** | 1 | 证据不足｜不足、curve反对｜等待basis/海外确认 |

分项均已复算。PR/NI只有两层，封顶69；M只有一层，封顶59。LU/FU共享产品与运输因子，不能叠加满额；所有期货最大损失均不由计划止损限定。

## 七、前三名交易卡

### 1. LU2611｜恢复型条件多｜75

**事实：** T日OHLC=5553/5846/5470/5673，结算5687；1D +1.12%、5D +10.06%，ΔOI +625，back 2.81%。早前Night OHLC=5553/5797/5470/5793，vs close +2.73%、vs settlement +3.00%、Night ΔOI +5,399；日盘follow-through **-2.07%**。

- 市场隐含：产品紧张仍在，但Night大部分涨幅被日盘兑现。分歧：亚洲柴油裂解纪录高位可能让低硫产品强于原油；最强竞争解释是柴油并非LU exact标的，且沙特替代装船缓解原料风险。
- 最佳表达：LU2611单腿条件多，1手为一单位；不以柴油裂解构造伪套利。
- 好成交：21:30—21:45在5580—5660承接并重上5685/VWAP，先1/3仓。
- 中成交：突破5800后回踩5760—5800不破，仓位减半。
- 坏成交：直接高于5860、滑点超过计划1R的20%或深度不足，放弃。
- 止损：30分钟接受5530下方；逻辑失效为跌破5470、back低于1.5%、Brent跌破104或LU继续弱于FU。
- 退出：TP1 5800或+1.5R；TP2 6000或+3R；1—3D无扩张退出。
- 风险：0.15%—0.25% NAV；与FU合并初始≤0.35%。计划止损不代表最大损失有限。
- 参数：repo仅确认最后交易日10月30日、最后交割日11月6日；multiplier、tick、tick value、动态margin/limit及官方夜盘参数未由本次元数据确认，**参数补齐前不得实际下单**。今晚预计有Night，仍以交易所当日安排为准；实物交割，10月中旬前复核移仓。
- 压力：因动态参数不完整，不编一板/两板金额；最坏情景包括阿曼替代供应扩大、夜盘低开、流动性消失与保证金上调。

### 2. FU2611｜恢复型条件多｜73

**事实：** T日OHLC=4400/4606/4350/4488，结算4493；1D +0.25%、5D +14.21%，ΔOI +2,116，back 18.14%、z=2.11。早前Night OHLC=4400/4564/4350/4551，vs close +1.68%、vs settlement +1.54%、Night ΔOI +14,860；日盘follow-through **-1.38%**。

- 市场隐含：深back计入近端供给紧张，但日盘拒绝Night高位。分歧是产品端紧张可能比原油持续；反证是FU不是柴油、15:00后油价回落且Night仓增未全部保留。
- 好成交：21:30后4410—4470承接并重上4495/VWAP，且FU/LU不再走弱，先1/3仓。
- 中成交：突破4608后回踩4560—4600成功，仓位减半。
- 坏成交：直接高于4660或滑点过大，放弃。
- 止损：30分钟接受4380下方；失效为跌破4350、back低于15%、Brent低于104或产品相对SC继续走弱。
- 退出：TP1 4605或+1.5R；TP2 4750或+3R；1—3D时间止损。
- 风险0.15%—0.20% NAV；若LU触发，FU不得独立叠加满额。
- 参数：SHFE产品规则确认10吨/手；按惯例tick 1元/吨、tick value 10元，结算名义44,930元，但动态margin/limit须按9月11日后调整再核验。repo确认最后交易日10月30日、最后交割日11月3日；实物交割，10月中旬前移仓。[SHFE燃料油合约](https://www.shfe.com.cn/eng/Market/Futures/Energy/fu_f/ContractText/)
- 压力：一板=`44,930×L`；两板=`44,930×[1-(1-L)^2]`，L下单前核实，不能把计划止损写成有限损失。

### 3. PR611｜回撤条件多｜69

**事实：** T日OHLC=8340/8744/8248/8646，结算8570；1D +3.18%、5D +8.34%，ΔOI +4,770，back 2.40%、z=1.57。早前Night OHLC=8340/8620/8248/8592，vs close +2.19%、vs settlement +3.44%、Night ΔOI +3,835；日盘follow-through **+0.63%**。

- 市场定价：油价与聚酯成本上移已部分进入瓶片。分歧是PR比PX/TA更能保持日盘接受；竞争解释是短期成本挤压并不等于下游需求或利润改善。
- 好成交：21:30后8500—8600承接并重上8650/VWAP，先1/3仓。
- 中成交：突破8745后回踩8700—8745不破，仓位减半。
- 坏成交：直接高于8840或PX/TA同步转弱，放弃。
- 止损：30分钟接受8440下方；失效为跌破8248、back低于1%、PX/TA转负且原油跌破104。
- 退出：TP1 8750或+1.5R；TP2 9000或+3R；1—3D无新增实体确认退出。
- 风险0.15%—0.20% NAV；因只有两层支持，不升级为确认交易。
- 参数：15吨/手、tick 2元/吨、tick value 30元；结算名义128,550元。repo基础margin 7%、limit 6%，但当日动态参数仍需下单前核验；最后交易日11月13日、最后交割日11月18日，实物交割，10月底前移仓。
- 压力：按6%基础限幅，一板约7,713元/手、两板复合约14,963元/手；相关性破裂时PR可与PX/TA脱钩。

## 八、商品期权专项

9月16日T日期权采集失败；下表为**9月15日最新有效但已落后于应得T日的历史截面**。本期底层价格已变化，只能判断旧波动结构，不能作为今晚可成交报价或第五层证据。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 71.45%/42.49% | +28.96vol | -3.38/+0.13 | Y/N/N | event vol仍贵，底层已变 |
| PX611/09-28 | 44.43%/31.44% | +12.99vol | +1.84/+0.39 | Y/N/N | 近到期、Delta待重算 |
| TA701/12-11 | 35.39%/26.18% | +9.20vol | +3.41/+1.39 | Y/Y/N | 上行偏度已贵 |
| PR611/10-13 | 27.03%/27.65% | -0.63vol | -19.27/+3.07 | Y/Y/N | 极端RR需先排查数据/重报价 |
| FG701/12-11 | 21.80%/25.69% | -3.89vol | +5.45/+1.98 | Y/Y/N | IV<RV不单独证明便宜 |
| M2701/12-16 | 14.04%/11.61% | +2.43vol | +4.17/+1.91 | Y/Y/N | 今日日盘上冲后不可沿用Delta |
| LC2701/12-07 | 44.99%/39.03% | +5.96vol | +1.84/+1.49 | Y/N/N | 无Night、实体不足 |

当前没有可证明优于裸期货的期权结构。若取得实时双边报价，可研究FU2611牛市call spread或PR611有限净支出call spread，但执行价、Delta、最大净支出、盈亏平衡、Greeks、滑点与行权交割均须重算；Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、21:00夜盘风险地图

四层严格区分：①9月16日中国EOD；②属于9月16交易日的已完成Night；③15:00—19:30海外新增；④今晚21:00尚未发生、归属9月17日。

| 品种 | 早前Night→日盘→海外 | 21:00判断 | 追价/等待 | 开盘确认 |
|---|---|---|---|---|
| LU | +2.73%→-2.07%→柴油裂解纪录、原油回落 | 平/小高开，方向冲突 | 不追；30—45m | 5530/5660/5685/5800、LU/FU |
| FU | +1.68%→-1.38%→产品紧、原油回落 | 平开倾向 | 不追；30m | 4380/4470/4495/4608、back |
| SC | +2.55%→-3.84%→Brent回落、阿曼替代装船 | 低/平开，旧多失效 | 不接首刀；45m | 811/827/838、back6.5% |
| PR/TA/PX | PR/TA日盘接力、PX回吐→原油回落 | 小高/平开分化 | 30—45m | PR8600/8650、TA6530、PX9750 |
| EB/EG | 主力错位；EG涨但减仓21.7% | 高波动、回吐风险 | 45m | exact主力、OI、curve |
| M/RM | Night强→M日盘+1.90%→CBOT偏强 | 偏高，但contango | 45m | M3414/3479、RM2320、basis |
| NI/SS | 夜弱→日盘仍弱→LME镍约16250 | 低/平开 | 不追空；30—45m | NI121000/122500、roll |
| CU/AL/ZN | 夜盘混合→日盘反弹→LME偏强 | 小高开 | 不追；30m | CU107200/107870、LME、CNH |
| AU/AG | 代表合约错位→中国反弹→海外金银+1% | 偏高但FOMC前脆弱 | 30—45m | DXY、10Y、02:00风险 |
| FG/SA | Night近零→日盘偏弱 | 平/低开 | 不追空；30m | FG905/914、SA1007/1021、curve |
| EC/LC/AP/JD/SF/SM/SI/PS | 无制度Night | 今晚不交易 | 9月17日09:00后30—45m | 量仓、curve、实体 |

21:00最不值得交易的是接SC第一刀、追PR/M第一跳、低开追NI/LC/FG，以及任何未重报价的期权。人民币/美元同一时点exact USD/CNH仍不可得；不编进口成本贡献率。

## 十、未来24小时与7天事件

- 9月16日21:00：下一合法Night，归属9月17日；能源与聚酯至少等30—45分钟。
- 9月16日22:30附近：EIA周报。API称原油+710万桶，正式库存若同向，SC/FU/LU先降Delta；若相反也不追第一跳。[EIA周报](https://www.eia.gov/petroleum/supply/weekly/)
- 9月17日02:00：FOMC决议，市场高度计价加息25bp；AU/AG/CU/NI禁止跨事件裸高Delta或裸Vega。[美联储日历](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-muted-investors-brace-fed-rate-decision-2026-09-16/)
- 未来24小时：Saudi Yanbu与East-West管道修复、Sohar替代装船、Hormuz可见通行与Perim安全；恢复会压缩能源风险溢价，柴油持续紧张则利多更偏产品端。
- 9月18日前后：BOJ政策决定可能推动美元/日元、贵金属与工业金属再定价；避免把单次美元回落当趋势确认。
- 未来7日：交易所动态保证金/限幅、SC/FU/LU滚动；CFTC COT只作滞后拥挤背景，USDA出口销售与北美收割天气复核M/RM/C。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)｜[USDA](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月16日EOD、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差/跨期、跨品种/跨市场、加工利润、风格/中性、波动率、偏度与事件凸性扫描；动态扩展后统一输入77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为占位，RS/WR流动性不足，均保留覆盖记录。
- 黑色建材9/9：FG弱价与back冲突；JM日盘反弹但5D仍弱，I/RB存在roll/curve限制，未发现三层优势。
- 有色贵金属12/12：NI低分入榜；CU旧空退出，AU/AG等待FOMC，黄金信用主题未闭环。
- 能源炼化化工25/25：LU/FU/PR入榜；SC旧多失效；PX/TA/EB/EG成本传导分化，EG减仓上涨不作需求确认。
- 新能源及GFEX新材料全部扫描：LC最弱但OI下降、back和C级现货反对追空；PT/PD缺A级实体与exact海外映射。
- 农产品油脂饲料畜牧22/22：M低分入榜；RM同向但curve反对，C/油脂无三层共振。
- 航运及软商品全部扫描：EC旧多继续退出；CJ弱价减仓、AP价跌仓增，均缺实体闭环。
- Night应覆盖801合约，实际587条有效、55产品；204 outside-window及10 no-trade均非错误。
- 期权应覆盖64产品，实际最新有效52；12个失败、0个execution-ready；T日采集失败使全体降为历史背景。
- A/B级basis、exact import parity、可靠加工利润、完整beta-neutral篮子与可执行期权报价均不可得，不发布伪套利。

单笔试仓最大损失0.15%—0.25% NAV；取得Night价格、curve与非价格层确认后才可提高至0.75%—1.0%。LU/FU初始合并≤0.35%，能源—聚酯共享因子合并≤0.60%，同主题总风险≤2.5%。压力测试包括1/2个涨跌停、阿曼替代供应扩大、管道突发恢复、夜盘gap、流动性消失、保证金上调、相关性破裂、IV跳升/塌陷、交割挤压和人民币急变。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：LU2611在21:30—21:45于5580—5660承接并重上5685，或FU2611在4410—4470承接并重上4495；PR611仅8500—8600承接并重上8650，能源—聚酯共享风险合计≤0.60%。  
C. 今晚应继续观察的机会：M2701回撤后的价仓延续、NI2611反抽失败、TA相对PX/EB、FOMC前AU/AG，以及9月16日期权链修复与实时重报价。  
D. 今晚必须避免或退出的交易：若此前建立则按失效规则处置SC2611旧多；避免接SC首刀、追PR/M第一跳、低开追NI/LC/FG、恢复EC旧多，以及在execution-ready=false时臆测期权成本。
