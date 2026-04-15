# \[20251030\] Compliance 支持 Solana

# 背景

Solana 的账户模型与其他链不同。为保证 Phalcon Compliance 的展示逻辑能正确适配 Solana，需要在地址识别和页面展示上做一些调整。

# 详细方案

## Token Account 识别与转换

Solana 采用 **Token Account** 管理代币资产，每个 Token Account 对应一个 **owner account**。  
示例：[Token Accounts of DEVXfoKFTu2D6GNaSVyCjzwYECmfADQhyXC9jZupxKDT](https://solscan.io/account/DEVXfoKFTu2D6GNaSVyCjzwYECmfADQhyXC9jZupxKDT#portfolio)

目前系统在数据入库时仅保留 **owner account** 之间的转账记录，以保持与其他链一致的“地址转账”语义。

因此，在用户查询或交易解析场景中需增加以下逻辑：

*   若输入地址为 **Token Account**，系统需自动识别并转换为对应的 **owner account** 进行展示；
    
*   在解析交易的 transfer 信息时，也需要将 token account 统一转换为 owner account。
    

#### 交易解析

*   在解析交易的所有 `transfer` 信息时，系统需确保输出的地址均为 Owner Account。
    
*   当前解析逻辑已支持此能力，具体实现可参考内部方案（ $\color{#0089FF}{@陈元}$ ）。
    

#### 地址识别

*   查询地址时，通过 Solana RPC 或 Solscan API 获取 `account info`：
    
    *   若结果为 Token Account，则读取其对应的 `owner account`，并以此为准进行展示；
        
    *   若无法确定该账户类型（部分场景下 RPC 与 API 均无结果），则默认展示原始 Token Account 信息，不做强制转换。
        

## 地址（Screen 流程）

在 Screen 流程中，用户在搜索框中输入地址时：

*   若该地址为 Solana 的 Token Account，系统自动识别并转换为对应的 Owner Account；
    
*   搜索结果展示 Owner Account 信息；
    
*   同时在界面提示用户：
    

> “Token account has been transformed to owner account.”

## 交易

### 交易列表页

From 和 To 字段的展示：

*   交易中只有一笔 transfer：
    
    *   From 和 To 展示 Transfer 的 from 和 to
        
*   交易中包含多笔 transfer：
    
    *   From 展示 Signer 地址，若有多个 Signer，展示 第一个和 +n，hover 后展示全部
        
    *   To 地址不展示
        

### 交易详情页

*   删除 Basic Information 模块 Other Information 中的 **Tx Type** 字段；