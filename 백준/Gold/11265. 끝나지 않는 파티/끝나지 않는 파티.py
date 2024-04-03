import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, n + 1):
        graph[i][j] = temp[j - 1]
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    print('Enjoy other party' if graph[a][b] <= c else 'Stay here')
