from openclaw_v4.schemas.core import MVMVerification, ResearchChain, RiskDecision, SDRSignal


class InvariantViolation(ValueError):
    pass


class InvariantSuite:
    def validate_lineage(
        self,
        research: ResearchChain,
        mvm: MVMVerification,
        sdr: SDRSignal,
        risk_decision: RiskDecision,
    ) -> None:
        if mvm.research_id != research.research_id:
            raise InvariantViolation('MVMVerification.research_id must match ResearchChain.research_id')
        if sdr.research_id != research.research_id:
            raise InvariantViolation('SDRSignal.research_id must match ResearchChain.research_id')
        if sdr.mvm_approval_id != mvm.mvm_approval_id:
            raise InvariantViolation('SDRSignal.mvm_approval_id must match MVMVerification.mvm_approval_id')
        if risk_decision.sdr_id != sdr.sdr_id:
            raise InvariantViolation('RiskDecision.sdr_id must match SDRSignal.sdr_id')
        if risk_decision.mvm_approval_id != mvm.mvm_approval_id:
            raise InvariantViolation('RiskDecision.mvm_approval_id must match MVMVerification.mvm_approval_id')
