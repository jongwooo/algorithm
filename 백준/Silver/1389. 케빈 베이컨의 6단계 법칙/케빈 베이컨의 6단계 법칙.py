import sys

INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
min_kevin_bacon = INF
idx = 0
for i in range(1, n + 1):
    if min_kevin_bacon > sum(graph[i][1:]):
        min_kevin_bacon = sum(graph[i][1:])
        idx = i
print(idx)
