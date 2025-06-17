# nice_list = [[1,2],[3,4],[5,6]],[[10,11,12],[13,14,15],[16,17,18]]
# output = [ digit for each_list in nice_list for each_list2 in each_list for digit in each_list2]
# print(output)
alphabet = 'абвгґдеєжзииїйклмнопрстуфхцчшщьюя'

input_str = input('Вкажіть речення: ')
shift = int(input('Вкажіть здвиг: '))

result = ''

for char in input_str.lower():
    if char in alphabet:
        idx = alphabet.index(char)
        new_idx = (idx + shift) % len(alphabet)
        result += alphabet[new_idx]
    else:
        result += char  # залишаємо символ без змін

print('Зашифроване речення:', result)
