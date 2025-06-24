class Date:
    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self._day = day
        self._month = month
        self._year = year

    def __str__(self) -> str:
        return f"Date(day={self._day}, month={self._month}, year={self._year})"

    @classmethod
    def in_date_valid(cls, data: str) -> bool:
        try:
            dmy_list = list(map(int, data.replace(' ', '').split(',')))
            if len(dmy_list) != 3:
                return False
            day, month, year = dmy_list
            return 1 <= day <= 31 and 1 <= month <= 12 and year >= 0
        except ValueError:
            return False

    @classmethod
    def from_string(cls, data: str) -> 'Date':
        if cls.in_date_valid(data):
            day, month, year = map(int, data.replace(' ', '').split(','))
            return cls(day, month, year)
        else:
            raise ValueError("Invalid date format or values")

# Приклад використання
my_date = Date.from_string("15, 8, 2023")
print(my_date)
