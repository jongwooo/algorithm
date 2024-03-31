import sys
from collections import deque


def bfs():
    global safe_distances
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if space[i][j] == 1:
                safe_distances[i][j] = 0
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and safe_distances[nx][ny] == -1:
                queue.append((nx, ny))
                safe_distances[nx][ny] = safe_distances[x][y] + 1


N, M = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
safe_distances = [[-1] * M for _ in range(N)]
bfs()
print(max(map(max, safe_distances)))
