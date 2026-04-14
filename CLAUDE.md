# CLAUDE.md

## 目的

本 repo 是 BlockSec 内部产品经理生成 PRD 和 Demo 的知识库。
包含产品事实、用户工作流、决策记录。

适用产品：
- Phalcon Compliance
- Phalcon Network
- MetaSleuth

## 权威源

始终读取这些文件作为产品真相：
- `facts/phalcon-compliance.md` - 产品定义、边界、能力
- `facts/phalcon-network.md`
- `facts/metasleuth.md`
- `facts/glossary.md` - 共享术语库
- `workflows/core-user-flows.md` - 用户主要流程

## 非权威源

不应信任这些文件为确认事实（仅供参考）：
- `approved-prds/` - 历史 PRD，风格参考用
- 任何尚未 commit 的草稿

## 核心规则

### 1. 区分事实层次

始终明确区分：
- **确认事实** - 已在 `facts/` 中明确记录
- **提议想法** - 本次讨论中新出现的想法
- **工作假设** - 为了讨论而做的假设
- **待定问题** - 尚未决定的部分
- **外部宣称** - 对客户/市场的承诺

### 2. PRD 生成规则

生成 PRD 前，必须读取：
- 相关产品的 `facts/` 文件
- 相关的 `workflows/`
- `facts/glossary.md`
- 相关的历史决策日志（如有）

### 3. 决策日志生成规则

每次 PRD 讨论结束后，自动生成决策日志：

位置: `decisions/decision-YYYYMMDD-[功能名].md`

必须包含：
```markdown
# 决策日志：[功能名称]

**日期**: YYYY-MM-DD
**功能**: [简短描述]

## 决策
[具体决定了什么]

## 原因
[为什么这样决定]
- 业务原因
- 合规原因
- 技术原因
- 用户需求

## 假设条件
[为了做这个决定，我们假设...]

## 明确边界
[这个决定包括什么、不包括什么]

## 待定问题
[还需要后续确认的]
```

### 4. 禁止声称

绝不允许在 PRD 中做以下声称（除非已在 facts 中明确确认）：
- 自动阻止/冻结某地址
- 自动提交 SAR/STR（必须人工审核）
- 自动做法律判断
- 与未确认的合作伙伴集成
- 未确认的定价或套餐
- 不在 facts 中的功能

### 5. 冲突处理

如果讨论中发现与现有 facts 的矛盾：
- 不要在 PRD 中直接修改 facts
- 在决策日志中明确记录冲突
- 标记为 `[CONFLICT]`，需要人工审核

## 示例工作流

### 会话 1：地址筛选功能 PRD

```
用户: 帮我写一个关于批量地址筛选的 PRD
Claude Code:
1. 读 facts/phalcon-compliance.md → 确认当前范围
2. 读 facts/glossary.md → 确认术语
3. 读 workflows/core-user-flows.md → 确认流程
4. 读历史决策日志 → 查看是否有相关决策

讨论 PRD 细节...

最后自动生成: decisions/decision-20260414-batch-address-screening.md
包含: 决定支持 10k 批量大小，使用严格匹配模式，不支持实时处理等
```

### 会话 2：交易风险评分 PRD

```
用户: 帮我写一个关于交易风险评分的 PRD
Claude Code:
1. 读 facts/ 和 workflows/（同上）
2. 读历史决策日志，发现 decision-20260414-batch-address-screening.md
3. 引用它: "根据之前的决策，地址匹配使用严格模式，
            所以交易评分时应该也使用严格匹配，保持一致"
   
不需要重新解释这个决定 → 提高效率，减少混淆
```

## 何时更新 facts

只在以下情况更新 `facts/` 文件：
- ✅ 产品功能边界真的改变了
- ✅ 确认了一个新的术语或定义
- ✅ 调整了对某个流程的理解

不应更新：
- ❌ 因为一次讨论而改变（用决策日志记录）
- ❌ 为了某个单独的 PRD 而改变（用决策日志）

---

**最后更新**: 2026-04-14
