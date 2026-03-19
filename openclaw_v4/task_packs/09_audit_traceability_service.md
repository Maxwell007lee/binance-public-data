# Task Pack 09 - Audit Traceability Service

## Objective
Implement replayable audit envelopes and evidence retention.

## Service Contract
- Input: any transition event + `EvidencePack`
- Output: `AuditEnvelope`

## Rules
- Every critical transition must include a replay pointer.
- Audit envelopes must be serializable.
- Replay API must be defined, even if implementation is skeletal.

## Acceptance Criteria
- Replay metadata exists on every critical state change.
- Audit serialization contract tests pass.
