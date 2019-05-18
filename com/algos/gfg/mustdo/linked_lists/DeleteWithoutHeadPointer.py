'''
Problem Statement: You are given a pointer/reference to a node to be deleted in a linked list of size N. The task is to
delete the node. Pointer/reference to head node is not given. You may assume that the node to be deleted is not the
last node.
'''

from com.algos.gfg.mustdo.linked_lists.SingleLinkedList import LinkedList, Node


def delete_without_head(node_to_delete):
    node_to_delete.data = node_to_delete.next.data;
    node_to_delete.next = node_to_delete.next.next;


if __name__ == '__main__':
    test_cases = int(input())
    lists, list_count, delete_nodes_list = [], [], []

    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(map(int, input().split())))
        delete_nodes_list.append(int(input()))

    for i in range(test_cases):

        list = LinkedList()
        node_to_delete = None
        for j in range(list_count[i]):
            node = Node(lists[i][j])
            list.add_node(node)

            if node.data == delete_nodes_list[i]:
                node_to_delete = node;

        delete_without_head(node_to_delete)
        list.print_list()
        print()


