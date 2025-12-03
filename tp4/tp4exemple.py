jour=['lundi','mardi','mercredi', 1800,20.357,'jeudi','vendredi']
print(jour)
print(jour[2])
print(jour[4])
print(jour[0])
print((jour[-4]),":affiche le chiffre avec la postion -4 en fonction du 0")


print(len(jour),":affiche le nombre d'élement dans la liste")

del(jour[3])
print((jour),":sans le jour numero 3 donc 1800")

jour.remove(20.357)
print((jour),":sans le 20.357")

jour.append('samedi')
print((jour),"le samedi ce rajoute dans la liste")

print(jour.index('samedi'),'affiche la position de samedi dans la liste')

jour.reverse()
print((jour),"affiche la liste en inverse")

jour.sort()
print((jour),"affiche la liste de maniere ranger en fonction de l'alphabet")

