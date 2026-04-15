# PM Copilot Skill Plan

用于 Claude Code 的产品需求文档生成 Skill。帮助 BlockSec PM 快速编写 PRD，复用过去的决策，加速新 PM 学习。

---

## 快速开始

### 对 PM 来说：怎么用？

在 Claude Code 中：

```
我想写一个 [需求名称] 的 PRD

[可选：贴一个截图或描述当前的 UI]
```

然后 Claude Code 会：
1. 读取 `facts/` 中的产品定义
2. 读取 `workflows/` 中的工作流说明
3. 读取 `approved-prds/` 中的历史 PRD 作为参考
4. 问你 6 个关键问题（需求、用户、边界等）
5. 自动生成一份完整的 PRD
6. 记录决策逻辑到 `decisions/` 中（下次可以查阅）

### 对其他开发者来说：怎么集成？

如果你想在自己的 Claude Code skill 中集成这个系统：

```bash
# 克隆或导入这个仓库
git clone <pm-copilot-repo-url>

# 在你的 Claude.md 中引用
See aml-cft-pm-copilot/CLAUDE.md for product knowledge
```

---

## 系统结构

```
approved-prds/          历史 PRD（v3.1+） + 用户手册链接
├── _references.md      → Phalcon Compliance/Network/MetaSleuth 用户手册
├── [20251111]...       → 历史 PRD 按时间组织
└── [20260305]...

facts/                  产品事实库（权威源）
├── glossary.md         共享术语表（SAR、Entity、Risk Score 等）
├── guardrails.md       产品边界和安全规则
├── phalcon-compliance.md
├── phalcon-network.md
└── metasleuth.md

workflows/              核心用户工作流
├── address_screening.md
├── transaction_screening.md
└── core-user-flows.md

decisions/              自动生成的决策日志
└── (每次 PRD 后自动生成)

assets-index.md         产品截图/UI 索引
```

---

## 工作流程详解

### 场景 1：新 PM 想快速学习

**老 PM 说：** "地址筛选为什么用严格匹配，不支持模糊匹配？"

**新 PM 可以：**
1. 读 `facts/phalcon-compliance.md` → 了解产品定义
2. 读 `workflows/address_screening.md` → 了解工作流
3. 读 `approved-prds/_references.md` → 打开用户手册看当前 UI
4. 查 `approved-prds/` 里关于地址筛选的历史 PRD → 看过去为什么这样设计
5. 查 `decisions/` 里相关的决策日志 → 看完整的决策背景

**结果：** 新 PM 不用打扰老 PM，自己就能理解全貌。

### 场景 2：要写一个新 PRD

**在 Claude Code 中：**

```
我想为 Phalcon Compliance 写一个"批量地址导出"功能的 PRD

这是当前的列表页截图：
[贴截图或描述]
```

**Claude Code 会：**

1. **读取知识库**
   - facts/phalcon-compliance.md → 产品边界
   - workflows/address_screening.md → 相关工作流
   - approved-prds/_references.md → 读 GitHub 用户手册（实时）
   - approved-prds/[20251111].../ → 找相关的历史 PRD

2. **问你 6 个问题**
   - 这个功能解决什么问题？（需求真实性）
   - 你想支持的最小化版本是什么？（产品聚焦）
   - 有没有类似的功能已经存在？（避免重复）
   - 等等...

3. **自动生成**
   - PRD 文档（带截图、背景、接受标准）
   - 决策日志（记录你做了什么决策、为什么）

4. **保存决策日志**
   ```
   decisions/decision-20260415-batch-export.md
   ```

5. **下次写 PRD 时**
   - Claude Code 自动读到这个决策日志
   - 如果新 PRD 与过去的决策相关，会主动提醒
   - 减少重复解释

---

## 核心约定

### 1. Facts 是权威源

如果产品定义和用户手册有冲突，以用户手册为准（最新）。  
Facts/ 中的定义应该定期更新，保持与用户手册一致。

### 2. Decisions 是记录，不是法律

每个决策日志都记录了当时的假设。如果后续改了主意，新的决策日志会记录改变的理由。  
历史决策永不删除，方便追溯。

### 3. Assets Index 是轻量级的

不需要维护复杂的图片库。只需要在对话中提一下（"这是列表页"），Claude Code 会自动索引和保存。

### 4. Approved-PRDs 是参考，不是教科书

历史 PRD 用来理解过去的决策背景，不是复制粘贴的模板。  
每个新 PRD 都应该基于当前的用户、问题和市场情况重新思考。

---

## 使用规则

### Do ✅
- 在 Claude Code 中和我讨论 PRD（自然对话）
- 定期（比如月底）读一遍决策日志，确认逻辑是否一致
- 当产品有重大改动时，更新 facts/ 中的定义
- 给新 PM 分享这个系统，让他们自己查阅而不是被打扰

### Don't ❌
- 不要手动编辑 decisions/ 中的日志（由 Claude Code 自动生成）
- 不要把草稿 PRD 存到 approved-prds/（只存已确认的）
- 不要覆盖或删除历史 PRD（历史很重要）
- 不要直接复制历史 PRD 作为新 PRD（每次要重新思考）

---

## 关键文件说明

| 文件 | 用途 | 更新频率 |
|------|------|------|
| **facts/glossary.md** | 术语表（SAR、Entity 等） | 产品有新概念时 |
| **facts/guardrails.md** | 产品边界和安全规则 | 合规要求变化时 |
| **facts/phalcon-*.md** | 各产品的定义和目标用户 | 产品策略改变时 |
| **workflows/*.md** | 核心用户任务流 | 流程优化时 |
| **approved-prds/_references.md** | GitHub 用户手册链接 | 基本不变（链接是固定的） |
| **approved-prds/[DATE].../** | 历史 PRD 文档库 | 每次新 PRD 后新增 |
| **assets-index.md** | UI 截图索引 | 每次有新截图时 |
| **decisions/*.md** | 决策日志 | 每次 PRD 后自动生成 |

---

## 常见问题

**Q: 我想用这个系统，但不知道从哪开始**

A: 在 Claude Code 中说：
```
帮我理解 Address Screening 这个模块。
我需要了解它是什么、用户是谁、目前的工作流。
```

Claude Code 会自动读 facts/workflows/approved-prds，给你一个完整的背景。

---

**Q: 历史 PRD 太多了，怎么快速找到相关的？**

A: 打开 `approved-prds/` 文件夹，按日期和功能名一目了然。或者在 Claude Code 中问：
```
帮我找一下关于"地址匹配"的历史 PRD
```

Claude Code 会自动搜索。

---

**Q: 决策日志有什么用？**

A: 
- 新 PM 理解为什么某个功能这样设计
- 下次写相关 PRD 时，Claude Code 会自动提醒你过去的决策
- 团队 review PRD 时，有完整的决策背景可以查

---

**Q: 能不能删除一个过时的决策日志？**

A: 不要删。改为：
1. 新写一个决策日志，说明为什么改变了想法
2. 把旧决策日志的链接贴在新日志里，做版本追踪

这样团队能看到完整的演进过程。

---

## 开始使用

1. **了解系统**：读 `README.md` 和 `USAGE.md`
2. **熟悉知识库**：翻一遍 `facts/` 和 `workflows/`
3. **看历史 PRD**：打开 `approved-prds/` 看 2-3 个例子
4. **试写一个 PRD**：在 Claude Code 中：
   ```
   我想为 [功能名] 写 PRD。当前情况是 [简述]。
   ```
5. **查阅决策日志**：PRD 完成后，看自动生成的 `decisions/` 文件

---

**维护者：** Claude Code  
**最后更新：** 2026-04-15  
**版本：** 1.0 - 初始化完成
