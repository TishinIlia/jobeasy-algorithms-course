from random import randint


def bubble_sort(array: list):
    pass


def get_random_list(length: int):
    return [randint(-99, 99) for _ in range(length)]


a = get_random_list(10)
print(f'Input {a}')
result = bubble_sort(a)
print(f'Output {result}')
