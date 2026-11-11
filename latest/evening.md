---
report_date: 2026-11-11
edition: evening
generated_at_bjt: 2026-11-12T00:13:41+08:00
revision: 2
weekend_mode: false
china_options_date: 2026-11-10
china_options_fresh: false
archive_status: success
---

# 全球跨资产机会雷达晚间版｜2026-11-11｜revision 2

> **重跑截点：2026-11-12 00:13 BJT。** 本版替换20:04旧报告。中国现金市场已收盘；美国现金盘已经交易约1.5小时；美国国债现券因Veterans Day休市。中国商品11/11夜盘已启动：DCE豆粕夜盘窗口已经结束，INE原油仍在夜盘。Stock与Commodities仓库均已在旧报告之后补齐到11/11。

## 1. 一句话结论

**补数后中国商品与Stock证据恢复：M曲线仍强但今晚入场序列已过去；美股AI现金盘强反弹、VIX回落而美债休市。无立即新仓，只保留需完整顺序/报价确认的相对价值。**

## 2. 全市场仪表盘

| 模块 | 最新可得 | 变化/信号 | 时点与边界 |
|---|---:|---|---|
| UST 2Y/5Y/10Y/30Y | 4.73/4.81/4.98/5.35% | 热CPI后前端压力高；2s30s约62bp | 11/10官方EOD；11/11债市休市 |
| 10Y实际利率 | 2.78% | 黄金/长久期估值仍受压 | 11/10官方last-good |
| DXY / EURUSD / USDJPY / USDCNH | 102.47 / ~1.1133 / ~159.19 / ~6.6740 | 美元偏强、日元carry压力仍大，CNH稳定 | 11/11美国早盘，多时点 |
| QQQ | ~687.8，约+1.9% | AI relief从盘前进入现金盘 | 约10:30 ET |
| SOXX / SMH | ~153.3 / ~502.2，约+4.6%/+3.8% | 半导体强于QQQ；SOXX相对SMH略强 | 约10:06 ET |
| SOXX/SMH | ~0.3053 | 旧卡0.3040价格阈值在一个近同步快照中越过，但完整回踩序列未证明 | 约10:06 ET，跨provider |
| VIX / MOVE / HY OAS | ~18.6 / 92.43 / 3.34% | 股波回落；MOVE/HY滞后 | VIX 11/11盘中；MOVE11/10；HY11/9 |
| WTI / Brent | 87.12 / 92.81美元 | +1.3%/+1.4%，从两月低位反弹 | 11/11 13:14GMT |
| Gold / Silver | ~4043 / 52.81美元 | 小幅反弹；热CPI/实际利率仍反对追多 | 11/11美国早盘 |
| 中国现金宽度 | 3538涨/1828跌/214平，等权+1.14% | 成长、小盘明显强于大盘 | 11/11 EOD |
| SSE50 / CSI300 / CSI500 / CSI1000 | -0.27% / +0.41% / +1.01% / +1.37% | CSI1000相对SSE50领先1.64pp | 11/11 EOD |
| IH/IF/IC/IM2612 | 2742.2/4043.4/6664.0/6623.0 | OI约63192/173783/173915/290211 | 11/11 15:28二级快照，非官方复核 |
| IH/IF/IC/IM basis | -0.84%/-0.79%/-0.73%/-0.70% | **旧版IC +0.54%为计算错误，本版纠正** | 现金收盘×期指二级收盘 |
| HO/IO/MO 2612 | ATM IV约14.90/18.10/29.51%；RR25约-1.27/-0.92/-3.05vol | 仅last-good；不得推断11/11 vol crush或dealer方向 | 11/10 EOD |
| M2701/M2705 | close3139/2839；settle3137/2831 | close spread300、settle spread306；M2701涨但OI减1.34% | 11/11 fresh Wind EOD |
| SC2612/SC2701 | close604/591.9；settle598.1/584.1 | 近远月settle spread14；**流动性主力已滚到2701** | 11/11 fresh Wind EOD |
| 商品期权 | 64/64 sampled；ATM-ready60；skew-ready3；execution0 | 覆盖明显恢复，但仍无bid/ask/full-chain | 11/11 21:50 |
| China-Stock-Engine | 5580证券，36个union candidates | 1D等权+1.14%、3D+3.05%、5D+3.39%，tradability仍missing | 11/11 fresh |

关键质量变化是：20:04旧版里“商品核心批次失败”和“Stock停11/9”两条已经不成立。Commodities在22:07刷新至11/11，五所full-market、source-date match 100%、critical error=0；Stock在22:18前后完成11/11研究快照。

## 3. 相比20:04旧版真正发生了什么变化

1. **商品EOD从降级恢复为正式研究输入。** 11/11全市场数据已到位；M、SC、CU等曲线重新可核。缺口现在变成basis/warehouse/member ranking，而不是“没有当天期货数据”。
2. **Stock Engine也恢复到11/11。** 全市场5580只证券中36只进入candidate union；1/3/5/20日复权历史基本齐全。旧版“Stock停11/9”的判断废止。
3. **美股已经从盘前进入现金盘。** QQQ约+1.9%，SOXX/SMH约+4.6%/+3.8%，VIX降至约18.6。AI relief得到现金成交确认，但不是所有AI beta都等价。
4. **M2701-M2705研究逻辑增强，但执行窗口已经过去。** Fresh EOD确认close spread300、settlement spread306；同时M2701 OI日减25247，说明上涨包含空头回补。21:15的“回踩→收复→再回踩”序列无法事后证明，因此不能回填成交。
5. **SC旧卡需要退役，而不是简单换个数字。** Fresh数据表明SC2701已经是更高流动性的主力，SC2612变成近月/次主力；Brent最新独立核验92.81又低于旧卡93门槛。因此旧SC2612“610重夺”规则不能平移到SC2701。
6. **中国小盘相对强度比旧版更扎实。** 二级期指OI相对11/10官方基准估算IH/IF/IC/IM约+1720/+163/+4705/+9945，价格和OI更共振；但当日官方CFFEX文件和11/11期权链仍缺。

## 4. 全球统一Top5

| # | 机会 | 总分 | 研究 / 证据 / 执行 |
|---:|---|---:|---|
| 1 | M2701-M2705近多远空 | **73** | 有待验证优势 / 4层 / 今晚窗口已过，序列未知 |
| 2 | SOXX多 / SMH空相对价值 | **72** | 优势增强 / 现金盘+基本面+波动 / 完整retest与borrow未证 |
| 3 | IM2612多 / IH2612空 | **69** | 方向优势增强 / 现金宽度+期指价格OI+政策 / 11/12日盘再验 |
| 4 | 美国2s30s趋平 | **68** | 有待验证 / CPI与政策支持 / 债市休市、待DV01 |
| 5 | 黄金政策信用凸性 | **68** | 减弱但未失效 / 宏观混合 / 期权待询价 |

分项依次为逻辑/赔率凸性/催化/价格期限波动/拥挤技术：M **21/19/17/9/7**；SOXX/SMH **22/18/15/9/8**；IM/IH **20/15/14/10/10**；2s30s **21/16/15/8/8**；Gold **20/15/14/10/9**。均已重算。

## 5. Top3交易研究卡

### 卡1｜M2701-M2705近多远空：研究成立，**今晚不能回填执行**

idea_id保持 **COM-M-M2701-2705-WASDE-BACKWARDATION-LONG-20261111**。Fresh数据：M2701 close3139/settle3137，M2705 close2839/settle2831，因此close价差300、settlement价差306；现货主流报价同步上涨约70—90元/吨，外部CBOT/USDA成本端也提供支持。

但原规则是：先回踩292—298；首15分钟低点>=286；21:15收盘>=300；随后5分钟再回踩296—300不破；CBOT soy>=1220；深度正常；>304不追。**现在已经00:13，DCE夜盘已经结束。** EOD close300或settlement306都不能证明21:15后的顺序，也不能证明用户成交。

原止损284、TP1 340、TP2 370、11月18日14:55时间退出全部保留。按80元/组往返成本情景，296/300/304入场的TP1净R仍为1.80/1.33/1.00。下一合法窗口11月12日09:00必须重新取价；本版不创建新阈值来“追上市场”。

### 卡2｜SOXX多 / SMH空：**部分价格条件出现，完整signal仍未证明**

idea_id **AI-SOXX-SMH-CASHFLOW-CAPEX-RV-20261106**。约10:06 ET的近同步快照为SOXX 153.32、SMH 502.20，比率约**0.3053**，已经高于原0.3040第一价格门槛；QQQ约+1.9%、VIX约18.6，也说明现金盘风险偏好恢复。

但原AND/顺序是：开盘后30—45分钟，ratio先15分钟收>0.3040；随后回踩守0.3035；QQQ守首30分钟低点；borrow/fee核实；50/50。我们只有快照，没有完整“收盘→回踩”路径，也没有borrow，因此**signal_met=unknown，不认定成交**。

参考33股SOXX多/10股SMH空仅近似美元名义中性，不是Beta-neutral。stop仍为daily ratio close<0.3000或NVDA相对反弹>6%且ratio<0.3010；TP1/TP2 0.309/0.315。成本、借券和Beta未知时风险预算为0。

### 卡3｜旧SC2612重夺610多头：**新开仓计划退役**

Fresh EOD：SC2612 close604/settle598.1，SC2701 close591.9/settle584.1；SC2701成交/持仓更高，说明流动性主力已经roll。公开23:05辅助快照显示SC2612约609.9，但最新独立Brent核验为92.81，仍低于旧规则的93。

因此原规则“Brent>=93 AND SC首15分钟收>=610 AND 回踩608—611守住 AND spread>=10”没有被完整证明，而且**即使随后满足，也不应继续把SC2612当未来新仓主合约**。旧idea保留作历史父节点；若未来改做SC2701，必须新建child/alias并重新计算入场、止损、乘数压力和curve阈值，不能把610直接平移。

## 6. 黄金特别研究

“政策信用期权”判断仍是**减弱但未失效**。11月11日早盘黄金约4043美元、白银约52.81美元，属于前一日急跌后的修复；10Y实际利率last-good仍高达2.78%，DXY约102.47，是继续压制黄金的主要竞争解释。

新商品引擎带来一个有用但有限的本地截面：AU2612 ATM IV约20.8%，RR25约-1.42vol、BF25约+1.03vol，说明国内黄金期权局部skew可研究；但bid/ask覆盖0、surface/positioning/execution均false，不能据此声称某个价差“便宜”或可直接成交。

表达顺序不变：真实询价后的3—6个月GLD Call Spread > 确认后的MGC > Gold+long-bond Put Spread > no-trade。当前仍优先no-trade。

## 7. AI特别研究

CoreWeave今天给了一个很关键的反证：AI需求并没有随市场去杠杆一起消失。公司业绩推动股价约涨10%，Nvidia约涨5%；更重要的是公司提高收入展望，并表示不打算继续依赖无担保债务市场，现有合同现金流足以覆盖当前及未来债务偿付。

所以“AI = 全部Capex泡沫”的叙事需要下调。但SoftBank的数据中心设备减值也说明，**Capex timing和资本回报风险仍然真实存在**。

因此最自然的表达仍是“现金流/融资质量相对高的AI资产 vs 集中Capex beta”，而不是裸空整个QQQ或半导体。SOXX/SMH只是一个可交易代理，不是纯粹的现金流因子组合，更不是Beta-neutral。

## 8. 中国50/300/500/1000与公司专项

现金市场：SSE50 -0.27%、CSI300 +0.41%、CSI500 +1.01%、CSI1000 +1.37%。Stock Engine自己得到的全市场宽度为3538涨、1828跌、214平，等权+1.14%，成交约1.689万亿元；3日/5日等权收益约+3.05%/+3.39%，而20日仍约-2.59%。这是“短周期风险修复、较长周期仍未完全扭转”的典型结构。

二级期指11/11收盘：IH/IF/IC/IM2612约2742.2/4043.4/6664.0/6623.0，basis重新计算为**-0.84%/-0.79%/-0.73%/-0.70%**。20:04旧版里IC写成+0.54%是错误，本版纠正。与11/10官方引擎OI基准跨源比较，IH/IF/IC/IM约+1720/+163/+4705/+9945，小盘价格与OI共振比旧版认为的更强。

但HO/IO/MO仍停在11/10：ATM IV约14.90/18.10/29.51%，RR25约-1.27/-0.92/-3.05vol。IC仍没有一一对应CFFEX指数期权。**因此IM/IH研究升级到69分，但不进入今晚执行；11月12日09:30需重新核官方OI、basis和新期权链。**

Stock Engine的改善也很实质：它已经扫描5580只PIT证券并返回36个候选。不过tradability、行业和指数成分仍缺，很多候选只有价量证据。公开补证进一步说明为什么不能机械追突破：
- 汉王科技11/11涨停，但Q3收入同比-6.74%、单季净亏约5199万元、前三季度经营现金流约-2.34亿元；
- 蓝黛科技11/11涨停，但Q3收入-9.03%、单季净亏约1783万元、前三季度经营现金流为负；
- 华策影视11/11涨5.85%，Q3收入+109.97%，但单季归母净利-82.97%、前三季度经营现金流约-9.26亿元。

所以本期A股个股仍为0个统一Top5候选——不是因为Stock Engine没跑，而是**新价量信号没有与盈利/现金流/执行状态闭环**。

## 9. 商品全范围与未来24h/7d

商品全市场恢复后，77个品种、约806张合约重新可做后台扫描。当前最清晰的是：
- M：主次月强backwardation + 现货上调，但近月价格上涨同时OI下降，不能把全部上涨归因新多；
- SC：近月backwardation仍在，但主力已roll到2701，且海外油价仍处低位；
- CU：2612/2701 settlement spread约1230、backwardation约1.18%，但CU2612本身跌0.61%，没有实体层就不追价差；
- AG：国内主力close基本平、settlement偏弱，而海外银强反弹，方向冲突；
- MA：曲线压力很强，但price/OI关系与实体证据不足，避免只看curve追单。

商品期权本次64/64计划品种都取得core样本，60个series局部ATM-ready、3个skew-ready；这是明显改善。但**full_chain=false、surface=0、positioning=0、execution=0、bid/ask=0**，所以仍然不能输出可成交权利金、全链PCR、Dealer Gamma或“有限亏损已锁定”的结构。

未来事件：
- **11/12 09:00** 中国商品日盘：M价差和SC/CU主力重新取价；
- **11/12 09:30** A股/CFFEX：验证IM/IH价格、OI、basis与期权链；
- **11/12 23:00** Fed Barr演讲“Artificial Intelligence and Inequality”；
- **11/13 01:00** EIA周度石油报告（Veterans Day顺延）；
- **11/13 21:30** 美国10月PPI；
- **11/13 23:50** Fed Bowman；
- **11/14 08:00** Fed Jefferson谈技术与生产率；
- **11/17 22:15** 美国工业生产。

## 10. 风险预算、数据缺口与发布检查

风险预算不变：试仓0.25%—0.75% NAV，确认0.75%—1.50%，同一高确信主题总预算不超过2.5%—3.0%。保证金不是风险预算，计划止损不保证期货最大亏损。

本次预发布实际检查：
- Top5分项加总全部重算通过；
- M/SC旧idea的原始触发、止损、TP和time-exit没有为了重跑而移动；
- 旧SC2612因主力roll退出新开仓池，没有把参数平移到SC2701；
- IC basis已重新确定性计算并纠错；
- 商品期权64/64 core sample不等于full chain，所有执行边界继续保留；
- 仍未取得11/11官方CFFEX逐合约文件、11/11 HO/IO/MO、当前夜盘repo完整捕获、商品basis/warehouse/member ranking以及SOXX/SMH borrow/beta。

### 关键来源

- [US Treasury daily yields](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026)
- [US Treasury real yields](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_real_yield_curve&field_tdr_date_value=2026)
- [Reuters: CoreWeave/AI cloud rally](https://www.reuters.com/world/china/coreweave-sparks-ai-cloud-stock-rally-lifts-nvidia-results-ease-bubble-fears-2026-11-11/)
- [Reuters: oil rebound and Hormuz risk](https://www.reuters.com/business/energy/oil-rises-two-month-low-hormuz-shipping-attacks-offset-iran-truce-hopes-2026-11-11/)
- [Reuters: gold rebound after selloff](https://www.reuters.com/world/india/gold-edges-higher-after-sharp-selloff-fed-hike-bets-weigh-2026-11-11/)
- [同花顺：11月11日A股收盘](https://news.10jqka.com.cn/20261111/c681699803.shtml)
- [九期网：股指期货11月11日行情](https://www.9qihuo.com/hangqing)
- [中信期货：11月11日豆粕行情与现货/USDA背景](https://www.citicsf.com/e-futures/content/000508/826788)
- [Federal Reserve calendar](https://www.federalreserve.gov/newsevents/calendar.htm)
- [EIA holiday-adjusted schedule](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- [BLS November release schedule](https://www.bls.gov/schedule/2026/11_sched_list.htm)
- [China-Commodities-Engine current status](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/last_run_status.json)
- [China-Commodities-Engine current option surface](https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/options/surface_latest.json)
- [China-Stock-Engine opportunity radar](https://github.com/farfromexact/China-Stock-Engine/blob/main/data/latest/opportunity_radar_latest.json)
- [China-Options-Engine radar_latest](https://github.com/farfromexact/China-Options-Engine/blob/main/data/radar_latest.json)

A. 今天没有应立即建立的新仓位。  
B. 今天仅保留条件候选：SOXX多/SMH空只有在同窗ratio>0.3040→回踩守0.3035、QQQ守首30分钟低点且borrow/fee核实后才进入；黄金Call Spread仅RFQ。  
C. 今天继续观察：M2701-M2705强backwardation（原夜盘序列未知，不回填）、IM相对IH、11/12债市重开后的2s30s、SC2701 roll后的新参数，以及Stock Engine 36个候选的财务/公告闭环。  
D. 今天必须回避或若此前自有仓位则有条件退出：禁止把M settlement spread306当成21:15已触发；禁止继续用SC2612的610规则开新仓；禁止把11/10 HO/IO/MO或无bid/ask商品期权当11/11执行价；不因涨停/突破忽略盈利与现金流反证。