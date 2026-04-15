# Pricing Model v2

[《Pricing Model》](https://alidocs.dingtalk.com/i/nodes/93NwLYZXWyqAB0poHYj1wOXZWkyEqBQm)

[《产品定价调研-Token计费模式》](https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBBbarMdi5vKrKv9V1DK0g6l?utm_scene=person_space)

[《产品定价调研讨论\[Compliance\]》](https://alidocs.dingtalk.com/i/nodes/AR4GpnMqJzeABb2oFgZ4BlDZVKe0xjE3?dontjump=true)

## 定价

[请至钉钉文档查看附件《Pricing V2》](https://alidocs.dingtalk.com/i/nodes/dpYLaezmVNKEra7XcgBRrz7pJrMqPxX6?doc_type=wiki_doc&iframeQuery=anchorId%3DX02mhkkwwiydv75xilt8x8)

_**说明：**_

*   Team 模式下，如果增加1个席位，所有用量quota\*2，并增加协作模式，增加API集成，价格\*2（具体见表格）
    
*   仅Tier 3、4可升级为Team模式
    
*   仅Tier4升级后，可以支持API集成和Usage Training
    

## Q1：如何在客户未付费/未升级前，就体验到全部厉害的功能？

*   增加1条 sample data，可交互
    
*   🪝 限时体验（与P1 免费用户unlock引导同步讨论[《页面行为数据 for UX优化\[Compliance\]》](https://alidocs.dingtalk.com/i/nodes/6LeBq413JA10ZvgdTYMKPMNOJDOnGvpb?cid=70657646405&utm_source=im&utm_scene=person_space&iframeQuery=utm_medium%3Dim_card%26utm_source%3Dim&utm_medium=im_card&corpId=ding11de5443ac093187bc961a6cb783455b)）：
    
    *   邮件通知，提供7天免费体验，7天后提示该功能需要付费
        
    *   Audit Report/STR 等类似，如先“限时”免费尝试1次，第二次用户再点击的时候需要付费
        
    *   Risk Engine，对所有用户都可以查看detail，并可以新建进入模板，但是对于无权限用户，在填写完后提示要付费才能保存，或者只能保存1个，有效期7天，7天后Disable
        
    *   注意：这类限时体验功能，应有很明显的用户引导！
        

## Q2：每次扫描的单价差异不明显

*   强调随着tier的提升，功能变多，但单价降低。如：Unlock More Power, Pay Less Per Scan.
    
*   数字展示，依然引导用户年付费，但是展示每月的付费金额，与月付费金额做对比，下方展示per check的单价对比
    

## Q3：支付流程，绑定信用卡再支付对中国客户不友好

*   Stripe里有支付宝、微信支付的支持，可以在付款收银台上增加这两种扫码支付的入口
    

## 推荐

referral 用户可以生成专属邀请码，邀请新用户注册

*   每成功邀请一个新用户注册，邀请用户和被邀请用户都可以增加3次免费扫描额度（当月有效）
    
*   若被邀请用户完成付费转化，则根据其付费金额20%，充值进入邀请用户的账户，显示为账户余额，可以在付费充值时直接抵扣（3个月内有效）
    

在初期，仅定向邀请的用户（包括KOL）和付费客户可以生成邀请码（可以为其定制专属邀请码，显示尊贵性），邀请码生成配套海报（希望诙谐、标题党、吸引人，可以有多组海报供选择）

后期，产品逐渐丰满起来后，所有用户均可生成邀请码，自助流程（生成邀请码-生成海报-获知用户注册/充值情况-获知福利情况等）

## 钩子

~~7 days free trial~~

~~限时升级体验~~

~~限量升级体验~~