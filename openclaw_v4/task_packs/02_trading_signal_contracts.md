# 任务包 02：TradingSignal 与核心契约包

## 任务定位
把 `S-01` 的受控信号接口正式落地。V4.0 明确要求 `TradingSignal` 必须带 5 个强制血缘字段，并且 `confidence < 0.6` 需要被拦截，`signal_version` 要绑定 SDR 审批编号。

## 输入
- `02_signal_contract.avsc`
- `03_risk_decision_contract.avsc`
- `04_feature_spec_contract.json`

## 输出
- Avro / JSON Schema
- Pydantic models
- Schema registry 接口
- Contract tests

## 硬约束
以下字段必须存在：
- `model_run_id`
- `feature_hash`
- `hypothesis_id`
- `mvm_approval_id`
- `atlas_lineage_id`
- `compliance_checked`
- `signal_version`

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的 Schema / Contracts 工程师。

目标：
实现 S-01、RC-01、E-03 使用的核心对象契约，保证所有对象可验证、可序列化、可追溯。

请生成：
1. TradingSignal Avro schema
2. RiskDecision Avro schema
3. FeatureSpec JSON schema
4. 对应的 Pydantic models
5. schema validation service
6. contract tests

TradingSignal 强制字段：
- signal_id
- confidence
- model_run_id
- feature_hash
- hypothesis_id
- mvm_approval_id
- atlas_lineage_id
- compliance_checked
- signal_version

规则：
- confidence < 0.6 必须标记为 blocked
- 没有 mvm_approval_id 的信号不得视为 valid
- schema 必须可用于 Kafka/registry

输出：
- schemas/
- app/contracts/
- tests/contracts/
- README
```
