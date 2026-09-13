# 全球商品期货期权高风险机会雷达｜晚间版｜2026-09-13

`prompt_version=radar_2026-09-06_coverage_v1`  
实际生成：19:38 BJT；信息截点：19:30；最近完整中国交易时段：9月11日日盘。今日为周日，今晚无中国商品夜盘；下一日盘为9月14日09:00，下一夜盘为9月14日21:00、归属9月15日交易日。

## 一、今晚一句话结论

**截至本报告时点，无可立即执行的合格新交易；霍尔木兹再现船舶遇袭，SC/FU/EC周一上跳风险增加，但国际期货尚未开盘，必须等待价格确认。**

当前regime：**双航道与替代管道同时受扰、国内能源和航运深backwardation、周末事件风险高但无商品成交验证、热通胀约束金属、WASDE农业信号等待中国定价。**

最接近验证的是FU2611、EC2610和SC2610。缺失条件分别是周一产品端能否继续强于SC、集运是否真实计入红海风险，以及SC高开后能否形成45分钟接受。

## 二、数据质量与覆盖

本期优先读取[统一报告输入](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json)、[核心状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)、[Radar](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/radar_latest.json)，并下钻[逐合约EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)、期权曲面与元数据。

- 统一输入：schema v2，`requested_date=2026-09-11`，9月13日19:09:05生成。
- Futures：嵌入快照仍是9月13日06:03重新核验过的9月11日EOD；五所802合约、77产品，`source_date_match_pct=100%`、`full_market_ready=true`、critical errors=0，4条placeholder已排除。19:01针对周日自然日的刷新返回15个错误、0条新合约；这是非交易日刷新失败，不推翻已验证last-good，也不冒充9月13日行情。
- Market State：19:01生成的紧凑层继续使用9月11日同合约1D/3D/5D/20D；20个交易日历史完整。curve/量仓z-score等缺项不猜测。
- Physical：最近有效观测仍为9月11日，20项中18项在原生频率下可用，SC/LU unavailable；basis全部C级，仅作context。仓单有5条沿用。
- External：19:08刷新，`requested_date=2026-09-13`、source date仍为9月11日最后完整国际时段；17/22可用、5项unavailable，全部`context_only`。15:00—19:30没有WTI/Brent、LME、COMEX、CBOT、DXY、USD/CNH或实际利率的新常规时段报价；沙特股票与周末新闻另列代理/事件。
- Options：最新应得且有效截面仍为9月11日，23,272条chain、384个series、59/64产品；CJ/MA/PL/PR/ZC失败。373个surface-ready、78个positioning-ready、0个execution-ready；IV覆盖98.07%、OI覆盖69.35%、bid/ask覆盖0。
- Metadata：partial；有效合约匹配73.32%，multiplier/tick/margin/limit覆盖约29.8%，重点卡缺项不补猜。

Night状态优先采用module-specific文件：`trading_date=2026-09-13`、`night_session_date=2026-09-12`，06:03:38生成；`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=true`。请求802个合约，有效Night合约0、产品0，802条全部为合法`outside_night_window`；missing timestamp/price/quote、query error及unresolved均为0。

这表示**周末制度性没有Night Session**，不是行情缺失或工具截断。统一输入内嵌的旧9月12日596条快照继续按日历语义隔离；`night_session_fallback_used=false`、`overnight_day_decomposition_used=false`。

## 三、商品仪表盘

以下价格均为9月11日last-good EOD；Current Night为N/A。S/P/E表示surface/positioning/execution readiness。

| 板块/品种 | 合约；close/settle；1D/5D | Volume/OI/ΔOI；curve | Basis/Physical | 15:00—19:30海外/事件；Options | 周一信号 |
|---|---|---|---|---|---|
| 燃料油FU | FU2611；4289/4292；+4.66%/+10.85% | 139.93万/22.09万/+4,920；back 8.69% | C/context | 无新商品报价；管道仍停；Y/Y/N | 产品强于SC才多 |
| 原油SC | SC2610；812.9/809.9；+5.40%/+18.56% | 30.53万/3.50万/+697；back 7.03% | Physical缺失 | 霍尔木兹船舶遇袭；SC2611 Y/N/N | 高开后等45m |
| 集运EC | EC2610；2032/2044；+4.18%/+10.10% | 3.29万/2.59万/+2,200；back 22.36% | exact运价缺 | Hormuz/Perim风险；N/N/N | headline不等于EC盈利 |
| 低硫LU | LU2611；5453/5487；+4.53%/+10.85% | 22.06万/7.68万/+2,433；back 1.88% | Physical缺失 | 供应右尾；新期权未就绪 | 相对FU偏弱 |
| 铜CU | CU2610；108990/108660；-2.75%/-0.41% | 20.93万/19.89万/-35,215；back 0.65% | C/context | LME最后14225.5；Y/Y/N | 反抽失败才空 |
| 白银AG | AG2612；15623/15676；-4.76%/-4.09% | 17.32万/19.34万/+8,788；contango 0.76%、roll | C/context | COMEX最后约64.27；Y/N/N | 不追空 |
| 黄金AU | AU2612；944.94/944.54；-1.36%/-2.93% | 10.48万/15.84万/+7,777；轻contango | C/context | 金最后约4350；Y/N/N | 实际利率与避险冲突 |
| 碳酸锂LC | LC2701；134820/133960；-5.60%/-8.90% | 32.27万/40.76万/-1,124；back 1.68% | basis C；仓单沿用 | 无exact海外；Y/N/N | 不接第一刀 |
| 玻璃FG | FG701；973/984；+2.29%/+1.34% | 218.62万/115.50万/-41,191；contango 7.37% | basis C | 无exact海外；Y/Y/N | 挤压/contango冲突 |
| 焦煤JM | JM2701；1585/1612.5；-1.77%/-3.47% | 87.37万/48.67万/-38,125；back 1.67% | basis C | 无exact海外；Y/Y/N | 不追减仓下跌 |
| 红枣CJ | CJ701；7580/7630；-2.43%/-3.05% | 20.17万/22.52万/+3,946；contango 15.38% | CZCE仓单-261 | chain失败 | 弱价/深contango优先 |
| 豆粕M | M2701；3402/3422；+0.68%/+0.59% | 193.71万/273.38万/-51,707；contango 0.82% | basis C | 美豆最后1280.25；Y/Y/N | 报告未确认多头 |
| 玉米C | C2611；2255/2260；-0.40%/-1.61% | 46.69万/116.20万/-16,426；back 0.22% | C/context | WASDE减产接近预期；Y/Y/N | 高低开均不追 |
| 棕榈油P | P2701；10035/10151；-0.26%/-0.60% | 70.48万/58.33万/-7,195；contango 1.52% | basis C | BMD最后4816；Y/Y/N | 无方向优势 |
| 苯乙烯EB | EB2610；10036/10303；+0.20%/+6.47% | 170.59万/25.50万/-66,811；contango 0.68% | C/context | 上游事件升级；Y/Y/N | 成本扩散仍钝化 |

周五Brent收104.61美元/桶、WTI收100.05，分别回落2.81%和2.37%；这些仍是最后成交价，不能用周末新闻倒推新报价。[Reuters油市，2026-09-11](https://www.reuters.com/business/energy/oil-prices-set-end-week-over-100-first-time-nearly-4-months-2026-09-11/)

周日UKMTO报告一艘船在霍尔木兹遭弹体击中、起火并疏散船员；East-West管道仍处于预防性关闭。事件强化供应右尾，但并未提供周一开盘幅度。[Reuters，2026-09-13](https://www.reuters.com/business/energy/new-report-attack-strait-hormuz-shipping-fans-fears-threats-oil-supplies-2026-09-13/)

沙特股市提供唯一可见的周末交易代理：TASI跌1.0%、Saudi Aramco跌1.1%、Petro Rabigh跌7.3%。这是区域风险反应，不是Brent/SC/FU报价，也不构成可执行跨市场套利。[Reuters沙特股市，2026-09-13](https://www.reuters.com/world/middle-east/saudi-shares-drop-after-drone-attacks-target-key-oil-pipeline-2026-09-13/)

## 四、相比同日晨报真正变化

1. **霍尔木兹出现新的具体船舶遇袭。** 与此前“不会立即重开”的谈判风险相比，这是已发生事件；SC逻辑分+1，但催化已满分，赔率与价格分不增加。
2. **区域股票首次交易管道袭击。** Aramco和Petro Rabigh下跌支持基础设施风险具有经济意义，但它们只能算第4层代理证据，不能替代油价确认。
3. **管道恢复仍未确认。** 截点前没有权威恢复公告；若周一前恢复，能源与航运多头触发必须重新下移或取消。
4. **外交反证仍在。** 9月14日阿曼会谈预计不签署正式协议，但沙特尚未报复、地区仍推动临时交通安排；收益分布不是单向上涨。
5. **19:01周末刷新再次失败。** 根状态`full_market_ready=false`、15个errors描述的是9月13日请求0条新数据；统一输入中的9月11日last-good仍已验证、五所完整。这是状态冲突，按模块和快照日期披露。
6. **期权与实体没有新周末截面。** 最新有效T-1研究层仍可沿用，但不能冒充周一bid/ask或当前Delta。

旧建议台账：

- `COM-E-FU2611-PRODUCT-TIGHT-20260908`：维持77；事件继续支持，但周一是否强于SC仍未知。
- `COM-E-EC2610-HORMUZ-FREIGHT-20260911`：维持77；船舶风险升级，但油轮事故对EC利润映射仍不完整。
- `COM-E-SC2610-GAP-20260905`：73→74；新增船舶遇袭强化逻辑，坏成交与需求破坏仍限制赔率。
- `COM-M-CU2610-TARIFF-UNWIND-20260911`：维持67；无新增LME或国内价格。
- `COM-M-C2611-WASDE-CORN-20260912`：维持56；仅实体一层。
- 没有成交反馈，不假设用户持仓；若此前已按条件建立能源多头，周一首先重算gap风险，不自动加仓。

## 五、产业链地图

- **最强尾部：SC—FU—LU与海运，偏多，置信度中高。** 9月11日价量仓、backwardation及供应/航运事件构成1/2/4三层支持；缺周末商品价格、SC/LU实体、exact运价和执行报价。最强反证是外交安排、管道快速恢复及高价需求破坏。
- **产品强于芳烃聚酯，置信度中。** FU back 8.69%，EB价格钝化、OI大减并转contango；若周一FU不强于SC或EB/BZ反而领涨，不执行原产品相对逻辑。
- **航运：风险高、映射不纯，置信度中。** Hormuz船舶和Perim影响油轮与红海通道，但EC跟踪集装箱运价；缺exact航线、舱位与现货运价，不能把油轮费率当EC套利。
- **有色—贵金属方向冲突，置信度中低。** CU价格/OI支持关税溢价回吐，国内back反对追空；AU/AG面临热通胀与地缘避险的相反力量。黄金信用主题本期仍不成立。
- **最弱价格链：LC/PT/PD与黑色，置信度中低。** 单日下跌、减仓和反向curve不足以证明实体需求崩塌；周一避免接第一刀也避免追空。

## 六、机会排行榜

| 排名 | 机会 | 逻辑/赔率/催化/价曲波/仓技 | 总分 | 支持层 | 判断｜证据｜执行 |
|---|---|---:|---:|---|---|
| 1 | FU2611产品链延续多 | 23/14/20/12/8 | **77** | 1、2、4 | 存在待验证优势｜部分｜休市，周一等30—45m |
| 2 | EC2610航运冲击多 | 23/15/20/11/8 | **77** | 1、2、4 | 存在待验证优势｜部分｜休市，周一日盘触发 |
| 3 | SC2610高位接受多 | 24/10/20/12/8 | **74** | 1、2、4 | 存在待验证优势｜部分｜休市，周一等45m |
| 4 | CU2610关税回吐空 | 19/15/14/9/10 | **67** | 1、4 | 存在待验证优势｜部分｜反抽失败才空 |
| 5 | C2611 WASDE玉米减产多 | 16/13/14/5/8 | **56** | 3 | 证据不足｜不足｜等待中国价格确认 |

分项均已复算。新闻新鲜度不等于独立证据层；FU/SC/LU/EC共享供应—运输因子，不能作为四笔独立风险叠加。所有期货最大损失均不受结构限定。

## 七、前三名交易卡

### FU2611｜条件多｜77

事实：9月11日OHLC 4268/4417/4201/4289，settle 4292，1D +4.66%、5D +10.85%，ΔOI +4,920，back 8.69%。今晚无Night；15:00—19:30无新油价。

- 市场隐含：产品短缺和运输风险已大幅计价。分歧是FU可能比SC更耐久；最强竞争解释是周五只属成本补涨。
- 窗口：9月14日09:00后等30—45分钟，首跳不追。
- 好成交：4210—4260获接受并重上4295/VWAP，先1/3仓；中成交：突破4418后回踩成功，仓位减半；直接高于4450为坏成交。
- 止损：30分钟接受4190下方；失效：跌破4100、back明显收窄且Brent低于100，或管道恢复并伴随运费回落。
- TP1 4420或1.5R；TP2 4600或3R；1—3D无扩张退出。
- 风险0.25%—0.35% NAV，与SC/LU/EC合并；滑点超过计划1R的20%放弃。
- 10吨/手，tick 1元/吨，tick value 10元；名义42,920元。动态margin/limit未确认；最后交易日10月30日，实物交割。
- 一板压力=`42,920×L`；两板=`42,920×[1-(1-L)^2]`，L下单前核验。

### EC2610｜条件多｜77

事实：9月11日OHLC 2015.5/2108/1976/2032，settle 2044，1D +4.18%、5D +10.10%，ΔOI +2,200，back 22.36%。EC制度上无夜盘。

- 市场隐含：绕行和近端运力稀缺已部分计价。分歧是双航道事件可能延长风险；竞争解释是油轮受袭不等于集装箱运价上升。
- 窗口：9月14日09:00后等30分钟。
- 好成交：1990—2035获接受并重上2045/VWAP；中成交：突破2110并回踩不破；直接高于2160放弃。
- 止损：30分钟接受1970下方；失效：跌破1962、back收窄且通航/管道确认恢复。
- TP1 2150或1.5R；TP2 2300或3R；1—5D时间止损。
- 风险0.25%—0.35% NAV，与能源/航运主题合并。
- multiplier、tick、margin、limit及最后交易日未确认；参数补齐前不得实际下单，也不编一板、两板金额。

### SC2610｜条件多｜74

事实：9月11日OHLC 815/838.3/786.5/812.9，settle 809.9，1D +5.40%、5D +18.56%，ΔOI +697，back 7.03%。周日新增Hormuz船舶遇袭，但没有新油价。

- 市场隐含：供给中断已形成高位back；分歧是替代管道和Hormuz同时受扰仍可能未被周五价格完全计入。反证是外交缓和、需求破坏和管道快速恢复。
- 窗口：9月14日首跳不追，等45分钟。
- 好成交：790—810承接并重上813/VWAP；中成交：突破838.5后成功回踩；直接高于850、接近涨停或止损距离超过1R放弃。
- 止损：45分钟接受786下方；失效：跌破768.4、back收窄、Brent低于100且管道恢复。
- TP1 840或1.5R；TP2 875或3R；1—2D不扩张退出。
- 风险0.20%—0.35% NAV，与FU/LU/EC合并；不因新闻升级提高仓位。
- 1,000桶/手，tick 0.1元/桶，tick value 100元；名义809,900元。最后交易日9月30日，实物交割；最迟9月18日前复核移仓SC2611。[INE合约](https://www.ine.cn/eng/market/futures/energy/sc/contract/)
- 9月14日夜盘起相关合约风控调整；按16%压力假设，一板约129,584元/手，两板复合约238,435元/手。[Reuters风控摘要](https://www.reuters.com/business/energy/shanghai-exchange-adjust-trading-limits-some-oil-futures-contracts-2026-09-11/)

## 八、商品期权专项

最新有效截面为9月11日EOD；周末事件后moneyness、Delta、IV和成本均可能跳变。

| Underlying/expiry | ATM IV/RV20 | IV-RV | RR25/BF25 | S/P/E | 结论 |
|---|---:|---:|---:|---|---|
| FU2611/10-19 | 64.47%/43.35% | +21.11vol | -3.19/-0.62 | Y/Y/N | 事件凸性已贵，周一重报价 |
| SC2611/10-14 | 60.92%/41.07%代理 | +19.84vol | -1.68/+2.16 | Y/N/N | 非SC2610同底层，仅context |
| CU2610/09-23 | 15.17%/14.80% | +0.36vol | +0.80/+1.89 | Y/Y/N | IV-RV近零不证明可成交便宜 |
| AG2612/11-24 | 51.14%/35.16% | +15.98vol | +6.33/+8.34 | Y/N/N | 上行尾偏贵、positioning不足 |
| LC2701/12-07 | 43.64%/38.62% | +5.02vol | 未稳定 | Y/N/N | 周一重算Delta |
| FG701/12-11 | 21.93%/18.86% | +3.07vol | +7.89/+3.29 | Y/Y/N | 无bid/ask |

期权目前没有优于裸期货的**可执行证据**，但不代表所有期权昂贵。周一只有取得目标底层、到期、两腿数量及实时双边报价后，才能比较FU/SC有限净支出call spread；当前不发布权利金、Greeks或最大净支出。Dealer Gamma方向未知。

`research only; manual quote and manual confirmation required before execution; no premium quoted`

## 九、下一实际开盘风险地图

四层时间轴：①9月11日中国EOD；②周末没有已完成Night；③9月11日国际最后收盘；④9月13日Hormuz船舶事件及沙特股票代理反应。今晚21:00无中国夜盘；下一实际交易窗口为9月14日09:00。

| 品种 | EOD→周末新增 | 周一可能gap | 等待 | 核心确认 |
|---|---|---|---|---|
| FU/LU | 强back→管道未恢复、Hormuz再遇袭 | 高开右尾、也可能利多兑现 | 30—45m | FU守4210/4295、产品强于SC |
| SC | +5.4%/back7%→直接船舶风险 | 宽幅高开概率上升 | 45m | 786/810/813/838.5、Brent、管道 |
| EC | +4.18%/back22%→双航道风险 | headline高开但映射不纯 | 30m | 1970/2045/2110、实际绕行及现货运价 |
| EB/BZ/TA/PX | 国内弹性衰减→上游事件增强 | 跟油分化 | 45m | settlement、OI、curve、FU/SC breadth |
| CU | 国内弱但back→无新LME | 平/低开后反抽 | 45m | 108180/109200、LME、back |
| AG/AU | 中国跌、海外周五反弹→无新利率 | 双向 | 30—45m | DXY、10Y实际利率、换月价差 |
| C/M/Y/P/OI | 中国未交易WASDE→无新CBOT | 报告影响不确定 | 45m | 中国gap、OI、near-next、CBOT电子盘 |
| LC/PT/PD | 急跌、实体不足→无Night | 宽幅双向 | 45m | OI、curve、仓单有效期、交易所参数 |
| FG/JM/RB | 价格与curve冲突→无新信息 | 震荡/偏弱 | 30—45m | FG963/1010、JM1580、钢材breadth |
| AP/JD/SF/SM/SI/PS | 制度无Night、无exact外盘 | 国内信息主导 | 30—45m | 量仓、curve、实体更新 |

周一06:00后必须刷新Brent/WTI、Hormuz会谈预期、船舶损伤、管道状态、红海通航、DXY/CNH、实际利率和CBOT电子盘。当前触发均为计划锚，不是已验证信号。

## 十、未来24小时与7天事件

- 未来24小时：Hormuz遇袭船舶损伤、East-West管道恢复时间及Perim/曼德海峡通航；任何恢复都会压缩SC/FU/EC事件溢价。[Reuters Hormuz](https://www.reuters.com/business/energy/new-report-attack-strait-hormuz-shipping-fans-fears-threats-oil-supplies-2026-09-13/)
- 9月14日：阿曼主持伊朗与海湾国家会议。现有信息显示不预计签署正式协议；只按可验证交通安排调整Delta。[Reuters会谈](https://www.reuters.com/world/middle-east/no-signed-hormuz-deal-expected-yet-oman-meeting-monday-iranian-official-says-2026-09-12/)
- 9月14日09:00：中国商品日盘重开；所有旧条件至少延迟30—45分钟验证。
- 9月14日09:30：中国流通领域生产资料价格窗口；9月15日10:00工业、投资、消费、房地产及能源数据，以[国家统计局](https://www.stats.gov.cn/)实际日程为准。
- 9月14日21:00：下一合法中国夜盘，归属9月15日；核验SC/LU新限幅、保证金与开仓限制。
- 9月15—16日美国时间FOMC，决议约9月17日02:00 BJT：CU/AU/AG提前降低Delta/Vega。[美联储](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)
- 9月16日EIA周报常规窗口：关注成品油库存、炼厂开工、出口及战略库存。[EIA](https://www.eia.gov/petroleum/supply/weekly/)
- CFTC COT仅作滞后拥挤背景，不映射为中国会员确定方向。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)

## 十一、覆盖、风险与归档核对

强制63个代码全部完成9月11日last-good价格、同合约1D/3D/5D/20D、量仓、curve，以及方向、基差、跨期、跨品种/跨市场、加工利润、风格/中性、波动率、偏度和事件凸性扫描；另纳入动态品种，统一输入共77个产品。

- 实际有效取数并分析70个；JR/PM/RI/WH/ZC为占位，RS/WR流动性不足。
- 黑色建材9/9：FG深contango、JM价曲冲突最显著，未发现三层方向优势。
- 有色贵金属12/12：CU入榜；AG/AU宏观与避险冲突。
- 能源炼化化工25/25：FU/SC入榜；LU相对偏弱，EB/BZ/EG/TA/PX成本扩散钝化。
- 新能源及GFEX新材料全部扫描：LC/PT/PD缺新鲜实体与海外确认。
- 农产品油脂饲料畜牧22/22：C低分观察；M/P/Y/OI等待中国对WASDE定价。
- 航运与软商品全部扫描：EC入榜；CJ仓单变化不足以抵消弱价及深contango。
- Current Night应为0且实际0；旧9月12日快照隔离。
- 期权应覆盖64个、实际59个；5个产品不足，0个execution-ready。
- A/B级basis、exact import parity、可靠加工利润与beta-neutral篮子不可得，不发布伪套利。

风险预算：今晚休市，不新增风险。周一单笔试仓最大损失0.20%—0.35% NAV；取得新增价格和非价格层确认后才提高至0.75%—1.0%。FU/SC/LU/EC初始合并风险不超过0.75%。压力测试包括16%单板、两板复合、周末gap、流动性消失、保证金上调、相关性破裂、管道突然恢复及人民币急变。

固定六路径已从main回读验证：历史MD/JSON存在，latest日期与edition正确，status对应本期，manifest中`2026-09-13 + commodities_evening`恰好一条。[正式归档报告](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/09/2026-09-13_commodities_evening.md) `archive_status=success`，`ci_validation_status=pending_or_unverified`。

A. 今晚没有应立即建立的新仓位。  
B. 今晚只应挂条件单的仓位：无；周日无中国21:00夜盘，FU2611、EC2610、SC2610全部移至9月14日09:00后30—45分钟验证。  
C. 今晚应继续观察的机会：Hormuz遇袭后管道与通航状态、FU相对SC强度、EC航运back、CU关税回吐，以及WASDE后C/M/P/Y/OI的中国价格确认。  
D. 今晚必须避免或退出的交易：把周末事件倒推成油价、周一首跳追FU/SC/EC/C、把油轮费率或沙特股票当EC exact套利、追空CU/AG/LC，以及在execution-ready=false时臆测期权成本。
