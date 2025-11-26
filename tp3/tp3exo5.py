C1 = int(input("Donnez l’heure de début de la location (un entier):"))
C2 = int(input("Donnez l’heure de fin de la location (un entier) :"))
hmin = C1
hmax = C2
i = 0
stockc1=0

while True :
    if C1 < 0 or C1 > 24 or C2 < C1 or C2 > 24 :
        print ("c'est pas possible")
        C1 = int(input("horaire début:"))
        C2 = int(input("horaire fin:"))
    elif C1 < 7 or C1 > 17:
        stockc1 += +1
        C1 +=1
        print (stockc1, "heure(s) au tarif horaire de 1.0 euro (s) ")
    elif C2 > 7 or C2 < 17:
        print("fsdohfisquhfiush")