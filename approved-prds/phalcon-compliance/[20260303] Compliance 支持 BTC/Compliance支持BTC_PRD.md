# \[20260303\] Compliance 支持 BTC

# 背景

当前 Compliance 系统主要支持 EVM 账户模型链。

BTC 采用 UTXO（Unspent Transaction Output）模型，其交易结构与账户模型存在明显差异，因此在支持 BTC 时需要对筛查对象、资金流展示及 Alert 生成逻辑进行适配。

#### UTXO 模型核心特征

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bvjbANLq4B/img/593f671d-a0aa-4563-8fee-0cfee792c958.png)

*   Address 不直接持有余额
    
*   Address 的“余额”由多个 UTXO 组成
    
*   每个 UTXO：
    
    *   由某一笔历史交易的 output 产生
        
    *   在被后续交易消耗前，保持独立、可追溯
        

++👉 这意味着 BTC 的所有资金流动，本质上是 UTXO 的流转与继承++

交易示例：[https://intel.arkm.com/explorer/tx/00d8d624ebd0c993e7b80143f5231dd439bc2b309e51f2f0c3c915986b15af03](https://intel.arkm.com/explorer/tx/00d8d624ebd0c993e7b80143f5231dd439bc2b309e51f2f0c3c915986b15af03)

[https://intel.arkm.com/explorer/tx/28ce7fb6b65018e1a2bb0a8a62fe1f6a8029e10a8c7e57dd0d41c3a3f22cb9a6](https://intel.arkm.com/explorer/tx/28ce7fb6b65018e1a2bb0a8a62fe1f6a8029e10a8c7e57dd0d41c3a3f22cb9a6)

#### BTC 交易的结构特点

*   一笔 BTC 交易可以包含：
    
    *   多个 Input（消耗历史 UTXO）
        
    *   多个 Output（生成新的 UTXO）
        
*   Input 与 Output 之间 **不存在链上原生的一一对应关系**
    
*   交易中通常包含：
    
    *   实际转账给对方的 output
        
    *   找零（Change）output（返回给发送方控制的钱包）
        

### MetaSleuth 的做法

*   MetaSleuth 在展示资金流图时，将 BTC 交易 **抽象为 Address → Address 的资金流边**
    

*   这种抽象有利于：
    
    *   快速理解资金关系
        
    *   和其他链的展示逻辑统一
        

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/1759b60d-6020-432c-b8a2-a9f7e569d6a8.png)

缺点：

*   丢失原始 UTXO 的 input / output 结构
    
*   边数量从 `N + M` 膨胀为 `N × M`
    

# KYT & KYA

#### KYA 场景

用户输入一个 BTC 地址 -> 系统分析该地址历史上接收过的所有 UTXO -> 并对这些 UTXO 的来源路径进行多跳追踪 -> 从而判断该地址是否曾与高风险来源产生资金关联。

#### KYT 场景

在 BTC 中相比“扫交易/transfer”，更像是“扫一笔资金”

> 怎么明确一笔资金？

> 参考 下面 Elliptic 的文档，有如下推测

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/67de76a4-8b66-4d07-80b8-8085872e34bf.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/9a974fe9-6c17-495f-ae71-4ea53afd7760.png)

### 方案一：严格沿着 UTXO 追踪

**思路：**

*   每一笔 UTXO 单独追踪
    
*   风险严格继承，不做聚合
    

**问题示例：**

> 一个地址 99 BTC 来自 Sanctioned  
发出去的 1 BTC 来自“干净”UTXO  
→ 我们是否可以认为接收 1 BTC 的地址是“无风险”？

### 方案二：基于地址整体 Exposure

**思路：**

（和当前 Compliance 其他链基本一致）

*   地址作为风险主体
    
*   风险基于：
    
    *   历史 UTXO 的聚合 exposure
        
    *   金额 / 占比 / 路径
        

# 详细方案

在 Compliance 中新增 BTC 支持时遵循原则：

*   尽量兼容现有框架、模块和流程
    
*   不破坏用户已经养成的使用习惯，适配 BTC 的 UTXO 模型特点
    

## 通用规范

#### 外部跳转 BTC 浏览器

平台中 BTC 地址/交易跳转外部浏览器：

*   地址示例：[https://mempool.space/address/bc1qetycze920ljdcd0ec9hpt4hqyzlm3nzr4y9dak](https://mempool.space/address/bc1qetycze920ljdcd0ec9hpt4hqyzlm3nzr4y9dak)
    
*   交易示例：[https://mempool.space/tx/7a8ef9109cccae31447581efae0d7bf68cadcb2af55b0a4f71e030931e29f359](https://mempool.space/tx/7a8ef9109cccae31447581efae0d7bf68cadcb2af55b0a4f71e030931e29f359)
    

#### Coinbase 交易展示

Bitcoin 中有一类特殊的区块奖励交易，如：d2f4d12b31b47923cc317435e5dd6f4d13198cfc766d8c2020a0bfe1d7bc1e0b

对于这类交易，统一将 Input（From）地址展示为 “**Block Reward**”，不展示地址且无 Hover 效果。

## 界面搜索

界面上用户通过搜索框触发 BTC 风险筛查。

#### 地址

BTC 地址搜索流程与现有地址筛查流程保持一致：

用户输入地址 ->  系统识别为 BTC 地址 -> 查询是否存在交易 -> 展示搜索结果：链 + 地址 + Label +  tag -> 用户点击地址 -> 自动触发 Address Screening -> 跳转地址详情页

#### 交易

*   若为单 output 结构:
    
    *   用户输入交易 hash ->  展示链 + 交易 hash -> 用户点击交易 -> 筛查并跳转结果页![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/888a469a-94e3-4d96-8e0e-6fc303386a28.png)
        
*   多 Output 交易：
    
    *   **方案一：**
        
        *   用户输入交易 hash -> 展示链 + 交易 hash + input 地址 、 output 地址列表 -> 用户选择其中的一个 output 
            
        *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/804acab8-9903-4cd9-88d7-35fe0997ee18.png)
            
    
    *   **方案二：**
        
        *   用户输入交易 hash -> 展示链 + 交易 hash + output 地址列表 -> 用户选择其中的一个 output 地址进行筛查
            
        *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/3bfafa82-9509-47a3-9e7c-d17cc0a7c574.png)或![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/e812c5f0-ecfe-47ab-9684-e55ad778feda.png)
            
    *   在 Advanced Analyze 模式下：
        
        *   用户可以选择多个 Output 地址
            
        *   但 Direction 只能选择一个
            

## 筛查

BTC 筛查复用现有 **Risk Engine 规则体系**，无需新增规则类型。

#### Alert 生成逻辑

*   地址（与其他链一致）
    
    *   1 Address + 1 Rule （Engine） → 1 Alert
        
*   交易：
    
    *   BTC 的 Alert 以 Output 为最小粒度生成：
        
    *   1 Tx Hash + 1 Output Address + 1 Rule （Engine） → 1 Alert
        

说明：

*   Output 通过 output address 唯一标识
    
*   考虑到当前筛查的对象都是地址，所以将 output 按照地址进行聚合
    

#### Interaction Risk 筛查

*   地址：
    
    *   对所有接收过的 input 的来源进行溯源
        
    *   对所有 output 的去向进行追踪
        
*   交易：根据用户的选择：
    
    *   当选择 **Deposit** 时：
        
        *   对所有 Inputs 进行溯源分析
            
    *   当选择 **Withdrawal** 时：
        
        *   对选择的这一个 Output 进行去向分析
            
    *   当选择 **Both** 时：
        
        *   对交易的 Inputs 进行溯源，并对所选的 Output 进行追踪
            
    *   交易 Value：
        
        *   所选择的 Output 对应的 Value
            

#### Behavior Risk 筛查

*   地址：
    
    *   地址参与的每一笔交易即为一次行为事件
        
    *   地址在同一交易中的 所有 Input / Output 金额合并后计算
        
*   交易：
    
    *   以 Output 为最小分析单位
        
    *   根据用户选择的 Output 和 Direction 进行计算
        

## 交易列表页

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/155d6eeb-a2b7-4957-84ea-41079e1f88a9.png)

单 Output 交易，不支持点击展开子行：

*   单 Input：  
    `From` 字段展示该 Input 地址
    

*   多 Input：  
    `From` 字段展示 {第一个 Input 地址} +N（N 为省略的 Input 数量）。  
    用户可通过 展开或 hover 查看完整 Input 地址列表（交互上需避免与现有地址 hover 信息产生交互冲突）。
    

多 Output 交易：

*   `From` 字段展示逻辑与 单 Output 交易一致。
    
*   `To` 字段展示： -  
    

*   支持展开交易行，展开后每个子行展示：
    
    *   Output Index
        
    *   From 字段不展示
        
    *   To 字段展示对应的 Output 地址
        
    *   其他字段和其他链一致
        

## 地址/交易详情页

### 地址详情页

除 Transfers 模块外，其他模块和字段均不需要改动调整。

#### Transfers 模块

名称修改：Transfers 改成 Transactions

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/02b71572-5507-415b-ae79-d58c49baea03.png)

展示字段：

| 字段名 | 内容说明 |
| --- | --- |
| From | 展示交易 Input 地址摘要。<br>*   **不包含 Target 地址：**  <br>    格式：`第一个 Input 地址 (+其余 Input 地址数量)`  <br>    示例：`3DcwvCEhmRABvMW5iYJLzipaNSwQyBH2Ht (+2)`<br>    <br>*   **包含 Target 地址：**  <br>    格式：`Target Address (+其余 Input 地址数量)`  <br>    示例：`bc1qxyz... 0.35 (+2)`<br>    <br>Target 地址使用不同颜色高亮（不可点击）。 |
| To | 展示规则与 **Inputs 相同**。 |
| Amount | 表示 Target 地址在该交易中的 **BTC 净变化**。<br>*   减少：`-amount`（红色）<br>    <br>*   增加：`+amount`（绿色）<br>    <br>[示例 Tx](https://mempool.space/zh/tx/c89dbfbb917bea494225e42fa91efaef161fd324223859344c41576f3c790b2a) 中，bc1q3ukl...pqld0jwjl 的净变化是：<br>\-‎0.00368154 + 0.00319534 = -0.0004862 BTC |
| Tx Hash | 展示交易 Hash。 |
| Time | 交易发生时间 |
| Screen | 点击后弹出 **Transaction Detail** 弹窗，展示完整交易信息。<br>用户可在弹窗中：<br>*   选择需要筛查的 **Output**<br>    <br>*   选择 **Scan Direction（Deposit / Withdrawal）**<br>    <br>随后触发 **Transaction Screening**。 |

Note： 可以同步将其他链的 Transfers 列表也改一下，展示 From，To，Amount，Tx Hash，Time

### 交易详情页

#### Basic Information

展示如下字段：

| 字段名 | 内容说明 |
| --- | --- |
| Tx Time | 交易时间 |
| Label | label，默认无，用户可以添加 |
| Customer | 用户可以绑定 |
| Block | Block 数量 |
| Tx Fee | Tx Fee |

#### Risk Summary 模块

和当前保持一致

#### Risk Overview  模块

所有 Transfer No.X 的写法都需要改一下，改为 Output Address No.X。

Sender address  改为 Input address

Receiver address 改为 Output address

#### Token Transfers 模块

模块名改成：Transaction Inputs & Outputs

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/f6ef05f2-70e6-45de-beba-0f798caf79f6.png)

用两个表格分别展示 Input Addresses 列表和 Output Address 列表。

Input Addresses 列表包含字段：分页展示，每页最多 5 个

*   Address
    
*   Amount
    
*   Token
    
*   Value(USD)
    

Output Addresses 列表包含字段：

*   Index
    
*   Risk Level
    
*   Unresolved Alerts
    
*   Address
    
*   Screen Direction
    
*   Amount
    
*   Token
    
*   Value (USD)
    
*   Label
    
*   Customer
    
*   Screening Time
    

Alerts 和 Audit Logs 模块和现在保持一致，其中 Transfer No.X 的写法也要改成 Output Address No.X， 

#### Output （Transfer） 详情页

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/240df1e5-7cfa-44f2-bfbe-ab6452d57ff7.png)

Header 部分展示：

Output Address No.1  + \[对应的 output 地址\]

## Alert 详情页

主要是 Behavior 相关详情页中，涉及 Transfer 展示相关的需要考虑是否要调整。

### Address - Transit address

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/931a869c-1f35-48d3-a6c7-2dc61f557d89.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/8621c5d4-1a97-4863-8ec6-fc7231bdbe0e.png)

可以直接适配：展示每笔交易中与目标地址相关的所有 Inputs 和 Outputs，并根据该地址在该交易中的总流入与总流出聚合计算最终的 Amount / Value。

### Address - High Frequency

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/2ded3967-8468-43da-a446-7903b8b40ccc.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/1bae1d17-12d8-4974-8808-c8bfb4e2ec29.png)

同上，可以兼容

### Address - Large Transfer

同上，Alert Details 中表格直接按照上面弹窗的格式展示

### Transaction - Large Transfer

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/e9b3fbd1-4cd6-44f2-b62d-9636b8e9db3a.png)

*   列出所有 Input，默认前 5 个，更多的可以默认隐藏 （+N），用户点击后展开
    
*   Triggered Output 展示当前 Alert 关联的 Output 信息
    

触发逻辑也是看当前筛查的 Output 金额是否不小于用户配置的金额阈值。

### Transaction - Rapid Transit

#####  筛查逻辑

对象：

*   Output 地址 B
    
*   Direction = Deposit
    

步骤：

1.  Output Value 是否不小于金额阈值
    
2.  获取当前交易 TX 的所有 Inputs
    
3.  查询对应的产生每个 Input 的交易 TXi
    
4.  若所有 TXi 与当前交易 TX 的时间差均小于用户设定的时间窗口 t，则触发 Rapid Transit Alert。
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/50d37957-d169-48ce-aaa2-257ea985c210.png)

Alert Details 的展示样式可沿用当前的展示结构。

从左到右分别展示：

*   节点 1：
    
    *    TXi 交易节点
        
    *   展示最早的一笔 TXi 的交易 Hash (+N) ，其中 N 为省略的 TXi 的数量
        
*   边 1 - 2：
    
    *   展示 Inputs BTC 总和 + USD Value
        
    *   展示时间：TXi 的最早时间 ～ TXi 的最晚时间
        
*   节点 2：
    
    *   若交易包含多个 Input addresses，仅展示第一个地址，并在其后以 “+N” 形式标注其余数量；用户通过 hover 或点击 可查看完整的 Input 地址列表。
        
    *   节点上展示的时间为 最短的时间差。
        
*   边 2-3：
    
    *   展示对应 Output 的 BTC 总和 + USD Value
        
    *   展示当前交易 Hash
        
    *   展示当前交易时间
        
*   节点 3:
    
    *   所选的 Output 地址
        

# API 

增加 chainId = -1 代表 BTC 链

## 地址相关

地址相关的接口都不需要有太多的调整

## 交易相关

1.  Screen a single transaction
    
    对于 BTC 交易，transferIndex 字段无效，可以忽略 
    
2.  Get transfers of a transaction
    

# 参考

## Elliptic 

#### 公开的污点算法

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/b3292d58-fb3c-4109-9431-b30f772b5fa9.png)

不考虑 UTXO，看地址整体资金的 Exposure。

#### KYT API 文档

KYT 扫描，要指定：chain、hash、output\_address / output\_indicies 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/mPdnpZwv0eEgOw98/img/5ec0a3db-8598-4090-9fa3-888afb76879f.png)

## Chainalysis

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4nyeZmzL91pnLb/img/158bf98b-2d35-480d-b6eb-34f858c6f088.png)

看起来也是 Hash + output address 确定 transfer