import sys


def check_row(a, n):
    for i in range(9):
        if n == sudoku[a][i]:
            return False
    return True


def check_col(a, n):
    for i in range(9):
        if n == sudoku[i][a]:
            return False
    return True


def check_3x3_square(y, x, n):
    for r in range(3):
        for c in range(3):
            if n == sudoku[y - y % 3 + r][x - x % 3 + c]:
                return False
    return True


def solve_sudoku(n):
    if n == len(fill):
        for s in sudoku:
            print(*s)
        exit()
    for i in range(1, 10):
        y, x = fill[n]
        if check_row(y, i) and check_col(x, i) and check_3x3_square(y, x, i):
            sudoku[y][x] = i
            solve_sudoku(n + 1)
            sudoku[y][x] = 0


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
fill = []
for y in range(9):
    for x in range(9):
        if sudoku[y][x] == 0:
            fill.append((y, x))
solve_sudoku(0)
