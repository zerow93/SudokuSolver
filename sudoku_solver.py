def create_sudoku_arrays(sudoku_sdm):
    sudoku_array = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    for i in range(81):
        sudoku_array[i // 9][(i // 3) % 3][i % 3] = int(sudoku_sdm[i])
    return sudoku_array


def is_possible(sudoku_array, n, x, y):
    # checks if number 'n' is a possible solution in sudoku_array row, col, box.
    for i in range(9):
        row_cell = sudoku_array[x][i//3][i % 3]
        col_cell = sudoku_array[i][y//3][y % 3]
        box_cell = sudoku_array[i//3+x//3*3][y//3][y % 3]
        if n == row_cell or n == col_cell or n == box_cell:
            return False
    return True


def find_next_empty(sudoku_array):
    for x in range(9):
        for y in range(9):
            if sudoku_array[x][y//3][y % 3] == 0:
                return x, y
    return None, None


def solve_sudoku(sudoku_array):
    x, y = find_next_empty(sudoku_array)
    if x is not None:
        for n in range(1, 10):
            if is_possible(sudoku_array, n, x, y):
                sudoku_array[x][y // 3][y % 3] = n
                if solve_sudoku(sudoku_array):
                    return True
                sudoku_array[x][y // 3][y % 3] = 0
    else:
        return True
    return False


def print_solution_sudoku(sudoku_sdm):
    sudoku_array = create_sudoku_arrays(sudoku_sdm)
    if solve_sudoku(sudoku_array):
        print(' '*34+'\033[92m'+'♕♕♕'+'\033[0m'+' '*34)
        print('\033[92m'+'='*30+'SOLVED SUDOKU'+'='*30+'\033[0m')
        for x in range(9):
            print('+-----------------------'*3+'+')
            print('|', end="")
            for y in range(3):
                for i in range(3):
                    print("    ", sudoku_array[x][y][i], end="")
                print("", end="     |")
            print("")
        print('+-----------------------'*3+'+')
        print('\033[92m'+'='*30+'SOLVED SUDOKU'+'='*30+'\033[0m')
    else:
        print("COULDN'T BE SOLVED -> WRONG SUDOKU PARAMETERS")


# sudoku
# 000260701680070090190004500820100040004602900050003028009300074040050036703018000
# 001290075200300800070080006000103062105000403730608000600020030007001004890065107
# 100489006730000040000001295007120600500703008006095700914600000020000037800512004
# 004006079000000602056092300078061030509000406020540890007410920105000000840600100
# 000000680000073009309000045490000000803050902000000036960000308700680000028000000
# HARD 090400000200010000004003800400800500080000020001007003003500400000030070000009002
# HARD 200000100190020083003010500000000000007600050804201300000003200001802030000170049
# EMPTY SUDOKU == 000000000000000000000000000000000000000000000000000000000000000000000000000000000

sudoku_sdm_in = input("type your sudoku problem in .sdm format >")
print_solution_sudoku(sudoku_sdm_in)
