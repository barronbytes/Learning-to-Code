def insertion_sort(nums):
    # Loop through each element in the list
    for i in range(len(nums)):
        j = i
        # Compare and swap the current element leftward into the sorted portion
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]  # Swap with previous if out of order
            j -= 1  # Move left in the sorted portion
    return nums  # Return the fully sorted list


nums = [38, 27, 43, 3, 9, 82, 10]
print("Insertion Sort Result:", insertion_sort(nums))
