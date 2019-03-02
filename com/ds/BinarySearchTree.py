
from com.ds.BinaryTree import Node


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self, root, key):

        if self.root is None:
            self.root = Node(key)
            return

        if key < root.data:
            if root.left is None:
                root.left = Node(key)
            else:
                self.add(root.left, key)
        elif key > root.data:
            if root.right is None:
                root.right = Node(key)
            else:
                self.add(root.right, key)

    def remove(self, key):
        self.root = self.__remove(self.root, key)

    def __remove(self, root, key):

        if root is None:
            return root

        if key < root.data:
            root.left = self.__remove(root.left, key)
        elif key > root.data:
            root.right = self.__remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            node = self.find_in_order_successor(root)
            root.data = node.data
            root.right = self.__remove(root.right, node.data)

        return root

    def contains(self, root, key):

        if self.root is None:
            return False

        if key == root.data:
            return True

        if key < root.data:
            self.contains(root.left, key)
        elif key > root.data:
            self.contains(root.right, key)

        return False

    def find_in_order_successor(self, root):

        if root.right is not None:
            return BinarySearchTree.find_min_node(root.right)

        temp_root = self.root
        while temp_root is not None:
            if root.data < temp_root.data:
                successor = root
                temp_root = root.left
            elif root.data > temp_root.data:
                temp_root = temp_root.right
            else:
                break

        return successor

    def find_min_node(root):
        while root.left is not None:
            root = root.left

        return root

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
    bst.add(bst.root, 6)
    bst.add(bst.root, 5)
    bst.add(bst.root, 7)
    bst.add(bst.root, 10)
    bst.print_in_order(bst.root)

    bst.remove(10)
    bst.print_in_order(bst.root)

    bst.remove(8)
    bst.print_in_order(bst.root)

