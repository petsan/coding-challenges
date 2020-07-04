# Given a list of words, find all pairs of unique indices such that the concatenation of
# the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)]

words = ["code", "edoc", "d", "cbaa", "aabc", "da"]

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

print(palindrome_pairs(words)) # [(0, 1), (1, 0), (3, 4), (4, 3), (5, 2)]


# with dictionary, O(n X c^2)
def is_another_palindrome(word):
    return word == word[::-1]

def palindrome_pairs_with_dict(words):
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []

    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[:char_i]
            reversed_prefix = prefix[::-1]
            reversed_suffix = suffix[::-1]

            if (is_another_palindrome(suffix) and reversed_prefix in d):
                if i != d[reversed_prefix]:
                    result.append((i, d[reversed_prefix]))
            
            if (is_another_palindrome(prefix) and reversed_suffix in d):
                if i != d[reversed_suffix]:
                    result.append((d[reversed_suffix], i))
    print(d) # {'code': 0, 'edoc': 1, 'd': 2, 'cbaa': 3, 'aabc': 4, 'da': 5}
    return result

print(palindrome_pairs_with_dict(words)) # [(5, 2), (2, 5)]
