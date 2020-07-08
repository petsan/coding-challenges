class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# runs in O(n^2)t
def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    
    if root.value == value:
        return unival_helper(root.left, value) and \
               unival_helper(root.right, value)

    return False

def count_unival_subtrees(root):
    if root is None:
        return 0

    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    return 1 + left + right if is_unival(root) else left + right


preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return preorder[0]

    root = preorder[0]
    root_i = inorder.index(root)
    root.left = reconstruct(preorder[1:1 + root_i], inorder[0:root_i])
    root.rigth = reconstruct(preorder[1 + root_i:], inorder[root_i + 1:])

    return root
    