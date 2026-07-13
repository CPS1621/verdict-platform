from app.services.validator_service import validate_rule
import json

# Sample Sigma detection rule
rule_query = json.dumps({
    "selection": {
        "Image": "*powershell.exe"
    }
})

# Event that should match
event = {
    "Image": "cmd.exe"
}

result = validate_rule(rule_query, event)

print(result)