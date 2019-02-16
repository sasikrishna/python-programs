
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def add(self, ele):
        new_node = Node(ele)
        if self.head is None:
            self.head = new_node
            return

        temp_head = self.head
        while temp_head.next is not None:
            temp_head = temp_head.next;

        temp_head.next = new_node;

    def contains(self, ele):
        temp_head = self.head
        while temp_head is not None:
            if temp_head.data == ele:
                return True
            temp_head = temp_head.next

        return False

    def remove(self, ele):

        if self.head is None:
            return;

        if self.head.data == ele:
            self.head = self.head.next
            return True

        temp_head = self.head.next
        prev_node = temp_head
        is_node_deleted = False
        while temp_head is not None:
            if temp_head.data == ele:
                is_node_deleted = True
                prev_node.next = temp_head.next
                break
            prev_node = temp_head
            temp_head = temp_head.next

        return is_node_deleted

    def print_list(self):
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next


if __name__ == '__main__':
    list = SingleLinkedList();
    list.add(5)
    list.add(4)
    list.add(12)
    list.add(13)
    list.add(19)
    list.print_list();
    print("List contains element 4", list.contains(4))
    print("List contains element 6", list.contains(6))
    print("Removing element 13", list.remove(13))
    list.print_list();
    print("List contains element 13", list.contains(13))
