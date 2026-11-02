# 商品期货期权晨间雷达｜2026-11-03

> 生成：2026-11-03T07:13:31+08:00｜信息截点：2026-11-03T07:10:00+08:00｜中国最新完整EOD：2026-11-02｜下一真实窗口：2026-11-03 09:00；最早执行复核09:15｜仅研究，不下单，不假定成交或持仓

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；优先等SC反弹失败空、CU内外盘共振多，EC仅在运价转弱后跟踪。**

今晚海外与中国夜盘给出的风险不是“追空油化”，而是等价格回抽后验证：已研究但优势不足的是MA/BU/EB的单边空与AG反弹多；研究机会存在但等待条件的是SC、CU、EC；数据不足不能判断的是AG最终夜盘、SC/CU/EC商品期权执行报价与DCE官方交叉核对。最有价值的三项待验证观察：09:15 SC反弹—失败—曲线顺序、09:15 CU 0.60%曲线与LME共振、EC期货弱势能否得到新的实体运价转弱确认。

## 2. 数据质量、覆盖与事实台账

| 模块 | 实际状态 | 范围/日期 | 对结论的局部影响 |
|---|---|---|---|
| report_input | **empty**，0字节，不等于无市场数据 | [data/report_input_latest.json](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json) | 转读各模块last-good与状态；不能声称合并输入ready |
| Futures | 11-03刷新HTTP401失败；11-02 last-good verified/full_market_ready | 5所、806合约、77品种；source-date-match 100%，5个占位、critical 0 | 可做EOD研究；不是07:10实时成交报价 |
| Market State | analytically_ready | 77品种、每品种20个同合约观测 | 可用1/5D、RV20、量仓曲线；不把OI解释为新多新空 |
| Physical | 18/20有效、2不可用；0个A/B级basis | 日频11-02；LC/SI仓单陈旧到09-01 | 只作背景，不能提供第三层方向确认 |
| External | repo 17/22为context；另独立核海外收盘 | 11-02至11-03 07:10 | 能做方向映射，不能做精确跨境套利 |
| Night | 当前批次0/806、806 query_error、validation/published/complete均false | trading_date 11-03，session 11-02→11-03，标签合法；calendar_mismatch=false | Top候选改用准确合约第三方延时快照；official_night_close_verified=false |
| Options | 19/64产品、430合约；ATM19、skew12；surface/positioning/execution均0 | 11-02 EOD，core_v1/sampled_strikes，bid/ask覆盖0 | 局部IV/skew可研究；不可写净权利金、成交性、PCR或dealer Gamma |
| Metadata | partial | 806合约；match 67.49%、参数覆盖30.15%、night字段覆盖0 | Top3用交易所合约页/通知补参数；未知不猜 |
| Crosscheck | partial | SHFE238、INE63、CZCE243、GFEX48已比较且different=0；DCE HTTP412 | 没发现已比字段价格差异；量仓未交叉核，DCE局部未核 |
| Stock | available但execution_not_ready | 5,571报价；仅2个完整公司证据包；trade date 10-30 | 只做紫金/中海油利润桥；不作股票即时交易结论 |

后台覆盖：prompt 63个代码全部取得；LPG以引擎代码PG映射；另纳入BZ/JR/LG/OP/PD/PL/PM/PT/RI/RR/RS/WH/WR/ZC等动态/低活跃品种，总计77。黑色、金属、能化、新能源、农产品、航运均实际扫描；未入榜原因见本节板块结论，而非把品种移交其他版本。

| fact_id | 准确标的/口径 | 观测值、币种/单位 | 观测/known_at | 读取 | 直达来源 | 支持与局限 |
|---|---|---|---|---|---|---|
| F01 | 五所全市场 | 806合约/77品种；CNY或点；EOD close/settle | 2026-11-02 / 18:57生成 | 07:10读取 | https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json | 全范围初筛；5个占位、无关键错误；11-03刷新失败不抹去last-good |
| F02 | Night批次 | trading_date=11-03；0/806；806 query_error | 11-03 06:04 | 07:10 | https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json | 当前夜盘仓库不可用；日历标签合法、calendar_mismatch=false |
| F03 | SC2612/2701 | 681.0/676.7元/桶；latest trade snapshot | 11-03 02:30 | 07:10 | https://www.9qihuo.com/hangqing?productcode=sc | 油价冲击与曲线压缩；非交易所最终收盘 |
| F04 | CU2612/2701 | 108370/107740元/吨；latest trade snapshot | 11-03 01:00 | 07:10 | https://www.9qihuo.com/hangqing?productcode=cu | 内外修复；曲线0.585%仍低于0.60%门槛 |
| F05 | MA701/612 | 3422/3550元/吨；latest trade snapshot | 11-02 23:00 | 07:10 | https://www.9qihuo.com/hangqing?productcode=MA | 旧多最高3552<3580未触发；曲线反而扩大 |
| F06 | WTI/Brent | 96.46/104.77美元/桶；结算 | 11-02美国收盘 | 07:10 | https://www.wsj.com/business/energy-oil/oil-drops-amid-diplomatic-efforts-to-revive-mideast-peace-talks-964fc4d6 | 原油溢价回吐；谈判失败仍可反向gap |
| F07 | LME铜/COMEX银 | 14251美元/吨；51.04美元/盎司 | 11-02海外收盘 | 07:10 | https://www.wsj.com/finance/commodities-futures/gold-rises-but-expectations-of-tighter-u-s-monetary-policy-weigh-512a4860 | 支持CU/AG海外层；时区不同，不作无成本套利 |
| F08 | EC2611/2612与SCFIS | 2228.5/2585.5结算点；SCFIS2304.32点 | 11-02 | 07:10 | https://www.ine.cn/reports/tradedata/dailyandweeklydata/ | 期货弱、实体指数周涨4.8%反证 |
| F09 | 商品期权 | 430合约；19/64产品；bid/ask覆盖0 | 11-02 EOD / 11-03 06:24生成 | 07:10 | https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json | 局部ATM/skew研究；不可执行、不可推全链 |
| F10 | Physical | 18/20有效；所有basis为C级 | 11-02 | 07:10 | https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json | 仅背景；0个A/B级可计方向层 |
| F11 | 官方交叉核对 | SHFE238/INE63/CZCE243/GFEX48，差异0；DCE HTTP412 | 11-02 | 07:10 | https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json | 已比价字段无差异；不含量仓，不代表全所认证 |
| F12 | Stock利润桥 | 紫金H1；中海油前三季；CNY | 08-22/10-30发布 | 07:10 | https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF | 经营验证；非11-03新催化，股票执行参数未核 |

板块未入榜最重要异常：黑色RB价跌仓增但缺实体/海外/期权共振；新能源LC 5D -4.66%但仓单陈旧；农产品JD 5D +6.67%仅价格/曲线强；油脂OI曲线z＋2.99但期权无bid/ask；能化BU/EB价格暴跌而backwardation仍强，相关性断裂风险高。

## 3. 12项市场仪表盘

EOD列为close/settle；1D/5D按同合约settlement收益；Night“%”为快照相对EOD close/settle，不是官方夜盘最终收益。

| 板块/准确合约 | EOD close/settle | 1D/5D | volume/OI/ΔOI | RV20% | curve | basis/Physical | Night snapshot | 07:00海外 | Options | 信号 |
|---|---:|---:|---:|---:|---|---|---|---|---|---|
| 能源/SC2612 | 729.5 / 745.2 | ＋2.42% / ＋0.74% | 156,040 / 26,207 / -1,157 | 40.20 | 2612/2701结算＋1.333%；夜盘＋0.635% | 无合格A/B；原油实体序列未覆盖 | 681.0；-6.65%/-8.62%；02:30；OI 25,714（第三方快照） | WTI 96.46、Brent 104.77，约-7.4%/-7.6% | SC未入19品种样本 | 等反弹失败，不追空 |
| 有色/CU2612 | 107,810 / 107,580 | -0.56% / -0.55% | 104,635 / 183,642 / -3,183 | 11.03 | 2612/2701结算＋0.533%；夜盘＋0.585% | 现货109,875；基差C，不计层 | 108,370；＋0.52%/＋0.73%；01:00；OI 180,788 | LME 3M铜14,251（＋0.9%） | CU未入样本 | 差0.015个百分点到0.60%门槛 |
| 航运/EC2612 | 2,540 / 2,585.5 | -2.36% / -11.62% | 12,467 / 16,662 / ＋1,313 | 45.80 | 2611/2612收盘-12.44%、结算-13.81% | SCFIS欧线2,304.32，周＋4.8%（反证） | 制度无夜盘；不扣分 | 红海/伊朗谈判仍是双向跳空源 | EC未入样本 | 趋势空，但实体反证未解除 |
| 化工/MA701 | 3,557 / 3,553 | ＋2.60% / ＋6.19% | 3,228,791 / 908,240 / ＋27,035 | 38.57 | 612/701结算＋2.786%；夜盘＋3.741% | 现货3,991.67；基差C | 3,422；-3.80%/-3.69%；23:00；OI 906,781 | 油价暴跌利空成本，但近月更强 | MA612 ATM IV50.61、RR25＋1.21；与701不匹配且无bid/ask | 旧多无触发；空也等曲线收窄 |
| 贵金属/AG2612 | 11,885 / 11,754 | -5.01% / -9.93% | 620,971 / 222,692 / -15,625 | 33.63 | 近次月＋0.213%，z＋2.46 | 无方向实体层 | 23:20快照12,144；＋2.18%/＋3.32%；非最终收盘 | COMEX银约51.04（＋3.6%） | AG未入样本 | 旧空失效；反弹多仅观察 |
| 能化/BU2701 | 5,199 / 5,276 | ＋1.38% / ＋11.36% | 481,171 / 225,627 / -10,452 | 31.27 | 主曲线＋3.531%；夜盘2612/2701＋2.185% | 无合格A/B | 4,989；-4.04%/-5.44%；23:00 | 跟随原油下修 | BU未入样本 | 价格空、曲线紧；不做单边追空 |
| 化工/EB2612 | 10,443 / 10,481 | ＋2.22% / -0.64% | 1,379,806 / 320,320 / -15,433 | 32.82 | 主曲线＋4.761%；夜盘2612/2701＋3.464% | 未覆盖 | 10,005；-4.19%/-4.54%；23:00 | 油价与芳烃链下行 | EB未入样本 | 价格与曲线冲突 |
| 农产品/JD2612 | 3,564 / 3,535 | ＋3.03% / ＋6.67% | 654,076 / 211,562 / ＋1,158 | 27.57 | 近次月＋7.638% | 未覆盖 | 无合法夜盘 | 无独立海外确认 | JD未入样本 | 单层强，不追 |
| 黑色/RB2701 | 3,007 / 3,019 | -0.66% / -0.72% | 715,629 / 1,866,893 / ＋86,044 | 7.77 | 近次月-1.186%，z-1.71 | 现货3,112.84；基差C | 夜盘未作重点fallback | 无新增独立映射 | RB未入样本 | 价弱仓增仅作线索 |
| 新能源/LC2701 | 90,700 / 90,500 | ＋0.49% / -4.66% | 303,268 / 439,013 / -4,060 | 40.78 | 近次月＋0.710% | 现货94,000；基差C；仓单陈旧至09-01 | 无合法夜盘 | 无可比海外精确合约 | LC未入样本 | 实体质量不足 |
| 软商品/AP701 | 5,757 / 5,771 | ＋1.64% / ＋3.22% | 388,654 / 165,331 / -6,361 | 30.66 | 近次月＋6.561%，z-2.26 | 未覆盖 | 无夜盘 | 不适用 | AP701 ATM IV34.43、RR25-0.17；无bid/ask | 波动溢价仅观察 |
| 油脂/OI701 | 10,167 / 10,236 | -0.57% / -0.96% | 323,385 / 358,267 / -29,845 | 11.66 | 近次月＋4.728%，z＋2.99 | 未覆盖 | 未作重点fallback | CBOT油籽无强同向新增 | OI701 ATM IV15.54、RR25＋1.50；无bid/ask | 期权贵不等于可卖 |

## 4. 相比前序的5项真变化与旧观点处置

1. SC旧周末风险突破多因Brent跌至104.77、SC2612夜盘681而失效；新建父子关联的“反弹失败空”研究，但首个合法确认在09:15。
2. CU2612从EOD弱势转为夜盘108370，2612/2701由0.533%升至0.585%；仍低于旧计划0.60% AND门槛，原idea_id保留、未触发。
3. MA701旧多要求3580上方持续且回踩；夜盘最高3552、最新3422，触发从未成立。612/701反而由2.786%扩大至3.741%，不允许顺势追空。
4. EC2612日盘跌2.36%、5日跌11.62%，2611/2612 contango结算-13.81%；但同日SCFIS欧线现货指数周涨4.8%，空头证据由“偏一致”降为“价格/实体冲突”。
5. AG旧空的海外银价失效阈值49.5已被约51.04穿越；夜盘快照反弹，但非官方最终收盘且无期权样本，因此只撤旧空，不自动反手。

旧观点台账只继承稳定ID，不回填成交：SC旧多与MA旧多判定“逻辑失效/从未触发”，AG旧空判定“失效”，CU与EC保留原ID但信号仍未满足；实际持仓状态均为“未提供/未知”。变更属于新价格与海外证据，不是事后移动止损。

## 5. 产业链与Stock利润验证

| 传播链 | 方向/最强证据 | 最大反证/缺口 | Stock利润桥与表达比较 | 置信度 |
|---|---|---|---|---|
| 原油→FU/BU→芳烃/烯烃 | SC夜盘-6.65% vs close；Brent -7.6% | FU/BU/EB近月仍强backwardation | 中国海油前三季产量593.7百万桶油当量、归母利润1191.2亿元、capex约899亿元；产量/成本缓冲但不能消除油价敏感。直接SC/Brent因子更纯；证券状态未核 | 中高 |
| LME铜→沪铜→紫金利润 | LME3m 14251；CU夜盘+0.52% | EOD弱、曲线0.585%未达0.60%、基差C | 紫金H1收入1941.78亿元、归母利润391.70亿元、经营现金流554.72亿元；售价/销量、矿山成本、冶炼、套保、汇率、少数股东与capex共同传导。期货优于股权表达纯度 | 中 |
| 伊朗谈判→油价→MA/BU/EB | 三品种夜盘约-3.8%至-4.2% vs close | MA/BU/EB曲线仍紧 | 限定检索未发现11-02后改变链条的新经营披露；不扩展为独立股票筛选 | 中 |
| SCFIS现货→EC期货 | EC 5D -11.62%、contango -13.81% | SCFIS欧线周＋4.8%，方向相反 | 航运股利润受运量、租船成本、长协和传导滞后；输入未核，不作替代 | 中 |

Stock补证范围仅紫金矿业、中国海油；[紫金正式半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)与[中国海油经营披露](https://www.cnoocltd.com/english/presscenter/pressreleases/2026/202610/t20261030_123124.html)均为历史已发布资料，不是今日新增催化。CNINFO限定检索未发现11月2日后新的经营证据；股票当前报价、复权、停牌/涨跌停和成交成本未核，故不进入即时机会榜。

## 6. 统一机会榜

| 排名 | idea_id | 机会 | 方向/期限 | 逻辑/赔率/催化/市场/技术 | 有效支持层 | 反证与缺失 | 研究/证据/执行 |
|---:|---|---|---|---:|---|---|---|
| 1 | COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103 | SC2612反弹失败空 | 空/1—5D | 21/19/17/12/7 = **76** | 1价格、2曲线、4海外 | 3实体缺失/地缘再升级；缺5期权 | 高优先/3层合格/未就绪 |
| 2 | COM-M-CU2612-LME-TIGHTNESS-DIVERGENCE-LONG-20261102 | CU2612内外盘收敛多 | 多/1—5D | 21/18/15/12/8 = **74** | 1价格、2曲线、4海外 | EOD弱、美元/实际利率；缺3合格实体、5期权 | 重点/3层临界/未触发 |
| 3 | COM-T-EC2612-TREND-CONTANGO-SHORT-20261028 | EC2612趋势/contango空 | 空/1—10D | 19/16/13/11/8 = **67** | 1价格、2曲线 | 3 SCFIS周＋4.8%；缺4独立海外映射、5期权 | 观察偏空/2层封顶/未就绪 |
| 4 | COM-C-MA701-OIL-SHOCK-REVERSAL-SHORT-20261103 | MA701油价冲击反转空 | 空/1—5D | 18/15/14/10/8 = **65** | 1夜盘价格、4原油 | 2 612/701扩大至3.741%；缺3合格实体、5精确701期权 | 观察/2层封顶/禁止追空 |
| 5 | COM-M-AG2612-REFLEXIVE-BOUNCE-LONG-20261103 | AG2612反身性修复多 | 多/1—3D | 17/14/13/11/8 = **63** | 1反弹快照、4 COMEX银 | EOD 5D -9.93%、夜盘最终价缺失；缺2可比夜盘曲线、3实体、5期权 | 早期线索/2层封顶/数据不足 |

评分仅是研究优先级，不是胜率。SC/CU有3层才进入70+；EC/MA/AG仅2层，严格封顶69。公司股价与同一商品冲击不重复计层。

## 7. 三张研究/交易卡

### 卡1｜SC2612反弹失败空（COM-E-SC2612-USIRAN-DEESCALATION-REBOUND-FAILURE-SHORT-20261103）

- **事实/定价/推断/主观**：事实为EOD 729.5/745.2、02:30快照681、Brent 104.77、曲线1.333%→0.635%；市场已计入大部分谈判溢价回吐。推断是首个日盘可能出现风险对冲回补；主观分歧是“反弹失败”比追空更有赔率。
- **触发顺序**：09:00后先反弹691—699 → 15分钟收回691下方 → 再反抽691—699失败；并且 **SC2612/2701≤0.75% AND Brent≤106.5**。任何一步缺失都不执行。若直接低开680以下且无反弹，放弃追空。
- **分批与退出**：允许价好/中/坏=699/695/691，各仅作为触发后可达价；计划止损711，逻辑失效为曲线>1.00%或Brent>108。TP1 670、TP2 645；50%/30%/20%分批退出，最迟11-06 22:45。
- **确定性计算**：按1000桶/手、情景成本500元/手：好价风险12,500元，TP1/TP2净R=2.28/4.28；中价16,500元，1.48/3.00；坏价20,500元，1.00/2.22，坏价TP1赔率不足，宜放弃。
- **参数/交割**：tick 0.1元/桶=100元/手；夜盘21:00—02:30；最后交易11-30、交割至12-07。11-03收盘前限幅16%、一般保证金18%；收盘后调整为18%/20%。一手名义约681,000元，保证金不是风险预算。
- **压力**：中价空单若触及当日上限864.4，约亏169,900元/手；再按下一阶段18%上限近似约325,492元/手。止损不保证成交或最大亏损。
- **预算**：试仓0.50% NAV，手数=floor(0.005×NAV/16,500)；确认后不超过1.0%，油价共同因子总预算≤2.5%。

### 卡2｜CU2612内外盘收敛多（COM-M-CU2612-LME-TIGHTNESS-DIVERGENCE-LONG-20261102）

- **事实/错价**：EOD -0.56%，01:00快照108370，LME3m 14251；2612/2701由0.533%升至0.585%。市场已部分修复，但仍差0.015个百分点到旧计划门槛，不能提前认定共振。
- **触发顺序**：09:15后 **CU2612≥108400持续15分钟 AND 2612/2701≥0.60% AND LME3m≥14200**；随后回踩108050—108250且107900不破。开盘>109000无回踩则放弃。
- **分批与退出**：好/中/坏=108050/108150/108250；计划止损107600；独立逻辑失效为曲线<0.40%或LME<14050。TP1 110000、TP2 112000；40%/35%/25%退出；最迟11-06 14:45。
- **计算**：5吨/手、tick10元/吨=50元/手，成本假设100元/手。好/中/坏风险2,350/2,850/3,350元；TP1净R=4.11/3.21/2.58，TP2=8.36/6.72/5.57。
- **参数/压力**：夜盘21:00—01:00；最后交易12-15、交割至12-17；限幅8%、一般保证金10%。按8%下限情景，中价多单约亏45,982元/手。计划止损不封顶。
- **表达比较**：紫金股权含经营与资本结构噪音；CU期货因子更纯。期权本批无CU，不能伪造有限损结构。
- **预算**：试仓0.50% NAV，手数=floor(0.005×NAV/2,850)；与紫金股权合并因子，主题≤2.5%。

### 卡3｜EC2612趋势/contango空（COM-T-EC2612-TREND-CONTANGO-SHORT-20261028）

- **事实与竞争解释**：EOD 2540/2585.5、5D -11.62%、ΔOI +1313；2611/2612结算contango -13.81%。最强竞争解释是SCFIS现货周＋4.8%，期货可能已过度贴水，故价格破位不能单独触发。
- **触发顺序**：09:15后 **EC≤2520持续15分钟 AND contango≤-12% AND 新SCFIS/即期运价/船司报价同步转弱**，再等2520—2550反弹失败。没有实体转弱证据就不交易。
- **分批与退出**：好/中/坏=2550/2535/2520；止损2615，TP1 2400、TP2 2250；最迟11-09 14:45。50%/30%/20%退出。
- **计算**：50元/点，tick0.5点=25元/手，成本假设100元/手。风险3,350/4,100/4,850元；TP1净R=2.21/1.62/1.22，TP2=4.45/3.45/2.76。
- **参数/压力**：无夜盘、现金交割、最后交易12-28；现行EC2612限幅20%、交易所保证金22%。按20%上限情景，中价空单约亏28,480元/手，远大于计划止损风险。
- **预算**：仅0.25%—0.50% NAV试仓，航运主题≤2.5%；无账户与成交回执，不推定任何持仓。

## 8. 商品期权专项

- 口径：11-02 EOD，core_v1 / sampled_strikes；64目标、19成功、430合约。quote_coverage_complete仅指计划内样本，**不是全链**。
- 局部能力：ATM ready 19、skew ready 12；完整曲面、positioning、execution均0，dealer_gamma_direction_known=false，bid/ask覆盖0。
- AP701：ATM5800 IV34.425% vs RV20 30.657%，表面差＋3.77 vol；RR25 -0.17。OI701：ATM10200 IV15.54% vs RV20 11.665%，表面差＋3.88 vol；RR25 +1.50。缺bid/ask，不能据此卖波动。
- MA612：ATM3650 IV50.61%、RR25＋1.21、BF25＋3.045，到期11-11；候选是MA701，且夜盘后moneyness已变，不能跨标的/跨时点外推。
- SC/CU/EC/AG均未取得本批样本。研究机会仍在，但任何期权表达必须在09:15后询价；最高净支出只能受NAV风险预算约束，未询价前不称便宜、可成交或结构限损。

## 9. 09:00开盘风险地图

| 层 | 已知 | 开盘倾向 | 09:15/09:30/09:45动作 |
|---|---|---|---|
| Previous China EOD | SC、MA、BU、EB前日强；CU/EC/AG弱 | 与夜盘冲突大 | 先区分前结算与前收盘，不把close-settle差写成夜盘新增 |
| Current T Night | SC -6.65%、MA -3.80%、BU -4.04%、EB -4.19%；CU +0.52%、AG快照+2.18% | 能化低开、CU/AG偏高开 | 15分钟看缺口是否回补；30分钟核curve；45分钟才考虑加确认仓 |
| 07:00 Overseas | WTI/Brent约-7.4%/-7.6%，LME铜+0.9%，COMEX银+3.6% | 强化板块分化 | SC不追空；CU不追高；EC只看日盘与实体；AG需先补最终夜盘与精确曲线 |

合法窗口：2026-11-03为正常交易日，9:00开市；夜盘标签11-03、开始11-02符合交易日语义，无calendar_mismatch。EC、JD、LC、AP等制度无夜盘不构成质量惩罚。

## 10. 未来24小时/7日事件、行动前覆盖与发布校验

- **2026-11-03 09:00/09:15/09:30/09:45｜中国日盘与分层确认**：先查SC/CU/EC准确合约、曲线和海外锚；不把首笔跳空当持续信号。
- **2026-11-03 23:00｜美国9月JOLTS**：铜/贵金属的实际利率与美元风险；数据前降低Delta，期权报价合格才保留Vega。
- **2026-11-03美国时段｜美国中期选举**：美元、实际利率、能源政策和地缘消息跳空；不隔夜扩大同因子风险。
- **2026-11-04 23:30｜EIA周度石油状况报告**：SC/BU/FU/化工链；若库存与油价同向，才提高确认仓。
- **2026-11-05待官方周报时点｜USDA周度出口销售**：豆粕/油脂/玉米小麦；当前不预设方向。
- **2026-11-06 21:30｜美国10月就业报告**：美元与实际利率；CU/AG时间退出不得晚于数据后失控时段。
- **2026-11-07 04:30｜CFTC COT**：仅作拥挤背景，不把滞后持仓当实时dealer方向。
- **未来7日｜伊朗—美国谈判/潜在再升级；OPEC+/IEA未取得本窗口内新发布日**：SC双向gap核心；任何新闻先核原文与发生时间。
- **下一窗口｜USDA/WASDE**：本次未取得精确且位于7日内的正式发布时间；不得据猜测预埋农产品仓。

行动前覆盖清单：已扫描77品种、5层与方向/曲线/跨品种/跨境/波动；Top3核准确合约与参数；旧观点沿稳定ID；Night当前批次失败已隔离、fallback逐合约标时点；Stock仅2公司；未取得DCE官方核对、A/B实体基差、SC/CU/EC/AG期权执行报价与AG最终夜盘，故相关执行结论均受限。

发布前实算：五项分项均未超25/25/20/15/15且总和核对；SC/CU/EC三张卡的每手风险、目标PnL、净R与限幅压力已按同一货币重算；MD/JSON方向、分数、状态、触发顺序、时间退出与风险预算同源。未解缺口没有报“通过”。archive_status=success仅在六路径写后回读一致时成立；CI为pending_or_unverified。

### 来源

- [China Commodities Engine 11-02 EOD](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json)（2026-11-02 EOD）：五所806合约、77品种、EOD close/settle/量仓与曲线。
- [Market State](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json)（2026-11-02）：同合约1/5日收益、RV20、ΔOI与曲线z。
- [Night Session Status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json)（2026-11-03 06:04 BJT）：当前批次806/806 query_error、0合约、未发布、保留前一有效快照。
- [Physical](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json)（2026-11-02）：20目标、18有效、基差均C级不计方向确认。
- [Options Quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)（2026-11-02）：64目标、19成功、430合约、bid/ask覆盖0、非全链。
- [Options Surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)（2026-11-02）：19个ATM ready、12个skew ready、surface/positioning/execution均0。
- [Futures Official Crosscheck](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/crosschecks/futures_latest.json)（2026-11-02）：SHFE/INE/CZCE/GFEX可比价格差异0；DCE HTTP412。
- [SC exact-contract fallback](https://www.9qihuo.com/hangqing?productcode=sc)（2026-11-03 02:30 BJT）：SC2612 681.0、SC2701 676.7、供应商最新成交快照。
- [CU exact-contract fallback](https://www.9qihuo.com/hangqing?productcode=cu)（2026-11-03 01:00 BJT）：CU2612 108370、CU2701 107740、供应商最新成交快照。
- [MA exact-contract fallback](https://www.9qihuo.com/hangqing?productcode=MA)（2026-11-02 23:00 BJT）：MA701 3422、MA612 3550、旧多触发价未达。
- [Oil settlement and Iran talks](https://www.wsj.com/business/energy-oil/oil-drops-amid-diplomatic-efforts-to-revive-mideast-peace-talks-964fc4d6)（2026-11-02 US settlement）：WTI 96.46、Brent 104.77及日跌幅。
- [Reuters Iran negotiations](https://www.reuters.com/world/middle-east/iranians-have-left-doha-talks-draft-proposal-us-deal-being-circulated-official-2026-11-02/)（2026-11-02）：谈判仍无突破、草案流转且再升级风险仍在。
- [WSJ Metals](https://www.wsj.com/finance/commodities-futures/gold-rises-but-expectations-of-tighter-u-s-monetary-policy-weigh-512a4860)（2026-11-02）：LME 3M铜14251、COMEX银51.04。
- [INE 11-02 Daily Data](https://www.ine.cn/reports/tradedata/dailyandweeklydata/)（2026-11-02）：EC2611/2612官方收盘结算量仓。
- [SCFIS](https://www.sse.net.cn/index/singleIndex?indexType=scfis)（2026-11-02）：欧线2304.32、周涨4.8%。
- [CNOOC 3Q operational release](https://www.cnoocltd.com/english/presscenter/pressreleases/2026/202610/t20261030_123124.html)（2026-10-30）：前三季产量593.7百万桶油当量、归母利润1191.2亿元、资本开支约899亿元。
- [Zijin H1 filing](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)（2026-08-22）：2026H1收入1941.78亿元、归母利润391.70亿元、经营现金流554.72亿元。
- [BLS November schedule](https://www.bls.gov/schedule/2026/11_sched_list.htm)（2026-11）：JOLTS与就业报告发布时间。
- [EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)（2026-11）：周度石油报告常规发布时间。
- [CFTC COT schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)（2026-11）：11月6日COT发布时间。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：SC2612反弹失败空、CU2612三重确认多、EC2612实体运价转弱后空；任何AND/顺序条件缺失即不执行。
C. 今天继续观察：MA701、AG2612、BU/EB/FU曲线冲突，以及AP/OI局部波动结构。
D. 今天必须回避或有条件退出：旧SC突破多、旧MA回踩多、旧AG破位空均已失效；无成交回执，不默认持仓。