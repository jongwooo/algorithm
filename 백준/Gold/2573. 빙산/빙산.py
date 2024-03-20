import sys
from collections import deque


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = True
    seas = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        if sea > 0:
            seas.append((x, y, sea))
    for x, y, sea in seas:
        graph[x][y] = max(0, graph[x][y] - sea)


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
iceberg = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            iceberg.append((i, j))
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
group = 0
year = 0
while iceberg:
    visited = [[False] * m for _ in range(n)]
    melted = []
    group = 0
    for i, j in iceberg:
        if graph[i][j] and not visited[i][j]:
            bfs(i, j)
            group += 1
        if graph[i][j] == 0:
            melted.append((i, j))
    if group > 1:
        print(year)
        break
    iceberg = list(set(iceberg) - set(melted))
    year += 1
if group < 2:
    print(0)
