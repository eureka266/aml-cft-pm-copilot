# hypernative竞品demo

| 模块 | 主要功能 | 应用场景 |
| --- | --- | --- |
| **1. Screener** | 地址与交易筛查（KYT 类功能）<br>\- 识别高风险钱包<br>\- 追踪资金来源与去向- 生成 Suspicious Transaction Report（含hash、对 手方、时间戳等）<br>\- 支持自定义风险规则（如Mixer曝光比例>30%报警） | 合规、反洗钱、交易监控 |
| **2. Guardian** | 预交易模拟<br>\- 在用户签名前检测恶意合约、钓鱼攻击、资产流向变化- 提醒「不要签名」或自动拦截 | 钱包安全、DeFi 操作保护 |
| **3. Platform (Monitoring)** | 全链实时监控（70+公链）<br>\- 每个区块更新风险标签（比Chainalysis等快数周）<br>\- 支持300+风险类型（黑客攻击、钓鱼、混币、恐怖融资等）<br>\- 可联动Slack / Telegram / Lark 实时通知<br>\- 支持自动化响应（自动pause函数、资金迁移） | 安全事件检测、风险预警、自动化防御 |

根据你上传的《Hypernative Demo Meeting》逐字稿，这场会议透露了大量关于 **Hypernative 的产品能力、销售策略与客户引导逻辑** 的信息。以下是核心信息总结及对 Phalcon Compliance 的参考价值分析：

---

## 🧩 一、Hypernative 的业务定位与客户类型

**核心定位：**

> Web3 安全与风控监控平台，覆盖实时交易监控、风险检测、合规筛查、预交易防护等场景。

**客户群体：**

*   大型基金会（Ethereum L1、Solana Foundation）
    
*   金融机构（Stripe、Circle、Agora）
    
*   交易所与稳定币发行方
    
*   以及 DeFi 协议、托管机构（Fireblocks、MPC 钱包类）
    

**启示：**

> Hypernative 已成功把自己从“安全公司”延伸为“风险与合规基础设施供应商”。  
Phalcon 若要切入类似客户层面，可从「监管合规 + 实时安全」的融合角度包装产品，而非单纯 AML / KYA。

---

## 🧠 二、产品体系拆解（三大核心模块）

| 模块 | 主要功能 | 应用场景 |
| --- | --- | --- |
| **1. Screener** | 地址与交易筛查（KYT 类功能）- 识别高风险钱包- 追踪资金来源与去向- 生成 Suspicious Transaction Report（含hash、对手方、时间戳等）- 支持自定义风险规则（如Mixer曝光比例>30%报警） | 合规、反洗钱、交易监控 |
| **2. Guardian** | 预交易模拟- 在用户签名前检测恶意合约、钓鱼攻击、资产流向变化- 提醒「不要签名」或自动拦截 | 钱包安全、DeFi 操作保护 |
| **3. Platform (Monitoring)** | 全链实时监控（70+公链）- 每个区块更新风险标签（比Chainalysis等快数周）- 支持300+风险类型（黑客攻击、钓鱼、混币、恐怖融资等）- 可联动Slack / Telegram / Lark 实时通知- 支持自动化响应（自动pause函数、资金迁移） | 安全事件检测、风险预警、自动化防御 |

**启示：**

> Phalcon 若要竞争，可强化 **“预警速度 + 自动响应”** 两点：

---

## 📊 三、技术与数据亮点

*   **实时性**：按区块级（Solana 2s、Ethereum 12s）更新；
    
*   **链覆盖面**：70+（包括EVM与非EVM链，Sui/Aptos/Tron都支持）；
    
*   **风险库来源**：
    
    *   OFAC / FATF / UK / EU / Japan / Israel 多地区黑名单；
        
    *   恐怖融资、诈骗、钓鱼、可疑交易所；
        
    *   与 Circle、Tether 等大机构共享黑名单数据；
        
*   **报告生成**：一键导出 STR（适配监管需求）；
    
*   **API 自动化**：全量 API 接口可编程调用，避免人工筛查。
    

**启示：**

> Phalcon 可重点优化：

---

## 💬 四、销售与产品引导策略

1.  **三步推介逻辑：**
    
    *   先问使用场景（合规？风控？安全？）
        
    *   再介绍三个产品的差异化功能
        
    *   最后锁定“最有价值”的模块（screener）
        
2.  **试用策略：**
    
    *   提供 **1周 Guided Trial（带引导的沙盒）**
        
    *   要求客户明确测试目标与 use case
        
    *   提供 test case 模板，模拟典型风险事件（如 DeFi 被攻击）
        
    *   通过 Telegram 群组持续支持和引导测试
        
3.  **应对质疑策略：**
    
    *   当客户提到“有项目反映监控失败”时，强调：
        
        *   问题来自客户未正确配置（未设 watchlist、未接收通知）
            
        *   Hypernative 全部攻击均“检测到”，但未执行自动响应
            
    *   并举例 Balancer、Kinetic 成功阻止攻击的案例
        

**启示：**

> Phalcon 可以借鉴这种销售节奏：

---

## 🧩 五、Phalcon Compliance 可借鉴与差异化方向

| 方向 | Hypernative 的优势 | Phalcon 可参考改进 |
| --- | --- | --- |
| **定位** | “Security + Risk + Compliance” 一体化 | 将 KYA/KYT 与安全联动，如 “Address risk + On-chain Behavior Risk” |
| **更新频率** | 每区块实时标签更新 | 优化后端 pipeline 提速，或引入 “Near real-time mode” |
| **试用体验** | Guided Trial + Test Cases + 群组支持 | 设计 Guided Sandbox + 测试模板化体验 |
| **报告能力** | 一键 STR，含交易细节 | 对齐 FATF SAR 结构，支持 PDF 导出 |
| **响应机制** | 可触发 on-chain 自动操作 | 可推出 “Risk Engine Action” 自动响应层 |
| **合规覆盖** | 多地区 sanction 数据源 | 加入监管多元化标签（欧盟、日本、新加坡等） |
| **销售逻辑** | 强调实时性差异化（对比 Chainalysis/TRM） | 突出 “精准度 + 成本效益” 作为差异化竞争点 |

---

## 🔍 六、总结一句话

> Hypernative 的核心竞争力在于 **“区块级实时检测 + 自动化防护 + 合规可解释性”**；  
Phalcon 若要在竞品对比中脱颖而出，应强化 **“合规精准度 + 可操作的安全响应 + 高体验度 Sandbox”** 三个维度。

---

是否希望我帮你把这一份总结改写成一页内部分享用的简报稿（比如《Hypernative Demo 情报速览 – 对 Phalcon 的启示》），我可以帮你直接排版成结构化要点。