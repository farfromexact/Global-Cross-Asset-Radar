# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-23

> 数据截点：北京时间 2026-08-23 07:05。周末模式。仅用于研究与交易决策支持，不自动下单。中国国内部分使用最近完整交易日 2026-08-21 EOD；China-Commodities-Engine 不生产中国分钟、逐笔、夜盘/session产物，因此不得从仓库推断周五夜盘。周日07:00海外常规期货尚未重开，本期海外价格基线为8月21日美盘收盘，叠加8月22日至今周末新闻。下一中国日盘为2026-08-24（周一）09:00。

## 一、今日一句话结论

**有值得冒险的机会，但今天没有可立即建立的新仓：周一优先 FU2611 回撤确认多，其次 AG2610 回撤多/有限风险Call Spread，FG701失败反弹空。周末伊朗制裁与黑海风险抬升尾部，但伊拉克油轮获准通行使能源更可能出现“高开后分化”，追价赔率下降。**

## 二、数据质量与覆盖

第一读取层：`China-Commodities-Engine/data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；按需读取 `data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/latest.json`、`data/contract_meta.json`，并直接使用 `report_input` 内嵌 surface series。

统一报告输入仍为 `requested_date=2026-08-21`，`generated_at=2026-08-21T19:02:52.405697+08:00`。这在周日属于正常的最近完整中国EOD，而不是中国数据失败。五所 SHFE/INE/DCE/CZCE/GFEX 齐全，`full_market_ready=true`，`source_date_match_pct=100%`，critical errors=0，803个期货合约；unknown=0、duplicate=0、invalid OHLC=0、negative volume/OI=0，placeholder=5且已排除异常排行，核心无carried-forward。

Market State 同合约1D/3D/5D/20D、RV20、成交/OI z-score、ΔOI和curve可用，不拼接主力收益。Physical仅4/20映射：I港口库存（8/19周度）、JM NBS现货（8/10旬度）、FG企业库存（8/21周度）、TA加工费（8/21周度）；这些“fresh”仅代表原生频率仍有效，没有可验证方向变化时只作context。JM basis=Spot-Futures为337.3元/吨，但仅C级、缺交割地/税口径，`eligible_for_physical_score=false`，不得计分或称套利。

External仓库22个目标仅6个映射，5 fresh、1 stale，整体 `data_fresh=false`；所有可用跨境序列均为context_only，import parity全部不可执行。周日晨间仓库External没有新的周末价格，本期用公开新闻补充。Options 8/21共21,816条、59/64品种成功；AP/CJ/PL/PR/ZC因source-date停在8/20降级。独立surface约360/368 series research-ready、positioning约70/368 ready、execution=0/368，bid/ask coverage=0，dealer gamma方向未知。因此可以研究ATM IV/RR25/BF25和有限风险结构，但不能虚构净权利金、成交成本或精确slippage。

Contract metadata仍partial：DCE根metadata抓取异常、GFEX根metadata存在非fresh问题；Top交易参数缺失时使用交易所官网最新可核验公告，仍要求下单前复核券商保证金和临时风控调整。

## 三、商品仪表盘

| 板块 | 合约 | 8/21 close / settle | 1D结算 | 5D | 成交 / OI / ΔOI | curve | Physical/basis | Options | 信号 |
|---|---|---:|---:|---:|---|---|---|---|---|
| 能源 | FU2611 | 3845 / 3850 | +2.12% | +9.81% | 650,637 / 285,614 / +22,573 (+8.58%) | Back +7.47%，z≈+1.70 | 无完整实体层 | ATM 3850，IV 43.0%，RR25 -1.22，surface✓/positioning×/execution× | **最强条件多** |
| 能源 | BU2610 | 4508 / 4526 | +2.14% | +7.92% | 486,111 / 334,627 / -2,643 (-0.78%) | Back +3.16% | 无完整实体层 | ATM4550，IV27.745%，surface✓/positioning×/execution× | 多，但价涨仓减 |
| 贵金属 | AG2610 | 16771 / 16611 | +3.11% | +5.45% | 773,038 / 306,822 / +4,403 (+1.46%) | 轻Contango -0.14%，样本短 | 无实体确认 | ATM16600，IV47.265%，RR25 +7.81，BF25 +1.93，surface✓/positioning×/execution× | 趋势强、Call昂贵 |
| 建材 | FG701 | 907 / 906 | -1.09% | -3.10% | 1,575,371 / 1,601,238 / +148,375 (+10.21%) | Contango -3.35% | 最新周度库存7441.4重量箱，仅绝对水平 | surface ready；execution× | **失败反弹空** |
| 新能源 | LC2701 | 158680 / 156360 | +2.60% | +1.41% | 225,444 / 353,437 / +31,875 (+9.91%) | 仍Contango约-0.30% | 无验证锂库存序列 | 代表surface IV约35.37%，positioning×/execution× | 资金反弹，不叫短缺 |
| 农产品 | RM611 | 2238 / 2246 | -1.36% | +2.60% | 747,569 / 651,265 / — | Back约+3.96% | 实体层缺失 | surface ready；execution× | 价格与curve冲突，观望 |
| 有色 | CU2610 | 107520 / 107010 | +0.14% | -0.39% | ΔOI +7,165 (+4.22%)；V/OI≈0.38 | 近端约+0.26% | 无A/B基差 | ATM108000，IV14.3%，RR25 +4.14，positioning✓/execution× | LME squeeze缓和，不追 |
| 航运 | EC2610 | 1957 / 1885.5 | +7.56% | +18.66% | ΔOI约+11.84% | 高波动/不作普通curve套利 | 航运事件驱动 | 本期不做精确vol执行 | 极端动量，禁止追高 |

时间说明：以上国内价格均为2026-08-21完整EOD；周日07:00没有新的中国EOD，也没有可验证的中国夜盘层。海外最新有效收盘：Brent 94.39美元/桶、WTI 87.06美元/桶（8/21收盘），周涨约6.39%/5.66%；现货黄金约4623.94美元/盎司、白银约69.62美元/盎司（8/21纽约时段）。

## 四、相比上一期真正变化

1. **中国价格、curve、OI、IV没有新一根K线**：周六/周日休市，所有国内量价仍是8/21 EOD；本期变化来自周末事件分布，而不是伪造“周末涨跌”。
2. **伊朗风险继续抬升但变得更双向**：美国财政部长Bessent预计周一14:00 EDT公布对伊朗新制裁；伊朗公开反对并警告帮助美国的邻国。与此同时，伊朗已特别允许部分伊拉克油轮通过霍尔木兹。前者增厚上行尾部，后者降低“纯粹单向缺油”概率。
3. **Hormuz仍远未恢复正常**：Reuters称近期通过量仍显著低于战前水平，供应风险没有解除。因此FU/SC/BU的curve确认仍有效，但周一不该用周末headline追高。
4. **黑海粮食与能源尾部再抬升**：俄乌针对炼厂、港口和粮食基础设施的互袭升级，俄方警告将打击乌克兰敏感经济部门。对油和粮均是event convexity，不等于国内RM/油脂已获得实体确认。
5. **中国财政支持更多是“加快既有项目+消费/贷款补贴”**，不是大规模新增刺激。它足以让FG/RB空头在周一先遭遇beta short squeeze，但不足以否定FG自身的弱价+增仓+contango结构。
6. **Options赔率没有改善**：AG仍是“方向强但上行IV/skew很贵”；execution仍为0/368，周一必须拿到真实bid/ask后才把结构从研究卡变成执行卡。

## 五、产业链地图

**能源/炼化：最强，高置信度。** FU价格、ΔOI和Backwardation共振，海外Brent/WTI和Hormuz风险同向；缺口是国内炼厂利润、库存、裂解与周一开盘后的真实增量持仓。最重要的新信息不是“有没有headline”，而是周一高开后Back是否继续走强、OI是否继续增加。

**贵金属：方向强、赔率下降，中高置信度。** AG价格趋势和海外金银/弱美元同向，但AG2610 ATM IV 47.265%相对RV20 30.82%高约16.45 vol，RR25 +7.81 vol。方向看多不等于应该裸买Call，有限风险价差更合理。

**建材：最弱，中高置信度。** FG701 价格下跌、OI大增、contango三者同向；但Physical只有周度库存绝对水平，不能把实体层算满。财政headline使开盘直接追空的胜率下降，最优是等反弹失败。

**新能源：反弹而非短缺，中等置信度。** LC涨价+增仓但curve仍contango，且没有可验证锂库存/现货方向闭环；任何“锂短缺”叙事目前都超出证据。

**农产品/航运：事件风险高、可交易闭环不足。** Black Sea风险抬升粮食尾部；RM本身价格与curve冲突。EC动量极端，周一最危险的错误是把事件风险当成追价理由。

## 六、机会排行榜

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段/工具 | fresh证据层 | 主要惩罚 |
|---:|---|---:|---|---|---:|---|
| 1 | **FU2611 周一回撤确认多** | **79** | 多 / 1–5D | 条件试仓；期货优先，期权报价后Call Spread | 4：价仓、curve、海外、options | 周末gap；Physical缺失；execution× |
| 2 | **AG2610 周一回撤确认多** | **76** | 多 / 1–5D | 条件试仓；小期货或Call Spread/Fly | 3：价仓、海外、options | IV/skew贵；curve弱；execution× |
| 3 | **FG701 失败反弹空** | **74** | 空 / 1–5D | 条件试仓；期货，报价后Put Spread | 3：价仓、curve、options | 实体仅level；参数需复核 |
| 4 | BU2610 能源趋势替代多 | 72 | 多 / 1–5D | 仅在不持FU时做 | 4 | 与FU重复因子；价涨仓减 |
| 5 | EC2610 极端动量 | 69 | 观察 / 1–3D | 不追；等45分钟 | 2 | 过热、闭环不足 |

评分纪律未放松：没有80+确认交易。今天是周日，因此**A项没有立即新仓**；但周一存在70+条件交易，不应写成“今日商品期货期权无合格交易”。

## 七、前三名交易卡

### 1）FU2611｜79分｜回撤确认多

**事实**：8/21结算3850，1D +2.12%、5D +9.81%、ΔOI +8.58%；FU近端Backwardation约+7.47%、z≈+1.70；FU2611期权到期2026-10-19，ATM3850、IV43.0%，surface ready但positioning/execution not ready。海外Brent/WTI周线强，Hormuz仍受限。

**市场定价**：供应风险溢价已经很大。**推断**：周一第一回撤能否被承接，比周末再出现一条利多新闻更有信息量。**主观判断**：全市场最值得冒险的候选，但不到80分，不允许预埋追涨单。

**最佳表达**：期货优先。若周一真实quote恢复且spread合理，可用1:1 Call Spread（长腿约35–45Δ、短腿约15–25Δ）；不报净权利金，因为execution=false。

**入场/分批**：8/24 09:00后至少等30分钟，若gap≤约2%，3810–3850区域守住、价格重新站上VWAP/3850，先1/3；突破Opening Range高点再加1/3；只有ΔOI继续为正且Backwardation不收窄时再加最后1/3。若gap>2%–2.5%，至少等45分钟，不追。

**止损与失效**：3810有效跌破且15分钟不能收回先减半；进一步跌破约3770，同时Backwardation明显压缩、Brent早盘转弱，则逻辑失效。TP1约3970或+1R；TP2约4080或+2R；2个交易日不延续则时间止损。

**风险与参数**：10吨/手、tick 1元/吨、tick value 10元/手；按结算3850名义约38,500元/手。上期所2026-06-23公告显示FU2611涨跌停14%、一般持仓保证金16%、套保15%；券商加收未确认，周一下单前复核。标准交易时间含交易所规定夜盘；燃料油合约规则最后交易日为合约月份前一月份最后一个交易日，因此FU2611应在2026年10月底前完成主力迁移观察和roll，避免进入交割风险。按14%静态压力，一板逆向约5,390元/手，两板按复合下跌约10,025元/手。单笔初始最大损失0.35%–0.50% NAV；FU+BU合并初始≤0.75% NAV。

### 2）AG2610｜76分｜趋势多，但不要裸买贵Call

**事实**：8/21 close/settle 16771/16611，1D +3.11%、5D +5.45%、20D +17.59%、ΔOI +1.46%；RV20 30.82%。AG2610期权到期2026-09-23，ATM16600、ATM IV47.265%、RR25 +7.81、BF25 +1.93，OI覆盖0.758、surface ready、positioning=false、execution=false。海外8/21现货金+2.4%至约4623.94美元/盎司、银+2.3%至约69.62美元/盎司，DXY在三个月低位附近。

**市场定价**：上行尾部和Vega已经昂贵。**推断**：期货方向可以继续对，但裸Call的赔率可能很差。**主观判断**：更适合回撤+有限风险结构，而不是用“金银强”解释任何高开。

**最佳表达**：小仓期货，或真实quote确认后做1:1 Call Spread / Call Fly。建议长腿35–45Δ、短腿15–25Δ；最大净支出=实际净权利金且不超过单笔风险预算，本报告不虚构报价。Greeks除Delta区间外不报精确值。

**入场/退出**：周一等15–30分钟；gap≤2.5%，16600/16611守住并重新突破16770，且COMEX金银不反转、DXY未快速走强时试多。16480以下接受度增加则减仓；16200失守且海外同步转弱则逻辑失效。TP1 17350，TP2 17800；1–2个交易日不延续则退出。

**风险与参数**：15千克/手、tick 1元/千克、tick value 15元；按结算名义约249,165元/手。上期所最新可核验统一调整为黄金/白银14%涨跌停、一般持仓16%、套保15%；券商保证金和临时风控周一复核。最后交易日规则为合约月15日，AG2610参考2026-10-15；实物交割，提前roll。按14%静态压力，一板逆向约34,883元/手，两板复合约64,881元/手。最大损失0.35%–0.55% NAV。

### 3）FG701｜74分｜失败反弹空

**事实**：8/21 close/settle 907/906，1D -1.09%、5D -3.10%、20D -7.46%，ΔOI +10.21%；curve约-3.35% contango。周度FG企业库存7441.4重量箱只是绝对水平，未验证方向变化，不能算完整Physical层。

**市场定价**：地产/玻璃链弱势已经部分反映。**推断**：周一财政支持headline可能先触发short squeeze；只有反弹失败才提高空头赔率。**主观判断**：不适合开盘直接卖，适合让市场先证明政策beta不足以扭转品种结构。

**最佳表达与入场**：期货空；如真实期权bid/ask可用，再研究1:1 Put Spread。09:00后等30分钟，910–918反弹失败、重新跌回VWAP下方后试空；跌破899再加。30分钟接受在920上方则止损/放弃。TP1 899，TP2 880或+2R；2个交易日不破899则时间止损。

**风险与参数**：玻璃20吨/手、tick 1元/吨、tick value 20元；按906结算名义约18,120元/手。交易所产品规则基准为实物交割、交割月第10个交易日为最后交易日；但本期仓库动态margin/price-limit字段不完整，且未取得2026-08-23针对FG701的最新动态调整公告，因此**当前保证金、涨跌停、精确夜盘参数和1/2板压力损失均不硬填**，下单前必须复核。单笔最大损失0.25%–0.40% NAV。

## 八、商品期权专项

本期只能称“代表性样本”，不能称全市场最高/最低IV。

- **AG2610**：ATM IV47.265% vs RV20 30.82%，IV-RV约+16.45 vol；RR25 +7.81。方向强、上行skew昂贵，优先Call Spread/Fly，不裸追Call。
- **FU2611**：ATM IV43.0% vs RV20 37.93%，IV-RV约+5.07 vol；RR25 -1.22，BF25 +0.82。事件Vega有价值但不便宜；positioning not ready、execution not ready。
- **BU2610**：ATM IV27.745% vs RV20 23.63%，溢价约+4.11 vol，方向性Vega负担低于AG。
- **CU2610**：ATM IV14.3%、RR25 +4.14，positioning ready但execution=false；LME flash squeeze已经部分缓和，更适合观察skew normalization而非追价。
- **LC2701**：代表surface IV约35.37% vs RV20约27.19%，但curve仍contango、Physical缺失，不能把高IV解释成短缺确认。

必须回避：AP/CJ/PL/PR/ZC新期权方向结论；任何虚构bid/ask和净权利金；dealer gamma方向推断；在AG高开时裸买高IV Call。

## 九、8月24日09:00开盘风险地图

| 品种 | 中国基线 | 周末/海外映射 | 预期gap | 是否追价 | 等待 | 最重要确认 |
|---|---:|---|---|---|---|---|
| FU2611 | settle3850 | 油价周线强；Hormuz受限，但伊拉克获特殊通行 | 偏高、双向 | 否 | 30–45m | 3810/3850、VWAP、Opening Range、ΔOI、Back、Brent周日晚重开 |
| BU2610 | settle4526 | 同能源但自身价涨仓减 | 偏高 | 否 | 30–45m | 4525、OI是否恢复增加、FU/SC共振 |
| AG2610 | settle16611 | 金银周五强、美元弱 | 偏高 | >2.5%不追 | 15–30m | 16600/16770、COMEX金银、DXY/美债 |
| FG701 | settle906 | 国内财政支持或先挤空 | 平/先反弹均可能 | 不直接追空 | 30m | 910–918是否失败、899、curve |
| EC2610 | settle1885.5 | 运输/战争风险高 | 不确定、高波动 | 否 | 45m | 开盘量价、是否出现高开低走 |
| LC2701 | settle156360 | 无新Physical闭环 | 资金驱动 | 否 | 30m | curve是否收窄contango、现货/仓单是否同步 |

严格区分：国内是8/21 EOD；没有可审计中国夜盘价；周日07:00海外也没有正常交易价格，因此现在不能把任何“周末新闻”直接写成周一gap的已发生事实。

## 十、未来24小时 / 7日事件日历（北京时间）

- **8/24 06:00左右**：按CME常规Globex时段，周日18:00 ET对应北京周一06:00附近，能源/金属首先重新定价。处理：先看Brent/WTI/COMEX金银是否验证周末headline，再决定中国09:00是否延迟入场。
- **8/24 09:00**：中国商品日盘重开。处理：Top机会均不在集合竞价追价，按15/30/45分钟规则。
- **8/25 02:00**：美国财政部长Bessent周一14:00 EDT记者会，预计细化伊朗新制裁。Delta与Vega均高；能源建议有限风险、避免同因子过度叠加。
- **8/25 03:00**：USDA Cold Storage；**04:00** Crop Progress。油脂、饲料、畜牧和天气链关注；季节性仅作先验。
- **8/26 22:30**：EIA Weekly Petroleum Status Report。能源最大定时数据催化之一；若FU已盈利，数据前不应把风险预算全部用满。
- **8/27–8/29**：Jackson Hole Economic Symposium。美元、实际利率、金银Vega高敏感；贵金属持仓优先有限损失结构。
- **8/29 03:30**：CFTC COT常规发布（8/28 15:30 ET），数据通常截至此前周二。只用于拥挤/持仓背景，不当成实时资金流。
- **持续事件**：Hormuz通航与伊朗制裁、俄乌炼厂/港口/黑海粮运、热浪与作物天气、中国政策和交易所临时风控参数。未来7日本次未确认固定OPEC+会议或WASDE月报节点，不能强造事件。

## 十一、风险预算

试仓单笔最大损失0.25%–0.75% NAV；当前Top卡建议FU 0.35%–0.50%、AG 0.35%–0.55%、FG 0.25%–0.40%。只有价格+curve/海外/期权等至少4层在周一新交易时段继续确认，才允许向0.75%–1.0% NAV放大。FU/BU/SC/LU统一视为Hormuz/能源供应同一因子，初始总风险≤0.75% NAV，确认后≤1.5%，主题绝对上限2.5%–3.0%。AG/AU合并美元/实际利率/Vega风险。压力测试必须覆盖：1/2涨跌停、周末gap、相关性破裂、流动性消失、保证金上调、IV crash/jump、交割挤压、人民币急变、中国休市期间海外大波动。

## 十二、来源

- China-Commodities-Engine：`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`、`data/physical/latest.json`、`data/external/latest.json`、`data/options/quality_latest.json`、`data/options/latest.json`、`data/contract_meta.json`。
- Reuters 2026-08-21：Oil rises as Trump threatens sanctions on Iran partners；Gold rallies to 3-month high；China pledges timely fiscal support；Dollar falls to three-month low。
- Reuters 2026-08-22：Iran condemns US plans to announce new sanctions；Iran grants permission for Iraqi oil tankers to pass through Hormuz；Putin says Ukraine opened 'Pandora's box' with strikes on economic targets。
- EIA：Weekly Petroleum Status Report，next release 2026-08-26 10:30 ET。
- USDA NASS：2026-08-24 Cold Storage 15:00 ET、Crop Progress 16:00 ET。
- CFTC：2026 COT release schedule，2026-08-28 15:30 ET。
- SHFE：2026-06-23 FU风险参数公告；2025-10-17黄金/白银风险参数公告；燃料油/白银业务细则。
- CZCE：玻璃期货合约与业务细则；动态参数下单前复核。

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：8/24 FU2611回撤确认多、AG2610回撤确认多/报价后Call Spread、FG701失败反弹空；BU仅在不持FU时作为替代。
C. 今天应继续观察的机会：LC2701 price/OI强但contango、EC2610极端动量但不追、CU2610的LME squeeze/skew normalization、Black Sea粮食尾部对RM/油脂的传导。
D. 今天必须避免或退出的交易：周一追能源/白银高开、裸买高IV AG Call、把LC上涨解释成锂短缺、AP/CJ/PL/PR/ZC期权新方向仓、任何C/D级basis或context-only跨境价差“套利”。