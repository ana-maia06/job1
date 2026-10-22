def nombres():
    n = int(input("Insérez le nombre:"))

    if n % 2 == 0:
        print("Le nombre", n, "est pair")
    else:
        print("Le nombre", n, "est impair")

nombres()