import os


def detect_rule_type(filename: str):
    """
    Detects the rule type based on file extension.
    """

    extension = os.path.splitext(filename)[1].lower()

    if extension in [".yml", ".yaml"]:
        return "Sigma"

    elif extension == ".kql":
        return "KQL"

    elif extension == ".spl":
        return "SPL"

    elif extension == ".eql":
        return "EQL"

    else:
        return None