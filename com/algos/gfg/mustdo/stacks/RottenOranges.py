'''
Problem statement: Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the
 following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

So, we have to determine what is the minimum time required to all oranges. A rotten orange at index [i,j] can rot other
fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. If it is impossible
to rot every orange then simply return -1.
'''

from collections import deque


def find_min_time(matrix_list, row_columns):

    matrix = [[0 for i in range(row_columns[1])] for j in range(row_columns[0])]
    k = 0
    total_oranges = 0
    dequeue = deque()
    for i in range(row_columns[0]):
        for j in range(row_columns[1]):
            matrix[i][j] = matrix_list[k]

            if matrix_list[k] == 1:
                total_oranges += 1

            if matrix_list[k] == 2:
                dequeue.append(ElePosition(i, j))
                total_oranges += 1

            k += 1

    time_units = 0
    while len(dequeue) > 0:

        unrot_exists = False
        items_per_unit_time = len(dequeue)
        while items_per_unit_time > 0:
            elePosition = dequeue.popleft()
            i, j = elePosition.i, elePosition.j
            if i-1 >= 0 and matrix[i - 1][j] == 1:
                matrix[i-1][j] = 0
                unrot_exists = True
                dequeue.append(ElePosition(i-1, j))

            if i+1 < row_columns[0] and matrix[i + 1][j] == 1:
                matrix[i+1][j]=0
                unrot_exists = True
                dequeue.append(ElePosition(i+1, j))

            if j-1 >= 0 and matrix[i][j-1] == 1:
                matrix[i][j-1]=0
                unrot_exists = True
                dequeue.append(ElePosition(i, j-1))

            if j+1 < row_columns[1] and matrix[i][j + 1] == 1:
                matrix[i][j + 1]=0
                unrot_exists = True
                dequeue.append(ElePosition(i, j + 1))

            total_oranges -=1
            items_per_unit_time -=1

        if unrot_exists is True:
            time_units += 1

    return time_units if total_oranges <= 0 else -1


class ElePosition:
    def __init__(self, i, j):
        self.i = i;
        self.j = j;


if __name__ == '__main__':
    test_cases = int(input())

    for i in range(test_cases):
        row_columns = list(map(int, input().split()))
        matrix_list = list(map(int, input().split()))
        print(find_min_time(matrix_list, row_columns))


