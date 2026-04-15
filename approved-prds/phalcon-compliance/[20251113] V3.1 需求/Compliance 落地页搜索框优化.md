# Compliance 落地页搜索框优化

###  搜索框基础交互与Placeholder

*   Placeholder： 突出“试用”的概念，吸引用户操作：
    
    *    `Search by address or transaction hash for a FREE Trial screen.` 
        
*   支持输入地址/交易
    
*   基础校验：若输入的地址/交易不正确，不触发搜索
    

### 搜索结果与展示逻辑

和[《Home首页》](https://alidocs.dingtalk.com/i/nodes/20eMKjyp81BDLQEdi79RrgoPWxAZB1Gv?utm_scene=person_space&iframeQuery=anchorId%3Duu_mi32ay1k5pqvbsh7zb2)中的 快速扫描及 Example 保持相同逻辑。

即：

*   当用户**点击输入框**但**尚未输入**地址或交易时，下拉列表应展示示例数据。
    
    *   用户点击示例数据直接进入平台开始扫描
        
*   搜索地址
    
    *   列出地址所有链结果
        
    *   若结果中有支持试用的链（除 tron、eth 之外的链），同样展示，但标注不可试用
        
    *   点击地址结果直接进入平台开始扫描
        
*   搜索交易
    
    *   列出交易所有 transfer
        
        *   若为不支持试用的链，同样展示，但标注
            
    *   点击单条 transfer 进入平台开始扫描
        
    
    —> 进入平台后：
    
    *   验证用户身份：
        
        *   visitor / 点数用完：跳转 lite scan 结果页
            
        *   其他：跳转结果页