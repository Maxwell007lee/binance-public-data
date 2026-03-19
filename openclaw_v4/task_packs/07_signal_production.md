# 任务包 07：S-01 信号生产包

## 任务定位
把研究产物转成唯一受控的生产信号接口，目标是血缘追溯 100%、P99 < 100ms、SDR 审批 100%。

## 输入
- approved model artifact
- approved feature set
- `mvm_approval_id`
- SDR metadata

## 输出
- signal producer service
- confidence gate
- lineage binder
- signal event stream

## 硬约束
- 置信度不足要拦截
- 必须写入所有血缘字段
- 必须与 SDR 编号绑定

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的 S-01 信号生产工程师。

目标：
实现研发到生产之间唯一受控的信号出口。

请实现：
1. signal producer service
2. lineage binder
3. confidence gate
4. schema validator
5. Kafka publisher
6. latency metrics

要求：
- TradingSignal 必须包含全部强制字段
- confidence < 0.6 的信号必须被拦截
- signal_version 必须绑定 SDR approval id
- P99 latency target < 100ms

输出：
- app/signal_producer/
- schema validation middleware
- metrics/
- tests/
```
