import random
argent = random.randint(-500, 1694)
pin = int(input("Entrez votre PIN :"))
while pin != 6732:
    print("PIN incorrect. Veuillez reessayer.")
    pin = int(input("Entrez votre PIN :"))
print(f"Vous avez {argent}€ sur votre compte.")
answer = int(input("Voulez vous retirer de l'argent ?(0=Oui/1=Non):"))
if answer==0:
    argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    if argent_a_retirer<=0 or argent_a_retirer > argent:
        print("Montant incorrect")
        argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    elif argent_a_retirer>1000:
        print("Montant superieur au plafond. Le plafond est de 1000€.")
        argent_a_retirer=int(input("Combien d'argent voulez vous retirer?"))
    elif argent_a_retirer%5 !=0:
        print("Ce distributeur ne delivre que des billets. Veuillez choisir un montant multiple du nombre 5.")
    else:
        print
elif answer==1:
    print("Au revoir.")
else:
    print("Veuillez choisir entre 0 et 1")
    answer = int(input("Voulez vous retirer de l'argent ?(0/1):"))
