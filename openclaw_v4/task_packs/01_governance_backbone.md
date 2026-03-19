# 任务包 01：治理骨架与状态机总控包

## 任务定位
先把系统从“文档”变成“可执行治理框架”。这一包必须最先做，因为 V4.0 把 12 状态机、YAML、PostgreSQL 哈希链、10 条不变量、Fail-safe 定义为形式化基础。

## 输入
- `01_state_machine.yaml`
- `05_invariants.md`
- `06_acceptance_gates.md`
- `08_repo_policy.md`

## 输出
- 状态机引擎
- 状态跃迁守卫器
- 证据包校验器
- Hash-chain 记录器
- Gate 判定器

## 硬约束
- 不允许跳状态
- 没有证据包不得跃迁
- `S4_MVM_APPROVED` 必须要求 `mvm_approval_id`
- `S8_SDR_APPROVED` 必须要求三方联署
- 任意门控失败必须进入 `SR_REJECTED`

## 可直接复制的提示词
```text
你现在是 OpenClaw V4.0 的治理层系统工程师。

目标：
把策略生命周期实现为机构级可审计状态机，而不是普通应用流程。

请完成以下内容：
1. 生成一个可执行的 state machine engine，支持 S0~S10 + SR。
2. 每个状态都必须支持：
   - enter_conditions
   - guard_conditions
   - required_evidence
   - allowed_next_states
   - rejection_path
3. 必须支持 PostgreSQL 持久化和 hash-chain 审计记录。
4. 任意状态变更都必须记录 who / when / why / evidence_hash。
5. 对以下硬门槛做底层强约束：
   - S4 requires mvm_approval_id and repro_deviation < 1.0
   - S8 requires cro_sign + cio_sign + cto_sign
6. 输出：
   - repo tree
   - Python implementation
   - YAML loader
   - DB schema
   - unit tests
   - contract tests
7. 不要实现交易策略，不要实现 UI。

技术栈：
Python 3.11 + FastAPI + PostgreSQL + SQLAlchemy + Pydantic。

遵守：
默认拒绝，禁止绕过状态机直接调用执行链。
```
