import json
from datetime import datetime
clients = ""
with open("clients.json", "w") as f:
    json.dump(clients, f, indent=4, ensure_ascii=False)

with open("clients.json", "r") as f:
    clients = json.load(f)

print(json.dumps(clients, indent=4, ensure_ascii=False))
