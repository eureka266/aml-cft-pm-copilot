# Beosin KYT

Beosin 界面使用不收费，API 收费，Points 计费模式，扫描一次交易/transaction 即消耗一个 point.

# 总结

| Feature |  | Beosin | Phalcon |
| --- | --- | --- | --- |
| 链 & 资产支持 |  | 20 条链，自定义 Token 配置。 |  |
| 风险规则 | Exposure | *   29 个 Risk Indicator。会有一些风险地区、 杀猪盘、Money Mule 等类型标签。<br>    <br>*   Entity：可以对特定的 Entity 单独制定风险规则。<br>    <br>*   Sanction：可以单独配置关心的制裁名单。 | *   12 个 Risk Indicator |
|  | Behavior | [警告] 只有 Large Transfer | *   Large Transfer<br>    <br>*   Transit<br>    <br>*   High-frequency |
| Blacklist |  | Blacklist & Whitelist | Blacklist & Whitelist |
| Re-screening |  | [警告] 加入 Monitor 列表即可进行持续监控，新资金流触发新风险，交互和逻辑都比较奇怪。 | 可以配置新交易 re-screen 还是定期回扫。 |
| 跨链追踪 |  | 已支持 ✅ | 不支持 [打叉] |
| Dashboard |  | 只有 Alert 统计数据 | 比较全面，可以作为一个工作台面板。 |
| 任务 |  | [警告] <br>*   有 Alert ，但是只有手动将地址/交易加入 Monitor List 后才会产生。<br>    <br>*   对于同一个监控对象，只要是不同的新交易带来的风险都会产生新的 Alert，太多，基本不可用。 | 在 Alert 中可以进行任务处理和协作 |
| 协作 |  | 有 Alert 的 Assign 和 Comment | ✅ 支持协作能力 |
| 监管相关 | Audit Logs | [警告] 有全局的 Log，但不是很全面，使用也比较麻烦 | ✅ 比较好用 |
|  | Report | [警告] 有 SAR Report，但类似我们的 Address Report 和 Transaction Report。 | Report 中还包含 Audit Logs 等，另外支持 STR report。 |
| Customer |  | [打叉] | ✅ |

总结：

*   Beosin 在风险检测方面的能力可能还是比较强。
    
*   在界面使用、用户体验来说我们还有比较有优势。
    
*   从合规官的使用场景考虑，从界面、交互、报告、audit log 来说我们还是比较有优势。
    

# 试用记录

#### 支持的链 （20）

BTC、ETH、BSC、TRON、Polygon、Avalanche、Optimism、Arbitrum、KAIA、LTC、Stacks、Aptom、Merlin、Solana、NEO、TON、XRP、ZKSync、Iotex、HSK

#### 导航栏

*   Dashboard 
    
*   KYT
    
*   Stablecoin Monitoring
    
    *   Token View
        
    *   Token Alert
        
*   Alert & Monitor
    
    *   Alert
        
    *   Monitor
        
*   Path Tracing
    
*   Rule Setting
    
    *   Risk Strategies
        
    *   TokenBasket
        
    *   Black/White List
        
    *   Basic Setting
        
*   API Manage
    
*   Log
    
*   Report
    
*   User Guide
    
*   Report to Beosin
    

## Dashboard

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/0beddbd7-2a18-4a0c-a1ca-a993fcda5cca.png)

展示 Alert 概览，分四个等级展示 Alert 数量、Alert 趋势（每天触发的 Alert 数量）和最近触发的 Alert 列表（点击 More 跳转 Alert 界面）。

## KYT

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/dca71873-0b44-4469-9953-c9f28fedcb5f.png)

其实是 KYT 和 KYA 的结合，用户可以在这里输入地址或交易进行风险筛查。

### KYA

选择链、输入地址后点击 Start Analysis 即可进行筛查，会即刻跳转到地址详情页面。

如果不选择链，在搜索地址后会如下展示这个地址活跃的链，需要选择一条链后跳转详情页面展示筛查结果。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/70408e03-60a2-4b83-9c17-8d20eae936d5.png)

#### 地址详情页面展示

| 模块 | 详细说明 |
| --- | --- |
| **地址基础信息** | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/bb61c09c-55d9-425d-b0a2-9954d777ba44.png)<br>*   Add to Monitor：点击地址旁的 Monitor 按钮可以将地址添加到 Monitor 列表。（Monitor 列表中的地址有新的资金流动带来的 risk exposure 时会产生 Alert）<br>    <br>*   Tags、Risk Label、Risk List。其中 Risk List 分为 Blacklist 和 White list。<br>    <br>*   Assessment Type。地址的资产列表，可以选择“All Tokens”或特定 token，查看对应的风险评估结果。（评估仅基于所选 token  的资金流动路径。）<br>    <br>*   Inflow、Outflow、Balance。 |
| **风险评估** | 1.  Risk Assessment。包括：<br>    <br>*   Risk Assessment：显示风险等级和检测到的风险指标数量。<br>    <br>*   Inflow：检测到的风险指标、金额、距离、比例、风险等级。<br>    <br>*   Outflow：同流入。<br>    <br>*   \[Assessment History\] 点击后以抽屉的形式展示此地址的所有评估历史、评估资产、风险等级、操作人。<br>    <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/99db0bab-5a39-4bc2-b988-020378e60db5.png)<br>*   \[Generate Report\] 点击后会生成这个地址的 Report。<br>    <br>[请至钉钉文档查看附件《SAR-0x72BEFCa6f095099C3387cbCA32Bf4637c9F952C9.pdf》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc01qwrkj5d5sb6wmwm)<br>1.  Risk Map<br>    <br>以资金流图的形式展示评估地址与风险地址之间的路径。<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/c76d1509-7594-44a4-906f-e4ad0a5e212a.png)<br>*   和所有风险类型的交互路径都汇总展示在一张图上，可以在图的右上角点击具体风险类型可以切换高亮展示对应的风险路径，如下图：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/6c4652ca-9250-4d1b-a19e-1240e73d5d6f.png)<br>    <br>追踪算法和我们有些区别：从目标地址出发已经追踪到了 Phishing 地址却没有停止，继续追踪又遇到了 sanction 地址。 |
| **Funding Statistics** | 以桑基图的形式展示一个地址全部资金的 Exposure，分为 direct 和 indirect exposure 分别统计。（有点没看懂是怎么计算的）<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/f322d528-0b0f-48cd-adb9-2ccbe7b73ac2.png)<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/ce202e36-d888-429a-80dd-a348f73d4222.png) |

### KYT

输入交易 hash 并点击 Start Analysis 后，需要选择方向 Deposit 或 Withdrawal 才能开始风险评估。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/cc55b79a-68e7-4767-b621-7dc8b779ac1a.png)

评估逻辑：选择方向开始评估后，会对交易中每一笔 transfer 的入金进行追踪和风险评估。

#### 交易详情页面展示

| 模块 | 详细说明 |
| --- | --- |
| **交易基础信息** | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/6f612cab-7e8a-433b-a33a-ebfb602397b1.png)<br>*   同样可以加入 Monitor，后续检测到新的资金流动引入的风险时会产生 Alert。<br>    <br>*   交易后用 Deposit 的标签标明了本次分析的方向。<br>    <br>*   Assessment Type 列出了交易中的所有 Token，可以单独选择某个 token 进行风险评估。<br>    <br>*   From 和 To 部分其实也是列出了交易中每笔 transfer 的 from 、 to 地址及对应的资产变化情况。 |
| **Risk Assessment** | 1.  Risk Assessment<br>    <br>    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1c2db7e9-f52e-4cf9-a3ff-2bb011799677.png)<br>    <br>    内容和 Address 的类似，区别在于只展示所选的那个方向的风险评估数据。<br>    <br>    Report 示例：<br>    <br>    [请至钉钉文档查看附件《SAR-0x8df5c2ef0e727f0f7dbbcee6c0e7e7eb9ff7c3749c15d59b60fc6faf402bf8b2.pdf》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc022z0skqijjbvjq48)<br>    <br>2.  Risk Map<br>    <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/4cbcc27f-d29a-475e-a8cb-9dea743d63d4.png) |
| **Funding Statistics** | 此处将交易中的参与地址/资金记为 Direct Exposure。<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/e8e50714-dfca-4a03-914a-5f9e36f4ed32.png)<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1373468f-818a-42bd-8bb6-e800f3df54ad.png) |

## Stablecoin Monitoring

应该是为稳定币发行商提供的服务，这里用 Dashboard 展示稳定币的数据概览，也可以自行设置一些 Alert。（目前好像仅支持 USDT）

### Token View

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/847434ca-0cdb-466f-9c2b-da836245ea9e.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/33715f2c-7197-43ca-a4d3-b643a7ea12da.png)

点击 Category 后可以查看具体的 Top 10 Holders，如下图：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/529e4e1c-1007-47ae-82e3-0ab31ec3da31.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/2846ca68-ca5e-4842-a9d5-d0d3f32ed190.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/5aaf723d-8b9b-457d-9078-05f14c00ccad.png)

### Token Alert

该模块提供 Alert 配置功能，并可浏览所有产生的 Alert 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/c3eae760-7cd6-4c3f-8707-14113e19e55b.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/8f3e66e0-5244-4480-8677-bc8ac2e6391b.png)

## Alert & Monitor

用户可以将交易/地址加入 Monitor 列表，在加入时刻之后因为资金流动产生的新风险 exposure 会产生 Alert。

### Alert

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/f9f94349-35d2-4829-86b7-d5772e5ebea3.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1654635b-9cf2-4793-8070-dbe5d1daf793.png)

**Notification**

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/621921d1-718e-48a8-89e9-82940b14edce.png)

**Process**

 ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/3d5113d7-9cac-4581-b1fc-809b65972973.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/dde392a9-6a4b-4366-b718-862d08bbd9ca.png)

### Monitor

两个方式将交易/地址加入监控列表：

1.  在 KYT 的地址/交易详情页面
    
2.  在 Monitor 处通过上传表格文件。
    

[请至钉钉文档查看附件《monitor\_template\_tx.xlsx》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc044k8vkci036w3buh)

[请至钉钉文档查看附件《monitor\_template\_address.xlsx》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc044q4yrp2wi0rpob)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/f5008fde-1dfe-490b-a05c-d16f0ce122fb.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/0f1d7a2a-02fa-4ac6-bc48-20e00bc21f10.png)

可以 Disable 或 Edit Monitor：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/e84463a3-e73a-4690-ac54-0a70c4b4dbdf.png) 

点击 Alerts 后跳转 Alert list 界面筛选出当前监控对象的 Alert

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/9f654881-57f2-4e01-b6d9-ada4a6e81b47.png)

## Path Tracing

资金追踪及可视化工具。同样是在选择链、输入地址/交易后点击 Start Analysis 可以开始分析。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/6e815263-1abe-4f2e-ba30-95a187f1e9e8.png)

#### 追踪地址

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/2b2719f5-ca83-46b7-b482-1e2301cd5200.png)

有全局的 Analyze Settings：Token 和 Time

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1331836a-7064-4a62-a428-7baba7cbbf44.png)

在对每个地址进行追踪时，可以直接点击地址节点左右的 '+' 进行追踪，也可以设置 Analyze Setting 后进行追踪，每次设置的改变都是全局有效的。

跨链交易的展示：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/5de558c4-d6ac-4f98-b590-945487d23dae.png)

#### 追踪交易

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/f8326328-d281-4fb9-ab67-3ec2ea75c1da.png)

除了点击地址节点左右的 '+' 符号进行追踪外，还可以设置 Analyze Settings：

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/a6f032e0-4132-4af5-94d5-54d303f823b0.png)

## Rule Setting

### Risk Strategies

风险规则配置模块。风险规则的配置逻辑和 Chainalysis 比较相似，即对每一个风险类型/实体单独配置风险触发条件。

Severity 分为 Severe、HIgh、Medium、Low 四个等级，每个等级可以分别配置 Exposure、Direction、USD、percent 条件。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/6ff3224e-d2a0-425b-b69d-4edee2c8f300.png)

风险配置分为以下三种类型：

*   Malicious Risk：
    
    *   给定的 29 种风险类型，包括： Pig Butchering Scam、Honeypot Scam、Investment Fraud、Phishing、Online Piracy、Gambling、Scam、Stolen Funds、Ransomware、Hacker、Rug Pull Scam、Protocol Privacy、Money Mule、Undergroud Bank、Mixing Service、Fraud Shop、Darknet Market、Drug Dealing、Illicit Actor Organization、Grey List FATF、Published Jugements、High Risk Exchange、Official Freeze、High Risk Jurisdiction-FATF、Child Abuse Material、Special Measure、Terrorist Financing、Sanctions、Customized Blacklist
        
*   Entity Risk：
    
    *   可以指定某个特定的 Entity 进行风险规则配置，如下对 FixedFloat 进行单独配置![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/d9219f38-9bb6-4df1-966b-e39256e00ca3.png)
        
*   Other：
    
    *   目前仅允许配置大额 transfer 规则 ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/daa1aded-77b3-49d8-98b1-ce4d3e44024f.png)
        

### TokenBasket

用户可以在这里配置 KYA / KYT 的 token，每条链有默认 enable 的 token （如 ETH 45 个、BSC 19 个），用户如果想要检测之外的风险，就需要将需要的 token 加入到 Token Basket 中。

支持的 token 数量应该比我们多一点，但是还是有限制的。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/44b51cd0-8fa4-43fe-a12d-16ab0b61f91f.png)

### Black/White List

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1b56a926-69ad-4a97-8c25-8208add7b3df.png)

管理黑名单和白名单地址的模块。

#### Blacklist

黑名单地址扫描界面：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/e8219787-13f6-4d99-b265-4485f5c5e5e5.png)

API 查询返回结果：

```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "score": 30.0,
        "riskLevel": "High",
        "incomingScore": null,
        "incomingLevel": null,
        "incomingDetail": [],
        "outgoingScore": null,
        "outgoingLevel": null,
        "outgoingDetail": [],
        "riskTagScore": 30.0,
        "riskTagLevel": "High",
        "riskTagDetails": [
            "Customized Blacklist"
        ]
    }
}
```

#### Whitelist

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/8cee40b6-eb1f-4d27-abe6-a9763007bf3b.png)

白名单地址扫描界面：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/544b96bf-49d0-4021-9145-bb11aa94d15a.png)

### Basic Setting

#### 跨链传递风险

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/54c123eb-953f-46d1-8b1c-f40b6fbaa107.png)

#### 制裁风险

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/fc4b9ba4-d562-4976-8d25-df3db1871e0b.png)

列出所有支持的制裁名单，由用户配置选择关心的制裁名单。

每个制裁名单点开可以看到制裁 list （有些没有 crypto 地址，只是对地区和实体的制裁也列出来了，这些信息我们目前没有收集）

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/1e88e21b-24ca-46df-8ede-3691aaf0daf4.png)

#### Risk Level

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/94bef449-19d4-45da-9a5f-4259ecb1622e.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/51401aa2-5fd3-4c6b-bb6d-d07c7d49e71a.png)

## API Manage

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/744a4340-8314-42b5-bd1c-f17d33683263.png)

#### API 查询结果示例

```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "score": 30.0,
        "riskLevel": "High",
        "incomingScore": null,
        "incomingLevel": null,
        "incomingDetail": [],
        "outgoingScore": null,
        "outgoingLevel": null,
        "outgoingDetail": [],
        "riskTagScore": 30.0,
        "riskTagLevel": "High",
        "riskTagDetails": [
            "Phishing"
        ]
    }
}
```
```json
{
    "code": 200,
    "msg": "success",
    "data": {
        "score": 30.0,
        "riskLevel": "High",
        "risks": [
            {
                "riskStrategy": "Sanctions",
                "riskDetails": [
                    {
                        "riskName": "Sanctions",
                        "rate": 0,
                        "amount": 1.3773954820655604E-5
                    }
                ]
            },
            {
                "riskStrategy": "Official Freeze",
                "riskDetails": [
                    {
                        "riskName": "Official Freeze",
                        "rate": 1.32E-4,
                        "amount": 0.02728903126044317
                    }
                ]
            },
            {
                "riskStrategy": "Scam",
                "riskDetails": [
                    {
                        "riskName": "Scam",
                        "rate": 1.4E-5,
                        "amount": 0.00293204549787948
                    }
                ]
            },
            {
                "riskStrategy": "Grey List - FATF",
                "riskDetails": [
                    {
                        "riskName": "Grey List - FATF",
                        "rate": 6.0E-6,
                        "amount": 0.001324424068373151
                    }
                ]
            },
            {
                "riskStrategy": "Phishing",
                "riskDetails": [
                    {
                        "riskName": "Phishing",
                        "rate": 2.0E-6,
                        "amount": 3.1431509022478507E-4
                    }
                ]
            },
            {
                "riskStrategy": "Gambling",
                "riskDetails": [
                    {
                        "riskName": "Gambling",
                        "rate": 2.9E-4,
                        "amount": 0.060013361653081895
                    }
                ]
            }
        ]
    }
}
```

## Log

### Web Log

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/54a643c8-5280-499f-91a1-f80616f14579.png)

通过 Module 、Action 过滤，也可以实现不同模块 Audit Logs 查看和下载的能力，但是仍然不是很方便

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/d6bd4e2b-871b-4ded-bc26-d19270b503f5.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/17f385ae-945d-4667-b786-e387ee165827.png)

### API Log

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/e5db1c97-a84c-4f66-aa32-16c28fceb4b3.png)

## Report

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/769e7525-7aaf-4f56-8dcb-f031cd2079c1.png)

所有导出 Report 都会在这里产生记录，用户可以重新下载。

## User Guide

[请至钉钉文档查看附件《KYT User Guide.pdf》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc08a4sgtei27trz9yt)

## Report to Beosin

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/f9677c1e-dc97-4ad6-8e4d-1938ee3f1760.png)![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/2fe320d2-b95a-46c6-9adc-cf2321ab42f9.png)

[请至钉钉文档查看附件《template.xlsx》](https://alidocs.dingtalk.com/i/nodes/vy20BglGWO4AwmRpTlx4AEpeVA7depqY?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mc08bndqjjwlfjiyjqs)

# 小功能点记录

1.  标签信息的展示更加详细
    
    如下：有地区信息记录？但是据我的查询 KyberSwap 位于 Singapore
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/430a3b74-b5b7-49ae-a5ca-58ddef0906fe.png)
    
    [https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html](https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html)
    
    还有例如 Blacklisted USDT 会展示具体拉黑的交易。
    
2.  支持跨链追踪
    
    ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/50acec81-42be-4e07-8eca-bf955da0277f.png)
    
3.  新 feature 提示
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/QvjnA3jrXKL14OXo/img/63d86115-e728-4b88-afb5-5d54b61ede62.png)

# Archived

## 优势表格

| Feature | Beosin | Phalcon |
| --- | --- | --- |
| Unique Intelligence | / | Attacks, Phishing  <br>(self developed detecting engine) |
| API Workflow | / | Comprehensive API workflow with detailed, actionable risk data. (e.g., alert information, risk engine details) |
| Behavior Risk Detect | Only Large Transfer | Advanced behavior risk detection for money laundering, even with missing labels. |
| Task Assignment & Collaboration | / | Yes! Tasks can be routed and collaborated based on alerts. |
| Screening Result Management | / | *   All screened addresses/transactions (via UI or API) accessible in detailed lists.<br>    <br>*   All rules triggered via UI or API generate alerts. |
| Re-screening | Manual upload to monitoring list required. | Automatic re-screening for all screened addresses (via UI or API), with customizable cycles (periodic or transaction-triggered). |
| Export Audit Logs and STR Reports | Only address and transaction report. | Yes! We record audit logs for every module. |
| Customer Management | / | Dedicated customer module to aggregate, view, and manage customer data and associated addresses/transactions |
| Dashboard | Limited dashboard functionality. | Multi-dimensional dashboard with insights from alerts, tasks, scanned addresses, and transactions. |
| Notification Channel | Email only | Supports 7 notification channels for real-time alert delivery via common platforms. |