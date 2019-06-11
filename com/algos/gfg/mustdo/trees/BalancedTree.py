'''
Problem statement: Given a binary tree, find if it is height balanced or not.
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes
of tree.
'''

class Node:
    # Constructor to create a new Node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_height(root):
    if root is None:
        return 0

    return 1 + max(get_height(root.left), get_height(root.right))


def isBalanced(root):
    if root is None:
        return 1

    left_tree_height = get_height(root.left)
    right_tree_height = get_height(root.right)

    if abs(left_tree_height - right_tree_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)

# Initial Template for Python 3
if __name__ == '__main__':
    root = None
    t = int(input())
    for i in range(t):
    # root = None
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        dictTree = dict()

for j in range(n):
    if arr[3 * j] not in dictTree:
        dictTree[arr[3 * j]] = Node(arr[3 * j])
        parent = dictTree[arr[3 * j]]
        if j is 0:
            root = parent

    else:
        parent = dictTree[arr[3 * j]]

    child = Node(arr[3 * j + 1])
    if (arr[3 * j + 2] == 'L'):
        parent.left = child
    else:
        parent.right = child
    dictTree[arr[3 * j + 1]] = child

if isBalanced(root):
    print(1)
else:
    print(0)
