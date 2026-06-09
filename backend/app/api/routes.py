from fastapi import APIRouter
from backend.app.schemas.inputs import IndexInput, RiskInput
from backend.app.services.indices import calculate_indices
from backend.app.services.risks import classify_risk, calculate_financial_exposure

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok", "service": "GOVPESSOAS 360 MVP"}


@router.post("/indices")
def indices(payload: IndexInput):
    return calculate_indices(payload)


@router.post("/risks")
def risks(payload: RiskInput):
    classification = classify_risk(payload.probability, payload.impact)
    exposure = calculate_financial_exposure(
        probability=payload.probability,
        unit_cost=payload.unit_cost,
        quantity=payload.quantity,
    )
    return {"classification": classification, "exposure": exposure}
