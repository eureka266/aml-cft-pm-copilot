# Risk Exposure 饼图优化

# 背景与目标

在当前的 Risk Exposure 模块中，饼图数据基于已触发的 Alert（Triggered Alerts）进行统计和展示。  
然而，地址或交易在 Exposure（资金溯源和追踪）过程中可能识别出大量未触发 Alert 的风险敞口（Exposure Value），原因包括但不限于：

*   风险金额（Exposure Value）未达到 Alert 阈值
    
*   用户自定义规则未覆盖相应场景（没有配置对应的 risk indicator）
    

此类实际存在的风险敞口未在饼图中体现，引发用户对数据完整性的质疑。

### 痛点

*   当前饼图仅反映已触发 Alert 的部分风险 → **存在大量“隐形风险”未被展示**
    
*   用户误以为展示的 Exposure 饼图包含了完孩子呢过的数据 
    

### 目标

*   调整饼图的数据源，使其基于 **所有风险敞口数据 (Total Risk Exposure)**，无论是否触发 Alert
    
*   提升风险暴露展示的准确性、一致性与可信度
    
*   保留 alert 与 exposure 之间的层级关系：Exposure 表示资金分布；Alert 表示哪些风险已达到阈值
    

# 数据源及分组逻辑

## 数据

饼图**数据** 从原本的 Alerts 数据 → 图数据库返回的全部 Risk Exposure。

## 分组

因为 exposure 是基于 trace path（金流路径）的记录，而每条路径可以对应多个风险 indicator。

如果我们按单个 indicator 计算，就会产生重复。

示例： 一个地址 inflow 仅有一条资金路径，路径终点地址有 risk indicator：

*   Sanctioned
    
*   Blocked
    

如果分开计算：

*   Sanctioned = 100%
    
*   Blocked = 100%  
    → 饼图合计 = 200%
    

### 分组逻辑

每条 exposure record 的 risk\_indicator 先按照一定的逻辑排序，然后作为组合 key。

示例：

*   \["Sanctioned"\] → 组名：Sanctioned
    
*   \["Blocked"\] → 组名：Blocked
    
*   \["Sanctioned", "Blocked"\] → 组名：Sanctioned, Blocked
    
*   \[\]（没有风险）→ 不展示，归入 Other
    

### 组合方式

对属于同一风险组合的 exposure records：

*   exposure\_value\_usd 累加
    
*   risk\_level 取组中 **最高风险级别**
    
*   triggered\_alert = true 若组内任一 record 有 alert
    

对没有 risk indicator 的 exposure 路径：

*   全部归入 “Other”
    

# 展示

| 状态 | 展示颜色 |
| --- | --- |
| 该分组有 triggered alert | 对应 risk level 的颜色（Critical/High/Medium/Low） |
| 无 triggered alert，但有 Risk Indicator | **灰色** |
| Other（无风险敞口） | **浅灰色/Neutral** |

#### Hover 后展示

1.   触发过 alert 的分组，展示：
    
    *   Exposure Value (USD)
        
    *   Exposure Percent (%)
        
    *   Risk Level + 该分组的 risk indicator
        
    *   Triggered by: Risk Engine Name (可以点击跳转到对应的 risk engine)
        
2.  未触发过 alert，展示：
    
    *   Exposure Value (USD)
        
    *   Exposure Percent (%)
        
    *   No alerts triggered.
        

### By Address

*   饼图切换到 By Address 后，仅展示触发过 Alert 的地址
    
*   其余未触发过 Alert 的 risk indicator 合并为一整个区域，显示 Other risk address，hover 上去展示合并后的 exposure value、exposure percent、文案："No alerts triggered."
    

# 其他说明

饼图下方的 risk exposure 表格，依然和当前保持一致，仅展示**已触发了 alert** 的 risk indicator 分组下对应的每个地址、最短跳数、exposure value 和 exposure percent。