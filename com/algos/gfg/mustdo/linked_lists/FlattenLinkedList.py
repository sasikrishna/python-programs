'''
Problem statement: Given a Linked List of size N, where every node represents a linked list and contains two pointers of
 its type:
    1. a next pointer to the next node,
    2. a bottom pointer to a linked list where this node is head.
'''

from com.algos.gfg.mustdo.linked_lists.SingleLinkedList import LinkedList


def merge_lists(head1, head2):

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    new_head = LinkedList().head

    while True:
        if head1 is None:
            new_head.next = head2
            break

        if head2 is None:
            new_head.next = head1
            break

        if head1.data <= head2.data:
            new_head.next = head1
            head1 = head1.next
        else:
            new_head.next = head2
            head2 = head2.next

    return new_head.next


if __name__ == '__main__':
    pass

