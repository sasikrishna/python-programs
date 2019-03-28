'''
    Problem: Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
    Input
    2
    5
    1 2 3 -2 5
    4
    -1 -2 -3 -4
    Output
    9
    -1
'''


if __name__ == '__main__':
    test_cases = int(input())
    numbers = []
    num_list = []
    for i in range(test_cases):
        numbers.append(int(input()))
        num_list.append(list(map(int, input().split())))

    for i in range(test_cases):
        max_sum = num_list[i][0]
        curr_sum = num_list[i][0]
        for j in range(1, numbers[i]):
            curr_sum = max(num_list[i][j], curr_sum + num_list[i][j])
            max_sum = max(max_sum, curr_sum)

        print(max_sum)

