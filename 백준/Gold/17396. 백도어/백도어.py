import heapq
import sys

INF = int(1e15)


def dijkstra():
    distances = [INF] * N
    distances[0] = 0
    queue = []
    heapq.heappush(queue, (0, 0))
    while queue:
        dist, now = heapq.heappop(queue)
        if distances[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            if next_node != N - 1 and A[next_node] == 1:
                continue
            new_dist = dist + next_dist
            if new_dist < distances[next_node]:
                heapq.heappush(queue, (new_dist, next_node))
                distances[next_node] = new_dist
    return distances[N - 1]

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
result = dijkstra()
print(-1 if result == INF else result)
