# AML/CFT PM Copilot Decision System

BlockSec 内部产品经理知识库与决策系统。用于稳定、可追溯地生成 PRD 和 Demo 文档。

## 文件夹结构

```
├── README.md              # 本文件
├── CLAUDE.md              # Claude Code 使用规则
├── facts/                 # 产品事实（权威源）
├── workflows/             # 用户工作流（权威源）
├── decisions/             # 每个 PRD 会话的决策记录（自动生成）
├── approved-prds/         # 历史 PRD 存档（参考）
└── scripts/               # 钉钉集成脚本（待开发）
```

## 快速开始

1. 给 Claude Code 这个 repo 的链接
2. 开始写新的 PRD 时，Claude Code 会自动：
   - 读取 `facts/` 和 `workflows/`
   - 查阅相关的历史决策
   - 生成 PRD 和决策日志
3. 你审核决策日志，确认后 commit

## 权威源

始终信任这些文件作为产品真相：
- `facts/phalcon-compliance.md`
- `facts/phalcon-network.md`
- `facts/metasleuth.md`
- `facts/glossary.md`
- `workflows/core-user-flows.md`

## 决策日志

每次 PRD 会话后，Claude Code 自动生成决策日志到 `decisions/` 文件夹。
格式: `decision-YYYYMMDD-[feature-name].md`

包含：
- 决策内容
- 决策原因
- 假设条件
- 明确边界
- 待定问题

## 钉钉集成

TODO: 当 dingtalk-workspace-cli 支持文档导出后，
在 `scripts/` 下添加导入/导出脚本。

---

**最后更新**: 2026-04-14  
**维护者**: BlockSec PM Team
