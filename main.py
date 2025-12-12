import json
import time
from datetime import datetime

# ==========================
# Chargement des données clients
# ==========================
def charger_clients(fichier="clients.json"):
    with open(fichier, "r", encoding="utf-8") as f:
        return json.load(f)

# ==========================
# Sauvegarde des données clients
# ==========================
def sauvegarder_clients(clients, fichier="clients.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(clients, f, indent=4, ensure_ascii=False)

# ==========================
# Authentification
# ==========================
def authentifier(clients):
    while True:
        print("\n=== Authentification ===")
        id_saisi = input("Identifiant client : ").strip()
        mdp_saisi = input("Mot de passe : ").strip()

        # Vérification dans le dictionnaire
        for numero, client in clients.items():
            ident = str(client.get("identifiant", "")).strip()
            mdp_client = str(client.get("mot_de_passe", "")).strip()

            if id_saisi == ident and mdp_saisi == mdp_client:
                print(f"\nBonjour M./Mme {ident}.")
                return numero  # retourne la clé du client

        print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")

# ==========================
# Consultation du solde
# ==========================
def consulter_solde(client):
    print("\n=== Consultation du solde ===")
    print(f"Votre solde est de {client['solde']:.2f} €.")
    time.sleep(5)

# ==========================
# Retrait d'argent avec choix de billets
# ==========================
def retirer_argent(client):
    print("\n=== Retrait d'argent ===")
    montant = input("Combien souhaitez-vous retirer (€) ? ").strip()

    if not montant.isdigit() or int(montant) <= 0:
        print("Montant invalide.")
        time.sleep(2)
        return retirer_argent(client)

    montant = int(montant)

    # Vérification du solde
    if montant > client["solde"]:
        print("Fonds insuffisants.")
        time.sleep(2)
        return retirer_argent(client)

    # Étape 2 : proposer la répartition en billets
    while True:  # boucle pour recommencer si erreur
        print("\nRépartissez votre retrait en billets disponibles :")
        coupures = [5, 10, 20, 50, 100]
        coupure = input("Quelle coupure voulez-vous utiliser (5, 10, 20, 50, 100) ? ").strip()
            
        if not coupure.isdigit() or int(coupure) not in coupures:
            print("Coupure invalide.")
            time.sleep(2)
            continue

        coupure = int(coupure)

        # Vérification que le montant est divisible par la coupure
        if montant % coupure != 0:
            print(f"Impossible de retirer {montant} € uniquement en billets de {coupure} €.")
            time.sleep(2)
            continue 

        nb_billets = montant // coupure

        # Mise à jour du solde et historique
        client["solde"] -= montant
        client["retraits"].append({
            "montant": montant,
            "date": datetime.now().strftime("%d/%m/%Y")
        })

        print(f"\nRetrait de {montant} € effectué.")
        print("Voilà :")
        print(f"  - {nb_billets} billets de {coupure} €")
        print(f"Nouveau solde : {client['solde']:.2f} €.")
        time.sleep(5)
        break

# ==========================
# Dépôt d'argent
# ==========================
def deposer_argent(client):
    print("\n=== Dépôt d'argent ===")
    montant = input("Montant à déposer (€) : ").strip()
    if not montant.replace(".", "", 1).isdigit():
        print("Montant invalide.")
        time.sleep(5)
        return

    montant = float(montant)
    client["solde"] += montant
    client["depots"].append({
        "montant": montant,
        "date": datetime.now().strftime("%d/%m/%Y")
    })
    print(f"Dépôt effectué. Nouveau solde : {client['solde']:.2f} €.")
    time.sleep(5)

# ==========================
# Affichage de l'historique
# ==========================
def afficher_historique(client):
    print("\n=== Historique des opérations ===")
    print("\n--- Dépôts ---")
    for d in client["depots"]:
        print(f"+ {d['montant']} € le {d['date']}")
    print("\n--- Retraits ---")
    for r in client["retraits"]:
        print(f"- {r['montant']} € le {r['date']} | Détails: {r.get('details',{})}")
    time.sleep(5)

# ==========================
# Menu principal
# ==========================
def menu_operations(identifiant, clients):
    client = clients[identifiant]

    while True:
        print("\n=== Menu principal ===")
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
            time.sleep(5)

    sauvegarder_clients(clients)

# ==========================
# Programme principal
# ==========================
def main():
    print("=== Bienvenue sur AKBank ===")
    clients = charger_clients()
    identifiant = authentifier(clients)
    menu_operations(identifiant, clients)

# ==========================
# Lancement du programme
# ==========================
if __name__ == "__main__":
    main()