print("Bienvenue sur AKBank")

# Identifiants enregistrés
identifiant_enregistre = "Ana"
mot_de_passe_enregistre = "123"
solde_compte = 1000.0  # Solde initial

# Authentification
while True:
    identifiant_utilisateur = input("\nEntrez votre identifiant : ")
    mot_de_passe_utilisateur = input("Entrez votre mot de passe : ")

    if identifiant_utilisateur == identifiant_enregistre and mot_de_passe_utilisateur == mot_de_passe_enregistre:
        print(f"\nBonjour M. ou Mme {identifiant_enregistre}.")
        def menu_operations() :
            global solde_compte
        break
    else:
        print("\nIdentifiant ou mot de passe incorrect. Veuillez réessayer.")

# Fonction principale
def menu_operations():
    
    while True :
        print("\nQue souhaitez-vous faire ? :"
              "\n1 - Consulter votre solde"
              "\n2 - Retirer de l'argent"
              "\n3 - Déposer de l'argent"
              "\n4 - Quitter")
        
        choix_utilisateur = input("\nQue souhaitez-vous faire ? :"
                                  "\n1 - Consulter votre solde"
                                  "\n2 - Retirer de l'argent"
                                  "\n3 - Déposer de l'argent"
                                  "\n4 - Quitter"
                                  "\n\nVotre choix : ")
        
        if choix_utilisateur == "1":
            
            print(f"\nVotre solde est de {solde_compte:.2f} €.\n")
            
            input(f"\nVotre solde est de {solde_compte:.2f} €.\n\n"
                  "Appuyez sur sur une touche pour revenir au menu principal.")

        elif choix_utilisateur == "2":
            montant_retrait = float(input("Saisissez le montant à retirer : "))
            
            if montant_retrait <= solde_compte:
                solde_compte -= montant_retrait
                
                print("\nRetrait effectué.\n"
                  f"Votre solde est de {solde_compte:.2f} €.")
                
                input("\nRetrait effectué.\n"
                  f"Votre solde est de {solde_compte:.2f} €.\n\n"
                  "Appuyez sur une touche pour revenir au menu principal.")
                
            else:
                print("\nFonds insuffisants pour effectuer ce retrait.")

        elif choix_utilisateur == "3":
            montant_depot = float(input("Saisissez le montant à déposer : "))
            solde_compte += montant_depot
            
            print("\nDépôt effectué.\n"
                  f"Votre solde est de {solde_compte:.2f} €.")
            
            input("\nDépôt effectué.\n"
                  f"Votre solde est de {solde_compte:.2f} €.\n\n"
                  "Appuyez sur touche pour revenir au menu principal.")

        elif choix_utilisateur == "4":
            print("Merci d'avoir utilisé AKBank. À bientôt !")
            break

        else:
            input("Option invalide.\n"
                  "Appuyez sur une touche pour réessayer.")
            
