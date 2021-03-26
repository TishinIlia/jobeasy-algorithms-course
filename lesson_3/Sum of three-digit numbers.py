# Our code generates a random three-digit number and has to sum up all its digits. For example, if a number is 349,
# the code has to print the number 16, because 3 + 4 + 9 = 16.

n = int(input('Input a number of digits'))

# n = 4
# range() # numbers with 4 digits


# from random import randint
#
# random_number = randint(100, 999)
# print(f'random_number : {random_number}')

def sum_of_three(number): # 896
    once = number % 10 # 6

    number = number // 10 # 89

    tens = number % 10 # 9

    hung = number // 10 # 8

    return once + tens + hung


print(sum_of_three(random_number))
