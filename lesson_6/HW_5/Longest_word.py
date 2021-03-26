# Enter a string of words separated by spaces. Find the longest word.

string = input(f"Enter a string: ")


def longest_word(string_1):
    substring = ''
    result = ''
    for char in string_1:
        if char == ' ':
            if len(substring) > len(result):
                result = substring
            substring = ''
        else:
            substring += char
    else:
        if len(substring) > len(result):
            result = substring
    return result

print(longest_word(string))
