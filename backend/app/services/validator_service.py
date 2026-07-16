import json


def validate_rule(rule_query: str, event: dict):
    """
    Validates whether an event matches the Sigma detection rule.
    Returns a detailed verdict.
    """

    detection = json.loads(rule_query)

    selection = detection.get("detection", {}).get("selection", {})

    matched_fields = []

    print("Selection:", selection)

    for key, value in selection.items():

        event_value = event.get(key)

        if event_value is None:
            return {
                "status": "Missed",
                "confidence": 0,
                "matched_fields": matched_fields,
                "message": f"Field '{key}' is missing."
            }

        expected = value.replace("*", "").lower()

        if expected not in event_value.lower():
            return {
                "status": "Missed",
                "confidence": 0,
                "matched_fields": matched_fields,
                "message": f"Field '{key}' did not match."
            }

        matched_fields.append(key)

    return {
        "status": "Detected",
        "confidence": 95,
        "matched_fields": matched_fields,
        "message": "All required fields matched."
    }