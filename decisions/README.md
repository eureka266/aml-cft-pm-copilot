# 决策日志目录

这个文件夹包含每个 PRD 讨论会议的自动生成的决策日志。

## 文件命名规则

`decision-YYYYMMDD-[功能名].md`

示例:
- `decision-20260414-batch-address-screening.md`
- `decision-20260415-transaction-risk-scoring.md`

## 文件内容结构

每个决策日志应包含：
- 决策内容
- 决策原因
- 假设条件
- 明确边界
- 待定问题

详见 `../CLAUDE.md` 中的"决策日志生成规则"。

## 如何使用

### 查询相关决策

在写新 PRD 时，Claude Code 会自动查看这个文件夹，
找出与新功能相关的历史决策。

### 避免重复解释

如果之前的决策已经解决了某个问题，
Claude Code 会引用它，而不是重新讨论。

## 最后更新

2026-04-14
