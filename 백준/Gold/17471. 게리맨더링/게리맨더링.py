import sys
from collections import deque

INF = int(1e9)


def int_minus_one():
    return lambda x: int(x) - 1


def is_connected(nodes):
    if not nodes:
        return False
    queue = deque([nodes[0]])
    visited = [False] * n
    visited[nodes[0]] = True
    while queue:
        now = queue.popleft()
        for next_node in graph[now]:
            if next_node in nodes and not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
    return visited.count(True) == len(nodes)


def sum_populations(nodes):
    total = 0
    for node in nodes:
        total += populations[node]
    return total


n = int(sys.stdin.readline())
zones = {i for i in range(n)}
populations = list(map(int, sys.stdin.readline().split()))
graph = [set() for _ in range(n + 1)]
for now in range(n):
    _, *adjacent_zones = map(int_minus_one(), sys.stdin.readline().split())
    for zone in adjacent_zones:
        graph[now].add(zone)
        graph[zone].add(now)
result = INF
for i in range(1 << n):
    a = []
    for j in range(n):
        if i & (1 << j):
            a.append(j)
    b = list(zones.difference(a))
    if is_connected(a) and is_connected(b):
        result = min(result, abs(sum_populations(a) - sum_populations(b)))
print(result if result != INF else -1)
