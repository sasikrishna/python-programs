'''
Problem statement: Given an unsorted array of size N. Find the first element in array such that all of its left elements
 are smaller and all right elements to it are greater than it.
Input:
3
4
4 2 5 7
3
11 9 12
6
4 3 2 7 8 9

Output:
5
-1
7
'''

import sys

if __name__ == '__main__':
    test_cases = int(input())

    list_counts, lists = [], []
    for i in range(test_cases):
        list_counts.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        temp_list = [0] * list_counts[i]
        temp_list[0] = -sys.maxsize
        for j in range(1, list_counts[i]):
            temp_list[j] = max(temp_list[j - 1], lists[i][j - 1])

        print(temp_list)
        print(sys.maxsize)
        # Getting last number in array
        right_min = sys.maxsize
        is_ele_found = False

        for j in range(list_counts[i] - 1, -1, -1):

            if lists[i][j] > temp_list[j] and lists[i][j] < right_min:
                print(lists[i][j])
                is_ele_found = True
                break

            right_min = min(right_min, lists[i][j])

        if not is_ele_found:
            print('-1')


