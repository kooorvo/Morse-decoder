# <--- Point d'entrée --->
from encoder import encode
from decoder import decode

menu = input(f"Voulez-vous (entrer le numéro): \n"
"1. Encoder \n"
"2. Décoder\n")

if menu == "1":
    print(encode())
elif menu == "2":
    print(decode())
else:
    print("Ce choix n'existe pas")