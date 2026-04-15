# \[20250811\] Compliance 自助试用与订阅

# 背景与目标

通过客户沟通发现，部分客户具有以下特点：

*   调用量小、需求简单：他们需要快速体验产品的核心功能（如风险筛查）并查看结果。
    
*   现有 Demo 形式过于耗费资源。
    

因此，我们计划设计一套**自助化试用 → 订阅 → Onboarding → 正式使用**流程，目标是：

*   **降低试用门槛**：用户无需人工介入或复杂流程，能在 1–3 次交互内完成首次筛查。
    

*   **顺畅交互路径**：从落地页搜索/试用，到注册、试用体验、订阅、支付、欢迎引导，形成顺畅闭环，提升转化率。
    

*   **灵活订阅**：支持多档 Pricing Plan 与单次 Report 购买，满足不同用户需求。
    

# User Flow

1.  ++**Compliance 落地页**++
    

*   ~~查看到引导试用的 CTA，如 \[Start Free Trial\]~~
    
*   显示「Start Free Trial」CTA + **搜索框**（输入地址/交易）。
    

*   搜索或点击 CTA → 若未登录，进入注册/登录页。
    

1.  ++**试用注册/登录页**++
    

*   用户输入工作邮箱和密码进行注册
    
*   注册完成后，跳转至试用界面
    

1.  ++**试用界面**++
    

*   进入试用界面后，直接在搜索框中输入想要尝试的地址或交易哈希（需要将落地页搜索的内容带过来）
    
*   点击搜索后即可进行筛查
    
*   随后跳转到地址/交易详情页展示结果
    

1.  ++**结果展示**++
    

*   在现有的地址/交易详情页查看筛查结果，也可跳转到 Alert 界面查看风险详情。
    

1.  ++**订阅**++
    

*   查看不同的 Pricing Plan，选择其中一个符合需求的进行订阅
    
    *   如果有更多的次数需求，也可点击 Contact Us
        

1.  ++**支付与 Onboarding**++
    

*   用户选择套餐后，再选择使用 Crypto 还是 Card 支付，根据选择跳转至不同的支付页面完成订阅。
    
*   Onboarding 流程：
    
    *   提供 快速入门教程（弹窗展示）。
        
    *   发送欢迎邮件，包含常见问题解答、支持联系方式和高级功能介绍。
        

1.  ++**正式使用**++
    

*   在现有平台使用所有功能模块
    
*   如果有更多的筛查数量/功能需求，可以直接在 Billing 界面 Upgrade。
    

# 详细功能需求

#### 功能范围

| 模块 | 功能需求 |
| --- | --- |
| Compliance 落地页 | *   增加注册引导，点击后可以直接跳转平台注册<br>    <br>*   增加搜索框，引导用户搜索地址/交易，点击结果后会携带搜索结果跳转试用平台 |
| 登录/注册 | *   开放用户自助注册<br>    <br>*   需要严格限制仅工作邮箱可以注册<br>    <br>*   需要区分从不同渠道注册的用户 |
| 试用平台/界面 | *   在现有平台基础上，增加试用界面<br>    <br>*   Lock 试用用户不可用的功能<br>    <br>*   增加 Pricing Plan 展示界面 |
| 正式平台 | *   根据 Pricing Plan ，对订阅用户进行权限控制<br>    <br>*   增加 Billing & Usage 展示界面 |
| 订阅 | *    提供多种订阅 Plan，允许用户选择后订阅<br>    <br>*   同时提供单次 Report 购买的选项，满足小量用户的需求 |

> 以下内容按照页面/模块拆解

## Compliance 落地页

在 Compliance 落地页首页增加 **搜索框** 和引导试用 **CTA 按钮**，引导用户直接试用地址/交易搜索功能。试用仅开放 **ETH** 和 **Tron** 两条链。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/2dbfed3d-1751-40b6-a5e4-3d3e7aa62c0f.png)

### 搜索逻辑

*   **输入识别**
    
    *   地址：校验为合法 ETH / Tron 地址。
        
    *   交易：校验为合法 ETH / Tron 交易哈希。
        
*   **结果展示**（下拉框）
    
    *   地址：展示该地址活跃链信息（仅 ETH、Tron）。
        
    *   交易：展示对应链的交易。
        
    *   若未匹配到结果：展示提示信息：
        
        *   "No matching address or transaction found on supported trial chains (ETH & Tron)."
            
*   **点击结果**
    
    *   跳转至平台试用界面。
        
    *   携带查询参数（即点击的地址/交易）：~~直接跳转到对应地址/交易详情页（~~~~++需要有明显的 Screening 中的样式++~~~~）。~~
        

             考虑到在我们的平台中，输入地址/交易后还有其他的修改 label、customer，和选择要筛查的transfer，因此不好直接跳转结果页，改成把搜索内容带到试用平台的搜索框。

:::
Compliance 落地页的最终方案以 [《Compliance landing page》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=ZgpG2NdyVXXLMx90uqEbQLQKVMwvDqPk&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc) 为准
:::

## 试用注册/登录

*   用户点击官网上的 CTA 按钮进入平台后，若未登录，跳转至注册/登录页面（++支持切换登录/注册++）。 
    

#### 注册流程

参考：[https://airtable.com/signup](https://airtable.com/signup)

*   用户输入邮箱
    
    *   前端简单验证是否为工作邮箱，若验证不通过，直接在搜索框下展示提示文案：“Please use a work email.”。
        
*   点击 【Continue】按钮提交邮箱信息
    
    *   后端二次验证是否为企业邮箱（不知道是否有第三方 API 可使用？）
        
    *   点击后 【Continue】 按钮显示 Loading 状态等待后端返回结果
        
    *   根据后端返回结果展示不同信息/界面
        
        *   验证不通过：返回报错信息并展示
            
        *   为已注册用户：提示切换登录界面
            
        *   验证通过：展示注册下一步界面
            
*   注册界面：
    
    *   用户进一步填写密码 （两次）
        
    *   点击 \[Send Verification Email\] 进入邮箱验证界面
        
*   邮箱验证界面
    
    *   自动发送验证邮件到用户邮箱，附带**验证 Link** 和 **可输入验证码**
        
    *   用户可以点击 Link 自动完成验证，也可在邮箱验证界面输入验证码完成验证。
        
    *   点击 \[Verify\]
        
*   完成界面
    
    *   显示 “邮箱验证成功” + 引导按钮 \[Get Started\]
        
    *   点击后跳转平台‘
        

**验证邮件**

:::
Subject: Verify your email for Phalcon Compliance

Hello,

Thank you for signing up with **Phalcon Compliance**.  
Please verify your email address using the information below:

**Your verification code:** `**482913**`

Or, simply click the link below to verify directly:  
\[Verify Email Address\]

⚠️ Both the verification code and the link are valid for **10 minutes**.

If this request was not initiated, please ignore this email.

Best regards,  
**Phalcon Compliance Team**
:::

#### 登录流程

沿用原登录界面和流程

### 用户权限  

| **用户类型** | **来源** | **权限** | **试用入口行为** |
| --- | --- | --- | --- |
| 正式用户 | 后台开通 | 全部功能 | 点击试用直接进入平台 |
|  | 自助订阅 | 全部功能 | 点击试用直接进入平台 |
| 试用用户 | 自助注册 | 核心功能（3 次地址/交易筛查，默认规则） | 进入试用平台 |
|  | 后台开通 | 全部功能 | 点击试用直接进入平台 |
| 已过期用户 |  | 退回到试用界面，可以订阅 | 显示订阅引导页面 |

以下场景：

*   用户完成注册，第一次进入平台时
    
*   Security 用户第一次进入 Compliance 平台
    

弹窗展示用户引导和试用限制等内容。

:::
**Welcome to Phalcon Compliance**

We’re excited to have you on board!  
You’re now exploring in **Trial Mode**, where you can:

🔍 **Screen up to 3 addresses or transactions** (ETH & Tron supported)

📊 View **risk level and alerts** in real time

🚀 Get a first look at our core modules: **Addresses, Transactions, Alerts**

Some advanced features (like risk engines, auto re-screening, or reporting) are available on paid plans. Upgrade anytime when you’re ready.

                                                                                                                              \[Start First Screening\]            \[View Pricing Plan\]
:::

## 试用界面

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4j6OJ5jKN7RWbq3p/img/1f9e2625-7098-48af-8ceb-f0cbcc0c21bd.png)

*   在原平台模块的基础上，**增加 Quick Trial Hub 模块**展示试用界面。
    
    *   中心展示搜索框。
        
    *   搜索框下方提供 2-3 个示例地址/交易哈希，带++复制按钮++，降低试用门槛。  
        
    *   顶部显示 “Trial Mode”，并提示剩余试用次数 “Free Trial Usage：X/3”。  （全局展示）
        
    *   展示 “Upgrade” 按钮，点击跳转至 Pricing Plan 页面。（全局展示）
        
*   权限限制：  
    
    *   试用用户仅可访问 Addresses、Transactions、Alerts 模块，其他模块显示 **Lock 图标**，悬停提示 “Upgrade to unlock the full features”。  
        
    *   通过 URL 跳转到无权限模块时，界面显示 Lock 样式，提示 “Upgrade to access this feature”。
        
    *   仅分配 1 个 seat
        
*   搜索框逻辑
    
    *   显示搜索历史，便于重复操作。 
        
    *   自动识别输入字符串为地址或交易： （++同样只支持 eth 和 tron 链++）
        
        *   地址：下拉框列出所有活跃链地址，点击选中后触发筛查。  
            
        *   交易：下拉框识别交易所在链，点击后弹窗列出所有 transfer，用户选择 transfer 和方向后筛查（与现有导入交易流程一致）。(eth\tron 链)
            

## 结果展示 

地址/交易详情页有较大的改动，具体见： [《地址/交易结果展示优化》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=EpGBa2Lm8aRMaA25T0zwB05vWgN7R35y&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

*   用户点击筛查后，跳转至地址/交易详情页，展示风险筛查结果（风险评分、详细信息）。 
    

*   支持跳转至 Alert 界面查看详细风险警告。  
    

**试用限制**

用户 hover / 点击禁用功能时同样需要提示不可使用

*   地址模块：禁用 Add to Black/White List、Auto Re-screening（默认 disabled 且不可更改）。  
    
*   交易模块：禁用 STR Report Export。  
    

## Pricing Plan 及订阅

### 订阅/付费引导

1.  在 Quick Trial Hub 和结果页面顶部展示 “Upgrade” 按钮，点击跳转至 Pricing Plan 页面。  
    
2.  在用户的试用次数用完后，再次尝试使用 Screen 功能时，弹窗提示用户可以订阅或购买单次 Screen 以继续使用。
    

:::
**You’ve reached the end of your free trial.**

Upgrade your plan for more access.

Or purchase One-Time Plans for a few extra checks.

                                                                                                                                      \[Upgrade Plan\] \[Purchase Reports\]
:::

*   点击 【Upgrade Plan】-> 跳转 Pricing Plan 页面，展示可订阅的 Plan
    
*   点击 【Purchase Reports】-> 跳转 Pricing Plan 页面，滚动到单次购买 Report 的区域
    

### Pricing Plan 界面

> 此界面导航栏层级在 Quick Trial Hub 下面

*   列出 不同的 Pricing Plan，同时下方展示 Enterprise Plan，引导有更多次数/功能需求的用户和我们联系。
    
    *   点击 Talk to an Expert 后跳转到 Book Demo 的预约表单。
        
*   同样要将单次购买的选项放到这个界面。（++**用户已有订阅 Plan 时不再展示此选项**++）
    

~~具体的 Pricing Plan 细节待确认~~ 

最终确定的 Pricing Plan 见：                                                                     

[《Pricing Model》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=93NwLYZXWyqAB0poHYj1wOXZWkyEqBQm&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

#### Pricing Plan 界面原型

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/444918fd-7da1-481b-a2ad-07c67093c616.png)

功能对比表格：

| Feature | Starter | Growth | Pro | Enterprise |
| --- | --- | --- | --- | --- |
| Screens / month | 150 | 320 | 750 | Custom |
| Default Risk Engine | ✅ | ✅ | ✅ | ✅ |
| Custom Risk Engine | – | – | 10 | Unlimited |
| Export KYA/KYT Reports | ✅ | ✅ | ✅ | ✅ |
| Export STR Reports | – | ✅ | ✅ | ✅ |
| Auto Re-screening | – | – | ✅ | ✅ |
| Notification Channels | Email | Email, Slack, Telegram, Lark, PagerDuty, Discord | + Webhook | All 7 Notification Channels |
| API Integration | – | – | ✅ | ✅ |
| Dedicated Support | – | – | – | 24/7 |

*   点击提供的 Starter、Growth、Pro Plan 的 【Subscribe】按钮 -> 进入 checkout 页面，具体见下方 _**Plan订阅流程**_ 部分。
    
*   点击 Enterprise Plan 的 【Talk to an Expert】新 tab 打开官网 Talk to an Expert 的表单填写页面
    
*   点击下方的单次 Report 购买的 【Buy】按钮后同样进入 Checkout 页面，可以选择 Card 或 Crypto 支付，付款后为用户充值对应的点数。（单次 Report 购买后的平台使用相关内容见 [《\[20250811\] Compliance 自助试用与订阅》](https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JnARwkK1TZzam7LAV2LD0oRE?utm_scene=team_space&iframeQuery=anchorId%3Duu_mfg8r726bkqaosbvg8i)）
    

#### Plan  订阅流程

用户点击选择对应的 Plan，点击 _**\[Subscribe\]**_ 后进入 Checkout 页面。（考虑到要兼容 Upgrade Plan 的展示等，需要增加 Checkout 页面）

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/7ae7ef9a-3912-4228-8aca-bd235642d620.png)

根据用户在 Pricing 页面选择的 Plan 展示对应的 Plan 订阅结算页：

*   Billing Cycle 默认选中用户在 Pricing Plan 中点击的 Billing Cycle
    
*   用户在此界面还可以切换 Billing Cycle，切换后 Summary 部分的金额和文案 （Billed Monthly / Annually）相应改变。
    
*   用户可以自行选择 Credit Card / Crypto 付款，点击付款直接跳转对应 Stripe / Coinbase Commerce 进行付款
    
*   支付成功后：
    
    *   System -> Usage & Billing
        
    *    ++自动弹窗，同时发送欢迎邮件++。
        

> 所有文案见 [《文案汇总》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=mExel2BLV5BNvQedivLMKO1nJgk9rpMq&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

**创建 Plan 订阅特殊情况 — 购买的 Report 次数没用完**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/b2abbac5-0ae0-4ed8-a645-a027429c5fa6.png)

订阅价格要减去未使用完的 Report 折算价格： 折算价格 = 未用完次数 / 总次数 \* 总价格

### Plan  升级处理

*   费用计算：按周期剩余天数比例折算差价
    
*   支付限制：需沿用原付款方式（禁用其他方式，Hover提示原因）
    
*   周期限制：年付Plan仅允许升级年付（禁用月付，Hover提示原因）
    

#### Report 购买

*   购买筛查点数（可叠加，保持试用状态）
    
*   支付成功跳转Tria Hub
    

## 正式使用

订阅用户界面与正式用户一致，不过因为订阅模式，需要有一定的使用限制、billing 展示的不同，具体见下面：

### 使用限制和提示

自助订阅用户需要在筛查次数、功能使用等方面按照 Pricing Plan 的规定进行严格的限制。

*   **筛查次数限制**：不区分地址/交易、first/re-screen，严格按照当月可使用数量限制。
    
    *   当用户达到 Screen 次数上限后，禁用搜索框搜索、导入地址/交易按钮，用户点击时弹窗提示：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/094f9eb0-0840-4c07-b136-a2e037c582ed.png)
        
        *   点击 Upgrade 后跳转 Pricing 界面
            
*   **功能使用限制**：当用户尝试点击使用当前 Plan 不支持的功能时，弹窗提示：
    
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/c7c5f7d9-8efc-410f-b0b7-9a040123adc3.png)
        
    *   点击 Upgrade 后跳转 Pricing 界面
        

### Usage / Billing 页面

根据当前的 pricing 方案，自助订阅的用户有每个月的 Screen 用量限制，以及功能使用限制，需要在 Usage 界面有所体现。同时需要展示订阅的 Plan、Billing 等相关信息，综合为 Usage & Billing 页面。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/0dabf702-7451-4b5a-a5e5-fadc56786ea0.png)

#### 字段说明

| 模块 | 字段 | 说明 |
| --- | --- | --- |
| Current Plan | 当前订阅的 Plan 名称 | 后台开通的用户，这里展示 Enterprise Plan。 |
|  | Upgrade 按钮 | 当用户未取消当前订阅时，展示此按钮。用户点击后跳转 Pricing 界面。 |
|  | Cancel Subscription 按钮 | 当用户使用 Card 订阅，且未取消订阅时，展示此按钮。用户点击后需要弹窗二次确认。<br>:::<br>**Cancel Subscription**<br>Are you sure you want to cancel your subscription?<br>You will lose access to all premium features at the end of your current billing cycle.<br>                                          \[**Keep My Subscription**\] \[Confirm Cancel\]<br>:::<br>用户点击 Confirm Cancel 确认后，直接取消其订阅。 |
| Biling | Next Billing Date | 以下 3 种情况分别展示不同的信息：<br>*   Card 订阅，未取消： Next Billing Date：{下一次收费日}<br>    <br>*   Card 订阅，已取消：No further billing<br>    <br>*   Crypto 购买：No further billing |
|  | Manage Billing 按钮 | 点击后跳转 Stripe 用户 Billing 管理界面，可以：更改账单信息、支付卡信息、下载 invoice 等。 |
| Service Date | \- | 展示当前订阅周期的起止日期 |
| Usage | Screening Count | 根据用户订阅的 Plan 展示当前周期的 Screen 用量和总量 |
|  | Auto Re-screening | 展示当前 Plan 是否可以用这个功能： Yes / No |
|  | Customize Risk Engines | 展示当前 Plan 是否允许自定义 Risk engine：Yes / No |
|  | Export Report | 展示当前 Plan 是否可以用这个功能：Yes / No |
|  | API Integration | 展示当前 Plan 是否可以用这个功能：Yes / No |
| Billing History | Date | Billing 日期，展示格式：“yyyy-mm-dd”。 |
|  | Description | 展示格式：Plan 名称 + 付费周期，如：Starter Plan Monthly |
|  | Billing Amount | 展示付费金额 |
|  | Payment Method | 付费方式 |
|  | Invoice | 点击下载 Invoice |

### Dashboard 增加搜索框

考虑到 “导入地址” 对于一般用户来说没有 “搜索框” 使用起来更直观易懂。因此在 Dashboard 页面顶部保留输入框，及搜索后即进行导入、筛查。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/4093aaf7-699e-4b82-b074-4879862f8c16.png)

## 购买单次 Report 后使用

除了一般的按月订阅的选项外，还提供了单次 Report 购买的选项，用户可以在试用结束后选择购买 1/3/5 次 Report。

提供的能力包括：

*   筛查地址
    
*   导出 Report
    
*   查看 Alert
    

同样保留试用平台界面提供此能力，根据充值次数提供给用户额外的使用点数。

文案调整：

*   顶部的 Free Trial Usage -> Usage
    

#### 引导

在购买完 Report 后，筛查完成第一次进入地址/交易详情页时，高亮 \[KYA Report\] / \[KYT Report\] 按钮。

高亮形式：可以浮动 Pop 几下 按钮？

## 用户权限补充—后台开通用户&过期用户 （新增）

++**对所有用户均展示 Pricing Plan 界面**++

#### 后台开通正式用户

Current Plan 为 **Enterprise Plan**

Usage & Billing 展示内容和字段如下：

*   不展示 Upgrade、Manage Billing 按钮
    
*   Next Billing Date 显示为 Service 到期日
    
*   Next Billing Amount 显示 Contact Us
    
*   不展示 Billing History 模块
    
*   Usage 中：
    
    *   增加 Seats 和 Support
        
    *   Screening Count 可以展开
        

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/8b38539a-cba8-4539-9f4a-f39c0c81b870.png)

#### 后台开通试用

Current Plan 为 **Enterprise Plan**

其余展示样式和正式用户一样

#### 过期用户权限

1.  自助订阅后过期
    
    退回到试用状态，即有 Quick Trial Hub，不可用模块锁住
    
2.  后台开通试用后过期
    
    自动删除账号和数据，如需使用则再次注册
    
3.  后台开通正式使用后过期
    

暂不会出现此情况，待处理  $\color{#0089FF}{@程静}$ 

# 待优化

**TODO**：

*   正式使用界面的 Dashboard 顶部也加一个搜索框
    
    *   搜索交易的交互
        
*   到期提示
    
*   点数用完提示
    
*   后续升级 Plan 的需求？
    
*   Wallet Screening API 用户转化？
    
*   订阅过期用户的页面展示：
    
    *   退回到试用状态
        

**扩展思考**：

*   从小型机构用户的使用需求和流程来看，产品需要优化的点：
    
    *   地址/交易的详情页如何优化可以让“风险”信息的展示更加直观易懂？或者新增一个 report / 扫描结果的页面
        

# Archived

#### 过期用户权限

以下受限制的操作，点击后统一弹窗提示：

:::
Your subscription has expired. Renew now to unlock this feature.

\[Cancel\] \[Renew\]
:::

| 模块 | 操作限制 |  |
| --- | --- | --- |
| Dashboard | 允许：<br>*   浏览<br>    <br>限制：<br>Start Importing <br>*   Import Address<br>    <br>*   Import Transaction | 不允许，点击下拉框中的 Import Addresses / Import Transactions 后弹窗提示限制 |
| Alert Hub | 允许：<br>*   浏览<br>    <br>限制：<br>*   Assign to<br>    <br>*   Export Alert Report<br>    <br>*   Mark as Resolved<br>    <br>*   Save as CSV<br>    <br>*   Comment | 不允许，点击对应按钮后弹窗提示限制 |
| Addresses | 允许：<br>*   浏览<br>    <br>*   删除<br>    <br>*   导出 Address Report<br>    <br>    限制：<br>    <br>*   Import Address<br>    <br>*   修改 Label<br>    <br>*   修改 Tag<br>    <br>*   绑定到 Customer<br>    <br>*   Re-screen<br>    <br>*   Add to blacklist / whitelist<br>    <br>*   Comment | 不允许，点击对应按钮后弹窗提示限制 |
| Transactions | 允许：<br>*   浏览<br>    <br>*   删除<br>    <br>*   导出 Transaction Report<br>    <br>限制：<br>*   Import Transaction<br>    <br>*   Re-screen<br>    <br>*   STR Report<br>    <br>*   修改 Label<br>    <br>*   绑定到 Customer<br>    <br>*   Comment | 不允许，点击对应按钮后弹窗提示限制 |
| Customers | 允许：<br>*   浏览 <br>    <br>*   删除<br>    <br>*   导出 Report<br>    <br>    限制：<br>    <br>*   Create Customer<br>    <br>*   修改 Name<br>    <br>*   修改 Description<br>    <br>*   Add Address<br>    <br>*   Add Transaction<br>    <br>*   Comment | 不允许，点击对应按钮后弹窗提示限制 |
| Risk Engines | 允许：<br>*   浏览<br>    <br>*   导出 Report<br>    <br>    限制：<br>    <br>*   删除<br>    <br>*   Risk Engine 模板弹窗点击 \[Create\]<br>    <br>*   修改名称<br>    <br>*   修改 description<br>    <br>*   修改 trigger condition<br>    <br>*   Clone<br>    <br>*   Add Notification Channel |  |
| Notification Channels | 允许：<br>*   浏览<br>    <br>*   删除<br>    <br>    限制：<br>    <br>*   Create Channel<br>    <br>*   Map to risk engine |  |
| System - Usage | \- |  |
| System -Logs | \- |  |
| System - Screening Settings | 允许：<br>*   浏览<br>    <br>*   修改 Re-screening 周期<br>    <br>限制：<br>*   Add Address to Blacklist<br>    <br>*   Unblacklist |  |
| System - API | 允许：<br>*   浏览<br>    <br>限制：<br>*   Create API Key |  |
| Organization Settings | 允许：<br>*   浏览<br>    <br>*   删除<br>    <br>*   修改 Role<br>    <br>    限制：<br>    <br>*   Invite Member |  |
| Account Settings | \- |  |

#### Top Up 弹窗 

用于当前服务期内点数充值，单价与当前购买的 Plan 保持一致。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35oDXWN7Rl7E/img/df0bb438-3baa-4be7-9219-184e411ba9f4.png)

**Top-Up 规则**

*   价格：按当前 Plan 的**单价**计算（例如 Growth ≈ $0.95/screen）。
    
*   数量：步进 100；最小 100；与订阅周期**同到期**。
    
*   计费：进入支付方式选择 → 支付成功后即刻增加额度