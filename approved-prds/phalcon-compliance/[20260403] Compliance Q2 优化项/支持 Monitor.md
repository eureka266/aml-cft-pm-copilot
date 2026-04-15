# 支持 Monitor

# 背景与目标

## 现状问题

当前产品提供 Auto Re-screening 功能，用于定期对地址进行重新筛查，以发现风险变化。但在实际使用中存在以下问题：

*   **用户理解成本高**："Re-screening" 概念偏系统能力，非用户心智语言；用户难以理解其实际价值（持续监控风险变化）
    
*   **使用门槛高**：需要配置扫描周期；消耗筛查次数（credits）；用户存在心理负担（担心消耗过多）
    

## 目标

将 Auto Re-screening 升级为 Monitor（监控）能力，建立更符合用户心智的功能模型：用户可以持续关注某个地址的风险变化，并在关键变化发生时收到提醒。

**核心目标：**

*   降低理解成本（从"扫描" → "监控"）
    
*   降低使用门槛（无需配置周期）
    
*   提供持续风险感知能力
    
*   建立可扩展的长期功能基础
    

## 范围说明

**本次 PRD 包含：**

*   地址详情页 Monitor 功能
    
*   地址列表页 Monitor 状态与操作
    
*   Monitor 管理页
    
*   Audit Logs 新增日志类型
    
*   API 变更与 deprecation 计划
    
*   用户通知方案
    
*   Monitor 内部实现逻辑
    

**本次 PRD 不包含（后续处理）：**

*   Notes / Tags 从 Data Management 迁移
    
*   列表页批量 Monitor 操作
    
*   Monitor 管理页的批量操作
    

# 计费与权限（Pricing Plan V3 上线前）

## 当前阶段策略

Pricing Plan V3 上线前，Monitor 功能对付费用户**限时免费**，无额外收费。

| 用户层级 | Monitor 权限 |
| --- | --- |
| Starter / Growth / Pro / Enterprise | 可开启，上限 50 个 active Monitor |
| Free | 无权限，点击引导付费升级 |

*   每用户最多同时保持 **50 个 active Monitor**
    
*   超出 50 个时，给用户明确提示
    

## Pricing Plan V3 上线后的迁移

*   Monitor 功能切换为 Add-on 计费（详细见 Pricing Plan V3 PRD）
    
*   V3 上线时，用户 active Monitor 数量超出免费额度（1 个）的，超出部分**自动停止**
    
*   系统通知用户：可购买 Monitor Add-on 后在管理页手动重新开启所需 Monitor
    
*   计费额度统一按 **active Monitor 数量**计算
    

# Monitor 内部实现逻辑

## 技术实现

Monitor 底层通过定期 re-screening 实现，**不对用户暴露**扫描细节。用户感知的是"持续监控"，而非"定期扫描"。

## 扫描周期（动态调整）

每次扫描完成后，根据地址最新交易时间重新评估活跃度，动态决定下次扫描时间。

| 活跃度 | 判定标准（待确认） | 扫描频率 |
| --- | --- | --- |
| 高活跃 | 过去 1 小时内有交易 | 每 15–30 分钟 |
| 中活跃 | 过去 24 小时内有交易 | 每 1–2 小时 |
| 低活跃 | 超过 24 小时无交易 | 每 6–12 小时 |
| 不活跃 | 超过 7 天无交易 | 每 24–48 小时 |

*   对于过去 24 小时内交易笔数超过 100 笔的大交易量地址（阈值待确认）：
    
    *   不硬性限制，不阻止开启 Monitor
        
    *   用户开启 Monitor 时展示提示：This address has high transaction volume. Risk data may have a slight delay, and monitoring alerts may be more frequent.
        

# 功能设计

## 地址详情页

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bVrW2vLq4B/img/a5da7a81-e9da-444f-a821-aa354656a74a.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bVrW2vLq4B/img/8eef9f9b-a695-4b43-9495-370bfea0f355.png)

>  设计时可能需要考虑：

>  - 顶部按钮会不会太多了

> \- 怎么展示 Monitoring 状态 Badge？现在感觉放不下了

**移除：**

*   Auto Re-screening 开关及周期配置
    

**新增：**

*   **\[Monitor\] 按钮**：未开启 Monitor 时展示，点击开启
    
*   **\[Stop Monitor\] 按钮**：已开启 Monitor 时展示，点击关闭
    
*   **\[Monitoring\] 状态 badge**：已开启时展示，表明该地址正在被监控
    

**权限逻辑：**

*   付费用户（active Monitor < 50）：正常开启
    
*   付费用户（active Monitor = 50）：点击展示提示：  
    You've reached the limit of 50 active monitors. Please stop monitoring another address before adding a new one.
    
*   Free 用户：点击引导付费升级，弹出升级
    

**现有 Auto Re-screening 数据处理：**

*   上线时直接下线，不自动迁移为 Monitor
    
*   用户需手动开启 Monitor（通过提前通知引导，见用户通知方案章节）
    

## 地址列表页

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bVrW2vLq4B/img/38185a56-5f2a-4b76-9632-3ebac7ff6552.png)

**新增 Monitor 状态展示：**

*   列表每行增加 Monitoring 状态标识，已开启 Monitor 的地址显示 "Monitoring" badge
    

**新增行内操作：**

*   最右侧的 action 下拉框中新增 Monitor / Stop Monitor 选项
    
*   权限逻辑与详情页一致
    
*   操作后状态实时更新，无需刷新页面
    

**新增筛选项：**

*   在现有筛选器中增加 Monitor 状态筛选：
    
    *   "Monitoring"（勾选后只显示已开启 Monitor 的地址）
        
    *   "Not Monitoring"（勾选后只显示未开启的地址）
        
    *   默认不勾选 = 显示全部
        

## Monitor 管理页

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bVrW2vLq4B/img/fadaf639-eb26-4488-afd0-d1277880110e.png)

**页面位置：** Data Management 页面新增 Monitors Tab

**页面定位：** 集中展示和管理用户所有 Monitor 记录（含历史已停止的），方便用户感知用量使用情况和历史监控记录。

**顶部展示用量：**

*   当前 active Monitor 数量 / 上限（如：12 / 50 Active）
    

**Monitor 列表：**

| 字段 | 说明 |
| --- | --- |
| 地址 | 可点击跳转地址详情页 |
| 状态 | Active / Stopped |
| 开启时间 | Monitor 最近一次开启的时间 |
| 最近 Alert 时间 | 最近一次来源为 Monitor 的 Alert 触发时间；无则显示 "—" |
| 操作 | Active 状态显示 \[Stop Monitor\]；Stopped 状态显示 \[Monitor\] |

**筛选：**

*   状态筛选：Active / Stopped，默认显示 Active
    

## Audit Logs

### 现有日志调整

*   **"Address Screened"** 来源字段：移除 "Auto Re-screening"，保留 Manual / API
    
*   **"Alert Triggered"**（地址页和 Alert 页）：仅对 Monitor 触发的 Alert 新增来源标注 Source: Monitor；Manual / API 触发的保持现状
    

### 新增日志类型

| Event | Log 内容 | 触发时机 |
| --- | --- | --- |
| 开启监控 | 标题：Monitor Started 时间：\[自动记录\] 操作人：{用户邮箱} | 用户手动开启 Monitor 时，记录在地址页面 |
| 停止监控 | 标题：Monitor Stopped 时间：\[自动记录\] 操作人：{用户邮箱} / System | 用户手动关闭，或系统强制停止时；系统强制停止时 Reason: Plan downgraded 或 Reason: Monitor limit exceeded |

**静默条件：** Monitor 扫描后与上次相比命中规则集合无变化时，不产生任何 log。

## API 变更

### 变更内容

*   `enableReScreening` 字段（Address Screen 请求参数）标记为 deprecated，过渡期后移除
    
*   新增独立 Monitor 接口：
    
    *   `POST /monitors`（开启 Monitor，传入 chainId, address）
        
    *   `DELETE /monitors/{id}`（关闭 Monitor）
        

### 过渡期策略

*   `enableReScreening` 字段保留但标记为 deprecated，与新 Monitor 接口并行运行
    
*   过渡期结束时间点：待定（上线后根据用户迁移情况决定）
    
*   过渡期内旧字段仍可正常传递（但不起作用），但 API 文档中明确标注 deprecated 及预计下线时间
    

### 受影响用户

当前有在使用 `enableReScreening` 字段的 Enterprise 用户（少量）。

## 用户通知方案

### 阶段一：功能上线前

**目标受众：** 当前有在使用 Auto Re-screening 的用户（重点：Enterprise API 用户）

**通知渠道：**

*   Email 通知受影响用户
    
*   产品内 banner 提示（登录后可见）
    

**Email 文案：**

> **Subject:** Action Required: Auto Re-screening is becoming Monitor

> Hi \[Name\],

> We're upgrading Auto Re-screening to a new feature called **Monitor**, which gives you real-time risk change awareness without manual configuration.

> **What's changing:**

*   Auto Re-screening will be removed on \[date\]
    
*   Your existing Re-screening configurations will not be migrated automatically
    
*   You'll need to manually enable Monitor on addresses you want to keep tracking
    
*   The `enableReScreening` API field will be deprecated (details in our API docs)
    

> Monitor is currently **free for all paid users** — no extra charge during this period.

> **What you need to do:** After the update, go to your address list and enable Monitor on addresses you want to continue tracking.

> Questions? Reply to this email or contact support.

**Banner 文案：**

> **Auto Re-screening is being replaced by Monitor.** Your existing configurations will not migrate automatically. Learn more

### 阶段二：功能上线后

*   API 文档中标注 deprecated 字段及预计下线时间
    
*   产品内对仍在使用旧 Auto Re-screening 配置的地址展示迁移提示，引导用户切换到 Monitor
    

## 边界情况处理

| 场景 | 处理方式 |
| --- | --- |
| 用户删除已开启 Monitor 的地址 | Monitor 自动停止，记录 Monitor Stopped（来源：System） |
| 付费用户降级为 Free | 所有 Monitor 自动停止，记录 Monitor Stopped（来源：System，Reason: Plan downgraded），通知用户；重新升级后需手动重新开启 |
| Active Monitor 达到软上限（50 个） | 提示用户，阻止继续开启，不静默失败 |
| Pricing V3 上线，active 超出免费额度 | 超出部分自动停止，记录 Monitor Stopped（来源：System，Reason: Monitor limit exceeded），通知用户购买 Add-on 后手动重新开启 |