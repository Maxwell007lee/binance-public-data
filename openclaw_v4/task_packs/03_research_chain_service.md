# Task Pack 03 - Research Chain Service

## Objective
Define the research-chain boundary as an auditable intake service.

## Service Contract
- Input: `ResearchChain`
- Output: accepted/rejected research submission event

## Must Implement
- REST contract for create/get
- Kafka topic naming
- evidence reference persistence contract
- schema validation contract tests

## Acceptance Criteria
- No research object is accepted without evidence references.
- Research IDs are explicit and immutable in the contract.
- Downstream services consume research by ID, not ad hoc payload mutation.
