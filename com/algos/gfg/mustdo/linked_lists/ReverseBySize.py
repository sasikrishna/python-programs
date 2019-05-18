'''
Problem statement: Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the
function) in the linked list.
'''

from com.algos.gfg.mustdo.linked_lists.SingleLinkedList import LinkedList


def reverse_by_size(head, size):
    grp_start_node = None
    curr, prev, next = head, None, None

    while curr is not None:

        count = 0
        prev = None
        while count < size and curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if grp_start_node is None:
            grp_start_node = head
            head = prev
        else:
           # print("grp_start_node", curr.data)
            grp_start_node.next = prev

    return head


if __name__ == '__main__':
    test_cases = int(input())
    num_count, num_list, size = [], [], []

    for i in range(test_cases):
        num_count.append(int(input()))
        num_list.append(list(map(int, input().split())))
        size.append(int(input()))

    for i in range(test_cases):
        list = LinkedList()

        for j in range(num_count[i]):
            list.add(num_list[i][j])

        list.head = reverse_by_size(list.head, size[i])
        list.print_list()

