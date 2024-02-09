import sys
from collections import deque


def bfs():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and 0 <= nz < h and tomatoes[nz][ny][nx] == 0:
                queue.append((nz, ny, nx))
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1


m, n, h = map(int, sys.stdin.readline().split())
tomatoes = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
queue = deque([])
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 1:
                queue.append((z, y, x))
bfs()
unripe = False
day = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if tomatoes[z][y][x] == 0:
                unripe = True
            day = max(day, tomatoes[z][y][x])
print(-1 if unripe else day - 1)
