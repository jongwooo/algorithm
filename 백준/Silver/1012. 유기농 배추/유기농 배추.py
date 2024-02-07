import sys
from collections import deque


def bfs(y, x):
    queue = deque([])
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and field[ny][nx] == 1:
                queue.append((ny, nx))
                field[ny][nx] = -1


t = int(sys.stdin.readline())
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    cnt = 0
    for y in range(n + 1):
        for x in range(m + 1):
            if field[y][x] == 1:
                bfs(y, x)
                cnt += 1
    print(cnt)
