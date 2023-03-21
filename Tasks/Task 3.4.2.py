x = int(input("Введите год: "))
if (x % 400 == 0) or ((x % 100 != 0) and (x % 4 == 0)):
    print("Високосный")
else:
    print("Обычный")

