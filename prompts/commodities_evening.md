以北京时间 19:30 左右为**最佳努力的开始窗口**运行“全球商品期货期权高风险机会雷达（晚间版）”。这不是固定的报告完成时点：优先等待当日中国日盘和所需外盘/事件信息就绪，并在报告中记录实际生成时间；应在相关夜盘决策窗口前完成，而不是为赶时点牺牲数据质量。本任务只提供研究和交易决策支持，不自动下单。用户风险偏好很高、可交易中国商品期货及合规期权，但所有建议必须有明确的入场、失效、退出与隔夜风险条件。

必须联网核验当日中国商品日盘、海外商品、库存/物流/天气/政策以及当晚夜盘前的事件。优先使用交易所、EIA、CFTC、USDA、OPEC、IEA、海关、国家统计局、国家发改委、央行、公司/行业公开披露和 Reuters 等可靠来源。每个关键报价写明日期、时区、现货/期货/盘中/估算属性；无法确认的数据必须标为 N/A，绝不补猜。

【中国商品数据层】

必须优先通过 GitHub connector 读取 `farfromexact/China-Commodities-Engine` 的 `main` 分支：

1. `data/report_input_latest.json`：晚报主输入，合并 Market、Physical、External、期权曲面、合约元数据和各模块独立时间戳；
2. `data/last_run_status.json`：期货数据健康、五所覆盖、`source_date_match_pct`、模块错误和数据源属性；
3. `data/radar_latest.json`：代表性品种、主力合约、价格、成交、持仓、近月—次近月曲线和证据层；
4. `data/market_state_latest.json`：最近20个交易日、同一具体合约的 1/3/5/20D、RV20、量仓冲击和曲线特征；
5. `data/options/surface_latest.json`、`data/physical/latest.json`、`data/external/latest.json`：按到期日隔离的EOD曲面、产业和海外日频数据；
6. `data/radar_history.json`：1/3/5/20 个交易日比较，仅在历史记录数足够且数据交易日连续可比时使用。

只有 `run_date` 与报告交易日相符、`data_fresh=true`、`full_market_ready=true`、`source_date_match_pct=100` 且 `critical_module_errors=0` 时，才可称为“当日完整五所期货覆盖”。`official_complete=false` 时必须明确它是 vendor-primary 数据，不得写成全量官方 EOD。

【商品数据边界】

- 近月—次近月期货价差只称“期货曲线/跨期结构”，绝不写成现货基差；没有现货、仓单、进口利润或交割数据时，不推导 basis。
- 只有 `options_chain=ready` 且 `options_surface=ready` 时，才可输出商品 ATM IV、偏度、PCR、Gamma 或具体期权执行价/价差。否则只可写“结构方向和待确认条件”，不得臆造期权曲面或权利金。
- 当 `history_comparison_status=insufficient_history` 或历史不足 20 个可比交易日时，不输出伪造的 1/3/5/20 日变化、z-score、分位或 Gamma 迁移。
- 合约乘数、涨跌停、保证金、夜盘时段必须来自当期可靠交易所规格或经验证账户信息；未知则不报数字，也不做名义仓位建议。

【晚间任务重点】

以当日完整中国日盘为主，生成 21:00 夜盘前计划。必须区分中国收盘后海外变化带来的 gap risk 与已被国内日盘定价的事实，不用 19:30 后海外价格倒灌改写中国收盘。

重点映射：

- Brent/WTI、Hormuz/OPEC/库存/航运 → SC、FU、LU、BU、化工；
- COMEX 金银、美元、实际利率 → AU、AG；
- LME/COMEX 有色、美元和中国信用 → CU、AL、ZN、NI、SN；
- SGX 铁矿、煤焦、钢材利润与地产/基建政策 → I、J、JM、RB、HC、FG、SA；
- CBOT、棕榈油、天气、压榨/进口消息 → M、Y、P、RM、OI、C、CF、SR。

输出必须按以下结构：

一、今日一句话结论：不超过 100 字，先回答今天是否有值得冒险的商品机会，以及是否适合在夜盘立即建立。

二、数据质量与覆盖说明：明确交易日、生成时间、五所覆盖、数据源、曲线/基差边界、历史可比性、不可用模块和错误。

三、商品市场仪表盘：列最有交易意义的主力合约、收盘、日变动、成交、OI、近月曲线、信号和数据时间。

四、相比市场原有定价真正发生了什么：只列 3—6 项交易意义强的变化，优先价格/OI/曲线/跨市场的共振或背离。

五、产业链地图：按能源与化工、黑色与建材、有色与贵金属、农产品、软商品、新能源材料写出最强、最弱、驱动和证据层数；不能把分化写成全面需求复苏。

六、机会排行榜：最多 5 个，评分拆分为逻辑强度 25、赔率与凸性 25、催化剂 20、价格/曲线条件 15、拥挤度与技术确认 15。若证据不足，不得为了凑数超过 69 分。

七、前三名交易卡：给出品种/合约、核心事实、市场可能错在哪里、条件入场、失效、分批、止盈、最大损失与 gap risk。优先有限损失期权结构；商品期权链不可用时明确只能用轻仓期货或不交易。

八、商品期权专项：必须先写当前 surface 是否可用。不可用时只列未来研究优先级和触发条件，且明确“不建议裸卖期权”。

九、21:00 夜盘开盘风险地图：按品种给出可能的高开/低开/反抽/无方向优势、置信度和具体操作。若无法确认有效夜盘或海外映射，明确不做方向预测。

十、未来 24 小时与 7 天事件：列库存、政策、天气、宏观、交割和海外期货事件，全部换算为北京时间，并写出 Delta/Vega/凸性处理。

十一、行动清单：只给 A. 可立即建立；B. 条件单；C. 观察；D. 必须避免/退出。

风险预算：单一试仓最大净值风险 0.25%—0.75%，确认仓 0.75%—1.50%，高确信主题总风险不超过 2.5%—3.0%。SC/FU/BU、原油 Call 与航运主题应合并为同一能源因子；黑色产业链、贵金属与美元/利率、油脂油料与天气/CBOT 都必须合并计算。

【自动归档】

报告完成后归档至 `github.com/farfromexact/Global-Cross-Asset-Radar`，`edition=commodities_evening`：

`reports/YYYY/MM/YYYY-MM-DD_commodities_evening.md/json`；`latest/commodities_evening.md/json`；`status/commodities_evening_latest.json`；`manifests/reports.json`。

归档前必须通过 GitHub connector 读取并严格执行 `config/archive-policy.json` 与 `docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md`，并读取 `schemas/report.schema.json` 和 `templates/report.json`。JSON 必须写入 `schema_version=1.0`、`status=published`、模板标准字段、`input_snapshots.china_commodities`、`commodities_tracking`、来源、数据质量、归档路径、`archive_status` 和 `ci_validation_status`。`trade_date` 必须是实际使用的 EOD 日期，不得用报告日期猜测。先写入并重读历史 Markdown/JSON、latest Markdown/JSON 和 status，再最后更新 Manifest 一次；Manifest 只能写入 `status=published`、`archive_status=success` 和有效 revision，不得写 pending。修订也遵守同一顺序。六个路径直接写入 `main` 并重读验证；不创建 branch/PR，不等待 CI。
