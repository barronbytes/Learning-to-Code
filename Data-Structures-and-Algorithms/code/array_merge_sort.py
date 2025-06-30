def merge_sort(nums):
    # Base case: if array has one or zero elements, it's already sorted
    if len(nums) < 2:
        return nums
    
    # Divide step: split list into two halves
    mid = len(nums) // 2
    first = merge_sort(nums[:mid])
    second = merge_sort(nums[mid:])

    # Conquer step: merge two sorted halves
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0
    j = 0

    # Compare each element of the two halves and merge them in sorted order
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    # If there are remaining elements in first or second, append them
    final.extend(first[i:])
    final.extend(second[j:])
    return final

nums = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sort Result:", merge_sort(nums))