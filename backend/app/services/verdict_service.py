import json

from sqlalchemy.orm import Session

from app.models.verdict import Verdict


def save_verdict(
    db: Session,
    rule_id: int,
    rule_name: str,
    verdict: str,
    event: dict
):

    db_verdict = Verdict(
        rule_id=rule_id,
        rule_name=rule_name,
        verdict=verdict,
        event_data=json.dumps(event)
    )

    db.add(db_verdict)

    db.commit()

    db.refresh(db_verdict)

    return db_verdict