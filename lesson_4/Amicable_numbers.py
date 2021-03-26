from lesson_2.Get_devisors import get_divisors


def amicable_numbers(num_1, num_2):
    num_1_divisors = get_divisors(num_1)
    num_2_divisors = get_divisors(num_2)
    if sum(num_2_divisors) == num_1 and sum(num_1_divisors) == num_2:
        return True
    return False


print(amicable_numbers(220, 284))
