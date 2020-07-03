# Given an array of integers that are out of order, determine the bounds 
# of the smallest window that must be sorted in order for the entire array 
# to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3)
# Because, the array is sorted it becomes [3, 5, 6, 7, 9] indices 1->3 had to be changed.

arr1 = [3, 7, 5, 6, 9]

# here, we make a sorted copy of arr, then compare each i, once we find a != we set the left
# this inefficient and runs in O(n log n) time and space since we first created a sorted copy of the array
def window(array):
    left, right = None, None
    s = sorted(array)

    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
    return left, right
    
results = window(arr1)
print(results)


# we traverse the array left to right, and take note if each element is less than the
# maximum seen up to that point. this element would hav eto be part of the sorting window
# since we would have to move the maximum element past it.
# As a result we take the last element that is less than the running maximum, and use it as our right bound
# Similarly for the left bound , we traverse the array form right to left, and find the last element that 
# exceeds the running minimum.
# This will take two passes over the array, operating in O(n)t and O(1)s

def better_window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
    
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i
    
    return left, right
    
results = better_window(arr1)
print(results)
