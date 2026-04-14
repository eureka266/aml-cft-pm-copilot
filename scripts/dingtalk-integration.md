# Dingtalk 集成计划

## 目标

使用 [dingtalk-workspace-cli](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli) 
自动导出钉钉历史 PRD 文档，并导入确认的 PRD 文件到钉钉。

## 当前状态

❌ 待实现 - dingtalk-workspace-cli 暂不支持文档导出功能

## 预期工作流

### 导出历史 PRD

```bash
dingtalk workspace export-document \
  --space-name "ProductDocs" \
  --folder-name "PRDs" \
  --output-dir "./approved-prds/"
```

### 导入确认的 PRD

```bash
dingtalk workspace import-document \
  --file ./prd-drafts/new-prd.md \
  --target-space "ProductDocs" \
  --publish true
```

## 依赖项

- [ ] dingtalk-workspace-cli 添加文档导出 API
- [ ] dingtalk-workspace-cli 添加文档导入 API
- [ ] 脚本编写和测试

## TODO

1. 关注 dingtalk-workspace-cli 的发布更新
2. 文档导出功能发布后，编写导出脚本
3. 文档导入功能发布后，编写导入脚本
4. 集成到 PR/commit workflow（可选）

---

**最后更新**: 2026-04-14  
**所有者**: BlockSec PM Team
