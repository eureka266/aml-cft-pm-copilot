# PM Copilot Assets Index

轻量级产品截图和页面结构索引。记录各模块的 UI 现状、功能对标、竞品参考。

PRD 生成时自动引用。资产索引通过 `/scan-assets` 命令定期自动更新。

---

## 更新方式

### 方式 1：对话驱动（实时更新）

在 Claude Code 中说：
```
这是 Address Screening 列表页（新增批量导出）
[截图或描述]
```

我会立即更新本索引。

### 方式 2：自动扫描（定期维护）

在 Claude Code 中说：
```
/scan-assets
```

我会：
1. 扫描 `approved-prds/` 和 `competitors/` 中的所有新内容
2. 提取图片链接、UI 描述、功能对标
3. 自动更新本索引
4. 生成扫描报告

**推荐频率：** 每周或新增 3+ 个截图时运行

---

## Phalcon Compliance

### Address Screening

**功能**：地址风险筛选、批量导入、风险评分

**参考竞品**：
- [Merkle Science Address Screening](competitors/phalcon-compliance/merkle-science.md#address) — 支持上传 CSV、API、实时搜索；提供 Risk Level 和 Export Report
- [Chainalysis Reactor](competitors/phalcon-compliance/chainalysis.md)

**当前 UI 要点**：
- 批量导入：CSV 上传
- 结果展示：Risk Level、Alert 列表、关联交易
- 导出：支持 PDF 报告

**最后更新**：2026-04-15

---

### Transaction Monitoring

**功能**：交易风险识别、实时监控、规则配置

**参考竞品**：
- [Merkle Science Transaction](competitors/phalcon-compliance/merkle-science.md#transaction) — 支持风险规则配置、自动化策略、Alert 管理

**当前 UI 要点**：
- [待补充当前 UI]

**最后更新**：2026-04-15

---

### Risk Scoring & Policies

**功能**：风险评分引擎、自定义风险规则、政策管理

**参考竞品**：
- [Merkle Science Risk Management](competitors/phalcon-compliance/merkle-science.md#workspace-settings) — 支持多策略、多维度（Source of Funds、Behavior、Advanced）、FATF 预设规则、Custom Tags、Audit Trail

**当前 UI 要点**：
- Risk Policy 管理
- Rule 配置（AND 组合条件）
- Hit Rate 和审计日志

**最后更新**：2026-04-15

---

### Case Management & Workflow

**功能**：案件创建、协作分配、自动路由、签核流程

**参考竞品**：
- [Merkle Science Case Preferences](competitors/phalcon-compliance/merkle-science.md#workspace-settings) — 自动创建规则、成员分配、案件签核

**当前 UI 要点**：
- [待补充当前 UI]

**最后更新**：2026-04-15

---

### SAR/STR Reporting

**功能**：报告生成、合规填报、历史追溯

**参考竞品**：
- [Merkle Science Export Report](competitors/phalcon-compliance/merkle-science.md#export-report) — PDF 报告导出

**当前 UI 要点**：
- [待补充当前 UI]

**最后更新**：2026-04-15

---

### Dashboard & Workspace Settings

**功能**：概览统计、API 管理、集成配置、成员权限

**参考竞品**：
- [Merkle Science Dashboard](competitors/phalcon-compliance/merkle-science.md#dashboard) — Alerts 统计、Cases 统计、Rule 触发分布、Severity 分布
- [Merkle Science Workspace Settings](competitors/phalcon-compliance/merkle-science.md#workspace-settings) — API Keys、Integrations（Slack、Webhook、Fireblocks）、Members、Configurations

**当前 UI 要点**：
- 统计维度：Alerts、Cases、Rules、Severity
- 集成支持：Slack、Webhook 等
- 权限管理：Role-based 协作

**最后更新**：2026-04-15

---

## Phalcon Network

**参考竞品**：
- [待补充竞品对标]

**当前模块**：
- [待补充 UI 和功能]

**最后更新**：2026-04-15

---

## MetaSleuth

**参考竞品**：
- [待补充竞品对标]

**当前模块**：
- [待补充 UI 和功能]

**最后更新**：2026-04-15

---

## 竞品功能对标速查

| 功能 | Merkle Science | Chainalysis | Elliptic | TRM Labs | Slowmist |
|-----|--------|--------|----------|----------|----------|
| 地址筛选 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 交易监控 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 自定义规则 | ✅ | ? | ? | ? | ? |
| 协作案件 | ✅ | ? | ? | ? | ? |
| Slack 集成 | ✅ | ? | ? | ? | ? |
| Fireblocks 集成 | ✅ | ? | ? | ? | ? |

*更新自 `competitors/phalcon-compliance/`*

---

## 维护说明

- 每条资产记录包含：功能、参考竞品、UI 要点、更新时间
- 竞品链接指向 `competitors/phalcon-compliance/` 下的详细文档
- 通过 `/scan-assets` 自动提取新增内容，无需手动维护
- 图片/描述来自 `approved-prds/` 和 `competitors/` 中的 markdown 文件

---

**最后更新**：2026-04-15  
**维护方式**：对话驱动 + `/scan-assets` 自动扫描
