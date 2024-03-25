import sys
import heapq


def dijkstra(start):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for destination, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[destination]:
                distance[destination] = new_cost
                heapq.heappush(queue, (new_cost, destination))
    return distance


INF = int(1e9)
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
v1, v2 = map(int, sys.stdin.readline().split())
original_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)
v1_v2 = original_dist[v1] + v1_dist[v2] + v2_dist[n]
v2_v1 = original_dist[v2] + v2_dist[v1] + v1_dist[n]
result = min(v1_v2, v2_v1)
print(result if result < INF else -1)
