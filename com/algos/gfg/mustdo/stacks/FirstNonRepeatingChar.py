'''
Problem statement: Given an input stream of N characters consisting only of lower case alphabets. The task is to find
the first non repeating character, each time a character is inserted to the stream. If no non repeating element is
found print -1.
'''

from collections import deque


def print_first_char(char_list, char_count):
    frequency = [0] * 26
    dequeue = deque()
    index = 0;

    while index < char_count:
        dequeue.append(char_list[index])
        frequency[ord(char_list[index]) - 97] += 1
        while len(dequeue) != 0:
            element = dequeue[0]
            if frequency[ord(element) - 97] > 1:
                dequeue.popleft()
            else:
                print(element, end = ' ')
                break;

        if len(dequeue) == 0:
            print(-1, end=' ')

        index += 1

    print()


if __name__ == '__main__':
    test_cases = int(input())

    for i in range(test_cases):
        char_count = int(input())
        char_list = input().split()
        print_first_char(char_list, char_count)



