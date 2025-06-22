import time

def timer(func):
    started_at = time.time()
    result = func()
    ended_at = time.time()
    run_time = round(ended_at - started_at, 4)
    print(f'Результат: {result}, час виконання: {run_time} секунд')

    return result


def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(1, number + 1):
        result += sum([i_num**2 for i_num in range(10000)])
    return result

my_func = squares_sum
print(f'Function name: {my_func.__name__}')
timer(my_func)