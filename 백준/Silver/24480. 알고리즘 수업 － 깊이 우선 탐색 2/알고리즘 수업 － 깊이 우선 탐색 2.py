import sys

sys.setrecursionlimit(10 ** 8)


def dfs(cur):
    global visited, result, cnt
    visited[cur] = 1
    result[cur] = cnt
    graph[cur].sort(reverse=True)
    for next_node in graph[cur]:
        if not visited[next_node]:
            cnt += 1
            dfs(next_node)


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
result = [0] * (n + 1)
cnt = 1
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
dfs(r)
for i in result[1:]:
    print(i)
