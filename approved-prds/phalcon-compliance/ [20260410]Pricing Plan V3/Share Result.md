# Share Result

# 功能概述

用户可为任意筛查结果生成公开链接，任何人无需登录即可访问。Share Result 对所有计划（Free、Credits、Essential、Scale、Enterprise）开放。

**与现有 SEO 分享页的区别：**

|  | SEO 分享页（现有） | 用户 Share Result（新增） |
| --- | --- | --- |
| 生成方式 | 系统后台自动生成 | 用户主动生成 |
| 访问权限 | 过滤敏感配置后的公开内容 | 过滤敏感配置后的公开内容<br>展示内容范围和 SEO 分享页保持一致 |
| 链接有效期 | 永久 | 用户自设（无限期 / 7天 / 30天 / 90天） |
| 可撤销 | 否 | 是 |
| 获客 CTA | 有 | 有 |

# 分享链接生成

## 入口

筛查结果详情页右上角操作区，加入 **Share** 按钮（图标 + 文字）。

## 生成流程

用户点击 Share 按钮 → 弹出 Modal：

```plaintext
┌─────────────────────────────────────┐
│  Share this result                  │
│                                     │
│  Link expires in:                   │
│  ○ Never  ● 30 days  ○ 90 days      │
│  ○ 7 days  ○ Custom date            │
│                                     │
│  ┌────────────────────────┐ [Copy]  │
│  │ https://...phalcon/... │         │
│  └────────────────────────┘         │
│                                     │
│  ☐ Allow Phalcon to index this      │
│    result for public search (SEO)   │
│                                     │
│  Anyone with this link can view     │
│  this result without logging in.   │
│                                [×] │
└─────────────────────────────────────┘
```

**SEO 同意勾选项说明：**

*   默认**不勾选**（用户须主动授权）
    
*   勾选后：该结果页被纳入系统 SEO 索引（与现有后台生成的 SEO 分享页一致）
    
*   不勾选：链接仅供手动传播，不被搜索引擎收录
    
*   点击 "Share" 按钮后**立即生成链接**（不需要二次确认）
    
*   默认有效期：30 天
    
*   可选有效期：永久（Never）/ 7 天 / 30 天 / 90 天 / 自定义日期
    
*   链接生成后即时可用，可直接复制或点击图标分享
    

# 链接管理页

## 入口

## 页面内容

```plaintext
Shared Results
────────────────────────────────────────────────────────────
Address / Transaction    Created      Expires      Status   Actions
────────────────────────────────────────────────────────────
0xABC...123             Apr 1, 2026  May 1, 2026  Active   [Copy] [Revoke]
TAoLw...vvP             Mar 15, 2026 Expired      Expired  [Renew] [Delete]
0xDEF...456             Apr 9, 2026  Never        Active   [Copy] [Revoke]
────────────────────────────────────────────────────────────
```

*   **Active**：链接有效，可正常访问
    
*   **Expired**：链接已过期，访问时显示"This link has expired"
    
*   **Revoked**：用户手动撤销，访问时显示"This link is no longer available"
    
*   **Copy**：复制链接地址
    
*   **Revoke**：立即使链接失效（不可恢复，需二次确认）
    
*   **Renew**：对已过期链接重新设置有效期并激活（生成新链接）
    
*   **Delete**：从列表中删除记录
    

# 公开分享页

## 展示内容（过滤规则）

基于现有 SEO 分享页样式，以下内容**保留展示**：

*   地址/交易基本信息（地址、链、余额、资金流向）
    
*   整体风险评分和风险等级
    
*   风险标签（Sanctioned、Drug Trafficking 等系统标签）
    
*   风险分析详情（各维度占比）
    

## 引导 CTA

沿用现有 SEO 分享页的获客设计，无需新增底部区块：

*   **顶部 Banner**：提示结果是 XX 天前生成的，引导访客自行扫描获取最新结果
    
*   **右侧浮动 CTA 按钮**：常驻，引导注册/扫描
    

## 链接失效状态页

链接过期或被撤销时，访问该链接显示：

```plaintext
┌───────────────────────────────┐
│  [Phalcon Logo]               │
│                               │
│  This link is no longer       │
│  available.                   │
│                               │
│  The shared report has        │
│  expired or been removed.     │
│                               │
│  [Screen an address yourself] │
│  [Visit Phalcon Compliance]   │
└───────────────────────────────┘
```