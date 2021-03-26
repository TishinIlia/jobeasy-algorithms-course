# User inputs two numbers. One number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.


# a = int(input('Input value a '))
# b = int(input('Input value b '))
#
# print(f'a = {a}, b = {b}')

# option 1
# temp = a
# a = b
# b = temp

# option 2
# a = a + b  # 15
# b = a - b  # 10
# a = a - b  # 5

# option 3

a, b = 10, 5
# a, b = b, a // a = 5, b = 10
a, b = b, a + 100
#
print(f'a = {a}, b = {b}')

# string = 'Hello world'[::-1]
# print(string)