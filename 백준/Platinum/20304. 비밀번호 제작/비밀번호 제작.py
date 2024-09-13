import sys
from collections import deque


def bfs():
    global max_safety
    safety = [21 for _ in range(n + 1)]
    queue = deque([])
    for i in p:
        safety[i] = 0
        queue.append(i)
    while queue:
        cur = queue.popleft()
        for i in range(20):
            x = (1 << i) ^ cur
            if x <= n and safety[cur] + 1 < safety[x]:
                queue.append(x)
                safety[x] = safety[cur] + 1
                if max_safety < safety[x]:
                    max_safety = safety[x]


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
max_safety = 0
bfs()
print(max_safety)
