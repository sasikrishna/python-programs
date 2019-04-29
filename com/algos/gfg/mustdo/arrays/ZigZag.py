'''
Problem statement: Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e
you have to iterate on the original array only.
'''


def swap(num_list, index1, index2):
    temp = num_list[index1]
    num_list[index1] = num_list[index2]
    num_list[index2] = temp


if __name__ == '__main__':
    test_cases = int(input())

    list_count, lists = [], []
    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):

        zig_zag = True
        for j in range(1, list_count[i]):
            if zig_zag:
                if not lists[i][j] > lists[i][j - 1]:
                    swap(lists[i], j, j - 1)
                zig_zag = False
            else:
                if not lists[i][j] < lists[i][j - 1]:
                    swap(lists[i], j, j - 1)
                zig_zag = True

        for j in range(list_count[i]):
            print(lists[i][j], end=" ")

        print()
