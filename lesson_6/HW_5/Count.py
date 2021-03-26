# Write a Python function, which will count how many times a character (substring)
# is included in a string. DON’T USE METHOD COUNT

# string = input(f"Enter a string ")
# substring = input(f"Enter a substring ")


def count(given_string, given_substring, start, end):
    counter = 0
    if len(given_string) < len(given_substring):
        return counter
    index = given_string.find(given_substring, start, end)
    while index > -1:
        index = given_string.find(given_substring, index + 1, end)
        counter += 1
    return counter

print(count('my hello world of heroes', 'he', 5, 15))
print('my hello world of heroes'.count('he', 5, 15))
