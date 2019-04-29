'''
Problem statement: Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that
satisfies a2 + b2 = c2.
Input:
1
5
3 2 4 6 5

Output:
Yes
'''

if __name__ == '__main__':
    test_cases = int(input())

    list_counts = []
    lists = []
    for i in range(test_cases):
        list_counts.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        for j in range(list_counts[i]):
            sub_list = lists[i]

            triplet_found = False
            for k in range(list_counts[i]):
                sub_list[i] = pow(sub_list[i], 2)

            sub_list.sort()
            for k in range(list_counts[i] - 1, 1, -1):

                left, right = 0, k - 1
                while left < right:
                    if sub_list[left] + sub_list[right] == sub_list[k]:
                        print('Yes')
                        triplet_found = True
                        break


                    if sub_list[left] + sub_list[right] < sub_list[k]:
                        left += 1
                    else:
                        right -= 1

                if triplet_found:
                    break

            if triplet_found:
                break

        if not triplet_found:
            print('No')
