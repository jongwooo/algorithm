import sys


def rotate(arr):
    return list(map(list, reversed(list(zip(*arr)))))


def find_bead_loc():
    for y in range(N):
        for x in range(N):
            if board_0[y][x] == 'L':
                board_0[y][x] = '.'
                return y, x


N, K = map(int, sys.stdin.readline().split())
board_0 = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
y, x = find_bead_loc()
board_90 = rotate(board_0)
board_180 = rotate(board_90)
board_270 = rotate(board_180)
boards = (board_0, board_90, board_180, board_270)
fall_points = []
for d in range(4):
    temp = [[-1] * N for _ in range(N)]
    for j in range(N):
        destination = N
        for i in range(N - 1, -1, -1):
            if boards[d][i][j] == 'X':
                destination = i
            else:
                temp[i][j] = destination - 1
    fall_points.append(temp)
d = 0
for _ in range(K):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'L':
        d = (d + 1) % 4
        y, x = N - x - 1, y
    else:
        d = (d - 1) % 4
        y, x = x, N - y - 1
    y, x = fall_points[d][y][x], x
board = boards[d]
board[y][x] = 'L'
for b in board:
    print(''.join(b))
