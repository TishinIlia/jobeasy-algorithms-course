# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display element of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


def fibonacci(n):
    if n < 0:
        return 'Incorrect value'
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    fibonacci_1, fibonacci_2 = 1, 1
    i = 0
    while i < n - 2:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        i += 1
    else:
        return fibonacci_2

