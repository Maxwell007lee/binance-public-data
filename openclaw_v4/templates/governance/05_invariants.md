# OpenClaw V4.0 Invariants

## I-01 决策绑定
每笔 Fill 必须能唯一映射到一个有效的 APPROVED RiskDecision。

## I-02 时间一致性
特征事件时间不得晚于信号生成时间；信号生成时间不得晚于风控决策时间。

## I-03 状态单调性
策略生命周期状态只能前进或进入 SR_REJECTED，不得逆向跳转。

## I-04 批准依赖
没有 mvm_approval_id 的模型不得进入生产态。

## I-05 SDR 依赖
没有 cro_sign/cio_sign/cto_sign 的策略不得进入 S8 以后状态。

## I-06 信号血缘完整性
所有 TradingSignal 必须具备强制血缘字段，不得存在匿名信号。

## I-07 风控默认拒绝
无有效 RiskDecision、过期决策或签名异常时，E-03 必须拒单。

## I-08 审计可追溯
所有订单、成交、取消、拒单事件必须进入不可篡改审计链。

## I-09 可回放
任一生产事件都必须能使用冻结数据与冻结代码路径进行 replay。

## I-10 异常零容忍
orphan fill、审计链断裂、状态跳跃、未授权变更均视为 P0。
