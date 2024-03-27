import copy
import sys


def left(board):
    board = copy.deepcopy(board)
    for i in range(N):
        cursor = 0
        for j in range(1, N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][cursor] == 0:
                    board[i][cursor] = temp
                elif board[i][cursor] == temp:
                    board[i][cursor] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[i][cursor] = temp
    return board


def right(board):
    board = copy.deepcopy(board)
    for i in range(N):
        cursor = N - 1
        for j in range(N - 1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if board[i][cursor] == 0:
                    board[i][cursor] = temp
                elif board[i][cursor] == temp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = temp
    return board


def up(board):
    board = copy.deepcopy(board)
    for j in range(N):
        cursor = 0
        for i in range(N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if board[cursor][j] == 0:
                    board[cursor][j] = temp
                elif board[cursor][j] == temp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = temp
    return board


def down(board):
    board = copy.deepcopy(board)
    for j in range(N):
        cursor = N - 1
        for i in range(N - 1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0
                if board[cursor][j] == 0:
                    board[cursor][j] = temp
                elif board[cursor][j] == temp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = temp
    return board


def dfs(n, board):
    global max_num
    if n == 5:
        for b in board:
            max_num = max(max_num, max(b))
    else:
        dfs(n + 1, left(board))
        dfs(n + 1, right(board))
        dfs(n + 1, up(board))
        dfs(n + 1, down(board))


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_num = 0
dfs(0, board)
print(max_num)
