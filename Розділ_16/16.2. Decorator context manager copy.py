from contextlib import contextmanager

@contextmanager
def nex_num(num: int):
    yield num + 1

with nex_num(0) as next_num:
    print("Next number is: {}".format(next_num))
    print(10 / next_num)
    print("Next number is: {}".format(next_num))