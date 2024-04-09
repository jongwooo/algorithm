import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    d = [0] + list(map(int, sys.stdin.readline().split()))
    matrix = [[] for _ in range(n + 1)]
    parents = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x].append(y)
        parents[y] += 1
    w = int(sys.stdin.readline())
    queue = deque([])
    for i in range(1, len(parents)):
        if parents[i] == 0:
            queue.append(i)
            parents[i] = -1
    init_level = 0
    time_consumed = [0] * (len(parents) + 1)
    for v in queue:
        time_consumed[v] = d[v]
    while queue:
        building = queue.popleft()
        if building == w:
            break
        for next in matrix[building]:
            time_consumed[next] = max(time_consumed[next], time_consumed[building] + d[next])
            parents[next] -= 1
        for i in range(1, len(parents)):
            if parents[i] == 0:
                queue.append(i)
                parents[i] = -1
    print(time_consumed[w])
