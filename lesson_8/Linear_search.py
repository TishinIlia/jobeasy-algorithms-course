from random import randint


def linear_search(array: list, needed_item):
    pass


def get_random_list(length: int):
    return [randint(-10, 10) for i in range(length)]


a = sorted(get_random_list(10))
item = randint(-10, 10)
print(f'Input {a} \n {item} \n')
result = linear_search(a, item)
print(f'Output {result}')