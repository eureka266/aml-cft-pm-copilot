# Lite Scan & 分享页

# 背景和目标

## 需求背景

| **产品模块** | **核心目标** |
| --- | --- |
| **Lite Scan** | **内部用户转化与付费升级。** 优化访客 (Visitor) 和免费/低付费用户的体验，驱动其**注册/升级**。 |
| **结果分享页** | **品牌曝光与外部转化。** 成为 Phalcon Compliance 对外宣传和获取新用户的**主要外部入口**。 |

## 产品目标

本次目标旨在设计两个基于现有详情页的变体页面：

*   **Lite Scan 页面**
    
    *   仍位于 Phalcon Compliance 平台内部（保留左侧导航、顶部导航等结构）
        
    *   展示现有详情页的部分内容，对某些模块做遮盖或禁用
        
    *   面向 Visitor 用户及用量已耗尽的已注册用户
        
    *   目标是推动用户登录 / 升级订阅
        
    *   保留平台内部操作结构，例如 Audit Logs / Alerts 的位置，但在 Lite Scan 中禁用或遮盖
        
*   **结果分享页**
    
    *   完全独立于平台内部 UI（无侧边栏、无内部导航）
        
    *   面向外部用户浏览（来自 Cobo 等合作方的引流）
        
    *   需要具备强 SEO 能力、对外品牌曝光能力
        
    *   展示扫描的核心内容，但隐藏敏感字段
        
    *   强引导用户注册登录
        

两个页面均基于当前地址/交易详情页，通过：

*   模块移除
    
*   信息遮盖
    
*   交互禁用
    
*   CTA 引导增强
    

实现不同场景的差异化展示。

# 详细方案

## Lite Scan

*   面向 **Visitor 用户** 或 **用量耗尽用户**
    
*   帮助用户了解产品能力，可以获得初步的风险筛查结果
    
*   引导登录、付费、升级，提高平台内部转化率
    
*   保持平台“正常详情页”的结构感，避免页面割裂
    
*   Lite Scan 模式下不保存用户扫的地址、交易数据，不产生 Alert 数据等，只给用户展示单次风险筛查的结果。
    

### 地址详情页

[Figma  设计稿: https://www.figma.com/design/hsxEaRsCidIR2x3rh9XN3x/Phalcon?node-id=1332-7113&t=ucxanT1eQmac3uib-4](https://www.figma.com/design/hsxEaRsCidIR2x3rh9XN3x/Phalcon?node-id=1332-7113&t=ucxanT1eQmac3uib-4)

| **模块** | **详细说明 (与原详情页对比)** | **交互&文案** |
| --- | --- | --- |
| **页面结构** | **保留**左侧菜单、右侧 Audit Logs 和 Alerts 区域（但功能禁用或遮盖）。 | \- |
| **顶部按钮** | **移除/禁用**其他操作按钮（如 Re-screen Now、KYA Report 等）。 | \- |
| **Address Information** | **展示：** 风险等级、地址、Entity、Category、Balance、Total Inflow/Outflow。<br>**禁用** Customer、Auto Re-screening Status。 | \- |
| **Labels 和 Tags** | **禁用** 编辑功能。 | \- |
| **Risk Summary** | **展示：** 现有展示逻辑和样式。<br>**限制：** Hover 后**不再展示**详细风险信息。且在 Tips 中进行用户引导 | Tips 中引导文案：（提示注册登录/升级来解锁功能）<br>*   Visitor 用户：Sign in to view risk details<br>    <br>*   无 Credit 用户：Upgrade to view risk details |
| **Risk Overview** | **完整遮盖/移除** Entity Risk、Blacklist Risk、Behavior Risk 整个区域。 | 遮盖区域文案：<br>Unlock full risk insights – including detailed risk labels, behavioral risk analysis, and interactions with your custom blacklisted addresses.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **Risk Exposure 饼图** | **展示：** 风险资金分布饼图。<br>**图例**仅展示到 Risk Indicator，**不展示**具体百分比。<br>**禁用** By Risk Indicator 和 By Address 的切换功能。 | 饼图上的 Hover 交互保留，Hover 后展示：<br>*   Visitor 用户：Sign in to view precise value and percentage<br>    <br>*   无 Credit 用户：Sign in to view precise value and percentage |
| **Risk Exposure 列表** | 仅展示**第一个 Risk Indicator** 下的第一个风险地址数据。其余数据**全部遮盖**。**切换到其余 Risk Indicator 时全部遮盖**。 | 遮盖区域文案：<br>Unlock full risk insights – including flagged addresses, their risk labels, exposure value, and percentage of funds affected.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **风险资金流图** | 全部遮盖 | 遮盖区域文案：<br>Unlock full risk insights – view complete risk maps and detailed fund flows.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **Top Counterparties** | **资金流图**：**遮盖**。**对手方列表**：仅展示 **Top 3**，其余遮盖。 | 遮盖区域文案：<br>Unlock full risk insights – view top counterparty addresses and the interaction details.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **Transfers** | **完整遮盖**交易列表。 | 文案：<br>Unlock full risk insights - view all transfers related to the target address. |
| **Alerts** | **完整遮盖** | 文案：<br>Unlock Full Risk Insights – view all triggered alerts with detailed risk analysis. |
| **Audit Logs** | **禁用**该模块功能，不允许点击切换查看 | \- |

说明：

*   所有遮盖区域都统一用毛玻璃样式，上面展示引导文案 （对 Visitor 引导注册，对其余用户引导升级）
    
*   页面顶部提示用户当前为 Lite Scan 模式： 
    
*   对于用量用尽的用户，不允许对之前的地址 Re-screen （会导致之前可看到页面看不到）。
    
*   Hover 交互：所有的 Hover 展示的详细信息的地方改为展示引导 Tips。
    

### 交易详情页 

| **模块** | **详细说明 (与原详情页对比)** | **交互&文案** |
| --- | --- | --- |
| **页面结构** | **保留**左侧菜单、右侧 Audit Logs 和 Alerts 区域（但功能禁用或遮盖）。 | \- |
| **顶部按钮** | **移除/禁用**其他操作按钮（如 Re-screen Now、KYA Report 等）。 | \- |
| **Address Information** | **展示：** 风险等级、地址、Entity、Category、Balance、Total Inflow/Outflow。<br>**禁用** Customer、Auto Re-screening Status。 | \- |
| **Labels 和 Tags** | **禁用** 编辑功能。 | \- |
| **Risk Summary** | **展示：** 现有展示逻辑和样式。<br>**限制：** Hover 后**不再展示**详细风险信息。且在 Tips 中进行用户引导 | Tips 中引导文案：（提示注册登录/升级来解锁功能）<br>*   Visitor 用户：Sign in to view risk details<br>    <br>*   无 Credit 用户：Upgrade to view risk details |
| **Risk Overview** | **完整遮盖/移除** Participant Risk、Blacklist Risk、Behavior Risk 整个区域。 | 遮盖区域文案：<br>Unlock full risk insights – including detailed risk labels, behavioral risk analysis, and interactions with your custom blacklisted addresses.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **Risk Exposure 饼图** | **展示：** 风险资金分布饼图。<br>**图例**仅展示到 Risk Indicator，**不展示**具体百分比。<br>**禁用** By Risk Indicator 和 By Address 的切换功能。 | 饼图上的 Hover 交互保留，Hover 后展示：<br>*   Visitor 用户：Sign in to view precise value and percentage<br>    <br>*   无 Credit 用户：Sign in to view precise value and percentage |
| **Risk Exposure 列表** | 仅展示**第一个 Risk Indicator** 下的第一个风险地址数据。其余数据**全部遮盖**。**切换到其余 Risk Indicator 时全部遮盖**。 | 遮盖区域文案：<br>Unlock full risk insights – including flagged addresses, their risk labels, exposure value, and percentage of funds affected.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **风险资金流图** | 全部遮盖 | 遮盖区域文案：<br>Unlock full risk insights – view complete risk maps and detailed fund flows.<br>\[引导 CTA\]: <br>*   Visitor 用户：Sign in to view details<br>    <br>*   无 Credit 用户：Upgrade to view details |
| **Token Transfers** | 可查看，不能点击 Alert 打开 Alert 抽屉 | \- |
| **Transfer Overview** | 可查看 | \- |
| **Alerts** | **遮盖**全部区域 | 文案：<br>Unlock Full Risk Insights – view all triggered alerts with detailed risk analysis. |
| **Audit Logs** | **禁用**该模块功能，不允许切换到该 Tab 查看。 | \- |

*   Transfer 详情页保持和 Transaction 详情页一样的遮盖逻辑
    

### API 相关逻辑

当用户的 Screen 点数耗尽，以下接口不允许调用：

| 接口类型 | Action | 报错文案 |
| --- | --- | --- |
| **筛查类接口（Screen Address / Screen Transaction / Batch Screen）** | 禁止调用 | You have run out of screening credits. |

> 目的：Lite Scan 模式下的结果仅用于前端基础展示，不作为 API 能力提供给用户。

用户在现有 Plan 有效期内仍可调用其他接口。（黑名单、Customer 等接口也要加上数量限制逻辑和报错）

### Re-screen 逻辑

当用户 Screen 点数耗尽，不允许对曾经已经扫过的地址进行 Re-screen （界面或 Auto Re-screen 均不可）。

当用户在界面点击 Re-screen 时，弹窗提示：

:::
**Screening Quota Exhausted**

 Your monthly screening quota is currently depleted. Please purchase a credit pack or upgrade your plan to perform a re-screen.

\[Buy Credits\] \[Upgrade Plan\]
:::

## 结果分享页

[Figma  设计稿: https://www.figma.com/design/hsxEaRsCidIR2x3rh9XN3x/Phalcon?node-id=1347-8545&t=ucxanT1eQmac3uib-4](https://www.figma.com/design/hsxEaRsCidIR2x3rh9XN3x/Phalcon?node-id=1347-8545&t=ucxanT1eQmac3uib-4)

| **模块** | **详细规格** |
| --- | --- |
| **页面结构** | 移除左侧菜单、右侧 Alerts/Audit Logs。 |
| **基础信息** | **移除** `Customer`、`Screening Count` 和 `Auto Re-screening Status` 字段。 |
| **遮盖逻辑** | **与 Lite Scan 页面保持一致**。 |
| **引导 CTA** | 所有遮盖区域的 CTA 统一指向 **注册/登录 (Sign Up / Sign In)**，不区分 Credit/Plan 状态。 |
| **顶部引导栏** | 增加顶部引导栏（突显品牌、**结果创建时间**、搜索框），以及侧边浮动 CTA。 |
| **生成逻辑** | 后台实现分享页创建逻辑。页面展示**地址对应的静态风险结果**，并明确标注数据的时间戳。 |

## 其他逻辑

#### 分享页 URL

*   地址：https://blocksec.com/phalcon/compliance/report/{chainName}/{address}
    
*   交易：https://blocksec.com/phalcon/compliance/report/{chainName}/{transaction hash}
    

#### 分享页 Description 

*   地址：
    
    *   格式： KYA Report | Verified by Phalcon Compliance. {risk\_type\_label} risk detected for {address}({label}) on {chain name}.
        
    *   示例：KYA Report | Verified by Phalcon Compliance. Attack risk detected for 0xfb63aa935cf0a003335dce9cca03c4f9c0fa4779 (Yearn Finance Exploiter) on ETH.
        
*   交易：
    
    *   格式：KYT Report | Verified by Phalcon Compliance. {risk\_type\_label} risk detected for {transaction hash}({label}) on {chain name}.
        

**risk\_type\_label 生成规则**

*   将 Risk Summary 处的风险 Tag  去重后拼接，使用逗号分隔
    
*   示例：
    
    *   `Sanctioned`
        
    *   `Sanctioned, Human Trafficking`
        
    *   `Transit address, Large Transfer`
        

#### 分享页 Title

Crypto Risk Report for {addreess\_display} | Phalcon Compliance

**address\_display 规则:**

*   如果地址本身没有 label，直接展示全部地址
    
*   如果地址本身又 label，展示：label (地址前八位...地址后八位)
    

示例：Crypto Risk Report for Yearn Finance Exploiter (0xfb63aa...fa4779) | Phalcon Compliance

#### 分享页地址

[《分享页地址》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=YndMj49yWjwaygboTM4rR3AdV3pmz5aA&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

#### 空状态

当用户通过手动拼接 URL 访问某个地址或交易的分享页时：

*   URL 结构正确，但系统中尚未生成该 {address}/{transaction hash} 的报告：  
    → 展示 空状态页面，引导用户自行筛查。
    
*   URL 中的 {chainName} 不支持，或 {address}/{tx\_hash} 格式不符合规则：  
    → 展示 404 页面。
    

**页面文案**

顶部：

No Result Available

We couldn't find a pre-generated compliance result for this address or transaction. 

页面主体：

We don’t have a compliance report for this address or transaction yet.

Start a screening to get the latest risk result.

\[搜索框：自动填入对应 address / tx\_hash\]

CTA：

*   Sign Up for Free
    
*   Screen Now