def fonction(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")

    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")

    elif type == "légume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")

fonction("fruits", "hiver")
fonction("fruits", "été")
fonction("légume", "hiver")
fonction("légume", "été")