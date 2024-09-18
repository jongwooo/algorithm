import sys
from collections import deque


def topology_sort():
    queue = deque([])
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + times[i])
            if indegree[i] == 0:
                queue.append(i)


n = int(sys.stdin.readline())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
times = [0] * (n + 1)
for i in range(1, n + 1):
    t, cnt, *jobs = map(int, sys.stdin.readline().split())
    times[i] = t
    if cnt != 0:
        for j in jobs:
            graph[j].append(i)
            indegree[i] += 1
topology_sort()
print(max(dp))
