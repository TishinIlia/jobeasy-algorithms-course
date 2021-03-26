# Find the maximal sequence of consecutive zeros that surrounded by ones
# at both ends in the binary representation of a number entered by User.
from decimal import Decimal

number = int(input('Please input a number: '))


def to_bin(number):
    result = ''
    while number > 0:
        number, remainder = divmod(number, 2)
        result += str(remainder)
    return result[::-1]

# print(to_bin(137253))

num1 = Decimal(0.1)
num2 = Decimal(0.2)
num3 = Decimal(0.3)
print(num1 + num2 + num3)

def binary_gap(bin_number):
    print(bin_number)
    max_gap = 0
    counter = 0
    for item in str(bin_number):
        if item == '0':
            counter += 1
        elif item == '1':
            if counter > 0 and counter > max_gap:
                max_gap = counter
            counter = 0
    return max_gap


# print(binary_gap(to_bin(number)))