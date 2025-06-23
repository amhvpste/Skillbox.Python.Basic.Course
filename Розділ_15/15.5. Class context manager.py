import time

class Timer:
    def __init__(self):
        print('Timer initialized')
        self.start_time = None

    def __enter__(self) -> 'Timer':
        self.start_time = time.time()
        print('Timer started')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        print(f'{elapsed:.4f} seconds elapsed')

# Приклад використання
with Timer() as t1:
    print('Hello, World!')
    val_1 = 100 * 100 * 100000

with Timer() as t2:
    print('Another block')
    val_2 = 100 * 300 * 100000

with Timer() as t3:
    print('One more block')
    val_3 = 200 * 100 * 100000
