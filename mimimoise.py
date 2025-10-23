import json
from datetime import datetime

clients = { 
    "123" : {
        "nom" : "Tralalero", 
        "prénom" : "Tralala", 
        "solde" : 52465, 
        "dépots" : [ 
            {"montant" : 845, "date" : "14/01/2024"}, 
            {"montant" : 940, "date" : "03/02/2024"}
        ], 
        "retraits" : [ 
            {"montant" : 354, "date" : "27/03/2024"}, 
            {"montant" : 540, "date" : "09/04/2024"} 
        ] 
    }, 
    "321" : { 
        "nom" : "Bombardiro", 
        "prénom" : "Crocodilo", 
        "solde" : 21465, 
        "dépots" : [ 
            {"montant" : 546, "date" : "18/05/2024"}, 
            {"montant" : 456, "date" : "06/06/2024"} 
        ], 
        "retraits" : [ 
            {"montant" : 458, "date" : "22/07/2024"}, 
            {"montant" : 789, "date" : "11/08/2024"} 
        ] 
    }, 
    "231" : { 
        "nom" : "Ballerina", 
        "prénom" : "Cappuccina", 
        "solde" : 45308, 
        "dépots" : [ 
            {"montant" : 286, "date" : "30/09/2024"}, 
            {"montant" : 84, "date" : "05/10/2024"} 
        ], 
        "retraits" : [ 
            {"montant" : 68, "date" : "16/11/2024"}, 
            {"montant" : 57, "date" : "28/12/2024"} 
        ] 
    } 
}

with open("clients.json", "w") as f:
    json.dump(clients, f, indent=4, ensure_ascii=False)

with open("clients.json", "r") as f:
    clients = json.load(f)

print(json.dumps(clients, indent=4, ensure_ascii=False))