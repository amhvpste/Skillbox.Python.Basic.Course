from collections.abc import Callable
import functools

def counter(func: Callable) -> Callable:
    """Декоратор, що рахує кількість викликів функції."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1  # Змінюємо wrapper.count замість невизначеного count
        res = func(*args, **kwargs)
        print(f'Функція {func.__name__} викликана {wrapper.count} разів')
        return res

    wrapper.count = 0  # Ініціалізуємо лічильник
    return wrapper

@counter
def my_function() -> str:
    """Example function to demonstrate the counter decorator."""
    return "Hello, World!"

my_function()
my_function()
my_function()
