# Given a word w and a string s, find all indices in s which are the starting locations
# of anagrams of w. For example, given w is 'ab' and s is 'abxaba', return [0, 3, 4].


s = 'abxaba'
w = 'ab'


# Brute force - O(w X s)
# Go over each word-size window in s and check if it forms an anagram.

# The built-in Counter collection, when applied to a word forms a dictionary whose keys
# are characters and whose values are their respective counts.

from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def anagram_indeces(word, s):
    result = []

    for i in range(len(s) - len(word) + 1):
        window = s[i:i + len(word)]
        if is_anagram(window, word):
            result.append(i)
    
    return result

print(anagram_indeces(w, s)) # [0, 3, 4]


# Better: using a hash-map - O(s)
from collections import defaultdict

def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def anagram_indeces_better(word, s):
    result = []

    # First, make a frequency dictionary of both the initial window and the target word
    freq = defaultdict(int)

    # As we move along the string, we increment the count of each new character and decrement the count of the old
    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)

    if not freq:
        result.append(0)

    # if there is no difference between the frequencies of the target word and the current window,
    # we add the corresponding starting index to our result.
    for i in range(len(word), len(s)):
        start_char, end_char = s[i - len(word)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1
        del_if_zero(freq, end_char)

        if not freq:
            beginning_index = i - len(word) + 1
            result.append(beginning_index)

    return result

print(anagram_indeces_better(w, s)) # [0, 3, 4]
