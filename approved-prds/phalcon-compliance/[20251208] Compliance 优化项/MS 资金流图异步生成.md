# MS 资金流图异步生成

# 背景与目标

当前 Compliance 在以下位置会为用户自动预生成 MS  的资金流图，以便用户进一步跳转到 MS 做深入分析：

*   Interaction Risk 类型的 Alert Details，对每一个 Risk Indicator 自动生成一张对应的资金流图：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/pLdn55XaaBPwjno8/img/853c7fa7-6f36-408f-ac7b-accf3b83c6a7.png)
    
*   地址/交易详情页中的 Risk Overview，自动生成对应的汇总资金流图：![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/pLdn55XaaBPwjno8/img/c04c2243-5df7-47dd-a0d1-f1f958ad3f7c.png)
    

但由于部分图数据量大、生成耗时长（平均 5.3s，P90 = 9.7s，最长可达 50s），且用户点击跳转的频率较低，自动生成导致性能压力与资源浪费。因此需调整为 **按需异步生成** 模式。

# 新方案

所有原本展示资金流图的入口统一保留按钮： **\[Investigate on MetaSleuth\]** 。不再预生成图。用户点击后才触发图生成，完成后自动跳转至 MS。

### 交互

*   Hover 到按钮上展示 Tips：Generate and view the fund flow graph on MetaSleuth.
    
*   用户点击按钮：
    
    *   按钮进入不可用状态（disabled）
        
    *   按钮文案变为：\[Generating fund flow graph…\]
        
    *   弹出提示：Generating MetaSleuth fund flow graph, this may take a few seconds.
        
*   生成成功：
    
    *   按钮恢复可点击。
        
    *   按钮文案更新为 \[View on MetaSleuth\]，Hover 展示 tips：Open the generated fund flow graph on MetaSleuth.
        
    *   弹出提示（仅当用户未离开当前页面时。）：
        
        *   MetaSleuth fund flow ready, click to view. \[View on MetaSleuth\] （打开新页面）
            
*   可能因超时、网络异常或后端错误。
    
    *   按钮恢复为可点击
        
    *   弹出提示：Failed to generate the fund flow graph. Please try again later.
        

#### [问号] 数据更新相关

由于存在 Re-screen 与 Alert 数据更新逻辑：

*   Alert Details：当某个 Alert 的数据更新（一般是资金流图数据更细），其对应的 MS fund-flow 图即失效，前端需显示“重新生成”按钮。
    
*   Risk Overview：只要任意 Interaction Risk 类型的 Alert 数据发生更新，汇总 MS 图即失效，需要重新生成。