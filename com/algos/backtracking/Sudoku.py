# Sudoku problem solved using backtracking

def solve_sudoku(array):
    is_empty_cell_found = False;

    # Finding if there is any empty cell
    for i in range(0, 9):
        for j in range(0, 9):
            if array[i][j] == 0:
                row, col = i, j
                is_empty_cell_found = True
                break

        if is_empty_cell_found:
            break
    # print('row', row, 'col', col, 'is_empty_cell_found', is_empty_cell_found)
    if not is_empty_cell_found:
        return True

    for num in range(1, 10):
        # print(num)
        if _is_valid_move(array, row, col, num):
            # print('is valid move')
            array[row][col] = num
            if solve_sudoku(array):
                return True
            else:
                array[row][col] = 0

    return False


def _is_valid_move(array, row, col, num):

    # Checking row if same num already exists
    for i in range(0, 9):
        if array[row][i] == num:
            return False

    # Checking column if same num already exists
    for i in range(0, 9):
        if array[i][col] == num:
            return False

    # Checking the current cube
    row_start = row - row % 3
    column_start = col - col % 3
    # print(row_start, column_start)
    for i in range(row_start, row_start + 3):
        for j in range(column_start, column_start + 3):
            if array[i][j] == num:
                # print('matched in grid')
                return False
    return True


def print_array(array):
    for i in range(0, 9):
        for j in range(0, 9):
            print(sudoku_array[i][j], end = " ")
        print()


if __name__ == '__main__':
    sudoku_array = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                    [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1],
                    [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5],
                    [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0],
                    [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    solve_sudoku(sudoku_array)
    print_array(sudoku_array)
