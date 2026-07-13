from app.services.rule_service import upload_sigma_rule
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

import os
import shutil
import json

from app.database.database import get_db
from app.models.rule import Rule
from app.schemas.rule import RuleCreate, RuleUpdate, RuleResponse
from app.services.rule_parser import parse_rule
from app.schemas.validator import ValidationRequest
from app.services.validator_service import validate_rule
import hashlib

from app.models.verdict_event import VerdictEvent

router = APIRouter()


@router.post("/rules", response_model=RuleResponse)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    new_rule = Rule(
        rule_name=rule.rule_name,
        rule_type=rule.rule_type,
        severity=rule.severity,
        description=rule.description,
        query=rule.query
    )

    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return new_rule


@router.get("/rules", response_model=list[RuleResponse])
def get_rules(db: Session = Depends(get_db)):
    rules = db.query(Rule).all()
    return rules

@router.get("/rules/{rule_id}", response_model=RuleResponse)
def get_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    return rule

@router.put("/rules/{rule_id}", response_model=RuleResponse)
def update_rule(
    rule_id: int,
    updated_rule: RuleUpdate,
    db: Session = Depends(get_db)
):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    rule.rule_name = updated_rule.rule_name
    rule.rule_type = updated_rule.rule_type
    rule.severity = updated_rule.severity
    rule.description = updated_rule.description
    rule.query = updated_rule.query
    rule.status = updated_rule.status

    db.commit()
    db.refresh(rule)

    return rule

@router.delete("/rules/{rule_id}")
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    db.delete(rule)
    db.commit()

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

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_rule = upload_sigma_rule(file_path, db)

    return {
        "message": "Rule uploaded and saved successfully",
        "rule_id": new_rule.id,
        "rule_name": new_rule.rule_name
    }

@router.post("/rules/validate/{rule_id}")
def validate_uploaded_rule(
    rule_id: int,
    request: ValidationRequest,
    db: Session = Depends(get_db)
):
    # Get the rule from the database
    rule = db.query(Rule).filter(Rule.id == rule_id).first()

    if not rule:
        raise HTTPException(
            status_code=404,
            detail="Rule not found."
        )

    # Validate the event against the rule
    verdict = validate_rule(rule.query, request.event)

    # Convert event dictionary to JSON string
    event_json = json.dumps(request.event)

    # Generate SHA-256 hash
    hash_input = (
        str(rule.id)
        + rule.rule_name
        + verdict
        + event_json
    )

    verdict_hash = hashlib.sha256(
        hash_input.encode()
    ).hexdigest()

    # Create VerdictEvent object
    verdict_event = VerdictEvent(
        rule_id=rule.id,
        rule_name=rule.rule_name,
        verdict=verdict,
        event_data=event_json,
        verdict_hash=verdict_hash
    )

    # Save to database
    db.add(verdict_event)
    db.commit()

    # Return response
    return {
        "rule_id": rule.id,
        "rule_name": rule.rule_name,
        "verdict": verdict
    }