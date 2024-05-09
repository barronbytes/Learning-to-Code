"""
    Goal: reverse an array
    Input: list
    Output: list with items in reverse
"""

def reverse_array(items):
    list_reversed = []
    for i in range (len(items)-1, -1, -1):
        list_reversed.append(items[i])
        
    return list_reversed
