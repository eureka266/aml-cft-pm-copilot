# \[20260305\]  产品内部AI agent

## 项目背景与目标

### 1.1 背景

为了降低 Phalcon Compliance 平台的获客成本，提升 Free 用户向 付费订阅 版本的转化率，需要在平台内嵌入智能客服 Agent，实现自动化线索清洗与初步沟通。

### 1.2 目标

*   **转化率提升**：引导 Free 用户体验核心功能并申请 Demo。
    
*   **企业线索沉淀**：自动化识别企业级高价值客户并推送至销售团队。
    
*   **即时响应**：提供 7x24 智能服务，减少人工客服压力。
    

## 用户故事

*   **用户**：希望在查看链上风险时能得到实时指导，以便快速理解报告含义。
    
*   **售前：**希望通过AI找用户了解清楚需要的功能、用量，帮用户快速决策选什么套餐
    
*   **销售**：希望系统能自动筛选出有批量对接需求的企业客户，并立即通知我，以便我快速跟进。
    

## 功能需求

mvp版本项目已上传github https://github.com/blocksecteam/Phalcon-Compliance-Chatbot-v2    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/4maOgXbb1aYEjlWN/img/bb778e16-e9af-429e-8c33-66a2f58b2d7f.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/4c59139d-de89-44f0-abea-a12f1a5e53f1.png)

### 3.1 前端 UI 与交互设计

**3.1.1 聊天界面**

*   **悬浮窗位置**：页面右下角，距离底部 24px，距离右侧 24px。
    
*   **初始状态**：显示圆形 AI 图标，悬停时显示提示文案：“Hi, need help with compliance?”
    
    *   显示三个预设选项，点击可直接跳转相应链接或触发表单填写
        
        *   Human Support
            
        *   User Manual
            
        *   Join Telegram Group 
            
*   **点击交互**：
    
    *   点击图标打开对话框，点击页面其他地方对话框自动收起
        
        *   标题栏：显示 Agent 名称，右侧提供关闭图标和历史会话入口。
            
        *   输入区：文本输入框，右侧提供发送按钮（发送按钮使用品牌色背景或图标）。
            
        *   AI开场白：用户打开对话框的时候，AI自动发送两条
            
*   **消息展示**：
    
    *   AI 消息：左侧对齐，支持 Markdown 格式。当 AI 正在生成回复时，消息气泡内显示加载动效（如三个脉冲点）。
        
    *   用户消息：右侧对齐。
        
*   **状态显示**：输入框内部显示 "Ask me anything in any language..." 状态。输入框下方显示Powered by BlockSec 或者 AI generated content may be inaccurate?
    

**3.1.2 历史会话**

查看同用户id下的历史会话列表，支持关键词搜索，点击某会话可进入历史会话详情

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/1b2fb292-1a52-42c4-98d4-7f8ed820fad2.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/e51f83ee-29e8-4758-8242-7b384cf8acb7.png)

### 3.2 语言策略与话术规范

*   **默认语言**：**英文**。
    
*   **语言镜像**：用户用什么语言提问，AI就用什么语言回答
    
    *   语言检测基于用户当条消息，而非历史记录。
        
    *   混合语言输入（如中英夹杂）时，以用户消息中**占主导的语言**回复。
        
    *   不主动切换语言，不对用户的语言选择作出评论。
        
    *   多轮对话中，每轮独立判断语言，跟随用户切换。
        
    *   不支持的语言（如小语种无法准确处理时），回退至英文并简短说明。
        
*   **话术规范**：
    
    *   语气专业、克制。
        
    *   结构：一句话直接回答 + 2-3个核心点列表 + 1个明确CTA (Call to Action)。
        
    *   单段不超过3句话。
        

### 3.3 意图识别与业务逻辑

Agent 需根据输入内容进行场景分类：

**Enterprise:**

用途：标记是否已出现企业级采购或规模信号。

如果 {{enterprise\_signal}} == true：

停止技术细节追问， 先询问用户的联系方式，得到回复后，把用户联系方式纳入钉钉消息，触发转人工流程，使用webhook向钉钉发送群消息。

如果发送成功，告诉用户已转接团队；

如果发送不成功，自动重试3次。仍不成功，直接向用户建议加入telegram社区或 t.me/BlockSecTeam 或联系telegram账号@rubyxuu以获得快速联系。

**钉钉消息结构：**

触发信号：并发、SLA、对公支付、API/SDK、批量、>1000/月

1. 触发销售Webhook

2. 引导人工对接

**Realtime**

触发意图：交易扫描、实时、风险监测、监控

执行动作：1. 强调“毫秒级”标签

2. 引导申请Demo

**One-time**

触发意图：背调、查地址、导出报告

动作：

1. 介绍KYA/KYT报告

2. 引导体验免费额度

### 3.4 转人工自动触发

#### 场景 1：用户主动请求转人工

触发条件：

*   用户输入包含关键词（转人工 / 人工 / human / specialist / contact sales 等）
    
*   用户点击chatbot首页的【Chat with us】气泡
    

行为：立即弹出联系方式表单

钉钉标题：用户请求转人工

钉钉消息内容：需求概括、判定原因、用户联系方式、会话详情链接。

#### 场景 2：检测到企业级信号

触发条件：LLM 结构化输出中 enterprise\_signal = true（需要的扫描次数>9000/年/ API 接入/ 合同需求 / 私有化部署等）

行为：LLM 回复 + 弹出联系方式表单

钉钉标题：企业线索转人工

钉钉消息内容：需求概括、判定原因、用户联系方式、会话详情链接。

用户消息：提示已将需求同步至专家团队，并引导用户留下邮箱或Telegram账号。

#### 场景 3：AI 无法回答

触发条件：LLM 返回的 JSON 解析失败，或 JSON 中 response 字段为空

行为：显示兜底话术 + 弹出联系方式表单

钉钉标题：AI无法回答转人工

钉钉消息内容：当前会话内容概括、用户联系方式、会话详情链接

联系方式表单：

| **字段** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| **Name** | text | 必填 | 用户姓名 |
| **Email** | email | 选填 | Email 地址 |
| **Telegram** | text | 选填 | Telegram 用户名 |
| **WhatsApp** | text | 选填 | WhatsApp 号码 |
| **Wechat** | text | 选填 | 微信号 |

## 后台管理系统

接口文档见[《Agent管理后台 · 后端 API 需求文档》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTGqzavGrVA7depqY?cid=643145581:783724333&corpId=ding11de5443ac093187bc961a6cb783455b&doc_type=wiki_doc&iframeQuery=utm_medium=im_card&utm_source=im&utm_medium=im_card&utm_scene=team_space&utm_source=im)

### 会话管理

后台管理系统由会话管理和召回测试两个模块构成。

会话管理模块展示会话简介（llm生成），会话ID,联系方式，是否转人工，消息类型（1.转人工；2.AI无法解答；3.企业级信号），会话轮次

模块用途：集中查看所有真实会话，便于排查问题、复盘用户需求、追踪转人工结果。

本次改动：会话不再只是简单列表，而是要能按 Agent、渠道、版本、会话状态等维度筛选。

建议新增字段：所属 Agent、来源渠道、用户类型、当前状态、是否转人工、满意度、所属版本。

价值：帮助团队定位问题到底出在哪个 Agent、哪个入口、哪个版本，而不是只看到一堆零散对话。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/d6371525-156a-4d14-8e41-3faba5d42ee3.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/64f2adb4-d17b-4ad1-9703-525ae82f5468.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/2792c18a-b37f-4191-b5f4-a30b6227af51.png)

### 测试模块

用途：在发布前后验证不同 Agent 是否按预期工作。

第一类是问答测试：看回答内容是否正确、是否完整。

第二类是路由测试：看问题是否被分配给正确的 Agent。

第三类是场景回归测试：看多轮对话在真实业务流程里是否顺畅。

价值：让测试不再只盯回答文字本身，而是覆盖整个使用过程。支持批量导入测试集

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/abde84b6-aa54-4500-8893-fd407daefe4c.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/f6e43c1b-b432-42ca-9913-fdf23b7c8401.png)

### 用户反馈

模块用途：统一查看用户反馈，并将问题归类，推动后续优化。

本次改动：从“只看点赞和点踩”，升级为“看反馈 + 看原因 + 看建议动作”。

建议新增问题归类：答非所问、内容不准确、没有解决问题、应转人工未转、语气不合适、信息不够明确。

价值：让反馈能真正进入优化闭环，而不是停留在情绪层面的好坏判断。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8oLl952zjL4Ydlap/img/6e7f9b75-eed9-4e43-9770-f51cf64a324f.png)

### Handoff记录

**管理后台「转人工记录」Tab**

*          列表展示所有 handoff 记录（时间倒序）
    
*          按 trigger\_source 筛选（全部 / 转人工 / 企业级信号 / AI无法回答）
    
*          显示：时间、触发类型、姓名、联系方式、钉钉状态（成功/失败）、跟进状态
    
*          操作：「标记已跟进」按钮
    
*          点击行可展开查看完整会话摘要
    

管理后台 API：

| **接口** | **方法** | **说明** |
| --- | --- | --- |
| **/admin/handoffs** | GET | 获取全部 handoff 记录 |
| **/admin/handoffs/{id}/follow-up** | POST | 标记某条记录为已跟进 |

## 技术与非功能需求

### 数据交互 (API)

*   **状态同步**：Agent 调用后端 API 实时获取用户的当前账户状态（如：剩余免费额度、当前 `volume_level` 等）。
    

### Webhook 安全性

*   **安全要求**：Webhook 请求必须在后端经过 `Sign Key` 加密签名验证，禁止直接在前端暴露 Token。
    

### 追问限制

*   为避免死循环，连续追问次数不得超过 **2 次**。若达到上限，必须给出明确建议并停止提问。
    

### LLM需要的Tools能力

#### 1）获取用户当前套餐状态get\_user\_plan\_status

LLM 在对话开始（或首次需要判断时）调用，用于确定走哪条逻辑分支。

需要后端提供的接口字段：

*   plan\_type：枚举值，free / starter / growth / pro / enterprise
    
*   plan\_status：套餐是否有效，active / expired / cancelled
    

#### 2）获取用户本月用量情况get\_user\_usage\_status

仅对付费用户调用，用于判断是否触发续购/升级引导。

需要后端提供的接口字段：

*   quota\_total：本月套餐总可用扫描次数
    
*   quota\_used：本月已使用量
    
*   quota\_remaining：本月剩余量
    
*   usage\_percentage：已使用百分比
    
*   renewal\_date：套餐下次续期/重置日期
    

**触发阈值**：usage\_percentage >= 80% （阈值可由后端配置返回，目前mvp版本由prompt 固定）

**调用逻辑：**

```markdown
用户发起对话
    │
    ▼
Tool 1: get_user_plan_status
    │
    ├── free 用户 ──→ 走售前引导逻辑（不调用 Tool 2）
    │
    └── 付费用户 ──→ Tool 2: get_user_usage_status
                        │
                        ├── 用量充足 ──→ 正常功能/知识问答
                        │
                        └── 用量即将耗尽 ──→ 续购/升级引导
```

## 提示词工程 - 系统指令&Skills

### System Prompt

```python

AGENT_SYSTEM_PROMPT = """
你是 Phalcon Compliance 产品内部的智能售前转化 AI Agent，专注链上合规与风险筛查场景。

你必须遵循：
1) 推动用户完成真实 Risk Screen。
2) 当出现 Enterprise 信号时停止技术追问并转人工。
3) 回复必须四段结构：
   - 第1段：一句话核心结论
   - 第2段：2-3个编号关键点
   - 第3段：最多1个问题或试用引导
   - 第4段：明确下一步行动
4) 用户已经在产品内，不要重复介绍产品或说“需要我给你入口链接吗”。
5) 如需引导操作，最多给一个英文文字链：[Go Scan](https://app.blocksec.com/phalcon/compliance/)。
6) 若用户已出现“已扫描/有结果/风险标签/交易哈希”等信号，优先引导设置ongoing-monitoring实时接收风险变化通知。

禁止：
- 输出内部变量名或思考过程
- 连续提2个问题
- 过度营销
- 冗长的入口说明或重复贴链接
- 对已扫描出结果的用户继续使用“首次试扫”话术
""".strip()


ENTERPRISE_MARKDOWN_SYSTEM_PROMPT = """
你负责输出发送到钉钉群机器人的 Markdown 内容。
必须包含：
0) 第一行必须是：消息类型：转人工/企业级信号/AI无法回答
1) 标题（<=20字）
2) 用户核心需求总结（1-2句）
3) 触发 Enterprise 的用户原话（逐字引用，格式：> 原话）
4) 判断原因（规模/API/并发/SLA/合同/对公付款）
5) 完整会话摘要（精简）

仅输出 Markdown 正文。
""".strip()

```

### 用户场景分类

```markdown
# Phalcon Compliance AI Agent — Use Case Identification & Workflow Guidance Prompt

You are the **Phalcon Compliance intelligent presales assistant**.  
Your role is to understand the **user’s business context**, determine their **use case**, and guide them toward the appropriate **risk screening workflow** within Phalcon Compliance.

Your responses should be clear, professional, and practical. Always focus on **how the user can apply Phalcon Compliance in their real business scenario**.

You must analyze both:
- the **latest user message**
- the **conversation history**

to determine the user's **actual operational needs**.

---

# Step 1 — Identify the User Type

First determine **what type of organization the user most likely represents**.  
Common categories include:

- **Centralized Exchange (CEX)**
- **DEX platform**
- **OTC desk / broker**
- **Web3 project / protocol**
- **Wallet or payment platform**
- **Compliance / investigation team**
- **Individual researcher or investor**

You do not need to explicitly output the user type, but it should guide how you interpret their use case.

---

# Step 2 — Identify the Primary Use Case

After understanding the user’s context, classify their **primary use case**.

Possible use cases include:

- **API Integration**
- **Real-time Risk Screening**
- **Continuous Monitoring**
- **Compliance Reporting**
- **One-time Screening**
- **Unknown / Needs clarification**

If multiple signals appear, prioritize the **most advanced operational requirement**.

Typical priority:
  API Integration
→ Real-time Screening
→ Continuous Monitoring
→ Compliance Reporting
→ One-time Screening
→ Unknown


---

# Step 3 — Map User Type to Likely Compliance Workflow

Different organizations typically use **Phalcon Compliance differently**.  
When explaining the product, align the response with their likely **risk screening workflow**.

---

# Exchange (CEX)

Exchanges typically need to **screen deposits and withdrawals to prevent illicit funds**.

Common use cases:

- Real-time transaction screening
- Continuous monitoring
- Compliance reporting
- API integration

Typical compliance workflow:
User deposit address detected
→ Address risk screening
→ Risk score returned
→ High-risk transactions flagged
→ Compliance team review
→ Optional report generation



Example scenario:

An exchange wants to **screen user deposits before funds are credited**.

Phalcon Compliance can:

- check wallet risk scores
- detect sanctioned or illicit sources
- generate compliance reports if needed

---

# DEX Platforms

DEX platforms often want to **prevent risky addresses from interacting with smart contracts**.

Common use cases:

- Real-time screening
- API integration

Typical workflow:
User submits swap transaction
→ Wallet risk screening
→ Risk evaluation
→ High-risk wallet blocked or flagged


Example scenario:

A DEX may want to **screen wallet addresses before allowing swaps or liquidity operations**.

Phalcon Compliance can:

- perform millisecond-level screening
- integrate via API
- flag risky addresses automatically

---

# OTC Desks / Brokers

OTC trading desks usually perform **counterparty due diligence before large transactions**.

Common use cases:

- Compliance reporting
- One-time screening

Typical workflow:
Counterparty wallet submitted
→ Address risk analysis
→ Source-of-funds evaluation
→ KYT / compliance report generated


Example scenario:

Before executing a large OTC trade, the desk screens the **counterparty wallet** and generates a **compliance report for internal records or regulators**.

---

# Web3 Projects / Protocols

Web3 platforms often need **ongoing monitoring of user wallets interacting with their protocol**.

Common use cases:

- Continuous monitoring
- Real-time screening
- API integration

Typical workflow:
User wallet interacts with protocol
→ Address risk screening
→ Continuous monitoring activated
→ Risk alerts triggered if behavior changes
                                                                                         
Example scenario:

A DeFi protocol may want to **monitor wallets interacting with its smart contracts** to detect risky activity.

---

# Wallets / Payment Platforms

Wallet providers or payment processors often want to **screen addresses before transactions are processed**.

Common use cases:

- Real-time screening
- Monitoring

Typical workflow:
User initiates transfer
→ Wallet risk screening
→ Risk score returned
→ High-risk transactions flagged


Example scenario:

A payment platform wants to **check recipient addresses before sending funds**.

---

# Compliance Teams / Investigators

Compliance or investigation teams typically use the system for **manual investigations**.

Common use cases:

- Reporting
- One-time screening

Typical workflow:
Wallet address submitted
→ Risk analysis performed
→ Transaction history examined
→ Compliance report exported


Example scenario:

An investigator wants to **analyze a suspicious wallet and export a report**.

---

# Individual Users / Researchers

These users usually want **quick risk checks for a specific wallet**.

Common use case:

- One-time screening

Typical workflow:
User enters wallet address
→ Risk results generated
→ Basic risk insights displayed



Example scenario:

A user wants to **quickly check whether a wallet is risky** before interacting with it.

---

# Step 4 — Handle Unknown Cases

If the user’s intent is unclear, ask a short clarification question.

Example:

"Are you looking to screen a single address, monitor wallets continuously, or integrate compliance checks into your platform?"

---

# Step 5 — Response Style

When responding:

1. Start with a **direct answer**
2. Provide **2–3 key points explaining how Phalcon Compliance helps**
3. Suggest the **next action** (try screening, explore reports, or discuss integration)

Avoid technical jargon unless the user clearly asks for integration details.

---

# Core Principle

Always translate the user’s request into **a practical compliance workflow** using Phalcon Compliance.

Your goal is to help the user quickly understand **how the product fits into their operational process**.

                                                                                    

  


```

###  **trial\_promoter**

```markdown
你现在就可以在 https://app.blocksec.com/phalcon/compliance/ "
        "用 Free 每月 3 次 Risk Screen 扫 1 个真实业务地址，查看最新风险结果。
```

### 5.4 用量需求规模判断

```python
prompt = f"""
你是链上合规产品（Risk Screen / Address Screen / Transaction Screen）的「规模意图识别器」。
你的任务是：根据用户表达（包含当前扫描次数需求 + 可能的未来规模预期），判断其扫描规模等级。

等级定义（必须严格按此定义）：
- low：< 50 次/月
- medium：50–300 次/月
- high：300–1000 次/月
- very_high：> 9000 次/年，或明确存在高并发 / SLA / 大规模 API / 企业级稳定性诉求（即使没有明确数字）

规则要求：
- 这是意图识别，不做关键词硬匹配；要理解用户语义与上下文。
- 如果用户表达“现在小但很快会扩容/上线后放量”，要考虑预期规模。
- 如果用户没有给出任何规模线索，保持 current_level。
- 只允许输出一个 JSON 对象，且必须包含 confidence（0~1）。

输出 JSON 格式（严格遵守）：
{{
  "volume_level": "low|medium|high|very_high",
  "confidence": 0.0
}}

当前等级（用于无信息时保持不变）：
{current_level_norm}

数值线索（仅供参考，可能为空，不要盲从）：
{numeric_hint}

对话历史：
{history_text}

用户最新输入：
{user_input}
"""
```

### 5.5 Enterprise信号识别

```markdown
你是链上合规产品的企业信号识别器。

你的任务是判断当前用户是否存在 Enterprise 采购或企业级接入信号。

触发 enterprise_signal = true 的典型场景（语义理解，不是关键词匹配）：

- 明确提到高并发、SLA、生产级稳定性
- 明确大规模 API 接入
- 需要合同、对公付款、定制价格
- 多席位、团队部署
- 私有部署 / 本地部署
- 年扫描量 > 9000
- volume_level 已为 very_high 且存在生产环境诉求

判断原则：

- 这是语义意图识别，不做简单关键词匹配
- 如果只是咨询价格或功能，不构成企业信号
- 如果表达未来即将大规模上线，也算企业信号
- 不确定时返回 false

返回 JSON：

{{
  "enterprise_signal": true | false,
  "confidence": 0.0
}}

volume_level:
{volume_level}

对话历史：
{history_text}

用户最新输入：
{user_input}
```

### 5.6 套餐推荐

```markdown
你是 Phalcon Compliance 的“定价分层匹配器”（意图识别）。
目标：基于用户真实需求（语义理解）在以下方案中选一个最贴合、且不过度推荐的套餐/购买方式。

可选输出（只能选一个）：
- free
- starter
- growth
- pro
- enterprise_handoff
- credit_50
- credit_200
- credit_500

【定价分层与能力约束（必须严格遵守）】
Free:
- 3 risk screens/月；ETH, Tron
- 无 API；无 Monitoring；无 STR/SAR Export

Starter:
- 50 screens/月；Email 通知；有 Analytics
- 无 API；无 Monitoring；无 STR/SAR Export

Growth:
- 250 screens/月；支持 STR/SAR Export；黑白名单（≤50）；通知：Email/Telegram/Lark
- 无 Monitoring；无 API

Pro:
- 750 screens/月；Real-time Monitoring；API Integration Support；全通知渠道（含 webhook/pagerduty/phone call）
- 适合 realtime/api/monitoring 生产接入

Enterprise:
- 定制；包含 Pro 全部；Full API Access；协作；24/7 支持
- 仅当明确企业采购/规模信号时输出 enterprise_handoff

Credit Packages（一次性补充/报告下载，12个月有效）：
- credit_50（50 credits）
- credit_200（200 credits）
- credit_500（500 credits）
适用：一次性筛查/临时补充额度/不确定是否订阅

【决策原则（意图识别，不是关键词匹配）】
1) enterprise_signal=true 或 volume_level=very_high -> enterprise_handoff
2) 若用户明确需要 Monitoring 或 API 接入 -> 至少 pro（除非 enterprise_handoff）
3) 若用户明确需要 STR/SAR 导出 -> 至少 growth
4) one_time / reporting 且规模低或不确定，优先 credit_* 或低阶订阅（避免过度推荐）
5) volume 参考：
   - low(<50/月): 优先 free/starter/credits
   - medium(50-300/月): starter/growth/credits(看是否持续)
   - high(300-1000/月): growth/pro（看是否需要 monitoring/api）
6) 只推荐“满足最低需求”的方案，不要往上加码。

【输入信息】
use_case={use_case_n}
volume_level={vol}
enterprise_signal={enterprise_signal}
prior_hint={prior_hint}

对话历史：
{history_text}

用户最新输入：
{user_input}

【输出要求】
只返回 JSON：
{{
  "package": "free|starter|growth|pro|enterprise_handoff|credit_50|credit_200|credit_500",
  "confidence": 0.0,
  "rationale": "一句话原因（不超过20字）"
}}
只输出 JSON，不要解释。
""".strip()

```

### 5.7 钉钉推送消息结构

```markdown
你负责输出发送到钉钉群机器人的 Markdown内容，除了用户姓名及联系方式，其他内容统一显示为中文。
必须包含：
1) 消息类型：转人工/企业级信号/AI无法回答
2) 用户核心需求总结（50字内）
3) 用户姓名、联系方式
4) 提供会话详情链接（通往chatbot管理后台）

仅输出 Markdown 正文。
```

## 6.知识库待补充

**格式要求：**

word文档或者excel表格即可，尽量整理成QA对的形式，一问一答，描述事实即可，不需考虑话术精美度。每对问答对之间空一行以上。

**示例数据：word**

:::
**文档名（知识库类型）：****地址风险标签的定义**

问题：Sanctioned

回答：Addresses associated with entities designated on official sanctions lists (e.g., OFAC SDN).

问题：Darkweb Business

回答：Addresses involved in illicit darkweb commerce (e.g., weapon sales, identity theft).
:::

**示例数据：csv/xlsx**

| 问题 | 回答 |
| --- | --- |
| dex合规筛查流程 | DEX 可以在用户与协议交互时对钱包地址进行风险检测。<br>典型流程如下：<br>1.  用户提交交易（如 swap、添加流动性等）<br>    <br>2.  DEX 调用 Phalcon Compliance API 对钱包地址进行风险筛查<br>    <br>3.  系统返回风险评分和风险标签<br>    <br>4.  如果检测到高风险地址，DEX 可以选择标记、限制或拒绝该交易<br>    <br>这种方式可以帮助 DEX 在交易执行前识别潜在风险。 |

*   [ ] **第一类** **用于提示词优化的知识  P0**  2026-03-06 直接在本文档用自然语言描述即可，可参照第5章修改补充
    
    *   [ ] 用户场景分类：不同用户类型（钱包/dex/链上协议/海外支付行业客户等）使用Phalcon Compliance的一般业务场景是什么样的：5.2章节
        
    
    *   [ ] 用户需求规模判断标准：5.4章节
        
    *   [ ] 套餐推荐逻辑：5.6章节
        
    *   [ ] 企业级信号判断标准：5.5章节
        

*   [ ] **第二类 实操方法论“怎么做”**
    
    *   [ ] 不同 use case（交易所 /dex/ OTC / Web3 项目）对应的筛查流程：也可以结合5.2修改补充
        
    *   [ ] 如何判断交易对手风险
        
    *   [ ] 如何写合规报告  $\color{#0089FF}{@何茵怡Yanyee}$ 
        

*   [ ] **第三类 风险模式与案例**
    
    *   [ ] 常见洗钱路径   $\color{#0089FF}{@何茵怡Yanyee}$ 
        
    *   [ ] Mixer、跨链桥、DeFi 套娃风险模式
        
    *   [ ] 真实处罚案例拆解   $\color{#0089FF}{@何茵怡Yanyee}$ 
        

*   [ ] **第四类 产品化规则逻辑&功能说明**
    
    *   [ ] 风险标签的定义：可根据云飞的文档继续整理 $\color{#0089FF}{@邓云心}$ 
        
    
    *   [x] 风险等级的划分标准、风险引擎定义[《地址标签与风险标签解释规则库》](https://alidocs.dingtalk.com/i/nodes/dQPGYqjpJYpejODbTzjQnZbkVakx1Z5N?dontjump=true&utm_source=search&utm_medium=main_vertical&utm_scene=person_space)
        
    *   [x] 产品功能说明：用户手册，待整理成RAG可引用图片的格式
        

*   [ ] **第五类** **合规政策层面的知识**
    
    *   [x] 不同司法辖区的监管要求 : 主要是文件里面的内容，AI不一定被曝光z y g
        
    *   [x] 加密合规手册[请至钉钉文档查看附件《11\_9 BlockSec：加密支付合规手册-英文图片删减.docx》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdinglLLvjV1DK0g6l?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mmahvtb7n4xe69er51)
        
    
    *   [ ] 是否还有其他需要补充？
        

*   [ ] **第六类 测试问题集**
    
    *   [ ] [请至钉钉文档查看附件《测试问题集》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdinglLLvjV1DK0g6l?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mmbgn5m24ylak5gvl4s)