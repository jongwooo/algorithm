import sys
from collections import deque

func = (
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: 2 * x
)
n, k = map(int, sys.stdin.readline().split())
visited = [False] * 100_001
queue = deque([])
queue.append((n, 0))
while queue:
    n, cnt = queue.popleft()
    if n == k:
        print(cnt)
        break
    for f in func:
        next_n = f(n)
        if 0 <= next_n <= 100_000 and not visited[next_n]:
            queue.append((next_n, cnt + 1))
            visited[next_n] = True
