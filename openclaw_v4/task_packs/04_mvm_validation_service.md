# Task Pack 04 - MVM Validation Service

## Objective
Create the independent validation stage between research and signal issuance.

## Service Contract
- Input: `ResearchChain`
- Output: `MVMVerification`

## Rules
- Must issue `mvm_approval_id` only when validation is approved.
- Must remain independent from signal issuance implementation.
- Must publish evidence references for validation outcomes.

## Acceptance Criteria
- No signal issuance can proceed without approved `mvm_approval_id`.
- Rejected MVM verdicts stop flow by default.
