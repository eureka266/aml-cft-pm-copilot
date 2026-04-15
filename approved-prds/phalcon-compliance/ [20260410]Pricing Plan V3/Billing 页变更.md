# Billing 页变更

:::
原型：

[请至钉钉文档查看附件《billing-page.html》](https://alidocs.dingtalk.com/i/nodes/dpYLaezmVNKEra7XcmRb34NOJrMqPxX6?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mnsmze08v3aj4nz093)

（可下载后用浏览器打开查看）
:::

# V3 页面结构（完整）

```plaintext
① [条件] 页面顶部 Banner（场景 7 / 场景 9，按条件出现）
② Current Plan 卡片（扩展）
③ [条件] Credits 余额卡片（仅 Credits 用户）
④ [条件] Monitor Add-on 卡片（仅 Essential / Scale 用户）
⑤ Next Billing 卡片（微调）
⑥ [条件] Top-up 区域（仅订阅用户，额度不足时出现）
⑦ [条件] 年付切换提示（仅月付订阅用户，被动内嵌）
⑧ 发票表（不变）
```

# 页面顶部 Banner（条件出现）

**同一时刻只显示一条 Banner，优先级：场景 9 > 场景 7。**

## 场景 9：订阅用户接近屏数上限

触发：当月已使用 ≥ 80% 订阅配额

```plaintext
You've used 42 of 50 screenings this month.
Upgrade your plan or add a Top-up to continue screening.
[Upgrade plan]   [Top-up]                            [×]
```

*   \[Upgrade plan\] → 打开 Checkout Modal，预填当前计划上一档
    
*   \[Top-up\] → 页内滚动至 Top-up 区域（见 §七）
    
*   \[×\] → 当期关闭（下月重置）
    

## 场景 7：Credits 用户高用量

触发：Credits 用户当月已消耗 ≥ 30 次

```plaintext
💡 You've used 35 credits this month.
   An Essential plan (50/mo at $59) would cost less and include STR/SAR Reports, Monitoring & more.
   [Subscribe to Essential →]                                                        [Dismiss]
```

*   \[Dismiss\] → 永久关闭，不再显示
    
*   每个用户只触发一次
    

# 四、Current Plan 卡片（扩展）

V2 只显示计划名称。V3 扩展为包含用量、操作入口的完整卡片。

## 4.1 订阅用户（Essential / Scale）

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Current Plan                                              │
│                                                           │
│ Essential Plan · 50 screenings / mo · Monthly            │
│ Renews Jun 8, 2026                                        │
│                                                           │
│ 42 / 50 screenings used this period  [View usage →]      │
│                                                           │
│ [Upgrade]  [Change plan ↓]  [Cancel plan]                 │
└───────────────────────────────────────────────────────────┘
```

*   "42 / 50 screenings used" 为纯文本摘要，**不含进度条**（详细用量在 Usage 页）
    
*   \[View usage →\] 链接至 Billing & Usage > Usage 页
    
*   额度用尽时文字变为：`0 / 50 screenings remaining this period`（红色）
    

**按钮行为：**

| 按钮 | 行为 |
| --- | --- |
| Upgrade | 打开 Checkout Modal，预填当前计划的上一档（如 Essential 50 → Essential 100） |
| Change plan | 下拉菜单：列出所有可用档位（含更低档位）；选择后打开 Checkout Modal |
| Cancel plan | 打开取消确认 Dialog（见 §四·3） |

**降级说明**：通过 Change plan 选择更低档位时，Checkout Modal 内显示提示：

> "Downgrading takes effect at the start of your next billing period (Jun 8)."

## 4.2 Credits 用户

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Current Plan                                              │
│                                                           │
│ Credits (Pay-as-you-go)                                   │
│                                                           │
│ [Buy more credits →]   [Subscribe to a plan →]           │
└───────────────────────────────────────────────────────────┘
```

*   \[Buy more credits →\] → 打开 Checkout Modal，预填 Credits 购买（默认 100 次档）
    
*   \[Subscribe to a plan →\] → 跳转 Pricing 页
    

## 4.3 Free 用户

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Current Plan                                              │
│                                                           │
│ Free Plan                                                 │
│                                                           │
│ Screenings this month: 2 / 3 used · Resets Jun 8         │
│                                                           │
│ [Upgrade to Essential →]   [Buy Credits →]               │
└───────────────────────────────────────────────────────────┘
```

## 4.4 取消确认 Dialog

```plaintext
┌─────────────────────────────────────────────────────┐
│  Cancel your Essential plan?               [×]      │
│  ─────────────────────────────────────────────────  │
│  Your plan will remain active until Jun 7, 2026.    │
│  After that, your account will be downgraded to     │
│  Free (3 screenings/mo).                            │
│                                                     │
│  Your data and history will be retained.            │
│                                                     │
│  [Keep my plan]          [Confirm cancellation]     │
└─────────────────────────────────────────────────────┘
```

*   取消生效时间：当前计费周期结束
    
*   数据保留：账户数据不删除
    
*   \[Confirm cancellation\] → 写入取消标记，Current Plan 卡片显示"Cancels on Jun 7"倒计时
    

# 五、Credits 余额卡片（Credits 用户专属）

仅当账户有 Credits 余额时显示。

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Credits Balance                                           │
│                                                           │
│ 158 credits remaining                                     │
│ Expires Jan 14, 2027                                      │
│                                                           │
│ [Buy more credits]                                        │
└───────────────────────────────────────────────────────────┘
```

*   若有多批次 Credits（不同到期日），显示最早到期的批次：`158 credits remaining · Earliest expiry: Jan 14, 2027`
    
*   \[Buy more credits\] → 打开 Checkout Modal，预填 Credits 购买
    

# 六、Monitor Add-on 卡片（Essential / Scale 用户专属）

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Ongoing Monitoring                                        │
│                                                           │
│ 8 / 10 addresses monitored                               │
│ Current add-on: 10 monitors · +$60/mo                    │
│                                                           │
│ [Add more monitors]                                       │
└───────────────────────────────────────────────────────────┘
```

*   \[Add more monitors\] → 打开 Checkout Modal，预填 Monitor add-on 升级档位
    
*   若用满（10/10）：进度条红色，\[Add more monitors\] 按钮 Primary 样式（高亮）
    
*   若包含免费的 1 个监控（未购买 add-on）：```1 / 1 address monitored (free tier)\[Add Monitor Add-on →\]```
    

**Add-on 升降级规则：**

*   升级（增加监控数）→ 立即生效，当前周期按天数比例计费（prorated）
    
*   降级（减少监控数）→ 下个计费周期生效；当前期内的超额地址保持活跃直至周期结束
    

# 七、Next Billing 卡片（微调）

V2 已有，V3 补充计费明细。

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Next Billing Date                                         │
│                                                           │
│ Next Billing Date     Jun 8, 2026                        │
│ Next Billing Amount   $119.00                            │
│                                                           │
│ Breakdown:                                               │
│   Essential 50/mo          $59.00                        │
│   Monitor Add-on (10)      +$60.00                       │
│ ─────────────────────────────────────────                │
│   Total                    $119.00                       │
│                                                           │
│ Payment Method    Stripe · Visa ····4242  [Change]       │
└───────────────────────────────────────────────────────────┘
```

*   无 Monitor Add-on 时不显示明细区域（只显示单行 Amount）
    
*   年付用户：Next Billing Amount 显示年付总价，注明"Annual"
    
*   Credits 用户：显示"No subscription · No upcoming charge"
    
*   \[Change\] → 跳转 Stripe / Infini / Clink 对应的支付方式管理页（外部链接）
    

# 八、Top-up 区域（订阅用户额度不足时）

**显示条件：** 订阅用户当月剩余配额 ≤ 20%，或已用尽（0 剩余）

位置：Next Billing 卡片下方，发票表上方

```plaintext
┌───────────────────────────────────────────────────────────┐
│ Need more screenings this month?                          │
│                                                           │
│ Top up at your current plan rate: $1.18 / screening       │
│ Top-ups expire at the end of your current billing period. │
│                                                           │
│  [ 50 screenings — $59 ]  [ 100 screenings — $118 ]      │
│  [ 200 screenings — $236 ]                               │
│                                                           │
│ [Custom amount]                                           │
└───────────────────────────────────────────────────────────┘
```

*   单价 = 当前计划的单次筛查单价（Essential 50档：$59/50 = $1.18）
    
*   点击任意金额按钮 → 打开 Checkout Modal，预填 Top-up 信息
    
*   \[Custom amount\] → 打开 Checkout Modal，用户手动输入数量
    
*   Top-up 额度**不结转**至下一周期
    

# 九、年付切换提示（月付订阅用户，被动内嵌）

**显示条件：** 用户当前为月付订阅

位置：Top-up 区域下方（或发票表上方，始终可见，不可关闭）

```plaintext
Save 17% by switching to annual billing.
Your current plan: Essential 50/mo · $59/mo
Annual equivalent: $50/mo · billed $600/yr
[Switch to Annual →]
```

*   \[Switch to Annual →\] → 打开 Checkout Modal，预填当前计划的年付版本
    
*   年付用户不显示此区域
    

# 十、Usage 页 V3 变更

> Usage 页（Billing & Usage > Usage）负责详细用量展示，保持现有结构，仅更新以下内容。

## 10.0 Usage / Total 列展示规则

页面顶部已有服务周期起止日期和进度条，行内**不重复展示** reset 日期。用量按以下规则展示：

**列名：将 "Usage / Total" 改为 "Usage"**，适配以下四种格式：

| 限额类型 | 展示格式 | 说明 |
| --- | --- | --- |
| 周期配额（按月重置） | `42 / 50` + 进度条 | 无需 reset 日期，顶部已有周期信息 |
| 总量上限（累计上限） | `6 / 200 total` | "total" 标注区分于周期配额；可选淡色进度条 |
| 无上限 | `5,738`（纯数字） | 不显示分母，不显示进度条 |
| Boolean 功能 | `Yes` badge | 现有样式不变 |

**进度条颜色**（周期配额行）：< 80% 蓝色，≥ 80% 橙色，100% 红色

## 10.1 Screening Count 行

| 用户类型 | V3 显示 |
| --- | --- |
| Free | `2 / 3` + 进度条（周期配额） |
| Credits | `158 credits remaining`（另见 §五 Credits 余额卡片） |
| Essential / Scale | `42 / 50` + 进度条（周期配额） |
| Enterprise | `5,738`（无上限） |

**接近或用尽时，行右侧显示 inline CTA：**

*   ≥ 80%：`[Top-up]`（订阅用户）或 `[Buy credits]`（Credits 用户）
    
*   用尽：同上，按钮改为 Primary 样式
    

## 10.2 Ongoing Monitoring 行

| 用户类型 | V3 显示 |
| --- | --- |
| Free / Credits（试用期内） | `Trial · X days remaining` |
| Free / Credits（试用结束） | `—`（无权限） |
| Essential / Scale | `8 / 10 addresses`（总量上限，按 Add-on 档位） |
| Essential / Scale（未购 Add-on） | `1 / 1 total (free tier)` |
| Enterprise | `Unlimited` |

**用满时**（如 10/10），行右侧显示 `[Add monitors]` inline CTA

## 10.3 其他有配额的行

| 功能 | 限额类型 | 示例（Essential） |
| --- | --- | --- |
| Custom Risk Engines | 总量上限 | `3 / 10 total` |
| Customers | 总量上限 | `0 / 10 total` |
| Labels | 总量上限 | `6 / 200 total` |
| Tags | 总量上限 | `1 / 200 total` |
| Blacklist / Whitelist | 总量上限 | `0 / 50 total` |

具体各计划限额见总设计文档功能权限对照表（§三）。

## 10.4 Billing 页与 Usage 页的导航关系

*   Billing 页 Current Plan 卡片内的 `[View usage →]` 链接至 Usage 页
    
*   Usage 页顶部无需返回 Billing 的链接（面包屑导航 Billing & Usage > Usage 已足够）
    

# 十一、各用户类型视图汇总

| 区域 | Free | Credits | Essential/Scale 月付 | Essential/Scale 年付 |
| --- | --- | --- | --- | --- |
| 顶部 Banner | — | 场景 7（条件） | 场景 9（条件） | 场景 9（条件） |
| Current Plan 卡片 | ✅（简化版） | ✅（Credits 版） | ✅（含用量+操作） | ✅（含用量+操作） |
| Credits 余额卡片 | — | ✅ | — | — |
| Monitor Add-on 卡片 | — | — | ✅ | ✅ |
| Next Billing 卡片 | 无账单 | 无账单 | ✅（含明细） | ✅（年付总价） |
| Top-up 区域 | — | — | 条件显示（≤20%） | 条件显示（≤20%） |
| 年付切换提示 | — | — | ✅ | — |
| 发票表 | — | ✅ | ✅ | ✅ |