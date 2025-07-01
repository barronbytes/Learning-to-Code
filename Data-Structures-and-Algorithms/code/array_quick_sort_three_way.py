def quick_sort(arr):
    # Base case: if no need to sort (i.e. sublist is empty or has one item)
    if len(arr) <= 1:
        return arr

    # Dutch National Flag approach: use first element as pivot
    pivot = arr[0]

    # Initialize three partitions:
    smaller, equal, larger = [], [], []

    # Scan through the array and place values into appropriate partitions
    for num in arr:
        if num < pivot:
            smaller.append(num)      # Add to left partition
        elif num == pivot:
            equal.append(num)        # Add to middle (equal) partition
        else:
            larger.append(num)       # Add to right partition

    # Recursively sort left and right partitions and concatenate the result
    return quick_sort(smaller) + equal + quick_sort(larger)


# Example usage
nums = [38, 27, 3, 10, 82, 10, 10]
sorted_nums = quick_sort(nums)  # Returns new sorted list
print("Quick Sort Result:", sorted_nums)
