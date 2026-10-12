# 全球商品期货期权高风险机会雷达（晨间版）

**报告日期：2026-10-13｜生成：07:06 BJT｜信息截点：07:05 BJT｜prompt_version：`radar_2026-10-12_stock_v1`**

## 一、今日一句话结论

> **今天有铜、原油与贵金属三组待验证机会，但缺归属10月13日的精确夜盘和当前期权报价，9:00前不值得直接新增风险。**

**截至本报告时点，无可立即执行的合格新交易。** 当前regime为“国内高波动分化、外盘油强金银弱、铜内外同强，但中国Night执行层缺失”。最接近验证的是CU2611突破回踩多、SC2612油价映射多、AG2612外盘弱势确认空；下一有效窗口分别为09:15、09:30和09:30。LC2701暴跌与backwardation冲突仍是最重要早期异常，但没有支持无条件抄底或追空的实体与期权证据。

## 二、数据质量、时点与覆盖

### 2.1 实际读取、版本与最近会话

- 中国商品仓库：`farfromexact/China-Commodities-Engine@2b08a42cfe8285fa943c4827a6456127a42b0c77`。第一层读取`data/report_input_latest.json`、`data/night_session/last_run_status.json`、`data/last_run_status.json`、`data/radar_latest.json`；为精确EOD和合约参数下钻`data/latest.json`、`data/contract_meta.json`。统一输入schema v2，`requested_date=2026-10-12`，`generated_at=2026-10-12T19:11:00.250240+08:00`。
- 最近完整中国会话是10月12日日盘；下一合法中国日盘为10月13日09:00。10月13日为正常交易日。核心期货806合约、77品种，SHFE/INE/DCE/CZCE/GFEX五所齐全，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchanges=0。5条OHLC占位已排除；无负volume/OI、无重复或非法OHLC。
- Market State对72个流动性品种给出同合约1/3/5/20日、RV20、量仓z-score与near-next曲线；存在roll flag的I、RU等不把跨月拼接当真实收益。
- Physical：18/20目标可用，SC/LU unavailable；basis虽有数值但全为C级且不具备`eligible_for_physical_score`，只作context。仓单模块SHFE/DCE/GFEX失败并保留5条旧记录，本期不把它们当新增；CZCE仓单当日可用。Basis主模块、会员排名不可用。
- External仓库层为10月12日17/22条，usage=`context_only`；本报告再联网补足美国/欧洲收盘。无法完成exact-contract、币种、单位、品质、运费、税费、时点全对齐，因此所有跨市场内容均为映射，不称可执行套利。
- Contract Metadata整体`partial`：DCE contract-info失败，GFEX source-date未验证；CU/AG/SC动态保证金与限幅未发布，不推断。MA701参数相对完整；本期前三卡使用稳定合约规格作压力敏感度，但动态限幅/保证金缺失仍阻止“已可执行”标签。
- 前序基准来自`Global-Cross-Asset-Radar@5896f29fd37488b39ae2f6d276bba8a0bcb32b1c`：最近商品报告为10月12日晚报，最近同版为10月12日晨报；本次同日补跑不存在。稳定idea_id和旧观点处置见第十节。

### 2.2 Night Session质量闸门：应有而缺失

- 统一层Night仍是9月30日旧快照：`data_fresh=false`、`validation_passed=false`、`published=false`、`coverage_complete=false`。
- 模块专用`last_run_status`为周末快照：`trading_date=2026-10-11`、`night_session_date=2026-10-10`、`generated_at=2026-10-11T08:01:14.462305+08:00`，night contracts=0、product_count未发布、outside-window=592、query_error=214、unresolved=214、missing timestamp/price/quote=0；`previous_valid_snapshot_retained=true`。
- 归属10月13日、10月12日晚开始的Night Session本应发生，但仓库未生成当前快照；公开网页也未能可靠取得CU2611、SC2612、AG2612等精确合约OHLC、量仓和source timestamp。因此`night_session_fallback=false`，不是0涨跌，而是`missing`。任何重点候选最高79分且执行必须等09:00后重新取价。
- 不能计算`return_vs_close_pct`、`return_vs_settlement_pct`、Night Curve或EOD→Night分解；相对10月12日结算的盘面涨跌不能替代隔夜新增信息。旧9月30日Night和10月11日周末失败均与今日决策无关。

### 2.3 Options四级readiness

- 10月12日期权尝试抓到13604条，但模块状态`empty`且未发布；不能当可用T-1完整截面。统一层最新可用为10月9日14074条、185 series，其中181 surface-ready、41 positioning-ready、0 execution-ready，bid/ask coverage=0。
- 10月12日为截至晨报最新应得截面，既然失败，10月9日只保留历史背景，不计第五支持层；不报告ATM IV、RR25、BF25、IV-RV或当前结构成本。dealer Gamma方向未知。
- 所有期权结构仅为研究方向，固定限制：`research only; manual quote and manual confirmation required before execution; no premium quoted`。

### 2.4 Stock联动范围

- `farfromexact/China-Stock-Engine@5f80b92eb79694253cfc276b59a3e1688f171f79`较昨晚无新提交。本期沿manifest索引仅复核与重点商品相关的紫金矿业601899.SH、宝钢股份600019.SH，不是全A股扫描。
- 价量trade_date仍为10月9日，security state、ADT20、当前报价与执行状态未验证；股票10月13日尚未开盘。因此公司经营材料只用于利润传导和表达比较，不作为9:00前即时股票交易，也不把同一商品冲击引起的股价变化另算独立证据层。

### 2.5 07:00海外新增信息

- 原油：WTI 11月结算93.74美元/桶、+2.06%；Brent 12月106.65美元/桶、+1.84%。中东供应风险压过盘中俄柴油增供叙事，和中国10月12日SC结算下跌形成冲突。[Reuters，2026-10-12](https://www.reuters.com/business/energy/oil-climbs-mideast-conflict-tanker-attacks-persist-2026-10-11/)
- 贵金属：COMEX前月金结算4165.80美元/盎司、-0.6%；银60.141、-0.87%。DXY升0.37%至102.58，为18个月高位，方向上反对中国10月12日AG/AU日盘涨幅延续。[WSJ，2026-10-12](https://www.wsj.com/finance/commodities-futures/gold-rises-as-markets-weigh-oil-pullback-2c0301c2)；[Reuters美元，2026-10-12](https://www.reuters.com/world/asia-pacific/dollar-stays-near-18-month-high-mideast-conflict-inflation-data-focus-2026-10-12/)
- 铜：公开延迟行情显示LME铜约14812美元/吨、24小时+0.84%；与CU日盘上涨和backwardation同向，但不是精确进口平价。[LME Closing Prices，2026-10-12](https://www.lme.com/Market-data/Reports-and-data/LME-closing-prices)
- 农产品：CBOT 11月大豆约12.88美元/蒲式耳、跌3.75美分，12月玉米483美分、涨3.25美分，谷物信号分化；不把它映射成中国豆一/玉米必然高低开。[Brownfield，2026-10-12](https://www.brownfieldagnews.com/market-news/closing-grain-and-livestock-futures-october-12-2026/)
- 汇率：USD/CNH约6.6950，前收6.6927，人民币仅小幅偏弱；不能单独解释商品方向。[Investing，2026-10-12](https://www.investing.com/currencies/usd-cnh-historical-data)

## 三、商品仪表盘（12项展示；77品种均已初筛）

1D/5D均为同一当前合约结算收益；Night列`missing`而不是0。EOD curve是near-minus-next期货曲线，不是现货基差。

| 板块 | 品种/精确合约 | 10/12 close/settle | 1D/5D | Volume/OI/ΔOI | EOD curve | Basis/Physical | 10/13 Night | 07:00海外 | Options | 9:00信号 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 有色 | CU2611 | 110630/110770 | +1.06%/+1.22% | 72159/195149/+3109 | +0.81% backwardation，z=+1.21 | 现货112028；C级仅context | **missing** | LME约14812、+0.84% | 10/9历史S=Y/P=部分/E=N | 偏高开；等15分钟回踩 |
| 能源 | SC2612 | 719.3/709.5 | -1.24%/+3.61% | 58665/24990/+2282 | +2.95% backwardation，仅3观测 | Physical unavailable | **missing** | WTI/Brent +2.06%/+1.84% | 历史S=Y/P=N/E=N | 可能高开；等30分钟 |
| 贵金属 | AG2612 | 14816/14854 | +2.34%/-2.13% | 248317/288058/-2376 | -0.90% contango，z=-2.47 | 缺独立实体 | **missing** | 银-0.87%、金-0.6%、DXY强 | 历史S=Y/P=N/E=N | 偏低开；等30分钟 |
| 贵金属 | AU2612 | 905.52/907.78 | +0.97%/-0.47% | 170015/228793/+334 | +0.02%，近乎平 | 缺 | **missing** | 金-0.6%、美元强 | 历史S=Y/P=部分/E=N | 偏低开；不首跳追空 |
| 新能源 | LC2701 | 104740/108880 | -8.30%/-9.88% | 405572/429039/+7401 | +4.07% backwardation，z=+2.82 | 现货114000；C级仅context | 制度无夜盘 | 无exact锚 | 10/9历史S=Y/P=N/E=N | 09:45前不接飞刀 |
| 橡胶 | RU2701 | 20640/20780 | +2.77%/+6.81% | 563573/177637/+2950 | -0.95% contango；roll | 缺合格实体 | **missing** | SICOM exact缺 | 历史Y/Y/N | 不延续昨晨追多 |
| 橡胶 | NR2612 | 17620/17870 | +3.21%/+5.49% | 153854/85370/-3526 | -3.10% contango，z=-2.57 | 缺 | **missing** | exact缺 | 历史Y/N/N | 看RU/NR与curve，不追 |
| 化工 | MA701 | 3229/3257 | -1.93%/+11.01% | 1740113/773423/+12248 | +13.88% backwardation | 现货4050；C级 | **missing** | 油价上涨对空头不利 | 历史Y/部分/N | 先等45分钟，不续空 |
| 油品 | BU2611 | 5111/5160 | -2.99%/+0.16% | 642358/151851/-9394 | +12.00% backwardation | 缺 | **missing** | 原油强 | 历史Y/部分/N | 高开映射但需确认裂解 |
| 黑色 | JM2701 | 1546/1550 | +2.14%/+6.75% | 619932/413832/-11571 | +4.23% backwardation | 现货2206；C级 | **missing** | 无exact外锚 | DCE当前不可用 | 平高；等30分钟 |
| 豆类 | A2701 | 5510/5498 | +1.70%/+6.45% | 216796/258595/+20901 | -0.78% contango | 缺 | 制度无夜盘 | CBOT大豆小跌 | DCE不可用 | 内外冲突；等45分钟 |
| 航运 | EC2611 | 2786.5/2787.6 | +0.98%/-4.46% | 11833/22096/+801 | -21.94% contango，仅5观测 | 缺可比现货 | 制度无夜盘 | 运价/燃油映射不完整 | 无执行层 | 09:45前不交易 |

**强弱与regime**：EOD最强仍是铜，最弱仍是锂链；外盘新增最强是原油，最弱是贵金属。Night缺失使“境外变化是否已被中国夜盘预交易”无法判断，因此所有跨市场映射必须等中国开盘后的价格弹性确认。

## 四、相比上一交易日/昨晚真正变化

1. **原油结算翻转昨晚19:38快照**：晚报看到WTI/Brent盘中回落，本次最终结算却分别+2.06%/+1.84%。因此SC/BU由“低开风险”变为“高开风险”，但SC EOD结算下跌、Physical缺失，首跳不追。
2. **铜外盘延续而非回落**：LME延迟价约14812、24小时+0.84%，继续支持CU价格/OI与backwardation；CU仍是唯一三层同向候选。新增缺口是10月13日Night exact完全不可见，执行从昨晚21:30条件转为今日09:15后确认。
3. **贵金属弱势进一步确认**：金结算-0.6%、银-0.87%，DXY 102.58；这加强AG条件空的外盘层，但中国EOD价格上涨仍是反证，且缺Night不能知道弱势是否已在21:00后充分定价。
4. **MA空头吸引力下降**：昨日收盘已触发旧多头失效，但原油最终上涨且MA仍是极端backwardation，均反对继续追空；从晚报64分候选降为未入榜观察。
5. **股票证据无新增**：Stock commit、trade_date和两家公司研究材料均未变化；紫金/宝钢只保留利润桥，不能把“无更新”写成新催化。

## 五、产业链地图

| 产业链 | 方向/强弱 | EOD / Night | Curve与实体 | 期权/海外 | Stock利润桥与决策贡献 | 最大缺失/置信度 |
|---|---|---|---|---|---|---|
| 铜—矿山—冶炼 | **最强，条件多** | CU EOD涨且OI增；Night missing | backwardation +0.81%；basis C不计 | 期权T-1失败；LME同向 | 紫金H1收入、归母利润、OCF增长确认矿产金铜利润通道，但产量/成本/套保/汇率未量化；直接CU优于股票 | Night、进口平价、动态参数；中高 |
| 原油—炼化—沥青 | **外盘最强，国内待确认** | SC结算跌而close近平；Night missing | SC/BU backwardation；SC实体缺 | WTI/Brent最终上涨；期权exec N | 不引入炼化股：裂解价差、库存、长协和套保未对齐 | 中国夜盘、EIA前库存、裂解；中低 |
| 贵金属 | **外弱、内盘昨强** | AG/AU EOD涨；Night missing | AG contango支持空，AU近乎平 | 金银跌、DXY强；当前期权缺 | 紫金金业务仅context；股票报价滞后且早盘未开，不优于直接AG条件单 | Night、当前银报价/IV；中低 |
| 锂—新能源材料 | **最弱但曲线强冲突** | LC close -11.79%；无夜盘 | backwardation +4.07%反对追空；basis C | 期权历史且execution N | 无合格公司实时表达；不以“锂概念”替代利润证据 | 库存、成本、交割仓单；低 |
| 黑色—钢厂利润 | **焦煤强、成材弱平** | JM涨仓减；RB仅小涨；Night missing | JM backwardation、RB contango；basis C | 无可靠外锚，DCE期权缺 | 宝钢H1归母利润同比下降、毛利率约5.99%说明利润取决于钢价—矿价双边，不支持单凭矿价下跌做多股票 | 钢厂利润、库存、DCE参数；低 |

**公司原件复核**：紫金矿业2026H1合并收入1941.78亿元、归母净利润391.70亿元、经营现金流554.72亿元；宝钢股份2026H1收入1607.31亿元、归母净利润45.71亿元、毛利率约5.99%。它们是截至当前可用的旧经营事实，不是今天的新催化。[紫金半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)；[宝钢半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

| 排名 | idea_id / 方向 / 周期 | 分项：逻辑/凸性/催化/价曲波/拥挤 | 总分 | 有效支持层 | 三轴状态 | 反证、缺失与变化 |
|---|---|---:|---:|---:|---|---|
| 1 | `COM-E-CU2611-LME-BREAKOUT-LONG-20261012` 条件多 1—5D | 19/17/14/13/9 | **72** | 3：价格量仓、curve、外盘 | 待验证优势 / 部分 / 等09:15触发与参数 | Night缺、DXY强、basis C、options exec N；较晚报-1分因Night仍缺 |
| 2 | `COM-M-SC2612-OIL-GAP-LONG-20261013` 条件多 1—3D | 17/16/15/11/7 | **66** | 2：curve、外盘 | 待验证优势 / 部分 / 等09:30 | EOD结算下跌、实体/期权/Night缺；外盘结算反转使其新入榜 |
| 3 | `COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012` 条件空 1—3D | 17/16/14/11/8 | **66** | 2：curve、外盘宏观 | 待验证优势 / 部分 / 等09:30 | 中国EOD上涨反对，地缘尾部、Night与options缺；与晚报近持平 |
| 4 | `COM-E-LC2701-OVERSHOOT-REBOUND-WATCH-20261012` 条件多 1—5D | 15/15/12/8/6 | **56** | 1：curve | 证据不足 / 不足 / 等09:45 | 价格/OI反对，basis C，实体与期权执行缺；纯观察 |

分项均未超上限，总分已复核。CU三层才可超过70；SC/AG两层≤69；LC一层≤59。Night应有而缺失使所有候选最高79，且没有任何候选可在09:00前立即执行。MA、RU、JM、EC未入榜：MA的油价与curve反对追空；RU/NR的contango与无SICOM exact反对追多；JM缺Night与DCE参数；EC曲线极端但仅5观测且缺实体。

## 七、研究/交易卡（均为待触发，不是当前立即单）

### 1. CU2611条件多｜`COM-E-CU2611-LME-BREAKOUT-LONG-20261012`

- **事实**：10月12日O/H/L/C=110300/111100/110190/110630，settle=110770；1D +1.06%、5D +1.22%，OI195149、ΔOI+3109；curve +0.81% backwardation。LME延迟价约14812、24小时+0.84%。Night OHLC、双收益锚、ΔOI与Night curve全部missing。
- **市场定价/分歧**：市场已定价刺激和矿端扰动；分歧是若中国开盘后仍能站稳111100，内外同强和近端结构仍可能延续。最强反证为美元强、进口平价未对齐、利好拥挤及Night可能已完成价格发现但我们看不到。
- **五层**：①价格量仓支持；②curve支持；③Physical中性（C级basis不计）；④LME支持；⑤Options缺失。有效3层。
- **最佳表达**：CU2611期货条件多；紫金股票不优于直接商品。CU期权仅研究call spread，必须先获得当日两腿bid/ask、净支出、IV/skew与行权交割规则。
- **入场/成交情景**：09:15后。好=首15分钟回踩110800—111100守稳且LME≥14750，先半；中=突破111100后回踩不破，再半；坏=>112500无回踩，放弃。9:00首跳不追。
- **止损/失效/退出**：计划止损109950；日内有效跌破109600、LME<14600且curve转contango为逻辑失效。TP1=112800、TP2=115500；2日不扩张退出，最长5日。试仓计划风险NAV 0.25%—0.50%，期货最大损失不由结构限定。
- **参数/压力**：稳定规格5吨/手、tick 10元/吨、tick value 50元；10月12日名义约553150元/手，每1%不利变动约5532元/手。动态margin/price-limit未确认，故1/2限幅损失不填；LTD=2026-11-16，10月底前评估滚CU2612，避免交割月风险。
- **最坏/放弃**：夜盘信息已被充分预交易导致冲高回落、LME反转、人民币急变、流动性消失或临时提保；动态参数或当前盘口不能核实则放弃。

### 2. SC2612条件多｜`COM-M-SC2612-OIL-GAP-LONG-20261013`

- **事实**：O/H/L/C=714.7/723.6/695.3/719.3，settle=709.5；1D结算-1.24%、5D +3.61%，OI24990、ΔOI+2282；curve +2.95% backwardation但仅3观测。WTI/Brent结算+2.06%/+1.84%。Night exact和Physical均缺。
- **定价/分歧**：中国EOD没有计入美国时段最终油价上行；若9:00高开后仍守住前高附近，说明外盘风险溢价未被完全预交易。竞争解释是SC close已明显高于settle、外盘上涨全属地缘跳价，开盘会兑现回落。
- **五层**：①EOD价格层中性/反对；②curve支持；③Physical缺；④外盘支持；⑤Options缺。有效2层。
- **表达**：SC2612小规模条件多；不以BU替代，因为裂解和品质不同。SC call spread仅研究，当前报价与IV缺失。
- **入场/情景**：09:30后。好=开715—724、15分钟收于723.6上且回踩719—724守稳；中=先高开后回补缺口但Brent仍≥105.5，再现量价确认；坏=>735首跳或Brent<104.5，放弃。首跳不追。
- **风险/退出**：计划止损706；跌破695.3或Brent<103.5为逻辑失效。TP1=735、TP2=752；1日不扩张退出，最长3日。试仓风险NAV 0.25%。
- **参数/压力**：稳定规格1000桶/手、tick 0.1元/桶、tick value 100元；按719.3名义约719300元/手，每1%约7193元/手。动态margin/limit未确认，1/2限幅压力损失待参数；LTD=2026-11-30，11月中前滚动，实物交割风险高。
- **最坏/放弃**：中东headline反转、俄供给兑现、EIA前后gap、境内外时差相关性破裂、临时提保。若无法取得09:30价格和Brent同步报价则不做。

### 3. AG2612条件空｜`COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012`

- **事实**：O/H/L/C=14679/14995/14679/14816，settle=14854；1D +2.34%、5D -2.13%，ΔOI=-2376；curve -0.90% contango。COMEX金/银结算下跌、DXY升至102.58。Night exact缺。
- **定价/分歧**：中国日盘定价反弹；分歧是海外收盘弱势与contango可能带来回吐。最强反证是中国价格层仍强、中东风险可使贵金属瞬时反转、缺Night无法知道是否已低开。
- **五层**：①价格层反对；②curve支持空；③Physical缺；④外盘/美元支持空；⑤Options缺。有效2层。
- **表达**：AG2612期货条件空；put spread仅研究，不给strike、权利金或Greeks。
- **入场/情景**：09:30后同时满足AG<14679、COMEX银≤60.2且反抽14680—14800失败。好=14700附近失败；中=14650下破回抽；坏=<14400首跳，放弃追空。
- **止损/失效/退出**：止损15020；AG重回14995上且银>61.3为逻辑失效。TP1=14400、TP2=13950；1日不扩张退出，最长3日。试仓风险NAV 0.25%，与AU/美元同因子合并。
- **参数/压力**：稳定规格15千克/手、tick 1元/千克、tick value 15元；名义约222240元/手，每1%约2222元/手。动态margin/limit未确认，1/2限幅损失不填；LTD=2026-12-15，11月底前滚动，交割风险不可忽略。
- **旧观点处置/放弃**：旧AG多头不再加仓；若此前按条件建立且跌破14679，应按收紧失效退出，但不机械反手。地缘升级、银重新站上61.3或当前盘口缺失则放弃。

## 八、商品期权专项

- **样本**：10月12日尝试层13604条未发布；10月9日历史层14074条、185 series，181 surface-ready、41 positioning-ready、0 execution-ready。全市场product coverage约60.94%，bid/ask coverage=0。
- **IV-RV / skew / term**：最新应得10月12日截面失败，不能把10月9日ATM IV、RR25、BF25或期限结构冒充当前；CU RV20约15.93%、SC 57.94%、AG 31.69%仅是标的历史波动，不等于期权IV便宜或昂贵。
- **Event convexity**：CPI、PPI/EIA与中东headline具备凸性需求，但无当前期权成本，无法判断买波盈亏平衡。若盘前/盘中取得完整报价，优先比较CU call spread、SC call spread、AG put spread的最大净支出与事件后IV crush；否则使用小规模期货条件单或不交易。
- **回避**：所有裸卖期权、以旧IV估当前Greeks、以OI推dealer Gamma、无bid/ask的“低成本”结构、临近交割月虚假深度。

## 九、9:00开盘风险地图

三层必须分开：①Previous China EOD=10月12日；②Current T Night=应归属10月13日但**missing**；③07:00 Overseas=美国/欧洲10月12日收盘。缺Night意味着无法判断外盘变化是否已在中国21:00后预交易。

| 品种 | Previous EOD | Current T Night | 07:00 Overseas | 潜在开盘/追价 | 等待与确认 |
|---|---|---|---|---|---|
| CU2611 | 涨、OI增、backwardation | missing | LME铜上行 | 偏高开；不追首跳 | 15分钟：111100回踩、LME≥14750、OI/curve |
| SC2612 | 结算跌、close近平、backwardation | missing | WTI/Brent结算约+2% | 高开概率较高；不追 | 30分钟：723.6上方接受、Brent≥105.5、回补幅度 |
| AG/AU | 中国日盘涨；AG contango | missing | 金银跌、DXY强 | 偏低开；不机械反手 | 30分钟：AG 14679、银60.2、美元是否继续强 |
| MA701 | 收跌但极端backwardation | missing | 油价上涨反对空 | 平高/高开不确定；不追 | 45分钟：3176与3300区间、curve是否收窄 |
| RU/NR | EOD强但contango | missing | SICOM exact缺 | 无可靠gap方向 | 30分钟：20640/20980、RU/NR价差、OI |
| LC2701 | 暴跌、OI增、backwardation | 制度无夜盘 | 无exact锚 | 可能高波动双向 | 45分钟：104680低点、108880结算、产业成交 |
| A/C | EOD涨 | 制度无夜盘 | CBOT豆跌玉米涨 | 分化，不追 | 45分钟：国内现货/基差、量仓是否延续 |
| EC2611 | 小涨、极端contango但历史短 | 制度无夜盘 | 运价/燃油映射不完整 | 方向不足 | 45分钟：近远月同pair、成交深度 |

## 十、未来24h / 7d事件、覆盖核对与旧观点

### 10.1 事件日历（北京时间）

- **10月14日20:30**：美国9月CPI与Real Earnings，BLS官方日历确认。贵金属、美元、铜的Delta/Vega风险高；不在数据前扩大裸方向，期权只在核实净支出后做有限凸性。[BLS日历](https://www.bls.gov/schedule/2026/10_sched.htm)
- **10月15日20:30**：美国9月PPI；同上，关注工业金属和贵金属对利率预期的二次反应。[BLS日历](https://www.bls.gov/schedule/2026/10_sched.htm)
- **10月16日00:00**：EIA周度石油状态报告（Columbus Day延至周四12:00 ET，官方表确认）。SC/BU/FU/LU避免数据前满Delta，若有可靠报价可用有限支出价差替代裸期货。[EIA schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **未来7日**：IEA月报、OPEC+临时沟通、CFTC持仓、天气与矿山/油田/炼厂事件持续关注；本期未从官方页面核到新的OPEC+会议或IEA精确发布时间，不编时点。USDA 10月WASDE已于10月9日发布，下一月度报告不是24h催化。[USDA WASDE](https://www.usda.gov/about-usda/general-information/staff-offices/office-chief-economist/commodity-markets/wasde-report)
- **公司披露**：紫金/宝钢当前无在24h内已核实的定期报告安排；若出现公告，先区分经营事实、一次性项目和商品价格冲击，再决定是否改变直接商品表达。

### 10.2 覆盖核对

- **应覆盖**：63个指定代码＋动态上市合格品种；引擎实际含77品种。指定清单逐项均有产品级Market State，唯一字面差异是用户写`LPG`、引擎官方代码使用`PG`，按同一品种映射处理；不是缺失。
- **实际取得且已分析**：指定63/63的EOD与Market State；77/77引擎产品完成初筛。板块包括黑色建材、有色贵金属、能源化工、新能源、农产品油脂畜牧、航运软商品。展示12项不代表只扫描12项。
- **数据不足**：归属10月13日Night为全市场missing；SC/LU Physical缺；高质量basis=0；SHFE/DCE/GFEX仓单当次失败；DCE期权/参数受限；10月12日期权未发布、execution-ready=0；Stock tape只到10月9日。
- **不适用/流动性不足**：LC、A/C、EC等制度无夜盘不判pipeline错误；部分77品种（如JR/RI/RS/WH/ZC/WR等）流动性不足或历史/曲线样本短，保留在扫描状态但不进榜。
- **未入榜板块异常**：黑色看JM涨仓减与RB弱；油脂看P量仓增强但外盘不统一；橡胶看RU/NR强势与contango冲突；软商品看EC极端contango但仅5观测；化工看MA高波动与极端backwardation。均不足以超过榜内候选。

### 10.3 旧观点台账

- `COM-E-CU2611-LME-BREAKOUT-LONG-20261012`：昨晚首次提出。21:00后精确中国路径不可核，触发状态**未知**；今天继承原失效位，不假定成交。变化原因：外盘延续支持，但Night数据缺失使执行窗口推迟到09:15。
- `COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012`：昨晚首次提出。触发状态未知；金银收盘进一步走弱支持假设，但缺Night阻止认定已触发。旧`COM-E-AG2612-DAY-REVERSAL-LONG-20261009`继续为“不得加仓”；若此前建立，按14679/14995的更新条件管理。
- `COM-E-MA701-POSTSPIKE-REVERSAL-SHORT-20261012`：油价最终上涨与极端backwardation反对继续追空，降出Top5；旧多头`COM-M-MA701-MOMENTUM-HOLD-20261009`仍已失效。若此前有条件建立任何MA方向，应按各自原失效位处理，不把新观点自动变成反手。
- `COM-M-RU2701-SUPPLY-LONG-20261002`：10月12日日盘反转已使追多降级；当前Night再度缺失，继续观察而非恢复。
- `COM-M-SC2612-OIL-GAP-LONG-20261013`：本期新增研究，原因是外盘结算相对昨晚盘中快照显著翻转。没有用户持仓或成交反馈。

### 10.4 输入版本与关键缺口

- 商品commit：`2b08a42cfe8285fa943c4827a6456127a42b0c77`；Stock commit：`5f80b92eb79694253cfc276b59a3e1688f171f79`；前序归档commit：`5896f29fd37488b39ae2f6d276bba8a0bcb32b1c`。
- 决策关键缺口排序：①10月13日精确Night；②09:00实时中国盘口与动态参数；③10月12日期权曲面/两腿bid-ask；④可比Physical/进口平价。缺口只限制对应表达，不把其他可支持研究写成“市场没有机会”。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：CU2611在09:15后回踩111100守稳且LME≥14750；SC2612在09:30后站稳723.6且Brent≥105.5；AG2612仅在09:30后跌破14679且COMEX银≤60.2时人工确认。
C. 今天应继续观察的机会：LC价跌—backwardation冲突、RU/NR强势与contango、MA高波动但油价/curve反对追空，以及紫金/宝钢利润桥后续是否有新公司事实。
D. 今天必须避免或退出的交易：避免9:00首跳、LC抄底或追空、所有无当日bid/ask期权；若此前按条件建立的MA多头仍未退出应执行原失效纪律，AG旧多头跌破14679则有条件退出而非机械反手。
