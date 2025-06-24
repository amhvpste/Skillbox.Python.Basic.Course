import time
import functools
from collections.abc import Callable  # ✅ правильний Callable

def timer(func: Callable) -> Callable:
    """Decorator that measures the execution time of a function."""
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timer
def example_function(n: int) -> int:
    """Example function that simulates a time-consuming task."""
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == "__main__":
    result = example_function(1000000)
    print(f"Result: {result}")  

    # ✅ Використання декоратора для лямбда-функції
    my_sum = squares_sum = timer(lambda x, y: x + y)
    print(my_sum(5, 10))         # Output: 15
    print(squares_sum(5, 10))    # Output: 15
