# \[20260326\] Transaction 列表导出

#  需求背景

用户希望将交易筛查结果导出为报表，用于复核、留档和后续分析。报表需包含资金流入/流出地址、交易金额及涉风险金额、交易时间、风险信息以及关联商户 ID 等关键字段，并支持按时间范围筛选。

当前交易列表已覆盖上述主要信息，但不支持导出能力，因此需要新增导出功能。

注：当前 Risk Summary 未做结构化存储，本期仅支持导出 Risk Level，后续再补充主要风险原因等字段。

# 方案

## 交互

在表头增加 Export 按钮

—> 点击后弹窗：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/NpQlK5j514eQ4qDv/img/46151e4a-d585-41aa-b61d-68931a05302d.png)

用户可以自定义：

*   时区
    
*   Tx Date Range
    
    *   导出时间范围基于 Transaction Time（交易发生时间）
        

#### 筛选

导出数据需继承当前列表已应用的筛选条件。(Tx Time 除外)

当用户在列表中使用 **Tx Time 作为筛选条件**时：

*   导出弹窗中的 **Tx Date Range** 默认与当前筛选条件保持一致
    
*   用户仍可在弹窗中手动修改时间范围
    

> 说明：导出时间范围仅作为默认继承，不做强绑定

当用户在列表中应用了除 Tx Time 外的筛选条件（如 Chain、Risk Level 等）时，在导出弹窗中展示当前筛选状态提示：

*   当仅有 **1 个筛选条件**时：
    
    > This export has **{Filter Name}** filter applied
    
    筛选项名称：
    
    *   chain
        
    *   risk level
        
    *   label
        
    *   assets
        
    *   tx time
        
    *   last screening time
        
    *   from 
        
    *   to
        
*   当筛选条件 **≥ 2 个**时：
    

> This export has **{N} filters applied**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/NpQlK5j514eQ4qDv/img/8ddc7ebc-b70b-4d84-bb37-85f7abfcd811.png)

#### 导出

用户点击导出后：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/NpQlK5j514eQ4qDv/img/d69f7e63-26f4-4d2a-87ff-49a2946cd6e4.png)

考虑到导出时间可能会比较长，当导出时间超过 15 s 时变为异步任务，告知用户准备好后会通过邮件发送。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/NpQlK5j514eQ4qDv/img/e2a84817-de52-4d8a-a3c6-3ff9013f0e51.png)

邮件：

:::
**Your transaction export is ready**

Hi,

Your requested transaction report is now available.

You can download the report using the link below:

{{link}}

For security reasons, this link will expire in {{expiration\_time}}.

Best regards,  
Phalcon Compliance Team
:::

## 导出字段

本次导出以 **Transfer 维度**进行：

*   一笔交易中若包含多个 transfer，则导出为多行
    
*   每一行对应一个 transfer
    

导出字段：

| 字段 | 说明 |
| --- | --- |
| Chain | 所属链 |
| Tx Hash | 交易唯一标识 |
| Transfer Index | 交易内 transfer 序号（如果交易中只有一笔 trasnfer，这里是 0） |
| Risk Level | 风险等级 |
| Screen Direction | 筛查方向 |
| Last Screening Time | 最近筛查时间 |
| Value (USD) | 折算 USD |
| Token | Token 地址 |
| Amount | Token 数量 |
| From Address | 资金流出地址 |
| From Label | 流出地址的 label |
| To Address | 资金流入地址 |
| To Label | 流入地址的 label |
| Transaction Time | 交易发生时间（UTC 或用户选定时区） |
| Unresolved Alerts | 未处理告警数 |
| Customer | 关联的 customer id |
| Label | 用户添加的 label |
| Added Time | 添加时间 |