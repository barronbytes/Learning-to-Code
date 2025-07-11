# O(log n) — Logarithmic time


def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    if low > high: # handles empty array case
        return False
    is_found = False
    while low <= high:
        index = (low + high) // 2
        if arr[index] == target:
            is_found = True
            break
        elif target < arr[index]:
            high = index - 1
        else:
            low = index + 1
    return is_found


arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = binary_search(target, arr)
print("Target found:", result)


"""
Here are other example(s):


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

from: https://medium.com/@abasifreke/understanding-time-complexity-big-o-notation-software-performance-f90c5872a7c2

"""
