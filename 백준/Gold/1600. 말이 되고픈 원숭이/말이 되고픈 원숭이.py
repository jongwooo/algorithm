import sys
from collections import deque


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 0
    while queue:
        x, y, z = queue.popleft()
        if (x, y) == (h - 1, w - 1):
            return visited[x][y][z]
        for dx, dy in monkey_dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 1 and visited[nx][ny][z] == -1:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
        if z < k:
            for dx, dy in horse_dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != 1 and visited[nx][ny][z + 1] == -1:
                    queue.append((nx, ny, z + 1))
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
    return -1


k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
horse_dirs = ((-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1))
monkey_dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
print(bfs())
