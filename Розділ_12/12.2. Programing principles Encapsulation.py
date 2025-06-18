class Person:
    __count = 0  # private class variable

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.__count += 1

    def __str__(self):
        return "Ім'я: {}\t Вік: {}".format(self.__name, self.__age)

    @staticmethod
    def get_count():
        return Person.__count

    def set_age(self, age):
        if age in range(10, 90):
            self.__age = age
        else:
            raise Exception('Недопустимий вік')

# Створення об’єктів
misha = Person('Misha', 20)
tom = Person("Tom", 23)

# Перевірка кількості
print(Person.get_count())  # Має вивести: 2

# Оновлення віку
new_age = 80
misha.set_age(new_age)

# Перевірка виводу
print(misha)
