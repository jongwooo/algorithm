import sys

sys.setrecursionlimit(100_000)


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v + 1)]
edges = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])
result = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)
