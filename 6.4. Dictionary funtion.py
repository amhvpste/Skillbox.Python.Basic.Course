import random

numbers_list = [random.randint(1, 100) for _ in range(10)]
# new_list = []

# for i_num in numbers_list:
#     if i_num not in new_list:
#         new_list.append(i_num)

# print("Початковий список чисел:", numbers_list)
# print("Список без повторів:", new_list)

unique = set(numbers_list)
print("Унікальні числа з використанням set:", unique)