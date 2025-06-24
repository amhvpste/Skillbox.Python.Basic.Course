from typing import Callable
import functools

class CountClass:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self._func = func
        self._count = 0

    def __call__(self, *args, **kwargs):
        self._count += 1
        print(f"Function '{self._func.__name__}' called {self._count} times")
        return self._func(*args, **kwargs)

@CountClass
def say_hello():
    print("Hello, world!")

# Приклад виклику
say_hello()
say_hello()
