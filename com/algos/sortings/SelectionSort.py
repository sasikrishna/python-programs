
def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if i != min_index:
            temp = array[min_index]
            array[min_index] = array[i]
            array[i] = temp

    return  array


if __name__ == '__main__':
    print(selection_sort([14, 23, 13, 38, 2, 34, 95, 32, 7]))
