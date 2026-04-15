# \[20251210\] 情报网络（Phalcon Network）

# 背景与目标

## 背景

背景：[《\[20251112\] Phalcon Compliance情报网络》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=EpGBa2Lm8aRMaA25TvvQnN4nWgN7R35y&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

调研：[《情报网络调研》](https://alidocs.dingtalk.com/i/nodes/Y1OQX0akWmq7PNyoHA4j9PYwWGlDd3mE?utm_scene=person_space)

12.09 需求第一次讨论：[《情报网络需求（Lumen Network）》](https://docs.dingtalk.com/i/nodes/YndMj49yWjwaygboT2aPXOawV3pmz5aA?iframeQuery=utm_source%3Dportal%26utm_medium%3Dportal_recent)

BlockSec 计划构建情报网络 Phalcon Network，向项目方提供“非法/高风险资金流入实时告警”能力。该网络的价值在于：

*   将和项目方相关高风险链上资金流及时通知到项目方
    
*   通过 Public Good 形式扩大影响力，并为后续引入权威 Reporter（执法/监管等）打基础
    

本次 PRD 覆盖 场景一，仅包含最核心的「项目方加入网络 → 绑定地址 → 接收 告警」环节。

## 动机

*   对外
    
    *   以 Public Good 为原则，向行业提供基础、可信的链上风险告警能力
        
    *   降低项目方识别高风险入金的使用门槛与响应成本
        
*   对内
    
    *   提升 BlockSec / Phalcon Compliance 在行业中的认知度与专业影响力
        
    *   构建稳定的转化入口
        
        *   通过 Alert 引导用户进入 MS 和 Compliance 
            
        *   引导用户从事后了解转到事前阻断和合规措施，形成付费意愿
            

## 需求目标

在 Phase 1 中，情报网络将以 Public Good 为设计原则：

*   免费开放风险等级高的风险标签（和 Phalcon Compliance 中风险等级较高的 Risk Indicator 保持一致），具体如下：
    
    *   Sanctioned
        
    *   Terrorist Financing
        
    *   Human Trafficking
        
    *   Drug Trafficking
        
    *   Attack
        
    *   Scam
        
    *   Ransomware
        
    *   Child Abuse Material
        
    *   Laundering 
        
    *   Mixing
        
    *   Dark Market
        
    *   Darkweb Business
        
    *   Blocked 
        
    
    由于当前私有化标签均以地址为维度设置，因此风险引擎在完成所有路径扫描后，需要额外增加一个过滤步骤：将那些携带私有化标签的地址排除。
    
*   限制用户监控的地址数量
    
    *   限制多少个地址：3个
        
*   支持的链
    
    *   和 Phalcon Compliance 支持的链保持一致，且对所有用户都开放
        

在保持 Phase 1 公共属性与中立性的前提下，希望在后续阶段逐步引入：

*   执法机构
    
*   监管机构
    
*   其他权威组织
    

作为风险信息的 Reporter，共同构建一个多方情报网络。

因此，Phase 1 在产品设计上需要：

*   考虑到后续会有多种情报来源，在设计上留出兼容空间
    
*   保持平台的中立性，不能有明显的付费转化目的
    

为 Reporter 的加入留下空间且不会引起顾虑。

## 需求范围

*   Landing Page（介绍 + 申请入口）
    
*   申请 / 人工审核 / 受邀注册
    
*   用户界面：
    
    *   绑定监控地址
        
    *   绑定通知渠道
        
    *   语言 / 时区设置
        
    *   Alerts 统计与历史查看
        
*   多渠道消息推送
    
    *   警报消息内容
        
    *   Compliance / MetaSleuth 跳转（带 refer）
        

# 详细方案

**整体 User Flow：**

Landing Page → 申请加入 → 填写企业信息 → 提交申请 → 审核 →

审核通过邮件 → 注册账号 → 登录 → 

配置待监控的地址→绑定通知渠道  → 开始接收风险提醒

## 用户申请及注册

参考：[https://www.trmlabs.com/beacon-network](https://www.trmlabs.com/beacon-network)

### 落地页表单申请

用于筛选合格项目方并启动人工审核。

| **字段** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| **Company Information** |  |  |  |
| Organization Name | text | ✓ | 项目方名称 |
| Business Type | dropdown | ✓ | *   Crypto Business <br>    <br>    *   ~~Exchange (CEX / DEX)~~~~,~~<br>        <br>    *   Centralized Exchange<br>        <br>    *   Decentralized Exchange (DEX)<br>        <br>    *   Payment, On-Ramp / Off-Ramp Service<br>        <br>    *   Wallet or Custodial Service<br>        <br>    *   DeFi Protocol or Infrastructure<br>        <br>    *   ~~Web3 Application (NFT / Gaming / SocialFi)~~~~,~~<br>        <br>    *   Other Crypto Business<br>        <br>*   Law Enforcement & Public Investigation<br>    <br>    *   Law Enforcement Agency<br>        <br>    *   Financial Crime Investigation Unit<br>        <br>    *   Other Public Investigation Body<br>        <br>*   Regulatory & Supervisory Authority<br>    <br>    *   Financial Regulatory Authority<br>        <br>    *   Central Bank / Monetary Authority<br>        <br>    *   AML / Compliance Supervisory Body<br>        <br>    *   Other Regulatory Authority<br>        <br>一级选项：单选（Radio / Card）<br>二级选项：单选（Dropdown / Radio）<br>仅在选中某一一级选项后，展开对应的二级选项<br>用户 **必须选择一个二级选项** 才可提交表单<br>> **未选择一级选项：**Please select your organization category.<br>> **已选一级，未选二级：** Please select a specific organization type. |
| Official Website | URL | \- | 用于验证机构真实性 |
| Registration Country / Region | dropdown | ✓ |  |
| **Contact Information**    for review contact only |  |  |  |
| Corporate Email | email | ✓ |  |
| Name | text | ✓ |  |
| Position / Title | text | – |  |

> 可以搞一个钉钉机器人自动往群里推送表单填写信息

> 同时后端系统也需要有此信息，可以点击审批通过/不通过按钮自动发送邮件

### 审核流程 

*   **审核通过的****：**发送注册验证邮件 
    
    *   注册链接的规则
        
        *   `https://phalcon_network.blocksec.com/register?token=[Unique_Token]`
            
        *   **Token 唯一性**：
            
            *   每个通过审核的项目申请必须生成一个**全局唯一**的 UUID 或加密 Token。
                
            *   token 必须与该项目方的 Email 及申请记录在数据库中强绑定。
                
        *   **一次性**：
            
            *   Token 仅限使用一次。用户完成密码设置并点击“Create Account”成功后，该 Token 必须立即失效。
                
            *   若用户中途关闭页面且未完成注册，只要在有效期内，链接仍可再次访问
                
            *   Token 校验失败 → 返回“链接过期，请申请重新发送”
                
        *   **有效期设定**：自邮件发出时刻起算，有效期为 **72 小时**。
            
*   **审核不通过的：**发送审核不通过邮件通知、提示可以使用compliance开放平台
    
    *   **Subject**
        

Update on your BlockSec Phalcon Network application

**Email Body**

Hi {{Contact Name}},Thank you for your interest in the **BlockSec Intelligence Network**.

After careful review, we’re unable to approve your application at this time.

You can still access on-chain risk analysis and monitoring through our **Phalcon Compliance Open Platform**, which is available without joining the Phalcon Network.

👉 [Explore Phalcon Compliance](https://app.blocksec.com/phalcon/v2/) 

If you believe this decision may be based on incomplete information, you’re welcome to contact us for further discussion.

Best regards,  
**BlockSec Team**

**邮件内容见**

### 账号与权限逻辑

*   Phalcon 采用统一账号体系，以邮箱作为唯一用户标识，用户仅需维护一套账号密码。
    
*   Compliance 与 Network 不设独立账号或密码，作为同一账号下的产品权限存在。
    
*   用户通过任一产品完成注册或登录后，其账号凭证在所有已授权产品中通用。
    
*   情报网络邀请链接必须绑定唯一邮箱；注册时邮箱必须与邀请绑定邮箱一致，不支持更换
    

### 注册流程

在情报网络申请审核流程中，对用户提交的邮箱进行校验，校验成功后，人工在后台发送邀请链接邮件：

*   **若用户邮箱已存在对应的 Phalcon 账号**
    
    *   系统向该邮箱发送 Phalcon 账号登录链接邮件
        
    *   用户通过该链接使用原有 Phalcon 账号密码完成登录
        
        *   邮箱显示：默认填入情报网络申请时填写的邮箱、置灰不可编辑
            
        *   密码输入框：用户填写原有phalcon账号对应的密码
            
    *   登录成功后，自动授予 Network 权限并跳转至情报网络 Onboarding 页面
        
*   **若用户邮箱尚未注册过 Phalcon 账号**
    
    *   系统向该邮箱发送 Phalcon 注册链接邮件（包含 Network 权限）
        
    *   用户完成注册后，系统自动开通该邮箱对应的 Phalcon Compliance 权限。
        
        *   邮箱显示：默认填入情报网络申请时填写的邮箱、置灰不可编辑
            
        *   密码输入框：用户仅设置密码，至此完成注册流程
            
    *   注册成功后跳转至情报网络 Onboarding 页面
        

```postgresql
+----------------------------------------------------------------------------------+
|                                                                                  |
|  +----------------------------------+   +-------------------------------------+ |
|  |                                  |   |                                     | |
|  |  Stay alerted to illicit         |   |        Create your Phalcon account  | |
|  |  crypto activity                 |   |                                     | |
|  |                                  |   |  +-------------------------------+  | |
|  |  Detect illicit funds the moment |   |  | Work Email                    |  | |
|  |  they reach your platform.       |   |  | [ newuser@company.com     🔒 ]|  | |
|  |                                  |   |  |  Linked to your invitation    |  | |
|  |  Receive real-time alerts and    |   |  +-------------------------------+  | |
|  |  isolate suspicious assets to    |   |                                     | |
|  |  stop laundering at the source.  |   |  +-------------------------------+  | |
|  |                                  |   |  | Create Password               |  | |
|  |  For advanced investigations,    |   |  | [ Enter a strong password ]  |  | |
|  |  continue in Phalcon Compliance. |   |  |  At least 8 characters        |  | |
|  |                                  |   |  +-------------------------------+  | |
|  |                                  |   |                                     | |
|  |  • Real-time risk alerts         |   |  +-------------------------------+  | |
|  |  • Early exposure detection      |   |  | Confirm Password              |  | |
|  |  • Immediate asset isolation     |   |  | [ Re-enter password ]         |  | |
|  |                                  |   |  +-------------------------------+  | |
|  |                                  |   |                                     | |
|  |                                  |   |  ( ) I agree to the Terms &      |  | |
|  |                                  |   |      Privacy Policy              |  | |
|  |                                  |   |                                     | |
|  |                                  |   |      [ Create Account ]          |  | |
|  |                                  |   |                                     | |
|  |                                  |   |                                  |  | |
|  |                                  |   |                                  |  | |
|  +----------------------------------+   +-------------------------------------+ |
|                                                                                  |
+----------------------------------------------------------------------------------+
| © 2025 Phalcon Inc.                                                               |
+----------------------------------------------------------------------------------+

```

```postgresql
+----------------------------------------------------------------------------------+
|                                                                                  |
|  +----------------------------------+   +-------------------------------------+ |
|  |                                  |   |                                     | |
|  |  Stay alerted to illicit         |   |        Sign in to Phalcon Network   | |
|  |  crypto activity                 |   |                                     | |
|  |                                  |   |  +-------------------------------+  | |
|  |  Detect illicit funds the moment |   |  | Email                    |  | |
|  |  they reach your platform.       |   |  | [ user@company.com        🔒 ] |  | |
|  |                                  |   |  |  Linked to your Network access |  | |
|  |  Receive real-time alerts and    |   |  +-------------------------------+  | |
|  |  isolate suspicious assets to    |   |                                     | |
|  |  stop laundering at the source.  |   |  +-------------------------------+  | |
|  |                                  |   |  | Password                      |  | |
|  |  For advanced investigations,    |   |  | [ Enter your password       ] |  | |
|  |  continue in Phalcon Compliance. |   |  +-------------------------------+  | |
|  |                                  |   |                                     | |
|  |  • Real-time risk alerts         |   |  [ Forgot password? ]               | |
|  |  • Early exposure detection      |   |                                     | |
|  |  • Immediate asset isolation     |   |      [ Sign in ]                    | |
|  |                                  |   |                                     | |
|  |                                  |   |                                     | |
|  |                                  |   |                                     | |        
|  |                                  |   |                                     | |
|  +----------------------------------+   +-------------------------------------+ |
|                                                                                  |
+----------------------------------------------------------------------------------+
| © 2025 Phalcon Inc.                                                               |
+----------------------------------------------------------------------------------+

```

**登出后重新登入：**

*   登出后再次进入 Network 时 ，先走统一账号登录（邮箱可预填），再做 Network 权限校验；
    
    *   若有权限，进入 Network主页；
        
    *   若无权限，进入“无权限”的错误态页面。提示文案：Network access is not available for this account. 
        
        *   CTA：Apply Access 跳转落地页申请表单
            
        *   次按钮：Switch Account 返回登录页面
            

## Onboarding 流程 （此流程已移除）

## 用户界面

作为项目方进行风险监控与情报接收的工作台，主要用于创建风险监控、配置通知渠道等。

用户可在该页面完成以下操作：

*   创建和管理需要监控的地址
    
*   查看历史监控触发的情报告警及统计数据
    
*   绑定与管理通知渠道
    
*   统一管理语言、时区及通知方式等全局偏好设置
    

**用户界面结构：**

1.  **Welcome板块**
    
    1.  **显示内容：**
        
        1.  **主标题：Welcome to the Phalcon Network!**
            
        2.  **说明文案：Stay alerted to illicit crypto activity.** Detect illicit funds in real time and stop laundering at the source
            
    2.  **交互：**
        
        1.  点击Dismiss可关闭该板块
            
        2.  点击Help Doc可进入帮助文档
            
2.  **Monitoring Addresses**
    
3.  **Notification Channel**
    
4.  **Triggered Alerts**
    
5.  **导航栏**
    
    *   Language
        
    *   Timezone
        
    *   Help Doc
        
    *   Account 
        
        *   Account Settings
            
        *   Logout
            

### 监控地址列表  Monitoring Addresses

模块名称Monitoring Addresses

模块描述文案：Addresses added here will be continuously monitored for incoming illicit funds.

描述文案右侧显示tooltips

当用户尚未添加任何待监控的目标地址时，Monitoring Addresses列表内显示文案：

主文案：Don't have address yet

次文案：Add an address to monitor illicit inflows.

CTA：Add Monitoring Address

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/b4be968f-2477-4235-bfa5-4a3ddb6f73c3.png)

点击 Add Monitoring Address，在弹窗中可以搜索地址、添加 Note 完成 Monitoring Address 的添加。

用户搜索地址时需要同步展示系统默认的 Label。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/8616fb17-87c0-447a-ab24-ee29b3829add.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/fb7aeaa7-240c-4911-b9a1-a34eafb298df.png)

点击Create, 弹窗询问是否

标题：Connect a notification channel to receive alerts

文案描述：To receive alerts when illicit funds flow into your monitored address, please connect a notification channel.

主按钮：Connect Now    次按钮：Later

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/4cdd114c-97ad-4308-bd7b-4e8b93cd8acd.png)

添加了至少一个监控的地址时，用户界面显示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/526a5785-7655-4fc9-b254-2594fe4c7ffc.png)

列表字段：

*   Address：链图标 + 地址 + 系统 Label
    
*   Status（Active / Paused）
    
*   支持操作：
    

*   Pause / Resume
    
*   Delete
    

*   Note：添加地址时填入的备注，允许编辑
    
*   Created at：展示此地址添加时间
    

\*当用户已经添加了 3 个 address 时，不再展示 Add Monitoring Address 的按钮。

### 通知渠道管理Notification Channel

通知渠道在账户维度统一管理，不与单个 Alert 绑定。

通知渠道管理页面显示++已绑定的通知渠道列表++ & ++Create Channel CTA++

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/79f7edff-8c17-449e-8d3e-be2e5009d56e.png)

**交互说明：**

1.  **创建通知渠道**
    

*   点击 Create Channel，弹出 Create Notification Channel 弹窗
    
*   弹窗内容：
    
    *   显示 Channel Type 下拉选项框
        
    *   默认显示文案：Select Channel
        
    *   下拉可选项包括：Email、Telegram、Slack、Lark
        

**2）不同 Channel Type 的配置交互**

**a. Channel Type = Email**

*   下方展示：
    
    *   Email Address 输入框
        
    *   Verification Code 输入框
        
    *   Send Code 按钮 （需要有重复点击倒计时）
        
*   校验提示：
    
    *   a. 邮箱格式错误时，提示：Please enter a valid email
        
    *   b. 验证码格式错误时，提示：Please enter a valid code
        
*   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/0789143a-d596-4c63-89a3-7074dc9a7fd6.png)
    

**b. Channel Type = Telegram**

*   下方展示：
    
    *   Channel Name 输入框
        
    *   Telegram 配置框
        
*   Telegram 配置项包括：
    
    *   Chat Type：user / Group
        
    *   选择 Chat Type 后，在右侧填写 Telegram Chat ID
        
*   Telegram 配置框右上角显示：Get Chat ID
    
*   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/19bfb2ea-055f-4bfa-92ac-0b5d1e6cd58f.png)
    

**c. Channel Type = Slack**

*   下方显示 Slack 连接配置框
    
*   提示文案：  
    “Add @PhalconAlertBot to your workspace and authorize a specific channel to receive notifications from {{Channel Name}}”
    
*   操作按钮文案：Connect Slack
    
*   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/e24c4ca3-b02c-41ba-be11-a8cf08c7309f.png)
    

**d. Channel Type = Lark**

*   下方展示：
    
    *   Channel Name 输入框
        
    *   Webhook URL 输入框
        
    *   Signature 输入框
        
*   配置栏右上角显示：Help doc 链接  
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/137298be-b64c-4df7-bc8f-c55258c462bc.png)
    

**3）创建与取消操作**

*   点击 Create
    
    *   a. 若 Channel 格式正确且验证无误，提示：New Channel Created!
        
    *   b. 若存在未填写的输入框，Create 按钮禁用
        
*   点击 Cancel
    
    *   关闭 Create Notification Channel 弹窗
        
    *   返回 Notification Channel 管理主页面
        

**4）删除通知渠道**

*   在管理页面选择任意一行 Notification Channel
    
*   点击 Delete
    
*   显示提示：Channel Successfully Deleted!
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/e9110333-937e-43a2-a204-32c4c2dcceaf.png)

### 警报历史记录 Triggered Alerts

Triggered Alerts 模块用于展示已被监控规则触发的历史情报告警记录，并提供告警概览统计，支持用户快速判断整体风险态势，并进入单条告警详情页进行进一步调查。

Triggered Alerts没有数据的情况，显示文案：No alerts yet.

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/d32db98e-cd73-43ef-8c60-8f760bfe3e20.png)

列表字段：

*   Alert ID
    
    *   展示 Alert ID(如#ALERT-20230701-001)
        
*   Address
    
    *   展示完整或中间截断的地址字符串（如有地址label直接显示label）
        
    *   支持 hover 查看完整地址
        
    *   还需要考虑地址 Note 如何展示
        
*   Risk Type
    
    *   展示风险类型标签，如有多个，则都要展示
        
*   Alert Note
    
    *   用户可以对 Alert 添加 Note 备注，直接行内编辑修改
        
*   Triggered Time
    
    *   时间展示跟随用户配置的全局时区
        
*   Actions
    
    *   View Details
        
    
    可筛选项：
    
*   Address：支持按监控的地址对alert进行筛选
    
*   Risk Type：支持按风险类型对alert进行筛选
    
*   Start Date - End Date: 支持按alert触发事件进行筛选
    

搜索框：支持在my monitoring 模块按alert id, alert note关键词进行快捷检索

交互说明：

*   数据为只读
    
*   除Alert Note外其他字段均不支持编辑、删除或状态变更
    
*   点击 View Details 弹窗展示对应 Alert 详情
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/b226e881-831f-41c9-8861-a2b0e79db95e.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/605b5811-4b59-4d2c-ade8-42da068f1254.png)

Alert 详情内容：

*   固定标题 + Risk Type 
    
    *   若有多个 Risk Type，用逗号拼接
        
*   Alert ID：不需要有点击跳转的样式
    
*   Risk Information：
    
    *   Risk Type
        
    *   Information Source
        
*   Transaction Details
    
    *   From address：当条 transfer 对应的 from address。点击跳转对应 scan
        
    *   Monitored address：监控地址，也是当前 transfer 对应的 to address
        
    *   Transaction Hash：点击跳转 scan
        
    *   Value(USD)：当前 transfer 对应的美元价值
        
    *   Time：交易时间，跟随用户配置的失去，后面不用展示 （UTC）等
        
    *   View full risk details for this transaction：点击跳转 compliance 展示本条 transfer 的 lite scan 结果（如果用户已登录且还有用量，展示 screen 完整结果）
        
*   Fund Flow 资金图
    
    *   本条 alert 的 fund flow 资金流图
        
    *   点击跳转 MS 查看完整资金流图
        

### 导航栏

导航栏右侧为用户个人中心，包含“偏好设置（Preferences）”、“账户信息（Account）”及“退出登录（Logout）”三大功能区，旨在提供个性化的使用体验并管理用户会话。

1.  **Language (语言)**
    
    1.  简体中文 (zh-CN) / English (en-US)。
        
    2.  生效范围：全站 UI 文案、系统通知、错误提示。
        
2.  **Timezone (时区)**
    
    1.  前端显示：平台内所有风险事件的时间戳（Dashboard, History 等）均按此设置转化显示。
        
    2.  Alert 推送：同步影响Timezone设置生效后Alert消息（如邮件 Alert）中的时间信息。确保用户收到的邮件时间与其在平台设置的时区一致。
        
    3.  预设值：首次进入时默认跟随浏览器本地时区。
        
3.  **Help Doc(帮助文档入口)**
    
4.  **Account (账户管理)**
    
    1.  **Profile（个人资料**
        

*   **内容**：
    
    *   展示当前登录的 **Phalcon 账号** 基本信息，包括：
        
        *   注册邮箱
            
        *   Change Password 按钮
            
        *   2fa 认证开关
            

*   **Logout (退出登录)**
    
    *   **Phalcon Network 登出**：点击后清除 Phalcon Network 的本地 Session 和 Token，页面重定向至 Phalcon Network 登录页。
        
    *   **Phalcon 关联状态**：**不执行同步登出**。即用户登出 Phalcon Network 后，若其在另一标签页打开了 Phalcon Compliance，该 Phalcon 会话依然保持活跃。
        
    *   **身份覆盖逻辑**：若用户登出当前 Phalcon Network 账号后，登录了一个新的 Phalcon Network 账号，此时访问 Phalcon 应自动触发身份校验，用新的 Phalcon Network 账户信息“顶掉”或同步更新 Phalcon 的登录状态，以确保两端身份一致。
        

**交互需求表**

| **菜单项** | **子项** | **交互方式** | **逻辑说明** |
| --- | --- | --- | --- |
| Preferences | Language | 下拉切换 | 默认跟随浏览器；切换后全站刷新生效。 |
| Preferences | Timezone | 搜索选择 | 修改后需同步更新后台预警配置中的时区。 |
| Account | Profile | 页面跳转 | 仅展示，不提供 Input 输入框。 |
| Account | Terms | 外部链接 | 跳转至 `/terms-of-service`。 |
| Action | Logout | 二次确认弹窗 | 登出 Lumen 后不影响 Phalcon，除非登录新账号。 |

**补充说明：**

*   当用户点击导航栏右侧的 **Sign in** 按钮（登出后状态）进入登录页时，页面应能通过 Cookie 识别其最近一次使用的邮箱，并在 Email 输入框进行预填充。
    
*   **Phalcon 引导**：虽然导航栏不设常驻入口，但在注册完成后的“引导成功页”及“风险邮件”中，依然保留引导至 Phalcon 的快捷路径。
    

## 消息推送

观察到当前 Compliance  用户使用的通知渠道有：

*   Telegram
    
*   Lark
    
*   Slark
    
*   Email
    

可以先支持以上的通知渠道。

### 监控和警报机制

#### 监控范围

*   系统持续监控用户配置的 监控地址。
    
*   仅关注入金方向的 Transfer（`to address = monitoring address`）。
    
*   当单笔入金 Transfer  金额 **≥ 系统阈值 X（USD）** 时，才进入风险判断流程。
    

#### 风险判定逻辑

1.  **直接风险命中**
    
    *   若 Transfer  的 **from address** 直接命中任一支持的风险类型：
        
        *   立即触发 Alert
            
        *   不再执行资金多跳路径扫描。
            
2.  **间接风险命中**
    
    *   若 from address 未直接命中风险：
        
        *   对该 Transfer  执行入金方向的资金路径扫描。
            
        *   保留 `exposure value ≥ 阈值 Y（USD）` 的风险类型的路径。
            
    *   若存在符合条件的风险路径：
        
        *   **合并触发 1 条 Alert**
            
        *   在同一 Alert 中展示命中的多个风险类型。
            

#### Alert 合并规则

*   **单笔 Transfer  最多触发 1 条 Alert**。
    
*   同一 Transfer  命中的多个风险标签，在同一 Alert 中合并展示。
    

#### 阈值说明

*   阈值 **X** 为系统级配置。
    
*   Phase 1 使用统一默认值（待定）。
    
*   用户不可自定义。
    

一些待讨论问题：

1.   阈值 X 、Y 定为多少合适？
    

*   阈值 X：需要考虑到对性能的影响， 阈值越大扫的交易数量越少，参考 [《阈值设定参考》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=oP0MALyR8kqmxMYoH2z40DMPV3bzYmDO&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)中对不同类型地址不同交易金额下 24 小时内 transfer 数量的统计，定为 **$10,000** 比较保险。
    
*   阈值 Y：要 >= $5,000 且小于阈值 X，可以暂定为 **$5,000**。（设置高了的话，Alert 数量会比较少，反正都已经扫了，可以多报一些 Alert）
    

1.   本次第一阶段可采用 Transaction Screen 的方案，但后续到第二阶段是否要采用之前的资金监控的方案？
    

外部报告涉及两类监控场景，其实现逻辑不同：

*   **面向报告方（Reporter）：**
    
    *   需监控被报告地址的后续所有资金转移（需预计算），并在资金流入已知实体时向其发出警报。
        
    *   此场景现有 Compliance 引擎扫描缺乏主动触发机制？
        
*   **面向项目方**：
    
    *   在常规监控扫描中发现资金来源与外部报告相关时，需触发警报，可以用 KYT Screen 实现
        
    *   **衍生问题**：
        
        *   外部 Report 的风险与内部风险标签应该区分为不同的 Alert 进行展示
            
        *   外部 Report 应按 Case 划分 Alert，以便单独展示报告背景、报告方及所需行动等数据。
            

3.  这次实现的监控和 Compliance 产品后续要实现的监控不太一样
    

*   **Phalcon Compliance**
    
    *   监控对象：地址或交易本身
        
    *   持续 re-screen 看地址或交易有没有新的风险
        

*   **Phalcon Network**
    
    *   监控对象：地址
        
    *   有新的入金交易时 screen 那笔入金交易
        

### 消息内容结构及字段说明 

不论通过哪种通知渠道推送，消息内容和格式均统一如下。

| 内容 | 格式 | 说明 |
| --- | --- | --- |
| 标题 | Detection of Illicit Funds in Incoming Transfer **(\[Risk Description\])** | *   **Risk Description:** 标明对应的风险类型，加粗展示。<br>    <br>    *   英文：<br>        <br>        *   如果有 2 个类型，用 and 拼接，如：Sanctioned and Bloced<br>            <br>        *   如果有 3 个及以上类型，仅展示优先级最高的 1 个拼接 “and 2 more”，如：Sanctioned and 2 more |
| Alert ID | Alert ID: 3a0d14f0-4650-4abe-abbe-a9daf3edd46d \[Phalcon Network Alert Link\] | *   点击 ID 可以直接跳转到平台 |
| 风险详情（Risk Detail） | **Risk Information**<br>*   Risk type: \[Risk Type\]<br>    <br>*   Information source: \[Information Source\] | *   **Risk Type**: 风险类型<br>    <br>    *   有 多个时用逗号拼接<br>        <br>*   **Information Source**<br>    <br>    *   本次上线仅有 BlockSec Internal Label Library 这一种类型 |
| Transaction Data | **Transaction Details**<br>*   From address: \[From Address\]<br>    <br>*   Monitored address: \[Monitored Address\]<br>    <br>*   Transaction hash: \[Transaction Hash\]<br>    <br>*   Value(USD): \[Value\]<br>    <br>*   Transaction date: \[Transaction Date\] | *   **From address**：当前 transfer  中的 from 地址 （点击跳转 scan），如果有标签的话，优先展示标签<br>    <br>*   **Monitored address**: 当前 transfer  中的 to 地址 <br>    <br>    *   也为用户监控的地址，有 label 则优先展示 label 加地址前几位，有 note 时在后括号展示<br>        <br>    *   如：OKX Hot Wallet 0x829 (Waallet 1)<br>        <br>*   **Transaction Hash**：触发此 Alert 的交易 hash（点击跳转 scan）<br>    <br>*   **Value**：对应 Transfer 的美元价值<br>    <br>*   **Transaction Date**：交易的时间<br>    <br>    *   按照用户配置的时区展示（默认 UTC 时区）<br>        <br>    *   格式：yyyy-mm-dd hh:mm:ss (时区) |
| 跳转链接 | **🟠  Screen and view full risk details for this transaction** \[Compliance Lite Scan Link\]<br>View fund flow graph \[MS Fund Flow Link\] \| Pause monitor  \[Phalcon Network Link\] | *   **Compliance Lite Scan Link**：<br>    <br>    *   拼接的 compliance scan 链接（如果用户已登录则自动跳转扫描）<br>        <br>    *   扫描的是触发 Alert 的这笔 transfer<br>        <br>*   **MS Fund Flow Link**：预生成的 MS 资金流图分享链接，点击后自动跳转 MS 平台展示当前 Alert 相关资金流图。<br>    <br>*   **Phalcon Network Link**: 点击后跳转平台，Pause Monitor （弹出二次确认弹窗） |
| 资金流图 | 消息中需要附带可视化的资金流图路径，考虑到不同通知渠道的限制和要求不同。详细见 2.4.3 部分说明。 |  |

**消息示例**

:::
Detection of Illicit Funds in Incoming Transfer **(Sanctioned and Blocked)**

Alert ID: 3a0d14f0-4650-4abe-abbe-a9daf3edd46d

Risk Information

Risk Type: **Sanctioned, Blocked**

Information Source: BlockSec Internal Label Library

Transaction Details

From address: [TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9](https://tronscan.org/#/address/TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9)

Monitored address: TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC (Note)

Transaction hash: [3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35](https://tronscan.org/#/transaction/3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35)

Value (USD): $50,000

Time: 2025-10-20 07:11:48 UTC

**🟠 View full risk details for this transaction** 

View Fund Flow | Pause Monitor

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/8da017d8-8a16-4cc4-8f66-8bf1fd6c0d0a.png)
:::

### 资金流图展示

目标：在告警消息中提供 直观、可快速理解的资金路径概览，提升 Alert 的可读性。

**展示原则**

*   单条 Alert 对应 **一张总览资金流图**，合并展示该 Alert 命中的所有风险路径。
    
*   对中间节点进行 **Grouping / 聚合**，避免路径过长或节点过多导致图像不可读。
    
*   告警内容结构保持一致，展示形式根据通知渠道能力进行适配。
    

在生成 **MS Fund Flow 分享链接** 的同时：

*   同步生成对应的 资金流图预览图
    
*   将预览图上传并保存，链接预览使用
    

**各渠道展示策略**

*   **Telegram**：  
    受图片与文本长度限制影响，本期不直接发送图片，仅通过 **Fund Flow 分享链接的链接预览** 展示资金流图；该链接需作为消息中的**第一条链接**。
    
*   **Lark / Slack / Email**：  
    支持在消息中直接插入资金流图图片，并同时保留 Fund Flow 分享链接用于查看完整交互式分析。
    

#### 附：各渠道展示图片限制

待确认：是否可以实现点击图片跳转链接？

| 渠道 | 图片展示 | 链接预览 |
| --- | --- | --- |
| Telegram | *   可以文字和图片在一个消息中发送<br>    <br>*   图片可以设置在消息的最顶部或最底部<br>    <br>*   大小限制较严：<br>    <br>    *   和图片一起发送的文字（不能超过1024 个字符）<br>        <br>        *   上述示例消息基本就是极限了<br>            <br>    *   单纯文字（不能超过 4096 个字符）<br>        <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/139e3bc8-8af0-4b38-9f4f-18502c980f69.png) | 和消息发送一致，取消息中的第一个链接展示预览<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/3c4db645-5a6d-4993-a934-1b84305e7857.png) |
| Lark | *   富文本格式支持插入图片<br>    <br>*   图片需要先使用 API 进行上传，需要 API 权限<br>    <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/e8d97ed4-2b7c-48f5-ae73-1fca7ea1662c.png) | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/d650a9f4-5472-415d-b18f-1d510087bca6.png)<br>不展示图片 |
| Slark | *   富文本支持插入图片<br>    <br>*   试了一下没有什么限制 |  |
| Email | 支持 HTML 格式，可以插入图片 | 不支持 |

问题：如何避免一个用户收到太多重复消息？

*   设置 exposure value / percent 阈值？
    
    *   1w刀
        

# Archived

## Onboarding

### 触发条件

*   用户完成注册并首次登录系统时触发 Onboarding
    
*   用户必须完成至少一个 Monitor 的创建：添加 1 个地址且至少绑定一个通知渠道，才视为完成。
    
*   未完成 Onboarding 前：
    
    *   不可进入主系统功能页
        
    *   仅允许停留在 Onboarding 流程中（每次重新进入时要从头开始 Onboarding 流程）
        

### Onboarding 步骤

在 Onboarding 界面直接展示完成工作流的步骤，即：1. Add Monitoring Address 2. Connect Notification Channels 3. Review & Create.

在每个步骤用文案让用户清楚理解平台的工作流程。

1.  **Add Monitoring Address**
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/ec616824-7cce-4c55-b709-b1f0b3397ef2.png "待添加地址")![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/6f73e22b-3ecd-48a4-ad7e-e9bb5302fc47.png "已添加地址")

*   Continue 按钮默认 Disable
    
*   用户在搜索框输入地址，校验格式正确后进行搜索
    
*   搜索结果展示当前地址所有活跃链，如果对应的结果有 label 也需要展示
    
*   用户点击一个搜索结果后完成地址添加
    
    *   点击后完成回填
        
    *   一次只能选择一个地址
        
*   添加了一个地址后 Continue 按钮即变为可点击状态
    
*   用户可选为地址添加 Note，也可删除地址重新添加
    

1.  **Connect Notification Channels**
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/91e9f8f8-b37f-435d-8c18-81795bdf2b55.png)

*   用户可以 Back 返回上一步，还未 Connect Notification Channel 时 Continue 按钮 disable 状态
    
*   用户可以点击  Add Notification Channel 后开始添加，交互可以沿用 Phalcon
    
    *   本次支持 Telegram、Lark、Slark 和 Email 4 种通知渠道
        
*   用户链接了一个渠道后，Continue 按钮即可以点击
    

1.  **Review & Create**
    

展示地址、NC 和 示例 Alert 消息，用户点击 Create 按钮确认后即进入系统 Dashboard 界面。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/28b3afaa-c2f9-40ac-b946-e37869b9f036.png)