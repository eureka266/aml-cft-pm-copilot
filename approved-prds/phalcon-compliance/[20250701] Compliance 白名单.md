# \[20250701\] Compliance 白名单

# 背景

在当前 Compliance APP 中，所有用户导入的地址和交易，系统会自动匹配所有 Active Risk Engine。若命中规则，即生成对应 Alert，并基于所有现有 Alert 综合计算该地址或交易的 Risk Level。

然而，实际业务中经常存在以下**特殊场景**：

*   用户（如 Vitalik 地址）出于好奇或测试，与 Tornado.Cash 或其他隐私服务地址交互；
    
*   客户后续提供可信证据，证明原先的风险判断为误报；
    
*   地址曾被钓鱼、攻击或投毒，与高风险地址发生交互；
    
*   其他经合规团队确认需要豁免的场景（如内部控制钱包、合作方官方地址）
    

**当前主要痛点**：

*   Risk Level 是系统结合所有 Alert 自动计算的，无法手动干预。
    
*   缺乏可信地址的放行机制，无法在规则层做单独豁免。
    

### 功能目标

为解决上述痛点，需引入 **地址白名单功能**，以实现：

*   白名单地址**强制豁免风险**：
    
    *   地址筛查：Risk Level 固定为 “**No Risk**”，不触发任何 Alert；
        
    *   交易筛查：
        
        *   若`from`为白名单地址，仅豁免`from`方向风险，`to`方向正常扫描；
            
        *   若`to`为白名单地址，仅豁免`to`方向风险，`from`方向正常扫描；
            
        *   若`from`和`to`均为白名单地址，整笔交易豁免风险。
            
*   管理能力：支持单个 / 批量增删、状态互斥校验、全流程审计。
    

#### 黑名单逻辑明确：

同理，对于黑名单功能：

*   地址筛查时：Risk Level 固定为 Critical Risk，不产生 Alert。
    
*   交易筛查时：黑名单地址参与的交易，若筛查指定方向的地址为黑名单地址，则交易自动为 Critical，不产生 Alert。
    
*   当检测地址/交易是否对黑名单地址有 Direct Exposure 时，需要**产生 Alert**。![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/KM7qeobgyVz12lpj/img/787371be-ae99-41d1-9031-f4178fba7cf7.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/KM7qeobgyVz12lpj/img/57f30e3f-9121-4fe7-92f2-f8371705b36c.png)
    

# 需求概述

## 功能概述

*   新增 **白名单地址管理能力**，支持单个/批量添加、查看、移除
    
*   对白名单中的地址或包含白名单地址的交易，自动跳过风险扫描或部分方向扫描
    
*   与现有黑名单逻辑保持互斥，确保名单唯一性
    
*   所有操作可追溯 & 审计
    

## 使用场景

| 场景 | 用户操作 |
| --- | --- |
| 误报 Alert 涉及的地址需放行 | 从 Alert 跳转到地址详情页一键加入白名单 |
| 客户想批量上传可信地址（如合作方、官方地址） | 在白名单管理页或通过 API 批量导入未筛查过的地址 |
| 撤销白名单状态 | 从白名单移除，地址重新按正常流程扫描 |

# 详细功能说明

## 地址加入白名单

### 入口设计

*   **地址列表页 / 详情页**：
    
    *   新增 “Manage List” 下拉按钮，未在名单中时显示 “Add to Whitelist”；已在白名单时显示 “Remove from Whitelist”（与黑名单按钮综合考虑，互斥显示）。
        
*   **白名单管理页**：
    
    *   入口：在 “Screening Settings” 下新增 “Whitelist Management” 模块。
        
    *   新增 “Add Address to Whitelist” 按钮，支持：
        
        *   单个地址输入（需选择所属链，如 ETH/BSC）；
            
        *   批量导入（CSV 格式，支持字段：地址、链标识、加入原因）。
            

CSV 模版：

[请至钉钉文档查看附件《template.csv》](https://alidocs.dingtalk.com/i/nodes/93NwLYZXWyqAB0poHvonbroGWkyEqBQm?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mdo7gy3innphb8y0mm)

### 加入白名单流程

*   **校验逻辑**：
    
    *   地址格式校验：需符合对应链的地址规则（如以太坊 42 位字符），支持多链；
        
    *   互斥校验：若地址已在黑名单，弹窗提示 “Address is in Blacklist. Please remove it first.”。
        
*   **操作确认**：
    
    *   必填项：“Reason for Whitelisting”
        
    *   弹窗提示：“Adding this address to whitelist will fix Risk Level to No Risk”，确认后提交。
        
*   **成功反馈**：
    
    *   提示 “Added to whitelist successfully”，并引导用户跳转至白名单管理页（刷新状态）。
        

## 白名单管理

### 管理页面

在 Screening Settings 中新增“Whitelist Management”模块，展示白名单地址列表。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/KM7qeobgyVz12lpj/img/62c5679e-1ca4-46b5-b58c-6ea1201f2bba.png)

| 字段 | 描述 |
| --- | --- |
| Address | 链图标 + 地址 |
| Reason | 用户填写的加入原因 |
| Add Date | 加入日期 |
| Added By | 操作用户邮箱（若来源是 API，则显示 `API - {API name}`） |
| Action | \[Remove\] 按钮 |

*   支持搜索：按地址搜索
    

*   支持单个新增、CSV 批量导入。
    

#### 移出白名单

*   点击 “Remove” 按钮后，弹窗二次确认：
    
    *   提示：“I understand that this action will remove the whitelisted status and update the risk level for this address.”；
        
    *   需填写移除原因（必填，如 “地址不再可信”“误操作添加”）；
        

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/KM7qeobgyVz12lpj/img/f2d91f19-b295-4ddb-a458-7b957e8d5c66.png)

## 地址 & 交易筛查逻辑

### 地址筛查

#### 地址详情页

*   状态展示：
    
    *   若地址在白名单，显示“Whitelist Information”：加入原因、加入时间、操作人。
        
*   筛查放行：
    
    *   白名单地址自动禁用自动重新扫描（re-screening）。
        

*   手动触发扫描时，Risk Level 固定为 No Risk，不触发任何 Risk Engine，无新 Alert 生成。
    

### 交易筛查

*   交易详情页中，白名单地址旁显示 “白名单” 标识
    
*   筛查规则，适用于 Exposure 和 Behavior 类型的风险检测。
    

| 筛查方向 | 白名单地址参与场景 | 筛查逻辑 |
| --- | --- | --- |
| Deposit | from 地址若为白名单 | 跳过扫描，判定 `No Risk`。否则正常筛查。 |
| Withdrawal | to 地址若为白名单 | 跳过扫描，判定 `No Risk`。否则正常筛查。 |
| Both | from 或 to 若为白名单 | 对应方向跳过，若两个方向都是白名单时，才为 No Risk。 |

*   **风险判定**：豁免后剩余方向无风险则交易为 No Risk；未豁免方向有风险则按正常规则判定。
    

## 筛查和 Alert \[7.22 新增\]

考虑到以下情况，需要明确加入/移除黑白名单时筛查、alert 相关逻辑

*   未导入地址被加入黑名单，后被移出黑名单，是否要重新筛查
    
*   已有 Alert 的地址被加入/移除白名单时
    

| Action | 筛查 | Alert |
| --- | --- | --- |
| 地址加入白名单 | 地址：No Risk，不筛查<br>交易：不回扫 | 地址：已经产生的 Alert 更新 status 为 Expired<br>交易：不处理 |
| 地址移出白名单 | 地址：系统自动筛查，重新评估 Risk Level<br>交易：不回扫 | 地址：根据筛查的结果处理 Alert<br>交易：不处理 |
| 地址加入黑名单 | 地址：Critical Risk，不筛查<br>交易：不回扫 | 地址和交易均不处理 |
| 地址移出黑名单 | 地址：系统自动筛查<br>交易：不回扫 | 地址：根据筛查的结果处理 Alert<br>交易：不处理 |

## API  \[7.22 新增\]

### 地址

screen result / address detail 结果中要包含标识当前地址是否为黑/白名单的字段

```json
{
  ...
  "isBlacklisted": false,
  "blacklistedInfo": "",
  "isWhitelisted": true,
  "whitelistedInfo": "",
  ...
}
```

### 交易

screen result / transaction detail 中也要包含 from / to 地址是否为黑/白名单的字段

```json
{
  ...
  "fromIsBlacklisted": false,
  "fromIsWhitelisted": true,
  "toIsBlacklisted": true,
  "toIsWhitelisted": false,
  ...
}
```

### 白名单管理 API

增加以下两个 API 接口：

*   加入白名单
    
*   移出白名单
    

接口路径和字段都参考黑名单 API

## 系统 Logs 和 Audit Logs 

需要添加白名单相关的 Audit Logs，同时，由于以下原因，需要对系统 logs 和 audit logs 进行调整：

*   需要体现出地址/交易筛查，由于白名单/黑名单才有了最终 No Risk / Critical Risk 的结果
    
*   允许将未导入的地址加到白名单，需要在系统 Logs 记录这一操作。
    

### Audit Logs

| 模块 | 事件 | 内容 |
| --- | --- | --- |
| 地址 | 地址筛查，因在黑名单中而跳过筛查 | Address Screened<br>\[自动记录时间\]<br>Screen Source: {API//Manual}<br>操作人：（分不同的情况展示不同的内容）<br>\- 通过平台界面导入或点击“Re-screen”的，展示: {操作用户的邮箱}<br>\- API 执行的 Screen，展示：API - {API name}<br>Result：Skipped - Due to Blacklist |
|  | 地址筛查，因在白名单中而跳过筛查 | Address Screened<br>\[自动记录时间\]<br>Screen Source: {API//Manual}<br>操作人：（分不同的情况展示不同的内容）<br>\- 通过平台界面导入或点击“Re-screen”的，展示: {操作用户的邮箱}<br>\- API 执行的 Screen，展示：API - {API name}<br>Result：Skipped - Due to Whitelist |
|  | 地址被加入白名单 | 标题：Address is Whitelisted<br>时间：\[自动记录时间\]<br>内容：<br>Whitelisted due to: {用户填写的原因}<br>操作人：<br>{操作用户的邮箱} |
|  | 地址被移出白名单 | 标题：Address Remove from Whitelist<br>时间：\[自动记录时间\]<br>内容：<br>Removed from whitelist due to: {用户填写的移除原因}<br>操作人：<br>{操作用户的邮箱} |
| 交易 | 交易筛查，指定单边方向，指定方向的地址为白名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Deposit / Withdrawal<br>Screen Source: Manual<br>Result: Skipped - Due to Whitelist |
|  | 交易筛查，指定方向为 Both，其中一个方向的地址为白名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Both<br>Screen Source: Manual<br>Result: Deposit / Whithdrawal Skipped due to Whitelist |
|  | 交易筛查，指定方向为 Both，其中两个方向的地址为白名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Both<br>Screen Source: Manual<br>Result: Skipped - Due to Whitelist |
|  | 交易筛查，指定单边方向，指定方向的地址为黑名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Deposit / Withdrawal<br>Screen Source: Manual<br>Result: Skipped - Due to Blacklist |
|  | 交易筛查，指定方向为 Both，其中任意方向地址为黑名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Both<br>Screen Source: Manual<br>Result: Skipped - Due to Blacklist |

2025.12.1 更新：

| 交易筛查，指定方向为 Both，其中一个方向地址为黑名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Both<br>Screen Source: Manual<br>Result: Deposit / Whithdrawal Skipped due to Whitelist |
| --- | --- |
| 交易筛查，指定方向为 Both，两个方向地址均为黑名单地址 | Transaction Screened<br>\[自动记录时间\]<br>\[Transfer Index\]  <br>Direction: Both<br>Screen Source: Manual<br>Result: Skipped - Due to Blacklist |

### 系统 Logs

**阶段一**：在系统 Logs 中增加黑/白名单管理相关的内容。

| Category | Event | 内容 |
| --- | --- | --- |
| Blacklist/Whitelist Management | Add to Blacklist | added 1 address(es) to blacklist |
|  | Remove from Blacklist | removed 1 address(es) from blacklist |
| Blacklist/Whitelist Management | Add to Whitelist | added 1 address(es) to whitelist |
|  | Remove from Whitelist | removed 1 address(es) from whitelist |

**阶段二**：会优化 Logs 展示，将系统所有的 Audit Logs 汇总到一个界面展示。

(本次不做，待 PRD 详细梳理。)

可参考：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/KM7qeobgyVz12lpj/img/946bd009-d04a-40ce-a13b-168f6d96ceee.png)

## 黑名单逻辑明确（与白名单对齐）

#### 地址筛查

*   风险等级：固定为 “高风险（Critical Risk）”，不产生 Alert。
    
*   扫描机制：Disable Auto Re-screening，用户手动重新筛查时 Risk Level 仍然是 Critical Risk。
    

#### 交易筛查

*   风险判定：
    

| 筛查方向 | 黑名单地址参与场景 | 筛查逻辑 |
| --- | --- | --- |
| Deposit | from 地址若为黑名单 | 判定 `Critical Risk`。否则正常筛查。 |
| Withdrawal | to 地址若为黑名单 | 判定 `Critical Risk`。否则正常筛查。 |
| Both | from 或 to 若为黑名单 | 有一个方向地址为黑名单，则为 `Critical Risk`。 |