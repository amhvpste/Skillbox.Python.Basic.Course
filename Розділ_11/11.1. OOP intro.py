user_name = input('Як вас звати? ')
print('Оберіть 1, чи 2')
response = input('Оберіть 1, чи 2: ')

if response == '1':
    try:
        with open('chat.txt', 'r', encoding='utf-8') as file:
            messages = file.readlines()
            print(''.join(messages))
    except FileNotFoundError:
        print('Поки тут нічого немає.')

elif response == '2':
    new_message = input('Введіть повідомлення: ')
    with open('chat.txt', 'a', encoding='utf-8') as file:
        file.write(f'{user_name}: {new_message}\n')

else:
    print('Вибрано неправильний варіант. Спробуйте ще раз.')
