import sys
import heapq


def dijkstra(start):
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


INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)
for i in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
dijkstra(k)
for d in distance[1:]:
    print('INF' if d == INF else d)
