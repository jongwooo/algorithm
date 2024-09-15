import sys
import heapq

INF = int(1e9)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    times = [INF] * (n + 1)
    times[start] = 0
    while queue:
        time, now = heapq.heappop(queue)
        if times[now] < time:
            continue
        for next_node, next_time in graph[now]:
            new_time = time + next_time
            if new_time < times[next_node]:
                heapq.heappush(queue, (new_time, next_node))
                times[next_node] = new_time
    return times

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, sys.stdin.readline().split())
    graph[s].append((e, t))
result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])
print(result)
