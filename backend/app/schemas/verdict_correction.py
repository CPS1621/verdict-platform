from pydantic import BaseModel


class VerdictCorrectionRequest(BaseModel):
    verdict: str


class VerdictCorrectionResponse(BaseModel):
    id: int
    rule_id: int
    rule_name: str
    verdict: str
    verdict_hash: str