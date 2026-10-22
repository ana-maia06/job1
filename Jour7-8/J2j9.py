def nombres():
    resultat = []

    for i in range(0,31,2):
        resultat.append(i)

    resultat.append("")

    for i in range(0,31,3):
        resultat.append(i)

    return resultat

for nombre in nombres():
    print(nombre)


