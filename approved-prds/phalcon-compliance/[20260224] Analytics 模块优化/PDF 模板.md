# PDF 模板

 ![image.png](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/r4mlQ5bbyMrKNlxo/img/514fe4a0-d9d2-46c7-8943-5cc4a67bc71e.png)                                                                              Generated at: 2024-03-28 12:22:00 (UTC)

---

# Analytics Report

Date Range: {{start\_date}} – {{end\_date}}   Previous Period: {{previous\_start\_date}} – {{previous\_end\_date}}

Target Type: {{target\_filter}}   Chain: {{chain\_filter}}

# AI Insights

### Summary

{{ai\_summary}} 

### Key Insights

*   {{highlight1}}
    
*   {{highlight2}}
    
*   {{highlight3}}
    

# Core Metrics

| Metric | Current | Previous | Change |
| --- | --- | --- | --- |
| High & Critical Risk Ratio | {{risk\_ratio\_current}} | {{risk\_ratio\_previous}} | {{risk\_ratio\_change}} |
| High & Critical Risk Targets | {{risk\_count\_current}} | {{risk\_count\_previous}} | {{risk\_count\_change}} |
| Total Targets Screened | {{total\_targets\_current}} | {{total\_targets\_previous}} | {{total\_targets\_change}} |
| Total Screening Count | {{screening\_current}} | {{screening\_previous}} | {{screening\_change}} |

# Risk Overview

## Risk Trend

\[图片\]

Distribution of screened targets by risk level over time.

## Risk Distribution

\[图片\]

| Risk Level | Current Count | Previous Count | Percentage | Change |
| --- | --- | --- | --- | --- |
| No Risk | {{no\_risk\_count}} |  | {{no\_risk\_pct}} |  |
| Low | {{low\_count}} |  | {{low\_pct}} |  |
| Medium | {{medium\_count}} |  | {{medium\_pct}} |  |
| High | {{high\_count}} |  | {{high\_pct}} |  |
| Critical | {{critical\_count}} |  | {{critical\_pct}} |  |

## Top Triggered Rules

\[图片\]

| Rule Name | Current | Previous | Change % |
| --- | --- | --- | --- |
| {{rule\_name}} | {{current}} | {{previous}} | {{change\_pct}} |

## Identity Exposure Distribution

\[图片\]

Distribution of risk indicators directly associated with screened targets.

## Risk Exposure Flow

\[图片\]

Shows how screened targets receive and send funds across different risk indicators.  Flow width represents the total exposure value (USD).

# Screening Overview

## Screened Transaction Volume (USD)

\[图片\]

Total USD value of screened transactions over time.

## Screening Source Breakdown

| Source | Current | Previous | Change % |
| --- | --- | --- | --- |
| API | {{api\_count}} |  |  |
| Manual | {{manual\_count}} |  |  |
| System | {{system\_count}} |  |  |

## Screening Count Trend

\[图片\]

Total number of screening actions over time.