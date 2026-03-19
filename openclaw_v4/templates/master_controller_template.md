# OpenClaw V4.0 Master Controller Template

## System Identity
- Program: OpenClaw V4.0
- Phase: Phase 1 Skeleton
- Objective: Build an auditable, reproducible, replayable, gate-controlled production skeleton.

## Global Non-Negotiables
1. Strict dataflow only:
   - research_chain
   - mvm_independent_validation
   - signal_issuance
   - risk_execution
   - operations_control
   - ledger_clearing
   - audit_traceability
2. Control plane first, business plane second.
3. Explicit IO contracts only; no implicit fields.
4. Never bypass `mvm_approval_id`, `sdr_id`, `RiskDecision`.
5. Default reject.
6. Contract tests before implementation.
7. Every state transition emits an evidence pack and replay pointer.
8. Phase 1 excludes strategy logic.

## Execution Protocol For Claude / ChatGPT Codex
- Step 1: Read repository template.
- Step 2: Execute task packs in numeric order.
- Step 3: Do not start the next pack until the previous pack's acceptance criteria are met.
- Step 4: For every changed contract, update tests first.
- Step 5: For every state change, update audit/replay artifacts.

## Required Final Output
- repository structure
- service list
- interface definitions
- state machine definition
- core schemas
- test matrix
- CI/CD rules
- status summary of completed task packs
