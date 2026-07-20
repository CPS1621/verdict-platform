from pydantic import BaseModel


class ValidationRequest(BaseModel):
    event: dict