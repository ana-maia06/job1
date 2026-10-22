def mots():
    n1 = 3
    n2 = 5
    resultat = []

    for i in range(1, 101):
        if i % n1 == 0 and i % n2 == 0:
            resultat.append("FizzBuzz")
        elif i % n1 == 0:
            resultat.append("Fizz")
        elif i % n2 == 0:
            resultat.append("Buzz")
        else:
            resultat.append(i)

    return resultat

for nombre in mots():
    print(nombre)
