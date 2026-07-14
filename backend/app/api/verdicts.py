from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.verdict_event import VerdictEvent
from app.schemas.verdict import VerdictResponse

router = APIRouter()


@router.get("/verdicts", response_model=list[VerdictResponse])
def get_verdicts(db: Session = Depends(get_db)):
    verdicts = db.query(VerdictEvent).all()
    return verdicts


@router.get("/verdicts/{verdict_id}", response_model=VerdictResponse)
def get_verdict(
    verdict_id: int,
    db: Session = Depends(get_db)
):
    verdict = (
        db.query(VerdictEvent)
        .filter(VerdictEvent.id == verdict_id)
        .first()
    )

    if not verdict:
        raise HTTPException(
            status_code=404,
            detail="Verdict not found."
        )

    return verdict


@router.get("/verdicts/rule/{rule_id}", response_model=list[VerdictResponse])
def get_verdicts_by_rule(
    rule_id: int,
    db: Session = Depends(get_db)
):
    verdicts = (
        db.query(VerdictEvent)
        .filter(VerdictEvent.rule_id == rule_id)
        .all()
    )

    if not verdicts:
        raise HTTPException(
            status_code=404,
            detail="No verdicts found for this rule."
        )

    return verdicts