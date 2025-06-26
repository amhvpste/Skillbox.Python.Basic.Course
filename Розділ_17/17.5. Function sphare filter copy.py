from typing import List

my_name: List[int] = [1, 2, 3, 4, 5]  
other_name: List[int] = [6, 7, 8, 9, 10]

# Сума елементів попарно
result: List[int] = list(map(lambda x, y: x + y, my_name, other_name))
print(result)  # Output: [7, 9, 11, 13, 15]

# Фільтруємо лише парні числа
result_even = filter(lambda x: x % 2 == 0, result)
print(list(result_even))  # Output: []
