import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    global visited
    queue = deque([(x, y)])
    visited[x][y] = 1
    area = 0
    while queue:
        x, y = queue.popleft()
        area += 1
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    return area


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
area_cnt = 0
max_area = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] and not visited[i][j]:
            area_cnt += 1
            max_area = max(max_area, bfs(i, j))
print(area_cnt)
print(max_area)
