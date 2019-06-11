
# Initial Template for Python 3
import atexit
import io
import sys
import collections
import queue

# Contributed by : Nikhil Kumar Singh
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER \
             @ atexit.register


def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3

map = {}


def verticalOrder(root):
    map = {};
    verticalOrder_(root, 0)
    for list_ in map:
        print(" ".join(list_))


def verticalOrder_(root, level):
    if root is None:
        return

    if map.get(level) is None:
        map[level] = []

    list_ = map[level]
    list_.append(root.data)
    map[level] = list_

    verticalOrder_(root.left, level - 1)
    verticalOrder_(root.right, level + 1)

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Tree Class
class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = collections.defaultdict(Node)

    def Insert(self, parent, child, dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(str, input().strip().split()))  # parent child info in list
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        verticalOrder(tree.root)
        print()

