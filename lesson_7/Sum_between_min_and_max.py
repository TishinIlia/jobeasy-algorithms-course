# Find a sum of elements between min and max elements. Min and max elements are not included

def sum_between_min_and_max(array):
    if len(array) < 1:
        return 'Exception, should be at least one element'
    if len(array) in (1, 2):
        return []
    max_item = array[0]
    min_item = array[0]
    max_index = 0
    min_index = 0
    index = 0
    while index < len(array):
        if array[index] > max_item:
            max_item = array[index]
            max_index = index
        if array[index] < min_item:
            min_item = array[index]
            min_index = index
        index += 1

    min(min_index, max_index)
    max(min_index, max_index)

    sub_list = array[min(min_index, max_index) + 1:max(min_index, max_index)]
    return sum(sub_list)



print(sum_between_min_and_max([1, 1, 1, 1]))
