def tables():
    n = int(input("Inserer nombre:"))

    for i in range(1, n + 1):
        print("Table du", i)
   
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

print(tables())