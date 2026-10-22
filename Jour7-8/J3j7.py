def alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

    for i in range(1, 29):
        print(alphabet[0:2 * i - 1])

alphabet()