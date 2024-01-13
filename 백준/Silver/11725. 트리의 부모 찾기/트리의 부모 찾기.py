import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    start, end = map(int, input().split())
    graph[start] += [end]
    graph[end] += [start]
parents = [0] * (n + 1)
parents[1] = 1


def dfs(graph, v, parents):
    for i in graph[v]:
        if parents[i] == 0:
            parents[i] = v
            dfs(graph, i, parents)


dfs(graph, 1, parents)
for parent in parents[2:]:
    print(parent)
