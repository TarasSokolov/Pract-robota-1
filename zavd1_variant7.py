def expression(a, b):
    if a > b:
        x = 5 * a + b
    elif a == b:
        x = -125
    else:
        x = (a - 5) / b
    return x


def pyramid(n):
    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end=" ")

        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()


a = int(input("Введіть a: "))
while a <= 0:
    a = int(input("Введіть a ще раз: "))

b = int(input("Введіть b: "))
while b <= 0:
    b = int(input("Введіть b ще раз: "))

print("X =", expression(a, b))

n = int(input("Введіть N (1..10): "))
while n < 1 or n > 10:
    n = int(input("Введіть N ще раз (1..10): "))

pyramid(n)