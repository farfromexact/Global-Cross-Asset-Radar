# 全球商品期货期权高风险机会雷达｜晚间版｜2026-08-25

> 数据截点：北京时间2026-08-25 19:30。中国日盘为2026-08-25完整EOD；海外映射使用15:00—19:30可获得的最新公开报价。21:00中国夜盘尚未发生。

## 一、今日一句话结论

**有值得冒险的条件机会，但没有应立即建立的新仓：EG2610是唯一80+，只在21:00后回撤企稳并重获5500时做多；V2701、FG701只做失败反弹空，FU/AG均降级观察。**

今天的核心不是“能源继续涨”，而是**MEG自身供应紧张与原油风险溢价回吐发生分叉**。因此今晚最值得承担的是EG的“确认后多”，而不是把整个化工链一起买入。

## 二、数据质量与覆盖说明

第一读取层实际读取`farfromexact/China-Commodities-Engine`的`data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`；为Top候选继续读取`data/latest.json`、`data/market_state_latest.json`、`data/physical/latest.json`、`data/options/quality_latest.json`、`data/options/surface_latest.json`、`data/options/latest.json`和`data/contract_meta.json`。`report_input requested_date=2026-08-25`，`generated_at=2026-08-25T19:02:30.093324+08:00`。

核心Futures五所SHFE/INE/DCE/CZCE/GFEX齐全，803个合约，`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0；unknown/duplicate/invalid OHLC/negative volume-or-OI均为0，placeholder=7并排除异常排行。Market State具备20个交易日历史，1D/3D/5D/20D均按同一具体合约计算，不拼连续主力。

Physical在19:02完成，20个目标只有4个按原生频率可用、16个不可用、0 stale、0 carried-forward。FG企业库存7441.4重量箱是8月21日最新周度**绝对水平**；I港口库存为8月19日最新周度值且单位按原源保留；JM现货/基差为8月20日旬度数据但basis质量C，不能计方向评分；TA加工费为8月21日周度level。因此仓库Physical本身仍不能完整闭环FG/V/EG的当日方向。

External仓库日频层整体`data_fresh=false`，逐series可用但不得冒充19:30实时；没有exact-contract、币种、品质、税费、运费、时点全部对齐的可执行进口平价。今晚海外覆盖另加Reuters实时层。

Options独立流水线已是T日：22,014条、59/64品种、369个series；362个surface-ready、71个positioning-ready、0个execution-ready，IV覆盖98.57%、OI覆盖69.32%、bid/ask覆盖0，dealer-gamma方向未知。`report_input`内嵌T日surface可直接研究；但独立`data/options/surface_latest.json`当前为空文件，属于产物审计缺口。所有期权结构均须人工核价，不能报当前净权利金或精确滑点。

## 三、商品仪表盘

| 板块 | 合约 | 8/25 Close / Settle | 1D settle / 5D | Volume / OI / ΔOI | Curve | Physical / Options | 信号 |
|---|---|---:|---:|---|---|---|---|
| 聚酯上游 | **EG2610** | 5364 / 5497 | **+3.25% / +10.69%** | 1,859,195 / 361,462 / **+5.27%** | **主力-次月Back +6.26%** | MEG库存多年来低位；ATM IV40.30%，pos✓/exec× | **第一候选，但日内冲高回落** |
| 塑化 | **V2701** | 4539 / 4576 | **-2.08% / -3.48%** | 1,335,984 / 1,172,046 / **+18.14%** | **主力-次月Contango -0.80%** | ATM IV18.47%，pos×/exec× | **失败反弹空** |
| 建材 | **FG701** | 913 / 916 | **-0.76% / -0.22%** | 1,244,642 / 1,508,419 / **+1.90%** | **Contango约-3.34%** | 库存仅level；ATM IV23.27%，pos✓/exec× | **空头条件重新激活** |
| 能源 | FU2611 | 3842 / 3935 | +2.96% / +6.27% | 1,366,745 / 286,887 / +0.79% | **主力-次月Back +6.27%** | T日surface可用/exec× | **内强外弱，禁止追** |
| 贵金属 | AG2610 | 16631 / 16775 | -0.65% / +4.22% | 752,304 / 282,243 / **-5.37%** | 主力-2612轻Contango -0.14% | ATM IV44.85%，RR25 +8.32，pos×/exec× | **昨日多头降级** |
| 新能源 | LC2701 | 日内大跌 / 153960 | **-3.79% / -0.89%** | 229,133 / 354,226 / -1.37% | 近端转Back，但结构需谨慎 | T日surface可研究 | **价格与curve冲突** |
| 化工 | MA610 | 2925 / 2946 | +2.01% / +6.58% | 2,317,858 / 839,347 / 减仓 | 近端Back约+1.26% | surface✓/exec× | 价涨仓减，不追 |
| 建材 | SA701 | 1045 / 1046 | -1.04% / +0.77% | 1,608,290 / 1,078,079 / 小幅减仓 | 近端Contango | surface✓/exec× | 昨强今弱 |
| 黑色 | I2701 | EOD | +0.14% / — | 完整 | Market State可用 | 港库最新周度；期权surface可用 | 中性 |
| 航运 | EC2610 | EOD | -1.49% / 高位 | 完整 | 结构异常敏感 | 无完整实体/期权闭环 | 高波动观察 |

注：Curve均指期货合约之间的期限结构，不是现货基差。FU/EG等临近9月合约会污染“最近液态合约”算法，因此本报告对Top候选改用**当前主力对下一流动合约**复核，而不使用被交割月扭曲的prompt spread。

## 四、相比上一交易日真正变化

**1. EG从“强势观察”升级为唯一80+候选，但不是追涨。** 8月25日EG2610结算+3.25%、5D +10.69%，OI再增5.27%；主力2610对2611结算价仍有约6.26%Backwardation。更重要的是，CCFGroup 8月20日的最新产业研究显示中国MEG总库存与可见库存均降至多年低位，8—9月进口到货受Hormuz/Bab el-Mandeb阻断限制，实体紧张是独立于单日K线的证据。与此同时，今天最高5631、收盘5364，尾盘回吐明显，所以“供需强”不等于“21:00首跳可追”。

**2. 原油出现明确的15:00后反向映射。** Reuters 17:57 BJT附近报价显示Brent跌3.21%至89.21美元/桶、WTI跌3.34%至82.17美元/桶，均至一周低位；市场认为新一轮对伊朗制裁短期不如军事升级威胁供应。Hormuz运输仍高度受限、阿曼附近油轮又遭袭，因此这是“风险溢价回吐”，不是供应风险归零。对FU/BU是直接利空映射，对EG则主要压制追涨赔率而未破坏其独立库存逻辑。

**3. V2701成为新的高质量弱势候选。** close -2.87%、settle -2.08%，OI单日+18.14%，是非常明显的“价跌仓增归因线索”；主力2701对2702约-0.80% Contango。配合外油下跌，成本支撑变弱，但缺少PVC现货库存/地产终端的T日实体确认，因此只能做失败反弹空，不能把仓增写成“确定新增空头”。

**4. AG昨日的回撤多逻辑降级。** 国内settle -0.65%、close -1.50%、OI -5.37%；17:37 BJT Reuters显示现货黄金-0.4%、白银-1.4%，美元反弹和获利了结压制贵金属。AG仍有5D +4.22%的中期趋势，但今天没有新增风险的最佳时点。

**5. FG的空头条件重新出现。** 8月24日价格反弹且明显减仓曾使旧空头失效；今天转为价跌、OI回升、Contango持续。仓库里FG库存仍只是8月21日周度绝对水平，因此这是三层证据交易，不是“实体需求崩塌”结论。

## 五、产业链地图

| 链条 | 方向 | Price / Curve | 实体/海外 | Options | 最大缺口 | 置信度 |
|---|---|---|---|---|---|---|
| **MEG—聚酯** | **结构偏多、短线过热** | EG价/OI强，主力Back约6.26% | 库存多年低位、进口受阻；外油今日回落 | IV40.30% vs RV35.20%，pos✓/exec× | 聚酯减产幅度、21:00承接 | **高** |
| **PVC/地产塑化** | **偏弱** | V价跌/OI大增+Contango | 原油下跌削弱成本；实体库存缺 | IV18.47% vs RV11.64%，exec× | PVC社会库存、出口、地产需求 | 中高 |
| **玻璃建材** | 偏弱 | FG价跌/OI增+Contango | 仓库库存只有level | IV23.27% vs RV17.12%，pos✓ | 库存方向、深加工订单 | 中高 |
| **原油—燃料油** | 结构紧但短线降温 | FU国内仍Back | Brent/WTI欧盘约-3% | surface可用、exec× | 裂解/产品库存、Hormuz新进展 | 中 |
| **贵金属** | 中期多、短线回撤 | AG5D仍正、curve弱 | 金银欧盘回吐、美元反弹 | IV44.85%、call skew贵 | 实际利率/PCE/Jackson Hole | 中 |

最强产业链是**MEG供应紧张**；最弱的可交易结构是**PVC/地产塑化**。当前regime是“局部供应短缺与地缘尾部仍在，但宏观能源risk premium开始回吐”，不是商品普涨。

## 六、机会排行榜

| Rank | 机会 | Score | 逻辑/赔率/催化/结构技术 | Fresh证据层 | 阶段 |
|---:|---|---:|---|---:|---|
| **1** | **EG2610 回撤确认多** | **82** | 23 / 20 / 17 / 12 / 10 | **5** | 80+确认交易，但必须触发 |
| **2** | **V2701 失败反弹空** | **78** | 21 / 20 / 15 / 12 / 10 | **4** | 条件试仓 |
| **3** | **FG701 失败反弹空** | **74** | 20 / 19 / 13 / 12 / 10 | **3** | 条件试仓 |
| 4 | FU2611 内外盘冲突观察 | 68 | — | 3 | 观察 |
| 5 | AG2610 高位回撤观察 | 65 | — | 3 | 观察 |

EG虽然达到80+，但**80+不等于现在下单**：其日内从5631回落至5364，且19:30前外油大跌。触发必须来自21:00之后的价格承接，而不是来自评分本身。

## 七、前三名交易卡

### 1. EG2610｜条件多｜82

**事实：** settle 5497，1D +3.25%、5D +10.69%、OI +5.27%；主力EG2610对EG2611结算价Backwardation约6.26%。8月20日CCFGroup称中国MEG总库存与可见库存处多年低位，东华主港库存此前持续大幅去化，8—9月进口仍受中东航运阻断。T日期权EG2610/2026-09-16：ATM 5500，ATM IV40.295%，RV20约35.20%，IV-RV约+5.10vol，RR25 -2.31，positioning-ready=true，execution-ready=false。

**市场定价：** 稀缺已经被高期货价格和Backwardation明显price-in，今天5631→5364的回落说明边际多头并非无条件承接。  
**推断：** 如果外油下跌背景下EG仍能在夜盘守住5360—5400并重新接受5490/5500，说明其独立供需强于能源Beta。  
**主观判断：** 这是今晚唯一值得在确认后承担较大风险的商品。

**最佳表达：** 首选小期货仓完成方向确认；如逐合约quote确认流动性，再用2026-09-16 **1:1 Call Spread（长35–45Δ Call、短15–25Δ Call）**封顶gap风险。期权最大损失为净权利金，但当前bid/ask缺失，不报净支出。

**入场/分批：** 21:00后至少等30分钟，最好30–45分钟。第一条件是5360—5400不形成持续接受；第二条件是重新站上5490/5500。两者同时满足先1/3风险；站稳VWAP并重新突破夜盘首小时高点再加。  
**初始止损：** 30分钟有效接受在5320下方。  
**逻辑失效：** 主力-次月Backwardation快速压缩至约3%以下，且价格不能重回5400；或出现可靠的中东MEG到货恢复/聚酯大规模减产。  
**TP1 / TP2：** +1R / +2R；若重新测试5630附近但量价/OI不跟，优先减仓。  
**时间止损：** 两个交易时段仍不能重获5500，撤。  
**最大损失：** 初始0.45%–0.65% NAV；确认后同主题累计不超过1.25% NAV。  
**1—20D催化：** 中东航运、港口到货、聚酯开工/减产、EIA及原油波动。  
**最坏情景：** 外油继续暴跌+进口路线恢复+聚酯降负，EG高位紧张溢价快速坍塌。  
**放弃条件：** 21:00直接高开突破5630而无回踩；或直接低开跌破5320。

合约静态参数：10吨/手、tick 1元/吨、tick value 10元，5497对应名义约54,970元/手；标准合约最低保证金5%、基准涨跌停±4%，但**8月25日动态交易所保证金/涨跌停和券商保证金未独立确认**，不据旧静态参数计算一板/两板实际压力。夜盘21:00–23:00；实物交割；最后交易日规则为交割月倒数第4个交易日，EG2610精确日期本次未由metadata确认。计划在距LTD约10个交易日前或OI明显向后月迁移时roll。

### 2. V2701｜条件空｜78

**事实：** close4539、settle4576，settle -2.08%，5D -3.48%，OI +18.14%，OI change z-score约3.26；V2701对V2702结算价约-0.80% Contango。T日2026-12-16期权ATM4600、IV18.465%，RV20约11.64%，IV-RV约+6.82vol，RR25 +3.91；surface-ready=true，positioning-ready=false，execution-ready=false。

**市场定价：** 弱需求/供应压力已经进入价格，但当日大量增仓使进一步波动概率上升。  
**推断：** 只要反弹无法重新接受4600—4640，趋势空仍有赔率；若直接gap-down，赔率反而变差。  
**主观判断：** 比追空更适合等第一次失败反弹。

**最佳表达：** 期货空；若quote可执行，可用2026-12-16 **1:1 Put Spread（长35–45|Δ| Put、短15–25|Δ| Put）**限制gap。  
**入场/分批：** 等30分钟；4590—4640区域反弹失败并重新跌回4550下方，先1/3。跌破4525后仍无法快速收回再加。  
**止损：** 30分钟有效站稳4667/4680。  
**逻辑失效：** Contango快速消失并出现可靠PVC库存去化/出口改善。  
**TP1 / TP2：** 4525 / 4450附近，或+1R/+2R。  
**时间止损：** 两个交易日不创新低。  
**最大损失：** 0.35%–0.50% NAV。  
**最坏情景：** 夜盘政策/地产刺激引发塑化链同步涨停、空头无法退出。  
**放弃：** 21:00直接跳空跌破4500，不追。

当前业务规则显示V交易单位5吨/手、最小变动价位1元/吨，tick value 5元，4576名义约22,880元/手；夜盘21:00–23:00，实物交割，最后交易日为交割月第10个交易日。8月25日动态交易所保证金、涨跌停及券商保证金未确认，因此不虚构1/2板压力金额。计划T-10前roll。

### 3. FG701｜条件空｜74

**事实：** close913、settle916，settle -0.76%，OI +1.90%，近端结构维持Contango约-3.34%。T日2026-12-11期权ATM920、IV23.265%，RV20约17.12%，IV-RV约+6.15vol，RR25 +6.74，positioning-ready=true、execution-ready=false。仓库Physical只有8月21日企业库存7441.4重量箱的绝对level，不能算方向确认。

**市场定价：** 8月24日的反弹/减仓未延续，今天重新出现价跌仓增；但市场还没有给出实体需求崩塌证据。  
**推断：** 920—926是今天形成的第一阻力带，失败反弹才是好空点。  
**主观判断：** 空头逻辑恢复，但证据仍弱于EG/V。

**入场：** 等30分钟；920—926反弹失败，再跌回915下方先1/3；有效跌破907再加。  
**止损：** 30分钟有效站稳930。  
**逻辑失效：** Contango明显收窄，同时出现可验证库存下降/深加工订单改善。  
**TP1 / TP2：** 907 / 890—880区域。  
**时间止损：** 两交易日不破907撤。  
**最大损失：** 0.25%–0.40% NAV。  
**放弃：** 21:00直接gap-down跌穿900，不追。

FG交易单位20吨/手、tick 1元/吨、tick value 20元，916名义约18,320元/手；夜盘21:00–23:00，实物交割，最后交易日为交割月第10个交易日。标准合约最低保证金5%、基准价格限制±4%并受风险控制规则调整；**8月25日动态比例未确认**，因此不按静态4%虚构真实一板/两板压力。T-10前roll。

## 八、商品期权专项

本次不称“全市场最高/最低IV”，只列代表性可复核series。EG2610 ATM IV40.30% vs RV20 35.20%，约+5.10vol；V2701 18.47% vs 11.64%，约+6.82vol；FG701 23.27% vs 17.12%，约+6.15vol；AG2610 44.85% vs 29.97%，约+14.88vol，且RR25 +8.32，仍是明显昂贵的上行skew样本。

结构上，EG方向edge优于纯Vega edge，先期货确认再比较Call Spread；V/FG的IV均显著高于RV，买裸Put会支付较高波动率，优先Put Spread。AG继续回避裸买高IV ATM Call。全市场0个execution-ready、bid/ask coverage=0，任何spread都只是研究结构，须逐合约人工核价。Dealer Gamma方向未知，不做Gamma squeeze推断。

## 九、21:00夜盘开盘风险地图

| 品种 | 中国8/25日盘 | 15:00—19:30海外映射 | 预期开盘 | 置信度 | 追价 | 等待 | 夜盘后关键确认 |
|---|---|---|---|---|---|---|---|
| **EG2610** | settle +3.25%，close仅+0.75%，尾盘回吐 | Brent/WTI约-3.2%/-3.3%，但MEG自身进口紧张 | 平至小低/高波动 | 中 | **否** | **30–45m** | 5360—5400、5500、VWAP、主力-次月 |
| **V2701** | close -2.87%，OI +18% | 原油下跌削弱成本支撑 | 偏低 | 中高 | **否** | 30m | 4590—4640反弹、4525、OI |
| **FG701** | close -1.08%，价跌仓增 | 无直接海外强映射 | 平至偏低 | 中 | 否 | 30m | 920—926、907、Contango |
| FU2611 | settle +2.96%，但4059冲高后close3842 | **Brent/WTI大跌约3%** | **偏低** | 高 | **禁止首跳** | 30–45m | 3800附近承接、Back是否收窄 |
| AG2610 | 国内回撤、OI -5.37% | 金-0.4%、银-1.4%、美元反弹 | 偏低 | 中高 | 否 | 15–30m | 16600、海外银、DXY/实际利率 |
| MA610 | settle +2.01%，价涨仓减 | 能源映射转弱 | 平/小低 | 中 | 否 | 30–45m | 2900、VWAP、OI |
| LC2701 | settle -3.79%、close跌幅更大 | 无可靠直接海外映射 | — | — | — | — | **夜盘安排本次metadata未确认；下一确定窗口8/26 09:00** |
| EC2610 | 日盘回落 | 地缘航运风险仍高 | — | — | — | — | 夜盘资格未在本次metadata确认，不作21:00下注 |

今晚最容易犯的错：**看到EG日盘很强就忽略外油大跌直接追；或者看到FU外油大跌直接在21:00第一秒追空。** 两者都应等第一轮价格发现。

## 十、未来24h / 7d事件

- **8月26日20:30 BJT**：美国BEA发布7月Personal Income & Outlays/PCE，同时Q2 GDP二次估值。AG/AU及美元敏感商品需降低事件前裸Delta/Vega。
- **8月26日22:30 BJT**：EIA Weekly Petroleum Status Report。FU/SC/BU以及化工链若已有利润，数据前不扩大同一能源因子。
- **8月27日03:00 BJT附近**：USDA 8月26日15:00 ET的Broiler Hatchery、Peanut Stocks/Processing及美加牛/猪数据，主要映射养殖/饲料/花生链。
- **8月27—29日**：Jackson Hole Economic Policy Symposium，2026主题为“Financial Innovation: Implications for Payments and Policy”；贵金属核心风险来自美元与实际利率重新定价。
- **8月29日03:30 BJT**：CFTC按计划发布8月28日COT，反映此前周二持仓，只作positioning背景，不能代替实时流量。

风险预算：单一试仓最大损失0.25%—0.75% NAV；确认交易0.75%—1.50%；单一主题总风险≤2.5%—3.0%。EG/MA/FU不要因“都是强势化工”而忽略共同的中东/能源因子；V/FG则共享国内地产工业需求因子。压力测试包括1/2个涨跌停、相关性破裂、流动性消失、夜盘gap、保证金上调、IV跳升/塌陷和交割挤压。

## 数据与来源

- China-Commodities-Engine统一输入：`https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/report_input_latest.json`
- China-Commodities-Engine合约EOD：`https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/latest.json`
- China-Commodities-Engine Market State：`https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/market_state_latest.json`
- China-Commodities-Engine Physical：`https://github.com/farfromexact/China-Commodities-Engine/blob/main/data/physical/latest.json`
- Reuters 2026-08-25 oil：`https://www.reuters.com/business/energy/oil-prices-steady-investors-weigh-impact-expanded-us-sanctions-against-iran-2026-08-25/`
- Reuters 2026-08-25 gold：`https://www.reuters.com/world/india/gold-rises-highest-since-mid-may-buying-momentum-builds-2026-08-25/`
- CCFGroup 2026-08-20 MEG：`https://cnc.ccfgroup.com/newscenter/newsview.php?Class_ID=D00000&Info_ID=2026082030013`
- EIA WPSR：`https://www.eia.gov/petroleum/supply/weekly/index.php`
- BEA release schedule：`https://www.bea.gov/news/schedule`
- CFTC COT schedule：`https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm`
- Kansas City Fed Jackson Hole：`https://www.kansascityfed.org/research/jackson-hole-economic-symposium/jackson-hole-faqs/`

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：EG2610回撤确认多；V2701、FG701失败反弹空。
C. 今天应继续观察的机会：FU2611内外盘冲突、AG2610高位回撤、LC2701价格与curve冲突、MA610价涨仓减。
D. 今天必须避免或退出的交易：21:00追首跳、把外油下跌直接等同于所有化工做空、裸买AG高IV Call、execution=false时硬报期权权利金、重复堆同一能源/地产因子。
