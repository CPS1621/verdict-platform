import yaml


def parse_rule(file_path: str):
    """
    Reads a Sigma YAML rule and returns it as a Python dictionary.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        rule_data = yaml.safe_load(file)

    return rule_data