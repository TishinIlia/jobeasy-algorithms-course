from lesson_3.HW_1.Home_Sum_of_digit import sum_of_digits


def digital_root_rec(num):
    if num < 10:
        return num
    return digital_root_rec(sum_of_digits(num))
