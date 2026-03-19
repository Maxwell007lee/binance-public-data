# Task Pack 05 - Signal Issuance Service

## Objective
Emit SDR signals only after approved MVM verification.

## Service Contract
- Inputs: approved `MVMVerification`, referenced `ResearchChain`
- Output: `SDRSignal`

## Rules
- `sdr_id` is mandatory.
- Signal payload schema must be explicit.
- Service may define issuance envelopes but not strategy logic.

## Acceptance Criteria
- No downstream risk evaluation without `sdr_id`.
- `SDRSignal.mvm_approval_id` must match the upstream MVM approval.
