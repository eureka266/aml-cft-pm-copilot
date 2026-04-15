# KYT 平台功能初步梳理

[《KYT 产品调研》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=gwva2dxOW4ej4QEdFb9adeRbVbkz3BRL&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

[《KYT Proposal》](https://alidocs.dingtalk.com/api/doc/transit?dentryUuid=ydxXB52LJqqYB29oHAkGoQ6XJqjMp697&queryString=utm_medium%3Ddingdoc_doc_plugin_card%26utm_source%3Ddingdoc_doc)

# 客户类型

背景：基本上是延续监管行业对金融行业的要求。 2019 年，FATF 制定了指导方针，要求各国评估加密货币的风险并对服务提供者进行监管。 2020 年，欧盟通过了第五号反洗钱指令，规定了进一步的交易监控义务。

*   CEX：监管要求较严格，CEX 都会做 KYT 以满足监管/拿牌。
    
*   DEX：监管要求较为模糊，极少数 DEX 有 KYT 需求。
    
*   监管机构：对发牌的 VASP 进行 KYT 监管。
    
*   钱包/支付服务提供商
    
*   其他金融机构等
    

## 用户角色：

*   合规官：关注风险事件处理和报告。
    
*   安全风控人员：配置规则、分析风险趋势。
    
*   技术人员：负责 API 接入等。
    

# 用户流程图

![image](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/a/dvOWAo3Wyfxv8a51/e66c63c112014586b83ab62b8ba7d0581049.png)

*   虚线标注的流程是 KYT 平台不需要有的。
    

核心技术点：地址、资金风险评估，主要涉及到多跳风险传递。

# 功能点