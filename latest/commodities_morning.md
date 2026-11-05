# 商品期货期权晨间雷达｜2026-11-06

> 生成时间：2026-11-06 07:09:57（北京时间）｜信息截点：07:09:57｜中国最新完整EOD：2026-11-05｜当前夜盘归属交易日：2026-11-06｜研究用途，不下单，不假定成交或持仓。

## 1. 一句话结论

**截至本报告时点，无可立即执行的合格新交易；风险只值得留给SC回踩确认多、SN反弹失败空与CU近远月价差多，均须等待09:15后的顺序触发。**

最有价值的待验证观察：① SC2612能否在Brent 98美元上方背景下守住636—640并重夺642；② SN2612的国内夜盘跌幅是否在LME锡46,995美元/吨附近得到延续；③ CU2612/CU2701价差能否在850—900元/吨回踩后重新走强。下一真实交易窗口为2026-11-06 09:00中国日盘，首个合格确认窗口09:15。优势不足：EC、JM；条件未到：SC、SN、CU；关键数据不足：全部期权执行、EC即期运价、Stock当前交易能力。

## 2. 数据质量、覆盖与事实台账

| 模块 | 实际取得 | 能力判断与局部缺口 |
|---|---|---|
| Futures | 五所2026-11-05；806合约、77品种；SHFE 238、INE 63、DCE 214、CZCE 243、GFEX 48；source-date-match 100%，full_market_ready=true，critical=0 | 四个OHLC占位已排除强排序；vendor全市场就绪不等于交易所全字段认证 |
| Market State | 77品种、同准确合约20个交易日；1/3/5/20日、RV、量仓与曲线 | 主力换月不拼接；AG roll=true；部分曲线仅2个观测，不给z |
| Physical | 目标20、取得18、fresh 18、unavailable 2 | 18条basis均C级、A/B=0；CZCE仓单3条当前，GFEX LC/SI仓单沿用2026-09-01且stale；仅作背景 |
| External | 目标22、取得17、fresh 17，均context_only | repo油价与独立结算价存在合约/时点差；DXY、USD/CNH、实际利率等5项未取得；不做跨境套利 |
| Night | trading_date=2026-11-06；start=11-05、end=11-06；状态生成05:59:29，selected 806、night 420、outside 166、no-trade 6、query_error/unresolved 214，coverage 52.1092%，complete=false | 日历归属正确，无calendar_mismatch；但`data/night_session/latest.json`为空，和published/validated标签冲突。重点合约仅用准确合约延迟快照fallback；不称交易所最终夜盘收盘，official_night_close_verified=false |
| Options | 2026-11-05；1056记录；目标64、成功45（70.31%）；series 45；core ATM 44、skew 26；OI覆盖97.06%，bid/ask 0 | collection=core_v1，analytics=sampled_strikes；full-chain=false，surface/positioning/execution均0；局部IV/skew可研究，所有结构须人工询价 |
| Metadata | 806合约；contract match 67.49%，effective 73.45%；乘数/tick/保证金/限幅原生覆盖约30.15% | SC动态保证金/限幅另由INE公告核实；CU/SN当前动态保证金、限幅未完整取得，执行降级 |
| Official crosscheck | SHFE 238、INE 63、CZCE settle/pre-settle 243及close 186、GFEX 48均无价格差异；DCE HTTP 412 | state=partial、all_equal=false来自DCE source error，不代表已观察价格差；量/OI未被官方交叉核对 |
| Stock | last valid 2026-10-30，5571行情；11-05 backfill因iFinD 401设备限制失败 | 复权、行业、tradability未就绪；限定检索中国海油、紫金矿业、中远海控，10-31后未取得改变商品结论的经营新增；股票不具即时执行条件 |

全范围动作前覆盖：应覆盖原63代码并动态纳入PD/PT/PL/BZ/LG/OP等，实际分析77品种；黑色、金属、能源化工、新能源、农产品、航运全部完成价量/曲线初筛。板块未入榜依据：黑色仅JM价仓与夜盘偏强、实体basis不合格；金属异常集中在SN夜跌、CU曲线与AG回落；能化EOD极端下跌后夜盘分化；新能源LC/PS波动大但实体仓单陈旧；农产品AP强但无夜盘与赔率确认；EC仍弱但准确2612/2701远月升水仅148.5，未达旧条件。

### 关键事实台账

| fact_id | 标的/口径 | 观测、known_at与实际读取 | 支持判断 | 局限/来源 |
|---|---|---|---|---|
| F-CN-EOD-1105 | 五所806合约，CNY原生单位，close/settlement | 观测2026-11-05 EOD；引擎生成2026-11-06 06:05:56；读取约06:40 | 中国日盘全市场横截面与准确合约基准 | 四个占位；[root status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)、[futures](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json) |
| F-NIGHT-STATUS-1106 | 2026-11-06交易日夜盘状态 | start 11-05、end 11-06；生成05:59:29；读取约06:40 | 日历归属合法、批次仅部分覆盖 | 明细文件为空，不能由published推导逐合约就绪；[status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/night_session/last_run_status.json) |
| F-SC-NIGHT-1106 | SC2612 639.8，SC2701 632.8，CNY/bbl，最新成交快照 | 02:30 BJT；读取约06:55 | SC相对EOD close +2.483%、相对settle +0.219%；价差7.0/1.106% | 第三方延迟快照，不是官方结算；[exact-contract page](https://www.9qihuo.com/hangqing?heyue=sc2702)、[SHFE/INE delayed market](https://www.shfe.com.cn/eng/Market/) |
| F-METAL-NIGHT-1106 | CU2612 104,950；SN2612 343,040；CNY/t，最新成交快照 | CU/SN 01:00 BJT附近；读取约06:55 | CU相对close -1.372%但2612/2701价差约930；SN相对close -4.018% | OHLC/量仓为供应商范围，非已核纯夜盘；[delayed market list](https://www.9qihuo.com/hangqing) |
| F-OPT-1105 | 45个局部series，EOD IV/Delta样本 | 观测11-05；生成11-06 06:06:40；读取约06:45 | SC/SN/CU局部ATM与合格skew研究 | bid/ask=0、execution=0；[quality](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/quality_latest.json)、[surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json) |
| F-OIL-EXT-1105 | Brent 98.29、WTI 90.52，USD/bbl结算 | 11-05美国收盘，报道更新11-05 UTC；读取约07:00 | 油价风险溢价反弹，支持SC空头旧逻辑降级 | repo外部值Brent 99.15/WTI 91.20，存在合约或时点差；[Reuters](https://www.reuters.com/business/energy/oil-falls-fourth-day-expectations-lower-risk-iran-war-escalation-2026-11-05/) |
| F-LME-1105 | LME 3M铜14,011、锡46,995，USD/t | 11-05官方closing；读取约07:00 | 海外铜锡锚；SN国内跌幅明显更大 | 不与中国夜盘完全同一时点；[LME closing prices](https://www.lme.com/market-data/reports-and-data/lme-closing-prices) |
| F-STOCK-1030 | A股5571行、trade_date 10-30 | research_asof 10-31 10:37 BJT；11-05刷新失败；读取约07:02 | 只能做利润桥背景 | 当前报价/交易状态不明；[Stock status](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/last_run_status.json)、[manifest](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/manifest.json) |

## 3. 10项市场仪表盘

| 品种/准确合约 | EOD close/settle | 1D / 5D；RV20 | 量仓/曲线 | 已核夜盘快照（vs close / settle） | Physical/Options/海外 | 信号 |
|---|---:|---:|---|---|---|---|
| SC2612 | 624.3 / 638.4 | -5.59% / -3.84%；45.50 | EOD ΔOI -4,271；2612-2701 7.8=1.237% | 639.8，+2.483% / +0.219%；02:30；价差7.0=1.106% | 无A/B实体；ATM640 IV70.02、RR25 -5.86；Brent结算98.29 | 回踩确认多，禁追高 |
| SN2612 | 357,400 / 353,520 | +0.57% / -4.87%；28.33 | EOD ΔOI -6,022；EOD近曲线+1.607% | 343,040，-4.018% / -2.964%；01:00 | ATM355k IV37.59、RR25 -7.30；LME锡46,995 | 等反弹失败空，不追跌 |
| CU2612 | 106,410 / 106,320 | +0.08% / -0.89%；11.04 | EOD ΔOI +12,204；2612-2701 close价差850 | 104,950，-1.372% / -1.289%；01:00；同刻价差约930 | C级basis；ATM106k IV17.13；LME铜14,011 | 只做曲线相对强弱 |
| AG2702 | 12,743 / 12,629 | +4.99% / -4.92%；40.10 | roll=true；ΔOI +10,633；2611/12曲线z 2.86 | 12,631（02:14），-0.879% / +0.016%；2612-2702约-37 | ATM12,600 IV46.17；skew未ready；COMEX银约52附近 | 旧多失效，观察 |
| MA701 | 3,153 / 3,234 | -4.94% / -0.72%；43.94 | ΔOI -77,221；近曲线z 2.13 | 3,179，+0.825% / -1.701%；23:00；701/702=97 | C级basis；MA612 ATM IV51.79、RR25 -6.10 | 价差扩大，压缩暂缓 |
| JM2701 | 1,406.5 / 1,395 | +2.20% / +3.27%；29.52 | ΔOI +28,050；近曲线+3.792% | 1,418.5，+0.853% / +1.685%；23:00 | C级basis；DCE官方crosscheck缺失 | 相对强，但证据仅两层 |
| FU2701 | 4,112 / 4,307 | -10.06% / -9.35%；62.01 | ΔOI -33,985；近曲线+4.829% | 4,240，+3.113% / -1.555%；23:00 | C级basis；ATM IV73.23 | close/settle错位，禁误写夜涨 |
| LU2701 | 4,877 / 4,997 | -8.21% / -6.58%；50.78 | ΔOI -8,398；近曲线+3.742% | 5,083，+4.224% / +1.721%；23:00 | 无A/B实体；Brent反弹 | 高波动，赔率不足 |
| EC2612 | 2,430 / 2,389 | -1.81% / -7.43%；45.43 | ΔOI +893；EC2701-2612 close远升水148.5=6.11% | 制度无夜盘 | 即期运价未更新；无期权第五层 | 旧≥180条件未到 |
| AP701 | 5,841 / 5,689 | +0.82% / +6.17%；31.29 | ΔOI +1,351；近曲线+6.400% | 制度无夜盘 | ATM5700 IV34.37、RR25 -5.21；无A/B实体 | 观察，不追涨 |

## 4. 相比前序真正变化与旧观点处置

1. **SC旧空未触发且退出研究优先级。** 旧v6要求反弹630—638后15分钟跌破628、再反抽失败；夜盘最低628.2，未完成跌破，快照回到639.8。无成交回执，实际持仓仍未知；不得回填盈利。新方向另建子idea，不覆盖父idea。
2. **AG回撤多的原逻辑失效。** 旧计划要求12520守住、COMEX银≥52.5后重夺12640；AG2612夜低12400穿过12500失效线，且2702快照12631。旧v2退休，不下移止损。
3. **MA数据纠错再纠正。** 昨晚把MA702视作无效腿属于数据纠错错误；本次EOD与夜盘均确认MA702有效，恢复父idea `COM-C-MA701-702-BACKWARDATION-COMPRESSION-20261104`。但701/702 close价差由66扩大到夜盘97，属于反对压缩的新价格证据。
4. **CU出现“价跌、曲线强”。** CU2612夜盘较close跌1.37%，但同刻2612/2701价差约930，高于EOD 850；这是期限相对强弱，不推断新空或回补。
5. **SN国内跌幅超过海外锚。** SN2612较EOD close跌4.02%，LME锡官方收46,995；国内延续还是过度反应要靠09:15后的反弹失败区分。
6. **期权局部能力显著恢复。** 相比前晨19/64，本次成功45/64、ATM 44、skew 26；第五层可局部使用，但0个series执行就绪，不能把旧EOD IV当09:00权利金。

## 5. 产业链与传播路径

1. **中东运输风险→Brent/WTI→SC→LU/FU/BU。** 海外油价结算反弹、SC夜盘回补日盘跌幅，最强为LU相对close +4.22%，最弱为FU相对settle仍-1.56%。库存、炼厂利润和可比现货均缺，置信度中等。中国海油利润桥：售价上升利好但销量、套保、税费与传导滞后会削弱弹性；10-31披露有套保事项，故股票不如SC表达纯，且当前交易状态未核。
2. **LME铜/锡/贵金属→CU/SN/AG。** CU夜盘下跌而近远月价差扩大；SN国内跌幅大于LME锚；AG旧多被失效线否定。紫金矿业同时暴露金铜、产量与成本可缓冲单一价格，且11-05仅见债券上市信息而非经营新增，股票不是更优短周期表达。置信度中等。
3. **原油/煤→MA/PX/TA/EG/EB→下游聚酯塑料。** EOD广泛下跌，MA夜盘相对close反弹但701/702 backwardation更陡；18条basis全为C级，不能把现货绝对值写成套利。置信度中低。
4. **焦煤→焦炭→钢材/铁矿。** JM EOD与夜盘偏强、量仓上升，但basis C级且DCE官方接口未核完；RB/HC没有同强度确认。最强JM、最弱钢材，置信度中低。
5. **红海/运力→SCFIS→EC→中远海控。** EC 5D -7.43%、远月仍升水，但即期SCFIS未取得新日更；中远海控没有10-30后经营新增，股票包含运量、成本、汇率与船队资本开支，不能替代EC。置信度低。

## 6. 统一机会榜（研究优先级，不是胜率）

| 排名/idea_id | 方向/期限/工具 | 逻辑25 | 赔率25 | 催化20 | 价曲波15 | 拥挤15 | 总分 | 五层证据 | 研究/证据/执行 |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 `COM-M-SC2612-OVERNIGHT-REBOUND-CURVE-HOLD-LONG-20261106`（父：SC旧空） | 条件多，1—3D，SC2612 | 20 | 17 | 16 | 12 | 8 | **73** | 支持1/2/4；反对5（put skew已贵）；缺3 | focus / 3层 / 等09:15 |
| 2 `COM-M-SN2612-LME-DIVERGENCE-FAILED-BOUNCE-SHORT-20261106` | 条件空，1—5D，SN2612 | 19 | 16 | 14 | 13 | 8 | **70** | 支持1/4/5；反对：已跌4%、skew贵；缺2/3 | focus / 3层 / 等反弹失败 |
| 3 `COM-M-CU2612-2701-CURVE-RESILIENCE-LONG-20261106` | 多近空远，3—10D，1:1价差 | 18 | 16 | 14 | 11 | 9 | **68** | 支持1/2；反对4（外盘铜弱）；缺3/5方向 | watch / 2层上限 / 等价差回踩 |
| 4 `COM-E-JM2701-BACKWARDATION-CONTINUATION-20261105` | 偏多，3—10D，JM2701 | 17 | 15 | 13 | 11 | 9 | **65** | 支持1/2；Physical C、Options缺 | watch / 2层 / DCE核对缺失 |
| 5 `COM-E-EC2612-FAR-PREMIUM-REBOUND-FAILURE-SHORT-20261105` | 条件空，5—20D，EC2612 | 16 | 14 | 12 | 10 | 8 | **60** | 支持1/2；缺3/4/5 | watch / 2层 / 即期与≥180条件未到 |

## 7. 完整研究/交易卡（均非立即执行）

### 卡1｜SC2612条件多（新子idea，父空头保留历史）

- **新增事实/定价/分歧：** EOD close 624.3、settle 638.4；夜盘快照639.8，较close +2.483%但较settle仅+0.219%，2612/2701价差1.106%。Brent结算98.29；市场已部分计入风险溢价回归。分歧是假设若SC日盘守住曲线与Brent锚，日盘close过度下压仍可修复；最强竞争解释是close-settle错位已制造假反弹。
- **顺序触发：** 2026-11-06 09:15后，先回踩636—640且15分钟不收于632下方 **AND** 同时SC2612-SC2701价差≥1.00% **AND** Brent可靠同刻价≥98.0；随后15分钟重夺642。直接高开≥650、Brent<96.5或价差<0.80%放弃。
- **分批/风险：** 640/642/644各30%/30%/40%；计划止损632，逻辑失效为15分钟<632或Brent<96.5或曲线<0.8%；TP1 660、TP2 680；时间退出2026-11-10 22:45 BJT。每手乘数1000桶、tick0.1、tick价值100元；费用滑点情景500元/手。好/中/坏入场净R：TP1 2.29/1.67/1.24，TP2 4.65/3.57/2.84。
- **参数/压力：** SC2612最后交易日2026-11-30；夜盘至02:30。INE已公告SC2612/2701限幅±18%、一般持仓保证金20%。以642入场、前结638.4的一次跌停523.4，单手压力约-118,600元；若次日再按18%下移至约429.2，累计约-212,800元，远超计划止损，故本主题试仓≤NAV 0.35%、确认≤0.75%、总风险≤1.5%。止损不保证最大损失。
- **期权替代：** SC2612、到期2026-11-12、ATM640、IV70.02、RR25 -5.86，仅局部EOD研究；bid/ask缺失，不报权利金/Greeks/净成本，不称限损结构可执行。

### 卡2｜SN2612反弹失败空

- **新增事实/定价/分歧：** EOD close 357,400、settle 353,520；夜盘快照343,040，较close -4.018%。LME锡官方3M closing 46,995美元/吨。SN局部ATM355,000 IV37.59高于RV28.33，RR25 -7.30显示下侧已昂贵。分歧不是追空，而是只有国内反弹失败才证明弱势仍未充分释放；竞争解释是国内夜盘已过度反应，日盘可能均值回归。
- **顺序触发：** 09:15—10:00先反弹344,000—346,000，随后15分钟收回343,000下方 **AND** LME锡可靠同刻≤47,000；直接开盘≤340,000、LME锡>47,800或无法取得同刻外盘则放弃。
- **分批/风险：** 343,000/342,000/341,000各30%/30%/40%；计划止损351,000，逻辑失效为15分钟>351,000或LME锡>47,800；TP1 330,000、TP2 318,000；时间退出11-12 14:45。乘数1吨、tick10元、tick价值10元；成本情景200元。TP1净R 1.56/1.28/1.06，TP2 3.02/2.59/2.24。当前动态保证金/限幅未核，无法给可靠1/2涨跌停金额，只能按`手数×1吨×实际限幅价差`压力计；因此not execution-ready。
- **期权替代：** 2026-11-24到期局部series可研究put spread，但下侧skew已贵且无bid/ask；仅研究，执行前人工询价与确认，不提供未经验证的权利金。

### 卡3｜CU2612/CU2701 1:1多近空远价差

- **新增事实/定价/分歧：** EOD close价差850元/吨；01:00同刻快照约930。CU2612较EOD close -1.372%，LME铜官方close 14,011美元/吨。市场已计入外盘弱势，但近月相对远月更抗跌；分歧在期限而非方向。竞争解释是交割/roll与时点差制造暂时价差，且C级basis不能验证真实紧张。
- **顺序触发：** 09:15后价差先回踩850—900，15分钟不收于800下方，随后重夺900；同时CU2612不低于103,800，且两腿同刻有可成交深度。直接价差≥1,050不追、<800或LME铜<13,800放弃。
- **分批/风险：** 1:1多CU2612/空CU2701，价差900/925/950各30%/30%/40%；价差止损750，TP1 1,400、TP2 1,700；时间退出11-20 14:45或进入交割月前滚动。每腿乘数5吨、tick10元、单腿tick价值50元；双腿成本情景100元/组。TP1净R 2.82/2.33/1.95，TP2 4.59/3.87/3.32。CU2612/2701最后交易日分别12-15/01-15；夜盘至01:00。动态保证金/限幅未完整核实；两腿相关性断裂、单腿流动性消失、保证金同步上调为主要压力，计划止损不封顶。
- **期权替代：** CU2612 ATM106,000 IV17.13、RV11.04，但skew未ready、执行未ready；不以“IV>RV”直接判贵或便宜。

规模统一公式：`手数=floor(NAV×专属风险预算/每手计划风险)`；若结果<1则不做。相关金属主题SN+CU合并试仓≤NAV 0.50%、确认≤1.0%、主题总≤1.5%。

## 8. 商品期权专项

- 样本为2026-11-05 EOD、core_v1/sampled_strikes；45/64产品、1056合约，ATM 44、skew 26、surface/positioning/execution均0。quote_coverage_complete只表示计划样本完成，不是全链。
- 合格局部：SC2612 ATM640 IV70.02 vs RV45.50、RR25 -5.86；SN2612 ATM355k IV37.59 vs RV28.33、RR25 -7.30；AU2612 ATM880 IV21.81 vs RV19.58、RR25 -0.12；AP701 ATM5700 IV34.37 vs RV31.29、RR25 -5.21；MA612 ATM3350 IV51.79 vs MA主力RV43.94，但underlying不同，不能直接当同合约IV-RV套利。
- 仅ATM：AG2702 IV46.17 vs RV40.10、CU2612 IV17.13 vs RV11.04、LC2701 IV51.63 vs RV43.38、FU2701 IV73.23 vs RV62.01；skew未ready。
- BU2612 BF25=-51.34波动点违反通常解释，隔离为异常，不用于结构。单一到期不能外推term，样本OI不能推PCR/crowding/dealer gamma。
- 所有期权结构统一边界：**research only; manual quote and manual confirmation required before execution; no premium quoted**。美国就业前若已有非线性风险，只能讨论Delta/Vega方向；无报价不新增结构。

## 9. 09:00开盘风险地图

| 三层输入 | 潜在开盘 | 追价/套保 | 15/30/45分钟检查 |
|---|---|---|---|
| SC/LU/FU/BU：EOD大跌；合法夜盘SC、LU反弹；Brent 98.29 | SC/LU偏高开，FU受close/settle错位影响不确定 | 不追SC≥650；已有产业套保需求需按现货敞口，不把研究候选当对冲指令 | 09:15看SC 636—640与曲线；09:30看Brent同刻；09:45才允许顺序触发 |
| SN/CU/AG：EOD金属分化；夜盘SN/CU下跌；LME铜锡closing可比时点不同 | SN、CU偏低开，AG近平/低 | SN≤340k禁追空；CU只做价差 | 09:15反弹/价差；09:30外盘锚；09:45看第二次15m确认 |
| JM/黑色：EOD与夜盘JM偏强；Physical仅C级 | JM偏高开、钢材未必跟随 | 不把JM OI上升写成新多 | 09:15看JM是否守1400；09:30看I/J/RB同步；09:45无同步则降级 |
| EC/AP/LC：无夜盘 | 主要由日盘订单流决定 | EC旧条件远升水≥180未到；AP/LC不追跳空 | 09:15仅观察；09:30核成交与准确合约；09:45才评估结构 |

## 10. 未来24h / 7d事件与Stock联动

- **11-06 21:30 BJT：美国10月就业报告。** 美元、实际利率、黄金/白银、铜与油可能跳变；线性仓需把时间退出与宏观窗口错开，期权仅在取得真实净支出后才能讨论有限损。[BLS日历](https://www.bls.gov/schedule/2026/11_sched_list.htm)
- **11-07 04:30 BJT附近：CFTC COT。** 反映周二持仓，不是实时仓位；不得把净仓变化当dealer gamma。[CFTC schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- **11-09：中国10月CPI/PPI（官方日历日期，具体发布时间以公告为准）。** 关注农产品、黑色与化工需求预期。[NBS 2026 calendar](https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html)
- **11-10 21:30 BJT：美国10月CPI；11-10 EIA STEO。** 油、贵金属与工业金属的Delta/Vega均可能重定价；STEO准确北京时间待官网更新。[BLS](https://www.bls.gov/schedule/2026/11_sched_list.htm)、[EIA STEO](https://www.eia.gov/outlooks/steo/release_schedule.php)
- **11-12/13：EIA周度石油报告因Veterans Day延后，官网列11-12 12:00 ET（北京时间11-13 01:00）。** SC主题跨该窗口必须缩小线性风险。[EIA WPSR schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **USDA WASDE：** 官网只确认通常每月8—12日中午ET，本次精确发布日期未从日历页取得，标待核，不预置农业事件仓位。[USDA process](https://ers.usda.gov/topics/farm-economy/commodity-outlook/usda-outlook-process)
- **公司公开补证：** 中国海油最新相关经营/套保披露为10-31；紫金矿业11-05债券上市不改变铜金利润桥；中远海控未取得10-30后的经营新增。售价、销量、成本、套保、汇率、库存与资本开支共同决定利润，故三家公司均不优于本期准确商品表达，且Stock当前报价/停牌/流动性未核。[中国海油公告页](https://www.sse.com.cn/assortment/stock/list/info/company/index.shtml?COMPANY_CODE=600938)、[紫金矿业检索](https://www.sse.com.cn/home/search/index.shtml?webswd=%E7%B4%AB%E9%87%91%E7%9F%BF%E4%B8%9A)、[中远海控公告页](https://www.sse.com.cn/assortment/stock/list/info/announcement/index.shtml?productId=601919)

### 发布前实际校验

已重算5项评分及100分上限、SC/SN/CU好中坏净R、SC与CU曲线百分比、夜盘双锚收益；核对11-06夜盘日历归属、三张卡准确合约和最后交易日。未通过/未完成：Night明细为空、CU/SN动态保证金限幅、所有期权bid/ask、EC即期运价、Stock当前交易状态、USDA精确日期。受影响表达均标not execution-ready，其余研究保留。

A. 今天没有应立即建立的新仓位。
B. 今天仅应挂条件的候选：SC2612回踩确认多、SN2612反弹失败空、CU2612/2701价差多，全部等待09:15后完整顺序与同刻外盘/曲线确认。
C. 今天继续观察：JM相对强、EC远月升水、MA701/702价差、AP与LC；不因缺夜盘删除研究。
D. 今天必须回避或有条件退出：回避所有无bid/ask期权执行、追空SN≤340,000、追多SC≥650、BU异常BF；旧SC空v6与AG多v2均未触发且逻辑已失效，不默认存在持仓。

---

归档计划：edition=`commodities_morning`；archive_status写入后回读确认；CI=`pending_or_unverified`。
