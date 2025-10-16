print("Bienvenue sur AKBank")

# Identifiants enregistrés
identifiant_enregistre = "Ana"
mot_de_passe_enregistre = "123"
solde_compte = 1000.0  # Solde initial

# Fonction principale
def menu_operations():
    global solde_compte 

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1 - Consulter votre solde")
        print("2 - Retirer de l'argent")
        print("3 - Déposer de l'argent")
        print("4 - Quitter")

        choix_utilisateur = input("Votre choix : ")

        if choix_utilisateur == "1":
            print(f"Votre solde est de {solde_compte:.2f} €.")

        elif choix_utilisateur == "2":
            montant_retrait = float(input("Montant à retirer : "))
            if montant_retrait <= solde_compte:
                solde_compte -= montant_retrait
                print(f"Retrait effectué. Nouveau solde : {solde_compte:.2f} €.")
            else:
                print("Fonds insuffisants pour effectuer ce retrait.")

        elif choix_utilisateur == "3":
            montant_depot = float(input("Montant à déposer : "))
            solde_compte += montant_depot
            print(f"Dépôt effectué. Nouveau solde : {solde_compte:.2f} €.")

        elif choix_utilisateur == "4":
            print("Merci d'avoir utilisé AKBank. À bientôt !")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

# Authentification
while True:
    identifiant_utilisateur = input("\nEntrez votre identifiant : ")
    mot_de_passe_utilisateur = input("Entrez votre mot de passe : ")

    if identifiant_utilisateur == identifiant_enregistre and mot_de_passe_utilisateur == mot_de_passe_enregistre:
        print(f"\nBonjour M. ou Mme {identifiant_enregistre}.")
        menu_operations()
        break
    else:
        print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")
