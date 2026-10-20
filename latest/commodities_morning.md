# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-21｜版本：commodities_morning｜prompt_version：radar_2026-10-12_stock_v1｜数据协议：china_commodities_core_2026-10-17_v1**  
**生成时间：2026-10-21 07:11 北京时间｜信息截点：2026-10-21 07:08 北京时间**

## 1. 今天一句话结论

**截至本报告时点，无可立即执行的合格新交易；油链夜盘暴跌却与外盘仅小跌冲突，RM/LH空头也已进入追价区。**

已研究但优势不足：追空SC/FU、追涨AG/SN、抄底橡胶。研究机会存在但等待条件/报价：RM701与LH2701的反抽失败空、SC2612极端价差修复多。数据不足不能判断：油链真实夜盘曲线、DCE官方独立核价、所有期权结构的可成交成本。最有价值的三个待验证观察是：09:15—09:45油链是否修复；RM701能否在2258下形成二次确认；LH2701是否破9950而非低开后快速收回。

## 2. 数据质量与覆盖

本次固定读取ref：Global Radar `90c33753fc3cec5bb8c046aede3e7b3ff6644ad8`；China-Commodities-Engine `87d6e885ccbfbd15555d955506d780db9eaf43c3`；China-Stock-Engine `79c96a9d9e73a7c2a13d340229acc7c64f4ec144`。

| 模块 | requested/source/generated | 实际范围与质量 | 决策限制 |
|---|---|---|---|
| Futures | requested 10-20；source 10-20；10-21 06:03生成 | 806合约、77品种、五所；source-date match 100%，full_market_ready=true；critical/unknown/duplicate/invalid OHLC/负量仓均0，8个零量零仓占位 | vendor全市场分析就绪不等于全部交易所独立认证；占位记录不入排行 |
| Market State | 09-15至10-20；06:03生成 | 同准确合约20日历史，可用1/3/5/20D、RV20、量仓z和曲线 | roll警告品种不把跨月拼接当真实收益 |
| Physical | source 10-20；06:04生成 | 20目标中18 fresh、2 unavailable；validation/published=true；无carried | 所有basis均C级且eligible=0；现货绝对值只作背景，不计完整实体层或套利 |
| External | source 10-20；06:04生成 | 22目标中17 fresh、5 unavailable；WTI、Brent、LME、COMEX、CBOT、BMD、ICE可用 | 全部context_only；不同收盘时点不构成跨境套利 |
| Night | trading_date 10-21；会话10-20晚至10-21凌晨；05:57生成 | 806请求、414夜盘、168制度外、10无成交、214 query error/unresolved；validated/published=true、coverage_complete=false | `vendor_latest_trade_asof_snapshot`，official night close=false；重点同合约可作信息弹性，不能描述精确分钟路径 |
| Options | trade date 10-20；10-21 06:04北京可得 | core_v1/sampled_strikes；45/64品种、1022合约、45 series；ATM ready 44、skew 30、surface/positioning/execution均0；IV覆盖100%、OI 96.97%、bid/ask 0% | 可研究局部ATM/skew；不能编权利金、净成本、滑点、全链PCR或dealer Gamma |
| Contract Metadata | trade date 10-20 | effective match 73.45%；multiplier/tick/margin/limit覆盖30.15%；DCE contract info失败 | 重点卡缺动态参数时限制执行；静态规格与动态通知分开 |
| 官方EOD交叉核对 | trade date 10-20 | SHFE 238、INE 63、CZCE 243、GFEX 48匹配；所有可比close/settle/pre-settle差异为0；DCE HTTP 412 | state=partial来自DCE source error，不等于已发现价格差异；volume/OI未被该核对验证 |
| Stock | last-good 10-15；10-16回填失败 | 运输SSL握手超时；现有映射只含少量金铜/钢铁公司，未覆盖本期油链、饲料和生猪候选 | 不把旧股价或概念映射当当前利润证据；股票候选为0 |

Night日历一致性：`trading_date=2026-10-21`、`session_start_date=2026-10-20`、`session_end_date=2026-10-21`，与正常周二晚归属周三交易日一致，`calendar_mismatch=false`。SC/AG/AU快照到02:30，FU/RM/MA等为23:00附近供应商最新成交；不把兼容字段`night_close`称为交易所官方收盘。

覆盖核对：用户列出的63个代码全部进入映射初筛，其中LPG按引擎代码PG；同时扫描BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态或低流动性品种。实际取得并分析77个品种。板块限制：DCE官方核价和合约参数未完成，黑色原料、油脂、养殖、塑化仍可用vendor核心数据研究，但不能据此宣称官方全闭环或直接执行。

核心入口：[统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/report_input_latest.json)｜[EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/latest.json)｜[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/night_session/last_run_status.json)｜[期权质量](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/options/quality_latest.json)｜[官方交叉核对](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/crosschecks/futures_latest.json)。

## 3. 晨间仪表盘

下表1D/5D按结算价；curve为近流动月减次近流动月，不是现货基差。Night为合法归属10月21日的供应商快照，相对close是隔夜新增主锚；`ΔOI`只作归因线索。

| 板块/准确合约 | 10-20 EOD close/settle | 1D / 5D | 成交量 / OI / EOD ΔOI | curve | Night latest / vs close / Night ΔOI | 外盘/Options | 信号 |
|---|---:|---:|---:|---:|---|---|---|
| 原油 SC2612 | 727.2 / 727.3 | +1.18% / -0.64% | 146,437 / 35,749 / +2,469 | +0.55% | 694.8；-4.46%；+1,101；02:30 | Brent完整收盘约109；ATM730 IV56.64%、RR25 +6.22，但夜盘后moneyness失真 | 内盘暴跌与外油仅小跌冲突；不追空 |
| 燃油 FU2701 | 4,976 / 4,928 | -0.59% / +6.00% | 493,047 / 237,144 / +6,146 | +10.33%* | 4,658；-6.39%；-11,502；23:00 | 期权标的FU2612，不能替代本合约；HSFO/VLSFO缺 | 旧多失效；强EOD结构与夜盘价格冲突 |
| 菜粕 RM701 | 2,274 / 2,299 | -2.17% / -3.32% | 891,955 / 704,711 / +19,341 | -1.22% | 2,264；-0.44%；+760；22:59 | ATM2300 IV17.08% vs RV18.98%，RR25 +0.83；无报价 | 趋势空延续，但接近日内低位 |
| 生猪 LH2701 | 9,995 / 10,110 | -2.03% / -5.38% | 170,782 / 207,052 / +15,474 | -3.56% | 制度无夜盘 | Options缺；DCE官方核价缺 | 空头结构最干净，仍须日盘触发 |
| 甲醇 MA701 | 3,157 / 3,137 | -1.32% / -2.97% | 2,146,072 / 860,774 / +21,094 | +4.46%* | 3,049；-3.42%；+12,775；23:00 | 期权标的MA612；Brent仅小跌 | 价格层弱，但曲线跨roll、不可作确认 |
| 纯碱 SA701 | 938 / 946 | -0.73% / -2.97% | 868,888 / 1,317,795 / +9,993 | -2.44%* | 954；+1.71%；-8,950；23:00 | ATM950 IV24.19%、RR25 +2.86；execution false | 减仓反弹，不能等同趋势反转 |
| 玻璃 FG701 | 846 / 854 | -1.04% / -0.58% | 1,014,567 / 1,611,348 / +92,017 | 0.00% | 855；+1.06%；-49,993；23:00 | ATM850 IV22.25%、RR25 +5.35；现货C级 | 夜盘修复但量仓与日盘相反 |
| 白银 AG2612 | 13,967 / 13,861 | -0.68% / -5.63% | 306,494 / 280,523 / +1,015 | -0.19% | 14,075；+0.77%；+195；02:30 | COMEX银58.14；期权样本AG2611非本合约 | 内外同向修复，但不追高 |
| 黄金 AU2612 | 892.06 / 893.02 | -0.94% / -1.09% | 188,139 / 219,729 / -2,342 | -0.14% | 890.24；-0.20%；+4,484；02:30 | COMEX金4142.6；ATM896 IV19.93% | 弱势中性，不抄底 |
| 沪铜 CU2612 | 108,830 / 108,430 | -0.67% / -1.71% | 57,561 / 164,633 / +2,350 | +0.70% | 109,090；+0.24%；+2,280；01:00 | LME铜14,453.5美元/吨；期权样本CU2611 | 有限修复，等待109500上方确认 |
| 锡 SN2611 | 382,580 / 380,490 | +0.49% / — | 128,891 / 28,985 / — | 产品结构待核 | 386,970；+1.15%；-1,038；01:00 | ATM380000 IV26.70%、RR25 -4.95 | 价格强但减仓与put偏贵反对追涨 |
| 航运 EC2611 | 2,555 / 2,653 | -4.43% / -3.93% | 22,633 / 16,761 / -2,550 | -16.94% | 无夜盘 | 缺执行期权与现货运价同窗 | EOD close -7.96%，流动性风险高，回避追空 |

\* FU、MA、SA的产品curve存在错月或pair-roll限制，只作产品扫描，不能代替正式合约Night Curve。Night near/next两腿未在统一层同时给出，因此本期不生成正式Night Curve。

海外最近完整会话：repo的10月20日收盘为WTI 98.16美元/桶、Brent 109.01美元/桶、LME铜14,453.5美元/吨、铝3,025.5、锌3,739、镍15,795，COMEX金4,142.6美元/盎司、银58.14，SGX铁矿91.2美元/吨、CBOT大豆1,247.25美分/蒲式耳、豆粕343美元/短吨。Reuters同一交易日口径显示Brent结算108.79、活跃WTI 97.82，说明合约与截点不同，只用于验证“外油没有同步下跌4%—6%”，不拼接套利。[Reuters油价](https://www.reuters.com/business/energy/oil-eases-markets-assess-potential-waiver-russian-energy-middle-east-supply-2026-10-20/)；[Reuters贵金属](https://www.reuters.com/world/india/gold-slips-investors-weigh-fed-rate-outlook-2026-10-20/)。

## 4. 相比上一交易日/昨晚真正变化

1. **SC昨晚条件多头在入场前失效。** 旧计划要求21:15后守730且Brent不低于110；SC2612供应商快照最终694.8，较前收-4.46%，远低于718失效位。没有成交反馈，不假定曾建立仓位；原idea进入`invalidated_before_entry`。
2. **FU旧多再度失效且不能用强curve自动复活。** FU2701夜盘4,658、较前收-6.39%，OI较EOD少11,502；虽EOD产品curve仍+10.33%，但没有同会话两腿Night Curve，不能把旧结构当当前确认。
3. **RM空头方向延续但没有触发旧2258破位。** Night低2261、快照2264；旧“2258下二次确认”尚未出现。EOD价跌仓增与contango仍支持研究，但当前位置不允许追空。
4. **LH比RM更干净、但没有夜盘。** 10月20日close 9,995、OI增加15,474、curve -3.56%；下一条新证据只能来自09:00日盘，不把无夜盘视作缺陷。
5. **贵金属分化。** AG夜盘+0.77%并与外银上行一致，AU仍弱；AG期权样本是2611而不是正式卡的2612，不能把局部偏度算作第五层确认。
6. **期权研究广度保持、执行能力仍为零。** 45/64品种、ATM ready 44、skew 30，但0条execution-ready；这不是“全市场无期权机会”，只是本期不能给可成交结构。

旧观点台账：

- `COM-E-SC2612-GEOPOLITICAL-RECLAIM-LONG-20261020`：由等触发改为入场前失效，原因是Night价格跌破失效位；不假定成交。
- `COM-M-FU2701-HSFO-TIGHTNESS-LONG-20261018`：继续维持旧计划失效；强curve未被合法Night Curve复核，不能复活。
- `COM-M-RM701-NIGHT-BREAK-SHORT-20261020`：方向维持、触发未完成；今日改等反抽失败或2258二次破位。
- `COM-E-LH2701-WEAK-CURVE-SHORT-20261013`：逻辑维持；等待日盘，不假定此前成交。
- `COM-M-AL2612-CONTINUATION-LONG-20261020`：Night高23170但快照22975；没有分钟触发/成交路径，继续降级观察。

## 5. 产业链地图与Stock利润桥

1. **原油→燃料油→化工：** 外盘Brent/WTI仅小幅收低，SC/FU却分别-4.46%/-6.39%，MA-3.42%。最强解释是中国夜盘对地缘溢价或品种流动性的更激烈去化；竞争解释是供应商快照范围并非完整官方终盘。今天先验证是否修复，不把价差称跨市套利。置信度：中。
2. **油脂—菜粕—生猪：** RM日盘价跌仓增、Night再弱，LH日盘价跌仓增且contango；CBOT大豆/豆粕完整会话也偏弱，但中国现货压榨利润和养殖利润缺失。趋势空成立，实体层不足。置信度：中。
3. **纯碱—玻璃—烧碱：** SA/FG夜盘反弹但均伴随OI下降，SH近乎持平且OI上升；局部期权call skew偏贵。更像空头回补或保护需求线索，而非已确认新多。置信度：中低。
4. **贵金属—有色：** AG与海外白银同向修复，AU仍受实际利率/美元约束；CU夜盘小涨与LME铜高位相符，AL回落。紫金映射能说明金铜售价影响，但Stock最后有效价量为10月15日，产量、成本、套保、汇率及少数股东约束未更新；直接商品优于股票。置信度：中。
5. **橡胶—轮胎：** NR -2.13%、RU -1.66%，但两者Night OI均下降；BR亦弱。没有仓单、轮胎开工或准确公司利润桥的新数据，不把价格共振算实体确认。置信度：中低。

Stock决策贡献为“否定即时股票替代表达”，不是独立第六层。宝钢/紫金旧映射仅作利润传导背景；没有相关公司当前报价、证券状态与最新财务原件，股票候选为0。

## 6. 统一机会榜

| 排名/idea_id | 方向、期限、工具 | 逻辑/赔率/催化/价曲波/拥挤 | 总分 | 有效支持层；反证/缺口 | 三轴状态 |
|---|---|---:|---:|---|---|
| 1 `COM-M-RM701-NIGHT-BREAK-SHORT-20261020` | 条件空，1—3D，RM701期货 | 18/15/13/13/9 | **68** | 支持1、2；3缺，4仅弱映射，5中性且无报价 | 待验证优势/证据部分/等反抽或2258二次确认 |
| 2 `COM-E-LH2701-WEAK-CURVE-SHORT-20261013` | 条件空，3—10D，LH2701期货 | 18/14/12/13/10 | **67** | 支持1、2；实体混合，4/5缺失 | 待验证优势/证据部分/等09:15—09:30触发与参数 |
| 3 `COM-M-MA701-NIGHT-WEAKNESS-SHORT-20261021` | 条件空，1—3D，MA701期货 | 18/14/12/12/10 | **66** | 支持1、4；curve pair-roll，3缺，期权错月 | 待验证优势/证据部分/不追低开 |
| 4 `COM-M-AG2612-SILVER-REPAIR-LONG-20261021` | 条件多，1—5D，AG2612期货 | 17/14/10/12/11 | **64** | 支持1、4；curve弱，期权错月且无报价 | 早期优势/证据部分/等14075上留存 |
| 5 `COM-M-SC2612-NIGHT-DISLOCATION-RECLAIM-LONG-20261021` | 价差修复条件多，1—2D，SC2612期货/期权仅研究 | 15/17/11/7/9 | **59** | 仅4支持；1强反对，2需重算，3缺，5夜盘后失真 | 数据冲突/证据不足/仅等reclaim，不执行 |

所有分数均遵守证据层上限：RM/LH/MA/AG仅两层，最高不超过69；SC仅一层有效支持，不超过59。分数是研究优先级，不是胜率或仓位。

## 7. 三张研究/交易卡

### 卡1｜RM701条件空（延续原idea_id）

- **事实：** EOD close/settle 2,274/2,299，1D -2.17%、5D -3.32%，EOD OI +19,341，curve -1.22%；Night 2,264、相对close -0.44%，低点2,261，OI较EOD +760。ATM2300 IV17.08%低于RV20 18.98%，但bid/ask为0。
- **定价/推断：** 市场继续定价油粕供给偏松；最强反证是两日跌幅已大、局部call skew为正且缺现货压榨利润。价格/OI不用于断言新空身份。
- **入场：** 09:00首跳不追。好情景：09:15后反抽2,272—2,288失败再破2,258；中等：09:30后直接破2,250但15分钟不收回，仓位减半；坏情景：低开低于2,230，放弃追空。
- **风控：** 计划止损2,306；逻辑失效2,355；TP1 2,230、TP2 2,180；3个交易日时间退出。若此前已按条件建仓才执行减仓/退出，当前不假定持仓。
- **参数：** 10吨/手、tick 1元/吨、tick价值10元；仓库基准margin 7%、limit 6%，最后交易日2027-01-14、最后交割日1月19日；夜盘通常21:00—23:00，动态调整盘前再核。[郑商所菜粕规则](https://www.czce.com.cn/cn/uploadfile/2023/01/10/20230110103802217.pdf)。按2,258至2,306计划风险约480元/手，未计跳空；一板约1,379元/手。期货止损不封顶。

### 卡2｜LH2701条件空（延续原idea_id）

- **事实：** EOD close/settle 9,995/10,110，1D -2.03%、5D -5.38%、20D -17.17%；OI +15,474，curve -3.56%。制度无夜盘，09:00是唯一新增窗口。
- **定价/推断：** 价格与结构继续指向近端供给压力；竞争解释是20日跌幅已大、存栏下降与政策预期可造成急反弹。缺最新养殖利润和官方DCE核价，第三、四、五层不成立。
- **入场：** 首选09:15后反抽10,080—10,180失败；备选09:30后低于9,950且15分钟不收回、curve仍≤-3.5%。好成交10,030—10,120；中等9,950—10,030减半；低于9,880不追。
- **风控：** 计划止损10,220；逻辑失效10,320；TP1 9,800、TP2 9,500；5个交易日退出。
- **参数：** 官方标准16吨/手、tick 5元/吨、tick价值80元；无夜盘，实物交割，最后交易日为交割月倒数第4个交易日。[大商所生猪合约规则](http://www.dce.com.cn/dalianshangpin/ywfw/jystz/ywcs/2025082716495836078/index.html)。DCE动态margin/limit本次未核，execution仍受限；以10,050到10,220估算计划风险约2,720元/手，不含跳空和限板。

### 卡3｜SC2612极端价差修复多（新研究问题，不是旧多复活）

- **事实：** EOD close/settle 727.2/727.3；Night快照694.8、相对close -4.46%，低670、高740.4，OI较EOD +1,101；同期Brent完整会话约109美元，仅小幅收低。旧SC多已在718下失效，本卡是不同机制的价差修复研究。
- **定价/推断：** 若内盘跌幅主要来自风险溢价去化或流动性冲击，开盘可部分回补；竞争解释是中国盘提前反映新的供应/政策消息，外盘尚未完全定价。Night价格强反对，只有海外映射一层支持，因此仅59分。
- **入场：** 09:00绝不抄底。只有09:15重夺705、09:30守住710，准确SC2611—2612曲线不转负且Brent≥108，才允许NAV 0.25%以内研究试仓。好成交705—712；中等712—720减半；高于724不追。计划止损688，逻辑失效680；TP1 724、TP2 738；2日退出。
- **参数/期权：** 1000桶/手、tick 0.1元/桶、tick价值100元；SC2612最后交易日11月30日、最后交割日12月7日，夜盘21:00—02:30。10月9日通知口径的涨跌停16%、一般保证金18%，盘前须重核；按22元/桶止损距离计划风险约22,000元/手，天然不适合小账户线性追单。[INE交易时间](https://www.ine.cn/services/calenderandholidays/tradinghours/)｜[INE风险参数通知](https://www.ine.cn/eng/circularnews/circular/202610/t20261009_833652.html)。ATM730 IV56.64%与EOD标的对应，夜盘后已失真且execution=false；call spread只能`research only; manual quote and manual confirmation required before execution; no premium quoted`。

三卡共同风险：试仓NAV 0.25%—0.75%，确认0.75%—1.50%；同一油链、饲料—养殖因子跨商品与股票合并，高确信主题总预算≤2.5%—3.0%。压力覆盖1/2涨跌停、夜盘/开盘gap、流动性消失、保证金提高、相关性断裂、IV跳升/塌陷、交割挤压和中国休市期间海外波动。

## 8. 商品期权专项

- 样本为10月20日EOD，`collection_scope=core_v1`、`analytics_scope=sampled_strikes`；45/64品种成功、45 series、ATM ready 44、skew ready 30。完整surface、positioning、execution均为0，dealer_gamma_direction_known=false。
- **SC2612：** ATM730 IV56.64%、RR25 +6.22、BF25 +0.76；EOD时与RV20 55.07%接近。Night标的跌至694.8后，原ATM/Delta已不可比，不能把call skew直接当当前看涨证据。
- **RM701：** ATM2300 IV17.08% vs RV20 18.98%，RR25 +0.83；低IV-RV不自动证明便宜，且无bid/ask，不给权利金或最大损失。
- **FG701/SA701：** ATM850/950 IV22.25%/24.19%，RR25 +5.35/+2.86；只能说明抽样call相对put IV较高，不推全链crowding。
- **AG：** 有效series是AG2611而正式观察为AG2612；错月不替代。AU2612 ATM896 IV19.93%、RR25 +0.49，但方向证据不足。
- **MA/FU/AL/CU/NR：** Options underlying与期货正式卡月份不一致者，只作产品背景；单月样本不外推term、wing或tail。所有候选结构执行前必须取得具体腿bid/ask、净支出、Delta、Vega、行权交割与流动性。

波动率相对价值结论：SC高IV与高RV相称；RM局部IV低于RV但事件/成交成本未知；AG/AU方向分化。没有可立即执行的vol RV、跨期或偏度交易。

## 9. 09:00开盘风险地图

| 信息层 | 已知事实 | 开盘含义 |
|---|---|---|
| Previous China EOD（10-20） | SC收涨、FU强curve；RM/LH弱；EC极端下跌 | 日盘结构不能直接覆盖Night新价格 |
| Current T Night（归属10-21） | SC -4.46%、FU -6.39%、MA -3.42%、RM -0.44%、NR -2.13%；SA +1.71%、AG +0.77%、SN +1.15% | 油链与化工潜在大幅低开，贵金属/建材偏高开；均是vendor snapshot而非官方终盘 |
| 07:00海外最新完整会话 | Brent约109、WTI约98，跌幅显著小于内盘油链；银涨、金弱；LME铜高位 | 油链存在修复与继续脱钩两种路径；AG比AU更强，CU有限支撑 |

- **潜在低开：** SC、FU、MA、BR、NR/RU；SC<690或FU<4600不立即追空，先判断限幅和流动性。
- **潜在高开：** SA、FG、AG、SN；首跳不追，因多数伴随OI下降或偏度反证。
- **09:15：** 检查Night gap保留率、买卖盘厚度与动态限幅；油链能否重夺705/4,720。
- **09:30：** 核准确近次月曲线、成交量与OI；RM是否破2258，LH是否破9950且不收回。
- **09:45：** 只有价格、曲线、海外仍同向才把研究候选升级为试仓；没有实际报价和参数则继续等待。

信息弹性：SC/FU已在Night预交易了远大于外盘收盘的负向变动，09:00更像“验证超调还是新信息”而非简单跟随Brent。RM/LH的优势来自趋势而非突发事件，追价成本比方向判断更重要。

## 10. 未来24小时 / 7日事件

- **10月21日09:00—09:45：** 中国日盘吸收Night极端油链变动；Delta策略先确认gap留存，不提前裸卖波动。
- **10月21日22:30北京：** EIA Weekly Petroleum Status Report常规10:30 ET发布，关注原油、汽柴油库存与炼厂开工；SC/FU在发布前总风险合并。[EIA WPSR](https://www.eia.gov/petroleum/supply/weekly/)。
- **10月22日20:30北京：** USDA Weekly Export Sales常规08:30 ET发布；关注中国大豆采购、豆粕和油脂映射。[USDA发布页](https://www.fas.usda.gov/report-release-announcement/weekly-export-sales-309)。
- **10月24日03:30北京：** CFTC COT通常周五15:30 ET发布，只作滞后拥挤背景，不倒推今日中国资金身份。[CFTC日程](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)。
- **10月27—28日：** FOMC进入一周窗口；贵金属Delta/Vega暴露需防实际利率与美元共同冲击。
- **持续事件：** Hormuz航运、胡塞对沙特设施袭击、俄罗斯燃料出口恢复与炼厂政策可令油价双向gap；天气和南美播种影响豆系，但本期没有足够即时天气证据计层。
- **交易所/公司：** 每次行动前复核动态保证金、限幅、临近到期和交割；Stock引擎没有10月15日后的有效公司价量/披露，本期不设公司催化。

## 11. 行动前覆盖、缺口与输入版本

- 黑色/建材：I/JM/J/RB/HC/FG/SA/SF/SM均扫描；异常是JM弱、FG/SA夜盘修复；DCE官方核价和A/B basis缺。
- 金属：CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG均扫描；异常是SN、AG强于AU/AL；部分期权错月。
- 能源化工：SC/FU/LU/BU/PG/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP均扫描；异常集中SC/FU/MA/橡胶；HSFO/VLSFO、SC/LU实体缺。
- 新能源：LC/SI/PS及GFEX动态品种均扫描；LC仍高波，SI弱；GFEX无夜盘不构成数据错误。
- 农产品：A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK均扫描；RM/LH最弱；DCE Night缺失系接口范围限制，LH制度无夜盘。
- 航运：EC EOD异常下跌且无夜盘，流动性与运价同窗不足，回避追空。

关键缺口：214个Night具体合约查询失败、DCE官方核价HTTP 412、仓单5项carry-forward且多所刷新失败、全部basis C级、期权bid/ask 0%、Stock停留10月15日。沿用last-good不算新增催化；本报告没有用这些缺口证明“无机会”。

## 来源

- [China-Commodities-Engine统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/report_input_latest.json)（2026-10-21 06:05北京，支持模块日期、全范围扫描、Night和Options局部指标）
- [EOD futures](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/latest.json)（2026-10-20，支持准确合约OHLC/settle/volume/OI）
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/market_state_latest.json)（截至2026-10-20，支持1/3/5/20D、RV20与曲线）
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/physical/latest.json)与[External](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/external/latest.json)（2026-10-20，支持现货背景与海外完整会话）
- [Options quality](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/options/quality_latest.json)与[surface samples](https://github.com/farfromexact/China-Commodities-Engine/blob/87d6e885ccbfbd15555d955506d780db9eaf43c3/data/options/surface_latest.json)（2026-10-20，支持局部ATM/skew及执行限制）
- [Reuters油价](https://www.reuters.com/business/energy/oil-eases-markets-assess-potential-waiver-russian-energy-middle-east-supply-2026-10-20/)与[Reuters贵金属](https://www.reuters.com/world/india/gold-slips-investors-weigh-fed-rate-outlook-2026-10-20/)（2026-10-20完整海外会话）
- [Stock Engine映射](https://github.com/farfromexact/China-Stock-Engine/blob/79c96a9d9e73a7c2a13d340229acc7c64f4ec144/config/company_commodity_exposures.json)（最后有效交易日2026-10-15，支持利润桥约束与无当前候选结论）

A. 今天没有应立即建立的新仓位。  
B. 今天仅应挂条件的候选：RM701反抽2272—2288失败再破2258；LH2701反抽10080—10180失败或09:30后破9950；SC2612仅在重夺705/710、Brent≥108且曲线不转负时研究修复多。  
C. 今天继续观察：FU2701能否重夺4720、MA701低开留存、AG2612的14075确认、CU2612能否站109500，以及SA/FG减仓反弹。  
D. 今天必须回避或有条件退出：追空SC/FU/MA首跳、追涨AG/SN、抄底橡胶、无bid/ask期权；若此前已按条件建仓，SC旧多与FU旧多均按失效处理。
