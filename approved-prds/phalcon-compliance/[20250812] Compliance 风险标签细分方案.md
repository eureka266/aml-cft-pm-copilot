# \[20250812\] Compliance 风险标签细分方案

# 背景与目标

在 KYT / KYA 场景中，风险扫描结果需要更细粒度的区分，原因包括：

*   **可解释性**：客户希望明确知道风险的具体来源和细节，提升信任度与透明度。
    
*   **可定制化风控**：部分客户只关心特定类型的风险来源（例如仅关注某几个无 KYC 交易所），如果 API 返回更详细的信息，客户可在本地自定义风控规则。
    

## 现有 Risk Indicator 列表

| Risk Indicator | 说明 | 涉及标签 |
| --- | --- | --- |
| Sanctioned | 地址所属实体被制裁 | SANCTIONED |
| Attack | 攻击事件相关地址 | ATTACKER, EXPLOIT |
| Scam | 欺诈活动相关地址，包括 phishing、honeypot 等各种类型的欺诈活动 | SCAM |
| Ransomware | 勒索软件地址 | RANSOMWARE |
| Child Abuse Material | 儿童色情相关地址 | CHILD ABUSE MATERIAL |
| Laundering | 有洗钱行为的地址 | LAUNDERING |
| Mixing | 混币器或提供洗钱服务的隐私服务等的地址 | MIXING, MIXER |
| Dark Market | 暗网市场地址 | DARK MARKET |
| Darkweb Business | 在暗网中活动的小作坊或个人经营者地址 | DARKWEB BUSINESS |
| Blocked | 被著名合约（如 USDC、USDT）地址拉黑的地址 | BLOCKED |
| Gambling | 赌博服务相关地址 | GAMBLING |
| No KYC Exchange | 无 KYC 或 弱 KYC 的交易所地址 | NO KYC |
| Terrorist Financing | 与恐怖主义融资相关的地址（如资金流向恐怖组织、为恐怖活动提供支持） | TERRORIST, TERRORIST FINANCING |
| FATF High Risk Jurisdiction | 注册地位于 FATF 黑名单国家/地区的实体地址（如该地区交易所、机构地址） | FATF HIGH RISK JURISDICTION |
| FATF Grey List Jurisdiction | 注册地位于 FATF 灰名单国家/地区的实体地址（如土耳其、缅甸交易所） | FATF GREY LIST |

## 现状和存在问题

### 实体风险

*   当前展示：命中的 **Risk Indicator + Detail 信息**（参考[《Alert》](https://alidocs.dingtalk.com/i/nodes/Y1OQX0akWmq7PNyoHkbrR2yBWGlDd3mE?utm_scene=team_space&iframeQuery=anchorId%3Duu_m9i5yhymlm5dptabugf)）![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/8ccd3ee7-76b4-4cd3-bf2c-11d8c6f4063a.png?x-oss-process=image/crop,x_0,y_618,w_2122,h_374/ignore-error,1)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/7a5c5c5c-4a00-4c24-885d-2b8595e648be.png?x-oss-process=image/crop,x_0,y_651,w_2110,h_355/ignore-error,1)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/5a99610a-c0ee-437b-bb7f-9f7bb28a5de4.png)
    

*   API 会返回地址的 label、entity、category、tags
    
*   提供的信息基本可以满足需求，仍然有一些问题：
    
    1.  **数据结构分散**：Risk Indicator & Detail 信息在 Alert 字段获取，地址标签信息在外层字段，不够结构化。
        
    2.  **信息缺失**：例如 下图所示 Terrorist Financing 这种 indicator 的 detail 信息缺失
        

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/3ab317de-ebbd-4478-b3f5-96d774032640.png)

### 交互风险

*   现状：Alert 和 API 中仅展示 **一级 Risk Indicator**
    

*   Alert 会将同一方向的 Risk Indicator 合并，导致二级标签无法直接展示
    

*   改进：如展示所有二级标签，需分别列出其对应的 **Exposure value** 与 **percent**，例如：
    
*   Attack         |         Incoming        |               1 Hop           |         $10,000          |        20%
    
    *   Bybit Exploiter         |          1 Hop         |          $5,000         |         10%
        
    *   Infini Exploiter         |         2 Hops         |         $5,000          |         10%
        

# Risk Indicator 补充信息 

为了提高风险可解释性和定制化处理，**Risk Indicator** 需要在 **Entity Risk** 和 **Interaction Risk** 类型的 Alert 中补充展示详细信息。

具体展示的详细信息如下：

| Risk Indicator | 补充信息 | 获取字段 |
| --- | --- | --- |
| Sanctioned | 展示制裁名单来源，如： OFAC / NBCTF / MOFJ / OFSI / 特定国家名单 | attribute 的 comp\_info |
| Attack | 展示具体的攻击事件，如：Bybit Exploiter / Infini Exploiter | *   如果 risk indicator 是 地址的  attribute <br>    <br>    *   展示 attribute 的 comp\_info<br>        <br>*   如果 risk indicator 是 entity 的 attribute<br>    <br>    *   展示 entity name |
| Scam | 展示细化的诈骗类型，如：Phishing / Honey Pot |
| Ransomware | 展示具体的勒索家族，如：Conti / REvil / LockBit | entity name |
| Child Abuse Material | ？<br>展示具体的实体名称 | entity name |
| Laundering | ？<br>展示具体的洗钱事件 | attribute 的 comp\_info |
| Mixing | 展示具体的实体名称，如：Tornado Cash 等 | *   如果 risk indicator 是 地址的  attribute <br>    <br>    *   展示 attribute 的 comp\_info<br>        <br>*   如果 risk indicator 是 entity 的 attribute<br>    <br>    *   展示 entity name<br>        <br>*   如果 risk indicator 是 entity 的 category<br>    <br>    *   展示 entity name |
| Dark Market | 展示具体的实体名称，如： Silk Road 等 | entity name |
| Darkweb Business | 展示具体的暗网业务子类，如：Account Selling, Weapon | attribute 的 comp\_info |
| Blocked | 展示具体 Block 的合约信息，如：Blocked by USDT | attribute 的 comp\_info |
| Gambling | 展示具体的实体名称，如：Stake.com | entity name |
| No KYC Exchange | 展示具体的实体名称，如：ChangeNow | entity name |
| Terrorist Financing | ？<br>展示具体的恐怖主义事件/恐怖组织名称 | *   如果 risk indicator 是 地址的  attribute <br>    <br>    *   展示 attribute 的 comp\_info<br>        <br>*   如果 risk indicator 是 entity 的 attribute<br>    <br>    *   展示 entity name<br>        <br>*   如果 risk indicator 是 entity 的 category<br>    <br>    *   展示 entity name |
| FATF High Risk Jurisdiction | 展示实体名称 + 国家/地区名称，如：Nobitex.ir - Iran<br>格式：{实体名称} + {国家/地区名称} | entity + ？<br>entity +  entity 的 country name 字段 ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/6a9e34d9-92f8-4eea-8133-0e77b0c56907.png) |
| FATF Grey List Jurisdiction | 展示实体名称 + 国家/地区名称，如：Ourbit - British | entity + ？<br>entity +  entity 的 country name 字段 ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/6a9e34d9-92f8-4eea-8133-0e77b0c56907.png) |

## Entity Risk

*   对于大多数 **Risk Indicator**，Entity Risk Alert 已正确展示 **detail** 信息。
    

*   对于 **FATF High Risk Jurisdiction** 和 **FATF Grey List Jurisdiction**，需要拼接两个字段（实体名称 + 国家/地区），以便完整展示。
    

## Interaction Risk 

### 阶段一：

仅在 API 中展示

原来：

*   从图数据库获取所有风险路径后，按照 Risk Indicator + Direction 进行分组展示结果
    

*   **处理流程**： $\color{#0089FF}{@贺秋实}$ 
    
    1.  从图数据库获取所有风险路径后，查询携带 **Risk Indicator** 的地址，并从标签库获取补充信息（和 Entity Risk 的 detail 字段获取方式一致）。
        
    2.  根据补充信息，在原始 **Risk Indicator + Direction** 分组基础上，再按补充信息细分。
        
        *   如果未能获取详细信息，直接使用 **Risk Indicator** 作为描述。
            
        *   如果 **Risk Indicator** 下所有项均无补充信息，则不展示小组。
            
    3.  对每个小组展示最小跳数（Hop）、**exposure value** 和 **exposure percent**。
        

 **原来展示示例** ：

● Attack        | Incoming      | 1 Hop       | $10,000      | 20%

**增加详细信息后**：

● Attack        | Incoming      | 1 Hop       | $10,000      | 20%

    ○ Bybit Exploiter | 1 Hop   | $5,000      | 10%

    ○ Infini Exploiter | 2 Hops  | $5,000     | 10%

#### API  字段修改

原来展示字段：

```json
{
    "riskIndicator": 2,
    "riskIndicatorDescription": "Attack",
    "direction": "incoming",
    "hop": 5,
    "exposureValue": "0.274347023254633781",
    "exposurePercent": "0.000000025082790309778913"
},
```

补充详细信息后：

```json
{
    "riskIndicator": 2,
    "riskIndicatorDescription": "Attack",
    "direction": "incoming",
    "hop": 5,
    "exposureValue": "0.274347023254633781",
    "exposurePercent": "0.000000025082790309778913",
    "contributions": [
        {
            "detail": "Bybit Exploiter", //补充信息
            "hop": 1,
            "exposureValue": "0.1456",
            "exposurePercent": "0.0000000012"
        },
        ...
    ]
}
```

# 二级标签定义（TBD）

| Risk Indicator | 二级标签（示例） | 补充信息 | 划分逻辑 |
| --- | --- | --- | --- |
| Sanctioned | OFAC / NBCTF / MOFJ / OFSI / 特定国家名单 |  | 按制裁名单来源划分 （要不要展示实体？） |
| Attack |  | Bybit Exploiter / Infini Exploiter | 按具体的攻击事件划分？ |
| Scam | Phishing / Ponzi / Rug Pull / Honeypot / 等 |  | 按诈骗类型划分? 还是具体的事件？ |
| Ransomware |  | Conti / REvil / LockBit | 按勒索软件家族划分 |
| Child Abuse Material |  |  | 待补充可细分来源 |
| Laundering |  |  | 展示实体名称？ |
| Mixing |  | Tornado Cash / ChipMixer / Blender.io 等 | 按混币服务提供者划分 |
| Dark Market |  | Silk Road / Hydra / AlphaBay 等 | 按暗网市场名称划分 |
| Darkweb Business |  |  | 按暗网商家 ID 划分 |
| Blocked | Blocked by USDT，Blocked by USDC |  | 按拉黑的合约平台划分 |
| Gambling |  | Stake.com / Rollbit / 1xBit 等 | 按赌博平台划分 |
| No KYC Exchange |  | 实体名称 | 按交易所名称划分 |
| Terrorist Financing |  | Hamas / ISIS / Al-Qaeda 等 | 按组织名称划分 |
| FATF High Risk Jurisdiction | 国家/地区 | 实体 | 按国家划分 ? 按实体名称 |
| FATF Grey List Jurisdiction | 国家/地区 | 实体 | 按国家划分 ? 按实体名称 |

也可以考虑展示：一级标签 + 二级标签 + Entity 名称

# 参考

## Elliptic

*   二级标签结构：**Entity → Category**
    
*   可在规则配置时选定 Entity / Category / 国家
    

在规则配置时，可以指定到 Entity 或 Category 或国家/地区。![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/08881787-8a7a-4864-bdc7-b4c7ec03e43d.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/d9123cdf-dd6b-4571-82f9-8a7fc0129301.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/626084f6-ef76-4811-b13f-7e5fd3fce8c4.png)

## Merkle Science

*   三级标签结构： Entity -> Entity Sub-Type -> Entity Type
    

每个标签的地址都有自己的 Entity，每个 Entity 有 Entity Type 和 Entity Sub-Type，规则配置时可以配置到 Entity Type 或 Entity Sub-Type 或 Entity Name，在界面/API 返回时会同时包含 这三项信息。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/7c1709c4-bd53-444c-a459-db0d59e37c50.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/b6d6eef3-2da1-4324-96f2-2d2e22692bfe.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/AJdl65AdyoaeaOke/img/3f78d39a-9ce0-41a4-b713-43c1e85e075b.png)