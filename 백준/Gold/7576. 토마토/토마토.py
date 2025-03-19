import sys
from collections import deque


def in_range(i, j):
    return 0 <= i < n and 0 <= j < m


def bfs():
    global box
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not box[nx][ny]:
                queue.append((nx, ny))
                box[nx][ny] = box[x][y] + 1
    min_days = 0
    for b in box:
        for i in range(m):
            if not b[i]:
                return -1
            if min_days < b[i]:
                min_days = b[i]
    return min_days - 1


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(bfs())
