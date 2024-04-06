import sys
from collections import deque


def monitoring():
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                queue.append((i, j, grid[i][j]))


def spread():
    while queue:
        x, y, dust = queue.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and (nx, ny) not in air_cleaner:
                grid[nx][ny] += dust // 5
                cnt += 1
        grid[x][y] -= (dust // 5) * cnt


def clean():
    global grid
    x, y = air_cleaner[0]
    y += 1
    d = 1
    temp = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d - 1) % 4
            continue
        if (x, y) == air_cleaner[0]:
            break
        grid[x][y], temp = temp, grid[x][y]
        x, y = nx, ny
    x, y = air_cleaner[1]
    y += 1
    d = 1
    temp = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == R or ny == C or nx == -1 or ny == -1:
            d = (d + 1) % 4
            continue
        if (x, y) == air_cleaner[1]:
            break
        grid[x][y], temp = temp, grid[x][y]
        x, y = nx, ny


R, C, T = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
air_cleaner = []
for i in range(R - 1):
    if grid[i][0] == grid[i + 1][0] == -1:
        air_cleaner.append((i, 0))
        air_cleaner.append((i + 1, 0))
        break
queue = deque([])
for _ in range(T):
    monitoring()
    spread()
    clean()
monitoring()
print(sum(queue[i][2] for i in range(len(queue))))
