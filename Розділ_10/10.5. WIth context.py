line_count = 0
sym_num = 0

try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            length = len(i_line)
            if i_line.endswith('\n'):
                length -= 1  # або length = len(i_line.strip())
            if length < 3:
                raise Exception(f'Імʼя в рядку {line_count} має менше трьох символів')
            sym_num += length
except FileNotFoundError:
    print('no file')
finally:
    print('sum num', sym_num)