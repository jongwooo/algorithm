import sys
from collections import deque


def rotate(size):
    global grid
    temp = [[0] * grid_size for _ in range(grid_size)]
    for x in range(0, grid_size, size):
        for y in range(0, grid_size, size):
            for i in range(size):
                for j in range(size):
                    temp[x + j][y + size - i - 1] = grid[x + i][y + j]
    grid = temp


def melt():
    melt_candidates = []
    for x in range(grid_size):
        for y in range(grid_size):
            cnt = 0
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx][ny] > 0:
                    cnt += 1
            if cnt < 3 and grid[x][y] != 0:
                melt_candidates.append((x, y))
    for x, y in melt_candidates:
        grid[x][y] -= 1


def bfs():
    global ice_sum, max_area_cnt
    visited = [[False] * grid_size for _ in range(grid_size)]
    for i in range(grid_size):
        for j in range(grid_size):
            area_cnt = 0
            if visited[i][j] or grid[i][j] == 0:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                ice_sum += grid[x][y]
                area_cnt += 1
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < grid_size and 0 <= ny < grid_size and not visited[nx][ny] and grid[nx][ny] != 0:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
            max_area_cnt = max(max_area_cnt, area_cnt)


dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
N, Q = map(int, sys.stdin.readline().split())
grid_size = 2 ** N
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(grid_size)]
L = list(map(int, sys.stdin.readline().split()))
for x in L:
    rotate(2 ** x)
    melt()
ice_sum = 0
max_area_cnt = 0
bfs()
print(ice_sum)
print(max_area_cnt)
