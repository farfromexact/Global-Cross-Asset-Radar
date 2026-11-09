# 商品期货期权晚间雷达｜2026-11-09

- **生成时间/截点**：2026-11-09 19:32:06 北京时间
- **最新完整中国日盘**：2026-11-09；今晚21:00夜盘归属交易日 **2026-11-10**
- **研究范围**：境内77个实际产品、806个合约；全球映射、产业链、期货、期权与公司利润验证
- **研究性质**：决策支持，不下单；未收到成交回执，实际持仓状态为“未提供/未知”

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；今晚只承担白银回踩确认、铜跨期回撤确认和原油反弹失败三类条件风险，不追21:00缺口。**

机会分层：AG2702、CU2612-CU2701和SC2612存在研究赔率，但均等待21:00后的准确报价和顺序触发；AP701的局部波动率研究仍在，缺bid/ask与净权利金；EC/LC/FG等已研究但优势不足。数据不足不等于无机会：DCE官方核对、A/B级基差、完整期权链及公司当日交易状态仍缺。

最有价值的三个下一窗口观察：

1. **21:15—21:45 AG2702**：外盘银价是否被高开一次性计价，回踩12600后能否15分钟收回12700。
2. **21:15以后 CU2612-CU2701**：1150价差是否先回撤至950—1000、再收回1050；没有回撤不追。
3. **21:00以后 SC2612**：632—638反弹能否失败，同时近远月比率压至1.0%以内且Brent不高于96.50美元/桶。

## 2. 数据质量与覆盖

| 模块 | 实际取得 | 日期/生成 | 就绪度 | 关键缺口与局部影响 |
|---|---:|---|---|---|
| Futures | 806合约、77产品；SHFE 238/INE 63/DCE 214/CZCE 243/GFEX 48 | EOD 11-09；19:01:19 | published、analytically_ready；full_market_ready=true；source-date 100% | 7个占位记录不进排行；无critical error |
| Market State | 77产品；准确合约1/3/5/20D、RV、量仓、曲线 | 11-09 | analytically_ready但history_complete=false | 部分品种缺z值或近远月pair；不把拼接主力当真实收益 |
| Physical | 18/20 | 19:10:18 | available、context | A/B基差=0；全部现货/基差只作背景，不作套利确认 |
| External | 17/22 | 19:10:20 | available、context_only | 公共连续合约快照缺交易所认证时戳；可作方向映射，不作跨境套利 |
| Historical Night | 420/806，52.1092% | 11-06晚至11-07凌晨，归属11-09 | published/validated；coverage incomplete | 214 query_error/unresolved；detail为空；只证明历史会话，**不是今晚** |
| Tonight Night | 0（尚未开始） | 21:00归属11-10 | future window | 不因未来数据不存在扣分；不使用fallback |
| Options | 64目标、44成功、1058样本、44 series | 11-09 19:02:10 | core ATM 44、skew 26；surface/positioning/execution均0 | full_chain=false，bid/ask=0，不能编权利金、PCR、dealer gamma或成交性 |
| Metadata | 上期所/上期能源/郑商所可用 | 11-09 | partial | DCE接口错；GFEX metadata日期错位；受影响参数不猜 |
| Official crosscheck | SHFE238、INE63、CZCE243（close可比183）、GFEX48 | 11-09 19:11 | partial | 真实different=0；DCE HTTP412导致all_equal=false，不代表发现价差；不核量/OI |
| Stock | 5579证券目录、两家公司最小财务包 | trade_date 11-06；research_asof 11-07 | research only | 当日价量/停牌/流动性与执行均未就绪 |

读取路径与固定ref：[Futures](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/latest.json)、[Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/market_state_latest.json)、[Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/physical/latest.json)、[External](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/external/latest.json)、[Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/options/quality_latest.json)、[Options surface](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/options/surface_latest.json)、[Crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/crosschecks/futures_latest.json)。report_input为空，已按协议下钻；商品ref=c391cc55a2e6376a95085236e9564e89d04cc630，Stock ref=c0b7c87287c5562ee4e64d6298b5fa4ffa256d1f。

### 全范围扫描记录

- 黑色9/9：I/JM/J/RB/HC/FG/SA/SF/SM全取；FG量能z=3.62、SM持仓增幅显著，但收盘/结算与实体证据不一致，未入可执行榜。
- 金属17项及新增：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG等全取；AG、CU下钻，SN/SS异常列入观察。
- 能化：SC/FU/LU/BU/LPG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP及实际新增BZ/PG/PL等全取；SC下钻，BU/BR、PP/L/PG/LU列异常。
- 新能源：LC/SI/PS及GFEX实际新增PT全取；LC跌幅与增仓突出，但实体和海外层不足。
- 农产品：A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK全取；AP下钻；DCE官方核对失败局部限制豆油脂等精确定价结论。
- 航运：EC取得日盘与曲线；无夜盘，缺当日运价实体数据，下一窗口11月10日09:00。

### 可追溯事实台账（关键摘录）

| fact_id | 标的/口径 | 观测值与时间 | 支持判断 | 局限/来源 |
|---|---|---|---|---|
| F01 | 五所EOD，CNY合约价 | 11-09，806合约 | 全市场初筛有效 | vendor核心，不等于全官方认证；[数据](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/latest.json) |
| F02 | official settlement/close | SHFE/INE/CZCE/GFEX different=0 | 重点价格未见可信差异 | DCE HTTP412；不核量仓；[crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/crosschecks/futures_latest.json) |
| F03 | 历史night | trading_date=11-09，start=11-06 | 日历归属合法 | 非今晚、非官方终收；[status](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/night_session/last_run_status.json) |
| F04 | options core_v1 | 44/64，ATM44，skew26 | 局部IV/skew可研究 | execution=0；[surface](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/options/surface_latest.json) |
| F05 | 外盘公共快照 | 19:10：银52.525、LME铜13853、Brent96.42、WTI89.43 | 今晚贵金属偏高开、油偏低开先验 | context_only，无交易所认证时戳；[external](https://github.com/farfromexact/China-Commodities-Engine/blob/c391cc55a2e6376a95085236e9564e89d04cc630/data/external/latest.json) |
| F06 | AG2702 | close12632/settle12610；5D +6.95%；ΔOI +8065 | 趋势、参与度与外盘同向 | IV45.45>RV39.87，追价成本高 |
| F07 | CU2612-CU2701 | close/settle spread均1150 | 近月韧性仍在 | 已离950—1000入场区；两腿OI分化 |
| F08 | SC2612 | high645.8、close631、settle637.6；curve close 7 | 旧多头reclaim646未发生；反弹失败可研究 | backwardation反对直接追空 |
| F09 | 中国CPI/PPI | 09:30发布：CPI同比0.7%、核心0.8%、PPI环比0.7%/同比5.7% | 工业品通胀仍高但食品弱 | 宏观不能替代品种实体证据；[NBS](https://www.stats.gov.cn/sj/sjjd/202611/t20261109_1965796.html) |
| F10 | Brent/WTI | Reuters 10:11 GMT：97.57/90.45 | 缓和言论压油 | 航运袭击仍是反证；[Reuters](https://www.reuters.com/business/energy/oil-falls-open-trump-says-fresh-iran-attacks-unlikely-2026-11-08/) |
| F11 | 紫金Q3，人民币/吨/千克 | 9M归母575.26亿元、OCF842.76亿元；矿产铜815,721吨、金70,130千克、银348,413千克 | 价格/产量共同解释利润，不是单一商品beta | 旧Q3披露，不是今日公司催化；[原报](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF) |
| F12 | 宝钢Q3 | 钢材售价、销量/结构与原料共同决定利润 | 拒绝“原料跌=钢企必利好” | 当日证券状态未核；[SSE](https://www.sse.com.cn/assortment/stock/list/info/announcement/index.shtml?productId=600019) |

## 3. 12项目盘

| 标的 | EOD close/settle | 1D/5D与量仓 | 曲线/实体 | 海外/Options | 信号 |
|---|---|---|---|---|---|
| AG2702 | 12632/12610 | settle +0.28%；5D +6.95%；ΔOI +8065 | curve z 2.37 | 银52.525；ATM IV45.45，skew不可用 | 回踩确认多，不追高开 |
| CU2612-2701 | spread 1150/1150 | CU2612 ΔOI -3691；2701 +1455 | 近月升水 | LME 13853；2612 IV17.20、RR25 -7.11 | 只等950—1000回撤 |
| SC2612 | 631/637.6 | close -0.91%；5D -14.24%；ΔOI +1117 | close curve +7，backwardation | Brent96.42；SC2701 IV60.14 | 反弹失败空，曲线反对追空 |
| AP701 | 5860/5887 | settle -1.37%；5D +2.01%；ΔOI -12816 | 现货缺A/B | IV35.61 vs RV37.20；RR25 -1.82 | 长凸性待询价 |
| FG701 | 888/900 | close -0.45%、settle +0.90%；vol z3.62；ΔOI +26716 | curve -1.21%；C级现货 | IV25.75、RR25 +2.10 | 量大但方向冲突 |
| LC2701 | 87480/89760 | close -4.85%；ΔOI +9104 | C级现货92500 | IV54.07 vs RV42.5 | 一层下压，不追空 |
| BR2612 | 15750/15745 | settle +1.42% | close backwardation +210 | IV37.07、RR25 -2.44 | 能化相对强，不单做 |
| BU2612 | 4610/4630 | close -2.94%；5D -15.49% | backwardation 9.91% | IV47.97 | 价格与曲线冲突 |
| EC2612 | 2351.5/2317.5 | close近0；5D -10.37%；ΔOI -130 | contango -6.17% | 无期权/当日运价 | 趋势空观察 |
| SN2612 | 346560/348900 | settle +0.75%；5D -4.23% | backwardation约1.21% | IV39.70、RR25 -10.11 | 禁止追空 |
| AU2612 | 882.76/877.06 | close +0.40%；5D +4.51%；ΔOI -3132 | 曲线轻微 | 金4108.6；IV22.65>RV18.95 | 外盘偏多、期权不便宜 |
| PP2701 | 9341/9461 | close -1.63%；5D -10.42%；ΔOI +21034 | curve z2.18 | DCE官方核对缺 | 价跌仓增只作线索 |

## 4. 相比前序的真变化

1. **EOD更新**：前序晨报使用11月6日EOD；现已取得11月9日全五所vendor EOD。官方核对除DCE接口外未发现价格差异。
2. **贵金属新增弹性**：AG2702的5日趋势和增仓与19:10外盘银价同向，但中国夜盘尚未开；“可能高开”不等于可追。
3. **铜观点不变、赔率未改善**：价差由晨间观测附近回到1150，仍高于入场区。外盘铜13853支持逻辑，国内两腿OI混合降低技术确信。
4. **原油方向修订**：旧SC多头计划要求reclaim 646，日高只有645.8，未满足；收盘631与油价走弱使新研究转向“反弹失败空”，但backwardation保留最强反证。
5. **苹果降分**：ATM IV 35.61%仅略低于RV20 37.20%，而bid/ask仍缺；由70降至68，保留研究、不包装为便宜期权。
6. **数据能力变化**：Options成功产品44/64、skew-ready 26；完整曲面、positioning、execution仍全为0。

## 5. 产业链与传播路径

1. **金银—美元/实际利率—国内AG/AU—紫金利润桥（中高置信）**  
   外盘银/金相对中国15:00后偏强 → 21:00存在高开，但美国CPI将在11月10日21:30重置美元与实际利率。紫金9M矿产金同比增长、矿产银增长，售价/单位成本改善支持利润；但库存、套保、汇率、Capex和少数股东未量化，股票不是AG2702的干净替代。直接期货更纯粹，股权只作中期经营验证。

2. **铜矿—LME/SHFE—近远月—紫金（中置信）**  
   LME 13853与国内近月升水支持CU期限韧性；但2612 OI下降、2701 OI上升，可能含移仓，不能叫“新多”。紫金矿产铜9M 815,721吨低于上年829,903吨，Q3 281,313吨高于Q2 275,193吨：销量并非单向放大，售价/成本才是利润桥主驱动。

3. **地缘—Brent/WTI—SC/FU/LU/BU/PG（中置信）**  
   缓和言论压Brent/WTI → SC反弹失败空的外盘层成立；但霍尔木兹航运袭击、炼厂火灾与SC backwardation共同构成反证。BU价格跌而曲线陡峭、BR相对强，说明不能把全能化简化为单向油价交易。

4. **煤—玻璃/纯碱—建筑需求（低中置信）**  
   FG量能与增仓显著，SA减仓，二者期权RR均偏正；但close/settle冲突、基差仅C级、库存与加工利润缺独立变化，因此不做FG-SA相对价值单。

5. **果品—AP库存/天气—局部波动率（中低置信）**  
   AP跌价伴随减仓，IV略低于RV；这支持询价长凸性，不支持已验证方向。WASDE并非苹果直接供需报告，不能硬写成AP催化；下一有效价格窗口为11月10日09:00。

### Stock限定补证与表达比较

- **紫金矿业**：9M营业收入2834.53亿元、归母净利润575.26亿元、OCF842.76亿元；矿山金销售价/毛利率与铜精矿价/毛利率上升，矿产金量增、矿产铜量同比降但Q3环比回升。最强竞争解释是高利润来自价格、品类组合与项目并表，而非今晚银价单点。若金银铜回落且单位成本上升、Q4产量/毛利率不守，净受益判断被推翻。
- **宝钢股份**：原料回落只有在钢材售价、销量、产品结构与库存损益不恶化时才传导为利润；旧Q3毛利证据不支持用股票替代黑色单边。两家公司当日证券状态未核，均非即时表达。
- 本期限定检索范围为这两家映射公司的交易所公告/IR，未发现Q3之后足以改变商品方向的新经营披露；新增公司候选0。

## 6. 统一机会榜

| 排名 | 机会/idea_id | 方向/期限 | 逻辑/赔率/催化/价曲波/技术 | 总分 | 五层支持；反证/缺失 | 三轴状态 |
|---:|---|---|---|---:|---|---|
| 1 | AG2702 gap absorption / COM-E-AG2702-EXTERNAL-SILVER-GAP-ABSORPTION-LONG-20261109 | 条件多，1—5D | 19/16/16/13/8 | **72** | 支持1/2/4；反对5；缺3 | 优先 / 3层 / 未执行 |
| 2 | CU2612-2701 / COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106 rev7 | 多近空远，1—10D | 20/17/15/12/7 | **71** | 支持1/2/4；反对5；缺3 | 优先 / 3层 / 未执行 |
| 3 | SC2612 failed rebound / COM-E-SC2612-DEESCALATION-FAILED-REBOUND-SHORT-20261109 | 条件空，1—5D | 19/15/15/10/9 | **68** | 支持1/4；反对2/5；缺3 | 重点 / 2层封顶 / 未执行 |
| 4 | AP701 local vol / COM-M-AP701-LOCAL-VOL-CONVEXITY-WATCH-20261107 rev4 | 双向凸性，1—20D | 18/16/13/12/9 | **68** | 支持1/5；价格层内部反证；缺3/4 | 重点 / 2层 / 待询价 |
| 5 | EC2612 contango short / COM-M-EC2612-CONTANGO-TREND-SHORT-20261106 rev5 | 条件空，1—10D | 17/14/14/10/9 | **64** | 支持1/2；缺3/4/5 | 观察 / 2层 / 日盘待核 |

评分仅代表研究优先级，不是胜率。所有分项均已重算，未用0/null冒充未知赔率。

## 7. 研究/交易卡

### 卡1｜AG2702外盘银价缺口吸收多

- **新增事实**：AG2702 close/settle 12632/12610，前结12575；5D +6.95%，ΔOI +8065；19:10外盘银52.525美元/盎司。
- **市场已定价**：日盘已体现趋势，ATM IV45.45%高于RV20 39.87%，凸性并不便宜；今晚高开可能一次性消化外盘。
- **分歧/PnL来源**：只赚“高开后回踩不破、再度走强”，不赚开盘追价。最强竞争解释是美元/实际利率在美国CPI前反转，使高开成为兑现。
- **触发（AND且顺序）**：21:00开盘相对12632不高于+1.5% → 回踩12600并保持5分钟 → 15分钟收盘≥12700 **AND** 可核国际银≥52.30。
- **分批/退出**：确认后50%，再15分钟守12700加50%；stop12480；TP1 13050、TP2 13400；11月13日日盘收盘前退出。直接≥12850未回踩、银<51.80、盘口失真均放弃。
- **好/中/坏成交**：12700/12720/12750；成本与滑点假设450元/手。净风险3750/4050/4500；TP1净R 1.28/1.11/0.90，TP2净R 2.68/2.41/2.07。坏成交只保留TP2赔率，不为TP1追价。
- **合约参数**：15千克/手，tick 1元/千克=15元；夜盘21:00—02:30；最后交易日2027-02-15。AG2702适用涨跌停20%、一般保证金22%（仍须券商盘前复核）。名义189,150元/手；保证金约41,613元。
- **压力**：按前结，一限不利约37,725元/手；两次复合跌停约67,905元。计划止损不保证最大亏损。试仓上限0.50% NAV，手数=floor(0.005×NAV/4500)并再受保证金和流动性限制。
- 参数来源：[SHFE白银](https://www.shfe.com.cn/products/futures/metal/ferrousandpreciousmetal/ag_f/)；[风险参数通知](https://www.shfe.com.cn/publicnotice/notice/202609/t20260921_833503.html)。

### 卡2｜CU2612-CU2701近远月韧性多

- **事实/定价**：close与settle价差均1150；LME铜13853。价差高于950—1000入场区，说明逻辑被部分定价；2612减仓、2701增仓使“需求驱动”解释不唯一。
- **触发**：21:15后先回撤950—1000且全过程不低于800 → 15分钟收回1050 **AND** LME铜≥13750 **AND** 两腿双边深度可接受。50%+50%。
- **参数不追改**：沿用晨报原trigger/stop/TP；仅把下一可验证会话明确为今晚，绝不因日盘OHLC可能穿越就认定已触发或成交。
- **止损/目标**：stop800；TP1 1400、TP2 1650；11月13日日盘收盘/流动性roll前退出。
- **好/中/坏**：950/975/1000，成本500元/对；风险1250/1375/1500；TP1净R 1.40/1.18/1.00，TP2 2.40/2.09/1.83。
- **参数与压力**：每腿5吨，tick10元/吨=50元；夜盘至01:00；9%限幅、一般保证金11%。总名义约1,049,250元；保证金约115,418元；一限静态压力94,433元，两限静态188,865元。试仓上限0.50% NAV。
- **失效**：价差<800，或LME<13750且曲线同步失败；价差不开回撤则不交易。
- Stock比较：紫金能验证中期矿山利润，却混入金/银/锂、产量、套保与公司治理风险，不能替代这组纯期限结构。

### 卡3｜SC2612缓和交易的反弹失败空

- **台账修订**：旧短idea `COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103`已于11月6日到期，保留原失败/到期记录；本卡为新successor。晨报多头idea要求646重夺，今日high=645.8，未满足，且未假设持仓。
- **事实/定价**：SC2612 close/settle 631/637.6，前结636.8；SC2701 close624；close曲线7元（约1.12%）仍backwardation。Brent公共快照96.42，Reuters 10:11 GMT为97.57。
- **分歧/PnL来源**：市场已压低油价，但若外交缓和继续且曲线同步松动，国内反弹失败仍有二次下行；最强竞争解释是航运袭击/炼厂事故扩大、backwardation维持，空头被快速挤压。
- **触发（严格顺序）**：反弹632—638 → 15分钟收盘<628 **AND** 同时近远月比率≤1.0% **AND** Brent≤96.50 → 首次回抽628失败。628/627/626按30/30/40。
- **止损/目标**：stop638；逻辑失效包括Brent>98.50、曲线>1.5%、15分钟收盘≥638或新增供应中断；TP1 610、TP2 595；11月10日22:45前退出。若直接≤615，放弃追空。
- **好/中/坏**：628/627/626；成本1500元/手。净风险11500/12500/13500；TP1净R 1.43/1.24/1.07；TP2 2.74/2.44/2.19。
- **参数**：1000桶/手，tick0.1元/桶=100元；夜盘至02:30；限幅18%、一般保证金20%；当前名义637,600元、保证金约127,520元。一限不利114,624元，两次复合涨停约249,888元。试仓专属上限0.25% NAV。
- **Options替代**：SC2701 ATM630 IV60.135%，skew与execution均未ready，且underlying不是SC2612；不能声称put便宜或限损结构可成交。

## 8. 商品期权专项

样本为11月9日EOD、core_v1/sampled_strikes：64目标、44成功、44 series、1058合约；quote coverage只表示计划采样完成，不是全链。core_atm 44、skew 26、surface/positioning/execution均0，bid/ask 0、model Greeks 0、vendor Greeks按原单位100%，OI覆盖97.83%，dealer净Gamma未知。

- **AG2702**：ATM12600、IV45.45% vs RV20 39.87%；skew不可用。方向候选优先期货，long call/vertical仅作为待询价备选，最大净支出倒推上限0.35% NAV。
- **CU2612**：ATM106000、IV17.20%、RR25 -7.11、BF25 2.265。put skew偏贵是多头反证；不把RR解释为dealer方向。
- **AP701**：ATM5900、IV35.61%、RR25 -1.82、BF25 0.20；IV略低于RV不等于便宜。需准确legs、到期、双边价、总debit和局部Greeks后才可限损。
- **SC2701**：ATM630、IV60.135%，仅ATM-ready；不能映射为SC2612执行价。
- **SN2612**：RR25 -10.11显示采样put偏贵；positioning=false，禁止推全链拥挤/PCR。
- term结构至少需要两个准确可比到期，本期局部样本不满足；不研究wing、完整surface或跨期vol RV。

## 9. 21:00夜盘风险地图

历史night（11月6日晚、归属11月9日）已完成但细节为空，只保留流程证据；今晚归属11月10日，尚未发生。

| 板块/标的 | Previous China EOD | 19:10海外/事件 | 21:00先验 | 15/30/45分钟 |
|---|---|---|---|---|
| AG/AU | 5D上涨，AG增仓 | 银52.525、金4108.6 | 偏高开；不得追价 | 21:15看缺口吸收；21:30看12600/12700；21:45看增量成交与外盘同向 |
| CU | spread1150；近月韧性 | LME铜13853 | 高开/坚挺已部分计价 | 只接受先回撤再收回；无回撤即放弃 |
| SC/能化 | SC close631，曲线backwardation | Brent96.42、WTI89.43；缓和与航运袭击冲突 | 偏低开但挤空风险高 | 21:15看632—638反弹；21:30看628与曲线；21:45再核Brent |
| 黑色/FG-SA | FG巨量、SA减仓 | 无强海外增量 | 低置信分化 | 等close/settle冲突被方向性量仓确认 |
| 橡胶/化工 | BR强、BU/PP/L弱 | 原油偏弱 | 相对强弱可持续但不可跨品种硬套利 | 检查精确合约、单位和相关性；不以单腿代理篮子 |
| AP/EC | 日盘数据有效 | 制度无对应夜盘 | 今晚无交易窗口 | 下一真实窗口11月10日09:00；不写21:00触发 |

若报告被补跑到21:00以后，以上前瞻条件即过期，必须改用实际已核报价重审，不能宣称当时可执行。

## 10. 未来24小时/7日事件（北京时间）

- **11月10日21:30**：美国10月CPI/实际收入；影响USD、实际利率、金银铜油。AG/AU不带满Delta硬扛，期权Vega须先有实价。[BLS](https://www.bls.gov/schedule/2026/11_sched_list.htm)
- **11月11日01:00**：USDA WASDE；豆粕、油脂、玉米、小麦、棉花。无双边报价不做裸事件vol。[USDA](https://esmis.nal.usda.gov/sites/default/release-files/795937/wasde0626v2.pdf)
- **11月11日01:00—01:15**：EIA STEO；核供需路径与地缘风险溢价。[EIA](https://www.eia.gov/outlooks/steo/release_schedule.php)
- **11月13日01:00/03:00**：Veterans Day延后的EIA周度摘要/详表；核库存、炼厂负荷、进出口和产品裂解。[EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **11月13日17:00**：IEA OMR；SC/FU/LU/BU/PG降低事件Delta或仅用已验证有限debit。[IEA](https://www.iea.org/events/oil-market-report-november-2026)
- **CFTC**：11月16日15:30 ET延迟发布，即北京时间11月17日04:30，略超本报告7日截止；此前不编当前拥挤度。[CFTC](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **OPEC+**：本次未核到未来7日正式会议；不把新闻猜测当催化。地缘、霍尔木兹航运、矿山/炼厂意外为持续非定时风险。
- **公司**：本次限定检索紫金/宝钢公告与IR，未发现Q3之后改变本期商品方向的经营披露；若出现产量、套保、检修或长协公告，只在known_at后纳入。

### 发布前校验

- 77产品/806合约扫描、12项仪表盘、5条产业链、Top5/Top3上限：通过。
- 五候选分项加总与层数封顶、AG/CU/SC PnL/净R/压力、币种单位：已实际重算。
- 日历：EOD=11-09；今晚21:00归属11-10；历史night未冒充今晚；AP/EC下一窗口=11-10 09:00。
- MD/JSON的idea_id、方向、分数、触发顺序、专属风险上限同源；schema无法表达的顺序细节完整留在MD。
- 未解缺口：DCE官方核对、A/B基差、night细节、期权bid/ask/完整链/执行、Stock当日交易状态、海外快照认证时戳。
- CI只标记 `pending_or_unverified`；不等待、不轮询。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：AG2702缺口吸收多、CU2612-CU2701回撤再收复、SC2612反弹失败空；三者均须21:00后准确报价与AND顺序触发。
C. 今天继续观察：AP701局部凸性询价、EC2612 contango、FG701量能冲突、LC2701下压、BR-BU强弱及紫金/宝钢利润桥。
D. 今天必须回避或有条件退出：回避追AG/CU高开、SC直接低开追空、任何无bid/ask期权；旧SC多头未触发且研究关闭，若用户另有真实持仓只按原止损/时间退出处理。
