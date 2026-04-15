# Address& Transaction Label → Note

# 现状

当前 Compliance 系统中，地址信息包含两类标识：

*   系统 Label（来自标签库）
    
*   用户自定义 Label（用户编辑）
    

随着产品使用深入，现有设计逐渐暴露出理解成本高、使用率低的问题，同时也影响了该功能的商业价值转化。

同时，交易也有用户自定义 Label （用户编辑），本次需一并修改。

*   交易中只有一笔 transfer：仅可对交易自身添加 Label
    
*   交易有多笔 transfer：  可对交易和每笔 transfer 分别添加 label
    

### 当前逻辑

| 类型 | 来源 | 可编辑 | 展示 |
| --- | --- | --- | --- |
| System Label | 标签库 | ❌ | 与用户 Label 混合 |
| User Label | 用户输入 | ✅ | 覆盖 System Label |

若地址有任意 label，展示时会默认展示 label 而不是地址，hover 后可看到 label 和地址信息，如图：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQ5bWxW8yvlxo/img/24679e62-25b8-4126-9bd8-d6131608596c.png)

### 编辑入口

*   地址列表页，hover 到地址上，tips 中可以修改 label
    
    *   地址有 Label 时：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQ5bWxW8yvlxo/img/5bf0a069-bce7-4fd8-b36a-8c693df7ef0c.png)
        
    *   地址无 label 时：  
        ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/dbaa7b97-3fea-4a2e-8a41-5a7f9a32d324.png)
        
*   地址详情页
    
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/a2da892a-4922-44f1-a5a4-285917e9ad56.png)
        
*   交易列表页
    
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/b68f10fc-b944-481f-b524-b24aae8b9abe.png)
        
*   交易详情页
    
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/55096f63-3931-4bef-9046-b6e6c7e022ff.png)
        
    *   ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/dc42df9c-b733-4d9b-ba47-dbbce61d7ee2.png)
        

### 用户 label 列表

当前 label 添加数量为付费功能， 免费用户可以添加 3 个，不同付费 plan 的用户有不同的 label 数量。用户可以统一在一个位置查看和管理其所有的 label。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/3M0OzeZLdPb0Yqze/img/0ad13bfa-a310-4f71-ab64-01c75ea605b9.png)

# 问题

#### 概念混淆

*   用户无法区分：
    
    *   系统标签 vs 用户自定义标签
        
*   存在误解：
    

> 用户以为自定义 Label 会进入平台标签库，被其他用户看到

#### 信息覆盖

*   用户添加 Label 后：
    
    *   系统 Label 被隐藏
        
*   导致：
    
    *   原始风险信息丢失
        
    *   判断依据不完整
        

#### 使用门槛高

*   编辑入口较隐蔽
    
*   用户不容易发现该功能
    

# 目标

### 概念重构

将：

> User Label → Note

明确区分：

| 类型 | 名称 | 说明 |
| --- | --- | --- |
| 系统标签 | Label | 平台标签库返回 |
| 用户备注 | Note | 用户私有备注 |

#### 提升信息表达清晰度

*   Label 与 Note 不再互相覆盖
    
*   同时展示
    

#### 提升 Note 使用率

*   提供更清晰入口
    
*   强化使用场景
    

### 展示逻辑

#### 地址列表页

*   Note 与 Label 同时展示
    
*   不互相覆盖
    

#### 地址详情页

Label： 

*   保持原位置
    
*   不可编辑
    

:::
交易 Note 修改为只能给交易本身添加，不能给 Transfer 分别添加自己的 Note 
:::

#### 其他

*   其他地方的 “Label " 字段表述也统一修改为 Note
    
    *   pricing plan
        
    *   data management 的 label 列表
        
    *   audit logs 中 update label 相关
        
    *   API 新增 Note 字段