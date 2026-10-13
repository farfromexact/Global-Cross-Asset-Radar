# 全球商品期货期权高风险机会雷达（晚间版）

**报告日期：2026-10-13｜生成：19:56 BJT｜信息截点：19:29 BJT｜prompt_version：\`radar_2026-10-12_stock_v1\`**

## 一、今晚一句话结论

> **截至本报告时点，无可立即执行的合格新交易；国内油品强势与收盘后国际油价回落冲突，最值得等21:30确认，生猪空头则等明早。**

当前regime是“**中国能源链动量/近端紧张很强，但外盘边际转弱；农畜与新能源偏弱；期权、Night与动态参数执行层明显降级**”。最接近验证的三个观察项是：LU2612能否在Brent恢复105.5美元/桶同时守住5965、BZ2611能否放量站稳9758、LH2701能否在10月14日09:30跌破10600后不迅速收回。以上均是条件候选，不是已触发订单。

## 二、数据质量、时点与覆盖

### 2.1 实际读取、版本与最新会话

- 中国商品仓库固定于本次读取的 \`farfromexact/China-Commodities-Engine@9eb28aeffabf20bb79f7ba8c3993f62a3a833fd6\`。第一层读取 \`data/report_input_latest.json\`、\`data/last_run_status.json\`、\`data/night_session/last_run_status.json\`、\`data/radar_latest.json\`；为精确合约、实体、海外及参数审计，下钻 \`data/latest.json\`、\`data/night_session/latest.json\`、\`data/physical/latest.json\`、\`data/external/latest.json\`、\`data/contract_meta.json\`。
- 统一输入 \`requested_date=2026-10-13\`、\`generated_at=2026-10-13T19:12:47.437134+08:00\`、schema v2。最近完整中国交易时段为10月13日日盘；今晚21:00若正常开市，属于下一交易日10月14日。
- **Futures/Market State**：806个具体合约、77个品种；SHFE/INE/DCE/CZCE/GFEX五所齐全，\`full_market_ready=true\`、\`source_date_match_pct=100%\`、critical errors=0、excluded exchanges=0。4条OHLC占位记录已排除异动排序；无重复、负volume/OI或非法OHLC。20个交易日同合约历史可用；72个品种具备本期可比状态，JR/PM/RI/WH/ZC流动性或历史不足。
- **Physical**：20条中18条在原生频率下fresh，SC/LU unavailable；无本期新增可用A/B级basis。FU、LC、CU、SA等现货映射均为C级，缺地区/品质/含税/交割地，只作context。SHFE/DCE/GFEX仓单模块有失败或旧值，不能冒充社会库存或本期确认。
- **External仓库层**：19:12生成，17/22序列fresh，全部 \`usage=context_only\`，不构成全口径进口平价。19:12值：WTI 91.87美元/桶、Brent 104.74、LME铜14638美元/吨、COMEX金4205.3美元/盎司、银60.53；均标为连续/代理行情而非exact-contract套利报价。[商品统一输入](https://github.com/farfromexact/China-Commodities-Engine/blob/9eb28aeffabf20bb79f7ba8c3993f62a3a833fd6/data/report_input_latest.json)
- **Contract Metadata**：quality=partial；有效合约匹配73.45%，乘数/最小变动覆盖36.1%，夜盘字段0%，保证金/限幅约30.15%。LU2612/SC2612的最后交易日为2026-11-30、最后交割日为2026-12-07，但本次仓库未给乘数/tick；交易所标准合约显示LU为10吨/手、1元/吨最小变动，因此tick value=10元。SC标准为1000桶/手、0.1元/桶，tick value=100元。10月12日结算后SC2612、LU2612涨跌停16%，一般持仓保证金18%、套保17%。[INE参数通知，2026-10-09](https://www.ine.cn/publicnotice/notice/202610/t20261009_833669.html) [INE日周数据单位说明](https://www.ine.cn/reports/tradedata/dailyandweeklydata/)
- **Options**：统一层仍是10月9日截面，14074条、185 series，181 surface-ready、41 positioning-ready、0 execution-ready，bid/ask coverage=0；相对10月13日已落后于最新应得截面，因此只作历史背景，不计第五支持层。DCE产品跳过或权限失败；不得输出当前ATM IV、RR25、BF25、权利金或可成交结构。
- **Stock联动**：固定于 \`farfromexact/China-Stock-Engine@67678376a04e75a8c6911b52349e5ac337427a33\`，只读取映射配置、紫金矿业601899与宝钢股份600019对应分片及机会雷达，不是全A股扫描。价量trade_date=10月12日，研究asof为10月13日07:36 BJT；5D/20D、复权、ADT、行业和execution未就绪，股票今晚已收盘。紫金2026H1收入1941.78亿元、归母利润391.70亿元、经营现金流554.72亿元，说明金铜业务到利润的通道存在，但不能把旧半年报当今天催化；宝钢H1归母利润同比下降6.30%，反驳“铁矿弱就必然利好钢企”的简单映射。直接商品工具仍优于当前股票表达。

### 2.2 已完成Night Session：属于10月13日交易日，不是今晚未来行情

模块记录 \`trading_date=2026-10-13\`、\`night_session_date/session_start_date=2026-10-12\`、\`generated_at=2026-10-13T08:59:xx+08:00\`、\`data_fresh=true\`、\`validation_passed=true\`、\`published=true\`，但 \`coverage_complete=false\`。在806个选择合约中，只有5个有效夜盘记录、4个品种；outside-window=585、query_error=214、unresolved=214，missing timestamp/price/quote均为0。有效记录仅CY705/CY707、PL610、SA610、SH610。

这些数据是昨晚至今凌晨已经完成、归属10月13日的连续交易阶段，**绝不是今晚21:00的10月14日行情**。LU/FU/SC/BZ/LH/LC/CU/AG等重点具体合约没有可验证的同合约Night OHLC/量仓；DCE合约多为query_error。因此本期没有对这些合约强算overnight、day_follow_through或Night curve。SA虽有SA610夜收954，但正式观察合约是SA701，不能跨月替代。[Night状态](https://github.com/farfromexact/China-Commodities-Engine/blob/9eb28aeffabf20bb79f7ba8c3993f62a3a833fd6/data/night_session/last_run_status.json)

### 2.3 15:00—19:29海外新增定价

- Brent从周一结算106.65美元/桶回落至仓库19:12的104.74，约-1.79%；WTI从93.74回落至91.87，约-1.99%。早欧时段WSJ记录Brent约105.50、WTI约92.58，方向一致。这是中国收盘后对国内油品强势的反证，不代表中国期货已交易该信息。[WSJ，2026-10-13](https://www.wsj.com/finance/commodities-futures/oil-futures-decline-on-possible-technical-correction-a4fa2f4b)
- Reuters在16:58 BJT附近记录现货金4186.91美元/盎司、+0.4%，现货银60.4481、+0.2%；仓库19:12 COMEX代理金4205.3、银60.53。金银相对中国日盘分化，且DXY在18:01 BJT约102.33、-0.25%，美元边际回落。[Reuters，2026-10-13](https://www.reuters.com/world/india/gold-eases-firm-dollar-spotlight-us-inflation-data-2026-10-13/) [MarketWatch DXY](https://www.marketwatch.com/investing/index/dxy)
- LME铜仓库值14638美元/吨，较前一可比值约14812低约1.17%；CU2611日盘仅小涨，昨夜/今晨铜突破多头条件没有获得海外延续。USD/CNH缺少同口径、同截点可靠输入，人民币作用只能标“未确认”，不能为境内价格变化编精确归因。

## 三、商品仪表盘（展示12项；实际扫描77品种）

1D/5D均为当前具体合约结算收益；curve为近月减次近月期货价差率，不是现货基差。Night缺失写“missing”，不写0。

| 板块 | 品种/具体合约 | 10/13 close/settle | 1D/5D | Volume/OI/ΔOI | EOD curve | Basis/Physical | 早前Night与Day | 15:00后海外 | Options | 21:00/下一信号 |
|---|---|---:|---:|---:|---|---|---|---|---|---|
| 油品 | LU2612 | 5940/5965 | +6.37%/+12.23% | 169614/78533/+13678 | LU2611-LU2612 +4.41%，backwardation | Physical missing | exact Night missing；不可分解 | Brent/WTI约-1.8%/-2.0%，反对 | 10/9无LU series；E=N | 偏低/高波动；首跳不追，等30分钟 |
| 油品 | FU2701 | 4608/4649 | +3.96%/+16.40% | 281392/178952/+6667 | FU2611-FU2612 +8.01%，backwardation | 现货7612.5；C级basis，仅context | exact Night missing | 原油回落，方向反对 | 10/9 S=Y/P=N/E=N | 偏低；等30分钟看4600与curve |
| 原油 | SC2612 | 727.9/732.0 | +3.17%/+7.44% | 58856/27036/+2046 | SC2611-SC2612 +2.91%，backwardation | Physical missing | exact Night missing | Brent104.74、WTI91.87，反对 | 10/9 S=Y/P=N/E=N | 偏低；等30—45分钟，Brent须重回105.5 |
| 化工 | BZ2611 | 9685/9524 | +2.36%/+10.54% | 121529/28047/+6812 | BZ2610-BZ2611 +8.11%，z=+1.11 | missing | DCE query_error；不可分解 | 原油回落为成本/情绪反证，非exact映射 | DCE skipped | 等45分钟；站稳9758再研究 |
| 畜牧 | LH2701 | 10605/10685 | -2.60%/-5.69% | 115309/171226/+9703 | LH2611-LH2701 -4.63%，contango | missing | 制度无可用Night记录 | 无exact海外锚 | DCE skipped | 无夜盘；10/14 09:30等30分钟 |
| 新能源 | LC2701 | 107060/105480 | -3.12%/-11.76% | 314846/422392/-6647 | LC2610-LC2611 -0.62%，contango | 现货111000；C级basis +5520 | 制度无有效Night | 无exact海外锚 | 10/9 S=Y/P=N/E=N | 无夜盘；10/14 09:45，不接飞刀 |
| 有色 | CU2611 | 110990/110900 | +0.12%/+1.46% | 70492/195710/+561 | CU2610-CU2611 +0.60%，轻backwardation | 现货111481.67；C级basis +581.67 | exact Night missing | LME铜14638、约-1.17%，反对 | 10/9 S=Y/P=部分/E=N | 偏低；旧突破条件取消 |
| 贵金属 | AG2612 | 14743/14688 | -1.12%/-1.46% | 232041/284275/-3783 | AG2610-AG2611 -0.50%，contango | missing | exact Night missing | 国际银约60.45—60.53，小涨 | 10/9 S=Y/P=N/E=N | 内外冲突；等30分钟，不追空 |
| 橡胶 | BR2612 | 16045/16065 | -2.22%/+5.59% | 76661/65687/+3467 | BR2610-BR2611 +3.02%，z=+2.25 | missing | exact Night missing | 无exact丁二烯锚 | 10/9 S=Y/P=N/E=N | 价跌仓增但curve反对追空；等45分钟 |
| 建材 | SA701 | 961/975 | -2.01%/-3.75% | 1179690/1375850/+93033 | SA610-SA611 -0.95%，contango | 现货1064.29；C级basis +89.29 | SA610夜收954，不同合约不可比 | 无exact海外锚 | 10/9 S=Y/P=部分/E=N | 21:00等30分钟；确认SA701而非SA610 |
| 豆类 | A2701 | 5526/5508 | +0.18%/+6.54% | 229922/289573/+30978 | A2611-A2701 -0.82%，contango | missing | DCE query_error | CBOT豆1282.25，仅context | DCE失败 | 无夜盘；10/14 09:45看contango |
| 航运 | EC2611 | 2735/2761.5 | -0.52%/-3.83% | 12242/20815/-1281 | EC2610-EC2611 -20.73%，deep contango | 运价exact口径missing | 制度无可用Night | 无同口径运价更新 | 无可用series | 无夜盘；10/14 09:45，不抄底 |

## 四、相比上一交易日/今晨真正变化

1. **油品链成为全市场最强，但新信息冲突加剧**：LU/FU/SC结算分别+6.37%/+3.96%/+3.17%，同时backwardation与OI上升；但中国收盘后Brent/WTI约回落1.8%—2.0%。因此“价格—量仓”和“曲线”支持继续偏多，“境外定价”明确反对，不能把中国日盘涨幅机械外推到今晚。
2. **纯苯取代铜成为最强研究异常之一**：BZ2611 1D +2.36%、5D +10.54%，OI单日+6812、curve +8.11%；但DCE Night、期权、实体和参数均缺，支持仍只有两层，评分上限69。
3. **生猪弱势获得价仓与曲线一致确认**：LH2701 1D -2.60%、5D -5.69%，OI +9703，contango -4.63%。这只是“跌价增仓”归因线索，不证明新空身份；缺实体猪价/出栏/冻品数据，不能升至70+。
4. **旧观点处置**：CU多头要求“CU>111100且LME≥14750”，截至截点CU110990、LME14638，未成立；AG空头要求“AG<14679且银≤60.2”，AG14743、银约60.45—60.53，未成立；MA空头未跌破原3176触发；均取消当晚条件且不假定成交。LC虽收107060，但曲线已从旧backwardation转contango，旧超跌反弹观察降级并到期，不把日线触价当成交。
5. **Stock没有提供更优表达**：紫金H1经营数据支持长期金铜利润通道，但10月12日股价、执行状态与多周期风险指标不完整；宝钢H1利润/现金流下降说明钢铁利润桥受售价、原料、销量和套保共同影响。两者只改变表达比较，不新增Top机会或独立证据层。

## 五、产业链地图

| 产业链 | 方向/最强最弱 | EOD与Night→Day | curve/实体 | 期权/海外 | 公司利润桥 | 最大缺失/置信度 |
|---|---|---|---|---|---|---|
| 原油—燃料油—低硫 | 最强，但外盘反向 | LU/FU/SC日盘强；exact Night不可分解 | 三者backwardation；SC/LU Physical缺 | 10/9旧surface、execution均N；Brent/WTI回落 | 无必要股票表达；直接期货价格发现更纯 | exact Night、库存裂解、当前期权报价；中 |
| 芳烃—纯苯 | BZ最强 | BZ价涨仓增；DCE Night query_error | +8.11% backwardation；无合格实体/加工利润 | DCE期权缺；原油回落仅间接反证 | 未读取化工公司，避免概念映射 | 加工利润、库存、参数；中低 |
| 养殖—饲料 | LH最弱、A偏强 | LH跌价增仓；A价仓同升；无可用Night | LH/A均contango；实体缺 | DCE期权缺；CBOT仅context | 无公司候选，避免猪价跌即等于养殖股利空 | 现货猪价/出栏/饲料成本；中低 |
| 锂—新能源材料 | LC持续弱 | 1D/5D/20D均弱，OI下降；无夜盘 | curve转contango；现货basis C级 | 旧surface不可执行；海外映射缺 | 无当前公司产销/成本验证，股票不优 | GFEX仓单陈旧、当前期权报价；低 |
| 铜—金银 | 铜旧突破失败；金银内外分化 | CU平、AG弱；exact Night缺 | CU轻backwardation、AG contango；basis仅C级 | LME铜回落，国际金银小涨；旧surface | 紫金经营事实支持长期暴露，但股票时点/执行不合格 | 库存、USD/CNH、当前期权面；中低 |

## 六、机会排行榜（研究吸引力，不是胜率或仓位）

本期没有70+候选；所有正式榜候选只有两个有效独立支持层，严格不超过69分。

| 排名/idea_id | 方向/期限/阶段/工具 | 评分（逻辑/赔率/催化/价曲波动/拥挤技术） | 支持层；反证/缺口 | 研究判断｜证据｜执行 |
|---|---|---:|---|---|
| 1 \`COM-E-BZ2611-TIGHT-CURVE-LONG-20261013\` | 条件多；1—5D；等21:45；BZ2611期货 | **68**（18/17/12/12/9） | 支持：①价量仓②curve；反对：油价回落；缺实体、Night、期权、参数 | 存在待验证优势｜部分｜等待触发/待参数 |
| 2 \`COM-E-LH2701-CONTANGO-BREAK-SHORT-20261013\` | 条件空；2—10D；明早验证；LH2701期货 | **66**（18/16/12/11/9） | 支持：①价格/OI②contango；反对：绝对价格已低；缺现货供需、期权 | 存在待验证优势｜部分｜休市/等待10月14日09:30 |
| 3 \`COM-E-LU2612-ENERGY-ELASTICITY-LONG-20261013\` | 条件多；1—3D；等21:30；LU2612期货 | **64**（16/14/12/13/9） | 支持：①价量仓②backwardation；反对：Brent/WTI回落；缺Physical/Night/当前期权 | 存在待验证优势｜部分｜等待触发/待实时外盘 |
| 4 \`COM-M-SC2612-OIL-GAP-LONG-20261013\` | 条件多；1—3D；旧晨报idea延续；SC2612期货 | **61**（15/13/12/12/9） | 支持：①价量仓②backwardation；反对：海外油价跌；缺库存/Physical/当前期权 | 存在待验证优势但下降｜部分｜等待Brent恢复 |

未入正式榜的BR2612空头只有价格/OI一层，backwardation反对，研究吸引力不超过59；LC2701反弹缺支持层，不评分而保留问题清单。

## 七、前三名研究/交易卡

### 7.1 BZ2611纯苯条件多头｜研究卡，非当前可执行卡

- **事实**：close/settle=9685/9524；1D +2.36%、5D +10.54%；volume 121529、OI 28047、ΔOI +6812；BZ2610-BZ2611 curve +8.11%、z=+1.11。DCE Night为query_error，期权与官方参数缺。
- **市场可能隐含/我们的分歧**：市场已计入近端偏紧与能源成本风险；分歧仅在“近端紧张是否仍能穿透油价收盘后回落”。新增支持是价仓和backwardation同步；最强竞争解释是节后补涨/换月和流动性放大，而非实体短缺。
- **最佳表达**：只在当前具体合约BZ2611上做条件线性多头；不以化工股票或旧期权替代。1腿，1手为一个风险单位；参数未确认前不下单。
- **触发/成交情景**：21:45后站稳9758（日内高点技术锚）且BZ2610-BZ2611 backwardation不低于6%。好成交9700、止损9500，TP1/TP2=9950/10200，对应约1.25R/2.50R；中成交9750约0.80R/1.80R；坏成交>9800或跳空>2%放弃。成本、滑点和每手金额因乘数/tick未确认而不编。
- **失效/退出**：收回9524下方或curve降至3%以下逻辑失效；TP1减半、TP2再减，余仓2个交易日未创新高退出；最长5D。最坏情景为夜盘gap、流动性消失、保证金上调；期货止损不构成最大损失封顶。
- **催化/风险预算**：1—5D看油价、纯苯库存/加工利润、装置消息；单次试仓计划损失0.25%—0.50% NAV。需要先核乘数、tick、保证金、限幅、夜盘安排、最后交易日和交割资格。

### 7.2 LH2701生猪条件空头｜明早研究卡

- **事实**：close/settle=10605/10685；1D -2.60%、5D -5.69%、20D -14.59%；volume 115309、OI 171226、ΔOI +9703；LH2611-LH2701 -4.63% contango。无可用Night、实体猪价/出栏/冻品和DCE期权。
- **市场可能隐含/分歧**：市场隐含远期供应宽松；我们只同意趋势和曲线，不同意在缺实体时无条件追空。最强反证是绝对价格已低、政策/收储或现货反弹引发快速修复。
- **表达与窗口**：生猪无本期可验证夜盘，下一有效窗口10月14日09:00；等30分钟。09:30后若反抽10650—10720失败并再次跌破10600，才做LH2701空头。好成交10680、止损10900、TP1/TP2=10350/10050，约1.50R/2.86R；中成交10620约0.96R/2.04R；坏成交<10520直接追空放弃。
- **失效/退出**：日内收回10900或contango收窄至2%以内失效；TP1减半，TP2/第5个交易日清余仓，最长10D。缺乘数/tick/动态保证金/限幅/最后交易日，名义本金、1/2个限幅压力金额和交割参数均标未确认；不得据此即时执行。
- **风险**：计划风险0.25% NAV；压力情景包括政策跳空、涨停、流动性消失和现货基差快速修复。期货最大损失不由结构限定。

### 7.3 LU2612低硫燃料油条件多头｜等待外盘修复

- **事实**：close/settle=5940/5965；1D +6.37%、5D +12.23%；volume 169614、OI 78533、ΔOI +13678；LU2611-LU2612 +4.41% backwardation。中国收盘后Brent/WTI约-1.8%/-2.0%；exact prior Night与Physical缺。
- **市场可能隐含/分歧**：中国市场已计入炼化/航运燃料紧张；我们的分歧是海外回撤可能意味着边际价格弹性已下降，只有Brent恢复和LU不回吐时才值得承担Delta。最强反证是地缘风险溢价快速压缩。
- **参数**：交易所标准10吨/手、1元/吨tick、tick value 10元；按close名义约59400元/手。10月12日结算后限幅16%，一般保证金18%，静态保证金约10692元/手，实际以经纪商为准；单个/两个限幅理论压力约9504/19008元/手，不含连板扩限、滑点和提保。最后交易日2026-11-30、最后交割日12-07；临近11月中旬前主动移仓，不进入交割月风险区。
- **入场与场景**：今晚有通常21:00连续交易窗口，但当前仓库Night字段缺，先等30分钟。只有Brent恢复≥105.5且LU2612在5965上方稳定15分钟：好成交5980、止损5850、TP1/TP2=6150/6350，约1.31R/2.85R；中成交6030约0.67R/1.78R；坏成交>6100或首跳>2.5%放弃。分两批50%/50%，TP1减半。
- **失效/退出**：LU跌破5850或Brent<103.5且30分钟不收回，逻辑失效；第3个交易日未延续则时间退出。持仓风险与SC/FU/BU同因子合并；期货最大损失不封顶。

## 八、商品期权专项

- 最新可读截面为10月9日、不是T日。整体series 185；surface-ready 181、positioning-ready 41、execution-ready 0，bid/ask coverage=0。LU无有效series；FU/SC/LC/CU/AG/BR/SA有旧surface，但均不能代表10月13日IV、skew或当前报价；DCE的BZ/LH/A未覆盖。
- 因标的自10月9日后大幅变化，旧ATM moneyness不可比；本期不报告ATM IV、RR25/BF25、IV-RV或dealer Gamma方向。RV20仅线性参考：LU 46.36%、SC 58.47%、BZ 39.99%、LH 18.07%、LC 44.38%。
- 事件凸性上，油品面对地缘/EIA尾部，CPI影响金银铜；但“事件大”不等于期权便宜。若盘中人工核验目标series、bid/ask、净支出和exercise/delivery后，可研究有限支出看涨价差；当前统一结论仍是：**research only; manual quote and manual confirmation required before execution; no premium quoted**。
- 回避：卖裸Vega、用10月9日旧IV判断10月13日便宜、用OI节点推dealer净Gamma、对DCE缺失链虚构结构。

## 九、21:00夜盘开盘风险地图

严格四层：①10月13日中国EOD；②已完成、归属10月13日的早前Night（重点合约多数缺失，只作质量披露）；③15:00—19:29海外；④尚未发生、归属10月14日的下一Night。

| 品种 | T日EOD | 早前T Night | 海外新增/冲突 | 下一窗口判断 | 首跳/等待 | 最重要确认 |
|---|---|---|---|---|---|---|
| LU/FU/SC | 强涨、价仓同升、backwardation | exact missing | Brent/WTI回落，明显冲突 | 偏低开或高波动，未证明趋势反转 | 不追；30—45分钟 | Brent105.5、LU5965、SC732、curve是否维持 |
| BZ | close接近日高、OI跳升、backwardation | DCE query_error | 原油回落仅间接反证 | 平/低开后再判 | 等45分钟 | BZ9758、curve≥6%、成交/OI |
| CU | 日盘小涨、轻backwardation | exact missing | LME铜回落约1.17% | 偏低开 | 等30分钟 | CU110450/111340、LME14600、USD/CNH |
| AG/AU | 中国银弱金弱；curve偏平/contango | exact missing | 国际金银小涨、DXY回落 | 内外冲突，平开偏分化 | 等30分钟 | AG14512/14815、国际银60.2/61 |
| BR/RU/NR | BR跌、RU/NR弱，曲线分化 | exact missing | 无exact外盘锚 | 平低开、高波动 | 等45分钟 | BR16000、RU20300、NR17220及曲线 |
| SA/MA | SA弱、MA小跌但5D仍强 | 仅SA610有夜值，不能替SA701 | 油价回落对MA间接偏空 | 偏弱，需防反抽 | 等30—45分钟 | SA701 975、MA3193/3278、OI |
| LH/LC/A/EC | 无可验证夜盘窗口 | 不适用/缺失 | 海外映射不足 | 下一实际日盘10月14日09:00 | 等30—45分钟 | LH10600、LC105480、A contango、EC curve |

若21:00开盘gap超过各自日内技术锚或一个有效限幅尺度，所有静态入场价自动失效；不得用收盘前海外数值假装开盘后仍有效。

## 十、未来24h / 7d事件、覆盖核对与台账

### 10.1 未来事件（北京时间）

| 时间 | 事件 | 交易处理 |
|---|---|---|
| 10/14 20:30 | 美国9月CPI；BLS官方定于10月14日08:30 ET发布 | 金银铜与DXY高跳空；数据前减Delta，只有验证报价后才考虑有限支出Vega。[BLS](https://www.bls.gov/cpi/) |
| 10/15 20:30 | 美国PPI/零售销售，具体时点按官方再核 | 油品与贵金属等待首轮15—30分钟，不用旧IV卖波动 |
| 10/16 00:00 | EIA周度石油状态报告；Columbus Day周官方改为10月15日12:00 ET | LU/FU/SC/BU发布前降同因子风险；库存意外不追首跳。[EIA](https://www.eia.gov/petroleum/supply/weekly/schedule.php) |
| 未来1—7日 | OPEC+/IEA、CFTC、USDA/天气、交易所临时参数、油田炼厂/化工装置及地缘消息 | 未确认精确时点者不编日历；油品以有限风险或延迟入场 |
| 公司层 | 紫金/宝钢下一正式披露与10月13日股票价量补齐 | 只在A股开市、证券状态与成本可核后比较；旧半年报不是新催化 |

### 10.2 覆盖核对

| 板块 | 应覆盖 | 实际取得且分析 | 数据不足 | 不适用/流动性不足 | 未入榜最重要异常/无异常依据 |
|---|---:|---:|---|---|---|
| 黑色建材 | I/JM/J/RB/HC/FG/SA/SF/SM（9） | 9/9价格量仓curve | DCE参数/期权；多数实体不合格 | 0 | SA跌价增仓但Physical仅C级；JM 5D强而20D仍弱 |
| 有色贵金属 | CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG（12） | 12/12 | exact Night、当前期权、部分实体 | 0 | 铜旧多条件失败；金银内外冲突，无优势 |
| 能源化工 | SC/FU/LU/BU/LPG(PG)/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP（21） | 21/21，LPG按引擎PG映射 | SC/LU Physical；多数Night/期权/参数 | 0 | LU/FU/SC/BZ最强；BR价跌仓增但backwardation反对追空 |
| 新能源 | LC/SI/PS（3）及动态GFEX | 3/3并扫描PD/PT等 | GFEX仓单陈旧、当前期权报价 | 0 | LC 20D -25.50%，但无实体确认，不抄底亦不追空 |
| 农产品/畜牧 | A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK（17） | 17/17 | DCE Night/期权、实体与exact外盘 | 0 | LH最弱；A量仓强但contango和海外不确认 |
| 航运 | EC（1） | 1/1 | 同口径运价与期权 | 无夜盘 | deep contango但缺反转/实体证据 |
| 动态新增 | 引擎总77品种 | 77初筛、72可比分析 | JR/PM/RI/WH/ZC | 5 | PL/PD/PT/BZ等保留扫描；不因未入榜消失 |

策略类别已扫描方向、curve/跨期、基差、跨品种/跨市场、产业链RV、中性组合、IV/skew/term/event convexity；1D/3D/5D/20D均仅用同合约历史。基差套利和跨市套利因品质/税费/运费/时点不齐不适用；股票仅作利润桥比较。

### 10.3 旧观点与输入版本

- \`COM-E-CU2611-LME-BREAKOUT-LONG-20261012\`：上次等待触发；当前条件失败，状态改为取消/观察，不假定成交。原因：价格与海外变化。
- \`COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012\`：双触发未成立，取消当晚条件。原因：价格变化。
- \`COM-E-MA701-POSTSPIKE-REVERSAL-SHORT-20261012\`：未跌破3176，继续仅背景，不重置触发。原因：触发未到。
- \`COM-E-LC2701-OVERSHOOT-REBOUND-WATCH-20261012\`：curve转contango，旧观察到期并降级。原因：新数据/观点修订。
- \`COM-M-SC2612-OIL-GAP-LONG-20261013\`：中国价格支持，但Brent跌破105.5外盘条件；降至61分等待恢复，不假定晨间成交。

输入版本：Global Radar前序为10月13日晨报及10月12日晚报；商品引擎commit \`9eb28ae…\`；Stock commit \`6767837…\`。Night exact-contract缺口、当前期权和动态参数只限制相关工具，不抹掉早期方向异常。

风险预算：单一试仓计划最大损失NAV 0.25%—0.75%，确认交易0.75%—1.50%，同一高确信主题总预算≤2.5%—3.0%；LU/FU/SC/BZ属于同一能源因子，必须合并。计划止损不是保证最大亏损。压力测试一个/两个涨跌停、相关性断裂、流动性消失、夜盘gap、保证金提高、IV跳升/塌陷、交割挤压、人民币急变及中国休市期间海外大动。

A. 今晚没有应立即建立的新仓位。
B. 今晚仅应挂条件的候选：BZ2611站稳9758且curve≥6%；LU2612须Brent≥105.5并守住5965，均需等21:30—21:45与参数确认。
C. 今晚继续观察：SC2612外盘修复、LH2701明早10600破位、CU/AG内外盘冲突、LC2701 curve与实体是否重新确认。
D. 今晚必须回避或有条件退出：油品首跳追多、缺DCE参数或当前期权报价的下单、旧CU/AG/LC条件单；若此前按条件建立且触发各卡失效位，应退出而非摊薄。
