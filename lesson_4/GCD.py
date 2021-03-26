# Find divisor of two or more integers, which are not all zero,
# is the largest positive integer that divides each of the integers.

from lesson_3.Get_divisors import get_divisors


def in_list(num, list_of_numbers):
    return num in list_of_numbers



def greater_common_divisor(num_1, num_2):
    divisors_num_1 = get_divisors(num_1)
    divisors_num_2 = get_divisors(num_2)

    result = []
    for num in divisors_num_1:
        if in_list(num, divisors_num_2):
            result.append(num)
    return max(result)


print(greater_common_divisor(24, 48))