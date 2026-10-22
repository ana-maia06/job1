L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(9):
    L[i] = int(L[i] + 0.5)

for i in range(9):
    for j in range(i + 1, 9):
        if L[i] > L[j]:
            temporaire = L[i]
            L[i] = L[j]
            L[j] = temporaire

print(L)


def list():
    for i in range(9):
        L[i] = int(L[i] + 0.5)

    for i in range(9):
        for j in range(i + 1, 9):
            if L[i] > L[j]:
                temporaire = L[i]
                L[i] = L[j]
                L[j] = temporaire

list()