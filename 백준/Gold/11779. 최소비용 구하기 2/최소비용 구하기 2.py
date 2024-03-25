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
        for next, next_dist in graph[now]:
            new_dist = dist + next_dist
            if distance[next] > new_dist:
                distance[next] = new_dist
                prev_node[next] = now
                heapq.heappush(queue, (new_dist, next))


INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
prev_node = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])
path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)
path.reverse()
print(len(path))
print(*path)
