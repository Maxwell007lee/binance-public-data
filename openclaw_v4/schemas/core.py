from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List


@dataclass(frozen=True, slots=True)
class EvidencePack:
    evidence_id: str
    artifact_hash: str
    artifact_uri: str
    collected_at: str
    collected_by: str
    replay_pointer: str

    def model_dump_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)


@dataclass(frozen=True, slots=True)
class ResearchChain:
    research_id: str
    hypothesis_id: str
    feature_snapshot_id: str
    model_version: str
    dataset_version: str
    author: str
    evidence_refs: List[str]

    def model_dump_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)


@dataclass(frozen=True, slots=True)
class MVMVerification:
    verification_id: str
    research_id: str
    mvm_approval_id: str
    verifier: str
    status: str
    evidence_refs: List[str]

    def __post_init__(self) -> None:
        if self.status not in {'approved', 'rejected'}:
            raise ValueError('status must be approved or rejected')


@dataclass(frozen=True, slots=True)
class SDRSignal:
    sdr_id: str
    research_id: str
    mvm_approval_id: str
    signal_type: str
    payload: Dict[str, Any]
    issuer: str

    def __post_init__(self) -> None:
        allowed = {'allocation_instruction', 'execution_instruction', 'cancel_instruction'}
        if self.signal_type not in allowed:
            raise ValueError(f'signal_type must be one of {sorted(allowed)}')


@dataclass(frozen=True, slots=True)
class RiskDecision:
    decision_id: str
    sdr_id: str
    mvm_approval_id: str
    verdict: str
    constraints_applied: List[str]
    decided_by: str

    def __post_init__(self) -> None:
        if self.verdict not in {'approved', 'rejected'}:
            raise ValueError('verdict must be approved or rejected')


@dataclass(frozen=True, slots=True)
class GateDecision:
    gate_name: str
    decision: str
    allowed: bool
    reasons: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.decision not in {'allow', 'reject'}:
            raise ValueError('decision must be allow or reject')


@dataclass(frozen=True, slots=True)
class AuditEnvelope:
    audit_id: str
    workflow_name: str
    transition: str
    actor: str
    evidence_pack: EvidencePack
    payload_snapshot: Dict[str, Any]

    def model_dump_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)
