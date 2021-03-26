# When given a string the code deletes all duplicates leaving only one of each character.

string1 = input(f"Enter a string: ")


def unique_characters_string(string):
    # # option 1
    # result = ''
    # for char in string:
    #     if result.count(char) == 0:
    #         result += char
    # # option 2
    # result = ''
    # for char in string:
    #     if char not in result:
    #         result += char
    # # option 3
    return ''.join(set(string))
    # return result
    # acc = 0
    # num = '1371623'
    # arr = [int(x) for x in num]
    # for char in num:
    #     acc += int(char)


print(unique_characters_string(string1))
