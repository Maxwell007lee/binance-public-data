# 任务包 08：RC-01 实时风控 + E-03 执行引擎包

## 任务定位
这是生产硬门。V4.0 已明确四层不可绕过：Layer 1 本地白名单物理拒单；Layer 2 Kafka 堵塞自动 gRPC 降级；Layer 3 网络分区 Fail-safe；Layer 4 审计哈希链 / 零容忍 orphan fill。

## 输入
- TradingSignal
- RiskDecision
- whitelist snapshot
- market/order interfaces

## 输出
- risk gate service
- local whitelist validator
- gRPC fallback
- fail-safe controller
- execution engine
- reject reason audit trail

## 硬约束
- 无有效风险决策即拒单
- 风险决策过期即拒单
- RC-01 宕机也不得默认放行
- 所有订单都要有审计日志

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的 RC-01 / E-03 联合工程师。

目标：
实现不可绕过的实时风控与执行闭环，默认拒绝，绝不默认放行。

必须实现：
1. RiskDecision validation
2. local whitelist check in E-03
3. Kafka lag detection and gRPC fallback
4. network partition fail-safe behavior
5. order submit / amend / cancel / fill pipeline
6. reject-reason audit logging
7. orphan fill detection hooks

规则：
- 无 APPROVED 决策不得下单
- 风险决策过期不得下单
- RC-01 宕机也不得放行
- network partition 时停止接收新信号
- 每笔订单和成交必须能被追踪到风险决策

输出：
- risk_gateway/
- execution_engine/
- grpc_fallback/
- fail_safe/
- tests/integration/
```
