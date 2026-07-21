import hashlib
import json


def generate_verdict_hash(
    rule_id: int,
    rule_name: str,
    verdict: str,
    event_data: dict
) -> str:
    """
    Generate a SHA-256 hash for a verdict.
    """

    payload = {
        "rule_id": rule_id,
        "rule_name": rule_name,
        "verdict": verdict,
        "event_data": event_data
    }

    payload_string = json.dumps(payload, sort_keys=True)

    return hashlib.sha256(
        payload_string.encode("utf-8")
    ).hexdigest()