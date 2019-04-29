'''
Problem statement: Given an input stream of n integers, find the kth largest element for each element in the stream.
'''

import heapq

if __name__ == '__main__':
    test_cases = int(input())

    list_count, lists = [], []
    for i in range(test_cases):
        list_count.append(list(map(int, input().split())))
        lists.append(list(map(int, input().split())))

    for i in range(test_cases):
        min_heap = []
        for j in range(list_count[i][1]):
            heapq.heappush(min_heap, lists[i][j])

            if len(min_heap) > list_count[i][0]:
                heapq.heappop(min_heap)

            if len(min_heap) == list_count[i][0]:
                print(min_heap[0], end = " ")
            else:
                print(-1, end = " ")

        print()
