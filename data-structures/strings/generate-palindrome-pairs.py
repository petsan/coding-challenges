# Given a list of words, find all pairs of unique indices such that the concatenation of
# the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)]

words = ["code", "edoc", "da", "d"]

# Brute force 
# O(n^2 X c) wher n is the number of words and c is the length of the longest word.
# O(n^2) if we drop the c

def is_palindrome(word):
    # simple string reverse method
    # returns true if string == reversed string
    return word == word[::-1]

def palindrome_pairs(words):
    result = []

    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                result.append((i, j))

    return result

print(palindrome_pairs(words)) # [(0, 1), (1, 0), (2, 3)]

