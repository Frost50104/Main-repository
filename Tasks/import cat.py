from cat import Cat

class Dog(Cat):

    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog1 = Dog("Рекс", "мальчик", 2)

print("dog1.get_pet =", dog1.get_pet())

