'''
Problem statement: Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
'''

import sys


def min_length(string):
    return __min_length(list(string), 0, len(string) - 1)


def __min_length(char_list, left, right):

    if left > right: return sys.maxsize
    if left == right: return 0
    if left == right - 1: return 0 if char_list[left] == char_list[right] else 1

    if char_list[left] == char_list[right]:
        return __min_length(char_list, left + 1, right - 1)

    return min(__min_length(char_list, left + 1, right), __min_length(char_list, left, right - 1)) + 1


if __name__ == '__main__':
    test_cases = int(input())
    string_list = []

    for i in range(test_cases):
        string_list.append(input())

    for i in range(test_cases):
        print(min_length(string_list[i]))

