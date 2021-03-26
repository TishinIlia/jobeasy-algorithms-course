from random import randint

length = int(input('Enter a number of items: '))
list_numbers = []

for _ in range(length):
    list_numbers.append(randint(1, 10))
print(list_numbers)

def ar_mn(arr):
    result = []
    arith = sum(arr) / len(arr)
    for item in arr:
        if item < arith:
            result.append(item)
    return result


print(ar_mn(list_numbers))