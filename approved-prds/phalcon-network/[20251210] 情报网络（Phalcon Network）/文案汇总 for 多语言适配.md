# 文案汇总 for 多语言适配

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4jKqm0bPPBz8Ynw1/img/13444efe-51a6-4cbf-96d2-670fa4abdb6c.png)

# 用户申请及注册

申请表单

| **EN** | **ZH-CN** |
| --- | --- |
| Apply to join Phalcon Network | 申请加入 Phalcon Network |
| Tell us about your organization. We review applications manually. | 请填写机构信息。我们将进行人工审核。 |
| Company information | 机构信息 |
| Organization name | 机构名称 |
| Enter your organization name | 请输入机构名称 |
| Business type | 机构类型 |
| Select a category | 请选择类别 |
| Please select your organization category. | 请选择机构类别。 |
| Please select a specific organization type. | 请选择具体机构类型。 |
| Official website | 官网链接 |
| Registration country / region | 注册国家/地区 |
| Select a country / region | 请选择国家/地区 |
| Contact information (for review contact only) | 联系信息（仅用于审核沟通） |
| Corporate email | 企业邮箱 |
| name@company.com | name@company.com |
| Contact person name | 联系人姓名 |
| Enter name | 请输入姓名 |
| Contact position / title (optional) | 职位/头衔（可选） |
| Enter position / title | 请输入职位/头衔 |
| By submitting, you confirm the information is accurate and you have authority to apply on behalf of your organization. | 提交即表示您确认信息真实准确，并有权代表机构提交申请。 |
| Submit application | 提交申请 |
| Application submitted | 申请已提交 |
| We’ll email you after review. If approved, you’ll receive a one-time registration link. | 审核完成后我们将发送邮件通知。若通过，您将收到一次性注册链接。 |

## 页面文案

### 注册页面

V1

左上角logo:

Blocksec Phalcon Network 

Powered by Phalcon Compliance ｜ A Platform for Crypto Compliance, Risk Investigation & Law Enforcement

**主标题：**

EN：Stay Alerted to Illicit Crypto Inflows  
ZH-CN：

**描述文字：**

EN：Detect illicit funds the moment they reach your platform. Receive real-time alerts and isolate suspicious assets to stop laundering at the source. 

For advanced investigations, continue in ++Phalcon Compliance++.

ZH-CN：当可疑资金触及您的平台，Phalcon 即刻侦测。

实时告警并协助隔离高风险资产，在风险扩散前完成处置。

如需深入调查，可无缝转入 Phalcon Compliance 继续分析。

### 登录页面

From raw address to risk alert - in minutes

➡️ Add addresses to watch 

➡️ Get alerts with triggered risk types

➡️ Investigate and configure monitoring in Phalcon Compliance

Sign in to Phalcon Network

Forgot your password?

## 提示文案

**审核通过-发送注册链接**

| 场景 | 英文 | 中文 |
| --- | --- | --- |
| 超过 72 小时访问链接已过期 | Link expired. Please request a new one. | 链接过期，请申请重新发送 |
| Token 已被使用过 / 重复注册 | Account already activated. Please sign in. | 该链接已完成注册，请直接登录 |
| Token 格式错误/不存在，非法访问 | Invalid registration link. | 无效的注册链接 |

## 邮件模版

|  | 英文 | 中文 |
| --- | --- | --- |
| 审核通过邮件（未注册过phalcon账号的用户）<br>key=register | ```json<br>[<br>  {<br>    "id": "mail-subject",<br>    "translation": "Welcome to Phalcon Network – Your Application Has Been Approved"<br>  },<br>  {<br>    "id": "mail.greeting",<br>    "translation": "Hello {{.}},"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "We are pleased to inform you that your application for access to Phalcon Network has been approved."<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "Please click the link below to complete your account registration and get started with on-chain risk monitoring:"<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "Register Now"<br>  },<br>  {<br>    "id": "mail.urlDesc",<br>    "translation": "If the button doesn’t work, copy and paste the link into your browser.This link is valid for {{.}} hours."<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "After completing registration, you will be able to add blockchain addresses for monitoring, configure real-time alert notification channels, and initiate platform-level monitoring of illicit crypto activities. Your account will also be granted access to the Phalcon Compliance AML platform, enabling a one-stop investigation workflow from alerts to on-chain analysis, helping you respond and trace incidents more efficiently. If you have any questions, feel free to reply to this email directly or refer to the <a href=\"https://blocksec.gitbook.io/phalcon-network-help-center/product-network-help-docs\">Help Documentation</a>."<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "Best regards,<br>Phalcon Support Team"<br>  }<br>]<br>``` | ```json<br>[<br> {<br>    "id": "mail-subject",<br>    "translation": "欢迎加入Phalcon Networ – 您的申请已通过"<br>  },<br>  {<br>    "id": "mail.greeting",<br>    "translation": "{{.}}，您好！"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "我们很高兴地通知您，您申请的 Phalcon Network 访问权限已审核通过。"<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "请点击下方链接完成账户注册，开启链上风险监控之旅："<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "立即注册"<br>  },<br>   {<br>    "id": "mail.urlDesc",<br>    "translation": "如果按钮无法点击，请复制以下链接在浏览器中打开。该链接在{{.}}小时内有效。"<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "完成注册后，您可以添加区块链地址进行监控、配置实时告警通知渠道，并启动对非法加密活动的平台级监测。您的账户还将同步开通 Phalcon Compliance 反洗钱合规平台权限，支持从告警到链上分析的一站式调查流程，帮助您更高效地响应和溯源。如有任何疑问，欢迎直接回复本邮件或查阅 <a href=\"https://blocksec.gitbook.io/phalcon-network-help-center/product-network-help-docs\">帮助文档</a>。"<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "祝好，<br>Phalcon 支持团队"<br>  }<br>]<br>``` |
| 审核通过邮件（注册过phalcon账号的用户）<br>key= login | ### Subject<br>Your access to Phalcon Network has been approved<br>```json<br>[<br> {<br>    "id": "mail.greeting",<br>    "translation": "Hi {{.}},"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "We’re pleased to inform you that your application to join Phalcon Network has been approved."<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "Since you already have a Phalcon account, no additional registration is required. You can get started by signing in with your existing account using the link below."<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "Continue to Phalcon Network"<br>  },<br>  {<br>    "id": "mail.urlDesc",<br>    "translation": "If the button doesn’t work, copy and paste the link into your browser.This link is valid for {{.}} hours."<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "After signing in, you’ll be guided to:<br>&bull; Add your project’s monitoring addresses;<br>&bull; Configure notification channels for real-time alerts;<br>&bull; Begin monitoring illicit crypto activity as it reaches your platform.<br><br>If you have any questions, feel free to reply to this email or refer to our help doc: <a href=\"https://blocksec.gitbook.io/phalcon-network-help-center/product-network-help-docs\">Phalcon Network Help Center</a>."<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "Best regards,<br>Phalcon Support Team"<br>  }<br>]<br>``` | **主题**  <br>Phalcon Network 访问权限已获批<br>```json<br>[<br>  {<br>    "id": "mail.greeting",<br>    "translation": "{{.}}，您好！"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "我们很高兴通知您，您申请加入 Phalcon Network 的请求已通过审核。"<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "由于您已拥有 Phalcon 账户，无需再次注册。您可以通过下方链接直接登录现有账户，即可开始使用。"<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "立即进入 Phalcon Network"<br>  },<br>  {<br>    "id": "mail.urlDesc",<br>    "translation": "如果按钮无法点击，请复制以下链接在浏览器中打开。该链接在{{.}}小时内有效。"<br>  },<br> {<br>    "id": "mail.help",<br>    "translation": "登录后，您将可以：<br>&bull; 添加待监控的地址；<br>&bull; 配置实时警报通知渠道；<br>&bull; 监控涉及您平台的非法入金。<br><br>如有任何疑问，欢迎随时回复本邮件或查阅 <a href=\"https://blocksec.gitbook.io/phalcon-network-help-center/product-network-help-docs\">Phalcon Network 帮助文档</a>。"<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "祝好，<br>Phalcon 支持团队"<br>  }<br>]<br>``` |
| 注册未完成提醒<br>key= register\_not\_complete | ## Subject: Complete your registration to activate your Phalcon Network account<br>```json<br>[<br>  {<br>    "id": "mail.greeting",<br>    "translation": "Hi {{.}},"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "We noticed that your registration for the BlockSec Phalcon Network hasn’t been completed yet."<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "To activate your account and start receiving real-time alerts, please complete your registration using the link below:"<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "Complete registration"<br>  },<br>  {<br>    "id": "mail.urlDesc",<br>    "translation": "If the button doesn’t work, copy and paste the link into your browser.This link is valid for {{.}} hours."<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "If you’ve already completed registration, please ignore this email."<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "Best regards,<br>Phalcon Support Team"<br>  }<br>]<br>``` | **主题：请尽快完成注册，激活您的 Phalcon Network 账户**<br>```json<br>[<br>  {<br>    "id": "mail.greeting",<br>    "translation": "{{.}}，您好！"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "我们留意到您尚未完成 BlockSec Phalcon Network 的账户注册。为保障您的访问权限，请您尽快完成注册，以便正常开启链上实时监控与告警功能。"<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "请点击下方链接，继续完成注册："<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "去完成注册"<br>  },<br>   {<br>    "id": "mail.urlDesc",<br>    "translation": "如果按钮无法点击，请复制以下链接在浏览器中打开。该链接在{{.}}小时内有效。"<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "完成注册后，您将可立即：<br>&bull; 接入链上风险监控系统；<br>&bull; 配置实时告警通知；<br>&bull; 使用 Phalcon Compliance 进行深度交易分析。<br><br>如您已完成注册，请忽略本邮件。如有任何疑问，我们随时为您提供帮助。"<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "祝好，<br>Phalcon支持团队"<br>  }<br>]<br>``` |
| 申请未通过<br>key= apply\_failed | Subject: Update on your BlockSec Phalcon Network application<br>```json<br>[<br>  {<br>    "id": "mail.greeting",<br>    "translation": "Hi {{.}},"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "Thank you for your interest in the BlockSec Phalcon Network. After careful review, we’re unable to approve your application at this time."<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "You can still access on-chain KYC/AML risk analysis through the Phalcon Compliance Open Platform:"<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "Explore Phalcon Compliance"<br>  },<br>{<br>    "id": "mail.urlDesc",<br>    "translation": "If the button doesn’t work, copy and paste the link into your browser.This link is valid for {{.}} hours."<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "Phalcon Compliance provides on-chain KYC/AML risk analysis to help safeguard your project. If you have further questions or future collaboration interests, feel free to reach out."<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "Best regards,<br>Phalcon Support Team"<br>  }<br>]<br>``` | **主题**：您的 Phalcon Network 申请状态更新<br>```json<br>                     [<br>  {<br>    "id": "mail.greeting",<br>    "translation": "尊敬的 {{.}}，"<br>  },<br>  {<br>    "id": "mail.response",<br>    "translation": "您好！感谢您关注并申请 BlockSec Phalcon Network。我们已完成对您申请的审核，此次暂时无法通过您的申请。"<br>  },<br>  {<br>    "id": "mail.intro",<br>    "translation": "您仍可通过 Phalcon Compliance 开放平台，使用专业的链上风险分析服务："<br>  },<br>  {<br>    "id": "mail.urlText",<br>    "translation": "前往 Phalcon Compliance"<br>  },<br>   {<br>    "id": "mail.urlDesc",<br>    "translation": "如果按钮无法点击，请复制以下链接在浏览器中打开。该链接在{{.}}小时内有效。"<br>  },<br>  {<br>    "id": "mail.help",<br>    "translation": "Phalcon Compliance 提供专业的链上风险分析能力，持续保障您的项目安全。如果您今后有新的合作意向或需了解更多服务，欢迎随时与我们联系。感谢您的理解与支持！"<br>  },<br>  {<br>    "id": "mail.signature",<br>    "translation": "祝好，<br>Phalcon支持团队"<br>  }<br>]<br>``` |

# Onboarding 流程

## 页面文案

| 模块/位置 |  | 英文 | 中文 |
| --- | --- | --- | --- |
| 固定 |  | **Welcome to the Phalcon Network!**  <br>Complete the setup below to start receiving notifications when illicit funds flow into your monitored addresses. | **欢迎加入 Phalcon Network！**  <br>请完成以下设置，即可在非法资金流入您监控的地址时接收通知。 |
| 步骤 |  | 1.  Add Monitoring Address<br>    <br>2.  Connect Notification Channels<br>    <br>3.  Review & Create | 1.  添加监控地址<br>    <br>2.  绑定通知渠道<br>    <br>3.  查看并创建 |
| 第一步：添加监控地址 | 说明文案 | Add the address you want to monitor.<br>We continuously monitor incoming transfers to this address and notify you when illicit fund inflows are detected.<br>（结尾 tips 文案：To reduce noise and focus on the most relevant illicit signals, only incoming transfers over USD 10,000 are monitored.<br>） | 添加您希望监控的地址。<br>系统将持续监控该地址的所有入金交易，并在检测到非法资金流入时向您发送通知。<br>（tips 文案：为减少无关干扰、聚焦最重要的非法资金信号，当前仅监控单笔金额超过 10,000 美元的入金交易。） |
|  | 其他文案 | *   Address<br>    <br>*   Add note | *   地址<br>    <br>*   添加备注 |
|  | 按钮 | Continue | 继续 |
| 第二步：绑定通知渠道 | 说明文案 | Choose how you want to receive notifications.  <br>When illicit fund inflows related to your monitored addresses are detected, notifications will be delivered in real time through the selected channels. | 请选择您希望接收通知的方式。<br>当系统检测到与您监控地址相关的非法资金流入时，将通过所选渠道实时通知您。 |
|  | 其他文案 | *   Notification Channels<br>    <br>*   Add Notification Channel | *   通知渠道<br>    <br>*   添加通知渠道 |
|  | 按钮 | *   Back<br>    <br>*   Continue | *   返回<br>    <br>*   继续 |
| 第三步：查看并创建 | 说明文案 | Review your setup before creating the monitor.<br>Once created, monitoring will begin and you will receive notifications when illicit fund inflows are detected. | 请确认您的监控设置。<br>创建后，系统将开始对所选地址进行监控，并在检测到非法资金流入时向您发送通知。 |
|  | 其他文案 | *   Monitoring Address<br>    <br>*   Connected Notification Channels<br>    <br>*   Preview Test Alert | *   监控地址<br>    <br>*   已连接的通知渠道<br>    <br>*   预览示例告警 |
|  | 按钮 | *   Back<br>    <br>*   Create | *   返回<br>    <br>*   创建 |

## 提示文案

# 消息推送部分

## 消息文案

#### Telegram

| 英文 | 中文 | 说明 |
| --- | --- | --- |
| 🚨 Detection of Illicit Funds in Incoming Transfer **(Sanctioned and Blocked)**<br>Alert ID: 3a0d14f0-4650-4abe-abbe-a9daf3edd46d<br>Monitored Address: Label \| TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC (Note)<br>**Risk Information**<br>🏷️ Risk type: **Sanctioned, Blocked**<br>💰 Illicit fund value: $2,289<br>🗂️ Information source: BlockSec Internal Label Library<br>**Transaction Details**<br>⛓️ Chain: {Chain Logo}{Chain Name}<br>📥 From address: [TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9](https://tronscan.org/#/address/TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9)<br>🎯 To address: TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC<br>🔗 Transaction hash: [3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35](https://tronscan.org/#/transaction/3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35)<br>💰 Value (USD): $50,000<br>🕒 Time: 2025-10-20 07:11:48 UTC<br> **\[View full risk details in Phalcon Compliance\]**<br>(Compliance transaction lite scan 链接) | 🚨 检测到非法资金流入交易（**Sanctioned, Blocked**）<br>警报 ID：3a0d14f0-4650-4abe-abbe-a9daf3edd46d<br>监控地址：Label \|TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC（备注）<br>**风险信息**<br>🏷️ 风险类型：**Sanctioned, Blocked**<br>💰 非法资金金额：$2,289<br>🗂️ 信息来源：BlockSec 内部标签库<br>**交易详情**<br>⛓️ 链：{链 Logo}{链名}<br>📥 转出地址：[TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9](https://tronscan.org/#/address/TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9)<br>🎯 转入地址：TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC<br>🔗 交易哈希：[3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35](https://tronscan.org/#/transaction/3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35)<br>💰 交易金额（美元）：$50,000<br> 🕒 交易时间：2025-10-20 07:11:48（UTC）<br>**\[在 Phalcon Compliance 中查看完整风险详情\]**<br>(Compliance transaction lite scan 链接) | 和其他通知渠道消息的主要不同：<br>*   点击 Alert ID 链接跳转 Network 平台自动展示对应 Alert 详情。**同时该链接支持预览 Network 资金流图。**<br>    <br>*   不在消息中直接展示 fund flow 图<br>    <br>*   View full risk details in Phalcon Compliance / 在 Phalcon Compliance 中查看完整风险详情   <br>    要以消息 button 的形式展示。如下图![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4jKqm0bPPBz8Ynw1/img/4f462cad-aa55-4aee-a70a-be59474651db.png) |

#### Slack、Lark、Email

| 英文 | 中文 | 中英文区别说明 |
| --- | --- | --- |
| 🚨Detection of Illicit Funds in Incoming Transfer **(Sanctioned and Blocked)**<br>Alert ID: 3a0d14f0-4650-4abe-abbe-a9daf3edd46d<br>**Risk Information**<br>*   Risk Type: **Sanctioned, Blocked**<br>    <br>*   Information Source: BlockSec Internal Label Library<br>    <br>**Transaction Details**<br>*   From address: [TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9](https://tronscan.org/#/address/TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9)<br>    <br>*   Monitored address: Label \| TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC (Note)<br>    <br>*   Transaction hash: [3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35](https://tronscan.org/#/transaction/3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35)<br>    <br>*   Value (USD): $50,000<br>    <br>*   Time: 2025-10-20 07:11:48 UTC<br>    <br>**\[View full risk details in Phalcon Compliance\]**<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/8da017d8-8a16-4cc4-8f66-8bf1fd6c0d0a.png) | 检测到非法资金流入交易（**Sanctioned, Blocked**）<br>警报 ID：3a0d14f0-4650-4abe-abbe-a9daf3edd46d<br>**风险信息**<br>*   风险类型：**Sanctioned，Blocked**<br>    <br>*   信息来源：BlockSec 内部标签库<br>    <br>**交易详情**<br>*   转出地址：[TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9](https://tronscan.org/#/address/TUVjMdWHQ6RX1xC9WZmWvPy35A73dmwhC9)<br>    <br>*   监控地址：Label \| TMEKGe8Sa6aTLdD6qnNr87BZkpmTgKrbjC（Note，如有）<br>    <br>*   交易哈希：[3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35](https://tronscan.org/#/transaction/3de7809248060ebe920999f02090b816d2b36a801389e96b5575ce5fdceeae35)<br>    <br>*   交易金额（美元）：$50,000<br>    <br>*   交易时间：2025-10-20 07:11:48（UTC）<br>    <br>**\[在 Phalcon Compliance 中查看完整风险详情\]**<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952BDbeAMlap/img/8da017d8-8a16-4cc4-8f66-8bf1fd6c0d0a.png) | *   标题的括号中展示本条 Alert 中包含的所有 Risk Indicator，全部用 、拼接。<br>    <br>*   View full risk details in Phalcon Compliance / 在 Phalcon Compliance 中查看完整风险详情   <br>    **用按钮的形式展示** |

# 主页面-Add Monitoring Address弹窗

# 主页面-概览指标区

| module | key | text | cn\_text | description |
| --- | --- | --- | --- | --- |
| alerts\_overview | section.title | Overview | 概览 | 概览指标区标题 |
| alerts\_overview | metric.total\_alerts.label | Total Alerts | 告警总数 | 当前账户下累计触发的告警总数 |
| alerts\_overview | metric.alerts\_last\_7\_days.label | Alerts in Last 7 Days | 近 7 天告警数 | 最近 7 天累计触发的告警数量 |
| alerts\_overview | metric.addresses\_impacted.label | Addresses Impacted | 命中地址数 / 监控地址总数 | 被命中过的地址数 / 监控地址总数（进度条或环形占比） |
| alerts\_overview | metric.total\_alert\_value\_usd.label | Total Alert Value (USD) | 告警总入金金额（USD） | 所有 Alert 中涉及的入金金额累计（USD） |
| alerts\_overview | metric.top\_risk\_types.label | Top Risk Types | 高频风险类型 | 近 7 天内出现频率最高的风险类型（名称 + 百分比） |
| alerts\_overview | metric.avg\_alert\_value.label | Avg Alert Value | 平均告警入金金额 | 单条 alert 的平均入金金额 |
| alerts\_overview | metric.avg\_alert\_value.value\_template | Avg Alert Value {amount} | 平均告警入金金额 {amount} | 展示模板；amount 例：$48,200 |
| alerts\_overview | metric.last\_alert\_time.label | Last Alert Time | 最近一次告警时间 | 展示距离最近一次告警的时间 |
| alerts\_overview | metric.last\_alert\_time.value\_template | Last Alert {duration} ago | {duration} 前发生告警 | 展示模板；duration 例：2 hours / 15 minutes |

# 主页面 - Triggered Alerts模块

## 页面文案

| module | key | text | cn\_text | description |  |
| --- | --- | --- | --- | --- | --- |
| triggered\_alerts | section.title | Triggered Alerts | 已触发告警 | Triggered Alerts 模块标题 |  |
| triggered\_alerts | section.desc | Historical alerts triggered by your monitoring rules. | 由监控规则触发的历史告警记录。 | 模块说明（可选） |  |
| triggered\_alerts | badge.read\_only | Read-only | 只读 | 只读标签（可选） |  |
| triggered\_alerts | table.col.related\_alert | Related Alert | 关联告警 | 展示 Alert ID，如 #ALERT-20230701-001 |  |
| triggered\_alerts | table.col.address | Address | 地址 | 展示完整或截断地址；hover 查看完整地址 |  |
| triggered\_alerts | table.col.risk\_type | Risk Type | 风险类型 | 风险类型标签，如 Illicit Funds / High Risk |  |
| triggered\_alerts | table.col.intelligence\_source | Intelligence Source | 情报来源 | Public / Private |  |
| triggered\_alerts | intelligence\_source.public | Public | 公开 | 情报来源枚举 |  |
| triggered\_alerts | intelligence\_source.private | Private | 私有 | 情报来源枚举 |  |
| triggered\_alerts | table.col.triggered\_time | Triggered Time | 触发时间 | 触发时间列 |  |
| triggered\_alerts | table.col.actions | Actions | 操作 | 操作列 |  |
| triggered\_alerts | action.view\_details | View Details | 查看详情 | 进入单条告警详情页 |  |
| triggered\_alerts | tooltip.full\_address | Full address | 完整地址 | hover 查看完整地址提示（可选） |  |

提示文案

# 导航栏

## Notification Channels（通知渠道）

### 页面文案

| key | text | cn\_text | description |
| --- | --- | --- | --- |
| key | text | cn\_text | description |
| btn.create | Create Channel | 创建 | 管理页与弹窗主操作按钮 |
| title.create | Create Notification Channel | 创建通知渠道 | 创建弹窗标题 |
| label.channel\_type | Channel Type | Channel 类型 | 字段标签 |
| placeholder.channel\_type | Select Channel | 选择 Channel | 下拉占位 |
| option.channel\_type.email | Email | 邮箱 | 下拉选项 |
| option.channel\_type.telegram | Telegram | Telegram | 下拉选项 |
| option.channel\_type.slack | Slack | Slack | 下拉选项 |
| option.channel\_type.lark | Lark | Lark | 下拉选项 |
| label.email | Email Address | 邮箱地址 | Email 输入框 |
| label.verification\_code | Verification Code | 验证码 | 验证码输入框 |
| btn.send\_code | Send Code | 发送验证码 | 发送验证码按钮 |
| label.channel\_name | Channel Name | 渠道名称 | 通用名称输入框 |
| title.telegram\_config | Telegram Configuration | Telegram 配置 | Telegram 配置区标题 |
| label.telegram\_chat\_type | Chat Type | 聊天类型 | Telegram Chat Type |
| option.telegram\_chat\_type.user | User | 用户 | Chat Type 选项 |
| option.telegram\_chat\_type.group | Group | 群组 | Chat Type 选项 |
| label.telegram\_chat\_id | Telegram Chat ID | Telegram Chat ID | Chat ID 输入框 |
| link.telegram\_get\_chat\_id | Get Chat ID | 获取 Chat ID | Telegram 辅助入口 |
| hint.slack\_config | Add @PhalconAlertBot to your workspace and authorize a specific channel to receive notifications from {{Channel Name}} | 将 @PhalconAlertBot 添加到工作区，并授权频道接收 {{Channel Name}} 的通知 | Slack 配置说明 |
| btn.connect\_slack | Connect Slack | 连接 Slack | Slack 授权按钮 |
| label.lark\_webhook | Webhook URL | Webhook 地址 | Lark Webhook 输入框 |
| label.lark\_signature | Signature | 签名 | Lark Signature 输入框 |
| link.lark\_help | Help doc | 帮助文档 | Lark 帮助文档链接 |
| btn.cancel | Cancel | 取消 | 关闭弹窗 |
| action.delete | Delete | 删除 | 删除 Channel 操作 |

### 提示文案

| key | text | cn\_text | description |
| --- | --- | --- | --- |
| success.create | New Channel Created! | 新 Channel 创建成功 | 创建成功提示 |
| success.delete | Channel Successfully Deleted! | Channel 删除成功 | 删除成功提示 |
| error.email\_invalid | Please enter a valid email | 请输入有效的邮箱地址 | 邮箱格式错误 |
| error.code\_invalid | Please enter a valid code | 请输入有效的验证码 | 验证码格式错误 |
| error.channel\_name\_required | Please enter Channel Name | 请输入 Channel 名称 | 必填校验 |

7.2