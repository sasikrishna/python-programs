'''
    Problem: Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
    Input:
    2
    5 12
    1 2 3 7 5
    10 15
    1 2 3 4 5 6 7 8 9 10
    Output:
    2 4
    1 5
'''


if __name__ == '__main__':
    test_cases = input()

    numbers_count = []
    sum = []
    numbers = []
    for i in range(int(test_cases)):
        temp = input()
        numbers_count.append(int(temp.split()[0]))
        sum.append(int(temp.split()[1]))
        numbers.append(input().split())

    for i in range(int(test_cases)):
        num_list = list(map(int, numbers[i]))

        start, curr_sum, end = 0, 0, 0
        for j in range(len(num_list) + 1):

            while curr_sum > sum[i]:
                curr_sum -= num_list[start]
                start += 1

            if curr_sum == sum[i]:
                end = j - 1
                break

            if j < len(num_list):
                curr_sum += num_list[j]

        if end:
            print(start + 1, end + 1)
        else:
            print(-1)
