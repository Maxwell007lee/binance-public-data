# Task Pack 02 - State Machine and Gates

## Objective
Implement deterministic workflow control and hard-gate enforcement.

## Required Hard Gates
- `mvm_approval_id`
- `sdr_id`
- `RiskDecision`

## Deliverables
- State machine definition file.
- Gate evaluator.
- Invariant validator.
- Audit transition wrapper requiring evidence packs.

## Acceptance Criteria
- Invalid edges are rejected.
- Missing evidence pack rejects transition.
- Missing any hard gate rejects downstream flow.
- Approved flow is allowed only when all gates are satisfied.
