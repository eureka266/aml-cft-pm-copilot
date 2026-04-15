# Engine 规则更新

**更新原因**：

*   不久前我们对 **Transaction Exposure Value** 的计算方法进行了优化，导致计算结果和之前相比整体更小。
    
*   随着订阅功能上线，试用用户将仅能使用平台预设的 **Default Risk Engine**。为降低漏报风险，需要适度下调默认规则中的阈值。
    

对以下两个交易类型的 Risk Engine 进行修改，修改部分已标黄。

|  | 内容 |
| --- | --- |
| Name | Transaction Exposed to Illicit Entities |
| Description | Flags transactions where the address has direct or indirect exposure to illegal entities. |
| 模板 | Interaction Risk |
| Risk Level | **Critical** |
| Trigger Condition | *   Risk Indicator:<br>    <br>    *   Sanctioned, Attack, Scam, Ransomware, Child Abuse Material, Laundering, Mixing, Dark Market, Darkweb Business, Terrorist Financing<br>        <br>*   Direction<br>    <br>    *   deposit or withdrawal<br>        <br>*   Interaction Type<br>    <br>    *   direct or indirect<br>        <br>*   Exposure Value<br>    <br>    *   ~~\>= 10,000~~  修改为：>= 5,000 |

|  | 内容 |
| --- | --- |
| Name | Transaction Exposed to High-Risk Entities |
| Description | Identifies transactions with direct or indirect interactions with high-risk entities. |
| 模板 | Interaction Risk |
| Risk Level | **High** |
| Trigger Condition | *   Risk Indicator:<br>    <br>    *   Gambling, Blocked, No KYC Exchange、FATF High Risk Jurisdication<br>        <br>*   Direction:<br>    <br>    *   deposit or withdrawal<br>        <br>*   Interaction Risk<br>    <br>    *   direct or indirect<br>        <br>*   Exposure Value<br>    <br>    *   ~~\>= 10,000~~  修改为：>= 5,000<br>        <br>*   Exposure Percent<br>    <br>    *   ~~\>= 10%~~ 修改为：>= 50% |