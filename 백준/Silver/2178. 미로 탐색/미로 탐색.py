from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs():
    queue = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[n - 1][m - 1]


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
n, m = map(int, input().split())
grid = [list(map(int, input())) for _ in range(n)]
print(bfs())
