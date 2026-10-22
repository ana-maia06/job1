def gestion_stock():
    nom = "Spaghetti"
    prix = 1.30
    stock = 100

    nom_depart = nom
    prix_depart = prix
    stock_depart = stock

    stock = stock + 20
    stock = stock - 7
    prix = prix * 1.10

    return nom_depart, prix_depart, stock_depart, nom, prix, stock 

nom_depart, prix_depart, stock_depart, nom, prix, stock = gestion_stock()

print(nom_depart)
print(prix_depart)
print(stock_depart)

print(nom)
print(prix)
print(stock)

    