# O(n) — Linear Time


def find_maximum(nums):
    max = -float("inf")
    for num in nums:
        if num > max:
            max = num
    return max


nums = [3, 17, 2, 99, 24, 1]
maximum_value = find_maximum(nums)
print("The maximum value is:", maximum_value)


"""
Here are other examples:


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
