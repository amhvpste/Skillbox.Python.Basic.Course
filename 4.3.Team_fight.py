import random

squad1 = [random.randint(50,80) for _ in range(10)]
squad2 = [random.randint(30,60) for _ in range(10)]
squad3_condition = [("Загинув" if squad1[i_damage]+squad2[i_damage] > 100
                    else "Живий")
                    for i_damage in range(10)]
print('урон першої команди',squad1)
print('урон другої команди', squad2)
print('Результат',squad3_condition)