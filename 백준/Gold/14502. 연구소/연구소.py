import sys
from copy import deepcopy
from collections import deque


def dfs(depth):
    if depth == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
                dfs(depth + 1)
                grid[i][j] = 0


def bfs():
    global max_area
    copied = deepcopy(grid)
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if copied[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and copied[nx][ny] == 0:
                queue.append((nx, ny))
                copied[nx][ny] = 2
    area = 0
    for c in copied:
        area += c.count(0)
    if max_area < area:
        max_area = area


dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_area = 0
dfs(0)
print(max_area)
