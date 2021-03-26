from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)


# def two_mins(array):
#     result = []
#     min_element = min(array)
#     result.append(min_element)
#     array.remove(min_element)
#     min_element = min(array)
#     result.append(min_element)
#     return result
#
#
# print(two_mins(list_numbers))

def n_mins(array, n):
    result = []
    if len(array) < n:
        n = len(array)
    for _ in range(n):
        min_element = min(array)
        result.append(min_element)
        array.remove(min_element)
    return result

print(n_mins(list_numbers, length))