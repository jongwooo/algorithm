import sys
from collections import deque


def turn(c):
    global d
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4


def game(head_x, head_y):
    time = 0
    snake = deque([(head_x, head_y)])
    board[head_x][head_y] = -1
    while True:
        time += 1
        head_x += dx[d]
        head_y += dy[d]
        if head_x < 0 or N <= head_x or head_y < 0 or N <= head_y:
            break
        else:
            if board[head_x][head_y] == 1:
                board[head_x][head_y] = -1
                snake.append((head_x, head_y))
            elif board[head_x][head_y] == 0:
                board[head_x][head_y] = -1
                snake.append((head_x, head_y))
                tail_x, tail_y = snake.popleft()
                board[tail_x][tail_y] = 0
            else:
                break
            if time in snake_dirs:
                turn(snake_dirs[time])
    return time


N = int(sys.stdin.readline())
board = [[0] * N for _ in range(N)]
K = int(sys.stdin.readline())
apples = []
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 1
    apples.append((r - 1, c - 1))
L = int(sys.stdin.readline())
snake_dirs = dict()
for _ in range(L):
    X, C = sys.stdin.readline().rstrip().split()
    snake_dirs[int(X)] = C
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
d = 1
print(game(0, 0))
