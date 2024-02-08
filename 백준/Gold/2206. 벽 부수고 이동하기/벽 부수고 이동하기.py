import sys
from collections import deque


def bfs():
    queue = deque([])
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        y, x, w = queue.popleft()
        if x == m - 1 and y == n - 1:
            return visited[y][x][w]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 0 and visited[ny][nx][w] == 0:
                    queue.append((ny, nx, w))
                    visited[ny][nx][w] = visited[y][x][w] + 1
                elif graph[ny][nx] == 1 and w == 0:
                    queue.append((ny, nx, w + 1))
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
    return -1


n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(sys.stdin.readline().rstrip()))))
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
print(bfs())
