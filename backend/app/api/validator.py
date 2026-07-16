from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.validator import ValidationRequest
from app.services.validator_service import validate_rule
from app.services.verdict_service import save_verdict
from app.kafka.producer import publish_verdict
from app.database.database import get_db

router = APIRouter(
    prefix="/validator",
    tags=["Validator"]
)


@router.post("/validate")
def validate(
    request: ValidationRequest,
    db: Session = Depends(get_db)
):

    print(">>> validator.py endpoint called <<<")

    result = validate_rule(
        request.rule_query,
        request.event
    )

    save_verdict(
        db=db,
        rule_id=1,
        rule_name="Suspicious PowerShell",
        verdict=result["status"],
        event=request.event
    )

    publish_verdict({
        "rule_id": 1,
        "rule_name": "Suspicious PowerShell",
        "status": result["status"],
        "confidence": result["confidence"],
        "matched_fields": result["matched_fields"],
        "event": request.event
})
    print(result)

    return result