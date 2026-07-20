from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

import os
import shutil

from app.database.database import get_db
from app.schemas.rule import RuleCreate, RuleUpdate, RuleResponse
from app.schemas.validator import ValidationRequest

from app.services.rule_service import (
    upload_sigma_rule,
    get_all_rules,
    get_rule_by_id,
    create_rule as create_rule_service,
    update_rule as update_rule_service,
    delete_rule as delete_rule_service,
    validate_uploaded_rule
)

router = APIRouter()


@router.post("/rules", response_model=RuleResponse)
def create_rule(
    rule: RuleCreate,
    db: Session = Depends(get_db)
):
    return create_rule_service(db, rule)


@router.get("/rules", response_model=list[RuleResponse])
def get_rules(db: Session = Depends(get_db)):
    return get_all_rules(db)


@router.get("/rules/{rule_id}", response_model=RuleResponse)
def get_rule(
    rule_id: int,
    db: Session = Depends(get_db)
):
    rule = get_rule_by_id(db, rule_id)

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Rule not found"
        )

    return rule


@router.put("/rules/{rule_id}", response_model=RuleResponse)
def update_rule(
    rule_id: int,
    updated_rule: RuleUpdate,
    db: Session = Depends(get_db)
):
    rule = update_rule_service(
        db,
        rule_id,
        updated_rule
    )

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Rule not found"
        )

    return rule


@router.delete("/rules/{rule_id}")
def delete_rule(
    rule_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_rule_service(
        db,
        rule_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Rule not found"
        )

    return {
        "message": "Rule deleted successfully"
    }


@router.post("/rules/upload")
def upload_rule(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    new_rule = upload_sigma_rule(
        file_path,
        db
    )

    return {
        "message": "Rule uploaded and saved successfully",
        "rule_id": new_rule.id,
        "rule_name": new_rule.rule_name
    }


@router.post("/rules/validate/{rule_id}")
def validate_rule_endpoint(
    rule_id: int,
    request: ValidationRequest,
    db: Session = Depends(get_db)
):
    result = validate_uploaded_rule(
        db=db,
        rule_id=rule_id,
        event=request.event
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Rule not found."
        )

    return result