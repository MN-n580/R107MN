CU = int(input("choisi un nombre :"))
N = 0
somme = 0

while True:
    N += 1
    somme += N
    if somme > CU :
        break
print (N-1)