# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0

from random import randint

# n = int(input("Enter a number of digits "))
# n = 5
# digits = 84621
# (10000, 99999)

# down 10 ** 4
# up (10 ** 5) - 1


# n = 3

# down 100
# 10 ** 2

# up 999
# (10 ** 3) - 1


# n = 4
# 1000 - down (10 ** 3)
# 9999 - up (10 ** 4) - 1

# n = 3
# 100 - down (10 ** 2)
# 999 - up (10 ** 3) - 1

# down = 10 ** (digits - 1)
# up = (10 ** digits) - 1
# random_value = randint(down, up)


def sum_of_digits(number):
    digits_sum = 0
    for char in str(number):
        digits_sum += int(char)
    return digits_sum

# sum_of_digits(n)
