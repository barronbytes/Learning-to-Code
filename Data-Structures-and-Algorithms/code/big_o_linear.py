# O(n) — Linear Time


def find_number(arr, target):
    is_found = False
    for element in arr:
        if element == target:
            is_found = True
    return is_found


arr = [1, 2, 3, 4, 5]
target = 3
print(find_number(arr, target))


"""
Here are other example(s):


def find_maximum(nums):
    max = -float("inf")
    for num in nums:
        if num > max:
            max = num
    return max


def find_minimum(nums):
    has_data = bool(nums)
    result = None if not has_data else min(nums)
    return result


def sum(nums):
    result = 0
    has_data = bool(nums)
    for num in nums:
        result += num
    return 0 if not has_data else result

    
def average_followers(nums):
    has_data = bool(nums)
    total = sum(nums)
    return None if not has_data else total / len(nums)

"""
