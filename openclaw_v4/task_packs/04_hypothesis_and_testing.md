# 任务包 04：假说生成与三阶段多重检验包

## 任务定位
V4.0 已经把 `R-01` 的统计制度明确成三阶段：探索：BH-FDR；准入：Bonferroni；生产：Bayes 后验。

## 输入
- 假说定义
- 样本集
- IC 口径
- N 次检验元数据

## 输出
- hypothesis registry
- BH-FDR engine
- Bonferroni engine
- Bayesian posterior evaluator
- 去重逻辑
- 审批前报告

## 硬约束
- `探索阶段 = BH-FDR`
- `准入阶段 = Bonferroni`
- `生产阶段 = P(IC>0.05|data) > 0.9`

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的研究方法学工程师。

目标：
为 R-01 实现可审计的三阶段多重检验机制。

请实现：
1. hypothesis registry
2. batch hypothesis ingestion
3. BH-FDR evaluator
4. Bonferroni evaluator
5. Bayesian posterior evaluator
6. duplicate hypothesis detector
7. evidence report generator

规则：
- exploration stage uses BH-FDR
- admission stage uses Bonferroni
- production stage requires posterior probability P(IC>0.05|data) > 0.9
- 所有结论必须带 hypothesis_id 和 evidence bundle

输出：
- research_registry/
- stats/
- reports/
- tests/
- docs/
```
