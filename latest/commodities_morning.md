# 商品期货期权晨间雷达｜2026-10-14

> **截至本报告时点，无可立即执行的合格新交易。贵金属与锡夜盘继续走弱，燃料油则延续强势；但IEA月报与美国CPI同日临近，开盘追价赔率不足。**

- `prompt_version`: `radar_2026-10-12_stock_v1`
- 生成时间：2026-10-14 07:03（北京时间）；研究截点：2026-10-14 07:00。
- 最近完整中国EOD：2026-10-13；当前交易日Night Session：2026-10-13晚至10月14日凌晨，归属2026-10-14交易日；下一窗口：08:55集合竞价、09:00日盘。
- 当前regime：国内高波动品种分化；能源价格—曲线强但外盘内部冲突；贵金属与锡夜盘弱；期权执行层不可用。

最接近触发的三项是：AG2612反抽失败空头、FU2611回踩多头、OI701结构多头。它们均需09:30—09:45确认；当前没有可直接建立的新仓。

## 二、数据质量与覆盖

### 2.1 固定输入版本

|仓库|本次固定ref|实际读取|
|---|---|---|
|Global-Cross-Asset-Radar|`b8614d673a10b39cecd80b8392fd0433c7539bad`|`manifests/reports.json`、10月13日晨/晚报及JSON、archive policy、归档说明、schema/template|
|China-Commodities-Engine|`7f36ceb6e4d6ca1677c226db12259210457549b0`|`data/report_input_latest.json`、`data/last_run_status.json`、`data/night_session/last_run_status.json`、`data/radar_latest.json`；下钻`data/latest.json`、`data/night_session/latest.json`、`data/contract_meta.json`|
|China-Stock-Engine|`67678376a04e75a8c6911b52349e5ac337427a33`|首层5文件；按索引读取紫金矿业、宝钢股份两个实际公司分片|

商品统一输入`requested_date=2026-10-13`，`generated_at=2026-10-14T06:12:33+08:00`。Futures/Market State为10月13日且fresh；Physical与External均于10月14日06:12生成、原始观察日10月13日；Options仍是10月9日旧截面。

### 2.2 核心质量闸门

- Futures：五所、806份合约、77个品种；`full_market_ready=true`、`source_date_match_pct=100%`、critical errors=0、excluded exchange=0。4条OHLC占位已从异常排序中排除；仓单有5条carry-forward。
- `official_complete=false`主要来自期权、基差、会员排名及部分参数模块，并不否定已验证核心期货EOD。五所EOD源日期均为10月13日。
- Physical：20个目标中18个fresh、2个unavailable；可得基差均为C级，地区、品质、税和交割地不齐，只作context。CZCE当日仓单可用；GFEX的LC/PS/SI等仓单仍停留9月1日且stale，不计方向证据。
- External repo层：17/22个目标fresh、5个unavailable，均为`context_only`，没有可执行进口平价。
- Contract metadata：partial；有效合约匹配73.45%，乘数/最小变动/保证金/限幅覆盖仅30.15%，夜盘与交割单位覆盖不足。未知参数不推断。

### 2.3 Night Session质量

`trading_date=2026-10-14`，`night_session_date/session_start_date=2026-10-13`，生成于05:59；`data_fresh=true`、`validation_passed=true`、`published=true`。共417份合约、37个品种有有效夜盘记录；`missing_timestamp/price/quote=0`，但214份具体合约`query_error/unresolved`，故`coverage_complete=false`。51.737%不是“完整率”，无夜盘与合法窗口外合约也包含在分母中。

重点准确合约AG2612、SN2611、OI701、LU2612、CU2611、RU2701、FU2611均已核到fresh记录；DCE的BZ2611、LH2701具体夜盘未能确认，本期不以媒体概数替代。

### 2.4 Options与Stock

- Options：最新正式有效层仍为10月9日，14,074份合约、185个series；181个surface-ready、41个positioning-ready、0个execution-ready；IV覆盖98.78%、OI覆盖69.36%、bid/ask覆盖0。10月13日采集attempt有11,314条但未发布，不能覆盖正式截面。所有结构均是研究表达，禁止填权利金、净支出、滑点或Greeks。
- Stock：股票交易日为10月12日，research_asof为10月13日07:36。5,561条有报价，原始1D/3D较完整；5D/20D、复权、RV、ADT、行业、证券状态和实时执行检查均未就绪。公司目录只有紫金矿业和宝钢股份，不代表全市场公司覆盖。

## 三、商品仪表盘（展示12项；全量扫描见覆盖核对）

`1D/5D`均为同一具体主力的结算收益；Night主锚为相对前收。`—`表示未能在统一层确认同合约夜盘，不表示制度无夜盘。

|板块|品种/合约|10/13 close/settle|1D / 5D|volume / OI / ΔOI|EOD curve；basis/Physical|10/14 Night close；vs close/vs settle；ΔOI|07:00海外与Options|09:00信号|
|---|---|---:|---:|---:|---|---|---|---|
|贵金属|AG2612|14743 / 14688|-1.12% / -1.46%|232041 / 284275 / -3783|近月contango -0.50%；basis缺|14466；-1.88%/-1.51%；+7149，02:30 fresh|COMEX银59.161、-1.63%；旧surface可研究、execution否|偏低开；等30分钟反抽失败|
|燃料油|FU2611|5268 / 5325|该合约close +3.50%；产品主力5D +16.40%|499133 / 112867 / EOD精确ΔOI未列|FU2611-12 backwardation 8.01%；现货仅绝对值context|5438；+3.23%/+2.12%；+5081，23:00 fresh|Brent -0.9%、WTI +0.4%、柴油约+5%；旧期权execution否|高开但不追；等30分钟|
|有色|SN2611|396500 / 397220|-0.19% / -2.88%|98319 / 32769 / -1395|近月backwardation仅0.04%；实体缺|383250；-3.34%/-3.52%；+3907，01:00 fresh|LME锡精确收盘未验证；旧期权execution否|低开风险；等30分钟反抽|
|油脂|OI701|10399 / 10394|+0.19% / +3.48%|327030 / 350947 / +17154|backwardation 2.60%，z=2.08；仓单1274、日变0|10446；+0.45%/+0.50%；+5484，23:00 fresh|CBOT豆油/大豆偏弱代理；旧surface、execution否|小高开；等30分钟curve确认|
|畜牧|LH2701|10605 / 10685|-2.60% / -5.69%|115309 / 171226 / +9703|LH2611-2701 contango 4.63%；实体缺|—；DCE具体合约未确认|海外映射不适用；DCE期权缺|平/低开；只等反抽失败|
|原油|SC2612|727.9 / 732.0|+3.17% / +7.44%|58856 / 27036 / +2046|backwardation 2.91%；Physical缺|同合约—；代表SC2611为753.3、+1.21% vs close|Brent105.69跌0.9%，WTI94.14涨0.4%；SC期权正式层旧|内外冲突，不追首跳|
|低硫油|LU2612|5940 / 5965|+6.37% / +12.23%|169614 / 78533 / +13678|backwardation 4.41%；Physical缺|5916；-0.40%/-0.82%；-2459，23:00 fresh|Brent回落反对；期权无执行报价|偏低/平开，等30分钟|
|芳烃|BZ2611|9685 / 9524|+2.36% / +10.54%|121529 / 28047 / +6812|backwardation 8.11%；Physical缺|—；DCE query error|油价分歧；DCE期权缺|昨晚条件状态未知，重新报价|
|铜|CU2611|110990 / 110900|+0.12% / +1.46%|70492 / 195710 / +561|backwardation 0.60%；C级basis仅context|110730；-0.23%/-0.15%；-922，01:00 fresh|LME 3M约14618.5、+0.54%；期权旧且不可执行|内外冲突，旧多头继续取消|
|橡胶|RU2701|20305 / 20515|-1.28% / +7.75%|596979 / 172811 / -4826|contango 3.90%；Physical缺|20330；+0.12%/-0.90%；-336，23:00 fresh|SGX TSR20代理+0.23%；期权旧且不可执行|相对close弹性弱，不追反弹|
|新能源|LC2701|107060 / 105480|-3.12% / -11.76%|314846 / 422392 / -6647|近端contango 0.62%；GFEX仓单stale|制度无夜盘|海外/实体不足；旧surface、execution否|09:45后仅观察|
|建材|SA701|961 / 975|-2.01% / -3.75%|1179690 / 1375850 / +93033|contango 0.95%；仓单3200、日变0|960；-0.10%/-1.54%；+21786，23:00 fresh|无可靠跨市映射；期权旧|相对close几乎无新增，勿把vs settle当新跌势|

## 四、相对上一期真正变化

1. **AG空头由“昨日未触发”转为今晨重新等待验证。** 10月13日白天未跌破旧触发14679；今夜收14466、较前收-1.88%，COMEX银亦收跌1.63%。这是新增的价格层与海外层支持，但不代表09:00已成交。
2. **FU成为能源链最强的新增弹性。** FU2611夜盘较前收+3.23%、OI增加5081，且EOD近月backwardation约8%；然而Brent回落、WTI小涨、柴油显著走强，说明这是产品与品种分化，不宜解释为普遍原油多头。
3. **SN出现全夜盘最大跌幅。** SN2611较前收-3.34%、OI增加3907；但EOD曲线几乎平坦且LME锡精确收盘未核，只有第一层支持，不能给70分以上。
4. **BZ与LH旧条件均失去可验证夜盘路径。** DCE具体夜盘查询失败，昨晚BZ 21:45触发状态未知；LH仍保留到09:30的反抽失败方案，但不得宣称夜盘确认。
5. **CU多头继续取消。** LME铜仍强，但CU2611夜盘较前收-0.23%，内外不同向；昨日111100接受条件仍未获有效确认。
6. **期权没有变成可执行工具。** 10月13日attempt未正式发布，正式层仍为10月9日且bid/ask为零；本期新增行情使旧moneyness更不可直接用于下单。

## 五、产业链地图

|链条|方向与最强/最弱|价格—Night—curve|实体/仓单|海外/期权|Stock利润桥|最大缺失；置信度|
|---|---|---|---|---|---|---|
|原油—燃料油—沥青|最强FU，LU夜盘转弱；SC内外冲突|FU2611夜盘+3.23%、backwardation 8.01%；LU -0.40%；SC代表月+1.21%|FU现货绝对值仅context，无可比变化|Brent跌、WTI涨、柴油强；期权不可执行|目录无能源公司，不能据此称无受益者|裂解、库存、精确进口成本缺；中等|
|贵金属|AG弱于AU|AG夜盘-1.88%，contango；AU夜盘-0.79%|无有效实体层|COMEX银-1.63%、金-0.31%；CPI前凸性风险高|紫金金业务仅条件暴露，旧半年报不是新催化|当前期权报价、真实利率最新官方值缺；中高|
|有色—铜/锡|铜外强内弱；锡夜盘最弱|CU夜盘-0.23%但backwardation；SN夜盘-3.34%、curve近平|CU spot仅C级basis；无锡实体|LME铜+0.54%；锡精确外盘缺|紫金铜利润桥支持长期暴露，但不优于CU直接工具|矿山/冶炼量价、LME锡缺；铜中、锡低|
|油脂油料|OI/RM相对强|OI夜盘+0.45%、backwardation 2.60%；RM夜盘+0.55%|OI仓单不变、RM仓单-1070，仅仓单不当社会库存|CBOT大豆/豆油偏弱；DCE期权缺|目录无农业公司|进口平价、压榨利润、社会库存缺；中等|
|黑色—建材|JM相对强，SA/FG偏弱|JM EOD+0.68%且backwardation；SA日跌、夜盘相对close仅-0.10%；FG小反弹|CZCE仓单可用但钢矿实体不足|SGX铁矿代理偏弱；期权局部缺|宝钢2026H1利润/现金流同比承压，只验证利润挤压，非即时表达|钢材利润、港库、焦煤现货缺；中低|

Stock决策贡献：紫金矿业2026H1营收、归母净利、经营现金流同比约+15.78%/+68.17%/+92.41%，但自产矿与冶炼、成本、套保和少数股东尚未量化；宝钢同期归母净利与经营现金流同比-6.30%/-11.01%，支持钢材—原料利润挤压的方向背景。两者都是已公布半年报，不是本期新催化，且证券状态/实时执行未核，均不进入统一Top5。

## 六、机会排行榜

分数是研究排序，不是胜率、期望收益或仓位。分项顺序为逻辑25/赔率凸性25/催化20/价格曲线波动15/拥挤技术15。

|排名|idea_id；方向/期限|分项=总分|工具/限损|有效支持层；反证/缺失|三轴状态|
|---:|---|---:|---|---|---|
|1|`COM-E-AG2612-OVERSEAS-FADE-SHORT-20261012`；空，1—3D|18/17/16/12/9=**72**|AG2612期货；止损不封顶。put spread仅研究|3层：价量OI、contango、COMEX银；反证为CPI/地缘上跳与期权报价缺|判断：存在待验证优势；证据：部分；执行：等09:30反抽失败|
|2|`COM-M-FU2611-TIGHT-PRODUCT-LONG-20261014`；多，1—3D|18/17/15/11/8=**69**|FU2611期货；止损不封顶|2层：价量OI、backwardation；反证为Brent回落、临近交割、参数缺|判断：存在待验证优势；证据：部分；执行：等09:30回踩|
|3|`COM-M-OI701-CURVE-LONG-20261014`；多，2—10D|18/16/13/12/9=**68**|OI701期货；止损不封顶|2层：价量OI、曲线；反证为CBOT偏弱、实体不足、DCE期权缺|判断：存在待验证优势；证据：部分；执行：等09:30—09:45|
|4|`COM-E-LH2701-CONTANGO-BREAK-SHORT-20261013`；空，2—10D|17/16/13/11/9=**66**|LH2701期货；止损不封顶|2层：EOD价量OI、contango；夜盘/实体/期权缺|判断：存在待验证优势；证据：部分；执行：等09:30且参数待核|
|5|`COM-M-SN2611-NIGHT-BREAK-SHORT-20261014`；空，1—3D|15/15/12/9/8=**59**|SN2611期货；止损不封顶|1层：价格成交OI；curve中性，外盘/实体/期权缺|判断：证据不足；证据：不足；执行：仅早期异常观察|

没有80+候选；唯一70+候选仍缺当前执行报价/参数并面对CPI事件，不构成立即新仓。

## 七、研究/交易卡

### 卡1｜AG2612反抽失败空头（72）

- 事实：10月13日close/settle=14743/14688；Night OHLC=14644/14662/14355/14466，较前收-1.88%、较结算-1.51%，Night ΔOI=+7149。COMEX银结算59.161、-1.63%。EOD近月contango约0.50%。
- 市场定价：夜盘已预交易银价弱势，09:00低开并非“新信息”；若开盘直接砸向14380以下，赔率恶化。
- 推断/分歧：CPI前美元与名义收益率没有同步走强，银价下跌不能只归因宏观；工业属性与风险偏好可能仍在被重估。最强反证是CPI偏软、美元/实际利率急跌或地缘升级触发金银反抽。
- 最佳表达：AG2612期货空；1手。期权put spread只有取得当日两腿bid/ask、IV/skew和总净支出后才可替代。当前无权利金。
- 入场：09:30后反抽14550—14650失败、再跌破14460时分两批；开盘低于14380不追。好/中/坏成交=14580/14480/<14380放弃。
- 风险与退出：计划止损15020；逻辑失效仍沿用14995上方且COMEX银>61.3。TP1=14150，TP2=13750；到10月14日20:15前未扩大利润则减半或退出，CPI前不留新增满额裸Delta。
- 情景R：以14580入、15020止损计计划1R=440点；TP1约0.98R、TP2约1.89R，未计滑点/gap。低开追单会显著降低R。
- 参数/压力：last trading day=2026-12-15；仓库未确认multiplier、tick、margin、limit和交割单位。1/2个涨跌停压力损失因此只能按“名义敞口×实际限幅”在盘前重算；止损不保证最大亏损。

### 卡2｜FU2611回踩多头（69）

- 事实：10月13日close/settle=5268/5325；Night OHLC=5272/5466/5272/5438，较前收+3.23%、较结算+2.12%，Night ΔOI=+5081。EOD FU2611-2612 backwardation约8.01%。
- 市场定价：高硫燃料油已经吸收了大量产品紧张溢价；Brent反而收跌0.9%，WTI微涨且柴油约涨5%，指向产品分化而非统一原油牛市。
- 推断/分歧：如果FU在Brent回落时仍守住5380并维持深backwardation，说明近端燃料油约束比原油方向更重要。竞争解释是临近交割和区域物流造成的短期挤压，持续性很低。
- 最佳表达：FU2611期货多，1手；由于10月30日最后交易日，必须主动roll，且不能把未报价call spread当限损替代。
- 入场：09:30后回踩5380—5430守住、近月backwardation仍≥6%；突破5466后不直接追，等回测。>5500或gap>2%放弃。
- 风险与退出：计划止损5260；收盘/30分钟有效跌回5325且curve<4%逻辑失效。TP1=5600、TP2=5850；10月16日前不创新高退出，最晚10月20日前roll/平仓。
- 情景R：以5400入、5260止损，1R=140点；TP1约1.43R、TP2约3.21R，未计滑点。参数缺失使现金R待报价。
- 参数/压力：last trading day=2026-10-30，交割与流动性风险高；multiplier/tick/tick value/margin/limit在仓库为空，盘前必须查官方动态参数。1/2限幅压力损失未能可靠量化。

### 卡3｜OI701结构多头（68）

- 事实：10月13日close/settle=10399/10394；Night OHLC=10429/10473/10413/10446，较前收+0.45%、较结算+0.50%，Night ΔOI=+5484。EOD主力ΔOI=+17154，near-next backwardation=2.60%、z=2.08；仓单1274、日变0。
- 市场定价：国内菜油结构偏紧已被部分价格化；CBOT大豆/豆油偏弱，外盘没有确认中国夜盘强势。
- 推断/分歧：若09:00后OI能抗住外盘偏弱且backwardation维持，国内特定供需的定价权高于泛油脂beta。反证是外盘继续下跌、OI回落且曲线收窄。
- 最佳表达：OI701期货多，1手；不把C级basis或未对齐进口平价当套利。DCE期权链缺失。
- 入场：09:30—09:45守住10410—10430并突破10473后回测；>10520放弃追价。好/中/坏=10420/10470/>10520放弃。
- 风险与退出：计划止损10280；curve<1%或日内有效跌破10350逻辑失效。TP1=10600、TP2=10850；5D不创新高退出，最长10D。
- 情景R：以10420入、10280止损，1R=140点；TP1约1.29R、TP2约3.07R，未计滑点。
- 参数/压力：仓库确认multiplier=10吨/手、tick=1元/吨、tick value=10元、last trading day=2027-01-14；margin、price limit、night session字段未确认。名义金额约104,200元/手；按实际保证金与限幅盘前重算1/2限幅压力。

风险预算：单一试仓计划损失NAV 0.25%—0.50%，三项均未达到确认仓门槛；AG与贵金属、FU与能源共同因子需合并，单一主题总风险不得超过2.5%—3.0%。

## 八、商品期权专项

- 截面：正式层为10月9日EOD，不是10月13日/14日当前报价；IV覆盖高但bid/ask为零。
- IV-RV：只有具体series `surface_ready=true`才可比较；夜盘大幅改变AG、SN、FU的moneyness，旧ATM、RR25、BF25不能冒充今晨可比执行面。
- Event convexity：IEA月报与CPI同日，理论上提高能源/贵金属事件凸性价值；但没有当日权利金，无法证明长波动便宜。
- 结构：AG put spread、FU/OI call spread仅是有限损失研究框架。执行前必须取得准确underlying、expiry、strike/Delta、两腿bid/ask、净支出、最大损失和行权交割规则。
- 回避：裸卖短到期期权、用vendor Greeks当模型Greeks、从OI推做市商净Gamma、把10月9日IV当当前ATM。

## 九、09:00开盘风险地图

严格三层：Previous China EOD=10月13日；Current T Night=归属10月14日；Overseas=10月13日国际收盘至07:00。Night已经交易过的信息不得再当09:00新增。

|品种|Previous EOD|Current T Night|07:00 Overseas|开盘判断与等待|
|---|---|---|---|---|
|AG|EOD偏弱、contango|较前收-1.88%，已大幅预交易|COMEX银-1.63%|偏低开；不追空首跳，等30分钟反抽失败|
|FU2611|日盘强、backwardation深|再涨3.23%，多数利多已定价|Brent跌、WTI涨、柴油强|高开；等30分钟看5380与curve，首跳不追|
|SN|EOD小跌、curve近平|再跌3.34%，夜盘主导价格发现|LME锡精确收盘缺|低开风险；等30—45分钟，外盘缺口限制执行|
|OI|EOD小涨、backwardation|+0.45%，强化但幅度有限|CBOT油籽偏弱|小高/平开；等30分钟内外冲突解决|
|SC/LU|EOD大涨|SC代表月+1.21%，LU -0.40%|Brent跌、WTI涨|分化开盘；SC/LU均等30分钟，不把SC2611代SC2612|
|CU|EOD微涨、backwardation|CU2611 -0.23%|LME铜约+0.54%|平开/冲突；等15—30分钟，不恢复旧多|
|RU/NR|EOD转弱、contango|RU +0.12%、NR +0.17% vs close，弹性弱|TSR20代理小涨|近乎平开；等30分钟curve，不追反弹|
|LH/BZ|EOD分别弱/强|具体DCE夜盘缺|无直接海外确认|09:30重新定价；不能沿用昨晚已过触发|
|LC/EC|EOD弱|制度无夜盘|代理有限|09:45后观察，不抄底首跳|

## 十、未来24小时与7天事件、旧观点与覆盖核对

### 10.1 事件日历（北京时间）

- **10月14日16:00 IEA Oil Market Report**：能源Delta/Vega事件；FU/SC/LU若上午触发，发布前降新增裸Delta或缩小规模。[IEA官方](https://www.iea.org/data-and-statistics/data-product/oil-market-report-omr)
- **10月14日20:30 美国9月CPI与实际收入**：贵金属、美元、实际利率核心事件；AG条件单若触发，20:15前重新评估，期权仅限已确认净支出的结构。[BLS日历](https://www.bls.gov/schedule/2026/)
- **10月15日20:30 美国PPI**：CPI后第二轮通胀验证；避免把单次数据冲击当趋势。
- **10月16日00:00 EIA周度石油状态报告**：假日顺延；能源链在数据后至少等15—30分钟。[EIA官方](https://www.eia.gov/petroleum/supply/weekly/schedule.php)
- **10月16日 USDA出口销售（具体北京时间待核）**：油脂饲料背景；不在时点未核时预设盘中触发。
- **10月17日03:30 CFTC COT**：仅作滞后拥挤背景，不作即时入场。[CFTC官方](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm)
- 未来7天继续核验Hormuz船流、沙特/也门冲突、俄柴油交易与OPEC+实际产量；新闻只有在价格、物流或实体吞吐获得独立验证后才升级证据层。

### 10.2 旧观点台账

- CU2611旧条件多：未触发并继续取消；LME强但中国夜盘弱，不恢复。
- SC2612旧条件多：昨日Brent未达要求；今晨同合约Night缺，继续观察，不认定成交。
- AG2612旧条件空：昨日白天未触发；今晨有新夜盘/海外证据，保留同一`idea_id`重新等09:30，不追低开。
- LC2701反弹观察：curve已转contango，原反弹分歧消失；仍为低分观察。
- BZ2611昨晚条件多：DCE夜盘路径不可核，状态未知且窗口已过；必须09:00后重报，不沿用9758条件单。
- LH2701空头：保留原反抽失败触发；无夜盘确认、参数仍缺。
- LU2612旧多：Night转弱且Brent回落，降出榜；不按昨晚条件追价。

### 10.3 覆盖核对

|板块|应覆盖|实际取数并分析|数据不足/不适用|未入榜最值得跟踪|
|---|---:|---:|---|---|
|黑色建材|I/JM/J/RB/HC/FG/SA/SF/SM（9）|9|高质量basis、社会库存、DCE夜盘部分缺|SA价跌仓增但夜盘相对close几乎无新增；JM价格/OI强|
|有色贵金属|CU/BC/AL/AO/AD/ZN/PB/NI/SN/SS/AU/AG（12）|12|LME锡等部分精确收盘、当日期权报价缺|SN夜盘破位；CU内外冲突；ZN库存反对|
|能源化工|SC/FU/LU/BU/PG(Prompt中的LPG)/PX/TA/PF/PR/MA/PP/L/V/EG/EB/RU/NR/BR/SH/UR/SP（21）|21|进口平价、裂解、社会库存、DCE夜盘部分缺|FU最强；LU转弱；MA vs close上升但vs settle近零|
|新能源材料|LC/SI/PS及GFEX新增PD/PT（5）|5|GFEX仓单stale；无夜盘|LC持续弱且contango，不抄底；PD弱势|
|农产品油脂畜牧|A/B/M/RM/Y/P/OI/C/CS/LH/JD/CF/CY/SR/AP/CJ/PK（17）|17|DCE夜盘/期权、进口平价、加工利润缺|OI/RM结构强；LH跌价增仓线索；AP/CJ弱|
|航运|EC（1）|1|无夜盘、跨市场映射不足|EC 5D偏弱、深曲线不可直接当套利|
|动态新增|JR/PL/PM/RI/RS/WH/ZC/LG/RR/PD/PT/OP/WR及实际PG映射等|均纳入77品种扫描|部分低流动性/无有效curve|PL夜盘+1.63%但流动性与实体不足，不入榜|

指定63个文本代码中“LPG”在实际交易所代码按PG处理；63个逻辑品种均已覆盖。77个引擎品种均完成价格/curve/量仓初筛；Options、Physical、External、Stock只在各自可得范围内分析，缺失没有被改写为“无机会”。

### 10.4 关键来源

- [China-Commodities-Engine统一输入（固定ref）](https://github.com/farfromexact/China-Commodities-Engine/blob/7f36ceb6e4d6ca1677c226db12259210457549b0/data/report_input_latest.json)
- [核心期货EOD（固定ref）](https://github.com/farfromexact/China-Commodities-Engine/blob/7f36ceb6e4d6ca1677c226db12259210457549b0/data/latest.json)
- [Night Session（固定ref）](https://github.com/farfromexact/China-Commodities-Engine/blob/7f36ceb6e4d6ca1677c226db12259210457549b0/data/night_session/latest.json)
- [Reuters：10月13日油价与柴油/地缘分歧](https://www.reuters.com/business/energy/oil-ticks-lower-russia-diesel-supply-prospects-counter-gulf-supply-risks-2026-10-13/)
- [WSJ：COMEX金银10月13日结算](https://www.wsj.com/finance/commodities-futures/gold-falls-as-markets-focus-on-u-s-data-bb4eb024)
- [LME铜](https://www.lme.com/metals/non-ferrous/lme-copper)
- [紫金矿业2026年半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225550244.PDF)
- [宝钢股份2026年半年报](https://static.cninfo.com.cn/finalpage/2026-08-22/1225489250.PDF)

A. 今天没有应立即建立的新仓位。
B. 今天只应挂条件单的仓位：09:30后AG2612仅反抽14550—14650失败并再破14460时空；FU2611仅回踩5380—5430守住且backwardation≥6%时多；OI701仅守住10410—10430并突破10473后多，均须人工核验参数与报价。
C. 今天应继续观察的机会：SN2611夜盘破位、LH2701反抽失败、SC/LU内外冲突、CU外强内弱、RU/NR相对close弹性弱，以及紫金/宝钢利润桥是否出现新公司事实。
D. 今天必须避免或退出的交易：避免9:00首跳追AG空或FU多、沿用已过的BZ/LU昨晚条件、抄底LC、使用10月9日期权面下单；若此前已按条件建立与本报告相反的AG多头，应按原失效纪律退出而非机械反手。
