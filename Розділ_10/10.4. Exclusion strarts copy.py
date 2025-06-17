sym_num = 0
line_count = 0

try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1

            if length < 3:
                raise Exception(f'Імʼя в рядку {line_count} має менше трьох символів')

            sym_num += length

except FileNotFoundError:
    print('no file')

except Exception as e:
    print('Error:', e)

finally:
    print('sum num', sym_num)
