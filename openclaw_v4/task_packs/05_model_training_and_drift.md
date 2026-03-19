# 任务包 05：模型训练、因果发现与漂移监控包

## 任务定位
思维导图把 `M-01/M-02/M-03/M-04` 放在研究链内，且 `M-03` 明确要求隔离仓库 + ComplianceFilter，`M-04` 要负责生产期漂移监控。

## 输入
- 特征集
- 标签集
- 训练数据版本
- Model config

## 输出
- train pipeline
- causal discovery reports
- MLflow integration
- DVC hash binding
- CPCV / 泄漏检测
- drift monitor

## 硬约束
- 训练产物必须绑定 `mlflow_run_id`
- 数据必须绑定 `dvc_data_hash`
- 必须输出 causal report
- 必须输出 leak check

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的模型平台工程师。

目标：
实现 M-01 / M-02 / M-04 的研究训练闭环，并为 RC-02 独立验证提供可复现产物。

请实现：
1. causal discovery pipeline
2. model training pipeline
3. MLflow artifact tracking
4. dataset hash binding
5. CPCV-based leakage checks
6. overfit diagnostics
7. drift monitoring for production models

输出必须包含：
- causal_report_id
- mlflow_run_id
- dvc_data_hash
- leakage_report
- drift_report

不要：
- 直接接入生产交易
- 绕过状态机
```
