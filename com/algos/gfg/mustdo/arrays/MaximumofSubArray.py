'''
Problem statement: Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.
Input:
2
9 3
1 2 3 1 4 5 2 3 6
10 4
8 5 10 7 9 4 15 12 90 13

Output:
3 3 4 5 5 5 6
10 10 10 15 15 90 90
'''

if __name__ == '__main__':
    test_cases = int(input())
    lengths = []
    lists = []

    for i in range(test_cases):
        lengths.append(list(map(int, input().split())))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
       for j in range(lengths[i][0]):
            max_number = 0
            loop_completed = False
            for k in range(j, j + lengths[i][1]):
                if k >= lengths[i][0]:
                    loop_completed = True
                    break

                max_number = max(max_number, lists[i][k])

            if loop_completed:
                break

            print(max_number, end = " ")


