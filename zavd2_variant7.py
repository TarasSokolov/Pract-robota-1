from mod1 import expression
from mod2 import numbers

print("1 - Обчислити вираз")
print("2 - Вивести кожне п'яте число")

choice = int(input("Ваш вибір: "))

if choice == 1:
    a = float(input("Введіть a: "))
    print("y =", expression(a))

elif choice == 2:
    numbers()

else:
    print("Неправильний вибір")