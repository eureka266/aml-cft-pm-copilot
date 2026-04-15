# Home首页

# 1. 背景与目标

Phalcon 提供地址/交易风险扫描、事件监控、合规分析等能力。Home 页面是用户进入产品后的核心交互起点，承担“价值展示 + 权限分层 + 升级转化”的关键角色。

通过home页的改造，希望实现：

1.  强化扫描入口，将 Phalcon 的“核心价值”与“高阶价值”在 Home 清晰呈现
    
2.  提供最近扫描、热点事件等链上动态，直观展现产品数据能力
    
3.  通过受限展示刺激注册 / 升级 / 补额度
    

# 2. 用户类型与功能权限

| **模块** | **Visitors** | **Free Trial** | **Starter** | **Growth** | **Pro** | **Enterprise** |
| --- | --- | --- | --- | --- | --- | --- |
| **核心筛查区域** | 完整可用 |  |  |  |  | 完整可用 |
| ~~**Recent Critical Events**~~ | ~~展示最新数据；不可点击详情（弹注册）~~ | ~~展示最新数据~~ |  |  |  |  |
| **Compliance Hotspots** | 显示 Trending Searches 和 Compliance 相关最新 Blog<br>Visitor 可点击直接 search 地址，进入lite scan结果页 |  |  |  |  | 完整可用 |
| **Recent screened addresses** | 不显示 | ~~默认显示最近3次扫描记录，点击可进入详情页~~<br>~~额度达到限制时，进入详情页后展示lite scan页面~~<br>free及以上等级用户达到额度限制时，点击过往扫描的地址允许继续查看之前的完整扫描结果，点击rescreen才提示升级![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/7c0183dd-dac0-4e1b-b18c-934e9acfc905.png) |  |  |  | 完整可用 |
| **Recent screened transactions** | 不显示 |  | 完整可用 |
| **Configurable Risk Engines** | 展示说明+预览图；引导注册 | 展示说明+预览图；引导试用/升级**解锁功能** | 展示说明+预览图；引导试用/升级**获取更多数量** | 不显示 | 不显示 | 不显示 |
| **Customer Profiling & Internal Watchlist** |  | 展示说明+预览图；引导试用/升级**获取更多次数** | 不显示 | 不显示 | 不显示 | 不显示 |
| ###  Auto Monitoring & Alerts |  | 展示说明+预览图；引导试用/升级**解锁功能** | 不显示 | 不显示 | 不显示 | 不显示 |
| **API Intergration** | 不显示 | 不显示 | 不显示 | 展示说明+预览图；引导升级 | 显示快捷入口？ | 显示快捷入口？ |
| **Team Colaboration**<br>**(assigned to me..)** | 不显示 | 完整可用 | 完整可用 | 完整可用 | 展示说明+预览图；引导订购enterprise plan | 完整可用 |
| **Message Center** | 不显示 | 完整可用 | 完整可用 | 完整可用 | 完整可用 | 完整可用 |
| 示意图 | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/e9c5aaac-f42b-4896-919b-dcc42bd31e5a.png) |  |  |  |  | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/f7d25e07-68a4-4180-894e-92a1462f08ce.png) |

Enterprise用户首页按顺序显示: 

1.  4.1核心筛查区域
    
2.  4.5-4.6 Alert, Message center
    
3.  4.3-4.4 Recent Risk Addresses / Transaction
    
4.  4.2 Compliance Hotspots
    

# 3. Home 页面整体架构

Home 可能从不同入口进入，但结构保持一致，仅做轻提示。不再显示welcome弹窗![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/6140e692-1b69-440c-ba46-3557d78e79dc.png)，改为页面顶部的欢迎banner。

*   官网 / 邮件入口 → Home（第一次访问）
    
*   官网搜索 → 详情页 → Home 
    
*   顶部扫描栏多次使用 → Home
    
*   注册完成 → Home，显示
    

新注册用户首次进入首页：

:::
Welcome! You’re now in Trial Mode - enjoy 3 deep scans and unlimited Lite Scans. Start screening now!
:::

访客进入首页：

:::
Welcome to Phalcon Compliance — explore risk insights with 3 deep scans and unlimited Lite Scans. Sign up to get started.
:::

Home 固定由四大区组成：

1.  **顶部：核心搜索区**
    
2.  **中部：可体验模块区（数据模块）**
    
    *   Recent Critical Events
        
    *   Recent screened addresses
        
    *   Recent screened transactions
        
3.  **中部下方：影子模块区（高级能力模块）**
    
    *   In-depth Analytics
        
    *   Custom Risk Engines
        
    *   Notification Channel
        
    *   Label Your Customer
        
    *   On-going Monitoring
        
    *   Blacklist/whitelist
        
4.  **底部：统一 CTA 区（Upgrade / Add credits / Sign Up for free）**
    

# 4. 各模块功能需求

## 可以使用的模块

### 4.1 核心筛查区域 

**模块说明：**

*   将首页入口统一为**一个简单搜索框**。
    
*   用户只需输入「交易哈希 / 地址」，即可在同一处看到**所有支持链上的匹配结果**，点击即可发起合规扫描（screen），完成后自动跳转到详情页。
    
*   为进阶用户保留**批量导入**和**自定义 label / tag** 等高级能力。
    

| **用户类型** | **行为** |
| --- | --- |
| Visitor | 扫描地址/交易可进入lite scan结果页 |
| Free /Starter / Growth/Pro<br>扫描次数充足 | 扫描地址/交易可进入risk detail结果页 |
| Free /Starter / Growth/Pro<br>扫描次数用尽/套餐过期 | 扫描地址/交易可进入lite scan结果页 |

*   首页保留一个主搜索框：
    
    *   占位文案示例：`Search by transaction hash or address`
        
    *   支持输入：区块链地址/交易哈希（Tx Hash）
        
*   输入后行为：
    
    *   系统自动识别输入类型（地址 / 交易），并在**所有支持链**上进行匹配。
        
*   校验与提示：
    
    *   若输入既不符合地址也不符合交易哈希规则，则在搜索框下方显示错误提示：
        
        *   例如：`Invalid address or transaction hash`
            

**搜索结果展示（搜索框下方）**

1.  搜索框下方出现「联想结果列表」，每条结果项包含信息：
    
    *   链图标 + 链名（Tron / Ethereum 等）
        
    *   类型：Address / Transaction
        
    *   主体内容：地址或 Tx Hash（可中间省略部分字符）
        
2.  若在任何链上均无匹配：
    
    *   在搜索框下方显示 `No related address or transaction found on supported chains`
        

#### 1）快速扫描

*   **地址快速扫描**
    
    *   搜索框输入地址，在下拉的匹配结果列表中，直接点选需要扫描的地址，跳转详情页
        
    *   用户匹配到**不支持免费试用的链**时
        
        *   鼠标点击这条👑链所在行，弹出price plan弹窗
            
        *   Eth, Tron（free plan可扫的链）上的地址，希望优先展示在前排![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/64401b1d-dd50-4fb6-9a7e-8aa60de6b9e8.png)
            
*   **交易快速扫描**
    
    *   搜索框输入交易，显示transaction下的所有transfer，必须选择一条transfer扫描。点击transfer跳转详情页
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/b73efac9-0358-4823-ae14-f3b3132b8382.png)
        
    *   如果用户希望选多条transfer扫描，则必须在高级配置窗口配置
        
    *   加载页
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/6493b8e1-8450-4eda-9fd8-6e749ae98578.png)
        

#### 2）Example数据展示

*   点击输入框、尚未输入地址或交易时，输入框下拉栏显示示例地址+交易。
    
*   点击每行示例地址/交易，可以进入示例数据的详情页（触发alert的某次静态数据）不占用扫描次数
    

```plaintext
{Entity Name} · {RiskLabel} 
{Address}
```
```plaintext
 {ActionType}  by {Actor}
{TxHash}
```

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/02d16740-414c-4c19-9b54-9e146f1bf595.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/aa3a2365-8087-4281-9b48-0c17a6a7d7e1.png)

### Example Addresses

*   **Exposure: Scam & Mixer Linked**  
    `0xc5f0e0424052f95418f35da2e6267616ae06cb1d` (ETH)
    
*   **Exposure: Child Abuse Material**   
    `TXCNbqsX3D3bBLAUiARAaFKbT9Yt28NJ4q` (TRON)
    
*   **Entity: Ourbit Deposit Address**  
    `0x5dd0157edfb056ab42d431e587c08bdf168b5318` (ETH)
    

### Example Transaction

*   **Incident: Bybit Exploiter-related**  
    `0xd4da5a15914ab32e788ce77775ab8e28e9720921658497ebd0db69d3e352d734` (ETH)
    

**Address示例数据**

| **Entity Name** | **Risk Label** | **Address** |
| --- | --- | --- |
| 創意私房 (TPbRDK) | Child Abuse Material Related | TXCNbqsX3D3bBLAUiARAaFKbT9Yt28NJ4q |
| Linghang Guarantee | Human Trafficking | TEGG7fN6fET1SMsgebAqFqrb3nZJpZUCnm |
| / | Scam-linked Mixer Exposure | 0xc5f0e0424052f95418f35da2e6267616ae06cb1d |
| / | Bit24.cash: Hot Wallet | TGfVBoUwvVR7dMsNFWYThUjyPKwMV28UpK |

**Transaction示例数据**

| **Action Discription** |  |  | **Tx Hash** |
| --- | --- | --- | --- |
| Risky Deposit to Kucoin |  |  | 18165612bcd6b254d0230d08aef6e510b8d1799275414d96b4b606c555f25325 |
| Rapid Transit $13,950,479.53 in 5 minutes |  |  | 0x7501847c70d2cdcfbb8c6bd3585640f568cd287242b64027e5a829646e084257 |
|  |  |  |  |
| ~~Kyber Network Exploit~~ |  |  | ~~0xde64ab6dccf27bda99fa7efdc2fcc58475859dae4fd95a8da267dc0994ab5971~~ |

#### 3）批量扫描

**CTA位置：**批量上传按钮出现在示例数据的底部，不干扰快速扫描的用户选择地址/交易。

**交互行为：**

*   点击upload csv出现以下弹窗
    
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/94c9678f-1c64-4438-8dd0-2f302d02654d.png)
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/0834565c-9f38-4c86-9529-c6b43e7f4be3.png)
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/ef028b31-76aa-4b3a-a6f4-eb2881bd7007.png)
        
    *   当前账户的剩余扫描次数 **少于** 本次批量上传的address / transfer的总数量时：
        
        *   系统仍会按照 CSV 文件中的顺序，将所有超出扫描额度的行显示在 **\[上传完成\]** 的预览窗口中。
            
        *   对于超出扫描次数的 transfer 行，其 **Status** 字段显示为 **“No credits”**。
            
        *   页面顶部显示提示文案：
            
            *   Credits Limit Reached
                
            *   Your credit balance is too low to view full results.
                
            *   文字链：Top up
                
        *   将弹窗中的 CTA 按钮文案由 **“OK”** 调整为 **“Continue”**。                                    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/6e25e5b5-df46-4947-adac-f75c71d3cbb4.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/3af3c9f8-aa10-4ad9-909d-50e54b0ce0da.png)
            
*   点击Top up 进入pricing plan页面
    
*   点击continue，进入列表页。列表页中status为✅的行会进入地址/交易列表页，status为“No credit”的行不会被加入列表页。
    

\*visitor用户不支持多个transfer扫描，

visitor用户hover到高级配置icon时：显示气泡Sign up to unlock Advanced Config

visitor用户hover到上传csv按钮时：显示气泡Sign up to unlock Bulk Screenings

#### 4）高级配置-扫描

*   **地址高级配置-扫描**
    
    *   1.输入地址，hover到下拉列表某条匹配结果时，在该行右侧出现一个 ⚙️ 图标![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/45ad3e93-d45a-4bad-8fb8-730117f484cd.png)
        
    *   2.点击高级配置按钮，打开该条地址匹配结果对应的高级配置弹窗
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/590b55b6-e578-4b86-95b6-be4cdf39677f.png)
        
*   **交易高级配置-扫描**
    
    *   1.输入交易，在该transaction组的tx hash行右侧提供高级配置按钮![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/2b5c9f84-e245-4903-9841-097ef791986a.png)
        
    *   2.点击高级配置按钮，打开这一条匹配结果对应的高级配置弹窗
        
        *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/cabd0dcd-b9c8-44fe-be77-917dbab030c1.png)
            
    *   3.点击screen进入详情页
        

### 4.2 Compliance Hotspots

**1.1 模块说明**

~~本模块旨在展示平台标签数据库中~~~~**最新收录**~~~~、具有~~~~**最高风险等级**~~~~或~~~~**重大影响**~~~~的地址数据。~~

展示当前市场最热门的搜索地址和平台最新的内容产出，作为用户探索平台内容和功能的入口。

| 列表元素 | 字段构成 | 交互 |
| --- | --- | --- |
| **Trending Searches** (3-5 条) | `[Risk Type Badge]: Address / Tx hash` | 点击列出的地址/交易可以直接进行筛查 |
| **Latest Insights** (2-3 条) | `[Category Tag] Title: {Blog Title}` | 点击 **Read More** 按钮，跳转至官网对应的 Blog 页面 |

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/a742912e-ebb8-4a26-94aa-0aa88439af08.png)

**1.2 展示结构**

**1）Trending Searches 字段**

展示定期手动维护的数据，点击View Report进入结果分享页

| 字段 | 说明 |
| --- | --- |
| **Chain** | 地址所在链 |
| **Type** | address / transaction |
| **Target** | 具体的地址或交易 hash |
| **Risk Type** | 风险类型，如 “Sanctioned” |
| **Risk  Detail** | 风险详细信息，如：“OFAC Sanctioned” |
| **Label** | 地址的 Label |
| **Report Link** | 结果分享报告的链接，用于点击后打开分享页 |

有 label 的示例：\[Sanctioned\] Huione: Deposit (eth，0x1234…5678) 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/1837095f-25e2-4387-83ef-e1cd0c6419f5.png)

**需要展示的数据：**

| **地址标签** | **链** | **地址** |
| --- | --- | --- |
| Huione Group > EXCHANGE | Tron | TQuFSvpct2FeBrKjRh8NDqtGAci2Z15RSa |

**2）Latest Insights 字段**

| 字段 | 说明 |
| --- | --- |
| **Type** | Blog Type |
| **Title** | 标题 |
| **Description** | Description |
| **Time** | 发布时间 |
| **Link** | Blog Link，用于跳转 |

### 4.3 Historical Risk Addresses

本模块作为地址列表页的快速入口，用于展示**最近完成扫描且被标记为非 No Risk 的地址**，并按**最新扫描时间**倒序排列。点击任一地址行可进入该地址的风险详情页。

**展示内容**

*   默认显示最近三条
    
*   字段：
    
    *   Address
        
    *   Risk Level
        
    *   Label Name
        
    *   Last screened time
        
*   点击地址行可进入详情页 （按tier限制遮盖的页面） 
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/e4764d36-d216-46b3-8a40-0c1450f147a3.png)

### 4.4 Historical Risk Transactions

本模块作为交易列表页的快捷入口，展示最近扫描过的风险类型非No Risk的交易。

仅展示最近3次扫描记录，点击View all 可进入交易列表页

*   字段：
    
    *   Tx Hash（或 Label
        
    *   Risk Level
        
    *   Label Name
        
    *   Last screened time
        

### 4.5 Alert Hub

Alert & Messages center 示例显示，保留上版本显示逻辑

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/b35f7b73-9a90-44f1-9d7c-2ff6c47ab645.png)

### 4.6 Message Center

保留上版本显示逻辑

## 面向visitor的引导钩子模块

### 4.7 Configurable Risk Engines

*   展示自定义风险引擎能力，吸引订阅升级
    

说明文案：

> **Create and fine-tune custom risk engines with configurable rules and thresholds.**

🔹CTA 名称

*   预览态（Visitor / Free Trial / Basic）：  
    **Upgrade to configure Risk Engines**
    
*   已解锁（Growth / Pro / Enterprise）：  
    **Manage Risk Engines**
    

CTA 文案（首页预览态）

*   Upgrade to unlock Risk Engines（访客 / Free Trial / Basic）
    

*   View Risk Engines（Growth / Pro / Enterprise）
    

### 4.8 Entity Profiles — Powered by Watchlists

**模块用途：**展示label & tag， blacklist/whitelist高级能力，吸引付费升级

**说明文案：**

*   **Get enriched labels & risk tags** from certified watchlists, plus add your own to match your business needs.
    

*   **Group related addresses into one profile** so your team can see risks, alerts, and customer context in one place for faster AML/CFT reviews.
    

**CTA按钮文案 ：**

*   **面向visitors:** Sign Up to Try Watchlists
    
*   **面向free user：**Subscribe to Custom Watchlists  跳转price plan
    
*   **面向starter:** Upgrade to Custom Watchlists  跳转price plan
    

### 4.9 Auto Monitoring & Alerts

模块用途：展示定时rescreen功能，以及notification channel 的付费功能

Stay ahead of risk with automated checks and instant alerts—anywhere.

*   **Auto screening** for key addresses and transactions.
    

*   **Instant alerts** via email, Telegram, Lark, webhook, and more.
    

**CTA按钮文案**: Enable Automated Monitoring → notification channel 页面

### 4.10 Team Collaboration /Alert Resolution Hub

alert & message center的预览版本，查看团队解决alert的进度

> Notice risk signals and assign alerts to the right team members, ensuring every issue is owned, reviewed, and resolved.

Route, review, and resolve alerts faster — all in one streamlined workspace.

**订阅用户：**显示alert和message center模块

**visitors:** 遮盖的alert和message center模块，模块内部放示例数据。遮罩上方显示说明文字和预览图

:::
**Collaborative Alerts for Faster Risk Resolution**

Notice risk signals and assign alerts to the right team members, ensuring every issue is owned, reviewed, and resolved.

**Sign up** to unlock Team Collaboration.
:::

**CTA文案：**  
Unlock Advanced Workflows  
Upgrade for Full Access  
Try It Free   
Boost Your Team’s Efficiency 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/b35f7b73-9a90-44f1-9d7c-2ff6c47ab645.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/6033f6ad-d4b3-4bbb-8cac-b8cb93695cb5.png)

## 页面底部升级引导CTA

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/eYVOL5jG5kzWzlpz/img/7d7b5565-f027-4e64-be81-a6cd3bae3316.png)