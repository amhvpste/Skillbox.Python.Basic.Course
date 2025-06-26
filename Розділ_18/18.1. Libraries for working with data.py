from collections import Counter

def can_be_poly(val: str) -> bool:
    # Рахуємо кількість непарних літер
    odd_counts = sum(1 for count in Counter(val).values() if count % 2)
    return odd_counts <= 1  # Для паліндрому допускається максимум одна непарна літера

print(can_be_poly('aabbcc'))     # True (усі парні)
print(can_be_poly('aabbccd'))    # True (одна непарна)
print(can_be_poly('aabbccdd'))   # False (дві непарні)
