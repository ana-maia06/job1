def nombres():
    N = 1
    resultat = []

    while N < 13:
        resultat.append(N)
        N = N + 1

    return resultat

for nombre in nombres():
    print(nombre)