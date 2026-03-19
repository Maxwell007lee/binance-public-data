from openclaw_v4.schemas.core import GateDecision, MVMVerification, ResearchChain, RiskDecision, SDRSignal


class GateEvaluator:
    def evaluate_research_to_signal(
        self,
        research: ResearchChain,
        mvm: MVMVerification | None,
        sdr: SDRSignal | None,
        risk_decision: RiskDecision | None,
    ) -> GateDecision:
        reasons: list[str] = []
        if not research.evidence_refs:
            reasons.append('research evidence_refs must not be empty')
        if mvm is None or not mvm.mvm_approval_id:
            reasons.append('missing required hard gate: mvm_approval_id')
        elif mvm.status != 'approved':
            reasons.append('mvm verification must be approved')
        if sdr is None or not sdr.sdr_id:
            reasons.append('missing required hard gate: sdr_id')
        if risk_decision is None:
            reasons.append('missing required hard gate: RiskDecision')
        elif risk_decision.verdict != 'approved':
            reasons.append('RiskDecision verdict must be approved')
        elif sdr is not None and risk_decision.sdr_id != sdr.sdr_id:
            reasons.append('RiskDecision.sdr_id must match SDRSignal.sdr_id')
        if mvm is not None and sdr is not None and sdr.mvm_approval_id != mvm.mvm_approval_id:
            reasons.append('SDRSignal.mvm_approval_id must match MVMVerification.mvm_approval_id')

        allowed = not reasons
        return GateDecision(
            gate_name='research_to_signal_gate',
            decision='allow' if allowed else 'reject',
            allowed=allowed,
            reasons=reasons,
        )
