'''
Problem statement: Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where
    the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
'''

if __name__ == '__main__':
    test_cases = int(input())

    lists_length = []
    lists = []
    for i in range(test_cases):
        lists_length.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        left_max_list, right_max_list = [], [0] * lists_length[i]
        # Calculating left max list
        left_max_list.append(lists[i][0])
        for j in range(1, lists_length[i]):
            left_max_list.insert(j, max(lists[i][j], left_max_list[j - 1]))

        # Calculating right max list
        right_max_list[lists_length[i] - 1] = lists[i][lists_length[i] - 1]
        for j in range(lists_length[i] - 2, -1, -1):
            right_max_list[j] = max(lists[i][j], right_max_list[j + 1])

        water_length = 0
        for j in range(lists_length[i]):
            water_length += min(left_max_list[j], right_max_list[j]) - lists[i][j]

        print(water_length)
