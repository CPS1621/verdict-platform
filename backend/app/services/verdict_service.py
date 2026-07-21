import json

from sqlalchemy.orm import Session

from app.models.verdict import Verdict
from app.utils.hash_utils import generate_verdict_hash


def save_verdict(
    db: Session,
    rule_id: int,
    rule_name: str,
    verdict: str,
    event: dict
):

    verdict_hash = generate_verdict_hash(
        rule_id=rule_id,
        rule_name=rule_name,
        verdict=verdict,
        event_data=event
    )

    db_verdict = Verdict(
        rule_id=rule_id,
        rule_name=rule_name,
        verdict=verdict,
        event_data=json.dumps(event),
        verdict_hash=verdict_hash
    )

    db.add(db_verdict)

    db.commit()

    db.refresh(db_verdict)

    return db_verdict


def get_all_verdicts(db: Session):
    return db.query(Verdict).all()


def get_verdict_by_id(db: Session, verdict_id: int):
    return (
        db.query(Verdict)
        .filter(Verdict.id == verdict_id)
        .first()
    )


def get_verdicts_by_rule(db: Session, rule_id: int):
    return (
        db.query(Verdict)
        .filter(Verdict.rule_id == rule_id)
        .all()
    )