def bubble_sort(nums):
    swapped = True
    end = len(nums)
    while swapped:
        swapped = False
        for i in range(end - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        end -= 1  # After each full pass, the largest remaining element is in its final position
                  # So we reduce the range of future passes to skip that sorted end
    return nums


nums = [38, 27, 43, 3, 9, 82, 10]
print("Bubble Sort Result:", bubble_sort(nums))
