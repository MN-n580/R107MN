jour=input('entre le nombre de jour n-1:')
heure=input('entre le nombre heure:')
minut=input('entre nombre minute:')
minut=int(minut)
jour=int(jour)
heure=int(heure)
nombre_minute=((jour*24+heure)*60)+minut
print(nombre_minute)
