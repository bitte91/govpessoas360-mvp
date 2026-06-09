from pydantic import BaseModel, Field


class IndexInput(BaseModel):
    strategy: float = Field(ge=0, le=100)
    organization: float = Field(ge=0, le=100)
    risk_management: float = Field(ge=0, le=100)
    transparency: float = Field(ge=0, le=100)

    payroll: float = Field(ge=0, le=100)
    labor_contracts: float = Field(ge=0, le=100)
    self_diagnosis: float = Field(ge=0, le=100)
    training: float = Field(ge=0, le=100)

    documentation: float = Field(ge=0, le=100)
    harmful_agents: float = Field(ge=0, le=100)
    benefits_management: float = Field(ge=0, le=100)
    litigation: float = Field(ge=0, le=100)

    pgr_ppra: float = Field(ge=0, le=100)
    pcmso: float = Field(ge=0, le=100)
    sst_training: float = Field(ge=0, le=100)
    accidents: float = Field(ge=0, le=100)
    investment: float = Field(ge=0, le=100)


class RiskInput(BaseModel):
    category: str
    probability: int = Field(ge=1, le=5)
    impact: int = Field(ge=1, le=5)
    unit_cost: float = Field(ge=0)
    quantity: int = Field(ge=1)
