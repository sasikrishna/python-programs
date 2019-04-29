'''
Problem statement: Given a sorted array A, size N, of integers; every element appears twice except for one. Find that
element in linear time complexity and without using extra memory.
'''

if __name__ == '__main__':
    test_cases = int(input())

    list_count, lists = [], []
    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        low, high = 0, list_count[i] - 1
        while low < high:
            mid = int((low + high) / 2)

            if mid % 2 == 0:
                if lists[i][mid] == lists[i][mid + 1]:
                    low = mid + 1
                else:
                    high = mid
            else:
                if lists[i][mid] == lists[i][mid - 1]:
                    low = mid + 1
                else:
                    high = mid

        if low == high:
            print(lists[i][low])



