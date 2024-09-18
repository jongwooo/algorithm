import sys
from collections import deque


def bfs():
    queue = deque([(r1, c1, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[r1][c1] = True
    while queue:
        r, c, cnt = queue.popleft()
        if (r, c) == (r2, c2):
            return cnt
        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
    return -1


n = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
dirs = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
print(bfs())
