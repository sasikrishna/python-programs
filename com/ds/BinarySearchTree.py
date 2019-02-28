
from com.ds.BinaryTree import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, root, data):

        if self.root is None:
            self.root = Node(data)
            return

        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self.add(root.left, data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self.add(root.right, data)

    def remove(self):
        pass

    def contains(self, root, data):
        if self.root is None:
            return False

        if data == root.data:
            return True

        if data < root.data:
            self.contains(root.left, data)
        elif data > root.data:
            self.contains(root.right, data)

        return False

    def print_in_order(self, root):

        if root is None:
            return

        self.print_in_order(root.left)
        print(root.data)
        self.print_in_order(root.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.add(bst.root, 8)
    bst.add(bst.root, 9)
    bst.add(bst.root, 7)
    bst.add(bst.root, 5)
    bst.add(bst.root, 6)
    bst.add(bst.root, 10)
    bst.print_in_order(bst.root)

