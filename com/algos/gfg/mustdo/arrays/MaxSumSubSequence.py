# code
import time

start = time.time()

if __name__ == '__main__':
    test_cases = int(input())

    list_count = []
    lists = []
    for i in range(test_cases):
        list_count.append(int(input()))
        lists.append(list(map(int, input().split())))

    # print('End time', time.time() - start)

    for i in range(test_cases):
        sum = [0] * list_count[i]
        sum[0] = lists[i][0]
        max_sum = sum[0]
        for j in range(1, list_count[i]):
            sum[j] = lists[i][j]
            for k in range(0, j):
                if lists[i][j] > lists[i][k] and sum[j] < sum[k] + lists[i][j]:
                    sum[j] = sum[k] + lists[i][j]

            max_sum = max(max_sum, sum[j])
        print(max_sum)
