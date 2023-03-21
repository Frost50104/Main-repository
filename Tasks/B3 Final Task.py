num = int(input("Введите число: "))

answer5 = 0
answer7 = 0
answer9 = 0

while num > 0:
    if num % 10 == 5:
        answer5 += 1
    elif num % 10 == 7:
        answer7 += 1
    elif num % 10 == 9:
        answer9 += 1
    num = num // 10

print("5:", answer5)
print("7:", answer7)
print("9:", answer9)
