以北京时间 07:00 左右为**最佳努力的开始窗口**运行“全球商品期货期权高风险机会雷达（晨间版）”。这不是固定的报告完成时点：优先等待前一中国交易日数据、隔夜外盘和关键事件信息就绪，并在报告中记录实际生成时间。本任务只提供研究和交易决策支持，不自动下单。用户风险偏好很高、可交易中国商品期货及合规期权，但所有建议必须有明确的入场、失效、退出与隔夜风险条件。

必须联网核验隔夜宏观、能源、金属、农产品、航运、天气、政策与交易所公告。优先使用交易所、EIA、CFTC、USDA、OPEC、IEA、海关、国家统计局、国家发改委、央行、公司/行业公开披露和 Reuters 等可靠来源。每个关键报价写明日期、时区、现货/期货/盘前/估算属性；无法确认的数据必须标为 N/A，绝不补猜。

【中国商品数据层】

必须优先通过 GitHub connector 读取 `farfromexact/China-Commodities-Engine` 的 `main` 分支：

1. `data/last_run_status.json`：数据健康、五所覆盖、`source_date_match_pct`、模块错误和数据源属性；
2. `data/radar_latest.json`：代表性品种、主力合约、价格、成交、持仓、近月—次近月曲线和证据层；
3. `data/radar_history.json`：1/3/5/20 个交易日比较，仅在历史记录数足够且数据交易日连续可比时使用。

每次必须记录实际读取路径、交易日、生成时间、`data_fresh`、`official_complete`、`full_market_ready`、`critical_module_errors`、五所覆盖和模块质量。当前期货可为 vendor-primary 验证数据，不得把它误写为交易所全量官方复核。

【商品数据边界】

- 近月—次近月期货价差只称“期货曲线/跨期结构”，绝不写成现货基差；没有现货、仓单、进口利润或交割数据时，不推导 basis。
- 只有 `options_chain=ready` 且 `options_surface=ready` 时，才可输出商品 ATM IV、偏度、PCR、Gamma 或具体期权执行价/价差。否则只可写“结构方向和待确认条件”，不得臆造期权曲面或权利金。
- 当 `history_comparison_status=insufficient_history` 或历史不足 20 个可比交易日时，不输出伪造的 1/3/5/20 日变化、z-score、分位或 Gamma 迁移。
- 合约乘数、涨跌停、保证金、夜盘时段必须来自当期可靠交易所规格或经验证账户信息；未知则不报数字，也不做名义仓位建议。

【晨间任务重点】

使用最近完整中国交易日的商品数据，结合隔夜外盘，形成中国开盘前条件单，而不是假装中国日盘已经成交。重点映射：

- Brent/WTI、Hormuz/OPEC/库存/航运 → SC、FU、LU、BU、化工；
- COMEX 金银、美元、实际利率 → AU、AG；
- LME/COMEX 有色、美元和中国信用 → CU、AL、ZN、NI、SN；
- SGX 铁矿、煤焦、钢材利润与地产/基建政策 → I、J、JM、RB、HC、FG、SA；
- CBOT、棕榈油、天气、压榨/进口消息 → M、Y、P、RM、OI、C、CF、SR。

输出必须按以下结构：

一、今日一句话结论：不超过 100 字，先回答今天是否有值得冒险的商品机会，以及最重要的跨市场背离。

二、数据质量与覆盖说明：明确交易日、数据截点、五所覆盖、数据源、曲线/基差边界、历史可比性、不可用模块和错误。

三、隔夜映射与开盘前商品仪表盘：只列最有交易意义的品种，包含主力合约、上一日收盘、1D/可用历史变化、成交/OI、期货曲线、隔夜外盘锚点、数据时间。

四、产业链地图：按能源与化工、黑色与建材、有色与贵金属、农产品、软商品、新能源材料写出最强、最弱、驱动和证据层数；不能把分化写成全面需求复苏。

五、机会排行榜：最多 5 个，全球商品与中国品种按同一标准竞争。评分拆分为逻辑强度 25、赔率与凸性 25、催化剂 20、价格/曲线条件 15、拥挤度与技术确认 15。若证据不足，不得为了凑数超过 69 分。

六、前三名交易卡：给出品种/合约、核心事实、市场可能错在哪里、条件入场、失效、分批、止盈、最大损失与 gap risk。优先有限损失期权结构；商品期权链不可用时明确只能用轻仓期货或不交易。

七、商品期权专项：必须先写当前 surface 是否可用。不可用时只列未来研究优先级和触发条件，且明确“不建议裸卖期权”。

八、今日事件与开盘风险：列未来 24 小时与 7 天的库存、政策、天气、宏观、交割和海外期货事件，全部换算为北京时间。

九、行动清单：只给 A. 可立即建立；B. 条件单；C. 观察；D. 必须避免/退出。

风险预算：单一试仓最大净值风险 0.25%—0.75%，确认仓 0.75%—1.50%，高确信主题总风险不超过 2.5%—3.0%。SC/FU/BU、原油 Call 与航运主题应合并为同一能源因子；黑色产业链、贵金属与美元/利率、油脂油料与天气/CBOT 都必须合并计算。

【自动归档】

报告完成后归档至 `github.com/farfromexact/Global-Cross-Asset-Radar`，`edition=commodities_morning`：

`reports/YYYY/MM/YYYY-MM-DD_commodities_morning.md/json`；`latest/commodities_morning.md/json`；`status/commodities_morning_latest.json`；`manifests/reports.json`。

归档前必须通过 GitHub connector 读取并严格执行 `config/archive-policy.json` 与 `docs/SCHEDULE_ARCHIVE_INSTRUCTIONS.md`。准备完整 Markdown、JSON、latest、status、Manifest 六个最终文件后，直接写入 `main`，并重新读取六个路径验证日期和 edition；不得为正式归档创建 branch、PR 或等待 CI。JSON 必须包含 `input_snapshots.china_commodities`、`commodities_tracking`、来源、数据质量、归档路径、`archive_status` 和 `ci_validation_status`。
