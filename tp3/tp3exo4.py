from time import *

CU = int(input("choisi un nombre pour la factorielle:"))
vrai = bool(input("choisi pour la méthode entre True ou riene:"))
i = 0
sommefac=1
stock = CU
if vrai :
    while CU != 0:
        i += 1
        sommefac *= i
        print(sommefac)
        CU = CU - 1
        sleep(0.1)
    print("voici la somme factorielle de ",stock," dans une boucle while")
else :
    for j in range (1, CU+1):
        i += 1
        sommefac *= i
        print(sommefac)
        CU = CU - 1
        sleep(0.1)
    print("voici la somme factorielle de ",stock," dans une boucle FOR")