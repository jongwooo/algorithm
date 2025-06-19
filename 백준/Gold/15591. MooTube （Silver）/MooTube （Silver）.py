import sys
from collections import deque


def bfs(k, v):
    queue = deque([v])
    visited = [0] * (N + 1)
    visited[v] = 1
    result = 0
    while queue:
        v = queue.popleft()
        for next_v, next_u in usado[v]:
            if not visited[next_v] and k <= next_u:
                queue.append(next_v)
                visited[next_v] = 1
                result += 1
    return result


N, Q = map(int, sys.stdin.readline().split())
usado = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, sys.stdin.readline().split())
    usado[p].append((q, r))
    usado[q].append((p, r))
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(k, v))
