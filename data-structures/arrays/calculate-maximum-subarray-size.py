# Given an array of numbers, find the maximum sum of any contiguous subarray of
# the array. For example, given the array [34, -50, 42, 14, -5, 86], the maximum
# sum would be 137, since we would sum the subarray [42, 14, -5, 86]. Given the
# array [-5, -1, -8, -9], the maximum sum would be 0, since we would choose not
# to take any elements.

# Do this in O(n) time.

# Follow-up: What if the elements can wrap around? For example, given [8, -1, 3, 4]
# return 15, since we would choose the numbers 3, 4, and 8 where 8 is obtained from 
# wrapping around.


array1 = [34, -50, 42, 14, -5, 86]
array2 = [-5, -1, -8, -9]
array3 = [8, -1, 3, 4]

# Brute force
def max_subarray_sum_brute(arr):
    current_max = 0
    for i in range(len(arr) -1):
        for j in range(i, len(arr)):
            current_max = max(current_max, sum(arr[i:j]))
    return current_max

result1 = max_subarray_sum_brute(array1)
result2 = max_subarray_sum_brute(array2)
result3 = max_subarray_sum_brute(array3)
print(result1, result2, result3)

# Kadane's algorithm
def max_subarray_sum_kadane(arr):
    max_ending_here = max_so_far = 0
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_ending_here

print(max_subarray_sum_kadane(array1))

#  Circular wrap-around followup
def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)

    return max(max_subarray_sum(arr), max_subarray_sum_wraparound)

def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def min_subarray_sum(arr):
    min_ending_here = min_so_far =0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

result1 = maximum_circular_subarray(array1)
result2 = maximum_circular_subarray(array2)
result3 = maximum_circular_subarray(array3)
print(result1, result2, result3)
