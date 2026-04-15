# Risk Exposure 支持导出 CSV 

*   **入口**：地址/交易/transfer 详情页的 Risk Exposure 表格区域，新增一个“导出”按钮。
    

*   **交互**： Hover 后显示 Tips：Save as CSV。点击按钮后直接生成 CSV 文件并下载
    
*   **数据范围**： 导出当前表格中的所有数据。
    

![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/pLdn55XaaBPwjno8/img/038787f9-0b24-49ae-9f9e-7486a1f67057.png)

*   Lite Scan 模式不允许下载 csv（展示按钮禁用状态，hover 后显示通用 tips）
    

**文件命名格式：**

*   地址：`address_{chainId}_{地址前 6 位}_{timestamp}.csv`
    
*   交易：transaction\_{chainId}\_{tx hash 前 6 位}\_{timestamp}.csv
    

*   transfer： transfer\_{chainId}\_{tx hash 前 6 位}\_{transferId}\_{timestamp}.csv
    

| **CSV 标题 (英文)** | **说明** | **示例** |
| --- | --- | --- |
| **Chain** | 链名称 |  |
| **Address** | 风险地址 | 0x67d40ee1a85bf4a4bb7ffae16de985e8427b6b45 |
| **Label** | 地址的标签 | OFAC Blocked: 0x67d...b45 |
| **Risk Indicator** | 风险指标，如果有多个，用分号拼接 | Sanctioned;Blocked |
| **Risk Detail** | Risk indicator 对应的 detail，有多个的话用英文分号拼接，同一 Risk Indicator 下的多个 Risk Detail 用逗号拼接，顺序和 Risk Indicator 对应 | OFAC Sanctioned;Blocked by USDT,Blocked By USDC |
| **Hop** | 跳数 | 1 |
| **Direction** | 方向 |  |
| **Exposure Value** | 风险资金金额(USD) | 17195460.56 |
| **Exposure Percent** | 风险资金占比 | 0.1102 |