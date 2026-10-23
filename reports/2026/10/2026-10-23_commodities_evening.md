# 全球商品期货期权高风险机会雷达｜晚间版｜2026-10-23

> 信息截点：2026-10-23 19:30 北京时间；实际生成：2026-10-23T19:38:28+08:00。中国最新完整日盘为2026-10-23；今晚21:00尚未开始，周五夜盘归属2026-10-26交易日。只做研究与决策支持，不下单，不假定持仓或成交。

## 1. 一句话结论

截至本报告时点，无可立即执行的合格新交易；油链只等21:00后回踩确认，白银只等反抽失败，禁止追涨油品或追空AG。

今晚值得承担的是“有顺序、有回踩、有跨市场/曲线确认”的小风险，不是首跳方向赌注。已研究但优势不足：SA/SH、黑色、有色、航运与新能源；研究机会存在但等待条件/报价：SC、FU、AG；关键数据不足不能判断：DCE夜盘与官方价格核对、完整期权链及可成交权利金。最有价值的下一观察是21:15油链留存、21:30回踩结构、21:45白银反抽是否失败。

## 2. 事实台账、数据质量与全范围覆盖

| fact_id | 可追溯事实 | 观测/known_at | 来源与局限 |
|---|---|---|---|
| F-001 | 五所806合约、77个实际产品；63代码清单全部覆盖（LPG按交易所代码PG映射），另有14个动态品种；source_date_match=100%，vendor full_market_ready=true，critical=0 | 2026-10-23 EOD；生成19:02 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/latest.json)；official_complete=false源于可选官方模块未全，而非vendor期货市场缺所 |
| F-002 | 上一合法夜盘归属交易日2026-10-23，起始2026-10-22；408/806合约有夜盘记录，214个query_error/unresolved | 2026-10-22 20:00至2026-10-23 03:45 BJT；生成08:49 | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/night_session/last_run_status.json)；vendor latest-trade snapshot；非交易所核验最终收盘，OHLC/量仓非纯夜盘确认口径 |
| F-003 | SC2612 close/settle=724.9/717元/桶；结算1D +2.14%，ΔOI +611；SC2611-SC2612 exact-close=+0.11% | 2026-10-23 EOD | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/latest.json)；今晚21:00尚未发生；exact-close价差不等于可成交套利净收益 |
| F-004 | FU2701 close/settle=5139/5028元/吨；结算1D +4.49%，ΔOI +20124；FU2701-FU2702 exact-close=+4.03% | 2026-10-23 EOD | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/latest.json)；高波动与高volume-z同时提高回撤和滑点风险 |
| F-005 | AG2612 close/settle=13108/13255元/千克；结算1D -4.16%，5D -4.56%；AG2612-AG2702 exact-close=-0.25% | 2026-10-23 EOD | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/latest.json)；原晨报禁止131?低位追空条件已越过；无分钟顺序不能假定旧计划成交 |
| F-006 | Options计划64品种，成功45（70.31%）；1031/1050采样记录；ATM ready 44、skew ready 26、surface/positioning/execution ready均0 | 2026-10-23 EOD；生成19:03 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/options/quality_latest.json)；core_v1 sampled_strikes，quote coverage不代表全链；零bid/ask，不可宣称可成交 |
| F-007 | Physical目标20、原生频率内fresh 18、不可用2；可读spot-basis均为C级且eligible_for_physical_score=false | 生成2026-10-23 19:13 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/physical/latest.json)；地区/等级/含税/交割地对齐不足，不能作为方向层或无风险套利证据 |
| F-008 | External目标22、fresh 17、不可用5；Brent 114.79美元/桶、COMEX银54.09美元/盎司等为repo日频latest | 2026-10-23；生成19:13 BJT | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/external/latest.json)；context_only且缺统一可比时点，不构成跨境套利报价 |
| F-009 | 官方价格交叉核对：SHFE238、INE63、CZCE243、GFEX48 matched且settle/close/pre-settle差异0；DCE HTTP 412 | 2026-10-23 EOD | [直达](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/crosschecks/futures_latest.json)；partial，不含成交量/OI官方核对；DCE候选受限 |
| F-010 | Reuters约09:36 GMT现货银53.8882美元/盎司、现货金4026.15；Reuters前一日结算Brent 113.17美元/桶且技术上超买 | 2026-10-23 17:36 BJT附近；油价为2026-10-22结算 | [直达](https://www.reuters.com/world/india/gold-heads-steep-weekly-loss-oil-prices-fuel-fed-rate-concerns-2026-10-23/)；不同品种/窗口，仅作方向映射；不是中国合约可成交报价 |
| F-011 | Stock引擎trade_date=2026-10-21、5576只报价；复权/行业成分覆盖0、5568只tradability unknown；中国石油/中国石化仅见三季报业绩说明会通知，未见截点前经营数字更新 | 仓库research_asof 2026-10-22；公告检索截至2026-10-23 19:30 BJT | [直达](https://github.com/farfromexact/China-Stock-Engine/blob/795e149866d7f1eefd1efdaf8fe510cd8f1c750e/data/latest/manifest.json)；Stock非执行就绪；中国石化截点后股东会决议已排除 |

| 模块 | 实际范围与状态 | 对结论的影响 |
|---|---|---|
| Futures/Market | 806合约、77品种，63核心代码全覆盖（LPG→PG）；SHFE238/INE63/DCE214/CZCE243/GFEX48。source-date 100%，invalid/duplicate/unknown均0；5个占位；full_market_ready=true | 全市场EOD可筛选；vendor完整不等于五所官方全面认证 |
| Metadata | effective contract match 73.45%；乘数/tick有效覆盖36.10%；保证金/限幅30.15%；48条carry-forward | Top3静态规格已查，动态参数仍不得猜 |
| Night | 合法旧会话408/806；outside 165、制度无成交19、query_error/unresolved 214；validated/published但coverage_complete=false | 只作今日EOD前证据；不能称今晚或交易所收盘 |
| Physical | 20目标、18 fresh、2 unavailable；0个eligible basis | 不给任何候选实体支持层 |
| External | 22目标、17 fresh、5 unavailable；均context_only | 可做方向映射，不能做跨境套利 |
| Options | 64目标、45成功；1031/1050样本；ATM44、skew26；surface/positioning/execution=0 | 可研究局部IV/skew；不可报权利金、净成本或dealer gamma |
| Crosscheck | SHFE/INE/CZCE/GFEX价格字段零差异；DCE HTTP 412；未核成交量/OI | DCE候选受局部限制，其他vendor数据不因此作废 |
| Stock | tape 2026-10-21；5576报价，复权/行业0，tradability unknown 5568；exposure config缺失 | 股票仅作利润桥背景，不是即时表达 |

后台扫描分板块完成：黑色9、金属13、能源化工22、新能源3、农产品15、航运1；交易所实际目录还覆盖BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等14个动态品种。未入榜最大异常：油链普涨、AG/AU去杠杆、Y价仓增强、SA/SH分化、EC五日急跌、LC close/settle分歧；其余品种未形成三层同向且赔率可验证的异常。

## 3. 12项市场仪表盘

| 品种/准确合约 | EOD close / settle | 1D / 5D / RV20 | 量仓与曲线 | 上一合法night snapshot | 海外映射 | Options | 信号 |
|---|---|---|---|---|---|---|---|
| SC SC2612 | 724.9 / 717 元/桶 | +2.14% / -0.83%; RV 49.45% | ΔOI +611; SC2611-SC2612 close +0.11% | 713.2；-0.03% vs前close / +1.60% vs前settle；02:30 | Brent repo 114.79；前日结算113.17 | ATM IV 64.89%，IV-RV +15.44pct；无skew/执行 | 油价风险溢价仍在，但只买回踩确认 |
| FU FU2701 | 5139 / 5028 元/吨 | +4.49% / +5.41%; RV 48.81% | ΔOI +20124; FU2701-FU2702 close +4.03% | 4922；+0.22% / +2.29%；23:00 | 原油强、海运保险高 | ATM IV 64.36%，IV-RV +15.55pct；不可执行 | 强于SC，拒绝追涨 |
| LU LU2612 | 6270 / 6205 元/吨 | +4.62% / +5.28%; RV 46.70% | ΔOI +6668; LU2612-LU2701 close +3.59% | 6130；+1.02% / +3.36%；23:00 | 受油价与中间馏分共同驱动 | 本期无合格局部执行指标 | 油链最强之一，仅作确认 |
| AG AG2612 | 13108 / 13255 元/千克 | -4.16% / -4.56%; RV 33.61% | ΔOI +44; AG2612-AG2702 close -0.25% | 13297；-2.29% / -3.86%；02:30 | 现货银53.8882美元/盎司，周线承压 | ATM IV 40.65%，IV-RV +7.03pct；无skew/执行 | 趋势弱，但当前位置禁追空 |
| AU AU2612 | 864.36 / 869.2 元/克 | -1.94% / -3.29%; RV 15.00% | ΔOI -9623; 近远月无本卡正式信号 | 869.74；-1.33% vs前close | 现货金4026.15美元/盎司，周跌约3.5% | 非榜单series | 去杠杆延续，赔率不足 |
| SA SA701 | 963 / 948 元/吨 | +1.28% / +0.85%; RV 17.21% | ΔOI -30787; SA701-SA703 close -3.22% | 945；+1.07% vs前close | 内需主导 | ATM IV24.24%，RR25 +0.35pct；不可执行 | 反向证据击穿旧空头，取消 |
| SH SH701 | 1579 / 1599 元/吨 | -2.02% / -7.84%; RV 14.11% | ΔOI -6741; 仓库曲线pair与主力月份不一致，隔离 | 1608；-0.12% vs前close | 烧碱链内生 | 期权underlier SH612，不能移植到SH701 | 弱势但数据错月，不执行 |
| Y Y2701 | 9125 / 9080 元/吨 | +1.53% / +2.78%; RV 11.45% | ΔOI +49944; near-next settle -0.88% | DCE 214合约query_error范围内，未核重点快照 | CBOT豆油66.73美分/磅、BMD棕榈4817令吉/吨 | 本期无执行报价 | 价格/OI增强但DCE核验缺口 |
| CU CU2612 | 107900 / 107310 元/吨 | -0.71% / -1.34%; RV 12.01% | ΔOI +2167; settle curve +0.76% | 107150；-0.41% vs前close | LME铜repo 14262.5美元/吨 | 无执行报价 | 内外时点不同，暂观察 |
| RB RB2701 | 3047 / 3043 元/吨 | -0.69% / -0.94%; RV 7.00% | ΔOI +19031; 无高质量basis确认 | 3045；-0.46% vs前close | 国内需求主导 | 无执行报价 | 价弱OI增只作线索 |
| AP AP701 | 5725 / 5726 元/吨 | -0.07% / -6.07%; RV 25.42% | ΔOI -16109; 仓库曲线pair非当前主力，隔离 | 制度无夜盘 | 无可比海外即时映射 | ATM IV31.64%，RR25 -6.72pct；不可执行 | put偏贵局部线索，反转触发未到 |
| EC EC2611 | 2443 / 2432 点 | -0.80% / -11.69%; RV 42.53% | ΔOI -2434; 不适用现货basis套利 | 无夜盘 | Hormuz运费/保险仍高，但航线机制不同 | 无执行报价 | 事件映射弱且高波动，观察 |

注：night的“% vs settle”包含前日日盘close-settle差，不是纯隔夜收益；OHLC/volume/OI属于vendor未核会话范围，本报告不据此编盘中路径或新多新空。

## 4. 相比前序的真变化

1. **数据纠错**：晨报生成时本交易日夜盘尚不可得；随后08:49发布了归属10月23日的合法snapshot。仅用于解释今日EOD前信息，不倒填晨报，也不当作今晚行情。
2. **油链再定价**：SC2612结算+2.14%，FU2701 +4.49%，LU2612 +4.62%；FU/LU近月升水明显。价格、期限、海外三层同向，但实体basis层仍缺。
3. **白银弱势延续**：AG2612结算-4.16%，外盘现货银约53.89；晨报的反抽后做空入口已越过，当前改为“只等新反抽失败”，不追空。
4. **纯碱旧观点失效**：SA701收963、结算+1.28%，前夜snapshot亦偏强；旧空头候选取消，不后移止损或重置ID。
5. **油脂线索抬升**：Y2701结算+1.53%、ΔOI +49944，但DCE官方交叉核对HTTP 412且夜盘具体合约未可靠确认，仍是观察而非执行。
6. **Options无执行升级**：45/64与44个ATM-ready支持局部IV研究，但bid/ask=0、execution-ready=0；任何权利金、净成本和成交性仍未知。

旧观点台账不重置：SC保留idea_id但换到新交易窗口；FU由观察升为条件候选；AG旧入口过期、未认定成交；SA取消；AP仍为早期观察。实际持仓状态均为“未提供/未知”。

## 5. 产业链与传播路径

| 产业链 | 价格/曲线/海外证据 | 最强 / 最弱 | 最大反证或缺口 | 置信度 |
|---|---|---|---|---|
| 中东→原油→燃料油/低硫/沥青 | SC/FU/LU/BU全面上涨；FU/LU近月升水；Brent维持113美元上方背景 | FU、LU / SC相对涨幅较小 | 海湾出口已回升但运费/保险仍高；实体basis缺失 | 中高；执行须回踩确认 |
| 贵金属→AG/AU→矿企 | AG/AU EOD与外盘同弱，AG轻微contango | 无 / AG | 避险回流可造成急反弹；期权IV高于RV | 中；只做反抽失败 |
| 氯碱/玻璃→SA/SH | SA上涨、SH下跌，产业链分化 | SA / SH | SH曲线与期权underlier错月；实体basis C级 | 低；旧SA空头取消 |
| 油脂→Y/P/OI与外盘豆棕 | Y2701价格与OI同升，外盘豆油/棕榈保持高位 | Y / 未形成 | DCE官方核对失败、重点夜盘未确认 | 低至中；观察 |
| 黑色/有色/航运/新能源 | RB、CU偏弱；EC 5D -11.69%；LC close/settle分歧大 | 无共同方向 / EC、LC波动 | 跨品种驱动不同，不能合并成单一风险因子 | 低；不入榜 |

Stock利润桥：油价上升可能抬高上游实现价，但炼化原料成本、库存损益、长协、套保、汇率与传导滞后都可能抵消。限定检索中国石油和中国石化，截点前只找到三季报业绩说明会通知，未找到经营数字增量；截点后的中国石化股东会决议被排除。股票数据又滞后且tradability未知，因此直接商品的条件表达优于股权；Stock未增加第五层之外的证据。

## 6. 统一机会榜

| 排名 | idea_id | 候选 | 逻辑/赔率/催化/价曲波/拥挤=总分 | 五层证据 | 研究/证据/执行 |
|---|---|---|---|---|---|
| 1 | COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021 | SC2612回踩确认多 | 22/18/19/13/4=76 | 支持：1价格/量仓、2期限结构、4海外映射；反：5期权IV显著高于RV，长凸性carry不利；缺：3实体供需 | 高/3层支持/not execution-ready |
| 2 | COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022 | FU2701近月强势回踩多 | 21/17/18/15/3=74 | 支持：1价格/量仓、2期限结构、4海外映射；反：5期权IV-RV溢价，且高波动追价风险；缺：3实体供需 | 高/3层支持/not execution-ready |
| 3 | COM-M-AG2612-SILVER-REPAIR-LONG-20261021 | AG2612反抽失败后条件空 | 21/17/17/14/3=72 | 支持：1价格/量仓、2轻微contango、4海外映射；反：5期权IV高于RV；急跌后反弹风险；缺：3实体供需 | 重点/3层支持/not execution-ready |

分数只表示研究优先级，不是胜率。三项均有三层支持而可进入70+；均因无实时触发、无动态参数与Options执行报价而不是立即新仓。

## 7. 完整研究/交易卡

### 1. COM-E-SC2612-POST-EIA-RECLAIM-LONG-20261021｜SC2612 conditional_long

- 新增事实：EOD close/settle 724.9/717；exact SC2611-SC2612 close spread +0.11%；Brent风险溢价仍高
- 已定价与分歧：日盘+2.14%结算涨幅和海外油价高位已反映大量地缘溢价。我们的分歧仅是：若今晚回踩而近月结构重新扩大，说明风险溢价未完全被需求/出口恢复反证消化
- 主要PnL/催化：SC2612方向上涨；非跨境无风险套利；周末中东标题、10月28日EIA
- 最强竞争解释：海湾出口恢复、Brent超买，溢价可能快速回吐
- 下一项区分观测：Brent≥113且SC2611-SC2612同一时点≥0.8%，并出现先回踩后5分钟收复728
- 入场：21:00后不追首跳；回踩720—726后，5分钟收盘≥728且上述两条件同时成立；727.5—731分两批；≥732放弃
- 失效/止损：15分钟收盘<719，或Brent<110，或近月转contango；止损不保证成交/封顶
- 目标与时间：TP1 744；TP2 758；最迟10月30日退出
- 合约参数：乘数1000桶/手、tick 0.1元=100元/手；静态合约页最低保证金5%、静态涨跌限4%，动态参数未核，不能用于今晚下单
- 好/中/坏成交重算：728：风险9000元/手，TP1 1.78R、TP2 3.33R；729.5：风险10500元/手，TP1 1.38R、TP2 2.71R；731：风险12000元/手，TP1 1.08R、TP2 2.25R。费用/滑点未知，净R将低于表值。
- 风险预算：试仓风险≤NAV 0.50%；与FU/LU/BU合并主题≤1.50%；期货为线性风险，最大损失不受计划止损保证封顶。

### 2. COM-E-FU2701-OIL-SHOCK-CURVE-LONG-20261022｜FU2701 conditional_long

- 新增事实：close/settle 5139/5028；1D +4.49%、ΔOI +20124；FU2701-FU2702 exact-close +4.03%
- 已定价与分歧：近月供应/运输风险已由大涨与backwardation明显定价。我们的分歧仅是：只在回踩不破且价差仍≥3.5%时，近月紧张才可能继续贡献PnL
- 主要PnL/催化：FU2701线性上行；油价与运费保险周末风险
- 最强竞争解释：高裂解/高价格抑制需求，回落将比SC更急
- 下一项区分观测：前15分钟守住5080，回踩5085—5125后5分钟收盘≥5130，同时Brent≥113、价差≥3.5%
- 入场：满足顺序后5090—5140分批；>5160不追
- 失效/止损：5035计划止损或exact价差<2.5%；不保证封顶
- 目标与时间：TP1 5260；TP2 5420；最迟10月30日退出
- 合约参数：乘数10吨/手、tick 1元=10元/手；静态合约页最低保证金8%、静态涨跌限5%，动态参数未核
- 好/中/坏成交重算：5090：风险550元/手，TP1 3.09R、TP2 6R；5120：风险850元/手，TP1 1.65R、TP2 3.53R；5140：风险1050元/手，TP1 1.14R、TP2 2.67R。费用/滑点未知，净R将低于表值。
- 风险预算：试仓风险≤NAV 0.35%；并入油链主题≤1.50%；期货为线性风险，最大损失不受计划止损保证封顶。

### 3. COM-M-AG2612-SILVER-REPAIR-LONG-20261021｜AG2612 conditional_short

- 新增事实：close/settle 13108/13255；1D -4.16%；现货银约53.89；exact curve -0.25%
- 已定价与分歧：日盘急跌与外盘周线弱势已高度定价，低位追空负凸性。我们的分歧仅是：只有反抽无法站稳且外盘银仍≤54，才证明去杠杆尚未结束
- 主要PnL/催化：AG2612方向下跌；10月27—28日Fed、10月29日美国PCE
- 最强竞争解释：贵金属避险回流或美元/实际利率下行触发剧烈反弹
- 下一项区分观测：先反抽13240—13320，再5分钟收盘<13200；同时现货银≤54且AG2612-AG2702≤-0.20%
- 入场：上述顺序满足后13150—13280分批；<13050禁止追空
- 失效/止损：13430计划止损或外盘银>55.5；不保证封顶
- 目标与时间：TP1 12850；TP2 12500；最迟10月28日Fed前退出或减至零
- 合约参数：乘数15千克/手、tick 1元=15元/手；静态规则页曾列最低保证金4%、涨跌限3%，动态参数未核
- 好/中/坏成交重算：13280：风险2250元/手，TP1 2.87R、TP2 5.2R；13220：风险3150元/手，TP1 1.76R、TP2 3.43R；13150：风险4200元/手，TP1 1.07R、TP2 2.32R。费用/滑点未知，净R将低于表值。
- 风险预算：试仓风险≤NAV 0.40%；贵金属主题≤1.00%；期货为线性风险，最大损失不受计划止损保证封顶。

规模公式：手数=floor[单笔允许风险金额 ÷（|入场−计划止损|×乘数+费用/滑点情景）]。无NAV、费用和盘口，因此不给手数。1/2限幅压力只能使用静态规则页作情景，不能冒充今晚动态限幅；保证金不等于风险预算。

## 8. 商品期权专项

- SC2612 ATM IV 64.89% vs RV20 49.45%，差+15.44pct；FU2701 64.36% vs 48.81%，+15.55pct；AG2612 40.65% vs 33.61%，+7.03pct。这里的“IV高于RV”仅是carry风险提示，不等于经模型证明的昂贵。
- AP701 core ATM 31.64%、RR25=-6.72pct、BF25=1.57pct，表明局部put IV高于call；但反转价位未触发、无夜盘、无bid/ask，不能把偏斜直接转成可执行多头。
- SA701 RR25=+0.35pct近中性；价格反向上行使旧空头逻辑失效。
- 单品种只有一个可比series，禁止外推term；surface_ready=false、positioning_ready=false、dealer_gamma_direction_known=false、execution_ready=false。任何call spread/put spread都必须在21:00后重算moneyness并获得各腿实时bid/ask；本报告只给成本上限框架，不称已便宜或有限损结构已可成交。

## 9. 21:00夜盘风险地图

- **Previous China EOD**：油链已大涨且FU/LU backwardation明显；AG急跌；Y价仓增强但DCE核验受限。
- **已完成历史night**：归属10月23日，能源偏强、贵金属偏弱；语义为vendor latest-trade snapshot，绝非今晚预测。
- **19:30可核海外**：Brent仍在113美元上方背景、现货银约53.89；油价技术超买与海湾出口恢复是最强反证。

21:00—21:15只看首跳是否留存，油品高开超过计划放弃价不追；21:15—21:30看SC/FU是否完成回踩并守住曲线；21:30—21:45才检查AG是否出现“先反抽、再跌破”的顺序。若内盘油高开而Brent跌破110，视为内外冲突；若AG直接跌破13050，放弃空头而不是追价。今晚有夜盘的合约风险跨周末，下一中国日盘为10月26日09:00。

## 10. 未来24小时/7日事件与风险处理

| 北京时间窗口 | 事件 | Delta/Vega与处理 |
|---|---|---|
| 10月23日21:00—21:45 | 周五夜盘，归属10月26交易日 | 不追首跳；15/30/45分钟分层确认 |
| 10月24—25日 | 中东、海湾出口/运输/保险周末标题 | 中国休市；油链合并gap和1—2限幅压力 |
| 10月26日09:00 | 下一中国日盘 | 无夜盘品种、DCE缺口与Stock窗口重估 |
| 10月27—28日 | Fed议息 | AG/AU短周期线性方案在会前退出；未报价期权不留未知Vega |
| 10月28日22:30附近 | EIA周度报告 | 以EIA官方发布为准；SC/FU不跨数据裸追 |
| 10月29日 | 美国PCE、ECB | 重评美元/实际利率与贵金属IV-RV |

行动前缺口：DCE官方与具体夜盘未补齐、Physical无可评分basis、Options无bid/ask/全链/持仓、Top3动态保证金与限幅未确认、Stock当前价格/复权/行业/可交易性不足、用户NAV和持仓账本缺失。

## 11. 发布前实证检查

实际重算三项分数与好/中/坏R；检查了SC/FU/AG乘数与tick、合约月份、close/settle基准、周五夜盘归属、旧触发与新窗口不混用、三层证据上限、Stock公告截点和MD/JSON共用候选对象。未通过或未完成的只有：DCE官方核对、动态交易参数、期权实时腿报价、实体basis和成交/持仓回执；因此三项均保持not execution-ready。CI状态为pending_or_unverified，不轮询。

## 12. 来源

1. [China Commodities Engine futures EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/latest.json)（2026-10-23）：五所806合约与77品种；准确合约close/settle/量仓；近远月exact价格。
2. [China Commodities Engine market state](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/market_state_latest.json)（2026-10-23）：1D/5D/RV20；OI变化与z值；仓库曲线指标。
3. [Night session status and snapshot](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/night_session/last_run_status.json)（2026-10-23）：合法会话日期与覆盖；vendor snapshot语义；query_error数量。
4. [Physical module](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/physical/latest.json)（2026-10-23）：20项目标、18项fresh；basis均不具物理评分资格。
5. [External module](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/external/latest.json)（2026-10-23）：22项目标、17项fresh；repo海外日频价格仅context。
6. [Options quality and surface](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/options/quality_latest.json)（2026-10-23）：45/64产品；ATM44、skew26；surface/positioning/execution均未就绪。
7. [Futures official crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/b0d41f1c9e8923bb016835492a3e2215e1d48780/data/crosschecks/futures_latest.json)（2026-10-23）：四所价格字段零差异；DCE HTTP 412；不含volume/OI核验。
8. [Reuters: gold and silver weekly loss](https://www.reuters.com/world/india/gold-heads-steep-weekly-loss-oil-prices-fuel-fed-rate-concerns-2026-10-23/)（2026-10-23）：现货金银欧洲时段报价；Fed与PCE日期；贵金属周线压力。
9. [Reuters: oil settles higher](https://www.reuters.com/business/energy/oil-rises-us-orders-diplomats-leave-saudi-arabia-amid-escalating-tensions-2026-10-22/)（2026-10-22）：Brent 113.17、WTI 99.47结算；Brent技术超买。
10. [Reuters: Gulf exports recover but shipping remains abnormal](https://www.reuters.com/commentary/reuters-open-interest/dont-mistake-mideast-oil-rebound-normality-2026-10-22/)（2026-10-22）：海湾出口恢复；Hormuz运输与保险成本异常；油价溢价竞争解释。
11. [SHFE trading hours](https://www.shfe.com.cn/services/calenderandholidays/tradinghours/)（2026-10-23）：夜盘从前一工作日21:00开始；周五夜盘归属下一交易日。
12. [INE crude contract specifications](https://tsite.shfe.com.cn/eng/market/futures/energy/sc/contract/)（规则页）：SC乘数、tick、静态保证金与涨跌限；最后交易日规则。
13. [SHFE fuel oil contract specifications](https://www.shfe.com.cn/products/futures/energyandchemical/fu_f/standard_fu/202312/t20231205_327331.html)（规则页）：FU乘数、tick、静态保证金与涨跌限；最后交易日规则。
14. [China Stock Engine latest manifest](https://github.com/farfromexact/China-Stock-Engine/blob/795e149866d7f1eefd1efdaf8fe510cd8f1c750e/data/latest/manifest.json)（2026-10-21）：股票报价日与能力缺口；tradability不就绪。
15. [中国石油2026年第三季度业绩说明会公告](https://www.cninfo.com.cn/new/disclosure/detail?annoId=1225615898)（2026-10-23）：仅为业绩说明会通知，不提供本报告所需经营增量。
16. [中国石化2026年第三季度业绩说明会通知](https://www.cninfo.com.cn/new/disclosure/detail?annoId=1225615855)（2026-10-23）：仅为业绩说明会通知；截点后决议不纳入。
17. [Prior commodities morning report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/507492be3a0770ff0a05741e0391cbf4a89a2828/reports/2026/10/2026-10-23_commodities_morning.json)（2026-10-23）：稳定idea_id；原始触发与禁止追价；晨报状态。
18. [Prior commodities evening report](https://github.com/farfromexact/Global-Cross-Asset-Radar/blob/507492be3a0770ff0a05741e0391cbf4a89a2828/reports/2026/10/2026-10-22_commodities_evening.json)（2026-10-22）：同版评分与旧计划；连续状态台账。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：SC2612回踩收复728、FU2701回踩收复5130、AG2612先反抽再跌破13200；必须满足各自AND与顺序条件。
C. 今天继续观察：Y2701价仓、AP701局部put偏斜、EC/LC高波动、SA/SH分化及油气公司后续经营披露。
D. 今天必须回避或有条件退出：不追21:00油品首跳、不在AG2612<13050追空、不把旧night当今晚行情；若此前按旧SA空头条件建仓，应按原失效/止损规则处理。