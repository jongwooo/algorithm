import sys
from collections import deque


def bfs():
    global min_cnt
    queue = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True
    while queue:
        now, cnt = queue.popleft()
        if now == 100:
            min_cnt = min(min_cnt, cnt)
        for dice in range(1, 7):
            next_node = now + dice
            if 0 < next_node <= 100 and not visited[next_node]:
                if grid[next_node]:
                    visited[next_node] = True
                    next_node = grid[next_node]
                queue.append((next_node, cnt + 1))
                visited[next_node] = True


n, m = map(int, sys.stdin.readline().split())
grid = [0] * 101
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    grid[x] = y
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    grid[u] = v
min_cnt = int(1e9)
bfs()
print(min_cnt)
