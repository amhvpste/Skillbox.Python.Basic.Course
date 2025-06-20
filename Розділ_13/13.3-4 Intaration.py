import random

class RandomNumber:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter
        else:
            raise StopIteration("Досягнуто ліміт генерації чисел")
        
my_iter = RandomNumber(limit=3)

for number in my_iter:
    print(number)

class Fibonacci:
    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        self.counter += 1
        value = self.cur_val
        self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val
        return value

# Використання
fib_iterator = Fibonacci(10)
for i_value in fib_iterator:
    print(i_value)
