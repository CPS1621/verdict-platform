from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.verdict import VerdictResponse
from app.services.verdict_service import (
    get_all_verdicts,
    get_verdict_by_id,
    get_verdicts_by_rule as get_verdicts_by_rule_service,
)

router = APIRouter()


@router.get("/verdicts", response_model=list[VerdictResponse])
def get_verdicts(db: Session = Depends(get_db)):
    return get_all_verdicts(db)


@router.get("/verdicts/{verdict_id}", response_model=VerdictResponse)
def get_verdict(
    verdict_id: int,
    db: Session = Depends(get_db)
):
    verdict = get_verdict_by_id(db, verdict_id)

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
    verdicts = get_verdicts_by_rule_service(db, rule_id)

    if not verdicts:
        raise HTTPException(
            status_code=404,
            detail="No verdicts found for this rule."
        )

    return verdicts