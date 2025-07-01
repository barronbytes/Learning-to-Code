def quick_sort(nums, low, high):
    # Base case: if no need to sort (i.e. no item, single item, or low > high)
    if low < high:
        # Sort smaller-than-pivot values, place pivot, and return pivot's sorted index
        p = partition(nums, low, high)
        quick_sort(nums, low, p - 1)    # Left recursion sublist (elements < pivot)
        quick_sort(nums, p + 1, high)   # Right recursion sublist (elements ≥ pivot)


def partition(nums, low, high):
    # Lomuto partition: last element becomes pivot
    pivot = nums[high]

    # Partitioning pointer i: tracks index above smaller-than-pivot region
    i = low

    # Scanning pointer j: checks each sublist element (value < pivot)
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i] # Swap value to partition index position
            i += 1 # Expand the partition index

    # Final swap: place pivot in its correct sorted position
    nums[i], nums[high] = nums[high], nums[i]

    # Return sorted pivot index
    return i


# Example usage
nums = [38, 27, 43, 3, 9, 82, 10]
quick_sort(nums, 0, len(nums)-1)  # Sorts the list in place
print("Quick Sort Result:", nums)
