# Default Risk Engines -25.11

# 背景与目标

当前 Interaction Risk Engine 的规则设计以单一金额阈值为主，主要用于识别高确定性的高额风险交易或地址暴露。例如：

*   地址的 Illicit 类型风险：Exposure Value ≥ 10,000 USD → Critical
    
*   地址的 High-Risk 类型风险：在金额阈值基础上叠加 Exposure Percent 条件 → High
    

该设计在系统早期阶段有效降低了误报率，但随着客户业务规模扩大、资金流复杂度提升，逐渐暴露出覆盖不足与解释成本偏高的问题。

#### 当前问题

*   风险覆盖不足
    
    *   现有规则无法有效覆盖很多风险场景，如：中低金额但风险确定性较高的 Illicit 暴露
        
*   风险分层能力不足
    
    *   当前 Interaction Risk Engine 主要输出 Critical / High 两个等级
        
*   用户解释成本较高
    
    *   当风险未触发但用户主观认为“存在风险”时：
        
        *   需要额外解释金额阈值与规则限制
            
        *   用户需自行理解并配置规则，学习成本较高
            

#### 目标

*   本次预计新增 8 个默认的 risk engine，其中地址类型的 4 个、交易类型的 4 个。
    
*   增加后整体规则覆盖情况如下:
    
    **Address – Illicit 风险覆盖**
    
    | Exposure Percent ↓ / Value → | < 1,000 | 1,000–5,000 | 5,000–10,000 | ≥ 10,000 |
    | --- | --- | --- | --- | --- |
    | \>= 1% | \- | 🟡 Medium | 🟠 High | 🔴 Critical _(已有)_ |
    | 0.1% – 1% | \- | \- | 🟠 High | 🔴 Critical _(已有)_ |
    | < 0.1% | \- | \- | \- | 🔴 Critical _(已有)_ |
    
    **Address – High-Risk 风险覆盖**
    
    | Exposure Percent ↓ / Value → | < 1,000 | 1,000–5,000 | 5,000–10,000 | ≥ 10,000 |
    | --- | --- | --- | --- | --- |
    | ≥ 10% | \- | 🟢 Low | 🟡 Medium | 🟠 High _(已有)_ |
    | < 10% | \- | \- | \- | \- |
    
    **Transaction – Illicit 风险覆盖**
    
    | Exposure Percent ↓ / Value → | < 1,000 | 1,000–2,000 | 2,000–5,000 | ≥ 5,000 |
    | --- | --- | --- | --- | --- |
    | \>= 1% | \- | 🟡 Medium | 🟠 High | 🔴 Critical _(已有)_ |
    | 0.1% – 1% | \- | \- | 🟠 High | 🔴 Critical _(已有)_ |
    | < 0.1% | \- | \- | \- | 🔴 Critical _(已有)_ |
    
    **Transaction – High-Risk 风险覆盖**
    
    | Exposure Percent ↓ / Value → | < 1,000 | 1,000–5,000 | ≥ 5,000 |
    | --- | --- | --- | --- |
    | ≥ 50% | \- | 🟡 Medium | 🟠 High _(已有)_ |
    | 25% – 50% | \- | 🟡 Medium | 🟡 Medium |
    | 10% – 25% | \- | \- | 🟡 Medium |
    | < 10% | \- | \- | \- |
    
*   规则增加方案：
    
    *   **新用户**：默认启用新增规则
        
    *   **已有免费用户**：直接更新默认规则，不进行强提示
        
    *   **已有付费用户**：
        
        *   新增规则默认 **Disabled**
            
        *   弹窗与 Banner 提示
            
        *   支持一键 Enable
            
*   根据测试结果：**Alert 数量预计增加 50%+**
    

# 当前 Interaction Risk Engine

| **Target Type** | **Address** |  | **Transaction** |  |
| --- | --- | --- | --- | --- |
| **Engine Name** | FATF Guidelines: Exposure to illicit entity | FATF Guidelines: Exposure to high-risk entity | Transaction Exposed to Illicit Entities | Transaction Exposed to High-Risk Entities |
| **Description** | Detects address that has direct or indirect exposure to illicit entities. | Detects address that has direct or indirect exposure to high-risk entities. | Detects transactions with direct or indirect interactions with illicit entities. | Detects transactions with direct or indirect interactions with high-risk entities. |
| **Risk Level** | **Critical** | **High** | **Critical** | **High** |
| **Risk Indicator** | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction |
| **Direction** | incoming or outgoing | incoming or outgoing | deposit or withdrawal | deposit or withdrawal |
| **Interaction Type** | direct or indirect | direct or indirect | direct or indirect | direct or indirect |
| **Exposure Value** | **\>= 10,000 USD** | **\>= 10,000 USD** | **\>= 5,000 USD** | **\>= 5,000 USD** |
| **Exposure Percent** | N/A | **\>= 10%** | N/A | **\>= 50%** |

基本原则：

*   Illicit 类型为确定的犯罪类型，等级较高且规则中无 Percent 限制以覆盖更大的检测场景
    
*   High-risk 类型为风险程度较轻的类型，加上 Exposure Percent 的限制避免误报和复杂的资金流图
    

# 新增 Risk Engine

规则测试内容见：[《规则修改测试》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=ZgpG2NdyVXXLMx90ubLyBxKNVMwvDqPk&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

## Address 类型

| **Engine Name** | Illicit Exposure - Address (High) | Illicit Exposure - Address (Medium) | High-Risk Exposure – Address (Medium) | High-Risk Exposure – Address (Low) |
| --- | --- | --- | --- | --- |
| Description | Detects addresses with significant direct or indirect exposure to confirmed illicit entities, indicating elevated criminal risk. | Detects addresses with moderate direct or indirect exposure to illicit entities, capturing early or limited criminal risk signals. | Detects addresses with meaningful exposure to high-risk entities, indicating potential compliance concerns. | Detects addresses with limited exposure to high-risk entities, serving as a low-severity risk awareness signal. |
| **Risk Level** | **High** | **Medium** | **Medium** | **Low** |
| **Risk Indicator** | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction |
| **Direction** | incoming or outgoing | incoming or outgoing | incoming or outgoing | incoming or outgoing |
| **Interaction Type** | direct or indirect | direct or indirect | direct or indirect | direct or indirect |
| **Exposure Value** | **\>= 5,000 and < 10,000** | **\>= 1,000 and < 5,000** | **\>= 5,000 and < 10,000** | **\>= 1,000 and < 5,000** |
| **Exposure Percent** | **\>= 0.1%** | **\>= 1%** | **\>= 10%** | **\>= 10%** |

原则：

*   对于 Illicit 的类型，为了防止误报不移除 Percent 限制，但会设定一个比较小的值防止误报。
    

## Transaction 类型

| **Engine Name** | Illicit Exposure – Transaction (High) | Illicit Exposure – Transaction (Medium) | High-Risk Exposure – Transaction (Medium / Upper Range) | High-Risk Exposure – Transaction (Medium) |
| --- | --- | --- | --- | --- |
| Description | Detects transactions with significant direct or indirect interactions with illicit entities, indicating high compliance risk. | Detects transactions with moderate exposure to illicit entities, capturing suspicious but lower-severity interactions. | Detects transactions with concentrated exposure to high-risk entities, indicating elevated transactional risk. | Detects transactions with moderate exposure to high-risk entities, highlighting potential compliance concerns. |
| **Risk Level** | **High** | **Medium** | **Medium** | **Medium** |
| **Risk Indicator** | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Attack, Sanctioned, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing, Human Trafficking, Drug Trafficking | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction | Gambling, Blocked, No KYC Exchange, FATF High Risk Jurisdiction |
| **Direction** | deposit or withdrawal | deposit or withdrawal | deposit or withdrawal | deposit or withdrawal |
| **Interaction Type** | direct or indirect | direct or indirect | direct or indirect | direct or indirect |
| **Exposure Value** | **\>= 2,000 and < 5,000** | **\>= 1,000 and < 2,000** | **\>= 5,000 USD** | **\>= 1,000 USD and < 5,000** |
| **Exposure Percent** | **\>= 0.1%** | **\>=1%** | **\>= 10% and < 50%** | **\>= 25%** |

#  Default 规则修改方案

本次 default 规则仅涉及规则新增，不会修改已有的 default 规则，对不同类型的用户采取以下的方案

## 新用户

新用户注册时默认启用新的 Default Risk Engine 

## 老用户

#### 免费用户

*   直接更新为 Default 规则
    
*   不进行弹窗或强提示
    

#### 付费用户

*   新增 Risk Engine 默认 Disabled
    
    *   避免用户没有及时感知而影响其风控策略
        

*   规则标记为 **“New”**
    

*   弹窗和 Banner 提示规则增加，允许一键 Enable，文案：
    
    *   弹窗：
        
        *   展示逻辑：在所有付费 project 中 admin、editor 用户第一次登录平台时展示，如果已经 Enable 了则不展示
            
        
        :::
        **New Default Risk Engines Available**
        
        We’ve added new default risk engines to improve coverage for **mid-to-low value risk exposures** that were not previously captured.
        
        To avoid impacting your existing risk workflow, these engines are **disabled by default**.  
        You can review the details and enable them at any time.
        
        `Enable All New Engines`｜`View Details`｜`Maybe Later`
        :::
        
    *   Banner 
        
        *   展示逻辑：在 risk engine 列表页展示，上线后默认展示两周
            
        *   文案：  
            New default risk engines are available to help detect mid-to-low value risk exposures. These engines are currently disabled to avoid impacting your existing workflow.  
            操作：\[Enable All New Engines\] 
            

*   给所有付费用户发送通知邮件，内容如下
    

:::
标题：New Default Risk Engines Available

Hi,

We’ve added several **new default risk engines** to your project to improve coverage for **mid-to-low value risk exposures**.

To avoid affecting your existing risk workflow, these new engines are **disabled by default**. You can review and enable them at any time in the **Risk Engine** settings.

No changes have been made to your current default or custom rules.

If you have any questions, feel free to reach out.

Best regards,  
**Phalcon Compliance**
:::

### 付费的projectId

```json
up_ce29bbaeb16d4e5ab08400beac66c8b6
up_9409516c3de245f09603af976c91ea28
up_c200538f289a4ea2b3d50713ea5037d8
up_f486cda810ab4a4a8bc45547ccc763f5

up_2fee7e4191d0432c9e4b7642469d0721
up_ca2db33799344cf198cea7ece6f995ad
u_15dbfe462ad245ffa97e006af4026fea

up_df1924fa8c2f499fac5e76773a62e351
up_46ad1d0578f247748cc249e8967fe51d
```