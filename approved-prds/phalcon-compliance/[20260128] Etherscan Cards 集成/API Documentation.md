# API Documentation

# Endpoint

Base url: https://api.blocksec.com/phalcon/compliance

Endpoint: GET `/address-risk`

# Request Parameterss

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `address` | String | Yes | Blockchain address |
| `chainId` | Number | Yes | Chain identifier (see full supported chain list below) |
| `isCA` | Boolean | No |  |

### Authentication

**Request Header**

```json
x-api-key: YOUR_API_KEY
```

# Response Filed

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `code` | Number | 0 表示成功；其他表示失败 |
| `message` | String | “Success” 或错误信息 |
| `data` | Object | 风险结果信息 |

`**data**` **Object**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `address` | String | 地址 |
| `chainId` | Number | chain id |
| `riskScore` | Number | 风险评分（1–5） |
| `riskLevel` | String | One of: `No Risk`, `Low`, `Medium`, `High`, `Critical` |
| `riskLevelCss` | String | 风险等级对应的 CSS 类名（要确认一下是他们定还是我们定这个 CSS class） |
| `riskIndicators` | Array of \[Object\] | 风险指标列表 |
| `riskIndicatorTags` | String | 包含所有风险指标标签的 HTML 字符串 |
| `riskSummary` | String | 风险摘要文本，可能包含 HTML 文本<br>具体生成规则和格式见下面详细说明 |
| `updatedAt` | Number | 表示最后更新时间的 Unix 时间戳（秒） |

`**riskIndicator**` **Object**

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | Number | Risk indicator |
| `name` | String | Risk indicator 名称 |
| `type` | String | Risk category (e.g. `Entity Risk`, `Interaction Risk`) |
| `direction` | String | Fund flow direction.<br>Available when `type` is `Interaction Risk`: `Incoming`, `Outgoing`, or `Both`.<br>Not applicable for `Entity Risk`. |

#### Risk Summary 生成规则

1.  Medium / High / Critical Risk
    

*   **实体风险**  
     **Associated with {entity\_risk\_indicator\_list} entities**
    
*   **交互风险**  
     **Has fund links to {interaction\_risk\_indicator\_list} addresses**
    

说明：

*   由于当前实现基于 Risk Score API，根据 Risk Score API 的设计，一个地址不会同时有实体风险和交互风险。
    
*   如果地址有多个 Risk Indicator，最多展示 2 个，当有 2 个 Risk Indicator 时，risk indictaor 拼接规则是：**{indicator\_1} and {indicator\_2}**
    

1.  Low Risk 
    
    Risk Summary 内容：No identified entity or high-risk activity found in recent history
    
2.  No Risk 
    

Risk Summary 内容：Verified Entity: {entity\_name\_tag}

格式：文字 + HTML （如下图）

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/MAeqxebpoVpRKO8j/img/2ed4f362-835f-4d8d-a7fb-b8c2bfe4462b.png)

# Other 

### Supported Chains

| Chain Name | Chain ID |
| --- | --- |
| ETH | 1 |
| BSC | 56 |
| Polygon | 137 |
| Base | 8453 |
| Optimism | 10 |
| Avalanche | 43114 |
| Arbitrum | 42161 |

### Risk Indicators

| **ID** | **Risk Indicator** | **Description** |
| --- | --- | --- |
| 1 | Sanctioned | Addresses associated with entities designated on official sanctions lists (e.g., OFAC SDN). |
| 2 | Attack | Addresses tied to attackers, exploit contracts, or related fund transfers. |
| 3 | Scam | Addresses involved in fraudulent schemes, including phishing, Ponzi, honeypot, or pig-butchering scams. |
| 4 | Ransomware | Addresses controlled by ransomware operators or used for extortion payments. |
| 5 | Child Abuse Material | Addresses facilitating transactions for platforms distributing child sexual abuse material (CSAM). |
| 6 | Laundering | Addresses suspected of engaging in money laundering activities. |
| 7 | Mixing | Addresses belonging to cryptocurrency mixers or privacy services that obscure transaction trails. |
| 8 | Dark Market | Addresses operated by darknet marketplaces (e.g., Hydra). |
| 9 | Darkweb Business | Addresses involved in illicit darkweb commerce (e.g., weapon sales, identity theft). |
| 10 | Blocked | Addresses blacklisted by major smart contracts or issuers (e.g., USDT, USDC). |
| 11 | Gambling | Addresses belonging to online gambling platforms. |
| 12 | No KYC Exchange | Addresses linked to virtual asset service providers lacking robust Know-Your-Customer procedures. |
| 13 | Terrorist Financing | Addresses linked to terrorist organizations or used for funding terrorist activities. |
| 14 | FATF Grey List Jurisdiction | Entities registered in countries or regions listed on the FATF grey list. |
| 15 | FATF High Risk Jurisdiction | Entities registered in countries or regions listed on the FATF blacklist. |
| 16 | Human Trafficking | Addresses linked to organizations or transactions involved in human trafficking activities. |
| 17 | Drug Trafficking | Addresses linked to entities (such as a person, group, or organization) that are involved in the illegal production, transportation, or distribution of drugs. |