import sys
from collections import deque

EMPTY = '.'
WATER = '*'
TUNNEL = 'D'
HEDGEHOG = 'S'


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def bfs(sx, sy):
    visited[sx][sy] = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dirs:
            nx = cx + dx
            ny = cy + dy
            if in_range(nx, ny):
                if (graph[nx][ny] == EMPTY or graph[nx][ny] == TUNNEL) and graph[cx][cy] == HEDGEHOG:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1
                    graph[nx][ny] = HEDGEHOG
                elif (graph[nx][ny] == EMPTY or graph[nx][ny] == HEDGEHOG) and graph[cx][cy] == WATER:
                    queue.append((nx, ny))
                    graph[nx][ny] = WATER


dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
dr, dc, sr, sc = 0, 0, 0, 0
queue = deque([])
for i in range(r):
    for j in range(c):
        if graph[i][j] == TUNNEL:
            dr, dc = i, j
        if graph[i][j] == HEDGEHOG:
            sr, sc = i, j
            queue.append((i, j))
for i in range(r):
    for j in range(c):
        if graph[i][j] == WATER:
            queue.append((i, j))
bfs(sr, sc)
print((visited[dr][dc] - 1) if visited[dr][dc] else 'KAKTUS')
