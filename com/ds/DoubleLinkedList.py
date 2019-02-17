from com.ds.SingleLinkedList import Node


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert_begining(self, ele):

        if self.head is None:
            self.head = Node(ele)
            return True

        new_node = Node(ele)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node;

        self.head = new_node
        return True

    def insert_end(self, ele):

        if self.head is None:
            self.head = Node(ele)
            return True

        temp_head = self.head
        while temp_head.next is not None:
            temp_head = temp_head.next

        new_node = Node(ele)
        temp_head.next = new_node
        new_node.prev = temp_head

        return True

    def remove(self, ele):

        if self.head is None:
            return False

        temp_head = self.head
        prev = temp_head
        while temp_head.data != ele:
            prev = temp_head
            temp_head = temp_head.next

        # Checking if head reached to last in linked list
        if temp_head is None:
            return False

        prev.next = temp_head.next
        temp_head.prev = prev

        return True

    def print(self):
        temp_head = self.head

        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next


if __name__ == '__main__':
    list = DoubleLinkedList()
    list.insert_begining(20)
    list.insert_begining(42)
    list.insert_end(67)
    list.insert_begining(72)
    list.insert_end(43)
    list.insert_begining(23)
    list.insert_end(65)
    list.insert_begining(29)
    list.remove(67)
    list.print()
