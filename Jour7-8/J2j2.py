def nombres():
    i = 0

    for i in range(0, 21, 2):
        print(i)

nombres()


def nombres():
    resultat = []

    for i in range(0, 21, 2):
        resultat.append(i)

    return resultat

for nombre in nombres():
    print(nombre)


