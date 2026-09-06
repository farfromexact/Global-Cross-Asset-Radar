# 全球跨资产高风险机会雷达｜晚间版

## 2026-09-06｜周日｜截至北京时间20:12｜prompt_version=radar_2026-09-06_coverage_v1

**今天究竟有没有值得冒险的机会：有，但现在没有可立即成交的新仓。** 周末新增事实确认美国已打击三艘伊朗原油运输船，OPEC+会前可靠基线仍是10月政策不变、正式结果在截点尚未由OPEC或Reuters确认；因此第一机会仍是**周一重开后、只在温和gap/回撤被接受时买油价右尾凸性**。中国Long IH/Short IM仍有效，但5日已扩张2.74个百分点，不追开盘gap。

### 时间与数据口径

- 生成时间/信息截点：北京时间2026-09-06 20:12。
- 美国、中国、欧洲现金市场均休市；最近完整时段为美国/中国2026-09-04收盘。下一个中国可交易窗口为9月7日09:30；CME能源/金属/利率/股指期货常规周日夜间重开约为北京时间9月7日06:00，但Labor Day采用缩短时段，低流动性价格不能替代9月8日美国现金盘确认。
- 全球行情沿用9月4日已核验last-good，不冒充实时；本期新增仅包括9月6日可核验新闻、19:04刷新的中国商品紧凑层和归档台账。
- China-Options-Engine固定提交为 `ddf1ba3f220c5b803a8017fbddc843544035c92a`；`radar_latest.json`为9月4日EOD，`radar_history.json`确为空文件。
- China-Commodities-Engine固定提交为 `8f55b9943ce7d45caec1c0c6ebaddefa1554be0f`；`report_input_latest.json`生成于9月6日19:04，底层交易日为9月4日。期货层可作last-good全市场扫描；期权surface/execution均未就绪。

## 一、今日一句话结论

**地缘供给冲击+鹰派前端利率+低股指波动率：最大错位是油运风险升高而VIX/HY仍平静；油价凸性第一、IH/IM第二。**

## 二、隔夜 / 国内市场仪表盘

| 资产 | 最新值 | 1D | 约1W | 信号 | 数据时间/属性 |
|---|---:|---:|---:|---|---|
| UST 2Y / 5Y | 4.37% / 4.54% | +3/+2bp | +3/+6bp | 强就业后前端偏鹰 | 9/4 Treasury官方收盘 |
| UST 10Y / 30Y | 4.78% / 5.24% | +1/-1bp | +5/+2bp | 前端主导bear flatten | 9/4 Treasury官方 |
| 10Y real / BEI代理 | 2.43% / 2.35% | +1/约0bp | +1/约0bp | Gold仍受real yield约束 | 9/4；BEI=名义-实际 |
| 2s10s / 2s30s / 5s30s | 41/87/70bp | -2/-4/-3bp | — | 软NFP牛陡逻辑已撤销 | 9/4计算 |
| DXY | 约99.14 | +约0.2% | 约-0.6% | 冲高回落 | 9/4晚盘估算 |
| EUR/USD | 数据不足 | — | — | 不用非同步报价 | 9/4完整收盘未独立核验 |
| USD/JPY | 约156.2 | 约+0.3% | JPY约+2.2% | 前期日元交易已兑现一段 | 9/4晚盘 |
| USD/CNH | 数据不足 | — | — | 周末不猜价 | 同步高质量收盘缺失 |
| Nasdaq | 26,506.99 | -0.29% | +0.40% | 指数抗跌 | 9/4现金收盘 |
| SOXX | 519.86 | +3.52% | 约+2% | 硬件强于指数 | 9/4现金收盘 |
| WTI / Brent | $91.48 / $96.28* | +0.2%/跨源不硬算 | 约+9.7%/+7.6% | 周末冲击尚未入价 | 9/4结算/可靠收盘口径 |
| Gold spot / Dec期货 | $4,419.09 / $4,476.60 | -1.2%/-1.4% | 周度偏弱 | 政策信用独立性减弱 | 9/4 |
| VIX | 14.53 | +1.47% | 约持平 | 事件保险仍低 | Cboe 9/4 |
| MOVE | 约73.1 | -2.1% | 约+3% | 延迟参考 | 9/4二级源，非实时 |
| HY OAS | 2.65% | 约-1bp | 极紧 | 信用未确认Risk-off | 9/3 ICE/FRED，滞后 |
| IH2609 / IF2609 | 2915.8 / 4537.4 | +0.28%/+0.01% | +0.15%/-1.22%（5D） | 大盘相对强 | 9/4 EOD |
| IC2609 / IM2609 | 7608.0 / 7468.2 | -1.27%/-1.21% | —/-2.59%（5D） | 小盘弱、远月增仓 | 9/4 EOD |
| IH/IF/IC/IM基差 | -0.274/-0.234/-0.584/-0.531% | — | — | 非独立套利极值 | 9/4 |
| HO/IO/MO ATM IV | 14.43/18.63/28.87% | -0.02/+0.68/+0.41vol | +0.48/+1.79/+2.40vol（5D） | MO左尾仍贵 | 9/4 Engine |

*Brent不同页面的活跃合约/时点口径存在差异；本期不据此计算单日收益。  

## 三、相比今晨真正发生了什么变化

1. **地缘事实质量上升，但价格尚未验证。** CENTCOM已正式确认打击三艘IRGC相关原油运输船，包含Kharg/Jask附近目标；伊朗又宣称打击美国关联船只，后者缺乏独立确认。支持油价右尾，但不证明周一一定高开或高开能维持。
2. **OPEC+的“预期不变”更强，正式会后结论仍待核验。** Reuters 9月6日称两名知情人士预计10月政策不变；截至截点未取得OPEC正式声明或Reuters会后稿。竞争解释是会后意外增供或航运改善抵消地缘溢价。
3. **中国商品全量扫描从63代码扩到77个动态合格代码。** 72个有有效20D波动/活动指标，5个（JR、PM、RI、WH、ZC）无有效流动性/近次月结构；能源化工最强，EG 5D +16.18%且涨价增仓，MA/EB虽5D +13.93%/+12.02%但1D均涨价减仓，更像趋势后段或回补，不能等同fresh long。
4. **没有新的全球行情，因此今晨排行不因“重复运行”自动升降。** 油、IH/IM、QQQ事件凸性都仍为等待触发；Gold仍在观察，旧软NFP bull-steepener继续保持撤销。

## 四、机会排行榜

| 排名 | 机会 | 总分 | 逻辑25 | 赔率25 | 催化20 | 价/Vol15 | 技术15 | 研究/证据/执行 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | WTI/Brent 30–45D供应冲击Call Spread | **97** | 25 | 24 | 20 | 14 | 14 | 待验证优势/部分/等OPEC+与重开 |
| 2 | Long IH2609 / Short IM2609 Dollar-neutral | **95** | 25 | 22 | 18 | 15 | 15 | 存在优势/充分/周一确认 |
| 3 | QQQ/NDX 10–21D PPI/CPI Failed-Rally Put Spread | **92** | 24 | 23 | 20 | 14 | 11 | 待验证优势/部分/周二确认 |
| 4 | 2s30s DV01-neutral Bear Flattener | **88** | 23 | 19 | 19 | 13 | 14 | 待触发/部分/等通胀 |
| 5 | Long AI现金流硬件质量 / Short融资Duration Beta | **87** | 23 | 20 | 18 | 13 | 13 | 待验证优势/部分/周二确认 |

分数是研究排序，不是胜率。中国化工链EG/PG延续与MA/EB回补分化属于研究观察池；因商品期权面不可执行、跨品种对冲权重未校准，不为凑榜打分。

## 五、前三名交易卡

### #1 WTI/Brent 30–45D Call Spread

**市场隐含/分歧：** 周五价格尚未包含9月5日三艘油轮被击事实；但近一周涨幅已大，市场也已包含高地缘风险。我们的分歧只在“实际航运中断的持续时间可能高于周一温和gap所隐含”，不是“任何战争新闻都应追多”。

**工具：** 买35–40Δ Call、卖15–20Δ Call；若重开后call skew/vega爆贵，改Butterfly。实际到期选择覆盖未来30–45日；无同步surface，不猜合约代码和权利金。

**入场：** OPEC+正式结果确认后，且北京时间周一06:00重开45–60分钟。WTI若在92–95温和gap后守住首小时VWAP/低点、没有可信降级，做1/3；突破96–98且伴随新的航运/保险/港口中断证据再加。若直接>100，不追。

**失效/退出：** WTI<87或Brent<88并伴通航恢复/可信停火；TP1为WTI 98–102或1.5–1.8×debit，TP2为108–115或垂直价差最大价值75%–85%；EIA节假日延后数据前先落袋1/3。

**成交情景：** 净debit≤价差宽度25%为好（理论最大毛利约3R）；25%–35%为中（约1.9–3R）；35%–40%为坏、只允许更小仓；>40%放弃。上述未扣滑点/手续费，买卖价差须计入净debit。最大损失=净权利金；+Delta/+Gamma/+Vega/-Theta。试仓损失0.40%–0.60% NAV，确认后≤1%。

**最强反证：** OPEC+可交付增供、霍尔木兹/Kharg通航改善、美国释放库存或停火同时出现。

### #2 Long IH2609 / Short IM2609

**证据：** IH 9月4日上涨且主月OI +5,199、全期限OI +9,000；IM下跌、主月OI -1,981但全期限OI +9,193，支持“近月移仓+风险重建”，而非唯一的fresh short解释。IH相对IM 1/3/5D约+1.49/+1.88/+2.74个百分点。反证是价差已扩张、周一可能均值回归。

**工具/中性：** 多12手IH2609、空7手IM2609，按9月4日收盘名义约1049.7万/1045.5万元，Dollar mismatch约0.4%；不是Beta-neutral。IH乘数300元/点，IM 200元/点。交易所最低保证金和券商加收须在下单前实时确认；保证金不是最大损失。

**入场：** 9月7日09:30后等30–45分钟；优先相对价差先回吐0.3–0.6pct后重新转强，或IH领先IM≥0.35pct且IM不能收回7500/首小时中枢。开盘relative gap>1pct不追。

**失效/退出：** 自入场relative -0.65pct止损；或“IM领先IH≥0.6pct、IM/IC fresh OI增加、MO RR25修复至>-2.5vol”三项出现两项。TP1 +1.5pct，TP2 +3.0pct，5日无扩张退出。

**成交情景：** 回吐0.3–0.6pct后转强为好，TP1约2.3R/TP2约4.6R；平开确认属中，减半；gap>1pct或MO左尾IV再跳>4vol属坏，不开。12:7组合1pct逆向约亏10.5万元，2.5pct gap压力约26.2万元，未计basis/beta/slippage；最大损失非有限。期货Greeks为+IH Delta/-IM Delta，Gamma/Theta/Vega≈0。

### #3 QQQ/NDX 10–21D Failed-Rally Put Spread

**市场隐含/分歧：** VIX仅14.53且信用极紧，定价偏向事件可控；但油运冲击、PPI/CPI、加息尾部集中在一周内。反对证据是SOXX周五+3.52%、AI硬件需求强，因此只能等failed rally，不能裸空AI基本面。

**工具：** 覆盖9月10–11日数据，买35–40Δ Put、卖15–20Δ Put；完整surface未取得，不猜strike/权利金。

**入场：** 9月8日美股现金开盘30–60分钟，QQQ先涨0.5%–1%后失守VWAP，且2Y≥4.40%或DXY≥99.3；数据后若先冲后跌回事件高点下方可加。gap down>1.5%且VIX>20不追。

**失效/退出：** 2Y<4.25%、WTI<87且QQQ收盘新高、SOXX继续领涨；TP1标的-3%或1.5×debit，TP2 -5%至-6%或价差最大价值80%。

**成交情景：** debit≤宽度30%为好（毛利约2.3R）；30%–40%为中（约1.5–2.3R）；>40%为坏/放弃。最大损失=净debit；-Delta/+Gamma/+Vega/-Theta。油Call与QQQ Put共享地缘滞胀因子，合并预算≤1.5%–2.0% NAV。

## 六、黄金专项

**评级：减弱，观察。** 强就业后现货跌1.2%而10Y real仅升1bp，说明黄金仍主要服从美元/实际利率；“政策信用期权”机制未独立成立。当前竞争解释排序：传统real-yield/USD约70%，财政/货币信用约30%，流动性和避险需求作为条件变量。

重新激活3–6M Call Spread需：Gold>4500–4525，且10Y real仍≥2.42%、DXY没有显著走弱；若只是CPI偏软、real yield下降后上涨，应归类为传统降息交易。最强推翻证据是DXY>100、real10Y>2.50%且Gold<4350。央行周频购金、同日ETF流、最新CFTC细分仓位和完整Gold IV/skew未同步核验，结构待报价。

## 七、AI股票专项

**分类：真实需求强、估值/资金成本高、硬件现金流与融资Duration分化。** 周五Nasdaq -0.29%而SOXX +3.52%，反对“AI需求已反转”；但强NFP和高real yield压制远期现金流估值。优先多已兑现FCF/定价权的芯片、网络/互连、云软件monetization，空高融资依赖/远期Capex Beta；电力基础设施须区分已签订单与纯TAM叙事。

Oracle 9月10日盘后财报是关键实验：巨额RPO是否转成现金流、Capex是否继续压FCF。若周二现金盘60分钟后quality篮子领先≥1pct，可用45–90D Call Spread + 30–60D Put Spread做低净Beta；两日逆转>3pct且10Y下行则失效。反向组合成立条件是Capex链订单/利润率上修且估值拥挤已充分出清。

## 八、中国50 / 300 / 500 / 1000专项

**偏好：IH > IF > IC≈IM；最优是IH/IM相对价值，不是追空IM。**

| 指标 | IH2609 | IF2609 | IC2609 | IM2609 |
|---|---:|---:|---:|---:|
| 收盘/1D | 2915.8/+0.28% | 4537.4/+0.01% | 7608.0/-1.27% | 7468.2/-1.21% |
| 成交量 | 38,129 | 70,771 | 108,155 | 167,832 |
| 主月OI/变化 | 66,084/+5,199 | 134,178/+2,566 | 147,105/+2,570 | 220,708/-1,981 |
| 全期限OI变化 | +9,000 | +9,948 | +15,244 | +9,193 |
| 基差 | -0.274% | -0.234% | -0.584% | -0.531% |
| 次月-主月 | -19.8点 | -27.0 | -57.6 | -64.2 |

| 期权 | ATM IV | 1D/3D/5D | RR25/BF25 | PCR-OI | 10Δ Put | Gamma节点 |
|---|---:|---:|---:|---:|---:|---|
| HO2609 | 14.43% | -0.02/+0.21/+0.48vol | -0.64/+0.63 | 0.650 | 16.75% | 2900 |
| IO2609 | 18.63% | +0.68/+1.32/+1.79 | -3.05/+0.47 | 0.735 | 22.47% | 4600 |
| MO2609 | 28.87% | +0.41/+0.53/+2.40 | -3.82/+1.17 | 0.727 | 37.09% | 7600 |

20D期指最近可审计参考为IH +0.03%、IF -1.69%、IM +1.55%；`radar_history.json`为空，所以20D wings/RR/BF/PCR/OI变化不伪造。IC没有一一对应CFFEX指数期权；MO/IO/500ETF期权只能做代理，存在Beta、基差、跟踪误差与不能完全对冲的风险。价格/OI支持风格迁移，但不能唯一识别新多、新空或回补；“Gamma节点”是绝对Gamma暴露估算，不代表已知做市商净Gamma。

基差/跨期未出现足以独立交易的极端；MO左尾昂贵，有限风险表达应选HO Call Spread+MO Put Spread而不是裸买深OTM Put。中国股指评分95，证据充分，执行为周一等待触发；条件不成立则**今日中国股指无实际可执行交易**，但研究优势仍在。

## 商品与全范围覆盖核对（行动清单前）

| 板块 | 应覆盖 | 实际取数且分析 | 数据不足/不适用 | 未入榜最值得跟踪的异常或无异常依据 |
|---|---:|---:|---|---|
| 美国利率/曲线 | 2/5/10/30Y、2s10s/2s30s/5s30s、real、BEI、期限溢价、供给/拍卖/Fed | 9项价格/曲线完成 | 期限溢价模型、实时swaptions/CTD不足 | bear flatten已发生；需PPI/CPI确认 |
| 外汇 | DXY、EURUSD、USDJPY、USDCNH、skew/carry/crowding | DXY/JPY完成 | EUR、CNH同步收盘与期权偏度不足 | JPY已兑现，不追；其余无可验证新异常 |
| AI/科技 | Nasdaq/QQQ、SOXX/SMH、芯片/设备/网络/云/软件/电力 | 指数与产业层完成 | 同步公司篮子beta/IV面不足 | 硬件强于指数，现金流/Duration分化 |
| 原油/黄金/风险 | WTI、Brent、曲线/裂解/OPEC+/航运/OVX；Gold、VIX、MOVE、HY | 价格和新闻层完成 | 油曲线/裂解/OVX、Gold skew/CFTC/ETF、CTA/dealer net gamma不足 | 油运冲击最大；Gold政策信用独立性减弱 |
| 中国股指 | IH/IF/IC/IM、HO/IO/MO、现货/基差/跨期/多周期/代理边界 | 4期指+3期权完整9/4 EOD | history空导致20D期权历史缺失；ETF期权逐合约未取 | IH/IM仍是合格候选；IC代理风险已披露 |
| 中国商品 | 动态77代码，方向/曲线/OI/活动/1/3/5/20D | 77均扫描；72有有效指标 | JR/PM/RI/WH/ZC流动性不足；期权surface/execution unavailable | 能化：EG涨价增仓最强；MA/EB涨价减仓；PG/VC价量仓活跃。黑色：SF 1D+5.06%且增仓。新能源：LC 1D-4.08%。有色：AG/AU上涨减仓。农产品无全球Top5级别edge |

中国商品77代码来自五所：CZCE 26、DCE 21、GFEX 5、INE 5、SHFE 20。展示热力图子集：SF +5.06%、LC -4.08%、PD +3.84%、PG +3.11%、V +3.07%、AG +2.24%、AU +1.97%、SA +1.79%、AO +1.39%；但扫描未限于这些品种。底层5D最强为EG +16.18%、SC +15.33%、MA +13.93%、PG +13.11%、BZ +12.49%、EB +12.02%、V +11.50%。期权执行层不可用，故这些仅为期货研究线索，不给虚假期权结构或报价。

## 旧建议台账

| idea_id | 首次/上次状态 | 当前状态 | 原因与处置 |
|---|---|---|---|
| GXR-OIL-RIGHTTAIL-20260831 | 9/6晨报排行1 | 维持、等重开 | 新数据：CENTCOM确认油轮打击；价格仍未验证 |
| GXR-CN-IHIM-20260903 | 9/5晚报/9/6晨报持有或回撤加 | 维持、降追价意愿 | 价格变化已扩张2.74pct；无新交易日 |
| GXR-US-EVENTVOL-20260905 | 周二条件试仓 | 维持 | VIX低但目标surface待报价 |
| GXR-RATES-FLAT-20260905 | 等PPI/CPI | 维持 | 无新利率价格；催化未到 |
| GXR-AI-QUALITY-20260903 | 现金盘确认 | 维持 | 需求支持、定价证据仍部分 |
| GXR-GOLD-CREDIT-20260831 | 观察 | 维持观察 | 9/4价格反对独立信用交易 |
| GXR-RATES-BULLSTEEP-20260904 | NFP后牛陡 | **已撤销，不再入场** | 新数据：NFP+16.2万且2s30s压平 |
| GXR-JPY-DOWN-20260902 | 已兑现一段 | 不追、等157.5–159反弹失败 | 价格变化/赔率下降；不假设用户持仓 |

没有成交反馈，不假设用户建立过任何真实仓位；“持有/减仓”仅指若此前按条件建立。

## 九、未来24小时及未来7日事件（北京时间）

| 时间 | 事件 | 风险动作 |
|---|---|---|
| 9/6晚间 | OPEC+核心成员会议正式结果 | 结果未确认前不挂市价油单；若政策不变仍需等price acceptance |
| 9/7 约06:00 | CME周日夜间重开；Labor Day缩短时段 | 保留凸性、降低裸Delta；45–60分钟不追首个gap |
| 9/7 09:30 | 中国现金/期指开盘 | IH/IM等30–45分钟；油敏感化工避免开盘追 |
| 9/7 | PBOC 5000亿元3M买断式逆回购等量续作 | 若小盘因流动性转强，降IH/IM确信度 |
| 9/7 | 美国Labor Day，现金股债休市 | 延后美股期权入场至9/8 |
| 9/8–10美国时段 | 3Y/10Y/30Y常规拍卖窗口 | 线性curve仓降低gross；正式公告时间优先 |
| 9/9 09:30 | 中国8月CPI/PPI | 中国方向仓降Delta，不扩大Gamma/Vega |
| 9/10 20:15 | ECB决定 | EUR/USD、DXY相关仓降Delta |
| 9/10 20:30 | 美国PPI | QQQ/rates/Gold保留有限风险凸性 |
| 9/11约00:00–02:00 | EIA节假日延后WPSR | 油Call已有利润先兑现1/3 |
| 9/11 05:00 | Oracle财报电话会 | AI quality/Capex Beta关键验证 |
| 9/11 20:30 | 美国CPI/Real Earnings | 本周最大Fed路径催化，裸Gamma降至零 |

## 十、今日行动清单

**A. 今天可以立即建立的仓位：周日主要市场关闭，没有可立即成交的新仓；若此前已按条件建立IH/IM或有限风险油凸性，仅保留原风险预算。**  
**B. 今天只应挂条件单的仓位：OPEC+结果+重开45–60分钟确认后的WTI/Brent Call Spread；周一09:30–10:15确认后的Long 12 IH2609/Short 7 IM2609；周二QQQ Failed-Rally Put Spread。**  
**C. 今天应继续观察的机会：EG/PG价量仓延续与MA/EB回补分化、2s30s通胀确认flattener、AI现金流/Duration、Gold能否在高real yield下重上4525、USDJPY 157.5–159失败。**  
**D. 今天必须避免或退出的交易：退出旧软NFP bull-steepener；避免追>5%油gap、追MO深左尾Put、追空IM、裸卖Gamma，以及把油Call/QQQ Put/前端鹰派仓当成三个独立风险因子。**

## 风险预算

试仓最大损失NAV 0.25%–0.75%；确认交易0.75%–1.50%；单一高确信主题≤2.5%–3.0%。油Call、QQQ Put与rates flattener需按“地缘通胀/Fed”合并；IH/IM与MO/小盘ETF需按“小盘Beta”合并；Gold/空美元/长债Put需按“政策信用/real-rate”合并。

## 关键来源

- [U.S. Treasury Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_yield_curve)，2026-09-04。
- [U.S. Treasury Daily Treasury Par Real Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value=2026&type=daily_treasury_real_yield_curve)，2026-09-04。
- [Reuters：OPEC+ 9月6日会前预计维持10月政策](https://www.reuters.com/business/energy/opec-set-keep-oil-output-policy-unchanged-sunday-sources-say-2026-09-06/)，2026-09-06。
- [U.S. CENTCOM：打击三艘IRGC相关油轮](https://www.centcom.mil/)，2026-09-05。
- [FT：US strikes three Iranian oil tankers](https://www.ft.com/content/7c7c07db-cde5-474d-9a20-8e2c2f273d4e)，2026-09-06。
- [CME Holiday and Trading Hours](https://www.cmegroup.com/tools-information/holiday-calendar.html)，访问2026-09-06。
- [BLS 2026 release calendar](https://www.bls.gov/schedule/2026/09_sched_list.htm)，访问2026-09-06。
- [Cboe VIX Term Structure](https://www.cboe.com/tradable-products/vix/term-structure/)，2026-09-04。
- [ICE BofA US HY OAS via FRED](https://fred.stlouisfed.org/series/BAMLH0A0HYM2)，最新2026-09-03。
- [China-Options-Engine radar_latest](https://github.com/farfromexact/China-Options-Engine/blob/ddf1ba3f220c5b803a8017fbddc843544035c92a/data/radar_latest.json)，2026-09-04。
- [China-Commodities-Engine report_input_latest](https://github.com/farfromexact/China-Commodities-Engine/blob/8f55b9943ce7d45caec1c0c6ebaddefa1554be0f/data/report_input_latest.json)，生成2026-09-06 19:04。
