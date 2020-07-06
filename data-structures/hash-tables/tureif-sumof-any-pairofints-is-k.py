lst = [10, 15, 3, 7]
k = 17

def two_sum(lst, k):
    seen = {}
    print(seen)
    for num in lst:
        if k - num in seen: 
            print(seen)
            return True
        seen[num] = True
        print(seen)

print(two_sum(lst, k))

# {}
# {10: True}
# {10: True, 15: True}
# {10: True, 15: True, 3: True}
# {10: True, 15: True, 3: True}
# True
