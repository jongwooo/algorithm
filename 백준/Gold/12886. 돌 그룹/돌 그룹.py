import sys
from collections import deque


def bfs():
    queue = deque([(a, b)])
    visited = [[False] * (total + 1) for _ in range(total + 1)]
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        z = total - x - y
        if x == y == z:
            return 1
        for i, j in (x, y), (y, z), (z, x):
            if i < j:
                j -= i
                i += i
            elif i > j:
                i -= j
                j += j
            else:
                continue
            k = total - i - j
            x = min(i, j, k)
            y = max(i, j, k)
            if not visited[x][y]:
                queue.append((x, y))
                visited[x][y] = True
    return 0


a, b, c = map(int, sys.stdin.readline().split())
total = a + b + c
print(0 if total % 3 != 0 else bfs())
