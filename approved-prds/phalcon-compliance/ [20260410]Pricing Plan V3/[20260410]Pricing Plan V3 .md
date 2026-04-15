# \[20260410\]Pricing Plan V3 

# 背景与目标

Phalcon Compliance 定价体系从 V2 升级到 V3，核心功能：

*   **简化付费路径**：引入 Credits PAYG（按需购买）替代 Starter 订阅，降低首次付费门槛
    
*   **重组订阅档位**：Growth/Pro 更名为 Essential/Scale，增加灵活的档位（Screen 数）选择
    
*   **引入 Monitor Add-on**：新上线的 Monitor 功能变为付费 add-on，吸引付费且允许灵活扩容
    
*   **优化结算流程**：适配三家支付供应商的特性；改为 Modal 减少跳转步骤
    
*   **新增 Share Result**：用户可生成公开链接分享筛查结果，同时作为获客入口
    
*   **覆盖升级引导**：针对 V3 新结构设计转化触点
    

# V3 整体定价方案

## 计划总览

| 计划 | 类型 | 月付 | 年付（折合月） | Screenings |
| --- | --- | --- | --- | --- |
| **Free** | 订阅 | 免费 | — | 3/月 |
| **Credits** | PAYG | — | — | 按包购买，12 个月有效 |
| **Essential** | 订阅 | 从 $39/mo 起 | 从 $34/mo 起（省 17%） | 25–500/月（分档） |
| **Scale** | 订阅 | 从 $699/mo 起 | 从 $583/mo 起 | 750–5,000/月（分档） |
| **Enterprise** | 定制 | 联系销售 | — | 无限 |

## Credits 包档位

| Screenings | 总价 | 单价 |
| --- | --- | --- |
| 50 | $95 | $1.90/screening |
| 100 | $180 | $1.80/screening |
| 200 | $300 | $1.50/screening |
| 500 | $650 | $1.30/screening |
| 1,000 | $1,150 | $1.15/screening |
| 2,000 | $2,200 | $1.10/screening |

有效期：自购买日起 12 个月。账户同时有订阅 Plan 时，优先消耗订阅配额。

## Essential 订阅档位

| 月 screenings | 月付 | 年 screenings | 年付总价（折合月） |
| --- | --- | --- | --- |
| 25 | $39 | 300 | $408（$34/mo） |
| 50 | $59 | 600 | $600（$50/mo） |
| 100 | $109 | 1,200 | $1,104（$92/mo） |
| 250 | $249 | 3,000 | $2,520（$210/mo） |
| 500 | $469 | 6,000 | $4,800（$400/mo） |

## Scale 订阅档位

| 月 screenings | 月付 | 年 screenings | 年付总价（折合月） |
| --- | --- | --- | --- |
| 750 | $699 | 9,000 | $7,000（$583/mo） |
| 1,000 | $899 | 12,000 | $9,000（$750/mo） |
| 2,000 | $1,800 | 24,000 | $16,800（$1,400/mo） |
| 3,000 | $2,600 | 36,000 | $22,800（$1,900/mo） |
| 4,000 | $3,400 | 48,000 | $28,800（$2,400/mo） |
| 5,000 | $4,200 | 60,000 | $34,800（$2,900/mo） |

## Monitor Add-on（Essential / Scale 可叠加）

| 监控地址数 | 月付加价 | 年付加价（折合月） |
| --- | --- | --- |
| 1 | 免费包含 | — |
| 10 | +$60/mo | +$720/yr（+$60/mo） |
| 20 | +$100/mo | +$1,080/yr（+$90/mo） |
| 40 | +$160/mo | +$1,680/yr（+$140/mo） |
| 80 | +$240/mo | +$2,400/yr（+$200/mo） |
| 120 | +$360/mo | +$3,360/yr（+$280/mo） |
| 200 | +$500/mo | +$4,800/yr（+$400/mo） |

## Top-up（订阅用户补充额度）

订阅用户当前周期额度用尽后，可按**当前套餐单价**补充额度。补充额度随当前订阅周期失效，不结转。入口仅在 Billing & Usage 页展示，Pricing 页不展示。

## 升级/降级

*   升级/升档：沿用以前的逻辑，用户可随时升档/升级，计算 prorated amount 、立刻收费并升级。
    
*   降级/降档：沿用以前的逻辑，不允许降级和降档
    

# 功能权限对照表

| 功能模块 | Free | Credits | Essential | Scale | Enterprise |
| --- | --- | --- | --- | --- | --- |
| **支持链** | ETH、TRON | 全链 | 全链 | 全链 | 全链 |
| **Core Screening** |  |  |  |  |  |
| Risk Screen | ✅ | ✅ | ✅ | ✅ | ✅ |
| Default Risk Engines | ✅（只读） | ✅ | ✅ | ✅ | ✅ |
| **Sharing** |  |  |  |  |  |
| Share Result | ✅ | ✅ | ✅ | ✅ | ✅ |
| Audit Report Export | — | ✅ | ✅ | ✅ | ✅ |
| **Analytics & Data** |  |  |  |  |  |
| Alerts | ✅ | ✅ | ✅ | ✅ | ✅ |
| Analytics Dashboard | — | ✅ | ✅ | ✅ | ✅ |
| Customers | — | 1 | 10 | 30 | 无限 |
| Labels | 3 | 50 | 200 | 1,000 | 无限 |
| Tags | 3 | 50 | 200 | 1,000 | 无限 |
| **Compliance** |  |  |  |  |  |
| Custom Risk Engines | — | 3 | 10 | 20 | 无限 |
| STR / SAR Report | — | — | ✅ | ✅ | ✅ |
| Ongoing Monitoring | 7 天试用 | 7 天试用 | ✅（Add-on） | ✅（Add-on） | ✅ |
| Blacklist | — | — | 50 | 200 | 无限 |
| Whitelist | — | — | 50 | 200 | 无限 |
| **Notification** |  |  |  |  |  |
| Email | ✅ | ✅ | ✅ | ✅ | ✅ |
| Telegram / Lark | — | — | ✅ | ✅ | ✅ |
| Webhook & Others | — | — | — | ✅ | ✅ |
| **Team Collaboration** |  |  |  |  |  |
| Multi-seat Team Mode | — | — | — | — | ✅ |
| Task Assignment | — | — | — | — | ✅ |
| Comment | — | — | — | — | ✅ |
| **API & Workflow** |  |  |  |  |  |
| API Integration | — | — | — | ✅ | ✅ |
| **Support** |  |  |  |  |  |
| Email Support | ✅ | ✅ | ✅ | ✅ | ✅ |
| On-demand Training | — | — | — | ✅ | ✅ |
| Dedicated Support | — | — | — | — | ✅ |

**Ongoing Monitoring 7 天试用**：适用于 Free 和 Credits 用户，条件为该账户从未使用过 Monitor 功能（首次全局唯一）。

# 旧用户迁移方案

## 档位映射

| 当前 Plan | 当前价格 | V3 计划 | V3 价格 | 迁移 |
| --- | --- | --- | --- | --- |
| Starter（月付，50 次） | $59/mo | Essential 50 次档（月付） | $59/mo | 价格不变，功能升级，直接迁移 |
| Growth（月付，250 次） | $249/mo | Essential 250 次档（月付） | $249/mo | 价格功能不变，直接迁移 |
| Pro（月付，750 次） | $699/mo | Scale 750 次档（月付） | $699/mo | 价格功能不变，直接迁移 |

*   Starter → Essential 迁移，同等价格下新增权限：
    
    *   STR / SAR Report Export
        
    *   Blacklist & Whitelist（各 50 条）
        
    *   Telegram / Lark 通知
        
    *   Ongoing Monitoring（含 1 个免费监控地址）
        
    *   Audit Report Export
        
    *   Edit Default Risk Engines
        
    *   Share Result
        

## 迁移执行逻辑

*   **直接切换**：V3 上线时直接生效，对用户使用无影响（计划名称变化、功能只增不减）。
    
*   **无年付存量用户**：当前无 Growth / Pro 年付用户，无需处理锁价或过渡期问题。
    
*   **通知对象**：仅对**付费订阅用户**发送邮件通知（Free 用户不通知）。
    

# 用户通知方案

## 通知时间线

**通知对象：仅付费订阅用户（Starter / Growth / Pro），Free 用户不通知。**

| 时间节点 | 渠道 | 内容 |
| --- | --- | --- |
| V3 上线前 7–14 天 | 邮件 | 预告：Pricing Plan 即将更新，你的计划将升级为 Essential/Scale，价格不变，功能升级 |
| V3 上线当天 | 邮件 | 正式公告：新计划已上线，你的账户已迁移，附链接查看变化详情 |

## 5.3 产品内 Banner

V3 上线后 7 天内，已登录用户在产品内顶部展示一条横幅：

> 🎉 **Pricing Plan has been updated.** Your plan has been migrated. \[See what's new →\]

点击跳转至 Pricing 页或专门的 What's New 说明页。

# 详细方案

| 模块 | 功能范围 | 文档链接 |
| --- | --- | --- |
| Pricing Plans 页 | *   展示 V3 版本 Pricing Plan<br>    <br>*   free 用户、订阅用户查看内容区分 | [《Pricing Plans 页》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=QOG9lyrgJPvE5n02cXdoEk2vWzN67Mw4&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) |
| Checkout 流程 |  |  |
| Billing 页变更 | *   优化展示<br>    <br>*   增加 Top Up 入口 | [《Billing 页变更》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=dpYLaezmVNKEra7XcmRb34NOJrMqPxX6&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) |
| Share Result | *   地址/交易结果页增加**\[分享\]** 按钮，允许基于当前扫描结果生成结果分享页<br>    <br>*   用户可定义过期时间和是否被 index | [《Share Result》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=lyQod3RxJKBEy2ajiOmqMbkaVkb4Mw9r&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) |
| 升级引导 | *   优化当前系统中的升级引导<br>    <br>*   增加更多触发升级引导的场景，不同场景展示不同的引导内容 | [《升级引导》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=r1R7q3QmWe3XRKmoIXrM49D2JxkXOEP2&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) |
| 用户通知文案 | *   提醒用户 Pricing Plan 即将变更的通知文案 | [《用户通知文案》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=kDnRL6jAJMBEOZnkiwv2E6rw8yMoPYe1&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) |

**Credits 权限控制逻辑：**

*   权限以**点数余额**为准：账户有点数即享有 Credits 级别权限（分析、自定义引擎等）
    
*   点数用完后权限降回 Free 级别
    
*   12 个月有效期是**未使用点数的失效时间**，不是权限有效期
    
*   年付档位（如 $360/yr 对应 240 次）：一次性购买，全部点数当即发放，有效期 12 个月