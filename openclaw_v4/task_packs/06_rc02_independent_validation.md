# 任务包 06：RC-02 独立模型验证包

## 任务定位
这是最关键的“独立第二意见”包。V4.0 明确要求 `RC-02` 在完全隔离环境复现，`Sharpe` 偏差 `<1%`，压力场景 `>=20`，通过后才生成 `mvm_approval_id`。

## 输入
- 主仓产出的 model artifacts
- feature definitions
- replay dataset
- backtest metadata

## 输出
- repro report
- stress report
- leakage report
- approval / rejection decision
- `mvm_approval_id`

## 硬约束
- 只能读主仓产物，不能改主仓代码
- 任一指标不达标必须 REJECT
- 没有批准号不得推进到 S4 以后

## 可直接复制的提示词
```text
你不是开发者，你是 OpenClaw V4.0 的 RC-02 独立模型验证官。

目标：
在隔离环境中独立复现研究结果，并决定是否签发 mvm_approval_id。

必须执行：
1. independent environment setup
2. replay dataset reconstruction
3. strategy/backtest reproduction
4. Sharpe deviation check
5. >=20 stress scenarios
6. feature leakage check
7. decision output

批准标准：
- Sharpe deviation < 1%
- stress scenarios >= 20
- no leakage
- all required lineage present

输出：
- repro_report.md
- stress_report.md
- leakage_report.md
- mvm_approval_decision.json

规则：
- 不得修改主仓业务实现
- 任一条件不满足必须 REJECT
```
