# 快速开始：Next 3 Steps

你的 PM Copilot 知识库已经创建好了。现在是：

```
/tmp/aml-cft-pm-copilot/
```

## Step 1: 上传到 GitHub (5 分钟)

### 方法 A: 使用命令行

```bash
# 创建一个空 GitHub repo，名字随你喜欢，比如 aml-cft-pm-copilot

# 然后在本地运行：
cd /tmp/aml-cft-pm-copilot
git remote add origin https://github.com/YOUR-USERNAME/aml-cft-pm-copilot.git
git branch -M main
git push -u origin main
```

### 方法 B: 在 GitHub 上先创建，再 clone

到 https://github.com/new 创建 repo，然后：

```bash
git clone https://github.com/YOUR-USERNAME/aml-cft-pm-copilot.git
# 把所有文件复制进去，然后 git push
```

## Step 2: 更新产品信息 (30 分钟)

这些文件需要你的真实数据（现在是占位符）：

1. **`facts/phalcon-compliance.md`** - 现在只是样本，请根据钉钉文档更新
2. **`facts/phalcon-network.md`** - 改成实际的定义
3. **`facts/metasleuth.md`** - 改成实际的定义
4. **`facts/glossary.md`** - 你们的实际术语，我这里只是示例
5. **`workflows/core-user-flows.md`** - 确认工作流是否准确

这 5 个文件是你的"权威源"。建议花 30 分钟把钉钉里的信息整理到这里。

## Step 3: 开始用 (现在就行)

下一次你要写 PRD 时：

```
你: "帮我写一个关于 [功能名] 的 PRD，这是我的知识库：https://github.com/YOUR-USERNAME/aml-cft-pm-copilot"

Claude Code:
1. 读你的 facts + workflows
2. 查看历史决策（如果有的话）
3. 讨论新功能
4. 自动生成 PRD + 决策日志

你: 审核决策日志，眼睛过一遍，确认没问题

然后: git add decisions/decision-YYYYMMDD-[功能].md && git commit && git push

完成。下次有相关功能，Claude Code 直接参考这个决策，不用重复解释。
```

---

## 关键文件说明

| 文件 | 用途 | 谁维护 |
|-----|------|------|
| `facts/` | 产品事实（权威源） | 你定期更新 |
| `workflows/` | 用户工作流 | 你定期更新 |
| `decisions/` | PRD 会议的决策日志 | Claude Code 自动生成，你审核 |
| `approved-prds/` | 历史 PRD 存档 | 你上传确认的 PRD |

## 可选：加入历史 PRD

现在 `approved-prds/` 是空的。如果你想加入过去的 PRD 作为参考：

```bash
# 从钉钉下载几个最好的 PRD，转成 Markdown
# 放到对应的文件夹：
# approved-prds/phalcon-compliance/prd-地址筛选-v1.md
# approved-prds/phalcon-compliance/prd-交易监控-v1.md
# 等等

# Claude Code 会读这些，学习你的风格
```

这不是强制的，但有帮助。

---

## 钉钉集成（待后续）

`scripts/dingtalk-integration.md` 里记录了整合计划。
目前 dingtalk-workspace-cli 还不支持文档导出，但一旦支持了，
我们可以写脚本自动导出 / 导入。

---

## 你的第一个决策日志什么样

当你和我讨论完第一个 PRD，我会生成这样的文件：

```
decisions/decision-20260415-address-screening-batch.md

# 决策日志：批量地址筛选 API

**日期**: 2026-04-15  
**功能**: 批量地址筛选 API

## 决策
支持单次最多 10,000 个地址的批处理。
使用严格模式匹配（必须完全一致），不支持模糊匹配。
响应时间预期 2-3 分钟。

## 原因
- 用户需要高置信度（SAR 报告需要确定性）
- 模糊匹配会导致太多误报
- 批量大小 10k 覆盖 95% 的实际用例

## 假设条件
- 用户可以接受 2-3 分钟的延迟
- 黑名单数据每周更新一次就够

## 明确边界
- 不支持：实时处理、模糊匹配、跨链查询
- 支持：单批 10k 地址、多种地址格式、重试机制

## 待定问题
- 需要确认是否要支持多链地址（EVM、比特币等）
- 定价模型还没决定
```

下次你写交易风险评分相关的 PRD，我会先读这个决策，说：

> "根据你之前的决策，地址匹配用严格模式。
> 所以交易评分时也应该用严格匹配保持一致。
> 不需要再讨论这个。"

省时间，减混淆 ✅

---

## 就这样

现在你的系统已经准备好了。

接下来只需要：
1. 上传到 GitHub
2. 更新 5 个产品事实文件
3. 开始写 PRD，让决策自动沉淀

祝好 🚀

---

**Created**: 2026-04-14  
**System**: PM Copilot (Decision-focused, 2-PM Edition)
