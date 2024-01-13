from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[end] += [start]


def bfs(start):
    cnt = 1
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt


max_cnt = 1
result = []
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        result.clear()
        result.append(i)
    elif cnt == max_cnt:
        result.append(i)
print(*result)
