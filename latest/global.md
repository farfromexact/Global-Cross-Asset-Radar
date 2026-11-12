# 全球跨资产 Radar｜人工完整研究

- run_id：`20261112T234244+0800_5eb01e91f7534ca58a37d7036a7fddde`
- 共同研究截点／实际启动：北京时间2026-11-12 23:42:44（UTC+08:00）；UTC `2026-11-12T15:42:44Z`。
- 本文生成：`2026-11-12T16:03:47Z`，生成时刻不替代研究截点。
- Prompt：`on_demand_2026-11-12_v3`；Registry `35a9f798618284fd585fb5e199c1f60e5a05de62`。
- 商品Commit：`1db709dcf61a7f032747c1702673b3f78255ef8e`；期权Commit：`a4c16a18d16d039a30e9c162950096c9333a0a49`。
- 模式：`production`；`trigger=manual`；`execution_enabled=false`。
- 研究状态：完整范围已研究，具体数据/执行限制在各栏；机器表示非完整执行合同。

## 1. 结论

混合型通胀与治理风险：高实际利率压制贵金属，AI业绩分化仍强；铜曲线强化、豆粕价差转弱。优先研究AI相对价值与铜期限结构，不追已过窗口；中国风格缺当日确认。无立即新仓。

## 2. 全球仪表盘

### 会话与信息边界

共同截点为北京时间 **2026-11-12 23:42:44／UTC15:42:44**：中国股票/股指日盘结束，美国冬令时10:42:44，距09:30开盘已72分44秒；不能再提交本日开盘30—45分钟计划。美国11/11完整权益收盘可用，11/11现金美债是假日。中国商品本晚归属11/13交易日：M等常规23:00段已结束，AU/AG/SC等长夜盘尚处常规窗口，**仓库只提供前一晚数据**，本晚路径一律未知。下一中国常规日盘为11/13；股指09:30、各商品按制度09:00等分别处理，临时公告与账户状态仍须执行前复核。[NYSE时段与节假日](https://www.nyse.com/trade/hours-calendars)；[SH-COM-NIGHT-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/night_session/latest.json)。

| 资产 | 可核数值 | 1D／周变化或明确缺项 | 观测/属性 | 研究信号 |
|---|---|---|---|---|
| 美债2/5/10/30Y | 4.73／4.81／4.98／5.35% | 相对11/9 +17／+14／+10／+9bp；相对11/3 +12／+7／+3／+3bp | 11/10财政部日频；11/11现金债假日 | 通胀/政策前端重估强于远端；非实时 |
| 曲线/实际/BEI | 2s10s25、2s30s62、5s30s54bp；real10Y2.78%；粗BEI2.20% | 2s30s日−8bp、七日−9bp；real10Y日+12bp | 11/10同日曲线相减 | 更像真实折现率冲击；期限溢价最新值缺 |
| DXY | 缺同截点有效报价 | 1D/周缺 | 官方/可靠源检索未取可比值 | 不凭美元标签解释全部资产 |
| EUR/USD | 1.1154 | 11/6对11/5约−0.72%；周缺 | H10纽约午盘11/6；11/9发布 | 低频利差背景，非当前卖欧元触发 |
| USD/JPY | 158.23 | 11/6对11/5约+0.30%；周缺 | 同上 | carry顺风可被日元挤空推翻；FX skew缺 |
| USD/CNH | 缺；另有USD/CNY6.6760 | CNY11/6对11/5约+0.12%；CNH不算 | H10 onshore不替代offshore | 中国流动性与进口成本传导待同步汇率 |
| Nasdaq / QQQ | Nasdaq25466.19；QQQ未取得 | Nasdaq11/11 +1.597%；同口径周缺 | Nasdaq11/11完整收盘；美国现已11/12盘中 | 反弹不证明NVDA新治理消息已充分消化 |
| SOXX / SMH | 市价155.40／506.96美元；比0.306533 | SOXX NAV+6.07%非市价涨幅；SMH市价+4.824%；周缺 | 11/11收盘；SOXX官方、SMH可靠二手 | Q=58.60美元已高于旧计划20—40区；不能当11/12触发 |
| WTI / Brent | 86.77／92.97美元/桶，仅旧context | 不可比1D/周 | External标11/11，生成19:12BJT，非当晚美盘收盘 | 精确月份/曲线缺；国内SC单独分析 |
| COMEX / AU黄金 | COMEX4059.3美元/盎司仅context；AU2612 852.5元/克 | AU日收−2.382%；COMEX1D/周不可比 | AU11/12 EOD；海外旧错时context | 黄金对高实际利率仍敏感，不宣称脱钩 |
| VIX / MOVE / HY OAS | VIX17.49；MOVE缺；HY3.30% | VIX可比日/周未取；HY11/9→11/11 −4bp，11/4→11/11 −2bp | VIX11/11前收；HY11/11收、11/12 13:51Z发布 | 信用尚无系统性失序证据；期限、CTA、净Gamma缺 |

上表来源：[G-US-RATES-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)、[G-US-REAL-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026)、[G-FX-20261106](https://fred.stlouisfed.org/series/DEXJPUS)、[EUR/H10](https://fred.stlouisfed.org/series/DEXUSEU)、[CNY/H10](https://fred.stlouisfed.org/series/DEXCHUS)、[G-NASDAQ-20261111](https://fred.stlouisfed.org/series/NASDAQCOM)、[G-SOXX-20261111](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf)、[G-SMH-20261111](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/)、[SMH历史市价](https://uk.marketscreener.com/quote/etf/VANECK-SEMICONDUCTOR-ETF--29426371/quotes/)、[G-VIX-20261111](https://www.cboe.com/tradable-products/vix/)、[G-HY-20261111](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)、[SH-COM-EXTERNAL-20261111](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)。不同市场/频率并列是风险地图，不据此计算同步相关性。美元日变化从两日H10数值重算；周窗口缺时不以3天替5天。

### 中国主次合约、现货与可比收益

| 产品 | 主合约/close | 次合约/close | 现金指数 | 主basis点/年化 | 同合同1D/5D | 时点限制 |
|---|---|---|---|---|---|---|
| IH | IH2612 2,742.20 | IH2703 2,704.40 | 2,765.54 | -23.34 / -8.33% | -0.33 / -1.22% | 11/11EOD；11/12新价未取得 |
| IF | IF2612 4,043.40 | IF2703 3,982.60 | 4,075.71 | -32.31 / -7.82% | +0.47 / -0.68% | 11/11EOD；11/12新价未取得 |
| IC | IC2612 6,664.00 | IC2703 6,528.20 | 6,713.18 | -49.18 / -7.23% | +1.34 / +1.30% | 11/11EOD；11/12新价未取得 |
| IM | IM2612 6,623.00 | IM2703 6,478.20 | 6,669.55 | -46.55 / -6.89% | +1.63 / +2.38% | 11/11EOD；11/12新价未取得 |

年化=(F/S−1)×365/到期自然日，主合约12/18、37天以11/11观察日计算，**不是融资分红调整后的无风险套利收益**。完整量仓、次合约基差、1/3/5/20在第8栏。来源[G-CN-INDEX-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json)。

| 系列 | 到期日（引擎推断） | 报价中点ATM% | official-EOD ATM% | EOD同系列1D变动vol点 | EOD同系列5D变动vol点 |
|---|---|---|---|---|---|
| HO2611 | 2026-11-20 | 14.038 | 13.445 | -0.835 | -1.184 |
| HO2612 | 2026-12-18 | 14.648 | 14.340 | -0.404 | -1.315 |
| IO2611 | 2026-11-20 | 17.963 | 17.267 | -0.339 | -2.223 |
| IO2612 | 2026-12-18 | 17.789 | 17.666 | -0.340 | -1.754 |
| MO2611 | 2026-11-20 | 29.220 | 28.147 | -2.381 | -7.886 |
| MO2612 | 2026-12-18 | 27.948 | 27.579 | -1.630 | -6.393 |

HO/IO/MO的12月期限结构与25Δ/10Δ wings见第8栏。报价中点和官方结算/fallback-close是两条口径，不能用它们相减当“IV今日上升”。[G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json)。

### 商品输入与实体来源紧凑附录

11/12五所806合约、77产品全扫描；Night494记录/55产品属于11/11晚至11/12凌晨，OI/ΔOI空；Physical18/20仅C级现货、没有独立供需变化；External22目标/17有效但仅context。商品期权64系列/470样本合约，61 ATM可用、仅C与AU两组skew，bid/ask覆盖0，全曲面/全链持仓/执行均未就绪。SC市场状态主力是2701，其RV38.979%与IV52.05%同月；**不能移作SC2612卡的自身IV/RV**。商品RV只是有缺口历史的20观察值估计，非连续20交易日。官方crosscheck本批未完成，Wind EOD与官方独立核验不得混称。公开公司样本为3家原始披露，不能把局部经营证据变成全部商品实体层确认。[SH-COM-COVERAGE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[SH-COM-OPTIONS-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)。

### 三条跨资产机制

**利率：**10月核心环比0.3%与能源0.7%尚未允许把通胀风险消去；2年上行17bp而30年9bp支持“政策利率更久偏高”的竞争解释，10年实际上行12bp说明折现率压力并不只来自通胀补偿。原2s30s压平研究仍有机制基础，62bp曲线已吸收部分冲击；若30年供给溢价主导、远端先上行则该表达失效。缺OIS和期限溢价模型，不能把曲线变化完全归于Fed或财政失信。[G-US-CPI-202610](https://www.bls.gov/news.release/cpi.nr0.htm)、[G-FED-20261028](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)。

**FX：**旧H10美元相对欧元/日元偏强与高实际利率方向一致，但不能拼接为11/12的同步美元因子。日元carry面临政策与去杠杆反转；CNH走弱若伴DR007收紧才可能加重中国风险，单独汇率变化也可能是美元共同冲击。当前无CNH、DR007/中国国债的同日原始值，保留机制，暂不建立外汇方向仓。

**能源与风险：**SC日涨0.977%而近远月close差12.1→10，说明绝对价格修复没有同幅加强近端紧缺，减仓1646手也不能自动称新多。EIA库存尚未公布，早先API/媒体传闻不作原始供需层；成本冲击可推高化工售价，也可在需求弱时压缩加工利润。VIX前收17.49和HY330bp可与股票反弹共存，却不足以否定治理事件、债券拍卖或长短腿相关性断裂。现阶段更适合控制共同因子，而非把全部商品/股债当统一Risk-on。[SH-COM-SC-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[SH-COM-SC-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[SH-COM-EIA-CALENDAR-20261112](https://www.eia.gov/petroleum/supply/weekly/schedule.php)。

## 3. Delta Research

比较基准为同领域正式legacy **2026-11-12_morning_revision_1**，截点UTC00:05、北京08:05，实际生成08:05:54；索引published、archive success，固定归档commit `617f65af0f42a6065eac66e325d6ec2223a0c4ee`逐文件读取。新格式成功索引尚无前序，未采用v2隔离实验。旧稿只证明此前观点，不当当前事实。基准[全文](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-12_morning.md)、[JSON](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/2026-11-12_morning.json)。

| 主题/变化 | previous | current | 原因与处置 |
|---|---|---|---|
| AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106；strengthened | 前序72分；将多SOXX/空SMH解释为ETF权重相对价值，待回踩和借券。 | NVDA领导层调整是截点前新增治理事件，集中度差的重要性上升；当下错价仍未被同步报价证明，当前待评分。 | 原件与13:54:02Z可得上界已核；此前收盘发生在事件之前，不能把11/11反弹当事件后的价格确认。 [G-NVDA-GOVERNANCE-20261112](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition), [G-SOXX-20261111](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf), [G-SMH-20261111](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/) |
| COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111；weakened | 全球前序71分，close差300、日盘新计划要求15分钟不破296并收复303。 | 同合同11/12close差294，settle299；前日300/306、前夜307。绝对backwardation仍在，但新价不足支持原强势延续。 | 新增中国EOD而非旧夜盘；294低于逻辑阈296的方向不利，但日收不证明15分钟顺序或成交，不虚判已止损。 [SH-COM-M-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-M-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-WASDE-20261110](https://esmis.nal.usda.gov/sites/default/release-files/796142/wasde1126.pdf) |
| COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106；strengthened | 全球前序未入Top5；同合同11/11close差1220、前夜1290，原研究目标含1700。 | close差1680、settle1450；铜近月相对韧性加强，但已接近初版TP2，新增买入赔率恶化。 | 同合同差而非换月主力；近月本身下跌，曲线扩大可来自远月更弱，实体短缺待证。 [SH-COM-CU-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-CU-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json) |
| GOLD-POLICY-CREDIT-CONVEXITY-20261111；weakened | 前序65分观察，不沿用旧行权价。 | AU2612日收873.3→852.5、−2.382%，政策信用对冲论仍为有条件长期假说，短期独立性证据减弱。 | 高实际利率与黄金下跌相容；ETF月流入、旧CFTC不能抵消新增价格反证。不是金价跌就宣告长期保险永久失效。 [SH-COM-AU-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [G-US-REAL-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026), [G-GOLD-ETF-202610](https://www.gold.org/goldhub/data/global-gold-backed-etf-holdings-and-flows), [G-GOLD-COT-20261103](https://www.cftc.gov/dea/futures/deacmxsf.htm) |
| CN-IM-IH-SMALLCAP-BREADTH-RV-20261111；data_corrected | 前序将radar_history读取为空，历史比较能力不足；最新73分依据11/11。 | 同SHA fetch_blob取得60条完整历史，补1/3/5/20比较及双IV口径；最新仍11/11，当日风格未知，待评分。 | 真实读取纠错，不算新行情。MO2612官方IV三日下降7.596vol点与短期风格反弹相容，但20日相对弱势尚存。 [G-OPTIONS-CORE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json), [G-CN-INDEX-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json), [G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json) |
| COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111；weakened | 前序68分，等待SC收复610且曲线≥10、Brent同刻≥92.5，库存风险未消；首次晚版Brent门槛93与该晨版不同。 | EOD609.9接近610，但曲线由12.1缩至10；EIA顺延到截点后01:00，库存尚未知。 | 单一日收近阈值不能证明“15分钟突破→回踩”的路径；需先核EIA及同步海外合同，不把外部旧价当确认。 [SH-COM-SC-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-SC-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-EIA-CALENDAR-20261112](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |

信息层次：新增中国商品11/12EOD可以与11/11EOD比较；可用已完成Night仍为11/11晚，不是本晚；美股11/11完整收盘与11/12 NVDA公告严格先后；宏观CPI、Fed、WGC、USDA和10月/11月初公司财报本来已经公开，本次重读只能纠正研究解释。美债前序67分的2s30s观点机制暂未变，62bp前收不是新增收益机会。未取得中国11/12股指原件，不写“晨报小盘延续”。所有“原方案失效/是否成交”另按已确认触发链判断。

## 4. 统一候选：不超过五项

以下是**研究优先序**，不是已证实的回报排名。全球股票/利率/商品共用五个名额；独立公司研究没有另设股票榜。相对前序，铜进入、SC移至观察，M下调，IM不因旧分数73自动占第一。

| 序 | 候选 | 期限 | 研究结论 | 证据充分度 | 执行状态 | 合同损失边界 | 当前总分 |
|---|---|---|---|---|---|---|---|
| 1 | SOXX/SMH治理集中度差 | 事件1—20交易日 | 治理分化下的ETF相对价值待验证优势 | 事件原件强、持仓结构部分；当前价格/借券/Beta缺 | 待同步报价、借券与新窗口条件 | 线性ETF多空不封顶 | 待评分 |
| 2 | CU2612/CU2701近强远弱 | 原期限至11/20 | 期限结构相对强度增强，新增追价无优势 | 价格和曲线两层可观察；同向独立支持主要只有曲线1层，实体供需和可执行vol不足 | 只等回撤后新评估，不追1680 | 线性跨期不封顶 | 待评分 |
| 3 | IM2612/IH2612风格修复 | 原期限至11/25 | 11/11小盘修复成立，延续假说尚待11/12验证 | 历史价格/basis/IV可复算；当日广度、基差、Beta缺 | 休市；下一日盘重新核价，旧窗口已过 | 股指跨风格不封顶 | 待评分 |
| 4 | 美债2s30s压平 | 1—10交易日条件研究 | 2s30s压平有机制，赔率待验证 | CPI、Fed与财政部曲线充分支持机制；OIS、期限溢价、交易DV01缺 | 待拍卖/价格与DV01参数 | DV01配平仍不封顶 | 待评分 |
| 5 | M2701/M2705近月韧性 | 原期限至11/18 | backwardation保留，原强势延续证据削弱 | 价格/曲线可比，但当前两层同向支持不足；旧USDA不算新增 | 降早期观察，不恢复原新仓计划 | 线性跨期不封顶 | 待评分 |

固定权重仍为逻辑25、赔率/凸性25、催化20、价格/期限/波动15、拥挤/技术15。**五项均未给当前数字分值**：候选缺同步定价、成本、持仓/借券或DV01，赔率与技术分无法可靠重算，故按Prompt保留待评分；旧72/73/71/67等仅历史记录，不包装成当前评分。具体给分依据应怎样变化：AI的催化证据增强，但赔率/技术未知；CU期限强度增强，赔率下降，价格层可观察却不能把下跌/OI减少再当独立支持，现阶段1层同向证据的政策上限为59；IM补历史证明短期与20日分歧，不能按11/11强度给11/12技术分；利率逻辑未变但供给风险待定；M价差证据削弱，不用USDA同一冲击重复加分。

### 1. AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106

新增治理事实→SMH较高NVDA集中度可能承压→11/11价格在事件前，尚不能证明事件未定价；PnL来自ETF持仓差而非虚构纯现金流篮子。最强反证是路线、订单和临时管理团队连续性使治理折价迅速消退；下一决定性观察为同步ETF比率、NVDA相对表现和11/17财报。

**条件与下一决定性证据：**完整AND/顺序/报价/放弃、止损、目标和期限见第5栏AI卡；本日原开盘窗口已过。 来源：[G-NVDA-GOVERNANCE-20261112](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition), [G-SOXX-20261111](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf), [G-SMH-20261111](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/), [G-MSFT-FY27Q1](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast), [G-CRWV-2026Q3](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx)。

### 2. COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106

价差扩张460点，近月下跌而远月更弱：更像近端韧性/远期需求折价，不能仅凭曲线证明库存短缺。相较单边铜期货，跨期降低共同价格暴露但保留交割、近月流动性与曲线断裂风险。铜矿利润披露是经营背景，未证明11月国内现货紧缺。

**条件与下一决定性证据：**原初版900/925/950入场、止损750、TP1400/1700、11/20 14:45退出不追溯改动；当前1680不得当新买入许可。重新出现可比回撤、A/B级实体短缺和两腿成本后才重新评分。 来源：[SH-COM-CU-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-CU-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [PUB-ZIJIN-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF)。

### 3. CN-IM-IH-SMALLCAP-BREADTH-RV-20261111

短期现货和期货相对强度与ETF份额估算同向，但同源及高Beta反弹不能算多重独立alpha；20日小盘相对IH仍弱。PnL来自风格差及基差变化，非总市场方向。反证是短挤压/高Beta单日反弹；下一决定性观察为同期现货宽度、成交、两腿basis、Beta校准。

**条件与下一决定性证据：**完整历史参数与下一窗口条件见第5栏IM/IH卡；不能沿用旧行情确认当前信号。 来源：[G-CN-INDEX-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json), [G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json)。

### 4. UST-2S30S-HOT-CPI-FLATTENER-20261111

2s30s已收窄到62bp并吸收部分前端通胀重估。竞争解释是拍卖与财政供给抬升远端，使压平不再优于简单降低久期。收益来自2Y相对30Y收益率上行，并非所有利率上升均赚钱；与长期债Put Spread相比缺限损和可验证成本。

**条件与下一决定性证据：**候选表达为按DV01配平的空2Y/多30Y现金或期货；无具体债券/期货CTD、DV01、融资和报价，不生成数量。若远端供给溢价推动持续陡峭则撤销压平假说；等待拍卖后与PPI后同口径曲线。 来源：[G-US-RATES-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026), [G-US-REAL-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026), [G-US-CPI-202610](https://www.bls.gov/news.release/cpi.nr0.htm), [G-FED-20261028](https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm)。

### 5. COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111

USDA美国库存调低仍支持成本背景，但产量上调与全球库存规模、国内季节性需求是反证；当日近月相对价差缩小表明此前紧缺溢价并非持续扩大。PnL来自近远月再扩张；直接多M更暴露外盘/汇率；未报价期权不替跨期仓封顶。

**条件与下一决定性证据：**初版止损268/目标330与360，上一版新计划290/340与370并列保留；本次294低于上一逻辑门槛296，须重新证明303回收与现货/海外确认，不用已过日盘参数自动挂单；11/18原时间退出不延长。 来源：[SH-COM-M-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-M-CURVE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json), [SH-COM-WASDE-20261110](https://esmis.nal.usda.gov/sites/default/release-files/796142/wasde1126.pdf)。

同一idea_id的M/CU在商品报告分别为58/59分，是明示成本情景下的领域内条件研究优先级；本全球报告因跨资产比较所需的当前赔率与成本未齐，保留待评分。两种评分假设已分开，分数和执行状态不可互替，共同事实与单主题预算不变。

未入榜的重要研究：黄金的长期凸性用途保留，但AU新增下跌且完整海外期权链缺；SC等待EIA且曲线弱于绝对价格；AP波动线索的负IV−RV仅样本/历史比较，不能证明可买到便宜跨式。DXY/FX与MOVE缺同截点可靠值，方向性交易未入榜。A股三家公司经营证据参与反证AI与金属主题，缺价格/预期不能宣布个股alpha。

## 5. 两张完整条件研究卡

### 卡1｜SOXX / SMH：治理集中度差，保持原idea谱系

`AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106`。**研究结论：待验证优势；证据部分；执行待报价与参数。** 原exact-ID首次时间未查实：已读11/6—11/10资料中该ID未出现，最早可核同工具假说是11/10 08:13:30北京的 `AI-SOXX-SMH-NVDA-IDIOSYNCRATIC-RV-20261110`；11/6实际是QQQ/SMH。不能按ID后缀倒填首次日期，也不把换工具叫新发现。

**逻辑与价格分歧。** NVDA领导层变更可能提高特定公司的治理折价；官方SOXX中NVDA7.11%（11/10）对SMH17.67%（11/11），方向上支持低集中度对高集中度，但日期不一，不计算精确净NVDA暴露。上一完整收盘比值0.306533、组合Q=58.60美元已在旧入场Q20—40之外，且这发生在新公告之前。尚没有能证明新风险未定价的11/12同步成交，因此不能声称alpha已确认。最强竞争解释是CEO过渡平稳、路线和订单延续，NVDA跌幅很快被买回；其次是SOXX的AMD/模拟芯片权重受宏观或估值压缩更大。PnL只能按每腿算，不用“现金流龙头”标签代替持仓分析。[G-NVDA-GOVERNANCE-20261112](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)、[G-SOXX-20261111](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf)、[G-SMH-20261111](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/)。

**工具和合同。** 研究一个整数篮子为买33股SOXX、卖空10股SMH，美元计价、每股乘数1；ETF没有期货到期，借券可被召回，须核账户许可、实时证券状态、最小报价单位、费用、税、除息、T+1交收安排及组合两腿同步深度。本批未取得实时借券费、beta、股数调整/公司行动状态，均是硬门槛；不把美元近中性当Beta中性。基准总名义10197.80美元而净差58.60仅是点值，不是投资本金或保证金。相比单买SOXX，配对降低共同方向却引入SMH做空无限尾损；相比已报价SOXX call spread/SMH put spread，线性组合没有权利金上限保护；当前期权链未取得，不编腿、行权价、IV或Greeks。

**原计划逐字条件语义与有效窗口。** 上一版要求美国现金开盘后30—45分钟，ratio先回撤0.3045—0.3060，且15分钟收盘≥0.3055；**随后**回踩守0.3045；**同时AND** Q回撤20—40美元、QQQ守首30分钟低点、借券/费用/分红税/同步报价核验。ratio>0.3080且无回踩放弃，借券不可得、权重或公司行动异常也放弃。这些是上一版计划值，不是本批观察到的价格路径。11/12 23:00—23:15北京的原窗口已过去，禁止迟到追认；下一完整开盘窗口是11/13 22:30北京，30/45分钟对应23:00/23:15。届时仅在全套同步新数据证明上述联合约束仍有经济意义时，才可承继成新计划；否则留观察。Q与ratio必须同一时点：`Q=(33×ratio−10)×SMH`，不能分别挑不同时间最有利的数。

**分批与退出。** 原50/50对单个33:10篮子会出现16.5股，不能默认券商允许碎股卖空；只在总预算容纳**两个完整篮子66:20**时按每次33:10分两次，第二次仍须再次满足全部确认。若只能一个完整篮子则单次，不假写50/50。原止损Q=−20美元**OR**日线ratio<0.3010；逻辑失效为NVDA相对SOXX反弹>6% **AND** ratio<0.3020，仍需同窗口可比收益。原TP1 Q130、TP2 Q220，ratio约0.311/0.317仅辅助，不证明组合利润达到目标。原“20交易日”时间退出没有明确计时起点，本次不重置20天；该锚与真实开仓日未核前，不开新仓，若已有仓则按原实际订单期限处理。止损不保证成交，先到止损/逻辑失效/时间退出即停止等待目标；不以新观点移动旧止损。

**成本后情景。** 以下30/35/40美元是原20—40区间内的敏感性，不以20美元理想价美化，所有情景仍须验证顺序可达；成本10/15/25美元为情景而非实报，实际借券、分红税、成交滑点若超过假设必须重算。

| 成交情景 | 组合入场值 | 往返成本假设 | 止损计划损失 | TP1净利润 / R | TP2净利润 / R | 费用后盈亏平衡组合值 |
|---|---|---|---|---|---|---|
| 好 | 30.00 | 10.00 | 60.00 | 90.00 / 1.50 | 180.00 / 3.00 | 40.00 |
| 中 | 35.00 | 15.00 | 70.00 | 80.00 / 1.14 | 170.00 / 2.43 | 50.00 |
| 坏 | 40.00 | 25.00 | 85.00 | 65.00 / 0.76 | 155.00 / 1.82 | 65.00 |

单位均为美元/33:10篮子，R=目标净利润÷计划止损损失；不是最大损失或概率加权期望。

最不利列TP2也仅1.82R，TP1不足1R；这意味着坏价不能靠“主题更强”挽救。无可校准概率，不给精确胜率或期望收益。若两完整篮子分批，组合损益按真实加权入场累计，不把最好单腿代替篮子PnL：`PnL=33×ΔSOXX−10×ΔSMH−全部成本`。

**催化、压力与规模。** 未来1—20交易日主要是治理连续性公告、11/18北京凌晨NVDA财报、PPI和其他已发布指引的订单验证。用前收作压力基准，SOXX跌20%而SMH涨20%损失2039.56美元/篮子；相反40%冲击损失4079.12，尚未含汇率、借券召回和流动性成本；美国ETF不适用中国“单/双涨跌停”上限，不能把市场熔断当个券最大损失。若短腿翻倍，风险可远超该压力，理论不封顶。实际预算0；条件补齐后的研究压力预算上限0.25% NAV，篮子数≤floor(0.0025×美元NAV/最坏压力损失)，并受保证金、深度和整数限制；仅20%反向压力下一个篮子要求美元NAV≥815824，不能假定用户满足。跨报告所有AI股票、ETF、指数联动共用同一主题预算，不再分配三家公司预算。若治理折价消失且基本面继续强，降低净空NVDA风险；若利率与股市一起挤压，先降总名义而非盲目加空。

### 卡2｜IM2612 / IH2612：短期风格修复，长期相对趋势尚未确认

`CN-IM-IH-SMALLCAP-BREADTH-RV-20261111`。**研究结论：延续假说；证据部分；执行休市/待当日核价。** 首版2026-11-11 20:04:40北京、66分仅方向观察，没有数字入场/止损/TP；以下数字来自11/12晨版rev3，不能回填到首版。11/11 IM主约1/3/5日+1.633/+2.511/+2.377%，IH−0.327/−0.537/−1.218%，现金1000相对50也强；20日IM−2.686%对IH+0.307%说明修复尚未改写较长趋势。MO IV快速下降更像上行风险缓释，不等于未来波动廉价。[G-CN-INDEX-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json)、[G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json)。

**工具与定价。** 原篮子买5手IM2612、卖8手IH2612，乘数分别200/300元每指数点，`P=1000×IM−2400×IH`。最小变动0.2点对应单手40/60元为合同研究参数；本批官方PDF尝试超时，未独立重验现行保证金、手续费、限幅及到期调整，不能称全参数就绪。引擎按第三周五推定2026-12-18现金交割，须用当前中金所/券商确认，不套商品夜盘。基准11/11 P41720、总名义13204280元，净/总0.316%；资金占用与风险均不等于净差。Beta、行业权重、相关性与分红差异尚未校准，跨风格空腿不能保证中性。

**原触发与下一窗口。** 原日盘09:30后P先回撤/处于20000—50000；09:45收≥30000；**随后**15分钟低点≥20000 **AND** 10:00收≥40000 **AND** 现金CSI1000−SSE50同期收益差≥+0.40个百分点 **AND** IM年化basis不比IH差超过0.25个百分点 **AND** 两腿深度正常。50%在P40000—50000，二次5分钟守50000再50%；P>80000无回撤放弃，广度/basis不确认、Beta/费用/保证金无法核验也放弃。11/12原窗口已经过去，本次无11/12原始行情与分钟路径，信号、成交和持仓均未知；下一常规窗口11/13 09:30，09:45/10:00/10:15逐级检查。不能把11/11 P41720当次日入场。若下一窗口价格与基差明显偏离旧尺度，原计划继续停用，重新定价必须作为后续新版本，不能自动改阈值。

**分批/失效/期限。** 单个5:8篮子不能无损拆成2.5:4手；50/50须总共10IM:16IH，分两次5:8；仅能一个篮子则单次。原计划止损P=−60000；独立逻辑失效为现金风格差30分钟<−0.30个百分点 **OR** IM年化basis比IH更差>0.25个百分点。TP1 P180000、TP2 P320000，时间退出 **2026-11-25 14:55北京**，不因数据缺口延长。若此前有仓而确认触发原止损/逻辑失效/时间期限，则按可成交窗口退出；无真实订单不能写已退出、已盈利。

**可达性与损益。** 前序把P30000列好价，但完整入场必须10:00≥40000；本次删除这项不可直接达成的好价，改在40000/45000/50000内测算，三种费用3000/6000/12000元只是覆盖双腿费用与滑点的敏感性。`PnL=1000×ΔIM−2400×ΔIH−成本`，一半在40000、另一半50000时平均45000，不用30000的漂亮R。

| 成交情景 | 组合入场值 | 往返成本假设 | 止损计划损失 | TP1净利润 / R | TP2净利润 / R | 费用后盈亏平衡组合值 |
|---|---|---|---|---|---|---|
| 好 | 40,000.00 | 3,000.00 | 103,000.00 | 137,000.00 / 1.33 | 277,000.00 / 2.69 | 43,000.00 |
| 中 | 45,000.00 | 6,000.00 | 111,000.00 | 129,000.00 / 1.16 | 269,000.00 / 2.42 | 51,000.00 |
| 坏 | 50,000.00 | 12,000.00 | 122,000.00 | 118,000.00 / 0.97 | 258,000.00 / 2.11 | 62,000.00 |

单位均为人民币/5:8篮子，R=目标净利润÷计划止损损失；不是最大损失或概率加权期望。

各列TP1均低于1.34R，坏价甚至不足1R；TP2依赖更长风格延续，无法推精确期望值。若已观察P跌破入场逻辑同时又试图用便宜P买入，属于条件矛盾，应放弃而非套用原止损表。

**压力/预算。** 在11/11两腿价格上，IM跌10%、IH涨10%的相关性断裂压力为1320428元/篮子；连续两次复合10%反向冲击为2640438.80元，公式分别按多腿0.9²、空腿1.1²计算。这里10%仅压力尺度，现行临时限幅未重验，不声称交易所一定允许相同路径。一个篮子在0.25% NAV单次压力预算下所需NAV至少528171200元；这显示小净名义也可能不适合账户，不能仅按计划止损122000元定规模。实际执行预算0；补齐后数量取计划损失、1/2次压力、追加保证金、深度与整数约束的最小值。中国休市遇海外AI大幅波动、人民币急变、风格相关性断裂均优先降低总名义。用MO call spread加HO put spread可以研究有限权利金替代，但必须报价到腿，不能给当前期货仓自动封顶；IC用MO/IO代理还有指数跟踪风险。

未来1—20交易日催化是中国经营/信用数据、AI订单与海外风险传导、11/20近月期权到期及12月移仓预期；催化窗口、11/25计划退出与12/18合同到期三者分开。下一决定性观测是11/12及11/13真实全宽度/行业贡献，而不是只要IM OI增加就称新多。

两卡都不提供立即执行许可。原预算仍为试仓0.25%—0.75%、确认0.75%—1.50%、同主题≤2.5%—3.0% NAV；本批因执行输入不足仅预留0.25%研究压力上限且实际执行预算0，不能与商品报告叠加。账户NAV、权限与实际持仓未提供，未计算账户最优权重。

## 6. 黄金专题：政策信用假说接受价格反证

**本次判断：短期证据弱化；3—6个月保险用途保留，尚未确认正收益优势。** AU2612在11/12日盘收852.5元/克，对873.3跌2.382%；OI减2914是持仓净变化，不辨投资者动机。与11/10十年实际收益率2.78%并置，至少说明“黄金已摆脱真实折现率”的强论断没有得到证实；两日不同会话不能做严格因果回归。海外COMEX4059.3仅错时context，现货/COMEX当前精确合同未核，不能据此计算境内外溢价或套利。[SH-COM-AU-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[G-US-REAL-20261110](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026)、[SH-COM-EXTERNAL-20261111](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)。

| 解释 | 支持与可观察依据 | 最强竞争解释/证伪 |
|---|---|---|
| 政策信用/储备分散 | 若财政融资冲击推长端收益率上行而黄金持续强于美元与实际利率模型，才支持额外信用溢价 | 本次AU下跌不支持短期脱钩；央行最新购买原件缺，不能把“央行会买”当事实 |
| 实际利率与美元 | real10Y升至2.78%提升持金机会成本；旧H10美元偏强方向一致 | 同步DXY缺，若美元/实际利率上行时金价连续创新高才需提高替代解释权重 |
| 避险与流动性 | ETF月净流入+27亿美元、+19吨显示配置需求尚在 | 月度而非本日；现金紧张会使黄金与风险资产同跌，不保证每次危机正收益 |
| 仓位与波动溢价 | CFTC非商业净长179548手，周减6903；AU局部ATM21.98%；近25Δ样本call-put翼差−1.22、翼均值−ATM +1.04vol点 | 实际call Δ+0.2239/IV22.41%、put Δ−0.2782/IV23.63%，生成器容差未二核，非精确25Δ插值RR/BF；周持仓慢、样本skew非完整链，不推dealer方向或挤仓概率 |

ETF为10月报告、11/5公布，CFTC为11/3持仓、11/6发布；下一COT因假期在11/17北京04:30，并非本周五。AU RV19.782%是有断点的20观察估计，比ATM低约2.20vol点不证明卖波动有优势；当前只有11/24近月样本，不能外推到3—6月波动期限。[G-GOLD-ETF-202610](https://www.gold.org/goldhub/data/global-gold-backed-etf-holdings-and-flows)、[G-GOLD-COT-20261103](https://www.cftc.gov/dea/futures/deacmxsf.htm)、[SH-COM-OPTIONS-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[SH-COM-CFTC-CALENDAR-20261112](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)。

### 表达比较与实际决策

| 表达 | 适用假说与收益来源 | 本次决策与否决条件 |
|---|---|---|
| 3—6月Call Spread | 以净权利金换取温和上行凸性，减少单买Call的Vega成本 | 海外/远月准确expiry、两腿strike与bid/ask未取得，待询价；以每单位到期宽度W、全部净成本C≤W/3为**数学筛选**可保证最大到期净利/最大成本≥2，并非可成交报价或胜率。需同乘数、同到期、同货币、真实费用；不沿旧strike |
| 微型黄金期货确认 | 同步金价突破、实际利率/美元背离持续后取得线性Delta | 合同/保证金/限幅/roll未重验，当前无单；止损不能封顶，适合可承受追加保证金的条件研究，不能替代保险结构 |
| 黄金多＋长债Put Spread | 研究财政/通胀冲击使黄金强、长债弱的联合情景 | 可在该情景对冲，但经济关系可断裂；若黄金腿是期货，债券Put Spread不封顶黄金亏损。长债两腿IV/期限与可成交成本缺，不称已建成组合 |
| 反向/减持/对冲 | 若实际利率、美元与黄金同向负传导持续，先减少Delta；若有股票/金矿风险可对冲 | 未知实际持仓，仅条件性处理；不因单日下跌转成无止损裸空或卖出大尾部期权 |
| 不交易 | 等待价格与资金证据分离 | 当前优选；不支付无法验证的事件溢价，保留后续有限凸性研究 |

短期决定性观察是PPI/拍卖后真实利率和金价是否同向、EIA能源冲击是否经通胀传导、下一ETF/CFTC/央行披露的实际频率。若只有美元下跌带来的金价上涨，不提升政策信用假说；若利率上升、美元走强而黄金在多日相同会话保持强势，再检验额外驱动。若IV随恐慌大幅抬升，减少Vega或比较价差；若IV塌陷且现金紧张导致黄金一起下跌，也不能仅凭“保险便宜”扩大Delta。

紫金披露构成重要反证：金锭Q3粗毛利较Q2下降18.44%，同一公司铜精矿上升11.84%，说明数量、实现价和成本可抵消商品价格标签。黄金期货、金矿股票和政策信用保险不能当同一个工具。利润桥详见第8栏，跨报告黄金/金矿共享主题风险。[PUB-ZIJIN-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF)。

## 7. AI专题：把治理事件与经营兑现分开

**本次新变化是NVDA治理事件；经营资料整体仍显示需求强，但利润兑现与现金回收分化。** 官网11/12确认CEO过渡，媒体同事实13:54:02.149Z给出截点前已知上界；仅官网日期本身不够证明可得时刻。公司表示路线和客户承诺继续，是反对“整个AI订单立即崩塌”的直接管理层表态，仍需客户与财报验证。美国盘中价格未同步取得，不能断言治理风险已充分或未充分定价。[G-NVDA-GOVERNANCE-20261112](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)、[时间佐证](https://www.businessinsider.com/colette-kress-nvidia-cfo-interim-ceo-jensen-huang-resigns-2026-11)。

| 链条/实际下钻范围 | 已核经营证据 | 研究贡献、最强反证与缺口 |
|---|---|---|
| 芯片与龙头：NVIDIA；ETF持仓含AMD/AVGO/TSM等 | 治理变更是新事件；NVDA财政Q3结果11/17才发布 | 事件折价不等于基本面衰退，下一财报/交付验证；其余芯片公司未逐家读取新财报，不把ETF持仓当盈利审计 |
| 半导体设备：ASML | Q3收入116.62亿欧元、毛利57.5%；Q4收入指引142—152亿 | 安装/升级兑现与高毛利是反对全面Capex崩塌的证据；产能约束、出口规则与客户预期调整仍可伤估值，当前股价/共识缺 |
| 服务器/网络：工业富联、中际旭创、Arista | FII高收入利润伴低现金转化；中际11/6披露800G/1.6T订单；Arista Q3收入36.576亿美元、GAAP经营利润率44.9% | 网络需求不完全绑定单一GPU；Arista毛利63.6%低于去年64.6%，经营杠杆不能掩盖产品组合压力；FII/中际营运资本与资本支出要追踪 |
| 数据中心租赁/二线Capex：CoreWeave | Q3收入36.61亿美元、经营利润2.07亿、利息8.46亿、简单现金FCF−74.66亿 | 需求兑现强而融资负担更重；预期客户预付90亿美元可缓资金但尚未到账，不能据此定义安全债务或机械做空 |
| 电力/冷却/基础设施：Vertiv | Q3收入43.13亿美元，CFO7.94亿，adjusted FCF6.52亿 | 订单可在基础设施瓶颈处兑现，反对“所有高Capex链都是远期幻觉”；adjusted指标与别家FCF口径不同，当前估值与电网/电价数据缺 |
| 云与软件：Microsoft | FY27Q1收入922.79亿、经营利润459.15亿美元；CFO580亿但现金Capex393.67亿 | 现金盈利能力强，但简单FCF降至186.33亿、同比−27.39%；云高增长不保证股东即时现金增多。软件付费变现与推理成本分拆未取得，不编AI单独利润率 |

原始来源：[G-ASML-2026Q3](https://www.investor.asml.com/news-releases/news-release-details/asml-reports-eu11.7-billion-total-net-sales-and-eu5.0-billion-net-income-q3-2026)、[G-ANET-2026Q3](https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Networks-Inc--Reports-Third-Quarter-2026-Financial-Results/default.aspx)、[G-VRT-2026Q3](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067707/q32026exhibit991vrt10282026.htm)、[G-MSFT-FY27Q1](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)、[G-CRWV-2026Q3](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx)、[PUB-FII-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-30/1225639532.PDF)、[PUB-INNOLIGHT-20261106](https://static.cninfo.com.cn/finalpage/2026-11-06/1225660601.PDF)。以上为实际限定链条扫描，未声称全部上市公司已逐一审计；10月/11月初原件是本次重验的已知资料。

### 现金流桥与市场已定价部分

微软单季CFO同比+28.73%，现金Capex同比+102.99%，因此CFO−Capex从256.63亿降至186.33亿美元。经营盈利改善与股东可支配现金下降可以同时发生，这削弱“现金流龙头天然不受Capex影响”的旧二分法。CoreWeave的CFO19.75亿对PP&E94.41亿，差−74.66亿，且利息/经营利润约4.09倍；该比例是季度算术，不是偿债覆盖率。两家公司商业模式、租赁融资和资本支出时点不同，不能直接用该差额排序做空。支持长期需求的是云与设备/网络利润已实现；反证则是回款、扩产和融资期限错配。[G-MSFT-FY27Q1](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast)、[G-CRWV-2026Q3](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Third-Quarter-2026-Results/default.aspx)。

11/11纳指涨1.597%、SMH市价涨4.824%、SOXX NAV涨6.07%表明上一完整会话已反弹，但两ETF涨幅口径不同，不能相减当相对交易收益；这些前收都早于11/12领导层公告。SOXX/SMH当前估值错配未知，SOXX公开组合PE只能说明组合口径，不给“合理PE”。一旦价量显示SOXX改善仅来自AMD等高Beta权重，而非治理折价差，主题须收窄或撤销，不能把一切上涨认领成现金流逻辑成功。[G-NASDAQ-20261111](https://fred.stlouisfed.org/series/NASDAQCOM)、[G-SOXX-20261111](https://www.ishares.com/us/products/239705/ishares-phlx-semiconductor-etf)、[G-SMH-20261111](https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/)。

### 工具竞争与证伪路径

多现金流、空远期Capex可从盈利质量提出，但本批没有全体成员、权重、Beta、借券及一致FCF口径，故只称主题。反向“多Capex Beta、空成熟软件”若订单/预付款兑现且现金回报改善，也可能在资金改善时占优；这正是不能机械维持原空头的原因。SOXX/SMH提供可识别集中度差，但不是该主题的纯映射；单买行业ETF更简单却承担共同利率与AI估值风险；财报后再买有限风险价差可避免支付部分事件IV，却可能错过跳空。没有财报前后同到期、同delta的可成交IV，不宣称vol crush套利。

下一决定性证据依次是治理过渡对交付/研发的实际影响、NVDA财报与订单、云客户现金回收、设备出货兑现、中际与FII应收/存货周转、Vertiv经营现金流与产能；这些催化并非都在24小时内。若订单保持而资金成本下降，减少对Capex端的空头偏见；若收入开始失速且应收与库存继续增长，降低多头可信度；若仅利率抬升导致估值压缩，先减少共同久期而非声称公司经营已恶化。

## 8. 中国股指、期权与独立公司研究

### 四指数完整结构：历史可研究，当日状态不冒认

以下全为**11/11收盘**，来源固定SHA。中国11/12官方中金所日行情与指数原件真实尝试超时/不可访问；二手指数和期指有冲突，未纳入。该限制约束当日判断和执行，不删除可核历史研究。不能把商品已更新到11/12转嫁给股指源。[G-OPTIONS-CORE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json)。

| 准确合同 | close | settlement | 成交手 | OI手 | ΔOI手 | 现金basis点 | 年化basis | 推断expiry |
|---|---|---|---|---|---|---|---|---|
| IH2612 | 2,742.20 | 2,746.00 | 25,950 | 63,192 | +1720 | -23.34 | -8.33% | 2026-12-18* |
| IH2703 | 2,704.40 | 2,706.60 | 4,882 | 19,896 | +509 | -61.14 | -6.30% | 2027-03-19* |
| IF2612 | 4,043.40 | 4,048.60 | 56,405 | 173,783 | +163 | -32.31 | -7.82% | 2026-12-18* |
| IF2703 | 3,982.60 | 3,986.20 | 11,287 | 73,615 | +512 | -93.11 | -6.51% | 2027-03-19* |
| IC2612 | 6,664.00 | 6,671.80 | 102,586 | 173,915 | +4705 | -49.18 | -7.23% | 2026-12-18* |
| IC2703 | 6,528.20 | 6,534.00 | 21,226 | 65,616 | +1937 | -184.98 | -7.86% | 2027-03-19* |
| IM2612 | 6,623.00 | 6,628.40 | 196,766 | 290,211 | +9945 | -46.55 | -6.89% | 2026-12-18* |
| IM2703 | 6,478.20 | 6,480.80 | 37,602 | 104,945 | +958 | -191.35 | -8.18% | 2027-03-19* |

*到期日由引擎第三周五规则推断，假日调整及当前执行参数尚需官方确认。主次按源内主/次，不把不同月份连续序列拼收益。

| 固定合同/现金 | 1交易日 | 3交易日 | 5交易日 | 20交易日 |
|---|---|---|---|---|
| IH2612 | -0.327% | -0.537% | -1.218% | +0.307% |
| IH现金 | -0.268% | -0.785% | -1.531% | -0.410% |
| IF2612 | +0.467% | +0.622% | -0.683% | -2.817% |
| IF现金 | +0.409% | +0.529% | -0.625% | -3.366% |
| IC2612 | +1.335% | +1.806% | +1.295% | -3.063% |
| IC现金 | +1.013% | +1.756% | +1.376% | -3.824% |
| IM2612 | +1.633% | +2.511% | +2.377% | -2.686% |
| IM现金 | +1.371% | +2.524% | +2.422% | -3.412% |

截至11/11，端点分别为11/10、11/6、11/4、10/14；主约按准确2612合同从历史主/次记录匹配重算close-to-close，**不是close对前结算**。20日端点收益可算，但其中缺10/21，因此不计算连续20日RV。5日RV以11/4—11/11的5个相邻对数收益、样本标准差×√252重算，窗口极短，只作尺度，不与更长IV视作同一预测。

| 产品 | 现金RV5年化 | 参考ETF份额×价格估算申赎 | 次−主跨期点差 |
|---|---|---|---|
| IH | 6.483% | -3.061亿元 | -37.80 |
| IF | 11.981% | -9.860亿元 | -60.80 |
| IC | 24.188% | 9.015亿元 | -135.80 |
| IM | 26.872% | 9.655亿元 | -144.80 |

ETF估算50/300流出、500/1000流入支持11/11风格广度的一部分，但同源价格和份额估计不可重复算独立机构信号；未取得当日两融、全市场涨跌家数、行业贡献、正式指数权重、DR007/国债与CNH，不猜国家队。价格+OI不能辨新多、新空或套保。[G-CN-INDEX-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_latest.json)。

**跨风格竞争。** IF-IH更偏大盘内部行业差，11/11现金相对差约+0.677个百分点；IM-IF约+0.962pp；IM-IH约+1.638pp；IC-IF约+0.604pp；IM-IC约+0.358pp，均由上表现金同日收益相减，不是可直接购买的篮子回报。最强短期风格是IM相对IH，但20日其现货相对差约−3.002pp，反对把修复认成完整趋势反转。IC也修复而MO更贵，使IC/IF线性方案值得比较，不过IC没有默认同标的HO/IO/MO；用MO或ETF代理会混入指数、Beta、basis与跟踪误差。Dollar-neutral需按各乘数和价格配量；Beta-neutral还需同窗收益协方差，当前未校准。

**期限/期现。** 四主约都贴水，年化约−6.89%至−8.33%，远月更低；远月贴水不能被称无风险收益，因为分红、资金、卖空、手续费、保证金和交割日不同。跨期本质交易期限结构变化，可能比方向仓减少Delta，却保留分红预期、移仓和流动性风险；当前没有足够同日现货复制成本与正式成份，未建立期现套利仓。11/20近月期权到期与12/18主合约不同，不混成同一到期风险。

### HO / IO / MO：全可得期限与局部波动形状

| 系列 | 到期* | official-EOD forward | quote-mid ATM% | official-EOD ATM% | PCR OI |
|---|---|---|---|---|---|
| HO2611 | 2026-11-20 | 2,764.205 | 14.038 | 13.445 | 0.592 |
| HO2612 | 2026-12-18 | 2,745.745 | 14.648 | 14.340 | 0.617 |
| HO2701 | 2027-01-15 | 2,737.099 | 14.856 | 14.765 | 0.854 |
| HO2703 | 2027-03-19 | 2,708.873 | 14.711 | 14.658 | 0.908 |
| IO2611 | 2026-11-20 | 4,071.008 | 17.963 | 17.267 | 0.575 |
| IO2612 | 2026-12-18 | 4,047.072 | 17.789 | 17.666 | 0.643 |
| IO2701 | 2027-01-15 | 4,029.813 | 17.458 | 17.434 | 1.846 |
| IO2703 | 2027-03-19 | 3,992.663 | 17.503 | 17.457 | 0.702 |
| MO2611 | 2026-11-20 | 6,662.571 | 29.220 | 28.147 | 0.587 |
| MO2612 | 2026-12-18 | 6,627.249 | 27.948 | 27.579 | 0.650 |
| MO2701 | 2027-01-15 | 6,605.214 | 26.723 | 26.678 | 1.553 |
| MO2703 | 2027-03-19 | 6,497.762 | 25.817 | 25.790 | 0.557 |

| 12月系列 | 25Δ call/put IV% | 10Δ call/put IV% | RR25/BF25 vol点 | call/put成交 | call/put OI | call/put ΔOI | 绝对Gamma集中strike |
|---|---|---|---|---|---|---|---|
| HO2612 | 14.224 / 15.204 | 15.689 / 17.119 | -0.980 / 0.374 | 4,554 / 2,553 | 19,956 / 12,315 | +1139 / +479 | 2,800,2,700,2,900 |
| IO2612 | 17.378 / 18.352 | 17.789 / 19.677 | -0.974 / 0.200 | 16,029 / 8,251 | 52,665 / 33,860 | +1032 / +1514 | 4,000,4,200,4,100 |
| MO2612 | 26.914 / 29.585 | 27.467 / 33.343 | -2.671 / 0.670 | 45,696 / 30,334 | 94,402 / 61,394 | +2080 / +3418 | 7,000,6,600,6,800 |

| 同系列official-EOD ATM变动 | 1日vol点 | 3日vol点 | 5日vol点 | 20日vol点 |
|---|---|---|---|---|
| HO2611 | -0.835 | -1.394 | -1.184 | -1.867 |
| HO2612 | -0.404 | -2.300 | -1.315 | -1.075 |
| HO2701 | -0.159 | -1.236 | -0.685 | 缺失 |
| HO2703 | -0.202 | -0.862 | -0.808 | -0.815 |
| IO2611 | -0.339 | -4.202 | -2.223 | -1.422 |
| IO2612 | -0.340 | -3.362 | -1.754 | +0.070 |
| IO2701 | -0.787 | -2.969 | -1.884 | 缺失 |
| IO2703 | -0.486 | -2.076 | -1.549 | +0.223 |
| MO2611 | -2.381 | -8.599 | -7.886 | -0.339 |
| MO2612 | -1.630 | -7.596 | -6.393 | +0.342 |
| MO2701 | -1.756 | -6.217 | -5.184 | 缺失 |
| MO2703 | -1.765 | -4.460 | -4.591 | +0.541 |

来源[G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json)。模型Black76、无风险1.5%、平价forward；中点过滤有效买卖报价且过宽价差剔除，历史使用官方结算、缺失才close。两条IV基准不可直接相减。按绝对Gamma×OI的峰值是风险集中价位，不给dealer正/负Gamma方向。RR=call25−put25为负，说明同delta看跌翼相对贵；MO12月RR约−2.671vol点，明显比HO/IO约−0.98更偏防跌，不能仅凭PCR<1宣称看涨拥挤。远月部分新上市系列没有20日同系列历史，保持缺失。

**结构比较。** 短期MO IV高于HO/IO且倒挂随期限递减，反映风格波动差与事件需求；同系列MO12月3日IV下降7.596vol点并不证明其未来便宜。方向明确且可承受gap才比较线性；方向不确定但预计真实路径大于全部权利金/滑点时才考虑Long Gamma，本批无完整RV20和实时宽跨成本，不宣布成立。有限风险Short Gamma须检验两翼跳空与最大赔付，不能仅用高IV；Call/Put Spread控制权利金但有封顶收益；Calendar/Diagonal受近远IV、forward、不同expiry和行权风险影响；Butterfly只有中心与尾部概率/成交成本可核时才比较。本批没有可执行腿报价，不生成虚构组合Greeks、净成本或代替IC的完美期权对冲。ETF期权链未在本次源提供，50ETF/300ETF等列能力缺口，不把HO/IO误当ETF期权。

### 独立公司发现、利润桥与三条反证

本次仅对工业富联（601138）、中际旭创（300308）、紫金矿业（601899）做原始披露下钻；检索截至截点可得的最新公告，并阅读三季报及中际11月6日经营/回购公告。未取得三者同口径现价、复权3/5/20日收益、正式成份权重与实时证券状态，因此是公司事实发现，不能声称全A股价量筛选或确认估值错配；三者均不占用立即交易名额。10月财报和11月6日公告是本次重新核验的已知经营证据，不是11月12日新催化。

| 公司 | 已核业务与现金事实 | 分歧假设、反证与处置 |
|---|---|---|
| 工业富联 | 2026年前三季度合并收入9414.14亿元、归母净利403.75亿元；合并经营现金流32.16亿元，现金资本支出140.88亿元；CFO/合并净利7.96%，CFO减现金资本支出约−108.72亿元。原表千元已换算。 | AI服务器放量真实，但不能直接归为现金流定价权龙头。竞争解释是高速增长占用营运资金，非盈利造假结论。下一决定性观测是订单交付后回款、存货周转及客户付款条件；若订单放缓同时回款持续恶化，优先撤销多头研究。股价/预期未核，暂不判断便宜或做空。 |
| 中际旭创 | 前三季度归母净利222.38亿元，CFO80.08亿元，现金资本支出91.61亿元；简单现金剩余−11.52亿元。11月6日公告称800G/1.6T订单、价格和毛利率维持良好，主要客户订单基本覆盖2027年；这是管理层披露，不是客户独立确认。 | 高速光互连需求不能因单个GPU公司治理事件就整体否定；但预付锁料和Capex使利润到现金有滞后。继续观察收入兑现、回款和毛利率，而非单凭订单口径加仓。回购用途拟改注销尚须股东会审议，不能把注销当已完成。 |
| 紫金矿业 | Q3金锭与铜精矿显示不同传导：金锭量价下降、成本上升，铜精矿量价提升超过单位成本增幅。见下表重算。 | 矿业公司是多金属、运营与资本配置复合风险，不能替代纯黄金或铜期货。金价上升只有在销量、成本、套保及汇率传导未抵销时才提高净利润。财报能反驳“一切金属涨价均同等受益”，不能确认11月商品现货短缺。 |

**同口径简化毛利桥（Q3对Q2，人民币亿元）**：从各产品销量×（实现售价−单位销售成本）重算，价格/数量/成本效应采用固定顺序；不含内部销售抵销、非控股企业，不等于集团归母利润，也未单独识别库存、套保、税费、少数股东、汇率及并购变化。

| 分产品 | Q2毛利估算 | 销量效应 | 售价效应 | 单位成本效应 | Q3毛利估算 | 环比 |
|---|---:|---:|---:|---:|---:|---:|
| 矿山金锭 | 87.56 | −5.50 | −8.73 | −1.91 | 71.41 | −18.44% |
| 矿山铜精矿 | 107.32 | +6.13 | +8.58 | −2.00 | 120.03 | +11.84% |

公式：ΔGP=(Q3−Q2)×(P2−C2)+Q3×(P3−P2)−Q3×(C3−C2)，金锭kg转g乘1000。不能外推为未来固定弹性；若实现售价不能覆盖新增成本、或销量与回款下降，利润看多假设需撤销。现金流代理只是CFO减购建长期资产现金，不是完整FCFE。

工具比较：若交易的是黄金宏观冲击，先比较黄金本体或已报价限损期权；若交易铜短缺，先比较准确铜期货和曲线；只有公司订单、成本和回款的独立优势足以覆盖经营及估值风险时才考虑股票。AI链三类公司与海外AI篮子共享主题风险，不能分别增加一套预算。本次公司方向仍为观察，下一窗口先核真实价格/状态/估值，不填无依据PE、盈利弹性或胜率。

原始披露直达：[PUB-FII-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-30/1225639532.PDF)；[PUB-INNOLIGHT-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-30/1225643953.PDF)；[PUB-INNOLIGHT-20261106](https://static.cninfo.com.cn/finalpage/2026-11-06/1225660601.PDF)；[PUB-ZIJIN-2026Q3](https://static.cninfo.com.cn/finalpage/2026-10-24/1225620996.PDF)。关键事实、单位、披露时间及限制完整保留在本报告JSON facts，利润桥公式与结果完整列于本节；公开工具抽取记录有hash，未下载原PDF字节，不冒称原PDF哈希通过。

各公司新增发现的意义在于推翻过度简化：工业富联并非利润增长就现金充裕；中际订单披露支持光互连需求，但不是客户独立审计；紫金金锭与铜精矿盈利传导方向不同。公司价格通道的当日价量、复权3/5/20日、RV、公司行动、行业/正式成份、证券状态均未取得，不能确认股价错位、共识修订或便宜。其经营通道完整保留而不替价格通道补数。本次未建立公司新仓，若将来验证独立经营优势，再与行业ETF/铜或黄金本体竞争同一Top5名额与风险预算。

## 9. 未来24小时/7天、下一窗口、完整覆盖与旧观点台账

### 事件先后与风险处置（北京时间）

| 窗口 | 时点 | 事件 | 证据/决策影响 | 来源 |
|---|---|---|---|---|
| 未来24h | 11/13 01:00北京 | EIA WPSR，因Veterans Day由11/12 12:00EST发布 | 官方排期已核；截至截点库存未知；前后不追SC跳空，先核准确曲线 | [SH-COM-EIA-CALENDAR-20261112](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 未来24h | 11/13 21:30北京 | 美国10月PPI（11/13 08:30EST） | BLS已核；同时观察名义/实际利率与美元，不仅headline | [BLS](https://www.bls.gov/schedule/2026/) |
| 当日/未来24h边界 | 美国11/12拍卖日；准确时刻待公告 | 30年国债拍卖 | 财政部季度计划确认日期；未实际读取本期完整公告/结果，不填精确投标时刻或tail | [财政部排期](https://home.treasury.gov/system/files/221/TentativeAuctionScheduleQ42026.pdf) |
| 未来7d | 11/13日期，时区/时刻缺 | IEA November OMR | 不能确定严格24h内，不引用未来预测 | [SH-COM-IEA-CALENDAR-20261112](https://www.iea.org/events/oil-market-report-november-2026) |
| 未来7d | 11/17 04:30北京 | CFTC COT（11/16 15:30EST） | 官方假日延后；不写周五公布 | [SH-COM-CFTC-CALENDAR-20261112](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm) |
| 未来7d | 11/17 21:30北京 | 美国进出口价格 | BLS已核；与PPI/CPI口径不同，不直接视为PCE | [BLS](https://www.bls.gov/schedule/2026/) |
| 未来7d | 11/18约05:20、06:00北京 | NVIDIA财政Q3结果、电话会 | 公司预告已核；财报和治理事实分开，等待订单/利润/现金流 | [G-NVDA-EARNINGS-CALENDAR](https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873) |
| 未来7d | 11/18美国日期为规则推断，精确时刻待核 | 10/27—28 FOMC minutes | Fed说明通常三周后；只标预期日，不当精确日历；下一FOMC12/8—9在7日外 | [Fed calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) |
| 未来7d | 11/18 23:30北京，若无临时调整 | 下一正常EIA周报 | 按官方周三10:30EST规则，仅预告，届时核临时变化 | [SH-COM-EIA-CALENDAR-20261112](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 已发生/本窗未核精确新排期 | 就业11/6、CPI11/10已公布；其余不硬填 | PCE、ISM、零售、其他AI/公司财报、OPEC/USDA | 本批未成功读取这些项目新的精确排期/结果，不将媒体日历当原件；USDA11/10已读，非新增催化 | [G-US-CPI-202610](https://www.bls.gov/news.release/cpi.nr0.htm) [SH-COM-WASDE-20261110](https://esmis.nal.usda.gov/sites/default/release-files/796142/wasde1126.pdf) |
| 中国未来7d | 未取得精确官方新时点 | GDP、社融信贷、PMI/PBOC、工业/零售、A/H披露/政策 | 10月PPI11/9已核，CPI原文超时；社融/信用不假设必然某日发布；本批三A股公告已读，A/H未来公司清单不全 | [G-CN-PPI-202610](https://www.stats.gov.cn/sj/zxfbhjd/202611/t20261109_1965794.html) |
| 未来7d后邻近 | 11/20近月指数期权；11/24 AU/CU；11/26 AP | 到期/交割/展期 | 来自引擎推断或样本expiry；须交易所确认；不在到期前用跨期/跨标的替代风险 | [G-CN-OPTIONS-SURFACE-20261111](https://github.com/farfromexact/China-Options-Engine/blob/a4c16a18d16d039a30e9c162950096c9333a0a49/data/radar_history.json) [SH-COM-OPTIONS-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json) |
| 持续风险 | 无法排定时间 | 天气、地缘、运费、制裁、监管与A/H突发披露 | 没有本批新增原始天气冲击证明；情景风险不计事实支持层，不捏造即时消息 | 情景而非新增事实 |

新信息只有在本截点前公开才纳入当前研究；表中未来日期是预告，不能在报告完成较晚时倒填EIA、拍卖或盘中行情。没有精确发布时刻的日历项保留不确定性。若通胀/油价冲击推动实际利率与股票同时走坏，先减少AI、小盘、金属共同因子；若增长担忧主导、HY走阔同时长债上涨，压平与黄金对冲收益关系也须重审。IV抬升时降低净卖尾部或转已报价限损结构，IV塌陷不自动扩仓；时间退出、催化日与合同到期分开。

### 下一合法交易窗口地图

| 市场/窗口 | 高开情景 | 低开情景 | 平开情景 | 15/30/45分钟确认 |
|---|---|---|---|---|
| 中国股指/股票11/13常规09:30 | IM相对IH高开/跳价超过旧P80000而无回踩，放弃追价；不把A50/HSI错时代理当现金确认 | 若现金风格差与basis同时恶化，停止原多IM思路；低开本身不构成便宜 | 先取两腿同步、正式成份/宽度和证券状态，再看旧尺度是否有效 | 09:45查同周期现金/期货；10:00查持续15分钟与basis；10:15查回踩与成交深度；无数据则不确认 |
| 商品11/13常规09:00，各品种独立制度 | CU差接近/超过旧TP2不追；SC事件跳空先核海外月份/汇率，M高于禁追区不自动恢复 | M跌破逻辑区保留弱化；AU/AG与美元/real同跌先降共同风险；不能日低价倒填成交 | 先区分前夜/current夜盘，核成交与曲线，实体不确认则等待 | 09:15真实首段；09:30检查回踩顺序及价差同刻；09:45复核库存/成本传导；AP无夜盘只日盘 |
| 美国ETF11/13 22:30北京（09:30EST） | SOXX/SMH比率直接>0.308且无回踩放弃；治理事件不免追价规则 | 先分NVDA独有治理/全科技利率冲击；借券召回或QQQ首段失守则不建pair | 先核真实borrow、权重和同步Q，不引用11/11价格 | 22:45观察第一15分；23:00建首30分QQQ低点；23:15才判30—45分联合条件，非提前挂入场 |
| 本截点正在运行的欧美/长夜盘 | 窗口已开始不倒填开盘确认；缺实时不挂过去价 | 有真实仓才按已有订单的止损与保证金应对；无回执不宣布调仓 | 等待下一可核报价窗口；旧last-good只用于中期机制 | 不制造已过15/30/45分钟路径；事件后新时点须新研究截点，当前报告不加入后来事实 |

中国下一常规窗口仍须执行前确认交易所临时公告、券商及具体证券/合约状态；只读研究没有自动调度，也不在未来时点自动刷新/下单。原两张卡窗口已经过去，不承诺下一窗口自动继续。跨报告同一商品、黄金、AI或中国高Beta冲击共同计量；缺账户NAV/持仓只给规模公式。

### 七模块与独立公司覆盖

| 范围 | 实质研究/未入榜原因 | 具体局限 |
|---|---|---|
| 美国利率/国债 | 2/5/10/30Y与2s10s/2s30s/5s30s、10Y实际及粗BEI已核；分析前端政策重估与长端供给竞争，2s30s保留观察。 | 最新期限溢价、OIS/FedWatch隐含路径、具体交易债券DV01/CTD/成本未取得。 |
| FX | 美元/欧元/日元/人民币利差、carry和跨资产流动性机制已比较；H10仅11/6低频历史，不建当前FX方向仓。 | DXY、USD/CNH当前同刻行情和FX skew缺；onshore CNY不替CNH。 |
| AI/科技全链 | Nasdaq、SOXX/SMH、NVDA事件及MSFT/CRWV/ASML/ANET/VRT与FII/中际原始披露下钻，现金/Capex/估值风险分开。 | QQQ同步价、完整中性篮子权重/Beta、借券、事件期权报价和可靠共识未取得。 |
| 原油/能源 | WTI/Brent旧context与SC准确2612/2701曲线分开；EIA/IEA排期已核、库存未知；讨论裂解、成本汇率和地缘溢价竞争。 | WTI/Brent准确月份/实时曲线、OVX、可执行skew、裂解与库存本期原件、OPEC最新供给实报、运费原件不足；不能用SC2701波动率代SC2612。 |
| 黄金 | AU日盘、新旧宏观、月ETF和周CFTC检验政策信用假说；比较3—6月价差、微型期货、债券put搭配和不交易。 | 当前现货/精确COMEX、央行最新购金、海外长端期权链/成交成本缺；局部AU样本不能外推3—6月。 |
| 中国50/300/500/1000及IH/IF/IC/IM、HO/IO/MO、ETF期权 | 固定11/11主次价仓basis、1/3/5/20端点收益及12期限IV/wings/PCR/绝对Gamma已分析；同源双IV基准和历史读取纠错已分离。 | 11/12官方当日行情未取得；RV20内缺10/21；ETF期权链、当日广度/行业贡献/两融/DR007/中国国债缺；expiry假日调整未复核。 |
| 市场风险/流动性 | VIX前收与HY OAS未显示系统性信用崩溃，仍检验拍卖、治理、相关性和保证金冲击；多空小净名义不等风险小。 | VIX term、MOVE、CTA仓位、dealer净Gamma与全市场杠杆拥挤缺，不能推确定性挤仓。 |
| 独立A股公司发现与利润桥 | 限定工业富联、中际旭创、紫金三家公司本批最新原始公告/三季报；回款、Capex、金铜分产品量价成本重算形成对主题的反证。 | 价量发现通道当前行情缺；不声称全A股审计、确认估值错配或当日新经营催化。 |

### 中国商品全范围初筛：63个去重代码＋14个额外源内代码

原LPG按交易所合约代码PG映射；这63个去重产品全部在11/12源内出现，动态额外为 **BZ, JR, LG, OP, PD, PL, PM, PT, RI, RR, RS, WH, WR, ZC**。以下77项均处理了close、结算收益、成交/OI、曲线roll、样本IV。close只是当日价格；收益列明确是**settlement-to-settlement**，不能与第3栏准确close-to-close混称；5观察窗口/20观察波动的连续性与交割换对局限保留。ATM列为产品样本，除共享事实明确合同者外未逐项核与期货主约同月，不能直接配腿或计算同合同IV−RV。没有完整A/B级基差、仓单独立变化和产业供需，不把表格信号提升成可执行方向。来源[G-COM-FULL-SCAN-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)、[SH-COM-COVERAGE-20261112](https://github.com/farfromexact/China-Commodities-Engine/blob/1db709dcf61a7f032747c1702673b3f78255ef8e/data/report_input_latest.json)。

#### 黑色与建材

I/JM的结算日回落伴OI增加与RB/HC偏弱，链条没有一致需求加速；FG/SA微修复而锰硅偏弱，需真实产量/库存/利润区分供给冲击。没有A/B级实体层，暂不做统一空黑色，也不把单品OI增量当新空。跨品种钢矿/焦煤利润可研究但缺转换系数、焦化开工与基差不定量建仓。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| I | I2701 | 671.00 | -1.320 / -2.038 | +20078 | 16.630 | 偏弱/待实体 |
| JM | JM2701 | 1,386.00 | -1.380 / -0.108 | +2195 | 29.725 | 偏弱/待实体；曲线换对不拼z |
| J | J2701 | 1,927.50 | -0.514 / +2.328 | -2900 | 缺失 | 日回撤、5观察仍强 |
| RB | RB2701 | 3,024.00 | -0.263 / +0.033 | +33600 | 9.515 | 日回撤、5观察仍强 |
| HC | HC2701 | 3,170.00 | -0.282 / -0.126 | +8888 | 缺失 | 偏弱/待实体 |
| FG | FG701 | 895.00 | +0.113 / +0.113 | +6838 | 23.020 | 日与5观察同强 |
| SA | SA701 | 981.00 | +0.826 / -0.611 | -37625 | 22.160 | 日修复、5观察仍弱 |
| SF | SF701 | 5,778.00 | +0.000 / +1.192 | -2225 | 12.140 | 变化有限；曲线换对不拼z |
| SM | SM701 | 5,830.00 | -0.749 / -0.137 | -2023 | 10.560 | 偏弱/待实体 |

#### 金属与贵金属

CU近月相对曲线强化而绝对价跌，AL结算偏强、PB偏弱、金银close下跌，显示金属不是单一中国需求交易。铜跨期优于无区别追多有色，但已接近旧目标；AU/AG对金融条件敏感，铝/氧化铝/AD产业利润缺原料与库存，不能凭价格比宣称冶炼利润。BC/CU跨所需汇率、税和交割品级，不假套利。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| CU | CU2612 | 104,950.00 | -0.086 / -1.110 | -956 | 14.430 | 偏弱/待实体 |
| BC | BC2612 | 93,570.00 | -0.308 / -1.128 | -111 | 17.560 | 偏弱/待实体 |
| AL | AL2701 | 22,200.00 | +1.345 / -2.521 | +8024 | 13.710 | 日修复、5观察仍弱 |
| AO | AO2701 | 2,644.00 | +0.038 / +0.152 | +2338 | 13.695 | 日与5观察同强；曲线换对不拼z |
| AD | AD2701 | 21,840.00 | +0.530 / -2.956 | -943 | 14.100 | 日修复、5观察仍弱 |
| ZN | ZN2701 | 25,310.00 | +0.257 / -1.209 | +3588 | 15.390 | 日修复、5观察仍弱 |
| PB | PB2701 | 15,645.00 | -0.760 / -1.353 | +11564 | 13.130 | 偏弱/待实体 |
| NI | NI2701 | 122,940.00 | +0.426 / +1.475 | +4100 | 18.430 | 日与5观察同强 |
| SN | SN2612 | 348,490.00 | +0.223 / -1.041 | -2516 | 30.390 | 日修复、5观察仍弱 |
| SS | SS2701 | 14,020.00 | +0.072 / -0.676 | -3478 | 缺失 | 日修复、5观察仍弱 |
| AU | AU2612 | 852.50 | -1.153 / -2.138 | -2914 | 21.980 | 偏弱/待实体 |
| AG | AG2702 | 12,341.00 | +0.064 / -1.061 | +6057 | 40.275 | 日修复、5观察仍弱 |

#### 能源与化工

SC及多项化工结算日反弹、5观察收益仍弱，PG约−12.12%、L−8.12%、PP−6.69%，提示修复而非全面趋势确认；EG当日量仓扩张异常，需库存/装置确认。原油成本上升可能推产品价也可能压利润，PX/TA/PF/PR和L/PP/MA加工链不能把原料与产品同时上涨视为双利好。SC2701 IV52.05%对历史RV38.98%不自动给short-vol，地缘跳空和18%限幅有尾损。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| SC | SC2701 | 599.90 | +2.020 / -5.503 | +1123 | 52.050 | 日修复、5观察仍弱 |
| FU | FU2701 | 4,095.00 | +1.407 / -6.292 | +3657 | 56.185 | 日修复、5观察仍弱 |
| LU | LU2701 | 4,949.00 | +2.076 / -1.581 | +2733 | 缺失 | 日修复、5观察仍弱 |
| BU | BU2701 | 4,330.00 | +1.420 / -6.562 | -928 | 37.970 | 日修复、5观察仍弱 |
| LPG→PG | PG2701 | 5,960.00 | -0.017 / -12.122 | +2867 | 39.555 | 偏弱/待实体；曲线换对不拼z |
| PX | PX701 | 8,448.00 | +0.721 / -2.102 | +2761 | 29.405 | 日修复、5观察仍弱 |
| TA | TA701 | 6,050.00 | +0.907 / -1.152 | +45836 | 28.900 | 日修复、5观察仍弱；曲线换对不拼z |
| PF | PF701 | 7,762.00 | +1.102 / -1.407 | +710 | 26.370 | 日修复、5观察仍弱 |
| PR | PR701 | 7,630.00 | +1.259 / -1.536 | +1573 | 27.705 | 日修复、5观察仍弱 |
| MA | MA701 | 3,172.00 | +1.574 / -2.195 | -12340 | 41.990 | 日修复、5观察仍弱 |
| PP | PP2701 | 9,192.00 | +1.168 / -6.686 | -3385 | 28.560 | 日修复、5观察仍弱；曲线换对不拼z |
| L | L2701 | 8,368.00 | +0.252 / -8.116 | +8237 | 27.185 | 日修复、5观察仍弱；曲线换对不拼z |
| V | V2701 | 4,931.00 | +0.571 / -0.825 | -28058 | 17.810 | 日修复、5观察仍弱 |
| EG | EG2701 | 5,048.00 | +2.337 / -0.419 | +39468 | 32.225 | 日修复、5观察仍弱 |
| EB | EB2612 | 9,111.00 | +1.445 / -5.440 | +17964 | 35.505 | 日修复、5观察仍弱；曲线换对不拼z |
| RU | RU2701 | 19,435.00 | +1.537 / +2.904 | -4952 | 22.735 | 日与5观察同强 |
| NR | NR2701 | 16,495.00 | +1.689 / +3.435 | -377 | 25.885 | 日与5观察同强 |
| BR | BR2701 | 15,630.00 | +2.041 / +0.162 | +3735 | 32.025 | 日与5观察同强；曲线换对不拼z |
| SH | SH701 | 1,544.00 | -0.578 / +2.045 | -18913 | 25.635 | 日回撤、5观察仍强 |
| UR | UR701 | 1,747.00 | +0.345 / +0.634 | -6543 | 12.635 | 日与5观察同强 |
| SP | SP2701 | 4,670.00 | -0.639 / +0.517 | -182 | 15.910 | 日回撤、5观察仍强 |

#### 新能源与广期所

LC/SI日结算修复但LC、PS的5观察仍负，产业供需与仓单缺变化；PT/PD动态新品有交易记录但期权报价/元数据未充分复核，不提高方向优先级。硅料/工业硅成本链需产能、现金成本和库存，不能从LC的高IV推其他新品同等机会。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| LC | LC2701 | 90,900.00 | +0.701 / -1.894 | -6372 | 44.290 | 日修复、5观察仍弱 |
| SI | SI2612 | 8,610.00 | +0.760 / +0.408 | -23800 | 12.910 | 日与5观察同强 |
| PS | PS2701 | 33,910.00 | +0.088 / -1.993 | +4022 | 28.545 | 日修复、5观察仍弱 |

#### 农产品与软商品

M近远价差收缩削弱原近月强势；油脂OI/P短线强于Y，不能未经汇率与库存确认做跨品种套利。AP close涨3.974%、OI+15554最显著，IV29.685对有断点RV38.755只是long-vol调查线索，精确可买成本缺；JD/LH结算修复、C/CS偏弱，饲料和养殖利润需存栏/现货实证。CF/SR小幅变化而CY曲线换对，跨纺织链不硬接历史zscore。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| A | A2701 | 5,203.00 | +0.172 / +0.635 | +1846 | 13.595 | 日与5观察同强；曲线换对不拼z |
| B | B2701 | 3,883.00 | +0.309 / +0.180 | -1902 | 13.565 | 日与5观察同强 |
| M | M2701 | 3,131.00 | +0.064 / +0.738 | +6115 | 13.055 | 日与5观察同强；曲线换对不拼z |
| RM | RM701 | 2,275.00 | +0.221 / +4.039 | -14983 | 16.100 | 日与5观察同强 |
| Y | Y2701 | 8,771.00 | +0.504 / -0.171 | -13371 | 10.740 | 日修复、5观察仍弱 |
| P | P2701 | 8,997.00 | +1.698 / +0.394 | +7389 | 18.175 | 日与5观察同强 |
| OI | OI701 | 10,063.00 | +1.696 / -0.447 | +7267 | 14.165 | 日修复、5观察仍弱 |
| C | C2701 | 2,187.00 | -0.182 / -1.971 | +12163 | 8.615 | 偏弱/待实体 |
| CS | CS2701 | 2,467.00 | -0.402 / -1.668 | +7370 | 9.240 | 偏弱/待实体 |
| LH | LH2703 | 9,495.00 | +0.159 / +4.298 | +5913 | 26.295 | 日与5观察同强；曲线换对不拼z |
| JD | JD2701 | 3,294.00 | +1.946 / +2.106 | +17774 | 24.465 | 日与5观察同强 |
| CF | CF701 | 15,535.00 | +0.714 / +1.206 | +900 | 9.615 | 日与5观察同强 |
| CY | CY701 | 21,365.00 | +0.070 / +0.612 | +308 | 缺失 | 日与5观察同强；曲线换对不拼z |
| SR | SR701 | 5,187.00 | +0.425 / -1.123 | +16690 | 10.375 | 日修复、5观察仍弱；曲线换对不拼z |
| AP | AP701 | 6,201.00 | +2.896 / +7.418 | +15554 | 29.685 | 日与5观察同强 |
| CJ | CJ701 | 6,395.00 | -0.468 / -0.234 | +4166 | 27.570 | 偏弱/待实体 |
| PK | PK703 | 7,772.00 | +0.077 / -0.941 | +35584 | 9.040 | 日修复、5观察仍弱 |

#### 航运

EC2612结算1日−0.830%、5观察+2.491%，显示反弹后的回撤；缺本期现货指数、班轮报价、地缘航线与交割现金流，不能将SC成本变化线性映射运价。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| EC | EC2612 | 2,477.50 | -0.830 / +2.491 | -282 | 缺失 | 日回撤、5观察仍强 |

#### 动态新增与低流动性

原63之外14项均在源文件出现：BZ/LG/PL/OP/PT/PD等有交易记录，WR低量；JR/PM/RI/WH/ZC当日零量/OI仅记录覆盖，不当可执行市场。新增挂牌/交割细节尚未逐一官方核验，不把所有77称永久全市场或全部具备流动性。

| 代码 | 本源主合同 | close | 结算1D/5观察% | ΔOI手 | 样本ATM% | 初筛解释 |
|---|---|---|---|---|---|---|
| BZ | BZ2612 | 7,664.00 | +0.935 / -8.257 | +311 | 35.045 | 日修复、5观察仍弱；曲线换对不拼z |
| JR | JR611 | 2,662.00 | +0.000 / +0.000 | +0 | 缺失 | 零量/无方向证据 |
| LG | LG2701 | 808.00 | -0.308 / +1.696 | -7 | 7.470 | 日回撤、5观察仍强 |
| OP | OP2701 | 3,612.00 | +0.668 / +0.780 | +42 | 16.945 | 日与5观察同强 |
| PD | PD2702 | 246.80 | -0.646 / +1.589 | +766 | 缺失 | 日回撤、5观察仍强 |
| PL | PL701 | 8,950.00 | +1.411 / -8.323 | +556 | 27.970 | 日修复、5观察仍弱；曲线换对不拼z |
| PM | PM611 | 3,122.00 | +0.000 / +0.000 | +0 | 缺失 | 零量/无方向证据 |
| PT | PT2702 | 374.85 | -1.457 / +1.118 | +699 | 缺失 | 日回撤、5观察仍强 |
| RI | RI611 | 2,479.00 | +0.000 / +0.000 | +0 | 缺失 | 零量/无方向证据 |
| RR | RR2612 | 3,609.00 | -0.111 / +0.642 | -134 | 缺失 | 日回撤、5观察仍强 |
| RS | RS701 | 5,428.00 | +0.574 / -0.513 | -289 | 缺失 | 日修复、5观察仍弱 |
| WH | WH611 | 3,198.00 | +0.000 / +0.000 | +0 | 缺失 | 零量/无方向证据 |
| WR | WR2701 | 3,284.00 | -0.545 / -0.815 | -4 | 缺失 | 偏弱/待实体；曲线换对不拼z |
| ZC | ZC612 | 801.40 | +0.000 / +0.000 | +0 | 缺失 | 零量/无方向证据 |

上述初筛同时比较单边、同合约跨期、跨品种/跨所/跨境、产业利润与波动表达：本批最可核的是M/CU/SC准确期限变化，跨境缺同步汇率/税/交割转换，产业利润缺高质量现货原料，有限风险期权缺可执行买卖报价，故局部保留能力而不全盘否定研究。AP和EG是未入榜异常；低成交与零成交新品不因有字段而被视为可执行；同一价格/曲线/USDA共同冲击去重，不数成五份支持。

### 版本、核心读取与事实边界

Registry `35a9f798618284fd585fb5e199c1f60e5a05de62`，Prompt `on_demand_2026-11-12_v3`，global SHA256 `5c426cbcf887b408221ae4fbaf8b649a5f2525a623ecb1a110758e6e413a04f4`。商品数据Commit `1db709dcf61a7f032747c1702673b3f78255ef8e`，期权数据Commit `a4c16a18d16d039a30e9c162950096c9333a0a49`；同批共享版本与截点。实际执行器为当前ChatGPT协作环境，平台指明GPT-6 Astra Pro，未取得独立模型构建/供应商请求ID；没有额外模型API。`trigger=manual`、`execution_enabled=false`、`production_archive_enabled=true`、`default_archive_mode=production`。

| 实际核心文件 | 字节/交易日 | SHA-256 | 状态 |
|---|---|---|---|
| data/radar_latest.json | 72770 / 2026-11-11 | 6ae5f3be45f9e4d11faf0b3ea2da9438c9cfde45833a851b62bb8f25dfc460ad | read/parse/hash ok；11/12当前EOD stale |
| data/radar_history.json | 1830876 / 2026-11-11 | a12b30345095f7551ee6efc093403a3a22139048a85a7e3a3fde51ab193411aa | read/parse/hash ok；11/12当前EOD stale |
| data/latest.json | 802191 / 2026-11-11 | de55ae8d1560aaf1fc582a323ff46c65d221922b0d17d12a7461f35332b87694 | read/parse/hash ok；11/12当前EOD stale |

商品主输入`data/report_input_latest.json`已实际解析，SHA256 `09d26552dfb70e0fa3454318da563a05b94b7b36b7c355717e3ee92de96a0a6c`；对应模块由同批共享事实保存，结论逐候选判断。本次研究未读取或使用停用股票仓库内容和数据；公司为公开原件抽取记录，记录hash仅证明已留存抽取文字，不冒称原PDF字节hash。事实JSON均保留观测时间、known_at或明确未知、取得时间、来源与限制；截点后读取旧资料允许，截点后新消息未采用。原始期权history较大，file接口空content经实际blob读取纠正，未把截断称空。

### 旧idea台账与不可回写的历史条件

| idea_id/首提 | 原/上一计划与本批处理 | 变化与期限纪律 |
|---|---|---|
| AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106；未核实，不按ID猜日期 | 完整原始谱系及参数见第5栏；当前执行未就绪；实际持仓未知 | 前序rev6改回撤0.3045—0.3060、0.3055确认、Q20—40、stopQ−20/ratio0.3010、目标Q130/220；本次不移旧止损、不重置时间。新增治理事实提升研究优先，当前待评分；整数分批与坏成交R纠正只适用新计划审查。 |
| CN-IM-IH-SMALLCAP-BREADTH-RV-20261111；2026-11-11T20:04:40+08:00 | 完整原始谱系及参数见第5栏；当前执行未就绪；实际持仓未知 | 前序rev3 73分数字计划完整保留；本次历史读取纠错、补20日反证、排除入场未达40k的30k好价；当前11/12状态未知，非研究成功或失败判决。 |
| COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111；2026-11-11T07:08:24+08:00 | 首版11/11 07:08:24北京：多1M2701/空1M2705；价差先280—286且无低于270，AND15分钟收≥288，随后5分钟回踩284—288守住，AND CBOT≥1215，AND深度正常；原50/50在286附近及再次守290。止损268；逻辑15分钟<268 OR CBOT<1200 OR近月深度恶化。TP330/360；11/18日收或更早移仓退出；开盘>310无回踩、首印<270、同步报价/参数缺则放弃；成本80元情景。 | 初始268/330/360与上版290/340/370并列；这些历史变更不适用于假定已持旧仓。本次不再提高止损或延长时间，旧USDA不算新增催化。 |
| COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106；2026-11-06T07:09:57+08:00 | 首版11/6 07:09:57北京：多1CU2612空1CU2701；09:15以后价差先850—900、15分钟不破800，随后收复900 AND CU2612≥103800 AND同刻深度。入900/925/950，30%/30%/40%历史拟议；止损750；15分钟<750 OR LME<13800逻辑失效；TP1400/1700；11/20 14:45退出；直上1050无回踩放弃。旧分批对一组整数手不成立，未当已执行。 | 新增到全球统一观察优先项，不认领第二次发现；相关商品idea保留同ID。 |
| COM-E-SC2612-HORMUZ-RECLAIM-LONG-20261111；2026-11-11T19:32:42+08:00 | 首版11/11 19:32:42北京：从原看空父idea转为条件做多SC2612；21:00同源核价后Brent≥93 AND SC首15分钟收≥610 THEN5分钟回踩608—611守住 AND SC2612−SC2701≥10；50%610、第二确认50%不高于612，>614放弃。止损599；Brent<91.80 OR曲线<5失效；TP630/648；11/17 22:55退出；成本1500元/手情景。换方向保留父ID，不抹原空头。 | 前序晨版Brent门槛92.5与首次晚版93并列保留，不回填为相同参数；前序68分不沿用。库存未公布、价格与曲线不齐强。SC2701 IV/RV不可移为2612执行参数。父idea COM-E-SC2612-DEESCALATION-FAILED-REBOUND-SHORT-20261109 保留。 |
| UST-2S30S-HOT-CPI-FLATTENER-20261111；未核实，不按ID猜日期 | 首版未取得，不倒推首次日期。前序rev4 67分观察2s30s压平，未提供可核交易债券/CTD/DV01与完整参数，不能补造旧持仓。 | 无新同口径曲线价，不伪造评分上调/已赚钱；本次待评分、实际仓位未知。 |
| GOLD-POLICY-CREDIT-CONVEXITY-20261111；未核实，不按ID猜日期 | 首版未取得，不倒推首次日期。前序rev3 65分观察；3—6月凸性构想，未延用旧行权价。 | 相较前序弱化价格证据，不把长期用途等同立即买入或追认已有对冲成功。 |

M/铜/SC完整最初与上一参数在JSON `idea_ledger.historical_origin_record`及上一计划原记录中保留；两核心卡所有AND、OR、先后、持续确认、放弃和时间退出同时保留在`sections`。本批没有真实成交回执，没有模拟事后PnL；价格达到阈值不证明顺序、成交或期权赚钱。`machine_representation_complete=false`，正文条件是完整研究语义，不能作为自动执行器输入。

## 10. 归档交付与最终行动四行

本次计划正式批次为`reports/2026/11/12/20261112T234244+0800_5eb01e91f7534ca58a37d7036a7fddde/`，文件`global.md`、`global.json`与同批商品双文件、`run_manifest.json`；不添加实验前缀，不覆盖历史晨晚稿。报告生成后由统一协调者校验、逐文件实际写入回读、登记`manifests/runs.json`并协调`latest`。**最终真实归档/索引/latest状态以同批[run_manifest](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/main/reports/2026/11/12/20261112T234244+0800_5eb01e91f7534ca58a37d7036a7fddde/run_manifest.json)及最终交付为准**；本正文不预报写入或回读通过。CI状态`pending_or_unverified`，不把静态本地校验当CI。全文和JSON均从同一结构生成。

A. 截至共同截点可立即建立的新仓：没有。实际执行预算为0，未确认任何真实成交或持仓；保持人工启动与 execution_enabled=false。

B. 仅挂研究条件：SOXX/SMH等下一真实现金窗口的同步报价、借券与完整回踩链；IM/IH等下一中国日盘当期宽度、basis、Beta与整数篮子条件；美债2s30s等拍卖/PPI后的曲线及DV01。均不是已提交订单，补齐后研究压力预算上限0.25% NAV且与商品报告同主题共享。

C. 继续观察：铜期限结构强但不追1680；M价差294的弱化与303回收是否真有实体/海外确认；SC在EIA后与曲线同向验证；黄金3—6月有限凸性、AP局部vol线索、AI各环节现金回收和三家公司利润桥。缺报价只限制对应交易，不取消已完成研究。

D. 必须回避：用已过窗口或旧夜盘冒充当前信号，铜近旧目标追价，未询价裸卖波动，缺借券/Beta的假中性与碎手50/50，移动旧止损或重启AI20天。若此前确有仓且原止损、逻辑失效、时间退出或保证金约束已被真实数据触发，则按原计划在合法可成交窗口减仓/退出；无回执不称已操作。
