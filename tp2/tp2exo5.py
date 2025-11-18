chiffre = int(input("entre un nombre:"))
if chiffre == 0:
    print("votre nombre c'est 0 et c'est pair")
elif chiffre %2 ==0 and chiffre >0 :
    print("votre chiffre est positif et pair")
elif chiffre > 0 :
    print ("votre chiffre est impaire et positif")
elif chiffre < 0 and chiffre%2==0:
    print ("votre chiffre est negatif et pair")
else :
    print("votre chiffre est negatif et impair")

