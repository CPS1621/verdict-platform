from fastapi import APIRouter
from app.schemas.validator import ValidationRequest
from app.services.validator_service import validate_rule

router = APIRouter(
    prefix="/validator",
    tags=["Validator"]
)

@router.post("/validate")
def validate(request: ValidationRequest):

    print(">>> validator.py endpoint called <<<")

    result = validate_rule(
        request.rule_query,
        request.event
    )

    print(result)

    return result