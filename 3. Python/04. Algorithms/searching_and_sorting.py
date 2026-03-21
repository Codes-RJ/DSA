def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


values = [9, 4, 7, 1, 3]
values.sort()

print("Sorted values:", values)
print("Index of 7:", binary_search(values, 7))
