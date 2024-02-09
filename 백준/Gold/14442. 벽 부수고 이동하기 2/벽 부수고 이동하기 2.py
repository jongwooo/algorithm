import sys
from collections import deque


def bfs():
    queue.append((0, 0, k))
    visited[0][0][k] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and z > 0 and visited[nx][ny][z - 1] == 0:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z - 1))
                elif arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1


n, m, k = map(int, sys.stdin.readline().split())
queue = deque([])
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
print(bfs())
