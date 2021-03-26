# Populate a list of random numbers. Find and print the max element and the index of this element


from random import randint
lowest = int(input('From number'))
greatest = int(input('To number'))


length = int(input(f"Enter a list length "))
array_1 = []

for i in range(length):
    item = randint(lowest, greatest)
    array_1.append(item)


def find_max_item_and_its_index_in_list(array):
    pass


print(find_max_item_and_its_index_in_list(array_1))
