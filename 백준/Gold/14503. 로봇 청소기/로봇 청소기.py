import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    global d
    queue = deque([(r, c)])
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        clean = 0
        for _ in range(4):
            d = (d - 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if in_range(nx, ny) and not visited[nx][ny] and room[nx][ny] == NOT_CLEAND:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
                clean = 1
                break
        if not clean:
            nx = x - dx[d]
            ny = y - dy[d]
            if room[nx][ny] == WALL:
                print(cnt)
                break
            else:
                queue.append((nx, ny))


NOT_CLEAND = 0
WALL = 1
dx = (-1, 0, 1, 0)
dy = (0, 1, 0 , -1)
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bfs()
