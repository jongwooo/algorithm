import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
start, end = map(int, sys.stdin.readline().split())
costs = [1e9 for _ in range(n + 1)]
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])
while heap:
    cur_cost, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost
        if sum_cost >= costs[next_v]:
            continue
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
print(costs[end])
