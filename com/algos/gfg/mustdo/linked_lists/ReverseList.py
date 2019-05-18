'''
Problem statement:  Given a linked list of length N. The task is to reverse the list.
'''

from .SingleLinkedList import LinkedList


def reverse_list(head):
    curr, prev, next = head, None, None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


if __name__ == '__main__':
    test_cases = int(input())
    num_count, num_list = [], []

    for i in range(test_cases):
        num_count.append(int(input()))
        num_list.append(list(map(int, input().split())))

    for i in range(test_cases):
        list = LinkedList()
        numbers = num_list[i]
        for j in range(num_count[i]):
            list.add(numbers[j])

        list.head = reverse_list(list.head)
        list.print_list()
        print()
