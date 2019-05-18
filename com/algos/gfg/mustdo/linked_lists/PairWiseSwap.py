'''
Problem statement: Given a singly linked list of size N. The task is to swap elements pairwise.
'''

from com.algos.gfg.mustdo.linked_lists.SingleLinkedList import LinkedList


def sortbypairwise(head):
    curr, prev, next = head, None, None

    while curr is not None:
        next = curr.next

        if next is None:
            break

        nextNext = next.next
        next.next = curr

        if prev is None:
            head = next
        else:
            prev.next = curr.next

        curr.next = nextNext
        prev = curr
        curr = curr.next

    return head


if __name__ == '__main__':
    test_case = int(input())
    list_counts = []
    lists = []

    for i in range(test_case):
        list_counts.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_case):
        list = LinkedList()

        for j in range(list_counts[i]):
            list.add(lists[i][j])

        list.head = sortbypairwise(list.head)
        list.print_list()
