class Rectangle:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
    def __str__(self):
        return f'Rectangle : {self.x, self.y, self.a, self.b}'
    def get_area(self):
        return f'Area = {self.a * self.b}'

rect_1 = Rectangle(5, 10, 50, 100)

print(rect_1)
print(rect_1.get_area())

class Customers:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.'

    def corp(self):
        return f'{self.name} {self.surname}. {self.city}.'

costomer_1 = Customers('Иван','Петров','Москва',50)
costomer_2 = Customers('Владимир','Зайцев','Кострома',50)
costomer_3 = Customers('Олеся','Янина','Новосибирск',50)

guest_list = [costomer_1, costomer_2, costomer_3]

for guest in guest_list:
    print(guest.corp())

