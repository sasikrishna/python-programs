'''
Problem statement: Given a binary tree, return true if it is BST, else false. For example, the following tree is not BST,
 because 11 is in left subtree of 10. The task is to complete the function isBST() which takes one argument,
 root of Binary Tree.
'''

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:  # Binary tree Class
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i


def isBST(root):
    min = -100000000
    max = 100000000
    return isBSTUtil(root, min, max)


def isBSTUtil(root, min, max):
    if root is None:
        return 1

    if root.data < min or root.data > max:
        return 0

    return isBSTUtil(root.left, min, root.data - 1) and isBSTUtil(root.right, root.data + 1, max)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(1)
            continue
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k + 1]), arr[k + 2]))
            k += 3

        if isBST(root):
            print(1)
        else:
            print(0)
