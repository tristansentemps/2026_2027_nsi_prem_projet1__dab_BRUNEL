
# ==========================================
# Simulation d'un distributeur automatique
# ==========================================

# Paramètres du compte
CODE_PIN = "1234"
solde = 500
PLAFOND_RETRAIT = 300

# 1. IDENTIFICATION
tentatives = 0
identifie = False

while tentatives < 3:
    code = input("Veuillez saisir votre code PIN : ")

    if code == CODE_PIN:
        print("\nIdentification réussie ! Bienvenue.")
        identifie = True
        break
    else:
        tentatives += 1
        restantes = 3 - tentatives
        if restantes > 0:
            print(f"Code PIN incorrect. Il vous reste {restantes} tentative(s).")

if not identifie:
    print("Carte bloquée après 3 codes PIN incorrects.")
    print("Le programme va s'arrêter.")

else:
    # 2. MENU PRINCIPAL
    while True:
        print("\n========== DISTRIBUTEUR ==========")
        print("1. Consulter le solde")
        print("2. Retirer de l'argent")
        print("3. Quitter")
        print("==================================")

        choix = input("Votre choix : ")

        if choix == "1":
            # Consultation du solde
            print(f"Votre solde est de {solde} €.")

        elif choix == "2":
            # 3. RETRAIT D'ARGENT
            try:
                montant = int(input("Montant à retirer (en euros) : "))

                if montant <= 0:
                    print("Erreur : le montant doit être un entier positif.")

                elif montant % 10 != 0:
                    print("Erreur : le montant doit être un multiple de 10 €.")

                elif montant > solde:
                    print("Retrait refusé : solde insuffisant.")

                elif montant > PLAFOND_RETRAIT:
                    print(f"Retrait refusé : le plafond est de "
                          f"{PLAFOND_RETRAIT} € par retrait.")

                else:
                    # Mise à jour du solde
                    solde -= montant

                    print(f"Retrait accepté : {montant} €.")

                    # Distribution des billets
                    billets_50 = montant // 50
                    reste = montant % 50

                    billets_20 = reste // 20
                    reste = reste % 20

                    billets_10 = reste // 10

                    print("Voici vos billets :")
                    if billets_50 > 0:
                        print(f"- {billets_50} billet(s) de 50 €")
                    if billets_20 > 0:
                        print(f"- {billets_20} billet(s) de 20 €")
                    if billets_10 > 0:
                        print(f"- {billets_10} billet(s) de 10 €")

                    print(f"Votre nouveau solde est de {solde} €.")

            except ValueError:
                print("Erreur : veuillez saisir un montant entier valide.")

        elif choix == "3":
            print("Merci d'avoir utilisé notre distributeur. Au revoir !")
            break

        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
