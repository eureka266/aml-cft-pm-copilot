# 历史 PRD 存档

这个文件夹存储已确认和上线的 PRD 文档。

## 结构

```
approved-prds/
├── phalcon-compliance/
│   ├── prd-address-screening-v1.md
│   ├── prd-transaction-monitoring-v1.md
│   └── ...
├── phalcon-network/
│   ├── prd-...md
│   └── ...
├── metasleuth/
│   ├── prd-...md
│   └── ...
```

## 使用方式

### 风格参考

Claude Code 在生成新 PRD 时会读这些文件，学习你的：
- PRD 结构
- 写作风格
- 术语使用
- 格式偏好

### 搜索历史决策

虽然正式的决策日志在 `/decisions/` 文件夹，
但这里的 PRD 也包含了历史背景和设计思路。

## 上传新 PRD

完成 PRD 讨论后：
1. Claude Code 自动生成决策日志到 `/decisions/`
2. 你审核决策日志 ✓
3. PRD 最终稿提交到本文件夹对应的产品子文件夹
4. 同时可选：导入到钉钉（待 dingtalk-cli 支持）

## 最后更新

2026-04-14

---

**说明**: 这个文件夹是参考和存档用，不是权威源。
权威源是 `/facts/` 和 `/workflows/` 文件夹。
