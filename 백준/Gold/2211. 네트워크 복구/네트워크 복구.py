import heapq
import sys


def dijkstra(start):
    global prev_node
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next, next_dist in graph[now]:
            new_dist = dist + next_dist
            if new_dist < distance[next]:
                distance[next] = new_dist
                prev_node[next] = now
                heapq.heappush(queue, (new_dist, next))


INF = int(1e9)
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra(1)
print(n - 1)
for i in range(2, n + 1):
    print(i, prev_node[i])
