# Phalcon Network User Guide

## Get Started

### What Phalcon Network Does

Phalcon Network helps you detect illicit or high-risk funds flowing into your on-chain addresses and notifies you in real time.

Once monitoring is configured, you no longer need to manually track on-chain activity. After setup, incoming transfers are continuously screened. Alerts are sent to the configured notification channels when high-confidence risks are detected.

### Quick Setup (3 Steps)

**3 Steps to Receive Alerts**

1.  **Add an address to be monitored**  
    Add the wallet addresses you want to track, and we’ll continuously monitor them for risk activity.
    
2.  **Configure a Notification Channel**  
    Connect your preferred channel (e.g., Lark) so alerts are delivered to the right team in real time.
    
3.  **Receive and manage your risk alert**  
    Review alert details, take action, and keep track of alert status as you investigate.
    

After setup, alerts will be automatically delivered whenever risky funds reach your monitored addresses.

### What Kind of Alerts Will I Receive?

Each alert corresponds to **one specific incoming transaction** and includes:

*   Detected risk type(s)
    
*   Source address → your monitored address
    
*   Transaction value and timestamp
    
*   Direct links to detailed risk analysis and fund flow visualization
    

## 1. Join Phalcon Network

#### Access Requirements

Phalcon Intelligence Network is available to **approved or invited organizations only**.

#### How to Join

1.  Submit an application via the landing page
    
2.  Provide organization and contact information
    
3.  Wait for manual review
    
4.  Complete registration through the approval email
    

#### Important Notes

*   Invitation links are single-use and expire after 72 hours
    
*   If an invitation link expires before you complete login or registration, the invitation will become invalid
    
    *   Please request a **new invitation** or contact us at **phalcon\_support@blocksec.com** for assistance
        
*   Phalcon Network shares the same account system as **Phalcon Compliance**
    
    *   If you already have a Phalcon account, you will be redirected to the login page after approval
        

## 2. Monitor an Address

### What Can Be Monitored?

You can monitor:

*   Wallet addresses or contract addresses
    
*   Multi-chain addresses (same coverage as Phalcon Compliance)
    
*   Incoming transfers only
    

### Add a Monitoring Address

1.  Go to the dashboard or onboarding page
    
2.  Enter the address you want to monitor
    
3.  (Optional) Add a **Note** to describe the address (strongly recommended)
    
4.  Save the address to activate monitoring
    

Once saved, the system starts monitoring immediately.

### Monitoring Rules

*   Only incoming transactions are evaluated
    
*   Risk screening is triggered **only when the incoming value ≥ system threshold** (default: USD 10,000)
    
*   Each transaction generates **at most one alert**
    
*   Multiple risk types are merged into a single alert
    

### Manage Monitoring Status

*   You can pause or resume monitoring at any time
    
*   While paused, no new alerts will be generated
    
*   Monitoring resumes immediately when re-enabled
    

## 3. Receive Alerts

### What Triggers an Alert?

An alert is triggered when an incoming transaction is linked to high-risk or illicit intelligence, including:

*   Sanctioned entities
    
*   Scams and phishing
    
*   Ransomware
    
*   Laundering, mixing, dark markets, and other high-risk sources
    

### Alert Aggregation Rule

*   One transaction → one alert
    
*   Multiple risk types → merged into one alert
    
*   Multi-hop fund exposure → summarized into a single alert
    

This design prevents duplicate or excessive notifications.

## 4. Set up a Notification Channel

Notification channels determine **where and how you receive alerts**.   You must connect **one** channel to receive notifications.

### Supported Channels

| Channel | Best For | Characteristics |
| --- | --- | --- |
| Telegram | Individuals, small teams | Real-time, lightweight |
| Slack | Security & engineering teams | Team collaboration |
| Lark | Enterprise teams | Structured permissions |
| Email | Compliance & record keeping | Broad coverage, easy archiving |

You can connect single **channels** and manage it at the account level.

### Connnect to a Channel

#### Connect to Telegram

##### What You Need

*   A Telegram account
    
*   Permission to chat with bots
    

##### Steps

1.  Click **Add Notification Channel → Telegram**
    
2.  Open the displayed Telegram Bot link
    
3.  In Telegram, start a chat with the bot
    
4.  Send `/start` to the bot
    
5.  Return to the platform and confirm connection
    

Once connected, alerts will be delivered via this bot.

##### Troubleshooting

*   Make sure `/start` was sent to the bot
    
*   Do not mute or block the bot
    
*   Ensure you are logged into the correct Telegram account
    

#### Connect to Slack

##### What You Need

*   A Slack workspace
    
*   Permission to post messages in the target channel
    

##### Steps

1.  Click **Add Notification Channel → Slack**
    
2.  Click **Connect Slack**
    
3.  Log in to your Slack account
    
4.  Select the workspace and channel for alerts
    
5.  Authorize access
    

Alerts will be sent as bot messages to the selected channel.

##### Common Issues

*   Private channels require manually inviting the bot
    
*   You must have message-posting permissions in the channel
    

#### Connect to Lark

##### What You Need

*   A Lark enterprise account
    
*   Permission to manage or invite bots to the target group
    

**Steps**

1.  In the notification channel settings, select **Lark**.
    
2.  In Lark ([https://www.larksuite.com/messenger/](https://www.larksuite.com/messenger/)), add a **Custom Bot** to the group:
    
    1.  Open the target group → **More** → **Settings** → **Bots** → **Add Bot** → **Custom Bot**.![/Users/eureka266/Library/Group Containers/group.com.apple.notes/Accounts/2013FF3F-5FD4-4FA8-BCDB-24605F67D81B/Media/45BAC376-77C8-42DE-9A8B-921D354DB425/1_286C7FDE-AAD0-4924-A0B5-614665CA95F9/Pasted Graphic 1.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/34e67471-6e2f-456a-871a-0a57678973d7.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/26252d9d-5bf8-4052-a558-42bce7910d39.png)
        
    2.  Set a name and description, then confirm.
        
3.  After the bot is added, copy its **Webhook URL** & **Signature**. You’ll see a test message sent by the bot.![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/7ae8e609-73f9-4895-9e95-bf998caa429b.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/b1836c1b-d0cf-4851-baaf-f78c8c35835f.png)
    
4.  Go back to **Phalcon Network** and paste the **Webhook URL** and **Signature** into the Lark notification settings.
    
5.  Done. You can preview how messages will look before saving.
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/26acf2fc-09ab-4654-b323-9c837e964249.png)

**你需要准备：**

*   Lark 企业账号
    

对目标群聊有管理或邀请权限

**步骤：**

1.  选择渠道 在 Phalcon Network 通知渠道配置中，选择 “Lark”。
    
2.  添加机器人到群组
    
    *   进入需要推送警报的 Lark 群组，点击右上角「…」>「设置」>「机器人」。
        
        ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/75050061-392c-4c63-8084-f1cb777da003.jpg)Image options
        
    *   点击“添加机器人”，选择“自定义机器人”，设置名称并添加。
        
    
    ![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/7ed4a8d9-9dae-4cb6-933d-834530f239b2.jpg)Image options
    
3.  获取 Webhook
    
    添加成功后，复制机器人的 Webhook URL（格式如 `https://open.larksuite.com/open-apis/bot/v2/hook/xxxxxxxxxxx`）。
    
    同时在下方\[安全设置\]处勾选Set signature verification，复制Signature
    
    点击“完成”后，可以收到机器人发送的自动消息![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/8e742bca-3ce6-477c-84ff-483731eb1eb6.png)
    
4.  填写配置
    
    将 Webhook URL 与 Signature 粘贴到 Phalcon Network 的 Lark 配置框中。
    

完成 点击"创建"保存通知渠道配置，即可查看消息样式预览，开始接收通知。

![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/YdgOk2bg9vj37q4B/img/639f91a6-5183-45f3-bb24-0b75043a5cac.jpg)Image options

##### Troubleshooting

*   Ensure the bot is not removed from the group
    
*   Confirm the group allows bot messages
    

#### Connect to Email

##### Steps

1.  Click **Add Notification Channel → Email**
    
2.  Enter the email address
    
3.  Complete verification if required
    
4.  Save the channel
    

Alerts will be delivered as email notifications.

##### Recommended Settings

*   Add the alert sender to your email whitelist
    
*   Check spam or junk folders if alerts are missing
    

### After Connecting a Channel

*   New alerts are delivered in real time
    
*   One monitoring address can notify single channel
    
*   The notification channel can be removed or replaced at any time
    

## 5. Understanding an Alert

Each alert contains:

*   Risk type(s) and intelligence source
    
*   From address → monitored address
    
*   Transaction hash, value, and timestamp
    
*   Unique Alert ID for traceability
    

\[alert详情预览图\]

**Available Actions:**

From an alert, you can immediately:

*   🔍 View full transaction risk analysis in **Phalcon Compliance**
    
*   🧭 View the fund flow graph in **MetaSleuth**
    
*   ⏸ Pause monitoring for the affected address
    

## 6. Managing Monitoring and Alerts

What You Can Do：

*   Pause or resume monitored addresses
    
*   Edit address notes
    
*   View historical alerts and statistics
    

## FAQ

### Why Didn’t I Receive an Alert?

Possible reasons include:

*   The transaction value did not reach the system threshold
    
*   The incoming funds were not linked to high-risk intelligence
    
*   Monitoring was paused
    
*   Notification channels were not correctly configured
    

### What Intelligence Sources Are Used?

Currently, Phalcon Intelligence Network uses:

*   BlockSec internal high-risk address label library
    

This library aligns with the **public high-risk indicators** used in Phalcon Compliance, including sanctions, scams, ransomware, laundering, and mixing.

### Can There Be False Positives?

The system is designed for **high confidence and low noise**, but alerts are **risk signals**, not final determinations.

For deeper investigation, use Phalcon Compliance to review full transaction context and fund flows.

### Can I Customize Risk Types or Thresholds?

In Phalcon Network, risk types and alert thresholds are centrally managed to ensure consistent and neutral alert semantics across all users.

If you need:

*   Custom risk categories
    
*   Adjustable alert thresholds
    
*   More granular screening logic or ongoing re-screening
    

You can configure these options in **Phalcon Compliance**, which provides advanced monitoring, customization, and compliance workflows built on the same risk engine.

## What If My Address Is on an Unsupported Chain?

Monitoring is available only for supported blockchains.

If a blockchain is not supported, please contact **phalcon\_support@blocksec.com** to share your requirements or report suspicious activity. Additional chain support is evaluated on an ongoing basis.

## Phalcon Network – FAQ

### 一、What Is Phalcon Network & When Should I Use It

*   What is Phalcon Network designed to do?
    
*   What problems does Phalcon Network solve (and what it does not)?
    
*   How is Phalcon Network different from Phalcon Compliance?
    

### 二、How Alerts Work (Core Mechanics)

*   What triggers an alert in Phalcon Network?
    
*   Are alerts generated at the address, transaction, or fund-flow level?
    
*   Is alerting real-time or near real-time?
    
*   Does Phalcon Network analyze native transfers, token transfers, or both?
    
*   How are repeated or related transactions handled?
    

### 三、Alert Lifecycle & Monitoring Behavior

*   How many times can the same address trigger alerts?
    
*   Will alerts be repeated for the same risk source?
    
*   What happens when monitoring is paused?
    
*   Will alerts be backfilled after monitoring resumes?
    
*   Can alerts be dismissed or acknowledged?
    

### 四、Coverage & Limitations

*   Which blockchains are currently supported?
    
*   Are smart contract internal transfers monitored?
    
*   How are cross-chain transactions handled?
    
*   What happens if an address is on an unsupported chain?
    
*   Are historical transactions monitored or only new activity?
    

### 五、Notifications & Integrations

*   What notification channels are supported?
    
*   How quickly are alerts delivered after detection?
    
*   What happens if a notification fails?
    
*   Can multiple recipients receive the same alert?
    
*   Does Phalcon Network support webhooks or API access?
    

### 六、Risk Semantics & Intelligence

*   What does an alert represent in Phalcon Network?
    
*   Are alerts final risk determinations?
    
*   Does Phalcon Network use the same risk labels as Phalcon Compliance?
    
*   How often is risk intelligence updated?
    

### 七、Using Phalcon Network with Phalcon Compliance

*   Can I investigate a Network alert in Phalcon Compliance?
    
*   Does a Network alert affect Compliance risk scoring?
    
*   When should I upgrade to Phalcon Compliance?
    
*   Can Compliance users customize risk rules beyond Network defaults?
    

### 八、Common Issues & Troubleshooting

*   Why didn’t I receive an alert?
    
*   Why did I receive multiple alerts for similar activity?
    
*   Why did monitoring stop unexpectedly?
    
*   Who should I contact for support or feature requests?
    

## 8. Learn More

### Scope and Integration with Phalcon Compliance

Phalcon Intelligence Network acts as an extension and entry point to Phalcon Compliance:

*   Free, real-time risk awareness
    
*   Seamless transition to advanced investigations
    
*   Shared risk engine and labeling system
    

### Law Enforcement and Regulatory Participation

The platform is actively evolving to support law enforcement and regulatory collaboration.

If your organization is interested in participating, contact:

**phalcon\_support@blocksec.com**