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
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
min_round_trip_time_sum = INF
result = tuple()
for i in range(1, n):
    for j in range(2, n + 1):
        round_trip_time_sum = 0
        for k in range(1, n + 1):
            round_trip_time_sum += min(graph[k][i], graph[k][j]) * 2
        if round_trip_time_sum < min_round_trip_time_sum:
            min_round_trip_time_sum = round_trip_time_sum
            result = (i, j, round_trip_time_sum)
print(*result)
