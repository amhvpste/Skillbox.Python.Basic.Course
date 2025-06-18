class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'Так' if self.has_tail else 'Ніт'
        return 'Скільки ніг: {}, хвіст присутній - {}'.format(self.legs, tail)
    def walk(self):
        print('гуляє')


class Cat(Pet):
    def sound(self):
        print('Мяу')


class Dog(Pet):
    
    def sound(self):
        print('Гав')

class Frog(Pet):
    has_tail = False
    def sound(self):
        print('Ква')

# Перевірка:
cat = Cat()
dog = Dog()
frog =Frog()

print(cat)     # Скільки ніг: 4, хвіст присутній - Так
cat.sound()    # Мяу

print(dog)     # Скільки ніг: 4, хвіст присутній - Так
dog.sound()    # Гав

print(frog)     # Скільки ніг: 4, хвіст присутній - Так
frog.sound()    # Гав

cat.walk
dog.walk
frog.walk