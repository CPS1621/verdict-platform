from pydantic import BaseModel


class ValidationRequest(BaseModel):
    rule_query: str
    event: dict