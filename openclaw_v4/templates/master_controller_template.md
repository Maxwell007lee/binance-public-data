# OpenClaw V4.0 主控文件总说明

本目录提供 8 份主控治理模板，供 Claude / ChatGPT Codex 先搭制度骨架，再做业务实现。

## 模板列表
1. `governance/01_state_machine.yaml`
2. `governance/02_signal_contract.avsc`
3. `governance/03_risk_decision_contract.avsc`
4. `governance/04_feature_spec_contract.json`
5. `governance/05_invariants.md`
6. `governance/06_acceptance_gates.md`
7. `governance/07_test_matrix.csv`
8. `governance/08_repo_policy.md`

## 执行纪律
- 先治理，后业务。
- 先 contract tests，后实现。
- 默认拒绝，禁止默认放行。
- 禁止任何单一 AI 会话同时拥有：写主仓代码、修改验收标准、签发批准结论三种权力。
