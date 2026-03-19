# Task Pack 06 - Risk Execution Service

## Objective
Create the default-reject risk gate for every SDR.

## Service Contract
- Input: `SDRSignal`
- Output: `RiskDecision`

## Rules
- Default verdict is reject unless explicitly approved.
- Decision must reference both `sdr_id` and `mvm_approval_id`.
- Constraints applied must be recorded explicitly.

## Acceptance Criteria
- No execution path exists without a `RiskDecision` object.
- Mismatched cross references are rejected by invariants.
