# 全球商品期货期权高风险机会雷达｜晨间版｜2026-09-18

**prompt_version=radar_2026-09-06_coverage_v1**  
实际生成：07:06 BJT；信息截点：07:00；最近完整中国EOD：9月17日；当前交易日：9月18日；下一可交易窗口：09:00日盘。

## 一、今日一句话结论

**截至本报告时点，无可立即执行的合格新交易；最值得研究的是多LU2611/空SC2611相对价值与RM701回撤多，但均须等09:30—09:45确认。**

当前regime：**原油极端短缺溢价继续降温、成品油相对强；贵金属与铜在美元/收益率回落后反弹；国内化工和苹果偏弱，菜粕仓单骤降形成局部结构机会。**

最接近触发的是LU/SC名义中性组合、RM701与EC2610。前者缺日盘比价确认，RM缺本合约有效Night记录，EC缺exact运价与实体确认；三者都不是07:00可直接下单的仓位。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)与[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并按重点候选下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、[Night逐合约文件](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/latest.json)和[合约元数据](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/contract_meta.json)。

- 统一输入：schema v2，requested_date=2026-09-17，9月18日06:22:37生成；EOD=T-1、Night trading_date=T是正常晨间组合。
- Futures：9月17日EOD，五所806合约、77产品；full_market_ready=true、source_date_match_pct=100%、critical errors=0、excluded exchanges=0；8条OHLC占位记录排除，五条仓单序列沿用。
- Market State：同合约1D/3D/5D/20D历史完整；曲线仅在合约对和历史足够时使用，FG/PX/TA等仅4个观测，不输出稳定z-score。
- Physical：9月17日刷新成功，20项目标中18项按原生频率fresh、SC/LU unavailable；无stale。全部basis为C级或缺失，只作context，不计完整实体层。
- External：17/22 fresh、5项unavailable，均为context_only。repo连续合约WTI/Brent 96.53/99.46与Reuters近月结算101.91/104.82明显冲突，隔离repo油价，不构造跨市场套利。
- Options：9月17日16,016条、216个series、45/64产品；212个surface-ready、54个positioning-ready、0个execution-ready；IV/OI/bid-ask覆盖99.11%/69.50%/0。DCE全品种因数据供应商安全拒绝缺失；PR/PX/TA期权底层结算与期货EOD不一致，相关曲面隔离。
- Metadata：partial；有效合约匹配73.45%，multiplier/tick覆盖36.10%，margin/limit覆盖30.15%，last-trading-day覆盖73.45%；DCE端点失败、GFEX来源日期不一致。

Night质量闸门：trading_date=2026-09-18、night_session_date=2026-09-17，06:01:29生成；data_fresh=true、validation_passed=true、published=true，但coverage_complete=false。806个请求合约中423条有效、37个产品；165条合法outside-window、4条no-night-trade；missing timestamp/price/quote均为0，**query_error=214、unresolved_contract=214**，warning为“214 concrete contracts are unresolved”。

这批Night属于今天已完成的连续交易阶段。逐合约文件经connector返回0字节payload，但统一输入明确存在423条，读取状态记为empty connector payload / source not empty。SC/LU/FU等使用紧凑层exact-contract；RM701、M2701及全部DCE合约无法核实本段Night，不能用其他月份替代。Top候选近次月两腿也无法同时审计，故不强拼Night curve；night_session_fallback_used=false。

## 三、商品仪表盘

1D/5D为9月17日同合约结算收益；Night为归属9月18日的已完成session。曲线为near-minus-next期货结构，不是现货基差；S/P/E为surface/positioning/execution readiness。

| 板块/品种 | 合约；EOD close/settle；1D/5D | Volume/OI/ΔOI；EOD curve | Physical/basis | Night close；vs close/vs settle；ΔOI；质量/时点 | 07:00海外；S/P/E；信号 |
|---|---|---|---|---|---|
| 原油 SC | SC2611；785.2/805；-3.98%/+11.54% | 31.09万/4.43万/+2,831；back 6.80% | 缺失 | 762.5；-2.89%/-5.28%；-980；fresh/02:30 | WTI 101.91；Y/N/N；不追空 |
| 低硫 LU | LU2611；5541/5633；-0.95%/+7.32% | 12.19万/6.97万/+479；back 2.61% | 缺失 | 5574；+0.60%/-1.05%；+1,334；fresh/23:00 | Brent 104.82、柴油仍紧；N/N/N；相对强 |
| 燃油 FU | FU2611；4309/4404；-1.98%/+7.39% | 89.11万/20.36万/-10,433；back 13.69%、z1.00 | C/context | 4298；-0.26%/-2.41%；-1,990；fresh/23:00 | 产品紧但原油跌；Y/N/N；不追方向 |
| 聚酯 PR | PR611；8382/8504；-0.77%/+4.99% | 11.92万/6.30万/-6,100；back 2.54%、z1.45 | 缺失 | 8348；-0.41%/-1.83%；+206；fresh/23:00 | 油价回落；曲面错位；观察 |
| 聚酯 PX | PX611；9376/9570；-1.26%/+2.99% | 49.49万/17.73万/-13,827；back 0.44% | C；现货沿用 | 9338；-0.41%/-2.42%；-5,006；fresh/23:00 | 成本降温；曲面错位；偏弱 |
| 聚酯 TA | TA701；6388/6498；-0.34%/+3.84% | 208.21万/117.31万/-12,720；back 2.26% | C；现货沿用 | 6398；+0.16%/-1.54%；-10,146；fresh/23:00 | 成本降温；曲面错位；不追空 |
| 农产 RM | RM701；2425/2421；+2.07%/+2.67% | 59.59万/60.27万/+40,726；contango 0.78% | 仓单11,708，日减6,073 | exact RM701缺失；代表RM611不可替代 | CBOT豆/粕高位context；Y/Y/N；等报价 |
| 农产 M | M2701；3477/3480；+1.34%/+2.38% | 159.72万/292.81万/+38,192；contango 1.03% | C/context | DCE Night缺失 | CBOT豆1319.25/粕357；N/N/N；数据不足 |
| 航运 EC | EC2610；2215.5/2125.5；+3.68%/+8.33% | 1.99万/2.65万/+2,529；back 24.61% | exact运价缺 | 制度无Night | Hormuz船流仍低；N/N/N；回撤多研究 |
| 苹果 AP | AP701；7150/7144；-2.72%/-5.27% | 22.60万/14.63万/+18,845；back 4.46%、z2.63 | 缺高质库存 | 制度无Night | 无exact外盘；局部/N/N；不追空 |
| 玻璃 FG | FG701；905/907；-0.33%/-5.72% | 104.96万/130.57万/+59,909；back 3.83% | 仓单425、日减2,925 | 913；+0.88%/+0.66%；-47,960；fresh/23:00 | 无exact外盘；Y/Y/N；旧空取消 |
| 苯乙烯 EB | EB2611；9514/9769；-2.23%/-2.29% | 52.61万/26.18万/+18,556；back 1.84% | C/context | DCE Night缺失 | 上游回落；N/N/N；数据不足 |
| 铜 CU | CU2610；108500/108110；+0.63%/-3.24% | 7.99万/16.54万/-5,850；back 0.34% | C/context | 109650；+1.06%/+1.42%；-776；fresh/01:00 | LME 14464；Y/Y/N；反弹但不追 |
| 贵金属 AU/AG | AU2612 935/937.2；AG2612 15593/15667 | AU/AG价仓混合；轻contango/roll | context | 代表合约不同，不硬分解 | 金4380.6、银65.705；AU Y/N/N，AG曲面异常；不追 |
| 新能源 LC | LC2701；131180/130120；+2.96%/-8.30% | 21.31万/41.75万/-1,647；back 0.35% | 现货/仓单沿用，不计分 | 制度无Night | 无exact海外；Y/N/N；反弹观察 |

9月17日Brent结算104.82美元/桶、WTI 101.91，均约跌1%；沙特经阿曼增加转运并争取数日内恢复East-West部分能力，但三座泵站受损、完全修复仍可能需数周。[Reuters油市](https://www.reuters.com/business/energy/oil-prices-extend-losses-fears-middle-east-supply-disruptions-ease-2026-09-17/)｜[Reuters管道](https://www.reuters.com/business/energy/three-pumping-stations-along-saudi-east-west-pipeline-were-hit-recent-attack-2026-09-17/)

美元指数约100.23、收益率从高位回落；现货金约4360.36、白银约65.60，分别上涨逾2%和约4.2%。这是海外收盘/最新可核实信息，不是中国09:00日盘已成交事实。[Reuters美元](https://www.reuters.com/world/asia-pacific/hawkish-fed-lifts-dollar-seven-week-high-focus-turn-boj-2026-09-17/)｜[Reuters贵金属](https://www.reuters.com/world/india/gold-rises-over-1-investors-digest-fed-hike-oil-rally-stalls-2026-09-17/)

## 四、相比上一交易日/今晨真正变化

1. **SC空头延续，但赔率显著恶化。** EOD close跌6.35%，Night再相对前收跌2.89%；然而Night低点753.2、收762.5已接近上一卡TP2=760，且EOD back仍6.80%。旧空若曾触发已进入兑现区，新开仓严禁追低。
2. **LU相对SC的分歧成为本期最清晰结构。** EOD结算LU仅-0.95%而SC-3.98%；Night LU相对前收+0.60%，SC-2.89%，相对差再扩大3.49个百分点。柴油/产品紧张提供外部支持，但这不是exact进口套利。
3. **RM日盘价仓与仓单共同变化。** RM701结算+2.07%、OI增40,726；CZCE菜粕仓单降6,073张至11,708张。contango与缺失exact Night反对直接追多，故只有两层证据。
4. **EC出现日盘重新定价。** close+8.07%、结算+3.68%、OI增10.57%、back 24.61%；Hormuz可见船舶数量仍低支持事件催化，但油轮/船流不是SCFIS欧线exact运价，不能把它写成套利。
5. **FG旧空被Night否定。** EOD弱后Night相对前收+0.88%、OI减少47,960，旧反弹失败空条件取消；不把减仓反弹解释成确定资金身份。
6. **金银和铜转为反弹，而非黄金信用主题确认。** 海外金银大涨、CU Night +1.06%，但美元指数仍在100附近，AU/AG正式合约Night错配且AG偏度异常；只认价格反弹，不认完整信用错价。

旧建议台账：

- COM-M-SC2611-REVERSAL-20260917：69→66。9月17日EOD/Night区间覆盖旧触发、TP1和TP2，但无分钟路径与成交反馈，触发/兑现状态未知；若此前已按条件建立，Night低点753.2已穿越旧TP2=760，应按原计划退出，不把标的触及等同账户收益已实现。
- COM-M-M2701-SOYMEAL-FOLLOWTHROUGH-20260916：65→数据不足。9月17日EOD仍强，但DCE Night整段缺失，旧条件不滚动为今日条件单。
- COM-M-LU2611-FAILED-REBOUND-20260917：63→退出空头观察。LU Night转强且相对SC显著占优；新相对价值使用新ID COM-M-LUSC-RELATIVE-20260918。
- COM-E-FG701-WEAK-CONT-20260914：59→取消条件。Night反弹与OI下降反对旧空，不反向追多。
- COM-E-EC2610-HORMUZ-FREIGHT-20260911：旧多继续保持退出；本期新研究为日盘重定价，使用新ID COM-M-EC2610-REPRICE-20260918，不能偷换旧卡。
- 没有成交反馈，不假设用户持有任何仓位。

## 五、产业链地图

- **最强相对链：低硫/产品相对原油，偏多LU/空SC，置信度中。** 价格层与海外产品紧张支持；SC 6.80% back、SC/LU实体缺失和Night curve不可审计是主要反证。定义为名义中性，不是beta-neutral。
- **最强局部农产：RM—M，偏多RM、置信度中。** RM价涨仓增与仓单骤降支持，M也收涨；但RM contango、DCE Night缺失、CBOT只是代理且basis为C级。
- **航运：EC事件重定价，偏多但置信度中低。** 价格、OI与back共振；exact欧线运价、船期取消量和可比现货缺失，Hormuz船流只能作催化context。
- **最弱：原油—芳烃—苯乙烯，偏空但不追，置信度中。** SC/PX/PR/EB EOD走弱，SC Night继续跌；FU/LU相对强、深back与管道再受损风险反对广谱空头。
- **金属贵金属：反弹regime，置信度低。** CU exact Night上涨，海外金银反弹；缺正式AU/AG同合约Night与可执行期权，黄金信用主题仍未闭环，AI现金流/Capex也无可识别商品错价模型。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | 多14手LU2611/空1手SC2611名义中性 | 21/16/15/9/8 | **69** | 1、4 | 存在待验证优势｜部分、curve/实体反对｜等09:45 |
| 2 | RM701仓单收缩回撤多 | 19/15/14/10/10 | **68** | 1、2 | 存在待验证优势｜部分、Night缺失｜等09:30 exact报价 |
| 3 | EC2610事件重定价回撤多 | 18/15/14/10/10 | **67** | 1、2 | 存在待验证优势｜部分、exact运价缺｜等09:30 |
| 4 | SC2611反弹失败续空 | 18/16/14/9/9 | **66** | 1、4 | 存在待验证优势｜部分、已近旧TP2｜只等深反弹 |
| 5 | AP701弱势延续空 | 17/14/10/8/10 | **59** | 1 | 证据不足｜不足、back反对｜研究观察 |

分项均复算且不超过上限；前四仅两层支持，严格封顶69；AP仅一层，封顶59。本期无70+候选。所有期货/组合的最大损失均不由计划止损限定；分数只是研究排序，不是胜率、期望收益或仓位指令。

## 七、前三名交易卡

### 1. LU2611/SC2611｜多LU、空SC名义中性｜69

**事实：** LU previous close/settlement=5541/5633，Night OHLC=5518/5578/5455/5574，vs close +0.60%、vs settlement -1.05%，Night ΔOI +1,334；SC previous close/settlement=785.2/805，Night OHLC=770/775.9/753.2/762.5，vs close -2.89%、vs settlement -5.28%，Night ΔOI -980。Night比价=7.310，EOD close比价=7.057。  
**市场定价：** 原油短缺溢价退潮快于低硫产品紧张。  
**分歧：** 产品端紧张可能继续令LU跑赢SC；最强竞争解释是LU只是滞后补跌，SC 6.80% back和管道再受损会令原油突然反弹。

- 最佳表达：多14手LU2611、空1手SC2611。按Night价格，名义分别约780,360元与762,500元，相差约2.34%；这是dollar-neutral近似，不是beta-neutral。
- 收益公式：P&L=140×(LU退出价−LU入场价)−1000×(SC退出价−SC入场价)。
- 好成交：09:45后LU/SC比价在7.25—7.35获得接受，且开盘后标准化收益LU至少跑赢SC 0.5个百分点，先1/3组合。
- 中成交：比价突破7.40后回踩7.30—7.40不破，仓位减半。
- 坏成交：直接高于7.55、SC低于740形成追空、任一腿滑点超过组合1R的20%，放弃。
- 止损：30分钟接受7.05下方；计划止损不保证最大损失。
- 逻辑失效：比价跌破7.00，或Brent重上108且SC back>8%、LU/FU产品相对强度同时消失。
- TP1比价7.55或+1.5R；TP2 7.80或+3R；1—3D不扩张退出。
- 风险0.20%—0.30% NAV；与所有能源方向仓合并≤0.50%。
- LU交易单位10吨/手、tick 1元/吨、tick value 10元；SC 1,000桶/手、tick 0.1元/桶、tick value 100元。两腿均有夜盘、实物交割；2611最后交易日10月30日，交割风险要求最迟10月中旬移仓。[INE低硫规则](https://www.ine.cn/regulation/ineregulation/rules/202606/t20260626_832298.html)｜[INE原油合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 动态保证金/限幅未确认，不编伪精确压力金额；一板最坏损失公式为14×55,740×L_LU+762,500×L_SC，两板按各腿实际复合限幅计算。

### 2. RM701｜仓单收缩回撤条件多｜68

**事实：** EOD OHLC=2409/2442/2396/2425，结算2421；1D +2.07%、5D +2.67%，ΔOI +40,726；near-next contango 0.78%。CZCE仓单11,708张、日减6,073张。Night代表合约为RM611，**不能替代RM701**；exact RM701 Night缺失。

- 市场定价：日盘已计入部分现货可交割资源收缩。
- 分歧：仓单下降与价仓共振可能延续；竞争解释是仓单注销不等于社会库存下降，且contango、缺Night与高call skew反对追价。
- 好成交：取得09:00后exact RM701报价，09:30在2405—2425承接并重上2430/VWAP，先1/3仓。
- 中成交：突破2442后回踩2428—2442不破，仓位减半。
- 坏成交：直接高于2470、无法核实RM701夜盘/开盘报价或深度不足，放弃。
- 止损：30分钟接受2390下方。
- 逻辑失效：跌破2396，仓单快速回升，或contango扩大至1.5%以上且OI转降。
- TP1 2460或+1.5R；TP2 2520或+3R；1—3D无新增现货确认退出。
- 风险0.15%—0.25% NAV；与M/OI/Y方向合并≤0.50%。
- 10吨/手、tick 1元/吨、tick value 10元；结算名义24,210元。repo当前基础margin/limit为7%/6%，动态参数下单前复核；最后交易日2027年1月14日、实物交割。[CZCE菜粕合约](https://www.czce.com.cn/cn/sspz/czp/bzhy/qhhy/H077002011001001index_1.htm)｜[CZCE仓单日报](https://www.czce.com.cn/cn/jysj/cdrb/H077003010index_1.htm)
- 按6%基础限幅，一板约1,453元/手，两板复合约2,993元/手；实际风控参数更严时以交易所/期货公司为准。

### 3. EC2610｜事件重定价回撤条件多｜67

**事实：** EOD OHLC=2064/2219/2041/2215.5，结算2125.5；1D +3.68%、5D +8.33%，ΔOI +2,529；back 24.61%。EC制度上无Night。  
**市场定价：** 欧线运价风险溢价重新上升。  
**分歧：** Hormuz船流显著下降可能延长航运扰动；竞争解释是油轮与集装箱航线并非同一市场，替代装船和航线调整可能使headline不落到SCFIS欧线。

- 最佳表达：EC2610单腿条件多；不以油轮数据构造伪套利。
- 好成交：09:30后2150—2210获得接受并重上2220/VWAP，先1/3仓。
- 中成交：突破2219.5后回踩2190—2220不破，仓位减半。
- 坏成交：直接高于2280或没有exact欧线运价/船期补证，放弃。
- 止损：30分钟接受2090下方。
- 逻辑失效：跌破2041、back低于20%，或欧线船期恢复且现货运价未确认上行。
- TP1 2280或+1.5R；TP2 2400或+3R；1—5D无现货确认退出。
- 风险0.15%—0.25% NAV；与能源/航运共享因子合并≤0.50%。
- 合约乘数每点50元、tick 0.5点、tick value 25元；结算名义106,275元，基础限幅10%、最低保证金12%，10月26日最后交易并现金交割。[INE EC标准合约](https://www.ine.cn/products/futures/index_f/ec_f/standard_ec_f/202605/t20260511_831625.html)
- 一板不利压力约10,628元/手，两板复合下跌约20,192元/手；动态参数和涨跌停扩板风险须开盘前核验。

## 八、商品期权专项

最新有效截面为9月17日EOD；Night改变了底层moneyness和Delta。所有目标结构execution_ready=false，bid/ask覆盖为0。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 判断 |
|---|---:|---:|---:|---|---|
| SC2611/10-14 | 65.57%/48.78% | +16.79vol | +0.73/+1.41 | Y/N/N | 标的Night再跌，须重报价 |
| FU2611/10-19 | 60.62%/43.31% | +17.31vol | -0.50/+1.42 | Y/N/N | event vol仍贵 |
| RM701/12-11 | 20.80%/16.16% | +4.64vol | +6.39/+0.98 | Y/Y/N | call skew贵，且exact Night缺 |
| FG701/12-11 | 23.28%/25.66% | -2.39vol | +7.87/+2.41 | Y/Y/N | IV<RV不单独证明put便宜 |
| CU2610/09-23 | 13.73%/14.27% | -0.54vol | +2.66/+1.28 | Y/Y/N | 近到期，先核交割与Gamma |
| AU2612/11-24 | 24.63%/20.23% | +4.40vol | +2.98/+1.22 | Y/N/N | 正式Night错配，不执行 |
| AG2612/11-24 | 44.14%/31.46% | +12.68vol | +134.80/+66.36 | Y/N/N | 偏度明显异常，隔离 |
| LC2701/12-07 | 44.67%/41.07% | +3.59vol | +0.75/+1.35 | Y/N/N | positioning不足 |
| PR/PX/TA | 表面可见但底层结算错位 | N/A | N/A | partial/N/N | 隔离，不计第五层 |

当前没有可证明优于期货的期权结构。取得09:00实时双边报价后，才可比较RM701有限净支出call spread、SC2611 put spread或LU/SC线性组合；执行价、Delta、净支出、盈亏平衡、Greeks、滑点与行权交割必须重算。Dealer Gamma方向未知。

research only; manual quote and manual confirmation required before execution; no premium quoted

## 九、9:00开盘风险地图

严格三层：①Previous China EOD=9月17日；②Current Trading Day Night=归属9月18日、已完成但仅37个产品闭环；③07:00 Overseas=9月17日国际收盘与最新可核实事件。

| 品种 | EOD→Night→海外 | 09:00判断 | 追价/等待 | 核心确认 |
|---|---|---|---|---|
| LU/SC | LU EOD/Night均显著跑赢SC→原油续跌、产品仍紧 | 比价偏高 | 不追；45m | 比价7.25/7.40、标准化收益、back |
| SC | EOD-3.98%→Night -2.89%→外油约-1% | 低开，弱势已大量交易 | 严禁追空；45m | 753/762/780/805、back、管道 |
| FU | EOD-1.98%→Night -0.26%→柴油紧、原油跌 | 平/低开、冲突 | 45m | 4235/4298/4404、back |
| RM | EOD强/仓单降→exact Night缺→CBOT高位 | 数据不足，可能高开 | 30m且先补报价 | RM701 2396/2425/2442、仓单 |
| M/JM/I等DCE | EOD可用→Night全缺 | gap方向无法判断 | 45m | exact合约、量仓、curve |
| EC | EOD强/back深→制度无Night→船流低 | 09:00首次定价 | 30m | 2090/2219.5、exact运价 |
| PR/PX/TA/EB | EOD弱→前三Night弱/EB缺→油价跌 | 平/低开 | 30—45m | PR8340、PX9338、TA6398、breadth |
| FG/SA | EOD弱→Night反弹 | 平/小高开、旧空失效 | 不追；30m | FG905/913/919、SA1014 |
| CU | EOD反弹→Night+1.06%→LME高位 | 高开概率较高 | 不追；30m | 108500/109650/109850 |
| AU/AG | EOD混合→代表合约上涨→海外金银大涨 | 高开但合约错配 | 45m | exact主力、DXY、收益率 |
| AP/LC | 无Night；EOD一弱一强 | 09:00首次定价 | 30—45m | AP7046/7150、LC130120 |
| 其他无Night品种 | Previous EOD only | 09:00首次定价 | 30—45m | 量仓、curve、实体 |

原油的海外弱势已被SC Night大幅吸收；开盘后真正的新信息弹性应看SC能否守住753、LU/SC比价能否稳定在7.25上方。repo与可靠公开源均没有同一时点exact USD/CNH，本期只确认DXY约100.23、美元冲击边际下降，不量化人民币贡献。

## 十、未来24小时与7天事件

- 9月18日09:00：中国日盘；LU/SC与SC至少等45分钟，RM/EC至少等30分钟；DCE品种先补本合约报价。
- 9月18日亚洲时段：BOJ政策决定与日元波动可能改变DXY、金银和工业金属；AU/AG/CU避免第一跳高Delta。[Reuters BOJ前瞻](https://www.reuters.com/world/asia-pacific/japan-vows-effort-maintain-orderly-yen-moves-2026-09-17/)
- 未来24小时：East-West部分恢复、三座泵站修复、Sohar替代装船与Hormuz通行；重新受损会伤害SC空头，恢复则压缩原油back。[Reuters Hormuz船流](https://www.reuters.com/world/middle-east/number-ships-transiting-strait-hormuz-falls-three-wednesday-data-shows-2026-09-17/)
- 9月19日03:30附近：CFTC COT常规窗口，仅作滞后拥挤背景。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 9月21日前后：中国LPR与政策预期窗口；黑色、有色、新能源只按实际公告与price/curve反应调整，不预埋方向。
- 9月23日22:30：EIA周报；能源仓数据前降Delta，期权只允许有实时报价的有限净支出结构。[EIA日程](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- 未来7日：USDA出口销售、北美收割天气、中国大豆采购和马棕出口；RM/M/Y/P/OI必须用实际采购、basis与库存兑现复核。[USDA](https://www.fas.usda.gov/data/export-sales-query-system)
- OPEC+/IEA若无计划内新月报，不制造虚假催化；交易所保证金、限幅和SC/FU/LU交割月参数仍需每日复核。

## 十一、覆盖、风险与归档核对

- 应覆盖：强制63代码；统一输入实际77产品；期权应覆盖64产品。
- 实际取数且已分析：77个产品进入扫描，70个具备有效趋势/量仓/curve分析；Night 37产品/423合约；期权45产品、216 series。
- 数据不足：Night 214个具体合约query_error/unresolved，DCE及RM701/M2701本合约Night不可核实；SC/LU实体缺失；期权19产品失败、0 execution-ready；PR/PX/TA期权底层结算错位；A/B级basis、exact import parity、可靠加工利润、完整Night curve和可执行期权成本不足。
- 不适用/流动性不足：JR/PM/RI/WH/ZC为占位，RS/WR流动性极低；均保留覆盖记录，没有提高门槛后静默删除。
- 黑色建材9/9：FG旧空被Night反弹否定；DCE的I/J/JM仅有EOD，夜盘判断降级。
- 有色贵金属12/12：CU反弹最清晰；AU/AG海外强但正式Night合约错配，AG期权偏度隔离。
- 能源炼化化工25/25：LU/SC相对价值入榜；SC续空赔率差；PR/PX/TA/EB偏弱但缺实体闭环。
- 新能源及GFEX新材料全部扫描：LC反弹、SI/PS/PT/PD缺高质量实体和exact海外映射。
- 农产品油脂饲料畜牧22/22：RM入榜、M EOD强；DCE Night缺失使油脂、饲料和养殖开盘gap判断降级。
- 航运及软商品全部扫描：EC新研究入榜；AP低分观察，CF/CY/SR/CJ/PK无三层优势。
- 策略类别已扫：方向、基差/跨期、curve、跨品种/跨市场、加工链、dollar-neutral/风格、波动率、偏度与事件凸性；可定义的唯一优先RV是LU/SC，未定义beta-neutral篮子不发布。
- 周期已扫：1D/3D/5D/20D、1—3D战术、1—20D催化；缺历史或roll时不输出伪趋势。

风险预算：单笔试仓最大损失0.15%—0.30% NAV；只有09:00价格、curve及非价格层确认后才考虑0.75%。LU/SC组合与所有能源方向风险合并≤0.50%；农产品方向合并≤0.50%；任一主题总风险≤2.5%。压力测试覆盖1/2个涨跌停、组合相关性破裂、Saudi路线再中断、DCE夜盘盲区、流动性消失、保证金上调、IV跳升/塌陷、交割挤压和人民币急变。

固定六路径已从main回读验证，manifest中2026-09-18 + commodities_morning恰好一条；[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-18_commodities_morning.md)。archive_status=success，ci_validation_status=pending_or_unverified。

A. 今天没有应立即建立的新仓位。  
B. 今天只应挂条件单的仓位：09:45后LU/SC比价7.25—7.35获得接受且LU跑赢SC≥0.5个百分点时，多14手LU2611/空1手SC2611；或09:30后RM701在2405—2425承接并重上2430、EC2610在2150—2210承接并重上2220；单笔/组合风险0.15%—0.30%。  
C. 今天应继续观察的机会：SC2611深反弹失败续空、M2701在DCE Night缺失后的开盘gap、CU/金银反弹、AP701弱势，以及RM/SC期权实时重报价。  
D. 今天必须避免或退出的交易：追空已接近旧TP2的SC、用RM611替代RM701 Night、重启FG旧空、把Hormuz船流当EC exact运价、把C级basis称套利，以及在execution_ready=false时臆测期权成本。