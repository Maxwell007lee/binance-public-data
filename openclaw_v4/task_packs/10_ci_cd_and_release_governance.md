# Task Pack 10 - CI/CD and Release Governance

## Objective
Define merge and release controls for the phase-1 skeleton.

## Required CI Gates
- contract tests
- syntax / compile checks
- schema compatibility review trigger
- state machine change review trigger

## Release Rules
- default manual approval before production deploy
- immutable artifacts required
- evidence retention required
- no deploy when hard-gate enforcement is disabled

## Acceptance Criteria
- CI workflow file exists.
- CI runs contract suite before merge.
- Documentation explains release governance.
