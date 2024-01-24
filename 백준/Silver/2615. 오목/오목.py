import sys

input = sys.stdin.readline


def bfs(y, x):
    target = board[y][x]
    for i in range(4):
        cnt = 1
        ny = y + dy[i]
        nx = x + dx[i]
        while 0 <= ny < 19 and 0 <= nx < 19 and board[ny][nx] == target:
            cnt += 1
            if cnt == 5:
                if 0 <= y - dy[i] < 19 and 0 <= x - dx[i] < 19 and board[y - dy[i]][x - dx[i]] == target:
                    break
                if 0 <= ny + dy[i] < 19 and 0 <= nx + dx[i] < 19 and board[ny + dy[i]][nx + dx[i]] == target:
                    break
                print(target)
                print(y + 1, x + 1)
                exit(0)
            ny += dy[i]
            nx += dx[i]


board = [list(map(int, input().split())) for _ in range(19)]
dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1]
for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            bfs(y, x)
print(0)
