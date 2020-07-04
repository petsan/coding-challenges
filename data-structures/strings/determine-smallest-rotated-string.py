string = "xxabxx"
k = 1
k2 = 2

# t = O(n^2), s = O(n)
def bubble_swap(string):
    string = list(string)
    i = len(string)
    j = len(string)

    # Rotate so that i is at the beginning
    while i > 0:
        string = string[1:] + string[:1]
        i -= 1

    # Move the first two letters to the end in reversed order.
    string = string[:1] + string[2:] + string[1:2]
    string = string[1:] + string[:1]

    # Rotate back to the initial position.
    while len(string) > j + 1:
        string = string[1:] + string[:1]
        j += 1

    return ''.join(string)

print(bubble_swap(string))


# t = O(n log n), s = O(n)
def get_best_word(string, k):
    string = list(string)

    # return alphabetically earliest rotation if k = 1
    if k == 1:
        best = string
        for i in range(1, len(string)):
            if string[i:] + string[:1] < best:
                best = string[i:] + string[:i]
        return ''.join(best)
    
    # if k > 1 return the sorted string
    else:
        return ''.join(sorted(string))

print(get_best_word(string, k))
print(get_best_word(string, k2))
