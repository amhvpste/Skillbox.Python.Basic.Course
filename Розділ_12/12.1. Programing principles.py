class Water:
    def __str__(self):
        return 'Вода'
    
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Mud()

class Air:
    def __str__(self):
        return 'Повітря'
    
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dust()

class Fire:
    def __str__(self):
        return 'Вогонь'

class Earth:
    def __str__(self):
        return 'Земля'

class Storm:
    def __str__(self):
        return "Шторм"

class Vapor:
    def __str__(self):
        return "Пар"

class Mud:
    def __str__(self):
        return "Грязь"

class Dust:
    def __str__(self):
        return "Пил"

# Тест
water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(air + water)     # Шторм
print(water + fire)    # Пар
print(water + earth)   # Грязь
print(air + earth)     # Пил
