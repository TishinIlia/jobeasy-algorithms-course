# Write a Python program to check if a given string is an anagram of another given string.
# According to Wikipedia an anagram is direct word switch or word play, the result of rearranging the
# letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once;
# for example, the word anagram can be rearranged into nag-a-ram.
# Example: 'hearth' and 'earthh'

# str1 = input(f"Enter first string: ")
# str2 = input(f"Enter second string: ")

# from collections import Counter

def anagram_check(string_1, string_2):
    if not len(string_1) == len(string_2) and not string_1 == string_2:
        return False
    for char in string_1:
        if not string_1.count(char) == string_2.count(char):
            return False
    return True



# def is_anagram(string1, string2):
#     return Counter(string1) == Counter(string2)



# print(is_anagram('hearth', 'earthh'))
