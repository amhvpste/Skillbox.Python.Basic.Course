class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'Так' if self.has_tail else 'Ніт'
        return 'Скільки ніг: {}, хвіст присутній - {}'.format(self.legs, tail)
    

class Cat(Pet):
    def sound(self):
        print('Мяу')


class Dog(Pet):
    
    def sound(self):
        print('Гав')


# Перевірка:
cat = Cat()
dog = Dog()

print(cat)     # Скільки ніг: 4, хвіст присутній - Так
cat.sound()    # Мяу

print(dog)     # Скільки ніг: 4, хвіст присутній - Так
dog.sound()    # Гав
