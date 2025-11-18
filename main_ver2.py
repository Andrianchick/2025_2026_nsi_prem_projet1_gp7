import json
from datetime import datetime
client = ""
import mimimoise
identifiant = ""
mot_de_passe = ""
def importation_1():
    for identifant in mimimoise:
        identifant = identifant in mimimoise
def importation_2():
    for mot_de_passe in mimimoise:
        mot_de_passe = mot_de_passe in mimimoise
        
# Chargement des données clients
def charger_clients(fichier="clients.json"):
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

# Sauvegarde des données clients
def sauvegarder_clients(clients, fichier="clients.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(clients, f, indent=4, ensure_ascii=False)

# Authentification
def authentifier(clients):
    while True:
        id = input("\nEntrez votre identifiant client : ")
        mdp = input("Entrez votre mot de passe : ")
        
        if id == identifiant and mdp == mot_de_passe:
            print(f"\nBonjour M. ou Mme {identifiant}.")
            menu_operations()
        else:
            print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")

# Consultation du solde
def consulter_solde(client):
    print(f"\nVotre solde est de {client['solde']:.2f} €.")

# Retrait d'argent
def retirer_argent(client):
    montant = float(input("Montant à retirer : "))
    if montant <= client["solde"]:
        client["solde"] -= montant
        client["retraits"].append({
            "montant": montant,
            "date": datetime.now().strftime("%d/%m/%Y")
        })
        print(f"Retrait effectué. Nouveau solde : {client['solde']:.2f} €.")
    else:
        print("Fonds insuffisants.")

# Dépôt d'argent
def deposer_argent(client):
    montant = float(input("Montant à déposer : "))
    client["solde"] += montant
    client["depots"].append({
        "montant": montant,
        "date": datetime.now().strftime("%d/%m/%Y")
    })
    print(f"Dépôt effectué. Nouveau solde : {client['solde']:.2f} €.")

# Affichage de l'historique
def afficher_historique(client):
    print("\n--- Historique des dépôts ---")
    for d in client["depots"]:
        print(f"+ {d['montant']} € le {d['date']}")
    print("\n--- Historique des retraits ---")
    for r in client["retraits"]:
        print(f"- {r['montant']} € le {r['date']}")

# Menu principal
def menu_operations(identifiant, clients):
    client = clients[identifiant]

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1 - Consulter votre solde")
        print("2 - Retirer de l'argent")
        print("3 - Déposer de l'argent")
        print("4 - Voir l'historique")
        print("5 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            consulter_solde(client)
        elif choix == "2":
            retirer_argent(client)
        elif choix == "3":
            deposer_argent(client)
        elif choix == "4":
            afficher_historique(client)
        elif choix == "5":
            print("Merci d'avoir utilisé AKBank. À bientôt !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

    sauvegarder_clients(clients)

# Programme principal
def main():
    print("Bienvenue sur AKBank")
    clients = charger_clients()
    identifiant = authentifier(clients)
    menu_operations(identifiant, clients)

# Lancement du programme
if __name__ == "__main__":
    main()
