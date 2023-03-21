a = int(input("Введите число: ")) # целое, от 100 до 999, делится на 2 и 3 одновременно

if type(a) is not float:
    if 100 <= a <= 999:
        if a % 2 == 0:
            if a % 3 ==0:
                print("Да")

if type(a) is int and 100 <= a <= 999 and a % 2 == 0 and a % 3 ==0:
    print("Да")