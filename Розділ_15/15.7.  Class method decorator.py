class Petr:
    def __init__(self) -> None:
        self._name = "Petr"
        self._age = 30
    def __str__(self) -> str:
        return f"Person(name={self._name}, age={self._age})"
    @classmethod
    def create_from_string(cls, data: str) -> 'Petr':
        name, age = data.split(',')
        instance = cls()
        instance._name = name.strip()
        instance._age = int(age.strip())
        return instance
    # Приклад використання
        petr = Petr.create_from_string("Petr, 30")
        print(petr)
        print(petr._name)
        print(petr._age)
        petr = Petr.create_from_string("Petr, 30")
        print(petr)
        print(petr._name)   