# 任务包 03：严格金融特征工程包

## 任务定位
这是金融特征工程系统性开发的核心。必须从第一天就具备 point-in-time、一致性、可回放和 hash 化能力。

## 输入
- `FeatureSpec`
- 市场数据 schema
- 标签口径
- 时间戳规范

## 输出
- feature registry
- point-in-time join engine
- as-of join engine
- feature hash
- offline/online parity checker
- replay loader

## 硬约束
- 禁止未来函数
- 禁止训练和生产特征口径漂移
- 所有线上特征必须能回放
- 所有特征必须可注册、可版本化

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的金融特征工程负责人。

目标：
实现机构级严格特征工程系统，而不是 notebook 级别的临时 DataFrame 特征。

必须实现：
1. FeatureSpec registry
2. point-in-time join
3. as-of join
4. label horizon definition
5. future leakage detector
6. missing/outlier policy engine
7. feature_hash generator
8. offline-online parity checker
9. replayable feature loader

要求：
- 所有特征都必须注册到 FeatureSpec
- 所有特征都必须可回放
- 所有特征都必须产生 feature_hash
- 训练和生产特征必须一致
- 不允许 notebook 直连生产

输出：
- feature_store/
- feature_specs/
- parity_checker/
- replay/
- tests/unit/
- tests/integration/

技术优先：
Python + Feast-compatible design + Parquet + PostgreSQL metadata。
```
