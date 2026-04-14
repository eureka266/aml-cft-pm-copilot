# Glossary: AML/CFT 术语库

## 核心合规术语

| 术语 | 定义 |
|-----|------|
| **AML** | Anti-Money Laundering（反洗钱） |
| **CFT** | Combating the Financing of Terrorism（反恐融资） |
| **KYC** | Know Your Customer（了解你的客户） |
| **SAR** | Suspicious Activity Report（可疑活动报告） |
| **STR** | Suspicious Transaction Report（可疑交易报告，部分司法管辖区使用） |
| **Entity** | 实体 - 个人或组织（个人、公司、钱包地址等） |
| **Risk Score** | 风险分数 - 数值 0-100，表示合规风险等级 |

## 产品特定术语

| 术语 | 定义 |
|-----|------|
| **Address Screening** | 地址筛选 - 检查某地址是否在黑名单/制裁名单上 |
| **Batch Processing** | 批处理 - 一次提交多个地址查询 |
| **Watchlist** | 黑名单/监控名单 - AML、制裁、PEP 等 |
| **PEP** | Politically Exposed Person（政治公众人物） |
| **Match** | 匹配 - 地址/实体在某黑名单上找到了记录 |
| **False Positive** | 误报 - 实际不是犯罪，但被标记为风险 |
| **Case** | 案例 - 一组相关警报的集合，需要调查 |
| **Compliance Officer** | 合规官员 - 使用 Phalcon 进行风险识别的人员 |

## Phalcon 产品术语

| 术语 | 定义 |
|-----|------|
| **Screening Result** | 筛选结果 - 返回 "Match Found" / "No Match" / "Uncertain" |
| **Transaction Monitoring** | 交易监控 - 持续观察交易，触发预设规则时生成警报 |
| **Alert** | 警报 - 监控规则触发时生成的通知 |
| **Triage** | 分类 - 合规官员对警报的初步审查和分类 |
| **Investigation** | 调查 - 对警报或案例的深入审查 |

## 司法管辖区相关

| 缩写 | 定义 |
|-----|------|
| **FinCEN** | Financial Crimes Enforcement Network（美国金融犯罪执法部门） |
| **FATF** | Financial Action Task Force（反洗钱金融行动特别工作组） |
| **EU** | European Union（欧盟） |
| **HK** | Hong Kong（香港） |

## 最后更新

2026-04-14

---

**说明**: 这份术语表是所有 PRD 和讨论的基础。
如果引入新术语，请更新此文件并记录在决策日志中。
