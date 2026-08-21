# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-22

> 数据截点：北京时间 2026-08-22 07:04。周末模式。仅用于研究和交易决策支持，不自动下单。中国国内部分使用最近完整交易日 2026-08-21 EOD；China-Commodities-Engine 不生产分钟、逐笔或夜盘 session 数据，本期未取得足够可审计的 8月21日晚中国夜盘终值。仓库晨间 External 尚未完成 8月22日重建/部分滞后，因此隔夜海外层使用公开实时/收盘来源补充。下文“9:00开盘”均指下一中国交易日 2026-08-24（周一）09:00。

## 一、今日一句话结论

**商品市场有值得冒险的机会，但今天是周六，没有应立即建立的新仓位；周一优先 FU2611/BU2610 回撤条件多、AG2610 高波动趋势条件多，FG701反弹失败条件空。能源是最强产业链，建材仍最弱。**

## 二、数据质量与覆盖说明

本期第一读取层按 China-Commodities-Engine v2 协议读取 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；为具体合约价格与参数进一步读取 `data/latest.json`、`data/contract_meta.json`。统一输入 `requested_date=2026-08-21`，`generated_at=2026-08-21T19:02:52.405697+08:00`。

| 模块 | 状态 |
|---|---|
| Core Futures | 2026-08-21；SHFE/INE/DCE/CZCE/GFEX五所齐全；`full_market_ready=true`；`source_date_match_pct=100%`；critical errors=0；803合约 |
| Futures质量 | unknown=0；duplicate=0；invalid OHLC=0；placeholder=5；negative volume/OI=0；核心无carried-forward |
| Market State | 同合约1D/3D/5D/20D、RV20、成交/OI z-score、ΔOI、curve可用；主力切换不拼接收益 |
| Physical | 4条已验证：I港口库存(8/19周度)、JM NBS旬度现货(8/10)、FG库存(8/21周度)、TA加工费(8/21周度)。这些序列“fresh”仅指仍在原生频率有效；没有方向变化时只作context |
| Basis | 可推导JM=Spot-Futures，但仅C级、缺交割地/税口径，`eligible_for_physical_score=false`；不得称套利 |
| External repo | 22目标仅6映射、5 fresh、1 stale；Brent/LME Cu/SGX I/USDCNH/DXY为context_only；BMD Palm stale；import parity全部不可执行 |
| External晨间 | 仓库External生成仍是2026-08-21 06:29，整体`data_fresh=false`；这不是中国EOD失败。本期用Reuters/EIA/CFTC/USDA等公开源补充8/21海外收盘与未来事件 |
| Options | 2026-08-21；21,816合约；59/64商品成功，产品覆盖92.19%；368个series中360个`surface_ready`、70个`positioning_ready`、0个`execution_ready`；IV覆盖98.47%、OI覆盖68.74%、bid/ask覆盖0% |
| Options失败 | CZCE AP/CJ/PL/PR/ZC因请求8/21但源报价停在8/20而失败；这些品种期权不计本期fresh证据 |
| Dealer Gamma | `dealer_gamma_direction_known=false`，禁止推断方向 |
| Contract metadata | `quality_state=partial`；match coverage 67.37%，effective 73.35%；multiplier/tick/margin/limit覆盖29.76%，night session覆盖0%。缺参必须逐项查交易所 |

**数据闸门结论：** 中国核心期货层可用且完整；Physical、跨市场parity和合约参数仍不完整；商品期权“研究级曲面”可用，但没有可执行bid/ask，所以不能给精确权利金、净成本或成交滑点。周末尤其不得把海外8月21日晚变化冒充为中国已实现夜盘变化。

## 三、商品仪表盘（重点11项）

> 价格均为2026-08-21中国EOD，除非另注。curve定义为仓库的近月减次月期货结算，不是现货基差。

| 板块 | 品种/主力 | 收/结算 | 1D结算 | 5D | 成交量 | OI | ΔOI/线索 | curve | Physical/Basis | Options | 信号 |
|---|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| 能源炼化 | **FU2611** | 3845 / 3850 | +2.12% | **+9.81%** | 650,637 | 285,614 | 价格/OI细分仅作归因线索 | Backwardation | 无直接实体层 | ATM IV **43.0%**；RV20 37.93%；surface=Y/position=N/execution=N | **最强条件多，不追gap** |
| 能源炼化 | **BU2610** | 4508 / 4526 | +2.14% | **+7.92%** | 486,111 | 334,627 | price_up_oi_down；ΔOI z=-2.08 | **Back +3.16%** | 无直接实体层 | ATM IV **27.745%**；RV20 23.63%；RR25=-0.61；surface=Y/position=N/execution=N | 多头仍在，但OI下降降级 |
| 能源化工 | **MA610** | 2909 / 2880 | +1.80% | **+8.56%** | 1,957,108 | 873,688 | price_up_oi_up | Back +0.35%，z≈+1.34 | 无直接Physical | surface ready；execution=N | 油链扩散多，但证据弱于FU/BU |
| 黑色建材 | **FG701** | 907 / 906 | **-1.09%** | **-3.10%** | 1,575,371 | 1,601,238 | ΔOI +148,375，price_down_oi_up | **Contango -3.35%** | 最新周度库存7441.4“重量箱”，仅水平context | surface ready；execution=N | **建材弱势，反弹失败可空** |
| 黑色 | I2701 | 707.5 / 707 | +0.14% | — | 202,518 | — | 未作方向性OI结论 | 近月结构需结合仓库state | 8/19周度港口库存15964，单位按源保留 | 11个series surface-ready但position=0 | 中性，缺实体方向变化 |
| 贵金属 | **AG2610** | 16771 / 16611 | **+3.11%** | **+5.45%** | 773,038 | 306,822 | price_up_oi_up；OI change z≈+0.26 | 近月contango约-0.14%，仅4个观测，不计方向确认 | 无高质量basis | ATM IV **47.265%** vs RV20 **30.82%**；RR25 **+7.81 vol**；surface=Y/position=N/execution=N | 趋势强但凸性极贵，优先等回撤 |
| 有色 | CU2610 | 107520 / 107010 | +0.14%结算 | — | 66,412 | — | 不做客户方向推断 | — | 无可执行沪伦进口平价 | ATM IV **14.3%**；RR25 +4.14；position=Y/execution=N | LME squeeze缓和，不追高 |
| 新能源 | **LC2701** | 158680 / 156360 | +2.60% | +1.41% | 225,444 | 353,437 | **ΔOI +31,875/+9.91%**；vol z=2.51 | **Contango -0.30%** | Physical缺失 | surface ready；execution=N | 价格/OI强但curve不确认，观察而非追多 |
| 新能源 | PS2611 | 38430 / 38640 | +1.85% | +0.39% | 114,156 | — | price_up_oi_up | Contango -0.35% | Physical缺失 | surface ready；execution=N | 20D强但短期curve不支持短缺叙事 |
| 农油饲料 | **RM611** | 2238 / 2246 | **-1.36%** | +2.60% | 747,569 | 651,265 | price_down_oi_up | **Back +3.96%** | 无fresh进口平价 | surface ready；execution=N | 价格与curve冲突，不追空 |
| 软商品 | CF701 | 17065 / 17070 | +0.29% | +2.19% | 285,598 | — | ΔOI温和上升 | Contango约-1.58% | 仓单可用但不等于社会库存 | surface ready；execution=N | 中性偏强，非Top机会 |

海外8月21日纽约收盘后最重要的新增信息是：Brent结算94.39美元/桶、WTI 87.06美元/桶，当日分别+0.65%和+0.26%，周涨幅6.39%/5.66%；霍尔木兹商品船通行仍显著低于冲突前，且中国买家可获得的伊朗原油报价下降。能源风险溢价没有消失，但美国页岩油、阿联酋和委内瑞拉等替代供给抑制了“无限上行”叙事。

贵金属进一步加速：8月21日现货黄金约4623.94美元/盎司、+2.4%，现货白银约69.62美元/盎司、+2.3%。这支持AG方向，但AG2610 ATM IV 47.3%已经比RV20高约16.4 vol，且25D call skew很贵；因此“看多”不等于“买裸Call”。

## 四、相比上一期真正变化

1. **中国EOD基线前移到8月21日。** 上一期晨报用8月20日；本期五所核心期货完整更新，避免再用旧EOD推断周一。
2. **FU/BU多头延续，但内部质量发生分化。** FU2611 5D已达+9.81%；BU2610 5D+7.92%、Backwardation仍在，但BU出现“价涨OI降”归因线索，不能再把它描述为干净的增仓上涨。
3. **AG从“高波动观察”升级为方向性强势，但期权更贵。** AG2610 1D+3.11%、5D+5.45%；同时ATM IV47.27%对RV20 30.82%，RR25+7.81，追裸Call赔率变差。
4. **FG重新给出较干净的弱势结构。** 结算-1.09%、5D-3.10%、OI单日明显增加，近月contango约-3.35%；但周度库存只有绝对水平，没有方向变化，Physical仍不能计完整证据层。
5. **LC是最典型“价格强、curve不确认”。** 价格上涨、成交异常、OI+9.91%，但近端仍contango；不能把上涨自动解释成短缺。
6. **Options全市场质量反而从上一期64/64降至59/64。** AP/CJ/PL/PR/ZC的8/21源日期不匹配；Top候选FU/BU/AG/FG/MA本身series仍surface-ready，因此不影响这些候选的波动率研究，但全市场“最高/最低IV”结论应降级为代表样本。

## 五、产业链地图

| 链条 | 方向 | 最强 | 最弱/冲突 | Price/Curve | 实体确认 | Options | 海外映射 | 最大缺失 | 置信度 |
|---|---|---|---|---|---|---|---|---|---|
| 能源/炼化 | **供应风险偏多** | FU、BU | LU/下游裂解未闭环 | FU/BU均有Back确认 | 霍尔木兹物流/伊朗供应风险为外部实体证据；国内库存/炼厂数据缺 | FU/BU IV>RV，买波动不便宜 | Brent/WTI周线强 | 国内夜盘、裂解、炼厂开工、可执行跨境parity | **高** |
| 黑色/建材 | **偏弱** | I相对抗跌 | **FG最弱** | FG价格弱+Contango；I不够弱 | FG仅周度库存水平；铁水/钢厂利润缺 | surface可研究 | SGX铁矿repo只context | 铁水、钢材利润、地产实物、焦化库存 | 中高 |
| 贵金属 | **强趋势+高波动** | **AG** | 期权过贵 | 价格强，curve样本不足 | 无 | AG IV-RV极高、call skew昂贵 | 海外金银继续强，美元周内偏弱 | 中国夜盘终值、可执行bid/ask | 高方向/中赔率 |
| 有色 | 中性偏强 | 铜 | LME squeeze正在缓和 | 中国铜温和上涨 | 无A/B进口平价 | CU曲面ready且OI覆盖完整 | LME库存补入、挤仓缓和 | 精确沪伦比/FX/税运费 | 中 |
| 新能源材料 | **反弹但非短缺确认** | LC | PS短期跟随 | LC price/OI强但contango | 缺 | surface可研究 | 海外锚弱 | 现货、社会库存、排产、成本 | 中 |
| 农油饲料/软商品 | 混合 | CF/RM曲线部分支撑 | BMD palm stale | RM价格与Back冲突 | 进口平价/压榨缺 | 大部surface可用 | Black Sea粮运风险上升 | CBOT/BMD新鲜锚、天气、压榨 | 中低 |

当前Regime：**地缘供应冲击 + 精炼品风险溢价 + 贵金属高波动趋势 + 中国工业需求分化 + 新能源反弹但curve不确认**。这不是广谱商品牛市。

## 六、机会排行榜（最多5个）

| 排名 | 机会 | 分数 | 方向/持有期 | 阶段 | 工具 | Fresh证据层 | 数据惩罚 |
|---:|---|---:|---|---|---|---:|---|
| 1 | **FU2611 周一回撤条件多** | **79** | 多 / 1–5D | 条件试仓 | 期货；期权仅待可执行报价后Call Spread | **4层：1/2/4/5** | 无国内夜盘；Physical缺 |
| 2 | **BU2610 周一回撤条件多** | **77** | 多 / 1–5D | 条件试仓 | 期货；报价确认后Call Spread | **4层：1/2/4/5** | OI下降；Physical缺 |
| 3 | **AG2610 趋势延续但只做回撤/有限凸性** | **75** | 多 / 2–10D | 条件试仓 | 期货回撤；若期权报价恢复优先Call Spread/Call Fly | **3层：1/4/5** | IV明显高于RV；无执行报价 |
| 4 | **FG701 反弹失败条件空** | **72** | 空 / 2–10D | 条件试仓 | 期货；Put Spread仅待报价 | **3层：1/2/5** | Physical只有水平值；财政支持可能挤空 |
| 5 | **LC2701 price/OI强但curve不确认** | **68** | 观察多 / 2–10D | 观察 | 不追；等curve/现货确认 | **2个方向性层+1个冲突层** | 无Physical/海外锚，contango |

评分拆分：FU 23/18/19/11/8；BU 22/17/19/11/8；AG 21/18/18/10/8；FG 20/18/14/11/9；LC 19/16/13/9/11（逻辑/赔率凸性/催化/price-curve-vol/持仓技术）。风险偏好高不改变70分门槛。

## 七、前三名交易卡

### 1）FU2611——周一回撤条件多

**事实：** 8/21收3845、结3850、高3890、低3811；5D+9.81%，RV20 37.93%；曲线为Backwardation；FU2611期权ATM IV 43.0%，surface-ready、positioning not ready、execution not ready。海外Brent/WTI周五继续收高，霍尔木兹物流与伊朗出口仍是供应风险。

**市场定价/推断：** 能源风险溢价已部分进入价格与IV，继续做多的edge来自“供应风险尚未解除且曲线仍紧”，不是赌新闻标题本身。最大错误可能是替代供给快速补位、霍尔木兹恢复、美国/伊朗缓和，导致周末risk premium快速塌缩。

- 最佳表达：**FU2611期货条件多**；若周一期权出现真实bid/ask，再比较Call Spread，禁止按仓库缺失报价虚构净权利金。
- 入场：周一09:45后；若开盘gap≤2%，守住3850并重新突破3890，可分2笔；若gap>2.5%，至少等45分钟，不追。
- 初始止损：跌破3810后15分钟不能收回则减半；硬逻辑保护参考3770下方，同时要求Backwardation明显收窄或海外油价同步转弱。
- TP1/TP2：3970附近/+1R减仓；4080附近/+2R继续减。2个交易日无延续则时间止损。
- 最大损失：初始0.50% NAV；确认后最多1.0% NAV；FU+BU同主题合并初始≤0.75% NAV、确认后≤1.5% NAV。
- 参数：10吨/手；tick=1元/吨，tick value=10元/手；8/21结算名义≈38,500元/手；交易所当前一般保证金16%、涨跌停14%（上期所2026-06-23通知）；券商保证金未确认；FU2611最后交易日按规则为交割月前一月最后交易日，预计2026-10-30，正式下单前复核；实物交割，临近交割月必须提前滚动。
- 压力：以3850计，一板不利约5,390元/手；连续两板复合约10,025元/手。夜盘存在，但本期metadata未提供精确session终止时间。
- 放弃：周末出现明确停火/通航恢复；周一大幅高开后30–45分钟跌破开盘区间低点；Back显著收窄。

### 2）BU2610——回撤条件多，但弱于FU

**事实：** 8/21收4508、结4526、高4575、低4481；1D+2.14%、5D+7.92%、RV20 23.63%；近月Back约+3.16%；但出现price_up_oi_down、ΔOI z=-2.08。BU2610期权ATM IV27.745%，RR25=-0.61，surface-ready但positioning/execution不ready。

**推断：** BU仍受原油风险溢价和曲线支撑，但OI下降说明内部确认已经不如上一期，故评分低于FU。

- 最佳表达：BU2610期货条件多；期权只在可执行报价恢复后考虑Call Spread。
- 入场：周一09:30后；gap≤1.5%，4525附近不失并突破4575再入；gap>2.5%至少等45分钟。
- 初始止损：4480失守后不能快速收回减仓；若4450附近再失守且Back收窄则逻辑失效。
- TP1/TP2：4660 / 4760，或+1R/+2R管理；2个交易日无延续退出。
- 最大损失：0.35%–0.50% NAV；与FU合并计算。
- 参数：10吨/手；现行最小变动价位1元/吨，tick value=10元/手；名义≈45,260元/手；自2026-07-10结算后石油沥青涨跌停10%、一般保证金12%；券商保证金未确认；BU2610最后交易日2026-10-15，实物交割，9月下旬后逐步迁移远月。
- 压力：一板约4,526元/手；连续两板复合约8,599元/手。
- 放弃：周末供应风险显著缓和；周一高开低走跌破4481；价格继续上但OI/curve同步恶化。

### 3）AG2610——方向强，但不要把“看多”翻译成“买贵Call”

**事实：** 8/21收16771、结16611、高16872、低16201；1D+3.11%、5D+5.45%、20D+17.59%、RV20 30.82%；海外8/21现货银+2.3%至约69.62美元/盎司。AG2610期权ATM IV47.265%，IV-RV约+16.45 vol，RR25+7.81 vol，BF25+1.93；surface-ready，但positioning/execution不ready。

**市场定价：** 上行方向被价格与call skew同时反映，裸Call非常容易“方向对、结构错”。

- 最佳表达：若周一报价仍缺失，**只考虑小仓期货回撤多**；若真实bid/ask恢复，优先有限风险Call Spread或Call Fly，不给虚构执行价。
- 入场：等待30–45分钟。gap≤2.5%、16600上方稳定并重新突破16872才试；gap>3%不追。
- 初始止损：16480以下减仓；16200失守且海外银转弱/美元反弹为逻辑失效。
- TP1/TP2：17350 / 17800，或+1R/+2R；3个交易日没有延续则降仓。
- 最大损失：期货试仓0.25%–0.40% NAV；若转有限风险期权，最大净支出≤0.50% NAV。
- 参数：15千克/手；tick=1元/千克，tick value=15元/手；名义≈249,165元/手。最近检得上期所贵金属风控通知为涨跌停14%、一般保证金16%，本期repo参数字段缺失，正式下单前必须再次核验是否有后续调整；预计AG2610最后交易日2026-10-15，实物交割。券商保证金、夜盘精确结束时点本版未确认。
- 压力：若仍按14%限幅，一板不利约34,883元/手，两板复合约64,883元/手。
- 放弃：海外银周末/周日晚明显反转；周一冲高回落跌回16600下方；真实期权报价显示call skew进一步极端扩张。

## 八、商品期权专项

本期不能称“全市场最高/最低IV”，因为59/64品种成功、360/368 series surface-ready；以下仅为**代表样本**。

- AG2610：ATM IV47.265% vs RV20 30.82%，IV-RV约+16.45 vol，RR25+7.81；方向强但上行凸性很贵，避免裸追Call。
- FU2611：ATM IV43.0% vs RV20 37.93%，IV-RV约+5.1 vol；地缘事件Vega仍有价值，但优先有限风险价差而非单腿买波动。
- BU2610：ATM IV27.745% vs RV20 23.63%，IV-RV约+4.1 vol；相对AG/FU没那么贵，但bid/ask=0仍阻止精确执行。
- CU2610：ATM IV14.3%，RR25+4.14，positioning-ready=true但execution=false；LME squeeze缓和后更适合观察skew回落，而不是追事件波动。
- 必须回避：AP/CJ/PL/PR/ZC本期链源日期不匹配；所有series均没有执行级bid/ask；dealer gamma方向未知，禁止构造Gamma挤压叙事。
- Vol RV：AG相对BU/FU的IV溢价极大，但在无可执行bid/ask和跨品种Delta/Vega配比前，只能做研究观察，不能给正式跨品种vol spread交易卡。

## 九、下一中国交易日09:00开盘风险地图（2026-08-24）

1. **FU/BU：偏高开风险，但gap大小不可直接估。** 中国周五夜盘终值不可审计，海外周五收盘也可能已被夜盘部分吸收。若gap>2%–2.5%，最危险动作是追多；优先等30–45分钟，看开盘区间、OI增量、Back是否继续、Brent电子盘是否维持。
2. **AG：高gap+高IV双重风险。** 海外金银周五明显上涨，周一若大幅高开，裸期货和裸Call都可能获得极差entry。至少等30分钟；gap>3%原则上不追。
3. **FG：可能受国内财政支持标题带来反弹挤空。** 只有反弹失败且899/900附近低点再失守，才做趋势空；若contango收窄、OI快速下降，不做。
4. **LC/PS：不要把开盘上涨解释成短缺。** LC已有price/OI强但contango冲突，必须等30–45分钟并观察curve、仓单/现货能否给方向确认。
5. **RM/农产品：周末天气与Black Sea headlines可造成隔夜重估。** RM当前价格与Back冲突，开盘前不设单边预判。

开盘后最重要确认指标：**15/30/45分钟开盘区间、主力具体合约ΔOI、near-next curve、量能是否延续、外盘Brent/银价是否与国内同向。**

## 十、未来24h / 7d事件日历（北京时间）

- 未来24h（周末）：无主要定时中国商品数据发布可作为硬催化；重点是霍尔木兹通航、美国对伊朗交易伙伴制裁、伊朗出口/浮仓、俄乌对炼厂与Black Sea港口的袭击。处理：能源/粮食保留有限凸性，拒绝周一无确认追gap。
- **8月24日**：USDA NASS Crop Progress按官方2026发布日历更新。处理：油脂油料、玉米、棉花相关仓位控制隔夜Delta，天气交易优先有限风险期权。
- **8月26日 22:30 BJT**：EIA Weekly Petroleum Status Report（官方页面给出Next Release Date 8/26，标准时间10:30 ET）。处理：FU/BU/SC主题在数据前减事件Delta，若持期权关注Vega crush。
- **8月27–29日**：Kansas City Fed Jackson Hole Symposium，主题“Financial Innovation: Implications for Payments and Policy”。处理：美元、实际利率、黄金白银Vega；具体讲话时间以最终agenda为准。
- **8月28日 15:30 ET / 8月29日03:30 BJT**：CFTC下一期COT，通常对应周二持仓。处理：只描述分类持仓，不把管理基金/商业头寸等同最终客户；周一交易不依赖滞后COT。
- 中国7月工业企业利润：按既往月末发布时间在8月下旬高度相关，但本轮未检索到8月官方具体发布日期，因此**不把8/27写成已确认硬日历**，待NBS正式页确认。
- OPEC+/IEA：未来7天未检出需要提前定价的固定月报节点；但任何临时OPEC+沟通、制裁与航运安全消息均属于高Delta事件。

## 十一、风险预算

单一试仓最大损失0.25%–0.75% NAV；本期FU/BU/AG/FG均只允许条件试仓，单笔建议0.25%–0.50% NAV。确认交易可升至0.75%–1.0%，但FU+BU+SC/LU等能源同因子总风险合并计算，初始≤0.75%，确认后≤1.5%，单一高确信能源主题绝对上限2.5%–3.0%。AG与AU属于同一美元/实际利率/Vega因子，不得重复堆仓。

压力测试必须覆盖：1/2个涨跌停、周末gap、夜盘流动性消失、保证金上调、霍尔木兹突然恢复/再恶化、相关性断裂、IV跳升/塌陷、人民币急变、中国休市时海外大幅波动。跨品种/期权结构在bid/ask恢复前不做伪精确风险预算。

## 十二、最后四行

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：周一FU2611回撤条件多、BU2610回撤条件多、AG2610回撤趋势多、FG701反弹失败条件空；周末不挂可成交市价单。
C. 今天应继续观察的机会：LC2701 price/OI强但contango、RM611价格与Backwardation冲突、CU2610在LME squeeze缓和后的skew回落。
D. 今天必须避免或退出的交易：追高能源/白银gap、裸买高IV AG Call、AP/CJ/PL/PR/ZC期权新仓、任何把C/D级basis或context-only跨境价格写成套利的交易。

## Sources

- China-Commodities-Engine unified input: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json
- China-Commodities-Engine EOD: https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json
- Reuters, oil close Aug.21: https://www.reuters.com/business/energy/oil-set-second-weekly-rise-unsettled-us-iran-war-crimps-supply-2026-08-21/
- Reuters, Hormuz traffic Aug.21: https://www.reuters.com/world/middle-east/hormuz-ship-crossings-hover-single-digits-data-shows-2026-08-21/
- Reuters, Iranian oil offers to China Aug.21: https://www.reuters.com/business/energy/iranian-oil-offers-chinese-buyers-fall-us-blockade-bites-sources-say-2026-08-21/
- Reuters, gold/silver Aug.21: https://www.reuters.com/business/gold-steadies-heads-third-straight-weekly-gain-2026-08-21/
- Reuters, China fiscal support Aug.21: https://www.reuters.com/world/asia-pacific/china-pledges-timely-fiscal-support-bolster-growth-2026-08-21/
- Reuters, Black Sea wheat Aug.20: https://www.reuters.com/world/asia-pacific/global-wheat-buyers-brace-supply-squeeze-amid-black-sea-attacks-2026-08-20/
- EIA WPSR: https://www.eia.gov/petroleum/supply/weekly/
- CFTC COT release schedule: https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- USDA NASS release day calendar: https://www.nass.usda.gov/Publications/Reports_by_Release_Day/
- Kansas City Fed Jackson Hole: https://www.kansascityfed.org/research/jackson-hole-economic-symposium/
- SHFE FU risk parameters (2026-06-23): https://www.shfe.com.cn/publicnotice/notice/202606/t20260623_832251.html
- SHFE FU contract: https://www.shfe.com.cn/products/futures/energyandchemical/fu_f/standard_fu/202312/t20231205_327331.html
- SHFE BU risk notice (2026-07-08, exchange notice mirrored by market data portals): https://finance.eastmoney.com/a/202607083798524258.html
- SHFE silver risk notice (latest located in this run): https://www.shfe.com.cn/publicnotice/notice/202510/t20251017_829279.html
