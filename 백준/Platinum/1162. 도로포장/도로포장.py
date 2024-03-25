import sys
import heapq


def dijkstra(start, pave):
    queue = []
    heapq.heappush(queue, (0, start, pave))
    while queue:
        dist, now, pave = heapq.heappop(queue)
        if distance[now][pave] < dist:
            continue
        if pave + 1 <= k:
            for next, next_dist in graph[now]:
                if distance[next][pave + 1] > dist:
                    distance[next][pave + 1] = dist
                    heapq.heappush(queue, (dist, next, pave + 1))
        for next, next_dist in graph[now]:
            new_dist = dist + next_dist
            if distance[next][pave] > new_dist:
                distance[next][pave] = new_dist
                heapq.heappush(queue, (new_dist, next, pave))


INF = 987_654_321_987_654_321_000
n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [[INF] * (k + 1) for _ in range(n + 1)]
for i in range(k):
    distance[1][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1, 0)
result = INF
for i in range(k + 1):
    result = min(result, distance[n][i])
print(result)
