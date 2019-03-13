
def solve_n_queens(array):
    return _solve_n_queens(array, 0)


def _solve_n_queens(array, queen_number):

    if queen_number >= len(array):
        return True

    for column in range(0, len(array)):
        if _is_safe_move(array, queen_number, column):
            array[queen_number][column] = 1
            if _solve_n_queens(array, queen_number + 1):
                return True

            array[queen_number][column] = 0

    return False


def _is_safe_move(array, row, column):

    # Checking in same row if there exists any other queen
    for i in range(0, len(array)):
        if array[row][i] == 1:
            return False

    # Checking in same column if there exists any other queen
    for i in range(0, len(array)):
        if array[i][column] == 1:
            return False

    # Checking upper diagonal left side
    i, j = row, column
    while i >= 0 and j >= 0:
        if array[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Checking lower diagonal left side
    i, j = row, column
    while i < len(array) and j >= 0:
        if array[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Checking upper diagonal right side
    i, j = row, column
    while i < len(array)  and j < len(array):
        if array[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Checking lower diagonal right side
    i, j = row, column
    while i < len(array) and j < len(array):
        if array[i][j] == 1:
            return False
        i += 1
        j += 1

    return True


def print_board(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            print(array[i][j], end=" ")
        print()


if __name__ == '__main__':
    array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]];
    if solve_n_queens(array):
        print_board(array)
    else:
        print("Not possible")

    array = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]];
    if solve_n_queens(array):
        print_board(array)
    else:
        print("Not possible")
