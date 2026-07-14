from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_rules: int
    total_verdicts: int
    detected: int
    missed: int