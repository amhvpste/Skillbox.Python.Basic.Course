import os
import shutil
import re

# Шлях до папки з файлами (заміни на свою папку)
source_folder = 'C:/dev/skillbox_py/Skillbox.Python.Basic.Course-1'

# Проходимося по всіх файлах у папці
for filename in os.listdir(source_folder):
    # Пропускаємо папки
    if not os.path.isfile(os.path.join(source_folder, filename)):
        continue

    # Патерн: 1.1. Назва.py або 10.4. Назва.py
    match = re.match(r'(\d+)\.(\d+)\.\s*(.+)', filename)
    if match:
        section = match.group(1)  # Розділ
        lesson = match.group(2)   # Урок
        title = match.group(3)    # Назва

        # Назва папки розділу
        section_folder = f'Розділ_{section}'
        section_path = os.path.join(source_folder, section_folder)

        # Створюємо папку, якщо ще не існує
        os.makedirs(section_path, exist_ok=True)

        # Поточний і новий шлях до файлу
        current_file_path = os.path.join(source_folder, filename)
        new_file_path = os.path.join(section_path, filename)

        # Переносимо файл
        shutil.move(current_file_path, new_file_path)
        print(f'Файл {filename} переміщено в {section_folder}/')
    else:
        print(f'Файл {filename} не відповідає шаблону і пропущений.')
