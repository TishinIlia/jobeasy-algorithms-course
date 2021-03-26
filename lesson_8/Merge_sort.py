from random import randint
from math import floor


def merge_sort(array: list):
    pass

def get_random_list(length: int):
    return [randint(-99, 99) for i in range(length)]


a = get_random_list(10)
print(f'Input {a}')
result = merge_sort(a)
print(f'Output {result}')