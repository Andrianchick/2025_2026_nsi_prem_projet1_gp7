print("Bienvenue sur AKBank")

# Demande des identifiants
var_id = input("Entrez votre identifiant : ")
var_pin = input("Entrez votre mot de passe : ")

# Identifiants enregistrés
id = "Ana"
pin = "123"
solde = 1000  # Solde initial

# Vérification
if var_id == id and var_pin == pin:
    print(f"\nBonjour M. ou Mme {id}.")
    print("Tapez 1 pour consulter votre solde.")
    print("Tapez 2 pour retirer de l'argent.")
    print("Tapez 3 pour déposer de l'argent.")
    
    con = input("Votre choix : ")

    if con == "1":
        print(f"Votre solde est de {solde} €.")

    elif con == "2":
        retr = float(input("Tapez le montant que vous voulez retirer : "))
        if retr <= solde:
            solde -= retr
            print(f"Retrait effectué. Nouveau solde : {solde} €.")
        else:
            print("Fonds insuffisants pour effectuer ce retrait.")

    elif con == "3":
        dep = float(input("Tapez le montant que vous voulez déposer : "))
        solde += dep
        print(f"Dépôt effectué. Nouveau solde : {solde} €.")

    else:
        print("Option invalide. Veuillez recommencer.")

else:
    print("Votre identifiant ou mot de passe est invalide. Réessayez.")
karochi dobav mne v kod chto bi vse peremenie nazivalis ponyatno a tak je vosvrachai k nhachalu esli parol i id ne pravelnie bes neobhodimosti 
perewaspuskat kod pri kajdoi is treh funktsii predlaval chto vi eche hotite sdelat naprimer cnat dengi i poloji bew neobhodimosti 

