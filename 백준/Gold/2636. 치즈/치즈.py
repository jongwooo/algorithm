import sys
from collections import deque


def bfs():
    global grid
    queue = deque([(0, 0)])
    melt = deque([])
    visited = [[0] * c for _ in range(r)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = 1
                if grid[nx][ny] == 0:
                    queue.append((nx, ny))
                else:
                    melt.append((nx, ny))
    for x, y in melt:
        grid[x][y] = 0
    return len(melt)


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
r, c = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
time = 1
cnt = 0
for g in grid:
    cnt += sum(g)
while True:
    melted_cnt = bfs()
    cnt -= melted_cnt
    if cnt == 0:
        print(f'{time}\n{melted_cnt}')
        break
    time += 1
