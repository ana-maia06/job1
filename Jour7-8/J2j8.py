def tours():
    resultat = []

    for i in range(1, 13):
        resultat.append("tour " + str(i) + ":" + str(2 * i))

    return resultat

for ligne in tours():
    print(ligne)