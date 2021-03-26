# TODO: Write a function for decompressing string “a4b3c2d13”

def decompress_string(string):
    result = ''
    count = ''
    for ch in string[::-1]:
        if ch.isalpha():
            if len(count) > 0:
                result += ch * int(count[::-1])
                count = ''
            else:
                result += ch
        if ch.isdigit():
            count += ch
    return result[::-1]


print(decompress_string('abcd'))