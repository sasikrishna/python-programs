

def bubble_sort(array):

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp

    return array


if __name__ == '__main__':
    array = bubble_sort([15, 7, 8, 3])
    print(array)
