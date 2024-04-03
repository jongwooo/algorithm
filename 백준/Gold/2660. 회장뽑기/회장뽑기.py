import sys

INF = int(1e9)
n = int(sys.stdin.readline())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
scores = []
for i in range(1, n + 1):
    scores.append(max(graph[i][1:]))
min_score = min(scores)
print(min_score, scores.count(min_score))
for i, v in enumerate(scores):
    if min_score == v:
        print(i + 1, end=' ')
