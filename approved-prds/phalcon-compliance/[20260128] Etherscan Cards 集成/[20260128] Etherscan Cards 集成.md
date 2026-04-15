# \[20260128\] Etherscan Cards 集成

# 背景

Etherscan 在地址详情页中提供 Cards 区域，允许第三方数据服务商为地址补充额外信息。一方面为地址提供更丰富的数据信息，另一方面为数据提供方引流至其产品或平台。

示例：

*   EOA: [https://etherscan.io/address/0x67a7ee62151e943d30ea26b109f3bd2ba656ae3b#cards](https://etherscan.io/address/0x67a7ee62151e943d30ea26b109f3bd2ba656ae3b#cards)
    
*   CA: [https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#cards](https://etherscan.io/address/0xdac17f958d2ee523a2206206994597c13d831ec7#cards)
    

#### 目标

*   在 Etherscan 地址详情页中，提供 Phalcon Compliance 的地址风险摘要卡片
    
*   在高访问量场景下展示轻量级风险结果
    
*   **引导用户跳转至 Phalcon Compliance 查看完整合规分析**
    

## 场景与问题

Etherscan Cards 场景具备以下特征：

*   API 高频请求，预计 **最高 100k 次 / 天**
    
*   尽量低延迟 （可以做缓存）
    
*   Cards 区域定位为**信息补充与引导**，而非完整分析展示
    

因此不太适合直接用 Compliance 的能力提供，考虑使用 Risk Score API 实现该集成。

> Risk Score API 算法：[《Risk Score API》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=2X3LRMZdxkAJpee3RYNw8GgrBYeOq5Ew&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

> 对外 API 文档：[https://docs.metasleuth.io/blocksec-aml-api/wallet-screening-api](https://docs.metasleuth.io/blocksec-aml-api/wallet-screening-api)

和对方确认过，下面的配置可符合需求：

*   5 rps
    
*   time out 5s
    

# 方案

## 地址类型支持

可以和 Risk Score API 保持一致，同时支持 EOA 与 CA

*   EOA：实体风险 + 交互风险
    
*   CA：仅考虑实体风险（Risk Score API 现在的逻辑）
    

Etherscan 在请求 Cards 时应该可以传地址类型参数：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/meonarb79GjMQqXx/img/3c8f673e-247f-46fa-91db-d33fda25510d.png)

## 展示内容

设计稿如图：[https://www.figma.com/design/lJYNMUF6CkwW5VPOzKTzwK/Etherscan-Cards?node-id=23-597&t=NTo02GJ8tT98JAGY-0](https://www.figma.com/design/lJYNMUF6CkwW5VPOzKTzwK/Etherscan-Cards?node-id=23-597&t=NTo02GJ8tT98JAGY-0)

| 模块 | 字段 | 说明 |
| --- | --- | --- |
| Card 标题 | Address Compliance Risk |  |
| Card 内容 | Risk Overview + info 图标 | Hover 到 info 后展示 tips：<br>“This view shows a lightweight risk summary based on recent high-signal activity. The full report includes more comprehensive analysis and historical data.” |
|  | Risk Level | Critical、High、Medium、Low、No Risk<br>（对应于 Risk Level： 5-1） |
|  | Risk Indicator | 包含自身或交互风险，区分方向 |
|  | Risk Summary | 一句话概括地址当前风险情况，具体规则见 API 文档说明 |
|  | Powered by BlockSec |  |
| 跳转按钮 | View Detail on Phalcon Compliance | *   拼接地址，可以直接跳转 Compliance 展示结果页（登录限制等和 Compliance 保持一致）<br>    <br>*   带 utm 信息 |

#### 跳转 Phalcon Compliance 路径

示例：

[https://app.blocksec.com/phalcon/compliance/scan1/0x67a7ee62151e943d30ea26b109f3bd2ba656ae3b?utm\_source=etherscan&utm\_campaign=cards](https://app.blocksec.com/phalcon/compliance/scan1/0x67a7ee62151e943d30ea26b109f3bd2ba656ae3b?utm_source=etherscan&utm_campaign=cards)

要求：

*   包含 chain id，address
    
*   路径后续不会轻易改动，需要一直兼容
    
*   utm\_source: etherscan
    
*   utm\_campaign: cards
    

## 兼容 Risk Score API

需要做以下兼容处理：

### Risk Indicator 过滤与转换

根据 Risk Score API 返回的 Risk Indicator（见：[https://docs.metasleuth.io/blocksec-aml-api/wallet-screening-api#how-is-risk-assessed](https://docs.metasleuth.io/blocksec-aml-api/wallet-screening-api#how-is-risk-assessed)），需进行过滤和合并，最终仅展示 Compliance 所支持的 Risk Indicator（[《Risk Engine》](https://alidocs.dingtalk.com/i/nodes/P7QG4Yx2JpAbqpvoT5gb2A0A89dEq3XD?utm_scene=team_space&iframeQuery=anchorId%3Duu_m8sfey79g2nms4tnygi) ）。

注意：API 中 Suspicious 和 Compromised 两个 Indicator 目前 Compliance 暂不支持，若地址包含这两项，返回时需将其剔除。同时，若地址仅命中这两类 Indicator，其风险等级应默认为 Low Risk。

#### 交互方向判断

针对 Interaction Risk，API 会返回对应的 Risk Interaction 列表。需根据列表中的 transfer 记录，判断该地址与风险地址之间的交互方向——是 incoming、outgoing，还是 both。

#### No Risk 地址的 Entity 信息补充

Risk Score API 的设计中，仅当地址明确无风险时才会返回 No risk（risk score = 1）。对于此类结果，需额外调用 Address Label API，查询该地址的 Entity Name，用于前端展示。

## API 文档

[《API Documentation》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=dpYLaezmVNKEra7Xcknj6qdxJrMqPxX6&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

# Etherscan 方要求

thanks for waiting! now that the integration agreement is signed, as next steps could you share with us:

1.  title of the card you'd like to display (what it's used for)
    
2.  the info we should display inside the card (mockup optional)
    
3.  your API endpoint that corresponds to the data that we should call
    
4.  link to your site with an address as URL param (that we will redirect to from the card)
    

if your API endpoint meets our standards and your design can follow one of the templates below, we'll be able to integrate it much faster:

API stands HTTP-GET API (POST API can be supported later if needed)

1.  only one endpoint per card
    
2.  if API Key is required, then:
    
    1.  include relevant details in request headers, i.e. x-api-key, authorization, etc
        
    2.  include it as param in query string, i.e. apikey=\[ApiKeyHere\]
        
3.  \[address\] parameter is required (route-parameter or query-string)
    
    1.  chainId / chainName are required if supporting multichain
        
4.  API response should be:
    
    1.  in JSON format
        
    2.  include properties for checking API status if all requests are returned as 200-OK, for example:
        
        1.  success: true
            
        2.  status: "ok"
            
        3.  message: "ok"
            
    3.  ready to use - should not require custom logic/procedure to get data
        

note: the API may get spikes in traffic from Etherscan. we prepare for up to 100k calls per day and we do implement caching.

Design Templates:

1.  Bankless
    
2.  Vaults.fyi
    
3.  GoPlus
    

reference for templates here:  https://etherscan.io/address/vitalik.eth#cards https://etherscan.io/address/0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48#cards

if you'd like a design unique from the templates above, you can draft the html code for it. we'll review + adjust it to fit our code

*   you can inspect element on a live card on etherscan and edit the card-body to suit your design
    
*   you can also refer to this base html structure:
    

```json
<div class="card-body d-flex flex-column gap-7 p-4" [styling]>
   [Sub-title]
   [Card data]
   [Powered By]
</div>
```