# OpenClaw V4.0 AI Task Packs

These task packs are written so Claude / ChatGPT Codex can copy them directly into an execution session.

## Execution Order
1. `01_control_plane_foundation.md`
2. `02_state_machine_and_gates.md`
3. `03_research_chain_service.md`
4. `04_mvm_validation_service.md`
5. `05_signal_issuance_service.md`
6. `06_risk_execution_service.md`
7. `07_operations_control_service.md`
8. `08_ledger_clearing_service.md`
9. `09_audit_traceability_service.md`
10. `10_ci_cd_and_release_governance.md`

## Usage Rule
- Execute the packs strictly in order.
- Do not invent strategy logic in phase 1.
- Default reject unless the required gate is explicitly satisfied.
- Every state change must emit an evidence pack and be replayable.
