word = 'Привіт'
result = []

sym_list = list(word)

fist_part = word[:len(word) // 2]
print(fist_part[:: -1])

second_part = word[:len(word) // 2:]
print(second_part[:: -1])

result.extend(fist_part[:: -1]+second_part[:: -1])
