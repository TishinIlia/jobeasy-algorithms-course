# HW4-1
#
def LongestWordLength(str):
    n = len(str)
    res = 0
    curr_len = 0
    for i in range(0, n):
        if (str[i] != ' '):
            curr_len += 1
        else:
            res = max(res, curr_len)
            curr_len = 0
    return max(res, curr_len)
s = "I am a student at JobEasyAutomation"
print(LongestWordLength(s))

# HW4-2

# from string import punctuation
#
# regular_string = "Im a student at Jobeasy"
# valid_words = set(regular_string.split())
#
# irregular_string = "  Im a stu  dent at Job easy  "
# words = irregular_string.split()
#
# out_words = []
# i = 0
# while i < len(words):
#     word = words[i]
#     if word not in valid_words and i+1 < len(words):
#         next_word = words[i+1]
#         joined = word + next_word
#         if joined.strip(punctuation) in valid_words:
#             word = joined
#             i += 1
#     out_words.append(word)
#     i += 1

# regular = " ".join(out_words)
#
# print(regular)

# HW4-3

# s = 'the right temperature is the same for the week'
# sb = 'the'
# results = 0
# sub_len = len(sb)
# for i in range(len(s)):
#     if s[i:i+sub_len] == sb:
#         results += 1
# print(results)

# HW4-4

# import re
#
# string = "An apple,an avocado"
#
# pattern = re.compile('an', re.IGNORECASE)
#
# result = pattern.sub("one", string)
#
# print(result)