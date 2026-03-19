from pathlib import Path
import json
import unittest


from openclaw_v4.control_plane.gates import GateEvaluator
from openclaw_v4.control_plane.invariants import InvariantSuite, InvariantViolation
from openclaw_v4.control_plane.state_machine import WorkflowStateMachine
from openclaw_v4.schemas.core import (
    AuditEnvelope,
    EvidencePack,
    MVMVerification,
    ResearchChain,
    RiskDecision,
    SDRSignal,
)


class Phase1ContractTests(unittest.TestCase):
    def test_required_artifacts_exist(self):
        required = [
            Path('openclaw_v4/state_machines/system_flow.yaml'),
            Path('openclaw_v4/docs/services.md'),
            Path('openclaw_v4/docs/test_matrix.md'),
            Path('.github/workflows/phase1-ci.yml'),
        ]
        for artifact in required:
            self.assertTrue(artifact.exists(), f'missing artifact: {artifact}')

    def test_system_flow_order_is_strict(self):
        data = json.loads(Path('openclaw_v4/state_machines/system_flow.yaml').read_text())
        self.assertEqual(
            data['sequence'],
            [
                'research_chain',
                'mvm_independent_validation',
                'signal_issuance',
                'risk_execution',
                'operations_control',
                'ledger_clearing',
                'audit_traceability',
            ],
        )

    def test_default_reject_without_mandatory_gates(self):
        research = ResearchChain(
            research_id='res-1',
            hypothesis_id='hyp-1',
            feature_snapshot_id='feat-1',
            model_version='mv-1',
            dataset_version='dv-1',
            author='alice',
            evidence_refs=['s3://evidence/research.json'],
        )
        result = GateEvaluator().evaluate_research_to_signal(
            research=research,
            mvm=None,
            sdr=None,
            risk_decision=None,
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.decision, 'reject')
        self.assertIn('mvm_approval_id', result.reasons[0])

    def test_no_transition_without_evidence_pack(self):
        machine = WorkflowStateMachine.from_file('openclaw_v4/state_machines/system_flow.yaml')
        with self.assertRaises(ValueError):
            machine.transition('research_chain', 'mvm_independent_validation', evidence_pack=None)

    def test_transition_requires_expected_edge(self):
        machine = WorkflowStateMachine.from_file('openclaw_v4/state_machines/system_flow.yaml')
        evidence = EvidencePack(
            evidence_id='ev-1',
            artifact_hash='abc',
            artifact_uri='s3://evidence/ev-1.json',
            collected_at='2026-03-19T00:00:00Z',
            collected_by='tester',
            replay_pointer='kafka://audit/replay/1',
        )
        with self.assertRaises(ValueError):
            machine.transition('research_chain', 'risk_execution', evidence_pack=evidence)

    def test_hard_gates_allow_only_when_all_ids_present_and_approved(self):
        research = ResearchChain(
            research_id='res-1',
            hypothesis_id='hyp-1',
            feature_snapshot_id='feat-1',
            model_version='mv-1',
            dataset_version='dv-1',
            author='alice',
            evidence_refs=['s3://evidence/research.json'],
        )
        mvm = MVMVerification(
            verification_id='ver-1',
            research_id='res-1',
            mvm_approval_id='mvm-ok',
            verifier='bob',
            status='approved',
            evidence_refs=['s3://evidence/mvm.json'],
        )
        sdr = SDRSignal(
            sdr_id='sdr-1',
            research_id='res-1',
            mvm_approval_id='mvm-ok',
            signal_type='allocation_instruction',
            payload={'target_book': 'alpha-1', 'target_weight_bps': 150},
            issuer='signal-service',
        )
        risk = RiskDecision(
            decision_id='risk-1',
            sdr_id='sdr-1',
            mvm_approval_id='mvm-ok',
            verdict='approved',
            constraints_applied=['max_gross_notional'],
            decided_by='risk-engine',
        )
        result = GateEvaluator().evaluate_research_to_signal(research, mvm, sdr, risk)
        self.assertTrue(result.allowed)
        self.assertEqual(result.decision, 'allow')


    def test_lineage_invariants_reject_cross_reference_breaks(self):
        research = ResearchChain(
            research_id='res-1', hypothesis_id='hyp-1', feature_snapshot_id='feat-1',
            model_version='mv-1', dataset_version='dv-1', author='alice',
            evidence_refs=['s3://evidence/research.json'],
        )
        mvm = MVMVerification(
            verification_id='ver-1', research_id='res-2', mvm_approval_id='mvm-ok',
            verifier='bob', status='approved', evidence_refs=['s3://evidence/mvm.json'],
        )
        sdr = SDRSignal(
            sdr_id='sdr-1', research_id='res-1', mvm_approval_id='mvm-ok',
            signal_type='allocation_instruction', payload={'target_book': 'alpha-1'}, issuer='signal-service',
        )
        risk = RiskDecision(
            decision_id='risk-1', sdr_id='sdr-1', mvm_approval_id='mvm-ok',
            verdict='approved', constraints_applied=['max_gross_notional'], decided_by='risk-engine',
        )
        with self.assertRaises(InvariantViolation):
            InvariantSuite().validate_lineage(research, mvm, sdr, risk)

    def test_audit_envelope_is_replayable_and_explicit(self):
        evidence = EvidencePack(
            evidence_id='ev-2',
            artifact_hash='hash-2',
            artifact_uri='s3://evidence/ev-2.json',
            collected_at='2026-03-19T00:00:00Z',
            collected_by='tester',
            replay_pointer='kafka://audit/replay/2',
        )
        envelope = AuditEnvelope(
            audit_id='audit-1',
            workflow_name='openclaw_v4_phase1',
            transition='research_chain->mvm_independent_validation',
            actor='tester',
            evidence_pack=evidence,
            payload_snapshot={'research_id': 'res-1'},
        )
        data = json.loads(envelope.model_dump_json())
        self.assertEqual(data['evidence_pack']['replay_pointer'], 'kafka://audit/replay/2')
        self.assertNotIn('implicit_field', data)


if __name__ == '__main__':
    unittest.main()
