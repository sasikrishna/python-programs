
class BinaryTree:

    def __init__(self):
        self.root = None

    def print_in_order(self, root):

        if root is None:
            return

        self.print_in_order(root.left)
        print(root.data)
        self.print_in_order(root.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    binaryTree = BinaryTree()
    binaryTree.root = Node(10)
    binaryTree.root.left = Node(9)
    binaryTree.root.right = Node(8)
    binaryTree.root.left.left = Node(7)
    binaryTree.root.left.right = Node(6)
    binaryTree.root.right.left = Node(1)
    binaryTree.root.right.right = Node(2)
    binaryTree.print_in_order(binaryTree.root)
