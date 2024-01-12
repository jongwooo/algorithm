from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    graph[start] += [end]
    graph[end] += [start]

for g in graph:
    g.sort()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
