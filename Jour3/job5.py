for i in range(2, 1001):
    premier = True

    for j in range(2, i):
        if i % j == 0:
            premier = False

    if premier == True:
        print(i)