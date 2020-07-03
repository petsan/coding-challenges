arr1 = [1, 2, 3, 4, 5] # should return [120, 60, 40, 30, 24]
arr2 = [1, 2, 3] # should return [6, 3, 2]

# Given an array of integers, return a new array such that each
# element at index i of the new array is the product of all the 
# numbers in the original array except the one at i.
# O(n) time, O(n) space

def products(nums):
    if len(nums) < 3:
        return 0

    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result

results1 = products(arr1)
print(results1)
results2 = products(arr2)
print(results2)
