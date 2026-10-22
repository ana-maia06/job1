def fonction(nombre):
    if nombre > 0:
        resultat = "positif"
        return resultat

    elif nombre < 0:
        resultat = "negatif"
        return resultat 

    else:
        resultat = "zero"
        return resultat

print(fonction(0))
print(fonction(-8))
