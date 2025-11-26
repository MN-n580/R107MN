import random
nombre = random.randint (0,100)
nbrt = 1
CU = int(input("choisi un nombre :"))

while CU != nombre:
    nbrt += 1
    if CU > nombre :
        print ("c'est moins")
    if CU < nombre:
        print("c'est plus")
    CU = int(input(" recommence :"))

print ("vous avez trouvez en ", nbrt, "coup, le chiffre était bien",nombre)