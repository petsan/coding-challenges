# naive: O(n x k).t
lst = [10, 5, 2, 7, 8, 7]
k = 3

def max_of_subarrs(lst, k):
    for i in range(len(lst) - k + 1):
        print(max(lst[i:i + k]))

max_of_subarrs(lst, k)

# better: O(n).t O(n).s
from collections import deque

def max_of_subarrays(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their
    # corresponding values are in descending order.
    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])

max_of_subarrays(lst, k)
