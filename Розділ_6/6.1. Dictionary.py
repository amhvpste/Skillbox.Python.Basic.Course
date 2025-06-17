# contacts_list = [
#     {"name": "Іван Петренко", "phone": "+380631234567"},
#     {"name": "Олена Коваль", "phone": "+380671112233"},
#     {"name": "Андрій Шевченко", "phone": "+380503334455"},
#     {"name": "Марія Іванова", "phone": "+380931234321"},
#     {"name": "Сергій Бондар", "phone": "+380661112244"}
# ]


# contacts = {
#     "Іван Петренко": "+380631234567",
#     "Олена Коваль": "+380671112233",
#     "Андрій Шевченко": "+380503334455",
#     "Марія Іванова": "+380931234321",
#     "Сергій Бондар": "+380661112244"
# }

# name = input("Введіть ім'я контакту: ")
# if name in contacts:
#     print(f"Телефонний номер {name}: {contacts[name]}")
# else:
#     print(f"Контакт {name} не знайдено.")

# print("Список контактів:", contacts)
students_str = input('Введіть дані студента через пробіл\n(ім\'я, прізвище, вік, група, оцінка): ')

student_info = students_str.split()
student = dict()
student['імя'] = student_info[0]
student['прізвище'] = student_info[1]
student['вік'] = int(student_info[2])
student['група'] = student_info[3]
student['оцінка'] = [float(student_info[4])]  # список оцінок

# Наприклад, додаємо ще одну оцінку
i_grade = input("Введіть ще одну оцінку (або залиште порожнім): ")
if i_grade:
    student['оцінка'].append(float(i_grade))

# Виводимо інформацію
for key in student:
    print(f'{key}: {student[key]}')
