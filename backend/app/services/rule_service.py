import json

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.rule import Rule
from app.services.rule_detector import detect_rule_type
from app.services.rule_parser import parse_rule


def upload_sigma_rule(file_path: str, db: Session):
    """
    Uploads a Sigma rule, validates it,
    checks duplicates, and saves it to the database.
    """

    # Detect the rule type
    rule_type = detect_rule_type(file_path)

    if rule_type is None:
        raise HTTPException(
            status_code=400,
            detail="Unsupported rule type."
        )

    # Parse the Sigma rule
    rule_data = parse_rule(file_path)

    # Validate required fields
    required_fields = ["title", "description", "detection", "level"]

    for field in required_fields:
        if field not in rule_data:
            raise HTTPException(
                status_code=400,
                detail=f"Missing required field: {field}"
            )

    # Extract values
    rule_name = rule_data.get("title")
    description = rule_data.get("description")
    severity = rule_data.get("level")
    status = rule_data.get("status")

    # Check duplicate
    existing_rule = db.query(Rule).filter(
        Rule.rule_name == rule_name
    ).first()

    if existing_rule:
        raise HTTPException(
            status_code=409,
            detail="Rule with this name already exists."
        )

    # Convert detection to JSON
    query = json.dumps(rule_data.get("detection"))

    # Save to database
    new_rule = Rule(
        rule_name=rule_name,
        rule_type=rule_type,
        severity=severity,
        description=description,
        query=query,
        status=status
    )

    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return new_rule