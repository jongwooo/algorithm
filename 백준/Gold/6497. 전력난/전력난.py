import sys


def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m + 1)]
    edges = []
    costs = 0
    result = 0
    for _ in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        costs += z
        edges.append((z, x, y))
    edges.sort()
    for edge in edges:
        z, x, y = edge
        if find(x) != find(y):
            union(x, y)
            result += z
    print(costs - result)
