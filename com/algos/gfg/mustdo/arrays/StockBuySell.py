
'''
Problem statement: The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy
and sell the stock so that in between those days your profit is maximum.
'''

if __name__ == '__main__':
    test_cases = int(input())

    lists_count = [0] * test_cases
    lists = [0] * test_cases

    for i in range(test_cases):
        lists_count[i] = int(input())
        lists[i] = list(map(int, input().split()))

    for i in range(test_cases):
        intervals = []
        j = 0
        while j < lists_count[i]:
            local_minima_idx, local_maxima_idx = 0, 0

            # Finding local minima. Moving forward in the loop untill we find min price for buying stock
            while (j < lists_count[i] - 1) and (lists[i][j + 1] <= lists[i][j]):
                j += 1

            if j == lists_count[i] - 1:
                break

            local_minima_idx = j
            j += 1

            while (j < lists_count[i]) and (lists[i][j] >= lists[i][j - 1]):
                j += 1

            local_maxima_idx = j - 1

            intervals.append('(' + str(local_minima_idx) + ' ' + str(local_maxima_idx) + ')')

        if len(intervals) > 0:
            for j in range(len(intervals)):
                print(intervals[j], end = '')
            print()
        else:
            print('No Profit')
