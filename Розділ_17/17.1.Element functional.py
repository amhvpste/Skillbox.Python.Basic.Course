from typing import Callable
import functools

def decorator(func: Callable) -> Callable:
    """Decorator that prints the function name and its arguments."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def decorated_decorator(text: str, num: int) -> None:
    print('Print', text, num)

# Викликаємо функцію з аргументами
decorated_decorator("100 грн", 200)
