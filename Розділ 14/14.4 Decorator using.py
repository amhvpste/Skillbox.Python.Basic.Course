import time

def timer(func):
    def wrapper(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print(f'Результат: {result}, час виконання: {run_time} секунд')
        return result
    return wrapper

@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(1, number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for i_num in range(1, number + 1):
        result += i_num**3
    return result

# Виклики
my_sum_1 = squares_sum()
my_sum_2 = cubes_sum(10000)


from typing import Callable

def loggins(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Функція {func.__name__} викликана з аргументами {args} та {kwargs}, результат: {result}')
        return result  
