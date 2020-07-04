# Given an array of integers, return a new array where each element in the new array
# is the number of smaller elements to the right of that element in the original input array.
# 
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2 , 1, 0]

# 1 smaller element to the right of 3 (1)
# 1 smaller element to the right of 4 (1)
# 2 smaller elements to the right of 9 (6, 1)
# 1 smaller element to the right of 6 (1)
# 0 smaller elements to the right of 0 ()

array = [3, 4, 9, 6, 1]

def smaller_counts_naive(lst): # O(n^2)
    result = []

    for i, num in enumerate(lst): 
        count = sum(val < num for val in lst[i + 1:])
        result.append(count)

    return result

print(smaller_counts_naive(array))


# iterate backwards over the input list
# maintain a sorted list of elements we've already seen
# Look at seen to see where the current element would fit in
# O(n log n) O(n)
import bisect

def smaller_counts(lst):
    result = []
    seen = []

    for num in reversed(lst):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort(seen, num)

    return list(reversed(result))

print(smaller_counts(array))
