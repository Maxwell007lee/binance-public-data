# Task Pack 07 - Operations Control Service

## Objective
Define the operational control boundary after risk and before ledger booking.

## Service Contract
- Input: approved `RiskDecision` and control directives
- Output: operational disposition with evidence pack

## Must Support
- hold
- release
- kill switch
- supervisory intervention with evidence

## Acceptance Criteria
- Every operational override carries an evidence pack.
- Control actions are replayable and auditable.
