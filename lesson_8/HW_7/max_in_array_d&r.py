# Find the biggest number in the list

def find_max(arr: list):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if find_max(left) > find_max(right):
        return find_max(left)
    else:
        return find_max(right)


print(find_max([4, 2, 1, 3, 5, 6]))
