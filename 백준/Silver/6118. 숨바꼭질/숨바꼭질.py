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
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    a_i, b_i = map(int, sys.stdin.readline().split())
    graph[a_i].append((b_i, 1))
    graph[b_i].append((a_i, 1))
dijkstra(1)
max_dist = 0
for d in distance:
    if d == INF:
        continue
    max_dist = max(max_dist, d)
print(distance.index(max_dist), max_dist, distance.count(max_dist))
