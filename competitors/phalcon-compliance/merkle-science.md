# Merkle Science

### Dashboard 

进入系统后首先看到  Dashboard 页面

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/7ab159e9-f049-4d9c-88c5-f0fb1afd72e6.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/90165e2b-f2ff-4a75-8a55-c9c98d5060e7.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/926f4cb8-ab5d-464d-ad9a-6eecd18699db.png)

dashboard 中展示以下维度的统计信息：

*   Alerts ：
    
    *   创建数量
        
    *   解决数量
        
    *   open 数量
        
*   Open Alerts 中：
    
    *   分别和地址、交易、customer 关联的数量
        
*   Cases：
    
    *   创建数量
        
    *   解决数量
        
    *   open 数量
        
*   Rule 被触发的数量分布
    
*   Alerts 的 severity 分布图
    
*   等
    

### 导航栏：

*   Dashboard
    
*   Alerts
    
*   Addresses
    
*   Transactions
    
*   Customers
    
*   Cases
    

# Workspace Settings 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/78aca911-84c0-401b-91fe-bd061805567e.png)

点击 Workspace 旁的 Settings 进入相关设置页面。

| 界面 |  |
| --- | --- |
| **API Keys** | 生成和管理 API Key<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/196e95ef-025f-4bdb-856c-a85e923ca9e8.png) |
| **Integrations** | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/b990989f-0815-4394-8a7d-99fb4978a752.png)<br>Slack 和 Webhook 有点类似 Phalcon 的 Notification Channel，但又有差别。例如 Slack 还会推送：weekly report、usage、billing 等信息。<br> Fireblocks 有很大的不同，需要后续进一步了解。<br>“Automatically sync transactions from your Fireblocks account.”![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/41441163-c6ee-4233-866f-89690dd31d55.png) |
| **Workspace Members** | ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/8a979d1d-a166-470e-9313-d6fc17fc8473.png)<br>Workspace 成员管理<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/2412ef79-a5f0-4007-8d61-5a2cd2fe4b1b.png)<br>这里的 Role 主要用于工作流管理/协作。 |
| **Product Configurations** | 1.  **Monitoring Config**<br>    <br>*   Auto Resolve Alerts<br>    <br>可以设置特定 Severity 的 Alert 自动为 Resolved 状态<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/a1e5a4f5-0a10-4118-8e99-01e3a7b892c0.png)<br>*   **Continuous Monitoring**<br>    <br>即 Re-screening。当开启后，之前 screen 过的地址有新的交易时，就会实时更新 risk level。<br>Enable 后还可以指定 continuous monitoring 持续多长时间：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/29004e43-1668-4871-a112-e5289a77b58a.png)<br>Entity Based Moitoring: 自己添加 tag，携带指定 tag 的地址会被 re-screening<br>*   **Smart Contract Watchlist**<br>    <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/ace4ddc0-1855-4153-bdce-bc8a5aa4e0c8.png)<br>没有这个功能的权限，看起来像是实时交易 monitor 和 screen。<br>*   **Custom Lists**<br>    <br>可以用于给特定的地址固定的风险值。 （Blacklist 这个功能和 Tokenlon 之前说的 Block 用户地址有点类似，可以学习。）<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/23376134-d690-4b90-9f1c-6d9c5d8edfff.png)<br>*   **Case Preferences**<br>    <br>协作相关的设置。merkle science 提供了很全面的协作功能，case 的详细说明在后面的 case 界面。<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/20de44ed-2cf6-43f6-b21b-4f27c46cb2f1.png)<br>这里可以配置：<br>*   什么 severity 的 alert 自动创建 case<br>    <br>*   选择哪些成员会是处理 case 的成员<br>    <br>*   case assignment 规则<br>    <br>*    case resolve 的 approval 规则 |
| **Risk Management** | 重点！风险规则配置：<br>用户可以配置多个风险策略（Risk Policy），每个风险策略下可以包含多条风险规则（Risk Rule）。每条风险规则由多个条件（Condition）组成，并且这些条件之间是与（AND）关系。<br>Policy Type & Category<br>*   Transaction  <br>    <br>    *   Source of Funds<br>        <br>*   Address<br>    <br>    *   Source of Funds<br>        <br>    *   Behavior<br>        <br>    *   Source of Funds Advanced<br>        <br>*   Customer<br>    <br>    *   Source of Funds<br>        <br>    *   Behavior<br>        <br>    *   Source of Funds Advanced<br>        <br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/4d986911-7354-4900-9c7a-5e2c629b1965.png)<br>每个 Policy 下面还会展示一些统计维度信息：<br>*   扫描的地址数量<br>    <br>*   Flag 的地址数量<br>    <br>*   Hit Rate 等<br>    <br>同样提供 Audit Trail<br>按照 FATF Rules 提供了一些默认的 Risk Policy<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/288bf9e7-93ef-4768-861e-40822f9f478c.png)<br>Custom Tags 有点类似地址分组的概念：添加了 Custom Tag 的地址将仅使用对应的 Custom Tag 所关联的风险策略（Risk Policy）进行筛选（screen）。<br>![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/6ac4aac6-9445-4ac6-9d1b-82871744f0d5.png) |

# Screen

三种方式触发：

1.  upload csv  ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/019d952e-eba9-4e32-988c-1394cb75b4f2.png) 
    
2.  API
    
3.  在页面上方的搜索栏中搜索地址/交易，随后直接进行 screen ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/5aba99e2-5ece-4efa-a9b7-5d88145de05d.png)
    

## Address 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/64f771d7-7114-4e6a-89ab-ba04bbbea904.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/527b8c54-4292-40b4-b2ec-0428e0b44d03.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/99b0fad2-0f8b-4897-b1d8-ccab852f6760.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/7c043c51-8703-47ca-967c-8ff7fdf60020.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/f1f27da7-2158-465b-916f-dd7a6c1829bb.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/dcea81ca-c25c-4763-aa34-bb2a359c3635.png)

#### Export Report

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/936a97c7-2d53-464c-b444-5ca8d11de09c.png)

Report 示例：

[请至钉钉文档查看附件《Merkle Science - Address - 4739427.pdf》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdi40mo9BNV1DK0g6l?doc_type=wiki_doc&iframeQuery=anchorId%3DX02m848q8v1htj5eh0efn8)

#### Risk Level

一个感觉有点奇怪的点：如果一个地址的 Alert 被 Resolve 了（尽管有 Critical 的 Alert），地址的 Risk Level 会变成 No Risk。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/3dc1cd9d-8e8c-4886-b343-d8cd42561503.png)

## Transaction

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/6564e700-2ca6-40aa-a712-232c0a578901.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/a1cfaf92-4b80-4a54-b8b9-b1810fa790f7.png)

#### Export Report

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/18e64295-045d-4d69-9292-847e070ebce2.png)

[请至钉钉文档查看附件《Merkle Science - Transaction - 4177723.pdf》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdi40mo9BNV1DK0g6l?doc_type=wiki_doc&iframeQuery=anchorId%3DX02m848sfmutwga2gr92np)

## Customer

Customer 只做信息汇总展示，可以关联多个地址和交易。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/c3cfec49-55bf-4a56-81af-e43f7f3e7818.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/6ad74b88-a56a-43a0-a1cf-1db19528d04b.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/32232c37-a0ad-467d-90e2-e02ee9a07963.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/1a6ca77b-5bc3-4d0d-8b08-cc344784535a.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/480c7fd4-ce24-4944-8b31-adb1ae9906d0.png)

#### Export Report

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/6e53a39a-a4f6-4aa1-886d-98f0160dcd4d.png)

[请至钉钉文档查看附件《Merkle Science - Customer - Suspicious Customer.pdf》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdi40mo9BNV1DK0g6l?doc_type=wiki_doc&iframeQuery=anchorId%3DX02m8493kzuh71ytsnacvo)

## Alert

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/74cad228-d7de-4f95-8ce1-f6a0e0548c47.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/e1e36f07-547a-4c52-8d30-735ca1a695ec.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/a90a4483-2266-456b-b885-84ee6f0dc014.png)

#### Assign

*   一次只能 Assign 给一个用户
    
*   Assign 的时候可以填写 comment
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/a5b6de69-a545-45af-b44b-9647f24134fb.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/b3c73d7a-eaf2-411f-b38f-6dcdea944bce.png)

1.  Assign 后 Update 时间会改变。
    
2.  Assign 会记录在 Comments 中，comment 内容也会在这里。（但是没有特别标识标明和 Assign 动作相关，那感觉加这个 comment 也没啥必要）
    

#### Alert History 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/dd716182-35a7-4fad-b1a4-1213c8a7d2a7.png)

已经 Resolve 的 Alert 可以重新 Open，进行了一次这样的操作后， Alert History 下面就会显示这样的一条记录。

即 Alert 从 Open -> Resovle 为一次 History。

#### Alert Status

一个地址在配置好的风险引擎下，只会有一个最新的 Alert。

一个感觉到奇怪的点：已经 Resolve 的 Alert，还会因为 Re-screening 重新触发。

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/18a36238-2069-4c5c-81c5-601766ac4bea.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/dca6e169-398b-4df6-84f6-50414f2b9299.png)

#### Previous Trigger 

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/9f1fb78a-dd62-4d44-98b9-9ec5fea7ca6d.png)

只有 Alert Detail 改变时，会在 Previous Triggers 中体现。

## Case

Case 有 Status 和 Assign to

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/797d8133-f4e4-4ece-81d5-de5014618a5e.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/11d7202b-e192-412f-8346-513138c049b7.png)

# Risk Policy

## Address - Source of Funds

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/42c61d42-c339-49f3-9135-29471ad3bfbf.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/9c3c072f-4d46-4ef3-8bc7-a4e162eaa37e.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/7ca3198b-5204-41b6-8989-e506095c158a.png)

## Address - Behavior

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/4a1484d7-f905-416e-be0a-26e07d35aeff.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/716beb17-376d-4d99-bef0-d654a9c66682.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/a5a787d2-4105-492c-827e-39c4db88ff9b.png)

## Address - Source of Funds Advanced

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/8670f8f9-a62c-477e-9e08-f5fd6dba1382.png)

## Transaction - Source of Funds

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/790775e4-4242-4e2e-ae4e-621716b49f76.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/8510a2ef-0a26-4a09-9306-b0fcf7d26548.png)

## Cusomer - Source of Funds

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/3870f1ee-3749-4013-bcf9-90c8d52b6aea.png)

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/8K4ny5VQ27ApnLbj/img/314fdac4-c27d-49bb-a5b6-82302cded95f.png)