# OpenClaw V4.0 Phase-1 Services

## Repository Structure

```text
openclaw_v4/
  api/                    # FastAPI entrypoints
  control_plane/          # state machine, gates, invariants, audit orchestration
  business_plane/         # placeholder service boundaries only; no strategy logic in phase 1
  docs/                   # service catalog, test matrix, architecture notes
  schemas/                # explicit IO contracts with extra=forbid
  services/               # service interface notes and dependency wiring stubs
  state_machines/         # YAML state machine definitions
tests/contracts/          # contract-first tests for hard gates and replayability
.github/workflows/        # CI/CD gates
```

## Service List

1. **research-chain-service**: ingests research artifacts, dataset versions, model versions, and evidence references.
2. **mvm-validation-service**: independently validates research outputs and issues `mvm_approval_id` only on approval.
3. **signal-issuance-service**: emits an `SDRSignal` only after the MVM approval gate is satisfied.
4. **risk-execution-service**: evaluates each SDR through hard limits and emits a `RiskDecision`.
5. **operations-control-service**: handles manual/operational holds, kill-switches, and workflow supervision.
6. **ledger-clearing-service**: records approved actions into the accounting and settlement boundary.
7. **audit-traceability-service**: persists replayable evidence packages and audit envelopes for every transition.

## Service Interfaces

### 1. research-chain-service
- **Input contract**: `ResearchChain`
- **Output contract**: accepted `ResearchChain` event with evidence references only.
- **Kafka topics**:
  - `research-chain.submitted`
  - `research-chain.rejected`
- **REST endpoints**:
  - `POST /v1/research-chains`
  - `GET /v1/research-chains/{research_id}`

### 2. mvm-validation-service
- **Input contract**: `ResearchChain`
- **Output contract**: `MVMVerification`
- **Gate**: no signal issuance without `mvm_approval_id`
- **REST endpoints**:
  - `POST /v1/mvm-validations`
  - `GET /v1/mvm-validations/{verification_id}`

### 3. signal-issuance-service
- **Input contract**: approved `MVMVerification` + referenced `ResearchChain`
- **Output contract**: `SDRSignal`
- **Gate**: no downstream risk execution without `sdr_id`
- **REST endpoints**:
  - `POST /v1/signals`
  - `GET /v1/signals/{sdr_id}`

### 4. risk-execution-service
- **Input contract**: `SDRSignal`
- **Output contract**: `RiskDecision`
- **Gate**: default reject; explicit approval required.
- **REST endpoints**:
  - `POST /v1/risk-decisions`
  - `GET /v1/risk-decisions/{decision_id}`

### 5. operations-control-service
- **Input contract**: `RiskDecision` + control directives
- **Output contract**: operational disposition event with evidence pack reference
- **Responsibilities**:
  - workflow pause/resume
  - kill switch
  - supervisory override with evidence pack
- **REST endpoints**:
  - `POST /v1/ops/holds`
  - `POST /v1/ops/releases`
  - `POST /v1/ops/kill-switch`

### 6. ledger-clearing-service
- **Input contract**: approved operational disposition
- **Output contract**: immutable settlement/booking event
- **REST endpoints**:
  - `POST /v1/ledger/bookings`
  - `GET /v1/ledger/bookings/{booking_id}`

### 7. audit-traceability-service
- **Input contract**: any state transition + `EvidencePack`
- **Output contract**: `AuditEnvelope`
- **Replay rule**: every critical transition must include `replay_pointer`
- **REST endpoints**:
  - `POST /v1/audit/envelopes`
  - `POST /v1/audit/replay`
  - `GET /v1/audit/envelopes/{audit_id}`

## Control Plane First Principles

- All schemas are explicit and forbid undeclared fields.
- All hard gates are mandatory: `mvm_approval_id`, `sdr_id`, `RiskDecision`.
- Default decision is reject.
- Every transition must attach an `EvidencePack` and produce an `AuditEnvelope`.
- Business plane remains a placeholder in phase 1; no alpha, strategy, or order-generation logic is implemented.

## Platform Compatibility

- **API**: FastAPI
- **Primary DB**: PostgreSQL
- **Streaming bus**: Kafka
- **Low-latency controls/cache**: Redis
- **Model registry**: MLflow-compatible
- **Data/version lineage**: DVC-compatible
- **Feature registry**: Feast-compatible
