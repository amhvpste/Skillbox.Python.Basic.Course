text = input ('В цьому файлі: ')
words_list = text.split()

print(words_list)

new_text = '---'.join(words_list)

print(new_text)
