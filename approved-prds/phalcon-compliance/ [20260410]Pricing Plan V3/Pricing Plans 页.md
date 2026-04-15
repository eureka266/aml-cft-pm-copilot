# Pricing Plans 页

:::
原型：[请至钉钉文档查看附件《pricing-prototype.html》](https://alidocs.dingtalk.com/i/nodes/QOG9lyrgJPvE5n02cXdoEk2vWzN67Mw4?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mnskps27wujxd2hb4w)

（可下载后用浏览器打开查看）
:::

# 页面结构

页面区块：

```plaintext
Credits / Pay-as-you-go 区（未登录用户 / Free 用户可见）
Subscription Plans 区（含月付/年付切换）
Full Feature Comparison Table
```

**已订阅用户**访问 Pricing 页时：

*   隐藏 Credits / PAYG 区
    
*   高亮当前计划卡片（"Your current plan" 标记）
    
*   低于当前计划的订阅按钮：禁用状态
    
*   高于当前计划的订阅按钮：显示为 "Upgrade"
    
*   自动切换到用户当前的计费周期（月付/年付）
    

# Credits / PAYG 区

## 布局

```plaintext
Section eyebrow: "Pay-as-you-go"
┌─────────────────────────────────────────────┐
│ Credits                                      │
│ No subscription needed. Buy once, use at    │
│ your pace — valid for 12 months.            │
│                                             │
│ [滑块选量]                                   │
│  50 · 100 · 200 · 500 · 1,000 · 2,000      │
│                                             │
│ ┌──────────────────────────────────────┐    │
│ │ 50 screenings  $95 total  $1.90/screen│   │
│ │ valid 12 months          [Buy credits]│   │
│ └──────────────────────────────────────┘    │
│                                             │
│ What's included:                            │
│ ✓ All supported chains  ✓ Full Risk Screen  │
│ ✓ Audit Report Export   ✓ Share Result      │
│ ✓ Analytics Dashboard   ✓ 3 Custom Risk Engines│
│  ✓ 1 Customer · 50 Lables/Tags              │
└─────────────────────────────────────────────┘
```

## 滑块交互

*   6 个离散档位：50 / 100 / 200 / 500 / 1,000 / 2,000
    
*   拖动到任意档位后，结果区实时更新：数量、总价、单价
    
*   单价随数量增大而递减，体现批量优惠
    

# Subscription Plans 

*   月付/年付切换
    
    *   切换后所有卡片价格同步更新
        
    *   年付时展示：年付总价 + 折合月价（划线月价 → 折扣月价）
        
    *   年付时筛查次数展示为一年总数
        

其他文案等见原型

# Top-up

*   **入口**：仅在 Billing & Usage 页展示，Pricing 页不显示
    
    *   且仅当用户已有订阅 Plan 时展示
        
*   **计费逻辑**：按当前套餐单价，不低于下一次订阅的单价
    
    *   如用户当前 plan 为 Essential Plan 25 /month (单价 $1.56)，则 Top up 的单价也为 1.56
        
*   **有效期**：随当前订阅周期失效，不结转至下一周期