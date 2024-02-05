import sys
from collections import deque


def bfs(y, x):
    global max_size
    queue = deque([])
    queue.append((y, x))
    visited[y][x] = 1
    size = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == -1:
                queue.append((ny, nx))
                visited[ny][nx] = 1
                size += 1
    max_size = max(max_size, size)


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            visited[y][x] = 0
cnt = 0
max_size = 0
for y in range(n):
    for x in range(m):
        if visited[y][x] == -1:
            cnt += 1
            bfs(y, x)
print(cnt)
print(max_size)
