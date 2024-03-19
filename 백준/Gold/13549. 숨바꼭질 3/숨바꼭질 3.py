import sys
from collections import deque


def bfs():
    queue = deque([])
    if n == 0:
        queue.append(1)
    else:
        queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return time[x]
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < 100_001 and time[nx] == 0:
                if nx == 2 * x:
                    queue.appendleft(nx)
                    time[nx] = time[x]
                else:
                    queue.append(nx)
                    time[nx] = time[x] + 1


n, k = map(int, sys.stdin.readline().split())
time = [0] * 100_001
if n == 0:
    print(bfs() + 1)
else:
    print(bfs())
