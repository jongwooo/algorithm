import sys
from collections import deque


def str_to_digit():
    return lambda x: x if x == '.' or x == '#' else int(x)


def init_castles():
    global castles
    for i in range(n):
        for j in range(m):
            if board[i][j] != '.' and board[i][j] != '#':
                castle_cnt[board[i][j]] += 1
                castles[board[i][j]].append((i, j))


def bfs():
    global board
    is_expanded = True
    while is_expanded:
        is_expanded = False
        for pid in range(1, p + 1):
            if not castles[pid]:
                continue
            queue = castles[pid]
            for _ in range(s[pid]):
                if not queue:
                    break
                for _ in range(len(queue)):
                    x, y = castles[pid].popleft()
                    for dx, dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '.':
                            castles[pid].append((nx, ny))
                            board[nx][ny] = pid
                            castle_cnt[pid] += 1
                            is_expanded = True


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m, p = map(int, sys.stdin.readline().split())
s = [0] + list(map(int, sys.stdin.readline().split()))
board = [list(map(str_to_digit(), sys.stdin.readline().rstrip())) for _ in range(n)]
castles = [deque() for _ in range(p + 1)]
castle_cnt = [0] * (p + 1)
init_castles()
bfs()
print(*castle_cnt[1:])
