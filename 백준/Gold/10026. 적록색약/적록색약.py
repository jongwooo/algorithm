import sys
from collections import deque


def bfs(y, x, color):
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and graph[ny][nx] == color:
                queue.append((ny, nx))
                visited[ny][nx] = True


n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
normal = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            color = graph[y][x]
            bfs(y, x, color)
            normal += 1
visited = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if graph[y][x] == 'G':
            graph[y][x] = 'R'
color_weakness = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            color = graph[y][x]
            bfs(y, x, color)
            color_weakness += 1
print(normal)
print(color_weakness)
