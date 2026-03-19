# OpenClaw V4.0 Phase-1 Test Matrix

| Layer | Test Case | Expected Result |
| --- | --- | --- |
| Contract | State machine sequence matches required business order | Pass only if YAML sequence is exact |
| Contract | Missing `mvm_approval_id` | Reject |
| Contract | Missing `sdr_id` | Reject |
| Contract | Missing `RiskDecision` | Reject |
| Contract | Evidence pack omitted on transition | Reject with exception |
| Contract | Invalid state edge | Reject with exception |
| Contract | All hard gates present and approved | Allow |
| Contract | Audit envelope contains replay pointer | Pass |
| Schema | Undeclared fields in any core schema | Validation failure |
| CI | Contract suite required before merge | Mandatory gate |
| CI | Lint/type checks for skeleton package | Mandatory gate |
| Replay | Audit payload can be serialized for replay | Mandatory gate |
