try:
    with open('numbers.txt', 'r') as numbers_file:
        for i_line in numbers_file:
            print(i_line, end='')  # Просто друк

    num_count = 0
    num_sum = 0

    with open('numbers.txt', 'r') as numbers_file:
        for i_line in numbers_file:
            line = i_line.strip()
            if line:  # Якщо рядок не порожній
                num_count += 1
                num_sum += int(line)

    print('sum', num_sum / num_count)

except FileNotFoundError:
    print('Error: file not found')
except ValueError as e:
    print(f'Error: invalid number in file → {e}')
