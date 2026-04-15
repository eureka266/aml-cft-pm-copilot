# \[20251021\] 新增 Human Trafficking

| Risk Indicator | 指标描述 | 风险等级 | 推荐配置方案 |
| --- | --- | --- | --- |
| **Human Trafficking** | 涉及人口贩卖活动的组织或与人口贩卖资金往来相关的地址。 | **Critical** | 加入默认引擎：<br>*   “FATF Guidelines: Wallet owned by illicit entity”<br>    <br>*   “Transaction Involving Illicit Entities”<br>    <br>*   “FATF Guidelines: Exposure to illicit entity”<br>    <br>*   “Transaction Exposed to Illicit Entities” |

*   新增 Risk Indicator 和标签库中标签的对应关系，见[《Risk Engine》](https://alidocs.dingtalk.com/i/nodes/P7QG4Yx2JpAbqpvoT5gb2A0A89dEq3XD?utm_scene=team_space&iframeQuery=anchorId%3Duu_m8sfey79g2nms4tnygi)表格中标黄部分
    
*   另外，在 Risk Engine 处展示的每个 Risk Indicator 的 Description![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/WgZOZA8ojrAVXqLX/img/18806708-3222-4dc7-89e9-5f164ad20959.png)都有调整，见：[https://phalconv2-manual.blocksec.com/compliance/manual/risk-engines/exposure](https://phalconv2-manual.blocksec.com/compliance/manual/risk-engines/exposure)
    

#### 用户确认机制

*   通知方式：系统内通知 + 邮件推送
    
*   提供“一键应用”与“稍后配置”选项
    
*   设置明确的**确认截止时间**（如：7 天）
    
*   超过截止时间未操作的用户将自动应用推荐配置
    
*   一键应用/自动应用配置的变更（即所有系统操作帮助修改用户 Engine 的情况）需要记录 Audit Logs 
    
    *   用户点击一键应用：操作人记录为当前用户
        
    *   到期自动更改：操作人记录为 System
        

:::
对新增的 “试用用户”这种类型，不做通知，直接后台修改 Risk Engine （也需要记录 Audit Logs）
:::

# 通知方案

## 平台通知

:::
New Risk Indicators Added – Action Required

To enhance your compliance coverage, a new high-priority Risk Indicators have been added.

| **Risk Indicator** | **Description** | **Recommended Configuration** |
| --- | --- | --- |
| Human Trafficking | Addresses linked to organizations or transactions involved in human trafficking activities. | Add this indicator to default risk engines:<br>FATF Guidelines: Wallet owned by illicit entity<br>Transaction Involving Illicit Entities<br>FATF Guidelines: Exposure to illicit entity<br>Transaction Exposed to Illicit Entities |

**Note:** If no action is taken by **Octorber 31, 2025**, the recommended setup will be applied automatically.

**Actions:**

🔘 Apply Recommended Setup

🔘 Configure Later in Risk Engine

                                                                                                                                                                                 \[Confirm\] 
:::

## Email Notification 

**Subject**: 🔔 \[Action Required\] New Risk Indicator Added – Confirm Setup by {截止日期}

**Header**：New Risk Indicators to Strengthen Your Compliance Framework

Dear Compliance Officer,

To align with evolving AML/CFT standards, Phalcon Compliance has added the following new Risk Indicators:

| **Risk Indicator** | **Description** | **Recommended Configuration** |
| --- | --- | --- |
| **Human Trafficking** | Addresses linked to organizations or transactions involved in human trafficking activities. | Add this indicator to default risk engines:<br>*   FATF Guidelines: Wallet owned by illicit entity<br>    <br>*   Transaction Involving Illicit Entities<br>    <br>*   FATF Guidelines: Exposure to illicit entity<br>    <br>*   Transaction Exposed to Illicit Entities |

You can apply the suggested setup automatically or configure it manually.

> **Please confirm by \[截止时间\]**  
If no action is taken, the recommended configuration will be applied automatically.

**Take Action:**  
👉 \[Apply Recommended Setup\]  
🛠️ \[Go to Risk Engine to Configure Manually\]

Need help? Contact our support team.

Best regards,  
**Phalcon Compliance Team**

# 配置修改/新增详情

#### 修改已有 Default Risk Engine

| Engine Name | Type / Template | 具体修改 |
| --- | --- | --- |
| FATF Guidelines: Wallet owned by illicit entity | Address / Entity Risk | 增加 Risk Indicator：**Human Trafficking** |
| FATF Guidelines: Exposure to illicit entity | Address / Interaction Risk | 增加 Risk Indicator：**Human Trafficking** |
| Transaction Involving Illicit Entities | Transaction / Participant Risk | 增加 Risk Indicator：**Human Trafficking** |
| Transaction Exposed to Illicit Entities | Transaction / Interaction Risk | 增加 Risk Indicator：**Human Trafficking** |

# 通知机制与配置确认

## 用户通知策略

#### 弹窗通知（系统内）

*   **展示时机：**
    
    *   新指标上线后，用户首次登录平台后台页面自动弹出。
        
    *   仅对具备编辑权限（非 viewer）的用户展示。
        
    *   如果一个 team 中的其他用户已经点击了 `Apply Recommended Configuration`，对同一 team 中的其他人不再展示弹窗。
        
*   **交互行为：**
    
    *   `Apply Recommended Configuration`: 立即完成推荐配置并记录状态，后续不再展示弹窗。
        
    *   `Configure Later`: 暂不配置。
        

#### 邮件通知

*   **收件范围：**
    
    *   所有非 viewer 权限成员（如 admin、editor 等角色）。
        
*   **邮件内交互：**
    
    *   点击邮件中的操作按钮`Apply Recommended Setup`将跳转到系统界面，若未配置过，将弹出上述弹窗。
        
    *   若已完成配置，不再重复展示，展示下面的消息弹窗。
        

:::
**Configuration Already Completed**

You've already confirmed the recommended setup for the new Risk Indicators.

No further action is required.
:::

## 引擎配置

当用户在系统弹窗或邮件通知中选择 “**Apply Recommended Setup**” 时，系统将尝试将推荐的 Risk Indicator 更新应用到用户现有的默认 Risk Engine 中。

### 默认引擎

系统优先通过以下方式识别“默认风险引擎”：

*   `engine_name` 与系统默认名称完全一致；
    
*   若识别成功，将直接在引擎中追加推荐的 Risk Indicator。
    

修改成功提示：

Recommend Configuration applied successfully!

### 无法识别默认引擎的处理方式

若系统无法找到对应的默认引擎（可能因用户删除或重命名），将按以下策略处理：

重新创建未找到的 Risk Engine，但只包含此次新增的 Risk Indicator。

展示导入成功弹窗：

:::
Recommend Configuration applied successfully!

Some default Risk Engines could not be found. New engines with recommended configurations was created to ensure your compliance coverage remains complete.

                                                                            \[Confirm\]
:::