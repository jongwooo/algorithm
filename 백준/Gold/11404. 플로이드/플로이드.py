import sys

INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == INF else graph[i][j], end=' ')
    print()
