import json


def validate_rule(rule_query: str, event: dict):
    """
    Validates whether an event matches the Sigma detection rule.
    Returns one of:
    - Detected
    - Missed
    """

    detection = json.loads(rule_query)

    selection = detection.get("selection", {})

    for key, value in selection.items():

        event_value = event.get(key)

        if event_value is None:
            return "Missed"

        if value.replace("*", "").lower() not in event_value.lower():
            return "Missed"

    return "Detected"