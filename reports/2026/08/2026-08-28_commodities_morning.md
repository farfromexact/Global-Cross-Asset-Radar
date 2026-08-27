---
report_date: 2026-08-28
edition: commodities_morning
generated_at_bjt: 2026-08-28T07:09:06+08:00
commodity_trade_date: 2026-08-27
commodity_data_fresh: true
commodity_history_record_count: 20
archive_status: success
---

# 全球商品期货期权高风险机会雷达｜晨间版｜2026-08-28

> **数据截点：** 中国最近完整EOD=2026-08-27；中国夜盘采用公开可验证行情；海外增量截至北京时间约07:00。China-Commodities-Engine 当前 `report_input_latest.json` 为空，04:30左右根流水线又提前请求2026-08-28 EOD并失败，因此日线/Market State只使用8月27最后完整快照，不把失败的8月28根状态当作市场数据。

## 一、今日一句话结论

**今天有值得承担小风险的条件机会：SA701失败反弹空第一，SC2610高开后回撤承接多第二，JM2701回撤确认多第三；全部必须等9:00后30—45分钟，禁止开盘追价。**

## 二、数据质量与覆盖说明

第一读取层已检查 `data/report_input_latest.json`、`data/last_run_status.json`、`data/radar_latest.json`。今晨 `report_input_latest.json` 内容为空；根 `last_run_status` 为2026-08-28、`data_fresh=false`、`full_market_ready=false`、critical errors=15，原因是五所日线在收盘前被错误请求为8月28并返回0条。这个失败不代表8月27EOD失效。

本期中国EOD基线锁定到8月27最后有效快照：五所SHFE/INE/DCE/CZCE/GFEX完整，803个期货合约，source-date match=100%，`full_market_ready=true`、critical errors=0、unknown/duplicate/invalid OHLC/negative volume-OI均为0。历史同合约1D/3D/5D/20D可用，近月—次近月curve始终是期货期限结构，不等于现货基差。

Physical今晨requested_date=2026-08-28，20个目标仅4个映射、4个native-frequency fresh。最重要的新变化是：玻璃企业周度库存从8月21日7441.4降至8月28日7404.9，约-0.49%周环比；TA加工费由586.52升至677.532元/吨，约+15.5%。JM仓库内NBS旬度现货仍只是8月20日数据。周频/旬频fresh不等于“今天刚变化”。

External今晨6/22映射，其中5条fresh、1条stale；Brent/LME铜/SGX铁矿/USDCNH/DXY仍主要是8月26日收盘背景，故8月27海外增量使用Reuters等实时网页补充。Options为8月27 T日全市场链：22,348合约、376 series、64/64品种，IV coverage 98.33%、OI coverage 67.87%，但 `surface_latest.json` 当前为空，global surface_ready=false、positioning_ready=false、bid/ask coverage=0、execution_ready=false、dealer gamma direction unknown。因此本期不输出ATM IV、RR25/BF25、PCR、dealer Gamma、具体strike或权利金。

## 三、商品仪表盘

| 板块 | 合约 | 8/27 EOD / 夜盘 | 1D/5D与OI | Curve / Physical | 今晨信号 |
|---|---|---|---|---|---|
| 纯碱 | **SA701** | EOD close/settle **1011/1016**；夜盘主连约-0.49% | EOD约-2.21%；ΔOI **+10.66%** | Contango约3.23%；厂家库存187.27万吨、周四同比上周+1.51%，产量+2.72%、利用率+2.13pp | **78：失败反弹空** |
| 原油 | **SC2610** | EOD close/settle约**576.5/573.7**；夜盘 **601，+4.76%** | 日盘已反弹，夜盘再跳升 | Brent 8/27结算89.70、WTI 83.53；Hormuz船流仍低于常态 | **77：高开回撤承接多** |
| 焦煤 | **JM2701** | EOD close约**1609**；夜盘约**+1.88%**，22:57报1618 | 日盘价涨、ΔOI约+7.37% | Back约1.04%；Mysteel样本原煤/精煤库存周降 | **75：回撤确认多** |
| 棉花 | CF701 | EOD 17030/17020；夜盘+0.47% | EOD +0.65%，ΔOI +4.21% | Contango约1.63%；新疆高温干旱威胁单产 | **69：两层确认观察** |
| 菜粕 | RM611 | EOD 2348/2335；夜盘主连约-0.09% | EOD +2.32%，ΔOI +0.20% | Back约3.08%，直接Physical仍缺 | **68：不追强** |
| 豆粕 | M2701 | EOD 3355/3324 | EOD +1.78%，ΔOI +3.88% | Contango约1.17%；天气有利多但国内压榨/库存闭环缺 | 68：观察 |
| 玻璃 | FG701 | EOD 909/906；夜盘+0.88% | EOD OI -2.42% | Contango约2.02%；周度企业库存约-0.49% | **前期空头继续降级** |
| 乙二醇 | EG2610 | EOD 5028/5077，约-3.24% | OI约-7.49% | Back约4.22%；华东主港库存低 | 去杠杆与紧结构冲突 |
| 燃油 | FU2611 | EOD 3675/3687；夜盘主连-1.76% | EOD OI约-6% | 新加坡总油品库存+4%，高硫库存连续第二周升 | **弱于原油** |
| 有色 | CU2610 | 夜盘主连108590，+0.18% | OI约21.35万 | LME铜背景仍高位；无高质量进口平价闭环 | 观察 |
| 贵金属 | AU/AG | 沪金夜盘-0.18%，沪银+1.35% | — | 美元偏弱但22:00 Warsh讲话 | 事件等待 |
| 新能源 | SI/LC | 8/27 EOD分化 | — | Physical映射不足 | 数据不足，不强行判断 |

## 四、相比上一交易日/今晨真正变化

**1. SA701从69分观察升级到78分。** 昨晚只有“价跌仓增+Contango”两层，今晨补上了方向性实体证据：隆众口径本周纯碱产量76.62万吨、环比+2.72%，产能利用率80.44%、+2.13个百分点；厂家库存187.27万吨，较上周四增加2.78万吨、+1.51%。同时夜盘纯碱仍跌0.49%。这是价格/OI、curve、实体供需三层同向，但1000元附近低估值意味着只能等失败反弹，不能追空。

**2. 能源出现极端内部分化。** Reuters显示8月27 Brent结算+2.1%至89.70美元/桶、WTI +1.6%至83.53；SC2610中国夜盘收601、+4.76%。但FU夜盘反而跌1.76%，新加坡油品总库存周增4%至3918万桶、高硫燃料油库存升至1924万桶。上游地缘风险溢价与成品油库存压力同时存在，因此“多SC/空FU”值得研究，但在没有稳定beta/裂解配比前不作为正式双腿交易。

**3. JM2701把强势延伸到夜盘，而且有实体库存配合。** 8月27日盘close约1609，夜盘约+1.88%；此前EOD ΔOI约+7.37%、近端Backwardation约1.04%。Mysteel 523家炼焦煤矿山样本原煤库存周降5.8万吨、精煤库存周降21.1万吨。问题是8月反弹已经很大，故只做回撤确认，不做突破追价。

**4. FG空头逻辑进一步被削弱。** 夜盘玻璃+0.88%，最新周度企业库存从7441.4降至7404.9，约-0.49%；而8月27 EOD已经是价稳仓减、Contango收窄。前两天的FG失败反弹空现在不应继续机械滚动。

**5. CF仍是天气多头观察，但严格按证据纪律只能69。** 价涨仓增和夜盘+0.47%是一层，Reuters对新疆高温/干旱威胁棉花单产是实体供给层；但curve仍Contango，仓单/高质量basis和当前ICE棉价映射没有闭环，因此不人为凑第三层。

## 五、产业链地图

| 产业链 | 当前方向 | 最强/最弱 | Price/Curve | 实体/海外 | 最大缺口 | 置信度 |
|---|---|---|---|---|---|---|
| 纯碱—玻璃 | **SA空、FG空头降级** | 弱SA / 强FG夜盘 | SA价跌仓增+Contango；FG反弹 | SA产量/库存上升；FG库存下降 | 现货高质量basis、玻璃订单 | **高/中** |
| 原油—燃料油 | **上游强、产品弱** | 强SC / 弱FU | SC夜盘+4.76%，FU-1.76% | Hormuz风险未消；新加坡库存上升 | 裂解、beta配比 | **中高** |
| 双焦 | **偏多但拥挤** | JM > J | JM价仓+Back同向 | 矿山库存下降；需求仍可能被钢材弱势证伪 | 钢厂利润/补库持续性 | **中高** |
| 油粕饲料 | 偏多但curve分化 | RM/M强 | RM Back、M Contango | 中国作物天气风险 | 进口、压榨、港口库存 | 中 |
| 贵金属 | 事件等待 | AG相对强 | 夜盘银涨金跌 | 22:00 Warsh/Jackson Hole | 实际利率reaction | 中低 |

当前regime：**地缘驱动原油重新获得风险溢价；中国化工从“全面去风险”转成品种分化；SA的供给宽松最干净；双焦供给紧与需求证伪风险并存；农产品天气风险仍在但期限结构未普遍确认。**

## 六、机会排行榜

| Rank | 机会 | Score | Fresh层 | 方向 | 阶段 | 工具 | 数据惩罚 |
|---:|---|---:|---:|---|---|---|---|
| **1** | **SA701 失败反弹空** | **78** | **3** | 空 | 条件试仓 | SA701期货 | 低价供给收缩/政策反身性；动态保证金需确认 |
| **2** | **SC2610 高开后回撤承接多** | **77** | **3** | 多 | 条件试仓 | SC2610期货 | 夜盘已+4.76%，追价赔率差；地缘headline gap巨大 |
| **3** | **JM2701 回撤确认多** | **75** | **3** | 多 | 条件试仓 | JM2701期货 | 月内涨幅大；钢材需求可能证伪 |
| 4 | CF701 天气多 | **69** | 2 | 观察 | Watch | CF701 | curve反向、缺仓单/basis/ICE闭环 |
| 5 | RM611 趋势延续 | **68** | 2 | 观察 | Watch | RM611 | 夜盘未延续、OI增速放缓、Physical缺 |

**没有80+确认交易。今天可以承担风险，但只能是开盘后确认式试仓。**

## 七、前三名交易卡

### 1. SA701｜失败反弹空｜78

- **事实：** 8/27 close/settle 1011/1016，EOD ΔOI约+10.66%，近端Contango约3.23%；夜盘主连约-0.49%。隆众口径：产量76.62万吨、周环比+2.72%，利用率80.44%、+2.13pp；厂家库存187.27万吨，较上周四+1.51%。
- **市场定价：** 市场已重定价供应宽松，但1000附近也在计入减产/检修和低估值支撑。
- **推断：** 最有edge的不是继续打低点，而是反弹无法收复1018—1025后再次转弱。
- **主观判断：** 今日最佳条件单。
- **入场：** 09:00后等至少30分钟；若反弹1018—1028失败，重新跌破1010/VWAP，先1/2；跌破1000且OI不塌、Contango不明显收窄再加1/2。若直接低开<995，不追，等45分钟。
- **初始止损：** 15分钟接受在1035上方；**逻辑失效**为1050上方稳定、curve明显收窄/翻Back、产量下降且库存连续去化。
- **TP1/TP2：** 980 / 940；2—3个交易日不创新低时间止损。
- **风险预算：** 0.35%—0.50% NAV；与FG/地产化工弱需求因子合并不超过0.75%。
- **合约参数：** 20吨/手，tick 1元/吨，tick value 20元；按1011计名义约20,220元/手；夜盘21:00—23:00；最后交易日交割月第10个交易日，实物交割。标准合约最低保证金5%、标准限幅±4%，但**今日动态保证金/限幅需终端复核**。按标准4%仅作压力敏感度：单边1个限幅约809元/手，连续2个同向限幅约1,650元/手，不代表今日真实限幅。
- **gap plan：** 低开不追；高开至1025附近失败反而是更优入场。

### 2. SC2610｜高开后回撤承接多｜77

- **事实：** 8/27日盘close/settle约576.5/573.7；8/27夜盘收601，较结算+4.76%。Brent 8/27结算89.70、WTI 83.53，均明显反弹；Reuters称Hormuz船流虽改善但仍低于正常，伊朗提出重开海峡条件。
- **市场可能错在哪里：** 市场可能低估海峡持续受限的右尾；也可能高估headline对真实出口的长期冲击。
- **最佳表达：** 只做SC2610回撤确认多，不在601附近追；SC多/FU空RV只观察，未完成beta/裂解配比前不下双腿。
- **入场：** 9:00若明显高开，等45分钟。优先看592—596能否承接并重新站回600；若直接>606不追。先1/3，突破604.8夜盘高点且OI/成交跟进再加。
- **初始止损：** 30分钟接受在586下方；**逻辑失效**为580下方+Brent跌回86附近+Hormuz通行量显著正常化。
- **TP1/TP2：** 615 / 630；若24小时内地缘溢价不扩张则减仓。
- **风险预算：** 0.25%—0.40% NAV，因为单手名义巨大且headline gap高。
- **合约参数：** 1000桶/手，tick 0.1元/桶，tick value 100元；按601计名义约601,000元/手；最后交易日为交割月前一月最后交易日，实物交割。INE 6月23日公告显示SC2610等合约限幅14%、一般持仓保证金16%（若后续无新公告）；经纪商保证金未确认。以8/27结算573.7做14%压力：1个不利限幅约80,318元/手；连续2个不利限幅约149,391元/手。
- **gap plan：** 这是典型“不追夜盘高潮”的机会，只有回撤承接才有赔率。

### 3. JM2701｜回撤确认多｜75

- **事实：** 8/27日盘close约1609，夜盘22:57约1618、最终约+1.88%；EOD ΔOI约+7.37%，近端Back约1.04%。Mysteel 523矿样本原煤库存周降5.8万吨、精煤库存周降21.1万吨。
- **市场可能错在哪里：** 市场可能仍低估安监/复产慢对供应的约束；也可能已经过度交易旺季补库，随后被钢材弱需求证伪。
- **入场：** 等30—45分钟。1595—1605回撤不破并重新站上1615可1/3；突破1625且OI继续增长再加。若直接跳到1640以上不追。
- **初始止损：** 30分钟接受在1575下方；**逻辑失效**为1550下方+矿山库存转增+钢厂/焦企补库明显放缓。
- **TP1/TP2：** 1650 / 1700；两天不能突破前高减仓。
- **风险预算：** 0.25%—0.40% NAV；与黑色链其他多头合并≤0.75%。
- **合约参数：** 60吨/手，tick 0.5元/吨，tick value 30元；按1618计名义约97,080元/手；最后交易日交割月第10个交易日、实物交割。标准合约最低保证金5%，8/27行情页面显示当日上下限约±8%，但8/28动态参数需终端确认。按8%作压力敏感度：1个不利限幅约7,766元/手，连续2个约14,911元/手。

## 八、商品期权专项

8月27链覆盖已恢复到64/64品种、22,348合约，IV覆盖98.33%；但surface产物为空、positioning coverage不足、bid/ask=0、execution_ready=false。结论：**今天期权只能做研究方向，不能给具体可成交结构。** 若盘中人工取得fresh quotes，优先研究SA Put Spread、SC Call Spread以及JM Call Spread，均须满足：`research only; manual quote and manual confirmation required before execution; no premium quoted`。Jackson Hole前避免贵金属裸买高Vega，也不做任何基于dealer Gamma方向的推断。

## 九、9:00开盘风险地图

| 品种 | 可能场景 | 置信度 | 操作 |
|---|---|---|---|
| SC2610 | 夜盘601意味着相对EOD明显高开 | 高 | **等45分钟**；592—596承接后重返600才多，>606不追 |
| SA701 | 夜盘仍弱，可能平/低开 | 中高 | 低开<995不追；1018—1028反弹失败才空 |
| JM2701 | 夜盘近+2%，高开风险 | 高 | 等30—45分钟；回撤守1600附近优先，1640上方不追 |
| CF701 | 夜盘+0.47%，天气多头延续 | 中 | 等30分钟看17000是否守住；curve仍Contango，暂不升级 |
| FG701 | 夜盘+0.88%且周库存下降 | 中 | 不再按旧空头逻辑追空；先看915/920能否形成接受 |
| FU2611 | 与SC方向背离 | 中高 | 不追SC上涨去做FU多；先确认产品库存/裂解是否改善 |
| AU/AG | 国内金银分化，22:00有Warsh | 中 | 日盘不抢Vega，事件前压缩方向仓 |

## 十、未来24小时与7天事件

| 北京时间 | 事件 | 主要品种 | 处理 |
|---|---|---|---|
| **8/28 22:00** | Fed Chair Kevin Warsh Jackson Hole讲话 | AU/AG、CU、原油、美元 | 事件前不裸买昂贵Vega；方向仓减小，保留有限损失结构 |
| **8/28 22:00** | BLS 2026年3月CES preliminary benchmark | 美元、贵金属 | 次要但与Warsh同窗，避免把第一跳误判成单一事件 |
| **8/29 03:30** | CFTC COT周报 | 原油、金银、铜、农产品 | 只作拥挤度背景，不等同客户最终方向 |
| 周末 | Hormuz通航/伊朗—美国谈判与航运事件 | SC/FU/LU/PG | headline gap最高；周末前控制净Delta |
| 周末 | 中国东北/河南/新疆天气更新 | CF/C/M/RM | 连续高温/暴雨才加权，不用单次预报追价 |
| **9/2 22:30** | EIA Weekly Petroleum Status Report | SC/FU/LU | 若原油与产品库存继续背离，优先RV而非同向篮子 |
| **9/4 20:30** | 美国8月就业报告 | AU/AG、美元、有色 | 事件前降低跨资产重复美元/实际利率风险 |

## 十一、行动清单

A. 今天没有应立即建立的新仓位。

B. 今天只应挂条件单的仓位：SA701失败反弹空；SC2610回撤承接多；JM2701回撤确认多。

C. 今天应继续观察的机会：CF701天气多、RM611/M2701油粕强势、SC多/FU空相对价值、FG去库后的反抽持续性。

D. 今天必须避免或退出的交易：开盘追SC/JM高开、低位追空SA、继续机械持有旧FG空、追空EG、Jackson Hole前裸买贵金属高Vega。

## 风险预算与因子合并

单一试仓最大损失控制0.25%—0.50% NAV；今日没有确认交易，任何单主题不超过0.75%。SA与FG/地产化工弱需求合并；SC与FU/LU/PG/Hormuz合并；JM与J/RB/HC黑色需求合并；CF与M/RM天气/进口因子分开识别但总农产品天气风险≤1.0%。跨品种RV在没有beta/产业转化比率前只研究，不为了“中性”标签假装风险已消失。

## 数据与模型说明

事实数据、市场定价、推断和主观判断已分开。当前root 8/28失败状态不覆盖8/27最后完整EOD；`report_input_latest.json`为空是编排/发布异常，不是市场No-Trade。期货curve不等于现货basis；C/D级basis不计方向层。周度Physical只按原生频率解释。Options链完整不代表surface/positioning/execution就绪。

## 关键来源

- China-Commodities-Engine: https://github.com/farfromexact/China-Commodities-Engine
- Reuters，8/27油价与Hormuz：https://www.reuters.com/business/energy/oil-prices-extend-losses-expectations-talks-ease-middle-east-supply-woes-2026-08-27/
- Reuters，8/27新加坡油品库存：https://www.reuters.com/business/energy/singapore-oil-product-inventories-rebound-highest-three-weeks-2026-08-27/
- Reuters，中国作物天气：https://www.reuters.com/world/asia-pacific/heat-floods-threaten-china-crops-us-farm-purchases-loom-2026-08-27/
- 每日经济新闻，SC2610夜盘：https://www.nbd.com.cn/articles/2026-08-28/4562563.html
- 界面快报，国内23:00夜盘：https://www.jiemian.com/lists/1326kb.html
- 新华财经商品日报：https://www.cnfin.com/dz-lb/detail/20260827/4461396_1.html
- 隆众纯碱库存转述：https://qhweb.eastmoney.com/news/202608273855875994.html
- 郑商所纯碱业务细则：https://www.czce.com.cn/cn/uploadfile/2024/02/07/20240207112556986.pdf
- INE原油标准合约：https://www.ine.cn/products/futures/energyandchemical/sc_f/standard_sc_f/202312/t20231205_802540.html
- INE 2026-06-23保证金/限幅公告：https://www.ine.cn/publicnotice/notice/202606/t20260623_832248.html
- DCE焦煤合约Factsheet：https://www.dce.com.cn/dce/file/2026-01-15/17684624156122c9a882b9ae6dcbb289019bc092f6fc1681.pdf
- Kansas City Fed Jackson Hole：https://www.kansascityfed.org/newsroom/2026-news-releases/kansas-city-fed-to-host-annual-jackson-hole-economic-policy-symposium-2026/
- CFTC COT schedule：https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm
- EIA WPSR schedule：https://www.eia.gov/petroleum/supply/weekly/schedule.php
