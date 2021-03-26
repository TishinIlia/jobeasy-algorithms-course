from math import floor
from random import randint


def binary_search(array: list, needed_item):
    pass


def get_random_list(length: int):
    return [randint(-99, 99) for i in range(length)]


a = sorted(get_random_list(10))
item = randint(-99, 99)
print(f'Input {a} \n {item} \n')

result = binary_search(a, item)
print(f'Output {result}')