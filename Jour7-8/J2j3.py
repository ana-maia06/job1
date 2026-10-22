def nombres():
    resultat = []

    for i in range(1, 21):
        resultat.append(i ** 2)

    return resultat

for nombre in nombres():
    print(nombre)