temperature = int(input("Введите температуру: "))
isRain = (input("Есть дождь? "))
if isRain == "Да":
    isRain = True
else:
    isRain = False
if isRain is True:
    isRain2 = (input("Осадки сильные? "))
    if isRain2 == "Да":
        isRain2 = True
    else:
        isRain2 = False
if 20 < temperature < 30:
    if isRain is True:
        print("Футболку, шорты и дождевик")
    else:
        print("Футболку и шорты")
else:
    if temperature <= 0:
        print("Пуховик")
    else:
        if isRain is False:
            print("Пальто")
        else:
            if isRain2 is True:
                print("Пальто, резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")






