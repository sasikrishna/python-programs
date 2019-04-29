'''
Problem statement: Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that
the relative order among the elements will be same as those in A2. For the elements not present in A2, append them at
last in sorted order. It is also given that the number of elements in A2[] are smaller than or equal to number of
elements in A1[] and A2[] has all distinct elements.
'''

if __name__ == '__main__':
    test_cases = int(input())

    for i in range(test_cases):
        list_count, lists = [], []
        list_count.append(list(map(int, input().split())))
        lists.append(list(map(int, input().split())))
        lists.append(list(map(int, input().split())))

        hash_map = {}
        output_arr = []
        for j in range(list_count[0][0]):
            if hash_map.get(lists[0][j]) is None:
                hash_map[lists[0][j]] = 0
            hash_map[lists[0][j]] += 1

        for j in range(list_count[0][1]):
            if hash_map.get(lists[1][j]) is not None:
                freq = hash_map[lists[1][j]]

                for k in range(freq):
                    output_arr.append(lists[1][j])

                del hash_map[lists[1][j]]

        if len(hash_map) > 0:
            remaining_nums = list(hash_map)
            remaining_nums.sort()

            for k in range(len(remaining_nums)):
                for l in range(hash_map.get(remaining_nums[k])):
                    output_arr.append(remaining_nums[k])

        print(*output_arr)

