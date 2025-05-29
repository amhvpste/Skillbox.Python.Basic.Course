# user_name = input('Введіть ім\'я користувача: ')
# file_name = input('Введіть назву файлу: ')
#
# path = 'C/{user}/docs/folder/{new_file}.txt'.format(user=user_name, new_file=file_name)
# print('Шлях до файлу:', path)
#
# if not path.endswith('.txt') :
#     print('Помилка розширення файлу')
# elif not path.endswith('C:/'):
#     print('Помилка, не вірно вказаний диск')
# else:
#     print('Шлях до фалу',path)
#

word_list = []

for i_num in range(3):
    print('Введіть', i_num+1, 'слово', end=' ')
    word = input().lower()
    word_list.append(word)

text = input('введіть текст: ').lower().split()

print('\nПідрахунок слів в тексті')
for index in range(3):
    print(word_list[index], ':', text.count(word_list[index]))


