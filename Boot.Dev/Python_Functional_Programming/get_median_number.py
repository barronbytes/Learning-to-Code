'''
This program calculates the median number from an unsorted list of numbers. If the list is empty, then the program returns None.

Example:
    Input 1: [10, 2, 8, 4, 6, 12]
    Output 1: 7.0

    Input 2: [15, 3, 7, 9, 11]
    Output 2: 9
'''

def get_median_number(unsorted_numbers):
    if len(unsorted_numbers) == 0:
        return None

    is_length = len(unsorted_numbers)
    is_odd = is_length % 2 != 0
    i = is_length // 2
    is_sorted = sorted(unsorted_numbers)
    
    return is_sorted[i] if is_odd else sum(is_sorted[i-1:i+1]) / 2
