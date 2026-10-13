import random
argent = random.randint(-2500, 10000)
pin = int(input("Entrez votre PIN :"))
if pin == 1234:
    print(f"Vous avez {argent}€ sur votre compte")
else:
    print("PIN incorrect")
