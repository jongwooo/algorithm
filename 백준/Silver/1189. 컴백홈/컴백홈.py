import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def dfs(x, y, dist):
    global grid, cnt
    if dist == k and x == 0 and y == c - 1:
        cnt += 1
        return
    grid[x][y] = 'T'
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and grid[nx][ny] != 'T':
            grid[nx][ny] = 'T'
            dfs(nx, ny, dist + 1)
            grid[nx][ny] = '.'


dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
r, c, k = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
cnt = 0
dfs(r - 1, 0, 1)
print(cnt)
