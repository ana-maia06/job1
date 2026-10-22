def fonction(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("Nombre invalide")

fonction(4)
fonction(7)
fonction(-2)
fonction(3.5)
    

