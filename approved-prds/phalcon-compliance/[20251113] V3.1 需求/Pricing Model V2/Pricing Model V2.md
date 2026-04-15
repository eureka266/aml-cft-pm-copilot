# Pricing Model V2

第一版：[《Pricing Model》](https://alidocs.dingtalk.com/i/nodes/93NwLYZXWyqAB0poHYj1wOXZWkyEqBQm)

参考：[《产品定价调研-Token计费模式》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdi5vKrKv9V1DK0g6l?utm_scene=person_space)

# 背景与目标

为满足不同类型用户（个人分析者、小型安全公司、合规团队与持牌企业）的使用需求，Phalcon Compliance 计划重构定价体系，使产品能同时兼顾以下目标：

*   **降低初次付费门槛**，降低个人用户心理负担
    
*   **兼容现有 Pro 用户**，Pro 价格不变且功能不升级
    
*   通过功能限制与配额设计**引导付费升级**
    
*   增加**点数充值**、**alipay 等支付方式**等措施，进一步促进用户付费
    

目标是构建一个兼具灵活性与扩展性的 Pricing Model，覆盖从个人用户到企业客户的全生命周期。

# 对外定价方案

## 订阅 Plans

[请至钉钉文档查看附件《Pricing Plans》](https://alidocs.dingtalk.com/i/nodes/r1R7q3QmWe3XRKmoIBzDmyYrJxkXOEP2?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mhxcazjiogk115q1a0q)

*   Labels 和 Tags 限制：如果我们希望用户在我们这里存储数据，并通过这种形式增加用户黏性，是否真的有必要
    
*   Lite Scan 面向所有用户提供，详细见 [《Lite Scan & 分享页》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=Qnp9zOoBVBBbarMdi5nK69L1V1DK0g6l&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)
    

## 点数包

点数包作为订阅配额用尽后的溢价补充，旨在引导高频用户升级订阅。**点数包额度一年内有效**，价格设定始终高于下一个订阅方案的单价。

| 点数包容量 | 建议价格 | 单价 | 购买用户类型 | 逻辑 |
| --- | --- | --- | --- | --- |
| 50 次 | **$95** | **$1.90 / 次** | 所有付费层 | 远高于 Basic 年付成本 ($1.00/次)，旨在强烈引导用户升级。 |
| 200 次 | **$300** | **$1.50 / 次** | 所有付费层 | 仍高于 Growth 年付成本 ($0.83/次)。 |
| 500 次 | **$600** | **$1.20 / 次** | 所有付费层 | 仍高于 Pro 年付成本 ($0.78/次)，满足超大额临时需求。 |

*   除 Visitor ~~和~~ ~~Enterprise~~ 用户外的所有用户都可以购买点数包，有限期一年。
    
*   当用户账户中有订阅 Plan 时，优先消耗 Plan 中包含的点数。
    

# 用户类型及内部权限控制说明

## 用户分类及说明

| 用户类型 | 说明 |
| --- | --- |
| **Visitor** | 首次访问平台的未注册用户。可体验 **Lite Scan** 功能，并通过“解锁详细风险信息”等引导转化为 Free 用户。 |
| **Free** | 面向个人用户或首次接触平台的用户，可获得有限次数使用核心功能（如详细风险信息）以评估产品价值；可额外购买点数包满足轻量需求。 |
| **Starter** | 适用于独立分析人员、小型 U 商等需要更多筛查次数、Alert、Analytics 以及基础通知功能的用户。 |
| **Growth** | 面向中型 OTC 公司、安全或分析团队。相比 Starter，新增更完善的合规相关能力（STR/SAR Report、Blacklist 等）。 |
| **Pro** | 针对中小型团队的完整解决方案，提供全面功能与更高配额。相较 Growth，主要新增工作流功能（API 集成、Webhook 等）。 |
| **Enterprise** | 面向中大型企业，提供最高配额、更低单价、完整全部功能及专业服务支持，满足规模化合规与风险管理需求。 |

## 权限说明

| **功能模块/界面** |  | **Visitor** | **Free** | **Starter** | **Growth** | **Pro** | **Enterprise** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Home 界面** |  | ✅ |  |  |  |  |  |
|  | 不同 Plan 间展示内容差异化 |  |  |  |  |  |
| **Addresses / Transactions** | 列表页 | [打叉] | ✅ |  |  |  |  |
|  | 详情页 | **Lite Scan** | 点数用完后展示 Lite Scan 模式 |  |  |  |  |
|  | 分享页 | ✅ |  |  |  |  |  |
| **Alert Hub** | 列表/详情页 | [打叉] | ✅ |  |  |  |  |
|  | Assign 协作 | [打叉] |  |  |  |  | ✅ |
| **Customers** |  | [打叉] |  | 数量限制 |  |  | ✅ |
| **Analytics** |  | [打叉] |  | ✅ |  |  |  |
| **Risk Engines** | Default Risk Engines | [打叉] | ✅ （不可编辑） | ✅ |  |  |  |
|  | Custom Risk Engines | [打叉] |  | 数量限制 |  |  | ✅ |
| **Notification Channels** |  | [打叉] |  | 类型限制 |  |  | ✅ |
| **System** | Real-time Monitoring (Auto Re-screening) | [打叉] |  |  | ~~数量限制~~<br>Pro 开始可以使用 |  |  |
|  | 黑名单 / 白名单 | [打叉] |  |  | 数量限制 |  | ✅ |
|  | API | [打叉] |  |  |  | ✅ |  |
|  | Logs | [打叉] |  | ✅ |  |  |  |
| **Billing & Usage** | Pricing Plan | ✅ |  |  |  |  |  |
|  | Billing | [打叉] | ✅ |  |  |  |  |
|  | Usage | [打叉] | ✅ |  |  |  |  |
|  | Data Management | [打叉] | ✅ |  |  |  |  |
| **Audit Logs** | 查看 | [打叉] | ✅ |  |  |  |  |
|  | Comment | [打叉] |  |  |  |  | ✅ |

以下权限控制分为三类：

*   [打叉]（全锁）：不可使用/访问
    
*   **半锁**：按数量或类型限制
    
*   ✅：可使用
    

### 权限控制页面展示

#### 无权限页面

对于 当前 Plan 不包含的功能模块，用户依然可以点击进入该页面，但实际内容会替换为“模块介绍 + 升级引导”样式，以帮助用户理解模块价值并引导升级。

**示例**：

（Notification Channels 模块）

:::
### Enable Real-Time Compliance Alerts

Notification Channels help your team react faster to high-risk events and updates.

Immediate alerts for risk changes and flagged addresses

Faster decision-making in AML/KYT workflows

Streamlined routing to your team’s channels

This feature is not included in your current plan.  
**Upgrade to Starter →**
:::

*   右侧展示此模块界面截图
    

#### 有权限且有限制

对于用户具有功能访问权限，但数量/类型等受到订阅 Plan 限制的模块，在用户进入页面后仍展示全部功能，但需提供可视化的额度提示与升级引导。

*   **可正常操作该模块**（添加、编辑、删除等）
    

*   当用户已使用接近或达到额度上限时，显示以下状态：
    

**数量限制示例**：

（Customers 模块，接近额度上限）

:::
**You’re Nearing Your Customer Limit** (8/10 Used).

Upgrade your plan to instantly **expand your capacity to 30 customers** and support your growing business.

**\[Upgrade to Pro →\]**
:::

所有文案汇总见：

[《权限控制页面展示》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTa03pyzXVA7depqY?utm_scene=team_space)（待完善）

# Pricing Plans 页面

## 展示内容

#### Subscription Plans      

\[**Monthly**\] /  \[Annually\] （Save 17%）

**Free**

**Always free**

3 Risk Screens / month

*   Unlimited Lite Scan _(Limited-time Offer)_
    

*   Default Risk Engines
    

**Starter**

**$1.18** per screen

**$59 / month** for 50 Risk Screens

**\[Subscribe\]**

Everything in Free, plus:

*   Custom Risk Engines
    

*   Analytics & Alert Hub
    

*   Notification Channel: Email
    

**Growth**

**$1** per screen

**$249 / month** for 250 Risk Scrceens

**\[Subscribe\]**

Everything in Starter, plus:

*   STR / SAR Report Export
    

*   Blacklist / Whitelist Management
    

*   Notification Channels: Telegram, Slack
    

**Pro**

**$0.93** per screen

**$699 / month** for 750 Risk Screens

**\[Subscribe\]**

Everything in Growth, plus:

*   Ongoing Monitoring
    

*   API Integration
    

*   Notification Channels: Webhook & All Supported Channels
    

**Enterprise Plan**

For organizations with high-volume usage and custom needs.

*   Higher screen volumes at discounted rates
    
*   Multi-seat collaboration options
    
*   24/7 dedicated support
    
*   Tailored compliance solutions
    

**Compare All Features** 

|  | Free | Starter | Growth | Pro | Enterprise |
| --- | --- | --- | --- | --- | --- |
| Supported Blockchains | ETH & Tron | All Supported Chains |  |  |  |
| **Core Screening Features** |  |  |  |  |  |
| Risk Screen | 3 / Month | 50 / Month<br>(600 / yr annually) | 250 / Month<br>(3000 / yr annually) | 750 / Month<br>(9000 / yr annually) | Custom |
| Lite Scan | ✅ | ✅ | ✅ | ✅ | ✅ |
| Default Risk Engine | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Advanced Analysis** |  |  |  |  |  |
| Alerts | ✅ | ✅ | ✅ | ✅ | ✅ |
| Analytics | \- | ✅ | ✅ | ✅ | ✅ |
| Customers | \- | 1 | 10 | 30 | Unlimited |
| Labels | 3 | 50 | 200 | 1000 | Unlimited |
| Tags | 3 | 50 | 200 | 1000 | Unlimited |
| **Compliance Features** |  |  |  |  |  |
| Custom Risk Engines | \- | 3 | 10 | 20 | Unlimited |
| STR / SAR Report | \- | \- | ✅ | ✅ | ✅ |
| Real-time Monitoring | \- | \- | \- | ✅ | ✅ |
| Blacklist/Whitelist | \- | \- | 50 | 200 | Unlimited |
| **Team Collaboration & API** |  |  |  |  |  |
| Notification Channels | \- | Email | Eamil, Telegram, Lark | ALL | ALL |
| Team Collaboration | \- | \- | \- | \- | ✅ |
| API Intergration | \- | \- | \- | ✅ | ✅ |
| **Support & Trainning** |  |  |  |  |  |
| Support | Email | Email | Email | Email | Dedicated 24/7 |
| Trainning | \- | \- | \- | On Demand | ✅ |

#### Credit Package

All purchased credits are valid for 12 months from the date of purchase. 

**50 Credit** 

**$1.9** per screen

$95 total

**\[Buy\]**

**200 Credit**

**$1.5** per screen

$300 total

**\[Buy\]**

**500 Credit**

**$1.2** per screen

$600 total

**\[Buy\]**

_Note: You can purchase Credit Packages at any time for additional consumption when your Plan credits are exhausted; they serve as a backup supplement to your Plan credits._

## 设计&交互需求

*   价格展示：
    
    *   突出单价：每个 Plan 的 Screen 单价 显示在卡片上。
        
    *   切换至年度计费：切换到 Annually 后，展示年度总价和每年可用的 Risk Screens。
        

**Free**

**Always free**

3 Risk Screens / month

**Starter**

~~**$1.18**~~  **$1** per screen

**$599 / year** for 600 Risk Screens

**Growth**

~~**$1**~~  **$0.83** per screen

**$2,499 / year** for 3,000 Risk Screens

**Pro**

~~**$0.93**~~  **$0.78** per screen

**$6,999 / year** for 9,000 Risk Screens

*   用户已有 Plan 时的交互：
    
    *   自动切换周期：根据用户当前订阅周期（Monthly 或 Annually）自动切换显示。
        
    *   订阅按钮状态：
        
        *   低于当前 Plan（包含同 Plan 的短周期）：订阅按钮禁用。
            
        *   高于当前 Plan（包含同 Plan 的长周期）：订阅按钮显示为 Upgrade。
            

# 结算流程

用户点击 Pricing Plan 中订阅 Plan 的 Subscribe / Upgrade 按钮，或者 Credit Package 的 Buy 按钮后进入结算流程。

## 新增 Alipay / Wechat 付款

| **支付方式** | **图标** | **支持的计费模式** |
| --- | --- | --- |
| **Credit Card** | 保持现有 | 订阅, 一次性 (仅点数包购买) |
| **Crypto** | 保持现有 | 一次性（订阅 Plan + 点数包购买） |
| **E-Wallet （新增）** | 展示 Alipay + Wechat Pay 图标 | 一次性（订阅 Plan + 点数包购买） |

在结算页，必须根据用户选择的 **Payment Method** 动态更新提示文案，以避免用户误解是订阅还是单次购买。

*   Payment Method 选择 Credit Card 时：
    
    *   Summary 部分：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ld7bRxXvyWOBQ/img/27c53ce9-40f1-440c-9f42-76d316f9d8e5.png)
        
    *   文案： 
        
        *   Billied Monthly (或 Annually)  
            Next Renewal Date: {当前日期 + 订阅周期}
            
*   Payment Method 选择 Crypto / E-Wallet 时：
    
    *   Summary 部分展示：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ld7bRxXvyWOBQ/img/4c1ac499-deeb-4011-bbb1-26ab50a5f149.png)
        
    *   文案：
        
        *   Billed Once  
            Plan Expiration Date:  {当前日期 + 订阅周期}
            

#### E-Wallet 支付

用户点击 Pay with E-wallet 后跳转 Stripe 的付款页面，用户可以在付款页面中选择 Alipay 或 Wechat Pay，扫描提供的二维码后完成付款。

## 新增 Promotion Code

考虑到 **Referral 系统** 的引入以及可能增加的其他促销活动，结算页将支持用户输入 **促销码**，以满足被邀请用户订阅优惠折扣的需求。详细见：[《Referral邀请激励》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=R1zknDm0WRDEKRYZTng3avyNJBQEx5rG&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

#### 交互 

1.  **入口：** 在 **Total** 金额的上方，显示一个链接或按钮：**"Apply Promo Code"**。
    
2.  **展开：** 用户点击该链接后，展开一个输入框和一个 **\[Apply\]** 按钮。
    
3.  **验证：** 用户输入促销码并点击 **\[Apply\]**。
    
4.  **反馈：**
    
    *   **无效码：** 输入框下方显示红色提示：`Invalid Code.`
        
    *   **有效码：** 输入框收起（或锁定），折扣信息展示在 Code 下方。
        

> 可参考 MS 的设计图：[https://www.figma.com/design/upqwThgyFgRmSWr8aNjQr6/MetaSleuth?node-id=8316-5089&t=Iwq84ifn9lUi3yr7-4](https://www.figma.com/design/upqwThgyFgRmSWr8aNjQr6/MetaSleuth?node-id=8316-5089&t=Iwq84ifn9lUi3yr7-4)

### 促销码类型和展示

#### 订阅流程

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ld7bRxXvyWOBQ/img/d13dccb0-3dfc-41eb-b714-7afafd2c3de2.png)

当促销码有效时，如上图将输入框收起并在 Code 下方展示优惠信息，按照类型分别展示不同的文案，如下：

| **优惠类型** | **描述** | **展示文案** | **影响** |
| --- | --- | --- | --- |
| **单次优惠** | `one-time`。仅在**本次交易**时生效。 | `[X%] off one-time` 或 `[$Y] off one-time` | 仅影响本次交易的总金额。 |
| **多月优惠** | `multi-month`。在**前 N 个计费周期**内生效。 | `[X%] off for [N] month(s)` 或 `[$Y] off for [N] month(s)` | 影响 Total 金额，并应用于前 N 个月。 |
| **永久优惠** | `forever`。在**所有后续计费周期**内永久生效。 | `[X%] off forever` 或 `[$Y] off forever` | 影响 Total 金额，并应用于所有续费。 |

#### 升级流程（待完善）

## 新增余额抵扣

同样考虑到 **Referral 系统** 会给邀请人提供返利，用户账户中的返利余额需要在支付时支持抵扣。具体逻辑见：[《Referral邀请激励》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=R1zknDm0WRDEKRYZTng3avyNJBQEx5rG&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

*   勾选 `Apply Balance $50 (Expires May 20, 2026）` 
    

*   `总计 (Total)` 会在扣除促销折扣后，再减去余额抵扣金额。
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/Mp7ld7bRxXvyWOBQ/img/0930611a-6ffa-4e09-b9d7-bb4a2da7f1fa.png)