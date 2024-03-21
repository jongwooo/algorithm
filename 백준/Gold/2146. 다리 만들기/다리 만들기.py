import sys
from collections import deque


def divide_islands(i, j, island_num):
    queue = deque([(i, j)])
    visited[i][j] = True
    graph[i][j] = island_num
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = island_num


def bfs(island_num):
    global min_dist
    dist = [[-1] * n for _ in range(n)]
    queue = deque([])
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island_num:
                queue.append((i, j))
                dist[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > 0 and graph[nx][ny] != island_num:
                    min_dist = min(min_dist, dist[x][y])
                    return
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    queue.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dirs = ((-1, 0), (1, 0), (0, 1),  (0, -1))
cnt = 1
min_dist = sys.maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            divide_islands(i, j, cnt)
            cnt += 1
for i in range(1, cnt):
    bfs(i)
print(min_dist)
