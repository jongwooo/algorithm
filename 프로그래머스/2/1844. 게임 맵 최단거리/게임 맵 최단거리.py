from collections import deque


def bfs(maps):
    queue = deque([(0, 0)])
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return visited[x][y]
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 0 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return -1


def solution(maps):
    return bfs(maps)
