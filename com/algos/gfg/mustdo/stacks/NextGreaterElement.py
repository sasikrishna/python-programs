'''
Problem statement: Given an array A of size N having distinct elements, the task is to find the next greater element for
each element of the array in order of their appearance in the array. If no such element exists, output -1
'''

if __name__ == '__main__':
    test_cases = int(input())
    list_counts, lists = [], []

    for i in range(test_cases):
        list_counts.append(int(input()))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        list, stack = lists[i], []
        stack.append(list[0])
        for j in range(1, list_counts[i]):
            next = list[j]
            while len(stack) > 0 and next > stack[len(stack) - 1]:
                print('NGE for ', stack.pop(), next)

            stack.append(next)

        while len(stack) != 0:
            print('NGE for ', stack.pop(), -1)



