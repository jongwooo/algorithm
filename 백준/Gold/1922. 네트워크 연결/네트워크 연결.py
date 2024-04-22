import sys


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = []
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])
min_cost = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        min_cost += c
print(min_cost)
