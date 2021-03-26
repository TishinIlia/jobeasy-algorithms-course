# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

from lesson_3.HW_1.Home_Sum_of_digit import sum_of_digits

# def digital_root(number):
#     while number > 9:
#         number = sum_of_digits(number)
#     return number


def digital_root(number):
    while len(str(number)) > 1:
        result = 0
        for digit in str(number):
            result += int(digit)
        number = result
    return number


print(digital_root(493193))
