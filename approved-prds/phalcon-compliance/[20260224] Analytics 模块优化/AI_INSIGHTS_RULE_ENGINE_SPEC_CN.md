# AI\_INSIGHTS\_RULE\_ENGINE\_SPEC\_CN

# AI Insights Rule Engine 规则设计

# 1. 目标

本文档用于定义 Analytics AI Insights 的确定性规则引擎。

重点回答三件事：

*   需要有哪些规则
    
*   每条规则在什么条件下触发
    
*   每条规则在什么边界条件下应被抑制或降级
    

原则：

*   规则引擎负责决定"什么是重要的"
    
*   LLM 只负责决定"怎么表达"
    

---

# 2. 规则引擎原则

## 2.1 允许使用的数据来源

规则只能使用当前 PRD 已定义的 Analytics 图表和指标（对应 facts schema 字段）：

| 图表 / 模块 | facts 字段 |
| --- | --- |
| 核心指标卡片 | `core_metrics` |
| Risk Trend | `risk_trend` |
| Risk Level Distribution | `risk_level_distribution` |
| Top Triggered Rules | `top_triggered_rules` + `top_triggered_rules_meta` |
| Identity Exposure Distribution | `identity_exposure_distribution` |
| Risk Exposure Flow | `risk_exposure_flow` |
| Screened Transaction Volume | `screened_tx_volume_usd` |
| Screening Count Trend | `screening_volume_trend` |
| Screening Source Breakdown | `screening_source_breakdown` |

## 2.2 通用边界规则

除非单条规则另有说明，否则统一适用：

*   如果必需字段缺失（`null` 或 `undefined`），则该规则不触发
    
*   如果某规则需要与前一周期对比，而 previous period 数据不存在（如用户首次使用尚无历史数据），则该规则不触发
    
*   如果 current 和 previous 都低于该规则定义的最小绝对量阈值，则该规则不触发
    
*   如果两条规则描述的是同一现象，则保留 priority 更高的一条（见第 7 节去重规则）
    
*   如果没有任何有意义的规则触发，则输出 `no_significant_change`
    

## 2.4 数值约定

所有阈值均使用与 facts schema 一致的 **decimal 格式**：

| 描述 | 规则文档写法 | facts schema 示例 | 说明 |
| --- | --- | --- | --- |
| 百分比变化 | `change_pct >= 0.20` | `"change_pct": 0.3651` | 20% |
| 百分点变化 | `change_pp >= 0.005` | `"change_pp": 0.0054` | 0.5pp |
| USD 金额 | `>= 100000` | `"exposure_value_usd_current": 670000` | 整数 USD |

## 2.4 `**period_avg**` 定义（Spike 类规则专用）

Spike 类规则中 `period_avg` 的计算方式：

*   取当前时间周期内**所有 time bucket** 对应目标指标的算术平均值
    
*   计算时**包含**潜在 spike 所在的 bucket（保守计算）
    
*   若当前周期内 bucket 总数 `< 3`，则 spike 规则**不触发**（数据点不足，不可信）
    

**示例**：7 个 daily bucket 的 `high_plus_critical` 值为 `[5, 6, 4, 7, 5, 6, 20]`， 则 `period_avg = 53 / 7 ≈ 7.57`。Bucket 值 20 满足 `> 7.57 × 1.5 = 11.36`，且 `>= 8`，触发 spike。

`high_plus_critical`（每个 bucket 的派生值）= `risk_trend.series[i].high + risk_trend.series[i].critical`

## 2.5 Target scope 与 Spike 规则映射

| `meta.target_filter` | 触发的 Spike 规则 |
| --- | --- |
| `address` | `address_risk_spike` |
| `transaction` | `transaction_risk_spike` |
| `all` | `overall_risk_spike`（不同时触发 address 和 transaction 版本） |

---

# 3. 规则输出结构

每条规则输出统一的 JSON 结构（与 evidence schema 对齐）：

```plaintext
{
  "rule_id": "string",
  "title": "string",
  "category": "spike | trend | concentration | screening | identity_risk | interaction_risk | volume | fallback",
  "severity": "high | medium | low",
  "priority": 0,
  "related_view": "string",
  "entity_scope": "all | address | transaction",
  "driver_indicator": "string | null",
  "template": "string",
  "variables": {},
  "data_source": "string",
  "filter_hint": "string"
}
```

字段说明：

*   `priority`：整数，0–100，值越高越优先送入 prompt，见第 4 节速查表
    
*   `severity`：业务紧急程度（`high` = 需立即关注，`medium` = 值得注意，`low` = 参考信息）
    
*   `driver_indicator`：若规则指向单一 Risk Indicator，填写 indicator 名称（如 `"Mixing"`）；否则为 `null`
    
*   `template`：factual 句子模板，变量用 `{placeholder}` 表示；占位符统一引用 `variables` 中的 `_display` 格式化字段
    
*   `variables`：包含两类字段：
    
    *   原始值字段（decimal 格式，与 facts schema 一致）：供后续逻辑消费，如 `change_pct: 0.3651`
        
    *   `_display` 格式化字段（供 template 和 LLM 直接引用）：如 `change_pct_display: "+36.5%"`，避免 LLM 自行格式化导致的误差
        

`**_display**` 字段格式规范：

| 原始字段类型 | `_display` 格式规则 | 示例 |
| --- | --- | --- |
| `change_pct`（增长） | `"+X.X%"` | `"+36.5%"` |
| `change_pct`（下降） | `"-X.X%"` | `"-22.0%"` |
| `change_pp`（增长） | `"+X.Xpp"` | `"+0.54pp"` |
| `change_pp`（下降） | `"-X.Xpp"` | `"-0.40pp"` |
| `usd`（< $1M） | `"$XXX,XXX"` | `"$670,000"` |
| `usd`（≥ $1M） | `"$X.XXM"` | `"$12.57M"` |
| `ratio / pct`（展示用） | `"X.X%"` | `"3.5%"` |
| `multiplier` | `"X.Xx"` | `"2.6x"` |

---

# 4. Priority 速查表

| rule\_id | category | severity | priority |
| --- | --- | --- | --- |
| `address_risk_spike` | spike | high | **100** |
| `transaction_risk_spike` | spike | high | **100** |
| `overall_risk_spike` | spike | high | **95** |
| `overall_risk_increase` | trend | high | **90** |
| `overall_risk_decrease` | trend | medium | **85** |
| `interaction_risk_increase` | interaction\_risk | high | **80** |
| `interaction_risk_concentration` | interaction\_risk | medium | **75** |
| `interaction_risk_driver` | interaction\_risk | medium | **70** |
| `identity_risk_distribution_shift` | identity\_risk | medium | **65** |
| `identity_risk_concentration` | identity\_risk | medium | **60** |
| `rule_trigger_surge` | concentration | medium | **55** |
| `rule_concentration` | concentration | medium | **50** |
| `screened_tx_volume_increase` | volume | low | **45** |
| `screened_tx_volume_decrease` | volume | low | **45** |
| `screened_tx_volume_spike` | volume | low | **38** |
| `screening_count_surge` | screening | low | **35** |
| `screening_target_surge` | screening | low | **30** |
| `screening_rescreening_signal` | screening | low | **25** |
| `screening_source_shift` | screening | low | **20** |
| `no_significant_change` | fallback | low | **10** |

# 5. 规则

## 5.1 整体风险态势规则

### 规则：`overall_risk_increase`

**目的**：识别整体高风险 / 极高风险水平是否明显恶化

**数据来源**：

*   `core_metrics.high_critical_targets.current / previous / change_pct`
    
*   `core_metrics.high_critical_ratio.current / previous / change_pp`
    

**触发条件**（逻辑为 AND/OR 组合，见下）：

```plaintext
(
  high_critical_targets.change_pct >= 0.20        // 条件A：数量增长 ≥ 20%
  OR
  high_critical_ratio.change_pp >= 0.01          // 条件B：风险比例增长 ≥ 1pp
)
AND
high_critical_targets.current >= 10               // 当前周期绝对量 ≥ 10
AND
high_critical_targets.previous >= 10              // 前一周期绝对量 ≥ 10
```

**特殊说明**：若只有条件B触发（条件A不满足），还需额外要求：

```plaintext
high_critical_targets.current >= 20
AND
high_critical_targets.previous >= 20
```

（避免小基数样本下比例波动产生误报）

**边界条件**：

*   `previous_period` 数据不存在 → 不触发
    

**Priority & Severity**：90 / high

**driver\_indicator**：null

**related\_view**：`Risk Trend`

**data\_source**：`core_metrics`

**template**：

```plaintext
"High & Critical risk targets increased by {change_pct_display} from {prev_count} to {current_count}. The risk ratio changed by {change_pp_display} to {current_ratio_display}."
```

**variables 示例**：

```plaintext
{
  "change_pct": 0.3651,
  "change_pct_display": "+36.5%",
  "prev_count": 63,
  "current_count": 86,
  "change_pp": 0.0054,
  "change_pp_display": "+0.54pp",
  "current_ratio": 0.0354,
  "current_ratio_display": "3.5%"
}
```
---

### 规则：`overall_risk_decrease`

**目的**：识别整体高风险 / 极高风险水平是否明显改善

**数据来源**：同 `overall_risk_increase`

**触发条件**：

```plaintext
(
  high_critical_targets.change_pct <= -0.20       // 数量下降 ≥ 20%
  OR
  high_critical_ratio.change_pp <= -0.01         // 风险比例下降 ≥ 1pp
)
AND
high_critical_targets.current >= 10
AND
high_critical_targets.previous >= 10
```

特殊说明：同 `overall_risk_increase`，若只有比例下降触发，需 current 和 previous 均 `>= 20`。

**边界条件**：同 `overall_risk_increase`

**Priority & Severity**：85 / medium

**related\_view**：`Risk Trend`

**data\_source**：`core_metrics`

**template**：

```plaintext
"High & Critical risk targets decreased by {change_pct_display} from {prev_count} to {current_count}. The risk ratio changed by {change_pp_display} to {current_ratio_display}."
```

**variables 示例**：

```plaintext
{
  "change_pct": -0.2250,
  "change_pct_display": "-22.5%",
  "prev_count": 80,
  "current_count": 62,
  "change_pp": -0.004,
  "change_pp_display": "-0.40pp",
  "current_ratio": 0.028,
  "current_ratio_display": "2.8%"
}
```
---

## 5.2 Spike 类规则

### 规则：`address_risk_spike`

**目的**：识别地址维度高风险数量在某个时间 bucket 的异常突增

**数据来源**：

*   `risk_trend.series[].high + risk_trend.series[].critical`（派生为 `high_plus_critical`）
    
*   `risk_trend.granularity`
    

**触发条件**：

```plaintext
meta.target_type = "address"
AND
risk_trend.series bucket 数量 >= 3
AND
存在某个 bucket 满足：
  bucket.high_plus_critical > period_avg × 1.5
  AND bucket.high_plus_critical >= 8
```

**边界条件**：

*   `risk_trend.granularity = "month"` → 不触发（月粒度噪音过大）
    
*   `period_avg < 5` 且 `bucket.high_plus_critical < 10` → 不触发（极小基数噪音）
    
*   bucket 数量 `< 3` → 不触发
    

**Priority & Severity**：100 / high

**driver\_indicator**：null

**related\_view**：`Risk Trend`

**data\_source**：`risk_trend`

**filter**: `target:address`

**template**：

```plaintext
"Address risk spike detected: on {spike_date_display}, {spike_value} high-risk addresses were identified — {spike_multiplier_display} the period average of {period_avg}."
```

**variables 示例**：

```plaintext
{
  "spike_date": "2026-03-03T00:00:00Z",
  "spike_date_display": "Mar 3",
  "spike_value": 20,
  "period_avg": 7.57,
  "spike_multiplier": 2.64,
  "spike_multiplier_display": "2.6x"
}
```
---

### 规则：`transaction_risk_spike`

**目的**：识别交易维度高风险数量的异常 spike

**数据来源**：同 `address_risk_spike`

**触发条件**：

```plaintext
meta.target_type = "transaction"
AND
（其余同 address_risk_spike）
```

**边界条件**：同 `address_risk_spike`

**Priority & Severity**：100 / high

**related\_view**：`Risk Trend`

**data\_source**：`risk_trend`

**filter**: `target:tx`

**template**：

```plaintext
"Transaction risk spike detected: on {spike_date_display}, {spike_value} high-risk transactions were identified — {spike_multiplier_display} the period average of {period_avg}."
```

**variables**：同 `address_risk_spike`（数值对应交易维度）

---

### 规则：`overall_risk_spike`

**目的**：当 target scope 为 all 时，识别整体维度的高风险 spike

**数据来源**：同 `address_risk_spike`

**触发条件**：

```plaintext
risk_trend.series bucket 数量 >= 3
AND
存在某个 bucket 满足：
  bucket.high_plus_critical > period_avg × 1.5
  AND bucket.high_plus_critical >= 8
```

**边界条件**：

*   同 `address_risk_spike`
    
*   若 `target_filter` 可以精确确定为 address 或 transaction，则优先输出对应具体规则
    

**Priority & Severity**：95 / high

**related\_view**：`Risk Trend`

**data\_source**：`risk_trend`

**template**：

```plaintext
"Risk spike detected: on {spike_date_display}, {spike_value} high-risk targets were identified — {spike_multiplier_display} the period average of {period_avg}."
```

**variables**：同 `address_risk_spike`

---

## 5.3 Rule Trigger 类规则

### 规则：`rule_trigger_surge`

**目的**：识别某条规则的触发次数相较前一周期明显上升

**数据来源**：

*   `top_triggered_rules[].trigger_count_current`
    
*   `top_triggered_rules[].trigger_count_previous`
    
*   `top_triggered_rules[].change_pct`
    
*   `top_triggered_rules[].rule_name`
    

**触发条件**：

```plaintext
存在某条 rule 满足：
  trigger_count_current >= 20
  AND change_pct >= 0.50                         // 增长 ≥ 50%
```

对所有满足条件的规则，只输出 change_pct 最大的一条（最多 1 条 rule_trigger\_surge evidence）。

**边界条件**：

*   `trigger_count_current < 20` → 不触发（绝对量过小）
    
*   若同时触发 `rule_concentration`，且两者指向同一条规则，按去重规则处理（保留 priority 更高的 `rule_trigger_surge`）
    
*   仅使用 top_triggered_rules 中已返回的规则行，不对 others 进行推断
    

**Priority & Severity**：55 / medium

**driver\_indicator**：null（由 `rule_name` 变量承载）

**related\_view**：`Top Triggered Rules`

**data\_source**：`top_triggered_rules`

**template**：

```plaintext
"Rule \"{rule_name}\" surged by {change_pct_display} this period, with {current_count} triggers (up from {prev_count})."
```

**variables 示例**：

```plaintext
{
  "rule_name": "Mixer Interaction",
  "change_pct": 0.50,
  "change_pct_display": "+50.0%",
  "current_count": 42,
  "prev_count": 28
}
```
---

### 规则：`rule_concentration`

**目的**：识别某条规则在整体触发中是否占比过高

**数据来源**：

*   `top_triggered_rules[].trigger_count_current`
    
*   `top_triggered_rules[].rule_name`
    
*   `top_triggered_rules_meta.total_trigger_count_current`
    

**触发条件**：

```plaintext
top_triggered_rules_meta.total_trigger_count_current > 0
AND
存在某条 rule 满足：
  trigger_count_current >= 30
  AND trigger_count_current / total_trigger_count_current >= 0.30   // 占比 ≥ 30%
```

对所有满足条件的规则，只输出占比最高的一条。

**边界条件**：

*   `total_trigger_count_current = 0` → 不触发
    
*   必须使用 `total_trigger_count_current`（全量分母），不得用 top-N 行的求和
    
*   `trigger_count_current < 30` → 不触发
    

**Priority & Severity**：50 / medium

**related\_view**：`Top Triggered Rules`

**data\_source**：`top_triggered_rules`

**template**：

```plaintext
"Rule \"{rule_name}\" accounts for {share_pct_display} of all rule triggers this period ({current_count} of {total_count})."
```

**variables 示例**：

```plaintext
{
  "rule_name": "Mixer Interaction",
  "share_pct": 0.3333,
  "share_pct_display": "33.3%",
  "current_count": 105,
  "total_count": 315
}
```
---

## 5.4 Identity Risk 类规则

### 规则：`identity_risk_distribution_shift`

**目的**：识别目标自身风险类型分布是否出现明显变化

**数据来源**：

*   `identity_exposure_distribution.items[].risk_indicator`
    
*   `identity_exposure_distribution.items[].current_unique_targets`
    
*   `identity_exposure_distribution.items[].change_pct`
    
*   `identity_exposure_distribution.items[].change_pp`
    

**触发条件**：

```plaintext
identity_exposure_distribution.items 中按 current_unique_targets 排序的 top-2 indicator
  中至少有一个满足：
    abs(change_pct) >= 0.30                       // 数量变化 ≥ 30%
    OR abs(change_pp) >= 0.05                     // 占比变化 ≥ 5pp
AND
满足条件的 indicator 的 current_unique_targets >= 10
```

只输出变化最显著的 indicator（按 `abs(change_pct)` 排序取 top-1）作为 evidence 内容。

单次 insight 中最多输出 **1 条** `identity_risk_distribution_shift` evidence。

**边界条件**：

*   满足条件的 indicator 的 `current_unique_targets < 10` → 不触发
    
*   若 `identity_exposure_distribution.items` 为空或缺失 → 不触发
    

**Priority & Severity**：65 / medium

**driver\_indicator**：触发条件满足的 `risk_indicator` 名称（如 `"Mixing"`）

**related\_view**：`Identity Exposure Distribution`

**data\_source**：`identity_exposure_distribution`

**template**：

```plaintext
"{risk_type} risk indicator \"{indicator}\" changed by {change_pct_display} this period ({prev_count} → {current_count} unique targets), with its share shifting by {change_pp_display}."
```

**variables 示例**：

```plaintext
{
  "risk_type": "Entity",
  "indicator": "Mixing",
  "change_pct": 0.5294,
  "change_pct_display": "+52.9%",
  "prev_count": 17,
  "current_count": 26,
  "change_pp": 0.08,
  "change_pp_display": "+8.0pp"
}
```
---

### 规则：`identity_risk_concentration`

**目的**：识别某一风险类型是否在目标自身风险分布中明显占优

**数据来源**：

*   `identity_exposure_distribution.items[].risk_indicator`
    
*   `identity_exposure_distribution.items[].current_pct`
    
*   `identity_exposure_distribution.items[].current_unique_targets`
    

**触发条件**：

```plaintext
按 current_pct 排序取 top-1 indicator（记为 top1）：
  top1.current_pct >= 0.30                        // 占比 ≥ 30%
  AND top1.current_unique_targets >= 15           // 绝对量 ≥ 15
  AND (top1.current_pct - top2.current_pct) >= 0.05   // 与 top2 的差距 ≥ 5pp（主导性显著）
```

若 items 中只有 1 个 indicator，则不需要 top2 差距判断，直接用前两个条件。

**边界条件**：

*   `top1.current_unique_targets < 15` → 不触发
    
*   `top1.current_pct - top2.current_pct < 0.05` → 不触发（无明显主导项）
    

**Priority & Severity**：60 / medium

**driver\_indicator**：top1 的 `risk_indicator` 名称

**related\_view**：`Identity Exposure Distribution`

**data\_source**：`identity_exposure_distribution`

**template**：

```plaintext
"{risk_type} risk is concentrated in \"{indicator}\", accounting for {share_pct_display} of identified targets ({current_count} unique targets)."
```

**variables 示例**：

```plaintext
{
  "risk_type": "Entity",
  "indicator": "Mixing",
  "share_pct": 0.32,
  "share_pct_display": "32.0%",
  "current_count": 26
}
```
---

## 5.5 Interaction Risk 类规则

### 规则：`interaction_risk_increase`

**目的**：识别资金交互型风险是否明显上升

**数据来源**：

*   `risk_exposure_flow.flows[].exposure_value_usd_current`
    
*   `risk_exposure_flow.flows[].change_pct`
    
*   `risk_exposure_flow.summary.total_inflow_current / previous`
    
*   `risk_exposure_flow.summary.total_outflow_current / previous`
    

**触发条件**：

```plaintext
满足任一：
  条件A：某条单一 flow（单一 direction + indicator 组合）满足：
    change_pct >= 0.25                            // 单条 flow 增长 ≥ 25%
    AND exposure_value_usd_current >= 100000      // 当前金额 ≥ $100K
  条件B：总 inflow 或总 outflow 满足：
    (total_inflow_current - total_inflow_previous) / total_inflow_previous >= 0.20
    AND total_inflow_current >= 100000
    （outflow 同理）
```

条件A 和 条件B 可独立触发，但**只输出 1 条** `interaction_risk_increase` evidence（选触发最显著的）。

**边界条件**：

*   `previous_value < 20000 AND current_value < 100000` → 小基数放大，不触发
    
*   总 inflow/outflow 变化绝对值 `< 50000 USD` 且单条 flow 金额 `< 100000 USD` → 不触发
    
*   `previous period` 数据不存在 → 不触发
    

**Priority & Severity**：80 / high

**driver\_indicator**：触发条件中变化最大的 flow 对应的 indicator（若条件B触发则为 null）

**related\_view**：`Risk Exposure Flow`

**data\_source**：`risk_exposure_flow`

**template（条件A触发时）**：

```plaintext
"Interaction risk from \"{indicator}\" ({direction}) increased by {change_pct_display}, with current exposure at {current_usd_display}."
```

**template（条件B触发时）**：

```plaintext
"Total {direction} interaction risk increased by {change_pct_display}, reaching {current_usd_display} this period."
```

**variables 示例（条件A）**：

```plaintext
{
  "indicator": "Mixing",
  "direction": "inflow",
  "change_pct": 0.2523,
  "change_pct_display": "+25.2%",
  "current_usd": 670000,
  "current_usd_display": "$670,000"
}
```
---

### 规则：`interaction_risk_concentration`

**目的**：识别某个风险类型是否在资金交互中占据明显主导

**数据来源**：

*   `risk_exposure_flow.flows[].direction`
    
*   `risk_exposure_flow.flows[].source_node`（inflow 方向的 indicator）
    
*   `risk_exposure_flow.flows[].exposure_value_usd_current`
    
*   `risk_exposure_flow.summary.total_inflow_current / total_outflow_current`
    

**触发条件**：

```plaintext
存在某个 direction（inflow 或 outflow）中，某 indicator 满足：
  indicator_usd_current / total_direction_usd_current >= 0.30  // 占比 ≥ 30%
  AND indicator_usd_current >= 100000                          // 金额 ≥ $100K
  AND total_direction_usd_current > 0
```

**边界条件**：

*   `"Others"` 占比 `>= 0.40` 且最高命名 indicator 占比 `< 0.25` → 不触发（分布过于分散，结论不可靠）
    
*   `total_direction_usd_current` 为 0 → 不触发
    

**Priority & Severity**：75 / medium

**driver\_indicator**：触发条件满足的 indicator 名称

**related\_view**：`Risk Exposure Flow`

**data\_source**：`risk_exposure_flow`

**template**：

```plaintext
"\"{indicator}\" accounts for {share_pct_display} of {direction} interaction risk, with {current_usd_display} in the current period."
```

**variables 示例**：

```plaintext
{
  "indicator": "Mixing",
  "direction": "inflow",
  "share_pct": 0.35,
  "share_pct_display": "35.0%",
  "current_usd": 670000,
  "current_usd_display": "$670,000"
}
```
---

### 规则：`interaction_risk_driver`

**目的**：明确指出推动 Interaction Risk 变化的主要 Risk Indicator（supporting evidence）

**触发条件**（必须为第二轮评估，依赖前序结果）：

```plaintext
已存在至少一条：
  interaction_risk_increase（priority 80）
  OR interaction_risk_concentration（priority 75）
AND
存在某 indicator 在当前周期的 exposure_value_usd_current 明显领先：
  top1_usd - top2_usd >= 50000
  OR top1_change_pct - top2_change_pct >= 0.10
```

**边界条件**：

*   若 top1 与 top2 金额差 `< 50000 USD` 且增量差 `< 0.10` → 不触发（无明显主导）
    
*   该规则设计为 supporting evidence，在 top-5 evidence 列表中优先级低于 `interaction_risk_increase`（80）和 `interaction_risk_concentration`（75）
    

**Priority & Severity**：70 / medium

**driver\_indicator**：top1 indicator 名称

**related\_view**：`Risk Exposure Flow`

**data\_source**：`risk_exposure_flow`

**template**：

```plaintext
"The primary driver of interaction risk is \"{indicator}\", with {current_usd_display} exposure ({direction}), ahead of the next indicator by {gap_usd_display}."
```

**variables 示例**：

```plaintext
{
  "indicator": "Mixing",
  "current_usd": 670000,
  "current_usd_display": "$670,000",
  "direction": "inflow",
  "gap_usd": 280000,
  "gap_usd_display": "$280,000"
}
```
---

## 5.6 Screened Transaction Volume 类规则

### 规则：`screened_tx_volume_increase`

**目的**：识别被筛查交易金额是否明显上升

**数据来源**：

*   `screened_tx_volume_usd.series[].tx_value_usd_current`
    
*   `screened_tx_volume_usd.series[].tx_value_usd_previous`
    

**计算方式**：使用整个时间周期的**汇总值**对比，而非单个 bucket：

```plaintext
total_current  = sum(series[].tx_value_usd_current)
total_previous = sum(series[].tx_value_usd_previous)
period_change_pct = (total_current - total_previous) / total_previous
```

**触发条件**：

```plaintext
period_change_pct >= 0.25                         // 总量增长 ≥ 25%
AND
total_current >= 500000                           // 当前周期总量 ≥ $500K
```

**边界条件**：

*   `total_current < 500000` → 不触发
    
*   `previous period` 数据不存在 → 不触发
    
*   `total_previous = 0` 且 `total_current >= 500000` → 触发（前期无数据，视为 100% 增长，注意 template 中说明）
    

**Priority & Severity**：45 / low

**related\_view**：`Screened Transaction Volume`

**data\_source**：`screened_tx_volume_usd`

**template**：

```plaintext
"Screened transaction volume increased by {change_pct_display} to {current_usd_display} this period (from {prev_usd_display})."
```

**variables 示例**：

```plaintext
{
  "change_pct": 0.337,
  "change_pct_display": "+33.7%",
  "current_usd": 12570000,
  "current_usd_display": "$12.57M",
  "prev_usd": 9400000,
  "prev_usd_display": "$9.40M"
}
```
---

### 规则：`screened_tx_volume_decrease`

**目的**：识别被筛查交易金额是否明显下降

**数据来源**：同 `screened_tx_volume_increase`

**触发条件**：

```plaintext
period_change_pct <= -0.25                        // 总量下降 ≥ 25%
AND
(total_current >= 500000 OR total_previous >= 500000)  // 至少一个周期 ≥ $500K
```

**边界条件**：同 `screened_tx_volume_increase`

**Priority & Severity**：45 / low

**related\_view**：`Screened Transaction Volume`

**data\_source**：`screened_tx_volume_usd`

**template**：

```plaintext
"Screened transaction volume decreased by {change_pct_display} to {current_usd_display} this period (from {prev_usd_display})."
```

**variables 示例**：

```plaintext
{
  "change_pct": -0.2766,
  "change_pct_display": "-27.7%",
  "current_usd": 6800000,
  "current_usd_display": "$6.80M",
  "prev_usd": 9400000,
  "prev_usd_display": "$9.40M"
}
```
---

### 规则：`screened_tx_volume_spike`

**目的**：识别某个时间 bucket 的交易金额异常 spike

**数据来源**：

*   `screened_tx_volume_usd.series[].tx_value_usd_current`
    
*   `screened_tx_volume_usd.granularity`
    

**period\_avg 计算**：`mean(series[].tx_value_usd_current)`（对应章节 2.5 定义）

**触发条件**：

```plaintext
series bucket 数量 >= 3
AND
存在某个 bucket 满足：
  tx_value_usd_current > period_avg × 1.5         // spike 倍数 ≥ 1.5x
  AND tx_value_usd_current >= 250000              // 单 bucket ≥ $250K
```

**边界条件**：

*   `granularity = "month"` → 不触发
    
*   bucket 数量 `< 3` → 不触发
    

**Priority & Severity**：38 / low

**related\_view**：`Screened Transaction Volume`

**data\_source**：`screened_tx_volume_usd`

**template**：

```plaintext
"Transaction volume spike detected: {spike_date_display} recorded {spike_usd_display} — {spike_multiplier_display} the period average of {period_avg_usd_display}."
```

**variables 示例**：

```plaintext
{
  "spike_date": "2026-03-03T00:00:00Z",
  "spike_date_display": "Mar 3",
  "spike_usd": 12570000,
  "spike_usd_display": "$12.57M",
  "spike_multiplier": 2.2,
  "spike_multiplier_display": "2.2x",
  "period_avg_usd": 5700000,
  "period_avg_usd_display": "$5.70M"
}
```
---

## 5.7 Screening Behavior 类规则

### 规则：`screening_count_surge`

**目的**：识别 screening count 是否明显增加

**数据来源**：

*   `core_metrics.total_screening_count.current / previous / change_pct`
    

**触发条件**：

```plaintext
total_screening_count.change_pct >= 0.50          // 增长 ≥ 50%
AND
total_screening_count.current >= 100              // 当前绝对量 ≥ 100
```

**边界条件**：

*   `current < 100` → 不触发（绝对量过小）
    
*   若 `screening_rescreening_signal` 同时触发且描述同一变化，按去重规则处理（`screening_count_surge` priority 35 > `screening_rescreening_signal` priority 25，优先保留前者）
    

**Priority & Severity**：35 / low

**related\_view**：`Screening Count Trend`

**data\_source**：`core_metrics`

**template**：

```plaintext
"Screening count surged by {change_pct_display} this period, reaching {current_count} total screening actions (from {prev_count})."
```

**variables 示例**：

```plaintext
{
  "change_pct": 0.50,
  "change_pct_display": "+50.0%",
  "current_count": 2870,
  "prev_count": 1913
}
```
---

### 规则：`screening_target_surge`

**目的**：识别 unique screened targets 是否明显增加

**数据来源**：

*   `core_metrics.total_targets_screened.current / previous / change_pct`
    

**触发条件**：

```plaintext
total_targets_screened.change_pct >= 0.30         // 增长 ≥ 30%
AND
total_targets_screened.current >= 50              // 当前绝对量 ≥ 50
```

**边界条件**：

*   `current < 50` → 不触发
    
*   若同时触发 `screening_rescreening_signal`，因为 target 也在增加，则抑制 rescreening\_signal（见 5.7.4）
    

**Priority & Severity**：30 / low

**related\_view**：`Risk Trend`

**data\_source**：`core_metrics`

**template**：

```plaintext
"Unique screened targets grew by {change_pct_display} this period, from {prev_count} to {current_count}."
```

**variables 示例**：Insert Link

```plaintext
{
  "change_pct": 0.30,
  "change_pct_display": "+30.0%",
  "prev_count": 1870,
  "current_count": 2430
}
```
---

### 规则：`screening_rescreening_signal`

**目的**：识别 screening count 明显增加但 unique targets 相对稳定的情况，提示可能存在 re-screening 行为

**数据来源**：

*   `core_metrics.total_screening_count.change_pct / current`
    
*   `core_metrics.total_targets_screened.change_pct`
    

**触发条件**：

```plaintext
total_screening_count.change_pct >= 0.50          // count 增长 ≥ 50%
AND
abs(total_targets_screened.change_pct) <= 0.10    // target 变化 ≤ ±10%
AND
total_screening_count.current >= 100
```

**边界条件**：

*   若 `screening_count_surge` 已触发且 `screening_target_surge` 也同时触发 → 抑制本规则（count 和 target 都在增加，不是 re-screening 信号）
    
*   本规则设计为 supporting evidence，不独占 top 位置
    

**Priority & Severity**：25 / low

**related\_view**：`Screening Count Trend`

**data\_source**：`core_metrics`

**template**：

```plaintext
"Screening count increased by {count_change_pct_display} while unique targets remained nearly stable ({target_change_pct_display}), suggesting possible re-screening activity."
```

**variables 示例**：

```plaintext
{
  "count_change_pct": 0.50,
  "count_change_pct_display": "+50.0%",
  "target_change_pct": 0.04,
  "target_change_pct_display": "+4.0%"
}
```
---

### 规则：`screening_source_shift`

**目的**：识别 API / Manual / System 来源结构是否发生明显变化

**数据来源**：

*   `screening_source_breakdown[].source`
    
*   `screening_source_breakdown[].current_pct`
    
*   `screening_source_breakdown[].change_pp`
    
*   `screening_source_breakdown[].current_count`
    

**触发条件**：

```plaintext
存在某个 source（API / Manual / System）满足：
  abs(change_pp) >= 0.05                          // 来源占比变化 ≥ 5pp
  AND current_count >= 30                         // 当前该来源绝对量 ≥ 30
  AND current_pct > 0                             // 排除全 0 来源
```

输出变化幅度最大（按 `abs(change_pp)`）的 1 个 source 作为 evidence 内容。

**边界条件**：

*   `current_count < 30` → 该 source 不参与触发判断
    
*   `current_pct = 0` 且 `previous_pct = 0` → 排除（全 0 来源无意义）
    
*   每次 insight 只输出 1 条 `screening_source_shift`
    

**Priority & Severity**：20 / low

**related\_view**：`Screening Source Breakdown`

**data\_source**：`screening_source_breakdown`

**template**：

```plaintext
"Screening source mix shifted: \"{source}\" share changed by {change_pp_display} to {current_pct_display} of total screenings this period."
```

**variables 示例**：

```plaintext
{
  "source": "API",
  "change_pp": 0.0306,
  "change_pp_display": "+3.1pp",
  "current_pct": 0.5226,
  "current_pct_display": "52.3%"
}
```
---

## 5.8 Fallback 类规则

### 规则：`no_significant_change`

**目的**：在没有任何明显趋势、异常、集中度、screening 变化时，提供稳定兜底结论

**触发条件**：

```plaintext
所有 priority >= 20 的规则在去重和 prioritization 后均未触发
```

**边界条件**：

*   该规则始终为 low severity
    
*   不应覆盖真实存在的重要信号
    

**Priority & Severity**：10 / low

**related\_view**：`Risk Trend`

**data\_source**：null

**template**：

```plaintext
"No significant changes detected in risk levels, interaction risk, screening activity, or screened transaction volume during this period."
```

**variables**：`{}`

---

# 6. 优先级策略与 Evidence 选取

## 6.1 优先级排序（已在第 4 节 Priority 速查表中定义）

默认从高到低：

1.  Spike 类（100 / 95）
    
2.  Overall risk increase（90）
    
3.  Overall risk decrease（85）
    
4.  Interaction risk increase（80）
    
5.  Interaction risk concentration（75）
    
6.  Interaction risk driver（70，supporting）
    
7.  Identity risk distribution shift（65）
    
8.  Identity risk concentration（60）
    
9.  Rule trigger surge（55）
    
10.  Rule concentration（50）
    
11.  Screened TX volume increase / decrease（45）
    
12.  Screened TX volume spike（38）
    
13.  Screening count surge（35）
    
14.  Screening target surge（30）
    
15.  Screening rescreening signal（25）
    
16.  Screening source shift（20）
    
17.  No significant change（10）
    

## 6.2 送入 Prompt 的 Evidence 数量

*   去重后按 priority 降序排列
    
*   送入 prompt 的 evidence 上限：**top 5 条**
    
*   `no_significant_change` 只在无其他 evidence 时出现，且仍计入 top 5 限制
    

## 6.3 Evidence 对 LLM 输出的引导

| evidence severity | 对 LLM summary 的期望 |
| --- | --- |
| high | summary 必须提及；`overall_trend` 字段应对应 `increasing` 或 `decreasing` |
| medium | summary 应提及，或在 `key_highlights` 中体现 |
| low | 可纳入 `key_highlights` 或作为 `action.related_view` 依据 |

Spike evidence（priority 95–100）存在时，summary 必须包含 spike 的日期和量级描述。

---

# 7. 去重规则

## 7.1 Spike 去重

*   若 `address_risk_spike` 或 `transaction_risk_spike` 已触发，则抑制 `overall_risk_spike`
    
*   不同 spike（address 和 transaction）指向同一时间 bucket → 只保留 priority 更高的（同分时保留 `address_risk_spike`）
    
*   若 spike 完整解释了 `overall_risk_increase`（spike 仅为单 bucket 异常，非持续趋势）→ 可抑制 `overall_risk_increase`
    

**判断 spike 是否"完整解释"trend 的标准**：

*   risk_trend.series 中只有 1 个 bucket 的 \`high_plus_critical_ `明显高于其余 buckets（其余均在` periodavg × 1.2\` 以内）
    
*   则认为 spike 已完整解释，`overall_risk_increase` 可抑制
    

## 7.2 Interaction Risk 去重

*   `interaction_risk_increase`（80）和 `interaction_risk_driver`（70）若同时触发且描述同一 indicator：可同时保留（一主一辅）
    
*   `interaction_risk_concentration`（75）和 `interaction_risk_driver`（70）若同时触发：可同时保留
    

## 7.3 Screening 去重

*   `screening_count_surge`（35）和 `screening_rescreening_signal`（25）若同时触发且 target 也在增长：保留 `screening_count_surge`，抑制 `screening_rescreening_signal`
    
*   `screening_count_surge`（35）和 `screening_rescreening_signal`（25）若同时触发但 target 稳定：保留两者（一主一辅），优先级差距足够不会抢占 top 5
    

## 7.4 Rule Trigger 去重

*   `rule_trigger_surge`（55）和 `rule_concentration`（50）若指向同一条规则：只保留 `rule_trigger_surge`
    

---

# 8. 边界条件检查清单

每新增一条规则，都必须明确以下所有字段：

| 检查项 | 说明 |
| --- | --- |
| 来源图表 / facts 字段 | 精确到字段路径 |
| 是否依赖前一周期数据 | 若依赖，需明确"previous period 缺失时不触发" |
| 最小 count / amount | 绝对量阈值（decimal） |
| 比例阈值 vs 百分点阈值 | 明确使用哪种，decimal 格式 |
| 抑制条件 | 何时被更高 priority 规则覆盖 |
| priority（0–100 整数） | 见第 4 节速查表 |
| severity | high / medium / low |
| related\_view | 精确的前端视图名称 |
| driver\_indicator | 何时为具体 indicator 名，何时为 null |
| template + variables | 包含所有必要数值的事实句；template 中的占位符必须引用 `_display` 字段 |
| variables 中的 `_display` 字段 | 每个用于 template 的数值都有对应 `_display` 格式化版本（见第 3 节格式规范） |

没有完整定义以上所有字段的规则，**不应进入生产环境**。

---

# 9. 已确认阈值汇总（v1.0）

以下为本文档当前确认的所有阈值，可直接用于配置文件：

```plaintext
{
  "overall_risk_trend": {
    "count_change_pct_threshold": 0.20,
    "ratio_change_pp_threshold": 0.005,
    "min_count_for_count_trigger": 10,
    "min_count_for_ratio_only_trigger": 20
  },
  "risk_spike": {
    "multiplier_vs_avg": 1.5,
    "min_value": 8,
    "min_buckets": 3,
    "disabled_granularity": ["month"]
  },
  "rule_trigger": {
    "surge_change_pct_threshold": 0.50,
    "surge_min_count": 20,
    "concentration_share_threshold": 0.30,
    "concentration_min_count": 30
  },
  "identity_risk": {
    "distribution_shift_change_pct_threshold": 0.30,
    "distribution_shift_change_pp_threshold": 0.05,
    "distribution_shift_min_count": 10,
    "concentration_share_threshold": 0.30,
    "concentration_min_count": 15,
    "concentration_min_top1_top2_gap_pp": 0.05
  },
  "interaction_risk": {
    "flow_change_pct_threshold": 0.25,
    "total_flow_change_pct_threshold": 0.20,
    "min_usd": 100000,
    "small_base_prev_max": 20000,
    "small_base_current_min": 100000,
    "min_abs_change_usd": 50000,
    "concentration_share_threshold": 0.30,
    "concentration_others_max": 0.40,
    "concentration_named_min": 0.25,
    "driver_min_usd_gap": 50000,
    "driver_min_change_pct_gap": 0.10
  },
  "screened_tx_volume": {
    "change_pct_threshold": 0.25,
    "min_current_usd": 500000,
    "spike_multiplier": 1.5,
    "spike_min_bucket_usd": 250000,
    "spike_min_buckets": 3,
    "disabled_granularity": ["month"]
  },
  "screening": {
    "count_surge_change_pct_threshold": 0.50,
    "count_surge_min_current": 100,
    "target_surge_change_pct_threshold": 0.30,
    "target_surge_min_current": 50,
    "rescreening_count_change_pct_threshold": 0.50,
    "rescreening_target_stable_threshold": 0.10,
    "rescreening_min_count": 100,
    "source_shift_change_pp_threshold": 0.05,
    "source_shift_min_count": 30
  }
}
```