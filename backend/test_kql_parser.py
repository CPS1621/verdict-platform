from app.services.kql_parser import parse_kql

result = parse_kql("uploads/failed_logins.kql")

print(result)