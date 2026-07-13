def parse_kql(file_path: str):
    """
    Reads a KQL file and returns its query.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        query = file.read()

    return {
        "query": query
    }