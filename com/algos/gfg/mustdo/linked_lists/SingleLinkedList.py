
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        self.add_node(Node(data))

    def add_node(self, node):
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = node

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        # Added for solving list flattening probem
        self.next = None
