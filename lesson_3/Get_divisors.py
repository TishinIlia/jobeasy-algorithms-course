def get_divisors(num, include_num: bool):
    result = []
    end = num
    if include_num:
        end = num + 1

    for item in range(1, end):
        if num % item == 0:
            result.append(item)

    return result