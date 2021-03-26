# Given a string. Split it for two same parts. (if the string has odd characters, the first part should
# be greater for one character). Swap this parts and save the result in a new string and return it

from math import floor
from math import ceil


def split_in_half(string):
    string_len = len(string)
    print(string_len)
    # half = ceil(string_len / 2)
    half = string_len // 2
    half = floor(string_len / 2)
    print(half)
    left = string[:half]
    right = string[half:]
    print(left)
    print(right)
    return right + left

print(split_in_half('bbbbbcaaaaa'))
