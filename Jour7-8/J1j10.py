def calcul_gain():
    capital = 10000
    taux = 5

    gain1 = capital * taux / 100

    capital = capital + 5000
    taux = taux + 2
    gain2 = capital * taux / 100

    retrait = capital * 10 / 100
    capital = capital - retrait
    taux = taux - 1
    gain3 = capital * taux / 100

    return gain1, gain2, capital, gain3

gain1, gain2, capital, gain3 = calcul_gain()

print(gain1)
print(gain2)
print(capital)
print(gain3)