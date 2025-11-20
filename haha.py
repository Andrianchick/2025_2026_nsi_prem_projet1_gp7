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
    montant_souhaite = input("Combien souhaitez-vous retirer (€) ? ").strip()

    if not montant_souhaite.isdigit() or int(montant_souhaite) <= 0:
        print("Montant invalide.")
        time.sleep(5)
        return

    montant_souhaite = int(montant_souhaite)

    # Vérification du solde
    if montant_souhaite > client["solde"]:
        print("Fonds insuffisants.")
        time.sleep(5)
        return

    # Étape 2 : proposer la répartition en billets
    while True:  # boucle pour recommencer si erreur
        print("\nRépartissez votre retrait en billets disponibles :")
        options = [5, 10, 20, 50, 100]
        repartition = {}
        reste = montant_souhaite

        for billet in reversed(options):  # commencer par les grosses coupures
            nb = input(f"Combien de billets de {billet} € (reste {reste} €) ? ").strip()
            if nb.isdigit():
                nb = int(nb)
                # Vérification immédiate : pas plus que le reste
                if nb * billet > reste:
                    print(f"Vous demandez trop de billets de {billet} € (reste {reste} €).")
                    print("Recommencez la répartition.\n")
                    break  # sortir de la boucle for → recommencer
                repartition[billet] = nb
                reste -= billet * nb
        else:
            # Si la boucle for s'est terminée sans 'break'
            if reste == 0:
                # Mise à jour du solde et historique
                client["solde"] -= montant_souhaite
                client["retraits"].append({
                    "montant": montant_souhaite,
                    "date": datetime.now().strftime("%d/%m/%Y"),
                    "details": repartition
                })

                print(f"\nRetrait de {montant_souhaite} € effectué.")
                print("Répartition des billets :")
                for billet, nb in repartition.items():
                    if nb > 0:
                        print(f"  - {nb} x {billet} €")
                print(f"Nouveau solde : {client['solde']:.2f} €.")
                time.sleep(5)
                return
            else:
                print("\nLa répartition ne correspond pas au montant demandé.")
                print("Recommencez la répartition.\n")

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
