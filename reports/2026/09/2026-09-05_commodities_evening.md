# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-05

> revision: 1  
> generated_at_bjt: 2026-09-05T19:42:19+08:00  
> data_protocol_version: china_commodities_v2  
> 周末模式：9月5日为星期六。中国商品市场没有9月5日日盘，也没有今晚21:00夜盘。最后完整中国EOD为9月4日；9月4日晚至9月5日凌晨的合法连续交易已完成，但仓库将其标记为 `trading_date=2026-09-05`，这按自然日落在周六，属于交易日语义异常。本报告将其规范解释为“周五夜盘、下一有效交易日（9月7日）日盘之前的已完成价格发现”，绝不视为今晚未来行情。

## 一、今晚一句话结论

**今日商品期货期权无合格交易。** 市场本身今晚不可交易；周末新增的Kharg油轮遇袭消息把周一原油gap尾部抬高，但OPEC+周日会议、俄乌和谈线索与Friday-night已定价部分相互冲突，最优选择是保留风险预算，等周一9:00价格接受度。

## 二、数据质量与覆盖

第一读取层按协议读取了 China-Commodities-Engine 的 `data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json` 和 `data/radar_latest.json`，并按需读取 `data/market_state_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/contract_meta.json`。

统一输入 `schema_version=2`，requested_date=`2026-09-04`，generated_at=`2026-09-05T19:04:36+08:00`。最后可验证完整Futures为9月4日五所 SHFE/INE/DCE/CZCE/GFEX 共802合约：`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，6条OHLC placeholder排除。9月5日root refresh尝试因iFinD `Device exceed limit` 对五所/期权等模块报错，root状态显示fresh=false、full_market_ready=false；这是周六刷新任务/供应商访问失败，不能反推市场数据有问题，也不能覆盖module-specific/report_input里的9月4日last-good EOD。

Market State同样锁定9月4日，保留同一具体合约的1D/3D/5D/20D、RV20、Volume/OI z-score、ΔOI和near-next curve。今天没有新的中国EOD，因此这些指标均是“上一有效交易日状态”，不是9月5日涨跌。

Night Session状态显示 `trading_date=2026-09-05`、`night_session_date=2026-09-04`、generated_at=`2026-09-05T06:02:14+08:00`，611个有夜盘合约，fresh/validated/published=true。由于9月5日为周六，这个trading_date自然日标签不合法；真实可用事实是：周五21:00至周六凌晨的连续交易已经合法完成。按交易所“某交易日夜盘从前一交易日21:00开始”的规则，它应服务于下一有效交易日9月7日。故本报告只把它作为“Friday-night close → 周一日盘尚未发生”的半程价格发现，不能计算9月7日 `day_follow_through`。

Physical最新requested_date=9月4日，20个目标18个在各自原生频率下有效、2个不可用；但周六统一输入将其标为非fresh/未发布状态，且常用100ppi spot/basis多数缺地区、等级、税口径、交割地，属于C级context，不能作为周末fresh实体层或可执行basis。

External repo requested_date=9月5日，但所有市场价格观察仍止于9月4日；WTI continuous约91.22美元/桶、Brent约95.85、LME 3M铜约14,371.5美元/吨，均为Friday close/context。周六15:00–19:30全球主要商品期货交易所休市，因此没有新的“实时价格变化”可以合法补充；本时段只有新闻事件增量，最重要的是北京时间约15:16发布的Kharg Island附近伊朗油轮遭美方导弹击中的报道。该消息发生在Friday-night中国价格发现之后，属于周一潜在gap的**未定价事件证据**，不是“中国期货已经上涨”。

Options module-specific最终为9月4日：19,394张合约、352 series、52/64品种；IV coverage约97.71%、OI coverage约68.21%、bid/ask coverage=0；`surface_ready=false`、`positioning_ready=false`、`execution_ready=false`、dealer gamma方向未知。`surface_latest.json`为空。今晚禁止输出ATM IV、RR25/BF25、term structure、PCR、Gamma方向、具体权利金、滑点或成交成本。

Contract Metadata为9月4日official_partial；很多合约的multiplier/tick/night-session/margin/price-limit仍为空，9月5日动态刷新又受device-limit影响。所有重点合约的动态保证金、限幅、最后交易日与交割风险，必须在周一开盘前通过交易所最新参数再次复核。

## 三、商品仪表盘（最后完整EOD=2026-09-04；Friday-night为已完成的下一交易日价格发现）

| 板块 | 合约 | 9/4 EOD close/settle | 1D / 5D settle | Volume / OI / ΔOI | Curve / Basis / Physical | Friday-night close vs 9/4 close | 周末15:00–19:30增量 | Options | 下一窗口信号 |
|---|---|---:|---:|---|---|---|---|---|---|
| 黑色/合金 | SF611 | 6624 / 6564 | +5.06% / +8.42% | 133.5万 / 48.29万 / +2.08万 | curve偏back；C级basis；周末无新实体确认 | 无可靠同合约Friday-night分解 | 无海外直接锚 | not ready | 周一9:00，回撤吸收才看多 |
| 塑化 | V2701 | 5128 / 5040 | +3.07% / +11.50% | 266.8万 / 113.50万 / +9.12万 | near-next -2.03%，z=-3.55，深contango反证 | 5072，**-1.09%** | 无新价格；周末事件映射弱 | not ready | 周一9:00，先看5072/5040接受度 |
| 纯碱 | SA701 | 1093 / 1080 | +1.79% / 约强势延续 | 238.9万 / 121.84万 / 约+2.12万 | contango；C级basis | 1110，**+1.56%** | 无直接海外锚 | not ready | 周一9:00，高开不追，等30m |
| 原油 | SC2610 | 685.2 / 683.1 | -1.13% / +15.33% | 16.19万 / 3.58万 / -3.42% | back约+5.40%；basis不完整 | 690.7，**+0.80%** | Kharg油轮遇袭消息晚于Friday-night；OPEC+周日会议 | not ready | 周一9:00 gap双向；等30m |
| 黄金 | AU2610 | 965.96 / 970.82 | +1.97% / -2.31% | 27.42万 / 15.84万 / 价涨仓减 | curve近中性；宏观主导 | 958.0，**-0.82%** | 非农后美元/收益率偏强；周末地缘反向支撑 | not ready | 周一9:00，等15–30m |
| 白银 | AG2610 | 16250 / 16318 | +2.24% / -2.97% | 46.70万 / 20.78万 / 价涨仓减 | curve轻contango；宏观+工业混合 | 16080，**-1.05%** | 与黄金相同，beta更高 | not ready | 周一9:00，假突破风险高 |
| 乙二醇 | EG2610 | 5898 / 5844 | +0.57% / +16.18% | 179.2万 / 39.25万 / 价涨仓增 | back约+6.84%，z≈1.33 | 5866，**-0.54%** | 原油周末尾部支持但非exact parity | not ready | 周一9:00，先看油化工breadth |
| 甲醇 | MA610 | 3175 / 3206 | +0.56% / +13.93% | 260.0万 / 60.65万 / 价涨仓减 | back约+3.49%，z≈1.56；C级basis | 3187，**+0.38%** | 周末原油事件仅映射 | not ready | 周一9:00，等待链内确认 |
| 燃料油 | FU2611 | 3841 / 3872 | +0.21% / +5.50% | 80.0万 / 20.59万 / 价涨仓减 | back约+6.30%；C级basis | 3793，**-1.25%** | 原油周末风险偏上，但FU Friday-night偏弱 | not ready | 周一9:00，优先观察SC-FU相对强弱 |
| 新能源 | LC2701 | 141940 / 147040 | -4.08% / 高波动弱势 | 31.24万 / 39.26万 / OI高位 | curve仍偏back，实体层不足 | 无夜盘 | 周末无直接海外定价 | not ready | 周一9:00，不接第一刀 |

注：Curve为近月减次近月的期货结构，不是现货基差；Friday-night close只说明周五夜间已发生的价格发现。周六没有日盘，因此不存在9月5日 `day_follow_through`。

## 四、相比上一交易日真正变化

1. **从“日盘机会筛选”切换到“周末gap风险管理”。** 9月5日没有中国EOD，不能把周六root刷新失败或任何新闻当成中国当日涨跌；核心价格锚仍是9月4日EOD与随后已完成Friday-night。
2. **Friday-night对9月4日国内挤压进行了第一次验真，而且出现明显分化。** SA701在1093日盘收盘后又收1110（+1.56%），SC +0.80%、MA +0.38%；但V2701从5128回到5072（-1.09%），FU -1.25%、EG -0.54%。所以“周五所有材料/能化强势都会自然延续”已经被部分否定。
3. **贵金属被非农重新定价。** 美国8月非农+16.2万、失业率4.1%；2Y收益率上行、美元转强，国际金周五下跌约1.2%。中国Friday-night AU/AG分别相对9月4日close回落0.82%和1.05%，与宏观方向一致。
4. **油价周末新增一个Friday-night之后才出现的上行尾部。** Reuters北京时间约15:16报道，伊朗半官方Tasnim称Kharg Island锚地附近一艘伊朗油轮遭4枚美国导弹击中；没有伊朗官方公告或CENTCOM即时确认。Kharg在战争前承载约90%的伊朗原油出口，因此该消息对周一SC是未定价供应风险，但可信度必须打折。
5. **油的反证同样很强。** OPEC+七个核心成员周日会议据Reuters此前消息大概率维持10月产量政策不变；同日美方特使抵达莫斯科推进俄乌和谈，若缓和导致制裁/俄油风险溢价下降，会抵消伊朗冲击。周一SC不是单向“必高开”交易，而是binary gap。
6. **期权研究层没有改善，反而比周五19:30时更不适合结构化下单。** 最终module-specific只有52/64品种、surface/execution均not ready。任何“买call spread/做skew”的价格化建议都应推迟。

## 五、产业链地图

**1）原油—燃料油—炼化：周末最重要，但不是最适合提前下注。** 9月4日SC 5D仍+15.3%、curve偏back，Friday-night又+0.80%；与此同时FU Friday-night -1.25%，说明炼化端并未同步追随。周六Kharg消息把供应尾部重新抬高，Hormuz通行仍明显低于近期均值；但OPEC+周日政策会议和俄乌和谈提供反向催化。方向：上行尾部；置信度：事件高、交易中低；最大缺失：周日OPEC+结果与周一开盘接受度。

**2）纯碱/PVC/硅铁：国内挤压最强，但结构不统一。** SF周五量价仓共振，SA Friday-night继续+1.56%，但V Friday-night回吐1.09%，且V深contango是明显反证。最强：SA/SF；最弱确认：V。最大缺失：周末没有新增实体供需与高质量basis，期权not ready。置信度：中等偏低。

**3）贵金属：非农利率冲击已经得到Friday-night确认，但周末地缘可能反向。** AU/AG Friday-night走弱与美元/收益率上行一致；然而Kharg事件在其收盘后出现，可能重新增加避险需求。此时做空黄金最大的风险正是“宏观方向对、周末跳空方向错”。置信度：双向中等，交易置信度低。

**4）聚酯/甲醇：中期趋势仍强，Friday-night弹性不足。** EG 5D+16.2%、MA 5D+13.9%，curve均偏back；但Friday-night EG -0.54%、MA仅+0.38%，说明高趋势不等于新信息继续推动。周一若SC强而EG/MA不跟，是油价beta边际衰减的重要信号。置信度：中低。

**5）农产品：全球供给先验偏紧，国内没有fresh交易确认。** FAO称8月全球食品价格指数升至2022年以来最高，糖价环比大涨且全球谷物产量预测下调；但CBOT/ICE周六无新价格、中国也无新EOD，因此只作周一前的背景，不转化为70+交易。置信度：背景中等、交易低。

## 六、机会排行榜

**今日商品期货期权无合格交易，保留现金和观察仓。**

1. **SC2610 周一gap接受/回落双向观察｜69分｜观察**  
   fresh层=1（Friday-night价格）+4（周末地缘/政策事件）=2层，上限69。评分：逻辑20 / 赔率17 / 催化18 / price-curve-vol8 / 持仓技术6。Kharg事件增加上行尾部，但OPEC+与俄乌和谈使方向不对称且不可预判。
2. **AU2610 非农弱势 vs 地缘反转观察｜66分｜观察**  
   fresh层=1+4=2层。评分：逻辑18 / 赔率16 / 催化15 / price-curve-vol9 / 持仓技术8。Friday-night弱势有宏观确认，但周末新地缘风险可能打断该趋势。
3. **SA701 周一挤压延续观察｜59分｜观察**  
   fresh层只有第1层；Friday-night +1.56%说明相对强，但无fresh实体/海外/期权层，且前一日结构并不支持“真实短缺已经确认”。评分：逻辑17 / 赔率13 / 催化8 / price-curve-vol12 / 持仓技术9。

SF611虽是9月4日最强日盘候选，但周末没有同合约连续交易或新增独立证据，本次不把它排进fresh前三，只保留周一开盘观察。

## 七、前三名交易/观察卡

### 1）SC2610｜周一双向gap观察｜69

- **事实**：9/4 close/settle=685.2/683.1；1D settle=-1.13%，5D=+15.33%，OI下降约3.42%，curve约+5.40% backwardation。Friday-night close=690.7，相对9/4 close +0.80%。
- **周末新增事实**：北京时间9/5约15:16，Reuters报道Tasnim称Kharg附近伊朗油轮遭美方导弹击中，暂无伊朗官方公告或CENTCOM即时确认；该消息晚于Friday-night收盘。周日OPEC+核心成员会议是反向/二元催化。
- **市场定价**：Friday-night已经对非农、此前中东紧张交易过一次，但没有交易周六Kharg消息。
- **推断**：周一9:00更可能出现较大的SC gap/波动，而不是提供一个可在周末提前锁定的单边胜率。
- **主观判断**：只交易“gap之后的接受度”，不交易“新闻标题”。
- **最佳表达**：周一SC2610期货条件单；商品期权因surface/execution not ready仅研究，不报价。
- **入场**：周一9:00后至少等30分钟。若价格高开后能守住Friday-night 690.7并重新突破opening-range high，才考虑1/3多；若高开失败、跌回690.7下并且国际油价同步回吐，则可研究失败gap短。不要在集合竞价/第一跳追。
- **止损/失效**：opening-range反向突破；地缘消息被官方否认或OPEC+/俄乌消息显著改善供给预期则多头失效；反之若新的供应基础设施受损升级则空头失效。
- **TP**：TP1=1.5R，TP2=3R；时间止损1–3D。
- **风险预算**：初始probe最大损失0.25%–0.50% NAV；OPEC+结果明朗且价格确认后才可提高到0.75%–1.0%，同能源因子总风险暂≤1.5%。
- **交易参数**：repo contract metadata为partial；SC官方夜盘通常21:00–02:30，但**今晚周六无交易**，下一有效窗口周一9:00。multiplier/tick/margin/price limit/last trading day与交割风险均在周一开盘前复核最新交易所参数。
- **压力情景**：1/2个涨跌停、周日OPEC意外增产/减产、Kharg事件升级/否认、流动性跳空、保证金上调。

### 2）AU2610｜非农弱势/地缘反转观察｜66

- **事实**：9/4 close/settle=965.96/970.82；1D +1.97%，5D -2.31%，价涨仓减。Friday-night收958，相对9/4 close -0.82%。
- **宏观事实**：美国8月非农+16.2万、失业率4.1%，数据后2Y收益率上升、美元走强，国际现货黄金周五下跌约1.2%至4419美元附近。
- **市场定价**：Friday-night AU的下跌已经验证了“强就业→更鹰利率路径→黄金承压”。
- **反证**：周六Kharg事件发生在其收盘后，可能重新制造避险买盘；所以周一直接追空风险很差。
- **入场**：周一9:00后等15–30分钟。只有外盘黄金开周后仍弱、人民币无急贬、AU无法重夺958–966区域，才研究顺势空；若直接高开并站回966上方，空头放弃。
- **止损/失效**：opening-range high；实际利率快速回落/美元转弱/中东升级均使空头失效。
- **TP**：1.5R / 3R；时间止损1–2D。
- **风险预算**：0.25%–0.40% NAV。
- **参数/期权**：动态合约参数周一复核；Options surface/execution not ready，不提供ATM、skew或权利金，不把bull/bear spread写成可执行方案。

### 3）SA701｜挤压延续观察｜59

- **事实**：9/4 close/settle=1093/1080，日盘close约+3.02%；Volume 238.9万、OI 121.84万，估算ΔOI约+2.12万。Friday-night close=1110，相对9/4 close +1.56%。
- **市场定价**：SA比V更能把周五日盘挤压延续到Friday-night；V同期从5128回到5072（-1.09%）。
- **反证**：此前SA/V期限结构偏contango，周末又没有新的高质量basis/实体供需/Options层，不能把挤压自动解释成现货短缺。
- **入场**：周一9:00后等30分钟；只有1110附近能被接受、OI不明显回吐、near-next contango不继续恶化，再考虑升级为probe。若高开直接冲，不追。
- **失效**：跌回1093/1080下方并伴随OI回落；或V/FG/SF链内breadth同步转弱。
- **TP/时间止损**：1.5R / 3R；1–3D。
- **风险预算**：若升级，0.25%–0.40% NAV。当前评分59，**现在不下单**。
- **参数**：CZCE动态保证金、限幅、交割月规则下单前复核；周六无交易，下一窗口周一9:00。

## 八、商品期权专项

本期Options是**9月4日T-1相对于周末报告日**：19,394 contracts、352 series、52/64品种；IV coverage 97.71%，OI coverage 68.21%，bid/ask=0。虽然单合约可能带vendor IV，但全市场 `surface_ready=false`，且 `surface_latest.json` 为空，因此：

- 不报告ATM IV、RR25、BF25、term structure或IV-RV；
- 不报告PCR/crowding为完整结论；
- dealer gamma方向未知；
- execution not ready，禁止权利金、净成本、滑点和可成交性估算；
- 本周末最有价值的vol研究是等待周一SC/AU/AG开盘后的event-vol重定价，而不是现在猜哪条期权“便宜”。

所有商品期权结构在获得新fresh surface和真实报价前均不进入tradeable structures。

## 九、21:00夜盘开盘风险地图

**今晚21:00没有中国商品夜盘。** 9月5日是星期六；交易所夜盘是周一至周五，且“某交易日夜盘从前一交易日21:00开始”。9月4日21:00至9月5日凌晨的连续交易已经结束；仓库把它自然日标成`trading_date=9/5`，本报告已按周末交易日规则降级并规范为下一有效交易日9月7日前的Friday-night价格发现。周一9:00才是下一可交易窗口。

- **SC**：Monday gap上行尾部最大；Kharg消息未被Friday-night交易。不要预判第一跳；周一等30m，核心看690.7能否被接受、Brent/WTI周开是否同向，以及OPEC+结果。
- **AU/AG**：Friday-night非农后弱，但周末地缘反向。周一等15–30m，核心看国际金、美元/实际利率与958/16080的夜盘锚。
- **SA/V**：SA比V强；周一等30m。最重要不是开盘涨幅，而是curve是否改善、OI是否继续支持。
- **SF/LC**：无Friday-night可用于精确分解；下一窗口周一9:00。SF看高位吸收，LC不接第一刀。
- **EG/MA/FU**：等30–45m，必须看SC与炼化/化工breadth是否一起确认。若SC受周末消息大涨而FU/EG继续弱，优先研究相对价值而非追整个能化beta。

## 十、未来24小时 / 7日事件

- **9月6日（周日，时间未核实）OPEC+七个核心成员会议**：Reuters消息称基准预期是维持10月产量政策不变；任何偏离都会直接改变周一原油Delta。处理：周末不预置大仓，等待结果+价格。
- **9月7日09:00 北京时间：中国商品日盘重新开市**。Friday-night价格之后第一次吸收周六/周日新闻；SC、AU/AG、SA/V尤其需要opening range。
- **9月9日：EIA Short-Term Energy Outlook**。影响中期油价供需预期。
- **9月10日20:30：美国8月PPI**；**9月11日20:30：美国8月CPI**。影响美元、实际利率、黄金/白银与油价金融条件。
- **9月10日（美国东部时间，劳动节顺延）：EIA Weekly Petroleum Status Report**；官方页面注明当日12:00与14:00 ET分批发布。处理：能源Delta在数据前缩减。
- **9月10日：上期所热卷/不锈钢期权、能源中心低硫燃料油期权上市**。新产品首日只研究流动性与曲面，不把短历史当成熟vol信号。
- **9月11日：IEA Oil Market Report**。处理：关注供需、炼厂与库存预测对地缘溢价的修正。
- **9月12日00:00左右北京时间（USDA 9月11日12:00 ET）：WASDE + Crop Production**。处理：豆粕、油脂、玉米、棉花相关Delta/Vega在报告前降档。

## 十一、最终行动清单

A. 今晚没有应立即建立的新仓位。  
B. 今晚没有市场可挂中国商品条件单；周一9:00只考虑SC2610 gap接受/失败、AU2610非农弱势是否延续、SA701挤压是否获结构确认。  
C. 今晚应继续观察的机会：周日OPEC+结果、Kharg事件是否获官方确认/升级、俄乌和谈进展，以及周一SC-FU/EG相对强弱、SA-V分化。  
D. 今晚必须避免或退出的交易：把周六新闻当成中国已交易价格、把repo `trading_date=9/5`误写成今晚夜盘、周一集合竞价追SC/AU/SA首跳、在surface/execution not ready时臆测期权成本，以及用C级basis/仓单替代实体供需结论。

---

### 主要来源

- [China-Commodities-Engine unified report input](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)
- [China-Commodities-Engine root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- [Night Session status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)
- [Options Quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)
- [External](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/external/latest.json)
- [Reuters: Iranian tanker near Kharg Island hit, Sep. 5](https://www.reuters.com/world/middle-east/explosions-heard-near-irans-kharg-island-gulf-origin-unknown-fars-news-says-2026-09-05/)
- [Reuters: OPEC+ likely to keep October policy unchanged, Sep. 2](https://www.reuters.com/business/energy/opec-likely-to-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-02/)
- [Reuters: U.S. August payrolls, Sep. 4](https://www.reuters.com/business/us-nonfarm-payrolls-surge-august-unemployment-rate-steady-41-2026-09-04/)
- [Reuters: Gold after payrolls, Sep. 4](https://www.reuters.com/world/india/gold-holds-ground-with-us-payrolls-data-radar-2026-09-04/)
- [Reuters: Oil weekly close and Hormuz risk, Sep. 4](https://www.reuters.com/business/energy/oil-set-steepest-weekly-gain-since-mid-july-over-intensifying-us-iran-tensions-2026-09-04/)
- [SHFE 2026 holiday schedule](https://www.shfe.com.cn/services/calenderandholidays/holiday/)
- [INE trading hours](https://www.ine.cn/eng/reports/calendarholidays/tradingtime/)
- [BLS September 2026 schedule](https://www.bls.gov/schedule/2026/09_sched_list.htm)
- [EIA Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)
- [IEA September 2026 Oil Market Report](https://www.iea.org/events/oil-market-report-september-2026)
- [USDA WASDE release schedule](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
