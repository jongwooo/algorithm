computer = int(input())
edge = int(input())
graph = [[] for _ in range(computer + 1)]
for i in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [False] * (computer + 1)


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)
print(visited[2:].count(True))
