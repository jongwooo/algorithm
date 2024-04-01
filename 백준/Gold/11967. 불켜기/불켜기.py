import sys
from collections import deque


def bfs():
    dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    queue = deque([(1, 1)])
    visited[1][1] = True
    cnt = 1
    for a, b in switches[1][1]:
        if bulbs[a][b] == -1:
            bulbs[a][b] = 1
            cnt += 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 < nx <= N and 0 < ny <= N and bulbs[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                for a, b in switches[nx][ny]:
                    if bulbs[a][b] == -1:
                        bulbs[a][b] = 1
                        cnt += 1
                    for dx, dy in dirs:
                        na = a + dx
                        nb = b + dy
                        if 0 < na <= N and 0 < nb <= N and bulbs[na][nb] == 1 and visited[na][nb]:
                            queue.append((na, nb))
    return cnt


N, M = map(int, sys.stdin.readline().split())
bulbs = [[-1] * (N + 1) for _ in range(N + 1)]
bulbs[1][1] = 1
switches = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
visited = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().split())
    switches[x][y].append((a, b))
print(bfs())
