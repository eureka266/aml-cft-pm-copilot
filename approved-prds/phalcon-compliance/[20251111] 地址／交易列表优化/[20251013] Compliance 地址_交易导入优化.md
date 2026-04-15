# \[20251013\] Compliance 地址/交易导入优化

# 现状与问题

1.   概念理解困难
    

*   当前「导入」概念不直观。用户难以理解“导入地址/交易”与“筛查地址/交易”的区别。
    

1.  操作流程繁琐
    

*   导入 + 筛查的整体流程有太多确认和点击的步骤 （至少点击 5 次）
    

1.   信息展示与操作位置不合理
    

*   在交易导入弹窗中，Direction、Customer 等关键信息位于右方，需用户滚动才能看到。
    
*   其中 Direction 对交易筛查逻辑非常关键，却未被突出展示，导致用户可能遗漏或误选。
    

1.   引导与交互反馈不足
    

*   重复导入失败的提示文案不合理。  
    既然系统支持 **Re-screen**，则应在检测到重复导入时直接提示并允许用户选择 **Rescreen**，而非报错。
    

1.   弹窗设计不合理
    

*   地址导入弹窗目前分为 **Single Address** 与 **Upload CSV** 两个入口。
    
*   在 **Single Address** 模式中，用户搜索 EVM 地址后会展示该地址的多条活跃链，并允许多选添加。  
    然而此模式下仍可继续 “Add Address → 再次搜索”，与 “Single Address” 的概念矛盾，设计不统一。
    

# 优化目标

*   **统一用户心智**：明确核心操作是「筛查（Screen）」而非「导入」。
    

*   **简化流程**：减少不必要的确认环节，统一地址与交易的交互逻辑。
    

*   **提升关键信息可见性**：在确认弹窗中优先展示 Direction、Customer 等关键字段。
    

*   **优化重复导入逻辑**：改为支持 Re-screen 操作，提升引导体验。
    

*   **统一弹窗逻辑**：区分单次与批量操作模式，避免概念冲突。
    
*   **统一搜索操作**：在正式使用界面中也提供和试用同样的搜索框搜索交互（考虑在 Dashboard 保留搜索框？）
    

# 优化方案

## 单地址筛查流程优化

#### 优化前流程

搜索 → 选择链 → Add → 确认 Label / Customer → Import → 二次确认 + Screening 状态提示  → 跳转地址列表页

#### 优化后流程

搜索 → 选择链 → 确认 Label / Customer / Tags → **直接发起 Screening** → 跳转地址详情页 

详情见设计图：[https://www.figma.com/design/UOboiqdiQhZbg076ti7RnH/%F0%9F%94%B8-Compliance-Iterations-2.0?node-id=21-650&p=f&t=OzzHerEoVrDEs9du-0](https://www.figma.com/design/UOboiqdiQhZbg076ti7RnH/%F0%9F%94%B8-Compliance-Iterations-2.0?node-id=21-650&p=f&t=OzzHerEoVrDEs9du-0)

## 单交易筛查流程优化

#### 优化前流程

搜索 → Add → 确认 Direction / Label / Customer → Import → 二次确认 + Screening 状态提示  → 跳转交易列表页

#### 优化后流程

搜索 → 选择 transfer → 确认 Direction / Label / Customer → **直接发起 Screening** → 跳转交易详情页 

详情见设计图：[https://www.figma.com/design/UOboiqdiQhZbg076ti7RnH/%F0%9F%94%B8-Compliance-Iterations-2.0?node-id=21-650&p=f&t=OzzHerEoVrDEs9du-0](https://www.figma.com/design/UOboiqdiQhZbg076ti7RnH/%F0%9F%94%B8-Compliance-Iterations-2.0?node-id=21-650&p=f&t=OzzHerEoVrDEs9du-0)

## 文案优化

需要对平台内的文案进行统一优化，去除 ‘Import’ 的概念。

### CSV 导入弹窗

:::
**Here Are Your Uploaded Details**

✅ Address Upload Complete

Review the status of each address below.

🔍 Screening Started

We have started screening your uploaded addresses.

---

1 Address(es) successfully uploaded, 0 failed

Status

Uploaded
:::
:::
**Here Are Your Uploaded Details**

✅ Transaction Upload Complete

Review the status of each transfer below.

🔍 Screening Started

We have started screening your uploaded transactions.

---

1 Transfer(s) successfully uploaded, 0 failed

Status

Uploaded
:::

### 按钮

*   地址列表页的  Import Address 改为 Screen Address
    
*   交易列表页的 Import Transaction 改为 Screen Transaction
    
*   Dashboard 的 Start Importing 改为 Start Screening
    

#### Onboarding Guide

第二个步骤 "Import and Screen Addresses or Transactions" 文案修改：

:::
**Screen Addresses or Transactions**

Run screening on any address or transaction using all configured risk engines.

                                                            【Try Examples】 【Screen Address】 【Screen Transaction】
:::

# 参考

## Chainalysis 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3j4Vvz7aOXo/img/95c94b0d-9e18-4954-b065-b74bf1578c4f.png)

Note：地址页面没有链信息，所以是对于一个地址会自动扫全部链？这样就少了选择链这一步骤

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3j4Vvz7aOXo/img/26bf33a0-cb26-4ed3-9603-9c5d27c2a605.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3j4Vvz7aOXo/img/243022fa-00ac-49fa-815e-170be8840509.png)