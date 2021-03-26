def fibonacci_rec(num):
    if num < 0:
        return 'Only positive numbers'
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)

print(fibonacci_rec(100000))

