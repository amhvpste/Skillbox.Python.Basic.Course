class Water:
    """Клас, що представляє елемент 'Вода'. Може взаємодіяти з іншими елементами."""

    def __str__(self):
        """Повертає рядкове представлення елемента."""
        return 'Вода'

    def __add__(self, other):
        """
        Реалізує взаємодію Води з іншими елементами.
        - Повітря → Шторм
        - Вогонь → Пар
        - Земля → Грязь
        """
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None  # Якщо поєднання не визначено


class Air:
    """Клас, що представляє елемент 'Повітря'."""

    def __str__(self):
        return 'Повітря'

    def __add__(self, other):
        """
        Реалізує взаємодію Повітря з іншими елементами.
        - Вода → Шторм
        - Вогонь → Пар
        - Земля → Пил
        """
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None  # Якщо поєднання не визначено


class Fire:
    """Клас, що представляє елемент 'Вогонь'."""

    def __str__(self):
        return 'Вогонь'


class Earth:
    """Клас, що представляє елемент 'Земля'."""

    def __str__(self):
        return 'Земля'


class Storm:
    """Результат поєднання Води і Повітря — Шторм."""

    def __str__(self):
        return "Шторм"


class Vapor:
    """Результат поєднання Вогню та Води/Повітря — Пар."""

    def __str__(self):
        return "Пар"


class Mud:
    """Результат поєднання Води та Землі — Грязь."""

    def __str__(self):
        return "Грязь"


class Dust:
    """Результат поєднання Повітря та Землі — Пил."""

    def __str__(self):
        return "Пил"


# Тестування взаємодії елементів
water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(air + water)     # Шторм
print(water + fire)    # Пар
print(water + earth)   # Грязь
print(air + earth)     # Пил
