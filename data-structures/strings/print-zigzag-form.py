sentence = "thisisazigzag"
k = 4

# constant time O(k)
# row is the current row, desc represents whether we are descending, k is the number of lines
def get_spaces(row, desc, k): 
    max_spaces = (k - 1) * 2 - 1
    if desc:
        spaces = max_spaces - row * 2
    else:
        spaces = max_spaces - (k - 1 - row) * 2
    return spaces

# constant time O(k)
# are we descending represented mathematically
def is_descending(index, k):
    # check whether the index is more or less than halfway
    # through its oscillation back to the starting point.
    return index % (2 * (k - 1)) < k - 1

# O(k X n) time and O(n) space
def zigzag(sentence, k):
    n = len(sentence)

    #  O(n)
    for row in range(k):
        # create a list of empty spaces for the first row
        i = row
        line = [" " for _ in range(n)]

        while i < n:
            # get the line
            line[i] = sentence[i]
            # check if the line is desc or asc  
            desc = is_descending(i, k)
            # find out how many spaces are needed
            spaces = get_spaces(row, desc, k)
            # move to the next index
            i += spaces + 1
        # print out the row
        print("".join(line))

zigzag(sentence, k)
