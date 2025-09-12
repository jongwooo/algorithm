import sys
from collections import deque


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs(r, c):
    global visited
    queue = deque([(r, c)])
    visited[r][c] = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) and not visited[nr][nc] and field[nr][nc] == CABBAGE:
                queue.append((nr, nc))
                visited[nr][nc] = 1


EMPTY = 0
CABBAGE = 1
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[EMPTY] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = CABBAGE
    cnt = 0
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == CABBAGE and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
