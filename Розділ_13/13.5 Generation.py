def fibonacci(number):
    cur_val = 0
    next_val = 1
    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val



fib_seq= fibonacci(10)
for i_value in fib_seq:
    print(i_value)