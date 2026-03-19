# 任务包 10：TRE-01/TRE-02 + RC-03 审计追溯与清算包

## 任务定位
文档与思维导图已明确：`TRE-01` 为 CVA 三层模型，`TRE-02` 为四本账自动对账，`RC-03` 为 DecisionTracer 全链路追溯、6 级节点、10 条不变量、四层回放、零容忍 orphan fill。

## 输入
- fills
- positions
- fees
- transfers
- valuations
- decision traces

## 输出
- CVA engine
- reconciliation engine
- DecisionTracer API
- replay engine
- invariant runner
- orphan fill scanner

## 硬约束
- 每笔 Fill 必须能追到决策
- 对账异常必须落地
- 审计链不能被静默篡改

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的账务清算与审计追溯工程师。

目标：
实现 TRE-01 / TRE-02 / RC-03 的机构级闭环。

请实现：
1. 3-layer CVA engine
2. 4-book reconciliation engine
3. DecisionTracer API
4. replay engine
5. invariant runner
6. orphan fill scanner
7. audit hash verification

要求：
- every fill must map to a valid decision path
- reconciliation exceptions must create actionable outputs
- replay must be deterministic
- audit chain must be tamper-evident

输出：
- treasury/
- reconciliation/
- decision_tracer/
- replay/
- invariants/
- tests/
```
