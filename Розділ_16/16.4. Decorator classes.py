import functools
from datetime import datetime

def createtime(cls):
    """Декоратор класу, що додає час створення екземпляра."""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        instance._creation_time = datetime.now()
        print(f"Instance of {cls.__name__} created at {instance._creation_time}")
        return instance
    return wrapper

@createtime
class Function:
    def __init__(self, max_num: int) -> None:
        self._max_num = max_num

    def squares_sum(self) -> int:
        result = 0
        for _ in range(101):
            result += sum(i_num ** 2 for i_num in range(self._max_num))
        return result

    def cubes_sum(self, number: int) -> int:
        result = 0
        for _ in range(number + 1):
            result += sum(i_num ** 3 for i_num in range(self._max_num))
        return result

# Приклади використання:
my_function_1 = Function(max_num=1000)
print("squares_sum:", my_function_1.squares_sum())

my_function_2 = Function(max_num=2000)
print("cubes_sum:", my_function_2.cubes_sum(50))
