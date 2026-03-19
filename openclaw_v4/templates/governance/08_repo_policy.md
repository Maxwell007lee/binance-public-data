# Repo Policy

## 1. 仓库边界
- openclaw-core: 生产主链
- openclaw-validator: 独立验证，只读主仓产物
- openclaw-redteam: 攻击测试，不得写生产配置
- openclaw-infra: 基础设施与策略

## 2. 权限原则
- Builder 无权修改 acceptance gates
- Validator 无权直接修改主仓业务代码
- Red Team 无权签发批准号
- 只有指定审批流可以签发 mvm_approval_id / sdr_id

## 3. 分支保护
- main 仅允许受保护合并
- 必须通过 contract tests / integration tests / security checks
- 关键治理文件需要双审

## 4. 只读依赖
- validator 只读 core artifacts
- redteam 不得引用生产 secrets

## 5. 违规处理
- 任意越权、绕过、静默修改治理文件视为 P0
