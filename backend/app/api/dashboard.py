from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.rule import Rule
from app.models.verdict_event import VerdictEvent
from app.schemas.dashboard import DashboardStats

router = APIRouter()


@router.get("/dashboard/stats", response_model=DashboardStats)
def get_dashboard_stats(db: Session = Depends(get_db)):
    # Total rules
    total_rules = db.query(Rule).count()

    # Total verdicts
    total_verdicts = db.query(VerdictEvent).count()

    # Total detected
    detected = (
        db.query(VerdictEvent)
        .filter(VerdictEvent.verdict == "Detected")
        .count()
    )

    # Total missed
    missed = (
        db.query(VerdictEvent)
        .filter(VerdictEvent.verdict == "Missed")
        .count()
    )

    return DashboardStats(
        total_rules=total_rules,
        total_verdicts=total_verdicts,
        detected=detected,
        missed=missed
    )