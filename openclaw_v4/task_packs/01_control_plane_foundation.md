# Task Pack 01 - Control Plane Foundation

## Role
You are OpenClaw V4.0 chief systems engineer.

## Objective
Build the phase-1 control plane before any business logic.

## Mandatory Constraints
1. Preserve strict flow order: research_chain -> mvm_independent_validation -> signal_issuance -> risk_execution -> operations_control -> ledger_clearing -> audit_traceability.
2. Implement control-plane artifacts first: schema, state machine, gate, invariant, audit chain.
3. All contracts must have explicit input/output fields; no implicit fields.
4. Default reject.
5. Do not implement free-form alpha or strategy logic.
6. Write contract tests before implementation.

## Deliverables
- `schemas/`
- `control_plane/`
- `state_machines/`
- `tests/contracts/`
- `docs/services.md`
- `docs/test_matrix.md`

## Acceptance Criteria
- Core schemas exist for ResearchChain, MVMVerification, SDRSignal, RiskDecision, EvidencePack, AuditEnvelope.
- Contract tests fail if hard gates are absent.
- State machine file exists and encodes the required order.
