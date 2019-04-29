'''
Problem statement: Given a list of non negative integers, arrange them in such a manner that they form the largest number
 possible.The result is going to be very large, hence return the result in the form of a string.
'''

import functools


def greater(a, b):
    result1, result2 = a + b, b + a
    if int(result1) > int(result2):
        return 1
    return -1


if __name__ == '__main__':
    test_cases = int(input())

    list_count, lists = [], []
    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(input().split()))

    for i in range(test_cases):
        sorted_list = sorted(lists[i], key=functools.cmp_to_key(greater), reverse=True)
        print(*sorted_list, sep="")
