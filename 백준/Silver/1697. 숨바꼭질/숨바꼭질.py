import sys
from collections import deque


MAX_N = 100_001


def bfs(n):
    visited = [0] * MAX_N
    queue = deque([(n, 0)])
    while queue:
        x, cnt = queue.popleft()
        if x == k:
            return cnt
        for f in func:
            next_n = f(x)
            if 0 <= next_n <= 100_000 and not visited[next_n]:
                queue.append((next_n, cnt + 1))
                visited[next_n] = 1


func = (
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: 2 * x
)
n, k = map(int, sys.stdin.readline().split())
print(bfs(n))
