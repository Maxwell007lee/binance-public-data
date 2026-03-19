from __future__ import annotations

import json
from pathlib import Path

from openclaw_v4.schemas.core import AuditEnvelope, EvidencePack


class WorkflowStateMachine:
    def __init__(self, workflow_name: str, adjacency: dict[str, list[str]]):
        self.workflow_name = workflow_name
        self.adjacency = adjacency

    @classmethod
    def from_file(cls, path: str) -> 'WorkflowStateMachine':
        data = json.loads(Path(path).read_text())
        return cls(workflow_name=data['workflow_name'], adjacency=data['transitions'])

    def transition(self, from_state: str, to_state: str, evidence_pack: EvidencePack | None) -> AuditEnvelope:
        if evidence_pack is None:
            raise ValueError('every state transition requires an evidence pack')
        allowed_targets = self.adjacency.get(from_state, [])
        if to_state not in allowed_targets:
            raise ValueError(f'invalid transition: {from_state} -> {to_state}')
        return AuditEnvelope(
            audit_id=f'{from_state}-to-{to_state}',
            workflow_name=self.workflow_name,
            transition=f'{from_state}->{to_state}',
            actor='state-machine',
            evidence_pack=evidence_pack,
            payload_snapshot={'from_state': from_state, 'to_state': to_state},
        )
