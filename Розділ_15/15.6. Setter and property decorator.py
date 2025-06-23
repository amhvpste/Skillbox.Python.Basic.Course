class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
    def __str__(self) -> str:
        return f"Person(name={self._name}, age={self._age})"  
    
tom = Person("Tom", 25)
print(tom)

print(tom.age)      # Використання @property
tom.age = 30        # Використання @age.setter
print(tom.age)

print(tom.name)     # Використання @property
tom.name = "Tommy"  # Використання @name.setter
print(tom.name)
