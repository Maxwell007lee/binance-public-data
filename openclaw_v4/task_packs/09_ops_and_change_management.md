# 任务包 09：运营控制、纸交易、变更管理包

## 任务定位
`OP-01/02/03` 定义为运营控制链，要求 8 周纸交易监督、P&L 五维归因、CR 门控、四维偏差矩阵、五维归因误差 `<0.1%`。

## 输入
- simulated fills
- real fills
- strategy metadata
- change requests

## 输出
- paper trading supervisor
- attribution engine
- deviation matrix
- CR workflow service
- rollback template

## 硬约束
- 稳定性优先于收益性
- 未通过纸交易不得实盘推进
- 变更必须走 CR 门控

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的运营控制系统工程师。

目标：
实现 OP-01 / OP-02 / OP-03，使系统从“会交易”升级为“可监督、可归因、可控变更”。

请实现：
1. 8-week paper trading supervisor
2. deviation matrix engine
3. PnL five-dimension attribution engine
4. change request workflow
5. rollback package template

要求：
- stability first, profit second
- paper trading is mandatory before live promotion
- all production changes must bind to CR workflow
- attribution errors must be measurable and reportable

输出：
- ops_supervisor/
- attribution/
- change_management/
- reports/
- tests/
```
