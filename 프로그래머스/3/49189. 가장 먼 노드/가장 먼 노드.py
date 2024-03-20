from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        i = queue.popleft()
        for v in graph[i]:
            if not visited[v]:
                queue.append(v)
                visited[v] = visited[i] + 1


def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for f, t in vertex:
        graph[f].append(t)
        graph[t].append(f)
    bfs(graph, 1, visited)
    return visited.count(max(visited))
