n1 = 3
n2 = 5

for i in range(1, 101):
    if i % n1 == 0 and i % n2 == 0:
        print("FizzBuzz")
    elif i % n1 == 0:
        print("Fizz")
    elif i % n2 == 0:
        print("Buzz")
    else:
        print(i)
