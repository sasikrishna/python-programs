
'''
    Problem: Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
        Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
    Input:
    2
    1
    1
    5
    1 3 5 2 2

    Output:
    1
    3
'''

if __name__ == '__main__':
    test_cases = int(input())

    list_count = []
    lists = []
    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        total_sum = sum(lists[i])

        lhs_sum = 0
        equilibrium_found = False
        for j, num in enumerate(lists[i]):

            total_sum -= num
            if total_sum == lhs_sum:
                print(j+1)
                equilibrium_found = True
                break

            lhs_sum += num

        if not equilibrium_found:
            print(-1)
