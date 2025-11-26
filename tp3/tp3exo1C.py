inf10 = 0
inf15 = 0
sup15 = 0
for i in range (10):
    CU = int(input("choisi un nombre entre 0 et 20 : "))
    while CU < 0 or CU > 20:
        CU = int(input("tu dois choisir entre 0 et 20 ! : "))

    if CU < 10 :
        inf10 += 1
    elif CU >= 10 and CU <= 15 :
        inf15 += 1
    else:
        sup15 += 1
print (" Le nombre de valeurs inférieur strictement à 10:", inf10 )
print (" Le nombre de valeurs comprises entre 10 et 15:", inf15 )
print (" Le nombre de valeurs superieurs strictement à 15:", sup15 )
