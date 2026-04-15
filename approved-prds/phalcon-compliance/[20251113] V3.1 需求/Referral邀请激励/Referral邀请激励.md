# Referral邀请激励

# 1.背景

Phalcon Compliance 当前用户增长主要依赖官网注册和内容引流，缺乏用户主动传播动力。  
通过引入「邀请推荐机制」，目标是让现有用户成为主动传播者，实现用户裂变增长和自然转化提升。

**核心目标：**

*   激励活跃用户拉新，提高注册量与留存率；
    
*   通过返利激励提升邀请人用户的订购转化率；
    
*   构建稳定、可追踪的推荐闭环体系；
    
*   支持未来的KOL、合作伙伴分级激励体系扩展。
    

# 2.用户角色定义

*   **邀请人**：已注册用户，通过专属邀请码邀请他人注册。 
    
*   **被邀请人**：通过邀请码完成注册的新用户。
    
*   **系统管理员**：负责配置奖励规则、管理返利结算与用户状态。
    

# 3.Referral 机制

*   每位邀请人可生成一个专属邀请码或邀请链接
    
*   被邀请人注册后并完成初次扫描之后，双方各获得3次免费扫描额度（当月有效）
    
*   若被邀请人完成付费，邀请人获得10%金额作为账户余额（3个月有效，可抵扣充值）如账户余额达到100美金，可以人工申请提现。
    
*   所有注册用户均可自助生成邀请码、查看奖励、生成海报
    

# 4.初期方案

目标：验证邀请机制和奖励逻辑，让推广链接可用， 统计邀请效果并展示给用户

## 4.1 奖励规则

### 邀请未注册的用户

*   **注册奖励**
    
    *   被邀请人注册++并完成第一次扫描++后，邀请人、被邀请人各获得额外 **3****次免费深度扫描**。
        
    *   系统在 Usage & Billing → Screening Count 中显示奖励次数。
        
*   **付费返利**
    
    *   未订阅的用户通过邀请人链接充值或订购，或在支付页面填入邀请码，可获得10%优惠；
        
    *   被邀请人完成充值或订阅后，**邀请人**获得被邀请人订阅plan金额10%作为账户返利余额；如账户余额达到100美金，可以在平台填表申请提现，提现有效期在2025.12.31以内，由blocksec人工处理返现。
        
    *   返利余额可在充值/订阅时直接抵扣，**有效期 3 个月**。
        

### 邀请已注册未订购的用户

背景：在 Referral 初期阶段，邀请主要面向新注册用户。  
但在成长期，会出现以下情形：「某用户已注册 Phalcon，但未被任何人邀请，希望通过输入邀请码享受邀请优惠，同时让邀请人获得返利。」

1.  允许 **已注册用户**登录时/结算时手动输入邀请码 或 通过邀请链接自动绑定邀请关系。
    
2.  被邀请人完成绑定后立刻++解锁特色功能++：如可创建一个blacklist，限时使用3天
    
3.  被邀请人结算时，
    
    1.  被邀请人++享受购买优惠++（ 10% off）
        
    2.  邀请人获得当次订单金额10%返利及3次额外quota奖励。
        

## 4.2 用户流程

### 邀请人流程（Referrer）

1.  **生成邀请链接或邀请码**
    
    *   入口：Usage & Billing 的affiliate program活动banner / 菜单栏 Invite 按钮。
        
    *   系统生成带 ref 的链接或邀请码。
        
2.  **分享给对方**
    
    *   可复制链接、下载二维码、发送邀请码。
        
3.  **被邀请人注册或绑定邀请码后**
    
    *   **1：注册奖励**
        
        *   邀请人获得 +3 次扫描。
            
    *   **2：首次付费返利**
        
        *   邀请人获得邀请人订单金额 10% 的返利余额。
            
        *   若对方是已注册但首次订购，还额外获得 3 次扫描。
            
4.  **邀请人收到通知弹窗**
    
    *   注册奖励 →  免费扫描到账
        
    *   付费返利 →  返利到账
        
    *   即将到期 → 返利余额到期提醒
        
5.  **邀请人可执行操作**
    
    *   在结算时使用返利余额。
        
    *   继续邀请更多用户。
        

### 被邀请人流程（Invitee）

被邀请人有三种起始状态：

#### ① 未注册用户

1.  点击邀请链接 → 跳到注册页（自动带 ref）。
    
2.  注册完成后，自动绑定邀请关系。
    
3.  登录后弹出奖励弹窗。
    
4.  可直接使用扫描功能。
    
5.  若之后付费：
    
    *   被邀请人享受该笔订单 **10% 优惠**。
        
    *   邀请人获得 订单金额**10% 返利余额**。
        

#### ② 已注册但未订购用户

1.  点击邀请链接 → 自动跳到绑定邀请码页。  
    或  
    手动在设置页 / 结算页输入邀请码。
    
2.  输入邀请码后：
    
    *   解锁一个特色功能（如：可创建 blacklist 3 天）。
        
    *   结算订购时可享受 **10% off**。
        
3.  若该用户在绑定后首次付费：
    
    *   被邀请人获得优惠。
        
    *   邀请人获得 **10% 返利 + 3 次深度扫描奖励**。
        

#### ③ 已注册且已订购用户

*   点击邀请链接 → 弹窗引导邀请新人
    

## 4.3 功能页面

Referral 模块在初期阶段面向所有用户开放。此阶段的目标是快速验证邀请机制、奖励逻辑与展示效果，不改动架构结构，仅通过轻量入口让用户能：生成专属邀请链接 / 二维码、分享给被邀请用户、查看注册与返利结果。

**目标：**

*   让已注册登入的用户能够在平台上快速生成专属邀请链接；
    
*   链接可被分享，系统自动记录邀请关系；
    
*   不新增新菜单，入口轻量、显眼但不干扰主流程；
    

### 4.3.1 邀请入口

####  入口1 Usage & Billing  页面

位于  **Usage & Billing** 页面顶部卡片组下方     形式：活动banner

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/2b04036c-ac2c-4dd0-b9ef-2ed7e50e1040.png)

```plaintext
┌──────────────────────────────────────────────┐
│ 🎁 Invite users & earn rewards! Each signup gives you 
+3 free scans. │
│ [Generate Invite Link]                                               │
└──────────────────────────────────────────────┘

```

*   **点击行为**：
    
    *   打开弹窗（Invite Modal）展示专属链接与二维码
        
    *   弹窗内容详见下节
        

#### 入口 2 菜单栏Invite 按钮

invite🎁小按钮，放在菜单栏message center上方

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/1e728109-b576-4581-9dba-3adb1e779eec.png)

*   Tooltip 提示：`🎁 Invite & Earn`
    
*   点击后弹出以下弹窗内容
    

**显示逻辑：**

*   鼠标悬停 Tooltip 提示：
    

> “Invite friends and earn free scans & rebates!”

### 4.3.2 Invite&Reward核心模块

#### Invite tab

点击🎁出现的弹窗模块。在同一个弹窗内部提供invite 和 reward两个tab, 参考6.样式参考

**交互说明**

*   点击\[Copy Link\]：复制链接后 toast “Link copied!”
    
*   迪纳基\[Generate QR\]：生成并可下载 PNG
    
*   `[Invite now]`：调用系统分享（或打开分享渠道弹层：微信 / X / WhatsApp / 邮件）
    
*   `[View details]`：跳转 Usage & Billing，锚点到 Screening Count & Rebate Balance
    
*   顶部 `[✕]` 可关闭；关闭/点击视为已读（写入通知状态）
    

:::
Gift 3 free certified reports, get up to $100🏆

Invite friends to screen their counterpart address & Txn with Phalcon Compliance. Get 3 free reports, plus 10% of every payment they make on Phalcon Compliance.
:::
:::
\[  Invite Link        [https://app.blocksec.com/phalcon/v2/register?ref={{ref}](https://app.blocksec.com/phalcon/v2/register?ref={{ref})}  \]

 \[Copy Link\]   \[Generate Poster\]    

四种社交媒体快捷分享方式
:::
:::
**How it works**

• Invite friends → both get +{{signup\_scan\_count}} 3 free reports   (valid for  7 days.

• Earn **up to 20% of their order amount** on every purchase.  

• 2025 Special: cash-out up to $100
:::

**示意图**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/5ab13438-0787-4876-b636-5037c17fcdd5.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/8bbe0bf8-a811-4b1e-b860-474d5af74ec1.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/f2544dc4-5cb9-4702-ae6e-961edc1b29d5.png)

点击invite now，出现几种KOL传播的主要渠道，希望实现一键分享

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/602c6fdf-482e-4677-b2a4-bae2d9b2039a.png)

在返利余额卡片下方，用警示色（如黄色或红色）提示。例如：“$$\[X\] will expire on \[Date\]”。

#### Rewards Tab

 Your current rewards

• Referral balance: ${{rebate\_balance}} {{if exp\_soon}}(expires {{rebate\_expire}}){{/if}}

 • Free scans: {{free\_scans\_balance}}

:::
Notes：

Rewards usable at checkout. 2025 rewards: 20% cash-out if credits ≥ $100 by Dec 31, 2025.
:::
:::
**Cash Out**
:::

**动态字段**

| **字段** | **示例** | **说明** |
| --- | --- | --- |
| signup\_scan\_count | 3 | 注册即时奖励次数（你+被邀请人各得） |
| rebate\_rate | 20 | 返利比例 |
| rebate\_ttl | 1 months | 返利有效期 |
| rebate\_cap | $100 | 返利上限 |
| cap\_period | month | 上限周期（如月度） |
| rebate\_balance | 12.00 | 现有返利余额 |
| rebate\_expire | 2026-01-10 | 余额到期时间 |
| free\_scans\_balance | 8 | 账户当月剩余免费扫描 |
| ref | kolemail@example.com | 用于生成专属链接的标识 |

#### 余额提现 Cash Out

| 状态 | 条件 | 按钮样式 | Hover 文案 |
| --- | --- | --- | --- |
| **Disabled** | 返利余额 < $100 | 按钮置灰、不可点击 | “Need $X more to cash out. Hit $100 by 12/31 or lose your cash-out chance!” |
| **Enabled** | 返利余额 ≥ $100 | 高亮可点击 | “Ready to cash out. Deadline: 2025/12/31.” |

*   在reward页面显示Cash Out按钮
    
    *   **Cash Out按钮**
        
    *   **点击cash out 出现返现申请单**
        
        *   返现申请单提交成功后：
            
            *   表单关闭，页面显示成功提示："Cash Out submitted successfully! Your request is being processed and usually takes 3 business days."
                
            *   表单信息在后台发送给phalcon\_support@blocksec.com邮箱
                
            *   原 **Cash Out** 按钮状态：
                
                *   按钮置灰 (Disabled)。
                    
                *   按钮文案更新为：**"Pending Review"** 或 **"Cash Out Submitted"**。
                    
                *   下方可显示提现截止日期状态：**"Your cash out deadline was successfully reserved."**
                    
        *   返现申请单点击返回键可以回到invite & reward模块
            

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/a70e3738-a3af-48c5-af1d-2c42cec93ea4.png)仅为示意，返现申请单内容以下面表格为准。

| **Field Name** | **Copy** | **Type/Options** | **Notes** |
| --- | --- | --- | --- |
| **Title** | Cash-out Request | Text |  |
| **Intro Text** | Thanks for sharing Phalcon Compliance! We appreciate your support.<br>You currently have **$\[User\_Rebate\_Balance\] USD** available for cash-out.<br>To proceed, just tell us how to reach you — our team will follow up directly to arrange the payment. | Text |  |
| **Your Name** | Please tell us your name. | Text Input | Placeholder: "Enter your name" |
| **How should we contact you?** | Select your preferred way for us to reach you: | Dropdown | Options: Email, Telegram, WeChat, WhatsApp |
| **Your Contact Details** | Enter your email address / Telegram ID / X account / Linkedin ID | Text Input | Dynamic placeholder based on "Contact Method", e.g., "Enter your email address" or "Enter your Telegram username" |
| **Submit Button** | Submit | Button | Enabled when "Contact Method" and "Your Contact Details" are filled |
| **Next Steps** | After submitting, our support team will contact you within 2-3 business days to verify your information and arrange your payout. | Text |  |
| **Need help?** | If you need assistance, feel free to reach us directly:<br>Support Email:phalcon\_support@blocksec.com<br>Telegram: [t.me/BlockSecTeam](t.me/BlockSecTeam)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/f43f5da7-d593-4eea-b70a-7be3246aa51a.png) | Text (includes links or contact details) |  |

**返现申请提交成功，自动发送邮件到用户邮箱：**

:::
**Subject:** Your Cashback Request Has Been Received

**Body:**

Hi {Name},

Thank you for sharing Phalcon Compliance!  
We’ve received your cashback request, and it’s now under review. Our support team will contact you within **2–3 business days** regarding the next steps.

If you have any questions in the meantime, feel free to reply to this email.

Best regards,  
Phalcon Compliance Support Team
:::

### 4.3.3 邀请成功/奖励到账banner

通知推送一般收录进invite& rewards模块，当有新通知时🎁右上角出现小红点

邀请成功/奖励到账banner在下列时机出现，允许用户手动关闭

|  | 显示对象 | banner提示时机 | 文案 |
| --- | --- | --- | --- |
| 1 | 邀请人 | banner提示时机：邀请人邀请的新用户<br>注册并第一次扫描后 | 🎉 New signup from your invite link! You’ve earned 3 extra free screens. |
| 2 | 邀请人 | 邀请人邀请的新用户<br>注册并完成第一单订购后 | 💰 Your invitee just made a purchase! You’ve earned 10% cashback on their order. |
| 3 | 通过邀请链接进入的新用户（被邀请人） | 注册并完成第一次登入<br>【这种情况下不显示5.新用户欢迎文案 | 🎉You received 3 free screens from referral program. Complete your first screen to claim them. |
| 4 | 通过邀请链接进入的新用户被（被邀请人） | 注册并完成第一次扫描 | 🎉 You’ve got 3 free screens and a 10% off voucher from \[in\*\*\*\*@email.com\]. |
| 5 | 新用户 | 注册完毕第一次登入时 | Welcome aboard — enjoy clear risk results for every address and transaction. Start screening now! |
| 6 | 访客 | 第一次登入时 | Welcome to Phalcon Compliance! Check risk for addresses and transactions -  Sign up to get started. |

##### 注册奖励到账弹窗 

触发场景：被邀请人完成注册 → 登录成功后自动弹出。以toaster形式

:::
🎉 You’ve earned 3 free scans from \[Inviter Name\]’s invitation.                    \[✕\] 
:::

##### 已订阅用户点击邀请链接

不做任何弹窗提示

##### 返利到账提醒弹窗

触发场景：被邀请人完成首笔订阅/充值 → 邀请人返利到账；同时被邀请人可看到“你已获得返利抵扣额度”

:::
💰 You just earned ${{amount}} in referral credits!                                                \[✕\]

Usable at checkout — don’t let it go to waste.                 
:::

点击Apply credits at checkout：跳转至pricing plan 页面，用户结账时自动填充抵扣额度；

点击View details**：**跳转至 usage &billing区块查看余额明细；

点击View in Message Center: 打开消息中心对应记录

##### 返利余额即将过期弹窗

触发场景：返利余额剩余 ≤ 3 天时；登录即触发弹窗。

:::
⚠️ Your ${{amount}} credit expires in {{days}} days — use it now! \[✕\]

 Apply your credits before {{expire\_date}} to avoid expiration.      

 \[Use credits now\]              \[View details\]                      
:::

点击Use credits now, 跳转到pricing plan，自动应用抵扣；

View details,打开 Usage & Billing 页面查看返利余额详情；

View in Message Center,打开消息中心查看过期提醒记录；

##### 返利余额到期提醒

:::
⚠️ Your ${{amount}} credit expires in {{days}} days — use it now! 

Apply your credits before {{expire\_date}} to avoid expiration.           

 \[Use credits now\]     \[View details\]   
:::

### 4.3.4 注册页面-推荐码填写

在当前的账号密码输入栏下方新增“Referral Code”。样式可参考第7章

*   手动输入 或 自动填入（通过邀请链接进入时）
    

*   按下 "Apply" 会调用后端校验
    

### 4.3.5 结账页面-折扣/返利金额抵扣

结算页需要支持以下功能

1.  **邀请码绑定**
    
    *   新注册用户自动填入/手动输入邀请码
        
    *   点击apply开始校验
        
    *   校验成功首购享 10% OFF（被邀请人）
        
        *   点击 **Apply** 校验逻辑：是否为合法邀请码？是否属于邀请用户？当前用户是否符合“首购”？
            
        *   若成功 → 显示 **10% OFF** 并锁定优惠（不可与平台券叠加
            
        *   校验失败 → 清晰错误信息Invalid Promo Code
            
2.  **优惠活动区****Promotions & Discounts**
    
    *   可选金额券/折扣券。与邀请码折扣不可叠加
        
    *   **券1**：**Invite Reward（返利余额核销）**
        
        *   可选，使用邀请返利余额抵扣订单金额。默认勾选全部余额，可手动取消勾选。
            
            *   [勾选后，订单金额随之修改。](https://www.figma.com/design/xzBsa8kvbwTmOy1yMlacwV/%F0%9F%94%B6-Compliance---%E8%87%AA%E5%8A%A9%E8%AF%95%E7%94%A8%E4%B8%8E%E8%AE%A2%E9%98%85?node-id=1-5&p=f&t=BOx0fa1nMaL9c3im-0)如：原套餐金额为699，返现余额19，抵扣后结账金额为680
                
            *   **模块标题：** `Account Balance`
                
            *   **勾选文案：** `Use referral balance (Available: $180)`
                
    *   **券2:  Limited Promotion**（未来如有，平台活动优惠券等）
        

**邀请码适用范围：**

| **用户类型** | **是否可使用邀请码** |
| --- | --- |
| 新注册用户（未被邀请） | 可使用，绑定邀请关系，享受 10% 优惠 |
| 已注册但未订阅过的旧用户 | 不可再输入新的邀请码（灰化） |
| 注册时已经绑定过邀请码的用户 | 自动填入邀请码 |
| 已经完成首次付费的用户（续费） | 邀请码不再适用 |

**交互逻辑：**

*   用户填写邀请码 后，将自动触发一次验证
    

*   若有效 → 显示 10% Invitation Discount，用户可勾选，点击“Apply”使用优惠
    

*   若无效 → 显示错误提示，输入框保持可编辑。
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/c9decb51-1ca7-4640-b8c2-4aa6cdb6ab78.png)
    
    ## 4.4 埋点补充
    
    *   事件：
        
        *   kol\_invite\_link\_created（后台生成）
            
        *   invitee\_registered（新用户注册）
            
        *   invitee\_paid（新用户付费）
            
        *   reward\_granted（奖励发放）
            
    *   数据字段：referrer\_email, invitee\_id, reward\_type, amount, valid\_until, timestamp
        

# 5.防作弊与风控策略（本期暂不做限制）

提防同一人创建多个账号相互邀请，以获取注册奖励或返利的情况

*   **同设备/同IP注册仅计一次有效邀请**：记录浏览器指纹 + 设备指纹并拒绝在同一指纹上发放邀请奖励或标记为可疑。每次生成邀请/绑定时写入 device\_fingerprint；若已有另一个账号在同一 fingerprint 上获得奖励，拒发或进入人工审核。
    
*   **手机/邮箱验证**强制要求绑定手机号或邮箱验证（短信或邮件）才能生效邀请或领取奖励。阻挡一次性/临时邮箱注册。
    
*   **支付链路校验**：对付费返利，要求被邀请人的首笔付费完成且通过风控（非退款、非 chargeback），返利延迟（例如等待 7 天）再发放以防止退款滥用。
    
*   **频率/时间阈值**：新账号在短时间内完成多次邀请—注册—付费则标记可疑（例如 24 小时内同一 inviter 的 5 次成功注册触发审核）。
    
*    **账户关联历史**：若两个账号共享相同支付方式（卡号后 6 位）、同一收件地址、或同一设备指纹，则拒绝奖励或降额。
    

# 6.Affiliate Program参考

## Manus样式参考

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/07d003f1-3578-4cfb-8dac-1e2837d0cc2c.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/198774a3-718f-45e9-a25d-19d0324fe33f.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/e0816475-1ad7-4c3a-be37-507dd93d7ee8.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/729fe805-1913-4b80-8c3f-0f322bc74723.png)

点击redeem可以输入活动促销码，获得一些点数

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/cfcc4e7a-7e6e-48b9-8782-66f867442a70.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/afaff3e5-df40-467f-8a3f-6e380eb1adf9.png)

## Miro样式参考

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/6378e49e-1ad3-47a6-a31d-46d6a18d4c7c.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/1a60c35e-456c-493e-a9fe-3a696bd3bfdd.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/db2f0526-c7ab-41a1-8bae-89ba1037ab29.png)

## Fellou 样式参考

![/Users/eureka266/Library/Containers/com.bytedance.macos.feishu/Data/Library/Application Support/LarkShell/sdk_storage/698ecf9b05d146c5e3b51b1aebb32a12/resources/images/img_v3_02qd_00a2452a-e8b7-4bda-aafc-3ba20fae15hu.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/3458f89d-d23f-47cc-abb5-76c1e4aa231e.png)

![/Users/eureka266/Library/Containers/com.bytedance.macos.feishu/Data/Library/Application Support/LarkShell/sdk_storage/698ecf9b05d146c5e3b51b1aebb32a12/resources/images/img_v3_02qd_64216df9-8097-4641-98c9-853315d78ehu.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/ea96eb0d-6b47-4c29-8366-01e5eee8636c.png)

## Jazzy样式参考

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/54Lq35o8pJWp1l7E/img/bd770d18-478b-4e71-a7f0-7b6e36e9d8bd.png)